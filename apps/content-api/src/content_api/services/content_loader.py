"""Content loading with GitHub fetch, caching, and frontmatter parsing."""

import logging
from typing import Any

import httpx
import yaml
from api_infra.core.redis_cache import cache_response

from ..config import settings

logger = logging.getLogger(__name__)

CONTENT_CACHE_TTL = settings.content_cache_ttl

# Reusable httpx client for GitHub fetches (connection pooling)
_http_client: httpx.AsyncClient | None = None


def _get_http_client() -> httpx.AsyncClient:
    global _http_client
    if _http_client is None:
        _http_client = httpx.AsyncClient(timeout=10.0)
    return _http_client


def parse_frontmatter(content: str) -> tuple[dict[str, Any], str]:
    """Parse YAML frontmatter from markdown content.

    Args:
        content: Full markdown content, possibly with --- delimited frontmatter.

    Returns:
        Tuple of (frontmatter_dict, body_content).
        Returns ({}, content) if no frontmatter found.
        Returns ({}, content) on malformed YAML (graceful degradation).
    """
    if not content or not content.startswith("---"):
        return {}, content

    # Find the closing ---
    end_idx = content.find("---", 3)
    if end_idx == -1:
        return {}, content

    frontmatter_str = content[3:end_idx].strip()
    body = content[end_idx + 3 :].lstrip("\n")

    try:
        frontmatter = yaml.safe_load(frontmatter_str)
        if not isinstance(frontmatter, dict):
            return {}, content
        return frontmatter, body
    except yaml.YAMLError as e:
        logger.warning(f"[ContentLoader] Malformed YAML frontmatter: {e}")
        return {}, content


async def fetch_from_github(lesson_path: str) -> tuple[str, bool]:
    """Fetch lesson content from GitHub raw URLs.

    Args:
        lesson_path: Path like "01-Part/02-chapter/03-lesson"

    Returns:
        Tuple of (content, success)
    """
    if not lesson_path:
        return "", False

    clean_path = lesson_path.strip("/")
    if clean_path.startswith("docs/"):
        clean_path = f"apps/learn-app/{clean_path}"
    elif not clean_path.startswith("apps/"):
        clean_path = f"apps/learn-app/docs/{clean_path}"

    extensions = [""]
    if not clean_path.endswith((".md", ".mdx")):
        extensions = [".md", ".mdx", "/index.md", "/README.md"]

    client = _get_http_client()
    headers = {}
    if settings.github_token:
        headers["Authorization"] = f"token {settings.github_token}"

    for ext in extensions:
        url = f"https://raw.githubusercontent.com/{settings.github_repo}/main/{clean_path}{ext}"

        try:
            response = await client.get(url, headers=headers)

            if response.status_code == 200:
                logger.debug(f"Fetched content from GitHub: {url}")
                return response.text, True

        except Exception as e:
            logger.warning(f"Failed to fetch from GitHub {url}: {e}")
            continue

    return "", False


@cache_response(ttl=CONTENT_CACHE_TTL)
async def load_lesson_content(part_slug: str, chapter_slug: str, lesson_slug: str) -> dict:
    """Load lesson content with caching.

    Args:
        part_slug: Part directory name (e.g., "01-General-Agents-Foundations")
        chapter_slug: Chapter directory name (e.g., "02-general-agents")
        lesson_slug: Lesson file name without extension (e.g., "03-my-lesson")

    Returns:
        Dict with content, frontmatter_dict, chapter_slug, lesson_slug
    """
    lesson_path = f"{part_slug}/{chapter_slug}/{lesson_slug}"

    content, success = await fetch_from_github(lesson_path)

    if not success:
        return {
            "content": "",
            "frontmatter_dict": {},
            "chapter_slug": chapter_slug,
            "lesson_slug": lesson_slug,
            "found": False,
        }

    frontmatter_dict, body = parse_frontmatter(content)

    return {
        "content": content,
        "frontmatter_dict": frontmatter_dict,
        "chapter_slug": chapter_slug,
        "lesson_slug": lesson_slug,
        "found": True,
    }
