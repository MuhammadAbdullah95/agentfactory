"""MCP Client for PanaversityFS tool invocation.

This module provides a lightweight HTTP client for invoking PanaversityFS MCP tools.
It supports the key tools needed for hydration and ingestion workflows:
- plan_build: Delta detection for incremental builds
- read_content: Download individual files
- write_content: Upload content with conflict detection
- delete_content: Remove files from storage
- glob_search: Find files by pattern
- upload_asset: Upload binary assets
"""

import os
import json
import asyncio
from typing import Any
from dataclasses import dataclass

import httpx

from scripts.common.log_sanitizer import sanitize_message


class MCPError(Exception):
    """Base exception for MCP client errors."""
    pass


class MCPConnectionError(MCPError):
    """Raised when connection to MCP server fails."""
    pass


class MCPToolError(MCPError):
    """Raised when MCP tool returns an error."""
    def __init__(self, message: str, tool_name: str, error_type: str | None = None):
        super().__init__(message)
        self.tool_name = tool_name
        self.error_type = error_type


@dataclass
class MCPConfig:
    """Configuration for MCP client."""
    base_url: str
    timeout_seconds: float = 120.0
    max_retries: int = 3
    retry_delay_seconds: float = 1.0

    @classmethod
    def from_env(cls) -> "MCPConfig":
        """Load configuration from environment variables."""
        base_url = os.environ.get("PANAVERSITY_MCP_URL", "http://localhost:8000")
        timeout = float(os.environ.get("PANAVERSITY_MCP_TIMEOUT", "120"))
        return cls(base_url=base_url, timeout_seconds=timeout)


class MCPClient:
    """HTTP client for invoking PanaversityFS MCP tools.

    This client uses HTTP POST to invoke MCP tools directly, bypassing the
    stdio-based MCP protocol. This is simpler for CI/CD integration.

    Usage:
        async with MCPClient() as client:
            result = await client.plan_build("my-book")
            print(f"Manifest hash: {result['manifest_hash']}")
    """

    def __init__(self, config: MCPConfig | None = None):
        """Initialize MCP client.

        Args:
            config: Optional configuration. If not provided, loads from environment.
        """
        self.config = config or MCPConfig.from_env()
        self._client: httpx.AsyncClient | None = None

    async def __aenter__(self) -> "MCPClient":
        """Enter async context manager."""
        self._client = httpx.AsyncClient(
            base_url=self.config.base_url,
            timeout=httpx.Timeout(self.config.timeout_seconds)
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit async context manager."""
        if self._client:
            await self._client.aclose()
            self._client = None

    async def call_tool(self, tool_name: str, params: dict[str, Any]) -> dict[str, Any]:
        """Invoke an MCP tool with retry logic.

        Args:
            tool_name: Name of the MCP tool (e.g., "plan_build", "read_content")
            params: Tool parameters as a dictionary

        Returns:
            Tool response as a dictionary

        Raises:
            MCPConnectionError: If connection to server fails after retries
            MCPToolError: If tool returns an error response
        """
        if not self._client:
            raise MCPError("Client not initialized. Use 'async with MCPClient()' context manager.")

        last_error: Exception | None = None

        for attempt in range(self.config.max_retries):
            try:
                response = await self._client.post(
                    "/mcp/tools/call",
                    json={
                        "name": tool_name,
                        "arguments": params
                    }
                )

                if response.status_code == 200:
                    result = response.json()
                    # MCP tools return JSON string in content field
                    if "content" in result and isinstance(result["content"], list):
                        # Parse the text content from MCP response
                        for content_item in result["content"]:
                            if content_item.get("type") == "text":
                                return json.loads(content_item["text"])
                    return result

                elif response.status_code >= 500:
                    # Server error - retry
                    last_error = MCPConnectionError(f"Server error: {response.status_code}")
                    if attempt < self.config.max_retries - 1:
                        await asyncio.sleep(self.config.retry_delay_seconds * (attempt + 1))
                        continue

                else:
                    # Client error - don't retry
                    error_detail = response.text
                    try:
                        error_json = response.json()
                        error_detail = error_json.get("detail", error_detail)
                    except json.JSONDecodeError:
                        pass
                    # Sanitize error message to remove potential sensitive data
                    error_detail = sanitize_message(str(error_detail))
                    raise MCPToolError(
                        f"Tool '{tool_name}' failed: {error_detail}",
                        tool_name=tool_name,
                        error_type=str(response.status_code)
                    )

            except httpx.ConnectError as e:
                # Sanitize URL and error message
                safe_url = sanitize_message(self.config.base_url)
                safe_error = sanitize_message(str(e))
                last_error = MCPConnectionError(f"Failed to connect to {safe_url}: {safe_error}")
                if attempt < self.config.max_retries - 1:
                    await asyncio.sleep(self.config.retry_delay_seconds * (attempt + 1))
                    continue

            except httpx.TimeoutException as e:
                safe_error = sanitize_message(str(e))
                last_error = MCPConnectionError(f"Request timeout: {safe_error}")
                if attempt < self.config.max_retries - 1:
                    await asyncio.sleep(self.config.retry_delay_seconds * (attempt + 1))
                    continue

        if last_error:
            raise last_error
        raise MCPError("Unknown error during tool call")

    # Convenience methods for common tools

    async def plan_build(
        self,
        book_id: str,
        target_manifest_hash: str | None = None
    ) -> dict[str, Any]:
        """Get build plan with delta detection.

        Args:
            book_id: Book identifier
            target_manifest_hash: Previous manifest hash for incremental detection

        Returns:
            Plan build response with:
            - status: "unchanged" or "changed"
            - manifest_hash: Current manifest hash
            - files: List of changed files
            - changed_count: Number of changed files
            - total_files: Total files in book
        """
        params = {"book_id": book_id}
        if target_manifest_hash:
            params["target_manifest_hash"] = target_manifest_hash
        return await self.call_tool("plan_build", params)

    async def read_content(
        self,
        book_id: str,
        path: str,
        user_id: str | None = None
    ) -> dict[str, Any]:
        """Read content from storage.

        Args:
            book_id: Book identifier
            path: Content path within book
            user_id: Optional user ID for overlay content

        Returns:
            Content response with:
            - content: File content as string
            - file_hash_sha256: SHA256 hash of content
            - file_size: Size in bytes
            - source: "base" or "overlay"
        """
        params = {"book_id": book_id, "path": path}
        if user_id:
            params["user_id"] = user_id
        return await self.call_tool("read_content", params)

    async def write_content(
        self,
        book_id: str,
        path: str,
        content: str,
        expected_hash: str | None = None,
        user_id: str | None = None
    ) -> dict[str, Any]:
        """Write content to storage.

        Args:
            book_id: Book identifier
            path: Content path within book
            content: Markdown content to write
            expected_hash: Required for updates (conflict detection)
            user_id: Optional user ID for overlay content

        Returns:
            Write response with:
            - status: "success" or "error"
            - mode: "created" or "updated"
            - file_hash: New SHA256 hash
        """
        params = {"book_id": book_id, "path": path, "content": content}
        if expected_hash:
            params["expected_hash"] = expected_hash
        if user_id:
            params["user_id"] = user_id
        return await self.call_tool("write_content", params)

    async def delete_content(
        self,
        book_id: str,
        path: str,
        user_id: str | None = None
    ) -> dict[str, Any]:
        """Delete content from storage.

        Args:
            book_id: Book identifier
            path: Content path within book
            user_id: Optional user ID for overlay content

        Returns:
            Delete response with:
            - status: "success"
            - existed: Whether file existed before delete
        """
        params = {"book_id": book_id, "path": path}
        if user_id:
            params["user_id"] = user_id
        return await self.call_tool("delete_content", params)

    async def glob_search(
        self,
        book_id: str,
        pattern: str
    ) -> dict[str, Any]:
        """Search for files matching glob pattern.

        Args:
            book_id: Book identifier
            pattern: Glob pattern (e.g., "content/**/*.md")

        Returns:
            Search response with:
            - matches: List of matching file paths
            - count: Number of matches
        """
        return await self.call_tool("glob_search", {"book_id": book_id, "pattern": pattern})

    async def upload_asset(
        self,
        book_id: str,
        asset_type: str,
        filename: str,
        binary_data: str
    ) -> dict[str, Any]:
        """Upload binary asset.

        Args:
            book_id: Book identifier
            asset_type: Asset type (img, slides, videos, audio)
            filename: Original filename
            binary_data: Base64-encoded binary content

        Returns:
            Upload response with:
            - status: "success"
            - cdn_url: URL to access asset
            - file_size: Size in bytes
        """
        return await self.call_tool("upload_asset", {
            "book_id": book_id,
            "asset_type": asset_type,
            "filename": filename,
            "binary_data": binary_data
        })
