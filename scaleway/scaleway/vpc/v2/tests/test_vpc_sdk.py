from collections.abc import Generator

import pytest

from scaleway.vpc.v2 import (
    VpcV2API,
    VPC,
    PrivateNetwork,
    ListVPCsResponse,
    ListPrivateNetworksResponse,
)
from scaleway_core.api import ScalewayException
from scaleway_core.utils import random_name
from tests.utils import initialize_client_test
from vcr_config import scw_vcr

region = "fr-par"
tags = ["sdk-python", "regression-test"]
created_pn_count = 5
created_vpc_count = 1

# mypy: ignore-errors


@pytest.fixture(scope="module")
@scw_vcr.use_cassette
def vpc_api() -> VpcV2API:
    client = initialize_client_test()
    return VpcV2API(client, bypass_validation=True)


@pytest.fixture(scope="module")
@scw_vcr.use_cassette
def vpc(vpc_api: VpcV2API) -> Generator[VPC, None, None]:
    api = vpc_api
    vpc = api.create_vpc(
        enable_routing=True,
        region=region,
        name=random_name("vpc-test-sdk-python"),
    )
    yield vpc
    api.delete_vpc(vpc_id=vpc.id, region=region)


@pytest.fixture
@scw_vcr.use_cassette
def private_networks_to_cleanup(
    vpc_api: VpcV2API,
) -> Generator[list[PrivateNetwork], None, None]:
    api = vpc_api
    items: list[PrivateNetwork] = []
    yield items
    for pn in items:
        api.delete_private_network(private_network_id=pn.id)


@scw_vcr.use_cassette
def test_vpc_delete(vpc_api: VpcV2API) -> None:
    api = vpc_api
    vpc: VPC = api.create_vpc(
        enable_routing=True,
        region=region,
        name=random_name("vpc-test-sdk-python"),
    )

    assert vpc.id is not None
    assert vpc.region == region

    api.delete_vpc(vpc_id=vpc.id)

    with pytest.raises(ScalewayException):
        api.get_vpc(vpc_id=vpc.id)


@scw_vcr.use_cassette
def test_vpc_list(vpc_api: VpcV2API) -> None:
    api = vpc_api
    vpcs: ListVPCsResponse = api.list_vp_cs(region=region)
    assert isinstance(vpcs.vpcs, list)
    assert vpcs.total_count >= created_vpc_count


@scw_vcr.use_cassette
def test_private_network_create(
    vpc_api: VpcV2API,
    vpc: VPC,
    private_networks_to_cleanup: list[PrivateNetwork],
) -> None:
    api = vpc_api
    for i in range(created_pn_count):
        pn: PrivateNetwork = api.create_private_network(
            vpc_id=vpc.id,
            default_route_propagation_enabled=True,
            name=random_name(f"sdk-python-pn-{i}"),
        )
        private_networks_to_cleanup.append(pn)
        assert pn.vpc_id == vpc.id


@scw_vcr.use_cassette
def test_private_network_list(vpc_api: VpcV2API) -> None:
    api = vpc_api
    networks: ListPrivateNetworksResponse = api.list_private_networks(region=region)
    assert networks.total_count >= created_pn_count


@scw_vcr.use_cassette
def test_vpc_get(vpc_api: VpcV2API, vpc: VPC) -> None:
    api = vpc_api
    fetched_vpc: VPC = api.get_vpc(vpc_id=vpc.id, region=region)
    assert fetched_vpc is not None
    assert fetched_vpc.id == vpc.id


@scw_vcr.use_cassette
def test_vpc_update(vpc_api: VpcV2API, vpc: VPC) -> None:
    api = vpc_api
    updated = api.update_vpc(vpc_id=vpc.id, tags=tags)
    assert updated.tags == tags
    assert updated.id == vpc.id


@scw_vcr.use_cassette
def test_vpc_list_all(vpc_api: VpcV2API) -> None:
    api = vpc_api
    vpcs = api.list_vp_cs_all()
    assert len(vpcs) >= created_vpc_count
