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
    random_name,
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    ListClustersRequestOrderBy,
    ACLRule,
    ACLRuleSpec,
    AddAclRulesRequest,
    AddAclRulesResponse,
    AddClusterSettingsRequest,
    AddEndpointsRequest,
    AddEndpointsResponse,
    Cluster,
    ClusterMetricsResponse,
    ClusterSetting,
    ClusterSettingsResponse,
    ClusterVersion,
    CreateClusterRequest,
    Endpoint,
    EndpointSpec,
    EndpointSpecPrivateNetworkSpec,
    EndpointSpecPublicNetworkSpec,
    ListClusterVersionsResponse,
    ListClustersResponse,
    ListNodeTypesResponse,
    MigrateClusterRequest,
    NodeType,
    SetAclRulesRequest,
    SetAclRulesResponse,
    SetClusterSettingsRequest,
    SetEndpointsRequest,
    SetEndpointsResponse,
    UpdateClusterRequest,
    UpdateEndpointRequest,
)
from .content import (
    CLUSTER_TRANSIENT_STATUSES,
)
from .marshalling import (
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
)


class RedisV1API(API):
    """
    This API allows you to manage your Managed Databases for Redis™.
    """

    async def create_cluster(
        self,
        *,
        version: str,
        node_type: str,
        zone: Optional[Zone] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        user_name: str,
        password: str,
        tls_enabled: bool,
        cluster_size: Optional[int] = None,
        acl_rules: Optional[List[ACLRuleSpec]] = None,
        endpoints: Optional[List[EndpointSpec]] = None,
        cluster_settings: Optional[List[ClusterSetting]] = None,
    ) -> Cluster:
        """
        Create a Redis™ Database Instance.
        Create a new Redis™ Database Instance (Redis™ cluster). You must set the `zone`, `project_id`, `version`, `node_type`, `user_name` and `password` parameters. Optionally you can define `acl_rules`, `endpoints`, `tls_enabled` and `cluster_settings`.
        :param version: Redis™ engine version of the Database Instance.
        :param node_type: Type of node to use for the Database Instance.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param project_id: Project ID in which to create the Database Instance.
        :param name: Name of the Database Instance.
        :param tags: Tags to apply to the Database Instance.
        :param user_name: Name of the user created upon Database Instance creation.
        :param password: Password of the user.
        :param tls_enabled: Defines whether or not TLS is enabled.
        :param cluster_size: Number of nodes in the Redis™ cluster.
        :param acl_rules: List of ACLRuleSpec used to secure your publicly exposed cluster.
        :param endpoints: Zero or multiple EndpointSpec used to expose your cluster publicly and inside private networks. If no EndpoindSpec is given the cluster will be publicly exposed by default.
        :param cluster_settings: List of advanced settings to be set upon Database Instance initialization.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.create_cluster(
                version="example",
                node_type="example",
                user_name="example",
                password="example",
                tls_enabled=False,
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
                    zone=zone,
                    project_id=project_id,
                    name=name or random_name(prefix="ins"),
                    tags=tags,
                    user_name=user_name,
                    password=password,
                    tls_enabled=tls_enabled,
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
        Update a Redis™ Database Instance.
        Update the parameters of a Redis™ Database Instance (Redis™ cluster), including `name`, `tags`, `user_name` and `password`.
        :param cluster_id: UUID of the Database Instance to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the Database Instance.
        :param tags: Database Instance tags.
        :param user_name: Name of the Database Instance user.
        :param password: Password of the Database Instance user.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.update_cluster(
                cluster_id="example",
            )
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
        Get a Redis™ Database Instance.
        Retrieve information about a Redis™ Database Instance (Redis™ cluster). Specify the `cluster_id` and `region` in your request to get information such as `id`, `status`, `version`, `tls_enabled`, `cluster_settings`, `upgradable_versions` and `endpoints` about your cluster in the response.
        :param cluster_id: UUID of the cluster.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.get_cluster(
                cluster_id="example",
            )
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
        Get a Redis™ Database Instance.
        Retrieve information about a Redis™ Database Instance (Redis™ cluster). Specify the `cluster_id` and `region` in your request to get information such as `id`, `status`, `version`, `tls_enabled`, `cluster_settings`, `upgradable_versions` and `endpoints` about your cluster in the response.
        :param cluster_id: UUID of the cluster.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.get_cluster(
                cluster_id="example",
            )
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
        order_by: Optional[ListClustersRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        version: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListClustersResponse:
        """
        List Redis™ Database Instances.
        List all Redis™ Database Instances (Redis™ cluster) in the specified zone. By default, the Database Instances returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field. You can define additional parameters for your query, such as `tags`, `name`, `organization_id` and `version`.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param tags: Filter by Database Instance tags.
        :param name: Filter by Database Instance names.
        :param order_by: Criteria to use when ordering the list.
        :param project_id: Filter by Project ID.
        :param organization_id: Filter by Organization ID.
        :param version: Filter by Redis™ engine version.
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
        List Redis™ Database Instances.
        List all Redis™ Database Instances (Redis™ cluster) in the specified zone. By default, the Database Instances returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field. You can define additional parameters for your query, such as `tags`, `name`, `organization_id` and `version`.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param tags: Filter by Database Instance tags.
        :param name: Filter by Database Instance names.
        :param order_by: Criteria to use when ordering the list.
        :param project_id: Filter by Project ID.
        :param organization_id: Filter by Organization ID.
        :param version: Filter by Redis™ engine version.
        :param page:
        :param page_size:
        :return: :class:`List[Cluster] <List[Cluster]>`

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
        Scale up a Redis™ Database Instance.
        Upgrade your Redis™ Database Instance, either by upgrading to a bigger node type (vertical scaling) or by adding more nodes to your Database Instance to increase your number of endpoints and distribute cache (horizontal scaling, available for clusters only). Note that scaling horizontally your Redis™ Database Instance will not renew its TLS certificate. In order to refresh the TLS certificate, you must use the Renew TLS certificate endpoint.
        :param cluster_id: UUID of the Database Instance to update.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param version: Redis™ engine version of the Database Instance.
        One-Of ('action'): at most one of 'version', 'node_type', 'cluster_size' could be set.
        :param node_type: Type of node to use for the Database Instance.
        One-Of ('action'): at most one of 'version', 'node_type', 'cluster_size' could be set.
        :param cluster_size: Number of nodes for the Database Instance.
        One-Of ('action'): at most one of 'version', 'node_type', 'cluster_size' could be set.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.migrate_cluster(
                cluster_id="example",
            )
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
        Delete a Redis™ Database Instance.
        Delete a Redis™ Database Instance (Redis™ cluster), specified by the `region` and `cluster_id` parameters. Deleting a Database Instance is permanent, and cannot be undone. Note that upon deletion all your data will be lost.
        :param cluster_id: UUID of the Database Instance to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.delete_cluster(
                cluster_id="example",
            )
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
        Get metrics of a Redis™ Database Instance.
        Retrieve the metrics of a Redis™ Database Instance (Redis™ cluster). You can define the period from which to retrieve metrics by specifying the `start_date` and `end_date`.
        :param cluster_id: UUID of the cluster.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param start_at: Start date.
        :param end_at: End date.
        :param metric_name: Name of the metric to gather.
        :return: :class:`ClusterMetricsResponse <ClusterMetricsResponse>`

        Usage:
        ::

            result = await api.get_cluster_metrics(
                cluster_id="example",
            )
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
        List available node types.
        List all available node types. By default, the node types returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param include_disabled_types: Defines whether or not to include disabled types.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page:
        :param page_size:
        :return: :class:`ListNodeTypesResponse <ListNodeTypesResponse>`

        Usage:
        ::

            result = await api.list_node_types(
                include_disabled_types=False,
            )
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
        List available node types.
        List all available node types. By default, the node types returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param include_disabled_types: Defines whether or not to include disabled types.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page:
        :param page_size:
        :return: :class:`List[NodeType] <List[NodeType]>`

        Usage:
        ::

            result = await api.list_node_types_all(
                include_disabled_types=False,
            )
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
        List available Redis™ versions.
        List the Redis™ database engine versions available. You can define additional parameters for your query, such as `include_disabled`, `include_beta`, `include_deprecated` and `version`.
        :param include_disabled: Defines whether or not to include disabled Redis™ engine versions.
        :param include_beta: Defines whether or not to include beta Redis™ engine versions.
        :param include_deprecated: Defines whether or not to include deprecated Redis™ engine versions.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param version: List Redis™ engine versions that match a given name pattern.
        :param page:
        :param page_size:
        :return: :class:`ListClusterVersionsResponse <ListClusterVersionsResponse>`

        Usage:
        ::

            result = await api.list_cluster_versions(
                include_disabled=False,
                include_beta=False,
                include_deprecated=False,
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
        List available Redis™ versions.
        List the Redis™ database engine versions available. You can define additional parameters for your query, such as `include_disabled`, `include_beta`, `include_deprecated` and `version`.
        :param include_disabled: Defines whether or not to include disabled Redis™ engine versions.
        :param include_beta: Defines whether or not to include beta Redis™ engine versions.
        :param include_deprecated: Defines whether or not to include deprecated Redis™ engine versions.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param version: List Redis™ engine versions that match a given name pattern.
        :param page:
        :param page_size:
        :return: :class:`List[ClusterVersion] <List[ClusterVersion]>`

        Usage:
        ::

            result = await api.list_cluster_versions_all(
                include_disabled=False,
                include_beta=False,
                include_deprecated=False,
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
    ) -> ScwFile:
        """
        Get the TLS certificate of a cluster.
        Retrieve information about the TLS certificate of a Redis™ Database Instance (Redis™ cluster). Details like name and content are returned in the response.
        :param cluster_id: UUID of the cluster.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`ScwFile <ScwFile>`

        Usage:
        ::

            result = await api.get_cluster_certificate(
                cluster_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "GET",
            f"/redis/v1/zones/{param_zone}/clusters/{param_cluster_id}/certificate",
        )

        self._throw_on_error(res)
        return unmarshal_ScwFile(res.json())

    async def renew_cluster_certificate(
        self,
        *,
        cluster_id: str,
        zone: Optional[Zone] = None,
    ) -> Cluster:
        """
        Renew the TLS certificate of a cluster.
        Renew a TLS certificate for a Redis™ Database Instance (Redis™ cluster). Renewing a certificate means that you will not be able to connect to your Database Instance using the previous certificate. You will also need to download and update the new certificate for all database clients.
        :param cluster_id: UUID of the cluster.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.renew_cluster_certificate(
                cluster_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "POST",
            f"/redis/v1/zones/{param_zone}/clusters/{param_cluster_id}/renew-certificate",
            body={},
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
        Add advanced settings.
        Add an advanced setting to a Redis™ Database Instance (Redis™ cluster). You must set the `name` and the `value` of each setting.
        :param cluster_id: UUID of the Database Instance you want to add settings to.
        :param settings: Settings to add to the cluster.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`ClusterSettingsResponse <ClusterSettingsResponse>`

        Usage:
        ::

            result = await api.add_cluster_settings(
                cluster_id="example",
                settings=[],
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
        Delete advanced setting.
        Delete an advanced setting in a Redis™ Database Instance (Redis™ cluster). You must specify the names of the settings you want to delete in the request body.
        :param cluster_id: UUID of the Database Instance where the settings must be set.
        :param setting_name: Setting name to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.
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
        Set advanced settings.
        Update an advanced setting for a Redis™ Database Instance (Redis™ cluster). Settings added upon database engine initalization can only be defined once, and cannot, therefore, be updated.
        :param cluster_id: UUID of the Database Instance where the settings must be set.
        :param settings: Settings to define for the Database Instance.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`ClusterSettingsResponse <ClusterSettingsResponse>`

        Usage:
        ::

            result = await api.set_cluster_settings(
                cluster_id="example",
                settings=[],
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
        Set ACL rules for a cluster.
        Replace all the ACL rules of a Redis™ Database Instance (Redis™ cluster).
        :param cluster_id: UUID of the Database Instance where the ACL rules have to be set.
        :param acl_rules: ACLs rules to define for the cluster.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`SetAclRulesResponse <SetAclRulesResponse>`

        Usage:
        ::

            result = await api.set_acl_rules(
                cluster_id="example",
                acl_rules=[],
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
        Add ACL rules for a cluster.
        Add an additional ACL rule to a Redis™ Database Instance (Redis™ cluster).
        :param cluster_id: UUID of the Database Instance you want to add ACL rules to.
        :param acl_rules: ACLs rules to add to the cluster.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`AddAclRulesResponse <AddAclRulesResponse>`

        Usage:
        ::

            result = await api.add_acl_rules(
                cluster_id="example",
                acl_rules=[],
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
        Delete an ACL rule for a cluster.
        Delete an ACL rule of a Redis™ Database Instance (Redis™ cluster). You must specify the `acl_id` of the rule you want to delete in your request.
        :param acl_id: UUID of the ACL rule you want to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.delete_acl_rule(
                acl_id="example",
            )
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
        Get an ACL rule.
        Retrieve information about an ACL rule of a Redis™ Database Instance (Redis™ cluster). You must specify the `acl_id` of the rule in your request.
        :param acl_id: UUID of the ACL rule you want to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`ACLRule <ACLRule>`

        Usage:
        ::

            result = await api.get_acl_rule(
                acl_id="example",
            )
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
        Set endpoints for a cluster.
        Update an endpoint for a Redis™ Database Instance (Redis™ cluster). You must specify the `cluster_id` and the `endpoints` parameters in your request.
        :param cluster_id: UUID of the Database Instance where the endpoints have to be set.
        :param endpoints: Endpoints to define for the Database Instance.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`SetEndpointsResponse <SetEndpointsResponse>`

        Usage:
        ::

            result = await api.set_endpoints(
                cluster_id="example",
                endpoints=[],
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
        Add endpoints for a cluster.
        Add a new endpoint for a Redis™ Database Instance (Redis™ cluster). You can add `private_network` or `public_network` specifications to the body of the request.
        :param cluster_id: UUID of the Database Instance you want to add endpoints to.
        :param endpoints: Endpoints to add to the Database Instance.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`AddEndpointsResponse <AddEndpointsResponse>`

        Usage:
        ::

            result = await api.add_endpoints(
                cluster_id="example",
                endpoints=[],
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
        Delete an endpoint for a cluster.
        Delete the endpoint of a Redis™ Database Instance (Redis™ cluster). You must specify the `region` and `endpoint_id` parameters of the endpoint you want to delete. Note that might need to update any environment configurations that point to the deleted endpoint.
        :param endpoint_id: UUID of the endpoint you want to delete.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.delete_endpoint(
                endpoint_id="example",
            )
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
        Get an endpoint.
        Retrieve information about a Redis™ Database Instance (Redis™ cluster) endpoint. Full details about the endpoint, like `ips`, `port`, `private_network` and `public_network` specifications are returned in the response.
        :param endpoint_id: UUID of the endpoint you want to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`Endpoint <Endpoint>`

        Usage:
        ::

            result = await api.get_endpoint(
                endpoint_id="example",
            )
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
        Update an endpoint.
        Update information about a Redis™ Database Instance (Redis™ cluster) endpoint. Full details about the endpoint, like `ips`, `port`, `private_network` and `public_network` specifications are returned in the response.
        :param endpoint_id: UUID of the endpoint you want to get.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param private_network: Private Network details.
        One-Of ('endpoint_type'): at most one of 'private_network', 'public_network' could be set.
        :param public_network: Public network details.
        One-Of ('endpoint_type'): at most one of 'private_network', 'public_network' could be set.
        :return: :class:`Endpoint <Endpoint>`

        Usage:
        ::

            result = await api.update_endpoint(
                endpoint_id="example",
            )
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
