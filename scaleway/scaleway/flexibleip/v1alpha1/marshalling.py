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

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("mac_address", None)
    args["mac_address"] = field

    field = data.get("mac_type", None)
    args["mac_type"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("zone", None)
    args["zone"] = field

    return MACAddress(**args)


def unmarshal_FlexibleIP(data: Any) -> FlexibleIP:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'FlexibleIP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("ip_address", None)
    args["ip_address"] = field

    field = data.get("mac_address", None)
    args["mac_address"] = unmarshal_MACAddress(field) if field is not None else None

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("reverse", None)
    args["reverse"] = field

    field = data.get("server_id", None)
    args["server_id"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("zone", None)
    args["zone"] = field

    return FlexibleIP(**args)


def unmarshal_AttachFlexibleIPsResponse(data: Any) -> AttachFlexibleIPsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'AttachFlexibleIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("flexible_ips", None)
    args["flexible_ips"] = (
        [unmarshal_FlexibleIP(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return AttachFlexibleIPsResponse(**args)


def unmarshal_DetachFlexibleIPsResponse(data: Any) -> DetachFlexibleIPsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DetachFlexibleIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("flexible_ips", None)
    args["flexible_ips"] = (
        [unmarshal_FlexibleIP(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return DetachFlexibleIPsResponse(**args)


def unmarshal_ListFlexibleIPsResponse(data: Any) -> ListFlexibleIPsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListFlexibleIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("flexible_ips", None)
    args["flexible_ips"] = (
        [unmarshal_FlexibleIP(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListFlexibleIPsResponse(**args)


def marshal_AttachFlexibleIPRequest(
    request: AttachFlexibleIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.fips_ids is not None:
        output["fips_ids"] = request.fips_ids

    if request.server_id is not None:
        output["server_id"] = request.server_id

    return output


def marshal_CreateFlexibleIPRequest(
    request: CreateFlexibleIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.is_ipv6 is not None:
        output["is_ipv6"] = request.is_ipv6

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.reverse is not None:
        output["reverse"] = request.reverse

    if request.server_id is not None:
        output["server_id"] = request.server_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_DetachFlexibleIPRequest(
    request: DetachFlexibleIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.fips_ids is not None:
        output["fips_ids"] = request.fips_ids

    return output


def marshal_DuplicateMACAddrRequest(
    request: DuplicateMACAddrRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.duplicate_from_fip_id is not None:
        output["duplicate_from_fip_id"] = request.duplicate_from_fip_id

    return output


def marshal_GenerateMACAddrRequest(
    request: GenerateMACAddrRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.mac_type is not None:
        output["mac_type"] = MACAddressType(request.mac_type)

    return output


def marshal_MoveMACAddrRequest(
    request: MoveMACAddrRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.dst_fip_id is not None:
        output["dst_fip_id"] = request.dst_fip_id

    return output


def marshal_UpdateFlexibleIPRequest(
    request: UpdateFlexibleIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.reverse is not None:
        output["reverse"] = request.reverse

    if request.tags is not None:
        output["tags"] = request.tags

    return output
