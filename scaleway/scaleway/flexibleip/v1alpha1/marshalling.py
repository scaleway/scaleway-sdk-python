# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from dateutil import parser
from .types import (
    MACAddressType,
    AttachFlexibleIPsResponse,
    DetachFlexibleIPsResponse,
    FlexibleIP,
    ListFlexibleIPsResponse,
    MACAddress,
    CreateFlexibleIPRequest,
    UpdateFlexibleIPRequest,
    AttachFlexibleIPRequest,
    DetachFlexibleIPRequest,
    GenerateMACAddrRequest,
    DuplicateMACAddrRequest,
    MoveMACAddrRequest,
)


def unmarshal_MACAddress(data: Any) -> MACAddress:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'MACAddress' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id")
    args["id"] = field

    field = data.get("mac_address")
    args["mac_address"] = field

    field = data.get("mac_type")
    args["mac_type"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("zone")
    args["zone"] = field

    return MACAddress(**args)


def unmarshal_FlexibleIP(data: Any) -> FlexibleIP:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'FlexibleIP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description")
    args["description"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("ip_address")
    args["ip_address"] = field

    field = data.get("mac_address")
    args["mac_address"] = unmarshal_MACAddress(field) if field is not None else None

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("reverse")
    args["reverse"] = field

    field = data.get("server_id")
    args["server_id"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("tags")
    args["tags"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("zone")
    args["zone"] = field

    return FlexibleIP(**args)


def unmarshal_AttachFlexibleIPsResponse(data: Any) -> AttachFlexibleIPsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'AttachFlexibleIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("flexible_ips")
    args["flexible_ips"] = [unmarshal_FlexibleIP(v) for v in data["flexible_ips"]]

    field = data.get("total_count")
    args["total_count"] = field

    return AttachFlexibleIPsResponse(**args)


def unmarshal_DetachFlexibleIPsResponse(data: Any) -> DetachFlexibleIPsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DetachFlexibleIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("flexible_ips")
    args["flexible_ips"] = [unmarshal_FlexibleIP(v) for v in data["flexible_ips"]]

    field = data.get("total_count")
    args["total_count"] = field

    return DetachFlexibleIPsResponse(**args)


def unmarshal_ListFlexibleIPsResponse(data: Any) -> ListFlexibleIPsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListFlexibleIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("flexible_ips")
    args["flexible_ips"] = [unmarshal_FlexibleIP(v) for v in data["flexible_ips"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListFlexibleIPsResponse(**args)


def marshal_AttachFlexibleIPRequest(
    request: AttachFlexibleIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "fips_ids": request.fips_ids,
        "server_id": request.server_id,
    }


def marshal_CreateFlexibleIPRequest(
    request: CreateFlexibleIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "is_ipv6": request.is_ipv6,
        "project_id": request.project_id or defaults.default_project_id,
        "reverse": request.reverse,
        "server_id": request.server_id,
        "tags": request.tags,
    }


def marshal_DetachFlexibleIPRequest(
    request: DetachFlexibleIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "fips_ids": request.fips_ids,
    }


def marshal_DuplicateMACAddrRequest(
    request: DuplicateMACAddrRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "duplicate_from_fip_id": request.duplicate_from_fip_id,
    }


def marshal_GenerateMACAddrRequest(
    request: GenerateMACAddrRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "mac_type": MACAddressType(request.mac_type)
        if request.mac_type is not None
        else None,
    }


def marshal_MoveMACAddrRequest(
    request: MoveMACAddrRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "dst_fip_id": request.dst_fip_id,
    }


def marshal_UpdateFlexibleIPRequest(
    request: UpdateFlexibleIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "reverse": request.reverse,
        "tags": request.tags,
    }
