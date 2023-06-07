# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Dict, List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
    ScwFile,
    Zone,
    unmarshal_ScwFile,
)
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages,
    random_name,
    validate_path_param,
    wait_for_resource,
)
from .types import (
    CNI,
    ClusterStatus,
    Ingress,
    ListClustersRequestOrderBy,
    ListNodesRequestOrderBy,
    ListPoolsRequestOrderBy,
    NodeStatus,
    PoolStatus,
    PoolVolumeType,
    Runtime,
    Cluster,
    ClusterType,
    CreateClusterRequestAutoUpgrade,
    CreateClusterRequestAutoscalerConfig,
    CreateClusterRequestOpenIDConnectConfig,
    CreateClusterRequestPoolConfig,
    CreatePoolRequestUpgradePolicy,
    ExternalNode,
    ListClusterAvailableVersionsResponse,
    ListClusterTypesResponse,
    ListClustersResponse,
    ListNodesResponse,
    ListPoolsResponse,
    ListVersionsResponse,
    Node,
    Pool,
    UpdateClusterRequestAutoUpgrade,
    UpdateClusterRequestAutoscalerConfig,
    UpdateClusterRequestOpenIDConnectConfig,
    UpdatePoolRequestUpgradePolicy,
    Version,
    CreateClusterRequest,
    UpdateClusterRequest,
    UpgradeClusterRequest,
    SetClusterTypeRequest,
    MigrateToPrivateNetworkClusterRequest,
    CreatePoolRequest,
    UpgradePoolRequest,
    UpdatePoolRequest,
)
from .content import (
    CLUSTER_TRANSIENT_STATUSES,
    NODE_TRANSIENT_STATUSES,
    POOL_TRANSIENT_STATUSES,
)
from .marshalling import (
    marshal_CreateClusterRequest,
    marshal_CreatePoolRequest,
    marshal_MigrateToPrivateNetworkClusterRequest,
    marshal_SetClusterTypeRequest,
    marshal_UpdateClusterRequest,
    marshal_UpdatePoolRequest,
    marshal_UpgradeClusterRequest,
    marshal_UpgradePoolRequest,
    unmarshal_Cluster,
    unmarshal_Node,
    unmarshal_Pool,
    unmarshal_Version,
    unmarshal_ExternalNode,
    unmarshal_ListClusterAvailableVersionsResponse,
    unmarshal_ListClusterTypesResponse,
    unmarshal_ListClustersResponse,
    unmarshal_ListNodesResponse,
    unmarshal_ListPoolsResponse,
    unmarshal_ListVersionsResponse,
)


class K8SV1API(API):
    """
    Kubernetes API.

    Kubernetes API.
    """

    def list_clusters(
        self,
        *,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        order_by: ListClustersRequestOrderBy = ListClustersRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        status: ClusterStatus = ClusterStatus.UNKNOWN,
        type_: Optional[str] = None,
    ) -> ListClustersResponse:
        """
        List Clusters.
        List all existing Kubernetes clusters in a specific region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Organization ID on which to filter the returned clusters.
        :param project_id: Project ID on which to filter the returned clusters.
        :param order_by: Sort order of returned clusters.
        :param page: Page number to return for clusters, from the paginated results.
        :param page_size: Maximum number of clusters per page.
        :param name: Name to filter on, only clusters containing this substring in their name will be returned.
        :param status: Status to filter on, only clusters with this status will be returned.
        :param type_: Type to filter on, only clusters with this type will be returned.
        :return: :class:`ListClustersResponse <ListClustersResponse>`

        Usage:
        ::

            result = api.list_clusters()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/k8s/v1/regions/{param_region}/clusters",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "status": status,
                "type": type_,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListClustersResponse(res.json())

    def list_clusters_all(
        self,
        *,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        order_by: Optional[ListClustersRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        status: Optional[ClusterStatus] = None,
        type_: Optional[str] = None,
    ) -> List[Cluster]:
        """
        List Clusters.
        List all existing Kubernetes clusters in a specific region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Organization ID on which to filter the returned clusters.
        :param project_id: Project ID on which to filter the returned clusters.
        :param order_by: Sort order of returned clusters.
        :param page: Page number to return for clusters, from the paginated results.
        :param page_size: Maximum number of clusters per page.
        :param name: Name to filter on, only clusters containing this substring in their name will be returned.
        :param status: Status to filter on, only clusters with this status will be returned.
        :param type_: Type to filter on, only clusters with this type will be returned.
        :return: :class:`List[ListClustersResponse] <List[ListClustersResponse]>`

        Usage:
        ::

            result = api.list_clusters_all()
        """

        return fetch_all_pages(
            type=ListClustersResponse,
            key="clusters",
            fetcher=self.list_clusters,
            args={
                "region": region,
                "organization_id": organization_id,
                "project_id": project_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
                "status": status,
                "type_": type_,
            },
        )

    def create_cluster(
        self,
        *,
        type_: str,
        description: str,
        version: str,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        cni: CNI = CNI.UNKNOWN_CNI,
        enable_dashboard: Optional[bool] = None,
        ingress: Optional[Ingress] = None,
        pools: Optional[List[CreateClusterRequestPoolConfig]] = None,
        autoscaler_config: Optional[CreateClusterRequestAutoscalerConfig] = None,
        auto_upgrade: Optional[CreateClusterRequestAutoUpgrade] = None,
        feature_gates: Optional[List[str]] = None,
        admission_plugins: Optional[List[str]] = None,
        open_id_connect_config: Optional[
            CreateClusterRequestOpenIDConnectConfig
        ] = None,
        apiserver_cert_sans: Optional[List[str]] = None,
        private_network_id: Optional[str] = None,
    ) -> Cluster:
        """
        Create a new Cluster.
        Create a new Kubernetes cluster in a Scaleway region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Organization ID in which the cluster will be created.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Project ID in which the cluster will be created.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param type_: Type of the cluster (possible values are kapsule, multicloud, kapsule-dedicated-8, kapsule-dedicated-16).
        :param name: Cluster name.
        :param description: Cluster description.
        :param tags: Tags associated with the cluster.
        :param version: Kubernetes version of the cluster.
        :param cni: Container Network Interface (CNI) plugin running in the cluster.
        :param enable_dashboard: Defines whether the Kubernetes Dashboard is enabled in the cluster.
        :param ingress: Ingress Controller running in the cluster (deprecated feature).
        :param pools: Pools created along with the cluster.
        :param autoscaler_config: Autoscaler configuration for the cluster. It allows you to set (to an extent) your preferred autoscaler configuration, which is an implementation of the cluster-autoscaler (https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler/).
        :param auto_upgrade: Auto upgrade configuration of the cluster. This configuration enables to set a specific 2-hour time window in which the cluster can be automatically updated to the latest patch version.
        :param feature_gates: List of feature gates to enable.
        :param admission_plugins: List of admission plugins to enable.
        :param open_id_connect_config: OpenID Connect configuration of the cluster. This configuration enables to update the OpenID Connect configuration of the Kubernetes API server.
        :param apiserver_cert_sans: Additional Subject Alternative Names for the Kubernetes API server certificate.
        :param private_network_id: Private network ID for internal cluster communication (cannot be changed later).
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = api.create_cluster(
                type_="example",
                description="example",
                version="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/k8s/v1/regions/{param_region}/clusters",
            body=marshal_CreateClusterRequest(
                CreateClusterRequest(
                    type_=type_,
                    description=description,
                    version=version,
                    region=region,
                    organization_id=organization_id,
                    project_id=project_id,
                    name=name or random_name(prefix="k8s"),
                    tags=tags,
                    cni=cni,
                    enable_dashboard=enable_dashboard,
                    ingress=ingress,
                    pools=pools,
                    autoscaler_config=autoscaler_config,
                    auto_upgrade=auto_upgrade,
                    feature_gates=feature_gates,
                    admission_plugins=admission_plugins,
                    open_id_connect_config=open_id_connect_config,
                    apiserver_cert_sans=apiserver_cert_sans,
                    private_network_id=private_network_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Cluster(res.json())

    def get_cluster(
        self,
        *,
        cluster_id: str,
        region: Optional[Region] = None,
    ) -> Cluster:
        """
        Get a Cluster.
        Retrieve information about a specific Kubernetes cluster.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cluster_id: ID of the requested cluster.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = api.get_cluster(cluster_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "GET",
            f"/k8s/v1/regions/{param_region}/clusters/{param_cluster_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Cluster(res.json())

    def wait_for_cluster(
        self,
        *,
        cluster_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Cluster, bool]] = None,
    ) -> Cluster:
        """
        Waits for :class:`Cluster <Cluster>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cluster_id: ID of the requested cluster.
        :param options: The options for the waiter
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = api.wait_for_cluster(cluster_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in CLUSTER_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_cluster,
            options=options,
            args={
                "cluster_id": cluster_id,
                "region": region,
            },
        )

    def update_cluster(
        self,
        *,
        cluster_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        autoscaler_config: Optional[UpdateClusterRequestAutoscalerConfig] = None,
        enable_dashboard: Optional[bool] = None,
        ingress: Optional[Ingress] = None,
        auto_upgrade: Optional[UpdateClusterRequestAutoUpgrade] = None,
        feature_gates: Optional[List[str]] = None,
        admission_plugins: Optional[List[str]] = None,
        open_id_connect_config: Optional[
            UpdateClusterRequestOpenIDConnectConfig
        ] = None,
        apiserver_cert_sans: Optional[List[str]] = None,
    ) -> Cluster:
        """
        Update a Cluster.
        Update information on a specific Kubernetes cluster. You can update details such as its name, description, tags and configuration. To upgrade a cluster, you will need to use the dedicated endpoint.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cluster_id: ID of the cluster to update.
        :param name: New external name for the cluster.
        :param description: New description for the cluster.
        :param tags: New tags associated with the cluster.
        :param autoscaler_config: New autoscaler config for the cluster.
        :param enable_dashboard: New value for the Kubernetes Dashboard enablement.
        :param ingress: New Ingress Controller for the cluster (deprecated feature).
        :param auto_upgrade: New auto upgrade configuration for the cluster. Note that all fields need to be set.
        :param feature_gates: List of feature gates to enable.
        :param admission_plugins: List of admission plugins to enable.
        :param open_id_connect_config: OpenID Connect configuration of the cluster. This configuration enables to update the OpenID Connect configuration of the Kubernetes API server.
        :param apiserver_cert_sans: Additional Subject Alternative Names for the Kubernetes API server certificate.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = api.update_cluster(cluster_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "PATCH",
            f"/k8s/v1/regions/{param_region}/clusters/{param_cluster_id}",
            body=marshal_UpdateClusterRequest(
                UpdateClusterRequest(
                    cluster_id=cluster_id,
                    region=region,
                    name=name,
                    description=description,
                    tags=tags,
                    autoscaler_config=autoscaler_config,
                    enable_dashboard=enable_dashboard,
                    ingress=ingress,
                    auto_upgrade=auto_upgrade,
                    feature_gates=feature_gates,
                    admission_plugins=admission_plugins,
                    open_id_connect_config=open_id_connect_config,
                    apiserver_cert_sans=apiserver_cert_sans,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Cluster(res.json())

    def delete_cluster(
        self,
        *,
        cluster_id: str,
        with_additional_resources: bool,
        region: Optional[Region] = None,
    ) -> Cluster:
        """
        Delete a Cluster.
        Delete a specific Kubernetes cluster and all its associated pools and nodes. Note that this method will not delete any Load Balancer or Block Volume that are associated with the cluster.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cluster_id: ID of the cluster to delete.
        :param with_additional_resources: Defines whether all volumes (including retain volume type), empty Private Networks and Load Balancers with a name starting with the cluster ID will also be deleted.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = api.delete_cluster(
                cluster_id="example",
                with_additional_resources=True,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "DELETE",
            f"/k8s/v1/regions/{param_region}/clusters/{param_cluster_id}",
            params={
                "with_additional_resources": with_additional_resources,
            },
        )

        self._throw_on_error(res)
        return unmarshal_Cluster(res.json())

    def upgrade_cluster(
        self,
        *,
        cluster_id: str,
        version: str,
        upgrade_pools: bool,
        region: Optional[Region] = None,
    ) -> Cluster:
        """
        Upgrade a Cluster.
        Upgrade a specific Kubernetes cluster and possibly its associated pools to a specific and supported Kubernetes version.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cluster_id: ID of the cluster to upgrade.
        :param version: New Kubernetes version of the cluster. Note that the version should either be a higher patch version of the same minor version or the direct minor version after the current one.
        :param upgrade_pools: Defines whether pools will also be upgraded once the control plane is upgraded.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = api.upgrade_cluster(
                cluster_id="example",
                version="example",
                upgrade_pools=True,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "POST",
            f"/k8s/v1/regions/{param_region}/clusters/{param_cluster_id}/upgrade",
            body=marshal_UpgradeClusterRequest(
                UpgradeClusterRequest(
                    cluster_id=cluster_id,
                    version=version,
                    upgrade_pools=upgrade_pools,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Cluster(res.json())

    def set_cluster_type(
        self,
        *,
        cluster_id: str,
        type_: str,
        region: Optional[Region] = None,
    ) -> Cluster:
        """
        Change the Cluster type.
        Change the type of a specific Kubernetes cluster.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cluster_id: ID of the cluster to migrate from one type to another.
        :param type_: Type of the cluster. Note that some migrations are not possible (please refer to product documentation).
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = api.set_cluster_type(
                cluster_id="example",
                type_="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "POST",
            f"/k8s/v1/regions/{param_region}/clusters/{param_cluster_id}/set-type",
            body=marshal_SetClusterTypeRequest(
                SetClusterTypeRequest(
                    cluster_id=cluster_id,
                    type_=type_,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Cluster(res.json())

    def list_cluster_available_versions(
        self,
        *,
        cluster_id: str,
        region: Optional[Region] = None,
    ) -> ListClusterAvailableVersionsResponse:
        """
        List available versions for a Cluster.
        List the versions that a specific Kubernetes cluster is allowed to upgrade to. Results will include every patch version greater than the current patch, as well as one minor version ahead of the current version. Any upgrade skipping a minor version will not work.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cluster_id: Cluster ID for which the available Kubernetes versions will be listed.
        :return: :class:`ListClusterAvailableVersionsResponse <ListClusterAvailableVersionsResponse>`

        Usage:
        ::

            result = api.list_cluster_available_versions(cluster_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "GET",
            f"/k8s/v1/regions/{param_region}/clusters/{param_cluster_id}/available-versions",
        )

        self._throw_on_error(res)
        return unmarshal_ListClusterAvailableVersionsResponse(res.json())

    def _get_cluster_kube_config(
        self,
        *,
        cluster_id: str,
        region: Optional[Region] = None,
    ) -> Optional[ScwFile]:
        """
        Download the kubeconfig for a Cluster.
        Download the Kubernetes cluster config file (also known as `kubeconfig`) for a specific cluster to use it with `kubectl`.
        Tip: add `?dl=1` at the end of the URL to directly retrieve the base64 decoded kubeconfig. If you choose not to, the kubeconfig will be base64 encoded.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cluster_id: Cluster ID for which to download the kubeconfig.
        :return: :class:`Optional[ScwFile] <Optional[ScwFile]>`

        Usage:
        ::

            result = api._get_cluster_kube_config(cluster_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "GET",
            f"/k8s/v1/regions/{param_region}/clusters/{param_cluster_id}/kubeconfig",
        )

        self._throw_on_error(res)
        json = res.json()
        return unmarshal_ScwFile(json) if json is not None else None

    def reset_cluster_admin_token(
        self,
        *,
        cluster_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Reset the admin token of a Cluster.
        Reset the admin token for a specific Kubernetes cluster. This will revoke the old admin token (which will not be usable afterwards) and create a new one. Note that you will need to download kubeconfig again to keep interacting with the cluster.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cluster_id: Cluster ID on which the admin token will be renewed.

        Usage:
        ::

            result = api.reset_cluster_admin_token(cluster_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "POST",
            f"/k8s/v1/regions/{param_region}/clusters/{param_cluster_id}/reset-admin-token",
        )

        self._throw_on_error(res)
        return None

    def migrate_to_private_network_cluster(
        self,
        *,
        cluster_id: str,
        private_network_id: str,
        region: Optional[Region] = None,
    ) -> Cluster:
        """
        Migrate an existing cluster to a Private Network cluster.
        Migrate a cluster that was created before the release of Private Network clusters to a new one with a Private Network.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cluster_id: ID of the cluster to migrate.
        :param private_network_id: ID of the Private Network to link to the cluster.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = api.migrate_to_private_network_cluster(
                cluster_id="example",
                private_network_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "POST",
            f"/k8s/v1/regions/{param_region}/clusters/{param_cluster_id}/migrate-to-private-network",
            body=marshal_MigrateToPrivateNetworkClusterRequest(
                MigrateToPrivateNetworkClusterRequest(
                    cluster_id=cluster_id,
                    private_network_id=private_network_id,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Cluster(res.json())

    def list_pools(
        self,
        *,
        cluster_id: str,
        region: Optional[Region] = None,
        order_by: ListPoolsRequestOrderBy = ListPoolsRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        status: PoolStatus = PoolStatus.UNKNOWN,
    ) -> ListPoolsResponse:
        """
        List Pools in a Cluster.
        List all the existing pools for a specific Kubernetes cluster.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cluster_id: ID of the cluster whose pools will be listed.
        :param order_by: Sort order of returned pools.
        :param page: Page number for the returned pools.
        :param page_size: Maximum number of pools per page.
        :param name: Name to filter on, only pools containing this substring in their name will be returned.
        :param status: Status to filter on, only pools with this status will be returned.
        :return: :class:`ListPoolsResponse <ListPoolsResponse>`

        Usage:
        ::

            result = api.list_pools(cluster_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "GET",
            f"/k8s/v1/regions/{param_region}/clusters/{param_cluster_id}/pools",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "status": status,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPoolsResponse(res.json())

    def list_pools_all(
        self,
        *,
        cluster_id: str,
        region: Optional[Region] = None,
        order_by: Optional[ListPoolsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        status: Optional[PoolStatus] = None,
    ) -> List[Pool]:
        """
        List Pools in a Cluster.
        List all the existing pools for a specific Kubernetes cluster.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cluster_id: ID of the cluster whose pools will be listed.
        :param order_by: Sort order of returned pools.
        :param page: Page number for the returned pools.
        :param page_size: Maximum number of pools per page.
        :param name: Name to filter on, only pools containing this substring in their name will be returned.
        :param status: Status to filter on, only pools with this status will be returned.
        :return: :class:`List[ListPoolsResponse] <List[ListPoolsResponse]>`

        Usage:
        ::

            result = api.list_pools_all(cluster_id="example")
        """

        return fetch_all_pages(
            type=ListPoolsResponse,
            key="pools",
            fetcher=self.list_pools,
            args={
                "cluster_id": cluster_id,
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
                "status": status,
            },
        )

    def create_pool(
        self,
        *,
        cluster_id: str,
        node_type: str,
        autoscaling: bool,
        size: int,
        container_runtime: Runtime,
        autohealing: bool,
        root_volume_type: PoolVolumeType,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        placement_group_id: Optional[str] = None,
        min_size: Optional[int] = None,
        max_size: Optional[int] = None,
        tags: Optional[List[str]] = None,
        kubelet_args: Optional[Dict[str, str]] = None,
        upgrade_policy: Optional[CreatePoolRequestUpgradePolicy] = None,
        zone: Optional[Zone] = None,
        root_volume_size: Optional[int] = None,
    ) -> Pool:
        """
        Create a new Pool in a Cluster.
        Create a new pool in a specific Kubernetes cluster.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cluster_id: Cluster ID to which the pool will be attached.
        :param name: Pool name.
        :param node_type: Node type is the type of Scaleway Instance wanted for the pool. Nodes with insufficient memory are not eligible (DEV1-S, PLAY2-PICO, STARDUST). 'external' is a special node type used to provision instances from other cloud providers in a Kosmos Cluster.
        :param placement_group_id: Placement group ID in which all the nodes of the pool will be created.
        :param autoscaling: Defines whether the autoscaling feature is enabled for the pool.
        :param size: Size (number of nodes) of the pool.
        :param min_size: Defines the minimum size of the pool. Note that this field is only used when autoscaling is enabled on the pool.
        :param max_size: Defines the maximum size of the pool. Note that this field is only used when autoscaling is enabled on the pool.
        :param container_runtime: Customization of the container runtime is available for each pool. Note that `docker` has been deprecated since version 1.20 and will be removed by version 1.24.
        :param autohealing: Defines whether the autohealing feature is enabled for the pool.
        :param tags: Tags associated with the pool.
        :param kubelet_args: Kubelet arguments to be used by this pool. Note that this feature is experimental.
        :param upgrade_policy: Pool upgrade policy.
        :param zone: Zone in which the pool's nodes will be spawned.
        :param root_volume_type: Defines the system volume disk type. Two different types of volume (`volume_type`) are provided: `l_ssd` is a local block storage which means your system is stored locally on your node's hypervisor. `b_ssd` is a remote block storage which means your system is stored on a centralized and resilient cluster.
        :param root_volume_size: System volume disk size.
        :return: :class:`Pool <Pool>`

        Usage:
        ::

            result = api.create_pool(
                cluster_id="example",
                node_type="example",
                autoscaling=True,
                size=1,
                container_runtime=unknown_runtime,
                autohealing=True,
                root_volume_type=default_volume_type,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "POST",
            f"/k8s/v1/regions/{param_region}/clusters/{param_cluster_id}/pools",
            body=marshal_CreatePoolRequest(
                CreatePoolRequest(
                    cluster_id=cluster_id,
                    node_type=node_type,
                    autoscaling=autoscaling,
                    size=size,
                    container_runtime=container_runtime,
                    autohealing=autohealing,
                    root_volume_type=root_volume_type,
                    region=region,
                    name=name or random_name(prefix="pool"),
                    placement_group_id=placement_group_id,
                    min_size=min_size,
                    max_size=max_size,
                    tags=tags,
                    kubelet_args=kubelet_args,
                    upgrade_policy=upgrade_policy,
                    zone=zone,
                    root_volume_size=root_volume_size,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Pool(res.json())

    def get_pool(
        self,
        *,
        pool_id: str,
        region: Optional[Region] = None,
    ) -> Pool:
        """
        Get a Pool in a Cluster.
        Retrieve details about a specific pool in a Kubernetes cluster.
        :param region: Region to target. If none is passed will use default region from the config.
        :param pool_id: ID of the requested pool.
        :return: :class:`Pool <Pool>`

        Usage:
        ::

            result = api.get_pool(pool_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_pool_id = validate_path_param("pool_id", pool_id)

        res = self._request(
            "GET",
            f"/k8s/v1/regions/{param_region}/pools/{param_pool_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Pool(res.json())

    def wait_for_pool(
        self,
        *,
        pool_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Pool, bool]] = None,
    ) -> Pool:
        """
        Waits for :class:`Pool <Pool>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config.
        :param pool_id: ID of the requested pool.
        :param options: The options for the waiter
        :return: :class:`Pool <Pool>`

        Usage:
        ::

            result = api.wait_for_pool(pool_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in POOL_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_pool,
            options=options,
            args={
                "pool_id": pool_id,
                "region": region,
            },
        )

    def upgrade_pool(
        self,
        *,
        pool_id: str,
        version: str,
        region: Optional[Region] = None,
    ) -> Pool:
        """
        Upgrade a Pool in a Cluster.
        Upgrade the Kubernetes version of a specific pool. Note that it only works if the targeted version matches the cluster's version.
        :param region: Region to target. If none is passed will use default region from the config.
        :param pool_id: ID of the pool to upgrade.
        :param version: New Kubernetes version for the pool.
        :return: :class:`Pool <Pool>`

        Usage:
        ::

            result = api.upgrade_pool(
                pool_id="example",
                version="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_pool_id = validate_path_param("pool_id", pool_id)

        res = self._request(
            "POST",
            f"/k8s/v1/regions/{param_region}/pools/{param_pool_id}/upgrade",
            body=marshal_UpgradePoolRequest(
                UpgradePoolRequest(
                    pool_id=pool_id,
                    version=version,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Pool(res.json())

    def update_pool(
        self,
        *,
        pool_id: str,
        region: Optional[Region] = None,
        autoscaling: Optional[bool] = None,
        size: Optional[int] = None,
        min_size: Optional[int] = None,
        max_size: Optional[int] = None,
        autohealing: Optional[bool] = None,
        tags: Optional[List[str]] = None,
        kubelet_args: Optional[Dict[str, str]] = None,
        upgrade_policy: Optional[UpdatePoolRequestUpgradePolicy] = None,
    ) -> Pool:
        """
        Update a Pool in a Cluster.
        Update the attributes of a specific pool, such as its desired size, autoscaling settings, and tags.
        :param region: Region to target. If none is passed will use default region from the config.
        :param pool_id: ID of the pool to update.
        :param autoscaling: New value for the pool autoscaling enablement.
        :param size: New desired pool size.
        :param min_size: New minimum size for the pool.
        :param max_size: New maximum size for the pool.
        :param autohealing: New value for the pool autohealing enablement.
        :param tags: New tags associated with the pool.
        :param kubelet_args: New Kubelet arguments to be used by this pool. Note that this feature is experimental.
        :param upgrade_policy: New upgrade policy for the pool.
        :return: :class:`Pool <Pool>`

        Usage:
        ::

            result = api.update_pool(pool_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_pool_id = validate_path_param("pool_id", pool_id)

        res = self._request(
            "PATCH",
            f"/k8s/v1/regions/{param_region}/pools/{param_pool_id}",
            body=marshal_UpdatePoolRequest(
                UpdatePoolRequest(
                    pool_id=pool_id,
                    region=region,
                    autoscaling=autoscaling,
                    size=size,
                    min_size=min_size,
                    max_size=max_size,
                    autohealing=autohealing,
                    tags=tags,
                    kubelet_args=kubelet_args,
                    upgrade_policy=upgrade_policy,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Pool(res.json())

    def delete_pool(
        self,
        *,
        pool_id: str,
        region: Optional[Region] = None,
    ) -> Pool:
        """
        Delete a Pool in a Cluster.
        Delete a specific pool from a cluster. Note that all the pool's nodes will also be deleted.
        :param region: Region to target. If none is passed will use default region from the config.
        :param pool_id: ID of the pool to delete.
        :return: :class:`Pool <Pool>`

        Usage:
        ::

            result = api.delete_pool(pool_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_pool_id = validate_path_param("pool_id", pool_id)

        res = self._request(
            "DELETE",
            f"/k8s/v1/regions/{param_region}/pools/{param_pool_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Pool(res.json())

    def create_external_node(
        self,
        *,
        pool_id: str,
        region: Optional[Region] = None,
    ) -> ExternalNode:
        """
        Create a Kosmos node.
        Retrieve metadata for a Kosmos node. This method is not intended to be called by end users but rather programmatically by the kapsule-node-agent.
        :param region: Region to target. If none is passed will use default region from the config.
        :param pool_id:
        :return: :class:`ExternalNode <ExternalNode>`

        Usage:
        ::

            result = api.create_external_node(pool_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_pool_id = validate_path_param("pool_id", pool_id)

        res = self._request(
            "POST",
            f"/k8s/v1/regions/{param_region}/pools/{param_pool_id}/external-nodes",
        )

        self._throw_on_error(res)
        return unmarshal_ExternalNode(res.json())

    def list_nodes(
        self,
        *,
        cluster_id: str,
        region: Optional[Region] = None,
        pool_id: Optional[str] = None,
        order_by: ListNodesRequestOrderBy = ListNodesRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        status: NodeStatus = NodeStatus.UNKNOWN,
    ) -> ListNodesResponse:
        """
        List Nodes in a Cluster.
        List all the existing nodes for a specific Kubernetes cluster.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cluster_id: Cluster ID from which the nodes will be listed from.
        :param pool_id: Pool ID on which to filter the returned nodes.
        :param order_by: Sort order of the returned nodes.
        :param page: Page number for the returned nodes.
        :param page_size: Maximum number of nodes per page.
        :param name: Name to filter on, only nodes containing this substring in their name will be returned.
        :param status: Status to filter on, only nodes with this status will be returned.
        :return: :class:`ListNodesResponse <ListNodesResponse>`

        Usage:
        ::

            result = api.list_nodes(cluster_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "GET",
            f"/k8s/v1/regions/{param_region}/clusters/{param_cluster_id}/nodes",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "pool_id": pool_id,
                "status": status,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListNodesResponse(res.json())

    def list_nodes_all(
        self,
        *,
        cluster_id: str,
        region: Optional[Region] = None,
        pool_id: Optional[str] = None,
        order_by: Optional[ListNodesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        status: Optional[NodeStatus] = None,
    ) -> List[Node]:
        """
        List Nodes in a Cluster.
        List all the existing nodes for a specific Kubernetes cluster.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cluster_id: Cluster ID from which the nodes will be listed from.
        :param pool_id: Pool ID on which to filter the returned nodes.
        :param order_by: Sort order of the returned nodes.
        :param page: Page number for the returned nodes.
        :param page_size: Maximum number of nodes per page.
        :param name: Name to filter on, only nodes containing this substring in their name will be returned.
        :param status: Status to filter on, only nodes with this status will be returned.
        :return: :class:`List[ListNodesResponse] <List[ListNodesResponse]>`

        Usage:
        ::

            result = api.list_nodes_all(cluster_id="example")
        """

        return fetch_all_pages(
            type=ListNodesResponse,
            key="nodes",
            fetcher=self.list_nodes,
            args={
                "cluster_id": cluster_id,
                "region": region,
                "pool_id": pool_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
                "status": status,
            },
        )

    def get_node(
        self,
        *,
        node_id: str,
        region: Optional[Region] = None,
    ) -> Node:
        """
        Get a Node in a Cluster.
        Retrieve details about a specific Kubernetes Node.
        :param region: Region to target. If none is passed will use default region from the config.
        :param node_id: ID of the requested node.
        :return: :class:`Node <Node>`

        Usage:
        ::

            result = api.get_node(node_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_node_id = validate_path_param("node_id", node_id)

        res = self._request(
            "GET",
            f"/k8s/v1/regions/{param_region}/nodes/{param_node_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Node(res.json())

    def wait_for_node(
        self,
        *,
        node_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Node, bool]] = None,
    ) -> Node:
        """
        Waits for :class:`Node <Node>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config.
        :param node_id: ID of the requested node.
        :param options: The options for the waiter
        :return: :class:`Node <Node>`

        Usage:
        ::

            result = api.wait_for_node(node_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in NODE_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_node,
            options=options,
            args={
                "node_id": node_id,
                "region": region,
            },
        )

    def replace_node(
        self,
        *,
        node_id: str,
        region: Optional[Region] = None,
    ) -> Node:
        """
        Replace a Node in a Cluster.
        Replace a specific Node. The node will first be cordoned (scheduling will be disabled on it). The existing pods on the node will then be drained and rescheduled onto another schedulable node. Note that when there is not enough space to reschedule all the pods (such as in a one-node cluster), disruption of your applications can be expected.
        :param region: Region to target. If none is passed will use default region from the config.
        :param node_id: ID of the node to replace.
        :return: :class:`Node <Node>`
        :deprecated

        Usage:
        ::

            result = api.replace_node(node_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_node_id = validate_path_param("node_id", node_id)

        res = self._request(
            "POST",
            f"/k8s/v1/regions/{param_region}/nodes/{param_node_id}/replace",
        )

        self._throw_on_error(res)
        return unmarshal_Node(res.json())

    def reboot_node(
        self,
        *,
        node_id: str,
        region: Optional[Region] = None,
    ) -> Node:
        """
        Reboot a Node in a Cluster.
        Reboot a specific Node. The node will first be cordoned (scheduling will be disabled on it). The existing pods on the node will then be drained and rescheduled onto another schedulable node. Note that when there is not enough space to reschedule all the pods (such as in a one-node cluster), disruption of your applications can be expected.
        :param region: Region to target. If none is passed will use default region from the config.
        :param node_id: ID of the node to reboot.
        :return: :class:`Node <Node>`

        Usage:
        ::

            result = api.reboot_node(node_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_node_id = validate_path_param("node_id", node_id)

        res = self._request(
            "POST",
            f"/k8s/v1/regions/{param_region}/nodes/{param_node_id}/reboot",
        )

        self._throw_on_error(res)
        return unmarshal_Node(res.json())

    def delete_node(
        self,
        *,
        node_id: str,
        skip_drain: bool,
        replace: bool,
        region: Optional[Region] = None,
    ) -> Node:
        """
        Delete a Node in a Cluster.
        Delete a specific Node. Note that when there is not enough space to reschedule all the pods (such as in a one-node cluster), disruption of your applications can be expected.
        :param region: Region to target. If none is passed will use default region from the config.
        :param node_id: ID of the node to replace.
        :param skip_drain: Skip draining node from its workload.
        :param replace: Add a new node after the deletion of this node.
        :return: :class:`Node <Node>`

        Usage:
        ::

            result = api.delete_node(
                node_id="example",
                skip_drain=True,
                replace=True,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_node_id = validate_path_param("node_id", node_id)

        res = self._request(
            "DELETE",
            f"/k8s/v1/regions/{param_region}/nodes/{param_node_id}",
            params={
                "replace": replace,
                "skip_drain": skip_drain,
            },
        )

        self._throw_on_error(res)
        return unmarshal_Node(res.json())

    def list_versions(
        self,
        *,
        region: Optional[Region] = None,
    ) -> ListVersionsResponse:
        """
        List all available Versions.
        List all available versions for the creation of a new Kubernetes cluster.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ListVersionsResponse <ListVersionsResponse>`

        Usage:
        ::

            result = api.list_versions()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/k8s/v1/regions/{param_region}/versions",
        )

        self._throw_on_error(res)
        return unmarshal_ListVersionsResponse(res.json())

    def get_version(
        self,
        *,
        version_name: str,
        region: Optional[Region] = None,
    ) -> Version:
        """
        Get a Version.
        Retrieve a specific Kubernetes version and its details.
        :param region: Region to target. If none is passed will use default region from the config.
        :param version_name: Requested version name.
        :return: :class:`Version <Version>`

        Usage:
        ::

            result = api.get_version(version_name="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_version_name = validate_path_param("version_name", version_name)

        res = self._request(
            "GET",
            f"/k8s/v1/regions/{param_region}/versions/{param_version_name}",
        )

        self._throw_on_error(res)
        return unmarshal_Version(res.json())

    def list_cluster_types(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListClusterTypesResponse:
        """
        List cluster types.
        List available cluster types and their technical details.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number, from the paginated results, to return for cluster-types.
        :param page_size: Maximum number of clusters per page.
        :return: :class:`ListClusterTypesResponse <ListClusterTypesResponse>`

        Usage:
        ::

            result = api.list_cluster_types()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/k8s/v1/regions/{param_region}/cluster-types",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListClusterTypesResponse(res.json())

    def list_cluster_types_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ClusterType]:
        """
        List cluster types.
        List available cluster types and their technical details.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number, from the paginated results, to return for cluster-types.
        :param page_size: Maximum number of clusters per page.
        :return: :class:`List[ListClusterTypesResponse] <List[ListClusterTypesResponse]>`

        Usage:
        ::

            result = api.list_cluster_types_all()
        """

        return fetch_all_pages(
            type=ListClusterTypesResponse,
            key="cluster_types",
            fetcher=self.list_cluster_types,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
            },
        )
