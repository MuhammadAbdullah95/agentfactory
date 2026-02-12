"""Progress dashboard service — aggregates user journey data."""

import logging

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.auth import CurrentUser
from ..models.badge import UserBadge
from ..models.chapter import Chapter, ChapterAlias
from ..models.lesson import LessonCompletion
from ..models.progress import UserProgress
from ..models.quiz import QuizAttempt
from ..schemas.progress import (
    BadgeInfo,
    ChapterInfo,
    LessonInfo,
    ProgressResponse,
    StatsInfo,
    UserInfo,
)
from ..services.engine.badges import BADGE_DEFINITIONS
from .shared import upsert_user_from_jwt

logger = logging.getLogger(__name__)


async def get_progress(
    session: AsyncSession,
    user: CurrentUser,
) -> ProgressResponse:
    """Build full progress dashboard data.

    Queries:
    1. User info (from users table or JWT)
    2. Stats summary (from user_progress, single row)
    3. Badges (from user_badges)
    4. Chapters with quiz attempts and lesson completions
    """
    # Ensure user exists
    db_user = await upsert_user_from_jwt(session, user)
    await session.flush()

    # 1. User info
    user_info = UserInfo(
        display_name=db_user.display_name,
        avatar_url=db_user.avatar_url,
    )

    # 2. Stats summary
    result = await session.execute(select(UserProgress).where(UserProgress.user_id == user.id))
    progress = result.scalar_one_or_none()

    if progress is None:
        stats = StatsInfo(
            total_xp=0,
            quizzes_completed=0,
            perfect_scores=0,
            current_streak=0,
            longest_streak=0,
            lessons_completed=0,
            badge_count=0,
        )
    else:
        stats = StatsInfo(
            total_xp=progress.total_xp,
            quizzes_completed=progress.quizzes_completed,
            perfect_scores=progress.perfect_scores,
            current_streak=progress.current_streak,
            longest_streak=progress.longest_streak,
            lessons_completed=progress.lessons_completed,
            badge_count=progress.badge_count,
        )

    # 3. Badges
    result = await session.execute(
        select(UserBadge).where(UserBadge.user_id == user.id).order_by(UserBadge.earned_at)
    )
    badges = []
    for badge in result.scalars().all():
        badge_def = BADGE_DEFINITIONS.get(badge.badge_id)
        badges.append(
            BadgeInfo(
                id=badge.badge_id,
                name=badge_def.name if badge_def else badge.badge_id,
                earned_at=badge.earned_at,
            )
        )

    # 4. Chapters with quiz attempts and lesson completions
    # Get all chapters the user has interacted with (via quizzes)
    result = await session.execute(
        select(
            ChapterAlias.slug,
            Chapter.title,
            func.max(QuizAttempt.score_pct).label("best_score"),
            func.count(QuizAttempt.id).label("attempts"),
            func.coalesce(func.sum(QuizAttempt.xp_earned), 0).label("xp_earned"),
        )
        .join(Chapter, QuizAttempt.chapter_id == Chapter.id)
        .join(ChapterAlias, Chapter.id == ChapterAlias.chapter_id)
        .where(QuizAttempt.user_id == user.id)
        .group_by(ChapterAlias.slug, Chapter.title)
    )
    chapter_rows = result.all()

    # Get all lesson completions for this user
    result = await session.execute(
        select(LessonCompletion).where(LessonCompletion.user_id == user.id)
    )
    all_lessons = result.scalars().all()

    # Build lesson map by chapter_slug
    lesson_map: dict[str, list[LessonInfo]] = {}
    for lc in all_lessons:
        if lc.chapter_slug not in lesson_map:
            lesson_map[lc.chapter_slug] = []
        lesson_map[lc.chapter_slug].append(
            LessonInfo(
                lesson_slug=lc.lesson_slug,
                active_duration_secs=lc.active_duration_secs,
                completed_at=lc.completed_at,
            )
        )

    chapters = []
    seen_slugs = set()
    for row in chapter_rows:
        slug = row.slug
        seen_slugs.add(slug)
        chapters.append(
            ChapterInfo(
                slug=slug,
                title=row.title,
                best_score=row.best_score,
                attempts=row.attempts,
                xp_earned=row.xp_earned,
                lessons_completed=lesson_map.get(slug, []),
            )
        )

    # Include chapters that have lessons but no quizzes
    for slug, lessons in lesson_map.items():
        if slug not in seen_slugs:
            # Try to get the chapter title
            result = await session.execute(
                select(Chapter.title)
                .join(ChapterAlias, Chapter.id == ChapterAlias.chapter_id)
                .where(ChapterAlias.slug == slug)
            )
            title_row = result.first()
            title = title_row[0] if title_row else slug

            chapters.append(
                ChapterInfo(
                    slug=slug,
                    title=title,
                    best_score=None,
                    attempts=0,
                    xp_earned=0,
                    lessons_completed=lessons,
                )
            )

    return ProgressResponse(
        user=user_info,
        stats=stats,
        badges=badges,
        chapters=chapters,
    )
