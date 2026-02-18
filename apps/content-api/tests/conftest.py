"""Shared test fixtures for Content API tests."""

import asyncio
import os
from unittest.mock import AsyncMock, MagicMock

import pytest

# Set test environment variables before importing app modules
os.environ["DEV_MODE"] = "true"
os.environ["REDIS_URL"] = ""
os.environ["ALLOWED_ORIGINS"] = "http://localhost:3000,http://test.com"


@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for async tests."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True)
def _configure_api_infra():
    """Configure api_infra with mock settings for every test."""
    import api_infra
    from api_infra.core import redis_cache

    mock_settings = MagicMock()
    mock_settings.sso_url = "https://sso.example.com"
    mock_settings.dev_mode = True
    mock_settings.dev_user_id = "dev-user-123"
    mock_settings.dev_user_email = "dev@localhost"
    mock_settings.dev_user_name = "Dev User"
    mock_settings.redis_url = ""
    mock_settings.redis_password = ""
    mock_settings.redis_max_connections = 10
    mock_settings.content_cache_ttl = 2592000

    api_infra.configure(mock_settings)

    yield

    redis_cache._aredis = None


@pytest.fixture
def mock_redis():
    """Mock Redis client for testing."""
    mock = AsyncMock()
    mock.ping = AsyncMock(return_value=True)
    mock.get = AsyncMock(return_value=None)
    mock.setex = AsyncMock(return_value=True)
    mock.evalsha = AsyncMock(return_value=[1, 60000, 0])
    mock.script_load = AsyncMock(return_value="mock_sha")
    mock.aclose = AsyncMock()
    return mock
