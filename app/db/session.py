"""
SQLAlchemy Async Engine and Session Management
"""

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import settings

# Create the Async Engine
engine = create_async_engine(
    settings.ASYNC_DATABASE_URL,
    echo=settings.DEBUG,
    future=True,
)

# Async Session Factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI Dependency that provides an isolated async database session per HTTP request.
    Automatically closes the session after the request finishes.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()