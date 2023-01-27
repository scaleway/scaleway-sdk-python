# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Any, Awaitable, Dict, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    OneOfPossibility,
    WaitForOptions,
    fetch_all_pages_async,
    random_name,
    resolve_one_of,
    validate_path_param,
    wait_for_resource_async,
)
from .types import (
    FunctionHttpOption,
    FunctionPrivacy,
    FunctionRuntime,
    ListCronsRequestOrderBy,
    ListDomainsRequestOrderBy,
    ListFunctionsRequestOrderBy,
    ListLogsRequestOrderBy,
    ListNamespacesRequestOrderBy,
    ListTokensRequestOrderBy,
    ListTriggerInputsRequestOrderBy,
    ListTriggersRequestOrderBy,
    TriggerType,
    CreateTriggerInputRequestNatsClientConfigSpec,
    CreateTriggerInputRequestSqsClientConfigSpec,
    CreateTriggerRequestNatsFailureHandlingPolicy,
    CreateTriggerRequestSqsFailureHandlingPolicy,
    Cron,
    Domain,
    DownloadURL,
    Function,
    ListCronsResponse,
    ListDomainsResponse,
    ListFunctionRuntimesResponse,
    ListFunctionsResponse,
    ListLogsResponse,
    ListNamespacesResponse,
    ListTokensResponse,
    ListTriggerInputsResponse,
    ListTriggersResponse,
    Log,
    Namespace,
    Secret,
    SetTriggerInputsRequestNatsConfigs,
    SetTriggerInputsRequestSqsConfigs,
    SetTriggerInputsResponse,
    Token,
    Trigger,
    TriggerInput,
    UpdateTriggerInputRequestNatsClientConfigSpec,
    UpdateTriggerInputRequestSqsClientConfigSpec,
    UploadURL,
    CreateNamespaceRequest,
    UpdateNamespaceRequest,
    CreateFunctionRequest,
    UpdateFunctionRequest,
    CreateCronRequest,
    UpdateCronRequest,
    CreateDomainRequest,
    CreateTokenRequest,
    CreateTriggerRequest,
    UpdateTriggerRequest,
    CreateTriggerInputRequest,
    SetTriggerInputsRequest,
    UpdateTriggerInputRequest,
)
from .content import (
    CRON_TRANSIENT_STATUSES,
    DOMAIN_TRANSIENT_STATUSES,
    FUNCTION_TRANSIENT_STATUSES,
    NAMESPACE_TRANSIENT_STATUSES,
    TOKEN_TRANSIENT_STATUSES,
    TRIGGER_INPUT_TRANSIENT_STATUSES,
    TRIGGER_TRANSIENT_STATUSES,
)
from .marshalling import (
    marshal_CreateCronRequest,
    marshal_CreateDomainRequest,
    marshal_CreateFunctionRequest,
    marshal_CreateNamespaceRequest,
    marshal_CreateTokenRequest,
    marshal_CreateTriggerInputRequest,
    marshal_CreateTriggerRequest,
    marshal_SetTriggerInputsRequest,
    marshal_UpdateCronRequest,
    marshal_UpdateFunctionRequest,
    marshal_UpdateNamespaceRequest,
    marshal_UpdateTriggerInputRequest,
    marshal_UpdateTriggerRequest,
    unmarshal_Cron,
    unmarshal_Domain,
    unmarshal_Function,
    unmarshal_Namespace,
    unmarshal_Token,
    unmarshal_Trigger,
    unmarshal_TriggerInput,
    unmarshal_DownloadURL,
    unmarshal_ListCronsResponse,
    unmarshal_ListDomainsResponse,
    unmarshal_ListFunctionRuntimesResponse,
    unmarshal_ListFunctionsResponse,
    unmarshal_ListLogsResponse,
    unmarshal_ListNamespacesResponse,
    unmarshal_ListTokensResponse,
    unmarshal_ListTriggerInputsResponse,
    unmarshal_ListTriggersResponse,
    unmarshal_SetTriggerInputsResponse,
    unmarshal_UploadURL,
)


class FunctionV1Beta1API(API):
    """
    Functions API.

    Serverless functions API.
    """

    async def list_namespaces(
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
        List all your namespaces
        :param region: Region to target. If none is passed will use default region from the config
        :param page:
        :param page_size:
        :param order_by:
        :param name:
        :param organization_id:
        :param project_id:
        :return: :class:`ListNamespacesResponse <ListNamespacesResponse>`

        Usage:
        ::

            result = await api.list_namespaces()
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

    async def list_namespaces_all(
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
        List all your namespaces
        :param region: Region to target. If none is passed will use default region from the config
        :param page:
        :param page_size:
        :param order_by:
        :param name:
        :param organization_id:
        :param project_id:
        :return: :class:`List[ListNamespacesResponse] <List[ListNamespacesResponse]>`

        Usage:
        ::

            result = await api.list_namespaces_all()
        """

        return await fetch_all_pages_async(
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

    async def get_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
    ) -> Namespace:
        """
        Get the namespace associated with the given id.
        :param region: Region to target. If none is passed will use default region from the config
        :param namespace_id:
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = await api.get_namespace(namespace_id="example")
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

    async def wait_for_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
        options: Optional[
            WaitForOptions[Namespace, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> Namespace:
        """
        Waits for :class:`Namespace <Namespace>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config
        :param namespace_id:
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

        return await wait_for_resource_async(
            fetcher=self.get_namespace,
            options=options,
            args={
                "namespace_id": namespace_id,
                "region": region,
            },
        )

    async def create_namespace(
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
        Create a new namespace
        :param region: Region to target. If none is passed will use default region from the config
        :param name:
        :param environment_variables:
        :param project_id:
        :param description:
        :param secret_environment_variables:
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = await api.create_namespace()
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

    async def update_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
        environment_variables: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        secret_environment_variables: Optional[List[Secret]] = None,
    ) -> Namespace:
        """
        Update the space associated with the given id.
        :param region: Region to target. If none is passed will use default region from the config
        :param namespace_id:
        :param environment_variables:
        :param description:
        :param secret_environment_variables:
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = await api.update_namespace(namespace_id="example")
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

    async def delete_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
    ) -> Namespace:
        """
        Delete the namespace associated with the given id.
        :param region: Region to target. If none is passed will use default region from the config
        :param namespace_id:
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = await api.delete_namespace(namespace_id="example")
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

    async def list_functions(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListFunctionsRequestOrderBy = ListFunctionsRequestOrderBy.CREATED_AT_ASC,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListFunctionsResponse:
        """
        List all your functions
        :param region: Region to target. If none is passed will use default region from the config
        :param page:
        :param page_size:
        :param order_by:
        :param namespace_id:
        :param name:
        :param organization_id:
        :param project_id:
        :return: :class:`ListFunctionsResponse <ListFunctionsResponse>`

        Usage:
        ::

            result = await api.list_functions(namespace_id="example")
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

    async def list_functions_all(
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
        List all your functions
        :param region: Region to target. If none is passed will use default region from the config
        :param page:
        :param page_size:
        :param order_by:
        :param namespace_id:
        :param name:
        :param organization_id:
        :param project_id:
        :return: :class:`List[ListFunctionsResponse] <List[ListFunctionsResponse]>`

        Usage:
        ::

            result = await api.list_functions_all(namespace_id="example")
        """

        return await fetch_all_pages_async(
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

    async def get_function(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
    ) -> Function:
        """
        Get the function associated with the given id.
        :param region: Region to target. If none is passed will use default region from the config
        :param function_id:
        :return: :class:`Function <Function>`

        Usage:
        ::

            result = await api.get_function(function_id="example")
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

    async def wait_for_function(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
        options: Optional[
            WaitForOptions[Function, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> Function:
        """
        Waits for :class:`Function <Function>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config
        :param function_id:
        :param options: The options for the waiter
        :return: :class:`Function <Function>`

        Usage:
        ::

            result = api.wait_for_function(function_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in FUNCTION_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_function,
            options=options,
            args={
                "function_id": function_id,
                "region": region,
            },
        )

    async def create_function(
        self,
        *,
        namespace_id: str,
        runtime: FunctionRuntime,
        privacy: FunctionPrivacy,
        http_option: FunctionHttpOption,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        environment_variables: Optional[Dict[str, str]] = None,
        min_scale: Optional[int] = None,
        max_scale: Optional[int] = None,
        memory_limit: Optional[int] = None,
        timeout: Optional[str] = None,
        handler: Optional[str] = None,
        description: Optional[str] = None,
        secret_environment_variables: Optional[List[Secret]] = None,
    ) -> Function:
        """
        Create a new function
        :param region: Region to target. If none is passed will use default region from the config
        :param name:
        :param namespace_id:
        :param environment_variables:
        :param min_scale:
        :param max_scale:
        :param runtime:
        :param memory_limit:
        :param timeout:
        :param handler:
        :param privacy:
        :param description:
        :param secret_environment_variables:
        :param http_option: possible values:
         - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
         - enabled: Serve both HTTP and HTTPS traffic.

        :return: :class:`Function <Function>`

        Usage:
        ::

            result = await api.create_function(
                namespace_id="example",
                runtime=unknown_runtime,
                privacy=unknown_privacy,
                http_option=unknown_http_option,
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
                    runtime=runtime,
                    privacy=privacy,
                    http_option=http_option,
                    region=region,
                    name=name or random_name(prefix="fn"),
                    environment_variables=environment_variables,
                    min_scale=min_scale,
                    max_scale=max_scale,
                    memory_limit=memory_limit,
                    timeout=timeout,
                    handler=handler,
                    description=description,
                    secret_environment_variables=secret_environment_variables,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Function(res.json())

    async def update_function(
        self,
        *,
        function_id: str,
        runtime: FunctionRuntime,
        privacy: FunctionPrivacy,
        http_option: FunctionHttpOption,
        region: Optional[Region] = None,
        environment_variables: Optional[Dict[str, str]] = None,
        min_scale: Optional[int] = None,
        max_scale: Optional[int] = None,
        memory_limit: Optional[int] = None,
        timeout: Optional[str] = None,
        redeploy: Optional[bool] = None,
        handler: Optional[str] = None,
        description: Optional[str] = None,
        secret_environment_variables: Optional[List[Secret]] = None,
    ) -> Function:
        """
        Update the function associated with the given id.
        :param region: Region to target. If none is passed will use default region from the config
        :param function_id:
        :param environment_variables:
        :param min_scale:
        :param max_scale:
        :param runtime:
        :param memory_limit:
        :param timeout:
        :param redeploy:
        :param handler:
        :param privacy:
        :param description:
        :param secret_environment_variables:
        :param http_option: possible values:
         - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
         - enabled: Serve both HTTP and HTTPS traffic.

        :return: :class:`Function <Function>`

        Usage:
        ::

            result = await api.update_function(
                function_id="example",
                runtime=unknown_runtime,
                privacy=unknown_privacy,
                http_option=unknown_http_option,
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
                    runtime=runtime,
                    privacy=privacy,
                    http_option=http_option,
                    region=region,
                    environment_variables=environment_variables,
                    min_scale=min_scale,
                    max_scale=max_scale,
                    memory_limit=memory_limit,
                    timeout=timeout,
                    redeploy=redeploy,
                    handler=handler,
                    description=description,
                    secret_environment_variables=secret_environment_variables,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Function(res.json())

    async def delete_function(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
    ) -> Function:
        """
        Delete the function associated with the given id.
        :param region: Region to target. If none is passed will use default region from the config
        :param function_id:
        :return: :class:`Function <Function>`

        Usage:
        ::

            result = await api.delete_function(function_id="example")
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

    async def deploy_function(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
    ) -> Function:
        """
        Deploy a function associated with the given id.
        :param region: Region to target. If none is passed will use default region from the config
        :param function_id:
        :return: :class:`Function <Function>`

        Usage:
        ::

            result = await api.deploy_function(function_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_function_id = validate_path_param("function_id", function_id)

        res = self._request(
            "POST",
            f"/functions/v1beta1/regions/{param_region}/functions/{param_function_id}/deploy",
        )

        self._throw_on_error(res)
        return unmarshal_Function(res.json())

    async def list_function_runtimes(
        self,
        *,
        region: Optional[Region] = None,
    ) -> ListFunctionRuntimesResponse:
        """
        List available function runtimes.
        :param region: Region to target. If none is passed will use default region from the config
        :return: :class:`ListFunctionRuntimesResponse <ListFunctionRuntimesResponse>`

        Usage:
        ::

            result = await api.list_function_runtimes()
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

    async def get_function_upload_url(
        self,
        *,
        function_id: str,
        content_length: int,
        region: Optional[Region] = None,
    ) -> UploadURL:
        """
        Get an upload URL of a function associated with the given id.
        :param region: Region to target. If none is passed will use default region from the config
        :param function_id:
        :param content_length:
        :return: :class:`UploadURL <UploadURL>`

        Usage:
        ::

            result = await api.get_function_upload_url(
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

    async def get_function_download_url(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
    ) -> DownloadURL:
        """
        Get a download URL for a function associated with the given id.
        :param region: Region to target. If none is passed will use default region from the config
        :param function_id:
        :return: :class:`DownloadURL <DownloadURL>`

        Usage:
        ::

            result = await api.get_function_download_url(function_id="example")
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

    async def list_crons(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListCronsRequestOrderBy = ListCronsRequestOrderBy.CREATED_AT_ASC,
    ) -> ListCronsResponse:
        """
        List all your crons
        :param region: Region to target. If none is passed will use default region from the config
        :param page:
        :param page_size:
        :param order_by:
        :param function_id:
        :return: :class:`ListCronsResponse <ListCronsResponse>`

        Usage:
        ::

            result = await api.list_crons(function_id="example")
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

    async def list_crons_all(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListCronsRequestOrderBy] = None,
    ) -> List[Cron]:
        """
        List all your crons
        :param region: Region to target. If none is passed will use default region from the config
        :param page:
        :param page_size:
        :param order_by:
        :param function_id:
        :return: :class:`List[ListCronsResponse] <List[ListCronsResponse]>`

        Usage:
        ::

            result = await api.list_crons_all(function_id="example")
        """

        return await fetch_all_pages_async(
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

    async def get_cron(
        self,
        *,
        cron_id: str,
        region: Optional[Region] = None,
    ) -> Cron:
        """
        Get the cron associated with the given id.
        :param region: Region to target. If none is passed will use default region from the config
        :param cron_id:
        :return: :class:`Cron <Cron>`

        Usage:
        ::

            result = await api.get_cron(cron_id="example")
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

    async def wait_for_cron(
        self,
        *,
        cron_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Cron, Union[bool, Awaitable[bool]]]] = None,
    ) -> Cron:
        """
        Waits for :class:`Cron <Cron>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config
        :param cron_id:
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

        return await wait_for_resource_async(
            fetcher=self.get_cron,
            options=options,
            args={
                "cron_id": cron_id,
                "region": region,
            },
        )

    async def create_cron(
        self,
        *,
        function_id: str,
        schedule: str,
        region: Optional[Region] = None,
        args: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
    ) -> Cron:
        """
        Create a new cron
        :param region: Region to target. If none is passed will use default region from the config
        :param function_id:
        :param schedule:
        :param args:
        :param name:
        :return: :class:`Cron <Cron>`

        Usage:
        ::

            result = await api.create_cron(
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

    async def update_cron(
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
        Update the cron associated with the given id.
        :param region: Region to target. If none is passed will use default region from the config
        :param cron_id:
        :param function_id:
        :param schedule:
        :param args:
        :param name:
        :return: :class:`Cron <Cron>`

        Usage:
        ::

            result = await api.update_cron(cron_id="example")
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

    async def delete_cron(
        self,
        *,
        cron_id: str,
        region: Optional[Region] = None,
    ) -> Cron:
        """
        Delete the cron associated with the given id.
        :param region: Region to target. If none is passed will use default region from the config
        :param cron_id:
        :return: :class:`Cron <Cron>`

        Usage:
        ::

            result = await api.delete_cron(cron_id="example")
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

    async def list_logs(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListLogsRequestOrderBy = ListLogsRequestOrderBy.TIMESTAMP_DESC,
    ) -> ListLogsResponse:
        """
        List your application logs
        :param region: Region to target. If none is passed will use default region from the config
        :param function_id:
        :param page:
        :param page_size:
        :param order_by:
        :return: :class:`ListLogsResponse <ListLogsResponse>`

        Usage:
        ::

            result = await api.list_logs(function_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_function_id = validate_path_param("function_id", function_id)

        res = self._request(
            "GET",
            f"/functions/v1beta1/regions/{param_region}/functions/{param_function_id}/logs",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListLogsResponse(res.json())

    async def list_logs_all(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListLogsRequestOrderBy] = None,
    ) -> List[Log]:
        """
        List your application logs
        :param region: Region to target. If none is passed will use default region from the config
        :param function_id:
        :param page:
        :param page_size:
        :param order_by:
        :return: :class:`List[ListLogsResponse] <List[ListLogsResponse]>`

        Usage:
        ::

            result = await api.list_logs_all(function_id="example")
        """

        return await fetch_all_pages_async(
            type=ListLogsResponse,
            key="logs",
            fetcher=self.list_logs,
            args={
                "function_id": function_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def list_domains(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListDomainsRequestOrderBy = ListDomainsRequestOrderBy.CREATED_AT_ASC,
    ) -> ListDomainsResponse:
        """
        List all domain name bindings
        :param region: Region to target. If none is passed will use default region from the config
        :param page:
        :param page_size:
        :param order_by:
        :param function_id:
        :return: :class:`ListDomainsResponse <ListDomainsResponse>`

        Usage:
        ::

            result = await api.list_domains(function_id="example")
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

    async def list_domains_all(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDomainsRequestOrderBy] = None,
    ) -> List[Domain]:
        """
        List all domain name bindings
        :param region: Region to target. If none is passed will use default region from the config
        :param page:
        :param page_size:
        :param order_by:
        :param function_id:
        :return: :class:`List[ListDomainsResponse] <List[ListDomainsResponse]>`

        Usage:
        ::

            result = await api.list_domains_all(function_id="example")
        """

        return await fetch_all_pages_async(
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

    async def get_domain(
        self,
        *,
        domain_id: str,
        region: Optional[Region] = None,
    ) -> Domain:
        """
        Get a domain name binding
        :param region: Region to target. If none is passed will use default region from the config
        :param domain_id:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = await api.get_domain(domain_id="example")
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

    async def wait_for_domain(
        self,
        *,
        domain_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Domain, Union[bool, Awaitable[bool]]]] = None,
    ) -> Domain:
        """
        Waits for :class:`Domain <Domain>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config
        :param domain_id:
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

        return await wait_for_resource_async(
            fetcher=self.get_domain,
            options=options,
            args={
                "domain_id": domain_id,
                "region": region,
            },
        )

    async def create_domain(
        self,
        *,
        hostname: str,
        function_id: str,
        region: Optional[Region] = None,
    ) -> Domain:
        """
        Create a domain name binding
        :param region: Region to target. If none is passed will use default region from the config
        :param hostname:
        :param function_id:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = await api.create_domain(
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

    async def delete_domain(
        self,
        *,
        domain_id: str,
        region: Optional[Region] = None,
    ) -> Domain:
        """
        Delete a domain name binding
        :param region: Region to target. If none is passed will use default region from the config
        :param domain_id:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = await api.delete_domain(domain_id="example")
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

    async def issue_jwt(
        self,
        *,
        region: Optional[Region] = None,
        function_id: Optional[str] = None,
        namespace_id: Optional[str] = None,
        expires_at: Optional[datetime] = None,
    ) -> Token:
        """
        :deprecated

        Usage:
        ::

            result = await api.issue_jwt()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/functions/v1beta1/regions/{param_region}/issue-jwt",
            params={
                "expires_at": expires_at,
                **resolve_one_of(
                    [
                        OneOfPossibility("function_id", function_id),
                        OneOfPossibility("namespace_id", namespace_id),
                    ]
                ),
            },
        )

        self._throw_on_error(res)
        return unmarshal_Token(res.json())

    async def create_token(
        self,
        *,
        region: Optional[Region] = None,
        function_id: Optional[str] = None,
        namespace_id: Optional[str] = None,
        description: Optional[str] = None,
        expires_at: Optional[datetime] = None,
    ) -> Token:
        """
        Create a new revocable token
        :param region: Region to target. If none is passed will use default region from the config
        :param function_id: One-of ('scope'): at most one of 'function_id', 'namespace_id' could be set.
        :param namespace_id: One-of ('scope'): at most one of 'function_id', 'namespace_id' could be set.
        :param description:
        :param expires_at:
        :return: :class:`Token <Token>`

        Usage:
        ::

            result = await api.create_token()
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
                    function_id=function_id,
                    namespace_id=namespace_id,
                    description=description,
                    expires_at=expires_at,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Token(res.json())

    async def get_token(
        self,
        *,
        token_id: str,
        region: Optional[Region] = None,
    ) -> Token:
        """
        Get a token
        :param region: Region to target. If none is passed will use default region from the config
        :param token_id:
        :return: :class:`Token <Token>`

        Usage:
        ::

            result = await api.get_token(token_id="example")
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

    async def wait_for_token(
        self,
        *,
        token_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Token, Union[bool, Awaitable[bool]]]] = None,
    ) -> Token:
        """
        Waits for :class:`Token <Token>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config
        :param token_id:
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

        return await wait_for_resource_async(
            fetcher=self.get_token,
            options=options,
            args={
                "token_id": token_id,
                "region": region,
            },
        )

    async def list_tokens(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListTokensRequestOrderBy = ListTokensRequestOrderBy.CREATED_AT_ASC,
        function_id: Optional[str] = None,
        namespace_id: Optional[str] = None,
    ) -> ListTokensResponse:
        """
        List all tokens
        :param region: Region to target. If none is passed will use default region from the config
        :param page:
        :param page_size:
        :param order_by:
        :param function_id:
        :param namespace_id:
        :return: :class:`ListTokensResponse <ListTokensResponse>`

        Usage:
        ::

            result = await api.list_tokens()
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

    async def list_tokens_all(
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
        List all tokens
        :param region: Region to target. If none is passed will use default region from the config
        :param page:
        :param page_size:
        :param order_by:
        :param function_id:
        :param namespace_id:
        :return: :class:`List[ListTokensResponse] <List[ListTokensResponse]>`

        Usage:
        ::

            result = await api.list_tokens_all()
        """

        return await fetch_all_pages_async(
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

    async def delete_token(
        self,
        *,
        token_id: str,
        region: Optional[Region] = None,
    ) -> Token:
        """
        Delete a token
        :param region: Region to target. If none is passed will use default region from the config
        :param token_id:
        :return: :class:`Token <Token>`

        Usage:
        ::

            result = await api.delete_token(token_id="example")
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

    async def create_trigger(
        self,
        *,
        name: str,
        description: str,
        function_id: str,
        type_: TriggerType,
        region: Optional[Region] = None,
        nats_failure_handling_policy: Optional[
            CreateTriggerRequestNatsFailureHandlingPolicy
        ] = None,
        sqs_failure_handling_policy: Optional[
            CreateTriggerRequestSqsFailureHandlingPolicy
        ] = None,
    ) -> Trigger:
        """

        Usage:
        ::

            result = await api.create_trigger(
                name="example",
                description="example",
                function_id="example",
                type_=unknown_trigger_type,
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
                    description=description,
                    function_id=function_id,
                    type_=type_,
                    region=region,
                    nats_failure_handling_policy=nats_failure_handling_policy,
                    sqs_failure_handling_policy=sqs_failure_handling_policy,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Trigger(res.json())

    async def get_trigger(
        self,
        *,
        trigger_id: str,
        region: Optional[Region] = None,
    ) -> Trigger:
        """

        Usage:
        ::

            result = await api.get_trigger(trigger_id="example")
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

    async def wait_for_trigger(
        self,
        *,
        trigger_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Trigger, Union[bool, Awaitable[bool]]]] = None,
    ) -> Trigger:
        """
        Waits for :class:`Trigger <Trigger>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config
        :param trigger_id:
        :param options: The options for the waiter
        :return: :class:`Trigger <Trigger>`

        Usage:
        ::

            result = api.wait_for_trigger(trigger_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in TRIGGER_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_trigger,
            options=options,
            args={
                "trigger_id": trigger_id,
                "region": region,
            },
        )

    async def list_triggers(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListTriggersRequestOrderBy = ListTriggersRequestOrderBy.CREATED_AT_ASC,
    ) -> ListTriggersResponse:
        """

        Usage:
        ::

            result = await api.list_triggers(function_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/functions/v1beta1/regions/{param_region}/triggers",
            params={
                "function_id": function_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListTriggersResponse(res.json())

    async def list_triggers_all(
        self,
        *,
        function_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListTriggersRequestOrderBy] = None,
    ) -> List[Trigger]:
        """
        :return: :class:`List[ListTriggersResponse] <List[ListTriggersResponse]>`

        Usage:
        ::

            result = await api.list_triggers_all(function_id="example")
        """

        return await fetch_all_pages_async(
            type=ListTriggersResponse,
            key="triggers",
            fetcher=self.list_triggers,
            args={
                "function_id": function_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def update_trigger(
        self,
        *,
        trigger_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        nats_config: Optional[CreateTriggerRequestNatsFailureHandlingPolicy] = None,
        sqs_config: Optional[CreateTriggerRequestSqsFailureHandlingPolicy] = None,
    ) -> Trigger:
        """

        Usage:
        ::

            result = await api.update_trigger(trigger_id="example")
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
                    nats_config=nats_config,
                    sqs_config=sqs_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Trigger(res.json())

    async def delete_trigger(
        self,
        *,
        trigger_id: str,
        region: Optional[Region] = None,
    ) -> Trigger:
        """

        Usage:
        ::

            result = await api.delete_trigger(trigger_id="example")
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

    async def create_trigger_input(
        self,
        *,
        trigger_id: str,
        region: Optional[Region] = None,
        mnq_namespace_id: Optional[str] = None,
        nats_config: Optional[CreateTriggerInputRequestNatsClientConfigSpec] = None,
        sqs_config: Optional[CreateTriggerInputRequestSqsClientConfigSpec] = None,
    ) -> TriggerInput:
        """

        Usage:
        ::

            result = await api.create_trigger_input(trigger_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/functions/v1beta1/regions/{param_region}/trigger-inputs",
            body=marshal_CreateTriggerInputRequest(
                CreateTriggerInputRequest(
                    trigger_id=trigger_id,
                    region=region,
                    mnq_namespace_id=mnq_namespace_id,
                    nats_config=nats_config,
                    sqs_config=sqs_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_TriggerInput(res.json())

    async def get_trigger_input(
        self,
        *,
        trigger_input_id: str,
        region: Optional[Region] = None,
    ) -> TriggerInput:
        """

        Usage:
        ::

            result = await api.get_trigger_input(trigger_input_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_trigger_input_id = validate_path_param(
            "trigger_input_id", trigger_input_id
        )

        res = self._request(
            "GET",
            f"/functions/v1beta1/regions/{param_region}/trigger-inputs/{param_trigger_input_id}",
        )

        self._throw_on_error(res)
        return unmarshal_TriggerInput(res.json())

    async def wait_for_trigger_input(
        self,
        *,
        trigger_input_id: str,
        region: Optional[Region] = None,
        options: Optional[
            WaitForOptions[TriggerInput, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> TriggerInput:
        """
        Waits for :class:`TriggerInput <TriggerInput>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config
        :param trigger_input_id:
        :param options: The options for the waiter
        :return: :class:`TriggerInput <TriggerInput>`

        Usage:
        ::

            result = api.wait_for_trigger_input(trigger_input_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = (
                lambda res: res.status not in TRIGGER_INPUT_TRANSIENT_STATUSES
            )

        return await wait_for_resource_async(
            fetcher=self.get_trigger_input,
            options=options,
            args={
                "trigger_input_id": trigger_input_id,
                "region": region,
            },
        )

    async def list_trigger_inputs(
        self,
        *,
        trigger_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListTriggerInputsRequestOrderBy = ListTriggerInputsRequestOrderBy.CREATED_AT_ASC,
    ) -> ListTriggerInputsResponse:
        """

        Usage:
        ::

            result = await api.list_trigger_inputs(trigger_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/functions/v1beta1/regions/{param_region}/trigger-inputs",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "trigger_id": trigger_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListTriggerInputsResponse(res.json())

    async def list_trigger_inputs_all(
        self,
        *,
        trigger_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListTriggerInputsRequestOrderBy] = None,
    ) -> List[TriggerInput]:
        """
        :return: :class:`List[ListTriggerInputsResponse] <List[ListTriggerInputsResponse]>`

        Usage:
        ::

            result = await api.list_trigger_inputs_all(trigger_id="example")
        """

        return await fetch_all_pages_async(
            type=ListTriggerInputsResponse,
            key="inputs",
            fetcher=self.list_trigger_inputs,
            args={
                "trigger_id": trigger_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def set_trigger_inputs(
        self,
        *,
        trigger_input_id: str,
        region: Optional[Region] = None,
        sqs: Optional[SetTriggerInputsRequestSqsConfigs] = None,
        nats: Optional[SetTriggerInputsRequestNatsConfigs] = None,
    ) -> SetTriggerInputsResponse:
        """

        Usage:
        ::

            result = await api.set_trigger_inputs(trigger_input_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "PUT",
            f"/functions/v1beta1/regions/{param_region}/trigger-inputs",
            body=marshal_SetTriggerInputsRequest(
                SetTriggerInputsRequest(
                    trigger_input_id=trigger_input_id,
                    region=region,
                    sqs=sqs,
                    nats=nats,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetTriggerInputsResponse(res.json())

    async def update_trigger_input(
        self,
        *,
        trigger_input_id: str,
        region: Optional[Region] = None,
        nats_config: Optional[UpdateTriggerInputRequestNatsClientConfigSpec] = None,
        sqs_config: Optional[UpdateTriggerInputRequestSqsClientConfigSpec] = None,
    ) -> TriggerInput:
        """

        Usage:
        ::

            result = await api.update_trigger_input(trigger_input_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_trigger_input_id = validate_path_param(
            "trigger_input_id", trigger_input_id
        )

        res = self._request(
            "PATCH",
            f"/functions/v1beta1/regions/{param_region}/trigger-inputs/{param_trigger_input_id}",
            body=marshal_UpdateTriggerInputRequest(
                UpdateTriggerInputRequest(
                    trigger_input_id=trigger_input_id,
                    region=region,
                    nats_config=nats_config,
                    sqs_config=sqs_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_TriggerInput(res.json())

    async def delete_trigger_input(
        self,
        *,
        trigger_input_id: str,
        region: Optional[Region] = None,
    ) -> TriggerInput:
        """

        Usage:
        ::

            result = await api.delete_trigger_input(trigger_input_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_trigger_input_id = validate_path_param(
            "trigger_input_id", trigger_input_id
        )

        res = self._request(
            "DELETE",
            f"/functions/v1beta1/regions/{param_region}/trigger-inputs/{param_trigger_input_id}",
        )

        self._throw_on_error(res)
        return unmarshal_TriggerInput(res.json())
