# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from decimal import Decimal
from datetime import datetime
from typing import Any, Dict, List, Optional
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
    unmarshal_Money,
    marshal_Money,
    marshal_ScwFile,
    marshal_ServiceInfo,
    marshal_TimeSeries,
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    CronStatus,
    DomainStatus,
    FunctionHttpOption,
    FunctionPrivacy,
    FunctionRuntime,
    FunctionSandbox,
    FunctionStatus,
    ListCronsRequestOrderBy,
    ListDomainsRequestOrderBy,
    ListFunctionsRequestOrderBy,
    ListNamespacesRequestOrderBy,
    ListTokensRequestOrderBy,
    ListTriggersRequestOrderBy,
    NamespaceStatus,
    RuntimeStatus,
    TokenStatus,
    TriggerInputType,
    TriggerStatus,
    Cron,
    Domain,
    SecretHashedValue,
    Function,
    Namespace,
    Token,
    TriggerMnqNatsClientConfig,
    TriggerMnqSqsClientConfig,
    TriggerSqsClientConfig,
    Trigger,
    DownloadURL,
    ListCronsResponse,
    ListDomainsResponse,
    Runtime,
    ListFunctionRuntimesResponse,
    ListFunctionsResponse,
    ListNamespacesResponse,
    ListTokensResponse,
    ListTriggersResponse,
    UploadURL,
    CreateCronRequest,
    CreateDomainRequest,
    Secret,
    CreateFunctionRequest,
    CreateNamespaceRequest,
    CreateTokenRequest,
    CreateTriggerRequestMnqNatsClientConfig,
    CreateTriggerRequestMnqSqsClientConfig,
    CreateTriggerRequestSqsClientConfig,
    CreateTriggerRequest,
    UpdateCronRequest,
    UpdateFunctionRequest,
    UpdateNamespaceRequest,
    UpdateTriggerRequestSqsClientConfig,
    UpdateTriggerRequest,
)

def unmarshal_Cron(data: Any) -> Cron:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Cron' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("function_id", str())
    args["function_id"] = field

    field = data.get("schedule", str())
    args["schedule"] = field

    field = data.get("status", getattr(CronStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("args", None)
    args["args"] = field

    return Cron(**args)

def unmarshal_Domain(data: Any) -> Domain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Domain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("hostname", str())
    args["hostname"] = field

    field = data.get("function_id", str())
    args["function_id"] = field

    field = data.get("url", str())
    args["url"] = field

    field = data.get("status", getattr(DomainStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("error_message", None)
    args["error_message"] = field

    return Domain(**args)

def unmarshal_SecretHashedValue(data: Any) -> SecretHashedValue:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecretHashedValue' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("key", str())
    args["key"] = field

    field = data.get("hashed_value", str())
    args["hashed_value"] = field

    return SecretHashedValue(**args)

def unmarshal_Function(data: Any) -> Function:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Function' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("namespace_id", str())
    args["namespace_id"] = field

    field = data.get("status", getattr(FunctionStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("environment_variables", {})
    args["environment_variables"] = field

    field = data.get("min_scale", 0)
    args["min_scale"] = field

    field = data.get("max_scale", 0)
    args["max_scale"] = field

    field = data.get("runtime", getattr(FunctionRuntime, "UNKNOWN_RUNTIME"))
    args["runtime"] = field

    field = data.get("memory_limit", 0)
    args["memory_limit"] = field

    field = data.get("cpu_limit", 0)
    args["cpu_limit"] = field

    field = data.get("handler", str())
    args["handler"] = field

    field = data.get("privacy", getattr(FunctionPrivacy, "UNKNOWN_PRIVACY"))
    args["privacy"] = field

    field = data.get("domain_name", str())
    args["domain_name"] = field

    field = data.get("secret_environment_variables", [])
    args["secret_environment_variables"] = [unmarshal_SecretHashedValue(v) for v in field] if field is not None else None

    field = data.get("timeout", None)
    args["timeout"] = field

    field = data.get("error_message", None)
    args["error_message"] = field

    field = data.get("build_message", None)
    args["build_message"] = field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("http_option", getattr(FunctionHttpOption, "UNKNOWN_HTTP_OPTION"))
    args["http_option"] = field

    field = data.get("runtime_message", str())
    args["runtime_message"] = field

    field = data.get("sandbox", getattr(FunctionSandbox, "UNKNOWN_SANDBOX"))
    args["sandbox"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("ready_at", None)
    args["ready_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("private_network_id", None)
    args["private_network_id"] = field

    return Function(**args)

def unmarshal_Namespace(data: Any) -> Namespace:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Namespace' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("environment_variables", {})
    args["environment_variables"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("status", getattr(NamespaceStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("registry_namespace_id", str())
    args["registry_namespace_id"] = field

    field = data.get("error_message", None)
    args["error_message"] = field

    field = data.get("registry_endpoint", str())
    args["registry_endpoint"] = field

    field = data.get("secret_environment_variables", [])
    args["secret_environment_variables"] = [unmarshal_SecretHashedValue(v) for v in field] if field is not None else None

    field = data.get("region", )
    args["region"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("vpc_integration_activated", None)
    args["vpc_integration_activated"] = field

    return Namespace(**args)

def unmarshal_Token(data: Any) -> Token:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Token' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("token", str())
    args["token"] = field

    field = data.get("status", getattr(TokenStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("function_id", None)
    args["function_id"] = field

    field = data.get("namespace_id", None)
    args["namespace_id"] = field

    field = data.get("public_key", None)
    args["public_key"] = field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Token(**args)

def unmarshal_TriggerMnqNatsClientConfig(data: Any) -> TriggerMnqNatsClientConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TriggerMnqNatsClientConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("subject", str())
    args["subject"] = field

    field = data.get("mnq_nats_account_id", str())
    args["mnq_nats_account_id"] = field

    field = data.get("mnq_project_id", str())
    args["mnq_project_id"] = field

    field = data.get("mnq_region", str())
    args["mnq_region"] = field

    field = data.get("mnq_credential_id", None)
    args["mnq_credential_id"] = field

    return TriggerMnqNatsClientConfig(**args)

def unmarshal_TriggerMnqSqsClientConfig(data: Any) -> TriggerMnqSqsClientConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TriggerMnqSqsClientConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("queue", str())
    args["queue"] = field

    field = data.get("mnq_project_id", str())
    args["mnq_project_id"] = field

    field = data.get("mnq_region", str())
    args["mnq_region"] = field

    field = data.get("mnq_credential_id", None)
    args["mnq_credential_id"] = field

    return TriggerMnqSqsClientConfig(**args)

def unmarshal_TriggerSqsClientConfig(data: Any) -> TriggerSqsClientConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TriggerSqsClientConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("endpoint", str())
    args["endpoint"] = field

    field = data.get("queue_url", str())
    args["queue_url"] = field

    field = data.get("access_key", str())
    args["access_key"] = field

    field = data.get("secret_key", str())
    args["secret_key"] = field

    return TriggerSqsClientConfig(**args)

def unmarshal_Trigger(data: Any) -> Trigger:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Trigger' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("function_id", str())
    args["function_id"] = field

    field = data.get("input_type", getattr(TriggerInputType, "UNKNOWN_INPUT_TYPE"))
    args["input_type"] = field

    field = data.get("status", getattr(TriggerStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("error_message", None)
    args["error_message"] = field

    field = data.get("scw_sqs_config", None)
    args["scw_sqs_config"] = unmarshal_TriggerMnqSqsClientConfig(field) if field is not None else None

    field = data.get("scw_nats_config", None)
    args["scw_nats_config"] = unmarshal_TriggerMnqNatsClientConfig(field) if field is not None else None

    field = data.get("sqs_config", None)
    args["sqs_config"] = unmarshal_TriggerSqsClientConfig(field) if field is not None else None

    return Trigger(**args)

def unmarshal_DownloadURL(data: Any) -> DownloadURL:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DownloadURL' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("url", str())
    args["url"] = field

    field = data.get("headers", str())
    args["headers"] = field

    return DownloadURL(**args)

def unmarshal_ListCronsResponse(data: Any) -> ListCronsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListCronsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("crons", [])
    args["crons"] = [unmarshal_Cron(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListCronsResponse(**args)

def unmarshal_ListDomainsResponse(data: Any) -> ListDomainsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDomainsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domains", [])
    args["domains"] = [unmarshal_Domain(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListDomainsResponse(**args)

def unmarshal_Runtime(data: Any) -> Runtime:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Runtime' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("language", str())
    args["language"] = field

    field = data.get("version", str())
    args["version"] = field

    field = data.get("default_handler", str())
    args["default_handler"] = field

    field = data.get("code_sample", str())
    args["code_sample"] = field

    field = data.get("status", str())
    args["status"] = field

    field = data.get("status_message", str())
    args["status_message"] = field

    field = data.get("extension", str())
    args["extension"] = field

    field = data.get("implementation", str())
    args["implementation"] = field

    field = data.get("logo_url", str())
    args["logo_url"] = field

    return Runtime(**args)

def unmarshal_ListFunctionRuntimesResponse(data: Any) -> ListFunctionRuntimesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListFunctionRuntimesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("runtimes", [])
    args["runtimes"] = [unmarshal_Runtime(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListFunctionRuntimesResponse(**args)

def unmarshal_ListFunctionsResponse(data: Any) -> ListFunctionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListFunctionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("functions", [])
    args["functions"] = [unmarshal_Function(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListFunctionsResponse(**args)

def unmarshal_ListNamespacesResponse(data: Any) -> ListNamespacesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNamespacesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("namespaces", [])
    args["namespaces"] = [unmarshal_Namespace(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListNamespacesResponse(**args)

def unmarshal_ListTokensResponse(data: Any) -> ListTokensResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTokensResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("tokens", str())
    args["tokens"] = [unmarshal_Token(v) for v in field] if field is not None else None

    field = data.get("total_count", str())
    args["total_count"] = field

    return ListTokensResponse(**args)

def unmarshal_ListTriggersResponse(data: Any) -> ListTriggersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTriggersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("triggers", [])
    args["triggers"] = [unmarshal_Trigger(v) for v in field] if field is not None else None

    return ListTriggersResponse(**args)

def unmarshal_UploadURL(data: Any) -> UploadURL:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UploadURL' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("url", str())
    args["url"] = field

    field = data.get("headers", {})
    args["headers"] = field

    return UploadURL(**args)

def marshal_CreateCronRequest(
    request: CreateCronRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.function_id is not None:
        output["function_id"] = request.function_id
    else:
        output["function_id"] = str()

    if request.schedule is not None:
        output["schedule"] = request.schedule
    else:
        output["schedule"] = str()

    if request.args is not None:
        output["args"] = request.args
    else:
        output["args"] = None

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None


    return output

def marshal_CreateDomainRequest(
    request: CreateDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.hostname is not None:
        output["hostname"] = request.hostname
    else:
        output["hostname"] = str()

    if request.function_id is not None:
        output["function_id"] = request.function_id
    else:
        output["function_id"] = str()


    return output

def marshal_Secret(
    request: Secret,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.key is not None:
        output["key"] = request.key
    else:
        output["key"] = str()

    if request.value is not None:
        output["value"] = request.value
    else:
        output["value"] = None


    return output

def marshal_CreateFunctionRequest(
    request: CreateFunctionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.namespace_id is not None:
        output["namespace_id"] = request.namespace_id
    else:
        output["namespace_id"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.environment_variables is not None:
        output["environment_variables"] = request.environment_variables
    else:
        output["environment_variables"] = None

    if request.min_scale is not None:
        output["min_scale"] = request.min_scale
    else:
        output["min_scale"] = None

    if request.max_scale is not None:
        output["max_scale"] = request.max_scale
    else:
        output["max_scale"] = None

    if request.runtime is not None:
        output["runtime"] = str(request.runtime)
    else:
        output["runtime"] = None

    if request.memory_limit is not None:
        output["memory_limit"] = request.memory_limit
    else:
        output["memory_limit"] = None

    if request.timeout is not None:
        output["timeout"] = request.timeout
    else:
        output["timeout"] = None

    if request.handler is not None:
        output["handler"] = request.handler
    else:
        output["handler"] = None

    if request.privacy is not None:
        output["privacy"] = str(request.privacy)
    else:
        output["privacy"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.secret_environment_variables is not None:
        output["secret_environment_variables"] = [marshal_Secret(item, defaults) for item in request.secret_environment_variables]
    else:
        output["secret_environment_variables"] = None

    if request.http_option is not None:
        output["http_option"] = str(request.http_option)
    else:
        output["http_option"] = None

    if request.sandbox is not None:
        output["sandbox"] = str(request.sandbox)
    else:
        output["sandbox"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id
    else:
        output["private_network_id"] = None


    return output

def marshal_CreateNamespaceRequest(
    request: CreateNamespaceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.activate_vpc_integration is not None:
        output["activate_vpc_integration"] = request.activate_vpc_integration
    else:
        output["activate_vpc_integration"] = False

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.environment_variables is not None:
        output["environment_variables"] = request.environment_variables
    else:
        output["environment_variables"] = None

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.secret_environment_variables is not None:
        output["secret_environment_variables"] = [marshal_Secret(item, defaults) for item in request.secret_environment_variables]
    else:
        output["secret_environment_variables"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_CreateTokenRequest(
    request: CreateTokenRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="function_id", value=request.function_id,marshal_func=None
            ),
            OneOfPossibility(param="namespace_id", value=request.namespace_id,marshal_func=None
            ),
        ]),
    )

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()
    else:
        output["expires_at"] = None


    return output

def marshal_CreateTriggerRequestMnqNatsClientConfig(
    request: CreateTriggerRequestMnqNatsClientConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.subject is not None:
        output["subject"] = request.subject
    else:
        output["subject"] = str()

    if request.mnq_nats_account_id is not None:
        output["mnq_nats_account_id"] = request.mnq_nats_account_id
    else:
        output["mnq_nats_account_id"] = str()

    if request.mnq_project_id is not None:
        output["mnq_project_id"] = request.mnq_project_id
    else:
        output["mnq_project_id"] = str()

    if request.mnq_region is not None:
        output["mnq_region"] = request.mnq_region
    else:
        output["mnq_region"] = str()


    return output

def marshal_CreateTriggerRequestMnqSqsClientConfig(
    request: CreateTriggerRequestMnqSqsClientConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.queue is not None:
        output["queue"] = request.queue
    else:
        output["queue"] = str()

    if request.mnq_project_id is not None:
        output["mnq_project_id"] = request.mnq_project_id
    else:
        output["mnq_project_id"] = str()

    if request.mnq_region is not None:
        output["mnq_region"] = request.mnq_region
    else:
        output["mnq_region"] = str()


    return output

def marshal_CreateTriggerRequestSqsClientConfig(
    request: CreateTriggerRequestSqsClientConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.endpoint is not None:
        output["endpoint"] = request.endpoint
    else:
        output["endpoint"] = str()

    if request.queue_url is not None:
        output["queue_url"] = request.queue_url
    else:
        output["queue_url"] = str()

    if request.access_key is not None:
        output["access_key"] = request.access_key
    else:
        output["access_key"] = str()

    if request.secret_key is not None:
        output["secret_key"] = request.secret_key
    else:
        output["secret_key"] = str()


    return output

def marshal_CreateTriggerRequest(
    request: CreateTriggerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="scw_sqs_config", value=request.scw_sqs_config,marshal_func=marshal_CreateTriggerRequestMnqSqsClientConfig
            ),
            OneOfPossibility(param="scw_nats_config", value=request.scw_nats_config,marshal_func=marshal_CreateTriggerRequestMnqNatsClientConfig
            ),
            OneOfPossibility(param="sqs_config", value=request.sqs_config,marshal_func=marshal_CreateTriggerRequestSqsClientConfig
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.function_id is not None:
        output["function_id"] = request.function_id
    else:
        output["function_id"] = str()

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None


    return output

def marshal_UpdateCronRequest(
    request: UpdateCronRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.function_id is not None:
        output["function_id"] = request.function_id
    else:
        output["function_id"] = None

    if request.schedule is not None:
        output["schedule"] = request.schedule
    else:
        output["schedule"] = None

    if request.args is not None:
        output["args"] = request.args
    else:
        output["args"] = None

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None


    return output

def marshal_UpdateFunctionRequest(
    request: UpdateFunctionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.environment_variables is not None:
        output["environment_variables"] = request.environment_variables
    else:
        output["environment_variables"] = None

    if request.min_scale is not None:
        output["min_scale"] = request.min_scale
    else:
        output["min_scale"] = None

    if request.max_scale is not None:
        output["max_scale"] = request.max_scale
    else:
        output["max_scale"] = None

    if request.runtime is not None:
        output["runtime"] = str(request.runtime)
    else:
        output["runtime"] = None

    if request.memory_limit is not None:
        output["memory_limit"] = request.memory_limit
    else:
        output["memory_limit"] = None

    if request.timeout is not None:
        output["timeout"] = request.timeout
    else:
        output["timeout"] = None

    if request.redeploy is not None:
        output["redeploy"] = request.redeploy
    else:
        output["redeploy"] = None

    if request.handler is not None:
        output["handler"] = request.handler
    else:
        output["handler"] = None

    if request.privacy is not None:
        output["privacy"] = str(request.privacy)
    else:
        output["privacy"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.secret_environment_variables is not None:
        output["secret_environment_variables"] = [marshal_Secret(item, defaults) for item in request.secret_environment_variables]
    else:
        output["secret_environment_variables"] = None

    if request.http_option is not None:
        output["http_option"] = str(request.http_option)
    else:
        output["http_option"] = None

    if request.sandbox is not None:
        output["sandbox"] = str(request.sandbox)
    else:
        output["sandbox"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id
    else:
        output["private_network_id"] = None


    return output

def marshal_UpdateNamespaceRequest(
    request: UpdateNamespaceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.environment_variables is not None:
        output["environment_variables"] = request.environment_variables
    else:
        output["environment_variables"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.secret_environment_variables is not None:
        output["secret_environment_variables"] = [marshal_Secret(item, defaults) for item in request.secret_environment_variables]
    else:
        output["secret_environment_variables"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_UpdateTriggerRequestSqsClientConfig(
    request: UpdateTriggerRequestSqsClientConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.access_key is not None:
        output["access_key"] = request.access_key
    else:
        output["access_key"] = None

    if request.secret_key is not None:
        output["secret_key"] = request.secret_key
    else:
        output["secret_key"] = None


    return output

def marshal_UpdateTriggerRequest(
    request: UpdateTriggerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="sqs_config", value=request.sqs_config,marshal_func=marshal_UpdateTriggerRequestSqsClientConfig
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None


    return output
