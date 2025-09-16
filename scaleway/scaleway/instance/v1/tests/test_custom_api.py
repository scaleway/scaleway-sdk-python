from typing import Any, Generator

import pytest

from scaleway.instance.v1 import Server, BootType
from scaleway.instance.v1.custom_api import InstanceUtilsV1API
from tests.utils import initialize_client_test
from vcr_config import scw_vcr

server_name = "test-sdk-python-fixture"
server_name_extra = "test-sdk-python-extra"
max_retry = 10
interval = 0.01
commercial_type = "DEV1-S"
zone = "fr-par-1"

# mypy: ignore-errors


@pytest.fixture(scope="module")
def instance_api() -> InstanceUtilsV1API:
    client = initialize_client_test()
    return InstanceUtilsV1API(client, bypass_validation=True)


@pytest.fixture(scope="module")
@scw_vcr.use_cassette
def server(instance_api: InstanceUtilsV1API) -> Generator[Server, Any, None]:
    instance = instance_api._create_server(
        commercial_type=commercial_type,
        zone=zone,
        name=server_name,
        dynamic_ip_required=False,
        protected=False,
        boot_type=BootType.LOCAL,
        image="c00ae53c-1e29-4087-a384-47f3c5c1cd84",
    )
    server = instance.server
    assert server is not None, "Server creation failed"
    assert server.id is not None, "Server ID is None after creation"
    instance_api.wait_instance_server(server.id, zone=zone)

    yield server

    instance_api.delete_server(server_id=server.id, zone=zone)


@scw_vcr.use_cassette
def test_set_and_get_server_user_data(
    instance_api: InstanceUtilsV1API, server: Server
) -> None:
    key = "first key"
    content = b"this-is-a-test"
    instance_api.set_server_user_data(server.id, zone=zone, key=key, content=content)
    user_data = instance_api.get_server_user_data(server.id, key=key)

    assert user_data is not None


@scw_vcr.use_cassette
def test_set_and_get_all_user_data(
    instance_api: InstanceUtilsV1API, server: Server
) -> None:
    key = "first key"
    content = b"content first key"
    key_bis = "second key"
    content_bis = b"test content"
    another_key = "third key"
    another_content = b"another content to test"
    user_data: dict[str, bytes] = {
        key_bis: content_bis,
        another_key: another_content,
        key: content,
    }
    instance_api.set_all_server_user_data(server_id=server.id, user_data=user_data)
    response = instance_api.get_all_server_user_data(server_id=server.id)
    assert response.user_data == user_data
