# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from dateutil import parser
from .types import (
    ListPrivateNetworksResponse,
    PrivateNetwork,
    CreatePrivateNetworkRequest,
    UpdatePrivateNetworkRequest,
)


def unmarshal_PrivateNetwork(data: Any) -> PrivateNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("subnets", None)
    args["subnets"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("zone", None)
    args["zone"] = field

    return PrivateNetwork(**args)


def unmarshal_ListPrivateNetworksResponse(data: Any) -> ListPrivateNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_networks", None)
    args["private_networks"] = (
        [unmarshal_PrivateNetwork(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListPrivateNetworksResponse(**args)


def marshal_CreatePrivateNetworkRequest(
    request: CreatePrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.subnets is not None:
        output["subnets"] = request.subnets

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdatePrivateNetworkRequest(
    request: UpdatePrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.subnets is not None:
        output["subnets"] = request.subnets

    if request.tags is not None:
        output["tags"] = request.tags

    return output
