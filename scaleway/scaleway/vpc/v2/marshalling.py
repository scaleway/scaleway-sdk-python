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
    AclRuleProtocol,
    Action,
    ListPrivateNetworksRequestOrderBy,
    ListSubnetsRequestOrderBy,
    ListVPCsRequestOrderBy,
    Subnet,
    PrivateNetwork,
    Route,
    VPC,
    AddSubnetsResponse,
    DeleteSubnetsResponse,
    AclRule,
    GetAclResponse,
    ListPrivateNetworksResponse,
    ListSubnetsResponse,
    ListVPCsResponse,
    SetAclResponse,
    AddSubnetsRequest,
    CreatePrivateNetworkRequest,
    CreateRouteRequest,
    CreateVPCRequest,
    DeleteSubnetsRequest,
    SetAclRequest,
    UpdatePrivateNetworkRequest,
    UpdateRouteRequest,
    UpdateVPCRequest,
)

def unmarshal_Subnet(data: Any) -> Subnet:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Subnet' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("subnet", str())
    args["subnet"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("private_network_id", str())
    args["private_network_id"] = field

    field = data.get("vpc_id", str())
    args["vpc_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Subnet(**args)

def unmarshal_PrivateNetwork(data: Any) -> PrivateNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("subnets", [])
    args["subnets"] = [unmarshal_Subnet(v) for v in field] if field is not None else None

    field = data.get("vpc_id", str())
    args["vpc_id"] = field

    field = data.get("dhcp_enabled", False)
    args["dhcp_enabled"] = field

    field = data.get("default_route_propagation_enabled", False)
    args["default_route_propagation_enabled"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return PrivateNetwork(**args)

def unmarshal_Route(data: Any) -> Route:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Route' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("vpc_id", str())
    args["vpc_id"] = field

    field = data.get("destination", str())
    args["destination"] = field

    field = data.get("is_read_only", False)
    args["is_read_only"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("nexthop_resource_id", None)
    args["nexthop_resource_id"] = field

    field = data.get("nexthop_private_network_id", None)
    args["nexthop_private_network_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Route(**args)

def unmarshal_VPC(data: Any) -> VPC:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VPC' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("is_default", False)
    args["is_default"] = field

    field = data.get("private_network_count", 0)
    args["private_network_count"] = field

    field = data.get("routing_enabled", False)
    args["routing_enabled"] = field

    field = data.get("custom_routes_propagation_enabled", False)
    args["custom_routes_propagation_enabled"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return VPC(**args)

def unmarshal_AddSubnetsResponse(data: Any) -> AddSubnetsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddSubnetsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("subnets", str())
    args["subnets"] = field

    return AddSubnetsResponse(**args)

def unmarshal_DeleteSubnetsResponse(data: Any) -> DeleteSubnetsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeleteSubnetsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("subnets", str())
    args["subnets"] = field

    return DeleteSubnetsResponse(**args)

def unmarshal_AclRule(data: Any) -> AclRule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AclRule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("protocol", str())
    args["protocol"] = field

    field = data.get("source", str())
    args["source"] = field

    field = data.get("src_port_low", str())
    args["src_port_low"] = field

    field = data.get("src_port_high", str())
    args["src_port_high"] = field

    field = data.get("destination", str())
    args["destination"] = field

    field = data.get("dst_port_low", str())
    args["dst_port_low"] = field

    field = data.get("dst_port_high", str())
    args["dst_port_high"] = field

    field = data.get("action", str())
    args["action"] = field

    field = data.get("description", None)
    args["description"] = field

    return AclRule(**args)

def unmarshal_GetAclResponse(data: Any) -> GetAclResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetAclResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", str())
    args["rules"] = [unmarshal_AclRule(v) for v in field] if field is not None else None

    field = data.get("default_policy", str())
    args["default_policy"] = field

    return GetAclResponse(**args)

def unmarshal_ListPrivateNetworksResponse(data: Any) -> ListPrivateNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_networks", str())
    args["private_networks"] = [unmarshal_PrivateNetwork(v) for v in field] if field is not None else None

    field = data.get("total_count", str())
    args["total_count"] = field

    return ListPrivateNetworksResponse(**args)

def unmarshal_ListSubnetsResponse(data: Any) -> ListSubnetsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSubnetsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("subnets", str())
    args["subnets"] = [unmarshal_Subnet(v) for v in field] if field is not None else None

    field = data.get("total_count", str())
    args["total_count"] = field

    return ListSubnetsResponse(**args)

def unmarshal_ListVPCsResponse(data: Any) -> ListVPCsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVPCsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("vpcs", str())
    args["vpcs"] = [unmarshal_VPC(v) for v in field] if field is not None else None

    field = data.get("total_count", str())
    args["total_count"] = field

    return ListVPCsResponse(**args)

def unmarshal_SetAclResponse(data: Any) -> SetAclResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetAclResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", str())
    args["rules"] = [unmarshal_AclRule(v) for v in field] if field is not None else None

    field = data.get("default_policy", str())
    args["default_policy"] = field

    return SetAclResponse(**args)

def marshal_AddSubnetsRequest(
    request: AddSubnetsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.subnets is not None:
        output["subnets"] = request.subnets
    else:
        output["subnets"] = None


    return output

def marshal_CreatePrivateNetworkRequest(
    request: CreatePrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.default_route_propagation_enabled is not None:
        output["default_route_propagation_enabled"] = request.default_route_propagation_enabled
    else:
        output["default_route_propagation_enabled"] = False

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.subnets is not None:
        output["subnets"] = request.subnets
    else:
        output["subnets"] = None

    if request.vpc_id is not None:
        output["vpc_id"] = request.vpc_id
    else:
        output["vpc_id"] = None


    return output

def marshal_CreateRouteRequest(
    request: CreateRouteRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.vpc_id is not None:
        output["vpc_id"] = request.vpc_id
    else:
        output["vpc_id"] = str()

    if request.destination is not None:
        output["destination"] = request.destination
    else:
        output["destination"] = str()

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.nexthop_resource_id is not None:
        output["nexthop_resource_id"] = request.nexthop_resource_id
    else:
        output["nexthop_resource_id"] = None

    if request.nexthop_private_network_id is not None:
        output["nexthop_private_network_id"] = request.nexthop_private_network_id
    else:
        output["nexthop_private_network_id"] = None


    return output

def marshal_CreateVPCRequest(
    request: CreateVPCRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.enable_routing is not None:
        output["enable_routing"] = request.enable_routing
    else:
        output["enable_routing"] = False

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_DeleteSubnetsRequest(
    request: DeleteSubnetsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.subnets is not None:
        output["subnets"] = request.subnets
    else:
        output["subnets"] = None


    return output

def marshal_AclRule(
    request: AclRule,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.protocol is not None:
        output["protocol"] = str(request.protocol)
    else:
        output["protocol"] = str()

    if request.source is not None:
        output["source"] = request.source
    else:
        output["source"] = str()

    if request.src_port_low is not None:
        output["src_port_low"] = request.src_port_low
    else:
        output["src_port_low"] = str()

    if request.src_port_high is not None:
        output["src_port_high"] = request.src_port_high
    else:
        output["src_port_high"] = str()

    if request.destination is not None:
        output["destination"] = request.destination
    else:
        output["destination"] = str()

    if request.dst_port_low is not None:
        output["dst_port_low"] = request.dst_port_low
    else:
        output["dst_port_low"] = str()

    if request.dst_port_high is not None:
        output["dst_port_high"] = request.dst_port_high
    else:
        output["dst_port_high"] = str()

    if request.action is not None:
        output["action"] = str(request.action)
    else:
        output["action"] = str()

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None


    return output

def marshal_SetAclRequest(
    request: SetAclRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.rules is not None:
        output["rules"] = [marshal_AclRule(item, defaults) for item in request.rules]
    else:
        output["rules"] = str()

    if request.is_ipv6 is not None:
        output["is_ipv6"] = request.is_ipv6
    else:
        output["is_ipv6"] = str()

    if request.default_policy is not None:
        output["default_policy"] = str(request.default_policy)
    else:
        output["default_policy"] = str()


    return output

def marshal_UpdatePrivateNetworkRequest(
    request: UpdatePrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.default_route_propagation_enabled is not None:
        output["default_route_propagation_enabled"] = request.default_route_propagation_enabled
    else:
        output["default_route_propagation_enabled"] = None


    return output

def marshal_UpdateRouteRequest(
    request: UpdateRouteRequest,
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

    if request.destination is not None:
        output["destination"] = request.destination
    else:
        output["destination"] = None

    if request.nexthop_resource_id is not None:
        output["nexthop_resource_id"] = request.nexthop_resource_id
    else:
        output["nexthop_resource_id"] = None

    if request.nexthop_private_network_id is not None:
        output["nexthop_private_network_id"] = request.nexthop_private_network_id
    else:
        output["nexthop_private_network_id"] = None


    return output

def marshal_UpdateVPCRequest(
    request: UpdateVPCRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output
