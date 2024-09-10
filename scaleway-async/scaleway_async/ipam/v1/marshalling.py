# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
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

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("mac_address", None)
    if field is not None:
        args["mac_address"] = field
    else:
        args["mac_address"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return Resource(**args)


def unmarshal_Reverse(data: Any) -> Reverse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Reverse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("hostname", None)
    if field is not None:
        args["hostname"] = field

    field = data.get("address", None)
    if field is not None:
        args["address"] = field
    else:
        args["address"] = None

    return Reverse(**args)


def unmarshal_Source(data: Any) -> Source:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Source' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("zonal", None)
    if field is not None:
        args["zonal"] = field
    else:
        args["zonal"] = None

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field
    else:
        args["private_network_id"] = None

    field = data.get("subnet_id", None)
    if field is not None:
        args["subnet_id"] = field
    else:
        args["subnet_id"] = None

    return Source(**args)


def unmarshal_IP(data: Any) -> IP:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'IP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("address", None)
    if field is not None:
        args["address"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("is_ipv6", None)
    if field is not None:
        args["is_ipv6"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("reverses", None)
    if field is not None:
        args["reverses"] = (
            [unmarshal_Reverse(v) for v in field] if field is not None else None
        )

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

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

    field = data.get("source", None)
    if field is not None:
        args["source"] = unmarshal_Source(field)
    else:
        args["source"] = None

    field = data.get("resource", None)
    if field is not None:
        args["resource"] = unmarshal_Resource(field)
    else:
        args["resource"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    return IP(**args)


def unmarshal_ListIPsResponse(data: Any) -> ListIPsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("ips", None)
    if field is not None:
        args["ips"] = [unmarshal_IP(v) for v in field] if field is not None else None

    return ListIPsResponse(**args)


def marshal_CustomResource(
    request: CustomResource,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.mac_address is not None:
        output["mac_address"] = request.mac_address

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_AttachIPRequest(
    request: AttachIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.resource is not None:
        output["resource"] = marshal_CustomResource(request.resource, defaults)

    return output


def marshal_Source(
    request: Source,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("zonal", request.zonal),
                OneOfPossibility("private_network_id", request.private_network_id),
                OneOfPossibility("subnet_id", request.subnet_id),
            ]
        ),
    )

    return output


def marshal_BookIPRequest(
    request: BookIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.source is not None:
        output["source"] = marshal_Source(request.source, defaults)

    if request.is_ipv6 is not None:
        output["is_ipv6"] = request.is_ipv6

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.address is not None:
        output["address"] = request.address

    if request.tags is not None:
        output["tags"] = request.tags

    if request.resource is not None:
        output["resource"] = marshal_CustomResource(request.resource, defaults)

    return output


def marshal_DetachIPRequest(
    request: DetachIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.resource is not None:
        output["resource"] = marshal_CustomResource(request.resource, defaults)

    return output


def marshal_MoveIPRequest(
    request: MoveIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.from_resource is not None:
        output["from_resource"] = marshal_CustomResource(
            request.from_resource, defaults
        )

    if request.to_resource is not None:
        output["to_resource"] = marshal_CustomResource(request.to_resource, defaults)

    return output


def marshal_ReleaseIPSetRequest(
    request: ReleaseIPSetRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip_ids is not None:
        output["ip_ids"] = request.ip_ids

    return output


def marshal_Reverse(
    request: Reverse,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.hostname is not None:
        output["hostname"] = request.hostname

    if request.address is not None:
        output["address"] = request.address

    return output


def marshal_UpdateIPRequest(
    request: UpdateIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.tags is not None:
        output["tags"] = request.tags

    if request.reverses is not None:
        output["reverses"] = [
            marshal_Reverse(item, defaults) for item in request.reverses
        ]

    return output
