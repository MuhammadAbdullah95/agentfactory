"""Agent triage - select and create appropriate agent for request.

This module handles agent selection based on mode and context.
Designed to support multi-agent systems in the future.

Current agents:
- teach: Socratic tutor using lesson content (OpenAI)
- ask: Direct answer search engine (DeepSeek)

Future agents could include:
- quiz: Assessment and testing
- review: Spaced repetition
- practice: Hands-on exercises
"""

import logging
import os
from typing import TYPE_CHECKING

from agents import Agent, ModelSettings
from agents.model_settings import Reasoning

from .ask_agent import ask_agent
from .state import AgentState

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    pass

# Model configuration for Teach agent (uses OpenAI)
MODEL = os.getenv("STUDY_MODE_MODEL", "gpt-5-nano-2025-08-07")

# Context limit for teach content truncation
TEACH_CONTENT_LIMIT = 8000

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

Adapt based on what the student said:

If CORRECT: Confirm briefly ("Right!"), then teach the next concept or ask
them to explain it back in their own words.

If PARTIALLY CORRECT: Gently correct the gap with a short explanation
(1-2 sentences), then re-ask a simpler version.

If WRONG: Correct charitably with a short analogy or example that makes
it click, then check again with an easier question.

If "I DON'T KNOW" or STUCK: This is critical — do NOT ask another question.
TEACH the concept in 2-3 simple sentences with an analogy. Then ask them
to restate what you just explained.

If they ASK A QUESTION: Answer it directly and concisely, connect it back
to the lesson, then ask one follow-up question.

ALWAYS end with exactly ONE question. Keep response brief. No filler praise.
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

## HOW TO RESPOND (choose ONE approach per turn — NEVER show these labels)
- Ask what they know about a concept before explaining it.
- Give a short explanation (2-3 sentences max) with an analogy or example.
- Ask ONE focused question to lead them to discover the answer.
- Confirm correct answers briefly, then introduce the next concept.
- Ask them to explain it back in their own words.
- Give a related mini-task to apply what they learned.
- Switch modes — quiz, roleplay, or "teach it back to me."

## CRITICAL: WHEN STUDENT SAYS "I DON'T KNOW"
This is the most important rule. When a student says "I don't know" or \
seems stuck, you MUST:
1. TEACH the concept simply with an analogy (2-3 sentences)
2. Then ask them to restate what you just explained
You must NEVER respond to "I don't know" by asking another question or \
giving options. TEACH FIRST, then ask.

## RESPONSE RULES
- Be warm, patient, and plain-spoken. Few emoji, no exclamation overload.
- Be BRIEF. No essay-length responses. Aim for good back-and-forth.
- ONE question per response. Never ask multiple questions.
- Do NOT do the student's thinking for them. Guide with hints and steps.
- Use **bold** for key terms when first introduced.
- NEVER show internal labels like "Micro-explain:" in your response.

## NEVER DO
❌ Say "Great question!", "Nice start!" or any filler praise
❌ Give long lectures — keep explanations to 2-3 sentences max
❌ Ask multiple questions or give multiple-choice options
❌ Respond to "I don't know" with more questions — TEACH first
❌ Show move labels like "Micro-explain:" or "Guide question:" in output
❌ Ignore what the student said — always build on their response"""

# NOTE: ASK_PROMPT moved to ask_agent.py (uses DeepSeek provider)

# =============================================================================
# Agent Registry
# =============================================================================

# Available modes with their descriptions
AVAILABLE_MODES = {
    "teach": "Socratic tutor - teaches concepts then checks understanding (OpenAI)",
    "ask": "Direct explainer for highlighted text and specific questions (DeepSeek)",
}

# Teach mode config (ask mode handled by ask_agent.py)
TEACH_CONFIG = {
    "prompt": TEACH_PROMPT,
    "content_limit": TEACH_CONTENT_LIMIT,
}


def get_available_modes() -> list[str]:
    """Get list of available agent modes."""
    return list(AVAILABLE_MODES.keys())


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
    if mode not in AVAILABLE_MODES:
        raise ValueError(f"Unknown mode: {mode}. Available: {get_available_modes()}")

    # Ask mode: return singleton (uses dynamic instructions from context)
    # Note: context.metadata must be set with lesson_title, lesson_content, etc.
    # before calling Runner.run() - see chatkit_server.py
    if mode == "ask":
        return ask_agent

    # Teach mode: use OpenAI with Socratic tutoring
    display_name = user_name or "there"
    user_context = f"STUDENT NAME: {user_name}" if user_name else ""

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

    instructions = TEACH_CONFIG["prompt"].format(
        title=title,
        content=content[:TEACH_CONFIG["content_limit"]],
        user_context=user_context,
        greeting_instruction=greeting_instruction,
    )

    # Debug: log first 500 chars of instructions to verify prompt is correct
    logger.info(f"[Agent] mode={mode}, model={MODEL}, is_first={is_first_message}")
    logger.info(f"[Agent] Instructions preview: {instructions[:500]}")

    return Agent(
        name="study_tutor_teach",
        instructions=instructions,
        model=MODEL,
        model_settings=ModelSettings(reasoning=Reasoning(effort="minimal")),
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
