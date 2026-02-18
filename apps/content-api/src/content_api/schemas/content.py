"""Pydantic models for content API endpoints."""

from pydantic import BaseModel, Field


class LessonMeta(BaseModel):
    """Metadata for a single lesson in the book tree."""

    slug: str
    title: str
    sidebar_position: int = 0
    has_exercise: bool = False


class ChapterMeta(BaseModel):
    """Metadata for a chapter containing lessons."""

    slug: str
    title: str
    lessons: list[LessonMeta] = Field(default_factory=list)


class PartMeta(BaseModel):
    """Metadata for a part (top-level section) containing chapters."""

    slug: str
    title: str
    chapters: list[ChapterMeta] = Field(default_factory=list)


class BookTreeResponse(BaseModel):
    """Full book tree structure returned by GET /tree."""

    version: str = "1"
    parts: list[PartMeta] = Field(default_factory=list)
    total_lessons: int = 0
    total_chapters: int = 0


class LessonFrontmatter(BaseModel):
    """Parsed YAML frontmatter from a lesson file."""

    title: str = ""
    description: str = ""
    sidebar_position: int = 0
    skills: list[str] = Field(default_factory=list)
    learning_objectives: list[str] = Field(default_factory=list)
    cognitive_load: str = ""
    practice_exercise: str | None = None
    hide_table_of_contents: bool = False


class LessonContentResponse(BaseModel):
    """Full lesson content returned by GET /lesson."""

    chapter_slug: str
    lesson_slug: str
    content: str
    frontmatter: LessonFrontmatter
    credit_charged: bool = False


class CompleteRequest(BaseModel):
    """Request body for POST /complete."""

    chapter_slug: str
    lesson_slug: str
    active_duration_secs: int = Field(ge=0, default=0)


class CompleteResponse(BaseModel):
    """Response for POST /complete."""

    completed: bool = True
    xp_earned: int = 0
