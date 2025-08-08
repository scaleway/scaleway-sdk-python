from typing import List
import unittest
import uuid
import time

from scaleway_core.client import Client
from scaleway.instance.v1.api import InstanceV1API
from scaleway.instance.v1.types import VolumeVolumeType, BootType
from scaleway.block.v1alpha1 import BlockV1Alpha1API
from scaleway.instance.v1.types import Server, VolumeServerTemplate
from scaleway.block.v1alpha1.types import Volume, CreateVolumeRequestFromEmpty


server_name = f"test-sdk-python-{uuid.uuid4().hex[:6]}"
max_retry = 10
interval = 0.01
volume_size = 10000000000
commercial_type = "DEV1-S"
zone = "fr-par-1"


class TestE2EServerCreation(unittest.TestCase):
    def setUp(self) -> None:
        self.zone = zone
        self.client = Client.from_config_file_and_env()
        self.instanceAPI = InstanceV1API(self.client, bypass_validation=True)
        self.blockAPI = BlockV1Alpha1API(self.client, bypass_validation=True)
        self._server = None
        self._volumes = []

    def tearDown(self) -> None:
        for volume in self._volumes:
            self.instanceAPI.detach_server_volume(
                server_id=self._server.id, volume_id=volume.id
            )
            self.blockAPI.wait_for_volume(volume_id=volume.id)
            self.blockAPI.delete_volume(volume_id=volume.id)

        if self._server:
            self.instanceAPI.delete_server(zone=self.zone, server_id=self._server.id)

    def wait_test_instance_server(self, server_id):
        int = interval

        for i in range(1, max_retry):
            int *= i
            s = self.instanceAPI.get_server(zone=self.zone, server_id=server_id)

            if s.server.state == "running" or s.server.state == "stopped":
                return s

            time.sleep(int)

        return self.fail("Server did not reach 'running' state in time.")

    def create_test_instance_server(self) -> Server:
        volumes = dict[str, VolumeServerTemplate]()
        volumes = {
            "0": VolumeServerTemplate(
                volume_type=VolumeVolumeType.L_SSD,
                size=volume_size,
                boot=False,
            )
        }
        server = self.instanceAPI._create_server(
            commercial_type=commercial_type,
            zone=self.zone,
            name=server_name,
            dynamic_ip_required=False,
            volumes=volumes,
            protected=False,
            boot_type=BootType.LOCAL,
            image="c00ae53c-1e29-4087-a384-47f3c5c1cd84",
        )

        self._server = server.server

        self.wait_test_instance_server(server_id=server.server.id)

        return server.server

    def create_test_from_empty_volume(self, number) -> List[Volume]:
        volumes: List[Volume] = {}

        for i in range(number):
            volume = self.blockAPI.create_volume(
                from_empty=CreateVolumeRequestFromEmpty(size=1000000000),
            )

            self.blockAPI.wait_for_volume(volume_id=volume.id, zone=self.zone)

            self._volumes.append(volume)  # Ensure cleanup in tearDown
            volumes[i] = volume

        return volumes

    def test_attach_aditionnal_volume(self):
        server = self.create_test_instance_server()
        additional_volumes = self.create_test_from_empty_volume(1)
        additional_volume = additional_volumes[0]

        self.assertIsNotNone(server.id)
        self.assertEqual(server.zone, self.zone)

        self.assertIsNotNone(additional_volume.id)
        self.assertEqual(additional_volume.size, 1000000000)

        self.instanceAPI.attach_server_volume(
            server_id=server.id,
            volume_id=additional_volume.id,
            volume_type=VolumeVolumeType.SBS_VOLUME,
        )

        self.blockAPI.wait_for_volume(volume_id=additional_volume.id, zone=self.zone)

        updated_server = self.instanceAPI.get_server(
            zone=self.zone, server_id=server.id
        )
        attached_volumes = updated_server.server.volumes or {}
        attached_volume_ids = [v.id for v in attached_volumes.values()]
        self.assertIn(additional_volume.id, attached_volume_ids)
