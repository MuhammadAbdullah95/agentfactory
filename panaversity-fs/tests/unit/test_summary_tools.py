"""Unit tests for summary management tools."""

import pytest
import json
from panaversity_fs.tools.summaries import read_summary, write_summary, delete_summary
from panaversity_fs.models import ReadSummaryInput, WriteSummaryInput, DeleteSummaryInput
from panaversity_fs.errors import ContentNotFoundError


class TestWriteSummary:
    """Test write_summary tool."""

    @pytest.mark.asyncio
    async def test_write_new_summary(self, setup_fs_backend, sample_summary_content):
        """Test writing a new summary."""
        result = await write_summary(WriteSummaryInput(
            book_id="test-book",
            chapter_id="chapter-01",
            content=sample_summary_content
        ))

        data = json.loads(result)
        assert data["status"] == "success"
        assert "sha256" in data
        assert "chapter-01" in data["path"]

    @pytest.mark.asyncio
    async def test_write_overwrites_existing(self, sample_book_data):
        """Test that write_summary overwrites existing summary."""
        new_content = "# Updated Summary\n\nNew content."

        result = await write_summary(WriteSummaryInput(
            book_id=sample_book_data["book_id"],
            chapter_id=sample_book_data["chapter_id"],
            content=new_content
        ))

        data = json.loads(result)
        assert data["status"] == "success"

        # Verify update
        read_result = await read_summary(ReadSummaryInput(
            book_id=sample_book_data["book_id"],
            chapter_id=sample_book_data["chapter_id"]
        ))
        read_data = json.loads(read_result)
        assert "Updated Summary" in read_data["content"]

    @pytest.mark.asyncio
    async def test_write_creates_if_not_exists(self, setup_fs_backend, sample_summary_content):
        """Test that write creates summary if it doesn't exist."""
        result = await write_summary(WriteSummaryInput(
            book_id="test-book",
            chapter_id="chapter-99",
            content=sample_summary_content
        ))

        data = json.loads(result)
        assert data["status"] == "success"


class TestReadSummary:
    """Test read_summary tool."""

    @pytest.mark.asyncio
    async def test_read_existing_summary(self, sample_book_data):
        """Test reading existing summary."""
        result = await read_summary(ReadSummaryInput(
            book_id=sample_book_data["book_id"],
            chapter_id=sample_book_data["chapter_id"]
        ))

        data = json.loads(result)
        assert "content" in data
        assert "sha256" in data
        assert "file_size" in data
        assert "Test summary" in data["content"]

    @pytest.mark.asyncio
    async def test_read_nonexistent_summary(self, setup_fs_backend):
        """Test reading non-existent summary raises error."""
        with pytest.raises(ContentNotFoundError):
            await read_summary(ReadSummaryInput(
                book_id="test-book",
                chapter_id="chapter-99"
            ))


class TestDeleteSummary:
    """Test delete_summary tool."""

    @pytest.mark.asyncio
    async def test_delete_existing_summary(self, setup_fs_backend, sample_summary_content):
        """Test deleting existing summary."""
        # First create a summary
        await write_summary(WriteSummaryInput(
            book_id="test-book",
            chapter_id="chapter-02",
            content=sample_summary_content
        ))

        # Now delete it
        result = await delete_summary(DeleteSummaryInput(
            book_id="test-book",
            chapter_id="chapter-02"
        ))

        data = json.loads(result)
        assert data["status"] == "success"
        assert "deleted" in data["message"]

        # Verify deletion
        with pytest.raises(ContentNotFoundError):
            await read_summary(ReadSummaryInput(
                book_id="test-book",
                chapter_id="chapter-02"
            ))

    @pytest.mark.asyncio
    async def test_delete_nonexistent_summary(self, setup_fs_backend):
        """Test deleting non-existent summary raises error."""
        with pytest.raises(ContentNotFoundError):
            await delete_summary(DeleteSummaryInput(
                book_id="test-book",
                chapter_id="chapter-99"
            ))
