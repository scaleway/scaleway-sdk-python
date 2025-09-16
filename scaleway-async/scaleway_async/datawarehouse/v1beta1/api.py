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
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    ListDatabasesRequestOrderBy,
    ListDeploymentsRequestOrderBy,
    ListUsersRequestOrderBy,
    CreateDatabaseRequest,
    CreateDeploymentRequest,
    CreateEndpointRequest,
    CreateUserRequest,
    Database,
    Deployment,
    Endpoint,
    EndpointSpec,
    ListDatabasesResponse,
    ListDeploymentsResponse,
    ListPresetsResponse,
    ListUsersResponse,
    ListVersionsResponse,
    Preset,
    UpdateDeploymentRequest,
    UpdateUserRequest,
    User,
    Version,
)
from .content import (
    DEPLOYMENT_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Endpoint,
    unmarshal_Database,
    unmarshal_Deployment,
    unmarshal_User,
    unmarshal_ListDatabasesResponse,
    unmarshal_ListDeploymentsResponse,
    unmarshal_ListPresetsResponse,
    unmarshal_ListUsersResponse,
    unmarshal_ListVersionsResponse,
    marshal_CreateDatabaseRequest,
    marshal_CreateDeploymentRequest,
    marshal_CreateEndpointRequest,
    marshal_CreateUserRequest,
    marshal_UpdateDeploymentRequest,
    marshal_UpdateUserRequest,
)


class DatawarehouseV1Beta1API(API):
    """
    This API allows you to manage your Data Warehouse.
    """

    async def list_presets(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListPresetsResponse:
        """
        List available presets.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :return: :class:`ListPresetsResponse <ListPresetsResponse>`

        Usage:
        ::

            result = await api.list_presets()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/datawarehouse/v1beta1/regions/{param_region}/presets",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPresetsResponse(res.json())

    async def list_presets_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[Preset]:
        """
        List available presets.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :return: :class:`list[Preset] <list[Preset]>`

        Usage:
        ::

            result = await api.list_presets_all()
        """

        return await fetch_all_pages_async(
            type=ListPresetsResponse,
            key="presets",
            fetcher=self.list_presets,
            args={
                "region": region,
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
        List available Clickhouse versions.
        :param region: Region to target. If none is passed will use default region from the config.
        :param version:
        :param page:
        :param page_size:
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
            f"/datawarehouse/v1beta1/regions/{param_region}/versions",
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
        List available Clickhouse versions.
        :param region: Region to target. If none is passed will use default region from the config.
        :param version:
        :param page:
        :param page_size:
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

    async def list_deployments(
        self,
        *,
        region: Optional[ScwRegion] = None,
        tags: Optional[list[str]] = None,
        name: Optional[str] = None,
        order_by: Optional[ListDeploymentsRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListDeploymentsResponse:
        """
        List deployments.
        List all deployments in the specified region, for a given Scaleway Project. By default, the deployments returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field. You can define additional parameters for your query, such as `tags` and `name`. For the `name` parameter, the value you provide will be checked against the whole name string to see if it includes the string you put in the parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param tags: List deployments with a given tag.
        :param name: Lists deployments that match a name pattern.
        :param order_by: Criteria to use when ordering deployment listings.
        :param organization_id: Organization ID the deployment belongs to.
        :param project_id: Project ID the deployment belongs to.
        :param page:
        :param page_size:
        :return: :class:`ListDeploymentsResponse <ListDeploymentsResponse>`

        Usage:
        ::

            result = await api.list_deployments()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/datawarehouse/v1beta1/regions/{param_region}/deployments",
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
        return unmarshal_ListDeploymentsResponse(res.json())

    async def list_deployments_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        tags: Optional[list[str]] = None,
        name: Optional[str] = None,
        order_by: Optional[ListDeploymentsRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[Deployment]:
        """
        List deployments.
        List all deployments in the specified region, for a given Scaleway Project. By default, the deployments returned in the list are ordered by creation date in ascending order, though this can be modified via the order_by field. You can define additional parameters for your query, such as `tags` and `name`. For the `name` parameter, the value you provide will be checked against the whole name string to see if it includes the string you put in the parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param tags: List deployments with a given tag.
        :param name: Lists deployments that match a name pattern.
        :param order_by: Criteria to use when ordering deployment listings.
        :param organization_id: Organization ID the deployment belongs to.
        :param project_id: Project ID the deployment belongs to.
        :param page:
        :param page_size:
        :return: :class:`list[Deployment] <list[Deployment]>`

        Usage:
        ::

            result = await api.list_deployments_all()
        """

        return await fetch_all_pages_async(
            type=ListDeploymentsResponse,
            key="deployments",
            fetcher=self.list_deployments,
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

    async def get_deployment(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Deployment:
        """
        Get a deployment.
        Retrieve information about a given deployment, specified by the `region` and `deployment_id` parameters. Its full details, including name, status are returned in the response object.
        :param deployment_id: UUID of the deployment.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Deployment <Deployment>`

        Usage:
        ::

            result = await api.get_deployment(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "GET",
            f"/datawarehouse/v1beta1/regions/{param_region}/deployments/{param_deployment_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Deployment(res.json())

    async def wait_for_deployment(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[
            WaitForOptions[Deployment, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> Deployment:
        """
        Get a deployment.
        Retrieve information about a given deployment, specified by the `region` and `deployment_id` parameters. Its full details, including name, status are returned in the response object.
        :param deployment_id: UUID of the deployment.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Deployment <Deployment>`

        Usage:
        ::

            result = await api.get_deployment(
                deployment_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in DEPLOYMENT_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_deployment,
            options=options,
            args={
                "deployment_id": deployment_id,
                "region": region,
            },
        )

    async def create_deployment(
        self,
        *,
        name: str,
        version: str,
        replica_count: int,
        password: str,
        cpu_min: int,
        cpu_max: int,
        ram_per_cpu: int,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
        endpoints: Optional[list[EndpointSpec]] = None,
    ) -> Deployment:
        """
        Create a deployment.
        Create a new deployment.
        :param name: Name of the deployment.
        :param version: Clickhouse version to use for the deployment.
        :param replica_count: Number of replicas for the deployment.
        :param password: Password for the initial user.
        :param cpu_min: Minimum CPU count for the deployment.
        :param cpu_max: Maximum CPU count for the deployment.
        :param ram_per_cpu: RAM per CPU count for the deployment (in GB).
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: The Project ID on which the deployment will be created.
        :param tags: Tags to apply to the deployment.
        :param endpoints: Endpoints to associate with the deployment.
        :return: :class:`Deployment <Deployment>`

        Usage:
        ::

            result = await api.create_deployment(
                name="example",
                version="example",
                replica_count=1,
                password="example",
                cpu_min=1,
                cpu_max=1,
                ram_per_cpu=1,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/datawarehouse/v1beta1/regions/{param_region}/deployments",
            body=marshal_CreateDeploymentRequest(
                CreateDeploymentRequest(
                    name=name,
                    version=version,
                    replica_count=replica_count,
                    password=password,
                    cpu_min=cpu_min,
                    cpu_max=cpu_max,
                    ram_per_cpu=ram_per_cpu,
                    region=region,
                    project_id=project_id,
                    tags=tags,
                    endpoints=endpoints,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Deployment(res.json())

    async def update_deployment(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        cpu_min: Optional[int] = None,
        cpu_max: Optional[int] = None,
        replica_count: Optional[int] = None,
    ) -> Deployment:
        """
        Update a deployment.
        Update the parameters of a deployment.
        :param deployment_id: UUID of the deployment to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the deployment.
        :param tags: Tags of a deployment.
        :param cpu_min: Minimum CPU count for the deployment.
        :param cpu_max: Maximum CPU count for the deployment.
        :param replica_count: Number of replicas for the deployment.
        :return: :class:`Deployment <Deployment>`

        Usage:
        ::

            result = await api.update_deployment(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "PATCH",
            f"/datawarehouse/v1beta1/regions/{param_region}/deployments/{param_deployment_id}",
            body=marshal_UpdateDeploymentRequest(
                UpdateDeploymentRequest(
                    deployment_id=deployment_id,
                    region=region,
                    name=name,
                    tags=tags,
                    cpu_min=cpu_min,
                    cpu_max=cpu_max,
                    replica_count=replica_count,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Deployment(res.json())

    async def delete_deployment(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Deployment:
        """
        Delete a deployment.
        Delete a given deployment, specified by the `region` and `deployment_id` parameters. Deleting a deployment is permanent, and cannot be undone. Upon deletion, deletion all your data will be lost.
        :param deployment_id: UUID of the deployment to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Deployment <Deployment>`

        Usage:
        ::

            result = await api.delete_deployment(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "DELETE",
            f"/datawarehouse/v1beta1/regions/{param_region}/deployments/{param_deployment_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Deployment(res.json())

    async def get_deployment_certificate(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
    ) -> ScwFile:
        """
        :param deployment_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ScwFile <ScwFile>`

        Usage:
        ::

            result = await api.get_deployment_certificate(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "GET",
            f"/datawarehouse/v1beta1/regions/{param_region}/deployments/{param_deployment_id}/certificate",
        )

        self._throw_on_error(res)
        return unmarshal_ScwFile(res.json())

    async def list_users(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        order_by: Optional[ListUsersRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListUsersResponse:
        """
        List users associated with a deployment.
        :param deployment_id: UUID of the deployment.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the user to filter by.
        :param order_by: Criteria to use when ordering user listings.
        :param page:
        :param page_size:
        :return: :class:`ListUsersResponse <ListUsersResponse>`

        Usage:
        ::

            result = await api.list_users(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "GET",
            f"/datawarehouse/v1beta1/regions/{param_region}/deployments/{param_deployment_id}/users",
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
        deployment_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        order_by: Optional[ListUsersRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[User]:
        """
        List users associated with a deployment.
        :param deployment_id: UUID of the deployment.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the user to filter by.
        :param order_by: Criteria to use when ordering user listings.
        :param page:
        :param page_size:
        :return: :class:`list[User] <list[User]>`

        Usage:
        ::

            result = await api.list_users_all(
                deployment_id="example",
            )
        """

        return await fetch_all_pages_async(
            type=ListUsersResponse,
            key="users",
            fetcher=self.list_users,
            args={
                "deployment_id": deployment_id,
                "region": region,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    async def create_user(
        self,
        *,
        deployment_id: str,
        name: str,
        password: str,
        is_admin: bool,
        region: Optional[ScwRegion] = None,
    ) -> User:
        """
        Create a new user for a deployment.
        :param deployment_id: UUID of the deployment.
        :param name: Name of the user.
        :param password: Password for the user.
        :param is_admin: Indicates if the user is an administrator.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`User <User>`

        Usage:
        ::

            result = await api.create_user(
                deployment_id="example",
                name="example",
                password="example",
                is_admin=False,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "POST",
            f"/datawarehouse/v1beta1/regions/{param_region}/deployments/{param_deployment_id}/users",
            body=marshal_CreateUserRequest(
                CreateUserRequest(
                    deployment_id=deployment_id,
                    name=name,
                    password=password,
                    is_admin=is_admin,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_User(res.json())

    async def update_user(
        self,
        *,
        deployment_id: str,
        name: str,
        region: Optional[ScwRegion] = None,
        password: Optional[str] = None,
        is_admin: Optional[bool] = None,
    ) -> User:
        """
        Update an existing user for a deployment.
        :param deployment_id: UUID of the deployment.
        :param name: Name of the user.
        :param region: Region to target. If none is passed will use default region from the config.
        :param password: New password for the user.
        :param is_admin: Updates the user administrator permissions.
        :return: :class:`User <User>`

        Usage:
        ::

            result = await api.update_user(
                deployment_id="example",
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)
        param_name = validate_path_param("name", name)

        res = self._request(
            "PATCH",
            f"/datawarehouse/v1beta1/regions/{param_region}/deployments/{param_deployment_id}/users/{param_name}",
            body=marshal_UpdateUserRequest(
                UpdateUserRequest(
                    deployment_id=deployment_id,
                    name=name,
                    region=region,
                    password=password,
                    is_admin=is_admin,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_User(res.json())

    async def delete_user(
        self,
        *,
        deployment_id: str,
        name: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a user from a deployment.
        :param deployment_id: UUID of the deployment.
        :param name: Name of the user to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_user(
                deployment_id="example",
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)
        param_name = validate_path_param("name", name)

        res = self._request(
            "DELETE",
            f"/datawarehouse/v1beta1/regions/{param_region}/deployments/{param_deployment_id}/users/{param_name}",
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
        Delete an endpoint from a deployment.
        :param endpoint_id: UUID of the Endpoint to delete.
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
            f"/datawarehouse/v1beta1/regions/{param_region}/endpoints/{param_endpoint_id}",
        )

        self._throw_on_error(res)

    async def create_endpoint(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
        endpoint: Optional[EndpointSpec] = None,
    ) -> Endpoint:
        """
        Create a new endpoint for a deployment.
        :param deployment_id: UUID of the deployment.
        :param region: Region to target. If none is passed will use default region from the config.
        :param endpoint: Endpoint specification.
        :return: :class:`Endpoint <Endpoint>`

        Usage:
        ::

            result = await api.create_endpoint(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/datawarehouse/v1beta1/regions/{param_region}/endpoints",
            body=marshal_CreateEndpointRequest(
                CreateEndpointRequest(
                    deployment_id=deployment_id,
                    region=region,
                    endpoint=endpoint,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Endpoint(res.json())

    async def list_databases(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        order_by: Optional[ListDatabasesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListDatabasesResponse:
        """
        List databases within a deployment.
        :param deployment_id: UUID of the deployment.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the database to filter by.
        :param order_by: Criteria to use when ordering database listings.
        :param page:
        :param page_size:
        :return: :class:`ListDatabasesResponse <ListDatabasesResponse>`

        Usage:
        ::

            result = await api.list_databases(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "GET",
            f"/datawarehouse/v1beta1/regions/{param_region}/deployments/{param_deployment_id}/databases",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDatabasesResponse(res.json())

    async def list_databases_all(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        order_by: Optional[ListDatabasesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[Database]:
        """
        List databases within a deployment.
        :param deployment_id: UUID of the deployment.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the database to filter by.
        :param order_by: Criteria to use when ordering database listings.
        :param page:
        :param page_size:
        :return: :class:`list[Database] <list[Database]>`

        Usage:
        ::

            result = await api.list_databases_all(
                deployment_id="example",
            )
        """

        return await fetch_all_pages_async(
            type=ListDatabasesResponse,
            key="databases",
            fetcher=self.list_databases,
            args={
                "deployment_id": deployment_id,
                "region": region,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    async def create_database(
        self,
        *,
        deployment_id: str,
        name: str,
        region: Optional[ScwRegion] = None,
    ) -> Database:
        """
        Create a new database within a deployment.
        :param deployment_id: UUID of the deployment.
        :param name: Name of the database.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Database <Database>`

        Usage:
        ::

            result = await api.create_database(
                deployment_id="example",
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "POST",
            f"/datawarehouse/v1beta1/regions/{param_region}/deployments/{param_deployment_id}/databases",
            body=marshal_CreateDatabaseRequest(
                CreateDatabaseRequest(
                    deployment_id=deployment_id,
                    name=name,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Database(res.json())

    async def delete_database(
        self,
        *,
        deployment_id: str,
        name: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a database from a deployment.
        :param deployment_id: UUID of the deployment.
        :param name: Name of the database to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_database(
                deployment_id="example",
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)
        param_name = validate_path_param("name", name)

        res = self._request(
            "DELETE",
            f"/datawarehouse/v1beta1/regions/{param_region}/deployments/{param_deployment_id}/databases/{param_name}",
        )

        self._throw_on_error(res)
