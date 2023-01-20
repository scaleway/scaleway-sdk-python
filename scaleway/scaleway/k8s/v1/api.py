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
    CreateClusterRequestAutoUpgrade,
    CreateClusterRequestAutoscalerConfig,
    CreateClusterRequestOpenIDConnectConfig,
    CreateClusterRequestPoolConfig,
    CreatePoolRequestUpgradePolicy,
    ListClusterAvailableVersionsResponse,
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
    marshal_UpdateClusterRequest,
    marshal_UpdatePoolRequest,
    marshal_UpgradeClusterRequest,
    marshal_UpgradePoolRequest,
    unmarshal_Cluster,
    unmarshal_Node,
    unmarshal_Pool,
    unmarshal_Version,
    unmarshal_ListClusterAvailableVersionsResponse,
    unmarshal_ListClustersResponse,
    unmarshal_ListNodesResponse,
    unmarshal_ListPoolsResponse,
    unmarshal_ListVersionsResponse,
)


class K8SV1API(API):
    """
    Kapsule API.
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
        This method allows to list all the existing Kubernetes clusters in an account.
        :param region: Region to target. If none is passed will use default region from the config
        :param organization_id: The organization ID on which to filter the returned clusters
        :param project_id: The project ID on which to filter the returned clusters
        :param order_by: The sort order of the returned clusters
        :param page: The page number for the returned clusters
        :param page_size: The maximum number of clusters per page
        :param name: The name on which to filter the returned clusters
        :param status: The status on which to filter the returned clusters
        :param type_: The type on which to filter the returned clusters
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
        This method allows to list all the existing Kubernetes clusters in an account.
        :param region: Region to target. If none is passed will use default region from the config
        :param organization_id: The organization ID on which to filter the returned clusters
        :param project_id: The project ID on which to filter the returned clusters
        :param order_by: The sort order of the returned clusters
        :param page: The page number for the returned clusters
        :param page_size: The maximum number of clusters per page
        :param name: The name on which to filter the returned clusters
        :param status: The status on which to filter the returned clusters
        :param type_: The type on which to filter the returned clusters
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
    ) -> Cluster:
        """
        This method allows to create a new Kubernetes cluster on an account.
        :param region: Region to target. If none is passed will use default region from the config
        :param organization_id: The organization ID where the cluster will be created.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: The project ID where the cluster will be created.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param type_: The type of the cluster (possible values are kapsule, multicloud).
        :param name: The name of the cluster
        :param description: The description of the cluster
        :param tags: The tags associated with the cluster
        :param version: The Kubernetes version of the cluster
        :param cni: The Container Network Interface (CNI) plugin that will run in the cluster
        :param enable_dashboard: The enablement of the Kubernetes Dashboard in the cluster
        :param ingress: The Ingress Controller that will run in the cluster
        :param pools: The pools to be created along with the cluster
        :param autoscaler_config: This field allows to specify some configuration for the autoscaler, which is an implementation of the [cluster-autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler/).
        :param auto_upgrade: This configuration enables to set a specific 2-hour time window in which the cluster can be automatically updated to the latest patch version in the current minor one.
        :param feature_gates: List of feature gates to enable
        :param admission_plugins: List of admission plugins to enable
        :param open_id_connect_config: This feature is in ALPHA state, it may be deleted or modified. This configuration enables to set the [OpenID Connect configuration](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#openid-connect-tokens) of the Kubernetes API server.
        :param apiserver_cert_sans: Additional Subject Alternative Names for the Kubernetes API server certificate
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
        This method allows to get details about a specific Kubernetes cluster.
        :param region: Region to target. If none is passed will use default region from the config
        :param cluster_id: The ID of the requested cluster
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
        :param region: Region to target. If none is passed will use default region from the config
        :param cluster_id: The ID of the requested cluster
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
        This method allows to update a specific Kubernetes cluster. Note that this method is not made to upgrade a Kubernetes cluster.
        :param region: Region to target. If none is passed will use default region from the config
        :param cluster_id: The ID of the cluster to update
        :param name: This field allows to update the external name of the cluster. The internal name (used for instance in hostname) won't change.
        :param description: The new description of the cluster
        :param tags: The new tags associated with the cluster
        :param autoscaler_config: This field allows to update some configuration for the autoscaler, which is an implementation of the [cluster-autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler/).
        :param enable_dashboard: The new value of the Kubernetes Dashboard enablement
        :param ingress: The new Ingress Controller for the cluster
        :param auto_upgrade: The new auto upgrade configuration of the cluster. Note that all fields need to be set.
        :param feature_gates: List of feature gates to enable
        :param admission_plugins: List of admission plugins to enable
        :param open_id_connect_config: This feature is in ALPHA state, it may be deleted or modified. This configuration enables to update the [OpenID Connect configuration](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#openid-connect-tokens) of the Kubernetes API server.
        :param apiserver_cert_sans: Additional Subject Alternative Names for the Kubernetes API server certificate
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
        This method allows to delete a specific cluster and all its associated pools and nodes. Note that this method will not delete any Load Balancers or Block Volumes that are associated with the cluster.
        :param region: Region to target. If none is passed will use default region from the config
        :param cluster_id: The ID of the cluster to delete
        :param with_additional_resources: Set true if you want to delete all volumes (including retain volume type) and loadbalancers whose name start with cluster ID
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
        This method allows to upgrade a specific Kubernetes cluster and/or its associated pools to a specific and supported Kubernetes version.
        :param region: Region to target. If none is passed will use default region from the config
        :param cluster_id: The ID of the cluster to upgrade
        :param version: The new Kubernetes version of the cluster. Note that the version shoud either be a higher patch version of the same minor version or the direct minor version after the current one.
        :param upgrade_pools: This field makes the upgrade upgrades the pool once the Kubernetes master in upgrade.
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

    def list_cluster_available_versions(
        self,
        *,
        cluster_id: str,
        region: Optional[Region] = None,
    ) -> ListClusterAvailableVersionsResponse:
        """
        This method allows to list the versions that a specific Kubernetes cluster is allowed to upgrade to. Note that it will be every patch version greater than the actual one as well a one minor version ahead of the actual one. Upgrades skipping a minor version will not work.
        :param region: Region to target. If none is passed will use default region from the config
        :param cluster_id: The ID of the cluster which the available Kuberentes versions will be listed from
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
        This method allows to download the Kubernetes cluster config file (AKA kubeconfig) for a specific cluster in order to use it with, for instance, `kubectl`. Tips: add `?dl=1` at the end of the URL to directly get the base64 decoded kubeconfig. If not, the kubeconfig will be base64 encoded.

        :param region: Region to target. If none is passed will use default region from the config
        :param cluster_id: The ID of the cluster to download the kubeconfig from
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
        This method allows to reset the admin token for a specific Kubernetes cluster. This will invalidate the old admin token (which will not be usable after) and create a new one. Note that the redownload of the kubeconfig will be necessary to keep interacting with the cluster (if the old admin token was used).
        :param region: Region to target. If none is passed will use default region from the config
        :param cluster_id: The ID of the cluster of which the admin token will be renewed

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
        This method allows to list all the existing pools for a specific Kubernetes cluster.
        :param region: Region to target. If none is passed will use default region from the config
        :param cluster_id: The ID of the cluster from which the pools will be listed from
        :param order_by: The sort order of the returned pools
        :param page: The page number for the returned pools
        :param page_size: The maximum number of pools per page
        :param name: The name on which to filter the returned pools
        :param status: The status on which to filter the returned pools
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
        This method allows to list all the existing pools for a specific Kubernetes cluster.
        :param region: Region to target. If none is passed will use default region from the config
        :param cluster_id: The ID of the cluster from which the pools will be listed from
        :param order_by: The sort order of the returned pools
        :param page: The page number for the returned pools
        :param page_size: The maximum number of pools per page
        :param name: The name on which to filter the returned pools
        :param status: The status on which to filter the returned pools
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
        This method allows to create a new pool in a specific Kubernetes cluster.
        :param region: Region to target. If none is passed will use default region from the config
        :param cluster_id: The ID of the cluster in which the pool will be created
        :param name: The name of the pool
        :param node_type: The node type is the type of Scaleway Instance wanted for the pool. Nodes with insufficient memory are not eligible (DEV1-S, PLAY2-PICO, STARDUST). 'external' is a special node type used to provision instances from other cloud providers.
        :param placement_group_id: The placement group ID in which all the nodes of the pool will be created
        :param autoscaling: The enablement of the autoscaling feature for the pool
        :param size: The size (number of nodes) of the pool
        :param min_size: The minimum size of the pool. Note that this field will be used only when autoscaling is enabled.
        :param max_size: The maximum size of the pool. Note that this field will be used only when autoscaling is enabled.
        :param container_runtime: The customization of the container runtime is available for each pool. Note that `docker` is deprecated since 1.20 and will be removed in 1.24.

        :param autohealing: The enablement of the autohealing feature for the pool
        :param tags: The tags associated with the pool
        :param kubelet_args: The Kubelet arguments to be used by this pool. Note that this feature is to be considered as experimental
        :param upgrade_policy: The Pool upgrade policy
        :param zone: The Zone in which the Pool's node will be spawn in
        :param root_volume_type: The system volume disk type, we provide two different types of volume (`volume_type`):
          - `l_ssd` is a local block storage: your system is stored locally on
            the hypervisor of your node.
          - `b_ssd` is a remote block storage: your system is stored on a
            centralised and resilient cluster.

        :param root_volume_size: The system volume disk size
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
        This method allows to get details about a specific pool.
        :param region: Region to target. If none is passed will use default region from the config
        :param pool_id: The ID of the requested pool
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
        :param region: Region to target. If none is passed will use default region from the config
        :param pool_id: The ID of the requested pool
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
        This method allows to upgrade the Kubernetes version of a specific pool. Note that this will work when the targeted version is the same than the version of the cluster.
        :param region: Region to target. If none is passed will use default region from the config
        :param pool_id: The ID of the pool to upgrade
        :param version: The new Kubernetes version for the pool
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
        This method allows to update some attributes of a specific pool such as the size, the autoscaling enablement, the tags, ...
        :param region: Region to target. If none is passed will use default region from the config
        :param pool_id: The ID of the pool to update
        :param autoscaling: The new value for the enablement of autoscaling for the pool
        :param size: The new size for the pool
        :param min_size: The new minimun size for the pool
        :param max_size: The new maximum size for the pool
        :param autohealing: The new value for the enablement of autohealing for the pool
        :param tags: The new tags associated with the pool
        :param kubelet_args: The new Kubelet arguments to be used by this pool. Note that this feature is to be considered as experimental
        :param upgrade_policy: The Pool upgrade policy
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
        This method allows to delete a specific pool from a cluster, deleting all the nodes associated with it.
        :param region: Region to target. If none is passed will use default region from the config
        :param pool_id: The ID of the pool to delete
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
        This method allows to list all the existing nodes for a specific Kubernetes cluster.
        :param region: Region to target. If none is passed will use default region from the config
        :param cluster_id: The cluster ID from which the nodes will be listed from
        :param pool_id: The pool ID on which to filter the returned nodes
        :param order_by: The sort order of the returned nodes
        :param page: The page number for the returned nodes
        :param page_size: The maximum number of nodes per page
        :param name: The name on which to filter the returned nodes
        :param status: The status on which to filter the returned nodes
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
        This method allows to list all the existing nodes for a specific Kubernetes cluster.
        :param region: Region to target. If none is passed will use default region from the config
        :param cluster_id: The cluster ID from which the nodes will be listed from
        :param pool_id: The pool ID on which to filter the returned nodes
        :param order_by: The sort order of the returned nodes
        :param page: The page number for the returned nodes
        :param page_size: The maximum number of nodes per page
        :param name: The name on which to filter the returned nodes
        :param status: The status on which to filter the returned nodes
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
        This method allows to get details about a specific Kubernetes node.
        :param region: Region to target. If none is passed will use default region from the config
        :param node_id: The ID of the requested node
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
        :param region: Region to target. If none is passed will use default region from the config
        :param node_id: The ID of the requested node
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
        This method allows to replace a specific node. The node will be set cordoned, meaning that scheduling will be disabled. Then the existing pods on the node will be drained and reschedule onto another schedulable node. Then the node will be deleted, and a new one will be created after the deletion. Note that when there is not enough space to reschedule all the pods (in a one node cluster for instance), you may experience some disruption of your applications.
        :param region: Region to target. If none is passed will use default region from the config
        :param node_id: The ID of the node to replace
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
        This method allows to reboot a specific node. This node will frist be cordoned, meaning that scheduling will be disabled. Then the existing pods on the node will be drained and reschedule onto another schedulable node. Note that when there is not enough space to reschedule all the pods (in a one node cluster for instance), you may experience some disruption of your applications.
        :param region: Region to target. If none is passed will use default region from the config
        :param node_id: The ID of the node to reboot
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
        This method allows to delete a specific node. Note that when there is not enough space to reschedule all the pods (in a one node cluster for instance), you may experience some disruption of your applications.
        :param region: Region to target. If none is passed will use default region from the config
        :param node_id: The ID of the node to replace
        :param skip_drain: Skip draining node from its workload
        :param replace: Add a new node after the deletion of this node
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
        This method allows to list all available versions for the creation of a new Kubernetes cluster.
        :param region: Region to target. If none is passed will use default region from the config
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
        This method allows to get a specific Kubernetes version and the details about the version.
        :param region: Region to target. If none is passed will use default region from the config
        :param version_name: The requested version name
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
