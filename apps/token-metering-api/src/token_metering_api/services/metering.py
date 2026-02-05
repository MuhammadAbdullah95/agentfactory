"""Core metering service with v5 balance-only model.

v5 Logic:
1. Suspended? → BLOCK (ACCOUNT_SUSPENDED)
2. Expired (inactive 365+ days)? → BLOCK (INSUFFICIENT_BALANCE, is_expired=true)
3. available_balance >= estimated_tokens? → ALLOW (create reservation)
4. Otherwise → BLOCK (INSUFFICIENT_BALANCE)

Balance is stored directly on TokenAccount (not computed from allocations).
Reservations use Redis sorted set with Lua scripts for atomicity.
Deduction is simple: account.balance -= tokens_used
"""

import logging
import time
import uuid
from datetime import UTC, datetime, timedelta
from decimal import ROUND_HALF_UP, Decimal
from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..config import settings
from ..core.cache import (
    get_cached_pricing,
    invalidate_balance_cache,
    set_pricing_cache,
)
from ..core.redis import get_lua_script, get_redis
from ..models import (
    AccountStatus,
    BalanceSource,
    Pricing,
    TokenAccount,
    TokenTransaction,
    TransactionType,
)
from .account import AccountService

logger = logging.getLogger(__name__)

# Default pricing fallback (FR-049) with max_tokens (FR-069)
DEFAULT_PRICING = {
    "input": Decimal("0.001"),  # $0.001 per 1k tokens
    "output": Decimal("0.002"),  # $0.002 per 1k tokens
    "version": "default-v1",
    "max_tokens": 128_000,  # Default max tokens for unknown models
}

# Reservation key prefix
RESERVATIONS_KEY_PREFIX = "metering:reservations:"


class MeteringService:
    """Service for token metering with v5 balance-only model."""

    def __init__(self, session: AsyncSession):
        self.session = session
        self.redis = get_redis()
        self._account_service = AccountService(session, self.redis)

    async def check_balance(
        self,
        user_id: str,
        request_id: str,
        estimated_tokens: int,
        model: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Check balance and create reservation - v5 balance-only.

        Logic flow (per spec):
        1. Get/Create account (auto-create with STARTER_TOKENS if new)
        2. Suspended? → BLOCK (ACCOUNT_SUSPENDED)
        3. Expired (inactive 365+ days)? → BLOCK (INSUFFICIENT_BALANCE, is_expired=true)
        4. Create Redis reservation, get reserved_total
        5. available_balance = effective_balance - reserved_total
        6. available_balance >= estimated_tokens? → ALLOW
        7. Otherwise → BLOCK (INSUFFICIENT_BALANCE) + rollback reservation

        Returns:
            dict with 'allowed', 'reservation_id', 'reserved_tokens', 'expires_at'
            OR dict with 'allowed'=False and error info
        """
        # Get or create account (FR-011, FR-012) - delegated to AccountService
        account = await self._account_service.get_or_create(user_id)

        # FR-069: Validate estimated_tokens against model's max_tokens limit
        pricing = await self._get_pricing(model or "default")
        max_tokens = pricing.get("max_tokens", 128_000)
        if estimated_tokens > max_tokens:
            return {
                "allowed": False,
                "error_code": "ESTIMATED_TOKENS_EXCEEDS_LIMIT",
                "message": f"estimated_tokens {estimated_tokens} exceeds model limit {max_tokens}",
                "balance": account.balance,
                "available_balance": account.effective_balance,
                "required": estimated_tokens,
                "is_expired": account.is_expired,
            }

        # 1. Suspended? → BLOCK
        if account.status == AccountStatus.SUSPENDED:
            return {
                "allowed": False,
                "error_code": "ACCOUNT_SUSPENDED",
                "message": "Account suspended by admin",
                "balance": account.balance,
                "available_balance": 0,
                "required": estimated_tokens,
                "is_expired": False,
            }

        # 2. Check expiry (FR-024, FR-025, FR-026)
        effective_balance = account.effective_balance
        is_expired = account.is_expired

        if is_expired:
            return {
                "allowed": False,
                "error_code": "INSUFFICIENT_BALANCE",
                "message": "Balance expired due to inactivity. Grant or topup to continue.",
                "balance": account.balance,
                "available_balance": 0,
                "required": estimated_tokens,
                "is_expired": True,
            }

        # 3. Try to create reservation via Lua script (FR-033, FR-036)
        now = int(time.time())
        expiry = now + settings.reservation_ttl

        if self.redis:
            reserve_script = get_lua_script("reserve")
            if reserve_script:
                try:
                    key = f"{RESERVATIONS_KEY_PREFIX}{user_id}"
                    result = await reserve_script(
                        keys=[key],
                        args=[request_id, estimated_tokens, now, expiry],
                    )
                    status, reserved_total, existing_tokens = result

                    # Handle idempotency (FR-059)
                    if status == 1:  # Idempotent - same request_id, same tokens
                        logger.info(
                            f"[Metering] Idempotent /check for request_id={request_id}"
                        )
                        return {
                            "allowed": True,
                            "reservation_id": f"res_{request_id[:12]}",
                            "reserved_tokens": int(existing_tokens),
                            "expires_at": datetime.now(UTC)
                            + timedelta(seconds=settings.reservation_ttl),
                        }

                    # Handle conflict (FR-060)
                    if status == 2:  # Conflict - same request_id, different tokens
                        return {
                            "allowed": False,
                            "error_code": "REQUEST_ID_CONFLICT",
                            "message": (
                                f"Request ID {request_id} already used with "
                                "different parameters"
                            ),
                            "balance": account.balance,
                            "available_balance": effective_balance - int(reserved_total),
                            "required": estimated_tokens,
                            "is_expired": False,
                        }

                    # New reservation created - check if we have enough balance
                    available_balance = effective_balance - int(reserved_total)

                    if available_balance < 0:
                        # Insufficient balance - rollback reservation (FR-036a)
                        await self._remove_reservation(user_id, request_id)
                        return {
                            "allowed": False,
                            "error_code": "INSUFFICIENT_BALANCE",
                            "message": "Insufficient balance for request",
                            "balance": account.balance,
                            "available_balance": effective_balance
                            - (int(reserved_total) - estimated_tokens),
                            "required": estimated_tokens,
                            "is_expired": False,
                        }

                    # Success
                    return {
                        "allowed": True,
                        "reservation_id": f"res_{request_id[:12]}",
                        "reserved_tokens": estimated_tokens,
                        "expires_at": datetime.now(UTC)
                        + timedelta(seconds=settings.reservation_ttl),
                    }

                except Exception as e:
                    logger.error(f"[Metering] Redis reservation error: {e}")
                    # Fall through to fail-open

        # Fail-open: Redis unavailable (FR-033)
        if settings.fail_open:
            logger.warning(f"[Metering] Fail-open mode for user={user_id}")

            # Use SELECT FOR UPDATE for database-level locking (FR-033)
            try:
                async with self.session.begin_nested():
                    result = await self.session.execute(
                        select(TokenAccount)
                        .where(TokenAccount.user_id == user_id)
                        .with_for_update()
                    )
                    locked_account = result.scalar_one_or_none()

                    if locked_account:
                        locked_effective_balance = locked_account.effective_balance
                        if locked_effective_balance >= estimated_tokens:
                            return {
                                "allowed": True,
                                "reservation_id": f"failopen_{uuid.uuid4().hex[:12]}",
                                "reserved_tokens": estimated_tokens,
                                "expires_at": datetime.now(UTC)
                                + timedelta(seconds=settings.reservation_ttl),
                            }
            except Exception as e:
                # SQLite doesn't support FOR UPDATE, fall back to simple check
                logger.warning(
                    f"[Metering] SELECT FOR UPDATE not supported, "
                    f"using simple check: {e}"
                )
                if effective_balance >= estimated_tokens:
                    return {
                        "allowed": True,
                        "reservation_id": f"failopen_{uuid.uuid4().hex[:12]}",
                        "reserved_tokens": estimated_tokens,
                        "expires_at": datetime.now(UTC)
                        + timedelta(seconds=settings.reservation_ttl),
                    }

        # No balance
        return {
            "allowed": False,
            "error_code": "INSUFFICIENT_BALANCE",
            "message": "Insufficient balance for request",
            "balance": account.balance,
            "available_balance": effective_balance,
            "required": estimated_tokens,
            "is_expired": False,
        }

    async def finalize_usage(
        self,
        user_id: str,
        request_id: str,
        reservation_id: str,
        input_tokens: int,
        output_tokens: int,
        model: str,
        thread_id: str | None = None,
        usage_details: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Finalize reservation with actual token usage - v5 balance-only.

        Deducts from account.balance, updates last_activity_at.
        Idempotent via request_id (FR-061, FR-062).

        Returns:
            dict with transaction details
        """
        total_tokens = input_tokens + output_tokens

        # Check for existing transaction (idempotency - FR-061, FR-062)
        existing = await self._get_transaction_by_request_id(request_id)
        if existing:
            logger.info(f"[Metering] Idempotent return for request_id={request_id}")
            return {
                "status": "already_processed",
                "transaction_id": existing.id,
                "total_tokens": existing.total_tokens,
                "credits_deducted": existing.credits_deducted or 0,
                "balance_after": 0,  # Would need to query for accurate value
                "pricing_version": existing.pricing_version or "v1",
            }

        # Get account - delegated to AccountService
        account = await self._account_service.get_or_create(user_id)

        # Calculate cost with markup (FR-044, FR-045, FR-046, FR-047)
        pricing = await self._get_pricing(model)
        base_cost = self._calculate_base_cost(input_tokens, output_tokens, pricing)
        markup = Decimal(str(settings.markup_percent))
        total_cost = base_cost * (1 + markup / 100)

        # Round for display but store full precision (FR-065)
        total_cost_rounded = total_cost.quantize(
            Decimal("0.000001"), rounding=ROUND_HALF_UP
        )

        # Update account atomically (FR-032)
        now = datetime.now(UTC)
        async with self.session.begin_nested():
            # Deduct from balance (may go negative - FR-041)
            account.balance -= total_tokens
            account.last_activity_at = now  # FR-027
            account.updated_at = now

            self.session.add(account)

            # Store usage_details in extra_data
            extra_data = {}
            if usage_details:
                extra_data["usage_details"] = usage_details

            # Create transaction (FR-015, FR-017)
            transaction = TokenTransaction(
                user_id=user_id,
                transaction_type=TransactionType.USAGE,
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                total_tokens=total_tokens,
                base_cost_usd=base_cost,
                markup_percent=markup,
                total_cost_usd=total_cost_rounded,
                credits_deducted=total_tokens,  # Positive value (FR-522)
                balance_source=BalanceSource.BALANCE,
                model=model,
                request_id=request_id,
                pricing_version=pricing.get("version", "v1"),
                thread_id=thread_id,
                extra_data=extra_data,
            )
            self.session.add(transaction)
            await self.session.flush()

        await self.session.commit()

        # Remove reservation from Redis (FR-037)
        if self.redis and not reservation_id.startswith("failopen_"):
            await self._remove_reservation(user_id, request_id)

        # Invalidate balance cache (FR-056)
        await self._invalidate_balance_cache(user_id)

        return {
            "status": "finalized",
            "transaction_id": transaction.id,
            "total_tokens": total_tokens,
            "credits_deducted": total_tokens,
            "balance_after": account.balance,
            "balance_source": "balance",  # v5: always "balance"
            "thread_id": thread_id,
            "pricing_version": pricing.get("version", "v1"),
        }

    async def release_reservation(
        self,
        user_id: str,
        request_id: str,
        reservation_id: str,
    ) -> dict[str, Any]:
        """
        Release reservation without deducting tokens (FR-063, FR-064).

        Called when LLM call fails.
        Idempotent - releasing twice returns success.
        """
        # Failopen reservations always succeed (FR-064)
        if reservation_id.startswith("failopen_"):
            return {"status": "released", "reserved_tokens": 0}

        if not self.redis:
            return {"status": "released", "reserved_tokens": 0}

        # Use Lua script to remove reservation (FR-038)
        release_script = get_lua_script("release")
        if release_script:
            try:
                key = f"{RESERVATIONS_KEY_PREFIX}{user_id}"
                now = int(time.time())
                result = await release_script(keys=[key], args=[request_id, now])
                status, released_tokens = result

                return {"status": "released", "reserved_tokens": int(released_tokens)}
            except Exception as e:
                logger.error(f"[Metering] Release error: {e}")

        return {"status": "released", "reserved_tokens": 0}

    # === Private Helper Methods ===

    async def _remove_reservation(self, user_id: str, request_id: str) -> None:
        """Remove reservation from Redis sorted set (FR-036a, FR-037, FR-038)."""
        if not self.redis:
            return

        release_script = get_lua_script("release")
        if release_script:
            try:
                key = f"{RESERVATIONS_KEY_PREFIX}{user_id}"
                now = int(time.time())
                await release_script(keys=[key], args=[request_id, now])
            except Exception as e:
                logger.error(f"[Metering] Remove reservation error: {e}")

    async def _get_transaction_by_request_id(
        self, request_id: str
    ) -> TokenTransaction | None:
        """Get existing transaction for idempotency check."""
        result = await self.session.execute(
            select(TokenTransaction).where(
                TokenTransaction.request_id == request_id,
                TokenTransaction.transaction_type == TransactionType.USAGE,
            )
        )
        return result.scalar_one_or_none()

    async def _get_pricing(self, model: str) -> dict[str, Any]:
        """Get pricing for model with caching (FR-048, FR-049).

        Caching strategy:
        - Try Redis cache first (5-minute TTL)
        - On cache miss, query DB and cache result
        - Pricing changes are rare, so caching is safe
        """
        # Try cache first
        cached = await get_cached_pricing(self.redis, model)
        if cached:
            logger.debug(f"[Metering] Pricing cache hit for {model}")
            # Add max_tokens from default if not in cached data
            if "max_tokens" not in cached:
                cached["max_tokens"] = DEFAULT_PRICING.get("max_tokens", 128_000)
            return cached

        # Cache miss - query DB
        result = await self.session.execute(
            select(Pricing)
            .where(
                Pricing.model == model,
                Pricing.is_active == True,  # noqa: E712
            )
            .order_by(Pricing.effective_date.desc())
            .limit(1)  # FR-048: Explicit LIMIT 1 for query optimization
        )
        pricing = result.scalar_one_or_none()

        if pricing:
            pricing_dict = {
                "input": pricing.input_cost_per_1k,
                "output": pricing.output_cost_per_1k,
                "version": pricing.pricing_version,
                "max_tokens": pricing.max_tokens,  # FR-069: Include max_tokens
            }
            # Cache the result
            await set_pricing_cache(self.redis, model, pricing_dict)
            return pricing_dict

        # Fallback to default pricing (FR-049)
        return DEFAULT_PRICING

    def _calculate_base_cost(
        self, input_tokens: int, output_tokens: int, pricing: dict[str, Any]
    ) -> Decimal:
        """Calculate base cost before markup (FR-045)."""
        input_cost = (Decimal(input_tokens) / 1000) * pricing["input"]
        output_cost = (Decimal(output_tokens) / 1000) * pricing["output"]
        return input_cost + output_cost

    async def _invalidate_balance_cache(self, user_id: str) -> None:
        """Invalidate cached balance data (FR-056)."""
        await invalidate_balance_cache(self.redis, user_id)
        logger.debug(f"[Metering] Invalidated cache for {user_id}")
