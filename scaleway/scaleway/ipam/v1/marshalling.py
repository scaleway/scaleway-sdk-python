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
    ListIPsRequestOrderBy,
    ResourceType,
    Resource,
    Reverse,
    Source,
    IP,
    ListIPsResponse,
    CustomResource,
    AttachIPRequest,
    BookIPRequest,
    DetachIPRequest,
    MoveIPRequest,
    ReleaseIPSetRequest,
    UpdateIPRequest,
)

def unmarshal_Resource(data: Any) -> Resource:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Resource' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", getattr(ResourceType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("id", str())
    args["id"] = field

    field = data.get("mac_address", None)
    args["mac_address"] = field

    field = data.get("name", None)
    args["name"] = field

    return Resource(**args)

def unmarshal_Reverse(data: Any) -> Reverse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Reverse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("hostname", str())
    args["hostname"] = field

    field = data.get("address", None)
    args["address"] = field

    return Reverse(**args)

def unmarshal_Source(data: Any) -> Source:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Source' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("zonal", None)
    args["zonal"] = field

    field = data.get("private_network_id", None)
    args["private_network_id"] = field

    field = data.get("subnet_id", None)
    args["subnet_id"] = field

    field = data.get("vpc_id", None)
    args["vpc_id"] = field

    return Source(**args)

def unmarshal_IP(data: Any) -> IP:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'IP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("address", str())
    args["address"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("is_ipv6", False)
    args["is_ipv6"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("reverses", [])
    args["reverses"] = [unmarshal_Reverse(v) for v in field] if field is not None else None

    field = data.get("region", )
    args["region"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("source", None)
    args["source"] = unmarshal_Source(field) if field is not None else None

    field = data.get("resource", None)
    args["resource"] = unmarshal_Resource(field) if field is not None else None

    field = data.get("zone", None)
    args["zone"] = field

    return IP(**args)

def unmarshal_ListIPsResponse(data: Any) -> ListIPsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", str())
    args["total_count"] = field

    field = data.get("ips", str())
    args["ips"] = [unmarshal_IP(v) for v in field] if field is not None else None

    return ListIPsResponse(**args)

def marshal_CustomResource(
    request: CustomResource,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.mac_address is not None:
        output["mac_address"] = request.mac_address
    else:
        output["mac_address"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None


    return output

def marshal_AttachIPRequest(
    request: AttachIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.resource is not None:
        output["resource"] = marshal_CustomResource(request.resource, defaults)
    else:
        output["resource"] = str()


    return output

def marshal_Source(
    request: Source,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="zonal", value=request.zonal,marshal_func=None
            ),
            OneOfPossibility(param="private_network_id", value=request.private_network_id,marshal_func=None
            ),
            OneOfPossibility(param="subnet_id", value=request.subnet_id,marshal_func=None
            ),
            OneOfPossibility(param="vpc_id", value=request.vpc_id,marshal_func=None
            ),
        ]),
    )


    return output

def marshal_BookIPRequest(
    request: BookIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.source is not None:
        output["source"] = marshal_Source(request.source, defaults)
    else:
        output["source"] = Source()

    if request.is_ipv6 is not None:
        output["is_ipv6"] = request.is_ipv6
    else:
        output["is_ipv6"] = False

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.address is not None:
        output["address"] = request.address
    else:
        output["address"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.resource is not None:
        output["resource"] = marshal_CustomResource(request.resource, defaults)
    else:
        output["resource"] = None


    return output

def marshal_DetachIPRequest(
    request: DetachIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.resource is not None:
        output["resource"] = marshal_CustomResource(request.resource, defaults)
    else:
        output["resource"] = str()


    return output

def marshal_MoveIPRequest(
    request: MoveIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.from_resource is not None:
        output["from_resource"] = marshal_CustomResource(request.from_resource, defaults)
    else:
        output["from_resource"] = str()

    if request.to_resource is not None:
        output["to_resource"] = marshal_CustomResource(request.to_resource, defaults)
    else:
        output["to_resource"] = None


    return output

def marshal_ReleaseIPSetRequest(
    request: ReleaseIPSetRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip_ids is not None:
        output["ip_ids"] = request.ip_ids
    else:
        output["ip_ids"] = None


    return output

def marshal_Reverse(
    request: Reverse,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.hostname is not None:
        output["hostname"] = request.hostname
    else:
        output["hostname"] = str()

    if request.address is not None:
        output["address"] = request.address
    else:
        output["address"] = None


    return output

def marshal_UpdateIPRequest(
    request: UpdateIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.reverses is not None:
        output["reverses"] = [marshal_Reverse(item, defaults) for item in request.reverses]
    else:
        output["reverses"] = None


    return output
