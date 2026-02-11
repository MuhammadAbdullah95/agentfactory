"""ChatKit server for Study Mode - simple pattern from carfixer reference."""

from __future__ import annotations

import logging
import traceback
from collections.abc import AsyncIterator
from datetime import datetime

from agents import Runner, RunResultStreaming
from chatkit.agents import AgentContext, simple_to_agent_input, stream_agent_response
from chatkit.server import ChatKitServer
from chatkit.types import (
    AssistantMessageContent,
    AssistantMessageContentPartTextDelta,
    AssistantMessageItem,
    ThreadItemAddedEvent,
    ThreadItemDoneEvent,
    ThreadItemUpdatedEvent,
    ThreadMetadata,
    ThreadStreamEvent,
    UserMessageItem,
    UserMessageTextContent,
    WidgetItem,
)
from fastapi import HTTPException

from .chatkit_store import CachedPostgresStore, PostgresStore, RequestContext
from .fte import create_agent
from .fte.answer_verification import (
    extract_and_store_correct_answer,
    is_answer_message,
    strip_answer_marker,
    verify_student_answer,
)
from .metering import create_metering_hooks
from .services.content_loader import load_lesson_content

logger = logging.getLogger(__name__)

# Fake ID constant from agents SDK (used by OpenAIChatCompletionsModel)
# When using Chat Completions API, the SDK returns this placeholder ID
# which causes duplicate key errors if not replaced with real IDs
FAKE_RESPONSES_ID = "__fake_id__"

# Agent configuration
MAX_RECENT_ITEMS = 30
TITLE_MAX_WORDS = 6
TITLE_MAX_CHARS = 50

# Trigger patterns that indicate auto-start (AI should speak first)
TRIGGER_PATTERNS = {
    "",  # Empty
    "\u200B",  # Zero-width space (uppercase)
    "\u200b",  # Zero-width space (lowercase - just in case)
    "👋",  # Wave emoji
    "Teach me!",
    "Teach me",
    "__START_TEACHING__",
}

# Characters to strip (including zero-width chars)
INVISIBLE_CHARS = "\u200B\u200b\uFEFF\u00A0\t\n\r "


def _is_trigger_message(text: str) -> bool:
    """Check if message is an auto-start trigger (should be hidden)."""
    # Strip all whitespace including invisible Unicode chars
    clean_text = text.strip(INVISIBLE_CHARS)

    logger.debug(f"[Trigger] raw='{text!r}', clean='{clean_text!r}', len={len(clean_text)}")

    # Empty after stripping = trigger
    if not clean_text:
        return True

    # Check exact matches
    if clean_text in TRIGGER_PATTERNS:
        return True

    # Check if contains trigger pattern (handles "__START_TEACHING__|title|name")
    if "__START_TEACHING__" in clean_text:
        return True

    return False


def _generate_thread_title(user_text: str) -> str:
    """Generate thread title from first few words of user message."""
    # Take first few words
    words = user_text.split()[:TITLE_MAX_WORDS]
    title = " ".join(words)

    # Truncate if too long
    if len(title) > TITLE_MAX_CHARS:
        title = title[:TITLE_MAX_CHARS - 3] + "..."

    # Add ellipsis if we truncated words
    if len(words) < len(user_text.split()):
        if not title.endswith("..."):
            title += "..."

    return title or "New Chat"


def _user_message_text(item: UserMessageItem) -> str:
    """Extract text from user message item."""
    parts: list[str] = []
    for part in item.content:
        if isinstance(part, UserMessageTextContent):
            parts.append(part.text)
    return " ".join(parts).strip()


async def _stream_with_real_ids(
    context: AgentContext,
    result: RunResultStreaming,
    thread_id: str,
    verification_result: str | None = None,
) -> AsyncIterator[ThreadStreamEvent]:
    """
    Wrapper around stream_agent_response that:
    1. Replaces fake IDs with real ones
    2. Strips the <!--CORRECT:X--> marker from responses (including streaming deltas)
    3. Extracts and stores the correct answer for verification
    4. POST-PROCESSES feedback to ensure correct/incorrect matches server verification

    When using OpenAIChatCompletionsModel (for non-OpenAI providers like DeepSeek),
    the SDK returns "__fake_id__" for all message IDs. This causes duplicate key
    errors when saving to the database.

    This wrapper detects fake IDs and replaces them with store-generated IDs.
    """
    # Track ID mapping for this stream: fake_id -> real_id
    id_map: dict[str, str] = {}
    # Collect full response text for answer extraction
    full_response_text = ""
    # Buffer for potential partial marker at end of delta
    # The marker is <!--CORRECT:X--> (max 17 chars)
    marker_buffer = ""
    # Track if we've processed the first text chunk (for feedback correction)
    first_chunk_processed = False
    # Buffer to collect enough text to check feedback
    feedback_buffer = ""

    async for event in stream_agent_response(context, result):
        # Handle ThreadItemAddedEvent - replace fake ID
        if isinstance(event, ThreadItemAddedEvent):
            item = event.item
            if hasattr(item, "id") and item.id == FAKE_RESPONSES_ID:
                # Generate a real ID
                real_id = context.store.generate_item_id(
                    "message", context.thread, context.request_context
                )
                id_map[FAKE_RESPONSES_ID] = real_id
                logger.debug(f"[ChatKit] Replacing fake ID with: {real_id}")

                # Create new item with real ID
                if isinstance(item, AssistantMessageItem):
                    item = AssistantMessageItem(
                        id=real_id,
                        thread_id=item.thread_id,
                        created_at=item.created_at,
                        content=item.content,
                    )
                    event = ThreadItemAddedEvent(item=item)

        # Handle ThreadItemUpdatedEvent - strip markers from streaming deltas
        elif isinstance(event, ThreadItemUpdatedEvent):
            update = event.update
            if isinstance(update, AssistantMessageContentPartTextDelta):
                # Combine buffer with new delta
                combined = marker_buffer + update.delta
                full_response_text += update.delta

                # Strip any complete markers
                cleaned = strip_answer_marker(combined)

                # Check if text ends with potential partial marker
                # The marker starts with '<' and is max 17 chars
                partial_start = -1
                for i in range(min(17, len(cleaned)), 0, -1):
                    suffix = cleaned[-i:]
                    if suffix.startswith("<") and "<!--CORRECT:".startswith(
                        suffix[: len("<!--CORRECT:")]
                    ):
                        partial_start = len(cleaned) - i
                        break

                if partial_start >= 0:
                    # Buffer potential partial marker, emit rest
                    marker_buffer = cleaned[partial_start:]
                    emit_text = cleaned[:partial_start]
                else:
                    # No partial marker, emit all
                    marker_buffer = ""
                    emit_text = cleaned

                # POST-PROCESS FEEDBACK: Ensure correct/incorrect matches verification
                # Buffer first ~50 chars to check if feedback is correct
                if verification_result and not first_chunk_processed:
                    feedback_buffer += emit_text
                    if len(feedback_buffer) >= 50:
                        first_chunk_processed = True
                        # Check if LLM gave wrong feedback
                        lower_buf = feedback_buffer.lower()
                        if verification_result == "correct":
                            # Should say "Correct" but might say "Not quite"
                            if "not quite" in lower_buf or lower_buf.startswith("not"):
                                # WRONG feedback - prepend correct one
                                logger.warning(
                                    "[ChatKit] LLM said 'Not quite' for CORRECT answer - fixing"
                                )
                                emit_text = "Correct! " + feedback_buffer.lstrip()
                                # Remove "Not quite." if present
                                emit_text = emit_text.replace("Not quite.", "")
                                emit_text = emit_text.replace("Not quite", "")
                                emit_text = emit_text.strip()
                                if not emit_text.startswith("Correct"):
                                    emit_text = "Correct! " + emit_text
                            else:
                                emit_text = feedback_buffer  # Use buffered text
                        elif verification_result == "incorrect":
                            # Should say "Not quite" but might say "Correct"
                            if "correct" in lower_buf[:20] and "not" not in lower_buf[:30]:
                                # WRONG feedback - prepend correct one
                                logger.warning(
                                    "[ChatKit] LLM said 'Correct' for INCORRECT answer - fixing"
                                )
                                # Remove "Correct" and prepend "Not quite."
                                emit_text = feedback_buffer
                                words_to_remove = [
                                    "Correct!", "Correct.", "Correct",
                                    "That's right!", "That's right."
                                ]
                                for word in words_to_remove:
                                    emit_text = emit_text.replace(word, "")
                                emit_text = "Not quite. " + emit_text.strip()
                            else:
                                emit_text = feedback_buffer  # Use buffered text
                    else:
                        # Not enough buffered yet, skip this event
                        continue

                # Only yield if there's text to emit
                if emit_text:
                    event = ThreadItemUpdatedEvent(
                        item_id=event.item_id,
                        update=AssistantMessageContentPartTextDelta(
                            content_index=update.content_index,
                            delta=emit_text,
                        ),
                    )
                else:
                    # Skip this event - text is buffered
                    continue

        # Handle ThreadItemDoneEvent - use mapped ID and strip answer marker
        elif isinstance(event, ThreadItemDoneEvent):
            item = event.item
            if isinstance(item, AssistantMessageItem):
                # Collect text and strip only the hidden marker from content
                # Keep the A/B options as plain text (styled via CSS)
                new_content = []
                for content_item in item.content:
                    if hasattr(content_item, "text"):
                        original_text = content_item.text
                        # Only strip the hidden <!--CORRECT:X--> marker
                        cleaned_text = strip_answer_marker(original_text)
                        new_content.append(
                            AssistantMessageContent(
                                text=cleaned_text,
                                annotations=getattr(content_item, "annotations", []),
                            )
                        )
                    else:
                        new_content.append(content_item)

                # Get the real ID
                real_id = item.id
                if item.id == FAKE_RESPONSES_ID:
                    real_id = id_map.get(FAKE_RESPONSES_ID) or context.store.generate_item_id(
                        "message", context.thread, context.request_context
                    )
                    logger.debug(f"[ChatKit] Using real ID for done event: {real_id}")

                # Create new item with cleaned content
                item = AssistantMessageItem(
                    id=real_id,
                    thread_id=item.thread_id,
                    created_at=item.created_at,
                    content=new_content,
                )
                event = ThreadItemDoneEvent(item=item)

                # Extract and store correct answer for verification
                await extract_and_store_correct_answer(thread_id, full_response_text)

        yield event


class StudyModeChatKitServer(ChatKitServer[RequestContext]):
    """
    ChatKit server for Study Mode.

    This server handles read-only operations (items.list, threads.list, etc.)
    automatically via the base ChatKit server, and only uses custom logic
    for agent-triggering operations (threads.create, threads.run).
    """

    def __init__(self, store: CachedPostgresStore | PostgresStore):
        """Initialize the ChatKit server with PostgreSQL store."""
        super().__init__(store)
        logger.info("[ChatKit] StudyModeChatKitServer initialized")

    async def action(
        self,
        thread: ThreadMetadata,
        action: dict,
        sender: WidgetItem | None,
        context: RequestContext,
    ) -> AsyncIterator[ThreadStreamEvent]:
        """
        Handle widget button clicks (A/B option selection).

        When user clicks an option button, this method is called with
        the action payload containing the selected answer.
        """
        action_type = action.get("type", "")
        payload = action.get("payload", {})

        logger.info(f"[ChatKit] Action received: type={action_type}, payload={payload}")

        if action_type == "answer.select":
            answer = payload.get("answer", "")
            if answer in ("A", "B"):
                logger.info(f"[ChatKit] User selected answer: {answer}")

                # Create a user message item for the answer
                user_message = UserMessageItem(
                    id=self.store.generate_item_id("message", thread, context),
                    thread_id=thread.id,
                    created_at=datetime.now(),
                    content=[UserMessageTextContent(text=answer)],
                )

                # Yield the user message event
                yield ThreadItemDoneEvent(item=user_message)

                # Save to store
                await self.store.add_thread_item(thread.id, user_message, context=context)

                # Now call respond to get the AI's reaction
                async for event in self.respond(thread, user_message, context):
                    yield event
            else:
                logger.warning(f"[ChatKit] Invalid answer in action: {answer}")
        else:
            logger.warning(f"[ChatKit] Unknown action type: {action_type}")

    async def respond(
        self,
        thread: ThreadMetadata,
        input_user_message: UserMessageItem | None,
        context: RequestContext,
    ) -> AsyncIterator[ThreadStreamEvent]:
        """
        Generate response for user message using Study Mode agent.

        Args:
            thread: Thread metadata
            input_user_message: User's message (None for retry scenarios)
            context: Request context with user_id

        Yields:
            ThreadStreamEvent: Stream of chat events
        """
        # For read-only operations, base ChatKit server handles them
        if not input_user_message:
            logger.info(
                "[ChatKit] No user message - this is likely a read-only operation"
            )
            return

        try:
            # Extract user message
            user_text = _user_message_text(input_user_message)
            if not user_text:
                logger.warning("[ChatKit] Empty user message")
                return

            # ANSWER VERIFICATION: If user sent "A" or "B", verify against stored answer
            # The verification result is passed to create_agent() to select the right prompt
            verification_result = None
            if is_answer_message(user_text):
                verification_result = await verify_student_answer(thread.id, user_text)
                if verification_result == "correct":
                    logger.info("[ChatKit] Answer verified as CORRECT")
                elif verification_result == "incorrect":
                    logger.info("[ChatKit] Answer verified as INCORRECT")
                else:
                    logger.warning("[ChatKit] Could not verify answer (no stored answer)")
                    verification_result = None  # Ensure it's None for unknown

            # Get metadata from context
            lesson_path = context.metadata.get("lesson_path", "")
            user_name = context.metadata.get("user_name")
            selected_text = context.metadata.get("selected_text")

            # Get mode from ChatKit's composer.models picker (inference_options.model)
            # Default to "teach" if not set
            mode = "teach"
            if (
                input_user_message.inference_options
                and input_user_message.inference_options.model
                and input_user_message.inference_options.model in ("teach", "ask")
            ):
                mode = input_user_message.inference_options.model
            logger.info(f"[ChatKit] Mode: {mode}")

            logger.info(
                f"[ChatKit] Processing: user={context.user_id}, "
                f"lesson={lesson_path}, mode={mode}"
            )

            # Load lesson content
            content_data = await load_lesson_content(lesson_path)
            content = content_data.get("content", "")
            title = content_data.get("title", "Unknown")
            cached = content_data.get("cached", False)

            logger.info(
                f"[ChatKit] Content: title='{title}', "
                f"len={len(content)}, cached={cached}"
            )

            if not content:
                logger.warning(f"[ChatKit] No content for: {lesson_path}")

            # Get previous messages from thread for context
            previous_items = await self.store.load_thread_items(
                thread.id,
                after=None,
                limit=MAX_RECENT_ITEMS,
                order="desc",
                context=context,
            )
            items = list(reversed(previous_items.data))

            # Detect if this is the first message (new thread)
            # Check if there's already an AI response in the thread
            # Note: We can't just count items because trigger messages get deleted
            item_types = [type(item).__name__ for item in items]
            has_assistant_response = any(
                isinstance(item, AssistantMessageItem)
                or getattr(item, "type", "") == "assistant_message"
                for item in items
            )
            is_first_message = not has_assistant_response
            logger.info(
                f"[ChatKit] items={len(items)}, types={item_types}, "
                f"has_assistant={has_assistant_response}, is_first={is_first_message}"
            )

            # Store lesson data in metadata for dynamic instruction functions
            # This allows ask_agent's dynamic callable to access all context
            context.metadata["lesson_title"] = title
            context.metadata["lesson_content"] = content
            context.metadata["is_first_message"] = is_first_message

            # Create agent with appropriate greeting behavior and verification result
            agent = create_agent(
                title,
                content,
                mode,
                user_name=user_name,
                selected_text=selected_text,
                is_first_message=is_first_message,
                verification_result=verification_result,
            )
            logger.info(
                f"[ChatKit] Agent created: is_first={is_first_message}, "
                f"verification={verification_result}"
            )

            # Set thread title from first user message (if new thread)
            if is_first_message and "title" not in context.metadata:
                # If message is a trigger (empty/short), use lesson title instead
                if _is_trigger_message(user_text):
                    context.metadata["title"] = f"📚 {title}"  # Use lesson title
                else:
                    context.metadata["title"] = _generate_thread_title(user_text)
                logger.info(f"[ChatKit] Generated title: {context.metadata['title']}")
                # Save thread again with the generated title (base class saved with default)
                await self.store.save_thread(thread, context)

            # Convert to agent input format
            input_items = await simple_to_agent_input(items)

            # INJECT VERIFICATION: Add explicit verification to last message
            # This ensures LLM sees "[CORRECT]" or "[INCORRECT]" and can't ignore it
            if verification_result and input_items and isinstance(input_items, list):
                logger.info(f"[ChatKit] Injecting verification '{verification_result}' into input")
                # Find the last user message and annotate it
                injected = False
                for i in range(len(input_items) - 1, -1, -1):
                    item = input_items[i]
                    item_type = type(item).__name__
                    has_role = hasattr(item, "role")
                    logger.debug(f"[ChatKit] Item {i}: type={item_type}, has_role={has_role}")
                    if hasattr(item, "role") and item.role == "user":
                        if verification_result == "correct":
                            # Prepend strong verification message
                            original = item.content if hasattr(item, "content") else str(item)
                            item.content = (
                                f"[SERVER VERIFIED: CORRECT ✓]\n"
                                f"Student answer: {original}\n"
                                f"[YOU MUST SAY 'Correct!' - DO NOT SAY 'Not quite']"
                            )
                            logger.info("[ChatKit] Injected CORRECT verification")
                            injected = True
                        elif verification_result == "incorrect":
                            original = item.content if hasattr(item, "content") else str(item)
                            item.content = (
                                f"[SERVER VERIFIED: WRONG ✗]\n"
                                f"Student answer: {original}\n"
                                f"[YOU MUST SAY 'Not quite.' - DO NOT SAY 'Correct']"
                            )
                            logger.info("[ChatKit] Injected INCORRECT verification")
                            injected = True
                        break
                if not injected:
                    logger.warning("[ChatKit] Failed to inject - no user message found")

            # Fallback: if input_items is empty (race condition), use current user message
            if not input_items:
                logger.warning(
                    f"[ChatKit] Empty input_items for thread {thread.id}, "
                    f"using current user message as fallback"
                )
                input_items = user_text  # Agent SDK accepts string input

            # Create agent context
            agent_context = AgentContext(
                thread=thread,
                store=self.store,
                request_context=context,
            )

            # Create metering hooks if metering is enabled
            metering_hooks = create_metering_hooks()

            # Run agent with streaming
            logger.info(f"[ChatKit] Running agent for thread {thread.id}")
            result = Runner.run_streamed(
                agent,
                input_items,
                context=agent_context,
                hooks=metering_hooks,
            )

            # Use wrapper that fixes fake IDs and handles answer verification
            # Wrap in try/except to release metering reservation on error
            try:
                async for event in _stream_with_real_ids(
                    agent_context, result, thread.id, verification_result
                ):
                    yield event
            except HTTPException as http_err:
                # Handle metering 402 specially - show user-friendly message
                if http_err.status_code == 402:
                    detail = http_err.detail if isinstance(http_err.detail, dict) else {}
                    # v5 format: error_code, balance, available_balance, required, is_expired
                    error_code = detail.get("error_code", "INSUFFICIENT_BALANCE")
                    balance = detail.get("balance", 0)
                    available_balance = detail.get("available_balance", 0)
                    required = detail.get("required", 0)
                    is_expired = detail.get("is_expired", False)

                    if is_expired:
                        error_text = (
                            "Your account has been inactive for over"
                            " a year and your credits have expired."
                            " Please contact support to reactivate."
                        )
                    elif error_code == "ACCOUNT_SUSPENDED":
                        error_text = (
                            "Your account has been suspended. "
                            "Please contact support for assistance."
                        )
                    else:
                        # Default: insufficient balance — show USD, not raw credits
                        available_usd = available_balance / 10000
                        required_usd = required / 10000
                        fmt = ".4f" if required_usd < 0.1 else ".2f"
                        avail = f"${available_usd:{fmt}}"
                        needed = f"${required_usd:{fmt}}"
                        error_text = (
                            f"You've used your free credits. "
                            f"Your balance is {avail} but this "
                            f"request needs {needed}. "
                            f"Please top up to continue learning."
                        )

                    logger.warning(
                        f"[ChatKit] Metering blocked: error_code={error_code}, "
                        f"balance={balance}, required={required}, is_expired={is_expired}"
                    )

                    error_message = AssistantMessageItem(
                        id=self.store.generate_item_id("message", thread, context),
                        thread_id=thread.id,
                        created_at=datetime.now(),
                        content=[
                            AssistantMessageContent(text=error_text, annotations=[])
                        ],
                    )
                    yield ThreadItemDoneEvent(item=error_message)
                    return  # Don't re-raise, we handled it gracefully
                else:
                    # Release reservation and re-raise other HTTP errors
                    if metering_hooks:
                        await metering_hooks.release_on_error(agent_context)
                    raise
            except Exception:
                # Release metering reservation on streaming error
                if metering_hooks:
                    await metering_hooks.release_on_error(agent_context)
                raise

            logger.info(f"[ChatKit] Response completed for thread {thread.id}")

            # DELETE TRIGGER MESSAGE: If this was an auto-start trigger,
            # remove it so only the AI greeting shows
            if _is_trigger_message(user_text) and input_user_message:
                try:
                    await self.store.delete_thread_item(
                        thread.id,
                        input_user_message.id,
                        context,
                    )
                    logger.info(
                        f"[ChatKit] Deleted trigger message {input_user_message.id} "
                        f"from thread {thread.id}"
                    )
                except Exception as del_err:
                    logger.warning(f"[ChatKit] Failed to delete trigger: {del_err}")

        except HTTPException:
            # Re-raise HTTP exceptions (e.g., 402 from metering) for proper response
            raise
        except Exception as e:
            error_trace = traceback.format_exc()
            logger.error(f"[ChatKit] Error in respond(): {e}")
            logger.error(f"[ChatKit] Traceback:\n{error_trace}")

            # Send error message to client
            error_message = AssistantMessageItem(
                id=self.store.generate_item_id("message", thread, context),
                thread_id=thread.id,
                created_at=datetime.now(),
                content=[
                    AssistantMessageContent(
                        text=(
                            "I apologize, but I encountered an error. "
                            "Please try again."
                        ),
                        annotations=[],
                    )
                ],
            )
            yield ThreadItemDoneEvent(item=error_message)


def create_chatkit_server(
    store: CachedPostgresStore | PostgresStore,
) -> StudyModeChatKitServer:
    """Create a configured Study Mode ChatKit server instance."""
    return StudyModeChatKitServer(store)
