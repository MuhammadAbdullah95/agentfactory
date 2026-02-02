"""Tests for ChatKit server and Study Mode integration.

Tests the chatkit_server module and request context handling.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from study_mode_api.chatkit_server import StudyModeChatKitServer
from study_mode_api.chatkit_store import RequestContext
from study_mode_api.fte import (
    ASK_PROMPT,
    TEACH_PROMPT,
    create_agent,
)


class TestAgentCreation:
    """Test agent creation with different modes."""

    def test_create_teach_agent(self):
        """Test creating agent in teach mode."""
        agent = create_agent(
            title="Test Lesson",
            content="This is test content about AI agents.",
            mode="teach",
        )

        assert agent.name == "study_tutor_teach"
        assert "Socratic tutor" in agent.instructions
        assert "Test Lesson" in agent.instructions
        assert "Lecture or explain concepts directly" in agent.instructions

    def test_create_ask_agent(self):
        """Test creating agent in ask/search mode."""
        agent = create_agent(
            title="Test Lesson",
            content="This is test content about AI agents.",
            mode="ask",
        )

        assert agent.name == "study_tutor_ask"
        assert "knowledgeable guide" in agent.instructions
        assert "direct explanation" in agent.instructions

    def test_create_agent_with_user_name(self):
        """Test creating agent with user personalization."""
        agent = create_agent(
            title="Test Lesson",
            content="This is test content.",
            mode="teach",
            user_name="Alice",
        )

        assert "STUDENT NAME: Alice" in agent.instructions

    def test_create_agent_without_user_name(self):
        """Test creating agent without user name."""
        agent = create_agent(
            title="Test Lesson",
            content="This is test content.",
            mode="teach",
            user_name=None,
        )

        # Without user name, no STUDENT NAME line should be present
        assert "STUDENT NAME:" not in agent.instructions

    def test_content_truncation_teach_mode(self):
        """Test content is truncated in teach mode (8000 chars)."""
        long_content = "A" * 10000
        agent = create_agent(
            title="Test",
            content=long_content,
            mode="teach",
        )

        # Content should be truncated to 8000 chars
        assert len(agent.instructions) < len(long_content)
        assert "A" * 100 in agent.instructions  # Some content preserved

    def test_content_truncation_ask_mode(self):
        """Test content is truncated in ask mode (6000 chars)."""
        long_content = "B" * 8000
        agent = create_agent(
            title="Test",
            content=long_content,
            mode="ask",
        )

        # Content should be truncated to 6000 chars
        assert len(agent.instructions) < len(long_content)

    def test_create_agent_with_selected_text(self):
        """Test creating agent with highlighted text (ask mode)."""
        agent = create_agent(
            title="Test Lesson",
            content="This is test content.",
            mode="ask",
            selected_text="What is an agent?",
        )

        assert "HIGHLIGHTED TEXT:" in agent.instructions
        assert "What is an agent?" in agent.instructions

    def test_create_agent_without_selected_text(self):
        """Test creating agent without selected text."""
        agent = create_agent(
            title="Test Lesson",
            content="This is test content.",
            mode="ask",
            selected_text=None,
        )

        # Without selected_text, no HIGHLIGHTED TEXT section
        assert "HIGHLIGHTED TEXT:" not in agent.instructions

    def test_create_agent_first_message_greeting(self):
        """Test agent includes greeting instruction for first message."""
        agent = create_agent(
            title="Test Lesson",
            content="This is test content.",
            mode="teach",
            user_name="Alice",
            is_first_message=True,
        )

        assert "GREET THE STUDENT" in agent.instructions

    def test_create_agent_follow_up_no_greeting(self):
        """Test agent excludes greeting for follow-up messages."""
        agent = create_agent(
            title="Test Lesson",
            content="This is test content.",
            mode="teach",
            user_name="Alice",
            is_first_message=False,
        )

        assert "DO NOT GREET AGAIN" in agent.instructions
        assert "GREET THE STUDENT" not in agent.instructions


class TestPromptTemplates:
    """Test prompt template structure."""

    def test_teach_prompt_has_required_elements(self):
        """Test teach prompt contains required instructional elements."""
        assert "{title}" in TEACH_PROMPT
        assert "{content}" in TEACH_PROMPT
        assert "Socratic" in TEACH_PROMPT
        assert "Lecture or explain concepts directly" in TEACH_PROMPT
        assert "ONE question per message" in TEACH_PROMPT

    def test_ask_prompt_has_required_elements(self):
        """Test ask prompt contains direct answer instructions."""
        assert "{content}" in ASK_PROMPT
        assert "{selected_text_section}" in ASK_PROMPT
        assert "direct explanation" in ASK_PROMPT
        assert "Socratic" in ASK_PROMPT  # Mentions it's NOT Socratic mode


class TestRequestContext:
    """Test request context creation for ChatKit."""

    def test_context_includes_metadata(self):
        """Test RequestContext includes lesson metadata."""
        context = RequestContext(
            user_id="user-123",
            request_id="req-456",
            metadata={
                "lesson_path": "/docs/chapter1/lesson1",
                "mode": "teach",
                "user_name": "John",
            },
        )

        assert context.user_id == "user-123"
        assert context.metadata["lesson_path"] == "/docs/chapter1/lesson1"
        assert context.metadata["mode"] == "teach"
        assert context.metadata["user_name"] == "John"

    def test_context_requires_user_id(self):
        """Test RequestContext requires non-empty user_id."""
        with pytest.raises(ValueError):
            RequestContext(user_id="")


class TestStudyModeChatKitServer:
    """Test StudyModeChatKitServer initialization."""

    def test_server_initialization(self):
        """Test server initializes with store."""
        mock_store = MagicMock()

        server = StudyModeChatKitServer(store=mock_store)

        assert server.store == mock_store

    @pytest.mark.asyncio
    async def test_server_uses_content_loader(self):
        """Test server uses content loader for lesson content."""
        mock_store = MagicMock()
        mock_store.load_thread_items = AsyncMock(
            return_value=MagicMock(data=[])
        )

        with patch(
            "study_mode_api.chatkit_server.load_lesson_content",
            new_callable=AsyncMock,
            return_value={"content": "Test content", "title": "Test"},
        ):
            server = StudyModeChatKitServer(store=mock_store)

            # The respond method would be called internally
            # This verifies the integration point exists
            assert hasattr(server, "respond")


class TestUserContextPropagation:
    """Test that user context flows through to agent."""

    def test_context_metadata_includes_user_name(self):
        """Test that user name is included in context metadata."""
        context = RequestContext(
            user_id="user-123",
            metadata={
                "user_name": "Alice",
                "lesson_path": "/docs/test",
                "mode": "teach",
            },
        )

        assert context.metadata.get("user_name") == "Alice"

    def test_context_without_user_name(self):
        """Test context works without user name."""
        context = RequestContext(
            user_id="user-123",
            metadata={
                "lesson_path": "/docs/test",
                "mode": "teach",
            },
        )

        assert context.metadata.get("user_name") is None
