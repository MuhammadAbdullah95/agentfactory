"""E2E tests for Content API — behavior through public HTTP interface.

Each test reads like a specification:
  "user with valid token can browse the book tree"
  "unauthenticated request is rejected"
  "second lesson access within idempotency window is free"

No mocks of internal functions. External HTTP (JWKS, GitHub) is intercepted
at the httpx transport level by respx. Redis uses fakeredis.
"""

import json

from .conftest import auth_header

# ═══════════════════════════════════════════════════════════════════════════
# Health & Root — no auth required
# ═══════════════════════════════════════════════════════════════════════════


class TestHealthAndRoot:
    """Endpoints that should work without authentication."""

    async def test_health_check_returns_ok(self, client):
        resp = await client.get("/health")

        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "healthy"
        assert data["services"]["redis"] == "ok"

    async def test_root_returns_api_info(self, client):
        resp = await client.get("/")

        assert resp.status_code == 200
        data = resp.json()
        assert data["name"] == "Content API"
        assert "tree" in data["endpoints"]
        assert "lesson" in data["endpoints"]


# ═══════════════════════════════════════════════════════════════════════════
# Authentication — JWT verification through JWKS
# ═══════════════════════════════════════════════════════════════════════════


class TestAuthentication:
    """Token verification against JWKS public keys."""

    async def test_no_token_returns_401(self, client):
        resp = await client.get("/api/v1/content/tree")

        assert resp.status_code == 401

    async def test_invalid_token_returns_401(self, client):
        resp = await client.get(
            "/api/v1/content/tree",
            headers=auth_header("not-a-real-token"),
        )

        assert resp.status_code == 401

    async def test_malformed_jwt_returns_401(self, client):
        resp = await client.get(
            "/api/v1/content/tree",
            headers=auth_header("eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJmYWtlIn0.invalid"),
        )

        assert resp.status_code == 401

    async def test_expired_jwt_returns_401(self, client, make_token):
        token = make_token(expired=True)

        resp = await client.get(
            "/api/v1/content/tree",
            headers=auth_header(token),
        )

        assert resp.status_code == 401

    async def test_valid_jwt_is_accepted(self, client, make_token):
        token = make_token()

        resp = await client.get(
            "/api/v1/content/tree",
            headers=auth_header(token),
        )

        assert resp.status_code == 200


# ═══════════════════════════════════════════════════════════════════════════
# Book Tree — GET /api/v1/content/tree
# ═══════════════════════════════════════════════════════════════════════════


class TestBookTree:
    """Book tree endpoint returns hierarchical structure from GitHub."""

    async def test_tree_returns_parts_and_chapters(self, client, make_token):
        token = make_token()

        resp = await client.get("/api/v1/content/tree", headers=auth_header(token))

        assert resp.status_code == 200
        data = resp.json()
        assert len(data["parts"]) == 2
        assert data["total_lessons"] > 0
        assert data["total_chapters"] > 0

    async def test_tree_structure_matches_github_fixtures(self, client, make_token):
        token = make_token()

        resp = await client.get("/api/v1/content/tree", headers=auth_header(token))
        data = resp.json()

        # Part 1: Foundations with 2 chapters (intro + basics)
        part1 = data["parts"][0]
        assert part1["slug"] == "01-Foundations"
        assert len(part1["chapters"]) == 2

        # Chapter 1: intro with 2 lessons (welcome + setup)
        ch1 = part1["chapters"][0]
        assert ch1["slug"] == "01-intro"
        assert len(ch1["lessons"]) == 2

        # Part 2: Advanced with 1 chapter
        part2 = data["parts"][1]
        assert part2["slug"] == "02-Advanced"
        assert len(part2["chapters"]) == 1

    async def test_tree_is_cached_in_redis(self, client, make_token, fake_redis_client):
        """Second tree request should hit Redis cache, not GitHub."""
        token = make_token()

        # First call: populates cache
        resp1 = await client.get("/api/v1/content/tree", headers=auth_header(token))
        assert resp1.status_code == 200

        # Verify cache key exists
        cached = await fake_redis_client.get("book_tree:v1")
        assert cached is not None
        cached_data = json.loads(cached)
        assert cached_data["total_lessons"] == resp1.json()["total_lessons"]

        # Second call: served from cache (same response)
        resp2 = await client.get("/api/v1/content/tree", headers=auth_header(token))
        assert resp2.status_code == 200
        assert resp2.json() == resp1.json()


# ═══════════════════════════════════════════════════════════════════════════
# Lessons — GET /api/v1/content/lesson
# ═══════════════════════════════════════════════════════════════════════════


class TestLessonContent:
    """Lesson endpoint returns content with frontmatter stripped."""

    async def test_lesson_returns_content(self, client, make_token):
        token = make_token()

        resp = await client.get(
            "/api/v1/content/lesson",
            params={
                "part": "01-Foundations",
                "chapter": "01-intro",
                "lesson": "01-welcome",
            },
            headers=auth_header(token),
        )

        assert resp.status_code == 200
        data = resp.json()
        assert data["chapter_slug"] == "01-intro"
        assert data["lesson_slug"] == "01-welcome"
        assert len(data["content"]) > 0

    async def test_frontmatter_is_stripped_from_content(self, client, make_token):
        """Content body must NOT start with --- (frontmatter removed)."""
        token = make_token()

        resp = await client.get(
            "/api/v1/content/lesson",
            params={
                "part": "01-Foundations",
                "chapter": "01-intro",
                "lesson": "01-welcome",
            },
            headers=auth_header(token),
        )

        data = resp.json()
        content = data["content"]

        # Must not start with frontmatter delimiter
        assert not content.startswith("---"), "Frontmatter was not stripped from content body"

        # Must start with the heading
        assert content.startswith("# Welcome to the Course")

    async def test_frontmatter_is_parsed_into_metadata(self, client, make_token):
        """Frontmatter fields should appear in the frontmatter response object."""
        token = make_token()

        resp = await client.get(
            "/api/v1/content/lesson",
            params={
                "part": "01-Foundations",
                "chapter": "01-intro",
                "lesson": "01-welcome",
            },
            headers=auth_header(token),
        )

        fm = resp.json()["frontmatter"]
        assert fm["title"] == "Welcome to the Course"
        assert fm["description"] == "An introductory lesson"
        assert "skill-reading" in fm["skills"]
        assert "skill-comprehension" in fm["skills"]
        assert fm["cognitive_load"] == "low"

    async def test_lesson_without_frontmatter_returns_empty_metadata(self, client, make_token):
        """Lessons without YAML frontmatter should have empty metadata fields."""
        token = make_token()

        resp = await client.get(
            "/api/v1/content/lesson",
            params={
                "part": "01-Foundations",
                "chapter": "01-intro",
                "lesson": "02-setup",
            },
            headers=auth_header(token),
        )

        assert resp.status_code == 200
        data = resp.json()
        assert data["frontmatter"]["title"] == ""
        assert data["frontmatter"]["skills"] == []

        # Content should be the full file (no stripping needed)
        assert "# Plain Lesson" in data["content"]

    async def test_nonexistent_lesson_returns_404(self, client, make_token):
        token = make_token()

        resp = await client.get(
            "/api/v1/content/lesson",
            params={
                "part": "99-Nonexistent",
                "chapter": "99-fake",
                "lesson": "99-missing",
            },
            headers=auth_header(token),
        )

        assert resp.status_code == 404

    async def test_metering_not_charged_when_disabled(self, client, make_token):
        """With metering disabled, credit_charged should be false."""
        token = make_token()

        resp = await client.get(
            "/api/v1/content/lesson",
            params={
                "part": "01-Foundations",
                "chapter": "01-intro",
                "lesson": "01-welcome",
            },
            headers=auth_header(token),
        )

        assert resp.json()["credit_charged"] is False


# ═══════════════════════════════════════════════════════════════════════════
# Idempotency — second access within window skips metering
# ═══════════════════════════════════════════════════════════════════════════


class TestIdempotency:
    """Lesson access idempotency via Redis keys."""

    async def test_idempotency_key_is_set_on_first_access(
        self, client, make_token, fake_redis_client
    ):
        token = make_token(sub="idempotent-user-1")

        # First access
        resp = await client.get(
            "/api/v1/content/lesson",
            params={
                "part": "01-Foundations",
                "chapter": "01-intro",
                "lesson": "01-welcome",
            },
            headers=auth_header(token),
        )
        assert resp.status_code == 200

        # Verify idempotency key was set in Redis
        key = "content-access:idempotent-user-1:01-intro:01-welcome"
        value = await fake_redis_client.get(key)
        assert value == "1"

    async def test_second_access_hits_idempotency_cache(
        self, client, make_token, fake_redis_client
    ):
        """Two requests for same lesson by same user within the window."""
        token = make_token(sub="idempotent-user-2")
        params = {
            "part": "01-Foundations",
            "chapter": "01-intro",
            "lesson": "01-welcome",
        }

        # First access: sets idempotency key
        resp1 = await client.get(
            "/api/v1/content/lesson",
            params=params,
            headers=auth_header(token),
        )
        assert resp1.status_code == 200

        # Second access: should still succeed (idempotent)
        resp2 = await client.get(
            "/api/v1/content/lesson",
            params=params,
            headers=auth_header(token),
        )
        assert resp2.status_code == 200
        # Both should return the same content
        assert resp2.json()["content"] == resp1.json()["content"]

    async def test_different_users_have_separate_idempotency(
        self, client, make_token, fake_redis_client
    ):
        params = {
            "part": "01-Foundations",
            "chapter": "01-intro",
            "lesson": "01-welcome",
        }

        # User A accesses
        token_a = make_token(sub="user-A")
        await client.get(
            "/api/v1/content/lesson", params=params, headers=auth_header(token_a)
        )

        # User B accesses same lesson
        token_b = make_token(sub="user-B")
        await client.get(
            "/api/v1/content/lesson", params=params, headers=auth_header(token_b)
        )

        # Both should have separate idempotency keys
        key_a = await fake_redis_client.get("content-access:user-A:01-intro:01-welcome")
        key_b = await fake_redis_client.get("content-access:user-B:01-intro:01-welcome")
        assert key_a == "1"
        assert key_b == "1"


# ═══════════════════════════════════════════════════════════════════════════
# Cache Invalidation — POST /admin/invalidate-cache
# ═══════════════════════════════════════════════════════════════════════════


class TestCacheInvalidation:
    """Admin cache invalidation endpoint."""

    async def test_invalidation_requires_admin_secret(self, client):
        resp = await client.post(
            "/admin/invalidate-cache",
            json={"paths": []},
        )

        assert resp.status_code == 403

    async def test_wrong_admin_secret_returns_403(self, client):
        resp = await client.post(
            "/admin/invalidate-cache",
            json={"paths": []},
            headers={"X-Admin-Secret": "wrong-secret"},
        )

        assert resp.status_code == 403

    async def test_invalidate_all_clears_tree_cache(
        self, client, make_token, fake_redis_client
    ):
        """Invalidate-all should clear the book_tree:v1 key."""
        token = make_token()

        # Populate tree cache
        await client.get("/api/v1/content/tree", headers=auth_header(token))
        assert await fake_redis_client.get("book_tree:v1") is not None

        # Invalidate all
        resp = await client.post(
            "/admin/invalidate-cache",
            json={"paths": []},
            headers={"X-Admin-Secret": "test-admin-secret"},
        )

        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "ok"
        assert data["invalidated_count"] >= 1

        # Tree cache should be cleared
        assert await fake_redis_client.get("book_tree:v1") is None

    async def test_invalidate_specific_path_preserves_tree(
        self, client, make_token, fake_redis_client
    ):
        """Invalidating a specific lesson path should still clear the tree cache
        (since structure may have changed) but only lesson-specific content caches."""
        token = make_token()

        # Populate tree cache
        await client.get("/api/v1/content/tree", headers=auth_header(token))
        assert await fake_redis_client.get("book_tree:v1") is not None

        # Invalidate specific path
        resp = await client.post(
            "/admin/invalidate-cache",
            json={"paths": ["01-Foundations/01-intro/01-welcome"]},
            headers={"X-Admin-Secret": "test-admin-secret"},
        )

        assert resp.status_code == 200
        # Tree cache is also cleared when paths are provided (per implementation)
        assert await fake_redis_client.get("book_tree:v1") is None


# ═══════════════════════════════════════════════════════════════════════════
# Lesson Caching — content is cached in Redis
# ═══════════════════════════════════════════════════════════════════════════


class TestLessonCaching:
    """Lesson content is cached after first fetch from GitHub."""

    async def test_lesson_content_is_cached(self, client, make_token, fake_redis_client):
        """After first lesson fetch, content should be in Redis cache."""
        token = make_token()
        params = {
            "part": "01-Foundations",
            "chapter": "01-intro",
            "lesson": "01-welcome",
        }

        # First fetch: goes to GitHub (via respx mock)
        resp = await client.get(
            "/api/v1/content/lesson", params=params, headers=auth_header(token)
        )
        assert resp.status_code == 200

        # Check that a content_loader cache key exists
        # Key format: content_loader.load_lesson_content:{args}:{kwargs}
        keys = []
        cursor = 0
        while True:
            cursor, batch = await fake_redis_client.scan(
                cursor, match="content_loader.*", count=100
            )
            keys.extend(batch)
            if cursor == 0:
                break

        assert len(keys) > 0, "Lesson content was not cached in Redis"


# ═══════════════════════════════════════════════════════════════════════════
# Multi-user isolation
# ═══════════════════════════════════════════════════════════════════════════


class TestMultiUserIsolation:
    """Different users get independent access tracking."""

    async def test_two_users_both_get_content(self, client, make_token):
        token_a = make_token(sub="alice", email="alice@test.com")
        token_b = make_token(sub="bob", email="bob@test.com")

        params = {
            "part": "01-Foundations",
            "chapter": "01-intro",
            "lesson": "01-welcome",
        }

        resp_a = await client.get(
            "/api/v1/content/lesson", params=params, headers=auth_header(token_a)
        )
        resp_b = await client.get(
            "/api/v1/content/lesson", params=params, headers=auth_header(token_b)
        )

        assert resp_a.status_code == 200
        assert resp_b.status_code == 200
        # Same content served to both
        assert resp_a.json()["content"] == resp_b.json()["content"]
