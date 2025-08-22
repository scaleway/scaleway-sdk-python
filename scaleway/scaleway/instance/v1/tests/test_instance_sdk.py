import uuid

import pytest

from scaleway.block.v1 import BlockV1API
from scaleway.instance.v1 import InstanceV1API, VolumeServerTemplate, VolumeVolumeType, BootType
from scaleway_core.client import Client
from vcr_config import scw_vcr

server_name = f"test-sdk-python-{uuid.uuid4().hex[:6]}"
max_retry = 10
interval = 0.01
volume_size = 10000000000
commercial_type = "DEV1-S"
zone = "fr-par-1"
image_id = "c00ae53c-1e29-4087-a384-47f3c5c1cd84"

@pytest.fixture(scope="module")
@scw_vcr.use_cassette
def instance_api():
    client = Client.from_config_file_and_env()
    api = InstanceV1API(client)
    return api, client.default_project_id, zone

@pytest.fixture(scope="module")
@scw_vcr.use_cassette
def block_api():
    client = Client.from_config_file_and_env()
    api = BlockV1API(client)
    return api, client.default_project_id, zone

@scw_vcr.use_cassette
def test_instance_create(instance_api):
    api, project_id, zone = instance_api
    volumes = {
        "0": VolumeServerTemplate(
            volume_type=VolumeVolumeType.L_SSD,
            size=volume_size,
            boot=False,
        )
    }
    instance = api.create_instance(project_id=project_id, zone=zone, name=server_name, dynamic_ip_required=False, volume=volumes, protected=False, boot_type=BootType.LOCAL, image=image_id)
    assert instance.name == server_name
    assert instance.project_id == project_id
    assert instance.zone == zone
    assert instance.id is not None

