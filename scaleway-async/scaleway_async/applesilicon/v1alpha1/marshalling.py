# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from dateutil import parser
from .types import (
    ListOSResponse,
    ListServerTypesResponse,
    ListServersResponse,
    OS,
    Server,
    ServerType,
    ServerTypeCPU,
    ServerTypeDisk,
    ServerTypeMemory,
    CreateServerRequest,
    UpdateServerRequest,
)


def unmarshal_ServerTypeCPU(data: Any) -> ServerTypeCPU:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerTypeCPU' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("core_count", None)
    args["core_count"] = field

    field = data.get("name", None)
    args["name"] = field

    return ServerTypeCPU(**args)


def unmarshal_ServerTypeDisk(data: Any) -> ServerTypeDisk:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerTypeDisk' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("capacity", None)
    args["capacity"] = field

    field = data.get("type_", None)
    args["type_"] = field

    return ServerTypeDisk(**args)


def unmarshal_ServerTypeMemory(data: Any) -> ServerTypeMemory:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerTypeMemory' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("capacity", None)
    args["capacity"] = field

    field = data.get("type_", None)
    args["type_"] = field

    return ServerTypeMemory(**args)


def unmarshal_OS(data: Any) -> OS:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'OS' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("compatible_server_types", None)
    args["compatible_server_types"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("image_url", None)
    args["image_url"] = field

    field = data.get("label", None)
    args["label"] = field

    field = data.get("name", None)
    args["name"] = field

    return OS(**args)


def unmarshal_Server(data: Any) -> Server:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Server' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("deletable_at", None)
    args["deletable_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("ip", None)
    args["ip"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("type_", None)
    args["type_"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("vnc_url", None)
    args["vnc_url"] = field

    field = data.get("zone", None)
    args["zone"] = field

    return Server(**args)


def unmarshal_ServerType(data: Any) -> ServerType:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("cpu", None)
    args["cpu"] = unmarshal_ServerTypeCPU(field) if field is not None else None

    field = data.get("disk", None)
    args["disk"] = unmarshal_ServerTypeDisk(field) if field is not None else None

    field = data.get("memory", None)
    args["memory"] = unmarshal_ServerTypeMemory(field) if field is not None else None

    field = data.get("minimum_lease_duration", None)
    args["minimum_lease_duration"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("stock", None)
    args["stock"] = field

    return ServerType(**args)


def unmarshal_ListOSResponse(data: Any) -> ListOSResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListOSResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("os", None)
    args["os"] = [unmarshal_OS(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListOSResponse(**args)


def unmarshal_ListServerTypesResponse(data: Any) -> ListServerTypesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListServerTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server_types", None)
    args["server_types"] = (
        [unmarshal_ServerType(v) for v in field] if field is not None else None
    )

    return ListServerTypesResponse(**args)


def unmarshal_ListServersResponse(data: Any) -> ListServersResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListServersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("servers", None)
    args["servers"] = (
        [unmarshal_Server(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListServersResponse(**args)


def marshal_CreateServerRequest(
    request: CreateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name": request.name,
        "project_id": request.project_id or defaults.default_project_id,
        "type": request.type_,
    }


def marshal_UpdateServerRequest(
    request: UpdateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name": request.name,
    }
