import logging
import sys
from typing import List
import unittest
import uuid
import time

from scaleway.instance.v1 import CreateServerResponse
from scaleway_core.client import Client
from scaleway.instance.v1.api import InstanceV1API
from scaleway.block.v1alpha1 import BlockV1Alpha1API
from scaleway.instance.v1.types import Server, VolumeServerTemplate, VolumeVolumeType, ServerAction
from scaleway.block.v1alpha1.types import Volume, CreateVolumeRequestFromEmpty


server_name = f"test-sdk-python-{uuid.uuid4().hex[:6]}"
max_retry = 60
INTERVAL = 5
volume_size = 10
commercial_type = "DEV1-S"
zone = "fr-par-1"
image = "ubuntu_focal"

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

class TestE2EServerCreation(unittest.TestCase):
    def setUp(self) -> None:
        self.zone = zone
        self.client = Client.from_env()
        self.instanceAPI = InstanceV1API(self.client, bypass_validation=True)
        self.blockAPI = BlockV1Alpha1API(self.client, bypass_validation=True)
        self._server = None
        self._volumes = []

    def tearDown(self) -> None:
        for volume in self._volumes:
            self.instanceAPI.detach_server_volume(
                server_id=self._server.id, volume_id=volume.id
            )

            self.blockAPI.delete_volume(volume_id=volume.id)

        if self._server:
            self.instanceAPI.delete_server(zone=self.zone, server_id=self._server.id)

    def wait_test_instance_server(self, server_id):
        interval = INTERVAL

        for i in range(1, max_retry):
            logger.log(1, "value of i: ", i)
            interval *= i
            s = self.instanceAPI.get_server(zone=self.zone, server_id=server_id)
            if s.server.state == "running":
                return
            time.sleep(interval)

        self.fail("Server did not reach 'running' state in time.")

    def create_test_instance_server(self) -> Server | None:
        server = self.instanceAPI._create_server(
            commercial_type=commercial_type,
            zone=self.zone,
            name=server_name,
            dynamic_ip_required=True,
            protected=False,
            image=image,
        )

        self.instanceAPI.server_action(server_id=server.server.id, zone=self.zone, action=ServerAction.POWERON)

        logging.log(1, "value of server", server)

        self.wait_test_instance_server(server_id=server.server.id)
        self._server = server.server

        return server.server

    def create_test_from_empty_volume(self, number) -> List[Volume]:
        volumes: List[Volume] = []

        for i in range(number):
            volume = self.blockAPI.create_volume(
                from_empty=CreateVolumeRequestFromEmpty(size=10), zone=self.zone
            )

            self.blockAPI.wait_for_volume(volume_id=volume.id, zone=self.zone)

            self._volumes.append(volume)  # Ensure cleanup in tearDown
            volumes.append(volume)

        return volumes

    def test_attach_aditionnal_volume(self):
        server = self.create_test_instance_server()
        additional_volumes = self.create_test_from_empty_volume(1)
        additional_volume = additional_volumes[0]

        self.assertIsNotNone(server.id)
        self.assertEqual(server.zone, self.zone)

        self.assertIsNotNone(additional_volume.id)
        self.assertEqual(additional_volume.size, 10)

        self.instanceAPI.attach_server_volume(
            server_id=server.id, volume_id=additional_volume.id
        )

        self.blockAPI.wait_for_volume(volume_id=additional_volume.id, zone=self.zone)

        updated_server = self.instanceAPI.get_server(
            zone=self.zone, server_id=server.id
        )
        attached_volumes = updated_server.server.volumes or {}
        attached_volume_ids = [v.id for v in attached_volumes.values()]
        self.assertIn(additional_volume.id, attached_volume_ids)
