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

from agents import Agent

from .state import AgentState

if TYPE_CHECKING:
    pass

# Model configuration
MODEL = os.getenv("STUDY_MODE_MODEL", "gpt-5-nano-2025-08-07")

# Context limits for content truncation
TEACH_CONTENT_LIMIT = 8000
ASK_CONTENT_LIMIT = 6000

# =============================================================================
# Agent Prompts
# =============================================================================

TEACH_PROMPT = """You are a FRIENDLY TUTOR for the AgentFactory book using Socratic method.
{user_greeting}
PAGE: {title}
---
{content}
---

RULES:
1. EXPLAIN one concept (2-3 sentences)
2. ASK ONE checking question
3. Wait for response, then continue
4. Use bold for key terms
5. Be warm and encouraging
6. Stay focused on page content
7. Address the student by name when appropriate"""

ASK_PROMPT = """You are a SEARCH ENGINE for the AgentFactory book.
{user_greeting}
{content}

RULES:
- Give direct answers in 1-3 sentences
- NO "Great question!"
- NO follow-up questions
- Just answer and STOP"""

# =============================================================================
# Agent Registry (for future multi-agent support)
# =============================================================================

AGENT_REGISTRY = {
    "teach": {
        "prompt": TEACH_PROMPT,
        "content_limit": TEACH_CONTENT_LIMIT,
        "description": "Socratic tutor for deep understanding",
    },
    "ask": {
        "prompt": ASK_PROMPT,
        "content_limit": ASK_CONTENT_LIMIT,
        "description": "Direct answer search engine",
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
) -> Agent:
    """
    Create book-grounded study agent with optional user personalization.

    Args:
        title: Lesson title
        content: Lesson markdown content
        mode: "teach" for Socratic tutoring, "ask" for direct answers
        user_name: Optional student name for personalization

    Returns:
        Configured Agent instance
    """
    agent_config = get_agent_for_mode(mode)
    user_greeting = f"STUDENT: {user_name}" if user_name else ""

    if mode == "teach":
        instructions = agent_config["prompt"].format(
            title=title,
            content=content[:agent_config["content_limit"]],
            user_greeting=user_greeting,
        )
    else:
        instructions = agent_config["prompt"].format(
            content=f"CURRENT: {title}\n{content[:agent_config['content_limit']]}",
            user_greeting=user_greeting,
        )

    return Agent(name=f"study_tutor_{mode}", instructions=instructions, model=MODEL)


def create_agent_from_state(state: AgentState) -> Agent:
    """
    Create agent from AgentState object.

    This is the preferred method for multi-agent systems as it uses
    the centralized state object.

    Args:
        state: AgentState with all necessary context

    Returns:
        Configured Agent instance
    """
    return create_agent(
        title=state.lesson_title,
        content=state.lesson_content,
        mode=state.mode,
        user_name=state.user_name,
    )
