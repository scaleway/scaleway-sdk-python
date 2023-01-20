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
    ContainerHttpOption,
    ContainerPrivacy,
    ContainerProtocol,
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
    SecretHashedValue,
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


def unmarshal_Container(data: Any) -> Container:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Container' failed as data isn't a dictionary."
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

    field = data.get("http_option")
    args["http_option"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("max_concurrency")
    args["max_concurrency"] = field

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

    field = data.get("port")
    args["port"] = field

    field = data.get("privacy")
    args["privacy"] = field

    field = data.get("protocol")
    args["protocol"] = field

    field = data.get("region")
    args["region"] = field

    field = data.get("registry_image")
    args["registry_image"] = field

    field = data.get("secret_environment_variables")
    args["secret_environment_variables"] = [
        unmarshal_SecretHashedValue(v) for v in data["secret_environment_variables"]
    ]

    field = data.get("status")
    args["status"] = field

    field = data.get("timeout")
    args["timeout"] = field

    return Container(**args)


def unmarshal_Cron(data: Any) -> Cron:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Cron' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("args")
    args["args"] = field

    field = data.get("container_id")
    args["container_id"] = field

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

    field = data.get("container_id")
    args["container_id"] = field

    field = data.get("error_message")
    args["error_message"] = field

    field = data.get("hostname")
    args["hostname"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("url")
    args["url"] = field

    return Domain(**args)


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


def unmarshal_Token(data: Any) -> Token:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Token' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("container_id")
    args["container_id"] = field

    field = data.get("description")
    args["description"] = field

    field = data.get("expires_at")
    args["expires_at"] = parser.isoparse(field) if type(field) is str else field

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


def unmarshal_ListContainersResponse(data: Any) -> ListContainersResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListContainersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("containers")
    args["containers"] = [unmarshal_Container(v) for v in data["containers"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListContainersResponse(**args)


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


def marshal_Secret(
    request: Secret,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "key": request.key,
        "value": request.value,
    }


def marshal_CreateContainerRequest(
    request: CreateContainerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "environment_variables": request.environment_variables,
        "http_option": ContainerHttpOption(request.http_option),
        "max_concurrency": request.max_concurrency,
        "max_scale": request.max_scale,
        "memory_limit": request.memory_limit,
        "min_scale": request.min_scale,
        "name": request.name,
        "namespace_id": request.namespace_id,
        "port": request.port,
        "privacy": ContainerPrivacy(request.privacy),
        "protocol": ContainerProtocol(request.protocol),
        "registry_image": request.registry_image,
        "secret_environment_variables": [
            marshal_Secret(v, defaults) for v in request.secret_environment_variables
        ]
        if request.secret_environment_variables is not None
        else None,
        "timeout": request.timeout,
    }


def marshal_CreateCronRequest(
    request: CreateCronRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "args": request.args,
        "container_id": request.container_id,
        "name": request.name,
        "schedule": request.schedule,
    }


def marshal_CreateDomainRequest(
    request: CreateDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "container_id": request.container_id,
        "hostname": request.hostname,
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
                OneOfPossibility("container_id", request.container_id),
                OneOfPossibility("namespace_id", request.namespace_id),
            ]
        ),
        "description": request.description,
        "expires_at": request.expires_at,
    }


def marshal_UpdateContainerRequest(
    request: UpdateContainerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "environment_variables": request.environment_variables,
        "http_option": ContainerHttpOption(request.http_option),
        "max_concurrency": request.max_concurrency,
        "max_scale": request.max_scale,
        "memory_limit": request.memory_limit,
        "min_scale": request.min_scale,
        "port": request.port,
        "privacy": ContainerPrivacy(request.privacy),
        "protocol": ContainerProtocol(request.protocol),
        "redeploy": request.redeploy,
        "registry_image": request.registry_image,
        "secret_environment_variables": [
            marshal_Secret(v, defaults) for v in request.secret_environment_variables
        ]
        if request.secret_environment_variables is not None
        else None,
        "timeout": request.timeout,
    }


def marshal_UpdateCronRequest(
    request: UpdateCronRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "args": request.args,
        "container_id": request.container_id,
        "name": request.name,
        "schedule": request.schedule,
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
