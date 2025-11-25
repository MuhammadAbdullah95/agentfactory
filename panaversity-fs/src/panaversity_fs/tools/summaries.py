"""Summary management tools for PanaversityFS.

Implements 3 MCP tools for chapter summary management:
- read_summary: Read summary with metadata
- write_summary: Create or update summary
- delete_summary: Delete summary
"""

from panaversity_fs.server import mcp
from panaversity_fs.models import (
    ReadSummaryInput, WriteSummaryInput, DeleteSummaryInput,
    SummaryMetadata, OperationType, OperationStatus
)
from panaversity_fs.storage import get_operator
from panaversity_fs.storage_utils import compute_sha256
from panaversity_fs.errors import ContentNotFoundError
from panaversity_fs.audit import log_operation
from panaversity_fs.config import get_config
from datetime import datetime, timezone
import json


@mcp.tool(
    name="read_summary",
    annotations={
        "title": "Read Chapter Summary",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False
    }
)
async def read_summary(params: ReadSummaryInput) -> str:
    """Read chapter summary with metadata.

    Returns summary content plus metadata: file_size, last_modified, storage_backend, sha256, path.

    Args:
        params: book_id and chapter_id

    Returns:
        JSON with summary content and metadata
    """
    start_time = datetime.now(timezone.utc)
    summary_path = f"books/{params.book_id}/chapters/{params.chapter_id}/.summary.md"

    try:
        op = get_operator()
        config = get_config()

        # Read content
        try:
            content_bytes = await op.read(summary_path)
            content = content_bytes.decode('utf-8')
        except:
            raise ContentNotFoundError(summary_path)

        # Get metadata
        metadata = await op.stat(summary_path)
        file_hash = compute_sha256(content_bytes)

        response = {
            "path": summary_path,
            "content": content,
            "file_size": metadata.content_length,
            "last_modified": metadata.last_modified.isoformat(),
            "storage_backend": config.storage_backend,
            "sha256": file_hash
        }

        # Log success
        execution_time = int((datetime.now(timezone.utc) - start_time).total_seconds() * 1000)
        await log_operation(
            operation=OperationType.READ_SUMMARY,
            path=summary_path,
            agent_id="system",
            status=OperationStatus.SUCCESS,
            execution_time_ms=execution_time
        )

        return json.dumps(response, indent=2)

    except ContentNotFoundError:
        await log_operation(
            operation=OperationType.READ_SUMMARY,
            path=summary_path,
            agent_id="system",
            status=OperationStatus.ERROR,
            error_message="Summary not found"
        )
        raise

    except Exception as e:
        await log_operation(
            operation=OperationType.READ_SUMMARY,
            path=summary_path,
            agent_id="system",
            status=OperationStatus.ERROR,
            error_message=str(e)
        )
        return f"Error reading summary: {type(e).__name__}: {str(e)}"


@mcp.tool(
    name="write_summary",
    annotations={
        "title": "Write Chapter Summary",
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False
    }
)
async def write_summary(params: WriteSummaryInput) -> str:
    """Create or update chapter summary.

    Writes summary markdown at: books/[book-id]/chapters/[chapter-id]/.summary.md

    Args:
        params: book_id, chapter_id, and content

    Returns:
        JSON with path, file_size, and sha256
    """
    start_time = datetime.now(timezone.utc)
    summary_path = f"books/{params.book_id}/chapters/{params.chapter_id}/.summary.md"

    try:
        op = get_operator()

        # Write content
        content_bytes = params.content.encode('utf-8')
        await op.write(summary_path, content_bytes)

        # Get metadata
        metadata = await op.stat(summary_path)
        file_hash = compute_sha256(content_bytes)

        response = {
            "status": "success",
            "path": summary_path,
            "file_size": metadata.content_length,
            "sha256": file_hash
        }

        # Log success
        execution_time = int((datetime.now(timezone.utc) - start_time).total_seconds() * 1000)
        await log_operation(
            operation=OperationType.WRITE_SUMMARY,
            path=summary_path,
            agent_id="system",
            status=OperationStatus.SUCCESS,
            execution_time_ms=execution_time
        )

        return json.dumps(response, indent=2)

    except Exception as e:
        await log_operation(
            operation=OperationType.WRITE_SUMMARY,
            path=summary_path,
            agent_id="system",
            status=OperationStatus.ERROR,
            error_message=str(e)
        )
        return f"Error writing summary: {type(e).__name__}: {str(e)}"


@mcp.tool(
    name="delete_summary",
    annotations={
        "title": "Delete Chapter Summary",
        "readOnlyHint": False,
        "destructiveHint": True,
        "idempotentHint": True,
        "openWorldHint": False
    }
)
async def delete_summary(params: DeleteSummaryInput) -> str:
    """Delete chapter summary.

    Removes summary file at: books/[book-id]/chapters/[chapter-id]/.summary.md

    Args:
        params: book_id and chapter_id

    Returns:
        JSON with deletion confirmation
    """
    start_time = datetime.now(timezone.utc)
    summary_path = f"books/{params.book_id}/chapters/{params.chapter_id}/.summary.md"

    try:
        op = get_operator()

        # Check if exists
        try:
            await op.stat(summary_path)
        except:
            raise ContentNotFoundError(summary_path)

        # Delete
        await op.delete(summary_path)

        response = {
            "status": "success",
            "path": summary_path,
            "message": "Summary deleted"
        }

        # Log success
        execution_time = int((datetime.now(timezone.utc) - start_time).total_seconds() * 1000)
        await log_operation(
            operation=OperationType.DELETE_SUMMARY,
            path=summary_path,
            agent_id="system",
            status=OperationStatus.SUCCESS,
            execution_time_ms=execution_time
        )

        return json.dumps(response, indent=2)

    except ContentNotFoundError:
        await log_operation(
            operation=OperationType.DELETE_SUMMARY,
            path=summary_path,
            agent_id="system",
            status=OperationStatus.ERROR,
            error_message="Summary not found"
        )
        raise

    except Exception as e:
        await log_operation(
            operation=OperationType.DELETE_SUMMARY,
            path=summary_path,
            agent_id="system",
            status=OperationStatus.ERROR,
            error_message=str(e)
        )
        return f"Error deleting summary: {type(e).__name__}: {str(e)}"
