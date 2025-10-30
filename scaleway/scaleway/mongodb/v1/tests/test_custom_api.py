from datetime import datetime, timezone

import pytest

from scaleway.scaleway.mongodb.v1.custom_api import MongodbUtilsV1API
from scaleway.scaleway.mongodb.v1.api import MongodbV1API


class _DummyClient:
    pass


@pytest.mark.parametrize("method_name", ["create_snapshot", "update_snapshot"])
def test_utils_api_coerces_naive_datetime_to_utc(monkeypatch, method_name):
    captured = {}

    def dummy(self, **kwargs):  # type: ignore[no-untyped-def]
        captured.update(kwargs)
        return kwargs

    monkeypatch.setattr(MongodbV1API, method_name, dummy, raising=True)

    api = MongodbUtilsV1API(client=_DummyClient(), bypass_validation=True)

    # Build naive datetime without triggering DTZ001 (construct aware then strip tz)
    naive_dt = datetime(2030, 1, 1, 12, 0, 0, tzinfo=timezone.utc).replace(tzinfo=None)

    if method_name == "create_snapshot":
        api.create_snapshot(instance_id="iid", name="n", expires_at=naive_dt)
    else:
        api.update_snapshot(snapshot_id="sid", expires_at=naive_dt)

    assert "expires_at" in captured
    coerced = captured["expires_at"]
    assert isinstance(coerced, datetime)
    assert coerced.tzinfo is not None
    assert coerced.utcoffset() == timezone.utc.utcoffset(coerced)


@pytest.mark.parametrize("method_name", ["create_snapshot", "update_snapshot"])
def test_utils_api_preserves_aware_datetime(monkeypatch, method_name):
    captured = {}

    def dummy(self, **kwargs):  # type: ignore[no-untyped-def]
        captured.update(kwargs)
        return kwargs

    monkeypatch.setattr(MongodbV1API, method_name, dummy, raising=True)

    api = MongodbUtilsV1API(client=_DummyClient(), bypass_validation=True)

    aware_dt = datetime(2030, 1, 1, 12, 0, 0, tzinfo=timezone.utc)

    if method_name == "create_snapshot":
        api.create_snapshot(instance_id="iid", name="n", expires_at=aware_dt)
    else:
        api.update_snapshot(snapshot_id="sid", expires_at=aware_dt)

    assert captured["expires_at"] is aware_dt


