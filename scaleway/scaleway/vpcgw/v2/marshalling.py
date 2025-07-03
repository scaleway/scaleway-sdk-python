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
    GatewayNetworkStatus,
    GatewayStatus,
    ListGatewayNetworksRequestOrderBy,
    ListGatewaysRequestOrderBy,
    ListIPsRequestOrderBy,
    ListPatRulesRequestOrderBy,
    PatRuleProtocol,
    GatewayNetwork,
    IP,
    Gateway,
    PatRule,
    AddBastionAllowedIPsResponse,
    ListGatewayNetworksResponse,
    GatewayType,
    ListGatewayTypesResponse,
    ListGatewaysResponse,
    ListIPsResponse,
    ListPatRulesResponse,
    SetBastionAllowedIPsResponse,
    SetPatRulesResponse,
    AddBastionAllowedIPsRequest,
    CreateGatewayNetworkRequest,
    CreateGatewayRequest,
    CreateIPRequest,
    CreatePatRuleRequest,
    SetBastionAllowedIPsRequest,
    SetPatRulesRequestRule,
    SetPatRulesRequest,
    UpdateGatewayNetworkRequest,
    UpdateGatewayRequest,
    UpdateIPRequest,
    UpdatePatRuleRequest,
    UpgradeGatewayRequest,
)

def unmarshal_GatewayNetwork(data: Any) -> GatewayNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GatewayNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("gateway_id", str())
    args["gateway_id"] = field

    field = data.get("private_network_id", str())
    args["private_network_id"] = field

    field = data.get("masquerade_enabled", False)
    args["masquerade_enabled"] = field

    field = data.get("status", getattr(GatewayNetworkStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("push_default_route", False)
    args["push_default_route"] = field

    field = data.get("ipam_ip_id", str())
    args["ipam_ip_id"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("mac_address", None)
    args["mac_address"] = field

    return GatewayNetwork(**args)

def unmarshal_IP(data: Any) -> IP:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'IP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("address", str())
    args["address"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("reverse", None)
    args["reverse"] = field

    field = data.get("gateway_id", None)
    args["gateway_id"] = field

    return IP(**args)

def unmarshal_Gateway(data: Any) -> Gateway:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Gateway' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("bandwidth", 0)
    args["bandwidth"] = field

    field = data.get("status", getattr(GatewayStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("gateway_networks", [])
    args["gateway_networks"] = [unmarshal_GatewayNetwork(v) for v in field] if field is not None else None

    field = data.get("bastion_enabled", False)
    args["bastion_enabled"] = field

    field = data.get("ipv4", None)
    args["ipv4"] = unmarshal_IP(field) if field is not None else None

    field = data.get("version", None)
    args["version"] = field

    field = data.get("can_upgrade_to", None)
    args["can_upgrade_to"] = field

    field = data.get("bastion_port", 0)
    args["bastion_port"] = field

    field = data.get("smtp_enabled", False)
    args["smtp_enabled"] = field

    field = data.get("is_legacy", False)
    args["is_legacy"] = field

    field = data.get("bastion_allowed_ips", [])
    args["bastion_allowed_ips"] = field

    field = data.get("zone", )
    args["zone"] = field

    return Gateway(**args)

def unmarshal_PatRule(data: Any) -> PatRule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PatRule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("gateway_id", str())
    args["gateway_id"] = field

    field = data.get("public_port", 0)
    args["public_port"] = field

    field = data.get("private_ip", str())
    args["private_ip"] = field

    field = data.get("private_port", 0)
    args["private_port"] = field

    field = data.get("protocol", getattr(PatRuleProtocol, "UNKNOWN_PROTOCOL"))
    args["protocol"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return PatRule(**args)

def unmarshal_AddBastionAllowedIPsResponse(data: Any) -> AddBastionAllowedIPsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddBastionAllowedIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip_ranges", [])
    args["ip_ranges"] = field

    return AddBastionAllowedIPsResponse(**args)

def unmarshal_ListGatewayNetworksResponse(data: Any) -> ListGatewayNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListGatewayNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("gateway_networks", [])
    args["gateway_networks"] = [unmarshal_GatewayNetwork(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListGatewayNetworksResponse(**args)

def unmarshal_GatewayType(data: Any) -> GatewayType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GatewayType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("bandwidth", 0)
    args["bandwidth"] = field

    field = data.get("zone", )
    args["zone"] = field

    return GatewayType(**args)

def unmarshal_ListGatewayTypesResponse(data: Any) -> ListGatewayTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListGatewayTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("types", [])
    args["types"] = [unmarshal_GatewayType(v) for v in field] if field is not None else None

    return ListGatewayTypesResponse(**args)

def unmarshal_ListGatewaysResponse(data: Any) -> ListGatewaysResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListGatewaysResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("gateways", [])
    args["gateways"] = [unmarshal_Gateway(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListGatewaysResponse(**args)

def unmarshal_ListIPsResponse(data: Any) -> ListIPsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ips", [])
    args["ips"] = [unmarshal_IP(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListIPsResponse(**args)

def unmarshal_ListPatRulesResponse(data: Any) -> ListPatRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPatRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pat_rules", [])
    args["pat_rules"] = [unmarshal_PatRule(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListPatRulesResponse(**args)

def unmarshal_SetBastionAllowedIPsResponse(data: Any) -> SetBastionAllowedIPsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetBastionAllowedIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip_ranges", [])
    args["ip_ranges"] = field

    return SetBastionAllowedIPsResponse(**args)

def unmarshal_SetPatRulesResponse(data: Any) -> SetPatRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetPatRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pat_rules", [])
    args["pat_rules"] = [unmarshal_PatRule(v) for v in field] if field is not None else None

    return SetPatRulesResponse(**args)

def marshal_AddBastionAllowedIPsRequest(
    request: AddBastionAllowedIPsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip_range is not None:
        output["ip_range"] = request.ip_range
    else:
        output["ip_range"] = str()


    return output

def marshal_CreateGatewayNetworkRequest(
    request: CreateGatewayNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.gateway_id is not None:
        output["gateway_id"] = request.gateway_id
    else:
        output["gateway_id"] = str()

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id
    else:
        output["private_network_id"] = str()

    if request.enable_masquerade is not None:
        output["enable_masquerade"] = request.enable_masquerade
    else:
        output["enable_masquerade"] = False

    if request.push_default_route is not None:
        output["push_default_route"] = request.push_default_route
    else:
        output["push_default_route"] = False

    if request.ipam_ip_id is not None:
        output["ipam_ip_id"] = request.ipam_ip_id
    else:
        output["ipam_ip_id"] = None


    return output

def marshal_CreateGatewayRequest(
    request: CreateGatewayRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_
    else:
        output["type"] = str()

    if request.enable_smtp is not None:
        output["enable_smtp"] = request.enable_smtp
    else:
        output["enable_smtp"] = False

    if request.enable_bastion is not None:
        output["enable_bastion"] = request.enable_bastion
    else:
        output["enable_bastion"] = False

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.ip_id is not None:
        output["ip_id"] = request.ip_id
    else:
        output["ip_id"] = None

    if request.bastion_port is not None:
        output["bastion_port"] = request.bastion_port
    else:
        output["bastion_port"] = None


    return output

def marshal_CreateIPRequest(
    request: CreateIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_CreatePatRuleRequest(
    request: CreatePatRuleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.gateway_id is not None:
        output["gateway_id"] = request.gateway_id
    else:
        output["gateway_id"] = str()

    if request.public_port is not None:
        output["public_port"] = request.public_port
    else:
        output["public_port"] = 0

    if request.private_ip is not None:
        output["private_ip"] = request.private_ip
    else:
        output["private_ip"] = str()

    if request.private_port is not None:
        output["private_port"] = request.private_port
    else:
        output["private_port"] = 0

    if request.protocol is not None:
        output["protocol"] = str(request.protocol)
    else:
        output["protocol"] = None


    return output

def marshal_SetBastionAllowedIPsRequest(
    request: SetBastionAllowedIPsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip_ranges is not None:
        output["ip_ranges"] = request.ip_ranges
    else:
        output["ip_ranges"] = None


    return output

def marshal_SetPatRulesRequestRule(
    request: SetPatRulesRequestRule,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.public_port is not None:
        output["public_port"] = request.public_port
    else:
        output["public_port"] = 0

    if request.private_ip is not None:
        output["private_ip"] = request.private_ip
    else:
        output["private_ip"] = str()

    if request.private_port is not None:
        output["private_port"] = request.private_port
    else:
        output["private_port"] = 0

    if request.protocol is not None:
        output["protocol"] = str(request.protocol)
    else:
        output["protocol"] = getattr(PatRuleProtocol, "UNKNOWN_PROTOCOL")


    return output

def marshal_SetPatRulesRequest(
    request: SetPatRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.gateway_id is not None:
        output["gateway_id"] = request.gateway_id
    else:
        output["gateway_id"] = str()

    if request.pat_rules is not None:
        output["pat_rules"] = [marshal_SetPatRulesRequestRule(item, defaults) for item in request.pat_rules]
    else:
        output["pat_rules"] = str()


    return output

def marshal_UpdateGatewayNetworkRequest(
    request: UpdateGatewayNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.enable_masquerade is not None:
        output["enable_masquerade"] = request.enable_masquerade
    else:
        output["enable_masquerade"] = None

    if request.push_default_route is not None:
        output["push_default_route"] = request.push_default_route
    else:
        output["push_default_route"] = None

    if request.ipam_ip_id is not None:
        output["ipam_ip_id"] = request.ipam_ip_id
    else:
        output["ipam_ip_id"] = None


    return output

def marshal_UpdateGatewayRequest(
    request: UpdateGatewayRequest,
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

    if request.enable_bastion is not None:
        output["enable_bastion"] = request.enable_bastion
    else:
        output["enable_bastion"] = None

    if request.bastion_port is not None:
        output["bastion_port"] = request.bastion_port
    else:
        output["bastion_port"] = None

    if request.enable_smtp is not None:
        output["enable_smtp"] = request.enable_smtp
    else:
        output["enable_smtp"] = None


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

    if request.reverse is not None:
        output["reverse"] = request.reverse
    else:
        output["reverse"] = None

    if request.gateway_id is not None:
        output["gateway_id"] = request.gateway_id
    else:
        output["gateway_id"] = None


    return output

def marshal_UpdatePatRuleRequest(
    request: UpdatePatRuleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.public_port is not None:
        output["public_port"] = request.public_port
    else:
        output["public_port"] = None

    if request.private_ip is not None:
        output["private_ip"] = request.private_ip
    else:
        output["private_ip"] = None

    if request.private_port is not None:
        output["private_port"] = request.private_port
    else:
        output["private_port"] = None

    if request.protocol is not None:
        output["protocol"] = str(request.protocol)
    else:
        output["protocol"] = None


    return output

def marshal_UpgradeGatewayRequest(
    request: UpgradeGatewayRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_
    else:
        output["type"] = None


    return output
