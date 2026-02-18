"""Content loading with frontmatter parsing."""

import logging
from typing import Any

import yaml

logger = logging.getLogger(__name__)


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
