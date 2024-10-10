import logging
import sys
import unittest
from scaleway_core.client import Client
from scaleway.instance.v1 import InstanceV1API

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class TestTotalCountLegacy(unittest.TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.instance_api = InstanceV1API(self.client, bypass_validation=True)

    def test_list_servers_type(self):
        list_server_type = self.instance_api.list_servers_types(zone="fr-par-1")
        self.assertIsNotNone(list_server_type.total_count)
