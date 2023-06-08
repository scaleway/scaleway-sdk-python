# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from dateutil import parser
from .types import (
    FunctionHttpOption,
    FunctionPrivacy,
    FunctionRuntime,
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
    ListLogsResponse,
    ListNamespacesResponse,
    ListTokensResponse,
    ListTriggersResponse,
    Log,
    Namespace,
    Runtime,
    Secret,
    SecretHashedValue,
    Token,
    Trigger,
    TriggerMnqNatsClientConfig,
    TriggerMnqSqsClientConfig,
    TriggerSqsClientConfig,
    UpdateTriggerRequestSqsClientConfig,
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
)


def unmarshal_SecretHashedValue(data: Any) -> SecretHashedValue:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SecretHashedValue' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("hashed_value", None)
    args["hashed_value"] = field

    field = data.get("key", None)
    args["key"] = field

    return SecretHashedValue(**args)


def unmarshal_TriggerMnqNatsClientConfig(data: Any) -> TriggerMnqNatsClientConfig:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'TriggerMnqNatsClientConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("mnq_credential_id", None)
    args["mnq_credential_id"] = field

    field = data.get("mnq_namespace_id", None)
    args["mnq_namespace_id"] = field

    field = data.get("mnq_project_id", None)
    args["mnq_project_id"] = field

    field = data.get("mnq_region", None)
    args["mnq_region"] = field

    field = data.get("subject", None)
    args["subject"] = field

    return TriggerMnqNatsClientConfig(**args)


def unmarshal_TriggerMnqSqsClientConfig(data: Any) -> TriggerMnqSqsClientConfig:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'TriggerMnqSqsClientConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("mnq_credential_id", None)
    args["mnq_credential_id"] = field

    field = data.get("mnq_namespace_id", None)
    args["mnq_namespace_id"] = field

    field = data.get("mnq_project_id", None)
    args["mnq_project_id"] = field

    field = data.get("mnq_region", None)
    args["mnq_region"] = field

    field = data.get("queue", None)
    args["queue"] = field

    return TriggerMnqSqsClientConfig(**args)


def unmarshal_TriggerSqsClientConfig(data: Any) -> TriggerSqsClientConfig:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'TriggerSqsClientConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("access_key", None)
    args["access_key"] = field

    field = data.get("endpoint", None)
    args["endpoint"] = field

    field = data.get("queue_url", None)
    args["queue_url"] = field

    field = data.get("secret_key", None)
    args["secret_key"] = field

    return TriggerSqsClientConfig(**args)


def unmarshal_Cron(data: Any) -> Cron:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Cron' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("args", None)
    args["args"] = field

    field = data.get("function_id", None)
    args["function_id"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("schedule", None)
    args["schedule"] = field

    field = data.get("status", None)
    args["status"] = field

    return Cron(**args)


def unmarshal_Domain(data: Any) -> Domain:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Domain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("error_message", None)
    args["error_message"] = field

    field = data.get("function_id", None)
    args["function_id"] = field

    field = data.get("hostname", None)
    args["hostname"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("url", None)
    args["url"] = field

    return Domain(**args)


def unmarshal_Function(data: Any) -> Function:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Function' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("build_message", None)
    args["build_message"] = field

    field = data.get("cpu_limit", None)
    args["cpu_limit"] = field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("domain_name", None)
    args["domain_name"] = field

    field = data.get("environment_variables", None)
    args["environment_variables"] = field

    field = data.get("error_message", None)
    args["error_message"] = field

    field = data.get("handler", None)
    args["handler"] = field

    field = data.get("http_option", None)
    args["http_option"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("max_scale", None)
    args["max_scale"] = field

    field = data.get("memory_limit", None)
    args["memory_limit"] = field

    field = data.get("min_scale", None)
    args["min_scale"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("namespace_id", None)
    args["namespace_id"] = field

    field = data.get("privacy", None)
    args["privacy"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("runtime", None)
    args["runtime"] = field

    field = data.get("runtime_message", None)
    args["runtime_message"] = field

    field = data.get("secret_environment_variables", None)
    args["secret_environment_variables"] = (
        [unmarshal_SecretHashedValue(v) for v in field] if field is not None else None
    )

    field = data.get("status", None)
    args["status"] = field

    field = data.get("timeout", None)
    args["timeout"] = field

    return Function(**args)


def unmarshal_Log(data: Any) -> Log:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Log' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("level", None)
    args["level"] = field

    field = data.get("message", None)
    args["message"] = field

    field = data.get("source", None)
    args["source"] = field

    field = data.get("stream", None)
    args["stream"] = field

    field = data.get("timestamp", None)
    args["timestamp"] = parser.isoparse(field) if type(field) is str else field

    return Log(**args)


def unmarshal_Namespace(data: Any) -> Namespace:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Namespace' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description", None)
    args["description"] = field

    field = data.get("environment_variables", None)
    args["environment_variables"] = field

    field = data.get("error_message", None)
    args["error_message"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("registry_endpoint", None)
    args["registry_endpoint"] = field

    field = data.get("registry_namespace_id", None)
    args["registry_namespace_id"] = field

    field = data.get("secret_environment_variables", None)
    args["secret_environment_variables"] = (
        [unmarshal_SecretHashedValue(v) for v in field] if field is not None else None
    )

    field = data.get("status", None)
    args["status"] = field

    return Namespace(**args)


def unmarshal_Runtime(data: Any) -> Runtime:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Runtime' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("code_sample", None)
    args["code_sample"] = field

    field = data.get("default_handler", None)
    args["default_handler"] = field

    field = data.get("extension", None)
    args["extension"] = field

    field = data.get("implementation", None)
    args["implementation"] = field

    field = data.get("language", None)
    args["language"] = field

    field = data.get("logo_url", None)
    args["logo_url"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("status_message", None)
    args["status_message"] = field

    field = data.get("version", None)
    args["version"] = field

    return Runtime(**args)


def unmarshal_Token(data: Any) -> Token:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Token' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description", None)
    args["description"] = field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("function_id", None)
    args["function_id"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("namespace_id", None)
    args["namespace_id"] = field

    field = data.get("public_key", None)
    args["public_key"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("token", None)
    args["token"] = field

    return Token(**args)


def unmarshal_Trigger(data: Any) -> Trigger:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Trigger' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description", None)
    args["description"] = field

    field = data.get("error_message", None)
    args["error_message"] = field

    field = data.get("function_id", None)
    args["function_id"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("input_type", None)
    args["input_type"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("scw_nats_config", None)
    args["scw_nats_config"] = (
        unmarshal_TriggerMnqNatsClientConfig(field) if field is not None else None
    )

    field = data.get("scw_sqs_config", None)
    args["scw_sqs_config"] = (
        unmarshal_TriggerMnqSqsClientConfig(field) if field is not None else None
    )

    field = data.get("sqs_config", None)
    args["sqs_config"] = (
        unmarshal_TriggerSqsClientConfig(field) if field is not None else None
    )

    field = data.get("status", None)
    args["status"] = field

    return Trigger(**args)


def unmarshal_DownloadURL(data: Any) -> DownloadURL:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DownloadURL' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("headers", None)
    args["headers"] = field

    field = data.get("url", None)
    args["url"] = field

    return DownloadURL(**args)


def unmarshal_ListCronsResponse(data: Any) -> ListCronsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListCronsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("crons", None)
    args["crons"] = [unmarshal_Cron(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListCronsResponse(**args)


def unmarshal_ListDomainsResponse(data: Any) -> ListDomainsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDomainsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domains", None)
    args["domains"] = (
        [unmarshal_Domain(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListDomainsResponse(**args)


def unmarshal_ListFunctionRuntimesResponse(data: Any) -> ListFunctionRuntimesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListFunctionRuntimesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("runtimes", None)
    args["runtimes"] = (
        [unmarshal_Runtime(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListFunctionRuntimesResponse(**args)


def unmarshal_ListFunctionsResponse(data: Any) -> ListFunctionsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListFunctionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("functions", None)
    args["functions"] = (
        [unmarshal_Function(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListFunctionsResponse(**args)


def unmarshal_ListLogsResponse(data: Any) -> ListLogsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListLogsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("logs", None)
    args["logs"] = [unmarshal_Log(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListLogsResponse(**args)


def unmarshal_ListNamespacesResponse(data: Any) -> ListNamespacesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListNamespacesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("namespaces", None)
    args["namespaces"] = (
        [unmarshal_Namespace(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListNamespacesResponse(**args)


def unmarshal_ListTokensResponse(data: Any) -> ListTokensResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListTokensResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("tokens", None)
    args["tokens"] = [unmarshal_Token(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListTokensResponse(**args)


def unmarshal_ListTriggersResponse(data: Any) -> ListTriggersResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListTriggersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    args["total_count"] = field

    field = data.get("triggers", None)
    args["triggers"] = (
        [unmarshal_Trigger(v) for v in field] if field is not None else None
    )

    return ListTriggersResponse(**args)


def unmarshal_UploadURL(data: Any) -> UploadURL:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'UploadURL' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("headers", None)
    args["headers"] = field

    field = data.get("url", None)
    args["url"] = field

    return UploadURL(**args)


def marshal_CreateTriggerRequestMnqNatsClientConfig(
    request: CreateTriggerRequestMnqNatsClientConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "mnq_namespace_id": request.mnq_namespace_id,
        "mnq_project_id": request.mnq_project_id,
        "mnq_region": request.mnq_region,
        "subject": request.subject,
    }


def marshal_CreateTriggerRequestMnqSqsClientConfig(
    request: CreateTriggerRequestMnqSqsClientConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "mnq_namespace_id": request.mnq_namespace_id,
        "mnq_project_id": request.mnq_project_id,
        "mnq_region": request.mnq_region,
        "queue": request.queue,
    }


def marshal_CreateTriggerRequestSqsClientConfig(
    request: CreateTriggerRequestSqsClientConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "access_key": request.access_key,
        "endpoint": request.endpoint,
        "queue_url": request.queue_url,
        "secret_key": request.secret_key,
    }


def marshal_Secret(
    request: Secret,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "key": request.key,
        "value": request.value,
    }


def marshal_UpdateTriggerRequestSqsClientConfig(
    request: UpdateTriggerRequestSqsClientConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "access_key": request.access_key,
        "secret_key": request.secret_key,
    }


def marshal_CreateCronRequest(
    request: CreateCronRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "args": request.args,
        "function_id": request.function_id,
        "name": request.name,
        "schedule": request.schedule,
    }


def marshal_CreateDomainRequest(
    request: CreateDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "function_id": request.function_id,
        "hostname": request.hostname,
    }


def marshal_CreateFunctionRequest(
    request: CreateFunctionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "environment_variables": request.environment_variables,
        "handler": request.handler,
        "http_option": FunctionHttpOption(request.http_option),
        "max_scale": request.max_scale,
        "memory_limit": request.memory_limit,
        "min_scale": request.min_scale,
        "name": request.name,
        "namespace_id": request.namespace_id,
        "privacy": FunctionPrivacy(request.privacy),
        "runtime": FunctionRuntime(request.runtime),
        "secret_environment_variables": [
            marshal_Secret(v, defaults) for v in request.secret_environment_variables
        ]
        if request.secret_environment_variables is not None
        else None,
        "timeout": request.timeout,
    }


def marshal_CreateNamespaceRequest(
    request: CreateNamespaceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "environment_variables": request.environment_variables,
        "name": request.name,
        "project_id": request.project_id or defaults.default_project_id,
        "secret_environment_variables": [
            marshal_Secret(v, defaults) for v in request.secret_environment_variables
        ]
        if request.secret_environment_variables is not None
        else None,
    }


def marshal_CreateTokenRequest(
    request: CreateTokenRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "function_id",
                    request.function_id if request.function_id is not None else None,
                ),
                OneOfPossibility(
                    "namespace_id",
                    request.namespace_id if request.namespace_id is not None else None,
                ),
            ]
        ),
        "description": request.description,
        "expires_at": request.expires_at,
    }


def marshal_CreateTriggerRequest(
    request: CreateTriggerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "scw_sqs_config",
                    marshal_CreateTriggerRequestMnqSqsClientConfig(
                        request.scw_sqs_config, defaults
                    )
                    if request.scw_sqs_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "sqs_config",
                    marshal_CreateTriggerRequestSqsClientConfig(
                        request.sqs_config, defaults
                    )
                    if request.sqs_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "scw_nats_config",
                    marshal_CreateTriggerRequestMnqNatsClientConfig(
                        request.scw_nats_config, defaults
                    )
                    if request.scw_nats_config is not None
                    else None,
                ),
            ]
        ),
        "description": request.description,
        "function_id": request.function_id,
        "name": request.name,
    }


def marshal_UpdateCronRequest(
    request: UpdateCronRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "args": request.args,
        "function_id": request.function_id,
        "name": request.name,
        "schedule": request.schedule,
    }


def marshal_UpdateFunctionRequest(
    request: UpdateFunctionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "environment_variables": request.environment_variables,
        "handler": request.handler,
        "http_option": FunctionHttpOption(request.http_option),
        "max_scale": request.max_scale,
        "memory_limit": request.memory_limit,
        "min_scale": request.min_scale,
        "privacy": FunctionPrivacy(request.privacy),
        "redeploy": request.redeploy,
        "runtime": FunctionRuntime(request.runtime),
        "secret_environment_variables": [
            marshal_Secret(v, defaults) for v in request.secret_environment_variables
        ]
        if request.secret_environment_variables is not None
        else None,
        "timeout": request.timeout,
    }


def marshal_UpdateNamespaceRequest(
    request: UpdateNamespaceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "environment_variables": request.environment_variables,
        "secret_environment_variables": [
            marshal_Secret(v, defaults) for v in request.secret_environment_variables
        ]
        if request.secret_environment_variables is not None
        else None,
    }


def marshal_UpdateTriggerRequest(
    request: UpdateTriggerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "sqs_config",
                    marshal_UpdateTriggerRequestSqsClientConfig(
                        request.sqs_config, defaults
                    )
                    if request.sqs_config is not None
                    else None,
                ),
            ]
        ),
        "description": request.description,
        "name": request.name,
    }
