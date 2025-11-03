import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from vcr_config import scw_vcr
from vcr_config import PYTHON_UPDATE_CASSETTE
from tests.utils import initialize_client_test
from scaleway.mongodb.v1.custom_api import MongodbUtilsV1API


# mypy: ignore-errors


@scw_vcr.use_cassette
def test_create_snapshot_with_naive_expires_at_vcr() -> None:
    cassette = (
        Path(__file__).with_name("cassettes")
        / "test_create_snapshot_with_naive_expires_at_vcr.cassette.yaml"
    )
    if not cassette.exists() and not os.getenv("PYTHON_UPDATE_CASSETTE"):
        pytest.skip(
            "cassette not recorded yet; set PYTHON_UPDATE_CASSETTE=true to record"
        )
    client = initialize_client_test()
    api = MongodbUtilsV1API(client, bypass_validation=True)

    # During recording, require a real instance_id via env; during replay, use the fixed value matching the cassette
    if PYTHON_UPDATE_CASSETTE:
        instance_id = os.getenv("SCW_TEST_MONGODB_INSTANCE_ID")
        if not instance_id:
            pytest.skip("SCW_TEST_MONGODB_INSTANCE_ID not set while recording")
    else:
        instance_id = "00000000-0000-0000-0000-000000000000"

    # Naive datetime should be handled as UTC by the utils API
    naive_dt = datetime.now().replace(tzinfo=None) + timedelta(days=1)

    snapshot = api.create_snapshot(
        instance_id=instance_id,
        name="sdk-python-test-snapshot",
        expires_at=naive_dt,
    )

    assert snapshot is not None
