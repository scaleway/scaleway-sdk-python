import os

import pytest
from scaleway.vpc.v2 import VpcV2API
from scaleway_core.api import ScalewayException
from scaleway_core.client import Client
from scaleway_core.utils import random_name
from vcr_config import scw_vcr

region = "fr-par"
tags = ["sdk-python", "regression-test"]
created_pn_count = 5
created_vpc_count = 1

@pytest.fixture(scope="module")
def vpc_api():
    with scw_vcr.use_cassette("vpc_api.yaml"):
        client = Client.from_config_file_and_env()
        api = VpcV2API(client)
        return api, client.default_project_id, region


@pytest.fixture(scope="module")
def vpc(vpc_api):
    api, project_id, region = vpc_api
    with scw_vcr.use_cassette("vpc_create_fixture_setup.yaml"):
        vpc = api.create_vpc(
            enable_routing=True,
            region=region,
            project_id=project_id,
            name=random_name("vpc-test-sdk-python"),
        )
    yield vpc
    with scw_vcr.use_cassette("vpc_delete_fixture_teardown.yaml"):
        api.delete_vpc(vpc_id=vpc.id, region=region)


@pytest.fixture
def private_networks_to_cleanup(vpc_api):
    api, _, _ = vpc_api
    items = []
    yield items
    with scw_vcr.use_cassette("private_networks_delete_cleanup_fixture.yaml"):
        for pn in items:
            api.delete_private_network(private_network_id=pn.id)


@scw_vcr.use_cassette("test_vpc_delete.yaml")
def test_vpc_delete(vpc_api):
    api, project_id, region = vpc_api
    vpc = api.create_vpc(
        enable_routing=True,
        region=region,
        project_id=project_id,
        name=random_name("vpc-test-sdk-python"),
    )

    assert vpc.id is not None
    assert vpc.region == region

    api.delete_vpc(vpc_id=vpc.id)

    with pytest.raises(ScalewayException):
        api.get_vpc(vpc_id=vpc.id)


@scw_vcr.use_cassette("test_vpc_list.yaml")
def test_vpc_list(vpc_api):
    api, _, region = vpc_api
    vpcs = api.list_vp_cs(region=region)
    assert isinstance(vpcs.vpcs, list)
    assert vpcs.total_count >= created_vpc_count


@scw_vcr.use_cassette("test_private_network_create.yaml")
def test_private_network_create(vpc_api, vpc, private_networks_to_cleanup):
    api, project_id, _ = vpc_api
    for i in range(created_pn_count):
        pn = api.create_private_network(
            vpc_id=vpc.id,
            default_route_propagation_enabled=True,
            project_id=project_id,
            name=random_name(f"sdk-python-pn-{i}"),
        )
        private_networks_to_cleanup.append(pn)
        assert pn.vpc_id == vpc.id


@scw_vcr.use_cassette("test_private_network_list.yaml")
def test_private_network_list(vpc_api):
    api, _, region = vpc_api
    networks = api.list_private_networks(region=region)
    assert isinstance(networks.private_networks, list)
    assert networks.total_count >= created_pn_count


@scw_vcr.use_cassette("test_vpc_get.yaml")
def test_vpc_get(vpc_api, vpc):
    api, _, region = vpc_api
    fetched = api.get_vpc(vpc_id=vpc.id, region=region)
    assert fetched is not None
    assert fetched.id == vpc.id


@scw_vcr.use_cassette("test_vpc_update.yaml")
def test_vpc_update(vpc_api, vpc):
    api, _, _ = vpc_api
    updated = api.update_vpc(vpc_id=vpc.id, tags=tags)
    assert updated.tags == tags
    assert updated.id == vpc.id


@scw_vcr.use_cassette("test_vpc_list_all.yaml")
def test_vpc_list_all(vpc_api):
    api, _, _ = vpc_api
    vpcs = api.list_vp_cs_all()
    assert isinstance(vpcs, list)
    assert len(vpcs) >= created_vpc_count
