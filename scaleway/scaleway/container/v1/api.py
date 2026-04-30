# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region as ScwRegion,
    ServiceInfo,
    unmarshal_ServiceInfo,
)
from scaleway_core.utils import (
    WaitForOptions,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
)
from .types import (
    ContainerPrivacy,
    ContainerProtocol,
    ContainerSandbox,
    ListContainersRequestOrderBy,
    ListDomainsRequestOrderBy,
    ListNamespacesRequestOrderBy,
    ListTriggersRequestOrderBy,
    TriggerSourceType,
    Container,
    ContainerProbe,
    ContainerScalingOption,
    CreateContainerRequest,
    CreateDomainRequest,
    CreateNamespaceRequest,
    CreateTriggerRequest,
    CreateTriggerRequestCronConfig,
    CreateTriggerRequestDestinationConfig,
    CreateTriggerRequestNATSConfig,
    CreateTriggerRequestSQSConfig,
    Domain,
    ListContainersResponse,
    ListDomainsResponse,
    ListNamespacesResponse,
    ListTriggersResponse,
    Namespace,
    Trigger,
    UpdateContainerRequest,
    UpdateContainerRequestProbe,
    UpdateDomainRequest,
    UpdateNamespaceRequest,
    UpdateTriggerRequest,
    UpdateTriggerRequestCronConfig,
    UpdateTriggerRequestDestinationConfig,
    UpdateTriggerRequestNATSConfig,
    UpdateTriggerRequestSQSConfig,
)
from .content import (
    CONTAINER_TRANSIENT_STATUSES,
    DOMAIN_TRANSIENT_STATUSES,
    NAMESPACE_TRANSIENT_STATUSES,
    TRIGGER_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Container,
    unmarshal_Domain,
    unmarshal_Namespace,
    unmarshal_Trigger,
    unmarshal_ListContainersResponse,
    unmarshal_ListDomainsResponse,
    unmarshal_ListNamespacesResponse,
    unmarshal_ListTriggersResponse,
    marshal_CreateContainerRequest,
    marshal_CreateDomainRequest,
    marshal_CreateNamespaceRequest,
    marshal_CreateTriggerRequest,
    marshal_UpdateContainerRequest,
    marshal_UpdateDomainRequest,
    marshal_UpdateNamespaceRequest,
    marshal_UpdateTriggerRequest,
)


class ContainerV1API(API):
    """
    Easily run containers on the cloud with a single command.
    """

    def get_service_info(
        self,
        *,
        region: Optional[ScwRegion] = None,
    ) -> ServiceInfo:
        """
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ServiceInfo <ServiceInfo>`

        Usage:
        ::

            result = api.get_service_info()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/containers/v1/regions/{param_region}",
        )

        self._throw_on_error(res)
        return unmarshal_ServiceInfo(res.json())

    def create_namespace(
        self,
        *,
        name: str,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        description: Optional[str] = None,
        environment_variables: Optional[dict[str, str]] = None,
        secret_environment_variables: Optional[dict[str, str]] = None,
        tags: Optional[list[str]] = None,
    ) -> Namespace:
        """
        Create a new namespace.
        Namespace name must be unique inside a project.
        :param name: Namespace name.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Unique ID of the Project the namespace belongs to.
        :param description: Namespace description.
        :param environment_variables: Namespace environment variables.
        :param secret_environment_variables: Namespace secret environment variables.
        :param tags: A list of arbitrary tags associated with the namespace.
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = api.create_namespace(
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/containers/v1/regions/{param_region}/namespaces",
            body=marshal_CreateNamespaceRequest(
                CreateNamespaceRequest(
                    name=name,
                    region=region,
                    project_id=project_id,
                    description=description,
                    environment_variables=environment_variables,
                    secret_environment_variables=secret_environment_variables,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())

    def get_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Namespace:
        """
        Get the namespace associated with the specified ID.
        :param namespace_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = api.get_namespace(
                namespace_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_namespace_id = validate_path_param("namespace_id", namespace_id)

        res = self._request(
            "GET",
            f"/containers/v1/regions/{param_region}/namespaces/{param_namespace_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())

    def wait_for_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[WaitForOptions[Namespace, bool]] = None,
    ) -> Namespace:
        """
        Get the namespace associated with the specified ID.
        :param namespace_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = api.get_namespace(
                namespace_id="example",
            )
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

    def list_namespaces(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNamespacesRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ListNamespacesResponse:
        """
        List all namespaces the caller can access (read permission).
        By default, the namespaces listed are ordered by creation date in ascending order. This can be modified via the `order_by` field.

        Additional parameters can be set in the query to filter, such as `organization_id`, `project_id`, and `name`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param organization_id:
        :param project_id:
        :param name:
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
            f"/containers/v1/regions/{param_region}/namespaces",
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
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNamespacesRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> list[Namespace]:
        """
        List all namespaces the caller can access (read permission).
        By default, the namespaces listed are ordered by creation date in ascending order. This can be modified via the `order_by` field.

        Additional parameters can be set in the query to filter, such as `organization_id`, `project_id`, and `name`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param organization_id:
        :param project_id:
        :param name:
        :return: :class:`list[Namespace] <list[Namespace]>`

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
                "organization_id": organization_id,
                "project_id": project_id,
                "name": name,
            },
        )

    def update_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[ScwRegion] = None,
        description: Optional[str] = None,
        environment_variables: Optional[dict[str, str]] = None,
        secret_environment_variables: Optional[dict[str, str]] = None,
        tags: Optional[list[str]] = None,
    ) -> Namespace:
        """
        Update the namespace associated with the specified ID.
        Only fields present in the request are updated; others are left untouched.
        :param namespace_id: UUID of the namespace to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param description: Namespace description.
        :param environment_variables: Namespace environment variables.
        :param secret_environment_variables: Namespace secret environment variables.
        :param tags: A list of arbitrary tags associated with the namespace.
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = api.update_namespace(
                namespace_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_namespace_id = validate_path_param("namespace_id", namespace_id)

        res = self._request(
            "PATCH",
            f"/containers/v1/regions/{param_region}/namespaces/{param_namespace_id}",
            body=marshal_UpdateNamespaceRequest(
                UpdateNamespaceRequest(
                    namespace_id=namespace_id,
                    region=region,
                    description=description,
                    environment_variables=environment_variables,
                    secret_environment_variables=secret_environment_variables,
                    tags=tags,
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
        region: Optional[ScwRegion] = None,
    ) -> Namespace:
        """
        Delete the namespace associated with the specified ID.
        It also deletes in cascade any resource inside the namespace.

        This action **cannot** be undone.
        :param namespace_id: UUID of the namespace to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = api.delete_namespace(
                namespace_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_namespace_id = validate_path_param("namespace_id", namespace_id)

        res = self._request(
            "DELETE",
            f"/containers/v1/regions/{param_region}/namespaces/{param_namespace_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())

    def create_container(
        self,
        *,
        namespace_id: str,
        name: str,
        region: Optional[ScwRegion] = None,
        environment_variables: Optional[dict[str, str]] = None,
        secret_environment_variables: Optional[dict[str, str]] = None,
        min_scale: Optional[int] = None,
        max_scale: Optional[int] = None,
        memory_limit_bytes: Optional[int] = None,
        mvcpu_limit: Optional[int] = None,
        timeout: Optional[str] = None,
        privacy: Optional[ContainerPrivacy] = None,
        description: Optional[str] = None,
        image: str,
        protocol: Optional[ContainerProtocol] = None,
        port: Optional[int] = None,
        https_connections_only: Optional[bool] = None,
        sandbox: Optional[ContainerSandbox] = None,
        local_storage_limit_bytes: Optional[int] = None,
        scaling_option: Optional[ContainerScalingOption] = None,
        liveness_probe: Optional[ContainerProbe] = None,
        startup_probe: Optional[ContainerProbe] = None,
        tags: Optional[list[str]] = None,
        private_network_id: Optional[str] = None,
        command: Optional[list[str]] = None,
        args: Optional[list[str]] = None,
    ) -> Container:
        """
        Create a new container in a namespace.
        Name must be unique inside the given namespace.
        :param namespace_id: Unique ID of the namespace the container belongs to.
        :param name: Container name.
        :param region: Region to target. If none is passed will use default region from the config.
        :param environment_variables: Environment variables of the container.
        :param secret_environment_variables: Secret environment variables of the container.
        :param min_scale: Minimum number of instances to scale the container to.
        :param max_scale: Maximum number of instances to scale the container to.
        :param memory_limit_bytes: Memory limit of the container in bytes.
        :param mvcpu_limit: CPU limit of the container in mvCPU.
        :param timeout: Processing time limit for the container.
        :param privacy: Privacy policy of the container.
        :param description: Container description.
        :param image: Image reference (e.g. "rg.fr-par.scw.cloud/my-registry-namespace/image:tag").
        :param protocol: Protocol the container uses.
        :param port: Port the container listens on.
        :param https_connections_only: If true, it will allow only HTTPS connections to access your container to prevent it from being triggered by insecure connections (HTTP).
        :param sandbox: Execution environment of the container.
        :param local_storage_limit_bytes: Local storage limit of the container (in bytes).
        :param scaling_option: Parameter used to decide when to scale up or down.
        :param liveness_probe: If the liveness probe fails, the container will be restarted.
        It is performed periodically during the container's lifetime. The liveness probe is not executed until the startup probe (if defined) is successful.

        Possible check types:
        - http: Perform HTTP check on the container with the specified path.
        - tcp: Perform TCP check on the container.
        :param startup_probe: If the startup probe fails, the container will be restarted.
        This check is useful for applications that might take a long time to start. It is only performed when the container is starting.

        Possible check types:
        - http: Perform HTTP check on the container with the specified path.
        - tcp: Perform TCP check on the container.
        :param tags: Tags of the Serverless Container.
        :param private_network_id: When connected to a Private Network, the container can access other Scaleway resources in this Private Network.
        :param command: Command executed when the container starts. This overrides the default command defined in the container image. This is usually the main executable, or ENTRYPOINT script to run.
        :param args: Arguments passed to the command specified in the "command" field. These override the default arguments from the container image, and behave like command-line parameters.
        :return: :class:`Container <Container>`

        Usage:
        ::

            result = api.create_container(
                namespace_id="example",
                name="example",
                image="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/containers/v1/regions/{param_region}/containers",
            body=marshal_CreateContainerRequest(
                CreateContainerRequest(
                    namespace_id=namespace_id,
                    name=name,
                    region=region,
                    environment_variables=environment_variables,
                    secret_environment_variables=secret_environment_variables,
                    min_scale=min_scale,
                    max_scale=max_scale,
                    memory_limit_bytes=memory_limit_bytes,
                    mvcpu_limit=mvcpu_limit,
                    timeout=timeout,
                    privacy=privacy,
                    description=description,
                    image=image,
                    protocol=protocol,
                    port=port,
                    https_connections_only=https_connections_only,
                    sandbox=sandbox,
                    local_storage_limit_bytes=local_storage_limit_bytes,
                    scaling_option=scaling_option,
                    liveness_probe=liveness_probe,
                    startup_probe=startup_probe,
                    tags=tags,
                    private_network_id=private_network_id,
                    command=command,
                    args=args,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Container(res.json())

    def get_container(
        self,
        *,
        container_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Container:
        """
        Get the container associated with the specified ID.
        :param container_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Container <Container>`

        Usage:
        ::

            result = api.get_container(
                container_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_container_id = validate_path_param("container_id", container_id)

        res = self._request(
            "GET",
            f"/containers/v1/regions/{param_region}/containers/{param_container_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Container(res.json())

    def wait_for_container(
        self,
        *,
        container_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[WaitForOptions[Container, bool]] = None,
    ) -> Container:
        """
        Get the container associated with the specified ID.
        :param container_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Container <Container>`

        Usage:
        ::

            result = api.get_container(
                container_id="example",
            )
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

    def list_containers(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListContainersRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        namespace_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ListContainersResponse:
        """
        List all containers the caller can access (read permission).
        By default, the containers listed are ordered by creation date in ascending order. This can be modified via the `order_by` field.

        Additional parameters can be set in the query to filter, such as `organization_id`, `project_id`, and `name`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param organization_id:
        :param project_id:
        :param namespace_id:
        :param name:
        :return: :class:`ListContainersResponse <ListContainersResponse>`

        Usage:
        ::

            result = api.list_containers()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/containers/v1/regions/{param_region}/containers",
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
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListContainersRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        namespace_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> list[Container]:
        """
        List all containers the caller can access (read permission).
        By default, the containers listed are ordered by creation date in ascending order. This can be modified via the `order_by` field.

        Additional parameters can be set in the query to filter, such as `organization_id`, `project_id`, and `name`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param organization_id:
        :param project_id:
        :param namespace_id:
        :param name:
        :return: :class:`list[Container] <list[Container]>`

        Usage:
        ::

            result = api.list_containers_all()
        """

        return fetch_all_pages(
            type=ListContainersResponse,
            key="containers",
            fetcher=self.list_containers,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "organization_id": organization_id,
                "project_id": project_id,
                "namespace_id": namespace_id,
                "name": name,
            },
        )

    def update_container(
        self,
        *,
        container_id: str,
        region: Optional[ScwRegion] = None,
        environment_variables: Optional[dict[str, str]] = None,
        secret_environment_variables: Optional[dict[str, str]] = None,
        min_scale: Optional[int] = None,
        max_scale: Optional[int] = None,
        memory_limit_bytes: Optional[int] = None,
        mvcpu_limit: Optional[int] = None,
        timeout: Optional[str] = None,
        privacy: Optional[ContainerPrivacy] = None,
        description: Optional[str] = None,
        image: Optional[str] = None,
        protocol: Optional[ContainerProtocol] = None,
        port: Optional[int] = None,
        https_connection_only: Optional[bool] = None,
        sandbox: Optional[ContainerSandbox] = None,
        local_storage_limit_bytes: Optional[int] = None,
        scaling_option: Optional[ContainerScalingOption] = None,
        liveness_probe: Optional[ContainerProbe] = None,
        startup_probe: Optional[UpdateContainerRequestProbe] = None,
        tags: Optional[list[str]] = None,
        private_network_id: Optional[str] = None,
        command: Optional[list[str]] = None,
        args: Optional[list[str]] = None,
    ) -> Container:
        """
        Update the container associated with the specified ID.
        Only fields present in the request are updated; others are left untouched.
        :param container_id: UUID of the container to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param environment_variables: Environment variables of the container.
        :param secret_environment_variables: Secret environment variables of the container.
        :param min_scale: Minimum number of instances to scale the container to.
        :param max_scale: Maximum number of instances to scale the container to.
        :param memory_limit_bytes: Memory limit of the container in bytes.
        :param mvcpu_limit: CPU limit of the container in mvCPU.
        :param timeout: Processing time limit for the container.
        :param privacy: Privacy policy of the container.
        :param description: Container description.
        :param image: Image reference (e.g. "rg.fr-par.scw.cloud/my-registry-namespace/image:tag").
        :param protocol: Protocol the container uses.
        :param port: Port the container listens on.
        :param https_connection_only: If true, it will allow only HTTPS connections to access your container to prevent it from being triggered by insecure connections (HTTP).
        :param sandbox: Execution environment of the container.
        :param local_storage_limit_bytes: Local storage limit of the container (in bytes).
        :param scaling_option: Parameter used to decide when to scale up or down.
        :param liveness_probe: If the liveness probe fails, the container will be restarted.
        It is performed periodically during the container's lifetime. The liveness probe is not executed until the startup probe (if defined) is successful.

        Possible check types:
        - http: Perform HTTP check on the container with the specified path.
        - tcp: Perform TCP check on the container.
        :param startup_probe: If the startup probe fails, the container will be restarted.
        This check is useful for applications that might take a long time to start. It is only performed when the container is starting.

        Possible check types:
        - http: Perform HTTP check on the container with the specified path.
        - tcp: Perform TCP check on the container.
        :param tags: Tags of the Serverless Container.
        :param private_network_id: When connected to a Private Network, the container can access other Scaleway resources in this Private Network.
        :param command: Command executed when the container starts. This overrides the default command defined in the container image. This is usually the main executable, or ENTRYPOINT script to run.
        :param args: Arguments passed to the command specified in the "command" field. These override the default arguments from the container image, and behave like command-line parameters.
        :return: :class:`Container <Container>`

        Usage:
        ::

            result = api.update_container(
                container_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_container_id = validate_path_param("container_id", container_id)

        res = self._request(
            "PATCH",
            f"/containers/v1/regions/{param_region}/containers/{param_container_id}",
            body=marshal_UpdateContainerRequest(
                UpdateContainerRequest(
                    container_id=container_id,
                    region=region,
                    environment_variables=environment_variables,
                    secret_environment_variables=secret_environment_variables,
                    min_scale=min_scale,
                    max_scale=max_scale,
                    memory_limit_bytes=memory_limit_bytes,
                    mvcpu_limit=mvcpu_limit,
                    timeout=timeout,
                    privacy=privacy,
                    description=description,
                    image=image,
                    protocol=protocol,
                    port=port,
                    https_connection_only=https_connection_only,
                    sandbox=sandbox,
                    local_storage_limit_bytes=local_storage_limit_bytes,
                    scaling_option=scaling_option,
                    liveness_probe=liveness_probe,
                    startup_probe=startup_probe,
                    tags=tags,
                    private_network_id=private_network_id,
                    command=command,
                    args=args,
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
        region: Optional[ScwRegion] = None,
    ) -> Container:
        """
        Delete the container associated with the specified ID.
        It also deletes in cascade any resource linked to the container (crons, tokens, etc.).

        This action **cannot** be undone.
        :param container_id: UUID of the container to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Container <Container>`

        Usage:
        ::

            result = api.delete_container(
                container_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_container_id = validate_path_param("container_id", container_id)

        res = self._request(
            "DELETE",
            f"/containers/v1/regions/{param_region}/containers/{param_container_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Container(res.json())

    def create_domain(
        self,
        *,
        container_id: str,
        hostname: str,
        region: Optional[ScwRegion] = None,
        tags: Optional[list[str]] = None,
    ) -> Domain:
        """
        Create a new custom domain for the container with the specified ID.
        :param container_id: Unique ID of the container the domain will be assigned to.
        :param hostname: Domain assigned to the container.
        :param region: Region to target. If none is passed will use default region from the config.
        :param tags: A list of arbitrary tags associated with the domain.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.create_domain(
                container_id="example",
                hostname="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/containers/v1/regions/{param_region}/domains",
            body=marshal_CreateDomainRequest(
                CreateDomainRequest(
                    container_id=container_id,
                    hostname=hostname,
                    region=region,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def get_domain(
        self,
        *,
        domain_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Domain:
        """
        Get the custom domain associated with the specified ID.
        :param domain_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.get_domain(
                domain_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_domain_id = validate_path_param("domain_id", domain_id)

        res = self._request(
            "GET",
            f"/containers/v1/regions/{param_region}/domains/{param_domain_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def wait_for_domain(
        self,
        *,
        domain_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[WaitForOptions[Domain, bool]] = None,
    ) -> Domain:
        """
        Get the custom domain associated with the specified ID.
        :param domain_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.get_domain(
                domain_id="example",
            )
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

    def list_domains(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDomainsRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        namespace_id: Optional[str] = None,
        container_id: Optional[str] = None,
    ) -> ListDomainsResponse:
        """
        List all custom domains the caller can access (read permission).
        By default, the custom domains listed are ordered by creation date in ascending order. This can be modified via the `order_by` field.

        Additional parameters can be set in the query to filter the output, such as `organization_id`, `project_id`, `namespace_id`, or `container_id`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param organization_id:
        :param project_id:
        :param namespace_id:
        :param container_id:
        :return: :class:`ListDomainsResponse <ListDomainsResponse>`

        Usage:
        ::

            result = api.list_domains()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/containers/v1/regions/{param_region}/domains",
            params={
                "container_id": container_id,
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
        return unmarshal_ListDomainsResponse(res.json())

    def list_domains_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDomainsRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        namespace_id: Optional[str] = None,
        container_id: Optional[str] = None,
    ) -> list[Domain]:
        """
        List all custom domains the caller can access (read permission).
        By default, the custom domains listed are ordered by creation date in ascending order. This can be modified via the `order_by` field.

        Additional parameters can be set in the query to filter the output, such as `organization_id`, `project_id`, `namespace_id`, or `container_id`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param organization_id:
        :param project_id:
        :param namespace_id:
        :param container_id:
        :return: :class:`list[Domain] <list[Domain]>`

        Usage:
        ::

            result = api.list_domains_all()
        """

        return fetch_all_pages(
            type=ListDomainsResponse,
            key="domains",
            fetcher=self.list_domains,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "organization_id": organization_id,
                "project_id": project_id,
                "namespace_id": namespace_id,
                "container_id": container_id,
            },
        )

    def update_domain(
        self,
        *,
        domain_id: str,
        region: Optional[ScwRegion] = None,
        tags: Optional[list[str]] = None,
    ) -> Domain:
        """
        Update the domain associated with the specified ID.
        Only fields present in the request are updated; others are left untouched.
        :param domain_id: UUID of the domain to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param tags: A list of arbitrary tags associated with the domain.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.update_domain(
                domain_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_domain_id = validate_path_param("domain_id", domain_id)

        res = self._request(
            "PATCH",
            f"/containers/v1/regions/{param_region}/domains/{param_domain_id}",
            body=marshal_UpdateDomainRequest(
                UpdateDomainRequest(
                    domain_id=domain_id,
                    region=region,
                    tags=tags,
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
        region: Optional[ScwRegion] = None,
    ) -> Domain:
        """
        Delete the custom domain associated with the specified ID.
        :param domain_id: UUID of the domain to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.delete_domain(
                domain_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_domain_id = validate_path_param("domain_id", domain_id)

        res = self._request(
            "DELETE",
            f"/containers/v1/regions/{param_region}/domains/{param_domain_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def redeploy_container(
        self,
        *,
        container_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Container:
        """
        Redeploy a container.
        Performs a rollout of the container by creating new instances with the latest image version and terminating the old instances.
        When using mutable registry image references (e.g. `my-registry-namespace/image:tag`), this endpoint can be used to force the container to use
        the most recent image version available in the registry.
        :param container_id: ID of the container to redeploy.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Container <Container>`

        Usage:
        ::

            result = api.redeploy_container(
                container_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_container_id = validate_path_param("container_id", container_id)

        res = self._request(
            "POST",
            f"/containers/v1/regions/{param_region}/containers/{param_container_id}/redeploy",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Container(res.json())

    def create_trigger(
        self,
        *,
        container_id: str,
        name: str,
        region: Optional[ScwRegion] = None,
        description: Optional[str] = None,
        tags: Optional[list[str]] = None,
        destination_config: Optional[CreateTriggerRequestDestinationConfig] = None,
        cron_config: Optional[CreateTriggerRequestCronConfig] = None,
        sqs_config: Optional[CreateTriggerRequestSQSConfig] = None,
        nats_config: Optional[CreateTriggerRequestNATSConfig] = None,
    ) -> Trigger:
        """
        Create a new trigger for the container with the specified ID.
        :param container_id: ID of the container to trigger.
        :param name: Name of the trigger.
        :param region: Region to target. If none is passed will use default region from the config.
        :param description: Description of the trigger.
        :param tags: Tags of the trigger.
        :param destination_config: Configuration of the destination to trigger.
        :param cron_config: Configuration for a cron source.
        One-Of ('source_config'): at most one of 'cron_config', 'sqs_config', 'nats_config' could be set.
        :param sqs_config: Configuration for an SQS queue source.
        One-Of ('source_config'): at most one of 'cron_config', 'sqs_config', 'nats_config' could be set.
        :param nats_config: Configuration for a NATS source.
        One-Of ('source_config'): at most one of 'cron_config', 'sqs_config', 'nats_config' could be set.
        :return: :class:`Trigger <Trigger>`

        Usage:
        ::

            result = api.create_trigger(
                container_id="example",
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/containers/v1/regions/{param_region}/triggers",
            body=marshal_CreateTriggerRequest(
                CreateTriggerRequest(
                    container_id=container_id,
                    name=name,
                    region=region,
                    description=description,
                    tags=tags,
                    destination_config=destination_config,
                    cron_config=cron_config,
                    sqs_config=sqs_config,
                    nats_config=nats_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Trigger(res.json())

    def get_trigger(
        self,
        *,
        trigger_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Trigger:
        """
        Get the trigger associated with the specified ID.
        :param trigger_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Trigger <Trigger>`

        Usage:
        ::

            result = api.get_trigger(
                trigger_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_trigger_id = validate_path_param("trigger_id", trigger_id)

        res = self._request(
            "GET",
            f"/containers/v1/regions/{param_region}/triggers/{param_trigger_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Trigger(res.json())

    def wait_for_trigger(
        self,
        *,
        trigger_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[WaitForOptions[Trigger, bool]] = None,
    ) -> Trigger:
        """
        Get the trigger associated with the specified ID.
        :param trigger_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Trigger <Trigger>`

        Usage:
        ::

            result = api.get_trigger(
                trigger_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in TRIGGER_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_trigger,
            options=options,
            args={
                "trigger_id": trigger_id,
                "region": region,
            },
        )

    def list_triggers(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListTriggersRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        namespace_id: Optional[str] = None,
        container_id: Optional[str] = None,
        trigger_type: Optional[TriggerSourceType] = None,
    ) -> ListTriggersResponse:
        """
        List all triggers the caller can access (read permission).
        By default, the triggers listed are ordered by creation date in ascending order. This can be modified via the `order_by` field.

        Additional parameters can be set in the query to filter, such as `organization_id`, `project_id`, `namespace_id`, `container_id` or `trigger_type`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param organization_id:
        :param project_id:
        :param namespace_id:
        :param container_id:
        :param trigger_type:
        :return: :class:`ListTriggersResponse <ListTriggersResponse>`

        Usage:
        ::

            result = api.list_triggers()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/containers/v1/regions/{param_region}/triggers",
            params={
                "container_id": container_id,
                "namespace_id": namespace_id,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "trigger_type": trigger_type,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListTriggersResponse(res.json())

    def list_triggers_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListTriggersRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        namespace_id: Optional[str] = None,
        container_id: Optional[str] = None,
        trigger_type: Optional[TriggerSourceType] = None,
    ) -> list[Trigger]:
        """
        List all triggers the caller can access (read permission).
        By default, the triggers listed are ordered by creation date in ascending order. This can be modified via the `order_by` field.

        Additional parameters can be set in the query to filter, such as `organization_id`, `project_id`, `namespace_id`, `container_id` or `trigger_type`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param organization_id:
        :param project_id:
        :param namespace_id:
        :param container_id:
        :param trigger_type:
        :return: :class:`list[Trigger] <list[Trigger]>`

        Usage:
        ::

            result = api.list_triggers_all()
        """

        return fetch_all_pages(
            type=ListTriggersResponse,
            key="triggers",
            fetcher=self.list_triggers,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "organization_id": organization_id,
                "project_id": project_id,
                "namespace_id": namespace_id,
                "container_id": container_id,
                "trigger_type": trigger_type,
            },
        )

    def update_trigger(
        self,
        *,
        trigger_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[list[str]] = None,
        destination_config: Optional[UpdateTriggerRequestDestinationConfig] = None,
        cron_config: Optional[UpdateTriggerRequestCronConfig] = None,
        sqs_config: Optional[UpdateTriggerRequestSQSConfig] = None,
        nats_config: Optional[UpdateTriggerRequestNATSConfig] = None,
    ) -> Trigger:
        """
        Update the trigger associated with the specified ID.
        When updating a trigger, you cannot specify a different source type than the one already set.
        Only fields present in the request are updated; others are left untouched.
        :param trigger_id: ID of the trigger to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the trigger.
        :param description: Description of the trigger.
        :param tags: Tags of the trigger.
        :param destination_config: Configuration of the destination to trigger.
        :param cron_config: Configuration for a cron source.
        One-Of ('source_config'): at most one of 'cron_config', 'sqs_config', 'nats_config' could be set.
        :param sqs_config: Configuration for an SQS queue source.
        One-Of ('source_config'): at most one of 'cron_config', 'sqs_config', 'nats_config' could be set.
        :param nats_config: Configuration for a NATS source.
        One-Of ('source_config'): at most one of 'cron_config', 'sqs_config', 'nats_config' could be set.
        :return: :class:`Trigger <Trigger>`

        Usage:
        ::

            result = api.update_trigger(
                trigger_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_trigger_id = validate_path_param("trigger_id", trigger_id)

        res = self._request(
            "PATCH",
            f"/containers/v1/regions/{param_region}/triggers/{param_trigger_id}",
            body=marshal_UpdateTriggerRequest(
                UpdateTriggerRequest(
                    trigger_id=trigger_id,
                    region=region,
                    name=name,
                    description=description,
                    tags=tags,
                    destination_config=destination_config,
                    cron_config=cron_config,
                    sqs_config=sqs_config,
                    nats_config=nats_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Trigger(res.json())

    def delete_trigger(
        self,
        *,
        trigger_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Trigger:
        """
        Delete the trigger associated with the specified ID.
        This action **cannot** be undone.
        :param trigger_id: ID of the trigger to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Trigger <Trigger>`

        Usage:
        ::

            result = api.delete_trigger(
                trigger_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_trigger_id = validate_path_param("trigger_id", trigger_id)

        res = self._request(
            "DELETE",
            f"/containers/v1/regions/{param_region}/triggers/{param_trigger_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Trigger(res.json())
