import sys
import unittest
import logging
from typing import Dict

from scaleway_core.client import Client
from .custom_api import InstanceUtilsV1API

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class TestServerUserData(unittest.TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.instance_api = InstanceUtilsV1API(self.client, bypass_validation=True)
        self.server = self.instance_api._create_server(
            commercial_type="DEV1-S",
            zone="fr-par-1",
            image="ubuntu_jammy",
            name="my-server-web",
            volumes={},
            protected=False,
        )

    @unittest.skip("API Test is not up")
    def test_set_and_get_server_user_data(self) -> None:
        if self.server is None or self.server.server is None:
            self.fail("Server setup failed.")
        key = "first key"
        content = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10"
        self.instance_api.set_server_user_data(
            server_id=self.server.server.id, key=key, content=content
        )
        user_data = self.instance_api.get_server_user_data(
            server_id=self.server.server.id, key=key
        )
        self.assertIsNotNone(user_data)

    @unittest.skip("API Test is not up")
    def test_set_and_get_all_user_data(self) -> None:
        if self.server is None or self.server.server is None:
            self.fail("Server setup failed.")
        key = "first key"
        content = b"content first key"
        key_bis = "second key"
        content_bis = b"test content"
        another_key = "third key"
        another_content = b"another content to test"

        user_data: Dict[str, bytes] = {
            key_bis: content_bis,
            another_key: another_content,
            key: content,
        }
        self.instance_api.set_all_server_user_data(
            server_id=self.server.server.id, user_data=user_data
        )
        response = self.instance_api.get_all_server_user_data(
            server_id=self.server.server.id
        )
        self.assertIsNotNone(response)
