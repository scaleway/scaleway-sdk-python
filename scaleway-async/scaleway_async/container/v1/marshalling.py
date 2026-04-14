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
    ContainerPrivacy,
    ContainerProtocol,
    ContainerSandbox,
    ContainerStatus,
    DomainStatus,
    NamespaceStatus,
    TriggerDestinationConfigHttpMethod,
    TriggerSourceType,
    TriggerStatus,
    ContainerProbeHTTPProbe,
    ContainerProbeTCPProbe,
    ContainerProbe,
    ContainerScalingOption,
    Container,
    Domain,
    Namespace,
    TriggerCronConfig,
    TriggerDestinationConfig,
    TriggerNATSConfig,
    TriggerSQSConfig,
    Trigger,
    ListContainersResponse,
    ListDomainsResponse,
    ListNamespacesResponse,
    ListTriggersResponse,
    CreateContainerRequest,
    CreateDomainRequest,
    CreateNamespaceRequest,
    CreateTriggerRequestCronConfig,
    CreateTriggerRequestDestinationConfig,
    CreateTriggerRequestNATSConfig,
    CreateTriggerRequestSQSConfig,
    CreateTriggerRequest,
    UpdateContainerRequestProbeHTTPProbe,
    UpdateContainerRequestProbeTCPProbe,
    UpdateContainerRequestProbe,
    UpdateContainerRequest,
    UpdateDomainRequest,
    UpdateNamespaceRequest,
    UpdateTriggerRequestCronConfig,
    UpdateTriggerRequestDestinationConfig,
    UpdateTriggerRequestNATSConfig,
    UpdateTriggerRequestSQSConfig,
    UpdateTriggerRequest,
)


def unmarshal_ContainerProbeHTTPProbe(data: Any) -> ContainerProbeHTTPProbe:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContainerProbeHTTPProbe' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("path", None)
    if field is not None:
        args["path"] = field
    else:
        args["path"] = None

    return ContainerProbeHTTPProbe(**args)


def unmarshal_ContainerProbeTCPProbe(data: Any) -> ContainerProbeTCPProbe:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContainerProbeTCPProbe' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return ContainerProbeTCPProbe(**args)


def unmarshal_ContainerProbe(data: Any) -> ContainerProbe:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContainerProbe' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("failure_threshold", None)
    if field is not None:
        args["failure_threshold"] = field
    else:
        args["failure_threshold"] = 0

    field = data.get("interval", None)
    if field is not None:
        args["interval"] = field
    else:
        args["interval"] = None

    field = data.get("timeout", None)
    if field is not None:
        args["timeout"] = field
    else:
        args["timeout"] = None

    field = data.get("tcp", None)
    if field is not None:
        args["tcp"] = unmarshal_ContainerProbeTCPProbe(field)
    else:
        args["tcp"] = None

    field = data.get("http", None)
    if field is not None:
        args["http"] = unmarshal_ContainerProbeHTTPProbe(field)
    else:
        args["http"] = None

    return ContainerProbe(**args)


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
        args["concurrent_requests_threshold"] = 0

    field = data.get("cpu_usage_threshold", None)
    if field is not None:
        args["cpu_usage_threshold"] = field
    else:
        args["cpu_usage_threshold"] = 0

    field = data.get("memory_usage_threshold", None)
    if field is not None:
        args["memory_usage_threshold"] = field
    else:
        args["memory_usage_threshold"] = 0

    return ContainerScalingOption(**args)


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

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = ContainerStatus.UNKNOWN_STATUS

    field = data.get("environment_variables", None)
    if field is not None:
        args["environment_variables"] = field
    else:
        args["environment_variables"] = {}

    field = data.get("secret_environment_variables", None)
    if field is not None:
        args["secret_environment_variables"] = field
    else:
        args["secret_environment_variables"] = {}

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

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

    field = data.get("memory_limit_bytes", None)
    if field is not None:
        args["memory_limit_bytes"] = field
    else:
        args["memory_limit_bytes"] = 0

    field = data.get("mvcpu_limit", None)
    if field is not None:
        args["mvcpu_limit"] = field
    else:
        args["mvcpu_limit"] = 0

    field = data.get("local_storage_limit_bytes", None)
    if field is not None:
        args["local_storage_limit_bytes"] = field
    else:
        args["local_storage_limit_bytes"] = 0

    field = data.get("privacy", None)
    if field is not None:
        args["privacy"] = field
    else:
        args["privacy"] = ContainerPrivacy.UNKNOWN_PRIVACY

    field = data.get("image", None)
    if field is not None:
        args["image"] = field
    else:
        args["image"] = None

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

    field = data.get("https_connections_only", None)
    if field is not None:
        args["https_connections_only"] = field
    else:
        args["https_connections_only"] = False

    field = data.get("timeout", None)
    if field is not None:
        args["timeout"] = field
    else:
        args["timeout"] = None

    field = data.get("sandbox", None)
    if field is not None:
        args["sandbox"] = field
    else:
        args["sandbox"] = ContainerSandbox.UNKNOWN_SANDBOX

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

    field = data.get("public_endpoint", None)
    if field is not None:
        args["public_endpoint"] = field
    else:
        args["public_endpoint"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("scaling_option", None)
    if field is not None:
        args["scaling_option"] = unmarshal_ContainerScalingOption(field)
    else:
        args["scaling_option"] = None

    field = data.get("liveness_probe", None)
    if field is not None:
        args["liveness_probe"] = unmarshal_ContainerProbe(field)
    else:
        args["liveness_probe"] = None

    field = data.get("startup_probe", None)
    if field is not None:
        args["startup_probe"] = unmarshal_ContainerProbe(field)
    else:
        args["startup_probe"] = None

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field
    else:
        args["private_network_id"] = None

    return Container(**args)


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

    field = data.get("container_id", None)
    if field is not None:
        args["container_id"] = field
    else:
        args["container_id"] = None

    field = data.get("hostname", None)
    if field is not None:
        args["hostname"] = field
    else:
        args["hostname"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DomainStatus.UNKNOWN_STATUS

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

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

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = NamespaceStatus.UNKNOWN_STATUS

    field = data.get("environment_variables", None)
    if field is not None:
        args["environment_variables"] = field
    else:
        args["environment_variables"] = {}

    field = data.get("secret_environment_variables", None)
    if field is not None:
        args["secret_environment_variables"] = field
    else:
        args["secret_environment_variables"] = {}

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

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


def unmarshal_TriggerCronConfig(data: Any) -> TriggerCronConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TriggerCronConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("schedule", None)
    if field is not None:
        args["schedule"] = field
    else:
        args["schedule"] = None

    field = data.get("timezone", None)
    if field is not None:
        args["timezone"] = field
    else:
        args["timezone"] = None

    field = data.get("body", None)
    if field is not None:
        args["body"] = field
    else:
        args["body"] = None

    field = data.get("headers", None)
    if field is not None:
        args["headers"] = field
    else:
        args["headers"] = {}

    return TriggerCronConfig(**args)


def unmarshal_TriggerDestinationConfig(data: Any) -> TriggerDestinationConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TriggerDestinationConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("http_path", None)
    if field is not None:
        args["http_path"] = field
    else:
        args["http_path"] = None

    field = data.get("http_method", None)
    if field is not None:
        args["http_method"] = field
    else:
        args["http_method"] = TriggerDestinationConfigHttpMethod.UNKNOWN_HTTP_METHOD

    return TriggerDestinationConfig(**args)


def unmarshal_TriggerNATSConfig(data: Any) -> TriggerNATSConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TriggerNATSConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("server_urls", None)
    if field is not None:
        args["server_urls"] = field
    else:
        args["server_urls"] = []

    field = data.get("subject", None)
    if field is not None:
        args["subject"] = field
    else:
        args["subject"] = None

    return TriggerNATSConfig(**args)


def unmarshal_TriggerSQSConfig(data: Any) -> TriggerSQSConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TriggerSQSConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("endpoint", None)
    if field is not None:
        args["endpoint"] = field
    else:
        args["endpoint"] = None

    field = data.get("access_key_id", None)
    if field is not None:
        args["access_key_id"] = field
    else:
        args["access_key_id"] = None

    field = data.get("queue_url", None)
    if field is not None:
        args["queue_url"] = field
    else:
        args["queue_url"] = None

    return TriggerSQSConfig(**args)


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

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

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

    field = data.get("container_id", None)
    if field is not None:
        args["container_id"] = field
    else:
        args["container_id"] = None

    field = data.get("source_type", None)
    if field is not None:
        args["source_type"] = field
    else:
        args["source_type"] = TriggerSourceType.UNKNOWN_SOURCE_TYPE

    field = data.get("destination_config", None)
    if field is not None:
        args["destination_config"] = unmarshal_TriggerDestinationConfig(field)
    else:
        args["destination_config"] = None

    field = data.get("cron_config", None)
    if field is not None:
        args["cron_config"] = unmarshal_TriggerCronConfig(field)
    else:
        args["cron_config"] = None

    field = data.get("sqs_config", None)
    if field is not None:
        args["sqs_config"] = unmarshal_TriggerSQSConfig(field)
    else:
        args["sqs_config"] = None

    field = data.get("nats_config", None)
    if field is not None:
        args["nats_config"] = unmarshal_TriggerNATSConfig(field)
    else:
        args["nats_config"] = None

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
        args["containers"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    return ListContainersResponse(**args)


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
        args["domains"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

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
        args["namespaces"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    return ListNamespacesResponse(**args)


def unmarshal_ListTriggersResponse(data: Any) -> ListTriggersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTriggersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("triggers", None)
    if field is not None:
        args["triggers"] = (
            [unmarshal_Trigger(v) for v in field] if field is not None else None
        )
    else:
        args["triggers"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    return ListTriggersResponse(**args)


def marshal_ContainerProbeHTTPProbe(
    request: ContainerProbeHTTPProbe,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.path is not None:
        output["path"] = request.path

    return output


def marshal_ContainerProbeTCPProbe(
    request: ContainerProbeTCPProbe,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    return output


def marshal_ContainerProbe(
    request: ContainerProbe,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="tcp",
                    value=request.tcp,
                    marshal_func=marshal_ContainerProbeTCPProbe,
                ),
                OneOfPossibility(
                    param="http",
                    value=request.http,
                    marshal_func=marshal_ContainerProbeHTTPProbe,
                ),
            ]
        ),
    )

    if request.failure_threshold is not None:
        output["failure_threshold"] = request.failure_threshold

    if request.interval is not None:
        output["interval"] = request.interval

    if request.timeout is not None:
        output["timeout"] = request.timeout

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
        output["environment_variables"] = {
            key: value for key, value in request.environment_variables.items()
        }

    if request.secret_environment_variables is not None:
        output["secret_environment_variables"] = {
            key: value for key, value in request.secret_environment_variables.items()
        }

    if request.min_scale is not None:
        output["min_scale"] = request.min_scale

    if request.max_scale is not None:
        output["max_scale"] = request.max_scale

    if request.memory_limit_bytes is not None:
        output["memory_limit_bytes"] = request.memory_limit_bytes

    if request.mvcpu_limit is not None:
        output["mvcpu_limit"] = request.mvcpu_limit

    if request.timeout is not None:
        output["timeout"] = request.timeout

    if request.privacy is not None:
        output["privacy"] = request.privacy

    if request.description is not None:
        output["description"] = request.description

    if request.image is not None:
        output["image"] = request.image

    if request.protocol is not None:
        output["protocol"] = request.protocol

    if request.port is not None:
        output["port"] = request.port

    if request.https_connections_only is not None:
        output["https_connections_only"] = request.https_connections_only

    if request.sandbox is not None:
        output["sandbox"] = request.sandbox

    if request.local_storage_limit_bytes is not None:
        output["local_storage_limit_bytes"] = request.local_storage_limit_bytes

    if request.scaling_option is not None:
        output["scaling_option"] = marshal_ContainerScalingOption(
            request.scaling_option, defaults
        )

    if request.liveness_probe is not None:
        output["liveness_probe"] = marshal_ContainerProbe(
            request.liveness_probe, defaults
        )

    if request.startup_probe is not None:
        output["startup_probe"] = marshal_ContainerProbe(
            request.startup_probe, defaults
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


def marshal_CreateDomainRequest(
    request: CreateDomainRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.container_id is not None:
        output["container_id"] = request.container_id

    if request.hostname is not None:
        output["hostname"] = request.hostname

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreateNamespaceRequest(
    request: CreateNamespaceRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.description is not None:
        output["description"] = request.description

    if request.environment_variables is not None:
        output["environment_variables"] = {
            key: value for key, value in request.environment_variables.items()
        }

    if request.secret_environment_variables is not None:
        output["secret_environment_variables"] = {
            key: value for key, value in request.secret_environment_variables.items()
        }

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreateTriggerRequestCronConfig(
    request: CreateTriggerRequestCronConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.schedule is not None:
        output["schedule"] = request.schedule

    if request.timezone is not None:
        output["timezone"] = request.timezone

    if request.body is not None:
        output["body"] = request.body

    if request.headers is not None:
        output["headers"] = {key: value for key, value in request.headers.items()}

    return output


def marshal_CreateTriggerRequestDestinationConfig(
    request: CreateTriggerRequestDestinationConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.http_path is not None:
        output["http_path"] = request.http_path

    if request.http_method is not None:
        output["http_method"] = request.http_method

    return output


def marshal_CreateTriggerRequestNATSConfig(
    request: CreateTriggerRequestNATSConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.server_urls is not None:
        output["server_urls"] = request.server_urls

    if request.subject is not None:
        output["subject"] = request.subject

    if request.credentials_file_content is not None:
        output["credentials_file_content"] = request.credentials_file_content

    return output


def marshal_CreateTriggerRequestSQSConfig(
    request: CreateTriggerRequestSQSConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.region is not None:
        output["region"] = request.region
    else:
        output["region"] = defaults.default_region

    if request.endpoint is not None:
        output["endpoint"] = request.endpoint

    if request.access_key_id is not None:
        output["access_key_id"] = request.access_key_id

    if request.secret_access_key is not None:
        output["secret_access_key"] = request.secret_access_key

    if request.queue_url is not None:
        output["queue_url"] = request.queue_url

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
                    param="cron_config",
                    value=request.cron_config,
                    marshal_func=marshal_CreateTriggerRequestCronConfig,
                ),
                OneOfPossibility(
                    param="sqs_config",
                    value=request.sqs_config,
                    marshal_func=marshal_CreateTriggerRequestSQSConfig,
                ),
                OneOfPossibility(
                    param="nats_config",
                    value=request.nats_config,
                    marshal_func=marshal_CreateTriggerRequestNATSConfig,
                ),
            ]
        ),
    )

    if request.container_id is not None:
        output["container_id"] = request.container_id

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.tags is not None:
        output["tags"] = request.tags

    if request.destination_config is not None:
        output["destination_config"] = marshal_CreateTriggerRequestDestinationConfig(
            request.destination_config, defaults
        )

    return output


def marshal_UpdateContainerRequestProbeHTTPProbe(
    request: UpdateContainerRequestProbeHTTPProbe,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.path is not None:
        output["path"] = request.path

    return output


def marshal_UpdateContainerRequestProbeTCPProbe(
    request: UpdateContainerRequestProbeTCPProbe,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    return output


def marshal_UpdateContainerRequestProbe(
    request: UpdateContainerRequestProbe,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="http",
                    value=request.http,
                    marshal_func=marshal_UpdateContainerRequestProbeHTTPProbe,
                ),
                OneOfPossibility(
                    param="tcp",
                    value=request.tcp,
                    marshal_func=marshal_UpdateContainerRequestProbeTCPProbe,
                ),
            ]
        ),
    )

    if request.failure_threshold is not None:
        output["failure_threshold"] = request.failure_threshold

    if request.interval is not None:
        output["interval"] = request.interval

    if request.timeout is not None:
        output["timeout"] = request.timeout

    return output


def marshal_UpdateContainerRequest(
    request: UpdateContainerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.environment_variables is not None:
        output["environment_variables"] = request.environment_variables

    if request.secret_environment_variables is not None:
        output["secret_environment_variables"] = request.secret_environment_variables

    if request.min_scale is not None:
        output["min_scale"] = request.min_scale

    if request.max_scale is not None:
        output["max_scale"] = request.max_scale

    if request.memory_limit_bytes is not None:
        output["memory_limit_bytes"] = request.memory_limit_bytes

    if request.mvcpu_limit is not None:
        output["mvcpu_limit"] = request.mvcpu_limit

    if request.timeout is not None:
        output["timeout"] = request.timeout

    if request.privacy is not None:
        output["privacy"] = request.privacy

    if request.description is not None:
        output["description"] = request.description

    if request.image is not None:
        output["image"] = request.image

    if request.protocol is not None:
        output["protocol"] = request.protocol

    if request.port is not None:
        output["port"] = request.port

    if request.https_connection_only is not None:
        output["https_connection_only"] = request.https_connection_only

    if request.sandbox is not None:
        output["sandbox"] = request.sandbox

    if request.local_storage_limit_bytes is not None:
        output["local_storage_limit_bytes"] = request.local_storage_limit_bytes

    if request.scaling_option is not None:
        output["scaling_option"] = marshal_ContainerScalingOption(
            request.scaling_option, defaults
        )

    if request.liveness_probe is not None:
        output["liveness_probe"] = marshal_ContainerProbe(
            request.liveness_probe, defaults
        )

    if request.startup_probe is not None:
        output["startup_probe"] = marshal_UpdateContainerRequestProbe(
            request.startup_probe, defaults
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


def marshal_UpdateDomainRequest(
    request: UpdateDomainRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateNamespaceRequest(
    request: UpdateNamespaceRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.environment_variables is not None:
        output["environment_variables"] = request.environment_variables

    if request.secret_environment_variables is not None:
        output["secret_environment_variables"] = request.secret_environment_variables

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateTriggerRequestCronConfig(
    request: UpdateTriggerRequestCronConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.schedule is not None:
        output["schedule"] = request.schedule

    if request.timezone is not None:
        output["timezone"] = request.timezone

    if request.body is not None:
        output["body"] = request.body

    if request.headers is not None:
        output["headers"] = request.headers

    return output


def marshal_UpdateTriggerRequestDestinationConfig(
    request: UpdateTriggerRequestDestinationConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.http_path is not None:
        output["http_path"] = request.http_path

    if request.http_method is not None:
        output["http_method"] = request.http_method

    return output


def marshal_UpdateTriggerRequestNATSConfig(
    request: UpdateTriggerRequestNATSConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.server_urls is not None:
        output["server_urls"] = request.server_urls

    if request.subject is not None:
        output["subject"] = request.subject

    if request.credentials_file_content is not None:
        output["credentials_file_content"] = request.credentials_file_content

    return output


def marshal_UpdateTriggerRequestSQSConfig(
    request: UpdateTriggerRequestSQSConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.region is not None:
        output["region"] = request.region

    if request.endpoint is not None:
        output["endpoint"] = request.endpoint

    if request.access_key_id is not None:
        output["access_key_id"] = request.access_key_id

    if request.secret_access_key is not None:
        output["secret_access_key"] = request.secret_access_key

    if request.queue_url is not None:
        output["queue_url"] = request.queue_url

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
                    param="cron_config",
                    value=request.cron_config,
                    marshal_func=marshal_UpdateTriggerRequestCronConfig,
                ),
                OneOfPossibility(
                    param="sqs_config",
                    value=request.sqs_config,
                    marshal_func=marshal_UpdateTriggerRequestSQSConfig,
                ),
                OneOfPossibility(
                    param="nats_config",
                    value=request.nats_config,
                    marshal_func=marshal_UpdateTriggerRequestNATSConfig,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.tags is not None:
        output["tags"] = request.tags

    if request.destination_config is not None:
        output["destination_config"] = marshal_UpdateTriggerRequestDestinationConfig(
            request.destination_config, defaults
        )

    return output
