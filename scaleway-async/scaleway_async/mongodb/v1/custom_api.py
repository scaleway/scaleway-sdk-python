from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional, Any

from .api import MongodbV1API


def _ensure_tzaware_utc(value: Optional[datetime]) -> Optional[datetime]:
    if value is None:
        return None
    if value.tzinfo is None or value.tzinfo.utcoffset(value) is None:
        return value.replace(tzinfo=timezone.utc)
    return value


class MongodbUtilsV1API(MongodbV1API):
    """
    Async extensions for MongoDB V1.
    - Naive datetimes for expires_at are assumed to be UTC.
    """

    async def create_snapshot(self, **kwargs: Any) -> Any:
        expires_at = kwargs.get("expires_at")
        kwargs["expires_at"] = _ensure_tzaware_utc(expires_at)
        return await super().create_snapshot(**kwargs)

    async def update_snapshot(self, **kwargs: Any) -> Any:
        expires_at = kwargs.get("expires_at")
        kwargs["expires_at"] = _ensure_tzaware_utc(expires_at)
        return await super().update_snapshot(**kwargs)
