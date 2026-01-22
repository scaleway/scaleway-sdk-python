# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    WaitForOptions,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
)
from .types import (
    ListDeploymentsRequestOrderBy,
    ListNodeTypesRequestOrderBy,
    ListUsersRequestOrderBy,
    ListVersionsRequestOrderBy,
    CreateDeploymentRequest,
    CreateEndpointRequest,
    CreateUserRequest,
    Deployment,
    Endpoint,
    EndpointSpec,
    ListDeploymentsResponse,
    ListNodeTypesResponse,
    ListUsersResponse,
    ListVersionsResponse,
    NodeType,
    UpdateDeploymentRequest,
    UpdateUserRequest,
    UpgradeDeploymentRequest,
    User,
    Version,
    Volume,
)
from .content import (
    DEPLOYMENT_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Endpoint,
    unmarshal_Deployment,
    unmarshal_User,
    unmarshal_ListDeploymentsResponse,
    unmarshal_ListNodeTypesResponse,
    unmarshal_ListUsersResponse,
    unmarshal_ListVersionsResponse,
    marshal_CreateDeploymentRequest,
    marshal_CreateEndpointRequest,
    marshal_CreateUserRequest,
    marshal_UpdateDeploymentRequest,
    marshal_UpdateUserRequest,
    marshal_UpgradeDeploymentRequest,
)


class SearchdbV1Alpha1API(API):
    """
    The Cloud Essentials for Opensearch API allows you to manage your Opensearch resources.
    """

    def create_deployment(
        self,
        *,
        name: str,
        node_amount: int,
        node_type: str,
        version: str,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
        user_name: Optional[str] = None,
        password: Optional[str] = None,
        volume: Optional[Volume] = None,
        endpoints: Optional[list[EndpointSpec]] = None,
    ) -> Deployment:
        """
        Create a new Cloud Essentials for OpenSearch deployment.
        :param name: Name of the deployment.
        :param node_amount: Number of nodes.
        :param node_type: Node type.
        :param version: The Opensearch version to use.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project ID in which to create the deployment.
        :param tags: Tags.
        :param user_name: Username for the deployment user.
        :param password: Password for the deployment user.
        :param volume: Volume.
        :param endpoints: Endpoints to access the deployment.
        :return: :class:`Deployment <Deployment>`

        Usage:
        ::

            result = api.create_deployment(
                name="example",
                node_amount=1,
                node_type="example",
                version="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/searchdb/v1alpha1/regions/{param_region}/deployments",
            body=marshal_CreateDeploymentRequest(
                CreateDeploymentRequest(
                    name=name,
                    node_amount=node_amount,
                    node_type=node_type,
                    version=version,
                    region=region,
                    project_id=project_id,
                    tags=tags,
                    user_name=user_name,
                    password=password,
                    volume=volume,
                    endpoints=endpoints,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Deployment(res.json())

    def update_deployment(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> Deployment:
        """
        Update a Cloud Essentials for OpenSearch deployment.
        :param deployment_id: UUID of the deployment to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the deployment.
        :param tags: Tags of a deployment.
        :return: :class:`Deployment <Deployment>`

        Usage:
        ::

            result = api.update_deployment(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "PATCH",
            f"/searchdb/v1alpha1/regions/{param_region}/deployments/{param_deployment_id}",
            body=marshal_UpdateDeploymentRequest(
                UpdateDeploymentRequest(
                    deployment_id=deployment_id,
                    region=region,
                    name=name,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Deployment(res.json())

    def upgrade_deployment(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
        node_amount: Optional[int] = None,
        volume_size_bytes: Optional[int] = None,
    ) -> Deployment:
        """
        Upgrade a Cloud Essentials for OpenSearch deployment.
        :param deployment_id: UUID of the Deployment to upgrade.
        :param region: Region to target. If none is passed will use default region from the config.
        :param node_amount: Amount of node upgrade target.
        One-Of ('upgrade_target'): at most one of 'node_amount', 'volume_size_bytes' could be set.
        :param volume_size_bytes: Volume size upgrade target.
        One-Of ('upgrade_target'): at most one of 'node_amount', 'volume_size_bytes' could be set.
        :return: :class:`Deployment <Deployment>`

        Usage:
        ::

            result = api.upgrade_deployment(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "POST",
            f"/searchdb/v1alpha1/regions/{param_region}/deployments/{param_deployment_id}/upgrade",
            body=marshal_UpgradeDeploymentRequest(
                UpgradeDeploymentRequest(
                    deployment_id=deployment_id,
                    region=region,
                    node_amount=node_amount,
                    volume_size_bytes=volume_size_bytes,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Deployment(res.json())

    def get_deployment(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Deployment:
        """
        Retrieve a specific Cloud Essentials for OpenSearch deployment.
        :param deployment_id: ID of the deployment.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Deployment <Deployment>`

        Usage:
        ::

            result = api.get_deployment(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "GET",
            f"/searchdb/v1alpha1/regions/{param_region}/deployments/{param_deployment_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Deployment(res.json())

    def wait_for_deployment(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[WaitForOptions[Deployment, bool]] = None,
    ) -> Deployment:
        """
        Retrieve a specific Cloud Essentials for OpenSearch deployment.
        :param deployment_id: ID of the deployment.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Deployment <Deployment>`

        Usage:
        ::

            result = api.get_deployment(
                deployment_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in DEPLOYMENT_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_deployment,
            options=options,
            args={
                "deployment_id": deployment_id,
                "region": region,
            },
        )

    def delete_deployment(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Deployment:
        """
        Delete a Cloud Essentials for OpenSearch deployment.
        :param deployment_id: ID of the deployment.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Deployment <Deployment>`

        Usage:
        ::

            result = api.delete_deployment(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "DELETE",
            f"/searchdb/v1alpha1/regions/{param_region}/deployments/{param_deployment_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Deployment(res.json())

    def list_deployments(
        self,
        *,
        region: Optional[ScwRegion] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        order_by: Optional[ListDeploymentsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        tags: Optional[list[str]] = None,
        name: Optional[str] = None,
        version: Optional[str] = None,
    ) -> ListDeploymentsResponse:
        """
        Retrieve a list of Cloud Essentials for OpenSearch deployments.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: ID of the Organization containing the deployments.
        :param project_id: ID of the Project containing the deployments.
        :param order_by: Define the order of the returned deployments.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of deployments to return.
        :param tags: Filter by tag, only deployments with one or more matching tags will be returned.
        :param name: Deployment name to filter for.
        :param version: Engine version to filter for.
        :return: :class:`ListDeploymentsResponse <ListDeploymentsResponse>`

        Usage:
        ::

            result = api.list_deployments()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/searchdb/v1alpha1/regions/{param_region}/deployments",
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
        return unmarshal_ListDeploymentsResponse(res.json())

    def list_deployments_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        order_by: Optional[ListDeploymentsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        tags: Optional[list[str]] = None,
        name: Optional[str] = None,
        version: Optional[str] = None,
    ) -> list[Deployment]:
        """
        Retrieve a list of Cloud Essentials for OpenSearch deployments.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: ID of the Organization containing the deployments.
        :param project_id: ID of the Project containing the deployments.
        :param order_by: Define the order of the returned deployments.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of deployments to return.
        :param tags: Filter by tag, only deployments with one or more matching tags will be returned.
        :param name: Deployment name to filter for.
        :param version: Engine version to filter for.
        :return: :class:`list[Deployment] <list[Deployment]>`

        Usage:
        ::

            result = api.list_deployments_all()
        """

        return fetch_all_pages(
            type=ListDeploymentsResponse,
            key="deployments",
            fetcher=self.list_deployments,
            args={
                "region": region,
                "organization_id": organization_id,
                "project_id": project_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "tags": tags,
                "name": name,
                "version": version,
            },
        )

    def list_versions(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListVersionsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        version: Optional[str] = None,
    ) -> ListVersionsResponse:
        """
        List available Cloud Essentials for OpenSearch versions.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Define the order of the returned version.
        :param page: The page number to return, form the paginated results.
        :param page_size: Number of version to return.
        :param version: Filter by version.
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
            f"/searchdb/v1alpha1/regions/{param_region}/versions",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "version": version,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListVersionsResponse(res.json())

    def list_versions_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListVersionsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        version: Optional[str] = None,
    ) -> list[Version]:
        """
        List available Cloud Essentials for OpenSearch versions.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Define the order of the returned version.
        :param page: The page number to return, form the paginated results.
        :param page_size: Number of version to return.
        :param version: Filter by version.
        :return: :class:`list[Version] <list[Version]>`

        Usage:
        ::

            result = api.list_versions_all()
        """

        return fetch_all_pages(
            type=ListVersionsResponse,
            key="versions",
            fetcher=self.list_versions,
            args={
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "version": version,
            },
        )

    def list_node_types(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListNodeTypesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListNodeTypesResponse:
        """
        Retrieve a list of available node types.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of nodes in the response (name, vcpus or memory).
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of node types to return.
        :return: :class:`ListNodeTypesResponse <ListNodeTypesResponse>`

        Usage:
        ::

            result = api.list_node_types()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/searchdb/v1alpha1/regions/{param_region}/node-types",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListNodeTypesResponse(res.json())

    def list_node_types_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListNodeTypesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[NodeType]:
        """
        Retrieve a list of available node types.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of nodes in the response (name, vcpus or memory).
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of node types to return.
        :return: :class:`list[NodeType] <list[NodeType]>`

        Usage:
        ::

            result = api.list_node_types_all()
        """

        return fetch_all_pages(
            type=ListNodeTypesResponse,
            key="node_types",
            fetcher=self.list_node_types,
            args={
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    def create_endpoint(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
        endpoint_spec: Optional[EndpointSpec] = None,
    ) -> Endpoint:
        """
        Create a new endpoint on a deployment.
        :param deployment_id: ID of the deployment for which to create an endpoint.
        :param region: Region to target. If none is passed will use default region from the config.
        :param endpoint_spec: Specification of the endpoint you want to create.
        :return: :class:`Endpoint <Endpoint>`

        Usage:
        ::

            result = api.create_endpoint(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/searchdb/v1alpha1/regions/{param_region}/endpoints",
            body=marshal_CreateEndpointRequest(
                CreateEndpointRequest(
                    deployment_id=deployment_id,
                    region=region,
                    endpoint_spec=endpoint_spec,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Endpoint(res.json())

    def delete_endpoint(
        self,
        *,
        endpoint_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete an existing endpoint.
        :param endpoint_id: ID of the endpoint to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_endpoint(
                endpoint_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_endpoint_id = validate_path_param("endpoint_id", endpoint_id)

        res = self._request(
            "DELETE",
            f"/searchdb/v1alpha1/regions/{param_region}/endpoints/{param_endpoint_id}",
        )

        self._throw_on_error(res)

    def list_users(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListUsersRequestOrderBy] = None,
        name: Optional[str] = None,
    ) -> ListUsersResponse:
        """
        Retrieve a list of deployment users.
        :param deployment_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param name:
        :return: :class:`ListUsersResponse <ListUsersResponse>`

        Usage:
        ::

            result = api.list_users(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "GET",
            f"/searchdb/v1alpha1/regions/{param_region}/deployments/{param_deployment_id}/users",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListUsersResponse(res.json())

    def list_users_all(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListUsersRequestOrderBy] = None,
        name: Optional[str] = None,
    ) -> list[User]:
        """
        Retrieve a list of deployment users.
        :param deployment_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param name:
        :return: :class:`list[User] <list[User]>`

        Usage:
        ::

            result = api.list_users_all(
                deployment_id="example",
            )
        """

        return fetch_all_pages(
            type=ListUsersResponse,
            key="users",
            fetcher=self.list_users,
            args={
                "deployment_id": deployment_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "name": name,
            },
        )

    def create_user(
        self,
        *,
        deployment_id: str,
        username: str,
        password: str,
        region: Optional[ScwRegion] = None,
    ) -> User:
        """
        Create a new user.
        :param deployment_id: ID of the deployment in which to create the user.
        :param username: Username of the deployment user.
        :param password: Password of the deployment user.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`User <User>`

        Usage:
        ::

            result = api.create_user(
                deployment_id="example",
                username="example",
                password="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "POST",
            f"/searchdb/v1alpha1/regions/{param_region}/deployments/{param_deployment_id}/users",
            body=marshal_CreateUserRequest(
                CreateUserRequest(
                    deployment_id=deployment_id,
                    username=username,
                    password=password,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_User(res.json())

    def update_user(
        self,
        *,
        deployment_id: str,
        username: str,
        region: Optional[ScwRegion] = None,
        password: Optional[str] = None,
    ) -> User:
        """
        Update an existing user.
        :param deployment_id: ID of the deployment in which to create the user.
        :param username: Username of the deployment user.
        :param region: Region to target. If none is passed will use default region from the config.
        :param password: Password of the deployment user.
        :return: :class:`User <User>`

        Usage:
        ::

            result = api.update_user(
                deployment_id="example",
                username="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)
        param_username = validate_path_param("username", username)

        res = self._request(
            "PATCH",
            f"/searchdb/v1alpha1/regions/{param_region}/deployments/{param_deployment_id}/users/{param_username}",
            body=marshal_UpdateUserRequest(
                UpdateUserRequest(
                    deployment_id=deployment_id,
                    username=username,
                    region=region,
                    password=password,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_User(res.json())

    def delete_user(
        self,
        *,
        deployment_id: str,
        username: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete an existing user.
        :param deployment_id: ID of the deployment in which to create the user.
        :param username: Username of the deployment user.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_user(
                deployment_id="example",
                username="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)
        param_username = validate_path_param("username", username)

        res = self._request(
            "DELETE",
            f"/searchdb/v1alpha1/regions/{param_region}/deployments/{param_deployment_id}/users/{param_username}",
        )

        self._throw_on_error(res)
