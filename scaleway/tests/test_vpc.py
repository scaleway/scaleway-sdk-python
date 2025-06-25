import unittest
from scaleway.vpc.v2 import VpcV2API
from scaleway_core.api import ScalewayException
from scaleway_core.client import Client
from scaleway_core.utils import random_name

region = "fr-par"
tags = ["sdk-python", "regression-test"]
created_pn_count = 5
created_vpc_count = 1


class TestScalewayVPCV2(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.client = Client.from_env()
        self.vpcAPI = VpcV2API(self.client)
        self.project_id = self.client.default_project_id
        self.region = region
        self._pns_to_cleanup = []

        self._vpc = self.vpcAPI.create_vpc(
            enable_routing=True,
            region=self.region,
            project_id=self.project_id,
            name=random_name("vpc-test-sdk-python"),
        )

    @classmethod
    def tearDownClass(self):
        for pn in self._pns_to_cleanup:
            self.vpcAPI.delete_private_network(private_network_id=pn.id)

        if self._vpc is not None:
            self.vpcAPI.delete_vpc(vpc_id=self._vpc.id, region=self.region)

    def test_delete_vpc(self):
        vpc = self.vpcAPI.create_vpc(
            enable_routing=True,
            region=self.region,
            project_id=self.project_id,
            name=random_name("vpc-test-sdk-python"),
        )

        self.assertIsNotNone(vpc.id)
        self.assertEqual(vpc.region, self.region)

        self.vpcAPI.delete_vpc(vpc_id=vpc.id)

        with self.assertRaises(ScalewayException):
            self.vpcAPI.get_vpc(vpc_id=vpc.id)

    def test_list_vpcs(self):
        vpcs = self.vpcAPI.list_vp_cs(region=self.region)
        self.assertIsInstance(vpcs.vpcs, list)
        self.assertGreaterEqual(vpcs.total_count, created_vpc_count)

    def test_create_private_network(self):
        for i in range(created_pn_count):
            pn = self.vpcAPI.create_private_network(
                vpc_id=self._vpc.id,
                default_route_propagation_enabled=True,
                project_id=self.project_id,
                name=random_name(f"sdk-python-pn-{i}"),
            )
            self._pns_to_cleanup.append(pn)

            self.assertEqual(pn.vpc_id, self._vpc.id)

    def test_list_private_network(self):
        networks = self.vpcAPI.list_private_networks(region=self.region)
        self.assertIsInstance(networks.private_networks, list)
        self.assertGreaterEqual(networks.total_count, created_pn_count)

    def test_get_vpc(self):
        vpc = self.vpcAPI.get_vpc(vpc_id=self._vpc.id, region=self.region)

        self.assertIsNotNone(vpc)
        self.assertEqual(self._vpc.id, vpc.id)

    def test_update_vpc(self):
        vpc = self.vpcAPI.update_vpc(vpc_id=self._vpc.id, tags=tags)

        self.assertEqual(vpc.tags, tags)
        self.assertEqual(self._vpc.id, vpc.id)

    def test_list_vpc_all(self):
        vpcs = self.vpcAPI.list_vp_cs_all()

        self.assertIsInstance(vpcs, list)
        self.assertGreaterEqual(len(vpcs), created_pn_count)
