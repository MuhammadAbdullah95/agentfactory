"""Tests for authentication."""

from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException
from httpx import AsyncClient

from progress_api.config import settings
from progress_api.core.auth import get_current_user


@pytest.mark.asyncio
async def test_dev_mode_x_user_id_header(client: AsyncClient):
    """Dev mode: X-User-ID header is used as user identity."""
    response = await client.get("/health", headers={"X-User-ID": "test-user-42"})
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_production_mode_missing_auth_header():
    """Production mode: missing Authorization header returns 401."""
    original_dev_mode = settings.dev_mode
    settings.dev_mode = False

    try:
        request = MagicMock()
        request.headers = {}

        with pytest.raises(HTTPException) as exc_info:
            await get_current_user(request)
        assert exc_info.value.status_code == 401
        assert "Missing Authorization header" in exc_info.value.detail
    finally:
        settings.dev_mode = original_dev_mode


@pytest.mark.asyncio
async def test_production_mode_invalid_token_format():
    """Production mode: invalid token format returns 401."""
    original_dev_mode = settings.dev_mode
    settings.dev_mode = False

    try:
        request = MagicMock()
        request.headers = {"Authorization": "Bearer not-a-jwt"}

        with pytest.raises(HTTPException) as exc_info:
            await get_current_user(request)
        assert exc_info.value.status_code == 401
        assert "Invalid token format" in exc_info.value.detail
    finally:
        settings.dev_mode = original_dev_mode


@pytest.mark.asyncio
async def test_production_mode_expired_token():
    """Production mode: expired/invalid JWT returns 401."""
    original_dev_mode = settings.dev_mode
    original_sso_url = settings.sso_url
    settings.dev_mode = False
    settings.sso_url = "http://localhost:9999"  # Non-existent SSO

    try:
        # A properly formatted but invalid JWT (3 parts separated by dots)
        fake_jwt = (
            "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InRlc3QifQ"
            ".eyJzdWIiOiJ0ZXN0In0"
            ".fake_signature"
        )
        request = MagicMock()
        request.headers = {"Authorization": f"Bearer {fake_jwt}"}

        with pytest.raises(HTTPException) as exc_info:
            await get_current_user(request)
        # Either 401 (JWT verification failed) or 503 (can't reach SSO)
        assert exc_info.value.status_code in (401, 503)
    finally:
        settings.dev_mode = original_dev_mode
        settings.sso_url = original_sso_url
