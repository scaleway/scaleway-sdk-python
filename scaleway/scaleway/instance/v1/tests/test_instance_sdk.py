from typing import Generator

import pytest

from scaleway.instance.v1 import IpType
from scaleway.instance.v1.custom_api import InstanceUtilsV1API
from scaleway.instance.v1 import AttachServerVolumeRequestVolumeType
from scaleway.instance.v1.types import (
    VolumeVolumeType,
    BootType,
    Server,
    VolumeServerTemplate,
)
from scaleway.block.v1alpha1 import BlockV1Alpha1API
from scaleway.block.v1alpha1.types import Volume, CreateVolumeRequestFromEmpty
from tests.utils import initialize_client_test
from vcr_config import scw_vcr

server_name = "test-sdk-python-fixture"
server_name_extra = "test-sdk-python-extra"
max_retry = 10
interval = 0.01
volume_size = 10_000_000_000
commercial_type = "DEV1-S"
zone = "fr-par-1"

# mypy: ignore-errors


@pytest.fixture(scope="module")
def instance_block_api() -> tuple[InstanceUtilsV1API, BlockV1Alpha1API]:
    client = initialize_client_test()
    instance_api = InstanceUtilsV1API(client, bypass_validation=True)
    block_api = BlockV1Alpha1API(client, bypass_validation=True)
    return instance_api, block_api


@pytest.fixture(scope="module")
@scw_vcr.use_cassette
def instance_volume(
    instance_block_api: tuple[InstanceUtilsV1API, BlockV1Alpha1API],
) -> Generator[tuple[Server, list[Volume]], None, None]:
    instance_api, block_api = instance_block_api
    volumes_list: list[Volume] = []

    volumes = {
        "0": VolumeServerTemplate(
            volume_type=VolumeVolumeType.L_SSD,
            size=volume_size,
            boot=False,
        )
    }

    instance = instance_api._create_server(
        commercial_type=commercial_type,
        zone=zone,
        name=server_name,
        dynamic_ip_required=False,
        volumes=volumes,
        protected=False,
        boot_type=BootType.LOCAL,
        image="c00ae53c-1e29-4087-a384-47f3c5c1cd84",
    )

    server = instance.server
    assert server is not None, "Server creation failed"
    assert server.id is not None, "Server ID is None after creation"

    instance_api.wait_instance_server(server.id, zone=zone)

    yield server, volumes_list

    for volume in volumes_list:
        assert volume.id is not None
        instance_api.detach_server_volume(
            server_id=server.id, volume_id=volume.id, zone=zone
        )
        block_api.wait_for_volume(volume_id=volume.id, zone=zone)
        block_api.delete_volume(volume_id=volume.id, zone=zone)

    instance_api.delete_server(server_id=server.id, zone=zone)


@scw_vcr.use_cassette
def test_attach_additional_volume(
    instance_block_api: tuple[InstanceUtilsV1API, BlockV1Alpha1API],
    instance_volume: tuple[Server, list[Volume]],
) -> None:
    instance_api, block_api = instance_block_api
    server, volumes_list = instance_volume
    assert server.id is not None

    additional_volume = block_api.create_volume(
        from_empty=CreateVolumeRequestFromEmpty(size=volume_size),
    )
    assert additional_volume.id is not None

    updated_volume = block_api.wait_for_volume(
        volume_id=additional_volume.id, zone=zone
    )
    assert updated_volume.id is not None
    volumes_list.append(updated_volume)

    instance_api.attach_server_volume(
        server_id=server.id,
        volume_id=additional_volume.id,
        zone=zone,
        volume_type=AttachServerVolumeRequestVolumeType.SBS_VOLUME,
    )
    instance_api.wait_instance_server(server_id=server.id, zone=zone)
    block_api.wait_for_volume(volume_id=additional_volume.id, zone=zone)

    server_details = instance_api.get_server(server_id=server.id, zone=zone).server
    assert server_details is not None
    attached_volume_ids = [v.id for v in server_details.volumes.values()]
    assert additional_volume.id in attached_volume_ids


@scw_vcr.use_cassette
def test_list_server(
    instance_block_api: tuple[InstanceUtilsV1API, BlockV1Alpha1API],
) -> None:
    instance_api, _ = instance_block_api
    servers = instance_api.list_servers(zone=zone)
    assert len(servers.servers) >= 1
    assert servers.servers[0].name == server_name


@scw_vcr.use_cassette
def test_create_new_server(
    instance_block_api: tuple[InstanceUtilsV1API, BlockV1Alpha1API],
) -> None:
    instance_api, _ = instance_block_api
    server_instance = instance_api._create_server(
        commercial_type=commercial_type,
        zone=zone,
        name=server_name_extra,
        dynamic_ip_required=False,
        volumes={},
        protected=False,
        boot_type=BootType.LOCAL,
    )
    server = server_instance.server
    assert server is not None
    assert server.id is not None
    assert server.name == server_name_extra

    servers = instance_api.list_servers_all(zone=zone)
    assert len(servers) >= 2

    instance_api.delete_server(server_id=server.id, zone=zone)


@scw_vcr.use_cassette
def test_create_ip(
    instance_block_api: tuple[InstanceUtilsV1API, BlockV1Alpha1API],
) -> None:
    instance_api, _ = instance_block_api
    ip_instance = instance_api.create_ip(type_=IpType.ROUTED_IPV6).ip
    assert ip_instance is not None
    assert ip_instance.id is not None
    ips = instance_api.list_ips(zone=zone)
    assert int(ips.total_count) >= 1
    instance_api.delete_ip(ip=ip_instance.id, zone=zone)
