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
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'PrivateNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("subnets")
    args["subnets"] = field

    field = data.get("tags")
    args["tags"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("zone")
    args["zone"] = field

    return PrivateNetwork(**args)


def unmarshal_ListPrivateNetworksResponse(data: Any) -> ListPrivateNetworksResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_networks")
    args["private_networks"] = [
        unmarshal_PrivateNetwork(v) for v in data["private_networks"]
    ]

    field = data.get("total_count")
    args["total_count"] = field

    return ListPrivateNetworksResponse(**args)


def marshal_CreatePrivateNetworkRequest(
    request: CreatePrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name": request.name,
        "project_id": request.project_id or defaults.default_project_id,
        "subnets": request.subnets,
        "tags": request.tags,
    }


def marshal_UpdatePrivateNetworkRequest(
    request: UpdatePrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name": request.name,
        "subnets": request.subnets,
        "tags": request.tags,
    }
