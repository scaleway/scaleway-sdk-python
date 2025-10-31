import os
from datetime import datetime, timedelta, timezone

import pytest

from vcr_config import scw_vcr
from tests.utils import initialize_client_test
from scaleway.mongodb.v1.custom_api import MongodbUtilsV1API


# mypy: ignore-errors


@scw_vcr.use_cassette
def test_create_snapshot_with_naive_expires_at_vcr() -> None:
    client = initialize_client_test()
    api = MongodbUtilsV1API(client, bypass_validation=True)

    instance_id = os.environ.get("SCW_TEST_MONGODB_INSTANCE_ID")
    if not instance_id:
        pytest.skip("SCW_TEST_MONGODB_INSTANCE_ID not set for recording")

    # Naive datetime should be handled as UTC by the utils API
    naive_dt = datetime.now().replace(tzinfo=None) + timedelta(days=1)

    snapshot = api.create_snapshot(
        instance_id=instance_id,
        name="sdk-python-test-snapshot",
        expires_at=naive_dt,
    )

    assert snapshot is not None
