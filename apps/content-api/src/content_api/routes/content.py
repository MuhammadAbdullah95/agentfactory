"""Content API routes: tree, lesson, complete."""

import logging
import uuid

from api_infra.auth import CurrentUser, get_current_user
from api_infra.core.rate_limit import rate_limit
from api_infra.core.redis_cache import get_redis
from fastapi import APIRouter, Depends, HTTPException, Request, Response

from ..metering.client import get_metering_client
from ..schemas.content import (
    BookTreeResponse,
    CompleteRequest,
    CompleteResponse,
    LessonContentResponse,
    LessonFrontmatter,
)
from ..services.book_tree import build_book_tree
from ..services.content_loader import load_lesson_content, parse_frontmatter
from ..services.progress_client import get_progress_client

logger = logging.getLogger(__name__)

content_router = APIRouter(prefix="/api/v1/content", tags=["content"])


@content_router.get("/tree", response_model=BookTreeResponse)
@rate_limit("content_tree", max_requests=10, period_minutes=1)
async def get_tree(
    request: Request,
    response: Response,
    user: CurrentUser = Depends(get_current_user),
) -> BookTreeResponse:
    """Get the full book tree structure."""
    logger.info(f"[Tree] User {user.id} requesting book tree")
    return await build_book_tree()


@content_router.get("/lesson", response_model=LessonContentResponse)
@rate_limit("content_lesson", max_requests=30, period_minutes=1)
async def get_lesson(
    request: Request,
    response: Response,
    chapter: str,
    lesson: str,
    user: CurrentUser = Depends(get_current_user),
) -> LessonContentResponse:
    """Get lesson content with frontmatter and optional metering."""
    logger.info(f"[Lesson] User {user.id}: {chapter}/{lesson}")

    credit_charged = False
    reservation_id: str | None = None
    request_id = str(uuid.uuid4())

    # Idempotency check: content-access:{user_id}:{chapter}:{lesson} (1h TTL)
    redis = get_redis()
    idempotency_key = f"content-access:{user.id}:{chapter}:{lesson}"
    already_accessed = False

    if redis:
        try:
            existing = await redis.get(idempotency_key)
            if existing:
                already_accessed = True
                logger.info(f"[Lesson] Idempotent hit: {idempotency_key}")
        except Exception as e:
            logger.warning(f"[Lesson] Redis idempotency check failed: {e}")

    # Metering check (only if not already accessed and metering enabled)
    metering = get_metering_client()
    if metering and not already_accessed:
        try:
            auth_token = request.headers.get("Authorization")
            check_result = await metering.check(
                user_id=user.id,
                request_id=request_id,
                estimated_tokens=1,
                model="content-access",
                lesson_path=f"{chapter}/{lesson}",
                auth_token=auth_token,
            )

            if not check_result.get("allowed", True):
                error_code = check_result.get("error_code", "UNKNOWN")
                message = check_result.get("message", "Access denied")

                if error_code == "INSUFFICIENT_BALANCE":
                    raise HTTPException(status_code=402, detail=message)
                elif error_code == "ACCOUNT_SUSPENDED":
                    raise HTTPException(status_code=403, detail=message)
                elif error_code == "REQUEST_ID_CONFLICT":
                    raise HTTPException(status_code=409, detail=message)
                else:
                    raise HTTPException(status_code=402, detail=message)

            reservation_id = check_result.get("reservation_id")
            credit_charged = True

        except HTTPException:
            raise
        except Exception as e:
            # Fail-open: if metering is down, serve content anyway
            logger.error(f"[Lesson] Metering check failed (fail-open): {e}")

    # Load content
    try:
        result = await load_lesson_content(chapter, lesson)
    except Exception as e:
        logger.error(f"[Lesson] Content load failed: {e}")
        # Release reservation if content load fails
        if reservation_id and metering:
            try:
                auth_token = request.headers.get("Authorization")
                await metering.release(
                    user_id=user.id,
                    request_id=request_id,
                    reservation_id=reservation_id,
                    auth_token=auth_token,
                )
                credit_charged = False
            except Exception as release_err:
                logger.error(f"[Lesson] Release failed: {release_err}")
        raise HTTPException(status_code=500, detail="Failed to load content")

    if not result.get("found", False):
        # Release reservation if content not found
        if reservation_id and metering:
            try:
                auth_token = request.headers.get("Authorization")
                await metering.release(
                    user_id=user.id,
                    request_id=request_id,
                    reservation_id=reservation_id,
                    auth_token=auth_token,
                )
                credit_charged = False
            except Exception as release_err:
                logger.error(f"[Lesson] Release failed: {release_err}")
        raise HTTPException(status_code=404, detail=f"Lesson not found: {chapter}/{lesson}")

    # Finalize metering deduction
    if reservation_id and metering and credit_charged:
        try:
            auth_token = request.headers.get("Authorization")
            await metering.deduct(
                user_id=user.id,
                request_id=request_id,
                reservation_id=reservation_id,
                input_tokens=0,
                output_tokens=0,
                model="content-access",
                lesson_path=f"{chapter}/{lesson}",
                auth_token=auth_token,
            )
        except Exception as e:
            logger.error(f"[Lesson] Metering deduct failed: {e}")

    # Set idempotency key (1 hour TTL)
    if redis and not already_accessed:
        try:
            await redis.setex(idempotency_key, 3600, "1")
        except Exception as e:
            logger.warning(f"[Lesson] Redis idempotency set failed: {e}")

    # Parse frontmatter
    frontmatter_dict = result.get("frontmatter_dict", {})
    try:
        frontmatter = LessonFrontmatter(**frontmatter_dict)
    except Exception:
        frontmatter = LessonFrontmatter()

    return LessonContentResponse(
        chapter_slug=chapter,
        lesson_slug=lesson,
        content=result["content"],
        frontmatter=frontmatter,
        credit_charged=credit_charged,
    )


@content_router.post("/complete", response_model=CompleteResponse)
@rate_limit("content_complete", max_requests=30, period_minutes=1)
async def complete_lesson(
    request: Request,
    response: Response,
    body: CompleteRequest,
    user: CurrentUser = Depends(get_current_user),
) -> CompleteResponse:
    """Record lesson completion."""
    logger.info(f"[Complete] User {user.id}: {body.chapter_slug}/{body.lesson_slug}")

    progress = get_progress_client()
    if not progress:
        raise HTTPException(
            status_code=503,
            detail="Progress tracking service not configured",
        )

    auth_token = request.headers.get("Authorization")
    result = await progress.complete_lesson(
        chapter_slug=body.chapter_slug,
        lesson_slug=body.lesson_slug,
        active_duration_secs=body.active_duration_secs,
        auth_token=auth_token,
    )

    return CompleteResponse(
        completed=result.get("completed", False),
        xp_earned=result.get("xp_earned", 0),
    )
