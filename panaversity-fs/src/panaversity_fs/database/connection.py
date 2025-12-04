"""Async database connection management for PanaversityFS."""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
    AsyncEngine,
)

from ..config import get_config
from .models import Base


_engine: AsyncEngine | None = None
_session_factory: async_sessionmaker[AsyncSession] | None = None


def get_engine() -> AsyncEngine:
    """Get or create the async engine singleton.

    Returns:
        AsyncEngine: SQLAlchemy async engine configured from environment.
    """
    global _engine
    if _engine is None:
        config = get_config()
        _engine = create_async_engine(
            config.effective_database_url,
            echo=config.log_level == "DEBUG",
            pool_pre_ping=True,
        )
    return _engine


def get_session_factory() -> async_sessionmaker[AsyncSession]:
    """Get or create the session factory singleton.

    Returns:
        async_sessionmaker: Factory for creating AsyncSession instances.
    """
    global _session_factory
    if _session_factory is None:
        _session_factory = async_sessionmaker(
            get_engine(),
            class_=AsyncSession,
            expire_on_commit=False,
        )
    return _session_factory


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Get an async database session with automatic cleanup.

    Yields:
        AsyncSession: Database session that commits on success, rolls back on error.

    Example:
        async with get_session() as session:
            result = await session.execute(select(FileJournal))
            # Auto-commits on exit, rolls back on exception
    """
    factory = get_session_factory()
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise


async def init_db() -> None:
    """Initialize database tables (for development/testing).

    Creates all tables defined in models.py if they don't exist.
    For production, use Alembic migrations instead.
    """
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def reset_engine() -> None:
    """Reset the engine singleton (for testing).

    Call this between tests to ensure clean state.
    """
    global _engine, _session_factory
    if _engine is not None:
        await _engine.dispose()
        _engine = None
    _session_factory = None
