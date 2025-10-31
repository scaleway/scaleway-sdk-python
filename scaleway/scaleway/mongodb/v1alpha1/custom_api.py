from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Optional

from scaleway.mongodb.v1alpha1.api import MongodbV1Alpha1API  # type: ignore[import-untyped]


def _ensure_tzaware_utc(value: Optional[datetime]) -> Optional[datetime]:
    if value is None:
        return None
    if value.tzinfo is None or value.tzinfo.utcoffset(value) is None:
        return value.replace(tzinfo=timezone.utc)
    return value


class MongodbUtilsV1Alpha1API(MongodbV1Alpha1API):  # type: ignore[misc]
    """
    Extensions for MongoDB V1alpha1 that provide safer ergonomics.

    - Naive datetimes for expires_at are assumed to be UTC.
    """

    def create_snapshot(self, **kwargs: Any) -> Any:
        expires_at = kwargs.get("expires_at")
        kwargs["expires_at"] = _ensure_tzaware_utc(expires_at)
        return super().create_snapshot(**kwargs)

    def update_snapshot(self, **kwargs: Any) -> Any:
        expires_at = kwargs.get("expires_at")
        kwargs["expires_at"] = _ensure_tzaware_utc(expires_at)
        return super().update_snapshot(**kwargs)
