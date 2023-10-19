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
    IP,
    ListIPsResponse,
    Resource,
    Source,
    BookIPRequest,
    UpdateIPRequest,
)


def unmarshal_Resource(data: Any) -> Resource:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Resource' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("mac_address", None)
    args["mac_address"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("type", None)
    args["type_"] = field

    return Resource(**args)


def unmarshal_Source(data: Any) -> Source:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Source' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_network_id", None)
    args["private_network_id"] = field

    field = data.get("subnet_id", None)
    args["subnet_id"] = field

    field = data.get("zonal", None)
    args["zonal"] = field

    return Source(**args)


def unmarshal_IP(data: Any) -> IP:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'IP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("address", None)
    args["address"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("is_ipv6", None)
    args["is_ipv6"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("resource", None)
    args["resource"] = unmarshal_Resource(field) if field is not None else None

    field = data.get("source", None)
    args["source"] = unmarshal_Source(field) if field is not None else None

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("zone", None)
    args["zone"] = field

    return IP(**args)


def unmarshal_ListIPsResponse(data: Any) -> ListIPsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ips", None)
    args["ips"] = [unmarshal_IP(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListIPsResponse(**args)


def marshal_Source(
    request: Source,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "zonal", request.zonal if request.zonal is not None else None
                ),
                OneOfPossibility(
                    "private_network_id",
                    request.private_network_id
                    if request.private_network_id is not None
                    else None,
                ),
                OneOfPossibility(
                    "subnet_id",
                    request.subnet_id if request.subnet_id is not None else None,
                ),
            ]
        ),
    )

    return output


def marshal_BookIPRequest(
    request: BookIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.address is not None:
        output["address"] = request.address

    if request.is_ipv6 is not None:
        output["is_ipv6"] = request.is_ipv6

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.source is not None:
        output["source"] = marshal_Source(request.source, defaults)

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateIPRequest(
    request: UpdateIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.tags is not None:
        output["tags"] = request.tags

    return output
