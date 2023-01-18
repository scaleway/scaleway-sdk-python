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
    TriggerType,
    CreateTriggerInputRequestNatsClientConfigSpec,
    CreateTriggerInputRequestSqsClientConfigSpec,
    CreateTriggerRequestNatsFailureHandlingPolicy,
    CreateTriggerRequestNatsFailureHandlingPolicyNatsDeadLetter,
    CreateTriggerRequestNatsFailureHandlingPolicyRetryPolicy,
    CreateTriggerRequestNatsFailureHandlingPolicySqsDeadLetter,
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
    Runtime,
    Secret,
    SecretHashedValue,
    SetTriggerInputsRequestNatsConfigs,
    SetTriggerInputsRequestSqsConfigs,
    SetTriggerInputsResponse,
    Token,
    Trigger,
    TriggerInput,
    TriggerInputNatsClientConfig,
    TriggerInputSqsClientConfig,
    TriggerNatsDeadLetter,
    TriggerNatsFailureHandlingPolicy,
    TriggerRetryPolicy,
    TriggerSqsDeadLetter,
    TriggerSqsFailureHandlingPolicy,
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


def unmarshal_TriggerNatsDeadLetter(data: Any) -> TriggerNatsDeadLetter:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'TriggerNatsDeadLetter' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("mnq_namespace_id")
    args["mnq_namespace_id"] = field

    field = data.get("subject")
    args["subject"] = field

    return TriggerNatsDeadLetter(**args)


def unmarshal_TriggerRetryPolicy(data: Any) -> TriggerRetryPolicy:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'TriggerRetryPolicy' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("max_retries")
    args["max_retries"] = field

    field = data.get("retry_period")
    args["retry_period"] = field

    return TriggerRetryPolicy(**args)


def unmarshal_TriggerSqsDeadLetter(data: Any) -> TriggerSqsDeadLetter:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'TriggerSqsDeadLetter' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("mnq_namespace_id")
    args["mnq_namespace_id"] = field

    field = data.get("queue")
    args["queue"] = field

    return TriggerSqsDeadLetter(**args)


def unmarshal_SecretHashedValue(data: Any) -> SecretHashedValue:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SecretHashedValue' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("hashed_value")
    args["hashed_value"] = field

    field = data.get("key")
    args["key"] = field

    return SecretHashedValue(**args)


def unmarshal_TriggerInputNatsClientConfig(data: Any) -> TriggerInputNatsClientConfig:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'TriggerInputNatsClientConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("subject")
    args["subject"] = field

    return TriggerInputNatsClientConfig(**args)


def unmarshal_TriggerInputSqsClientConfig(data: Any) -> TriggerInputSqsClientConfig:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'TriggerInputSqsClientConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("queue")
    args["queue"] = field

    return TriggerInputSqsClientConfig(**args)


def unmarshal_TriggerNatsFailureHandlingPolicy(
    data: Any,
) -> TriggerNatsFailureHandlingPolicy:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'TriggerNatsFailureHandlingPolicy' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("nats_dead_letter")
    args["nats_dead_letter"] = (
        unmarshal_TriggerNatsDeadLetter(field) if field is not None else None
    )

    field = data.get("retry_policy")
    args["retry_policy"] = (
        unmarshal_TriggerRetryPolicy(field) if field is not None else None
    )

    field = data.get("sqs_dead_letter")
    args["sqs_dead_letter"] = (
        unmarshal_TriggerSqsDeadLetter(field) if field is not None else None
    )

    return TriggerNatsFailureHandlingPolicy(**args)


def unmarshal_TriggerSqsFailureHandlingPolicy(
    data: Any,
) -> TriggerSqsFailureHandlingPolicy:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'TriggerSqsFailureHandlingPolicy' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return TriggerSqsFailureHandlingPolicy(**args)


def unmarshal_Cron(data: Any) -> Cron:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Cron' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("args")
    args["args"] = field

    field = data.get("function_id")
    args["function_id"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("schedule")
    args["schedule"] = field

    field = data.get("status")
    args["status"] = field

    return Cron(**args)


def unmarshal_Domain(data: Any) -> Domain:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Domain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("error_message")
    args["error_message"] = field

    field = data.get("function_id")
    args["function_id"] = field

    field = data.get("hostname")
    args["hostname"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("url")
    args["url"] = field

    return Domain(**args)


def unmarshal_Function(data: Any) -> Function:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Function' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("cpu_limit")
    args["cpu_limit"] = field

    field = data.get("description")
    args["description"] = field

    field = data.get("domain_name")
    args["domain_name"] = field

    field = data.get("environment_variables")
    args["environment_variables"] = field

    field = data.get("error_message")
    args["error_message"] = field

    field = data.get("handler")
    args["handler"] = field

    field = data.get("http_option")
    args["http_option"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("max_scale")
    args["max_scale"] = field

    field = data.get("memory_limit")
    args["memory_limit"] = field

    field = data.get("min_scale")
    args["min_scale"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("namespace_id")
    args["namespace_id"] = field

    field = data.get("privacy")
    args["privacy"] = field

    field = data.get("region")
    args["region"] = field

    field = data.get("runtime")
    args["runtime"] = field

    field = data.get("runtime_message")
    args["runtime_message"] = field

    field = data.get("secret_environment_variables")
    args["secret_environment_variables"] = [
        unmarshal_SecretHashedValue(v) for v in data["secret_environment_variables"]
    ]

    field = data.get("status")
    args["status"] = field

    field = data.get("timeout")
    args["timeout"] = field

    return Function(**args)


def unmarshal_Log(data: Any) -> Log:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Log' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id")
    args["id"] = field

    field = data.get("level")
    args["level"] = field

    field = data.get("message")
    args["message"] = field

    field = data.get("source")
    args["source"] = field

    field = data.get("stream")
    args["stream"] = field

    field = data.get("timestamp")
    args["timestamp"] = parser.isoparse(field) if type(field) is str else field

    return Log(**args)


def unmarshal_Namespace(data: Any) -> Namespace:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Namespace' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description")
    args["description"] = field

    field = data.get("environment_variables")
    args["environment_variables"] = field

    field = data.get("error_message")
    args["error_message"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("region")
    args["region"] = field

    field = data.get("registry_endpoint")
    args["registry_endpoint"] = field

    field = data.get("registry_namespace_id")
    args["registry_namespace_id"] = field

    field = data.get("secret_environment_variables")
    args["secret_environment_variables"] = [
        unmarshal_SecretHashedValue(v) for v in data["secret_environment_variables"]
    ]

    field = data.get("status")
    args["status"] = field

    return Namespace(**args)


def unmarshal_Runtime(data: Any) -> Runtime:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Runtime' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("code_sample")
    args["code_sample"] = field

    field = data.get("default_handler")
    args["default_handler"] = field

    field = data.get("extension")
    args["extension"] = field

    field = data.get("implementation")
    args["implementation"] = field

    field = data.get("language")
    args["language"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("status_message")
    args["status_message"] = field

    field = data.get("version")
    args["version"] = field

    return Runtime(**args)


def unmarshal_Token(data: Any) -> Token:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Token' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description")
    args["description"] = field

    field = data.get("expires_at")
    args["expires_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("function_id")
    args["function_id"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("namespace_id")
    args["namespace_id"] = field

    field = data.get("public_key")
    args["public_key"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("token")
    args["token"] = field

    return Token(**args)


def unmarshal_Trigger(data: Any) -> Trigger:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Trigger' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description")
    args["description"] = field

    field = data.get("error_message")
    args["error_message"] = field

    field = data.get("function_id")
    args["function_id"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("nats_failure_handling_policy")
    args["nats_failure_handling_policy"] = (
        unmarshal_TriggerNatsFailureHandlingPolicy(field) if field is not None else None
    )

    field = data.get("sqs_failure_handling_policy")
    args["sqs_failure_handling_policy"] = (
        unmarshal_TriggerSqsFailureHandlingPolicy(field) if field is not None else None
    )

    field = data.get("status")
    args["status"] = field

    field = data.get("type_")
    args["type_"] = field

    return Trigger(**args)


def unmarshal_TriggerInput(data: Any) -> TriggerInput:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'TriggerInput' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("error_message")
    args["error_message"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("mnq_namespace_id")
    args["mnq_namespace_id"] = field

    field = data.get("nats_config")
    args["nats_config"] = (
        unmarshal_TriggerInputNatsClientConfig(field) if field is not None else None
    )

    field = data.get("sqs_config")
    args["sqs_config"] = (
        unmarshal_TriggerInputSqsClientConfig(field) if field is not None else None
    )

    field = data.get("status")
    args["status"] = field

    return TriggerInput(**args)


def unmarshal_DownloadURL(data: Any) -> DownloadURL:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DownloadURL' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("headers")
    args["headers"] = field

    field = data.get("url")
    args["url"] = field

    return DownloadURL(**args)


def unmarshal_ListCronsResponse(data: Any) -> ListCronsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListCronsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("crons")
    args["crons"] = [unmarshal_Cron(v) for v in data["crons"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListCronsResponse(**args)


def unmarshal_ListDomainsResponse(data: Any) -> ListDomainsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDomainsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domains")
    args["domains"] = [unmarshal_Domain(v) for v in data["domains"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListDomainsResponse(**args)


def unmarshal_ListFunctionRuntimesResponse(data: Any) -> ListFunctionRuntimesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListFunctionRuntimesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("runtimes")
    args["runtimes"] = [unmarshal_Runtime(v) for v in data["runtimes"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListFunctionRuntimesResponse(**args)


def unmarshal_ListFunctionsResponse(data: Any) -> ListFunctionsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListFunctionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("functions")
    args["functions"] = [unmarshal_Function(v) for v in data["functions"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListFunctionsResponse(**args)


def unmarshal_ListLogsResponse(data: Any) -> ListLogsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListLogsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("logs")
    args["logs"] = [unmarshal_Log(v) for v in data["logs"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListLogsResponse(**args)


def unmarshal_ListNamespacesResponse(data: Any) -> ListNamespacesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListNamespacesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("namespaces")
    args["namespaces"] = [unmarshal_Namespace(v) for v in data["namespaces"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListNamespacesResponse(**args)


def unmarshal_ListTokensResponse(data: Any) -> ListTokensResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListTokensResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("tokens")
    args["tokens"] = [unmarshal_Token(v) for v in data["tokens"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListTokensResponse(**args)


def unmarshal_ListTriggerInputsResponse(data: Any) -> ListTriggerInputsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListTriggerInputsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("inputs")
    args["inputs"] = [unmarshal_TriggerInput(v) for v in data["inputs"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListTriggerInputsResponse(**args)


def unmarshal_ListTriggersResponse(data: Any) -> ListTriggersResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListTriggersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count")
    args["total_count"] = field

    field = data.get("triggers")
    args["triggers"] = [unmarshal_Trigger(v) for v in data["triggers"]]

    return ListTriggersResponse(**args)


def unmarshal_SetTriggerInputsResponse(data: Any) -> SetTriggerInputsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SetTriggerInputsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("trigger_inputs")
    args["trigger_inputs"] = [unmarshal_TriggerInput(v) for v in data["trigger_inputs"]]

    return SetTriggerInputsResponse(**args)


def unmarshal_UploadURL(data: Any) -> UploadURL:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'UploadURL' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("headers")
    args["headers"] = field

    field = data.get("url")
    args["url"] = field

    return UploadURL(**args)


def marshal_CreateTriggerInputRequestNatsClientConfigSpec(
    request: CreateTriggerInputRequestNatsClientConfigSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "subject": request.subject,
    }


def marshal_CreateTriggerInputRequestSqsClientConfigSpec(
    request: CreateTriggerInputRequestSqsClientConfigSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "queue": request.queue,
    }


def marshal_CreateTriggerRequestNatsFailureHandlingPolicyNatsDeadLetter(
    request: CreateTriggerRequestNatsFailureHandlingPolicyNatsDeadLetter,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "mnq_namespace_id": request.mnq_namespace_id,
        "subject": request.subject,
    }


def marshal_CreateTriggerRequestNatsFailureHandlingPolicyRetryPolicy(
    request: CreateTriggerRequestNatsFailureHandlingPolicyRetryPolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "max_retries": request.max_retries,
        "retry_period": request.retry_period,
    }


def marshal_CreateTriggerRequestNatsFailureHandlingPolicySqsDeadLetter(
    request: CreateTriggerRequestNatsFailureHandlingPolicySqsDeadLetter,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "mnq_namespace_id": request.mnq_namespace_id,
        "queue": request.queue,
    }


def marshal_CreateTriggerRequestNatsFailureHandlingPolicy(
    request: CreateTriggerRequestNatsFailureHandlingPolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("nats_dead_letter", request.nats_dead_letter),
                OneOfPossibility("sqs_dead_letter", request.sqs_dead_letter),
            ]
        ),
        "retry_policy": marshal_CreateTriggerRequestNatsFailureHandlingPolicyRetryPolicy(
            request.retry_policy, defaults
        )
        if request.retry_policy is not None
        else None,
    }


def marshal_CreateTriggerRequestSqsFailureHandlingPolicy(
    request: CreateTriggerRequestSqsFailureHandlingPolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {}


def marshal_Secret(
    request: Secret,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "key": request.key,
        "value": request.value,
    }


def marshal_SetTriggerInputsRequestNatsConfigs(
    request: SetTriggerInputsRequestNatsConfigs,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "configs": [
            marshal_CreateTriggerInputRequestNatsClientConfigSpec(v, defaults)
            for v in request.configs
        ],
    }


def marshal_SetTriggerInputsRequestSqsConfigs(
    request: SetTriggerInputsRequestSqsConfigs,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "configs": [
            marshal_CreateTriggerInputRequestSqsClientConfigSpec(v, defaults)
            for v in request.configs
        ],
    }


def marshal_UpdateTriggerInputRequestNatsClientConfigSpec(
    request: UpdateTriggerInputRequestNatsClientConfigSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "subject": request.subject,
    }


def marshal_UpdateTriggerInputRequestSqsClientConfigSpec(
    request: UpdateTriggerInputRequestSqsClientConfigSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "queue": request.queue,
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
                OneOfPossibility("function_id", request.function_id),
                OneOfPossibility("namespace_id", request.namespace_id),
            ]
        ),
        "description": request.description,
        "expires_at": request.expires_at,
    }


def marshal_CreateTriggerInputRequest(
    request: CreateTriggerInputRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("nats_config", request.nats_config),
                OneOfPossibility("sqs_config", request.sqs_config),
            ]
        ),
        "mnq_namespace_id": request.mnq_namespace_id,
        "trigger_id": request.trigger_id,
    }


def marshal_CreateTriggerRequest(
    request: CreateTriggerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "nats_failure_handling_policy", request.nats_failure_handling_policy
                ),
                OneOfPossibility(
                    "sqs_failure_handling_policy", request.sqs_failure_handling_policy
                ),
            ]
        ),
        "description": request.description,
        "function_id": request.function_id,
        "name": request.name,
        "type": TriggerType(request.type_),
    }


def marshal_SetTriggerInputsRequest(
    request: SetTriggerInputsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("sqs", request.sqs),
                OneOfPossibility("nats", request.nats),
            ]
        ),
        "trigger_input_id": request.trigger_input_id,
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


def marshal_UpdateTriggerInputRequest(
    request: UpdateTriggerInputRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("nats_config", request.nats_config),
                OneOfPossibility("sqs_config", request.sqs_config),
            ]
        ),
    }


def marshal_UpdateTriggerRequest(
    request: UpdateTriggerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("nats_config", request.nats_config),
                OneOfPossibility("sqs_config", request.sqs_config),
            ]
        ),
        "description": request.description,
        "name": request.name,
    }
