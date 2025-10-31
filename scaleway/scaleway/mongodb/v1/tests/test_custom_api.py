from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from vcr_config import scw_vcr
from tests.utils import initialize_client_test
from scaleway.mongodb.v1.custom_api import MongodbUtilsV1API


# mypy: ignore-errors


@scw_vcr.use_cassette
def test_create_snapshot_with_naive_expires_at_vcr() -> None:
    cassette = (
        Path(__file__).with_name("cassettes")
        / "test_create_snapshot_with_naive_expires_at_vcr.cassette.yaml"
    )
    if not cassette.exists():
        pytest.skip("cassette not recorded yet; record locally then commit it")
    client = initialize_client_test()
    api = MongodbUtilsV1API(client, bypass_validation=True)

    # Fixed value to match cassette; record once locally, then CI replays
    instance_id = "00000000-0000-0000-0000-000000000000"

    # Naive datetime should be handled as UTC by the utils API
    naive_dt = datetime.now().replace(tzinfo=None) + timedelta(days=1)

    snapshot = api.create_snapshot(
        instance_id=instance_id,
        name="sdk-python-test-snapshot",
        expires_at=naive_dt,
    )

    assert snapshot is not None
