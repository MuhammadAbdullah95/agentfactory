"""Token metering data models (v5 - Balance Only).

v5 Changes (from v4):
- TokenAccount: Removed lifetime_used, balance defaults to STARTER_TOKENS (50k)
- TokenAllocation: Added STARTER allocation type for new user tracking
- TokenTransaction: Added STARTER type, removed TRIAL from BalanceSource
- Inactivity-based expiry via INACTIVITY_EXPIRY_DAYS (365 days)
"""

from sqlmodel import SQLModel

from .account import INACTIVITY_EXPIRY_DAYS, STARTER_TOKENS, AccountStatus, TokenAccount
from .allocation import AllocationType, TokenAllocation
from .pricing import Pricing
from .transaction import BalanceSource, TokenTransaction, TransactionType

__all__ = [
    "SQLModel",
    # Account (v5)
    "TokenAccount",
    "AccountStatus",
    "INACTIVITY_EXPIRY_DAYS",
    "STARTER_TOKENS",
    # Allocation (v5 - audit only, includes STARTER)
    "TokenAllocation",
    "AllocationType",
    # Transaction (v5 - includes STARTER)
    "TokenTransaction",
    "TransactionType",
    "BalanceSource",
    # Pricing
    "Pricing",
]
