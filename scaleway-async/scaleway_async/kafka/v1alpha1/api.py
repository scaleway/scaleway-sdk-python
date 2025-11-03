# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region as ScwRegion,
    ScwFile,
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
    ListUsersRequestOrderBy,
    Cluster,
    CreateClusterRequest,
    CreateClusterRequestVolumeSpec,
    CreateEndpointRequest,
    Endpoint,
    EndpointSpec,
    ListClustersResponse,
    ListNodeTypesResponse,
    ListUsersResponse,
    ListVersionsResponse,
    NodeType,
    UpdateClusterRequest,
    UpdateUserRequest,
    User,
    Version,
)
from .content import (
    CLUSTER_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Endpoint,
    unmarshal_Cluster,
    unmarshal_User,
    unmarshal_ListClustersResponse,
    unmarshal_ListNodeTypesResponse,
    unmarshal_ListUsersResponse,
    unmarshal_ListVersionsResponse,
    marshal_CreateClusterRequest,
    marshal_CreateEndpointRequest,
    marshal_UpdateClusterRequest,
    marshal_UpdateUserRequest,
)


class KafkaV1Alpha1API(API):
    """
    This API allows you to manage your Clusters for Apache Kafka®. This product is currently in Private Beta.
    """

    async def list_node_types(
        self,
        *,
        region: Optional[ScwRegion] = None,
        include_disabled_types: Optional[bool] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListNodeTypesResponse:
        """
        List available node types.
        :param region: Region to target. If none is passed will use default region from the config.
        :param include_disabled_types: Defines whether or not to include disabled types.
        :param page:
        :param page_size:
        :return: :class:`ListNodeTypesResponse <ListNodeTypesResponse>`

        Usage:
        ::

            result = await api.list_node_types()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/kafka/v1alpha1/regions/{param_region}/node-types",
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
        region: Optional[ScwRegion] = None,
        include_disabled_types: Optional[bool] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[NodeType]:
        """
        List available node types.
        :param region: Region to target. If none is passed will use default region from the config.
        :param include_disabled_types: Defines whether or not to include disabled types.
        :param page:
        :param page_size:
        :return: :class:`list[NodeType] <list[NodeType]>`

        Usage:
        ::

            result = await api.list_node_types_all()
        """

        return await fetch_all_pages_async(
            type=ListNodeTypesResponse,
            key="node_types",
            fetcher=self.list_node_types,
            args={
                "region": region,
                "include_disabled_types": include_disabled_types,
                "page": page,
                "page_size": page_size,
            },
        )

    async def list_versions(
        self,
        *,
        region: Optional[ScwRegion] = None,
        version: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListVersionsResponse:
        """
        List Kafka versions.
        List all available versions of Kafka at the current time.
        :param region: Region to target. If none is passed will use default region from the config.
        :param version: Kafka version to filter for.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of items to return.
        :return: :class:`ListVersionsResponse <ListVersionsResponse>`

        Usage:
        ::

            result = await api.list_versions()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/kafka/v1alpha1/regions/{param_region}/versions",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "version": version,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListVersionsResponse(res.json())

    async def list_versions_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        version: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[Version]:
        """
        List Kafka versions.
        List all available versions of Kafka at the current time.
        :param region: Region to target. If none is passed will use default region from the config.
        :param version: Kafka version to filter for.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of items to return.
        :return: :class:`list[Version] <list[Version]>`

        Usage:
        ::

            result = await api.list_versions_all()
        """

        return await fetch_all_pages_async(
            type=ListVersionsResponse,
            key="versions",
            fetcher=self.list_versions,
            args={
                "region": region,
                "version": version,
                "page": page,
                "page_size": page_size,
            },
        )

    async def list_clusters(
        self,
        *,
        region: Optional[ScwRegion] = None,
        tags: Optional[list[str]] = None,
        name: Optional[str] = None,
        order_by: Optional[ListClustersRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListClustersResponse:
        """
        List Kafka clusters.
        List all Kafka clusters in the specified region. By default, the clusters returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field. You can define additional parameters for your query, such as `tags` and `name`. For the `name` parameter, the value you include will be checked against the whole name string to see if it includes the string you put in the parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param tags: List Kafka cluster with a given tag.
        :param name: Lists Kafka clusters that match a name pattern.
        :param order_by: Criteria to use when ordering Kafka cluster listings.
        :param organization_id: Organization ID of the Kafka cluster.
        :param project_id: Project ID.
        :param page:
        :param page_size:
        :return: :class:`ListClustersResponse <ListClustersResponse>`

        Usage:
        ::

            result = await api.list_clusters()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/kafka/v1alpha1/regions/{param_region}/clusters",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListClustersResponse(res.json())

    async def list_clusters_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        tags: Optional[list[str]] = None,
        name: Optional[str] = None,
        order_by: Optional[ListClustersRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[Cluster]:
        """
        List Kafka clusters.
        List all Kafka clusters in the specified region. By default, the clusters returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field. You can define additional parameters for your query, such as `tags` and `name`. For the `name` parameter, the value you include will be checked against the whole name string to see if it includes the string you put in the parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param tags: List Kafka cluster with a given tag.
        :param name: Lists Kafka clusters that match a name pattern.
        :param order_by: Criteria to use when ordering Kafka cluster listings.
        :param organization_id: Organization ID of the Kafka cluster.
        :param project_id: Project ID.
        :param page:
        :param page_size:
        :return: :class:`list[Cluster] <list[Cluster]>`

        Usage:
        ::

            result = await api.list_clusters_all()
        """

        return await fetch_all_pages_async(
            type=ListClustersResponse,
            key="clusters",
            fetcher=self.list_clusters,
            args={
                "region": region,
                "tags": tags,
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
            },
        )

    async def get_cluster(
        self,
        *,
        cluster_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Cluster:
        """
        Get a Kafka cluster.
        Retrieve information about a given Kafka cluster, specified by the `region` and `cluster_id` parameters. Its full details, including name, status, IP address and port, are returned in the response object.
        :param cluster_id: UUID of the Kafka Cluster.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.get_cluster(
                cluster_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "GET",
            f"/kafka/v1alpha1/regions/{param_region}/clusters/{param_cluster_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Cluster(res.json())

    async def wait_for_cluster(
        self,
        *,
        cluster_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[WaitForOptions[Cluster, Union[bool, Awaitable[bool]]]] = None,
    ) -> Cluster:
        """
        Get a Kafka cluster.
        Retrieve information about a given Kafka cluster, specified by the `region` and `cluster_id` parameters. Its full details, including name, status, IP address and port, are returned in the response object.
        :param cluster_id: UUID of the Kafka Cluster.
        :param region: Region to target. If none is passed will use default region from the config.
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
                "region": region,
            },
        )

    async def create_cluster(
        self,
        *,
        version: str,
        node_amount: int,
        node_type: str,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        volume: Optional[CreateClusterRequestVolumeSpec] = None,
        endpoints: Optional[list[EndpointSpec]] = None,
        user_name: Optional[str] = None,
        password: Optional[str] = None,
    ) -> Cluster:
        """
        Create a Kafka cluster.
        Create a new Kafka cluster.
        :param version: Version of Kafka.
        :param node_amount: Number of nodes to use for the Kafka cluster.
        :param node_type: Type of node to use for the Kafka cluster.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: The ID of the Project in which the Kafka cluster will be created.
        :param name: Name of the Kafka cluster.
        :param tags: Tags to apply to the Kafka cluster.
        :param volume: Kafka volume information.
        :param endpoints: One or multiple EndpointSpec used to expose your Kafka cluster.
        :param user_name: Username for the kafka user.
        :param password: Password for the kafka user.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.create_cluster(
                version="example",
                node_amount=1,
                node_type="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/kafka/v1alpha1/regions/{param_region}/clusters",
            body=marshal_CreateClusterRequest(
                CreateClusterRequest(
                    version=version,
                    node_amount=node_amount,
                    node_type=node_type,
                    region=region,
                    project_id=project_id,
                    name=name or random_name(prefix="kafk"),
                    tags=tags,
                    volume=volume,
                    endpoints=endpoints,
                    user_name=user_name,
                    password=password,
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
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> Cluster:
        """
        Update a Kafka cluster.
        Update the parameters of a Kafka cluster.
        :param cluster_id: UUID of the Kafka Clusters to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the Kafka Cluster.
        :param tags: Tags of a Kafka Cluster.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.update_cluster(
                cluster_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "PATCH",
            f"/kafka/v1alpha1/regions/{param_region}/clusters/{param_cluster_id}",
            body=marshal_UpdateClusterRequest(
                UpdateClusterRequest(
                    cluster_id=cluster_id,
                    region=region,
                    name=name,
                    tags=tags,
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
        region: Optional[ScwRegion] = None,
    ) -> Cluster:
        """
        Delete a Kafka cluster.
        Delete a given Kafka cluster, specified by the `region` and `cluster_id` parameters. Deleting a Kafka cluster is permanent, and cannot be undone. Note that upon deletion all your data will be lost.
        :param cluster_id: UUID of the Kafka Cluster to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Cluster <Cluster>`

        Usage:
        ::

            result = await api.delete_cluster(
                cluster_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "DELETE",
            f"/kafka/v1alpha1/regions/{param_region}/clusters/{param_cluster_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Cluster(res.json())

    async def get_cluster_certificate_authority(
        self,
        *,
        cluster_id: str,
        region: Optional[ScwRegion] = None,
    ) -> ScwFile:
        """
        Get a Kafka cluster's certificate authority.
        Retrieve certificate authority for a given Kafka cluster, specified by the `region` and `cluster_id` parameters. The response object contains the certificate in PEM format. The certificate is required to validate the sever from the client side during TLS connection.
        :param cluster_id: UUID of the Kafka Cluster.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ScwFile <ScwFile>`

        Usage:
        ::

            result = await api.get_cluster_certificate_authority(
                cluster_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "GET",
            f"/kafka/v1alpha1/regions/{param_region}/clusters/{param_cluster_id}/certificate-authority",
        )

        self._throw_on_error(res)
        return unmarshal_ScwFile(res.json())

    async def renew_cluster_certificate_authority(
        self,
        *,
        cluster_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Renew the Kafka cluster's certificate authority.
        Request to renew the certificate authority for a given Kafka cluster, specified by the `region` and `cluster_id` parameters. The certificate authority will be renewed within a few minutes.
        :param cluster_id: UUID of the Kafka Cluster.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.renew_cluster_certificate_authority(
                cluster_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "POST",
            f"/kafka/v1alpha1/regions/{param_region}/clusters/{param_cluster_id}/renew-certificate-authority",
            body={},
        )

        self._throw_on_error(res)

    async def delete_endpoint(
        self,
        *,
        endpoint_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a Kafka cluster endpoint.
        Delete the endpoint of a Kafka cluster. You must specify the `endpoint_id` parameter of the endpoint you want to delete. Note that you might need to update any environment configurations that point to the deleted endpoint.
        :param endpoint_id: UUID of the endpoint to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_endpoint(
                endpoint_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_endpoint_id = validate_path_param("endpoint_id", endpoint_id)

        res = self._request(
            "DELETE",
            f"/kafka/v1alpha1/regions/{param_region}/endpoints/{param_endpoint_id}",
        )

        self._throw_on_error(res)

    async def create_endpoint(
        self,
        *,
        cluster_id: str,
        endpoint: EndpointSpec,
        region: Optional[ScwRegion] = None,
    ) -> Endpoint:
        """
        Create a new Kafka cluster endpoint.
        Create a new endpoint for a Kafka cluster. You can add `public_network` or `private_network` specifications to the body of the request. Note that currently only `private_network` is supported.
        :param cluster_id: UUID of the Kafka Cluster.
        :param endpoint: Endpoint object (`EndpointSpec`) used to expose your Kafka EndpointSpec.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Endpoint <Endpoint>`

        Usage:
        ::

            result = await api.create_endpoint(
                cluster_id="example",
                endpoint=EndpointSpec(),
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/kafka/v1alpha1/regions/{param_region}/endpoints",
            body=marshal_CreateEndpointRequest(
                CreateEndpointRequest(
                    cluster_id=cluster_id,
                    endpoint=endpoint,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Endpoint(res.json())

    async def list_users(
        self,
        *,
        cluster_id: str,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListUsersRequestOrderBy] = None,
        name: Optional[str] = None,
    ) -> ListUsersResponse:
        """
        Retrieve a list of deployment users.
        :param cluster_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param name:
        :return: :class:`ListUsersResponse <ListUsersResponse>`

        Usage:
        ::

            result = await api.list_users(
                cluster_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)

        res = self._request(
            "GET",
            f"/kafka/v1alpha1/regions/{param_region}/clusters/{param_cluster_id}/users",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListUsersResponse(res.json())

    async def list_users_all(
        self,
        *,
        cluster_id: str,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListUsersRequestOrderBy] = None,
        name: Optional[str] = None,
    ) -> list[User]:
        """
        Retrieve a list of deployment users.
        :param cluster_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param name:
        :return: :class:`list[User] <list[User]>`

        Usage:
        ::

            result = await api.list_users_all(
                cluster_id="example",
            )
        """

        return await fetch_all_pages_async(
            type=ListUsersResponse,
            key="users",
            fetcher=self.list_users,
            args={
                "cluster_id": cluster_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "name": name,
            },
        )

    async def update_user(
        self,
        *,
        cluster_id: str,
        username: str,
        region: Optional[ScwRegion] = None,
        password: Optional[str] = None,
    ) -> User:
        """
        Update an existing user.
        :param cluster_id: ID of the cluster in which to update the user's password.
        :param username: Username of the Kafka cluster user.
        :param region: Region to target. If none is passed will use default region from the config.
        :param password: New password for the Kafka cluster user.
        :return: :class:`User <User>`

        Usage:
        ::

            result = await api.update_user(
                cluster_id="example",
                username="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cluster_id = validate_path_param("cluster_id", cluster_id)
        param_username = validate_path_param("username", username)

        res = self._request(
            "PATCH",
            f"/kafka/v1alpha1/regions/{param_region}/clusters/{param_cluster_id}/users/{param_username}",
            body=marshal_UpdateUserRequest(
                UpdateUserRequest(
                    cluster_id=cluster_id,
                    username=username,
                    region=region,
                    password=password,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_User(res.json())
