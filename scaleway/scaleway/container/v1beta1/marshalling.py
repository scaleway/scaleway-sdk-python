# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    ContainerHttpOption,
    ContainerPrivacy,
    ContainerProtocol,
    ContainerSandbox,
    ContainerStatus,
    CronStatus,
    DomainStatus,
    NamespaceStatus,
    TokenStatus,
    TriggerInputType,
    TriggerStatus,
    ContainerHealthCheckSpecHTTPProbe,
    ContainerHealthCheckSpecTCPProbe,
    ContainerHealthCheckSpec,
    ContainerScalingOption,
    SecretHashedValue,
    Container,
    Cron,
    Domain,
    Namespace,
    Token,
    TriggerMnqNatsClientConfig,
    TriggerMnqSqsClientConfig,
    TriggerSqsClientConfig,
    Trigger,
    ListContainersResponse,
    ListCronsResponse,
    ListDomainsResponse,
    ListNamespacesResponse,
    ListTokensResponse,
    ListTriggersResponse,
    Secret,
    CreateContainerRequest,
    CreateCronRequest,
    CreateDomainRequest,
    CreateNamespaceRequest,
    CreateTokenRequest,
    CreateTriggerRequestMnqNatsClientConfig,
    CreateTriggerRequestMnqSqsClientConfig,
    CreateTriggerRequestSqsClientConfig,
    CreateTriggerRequest,
    UpdateContainerRequest,
    UpdateCronRequest,
    UpdateNamespaceRequest,
    UpdateTriggerRequestSqsClientConfig,
    UpdateTriggerRequest,
)


def unmarshal_ContainerHealthCheckSpecHTTPProbe(
    data: Any,
) -> ContainerHealthCheckSpecHTTPProbe:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContainerHealthCheckSpecHTTPProbe' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("path", None)
    if field is not None:
        args["path"] = field
    else:
        args["path"] = None

    return ContainerHealthCheckSpecHTTPProbe(**args)


def unmarshal_ContainerHealthCheckSpecTCPProbe(
    data: Any,
) -> ContainerHealthCheckSpecTCPProbe:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContainerHealthCheckSpecTCPProbe' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return ContainerHealthCheckSpecTCPProbe(**args)


def unmarshal_ContainerHealthCheckSpec(data: Any) -> ContainerHealthCheckSpec:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContainerHealthCheckSpec' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("failure_threshold", None)
    if field is not None:
        args["failure_threshold"] = field
    else:
        args["failure_threshold"] = 0

    field = data.get("http", None)
    if field is not None:
        args["http"] = unmarshal_ContainerHealthCheckSpecHTTPProbe(field)
    else:
        args["http"] = None

    field = data.get("tcp", None)
    if field is not None:
        args["tcp"] = unmarshal_ContainerHealthCheckSpecTCPProbe(field)
    else:
        args["tcp"] = None

    field = data.get("interval", None)
    if field is not None:
        args["interval"] = field
    else:
        args["interval"] = None

    return ContainerHealthCheckSpec(**args)


def unmarshal_ContainerScalingOption(data: Any) -> ContainerScalingOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContainerScalingOption' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("concurrent_requests_threshold", None)
    if field is not None:
        args["concurrent_requests_threshold"] = field
    else:
        args["concurrent_requests_threshold"] = None

    field = data.get("cpu_usage_threshold", None)
    if field is not None:
        args["cpu_usage_threshold"] = field
    else:
        args["cpu_usage_threshold"] = None

    field = data.get("memory_usage_threshold", None)
    if field is not None:
        args["memory_usage_threshold"] = field
    else:
        args["memory_usage_threshold"] = None

    return ContainerScalingOption(**args)


def unmarshal_SecretHashedValue(data: Any) -> SecretHashedValue:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecretHashedValue' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("key", None)
    if field is not None:
        args["key"] = field
    else:
        args["key"] = None

    field = data.get("hashed_value", None)
    if field is not None:
        args["hashed_value"] = field
    else:
        args["hashed_value"] = None

    return SecretHashedValue(**args)


def unmarshal_Container(data: Any) -> Container:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Container' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("namespace_id", None)
    if field is not None:
        args["namespace_id"] = field
    else:
        args["namespace_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = ContainerStatus.UNKNOWN

    field = data.get("environment_variables", None)
    if field is not None:
        args["environment_variables"] = field
    else:
        args["environment_variables"] = {}

    field = data.get("min_scale", None)
    if field is not None:
        args["min_scale"] = field
    else:
        args["min_scale"] = 0

    field = data.get("max_scale", None)
    if field is not None:
        args["max_scale"] = field
    else:
        args["max_scale"] = 0

    field = data.get("memory_limit", None)
    if field is not None:
        args["memory_limit"] = field
    else:
        args["memory_limit"] = 0

    field = data.get("cpu_limit", None)
    if field is not None:
        args["cpu_limit"] = field
    else:
        args["cpu_limit"] = 0

    field = data.get("privacy", None)
    if field is not None:
        args["privacy"] = field
    else:
        args["privacy"] = ContainerPrivacy.UNKNOWN_PRIVACY

    field = data.get("registry_image", None)
    if field is not None:
        args["registry_image"] = field
    else:
        args["registry_image"] = None

    field = data.get("max_concurrency", None)
    if field is not None:
        args["max_concurrency"] = field
    else:
        args["max_concurrency"] = 0

    field = data.get("domain_name", None)
    if field is not None:
        args["domain_name"] = field
    else:
        args["domain_name"] = None

    field = data.get("timeout", None)
    if field is not None:
        args["timeout"] = field
    else:
        args["timeout"] = None

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("protocol", None)
    if field is not None:
        args["protocol"] = field
    else:
        args["protocol"] = ContainerProtocol.UNKNOWN_PROTOCOL

    field = data.get("port", None)
    if field is not None:
        args["port"] = field
    else:
        args["port"] = 0

    field = data.get("secret_environment_variables", None)
    if field is not None:
        args["secret_environment_variables"] = (
            [unmarshal_SecretHashedValue(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["secret_environment_variables"] = []

    field = data.get("http_option", None)
    if field is not None:
        args["http_option"] = field
    else:
        args["http_option"] = ContainerHttpOption.UNKNOWN_HTTP_OPTION

    field = data.get("sandbox", None)
    if field is not None:
        args["sandbox"] = field
    else:
        args["sandbox"] = ContainerSandbox.UNKNOWN_SANDBOX

    field = data.get("local_storage_limit", None)
    if field is not None:
        args["local_storage_limit"] = field
    else:
        args["local_storage_limit"] = 0

    field = data.get("scaling_option", None)
    if field is not None:
        args["scaling_option"] = unmarshal_ContainerScalingOption(field)
    else:
        args["scaling_option"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("command", None)
    if field is not None:
        args["command"] = field
    else:
        args["command"] = []

    field = data.get("args", None)
    if field is not None:
        args["args"] = field
    else:
        args["args"] = []

    field = data.get("health_check", None)
    if field is not None:
        args["health_check"] = unmarshal_ContainerHealthCheckSpec(field)
    else:
        args["health_check"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("ready_at", None)
    if field is not None:
        args["ready_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["ready_at"] = None

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field
    else:
        args["private_network_id"] = None

    return Container(**args)


def unmarshal_Cron(data: Any) -> Cron:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Cron' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("container_id", None)
    if field is not None:
        args["container_id"] = field
    else:
        args["container_id"] = None

    field = data.get("schedule", None)
    if field is not None:
        args["schedule"] = field
    else:
        args["schedule"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = CronStatus.UNKNOWN

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("args", None)
    if field is not None:
        args["args"] = field
    else:
        args["args"] = {}

    return Cron(**args)


def unmarshal_Domain(data: Any) -> Domain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Domain' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("hostname", None)
    if field is not None:
        args["hostname"] = field
    else:
        args["hostname"] = None

    field = data.get("container_id", None)
    if field is not None:
        args["container_id"] = field
    else:
        args["container_id"] = None

    field = data.get("url", None)
    if field is not None:
        args["url"] = field
    else:
        args["url"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DomainStatus.UNKNOWN

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

    return Domain(**args)


def unmarshal_Namespace(data: Any) -> Namespace:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Namespace' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("environment_variables", None)
    if field is not None:
        args["environment_variables"] = field
    else:
        args["environment_variables"] = {}

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = NamespaceStatus.UNKNOWN

    field = data.get("registry_namespace_id", None)
    if field is not None:
        args["registry_namespace_id"] = field
    else:
        args["registry_namespace_id"] = None

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

    field = data.get("registry_endpoint", None)
    if field is not None:
        args["registry_endpoint"] = field
    else:
        args["registry_endpoint"] = None

    field = data.get("secret_environment_variables", None)
    if field is not None:
        args["secret_environment_variables"] = (
            [unmarshal_SecretHashedValue(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["secret_environment_variables"] = []

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("vpc_integration_activated", None)
    if field is not None:
        args["vpc_integration_activated"] = field
    else:
        args["vpc_integration_activated"] = False

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return Namespace(**args)


def unmarshal_Token(data: Any) -> Token:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Token' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("token", None)
    if field is not None:
        args["token"] = field
    else:
        args["token"] = None

    field = data.get("public_key", None)
    if field is not None:
        args["public_key"] = field
    else:
        args["public_key"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = TokenStatus.UNKNOWN

    field = data.get("container_id", None)
    if field is not None:
        args["container_id"] = field
    else:
        args["container_id"] = None

    field = data.get("namespace_id", None)
    if field is not None:
        args["namespace_id"] = field
    else:
        args["namespace_id"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("expires_at", None)
    if field is not None:
        args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["expires_at"] = None

    return Token(**args)


def unmarshal_TriggerMnqNatsClientConfig(data: Any) -> TriggerMnqNatsClientConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TriggerMnqNatsClientConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("subject", None)
    if field is not None:
        args["subject"] = field
    else:
        args["subject"] = None

    field = data.get("mnq_nats_account_id", None)
    if field is not None:
        args["mnq_nats_account_id"] = field
    else:
        args["mnq_nats_account_id"] = None

    field = data.get("mnq_project_id", None)
    if field is not None:
        args["mnq_project_id"] = field
    else:
        args["mnq_project_id"] = None

    field = data.get("mnq_region", None)
    if field is not None:
        args["mnq_region"] = field
    else:
        args["mnq_region"] = None

    field = data.get("mnq_credential_id", None)
    if field is not None:
        args["mnq_credential_id"] = field
    else:
        args["mnq_credential_id"] = None

    return TriggerMnqNatsClientConfig(**args)


def unmarshal_TriggerMnqSqsClientConfig(data: Any) -> TriggerMnqSqsClientConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TriggerMnqSqsClientConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("queue", None)
    if field is not None:
        args["queue"] = field
    else:
        args["queue"] = None

    field = data.get("mnq_project_id", None)
    if field is not None:
        args["mnq_project_id"] = field
    else:
        args["mnq_project_id"] = None

    field = data.get("mnq_region", None)
    if field is not None:
        args["mnq_region"] = field
    else:
        args["mnq_region"] = None

    field = data.get("mnq_credential_id", None)
    if field is not None:
        args["mnq_credential_id"] = field
    else:
        args["mnq_credential_id"] = None

    return TriggerMnqSqsClientConfig(**args)


def unmarshal_TriggerSqsClientConfig(data: Any) -> TriggerSqsClientConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TriggerSqsClientConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("endpoint", None)
    if field is not None:
        args["endpoint"] = field
    else:
        args["endpoint"] = None

    field = data.get("queue_url", None)
    if field is not None:
        args["queue_url"] = field
    else:
        args["queue_url"] = None

    field = data.get("access_key", None)
    if field is not None:
        args["access_key"] = field
    else:
        args["access_key"] = None

    field = data.get("secret_key", None)
    if field is not None:
        args["secret_key"] = field
    else:
        args["secret_key"] = None

    return TriggerSqsClientConfig(**args)


def unmarshal_Trigger(data: Any) -> Trigger:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Trigger' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("container_id", None)
    if field is not None:
        args["container_id"] = field
    else:
        args["container_id"] = None

    field = data.get("input_type", None)
    if field is not None:
        args["input_type"] = field
    else:
        args["input_type"] = TriggerInputType.UNKNOWN_INPUT_TYPE

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = TriggerStatus.UNKNOWN_STATUS

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

    field = data.get("scw_sqs_config", None)
    if field is not None:
        args["scw_sqs_config"] = unmarshal_TriggerMnqSqsClientConfig(field)
    else:
        args["scw_sqs_config"] = None

    field = data.get("scw_nats_config", None)
    if field is not None:
        args["scw_nats_config"] = unmarshal_TriggerMnqNatsClientConfig(field)
    else:
        args["scw_nats_config"] = None

    field = data.get("sqs_config", None)
    if field is not None:
        args["sqs_config"] = unmarshal_TriggerSqsClientConfig(field)
    else:
        args["sqs_config"] = None

    return Trigger(**args)


def unmarshal_ListContainersResponse(data: Any) -> ListContainersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListContainersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("containers", None)
    if field is not None:
        args["containers"] = (
            [unmarshal_Container(v) for v in field] if field is not None else None
        )
    else:
        args["containers"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListContainersResponse(**args)


def unmarshal_ListCronsResponse(data: Any) -> ListCronsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListCronsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("crons", None)
    if field is not None:
        args["crons"] = (
            [unmarshal_Cron(v) for v in field] if field is not None else None
        )
    else:
        args["crons"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListCronsResponse(**args)


def unmarshal_ListDomainsResponse(data: Any) -> ListDomainsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDomainsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("domains", None)
    if field is not None:
        args["domains"] = (
            [unmarshal_Domain(v) for v in field] if field is not None else None
        )
    else:
        args["domains"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListDomainsResponse(**args)


def unmarshal_ListNamespacesResponse(data: Any) -> ListNamespacesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNamespacesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("namespaces", None)
    if field is not None:
        args["namespaces"] = (
            [unmarshal_Namespace(v) for v in field] if field is not None else None
        )
    else:
        args["namespaces"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListNamespacesResponse(**args)


def unmarshal_ListTokensResponse(data: Any) -> ListTokensResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTokensResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("tokens", None)
    if field is not None:
        args["tokens"] = (
            [unmarshal_Token(v) for v in field] if field is not None else None
        )
    else:
        args["tokens"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    return ListTokensResponse(**args)


def unmarshal_ListTriggersResponse(data: Any) -> ListTriggersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTriggersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("triggers", None)
    if field is not None:
        args["triggers"] = (
            [unmarshal_Trigger(v) for v in field] if field is not None else None
        )
    else:
        args["triggers"] = []

    return ListTriggersResponse(**args)


def marshal_ContainerHealthCheckSpecHTTPProbe(
    request: ContainerHealthCheckSpecHTTPProbe,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.path is not None:
        output["path"] = request.path

    return output


def marshal_ContainerHealthCheckSpecTCPProbe(
    request: ContainerHealthCheckSpecTCPProbe,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    return output


def marshal_ContainerHealthCheckSpec(
    request: ContainerHealthCheckSpec,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="http",
                    value=request.http,
                    marshal_func=marshal_ContainerHealthCheckSpecHTTPProbe,
                ),
                OneOfPossibility(
                    param="tcp",
                    value=request.tcp,
                    marshal_func=marshal_ContainerHealthCheckSpecTCPProbe,
                ),
            ]
        ),
    )

    if request.failure_threshold is not None:
        output["failure_threshold"] = request.failure_threshold

    if request.interval is not None:
        output["interval"] = request.interval

    return output


def marshal_ContainerScalingOption(
    request: ContainerScalingOption,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="concurrent_requests_threshold",
                    value=request.concurrent_requests_threshold,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="cpu_usage_threshold",
                    value=request.cpu_usage_threshold,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="memory_usage_threshold",
                    value=request.memory_usage_threshold,
                    marshal_func=None,
                ),
            ]
        ),
    )

    return output


def marshal_Secret(
    request: Secret,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.key is not None:
        output["key"] = request.key

    if request.value is not None:
        output["value"] = request.value

    return output


def marshal_CreateContainerRequest(
    request: CreateContainerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.namespace_id is not None:
        output["namespace_id"] = request.namespace_id

    if request.name is not None:
        output["name"] = request.name

    if request.environment_variables is not None:
        output["environment_variables"] = request.environment_variables

    if request.min_scale is not None:
        output["min_scale"] = request.min_scale

    if request.max_scale is not None:
        output["max_scale"] = request.max_scale

    if request.memory_limit is not None:
        output["memory_limit"] = request.memory_limit

    if request.cpu_limit is not None:
        output["cpu_limit"] = request.cpu_limit

    if request.timeout is not None:
        output["timeout"] = request.timeout

    if request.privacy is not None:
        output["privacy"] = request.privacy

    if request.description is not None:
        output["description"] = request.description

    if request.registry_image is not None:
        output["registry_image"] = request.registry_image

    if request.max_concurrency is not None:
        output["max_concurrency"] = request.max_concurrency

    if request.protocol is not None:
        output["protocol"] = request.protocol

    if request.port is not None:
        output["port"] = request.port

    if request.secret_environment_variables is not None:
        output["secret_environment_variables"] = [
            marshal_Secret(item, defaults)
            for item in request.secret_environment_variables
        ]

    if request.http_option is not None:
        output["http_option"] = request.http_option

    if request.sandbox is not None:
        output["sandbox"] = request.sandbox

    if request.local_storage_limit is not None:
        output["local_storage_limit"] = request.local_storage_limit

    if request.scaling_option is not None:
        output["scaling_option"] = marshal_ContainerScalingOption(
            request.scaling_option, defaults
        )

    if request.health_check is not None:
        output["health_check"] = marshal_ContainerHealthCheckSpec(
            request.health_check, defaults
        )

    if request.tags is not None:
        output["tags"] = request.tags

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    if request.command is not None:
        output["command"] = request.command

    if request.args is not None:
        output["args"] = request.args

    return output


def marshal_CreateCronRequest(
    request: CreateCronRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.container_id is not None:
        output["container_id"] = request.container_id

    if request.schedule is not None:
        output["schedule"] = request.schedule

    if request.args is not None:
        output["args"] = request.args

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_CreateDomainRequest(
    request: CreateDomainRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.hostname is not None:
        output["hostname"] = request.hostname

    if request.container_id is not None:
        output["container_id"] = request.container_id

    return output


def marshal_CreateNamespaceRequest(
    request: CreateNamespaceRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.activate_vpc_integration is not None:
        output["activate_vpc_integration"] = request.activate_vpc_integration

    if request.name is not None:
        output["name"] = request.name

    if request.environment_variables is not None:
        output["environment_variables"] = request.environment_variables

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.description is not None:
        output["description"] = request.description

    if request.secret_environment_variables is not None:
        output["secret_environment_variables"] = [
            marshal_Secret(item, defaults)
            for item in request.secret_environment_variables
        ]

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreateTokenRequest(
    request: CreateTokenRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="container_id", value=request.container_id, marshal_func=None
                ),
                OneOfPossibility(
                    param="namespace_id", value=request.namespace_id, marshal_func=None
                ),
            ]
        ),
    )

    if request.description is not None:
        output["description"] = request.description

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()

    return output


def marshal_CreateTriggerRequestMnqNatsClientConfig(
    request: CreateTriggerRequestMnqNatsClientConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.subject is not None:
        output["subject"] = request.subject

    if request.mnq_nats_account_id is not None:
        output["mnq_nats_account_id"] = request.mnq_nats_account_id

    if request.mnq_project_id is not None:
        output["mnq_project_id"] = request.mnq_project_id

    if request.mnq_region is not None:
        output["mnq_region"] = request.mnq_region

    return output


def marshal_CreateTriggerRequestMnqSqsClientConfig(
    request: CreateTriggerRequestMnqSqsClientConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.queue is not None:
        output["queue"] = request.queue

    if request.mnq_project_id is not None:
        output["mnq_project_id"] = request.mnq_project_id

    if request.mnq_region is not None:
        output["mnq_region"] = request.mnq_region

    return output


def marshal_CreateTriggerRequestSqsClientConfig(
    request: CreateTriggerRequestSqsClientConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.endpoint is not None:
        output["endpoint"] = request.endpoint

    if request.queue_url is not None:
        output["queue_url"] = request.queue_url

    if request.access_key is not None:
        output["access_key"] = request.access_key

    if request.secret_key is not None:
        output["secret_key"] = request.secret_key

    return output


def marshal_CreateTriggerRequest(
    request: CreateTriggerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="scw_sqs_config",
                    value=request.scw_sqs_config,
                    marshal_func=marshal_CreateTriggerRequestMnqSqsClientConfig,
                ),
                OneOfPossibility(
                    param="scw_nats_config",
                    value=request.scw_nats_config,
                    marshal_func=marshal_CreateTriggerRequestMnqNatsClientConfig,
                ),
                OneOfPossibility(
                    param="sqs_config",
                    value=request.sqs_config,
                    marshal_func=marshal_CreateTriggerRequestSqsClientConfig,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.container_id is not None:
        output["container_id"] = request.container_id

    if request.description is not None:
        output["description"] = request.description

    return output


def marshal_UpdateContainerRequest(
    request: UpdateContainerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.environment_variables is not None:
        output["environment_variables"] = request.environment_variables

    if request.min_scale is not None:
        output["min_scale"] = request.min_scale

    if request.max_scale is not None:
        output["max_scale"] = request.max_scale

    if request.memory_limit is not None:
        output["memory_limit"] = request.memory_limit

    if request.cpu_limit is not None:
        output["cpu_limit"] = request.cpu_limit

    if request.timeout is not None:
        output["timeout"] = request.timeout

    if request.redeploy is not None:
        output["redeploy"] = request.redeploy

    if request.privacy is not None:
        output["privacy"] = request.privacy

    if request.description is not None:
        output["description"] = request.description

    if request.registry_image is not None:
        output["registry_image"] = request.registry_image

    if request.max_concurrency is not None:
        output["max_concurrency"] = request.max_concurrency

    if request.protocol is not None:
        output["protocol"] = request.protocol

    if request.port is not None:
        output["port"] = request.port

    if request.secret_environment_variables is not None:
        output["secret_environment_variables"] = [
            marshal_Secret(item, defaults)
            for item in request.secret_environment_variables
        ]

    if request.http_option is not None:
        output["http_option"] = request.http_option

    if request.sandbox is not None:
        output["sandbox"] = request.sandbox

    if request.local_storage_limit is not None:
        output["local_storage_limit"] = request.local_storage_limit

    if request.scaling_option is not None:
        output["scaling_option"] = marshal_ContainerScalingOption(
            request.scaling_option, defaults
        )

    if request.health_check is not None:
        output["health_check"] = marshal_ContainerHealthCheckSpec(
            request.health_check, defaults
        )

    if request.tags is not None:
        output["tags"] = request.tags

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    if request.command is not None:
        output["command"] = request.command

    if request.args is not None:
        output["args"] = request.args

    return output


def marshal_UpdateCronRequest(
    request: UpdateCronRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.container_id is not None:
        output["container_id"] = request.container_id

    if request.schedule is not None:
        output["schedule"] = request.schedule

    if request.args is not None:
        output["args"] = request.args

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_UpdateNamespaceRequest(
    request: UpdateNamespaceRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.environment_variables is not None:
        output["environment_variables"] = request.environment_variables

    if request.description is not None:
        output["description"] = request.description

    if request.secret_environment_variables is not None:
        output["secret_environment_variables"] = [
            marshal_Secret(item, defaults)
            for item in request.secret_environment_variables
        ]

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateTriggerRequestSqsClientConfig(
    request: UpdateTriggerRequestSqsClientConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.access_key is not None:
        output["access_key"] = request.access_key

    if request.secret_key is not None:
        output["secret_key"] = request.secret_key

    return output


def marshal_UpdateTriggerRequest(
    request: UpdateTriggerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="sqs_config",
                    value=request.sqs_config,
                    marshal_func=marshal_UpdateTriggerRequestSqsClientConfig,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    return output
