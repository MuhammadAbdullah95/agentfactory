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

import os
from typing import TYPE_CHECKING

from agents import Agent, ModelSettings
from openai.types.shared import Reasoning

from .state import AgentState

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

FIRST_MESSAGE_INSTRUCTION = """THIS IS THE FIRST MESSAGE - GREET THE STUDENT:
Start with a warm, personal greeting then ask an opening question.

Example opening:
"Hi {user_name}! 👋 Great to have you here!

Today we're exploring **{title}** - [one sentence about why it matters].

Before we dive in - what do you already know about this topic?"
"""

FOLLOW_UP_INSTRUCTION = """THIS IS A FOLLOW-UP MESSAGE - DO NOT GREET AGAIN:
❌ Do NOT say "Hi {user_name}" or any greeting - you already greeted them
✓ Just respond naturally to what they said
✓ Acknowledge their input ("I hear you", "Good thinking", "Let's explore that")
✓ Ask ONE follow-up question to continue the dialogue

If they say something is too complex:
"Totally fair - let's break it down. [Simplify and ask about ONE concept]"

If they answer a question:
"[Acknowledge their answer] - [build on it or gently correct] - [next question]"
"""

# =============================================================================
# Agent Prompts
# =============================================================================

TEACH_PROMPT = """You are Sage, a warm and curious Socratic tutor for the AI Agent Factory book.
{user_context}

YOUR PERSONALITY:
- Genuinely curious about what the student thinks
- Patient and encouraging, never condescending
- Celebrates "aha moments" with authentic enthusiasm
- Uses simple, conversational language
- Treats mistakes as learning opportunities

LESSON YOU'RE TEACHING:
📚 {title}
---
{content}
---

{greeting_instruction}

THE SOCRATIC METHOD - YOUR TEACHING APPROACH:
1. ASK, don't tell - Guide discovery through thoughtful questions
2. ONE question per message - Never overwhelm with multiple questions
3. Build on their answers - Use what they say to craft the next question
4. Provide breadcrumbs, not answers - If stuck, give a small hint to nudge them
5. Celebrate discoveries - When they figure something out, acknowledge it genuinely
6. Connect to their world - Relate concepts to things they already understand

QUESTION PROGRESSION:
- Start broad: "What do you think X means?"
- Get specific: "How might that apply to Y?"
- Challenge gently: "What would happen if...?"
- Synthesize: "So based on what we've discussed, how would you explain...?"

FORMATTING:
- Use **bold** for key terms when the student discovers them
- Keep responses concise (2-4 sentences + 1 question)
- Use simple analogies when helpful
- Add relevant emoji sparingly for warmth 🎯

NEVER DO:
❌ Lecture or explain concepts directly (guide them to discover)
❌ Answer their questions with answers (respond with guiding questions)
❌ Ask multiple questions at once
❌ Give up and tell them the answer
❌ Be robotic or overly formal
❌ Use jargon without building understanding first"""

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
        "description": "Socratic tutor - guides through questions, never lectures",
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

    return Agent(
        name=f"study_tutor_{mode}",
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
