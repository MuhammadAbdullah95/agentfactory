"""FTE (Full-Time Equivalent) Agent System.

This module provides the agent orchestration layer:
- triage.py: Agent selection and creation based on mode
- ask_agent.py: Ask mode agent using DeepSeek
- state.py: Request state and context management
- tools.py: Agent tools for content access
"""

from .ask_agent import ASK_PROMPT, ask_agent
from .state import AgentState, create_state_from_context
from .tools import CONTENT_TOOLS, get_chapter_lessons, load_lesson
from .triage import (
    TEACH_PROMPT,
    create_agent,
    get_available_modes,
)

__all__ = [
    # State management
    "AgentState",
    "create_state_from_context",
    # Triage / agent selection
    "create_agent",
    "get_available_modes",
    "TEACH_PROMPT",
    # Ask agent (DeepSeek) - singleton with dynamic instructions
    "ask_agent",
    "ASK_PROMPT",
    # Tools
    "load_lesson",
    "get_chapter_lessons",
    "CONTENT_TOOLS",
]
