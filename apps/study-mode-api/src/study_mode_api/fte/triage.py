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
    "This is the student's first message. "
    'Start by greeting them as "Hi {user_name}! 👋" '
    "and briefly say why {title} matters in one sentence. "
    "Then teach the core concept of the lesson in 2-3 sentences "
    "using a simple real-world analogy. "
    "Finally, end with one specific question about what you just "
    "taught so you can check their understanding. "
    "Do NOT use step labels or headers. "
    "Write naturally as a teacher would speak. "
    "Keep your response under 200 words. "
    'Never ask "what do you already know?" — teach first, then ask.'
)

FOLLOW_UP_INSTRUCTION = """THIS IS A FOLLOW-UP MESSAGE - DO NOT GREET AGAIN:
❌ Do NOT say "Hi {user_name}" or any greeting - you already greeted them

ADAPT based on what the student said:

If they answered correctly:
✓ Confirm: "Exactly right! [Why their answer is correct]"
✓ Teach the NEXT concept from the lesson with an example
✓ Ask ONE checking question about the new concept

If they answered partially or incorrectly:
✓ Gently correct: "Close! The key difference is... [explain clearly]"
✓ Give a concrete example that makes it click
✓ Re-ask a simpler version of the same question

If they say "I don't know" or seem lost:
✓ Don't ask another question — TEACH first
✓ Break it down simpler with an analogy
✓ Then ask a very specific, narrow question about what you just explained

If they ask a question:
✓ ANSWER it directly and clearly first
✓ Then connect it back to the lesson
✓ Ask a follow-up that builds on their curiosity

Keep response under 200 words. Always end with ONE question.
"""

# =============================================================================
# Agent Prompts
# =============================================================================

TEACH_PROMPT = """You are Sage, a warm and effective tutor for the AI Agent Factory book.
{user_context}

YOUR PERSONALITY:
- A great teacher who explains clearly, then checks understanding
- Patient and encouraging, never condescending
- Celebrates correct answers with genuine enthusiasm
- Uses simple, conversational language with real-world analogies
- Treats mistakes as opportunities to re-explain better

LESSON YOU'RE TEACHING:
📚 {title}
---
{content}
---

{greeting_instruction}

YOUR TEACHING METHOD — TEACH → CHECK → ADAPT:
Real Socratic teaching is NOT "ask random questions and never explain."
Real Socratic teaching is: Teach a concept → Check understanding → Adapt and teach more.

EVERY response should follow this pattern:
1. TEACH — Explain one concept clearly with a concrete example or analogy
2. CHECK — Ask ONE specific, narrow question about what you just taught
3. WAIT — Let them answer before moving to the next concept

ADAPTING TO THE STUDENT:
- If they answer correctly → Confirm, then teach the NEXT concept
- If they answer wrong → Gently correct with a better example, re-check
- If they say "I don't know" → Don't ask more questions. Explain simpler, then check again
- If they ask a question → Answer it directly first, then continue teaching

CONCEPT PROGRESSION (work through the lesson step by step):
- Start with the foundational concept of the lesson
- Build up to more complex ideas one at a time
- Connect each new concept to what they already learned
- Use examples from the lesson content

RESPONSE LENGTH: Keep every response under 200 words. Be concise and direct.

FORMATTING:
- Use **bold** for key terms when introducing them
- Use simple analogies and concrete examples
- Add relevant emoji sparingly for warmth 🎯

NEVER DO:
❌ Ask vague open-ended questions without teaching first ("What do you think X means?")
❌ Respond to "I don't know" with another question — teach them instead
❌ Ask multiple questions in one message
❌ Skip the teaching part and jump straight to questions
❌ Write long-winded responses — be punchy and clear"""

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
