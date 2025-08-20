from typing import Any, Generator

import pytest

from scaleway.k8s.v1 import K8SV1API, CNI
from scaleway.vpc.v2 import VpcV2API, PrivateNetwork
from scaleway_core.api import ScalewayException
from tests.utils import initialize_client_test
from vcr_config import scw_vcr

# mypy: ignore-errors


@pytest.fixture(scope="module")
@scw_vcr.use_cassette
def k8s_api() -> K8SV1API:
    client = initialize_client_test()
    return K8SV1API(client, bypass_validation=True)


@pytest.fixture(scope="module")
@scw_vcr.use_cassette
def private_network() -> Generator[PrivateNetwork, Any, None]:
    client = initialize_client_test()
    vpc_api = VpcV2API(client, bypass_validation=True)
    vpc = vpc_api.create_vpc(enable_routing=False)
    pn = vpc_api.create_private_network(
        vpc_id=vpc.id, default_route_propagation_enabled=True
    )
    yield pn
    vpc_api.delete_vpc(vpc_id=vpc.id)


def safe_wait_for_cluster(k8s_api: K8SV1API, cluster_id: str):
    try:
        return k8s_api.wait_for_cluster(cluster_id=cluster_id)
    except ScalewayException as e:
        err_type = getattr(e, "type", None) or getattr(e, "error", None)
        if err_type == "not_found" or "not found" in str(e).lower():
            return None
        raise


@scw_vcr.use_cassette
def test_k8s_cluster_list(k8s_api: K8SV1API, private_network: PrivateNetwork) -> None:
    cluster = k8s_api.create_cluster(
        type_="kapsule",
        version="1.32.7",
        cni=CNI.CILIUM,
        description="",
        private_network_id=private_network.id,
    )
    assert cluster.id is not None

    clusters = k8s_api.list_clusters()
    assert clusters.total_count >= 1

    k8s_api.delete_cluster(cluster_id=cluster.id, with_additional_resources=True)
    cluster = safe_wait_for_cluster(k8s_api=k8s_api, cluster_id=cluster.id)
    assert cluster is None
