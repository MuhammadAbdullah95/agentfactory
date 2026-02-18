"""E2E tests for progress tracking integration.

POST /api/v1/content/complete calls an external progress API via HTTP.
These tests exercise the real ProgressClient HTTP flow, mocked at the
transport level by respx.
"""

import json

from .conftest import auth_header

# ═══════════════════════════════════════════════════════════════════════════
# Progress API configured — completion works
# ═══════════════════════════════════════════════════════════════════════════


class TestProgressComplete:
    """Progress API is configured and healthy."""

    async def test_complete_returns_xp(self, client, make_token, enable_progress):
        """Successful completion returns completed=True and XP earned."""
        token = make_token()

        resp = await client.post(
            "/api/v1/content/complete",
            json={
                "chapter_slug": "01-intro",
                "lesson_slug": "01-welcome",
                "active_duration_secs": 120,
            },
            headers=auth_header(token),
        )

        assert resp.status_code == 200
        data = resp.json()
        assert data["completed"] is True
        assert data["xp_earned"] == 10

    async def test_complete_forwards_auth_to_progress_api(
        self, client, make_token, enable_progress
    ):
        """The Bearer token should be forwarded to the progress API."""
        token = make_token()

        await client.post(
            "/api/v1/content/complete",
            json={
                "chapter_slug": "01-intro",
                "lesson_slug": "01-welcome",
                "active_duration_secs": 60,
            },
            headers=auth_header(token),
        )

        assert enable_progress["complete"].called
        last_request = enable_progress["complete"].calls.last.request
        assert "Bearer" in last_request.headers.get("Authorization", "")

    async def test_complete_sends_lesson_payload(
        self, client, make_token, enable_progress
    ):
        """Progress API receives the correct chapter/lesson slugs."""
        token = make_token()

        await client.post(
            "/api/v1/content/complete",
            json={
                "chapter_slug": "02-basics",
                "lesson_slug": "01-first-steps",
                "active_duration_secs": 300,
            },
            headers=auth_header(token),
        )

        last_request = enable_progress["complete"].calls.last.request
        body = json.loads(last_request.content)
        assert body["chapter_slug"] == "02-basics"
        assert body["lesson_slug"] == "01-first-steps"
        assert body["active_duration_secs"] == 300


# ═══════════════════════════════════════════════════════════════════════════
# Progress API not configured — 503
# ═══════════════════════════════════════════════════════════════════════════


class TestProgressUnavailable:
    """Progress API not configured (default state)."""

    async def test_complete_503_when_not_configured(self, client, make_token):
        """Without progress API URL, complete returns 503."""
        token = make_token()

        resp = await client.post(
            "/api/v1/content/complete",
            json={
                "chapter_slug": "01-intro",
                "lesson_slug": "01-welcome",
                "active_duration_secs": 0,
            },
            headers=auth_header(token),
        )

        assert resp.status_code == 503
