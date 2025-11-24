"""Registry management tools for PanaversityFS.

Implements 1 MCP tool for book registry operations:
- list_books: List all registered books from registry.yaml
"""

from panaversity_fs.server import mcp
from panaversity_fs.models import ListBooksInput, BookMetadata, OperationType, OperationStatus
from panaversity_fs.storage import get_operator
from panaversity_fs.audit import log_operation
from datetime import datetime, timezone
import json
import yaml


@mcp.tool(
    name="list_books",
    annotations={
        "title": "List Registered Books",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False
    }
)
async def list_books(params: ListBooksInput) -> str:
    """List all registered books from registry.yaml (FR-024).

    Returns array of book metadata including status: [active, archived, migrating].

    Args:
        params (ListBooksInput): Empty input model (no parameters required)

    Returns:
        str: JSON array of book metadata

    Example:
        ```
        Input: {}
        Output: [
          {
            "book_id": "ai-native-python",
            "title": "AI-Native Python Development",
            "storage_backend": "fs",
            "created_at": "2025-01-01T00:00:00Z",
            "status": "active"
          },
          {
            "book_id": "generative-ai-fundamentals",
            "title": "Generative AI Fundamentals",
            "storage_backend": "s3",
            "created_at": "2025-02-01T00:00:00Z",
            "status": "active"
          }
        ]
        ```
    """
    start_time = datetime.now(timezone.utc)

    try:
        # Get operator
        op = get_operator()

        # Read registry.yaml
        registry_path = "registry.yaml"

        try:
            registry_bytes = await op.read(registry_path)
            registry_content = registry_bytes.decode('utf-8')

            # Parse YAML
            registry_data = yaml.safe_load(registry_content)

            # Extract books array
            books = registry_data.get('books', [])

            # Validate and return
            book_list = []
            for book in books:
                try:
                    # Validate with Pydantic model
                    book_metadata = BookMetadata(**book)
                    book_list.append(book_metadata.model_dump())
                except Exception as e:
                    # Skip invalid entries
                    continue

            # Log success
            execution_time = int((datetime.now(timezone.utc) - start_time).total_seconds() * 1000)
            await log_operation(
                operation=OperationType.LIST_BOOKS,
                path=registry_path,
                agent_id="system",
                status=OperationStatus.SUCCESS,
                execution_time_ms=execution_time
            )

            return json.dumps(book_list, indent=2, default=str)

        except FileNotFoundError:
            # Registry doesn't exist yet, return empty array
            return json.dumps([], indent=2)

    except Exception as e:
        # Log error
        await log_operation(
            operation=OperationType.LIST_BOOKS,
            path="registry.yaml",
            agent_id="system",
            status=OperationStatus.ERROR,
            error_message=str(e)
        )

        return f"Error listing books: {type(e).__name__}: {str(e)}"
