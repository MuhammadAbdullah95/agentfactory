"""HTTP client for progress-api (completion tracking)."""

import logging
from typing import Any

import httpx

from ..config import settings

logger = logging.getLogger(__name__)

PROGRESS_TIMEOUT = 10.0


class ProgressClient:
    """Async HTTP client for the progress API."""

    def __init__(self, base_url: str | None = None):
        self.base_url = (base_url or settings.progress_api_url).rstrip("/")
        self._client: httpx.AsyncClient | None = None

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.base_url,
                timeout=PROGRESS_TIMEOUT,
            )
        return self._client

    async def close(self) -> None:
        if self._client:
            await self._client.aclose()
            self._client = None

    async def complete_lesson(
        self,
        chapter_slug: str,
        lesson_slug: str,
        active_duration_secs: int = 0,
        auth_token: str | None = None,
    ) -> dict[str, Any]:
        """Record lesson completion via progress API."""
        client = await self._get_client()

        payload = {
            "chapter_slug": chapter_slug,
            "lesson_slug": lesson_slug,
            "active_duration_secs": active_duration_secs,
        }

        try:
            headers = {}
            if auth_token:
                headers["Authorization"] = auth_token

            response = await client.post(
                "/api/v1/progress/complete",
                json=payload,
                headers=headers,
            )

            if response.status_code == 200:
                return response.json()
            else:
                logger.error(
                    f"[Progress] Complete failed: status={response.status_code}, "
                    f"body={response.text}"
                )
                return {"completed": False, "xp_earned": 0}

        except httpx.TimeoutException as e:
            logger.error(f"[Progress] Complete timeout: {type(e).__name__}")
            return {"completed": False, "xp_earned": 0}
        except httpx.HTTPError as e:
            logger.error(f"[Progress] Complete failed: {type(e).__name__}: {e}")
            return {"completed": False, "xp_earned": 0}


# Module-level client instance
_client: ProgressClient | None = None


def get_progress_client() -> ProgressClient | None:
    """Get the global progress client. Returns None if progress API not configured."""
    global _client

    if not settings.progress_api_url:
        return None

    if _client is None:
        _client = ProgressClient()

    return _client
