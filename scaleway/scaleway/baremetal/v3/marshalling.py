# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    ServerPrivateNetworkStatus,
    ServerPrivateNetwork,
    ListServerPrivateNetworksResponse,
    SetServerPrivateNetworksResponse,
    PrivateNetworkApiAddServerPrivateNetworkRequest,
    PrivateNetworkApiSetServerPrivateNetworksRequest,
)


def unmarshal_ServerPrivateNetwork(data: Any) -> ServerPrivateNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerPrivateNetwork' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("server_id", None)
    if field is not None:
        args["server_id"] = field
    else:
        args["server_id"] = None

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field
    else:
        args["private_network_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = ServerPrivateNetworkStatus.UNKNOWN_STATUS

    field = data.get("ipam_ip_ids", None)
    if field is not None:
        args["ipam_ip_ids"] = field
    else:
        args["ipam_ip_ids"] = []

    field = data.get("vlan", None)
    if field is not None:
        args["vlan"] = field
    else:
        args["vlan"] = 0

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

    return ServerPrivateNetwork(**args)


def unmarshal_ListServerPrivateNetworksResponse(
    data: Any,
) -> ListServerPrivateNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServerPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("server_private_networks", None)
    if field is not None:
        args["server_private_networks"] = (
            [unmarshal_ServerPrivateNetwork(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["server_private_networks"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    return ListServerPrivateNetworksResponse(**args)


def unmarshal_SetServerPrivateNetworksResponse(
    data: Any,
) -> SetServerPrivateNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetServerPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("server_private_networks", None)
    if field is not None:
        args["server_private_networks"] = (
            [unmarshal_ServerPrivateNetwork(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["server_private_networks"] = None

    return SetServerPrivateNetworksResponse(**args)


def marshal_PrivateNetworkApiAddServerPrivateNetworkRequest(
    request: PrivateNetworkApiAddServerPrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    if request.ipam_ip_ids is not None:
        output["ipam_ip_ids"] = request.ipam_ip_ids

    return output


def marshal_PrivateNetworkApiSetServerPrivateNetworksRequest(
    request: PrivateNetworkApiSetServerPrivateNetworksRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.per_private_network_ipam_ip_ids is not None:
        output["per_private_network_ipam_ip_ids"] = {
            key: value for key, value in request.per_private_network_ipam_ip_ids.items()
        }

    return output
