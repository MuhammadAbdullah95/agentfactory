"""Agent-native teaching mode with function tools and guardrails.

This module implements the reviewer's suggested architecture:
- 4 function tools for agent autonomy
- 1 output guardrail for marker enforcement
- 1 agent creation function

Per reviewer: agent has full autonomy, server has zero branching.
"""

import logging
import re

from agents import Agent, GuardrailFunctionOutput, RunContextWrapper, function_tool, output_guardrail

from .teach_context import TeachContext
from .teach_instructions import teach_instructions

logger = logging.getLogger(__name__)

# Redis key patterns
ANSWER_KEY = "teach:correct_answer:{thread_id}"


# =============================================================================
# FUNCTION TOOLS (Exactly 4 per reviewer)
# =============================================================================


@function_tool
async def verify_answer(
    ctx: RunContextWrapper[TeachContext],
    answer: str,
) -> str:
    """
    Deterministic check against Redis-stored correct answer.

    Args:
        answer: Student's answer ("A", "B", or variations like "I think A")

    Returns:
        "CORRECT", "INCORRECT", or "UNKNOWN"
    """
    from ..core.redis_cache import get_redis

    thread_id = ctx.context.thread_id
    logger.info(f"[{thread_id}] verify_answer({answer})")

    redis = get_redis()
    if not redis:
        logger.warning(f"[{thread_id}] Redis unavailable")
        return "UNKNOWN"

    # Normalize answer
    normalized = _normalize_answer(answer)
    if not normalized:
        logger.warning(f"[{thread_id}] Could not normalize: {answer}")
        return "UNKNOWN"

    # Get stored answer
    key = ANSWER_KEY.format(thread_id=thread_id)
    try:
        stored = await redis.get(key)
    except Exception as e:
        logger.error(f"[{thread_id}] Redis error: {e}")
        return "UNKNOWN"

    if not stored:
        logger.warning(f"[{thread_id}] No stored answer")
        return "UNKNOWN"

    stored_str = stored.decode("utf-8") if isinstance(stored, bytes) else stored

    if normalized == stored_str:
        logger.info(f"[{thread_id}] -> CORRECT")
        return "CORRECT"

    logger.info(f"[{thread_id}] -> INCORRECT ({normalized} != {stored_str})")
    return "INCORRECT"


@function_tool
async def record_correct_answer(
    ctx: RunContextWrapper[TeachContext],
) -> str:
    """
    Record a correct answer. For single-chunk lessons, tracks progress toward completion.

    Returns:
        "MASTERY_ACHIEVED" if 5 correct on single-chunk lesson
        "PROGRESS_X_OF_5" for single-chunk lessons
        "ADVANCE_NOW" for multi-chunk lessons (proceed to advance_to_next_chunk)
    """
    thread_id = ctx.context.thread_id
    logger.info(f"[{thread_id}] record_correct_answer()")

    # For multi-chunk lessons, just advance normally
    if ctx.context.total_chunks > 1:
        logger.info(f"[{thread_id}] -> ADVANCE_NOW (multi-chunk lesson)")
        return "ADVANCE_NOW"

    # For single-chunk lessons, require 5 correct answers
    ctx.context.correct_count += 1

    if ctx.context.correct_count >= 5:
        logger.info(f"[{thread_id}] -> MASTERY_ACHIEVED")
        return "MASTERY_ACHIEVED"

    result = f"PROGRESS_{ctx.context.correct_count}_OF_5"
    logger.info(f"[{thread_id}] -> {result}")
    return result


@function_tool
async def advance_to_next_chunk(
    ctx: RunContextWrapper[TeachContext],
) -> str:
    """
    Move to next concept. Agent calls this after correct answer or max attempts.
    For single-chunk lessons, only call after MASTERY_ACHIEVED.

    Returns:
        Next chunk content as string, or "LESSON_COMPLETE"
    """
    thread_id = ctx.context.thread_id
    logger.info(f"[{thread_id}] advance_to_next_chunk()")

    ctx.context.current_chunk_index += 1
    ctx.context.attempt_count = 0
    ctx.context.correct_count = 0  # Reset for next chunk

    if ctx.context.current_chunk_index >= ctx.context.total_chunks:
        logger.info(f"[{thread_id}] -> LESSON_COMPLETE")
        return "LESSON_COMPLETE"

    chunk = ctx.context.current_chunk
    logger.info(f"[{thread_id}] -> NEXT_CHUNK: {chunk['title']}")
    return f"NEXT_CHUNK: {chunk['title']}\n\n{chunk['content']}"


@function_tool
async def record_incorrect_attempt(
    ctx: RunContextWrapper[TeachContext],
) -> str:
    """
    Track failed attempt. Agent calls this after incorrect answer.

    Returns:
        "MAX_ATTEMPTS_REACHED" or current attempt status
    """
    thread_id = ctx.context.thread_id
    logger.info(f"[{thread_id}] record_incorrect_attempt()")

    ctx.context.attempt_count += 1

    if ctx.context.attempt_count >= ctx.context.max_attempts:
        logger.info(f"[{thread_id}] -> MAX_ATTEMPTS_REACHED")
        return "MAX_ATTEMPTS_REACHED"

    result = f"ATTEMPT_{ctx.context.attempt_count}_OF_{ctx.context.max_attempts}"
    logger.info(f"[{thread_id}] -> {result}")
    return result


@function_tool
async def store_correct_answer(
    ctx: RunContextWrapper[TeachContext],
    correct_option: str,
) -> str:
    """
    Store which option is correct. Agent MUST call after asking every question.

    Args:
        correct_option: "A" or "B"

    Returns:
        "STORED" or error message
    """
    from ..core.redis_cache import get_redis

    thread_id = ctx.context.thread_id
    logger.info(f"[{thread_id}] store_correct_answer({correct_option})")

    if correct_option not in ("A", "B"):
        logger.error(f"[{thread_id}] Invalid option: {correct_option}")
        return "ERROR: Must be A or B"

    redis = get_redis()
    if not redis:
        logger.warning(f"[{thread_id}] Redis unavailable")
        return "ERROR: Redis unavailable"

    key = ANSWER_KEY.format(thread_id=thread_id)
    try:
        await redis.set(key, correct_option, ex=3600)  # 1 hour TTL
        logger.info(f"[{thread_id}] -> STORED")
        return "STORED"
    except Exception as e:
        logger.error(f"[{thread_id}] Redis error: {e}")
        return f"ERROR: {e}"


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================


def _normalize_answer(text: str) -> str | None:
    """Normalize answer to A or B."""
    clean = text.strip().upper()

    if clean in ("A", "B"):
        return clean

    # Match variations
    if clean in ("A)", "B)"):
        return clean[0]

    match = re.match(r"^OPTION\s*([AB])$", clean)
    if match:
        return match.group(1)

    # Word boundary match: "I think A because..." -> "A"
    word_match = re.search(r"\b([AB])\b", clean)
    if word_match:
        return word_match.group(1)

    return None


# =============================================================================
# OUTPUT GUARDRAIL (Simple per reviewer)
# =============================================================================


@output_guardrail
async def ensure_answer_marker(
    ctx: RunContextWrapper[TeachContext],
    agent: Agent,
    output: str,
) -> GuardrailFunctionOutput:
    """
    Reject output that has A/B question but missing <!--CORRECT:X--> marker.

    Simple check per reviewer's specification.
    """
    has_question = "A)" in output and "B)" in output
    has_marker = "<!--CORRECT:" in output

    if has_question and not has_marker:
        logger.warning(f"[{ctx.context.thread_id}] Guardrail triggered: missing marker")
        return GuardrailFunctionOutput(output_info=None, tripwire_triggered=True)

    return GuardrailFunctionOutput(output_info=None, tripwire_triggered=False)


# =============================================================================
# AGENT CREATION
# =============================================================================


def create_teach_agent() -> Agent:
    """Create the Socratic teaching agent with tools and guardrail."""
    return Agent(
        name="SocraticTutor",
        model="gpt-5-mini",
        instructions=teach_instructions,  # Dynamic callable
        tools=[
            verify_answer,
            record_correct_answer,
            advance_to_next_chunk,
            record_incorrect_attempt,
            store_correct_answer,
        ],
        output_guardrails=[ensure_answer_marker],
    )
