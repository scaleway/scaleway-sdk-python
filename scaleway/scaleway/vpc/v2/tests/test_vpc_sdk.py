from typing import Generator

import pytest

from scaleway.vpc.v2 import VpcV2API, VPC, PrivateNetwork, ListVPCsResponse, ListPrivateNetworksResponse
from scaleway_core.api import ScalewayException
from scaleway_core.client import Client
from scaleway_core.utils import random_name
from vcr_config import scw_vcr

region = "fr-par"
tags = ["sdk-python", "regression-test"]
created_pn_count = 5
created_vpc_count = 1


@pytest.fixture(scope="module")
@scw_vcr.use_cassette # type: ignore[misc]
def vpc_api() -> tuple[VpcV2API, str | None, str]:
        client = Client.from_config_file_and_env()
        api = VpcV2API(client)
        return api, client.default_project_id, region


@pytest.fixture(scope="module")
@scw_vcr.use_cassette # type: ignore[misc]
def vpc(vpc_api: tuple[VpcV2API, str, str]) -> Generator[VPC, None, None]:
    api, project_id, region = vpc_api
    vpc = api.create_vpc(
        enable_routing=True,
        region=region,
        project_id=project_id,
        name=random_name("vpc-test-sdk-python"),
    )
    yield vpc
    api.delete_vpc(vpc_id=vpc.id, region=region)


@pytest.fixture
@scw_vcr.use_cassette # type: ignore[misc]
def private_networks_to_cleanup(vpc_api: tuple[VpcV2API, str, str]) -> Generator[list[PrivateNetwork], None, None]:
    api, _, _ = vpc_api
    items: list[PrivateNetwork] = []
    yield items
    for pn in items:
        api.delete_private_network(private_network_id=pn.id)


@scw_vcr.use_cassette # type: ignore[misc]
def test_vpc_delete(vpc_api: tuple[VpcV2API, str, str]) -> None:
    api, project_id, region = vpc_api
    vpc: VPC = api.create_vpc(
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


@scw_vcr.use_cassette # type: ignore[misc]
def test_vpc_list(vpc_api: tuple[VpcV2API, str, str]) -> None:
    api, _, region = vpc_api
    vpcs: ListVPCsResponse = api.list_vp_cs(region=region)
    assert isinstance(vpcs.vpcs, list)
    assert vpcs.total_count >= created_vpc_count


@scw_vcr.use_cassette # type: ignore[misc]
def test_private_network_create(vpc_api: tuple[VpcV2API, str, str], vpc: VPC , private_networks_to_cleanup: list[PrivateNetwork]) -> None:
    api, project_id, _ = vpc_api
    for i in range(created_pn_count):
        pn: PrivateNetwork = api.create_private_network(
            vpc_id=vpc.id,
            default_route_propagation_enabled=True,
            project_id=project_id,
            name=random_name(f"sdk-python-pn-{i}"),
        )
        private_networks_to_cleanup.append(pn)
        assert pn.vpc_id == vpc.id


@scw_vcr.use_cassette # type: ignore[misc]
def test_private_network_list(vpc_api: tuple[VpcV2API, str, str]) -> None:
    api, _, region = vpc_api
    networks: ListPrivateNetworksResponse = api.list_private_networks(region=region)
    assert isinstance(networks.private_networks, list)
    assert networks.total_count >= created_pn_count


@scw_vcr.use_cassette # type: ignore[misc]
def test_vpc_get(vpc_api: tuple[VpcV2API, str, str], vpc: VPC) -> None:
    api, _, region = vpc_api
    fetched_vpc: VPC = api.get_vpc(vpc_id=vpc.id, region=region)
    assert fetched_vpc is not None
    assert fetched_vpc.id == vpc.id


@scw_vcr.use_cassette # type: ignore[misc]
def test_vpc_update(vpc_api: tuple[VpcV2API, str, str], vpc: VPC) -> None:
    api, _, _ = vpc_api
    updated = api.update_vpc(vpc_id=vpc.id, tags=tags)
    assert updated.tags == tags
    assert updated.id == vpc.id


@scw_vcr.use_cassette # type: ignore[misc]
def test_vpc_list_all(vpc_api: tuple[VpcV2API, str, str]) -> None:
    api, _, _ = vpc_api
    vpcs = api.list_vp_cs_all()
    assert isinstance(vpcs, list)
    assert len(vpcs) >= created_vpc_count
