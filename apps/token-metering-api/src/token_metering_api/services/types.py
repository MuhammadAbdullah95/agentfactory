"""TypedDict definitions for service return types (v5 - Balance Only).

Provides type safety for service method returns instead of dict[str, Any].
"""

from datetime import datetime
from typing import Literal, TypedDict


class CheckBalanceAllowed(TypedDict):
    """Successful balance check - reservation created."""

    allowed: Literal[True]
    reservation_id: str
    reserved_tokens: int
    expires_at: datetime


class CheckBalanceBlocked(TypedDict):
    """Failed balance check - request blocked."""

    allowed: Literal[False]
    error_code: Literal["INSUFFICIENT_BALANCE", "ACCOUNT_SUSPENDED", "REQUEST_ID_CONFLICT"]
    message: str
    balance: int
    available_balance: int
    required: int
    is_expired: bool


# Union type for check_balance return
CheckBalanceResult = CheckBalanceAllowed | CheckBalanceBlocked


class FinalizeResultSuccess(TypedDict):
    """Successful finalization."""

    status: Literal["finalized"]
    transaction_id: int
    total_tokens: int
    credits_deducted: int
    balance_after: int
    balance_source: str
    thread_id: str | None
    pricing_version: str


class FinalizeResultIdempotent(TypedDict):
    """Idempotent return - already processed."""

    status: Literal["already_processed"]
    transaction_id: int
    total_tokens: int
    credits_deducted: int
    balance_after: int
    pricing_version: str


# Union type for finalize_usage return
FinalizeResult = FinalizeResultSuccess | FinalizeResultIdempotent


class ReleaseResult(TypedDict):
    """Reservation release result."""

    status: Literal["released"]
    reserved_tokens: int


class GrantResult(TypedDict):
    """Admin grant tokens result."""

    success: Literal[True]
    transaction_id: int
    allocation_id: int
    tokens_granted: int
    new_balance: int


class TopupResult(TypedDict):
    """Admin topup tokens result."""

    success: Literal[True]
    transaction_id: int
    allocation_id: int
    tokens_added: int
    new_balance: int


class BalanceInfo(TypedDict):
    """User balance information."""

    user_id: str
    status: str
    balance: int
    effective_balance: int
    last_activity_at: str | None
    is_expired: bool
