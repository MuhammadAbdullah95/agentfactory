"""Integration tests for GET /api/v1/leaderboard."""

import pytest
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


async def _submit_quiz(client: AsyncClient, user_id: str, score: int) -> None:
    """Helper: submit a quiz for a given user."""
    await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "score_pct": score,
            "questions_correct": int(score * 15 / 100),
            "questions_total": 15,
        },
        headers={"X-User-ID": user_id},
    )


async def _refresh_view(test_session: AsyncSession) -> None:
    """Helper: refresh leaderboard materialized view."""
    await test_session.execute(text("REFRESH MATERIALIZED VIEW CONCURRENTLY leaderboard"))
    await test_session.commit()


@pytest.mark.asyncio
async def test_leaderboard_empty(client: AsyncClient, test_session: AsyncSession):
    """Empty leaderboard returns empty entries list."""
    # Refresh view so it reflects current (empty) state
    await _refresh_view(test_session)

    response = await client.get(
        "/api/v1/leaderboard",
        headers={"X-User-ID": "test-lb-empty"},
    )
    assert response.status_code == 200
    data = response.json()

    assert data["entries"] == []
    assert data["current_user_rank"] is None
    assert data["total_users"] == 0


@pytest.mark.asyncio
async def test_leaderboard_ranked_by_xp(client: AsyncClient, test_session: AsyncSession):
    """Users ranked by total XP descending."""
    # Create users with different scores
    await _submit_quiz(client, "lb-user-low", 50)
    await _submit_quiz(client, "lb-user-mid", 75)
    await _submit_quiz(client, "lb-user-high", 95)

    # Refresh materialized view
    await _refresh_view(test_session)

    response = await client.get(
        "/api/v1/leaderboard",
        headers={"X-User-ID": "lb-user-mid"},
    )
    assert response.status_code == 200
    data = response.json()

    assert len(data["entries"]) == 3
    # Verify ordering: highest XP first
    assert data["entries"][0]["total_xp"] >= data["entries"][1]["total_xp"]
    assert data["entries"][1]["total_xp"] >= data["entries"][2]["total_xp"]

    # Verify rank values
    assert data["entries"][0]["rank"] == 1
    assert data["entries"][0]["user_id"] == "lb-user-high"


@pytest.mark.asyncio
async def test_leaderboard_current_user_rank(client: AsyncClient, test_session: AsyncSession):
    """Current user's rank is included in response."""
    await _submit_quiz(client, "lb-rank-1", 90)
    await _submit_quiz(client, "lb-rank-2", 60)
    await _refresh_view(test_session)

    # Request as the lower-ranked user
    response = await client.get(
        "/api/v1/leaderboard",
        headers={"X-User-ID": "lb-rank-2"},
    )
    assert response.status_code == 200
    data = response.json()

    assert data["current_user_rank"] == 2


@pytest.mark.asyncio
async def test_leaderboard_excludes_opted_out_user(client: AsyncClient, test_session: AsyncSession):
    """User with show_on_leaderboard=False is excluded."""
    # Create a user who opts out
    await _submit_quiz(client, "lb-opted-out", 80)
    await _submit_quiz(client, "lb-visible", 70)

    # Opt out the user directly in the database
    await test_session.execute(
        text("UPDATE users SET show_on_leaderboard = FALSE WHERE id = :uid"),
        {"uid": "lb-opted-out"},
    )
    await test_session.commit()

    # Refresh materialized view
    await _refresh_view(test_session)

    response = await client.get(
        "/api/v1/leaderboard",
        headers={"X-User-ID": "lb-visible"},
    )
    assert response.status_code == 200
    data = response.json()

    user_ids = [e["user_id"] for e in data["entries"]]
    assert "lb-opted-out" not in user_ids
    assert "lb-visible" in user_ids


@pytest.mark.asyncio
async def test_leaderboard_response_shape(client: AsyncClient, test_session: AsyncSession):
    """Response has correct structure."""
    await _submit_quiz(client, "lb-shape-user", 85)
    await _refresh_view(test_session)

    response = await client.get(
        "/api/v1/leaderboard",
        headers={"X-User-ID": "lb-shape-user"},
    )
    assert response.status_code == 200
    data = response.json()

    assert "entries" in data
    assert "current_user_rank" in data
    assert "total_users" in data

    entry = data["entries"][0]
    assert "rank" in entry
    assert "user_id" in entry
    assert "display_name" in entry
    assert "avatar_url" in entry
    assert "total_xp" in entry
    assert "badge_count" in entry


@pytest.mark.asyncio
async def test_leaderboard_requires_auth(client: AsyncClient):
    """Missing auth header returns 401."""
    from progress_api.config import settings

    original_dev_mode = settings.dev_mode
    settings.dev_mode = False

    try:
        response = await client.get("/api/v1/leaderboard")
        assert response.status_code == 401
    finally:
        settings.dev_mode = original_dev_mode
