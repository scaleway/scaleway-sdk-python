# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    FlexibleIPStatus,
    MACAddressStatus,
    MACAddressType,
    MACAddress,
    FlexibleIP,
    AttachFlexibleIPsResponse,
    DetachFlexibleIPsResponse,
    ListFlexibleIPsResponse,
    AttachFlexibleIPRequest,
    CreateFlexibleIPRequest,
    DetachFlexibleIPRequest,
    DuplicateMACAddrRequest,
    GenerateMACAddrRequest,
    MoveMACAddrRequest,
    UpdateFlexibleIPRequest,
)


def unmarshal_MACAddress(data: Any) -> MACAddress:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'MACAddress' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("mac_address", None)
    if field is not None:
        args["mac_address"] = field
    else:
        args["mac_address"] = None

    field = data.get("mac_type", None)
    if field is not None:
        args["mac_type"] = field
    else:
        args["mac_type"] = MACAddressType.UNKNOWN_TYPE

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = MACAddressStatus.UNKNOWN

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    return MACAddress(**args)


def unmarshal_FlexibleIP(data: Any) -> FlexibleIP:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'FlexibleIP' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

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

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = FlexibleIPStatus.UNKNOWN

    field = data.get("ip_address", None)
    if field is not None:
        args["ip_address"] = field
    else:
        args["ip_address"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("reverse", None)
    if field is not None:
        args["reverse"] = field
    else:
        args["reverse"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("mac_address", None)
    if field is not None:
        args["mac_address"] = unmarshal_MACAddress(field)
    else:
        args["mac_address"] = None

    field = data.get("server_id", None)
    if field is not None:
        args["server_id"] = field
    else:
        args["server_id"] = None

    return FlexibleIP(**args)


def unmarshal_AttachFlexibleIPsResponse(data: Any) -> AttachFlexibleIPsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AttachFlexibleIPsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("flexible_ips", None)
    if field is not None:
        args["flexible_ips"] = (
            [unmarshal_FlexibleIP(v) for v in field] if field is not None else None
        )
    else:
        args["flexible_ips"] = []

    return AttachFlexibleIPsResponse(**args)


def unmarshal_DetachFlexibleIPsResponse(data: Any) -> DetachFlexibleIPsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DetachFlexibleIPsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("flexible_ips", None)
    if field is not None:
        args["flexible_ips"] = (
            [unmarshal_FlexibleIP(v) for v in field] if field is not None else None
        )
    else:
        args["flexible_ips"] = []

    return DetachFlexibleIPsResponse(**args)


def unmarshal_ListFlexibleIPsResponse(data: Any) -> ListFlexibleIPsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListFlexibleIPsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("flexible_ips", None)
    if field is not None:
        args["flexible_ips"] = (
            [unmarshal_FlexibleIP(v) for v in field] if field is not None else None
        )
    else:
        args["flexible_ips"] = []

    return ListFlexibleIPsResponse(**args)


def marshal_AttachFlexibleIPRequest(
    request: AttachFlexibleIPRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.fips_ids is not None:
        output["fips_ids"] = request.fips_ids

    if request.server_id is not None:
        output["server_id"] = request.server_id

    return output


def marshal_CreateFlexibleIPRequest(
    request: CreateFlexibleIPRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.is_ipv6 is not None:
        output["is_ipv6"] = request.is_ipv6

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.server_id is not None:
        output["server_id"] = request.server_id

    if request.reverse is not None:
        output["reverse"] = request.reverse

    return output


def marshal_DetachFlexibleIPRequest(
    request: DetachFlexibleIPRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.fips_ids is not None:
        output["fips_ids"] = request.fips_ids

    return output


def marshal_DuplicateMACAddrRequest(
    request: DuplicateMACAddrRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.duplicate_from_fip_id is not None:
        output["duplicate_from_fip_id"] = request.duplicate_from_fip_id

    return output


def marshal_GenerateMACAddrRequest(
    request: GenerateMACAddrRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.mac_type is not None:
        output["mac_type"] = request.mac_type

    return output


def marshal_MoveMACAddrRequest(
    request: MoveMACAddrRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.dst_fip_id is not None:
        output["dst_fip_id"] = request.dst_fip_id

    return output


def marshal_UpdateFlexibleIPRequest(
    request: UpdateFlexibleIPRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.tags is not None:
        output["tags"] = request.tags

    if request.reverse is not None:
        output["reverse"] = request.reverse

    return output
