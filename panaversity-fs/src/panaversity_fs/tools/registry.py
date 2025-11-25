"""Registry management tools for PanaversityFS.

Implements 1 MCP tool for book registry operations:
- list_books: List all books by scanning books/ directory (dynamic discovery)
"""

from panaversity_fs.app import mcp
from panaversity_fs.models import ListBooksInput, OperationType, OperationStatus
from panaversity_fs.storage import get_operator
from panaversity_fs.audit import log_operation
from panaversity_fs.config import get_config
from datetime import datetime, timezone
import json


@mcp.tool(
    name="list_books",
    annotations={
        "title": "List Books",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False
    }
)
async def list_books(params: ListBooksInput) -> str:
    """List all books by scanning books/ directory (FR-024).

    Dynamically discovers books by scanning subdirectories under books/.
    Each subdirectory name is treated as a book_id.

    Args:
        params (ListBooksInput): Empty input model (no parameters required)

    Returns:
        str: JSON array of book entries with book_id and storage_backend

    Example:
        ```
        Input: {}
        Output: [
          {
            "book_id": "ai-native-python",
            "storage_backend": "fs"
          },
          {
            "book_id": "generative-ai-fundamentals",
            "storage_backend": "fs"
          }
        ]
        ```
    """
    start_time = datetime.now(timezone.utc)

    try:
        # Get operator and config
        op = get_operator()
        config = get_config()

        # List books/ directory
        books_path = "books/"
        book_list = []

        try:
            # List immediate children of books/
            entries = await op.list(books_path)

            async for entry in entries:
                # Only include directories (paths ending with /)
                if entry.path.endswith('/'):
                    # Extract book_id from path: "books/ai-native-python/" -> "ai-native-python"
                    path_parts = entry.path.rstrip('/').split('/')
                    if len(path_parts) >= 2:
                        book_id = path_parts[-1]
                        # Skip hidden directories and special directories
                        if not book_id.startswith('.') and book_id != 'books':
                            book_list.append({
                                "book_id": book_id,
                                "storage_backend": config.storage_backend
                            })

        except Exception:
            # books/ directory doesn't exist yet, return empty array
            pass

        # Log success
        execution_time = int((datetime.now(timezone.utc) - start_time).total_seconds() * 1000)
        await log_operation(
            operation=OperationType.LIST_BOOKS,
            path=books_path,
            agent_id="system",
            status=OperationStatus.SUCCESS,
            execution_time_ms=execution_time
        )

        return json.dumps(book_list, indent=2)

    except Exception as e:
        # Log error
        await log_operation(
            operation=OperationType.LIST_BOOKS,
            path="books/",
            agent_id="system",
            status=OperationStatus.ERROR,
            error_message=str(e)
        )

        return f"Error listing books: {type(e).__name__}: {str(e)}"
