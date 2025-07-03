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
    ListServerPrivateNetworksRequestOrderBy,
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

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("server_id", str())
    args["server_id"] = field

    field = data.get("private_network_id", str())
    args["private_network_id"] = field

    field = data.get("status", getattr(ServerPrivateNetworkStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("ipam_ip_ids", [])
    args["ipam_ip_ids"] = field

    field = data.get("vlan", None)
    args["vlan"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return ServerPrivateNetwork(**args)

def unmarshal_ListServerPrivateNetworksResponse(data: Any) -> ListServerPrivateNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServerPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server_private_networks", str())
    args["server_private_networks"] = [unmarshal_ServerPrivateNetwork(v) for v in field] if field is not None else None

    field = data.get("total_count", str())
    args["total_count"] = field

    return ListServerPrivateNetworksResponse(**args)

def unmarshal_SetServerPrivateNetworksResponse(data: Any) -> SetServerPrivateNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetServerPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server_private_networks", str())
    args["server_private_networks"] = [unmarshal_ServerPrivateNetwork(v) for v in field] if field is not None else None

    return SetServerPrivateNetworksResponse(**args)

def marshal_PrivateNetworkApiAddServerPrivateNetworkRequest(
    request: PrivateNetworkApiAddServerPrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id
    else:
        output["private_network_id"] = str()

    if request.ipam_ip_ids is not None:
        output["ipam_ip_ids"] = request.ipam_ip_ids
    else:
        output["ipam_ip_ids"] = None


    return output

def marshal_PrivateNetworkApiSetServerPrivateNetworksRequest(
    request: PrivateNetworkApiSetServerPrivateNetworksRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.per_private_network_ipam_ip_ids is not None:
        output["per_private_network_ipam_ip_ids"] = {
            key: value
            for key, value in request.per_private_network_ipam_ip_ids.items()
        }
    else:
        output["per_private_network_ipam_ip_ids"] = str()


    return output
