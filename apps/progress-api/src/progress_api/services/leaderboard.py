"""Leaderboard service — reads from materialized view."""

import logging

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.auth import CurrentUser
from ..core.cache import get_cached_leaderboard, set_leaderboard_cache
from ..core.redis import get_redis
from ..schemas.leaderboard import LeaderboardEntry, LeaderboardResponse

logger = logging.getLogger(__name__)

# Maximum entries returned in the leaderboard
TOP_N = 100


async def get_leaderboard(
    session: AsyncSession,
    user: CurrentUser,
) -> LeaderboardResponse:
    """Fetch leaderboard from materialized view (or cache).

    Steps:
    1. Check Redis cache for leaderboard data
    2. If cache miss, query materialized view for top N
    3. Find current user's rank (even if not in top N)
    4. Cache the result
    """
    redis = get_redis()

    # 1. Check cache
    cached = await get_cached_leaderboard(redis)
    if cached is not None:
        # Still need to find current user's rank
        current_user_rank = None
        for entry in cached:
            if entry["user_id"] == user.id:
                current_user_rank = entry["rank"]
                break

        if current_user_rank is None:
            current_user_rank = await _get_user_rank(session, user.id)

        return LeaderboardResponse(
            entries=[LeaderboardEntry(**e) for e in cached],
            current_user_rank=current_user_rank,
            total_users=len(cached),
        )

    # 2. Query materialized view for top N
    result = await session.execute(
        text(
            "SELECT id, display_name, avatar_url, total_xp, rank, badge_count"
            " FROM leaderboard"
            " ORDER BY rank ASC"
            " LIMIT :limit"
        ),
        {"limit": TOP_N},
    )
    rows = result.all()

    entries = []
    current_user_rank = None
    for row in rows:
        entry = LeaderboardEntry(
            rank=row.rank,
            user_id=row.id,
            display_name=row.display_name,
            avatar_url=row.avatar_url,
            total_xp=row.total_xp,
            badge_count=row.badge_count,
        )
        entries.append(entry)
        if row.id == user.id:
            current_user_rank = row.rank

    # 3. If current user not in top N, find their rank separately
    if current_user_rank is None:
        current_user_rank = await _get_user_rank(session, user.id)

    total_users = len(entries)

    # 4. Cache the entries (not the user-specific rank)
    entry_dicts = [e.model_dump() for e in entries]
    await set_leaderboard_cache(redis, entry_dicts)

    return LeaderboardResponse(
        entries=entries,
        current_user_rank=current_user_rank,
        total_users=total_users,
    )


async def _get_user_rank(session: AsyncSession, user_id: str) -> int | None:
    """Get a specific user's rank from the materialized view."""
    result = await session.execute(
        text("SELECT rank FROM leaderboard WHERE id = :user_id"),
        {"user_id": user_id},
    )
    row = result.first()
    return row.rank if row else None


async def refresh_leaderboard(session: AsyncSession) -> None:
    """Refresh the materialized view concurrently.

    Called by the background scheduler.
    CONCURRENTLY allows reads during refresh (requires unique index).
    """
    await session.execute(text("REFRESH MATERIALIZED VIEW CONCURRENTLY leaderboard"))
    await session.commit()
    logger.info("[Leaderboard] Materialized view refreshed")
