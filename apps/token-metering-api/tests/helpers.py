"""Test helper functions."""

import hashlib
import uuid


def make_request_id(seed: str = "") -> str:
    """Generate a deterministic UUID from a seed string for reproducible tests.

    Usage:
        request_id = make_request_id("test-001")  # Always returns same UUID
        request_id = make_request_id()  # Random UUID
    """
    if seed:
        # Create deterministic UUID from seed using MD5 hash
        hash_bytes = hashlib.md5(seed.encode()).digest()
        return str(uuid.UUID(bytes=hash_bytes))
    return str(uuid.uuid4())
