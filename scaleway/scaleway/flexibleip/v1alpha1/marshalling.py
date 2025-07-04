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
    FlexibleIPStatus,
    ListFlexibleIPsRequestOrderBy,
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

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("mac_address", str())
    args["mac_address"] = field

    field = data.get("mac_type", getattr(MACAddressType, "UNKNOWN_TYPE"))
    args["mac_type"] = field

    field = data.get("status", getattr(MACAddressStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return MACAddress(**args)

def unmarshal_FlexibleIP(data: Any) -> FlexibleIP:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'FlexibleIP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("status", getattr(FlexibleIPStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("ip_address", str())
    args["ip_address"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("reverse", str())
    args["reverse"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("mac_address", None)
    args["mac_address"] = unmarshal_MACAddress(field) if field is not None else None

    field = data.get("server_id", None)
    args["server_id"] = field

    return FlexibleIP(**args)

def unmarshal_AttachFlexibleIPsResponse(data: Any) -> AttachFlexibleIPsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AttachFlexibleIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("flexible_ips", [])
    args["flexible_ips"] = [unmarshal_FlexibleIP(v) for v in field] if field is not None else None

    return AttachFlexibleIPsResponse(**args)

def unmarshal_DetachFlexibleIPsResponse(data: Any) -> DetachFlexibleIPsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DetachFlexibleIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("flexible_ips", [])
    args["flexible_ips"] = [unmarshal_FlexibleIP(v) for v in field] if field is not None else None

    return DetachFlexibleIPsResponse(**args)

def unmarshal_ListFlexibleIPsResponse(data: Any) -> ListFlexibleIPsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListFlexibleIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("flexible_ips", [])
    args["flexible_ips"] = [unmarshal_FlexibleIP(v) for v in field] if field is not None else None

    return ListFlexibleIPsResponse(**args)

def marshal_AttachFlexibleIPRequest(
    request: AttachFlexibleIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.fips_ids is not None:
        output["fips_ids"] = request.fips_ids
    else:
        output["fips_ids"] = str()

    if request.server_id is not None:
        output["server_id"] = request.server_id
    else:
        output["server_id"] = str()


    return output

def marshal_CreateFlexibleIPRequest(
    request: CreateFlexibleIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.is_ipv6 is not None:
        output["is_ipv6"] = request.is_ipv6
    else:
        output["is_ipv6"] = False

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.server_id is not None:
        output["server_id"] = request.server_id
    else:
        output["server_id"] = None

    if request.reverse is not None:
        output["reverse"] = request.reverse
    else:
        output["reverse"] = None


    return output

def marshal_DetachFlexibleIPRequest(
    request: DetachFlexibleIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.fips_ids is not None:
        output["fips_ids"] = request.fips_ids
    else:
        output["fips_ids"] = str()


    return output

def marshal_DuplicateMACAddrRequest(
    request: DuplicateMACAddrRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.duplicate_from_fip_id is not None:
        output["duplicate_from_fip_id"] = request.duplicate_from_fip_id
    else:
        output["duplicate_from_fip_id"] = str()


    return output

def marshal_GenerateMACAddrRequest(
    request: GenerateMACAddrRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.mac_type is not None:
        output["mac_type"] = str(request.mac_type)
    else:
        output["mac_type"] = str()


    return output

def marshal_MoveMACAddrRequest(
    request: MoveMACAddrRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.dst_fip_id is not None:
        output["dst_fip_id"] = request.dst_fip_id
    else:
        output["dst_fip_id"] = str()


    return output

def marshal_UpdateFlexibleIPRequest(
    request: UpdateFlexibleIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.reverse is not None:
        output["reverse"] = request.reverse
    else:
        output["reverse"] = None


    return output
