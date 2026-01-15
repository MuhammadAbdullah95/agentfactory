#!/usr/bin/env python3
"""
Scope Discovery - Parse input and discover lesson files

Handles:
- "Part 2" → All chapters in Part 2
- "Chapter 5" → Chapter 5 (asks if ambiguous)
- "Chapter 5 from Part 2" → Specific chapter
- Absolute paths → Use directly
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class ScopeMetadata:
    scope_type: str  # "part", "chapter", "lesson", "custom"
    part_number: Optional[int] = None
    chapter_number: Optional[int] = None
    chapter_name: Optional[str] = None
    needs_clarification: bool = False
    ambiguous_options: Optional[List[Dict]] = None
    error: Optional[str] = None


def parse_scope_input(user_input: str) -> ScopeMetadata:
    """
    Parse user input to extract scope intent.

    Examples:
    - "Part 2" → part_number=2, scope_type="part"
    - "Chapter 5" → chapter_number=5, needs_clarification (if multiple)
    - "Chapter 5 from Part 2" → part_number=2, chapter_number=5, scope_type="chapter"
    - "/path/to/file.md" → scope_type="custom"
    """
    user_input = user_input.strip()

    # Check for absolute path
    if user_input.startswith("/"):
        return ScopeMetadata(scope_type="custom")

    # Pattern: "Chapter X from Part Y"
    match = re.match(r"Chapter\s+(\d+)\s+from\s+Part\s+(\d+)", user_input, re.IGNORECASE)
    if match:
        chapter_num = int(match.group(1))
        part_num = int(match.group(2))
        return ScopeMetadata(
            scope_type="chapter",
            chapter_number=chapter_num,
            part_number=part_num
        )

    # Pattern: "Part X"
    match = re.match(r"Part\s+(\d+)", user_input, re.IGNORECASE)
    if match:
        part_num = int(match.group(1))
        return ScopeMetadata(scope_type="part", part_number=part_num)

    # Pattern: "Chapter X"
    match = re.match(r"Chapter\s+(\d+)", user_input, re.IGNORECASE)
    if match:
        chapter_num = int(match.group(1))
        return ScopeMetadata(
            scope_type="chapter",
            chapter_number=chapter_num,
            needs_clarification=True  # May exist in multiple parts
        )

    # Pattern: "Part X, Chapter Y"
    match = re.match(r"Part\s+(\d+),\s*Chapter\s+(\d+)", user_input, re.IGNORECASE)
    if match:
        part_num = int(match.group(1))
        chapter_num = int(match.group(2))
        return ScopeMetadata(
            scope_type="chapter",
            part_number=part_num,
            chapter_number=chapter_num
        )

    return ScopeMetadata(
        scope_type="custom",
        error=f"Could not parse scope: {user_input}"
    )


def find_part_directory(part_number: int, base_path: Path) -> Optional[Path]:
    """Find directory for part number (e.g., 01-Introducing-AI...)"""
    pattern = f"{part_number:02d}-*"
    matches = list(base_path.glob(pattern))
    if matches:
        return matches[0]
    return None


def find_chapter_directories(part_number: int, chapter_number: int, base_path: Path) -> List[Path]:
    """
    Find all chapter directories matching chapter number.

    Returns list of matching directories (may be multiple if chapter number exists in multiple parts)
    """
    all_chapters = []

    if part_number > 0:
        # Search specific part for matching chapter number
        part_pattern = f"{part_number:02d}-*"
        for part_dir in sorted(base_path.glob(part_pattern)):
            if part_dir.is_dir():
                # Look for chapter directories within this part
                chapter_pattern = f"{chapter_number:02d}-*"
                for chapter_dir in sorted(part_dir.glob(chapter_pattern)):
                    if chapter_dir.is_dir():
                        all_chapters.append(chapter_dir)
    else:
        # Search across all parts for matching chapter number
        for part_dir in sorted(base_path.glob(f"[0-9][0-9]-*")):
            if part_dir.is_dir():
                chapter_pattern = f"{chapter_number:02d}-*"
                for chapter_dir in sorted(part_dir.glob(chapter_pattern)):
                    if chapter_dir.is_dir():
                        all_chapters.append(chapter_dir)

    return all_chapters


def is_lesson_file(filename: str) -> bool:
    """
    Check if file is a lesson file (not quiz, summary, or README).

    Includes:
    - NN-lesson-name.md (regular lessons)
    - 00-build-*.md (L00 skill-first lessons)

    Excludes:
    - README.md
    - *.summary.md
    - *quiz.md
    """
    if filename == "README.md":
        return False
    if filename.endswith(".summary.md"):
        return False
    if "quiz" in filename.lower():
        return False
    # Match NN-*.md or 00-build-*.md patterns
    if re.match(r"^\d{2}-.*\.md$", filename):
        return True
    return False


def discover_lessons_in_directory(directory: Path) -> List[Path]:
    """
    Discover all lesson files in a directory.

    Returns sorted list of lesson paths.
    """
    if not directory.exists():
        return []

    lesson_files = []
    for md_file in directory.glob("*.md"):
        if is_lesson_file(md_file.name):
            lesson_files.append(md_file)

    # Sort by lesson number (natural sort)
    return sorted(lesson_files, key=lambda p: p.name)


def discover_lesson_files(scope: ScopeMetadata, base_path: Path) -> Tuple[List[Path], Optional[str]]:
    """
    Discover lesson files based on scope.

    Returns (lesson_files, warning_message)
    """
    lesson_files = []
    warnings = []

    if scope.scope_type == "part":
        # Find all chapters in part
        part_dir = find_part_directory(scope.part_number, base_path)
        if not part_dir:
            return [], f"Part {scope.part_number} not found"

        # Discover lessons from all chapters
        for chapter_dir in sorted(part_dir.glob(f"[0-9][0-9]-*")):
            if chapter_dir.is_dir():
                lessons = discover_lessons_in_directory(chapter_dir)
                lesson_files.extend(lessons)

    elif scope.scope_type == "chapter":
        # Find specific chapter
        if scope.part_number:
            # Specific part + chapter
            part_dir = find_part_directory(scope.part_number, base_path)
            if not part_dir:
                return [], f"Part {scope.part_number} not found"
            chapter_dirs = [
                d for d in part_dir.glob(f"{scope.chapter_number:02d}-*")
                if d.is_dir()
            ]
        else:
            # Chapter number only (search all parts)
            chapter_dirs = find_chapter_directories(0, scope.chapter_number, base_path)

        if not chapter_dirs:
            return [], f"Chapter {scope.chapter_number} not found"

        if len(chapter_dirs) > 1:
            warnings.append(f"⚠️  Found {len(chapter_dirs)} chapters with number {scope.chapter_number}")
            warnings.append("Using first match. Specify 'Chapter X from Part Y' for disambiguation.")

        chapter_dir = chapter_dirs[0]
        lesson_files = discover_lessons_in_directory(chapter_dir)

    elif scope.scope_type == "custom":
        # Custom input (file path or list)
        # Will be handled by caller
        pass

    warning_msg = "\n".join(warnings) if warnings else None
    return lesson_files, warning_msg


def extract_chapter_info(chapter_dir: Path) -> Tuple[int, str]:
    """
    Extract chapter number and name from directory.

    Example: "05-claude-code-features-and-workflows" → (5, "claude-code-features-and-workflows")
    """
    name = chapter_dir.name
    match = re.match(r"(\d+)-(.*)", name)
    if match:
        return int(match.group(1)), match.group(2)
    return 0, name


def extract_part_info(part_dir: Path) -> Tuple[int, str]:
    """
    Extract part number and name from directory.

    Example: "02-AI-Tool-Landscape" → (2, "AI-Tool-Landscape")
    """
    name = part_dir.name
    match = re.match(r"(\d+)-(.*)", name)
    if match:
        return int(match.group(1)), match.group(2)
    return 0, name


def format_discovery_confirmation(lesson_files: List[Path], scope_type: str,
                                   part_number: Optional[int] = None,
                                   chapter_number: Optional[int] = None) -> str:
    """
    Format user-friendly confirmation of discovered files.

    Example output:
    "Found 12 lessons in Chapter 5 (Part 2):
     1. 01-origin-story.md
     2. 02-installation-and-authentication.md
     ...

    Lesson count: 12
    Estimated word count: 45,000
    Estimated questions: 150"
    """
    if not lesson_files:
        return "No lessons found."

    # Scope description
    if scope_type == "part":
        scope_desc = f"Part {part_number}"
    elif scope_type == "chapter":
        scope_desc = f"Chapter {chapter_number}"
    else:
        scope_desc = "Selected scope"

    # Format file list
    file_list = []
    for i, lesson_file in enumerate(lesson_files, 1):
        file_list.append(f"  {i}. {lesson_file.name}")

    # Estimate questions (rough: 8-10 concepts per lesson × 2-3 questions per concept)
    lesson_count = len(lesson_files)
    estimated_questions = min(200, max(50, lesson_count * 12))

    confirmation = f"""Found {lesson_count} lessons in {scope_desc}:

{chr(10).join(file_list)}

Summary:
  Lesson count: {lesson_count}
  Estimated questions: {estimated_questions}

Warning: Large scope (>20 lessons) will generate 200+ questions. Consider splitting by chapter if needed."""

    return confirmation


def get_book_base_path() -> Path:
    """Get the base path for the book structure."""
    current_file = Path(__file__).resolve()
    # Navigate up from: mem/.claude/skills/assessment-architect/scripts/scope_discovery.py
    # To: mem/apps/learn-app/docs/
    # Current: mem/.claude/skills/assessment-architect/scripts/
    # Parents: [scripts (0), assessment-architect (1), skills (2), .claude (3), mem (4), root (5)]
    base = current_file.parents[4] / "apps" / "learn-app" / "docs"

    # Fallback: try absolute path from environment or cwd
    if not base.exists():
        alt_base = Path("/Users/mjs/Documents/code/panaversity-official/tutorsgpt/mem/apps/learn-app/docs")
        if alt_base.exists():
            return alt_base

    return base


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: scope_discovery.py '<scope_input>'")
        print("Examples:")
        print("  'Part 2'")
        print("  'Chapter 5'")
        print("  'Chapter 5 from Part 2'")
        sys.exit(1)

    scope_input = sys.argv[1]
    base_path = get_book_base_path()

    # Parse input
    scope = parse_scope_input(scope_input)
    if scope.error:
        print(f"Error: {scope.error}")
        sys.exit(1)

    # Discover files
    lesson_files, warning = discover_lesson_files(scope, base_path)

    if warning:
        print(warning)

    print(format_discovery_confirmation(lesson_files, scope.scope_type,
                                        scope.part_number, scope.chapter_number))

    # Print file paths for testing
    print("\nFile paths:")
    for f in lesson_files:
        print(f"  {f}")
