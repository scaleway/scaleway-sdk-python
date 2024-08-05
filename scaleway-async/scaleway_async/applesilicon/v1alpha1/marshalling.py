# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    OS,
    ServerTypeCPU,
    ServerTypeDisk,
    ServerTypeGPU,
    ServerTypeMemory,
    ServerTypeNetwork,
    ServerType,
    Server,
    ListOSResponse,
    ListServerTypesResponse,
    ListServersResponse,
    CreateServerRequest,
    ReinstallServerRequest,
    UpdateServerRequest,
)


def unmarshal_OS(data: Any) -> OS:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OS' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("label", None)
    if field is not None:
        args["label"] = field

    field = data.get("image_url", None)
    if field is not None:
        args["image_url"] = field

    field = data.get("family", None)
    if field is not None:
        args["family"] = field

    field = data.get("is_beta", None)
    if field is not None:
        args["is_beta"] = field

    field = data.get("version", None)
    if field is not None:
        args["version"] = field

    field = data.get("xcode_version", None)
    if field is not None:
        args["xcode_version"] = field

    field = data.get("compatible_server_types", None)
    if field is not None:
        args["compatible_server_types"] = field

    return OS(**args)


def unmarshal_ServerTypeCPU(data: Any) -> ServerTypeCPU:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeCPU' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("core_count", None)
    if field is not None:
        args["core_count"] = field

    field = data.get("frequency", None)
    if field is not None:
        args["frequency"] = field

    return ServerTypeCPU(**args)


def unmarshal_ServerTypeDisk(data: Any) -> ServerTypeDisk:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeDisk' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("capacity", None)
    if field is not None:
        args["capacity"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    return ServerTypeDisk(**args)


def unmarshal_ServerTypeGPU(data: Any) -> ServerTypeGPU:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeGPU' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("count", None)
    if field is not None:
        args["count"] = field

    return ServerTypeGPU(**args)


def unmarshal_ServerTypeMemory(data: Any) -> ServerTypeMemory:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeMemory' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("capacity", None)
    if field is not None:
        args["capacity"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    return ServerTypeMemory(**args)


def unmarshal_ServerTypeNetwork(data: Any) -> ServerTypeNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("public_bandwidth_bps", None)
    if field is not None:
        args["public_bandwidth_bps"] = field

    return ServerTypeNetwork(**args)


def unmarshal_ServerType(data: Any) -> ServerType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("stock", None)
    if field is not None:
        args["stock"] = field

    field = data.get("cpu", None)
    if field is not None:
        args["cpu"] = unmarshal_ServerTypeCPU(field)
    else:
        args["cpu"] = None

    field = data.get("disk", None)
    if field is not None:
        args["disk"] = unmarshal_ServerTypeDisk(field)
    else:
        args["disk"] = None

    field = data.get("memory", None)
    if field is not None:
        args["memory"] = unmarshal_ServerTypeMemory(field)
    else:
        args["memory"] = None

    field = data.get("minimum_lease_duration", None)
    if field is not None:
        args["minimum_lease_duration"] = field
    else:
        args["minimum_lease_duration"] = None

    field = data.get("gpu", None)
    if field is not None:
        args["gpu"] = unmarshal_ServerTypeGPU(field)
    else:
        args["gpu"] = None

    field = data.get("network", None)
    if field is not None:
        args["network"] = unmarshal_ServerTypeNetwork(field)
    else:
        args["network"] = None

    field = data.get("default_os", None)
    if field is not None:
        args["default_os"] = unmarshal_OS(field)
    else:
        args["default_os"] = None

    return ServerType(**args)


def unmarshal_Server(data: Any) -> Server:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Server' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("ip", None)
    if field is not None:
        args["ip"] = field

    field = data.get("vnc_url", None)
    if field is not None:
        args["vnc_url"] = field

    field = data.get("ssh_username", None)
    if field is not None:
        args["ssh_username"] = field

    field = data.get("sudo_password", None)
    if field is not None:
        args["sudo_password"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("deletion_scheduled", None)
    if field is not None:
        args["deletion_scheduled"] = field

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field

    field = data.get("os", None)
    if field is not None:
        args["os"] = unmarshal_OS(field)
    else:
        args["os"] = None

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

    field = data.get("deletable_at", None)
    if field is not None:
        args["deletable_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["deletable_at"] = None

    return Server(**args)


def unmarshal_ListOSResponse(data: Any) -> ListOSResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOSResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("os", None)
    if field is not None:
        args["os"] = [unmarshal_OS(v) for v in field] if field is not None else None

    return ListOSResponse(**args)


def unmarshal_ListServerTypesResponse(data: Any) -> ListServerTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServerTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server_types", None)
    if field is not None:
        args["server_types"] = (
            [unmarshal_ServerType(v) for v in field] if field is not None else None
        )

    return ListServerTypesResponse(**args)


def unmarshal_ListServersResponse(data: Any) -> ListServersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("servers", None)
    if field is not None:
        args["servers"] = (
            [unmarshal_Server(v) for v in field] if field is not None else None
        )

    return ListServersResponse(**args)


def marshal_CreateServerRequest(
    request: CreateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.os_id is not None:
        output["os_id"] = request.os_id

    return output


def marshal_ReinstallServerRequest(
    request: ReinstallServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.os_id is not None:
        output["os_id"] = request.os_id

    return output


def marshal_UpdateServerRequest(
    request: UpdateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.schedule_deletion is not None:
        output["schedule_deletion"] = request.schedule_deletion

    return output
