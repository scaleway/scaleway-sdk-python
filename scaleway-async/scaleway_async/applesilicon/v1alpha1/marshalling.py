# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    OS,
    ServerTypeCPU,
    ServerTypeDisk,
    ServerTypeMemory,
    ServerType,
    Server,
    ListOSResponse,
    ListServerTypesResponse,
    ListServersResponse,
    CreateServerRequest,
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

    field = data.get("type_", None)
    if field is not None:
        args["type_"] = field

    return ServerTypeDisk(**args)


def unmarshal_ServerTypeMemory(data: Any) -> ServerTypeMemory:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeMemory' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("capacity", None)
    if field is not None:
        args["capacity"] = field

    field = data.get("type_", None)
    if field is not None:
        args["type_"] = field

    return ServerTypeMemory(**args)


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

    field = data.get("disk", None)
    if field is not None:
        args["disk"] = unmarshal_ServerTypeDisk(field)

    field = data.get("memory", None)
    if field is not None:
        args["memory"] = unmarshal_ServerTypeMemory(field)

    field = data.get("minimum_lease_duration", None)
    if field is not None:
        args["minimum_lease_duration"] = field

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

    field = data.get("type_", None)
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

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("deletable_at", None)
    if field is not None:
        args["deletable_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )

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

    return output


def marshal_UpdateServerRequest(
    request: UpdateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    return output
