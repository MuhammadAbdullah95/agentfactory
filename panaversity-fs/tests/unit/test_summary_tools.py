"""Unit tests for summary management tools."""

import pytest
import json
from panaversity_fs.tools.summaries import (
    add_summary, update_summary, get_summary, list_summaries
)
from panaversity_fs.models import (
    AddSummaryInput, UpdateSummaryInput, GetSummaryInput, ListSummariesInput
)
from panaversity_fs.errors import ContentNotFoundError


class TestAddSummary:
    """Test add_summary tool."""

    @pytest.mark.asyncio
    async def test_add_new_summary(self, setup_fs_backend, sample_summary_content):
        """Test adding a new summary."""
        result = await add_summary(AddSummaryInput(
            book_id="test-book",
            chapter_id="chapter-01",
            content=sample_summary_content
        ))

        data = json.loads(result)
        assert data["status"] == "success"
        assert "file_hash" in data
        assert "chapter-01" in data["path"]

    @pytest.mark.asyncio
    async def test_add_duplicate_summary_fails(self, sample_book_data, sample_summary_content):
        """Test that adding duplicate summary returns error."""
        # Summary already exists from fixture
        result = await add_summary(AddSummaryInput(
            book_id=sample_book_data["book_id"],
            chapter_id=sample_book_data["chapter_id"],
            content=sample_summary_content
        ))

        data = json.loads(result)
        assert "already exists" in data["message"]


class TestUpdateSummary:
    """Test update_summary tool."""

    @pytest.mark.asyncio
    async def test_update_existing_summary(self, sample_book_data):
        """Test updating existing summary."""
        new_content = "# Updated Summary\n\nNew content."

        result = await update_summary(UpdateSummaryInput(
            book_id=sample_book_data["book_id"],
            chapter_id=sample_book_data["chapter_id"],
            content=new_content
        ))

        data = json.loads(result)
        assert data["status"] == "success"
        assert data["mode"] == "updated"

        # Verify update
        get_result = await get_summary(GetSummaryInput(
            book_id=sample_book_data["book_id"],
            chapter_id=sample_book_data["chapter_id"]
        ))
        get_data = json.loads(get_result)
        assert "Updated Summary" in get_data["content"]

    @pytest.mark.asyncio
    async def test_update_creates_if_not_exists(self, setup_fs_backend, sample_summary_content):
        """Test that update creates summary if it doesn't exist."""
        result = await update_summary(UpdateSummaryInput(
            book_id="test-book",
            chapter_id="chapter-99",
            content=sample_summary_content
        ))

        data = json.loads(result)
        assert data["status"] == "success"


class TestGetSummary:
    """Test get_summary tool."""

    @pytest.mark.asyncio
    async def test_get_existing_summary(self, sample_book_data):
        """Test getting existing summary."""
        result = await get_summary(GetSummaryInput(
            book_id=sample_book_data["book_id"],
            chapter_id=sample_book_data["chapter_id"]
        ))

        data = json.loads(result)
        assert "content" in data
        assert "file_hash_sha256" in data
        assert "file_size" in data
        assert "Test summary" in data["content"]

    @pytest.mark.asyncio
    async def test_get_nonexistent_summary(self, setup_fs_backend):
        """Test getting non-existent summary raises error."""
        # This tool raises exception (unlike read_content which returns error string)
        with pytest.raises(ContentNotFoundError):
            await get_summary(GetSummaryInput(
                book_id="test-book",
                chapter_id="chapter-99"  # Valid format but doesn't exist
            ))


class TestListSummaries:
    """Test list_summaries tool."""

    @pytest.mark.asyncio
    async def test_list_all_summaries_for_book(self, sample_book_data):
        """Test listing all summaries for a book."""
        result = await list_summaries(ListSummariesInput(
            book_id=sample_book_data["book_id"]
        ))

        data = json.loads(result)
        assert isinstance(data, list)
        assert len(data) >= 1
        assert any("chapter-01" in item["path"] for item in data)

    @pytest.mark.asyncio
    async def test_list_summaries_for_specific_chapter(self, sample_book_data):
        """Test listing summaries for specific chapter."""
        result = await list_summaries(ListSummariesInput(
            book_id=sample_book_data["book_id"],
            chapter_id=sample_book_data["chapter_id"]
        ))

        data = json.loads(result)
        assert isinstance(data, list)
        if len(data) > 0:
            assert all("chapter-01" in item["path"] for item in data)

    @pytest.mark.asyncio
    async def test_list_summaries_empty_book(self, setup_fs_backend):
        """Test listing summaries for book with no summaries."""
        result = await list_summaries(ListSummariesInput(
            book_id="empty-book"
        ))

        data = json.loads(result)
        assert data == []

    @pytest.mark.asyncio
    async def test_list_summaries_includes_metadata(self, sample_book_data):
        """Test that list includes path, file_size, last_modified."""
        result = await list_summaries(ListSummariesInput(
            book_id=sample_book_data["book_id"]
        ))

        data = json.loads(result)
        if len(data) > 0:
            item = data[0]
            assert "path" in item
            assert "file_size" in item
            assert "last_modified" in item
