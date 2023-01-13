# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Awaitable, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    ScwFile,
    Zone,
    unmarshal_ScwFile,
)
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages_async,
    random_name,
    validate_path_param,
    wait_for_resource_async,
)
from .types import (
    ListClustersRequestOrderBy,
    ACLRule,
    ACLRuleSpec,
    AddAclRulesResponse,
    AddEndpointsResponse,
    Cluster,
    ClusterMetricsResponse,
    ClusterSetting,
    ClusterSettingsResponse,
    ClusterVersion,
    Endpoint,
    EndpointSpec,
    EndpointSpecPrivateNetworkSpec,
    EndpointSpecPublicNetworkSpec,
    ListClusterVersionsResponse,
    ListClustersResponse,
    ListNodeTypesResponse,
    NodeType,
    SetAclRulesResponse,
    SetEndpointsResponse,
    CreateClusterRequest,
    UpdateClusterRequest,
    MigrateClusterRequest,
    AddClusterSettingsRequest,
    SetClusterSettingsRequest,
    SetAclRulesRequest,
    AddAclRulesRequest,
    SetEndpointsRequest,
    AddEndpointsRequest,
    UpdateEndpointRequest,
)
from .content import (
    CLUSTER_TRANSIENT_STATUSES,
)
from .marshalling import (
    marshal_AddAclRulesRequest,
    marshal_AddClusterSettingsRequest,
    marshal_AddEndpointsRequest,
    marshal_CreateClusterRequest,
    marshal_MigrateClusterRequest,
    marshal_SetAclRulesRequest,
    marshal_SetClusterSettingsRequest,
    marshal_SetEndpointsRequest,
    marshal_UpdateClusterRequest,
    marshal_UpdateEndpointRequest,
    unmarshal_ACLRule,
    unmarshal_Endpoint,
    unmarshal_Cluster,
    unmarshal_AddAclRulesResponse,
    unmarshal_AddEndpointsResponse,
    unmarshal_ClusterMetricsResponse,
    unmarshal_ClusterSettingsResponse,
    unmarshal_ListClusterVersionsResponse,
    unmarshal_ListClustersResponse,
    unmarshal_ListNodeTypesResponse,
    unmarshal_SetAclRulesResponse,
    unmarshal_SetEndpointsResponse,
)


class RedisV1API(API):
    """
    Managed Database for Redis™ API.
    """

    async def create_cluster(
        self,
        *,
        version: str,
        node_type: str,
        user_name: str,
        password: str,
        tls_enabled: bool,
        zone: Optional[Zone] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        cluster_size: Optional[int] = None,
        acl_rules: Optional[List[ACLRuleSpec]] = None,
        endpoints: Optional[List[EndpointSpec]] = None,
        cluster_settings: Optional[List[ClusterSetting]] = None,
    ) -> Cluster:
        """
        Create a cluster
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param project_id: The project ID on which to create the cluster
        :param name: Name of the cluster
        :param version: Redis™ engine version of the cluster
        :param tags: Tags to apply to the cluster
        :param node_type: Type of node to use for the cluster
        :param user_name: Name of the user created when the cluster is created
        :param password: Password of the user
        :param cluster_size: Number of nodes for the cluster
        :param acl_rules: List of ACLRuleSpec used to secure your publicly exposed cluster
        :param endpoints: Zero or multiple EndpointSpec used to expose your cluster publicly and inside private networks. If no EndpoindSpec is given the cluster will be publicly exposed by default.
        :param tls_enabled: Whether or not TLS is enabled
        :param cluster_settings: List of cluster settings to be set at cluster initialisation
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.create_cluster(
                version="example",
                node_type="example",
                user_name="example",
                password="example",
                tls_enabled=True,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/redis/v1/zones/{param_zone}/clusters",
            body=marshal_CreateClusterRequest(
                CreateClusterRequest(
                    version=version,
                    node_type=node_type,
                    user_name=user_name,
                    password=password,
                    tls_enabled=tls_enabled,
                    zone=zone,
                    project_id=project_id,
                    name=name or random_name(prefix="ins"),
                    tags=tags,
                    cluster_size=cluster_size,
                    acl_rules=acl_rules,
                    endpoints=endpoints,
                    cluster_settings=cluster_settings,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Cluster(res.json())

    async def update_cluster(
        self,
        *,
        cluster_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        user_name: Optional[str] = None,
        password: Optional[str] = None,
    ) -> Cluster:
        """
        Update a cluster
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param cluster_id: UUID of the cluster to update
        :param name: Name of the cluster
        :param tags: Tags of a given cluster
        :param user_name: Name of the cluster user
        :param password: Password of the cluster user
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.update_cluster(cluster_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "PATCH",
            f"/redis/v1/zones/{param_zone}/clusters/{param_cluster_id}",
            body=marshal_UpdateClusterRequest(
                UpdateClusterRequest(
                    cluster_id=cluster_id,
                    zone=zone,
                    name=name,
                    tags=tags,
                    user_name=user_name,
                    password=password,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Cluster(res.json())

    async def get_cluster(
        self,
        *,
        cluster_id: str,
        zone: Optional[Zone] = None,
    ) -> Cluster:
        """
        Get a cluster
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param cluster_id: UUID of the cluster
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.get_cluster(cluster_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "GET",
            f"/redis/v1/zones/{param_zone}/clusters/{param_cluster_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Cluster(res.json())

    async def wait_for_cluster(
        self,
        *,
        cluster_id: str,
        zone: Optional[Zone] = None,
        options: Optional[WaitForOptions[Cluster, Union[bool, Awaitable[bool]]]] = None,
    ) -> Cluster:
        """
        Waits for :class:`Cluster <Cluster>` to be in a final state.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param cluster_id: UUID of the cluster
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

        return await wait_for_resource_async(
            fetcher=self.get_cluster,
            options=options,
            args={
                "cluster_id": cluster_id,
                "zone": zone,
            },
        )

    async def list_clusters(
        self,
        *,
        zone: Optional[Zone] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
        order_by: ListClustersRequestOrderBy = ListClustersRequestOrderBy.CREATED_AT_ASC,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        version: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListClustersResponse:
        """
        List clusters
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param tags: Tags of the clusters to filter upon
        :param name: Name of the clusters to filter upon
        :param order_by: Criteria to use when ordering cluster listing
        :param project_id: Project ID to list the cluster of
        :param organization_id: Organization ID to list the cluster of
        :param version: Version of the clusters to filter upon
        :param page:
        :param page_size:
        :return: :class:`ListClustersResponse <ListClustersResponse>`

        Usage:
        ::

            result = await api.list_clusters()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/redis/v1/zones/{param_zone}/clusters",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
                "version": version,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListClustersResponse(res.json())

    async def list_clusters_all(
        self,
        *,
        zone: Optional[Zone] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
        order_by: Optional[ListClustersRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        version: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[Cluster]:
        """
        List clusters
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param tags: Tags of the clusters to filter upon
        :param name: Name of the clusters to filter upon
        :param order_by: Criteria to use when ordering cluster listing
        :param project_id: Project ID to list the cluster of
        :param organization_id: Organization ID to list the cluster of
        :param version: Version of the clusters to filter upon
        :param page:
        :param page_size:
        :return: :class:`List[ListClustersResponse] <List[ListClustersResponse]>`

        Usage:
        ::

            result = await api.list_clusters_all()
        """

        return await fetch_all_pages_async(
            type=ListClustersResponse,
            key="clusters",
            fetcher=self.list_clusters,
            args={
                "zone": zone,
                "tags": tags,
                "name": name,
                "order_by": order_by,
                "project_id": project_id,
                "organization_id": organization_id,
                "version": version,
                "page": page,
                "page_size": page_size,
            },
        )

    async def migrate_cluster(
        self,
        *,
        cluster_id: str,
        zone: Optional[Zone] = None,
        version: Optional[str] = None,
        node_type: Optional[str] = None,
        cluster_size: Optional[int] = None,
    ) -> Cluster:
        """
        Upgrade your Database for Redis® cluster to a new version or scale it vertically / horizontally. Please note: scaling horizontally your Database for Redis® cluster won't renew its TLS certificate. In order to refresh the SSL certificate, you have to use the dedicated api route.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param cluster_id: UUID of the cluster to update
        :param version: Redis™ engine version of the cluster.

        One-of ('action'): at most one of 'version', 'node_type', 'cluster_size' could be set.
        :param node_type: Type of node to use for the cluster.

        One-of ('action'): at most one of 'version', 'node_type', 'cluster_size' could be set.
        :param cluster_size: Number of nodes for the cluster.

        One-of ('action'): at most one of 'version', 'node_type', 'cluster_size' could be set.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.migrate_cluster(cluster_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "POST",
            f"/redis/v1/zones/{param_zone}/clusters/{param_cluster_id}/migrate",
            body=marshal_MigrateClusterRequest(
                MigrateClusterRequest(
                    cluster_id=cluster_id,
                    zone=zone,
                    version=version,
                    node_type=node_type,
                    cluster_size=cluster_size,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Cluster(res.json())

    async def delete_cluster(
        self,
        *,
        cluster_id: str,
        zone: Optional[Zone] = None,
    ) -> Cluster:
        """
        Delete a cluster
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param cluster_id: UUID of the cluster to delete
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.delete_cluster(cluster_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "DELETE",
            f"/redis/v1/zones/{param_zone}/clusters/{param_cluster_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Cluster(res.json())

    async def get_cluster_metrics(
        self,
        *,
        cluster_id: str,
        zone: Optional[Zone] = None,
        start_at: Optional[datetime] = None,
        end_at: Optional[datetime] = None,
        metric_name: Optional[str] = None,
    ) -> ClusterMetricsResponse:
        """
        Get metrics of a cluster
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param cluster_id: UUID of the cluster
        :param start_at: Start date to gather metrics from
        :param end_at: End date to gather metrics from
        :param metric_name: Name of the metric to gather
        :return: :class:`ClusterMetricsResponse <ClusterMetricsResponse>`

        Usage:
        ::

            result = await api.get_cluster_metrics(cluster_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "GET",
            f"/redis/v1/zones/{param_zone}/clusters/{param_cluster_id}/metrics",
            params={
                "end_at": end_at,
                "metric_name": metric_name,
                "start_at": start_at,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ClusterMetricsResponse(res.json())

    async def list_node_types(
        self,
        *,
        include_disabled_types: bool,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListNodeTypesResponse:
        """
        List available node types
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param include_disabled_types: Whether or not to include disabled types
        :param page:
        :param page_size:
        :return: :class:`ListNodeTypesResponse <ListNodeTypesResponse>`

        Usage:
        ::

            result = await api.list_node_types(include_disabled_types=True)
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/redis/v1/zones/{param_zone}/node-types",
            params={
                "include_disabled_types": include_disabled_types,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListNodeTypesResponse(res.json())

    async def list_node_types_all(
        self,
        *,
        include_disabled_types: bool,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[NodeType]:
        """
        List available node types
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param include_disabled_types: Whether or not to include disabled types
        :param page:
        :param page_size:
        :return: :class:`List[ListNodeTypesResponse] <List[ListNodeTypesResponse]>`

        Usage:
        ::

            result = await api.list_node_types_all(include_disabled_types=True)
        """

        return await fetch_all_pages_async(
            type=ListNodeTypesResponse,
            key="node_types",
            fetcher=self.list_node_types,
            args={
                "include_disabled_types": include_disabled_types,
                "zone": zone,
                "page": page,
                "page_size": page_size,
            },
        )

    async def list_cluster_versions(
        self,
        *,
        include_disabled: bool,
        include_beta: bool,
        include_deprecated: bool,
        zone: Optional[Zone] = None,
        version: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListClusterVersionsResponse:
        """
        List available Redis™ versions
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param include_disabled: Whether or not to include disabled Redis™ engine versions
        :param include_beta: Whether or not to include beta Redis™ engine versions
        :param include_deprecated: Whether or not to include deprecated Redis™ engine versions
        :param version: List Redis™ engine versions that match a given name pattern
        :param page:
        :param page_size:
        :return: :class:`ListClusterVersionsResponse <ListClusterVersionsResponse>`

        Usage:
        ::

            result = await api.list_cluster_versions(
                include_disabled=True,
                include_beta=True,
                include_deprecated=True,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/redis/v1/zones/{param_zone}/cluster-versions",
            params={
                "include_beta": include_beta,
                "include_deprecated": include_deprecated,
                "include_disabled": include_disabled,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "version": version,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListClusterVersionsResponse(res.json())

    async def list_cluster_versions_all(
        self,
        *,
        include_disabled: bool,
        include_beta: bool,
        include_deprecated: bool,
        zone: Optional[Zone] = None,
        version: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ClusterVersion]:
        """
        List available Redis™ versions
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param include_disabled: Whether or not to include disabled Redis™ engine versions
        :param include_beta: Whether or not to include beta Redis™ engine versions
        :param include_deprecated: Whether or not to include deprecated Redis™ engine versions
        :param version: List Redis™ engine versions that match a given name pattern
        :param page:
        :param page_size:
        :return: :class:`List[ListClusterVersionsResponse] <List[ListClusterVersionsResponse]>`

        Usage:
        ::

            result = await api.list_cluster_versions_all(
                include_disabled=True,
                include_beta=True,
                include_deprecated=True,
            )
        """

        return await fetch_all_pages_async(
            type=ListClusterVersionsResponse,
            key="versions",
            fetcher=self.list_cluster_versions,
            args={
                "include_disabled": include_disabled,
                "include_beta": include_beta,
                "include_deprecated": include_deprecated,
                "zone": zone,
                "version": version,
                "page": page,
                "page_size": page_size,
            },
        )

    async def get_cluster_certificate(
        self,
        *,
        cluster_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[ScwFile]:
        """
        Get the TLS certificate of a cluster
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param cluster_id: UUID of the cluster
        :return: :class:`Optional[ScwFile] <Optional[ScwFile]>`

        Usage:
        ::

            result = await api.get_cluster_certificate(cluster_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "GET",
            f"/redis/v1/zones/{param_zone}/clusters/{param_cluster_id}/certificate",
        )

        self._throw_on_error(res)
        json = res.json()
        return unmarshal_ScwFile(json) if json is not None else None

    async def renew_cluster_certificate(
        self,
        *,
        cluster_id: str,
        zone: Optional[Zone] = None,
    ) -> Cluster:
        """
        Renew the TLS certificate of a cluster
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param cluster_id: UUID of the cluster
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.renew_cluster_certificate(cluster_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "POST",
            f"/redis/v1/zones/{param_zone}/clusters/{param_cluster_id}/renew-certificate",
        )

        self._throw_on_error(res)
        return unmarshal_Cluster(res.json())

    async def add_cluster_settings(
        self,
        *,
        cluster_id: str,
        settings: List[ClusterSetting],
        zone: Optional[Zone] = None,
    ) -> ClusterSettingsResponse:
        """
        Add cluster settings
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param cluster_id: UUID of the cluster you want to add settings to
        :param settings: Settings to add on the cluster
        :return: :class:`ClusterSettingsResponse <ClusterSettingsResponse>`

        Usage:
        ::

            result = await api.add_cluster_settings(
                cluster_id="example",
                settings=[ClusterSetting(...)],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "POST",
            f"/redis/v1/zones/{param_zone}/clusters/{param_cluster_id}/settings",
            body=marshal_AddClusterSettingsRequest(
                AddClusterSettingsRequest(
                    cluster_id=cluster_id,
                    settings=settings,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ClusterSettingsResponse(res.json())

    async def delete_cluster_setting(
        self,
        *,
        cluster_id: str,
        setting_name: str,
        zone: Optional[Zone] = None,
    ) -> Cluster:
        """
        Delete a cluster setting
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param cluster_id: UUID of the cluster where the settings has to be set
        :param setting_name: Setting name to delete
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.delete_cluster_setting(
                cluster_id="example",
                setting_name="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_cluster_id = validate_path_param("cluster_id", cluster_id)
        param_setting_name = validate_path_param("setting_name", setting_name)

        res = self._request(
            "DELETE",
            f"/redis/v1/zones/{param_zone}/clusters/{param_cluster_id}/settings/{param_setting_name}",
        )

        self._throw_on_error(res)
        return unmarshal_Cluster(res.json())

    async def set_cluster_settings(
        self,
        *,
        cluster_id: str,
        settings: List[ClusterSetting],
        zone: Optional[Zone] = None,
    ) -> ClusterSettingsResponse:
        """
        Set cluster settings
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param cluster_id: UUID of the cluster where the settings has to be set
        :param settings: Settings to define for the cluster
        :return: :class:`ClusterSettingsResponse <ClusterSettingsResponse>`

        Usage:
        ::

            result = await api.set_cluster_settings(
                cluster_id="example",
                settings=[ClusterSetting(...)],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "PUT",
            f"/redis/v1/zones/{param_zone}/clusters/{param_cluster_id}/settings",
            body=marshal_SetClusterSettingsRequest(
                SetClusterSettingsRequest(
                    cluster_id=cluster_id,
                    settings=settings,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ClusterSettingsResponse(res.json())

    async def set_acl_rules(
        self,
        *,
        cluster_id: str,
        acl_rules: List[ACLRuleSpec],
        zone: Optional[Zone] = None,
    ) -> SetAclRulesResponse:
        """
        Set ACL rules for a given cluster
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param cluster_id: UUID of the cluster where the ACL rules has to be set
        :param acl_rules: ACLs rules to define for the cluster
        :return: :class:`SetAclRulesResponse <SetAclRulesResponse>`

        Usage:
        ::

            result = await api.set_acl_rules(
                cluster_id="example",
                acl_rules=[ACLRuleSpec(...)],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "PUT",
            f"/redis/v1/zones/{param_zone}/clusters/{param_cluster_id}/acls",
            body=marshal_SetAclRulesRequest(
                SetAclRulesRequest(
                    cluster_id=cluster_id,
                    acl_rules=acl_rules,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetAclRulesResponse(res.json())

    async def add_acl_rules(
        self,
        *,
        cluster_id: str,
        acl_rules: List[ACLRuleSpec],
        zone: Optional[Zone] = None,
    ) -> AddAclRulesResponse:
        """
        Add ACL rules for a given cluster
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param cluster_id: UUID of the cluster you want to add acl rules to
        :param acl_rules: ACLs rules to add to the cluster
        :return: :class:`AddAclRulesResponse <AddAclRulesResponse>`

        Usage:
        ::

            result = await api.add_acl_rules(
                cluster_id="example",
                acl_rules=[ACLRuleSpec(...)],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "POST",
            f"/redis/v1/zones/{param_zone}/clusters/{param_cluster_id}/acls",
            body=marshal_AddAclRulesRequest(
                AddAclRulesRequest(
                    cluster_id=cluster_id,
                    acl_rules=acl_rules,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_AddAclRulesResponse(res.json())

    async def delete_acl_rule(
        self,
        *,
        acl_id: str,
        zone: Optional[Zone] = None,
    ) -> Cluster:
        """
        Delete an ACL rule for a given cluster
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param acl_id: UUID of the acl rule you want to delete
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.delete_acl_rule(acl_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_acl_id = validate_path_param("acl_id", acl_id)

        res = self._request(
            "DELETE",
            f"/redis/v1/zones/{param_zone}/acls/{param_acl_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Cluster(res.json())

    async def get_acl_rule(
        self,
        *,
        acl_id: str,
        zone: Optional[Zone] = None,
    ) -> ACLRule:
        """
        Get an ACL rule
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param acl_id: UUID of the acl rule you want to get
        :return: :class:`ACLRule <ACLRule>`

        Usage:
        ::

            result = await api.get_acl_rule(acl_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_acl_id = validate_path_param("acl_id", acl_id)

        res = self._request(
            "GET",
            f"/redis/v1/zones/{param_zone}/acls/{param_acl_id}",
        )

        self._throw_on_error(res)
        return unmarshal_ACLRule(res.json())

    async def set_endpoints(
        self,
        *,
        cluster_id: str,
        endpoints: List[EndpointSpec],
        zone: Optional[Zone] = None,
    ) -> SetEndpointsResponse:
        """
        Set endpoints for a given cluster
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param cluster_id: UUID of the cluster where the endpoints has to be set
        :param endpoints: Endpoints to define for the cluster
        :return: :class:`SetEndpointsResponse <SetEndpointsResponse>`

        Usage:
        ::

            result = await api.set_endpoints(
                cluster_id="example",
                endpoints=[EndpointSpec(...)],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "PUT",
            f"/redis/v1/zones/{param_zone}/clusters/{param_cluster_id}/endpoints",
            body=marshal_SetEndpointsRequest(
                SetEndpointsRequest(
                    cluster_id=cluster_id,
                    endpoints=endpoints,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetEndpointsResponse(res.json())

    async def add_endpoints(
        self,
        *,
        cluster_id: str,
        endpoints: List[EndpointSpec],
        zone: Optional[Zone] = None,
    ) -> AddEndpointsResponse:
        """
        Add endpoints for a given cluster
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param cluster_id: UUID of the cluster you want to add endpoints to
        :param endpoints: Endpoints to add to the cluster
        :return: :class:`AddEndpointsResponse <AddEndpointsResponse>`

        Usage:
        ::

            result = await api.add_endpoints(
                cluster_id="example",
                endpoints=[EndpointSpec(...)],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "POST",
            f"/redis/v1/zones/{param_zone}/clusters/{param_cluster_id}/endpoints",
            body=marshal_AddEndpointsRequest(
                AddEndpointsRequest(
                    cluster_id=cluster_id,
                    endpoints=endpoints,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_AddEndpointsResponse(res.json())

    async def delete_endpoint(
        self,
        *,
        endpoint_id: str,
        zone: Optional[Zone] = None,
    ) -> Cluster:
        """
        Delete an endpoint for a given cluster
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param endpoint_id: UUID of the endpoint you want to delete
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.delete_endpoint(endpoint_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_endpoint_id = validate_path_param("endpoint_id", endpoint_id)

        res = self._request(
            "DELETE",
            f"/redis/v1/zones/{param_zone}/endpoints/{param_endpoint_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Cluster(res.json())

    async def get_endpoint(
        self,
        *,
        endpoint_id: str,
        zone: Optional[Zone] = None,
    ) -> Endpoint:
        """
        Get an endpoint
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param endpoint_id: UUID of the endpoint you want to get
        :return: :class:`Endpoint <Endpoint>`

        Usage:
        ::

            result = await api.get_endpoint(endpoint_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_endpoint_id = validate_path_param("endpoint_id", endpoint_id)

        res = self._request(
            "GET",
            f"/redis/v1/zones/{param_zone}/endpoints/{param_endpoint_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Endpoint(res.json())

    async def update_endpoint(
        self,
        *,
        endpoint_id: str,
        zone: Optional[Zone] = None,
        private_network: Optional[EndpointSpecPrivateNetworkSpec] = None,
        public_network: Optional[EndpointSpecPublicNetworkSpec] = None,
    ) -> Endpoint:
        """

        Usage:
        ::

            result = await api.update_endpoint(endpoint_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_endpoint_id = validate_path_param("endpoint_id", endpoint_id)

        res = self._request(
            "PATCH",
            f"/redis/v1/zones/{param_zone}/endpoints/{param_endpoint_id}",
            body=marshal_UpdateEndpointRequest(
                UpdateEndpointRequest(
                    endpoint_id=endpoint_id,
                    zone=zone,
                    private_network=private_network,
                    public_network=public_network,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Endpoint(res.json())
