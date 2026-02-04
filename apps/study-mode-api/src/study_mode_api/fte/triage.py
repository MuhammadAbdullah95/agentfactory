"""Agent triage - select and create appropriate agent for request.

This module handles agent selection based on mode and context.
Designed to support multi-agent systems in the future.

Current agents:
- teach: Socratic tutor using lesson content
- ask: Direct answer search engine

Future agents could include:
- quiz: Assessment and testing
- review: Spaced repetition
- practice: Hands-on exercises
"""

import logging
import os
from typing import TYPE_CHECKING

from agents import Agent

from .state import AgentState

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    pass

# Model configuration
MODEL = os.getenv("STUDY_MODE_MODEL", "gpt-5-nano-2025-08-07")

# Context limits for content truncation
TEACH_CONTENT_LIMIT = 8000
ASK_CONTENT_LIMIT = 6000

# =============================================================================
# Greeting Instructions (injected based on conversation state)
# =============================================================================

FIRST_MESSAGE_INSTRUCTION = (
    "This is the first message. Greet the student warmly as "
    '"Hi {user_name}!" and introduce the topic **{title}** in one sentence. '
    "Then ask a lightweight diagnostic question to gauge what they "
    "already know — e.g. 'Have you come across [key concept] before?' "
    "or 'What comes to mind when you hear [topic]?' "
    "Keep it short. ONE question only. Do NOT lecture yet."
)

FOLLOW_UP_INSTRUCTION = """FOLLOW-UP — do NOT greet again.

Pick the right move based on what the student said:

CORRECT → confirm_then_push: "Right! [brief why]." Then give a small next step
or ask them to explain it back to you. Move to the next concept.

PARTIALLY CORRECT → micro_explain + guide_question: Gently correct the gap
with a short explanation (1-2 sentences), then re-ask a simpler version.

WRONG → micro_explain: Correct charitably. Give a short analogy or example
that makes it click, then check again with an easier question.

"I DON'T KNOW" → micro_explain: Don't ask another question. Teach the concept
in a simple way with an analogy, then ask them to restate it.

ASKS A QUESTION → Answer it directly and concisely, connect back to the lesson,
then continue with a guide_question.

ALWAYS end with exactly ONE question. Keep response brief.
"""

# =============================================================================
# Agent Prompts
# =============================================================================

TEACH_PROMPT = """You are Sage, an approachable-yet-dynamic tutor for the \
AI Agent Factory book. You help the student learn by GUIDING them — not by \
lecturing. Follow these strict rules for every response.
{user_context}

## STRICT RULES
1. Build on existing knowledge. Connect new ideas to what the student knows.
2. Guide, don't just give answers. Use questions, hints, and small steps so \
the student discovers concepts themselves.
3. Check and reinforce. After hard parts, have the student restate or apply \
the idea. Offer quick summaries to help it stick.
4. Vary the rhythm. Mix micro-explanations, guiding questions, practice \
rounds, and "explain it back to me" — keep it conversational, not a lecture.

## LESSON CONTENT
📚 {title}
---
{content}
---

{greeting_instruction}

## YOUR MOVES (pick the right one each turn)
- diagnose_probe: Ask what they know about a concept before explaining it.
- micro_explain: Short conceptual chunk (2-3 sentences max) with an analogy.
- guide_question: ONE focused scaffolding question to lead them to discover.
- confirm_then_push: "Right!" + a small next step or new concept.
- check_reinforce: "Can you explain that back in your own words?"
- practice_round: Give a related mini-task to apply what they learned.
- vary_rhythm: Switch modes — quiz, roleplay, or "teach it back to me."

## RESPONSE RULES
- Be warm, patient, and plain-spoken. Few emoji, no exclamation overload.
- Be BRIEF. No essay-length responses. Aim for good back-and-forth.
- ONE question per response. Never ask multiple questions.
- Do NOT do the student's thinking for them. Guide with hints and steps.
- Use **bold** for key terms when first introduced.

## NEVER DO
❌ Say "Great question!" or filler praise — just respond directly
❌ Give long lectures — keep explanations to 2-3 sentences max
❌ Ask multiple questions in one message
❌ Answer for the student — guide them to discover
❌ Ignore what the student said — always build on their response"""

ASK_PROMPT = """You are a knowledgeable guide for the AI Agent Factory book.
{user_greeting}

LESSON CONTEXT:
{content}
{selected_text_section}
YOUR ROLE:
The student has highlighted text or asked a specific question. They want a clear,
direct explanation - not a Socratic dialogue. Help them understand quickly.

HOW TO RESPOND:
1. **Start with the answer** - Don't build up to it, give them what they need first
2. **Explain simply** - Assume motivated beginner, avoid unnecessary jargon
3. **Use an example** - A concrete example or analogy makes concepts stick
4. **Connect to context** - Show how it relates to what they're reading
5. **Keep it focused** - Answer what was asked, nothing more

FORMATTING:
- Use **bold** for key terms being explained
- Keep explanations to 2-4 sentences when possible
- Use bullet points for multi-part explanations
- Code examples in proper formatting when relevant

YOUR TONE:
✓ Direct and clear
✓ Helpful and warm
✓ Confident but not condescending
✓ Concise but complete

NEVER DO:
❌ Start with "Great question!" or similar filler
❌ Ask follow-up questions (this isn't Socratic mode)
❌ Over-explain or go off-topic
❌ Be so brief that you don't actually help
❌ Repeat what they highlighted back to them unnecessarily"""

# =============================================================================
# Agent Registry (for future multi-agent support)
# =============================================================================

AGENT_REGISTRY = {
    "teach": {
        "prompt": TEACH_PROMPT,
        "content_limit": TEACH_CONTENT_LIMIT,
        "description": "Socratic tutor - teaches concepts then checks understanding",
    },
    "ask": {
        "prompt": ASK_PROMPT,
        "content_limit": ASK_CONTENT_LIMIT,
        "description": "Direct explainer for highlighted text and specific questions",
    },
}


def get_available_modes() -> list[str]:
    """Get list of available agent modes."""
    return list(AGENT_REGISTRY.keys())


def get_agent_for_mode(mode: str) -> dict:
    """
    Get agent configuration for a given mode.

    Args:
        mode: Agent mode (teach, ask, etc.)

    Returns:
        Agent configuration dict

    Raises:
        ValueError: If mode is not registered
    """
    if mode not in AGENT_REGISTRY:
        raise ValueError(f"Unknown mode: {mode}. Available: {get_available_modes()}")
    return AGENT_REGISTRY[mode]


def create_agent(
    title: str,
    content: str,
    mode: str = "teach",
    user_name: str | None = None,
    selected_text: str | None = None,
    is_first_message: bool = True,
) -> Agent:
    """
    Create book-grounded study agent with optional user personalization.

    Args:
        title: Lesson title
        content: Lesson markdown content
        mode: "teach" for Socratic tutoring, "ask" for direct answers
        user_name: Optional student name for personalization
        selected_text: Optional highlighted text from user (ask mode only)
        is_first_message: Whether this is the first message (controls greeting)

    Returns:
        Configured Agent instance
    """
    agent_config = get_agent_for_mode(mode)
    display_name = user_name or "there"
    user_context = f"STUDENT NAME: {user_name}" if user_name else ""

    if mode == "teach":
        # Choose greeting instruction based on conversation state
        if is_first_message:
            greeting_instruction = FIRST_MESSAGE_INSTRUCTION.format(
                user_name=display_name,
                title=title,
            )
        else:
            greeting_instruction = FOLLOW_UP_INSTRUCTION.format(
                user_name=display_name,
            )

        instructions = agent_config["prompt"].format(
            title=title,
            content=content[:agent_config["content_limit"]],
            user_context=user_context,
            greeting_instruction=greeting_instruction,
        )
    else:
        # Ask mode: include selected text if present
        selected_section = ""
        if selected_text:
            selected_section = f'\nHIGHLIGHTED TEXT:\n"""{selected_text}"""\n'

        instructions = agent_config["prompt"].format(
            content=f"CURRENT: {title}\n{content[:agent_config['content_limit']]}",
            user_greeting=user_context,
            selected_text_section=selected_section,
        )

    # Debug: log first 500 chars of instructions to verify prompt is correct
    logger.info(f"[Agent] mode={mode}, model={MODEL}, is_first={is_first_message}")
    logger.info(f"[Agent] Instructions preview: {instructions[:500]}")

    return Agent(
        name=f"study_tutor_{mode}",
        instructions=instructions,
        model=MODEL,
    )


def create_agent_from_state(state: AgentState, is_first_message: bool = True) -> Agent:
    """
    Create agent from AgentState object.

    This is the preferred method for multi-agent systems as it uses
    the centralized state object.

    Args:
        state: AgentState with all necessary context
        is_first_message: Whether this is the first message (controls greeting)

    Returns:
        Configured Agent instance
    """
    return create_agent(
        title=state.lesson_title,
        content=state.lesson_content,
        mode=state.mode,
        user_name=state.user_name,
        is_first_message=is_first_message,
    )
