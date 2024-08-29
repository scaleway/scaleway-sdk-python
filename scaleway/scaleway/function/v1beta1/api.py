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
    random_name,
    resolve_one_of,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
)
from .types import (
    FunctionHttpOption,
    FunctionPrivacy,
    FunctionRuntime,
    FunctionSandbox,
    ListCronsRequestOrderBy,
    ListDomainsRequestOrderBy,
    ListFunctionsRequestOrderBy,
    ListNamespacesRequestOrderBy,
    ListTokensRequestOrderBy,
    ListTriggersRequestOrderBy,
    CreateCronRequest,
    CreateDomainRequest,
    CreateFunctionRequest,
    CreateNamespaceRequest,
    CreateTokenRequest,
    CreateTriggerRequest,
    CreateTriggerRequestMnqNatsClientConfig,
    CreateTriggerRequestMnqSqsClientConfig,
    CreateTriggerRequestSqsClientConfig,
    Cron,
    Domain,
    DownloadURL,
    Function,
    ListCronsResponse,
    ListDomainsResponse,
    ListFunctionRuntimesResponse,
    ListFunctionsResponse,
    ListNamespacesResponse,
    ListTokensResponse,
    ListTriggersResponse,
    Namespace,
    Secret,
    Token,
    Trigger,
    UpdateCronRequest,
    UpdateFunctionRequest,
    UpdateNamespaceRequest,
    UpdateTriggerRequest,
    UpdateTriggerRequestSqsClientConfig,
    UploadURL,
)
from .content import (
    CRON_TRANSIENT_STATUSES,
    DOMAIN_TRANSIENT_STATUSES,
    FUNCTION_TRANSIENT_STATUSES,
    NAMESPACE_TRANSIENT_STATUSES,
    TOKEN_TRANSIENT_STATUSES,
    TRIGGER_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Cron,
    unmarshal_Domain,
    unmarshal_Function,
    unmarshal_Namespace,
    unmarshal_Token,
    unmarshal_Trigger,
    unmarshal_DownloadURL,
    unmarshal_ListCronsResponse,
    unmarshal_ListDomainsResponse,
    unmarshal_ListFunctionRuntimesResponse,
    unmarshal_ListFunctionsResponse,
    unmarshal_ListNamespacesResponse,
    unmarshal_ListTokensResponse,
    unmarshal_ListTriggersResponse,
    unmarshal_UploadURL,
    marshal_CreateCronRequest,
    marshal_CreateDomainRequest,
    marshal_CreateFunctionRequest,
    marshal_CreateNamespaceRequest,
    marshal_CreateTokenRequest,
    marshal_CreateTriggerRequest,
    marshal_UpdateCronRequest,
    marshal_UpdateFunctionRequest,
    marshal_UpdateNamespaceRequest,
    marshal_UpdateTriggerRequest,
)


class FunctionV1Beta1API(API):
    """
    This API allows you to manage your Serverless Functions.
    """

    def list_namespaces(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNamespacesRequestOrderBy] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListNamespacesResponse:
        """
        List all your namespaces.
        List all existing namespaces in the specified region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of namespaces per page.
        :param order_by: Order of the namespaces.
        :param name: Name of the namespace.
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
            f"/functions/v1beta1/regions/{param_region}/namespaces",
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
        List all existing namespaces in the specified region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of namespaces per page.
        :param order_by: Order of the namespaces.
        :param name: Name of the namespace.
        :param organization_id: UUID of the Organization the namespace belongs to.
        :param project_id: UUID of the Project the namespace belongs to.
        :return: :class:`List[Namespace] <List[Namespace]>`

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
        :param namespace_id: UUID of the namespace.
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
            f"/functions/v1beta1/regions/{param_region}/namespaces/{param_namespace_id}",
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
        Get a namespace.
        Get the namespace associated with the specified ID.
        :param namespace_id: UUID of the namespace.
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
        Create a new namespace in a specified Organization or Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name:
        :param environment_variables: Environment variables of the namespace.
        :param project_id: UUID of the project in which the namespace will be created.
        :param description: Description of the namespace.
        :param secret_environment_variables: Secret environment variables of the namespace.
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
            f"/functions/v1beta1/regions/{param_region}/namespaces",
            body=marshal_CreateNamespaceRequest(
                CreateNamespaceRequest(
                    region=region,
                    name=name or random_name(prefix="ns"),
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
        Update the namespace associated with the specified ID.
        :param namespace_id: UUID of the namespapce.
        :param region: Region to target. If none is passed will use default region from the config.
        :param environment_variables: Environment variables of the namespace.
        :param description: Description of the namespace.
        :param secret_environment_variables: Secret environment variables of the namespace.
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
            f"/functions/v1beta1/regions/{param_region}/namespaces/{param_namespace_id}",
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
        :param namespace_id: UUID of the namespace.
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
            f"/functions/v1beta1/regions/{param_region}/namespaces/{param_namespace_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())

    def list_functions(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListFunctionsRequestOrderBy] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListFunctionsResponse:
        """
        List all your functions.
        :param namespace_id: UUID of the namespace the function belongs to.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of functions per page.
        :param order_by: Order of the functions.
        :param name: Name of the function.
        :param organization_id: UUID of the Organziation the function belongs to.
        :param project_id: UUID of the Project the function belongs to.
        :return: :class:`ListFunctionsResponse <ListFunctionsResponse>`

        Usage:
        ::

            result = api.list_functions(
                namespace_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/functions/v1beta1/regions/{param_region}/functions",
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
        return unmarshal_ListFunctionsResponse(res.json())

    def list_functions_all(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListFunctionsRequestOrderBy] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Function]:
        """
        List all your functions.
        :param namespace_id: UUID of the namespace the function belongs to.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of functions per page.
        :param order_by: Order of the functions.
        :param name: Name of the function.
        :param organization_id: UUID of the Organziation the function belongs to.
        :param project_id: UUID of the Project the function belongs to.
        :return: :class:`List[Function] <List[Function]>`

        Usage:
        ::

            result = api.list_functions_all(
                namespace_id="example",
            )
        """

        return fetch_all_pages(
            type=ListFunctionsResponse,
            key="functions",
            fetcher=self.list_functions,
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

    def get_function(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
    ) -> Function:
        """
        Get a function.
        Get the function associated with the specified ID.
        :param function_id: UUID of the function.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Function <Function>`

        Usage:
        ::

            result = api.get_function(
                function_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_function_id = validate_path_param("function_id", function_id)

        res = self._request(
            "GET",
            f"/functions/v1beta1/regions/{param_region}/functions/{param_function_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Function(res.json())

    def wait_for_function(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Function, bool]] = None,
    ) -> Function:
        """
        Get a function.
        Get the function associated with the specified ID.
        :param function_id: UUID of the function.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Function <Function>`

        Usage:
        ::

            result = api.get_function(
                function_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in FUNCTION_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_function,
            options=options,
            args={
                "function_id": function_id,
                "region": region,
            },
        )

    def create_function(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        environment_variables: Optional[Dict[str, str]] = None,
        min_scale: Optional[int] = None,
        max_scale: Optional[int] = None,
        runtime: Optional[FunctionRuntime] = None,
        memory_limit: Optional[int] = None,
        timeout: Optional[str] = None,
        handler: Optional[str] = None,
        privacy: Optional[FunctionPrivacy] = None,
        description: Optional[str] = None,
        secret_environment_variables: Optional[List[Secret]] = None,
        http_option: Optional[FunctionHttpOption] = None,
        sandbox: Optional[FunctionSandbox] = None,
    ) -> Function:
        """
        Create a new function.
        Create a new function in the specified region for a specified Organization or Project.
        :param namespace_id: UUID of the namespace the function will be created in.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the function to create.
        :param environment_variables: Environment variables of the function.
        :param min_scale: Minumum number of instances to scale the function to.
        :param max_scale: Maximum number of instances to scale the function to.
        :param runtime: Runtime to use with the function.
        :param memory_limit: Memory limit of the function in MB.
        :param timeout: Request processing time limit for the function.
        :param handler: Handler to use with the function.
        :param privacy: Privacy setting of the function.
        :param description: Description of the function.
        :param secret_environment_variables:
        :param http_option: Possible values:
         - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
         - enabled: Serve both HTTP and HTTPS traffic.
        :param sandbox: Execution environment of the function.
        :return: :class:`Function <Function>`

        Usage:
        ::

            result = api.create_function(
                namespace_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/functions/v1beta1/regions/{param_region}/functions",
            body=marshal_CreateFunctionRequest(
                CreateFunctionRequest(
                    namespace_id=namespace_id,
                    region=region,
                    name=name or random_name(prefix="fn"),
                    environment_variables=environment_variables,
                    min_scale=min_scale,
                    max_scale=max_scale,
                    runtime=runtime,
                    memory_limit=memory_limit,
                    timeout=timeout,
                    handler=handler,
                    privacy=privacy,
                    description=description,
                    secret_environment_variables=secret_environment_variables,
                    http_option=http_option,
                    sandbox=sandbox,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Function(res.json())

    def update_function(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
        environment_variables: Optional[Dict[str, str]] = None,
        min_scale: Optional[int] = None,
        max_scale: Optional[int] = None,
        runtime: Optional[FunctionRuntime] = None,
        memory_limit: Optional[int] = None,
        timeout: Optional[str] = None,
        redeploy: Optional[bool] = None,
        handler: Optional[str] = None,
        privacy: Optional[FunctionPrivacy] = None,
        description: Optional[str] = None,
        secret_environment_variables: Optional[List[Secret]] = None,
        http_option: Optional[FunctionHttpOption] = None,
        sandbox: Optional[FunctionSandbox] = None,
    ) -> Function:
        """
        Update an existing function.
        Update the function associated with the specified ID.
        :param function_id: UUID of the function to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param environment_variables: Environment variables of the function to update.
        :param min_scale: Minumum number of instances to scale the function to.
        :param max_scale: Maximum number of instances to scale the function to.
        :param runtime: Runtime to use with the function.
        :param memory_limit: Memory limit of the function in MB.
        :param timeout: Processing time limit for the function.
        :param redeploy: Redeploy failed function.
        :param handler: Handler to use with the function.
        :param privacy: Privacy setting of the function.
        :param description: Description of the function.
        :param secret_environment_variables: Secret environment variables of the function.
        :param http_option: Possible values:
         - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
         - enabled: Serve both HTTP and HTTPS traffic.
        :param sandbox: Execution environment of the function.
        :return: :class:`Function <Function>`

        Usage:
        ::

            result = api.update_function(
                function_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_function_id = validate_path_param("function_id", function_id)

        res = self._request(
            "PATCH",
            f"/functions/v1beta1/regions/{param_region}/functions/{param_function_id}",
            body=marshal_UpdateFunctionRequest(
                UpdateFunctionRequest(
                    function_id=function_id,
                    region=region,
                    environment_variables=environment_variables,
                    min_scale=min_scale,
                    max_scale=max_scale,
                    runtime=runtime,
                    memory_limit=memory_limit,
                    timeout=timeout,
                    redeploy=redeploy,
                    handler=handler,
                    privacy=privacy,
                    description=description,
                    secret_environment_variables=secret_environment_variables,
                    http_option=http_option,
                    sandbox=sandbox,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Function(res.json())

    def delete_function(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
    ) -> Function:
        """
        Delete a function.
        Delete the function associated with the specified ID.
        :param function_id: UUID of the function to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Function <Function>`

        Usage:
        ::

            result = api.delete_function(
                function_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_function_id = validate_path_param("function_id", function_id)

        res = self._request(
            "DELETE",
            f"/functions/v1beta1/regions/{param_region}/functions/{param_function_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Function(res.json())

    def deploy_function(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
    ) -> Function:
        """
        Deploy a function.
        Deploy a function associated with the specified ID.
        :param function_id: UUID of the function to deploy.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Function <Function>`

        Usage:
        ::

            result = api.deploy_function(
                function_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_function_id = validate_path_param("function_id", function_id)

        res = self._request(
            "POST",
            f"/functions/v1beta1/regions/{param_region}/functions/{param_function_id}/deploy",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Function(res.json())

    def list_function_runtimes(
        self,
        *,
        region: Optional[Region] = None,
    ) -> ListFunctionRuntimesResponse:
        """
        List function runtimes.
        List available function runtimes.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ListFunctionRuntimesResponse <ListFunctionRuntimesResponse>`

        Usage:
        ::

            result = api.list_function_runtimes()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/functions/v1beta1/regions/{param_region}/runtimes",
        )

        self._throw_on_error(res)
        return unmarshal_ListFunctionRuntimesResponse(res.json())

    def get_function_upload_url(
        self,
        *,
        function_id: str,
        content_length: int,
        region: Optional[Region] = None,
    ) -> UploadURL:
        """
        Get an upload URL of a function.
        Get an upload URL of a function associated with the specified ID.
        :param function_id: UUID of the function to get the upload URL for.
        :param content_length: Size of the archive to upload in bytes.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`UploadURL <UploadURL>`

        Usage:
        ::

            result = api.get_function_upload_url(
                function_id="example",
                content_length=1,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_function_id = validate_path_param("function_id", function_id)

        res = self._request(
            "GET",
            f"/functions/v1beta1/regions/{param_region}/functions/{param_function_id}/upload-url",
            params={
                "content_length": content_length,
            },
        )

        self._throw_on_error(res)
        return unmarshal_UploadURL(res.json())

    def get_function_download_url(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
    ) -> DownloadURL:
        """
        Get a download URL of a function.
        Get a download URL for a function associated with the specified ID.
        :param function_id: UUID of the function to get the the download URL for.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DownloadURL <DownloadURL>`

        Usage:
        ::

            result = api.get_function_download_url(
                function_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_function_id = validate_path_param("function_id", function_id)

        res = self._request(
            "GET",
            f"/functions/v1beta1/regions/{param_region}/functions/{param_function_id}/download-url",
        )

        self._throw_on_error(res)
        return unmarshal_DownloadURL(res.json())

    def list_crons(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListCronsRequestOrderBy] = None,
    ) -> ListCronsResponse:
        """
        List all crons.
        List all the cronjobs in a specified region.
        :param function_id: UUID of the function.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of crons per page.
        :param order_by: Order of the crons.
        :return: :class:`ListCronsResponse <ListCronsResponse>`

        Usage:
        ::

            result = api.list_crons(
                function_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/functions/v1beta1/regions/{param_region}/crons",
            params={
                "function_id": function_id,
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
        function_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListCronsRequestOrderBy] = None,
    ) -> List[Cron]:
        """
        List all crons.
        List all the cronjobs in a specified region.
        :param function_id: UUID of the function.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of crons per page.
        :param order_by: Order of the crons.
        :return: :class:`List[Cron] <List[Cron]>`

        Usage:
        ::

            result = api.list_crons_all(
                function_id="example",
            )
        """

        return fetch_all_pages(
            type=ListCronsResponse,
            key="crons",
            fetcher=self.list_crons,
            args={
                "function_id": function_id,
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
        :param cron_id: UUID of the cron to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Cron <Cron>`

        Usage:
        ::

            result = api.get_cron(
                cron_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cron_id = validate_path_param("cron_id", cron_id)

        res = self._request(
            "GET",
            f"/functions/v1beta1/regions/{param_region}/crons/{param_cron_id}",
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
        Get a cron.
        Get the cron associated with the specified ID.
        :param cron_id: UUID of the cron to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Cron <Cron>`

        Usage:
        ::

            result = api.get_cron(
                cron_id="example",
            )
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
        function_id: str,
        schedule: str,
        region: Optional[Region] = None,
        args: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
    ) -> Cron:
        """
        Create a new cron.
        Create a new cronjob for a function with the specified ID.
        :param function_id: UUID of the function to use the cron with.
        :param schedule: Schedule of the cron in UNIX cron format.
        :param region: Region to target. If none is passed will use default region from the config.
        :param args: Arguments to use with the cron.
        :param name: Name of the cron.
        :return: :class:`Cron <Cron>`

        Usage:
        ::

            result = api.create_cron(
                function_id="example",
                schedule="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/functions/v1beta1/regions/{param_region}/crons",
            body=marshal_CreateCronRequest(
                CreateCronRequest(
                    function_id=function_id,
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
        function_id: Optional[str] = None,
        schedule: Optional[str] = None,
        args: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
    ) -> Cron:
        """
        Update an existing cron.
        Update the cron associated with the specified ID.
        :param cron_id: UUID of the cron to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param function_id: UUID of the function to use the cron with.
        :param schedule: Schedule of the cron in UNIX cron format.
        :param args: Arguments to use with the cron.
        :param name: Name of the cron.
        :return: :class:`Cron <Cron>`

        Usage:
        ::

            result = api.update_cron(
                cron_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cron_id = validate_path_param("cron_id", cron_id)

        res = self._request(
            "PATCH",
            f"/functions/v1beta1/regions/{param_region}/crons/{param_cron_id}",
            body=marshal_UpdateCronRequest(
                UpdateCronRequest(
                    cron_id=cron_id,
                    region=region,
                    function_id=function_id,
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
        :param cron_id: UUID of the cron to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Cron <Cron>`

        Usage:
        ::

            result = api.delete_cron(
                cron_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_cron_id = validate_path_param("cron_id", cron_id)

        res = self._request(
            "DELETE",
            f"/functions/v1beta1/regions/{param_region}/crons/{param_cron_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Cron(res.json())

    def list_domains(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDomainsRequestOrderBy] = None,
    ) -> ListDomainsResponse:
        """
        List all domain name bindings.
        List all domain name bindings in a specified region.
        :param function_id: UUID of the function the domain is assoicated with.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of domains per page.
        :param order_by: Order of the domains.
        :return: :class:`ListDomainsResponse <ListDomainsResponse>`

        Usage:
        ::

            result = api.list_domains(
                function_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/functions/v1beta1/regions/{param_region}/domains",
            params={
                "function_id": function_id,
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
        function_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDomainsRequestOrderBy] = None,
    ) -> List[Domain]:
        """
        List all domain name bindings.
        List all domain name bindings in a specified region.
        :param function_id: UUID of the function the domain is assoicated with.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of domains per page.
        :param order_by: Order of the domains.
        :return: :class:`List[Domain] <List[Domain]>`

        Usage:
        ::

            result = api.list_domains_all(
                function_id="example",
            )
        """

        return fetch_all_pages(
            type=ListDomainsResponse,
            key="domains",
            fetcher=self.list_domains,
            args={
                "function_id": function_id,
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
        Get a domain name binding for the function with the specified ID.
        :param domain_id: UUID of the domain to get.
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
            f"/functions/v1beta1/regions/{param_region}/domains/{param_domain_id}",
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
        Get a domain name binding.
        Get a domain name binding for the function with the specified ID.
        :param domain_id: UUID of the domain to get.
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

    def create_domain(
        self,
        *,
        hostname: str,
        function_id: str,
        region: Optional[Region] = None,
    ) -> Domain:
        """
        Create a domain name binding.
        Create a domain name binding for the function with the specified ID.
        :param hostname: Hostame to create.
        :param function_id: UUID of the function to associate the domain with.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.create_domain(
                hostname="example",
                function_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/functions/v1beta1/regions/{param_region}/domains",
            body=marshal_CreateDomainRequest(
                CreateDomainRequest(
                    hostname=hostname,
                    function_id=function_id,
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
        Delete a domain name binding for the function with the specified ID.
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
            f"/functions/v1beta1/regions/{param_region}/domains/{param_domain_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def create_token(
        self,
        *,
        region: Optional[Region] = None,
        function_id: Optional[str] = None,
        namespace_id: Optional[str] = None,
        description: Optional[str] = None,
        expires_at: Optional[datetime] = None,
    ) -> Token:
        """
        Create a new revocable token.
        :param region: Region to target. If none is passed will use default region from the config.
        :param function_id: UUID of the function to associate the token with.
        One-Of ('scope'): at most one of 'function_id', 'namespace_id' could be set.
        :param namespace_id: UUID of the namespace to associate the token with.
        One-Of ('scope'): at most one of 'function_id', 'namespace_id' could be set.
        :param description: Description of the token.
        :param expires_at: Date on which the token expires.
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
            f"/functions/v1beta1/regions/{param_region}/tokens",
            body=marshal_CreateTokenRequest(
                CreateTokenRequest(
                    region=region,
                    description=description,
                    expires_at=expires_at,
                    function_id=function_id,
                    namespace_id=namespace_id,
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
        :param token_id: UUID of the token to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Token <Token>`

        Usage:
        ::

            result = api.get_token(
                token_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_token_id = validate_path_param("token_id", token_id)

        res = self._request(
            "GET",
            f"/functions/v1beta1/regions/{param_region}/tokens/{param_token_id}",
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
        Get a token.
        :param token_id: UUID of the token to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Token <Token>`

        Usage:
        ::

            result = api.get_token(
                token_id="example",
            )
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
        order_by: Optional[ListTokensRequestOrderBy] = None,
        function_id: Optional[str] = None,
        namespace_id: Optional[str] = None,
    ) -> ListTokensResponse:
        """
        List all tokens.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of tokens per page.
        :param order_by: Sort order for the tokens.
        :param function_id: UUID of the function the token is assoicated with.
        :param namespace_id: UUID of the namespace the token is associated with.
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
            f"/functions/v1beta1/regions/{param_region}/tokens",
            params={
                "function_id": function_id,
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
        function_id: Optional[str] = None,
        namespace_id: Optional[str] = None,
    ) -> List[Token]:
        """
        List all tokens.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number.
        :param page_size: Number of tokens per page.
        :param order_by: Sort order for the tokens.
        :param function_id: UUID of the function the token is assoicated with.
        :param namespace_id: UUID of the namespace the token is associated with.
        :return: :class:`List[Token] <List[Token]>`

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
                "function_id": function_id,
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
        :param token_id: UUID of the token to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Token <Token>`

        Usage:
        ::

            result = api.delete_token(
                token_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_token_id = validate_path_param("token_id", token_id)

        res = self._request(
            "DELETE",
            f"/functions/v1beta1/regions/{param_region}/tokens/{param_token_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Token(res.json())

    def create_trigger(
        self,
        *,
        name: str,
        function_id: str,
        region: Optional[Region] = None,
        description: Optional[str] = None,
        scw_sqs_config: Optional[CreateTriggerRequestMnqSqsClientConfig] = None,
        scw_nats_config: Optional[CreateTriggerRequestMnqNatsClientConfig] = None,
        sqs_config: Optional[CreateTriggerRequestSqsClientConfig] = None,
    ) -> Trigger:
        """
        Create a trigger.
        Create a new trigger for a specified function.
        :param name: Name of the trigger.
        :param function_id: ID of the function to trigger.
        :param region: Region to target. If none is passed will use default region from the config.
        :param description: Description of the trigger.
        :param scw_sqs_config: Configuration for a Scaleway Messaging and Queuing SQS queue.
        One-Of ('config'): at most one of 'scw_sqs_config', 'scw_nats_config', 'sqs_config' could be set.
        :param scw_nats_config: Configuration for a Scaleway Messaging and Queuing NATS subject.
        One-Of ('config'): at most one of 'scw_sqs_config', 'scw_nats_config', 'sqs_config' could be set.
        :param sqs_config: Configuration for an AWS SQS queue.
        One-Of ('config'): at most one of 'scw_sqs_config', 'scw_nats_config', 'sqs_config' could be set.
        :return: :class:`Trigger <Trigger>`

        Usage:
        ::

            result = api.create_trigger(
                name="example",
                function_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/functions/v1beta1/regions/{param_region}/triggers",
            body=marshal_CreateTriggerRequest(
                CreateTriggerRequest(
                    name=name,
                    function_id=function_id,
                    region=region,
                    description=description,
                    scw_sqs_config=scw_sqs_config,
                    scw_nats_config=scw_nats_config,
                    sqs_config=sqs_config,
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
        region: Optional[Region] = None,
    ) -> Trigger:
        """
        Get a trigger.
        Get a trigger with a specified ID.
        :param trigger_id: ID of the trigger to get.
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
            f"/functions/v1beta1/regions/{param_region}/triggers/{param_trigger_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Trigger(res.json())

    def wait_for_trigger(
        self,
        *,
        trigger_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Trigger, bool]] = None,
    ) -> Trigger:
        """
        Get a trigger.
        Get a trigger with a specified ID.
        :param trigger_id: ID of the trigger to get.
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
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListTriggersRequestOrderBy] = None,
        function_id: Optional[str] = None,
        namespace_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListTriggersResponse:
        """
        List all triggers.
        List all triggers belonging to a specified Organization or Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of triggers to return per page.
        :param order_by: Order in which to return results.
        :param function_id: ID of the function the triggers belongs to.
        One-Of ('scope'): at most one of 'function_id', 'namespace_id', 'project_id' could be set.
        :param namespace_id: ID of the namespace the triggers belongs to.
        One-Of ('scope'): at most one of 'function_id', 'namespace_id', 'project_id' could be set.
        :param project_id: ID of the project the triggers belongs to.
        One-Of ('scope'): at most one of 'function_id', 'namespace_id', 'project_id' could be set.
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
            f"/functions/v1beta1/regions/{param_region}/triggers",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                **resolve_one_of(
                    [
                        OneOfPossibility("function_id", function_id),
                        OneOfPossibility("namespace_id", namespace_id),
                        OneOfPossibility("project_id", project_id),
                    ]
                ),
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListTriggersResponse(res.json())

    def list_triggers_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListTriggersRequestOrderBy] = None,
        function_id: Optional[str] = None,
        namespace_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Trigger]:
        """
        List all triggers.
        List all triggers belonging to a specified Organization or Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of triggers to return per page.
        :param order_by: Order in which to return results.
        :param function_id: ID of the function the triggers belongs to.
        One-Of ('scope'): at most one of 'function_id', 'namespace_id', 'project_id' could be set.
        :param namespace_id: ID of the namespace the triggers belongs to.
        One-Of ('scope'): at most one of 'function_id', 'namespace_id', 'project_id' could be set.
        :param project_id: ID of the project the triggers belongs to.
        One-Of ('scope'): at most one of 'function_id', 'namespace_id', 'project_id' could be set.
        :return: :class:`List[Trigger] <List[Trigger]>`

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
                "function_id": function_id,
                "namespace_id": namespace_id,
                "project_id": project_id,
            },
        )

    def update_trigger(
        self,
        *,
        trigger_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        sqs_config: Optional[UpdateTriggerRequestSqsClientConfig] = None,
    ) -> Trigger:
        """
        Update a trigger.
        Update a trigger with a specified ID.
        :param trigger_id: ID of the trigger to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the trigger.
        :param description: Description of the trigger.
        :param sqs_config: Configuration for an AWS SQS queue.
        One-Of ('config'): at most one of 'sqs_config' could be set.
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
            f"/functions/v1beta1/regions/{param_region}/triggers/{param_trigger_id}",
            body=marshal_UpdateTriggerRequest(
                UpdateTriggerRequest(
                    trigger_id=trigger_id,
                    region=region,
                    name=name,
                    description=description,
                    sqs_config=sqs_config,
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
        region: Optional[Region] = None,
    ) -> Trigger:
        """
        Delete a trigger.
        Delete a trigger with a specified ID.
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
            f"/functions/v1beta1/regions/{param_region}/triggers/{param_trigger_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Trigger(res.json())
