# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Any, Dict, List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    OneOfPossibility,
    WaitForOptions,
    fetch_all_pages,
    random_name,
    resolve_one_of,
    validate_path_param,
    wait_for_resource,
)
from .types import (
    ContainerHttpOption,
    ContainerPrivacy,
    ContainerProtocol,
    ListContainersRequestOrderBy,
    ListCronsRequestOrderBy,
    ListDomainsRequestOrderBy,
    ListLogsRequestOrderBy,
    ListNamespacesRequestOrderBy,
    ListTokensRequestOrderBy,
    Container,
    Cron,
    Domain,
    ListContainersResponse,
    ListCronsResponse,
    ListDomainsResponse,
    ListLogsResponse,
    ListNamespacesResponse,
    ListTokensResponse,
    Log,
    Namespace,
    Secret,
    Token,
    CreateNamespaceRequest,
    UpdateNamespaceRequest,
    CreateContainerRequest,
    UpdateContainerRequest,
    CreateCronRequest,
    UpdateCronRequest,
    CreateDomainRequest,
    CreateTokenRequest,
)
from .content import (
    CONTAINER_TRANSIENT_STATUSES,
    CRON_TRANSIENT_STATUSES,
    DOMAIN_TRANSIENT_STATUSES,
    NAMESPACE_TRANSIENT_STATUSES,
    TOKEN_TRANSIENT_STATUSES,
)
from .marshalling import (
    marshal_CreateContainerRequest,
    marshal_CreateCronRequest,
    marshal_CreateDomainRequest,
    marshal_CreateNamespaceRequest,
    marshal_CreateTokenRequest,
    marshal_UpdateContainerRequest,
    marshal_UpdateCronRequest,
    marshal_UpdateNamespaceRequest,
    unmarshal_Container,
    unmarshal_Cron,
    unmarshal_Domain,
    unmarshal_Namespace,
    unmarshal_Token,
    unmarshal_ListContainersResponse,
    unmarshal_ListCronsResponse,
    unmarshal_ListDomainsResponse,
    unmarshal_ListLogsResponse,
    unmarshal_ListNamespacesResponse,
    unmarshal_ListTokensResponse,
)


class ContainerV1Beta1API(API):
    """
    Serverless Containers API.

    Serverless Containers API.
    """

    def list_namespaces(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListNamespacesRequestOrderBy = ListNamespacesRequestOrderBy.CREATED_AT_ASC,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListNamespacesResponse:
        """
        List all your namespaces.
        List all namespaces in a specified region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of namespaces per page.
        :param order_by: Order of the namespaces.
        :param name: Name of the namespaces.
        :param organization_id: UUID of the Organization the namespace belongs to.
        :param project_id: UUID of the Project the namespace belongs to.
        :return: :class:`ListNamespacesResponse <ListNamespacesResponse>`

        Usage:
        ::

            result = api.list_namespaces()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/containers/v1beta1/regions/{param_region}/namespaces",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListNamespacesResponse(res.json())

    def list_namespaces_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNamespacesRequestOrderBy] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Namespace]:
        """
        List all your namespaces.
        List all namespaces in a specified region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of namespaces per page.
        :param order_by: Order of the namespaces.
        :param name: Name of the namespaces.
        :param organization_id: UUID of the Organization the namespace belongs to.
        :param project_id: UUID of the Project the namespace belongs to.
        :return: :class:`List[ListNamespacesResponse] <List[ListNamespacesResponse]>`

        Usage:
        ::

            result = api.list_namespaces_all()
        """

        return fetch_all_pages(
            type=ListNamespacesResponse,
            key="namespaces",
            fetcher=self.list_namespaces,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "name": name,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    def get_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
    ) -> Namespace:
        """
        Get a namespace.
        Get the namespace associated with the specified ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param namespace_id: UUID of the namespace to get.
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = api.get_namespace(namespace_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_namespace_id = validate_path_param("namespace_id", namespace_id)

        res = self._request(
            "GET",
            f"/containers/v1beta1/regions/{param_region}/namespaces/{param_namespace_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())

    def wait_for_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Namespace, bool]] = None,
    ) -> Namespace:
        """
        Waits for :class:`Namespace <Namespace>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config.
        :param namespace_id: UUID of the namespace to get.
        :param options: The options for the waiter
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = api.wait_for_namespace(namespace_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in NAMESPACE_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_namespace,
            options=options,
            args={
                "namespace_id": namespace_id,
                "region": region,
            },
        )

    def create_namespace(
        self,
        *,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        environment_variables: Optional[Dict[str, str]] = None,
        project_id: Optional[str] = None,
        description: Optional[str] = None,
        secret_environment_variables: Optional[List[Secret]] = None,
    ) -> Namespace:
        """
        Create a new namespace.
        Create a new namespace in a specified region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the namespace to create.
        :param environment_variables: Environment variables of the namespace to create.
        :param project_id: UUID of the Project in which the namespace will be created.
        :param description: Description of the namespace to create.
        :param secret_environment_variables: Secret environment variables of the namespace to create.
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = api.create_namespace()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/containers/v1beta1/regions/{param_region}/namespaces",
            body=marshal_CreateNamespaceRequest(
                CreateNamespaceRequest(
                    region=region,
                    name=name or random_name(prefix="cns"),
                    environment_variables=environment_variables,
                    project_id=project_id,
                    description=description,
                    secret_environment_variables=secret_environment_variables,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())

    def update_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
        environment_variables: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        secret_environment_variables: Optional[List[Secret]] = None,
    ) -> Namespace:
        """
        Update an existing namespace.
        Update the space associated with the specified ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param namespace_id: UUID of the namespace to update.
        :param environment_variables: Environment variables of the namespace to update.
        :param description: Description of the namespace to update.
        :param secret_environment_variables: Secret environment variables of the namespace to update.
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = api.update_namespace(namespace_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_namespace_id = validate_path_param("namespace_id", namespace_id)

        res = self._request(
            "PATCH",
            f"/containers/v1beta1/regions/{param_region}/namespaces/{param_namespace_id}",
            body=marshal_UpdateNamespaceRequest(
                UpdateNamespaceRequest(
                    namespace_id=namespace_id,
                    region=region,
                    environment_variables=environment_variables,
                    description=description,
                    secret_environment_variables=secret_environment_variables,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())

    def delete_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
    ) -> Namespace:
        """
        Delete an existing namespace.
        Delete the namespace associated with the specified ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param namespace_id: UUID of the namespace to delete.
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = api.delete_namespace(namespace_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_namespace_id = validate_path_param("namespace_id", namespace_id)

        res = self._request(
            "DELETE",
            f"/containers/v1beta1/regions/{param_region}/namespaces/{param_namespace_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())

    def list_containers(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListContainersRequestOrderBy = ListContainersRequestOrderBy.CREATED_AT_ASC,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListContainersResponse:
        """
        List all your containers.
        List all containers for a specified region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of containers per page.
        :param order_by: Order of the containers.
        :param namespace_id: UUID of the namespace the container belongs to.
        :param name: Name of the container.
        :param organization_id: UUID of the Organization the container belongs to.
        :param project_id: UUID of the Project the container belongs to.
        :return: :class:`ListContainersResponse <ListContainersResponse>`

        Usage:
        ::

            result = api.list_containers(namespace_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/containers/v1beta1/regions/{param_region}/containers",
            params={
                "name": name,
                "namespace_id": namespace_id,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListContainersResponse(res.json())

    def list_containers_all(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListContainersRequestOrderBy] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Container]:
        """
        List all your containers.
        List all containers for a specified region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of containers per page.
        :param order_by: Order of the containers.
        :param namespace_id: UUID of the namespace the container belongs to.
        :param name: Name of the container.
        :param organization_id: UUID of the Organization the container belongs to.
        :param project_id: UUID of the Project the container belongs to.
        :return: :class:`List[ListContainersResponse] <List[ListContainersResponse]>`

        Usage:
        ::

            result = api.list_containers_all(namespace_id="example")
        """

        return fetch_all_pages(
            type=ListContainersResponse,
            key="containers",
            fetcher=self.list_containers,
            args={
                "namespace_id": namespace_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "name": name,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    def get_container(
        self,
        *,
        container_id: str,
        region: Optional[Region] = None,
    ) -> Container:
        """
        Get a container.
        Get the container associated with the specified ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param container_id: UUID of the container to get.
        :return: :class:`Container <Container>`

        Usage:
        ::

            result = api.get_container(container_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_container_id = validate_path_param("container_id", container_id)

        res = self._request(
            "GET",
            f"/containers/v1beta1/regions/{param_region}/containers/{param_container_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Container(res.json())

    def wait_for_container(
        self,
        *,
        container_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Container, bool]] = None,
    ) -> Container:
        """
        Waits for :class:`Container <Container>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config.
        :param container_id: UUID of the container to get.
        :param options: The options for the waiter
        :return: :class:`Container <Container>`

        Usage:
        ::

            result = api.wait_for_container(container_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in CONTAINER_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_container,
            options=options,
            args={
                "container_id": container_id,
                "region": region,
            },
        )

    def create_container(
        self,
        *,
        namespace_id: str,
        name: str,
        privacy: ContainerPrivacy,
        protocol: ContainerProtocol,
        http_option: ContainerHttpOption,
        region: Optional[Region] = None,
        environment_variables: Optional[Dict[str, str]] = None,
        min_scale: Optional[int] = None,
        max_scale: Optional[int] = None,
        memory_limit: Optional[int] = None,
        cpu_limit: Optional[int] = None,
        timeout: Optional[str] = None,
        description: Optional[str] = None,
        registry_image: Optional[str] = None,
        max_concurrency: Optional[int] = None,
        port: Optional[int] = None,
        secret_environment_variables: Optional[List[Secret]] = None,
    ) -> Container:
        """
        Create a new container.
        Create a new container in the specified region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param namespace_id: UUID of the namespace the container belongs to.
        :param name: Name of the container.
        :param environment_variables: Environment variables of the container.
        :param min_scale: Minimum number of instances to scale the container to.
        :param max_scale: Maximum number of instances to scale the container to.
        :param memory_limit: Memory limit of the container in MB.
        :param cpu_limit: CPU limit of the container in mvCPU.
        :param timeout: Processing time limit for the container.
        :param privacy: Privacy setting of the container.
        :param description: Description of the container.
        :param registry_image: Name of the registry image (e.g. "rg.fr-par.scw.cloud/something/image:tag").
        :param max_concurrency: Number of maximum concurrent executions of the container.
        :param protocol: Protocol the container uses.
        :param port: Port the container listens on.
        :param secret_environment_variables: Secret environment variables of the container.
        :param http_option: Configure how HTTP and HTTPS requests are handled.
        Possible values:
         - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
         - enabled: Serve both HTTP and HTTPS traffic.
        :return: :class:`Container <Container>`

        Usage:
        ::

            result = api.create_container(
                namespace_id="example",
                name="example",
                privacy=unknown_privacy,
                protocol=unknown_protocol,
                http_option=unknown_http_option,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/containers/v1beta1/regions/{param_region}/containers",
            body=marshal_CreateContainerRequest(
                CreateContainerRequest(
                    namespace_id=namespace_id,
                    name=name,
                    privacy=privacy,
                    protocol=protocol,
                    http_option=http_option,
                    region=region,
                    environment_variables=environment_variables,
                    min_scale=min_scale,
                    max_scale=max_scale,
                    memory_limit=memory_limit,
                    cpu_limit=cpu_limit,
                    timeout=timeout,
                    description=description,
                    registry_image=registry_image,
                    max_concurrency=max_concurrency,
                    port=port,
                    secret_environment_variables=secret_environment_variables,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Container(res.json())

    def update_container(
        self,
        *,
        container_id: str,
        privacy: ContainerPrivacy,
        protocol: ContainerProtocol,
        http_option: ContainerHttpOption,
        region: Optional[Region] = None,
        environment_variables: Optional[Dict[str, str]] = None,
        min_scale: Optional[int] = None,
        max_scale: Optional[int] = None,
        memory_limit: Optional[int] = None,
        cpu_limit: Optional[int] = None,
        timeout: Optional[str] = None,
        redeploy: Optional[bool] = None,
        description: Optional[str] = None,
        registry_image: Optional[str] = None,
        max_concurrency: Optional[int] = None,
        port: Optional[int] = None,
        secret_environment_variables: Optional[List[Secret]] = None,
    ) -> Container:
        """
        Update an existing container.
        Update the container associated with the specified ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param container_id: UUID of the container to update.
        :param environment_variables: Environment variables of the container.
        :param min_scale: Minimum number of instances to scale the container to.
        :param max_scale: Maximum number of instances to scale the container to.
        :param memory_limit: Memory limit of the container in MB.
        :param cpu_limit: CPU limit of the container in mvCPU.
        :param timeout: Processing time limit for the container.
        :param redeploy: Defines whether to redeploy failed containers.
        :param privacy: Privacy settings of the container.
        :param description: Description of the container.
        :param registry_image: Name of the registry image (e.g. "rg.fr-par.scw.cloud/something/image:tag").
        :param max_concurrency: Number of maximum concurrent executions of the container.
        :param protocol:
        :param port:
        :param secret_environment_variables:
        :param http_option: Configure how HTTP and HTTPS requests are handled.
        Possible values:
         - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
         - enabled: Serve both HTTP and HTTPS traffic.
        :return: :class:`Container <Container>`

        Usage:
        ::

            result = api.update_container(
                container_id="example",
                privacy=unknown_privacy,
                protocol=unknown_protocol,
                http_option=unknown_http_option,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_container_id = validate_path_param("container_id", container_id)

        res = self._request(
            "PATCH",
            f"/containers/v1beta1/regions/{param_region}/containers/{param_container_id}",
            body=marshal_UpdateContainerRequest(
                UpdateContainerRequest(
                    container_id=container_id,
                    privacy=privacy,
                    protocol=protocol,
                    http_option=http_option,
                    region=region,
                    environment_variables=environment_variables,
                    min_scale=min_scale,
                    max_scale=max_scale,
                    memory_limit=memory_limit,
                    cpu_limit=cpu_limit,
                    timeout=timeout,
                    redeploy=redeploy,
                    description=description,
                    registry_image=registry_image,
                    max_concurrency=max_concurrency,
                    port=port,
                    secret_environment_variables=secret_environment_variables,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Container(res.json())

    def delete_container(
        self,
        *,
        container_id: str,
        region: Optional[Region] = None,
    ) -> Container:
        """
        Delete a container.
        Delete the container associated with the specified ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param container_id: UUID of the container to delete.
        :return: :class:`Container <Container>`

        Usage:
        ::

            result = api.delete_container(container_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_container_id = validate_path_param("container_id", container_id)

        res = self._request(
            "DELETE",
            f"/containers/v1beta1/regions/{param_region}/containers/{param_container_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Container(res.json())

    def deploy_container(
        self,
        *,
        container_id: str,
        region: Optional[Region] = None,
    ) -> Container:
        """
        Deploy a container.
        Deploy a container associated with the specified ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param container_id: UUID of the container to deploy.
        :return: :class:`Container <Container>`

        Usage:
        ::

            result = api.deploy_container(container_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_container_id = validate_path_param("container_id", container_id)

        res = self._request(
            "POST",
            f"/containers/v1beta1/regions/{param_region}/containers/{param_container_id}/deploy",
        )

        self._throw_on_error(res)
        return unmarshal_Container(res.json())

    def list_crons(
        self,
        *,
        container_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListCronsRequestOrderBy = ListCronsRequestOrderBy.CREATED_AT_ASC,
    ) -> ListCronsResponse:
        """
        List all your crons.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of crons per page.
        :param order_by: Order of the crons.
        :param container_id: UUID of the container invoked by the cron.
        :return: :class:`ListCronsResponse <ListCronsResponse>`

        Usage:
        ::

            result = api.list_crons(container_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/containers/v1beta1/regions/{param_region}/crons",
            params={
                "container_id": container_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListCronsResponse(res.json())

    def list_crons_all(
        self,
        *,
        container_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListCronsRequestOrderBy] = None,
    ) -> List[Cron]:
        """
        List all your crons.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of crons per page.
        :param order_by: Order of the crons.
        :param container_id: UUID of the container invoked by the cron.
        :return: :class:`List[ListCronsResponse] <List[ListCronsResponse]>`

        Usage:
        ::

            result = api.list_crons_all(container_id="example")
        """

        return fetch_all_pages(
            type=ListCronsResponse,
            key="crons",
            fetcher=self.list_crons,
            args={
                "container_id": container_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    def get_cron(
        self,
        *,
        cron_id: str,
        region: Optional[Region] = None,
    ) -> Cron:
        """
        Get a cron.
        Get the cron associated with the specified ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cron_id: UUID of the cron to get.
        :return: :class:`Cron <Cron>`

        Usage:
        ::

            result = api.get_cron(cron_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cron_id = validate_path_param("cron_id", cron_id)

        res = self._request(
            "GET",
            f"/containers/v1beta1/regions/{param_region}/crons/{param_cron_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Cron(res.json())

    def wait_for_cron(
        self,
        *,
        cron_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Cron, bool]] = None,
    ) -> Cron:
        """
        Waits for :class:`Cron <Cron>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cron_id: UUID of the cron to get.
        :param options: The options for the waiter
        :return: :class:`Cron <Cron>`

        Usage:
        ::

            result = api.wait_for_cron(cron_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in CRON_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_cron,
            options=options,
            args={
                "cron_id": cron_id,
                "region": region,
            },
        )

    def create_cron(
        self,
        *,
        container_id: str,
        schedule: str,
        region: Optional[Region] = None,
        args: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
    ) -> Cron:
        """
        Create a new cron.
        :param region: Region to target. If none is passed will use default region from the config.
        :param container_id: UUID of the container to invoke by the cron.
        :param schedule: UNIX cron shedule.
        :param args: Arguments to pass with the cron.
        :param name: Name of the cron to create.
        :return: :class:`Cron <Cron>`

        Usage:
        ::

            result = api.create_cron(
                container_id="example",
                schedule="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/containers/v1beta1/regions/{param_region}/crons",
            body=marshal_CreateCronRequest(
                CreateCronRequest(
                    container_id=container_id,
                    schedule=schedule,
                    region=region,
                    args=args,
                    name=name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Cron(res.json())

    def update_cron(
        self,
        *,
        cron_id: str,
        region: Optional[Region] = None,
        container_id: Optional[str] = None,
        schedule: Optional[str] = None,
        args: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
    ) -> Cron:
        """
        Update an existing cron.
        Update the cron associated with the specified ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cron_id: UUID of the cron to update.
        :param container_id: UUID of the container invoked by the cron.
        :param schedule: UNIX cron schedule.
        :param args: Arguments to pass with the cron.
        :param name: Name of the cron.
        :return: :class:`Cron <Cron>`

        Usage:
        ::

            result = api.update_cron(cron_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cron_id = validate_path_param("cron_id", cron_id)

        res = self._request(
            "PATCH",
            f"/containers/v1beta1/regions/{param_region}/crons/{param_cron_id}",
            body=marshal_UpdateCronRequest(
                UpdateCronRequest(
                    cron_id=cron_id,
                    region=region,
                    container_id=container_id,
                    schedule=schedule,
                    args=args,
                    name=name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Cron(res.json())

    def delete_cron(
        self,
        *,
        cron_id: str,
        region: Optional[Region] = None,
    ) -> Cron:
        """
        Delete an existing cron.
        Delete the cron associated with the specified ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param cron_id: UUID of the cron to delete.
        :return: :class:`Cron <Cron>`

        Usage:
        ::

            result = api.delete_cron(cron_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cron_id = validate_path_param("cron_id", cron_id)

        res = self._request(
            "DELETE",
            f"/containers/v1beta1/regions/{param_region}/crons/{param_cron_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Cron(res.json())

    def list_logs(
        self,
        *,
        container_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListLogsRequestOrderBy = ListLogsRequestOrderBy.TIMESTAMP_DESC,
    ) -> ListLogsResponse:
        """
        List your container logs.
        List the logs of the container with the specified ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param container_id: UUID of the container.
        :param page: Page number.
        :param page_size: Number of logs per page.
        :param order_by: Order of the logs.
        :return: :class:`ListLogsResponse <ListLogsResponse>`

        Usage:
        ::

            result = api.list_logs(container_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_container_id = validate_path_param("container_id", container_id)

        res = self._request(
            "GET",
            f"/containers/v1beta1/regions/{param_region}/containers/{param_container_id}/logs",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListLogsResponse(res.json())

    def list_logs_all(
        self,
        *,
        container_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListLogsRequestOrderBy] = None,
    ) -> List[Log]:
        """
        List your container logs.
        List the logs of the container with the specified ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param container_id: UUID of the container.
        :param page: Page number.
        :param page_size: Number of logs per page.
        :param order_by: Order of the logs.
        :return: :class:`List[ListLogsResponse] <List[ListLogsResponse]>`

        Usage:
        ::

            result = api.list_logs_all(container_id="example")
        """

        return fetch_all_pages(
            type=ListLogsResponse,
            key="logs",
            fetcher=self.list_logs,
            args={
                "container_id": container_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    def list_domains(
        self,
        *,
        container_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListDomainsRequestOrderBy = ListDomainsRequestOrderBy.CREATED_AT_ASC,
    ) -> ListDomainsResponse:
        """
        List all domain name bindings.
        List all domain name bindings in a specified region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of domains per page.
        :param order_by: Order of the domains.
        :param container_id: UUID of the container the domain belongs to.
        :return: :class:`ListDomainsResponse <ListDomainsResponse>`

        Usage:
        ::

            result = api.list_domains(container_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/containers/v1beta1/regions/{param_region}/domains",
            params={
                "container_id": container_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDomainsResponse(res.json())

    def list_domains_all(
        self,
        *,
        container_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDomainsRequestOrderBy] = None,
    ) -> List[Domain]:
        """
        List all domain name bindings.
        List all domain name bindings in a specified region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of domains per page.
        :param order_by: Order of the domains.
        :param container_id: UUID of the container the domain belongs to.
        :return: :class:`List[ListDomainsResponse] <List[ListDomainsResponse]>`

        Usage:
        ::

            result = api.list_domains_all(container_id="example")
        """

        return fetch_all_pages(
            type=ListDomainsResponse,
            key="domains",
            fetcher=self.list_domains,
            args={
                "container_id": container_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    def get_domain(
        self,
        *,
        domain_id: str,
        region: Optional[Region] = None,
    ) -> Domain:
        """
        Get a domain name binding.
        Get a domain name binding for the container with the specified ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param domain_id: UUID of the domain to get.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.get_domain(domain_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_domain_id = validate_path_param("domain_id", domain_id)

        res = self._request(
            "GET",
            f"/containers/v1beta1/regions/{param_region}/domains/{param_domain_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def wait_for_domain(
        self,
        *,
        domain_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Domain, bool]] = None,
    ) -> Domain:
        """
        Waits for :class:`Domain <Domain>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config.
        :param domain_id: UUID of the domain to get.
        :param options: The options for the waiter
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.wait_for_domain(domain_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in DOMAIN_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_domain,
            options=options,
            args={
                "domain_id": domain_id,
                "region": region,
            },
        )

    def create_domain(
        self,
        *,
        hostname: str,
        container_id: str,
        region: Optional[Region] = None,
    ) -> Domain:
        """
        Create a domain name binding.
        Create a domain name binding for the container with the specified ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param hostname: Domain to assign.
        :param container_id: UUID of the container to assign the domain to.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.create_domain(
                hostname="example",
                container_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/containers/v1beta1/regions/{param_region}/domains",
            body=marshal_CreateDomainRequest(
                CreateDomainRequest(
                    hostname=hostname,
                    container_id=container_id,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def delete_domain(
        self,
        *,
        domain_id: str,
        region: Optional[Region] = None,
    ) -> Domain:
        """
        Delete a domain name binding.
        Delete the domain name binding with the specific ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param domain_id: UUID of the domain to delete.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.delete_domain(domain_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_domain_id = validate_path_param("domain_id", domain_id)

        res = self._request(
            "DELETE",
            f"/containers/v1beta1/regions/{param_region}/domains/{param_domain_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def issue_jwt(
        self,
        *,
        region: Optional[Region] = None,
        container_id: Optional[str] = None,
        namespace_id: Optional[str] = None,
        expires_at: Optional[datetime] = None,
    ) -> Token:
        """
        :deprecated

        Usage:
        ::

            result = api.issue_jwt()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/containers/v1beta1/regions/{param_region}/issue-jwt",
            params={
                "expires_at": expires_at,
                **resolve_one_of(
                    [
                        OneOfPossibility("container_id", container_id),
                        OneOfPossibility("namespace_id", namespace_id),
                    ]
                ),
            },
        )

        self._throw_on_error(res)
        return unmarshal_Token(res.json())

    def create_token(
        self,
        *,
        region: Optional[Region] = None,
        container_id: Optional[str] = None,
        namespace_id: Optional[str] = None,
        description: Optional[str] = None,
        expires_at: Optional[datetime] = None,
    ) -> Token:
        """
        Create a new revocable token.
        :param region: Region to target. If none is passed will use default region from the config.
        :param container_id: UUID of the container to create the token for.

        One-of ('scope'): at most one of 'container_id', 'namespace_id' could be set.
        :param namespace_id: UUID of the namespace to create the token for.

        One-of ('scope'): at most one of 'container_id', 'namespace_id' could be set.
        :param description: Description of the token.
        :param expires_at: Expiry date of the token.
        :return: :class:`Token <Token>`

        Usage:
        ::

            result = api.create_token()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/containers/v1beta1/regions/{param_region}/tokens",
            body=marshal_CreateTokenRequest(
                CreateTokenRequest(
                    region=region,
                    container_id=container_id,
                    namespace_id=namespace_id,
                    description=description,
                    expires_at=expires_at,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Token(res.json())

    def get_token(
        self,
        *,
        token_id: str,
        region: Optional[Region] = None,
    ) -> Token:
        """
        Get a token.
        Get a token with a specified ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param token_id: UUID of the token to get.
        :return: :class:`Token <Token>`

        Usage:
        ::

            result = api.get_token(token_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_token_id = validate_path_param("token_id", token_id)

        res = self._request(
            "GET",
            f"/containers/v1beta1/regions/{param_region}/tokens/{param_token_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Token(res.json())

    def wait_for_token(
        self,
        *,
        token_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Token, bool]] = None,
    ) -> Token:
        """
        Waits for :class:`Token <Token>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config.
        :param token_id: UUID of the token to get.
        :param options: The options for the waiter
        :return: :class:`Token <Token>`

        Usage:
        ::

            result = api.wait_for_token(token_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in TOKEN_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_token,
            options=options,
            args={
                "token_id": token_id,
                "region": region,
            },
        )

    def list_tokens(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListTokensRequestOrderBy = ListTokensRequestOrderBy.CREATED_AT_ASC,
        container_id: Optional[str] = None,
        namespace_id: Optional[str] = None,
    ) -> ListTokensResponse:
        """
        List all tokens.
        List all tokens belonging to a specified Organization or Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of tokens per page.
        :param order_by: Order of the tokens.
        :param container_id: UUID of the container the token belongs to.
        :param namespace_id: UUID of the namespace the token belongs to.
        :return: :class:`ListTokensResponse <ListTokensResponse>`

        Usage:
        ::

            result = api.list_tokens()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/containers/v1beta1/regions/{param_region}/tokens",
            params={
                "container_id": container_id,
                "namespace_id": namespace_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListTokensResponse(res.json())

    def list_tokens_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListTokensRequestOrderBy] = None,
        container_id: Optional[str] = None,
        namespace_id: Optional[str] = None,
    ) -> List[Token]:
        """
        List all tokens.
        List all tokens belonging to a specified Organization or Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of tokens per page.
        :param order_by: Order of the tokens.
        :param container_id: UUID of the container the token belongs to.
        :param namespace_id: UUID of the namespace the token belongs to.
        :return: :class:`List[ListTokensResponse] <List[ListTokensResponse]>`

        Usage:
        ::

            result = api.list_tokens_all()
        """

        return fetch_all_pages(
            type=ListTokensResponse,
            key="tokens",
            fetcher=self.list_tokens,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "container_id": container_id,
                "namespace_id": namespace_id,
            },
        )

    def delete_token(
        self,
        *,
        token_id: str,
        region: Optional[Region] = None,
    ) -> Token:
        """
        Delete a token.
        Delete a token with a specified ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param token_id: UUID of the token to delete.
        :return: :class:`Token <Token>`

        Usage:
        ::

            result = api.delete_token(token_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_token_id = validate_path_param("token_id", token_id)

        res = self._request(
            "DELETE",
            f"/containers/v1beta1/regions/{param_region}/tokens/{param_token_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Token(res.json())
