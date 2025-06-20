import logging
import sys
from typing import List
import unittest
import uuid
import time

from scaleway_core.client import Client
from scaleway.instance.v1.api import InstanceV1API
from scaleway.block.v1alpha1 import BlockV1Alpha1API
from scaleway.instance.v1.types import Server, VolumeServerTemplate
from scaleway.block.v1alpha1.types import Volume, CreateVolumeRequestFromEmpty

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

server_name = f"test-sdk-python-{uuid.uuid4().hex[:6]}"
max_retry = 10
interval = 0.1
volume_size = 10
commercial_type = "DEV1-S"
zone = "fr-par-1"
timeout_attach = 10


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
            logger.info("✅ Volume {volume.id} has been detach")

            self.blockAPI.delete_volume(volume_id=volume.id)
            logger.info("✅ Volume {volume.id} has been deleted")
        if self._server:
            self.api.delete_server(zone=self.zone, server_id=self._server.id)
            logger.info(f"🗑️ Deleted server: {self._server.id}")

    def wait_test_instance_server(self, server_id):
        for i in range(1, max_retry):
            interval *= i
            s = self.api.get_server(zone=self.zone, server_id=server_id)
            if s.state == "running":
                break
            time.sleep(interval)
        else:
            self.fail("Server did not reach 'running' state in time.")

    def create_test_instance_server(self) -> Server:
        volume = {
            "0": VolumeServerTemplate(
                volume_type="sbs_volume", name="my-volume", size=volume_size
            )
        }
        server = self.instanceAPI._create_server(
            commercial_type=commercial_type,
            zone=self.zone,
            name=server_name,
            dynamic_ip_required=True,
            volumes=volume,
        )
        logger.info(f"✅ Created server: {server.id}")
        self._server = server.server
        self.wait_test_instance_server(server_id=server.server.id)
        return server.server

    def create_test_from_empty_volume(self, number) -> List[Volume]:
        volumes: List[Volume] = {}
        for i in range(number):
            volume = self.blockAPI.create_volume(
                from_empty=CreateVolumeRequestFromEmpty(size=10),
            )
            logger.info("✅ Created server: {volume.id}")
            self._volumes.append(volume)  # Ensure cleanup in tearDown
            volumes.append(volume)

        return volumes

    def test_attach_aditionnal_volume(self):
        server = self.create_test_instance_server()
        additional_volumes = self.create_test_from_empty_volume(1)
        additional_volume = list(additional_volumes.values())[0]

        self.assertIsNotNone(server.id)
        self.assertEqual(server.zone, self.zone)

        self.assertIsNotNone(additional_volume.id)
        self.assertEqual(additional_volume.size, 10)
        logger.info(f"✅ Volume created with ID: {additional_volume.id}")

        self.instanceAPI.attach_server_volume(
            server_id=server.id, volume_id=additional_volume.id
        )
        logger.info(f"🔗 Attached volume {additional_volume.id} to server {server.id}")

        time.sleep(timeout_attach)

        updated_server = self.instanceAPI.get_server(
            zone=self.zone, server_id=server.id
        )
        attached_volumes = updated_server.volumes or {}
        attached_volume_ids = [v.volume.id for v in attached_volumes.values()]
        self.assertIn(additional_volume.id, attached_volume_ids)
        logger.info(
            f"✅ Volume {additional_volume.id} is attached to server {server.id}"
        )
