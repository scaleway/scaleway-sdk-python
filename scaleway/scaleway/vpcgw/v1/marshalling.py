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
    DHCPEntryType,
    GatewayNetworkStatus,
    GatewayStatus,
    ListDHCPEntriesRequestOrderBy,
    ListDHCPsRequestOrderBy,
    ListGatewayNetworksRequestOrderBy,
    ListGatewaysRequestOrderBy,
    ListIPsRequestOrderBy,
    ListPATRulesRequestOrderBy,
    PATRuleProtocol,
    DHCP,
    IpamConfig,
    GatewayNetwork,
    IP,
    DHCPEntry,
    GatewayType,
    Gateway,
    PATRule,
    ListDHCPEntriesResponse,
    ListDHCPsResponse,
    ListGatewayNetworksResponse,
    ListGatewayTypesResponse,
    ListGatewaysResponse,
    ListIPsResponse,
    ListPATRulesResponse,
    SetDHCPEntriesResponse,
    SetPATRulesResponse,
    CreateDHCPRequest,
    CreateDHCPEntryRequest,
    CreateGatewayNetworkRequestIpamConfig,
    CreateGatewayNetworkRequest,
    CreateGatewayRequest,
    CreateIPRequest,
    CreatePATRuleRequest,
    SetDHCPEntriesRequestEntry,
    SetDHCPEntriesRequest,
    SetPATRulesRequestRule,
    SetPATRulesRequest,
    UpdateDHCPEntryRequest,
    UpdateDHCPRequest,
    UpdateGatewayNetworkRequestIpamConfig,
    UpdateGatewayNetworkRequest,
    UpdateGatewayRequest,
    UpdateIPRequest,
    UpdatePATRuleRequest,
    UpgradeGatewayRequest,
)

def unmarshal_DHCP(data: Any) -> DHCP:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DHCP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("subnet", str())
    args["subnet"] = field

    field = data.get("address", str())
    args["address"] = field

    field = data.get("pool_low", str())
    args["pool_low"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("pool_high", str())
    args["pool_high"] = field

    field = data.get("enable_dynamic", False)
    args["enable_dynamic"] = field

    field = data.get("push_default_route", False)
    args["push_default_route"] = field

    field = data.get("push_dns_server", False)
    args["push_dns_server"] = field

    field = data.get("dns_servers_override", [])
    args["dns_servers_override"] = field

    field = data.get("dns_search", [])
    args["dns_search"] = field

    field = data.get("dns_local_name", str())
    args["dns_local_name"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("valid_lifetime", None)
    args["valid_lifetime"] = field

    field = data.get("renew_timer", None)
    args["renew_timer"] = field

    field = data.get("rebind_timer", None)
    args["rebind_timer"] = field

    return DHCP(**args)

def unmarshal_IpamConfig(data: Any) -> IpamConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'IpamConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("push_default_route", False)
    args["push_default_route"] = field

    field = data.get("ipam_ip_id", str())
    args["ipam_ip_id"] = field

    return IpamConfig(**args)

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

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("mac_address", None)
    args["mac_address"] = field

    field = data.get("enable_masquerade", False)
    args["enable_masquerade"] = field

    field = data.get("status", getattr(GatewayNetworkStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("enable_dhcp", False)
    args["enable_dhcp"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("dhcp", None)
    args["dhcp"] = unmarshal_DHCP(field) if field is not None else None

    field = data.get("address", None)
    args["address"] = field

    field = data.get("ipam_config", None)
    args["ipam_config"] = unmarshal_IpamConfig(field) if field is not None else None

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

def unmarshal_DHCPEntry(data: Any) -> DHCPEntry:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DHCPEntry' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("gateway_network_id", str())
    args["gateway_network_id"] = field

    field = data.get("mac_address", str())
    args["mac_address"] = field

    field = data.get("ip_address", str())
    args["ip_address"] = field

    field = data.get("hostname", str())
    args["hostname"] = field

    field = data.get("type", getattr(DHCPEntryType, "UNKNOWN"))
    args["type_"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return DHCPEntry(**args)

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

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("type", None)
    args["type_"] = unmarshal_GatewayType(field) if field is not None else None

    field = data.get("status", getattr(GatewayStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("gateway_networks", [])
    args["gateway_networks"] = [unmarshal_GatewayNetwork(v) for v in field] if field is not None else None

    field = data.get("upstream_dns_servers", [])
    args["upstream_dns_servers"] = field

    field = data.get("bastion_enabled", False)
    args["bastion_enabled"] = field

    field = data.get("ip", None)
    args["ip"] = unmarshal_IP(field) if field is not None else None

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

    field = data.get("ip_mobility_enabled", False)
    args["ip_mobility_enabled"] = field

    field = data.get("zone", )
    args["zone"] = field

    return Gateway(**args)

def unmarshal_PATRule(data: Any) -> PATRule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PATRule' failed as data isn't a dictionary."
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

    field = data.get("protocol", getattr(PATRuleProtocol, "UNKNOWN"))
    args["protocol"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return PATRule(**args)

def unmarshal_ListDHCPEntriesResponse(data: Any) -> ListDHCPEntriesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDHCPEntriesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dhcp_entries", [])
    args["dhcp_entries"] = [unmarshal_DHCPEntry(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListDHCPEntriesResponse(**args)

def unmarshal_ListDHCPsResponse(data: Any) -> ListDHCPsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDHCPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dhcps", [])
    args["dhcps"] = [unmarshal_DHCP(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListDHCPsResponse(**args)

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

def unmarshal_ListPATRulesResponse(data: Any) -> ListPATRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPATRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pat_rules", [])
    args["pat_rules"] = [unmarshal_PATRule(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListPATRulesResponse(**args)

def unmarshal_SetDHCPEntriesResponse(data: Any) -> SetDHCPEntriesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetDHCPEntriesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dhcp_entries", [])
    args["dhcp_entries"] = [unmarshal_DHCPEntry(v) for v in field] if field is not None else None

    return SetDHCPEntriesResponse(**args)

def unmarshal_SetPATRulesResponse(data: Any) -> SetPATRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetPATRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pat_rules", [])
    args["pat_rules"] = [unmarshal_PATRule(v) for v in field] if field is not None else None

    return SetPATRulesResponse(**args)

def marshal_CreateDHCPRequest(
    request: CreateDHCPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.subnet is not None:
        output["subnet"] = request.subnet
    else:
        output["subnet"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.address is not None:
        output["address"] = request.address
    else:
        output["address"] = None

    if request.pool_low is not None:
        output["pool_low"] = request.pool_low
    else:
        output["pool_low"] = None

    if request.pool_high is not None:
        output["pool_high"] = request.pool_high
    else:
        output["pool_high"] = None

    if request.enable_dynamic is not None:
        output["enable_dynamic"] = request.enable_dynamic
    else:
        output["enable_dynamic"] = None

    if request.valid_lifetime is not None:
        output["valid_lifetime"] = request.valid_lifetime
    else:
        output["valid_lifetime"] = None

    if request.renew_timer is not None:
        output["renew_timer"] = request.renew_timer
    else:
        output["renew_timer"] = None

    if request.rebind_timer is not None:
        output["rebind_timer"] = request.rebind_timer
    else:
        output["rebind_timer"] = None

    if request.push_default_route is not None:
        output["push_default_route"] = request.push_default_route
    else:
        output["push_default_route"] = None

    if request.push_dns_server is not None:
        output["push_dns_server"] = request.push_dns_server
    else:
        output["push_dns_server"] = None

    if request.dns_servers_override is not None:
        output["dns_servers_override"] = request.dns_servers_override
    else:
        output["dns_servers_override"] = None

    if request.dns_search is not None:
        output["dns_search"] = request.dns_search
    else:
        output["dns_search"] = None

    if request.dns_local_name is not None:
        output["dns_local_name"] = request.dns_local_name
    else:
        output["dns_local_name"] = None


    return output

def marshal_CreateDHCPEntryRequest(
    request: CreateDHCPEntryRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.gateway_network_id is not None:
        output["gateway_network_id"] = request.gateway_network_id
    else:
        output["gateway_network_id"] = str()

    if request.mac_address is not None:
        output["mac_address"] = request.mac_address
    else:
        output["mac_address"] = str()

    if request.ip_address is not None:
        output["ip_address"] = request.ip_address
    else:
        output["ip_address"] = str()


    return output

def marshal_CreateGatewayNetworkRequestIpamConfig(
    request: CreateGatewayNetworkRequestIpamConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.push_default_route is not None:
        output["push_default_route"] = request.push_default_route
    else:
        output["push_default_route"] = False

    if request.ipam_ip_id is not None:
        output["ipam_ip_id"] = request.ipam_ip_id
    else:
        output["ipam_ip_id"] = None


    return output

def marshal_CreateGatewayNetworkRequest(
    request: CreateGatewayNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="dhcp_id", value=request.dhcp_id,marshal_func=None
            ),
            OneOfPossibility(param="dhcp", value=request.dhcp,marshal_func=marshal_CreateDHCPRequest
            ),
            OneOfPossibility(param="address", value=request.address,marshal_func=None
            ),
            OneOfPossibility(param="ipam_config", value=request.ipam_config,marshal_func=marshal_CreateGatewayNetworkRequestIpamConfig
            ),
        ]),
    )

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

    if request.enable_dhcp is not None:
        output["enable_dhcp"] = request.enable_dhcp
    else:
        output["enable_dhcp"] = None


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

    if request.upstream_dns_servers is not None:
        output["upstream_dns_servers"] = request.upstream_dns_servers
    else:
        output["upstream_dns_servers"] = None

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

def marshal_CreatePATRuleRequest(
    request: CreatePATRuleRequest,
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

def marshal_SetDHCPEntriesRequestEntry(
    request: SetDHCPEntriesRequestEntry,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.mac_address is not None:
        output["mac_address"] = request.mac_address
    else:
        output["mac_address"] = str()

    if request.ip_address is not None:
        output["ip_address"] = request.ip_address
    else:
        output["ip_address"] = str()


    return output

def marshal_SetDHCPEntriesRequest(
    request: SetDHCPEntriesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.gateway_network_id is not None:
        output["gateway_network_id"] = request.gateway_network_id
    else:
        output["gateway_network_id"] = str()

    if request.dhcp_entries is not None:
        output["dhcp_entries"] = [marshal_SetDHCPEntriesRequestEntry(item, defaults) for item in request.dhcp_entries]
    else:
        output["dhcp_entries"] = None


    return output

def marshal_SetPATRulesRequestRule(
    request: SetPATRulesRequestRule,
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
        output["protocol"] = getattr(PATRuleProtocol, "UNKNOWN")


    return output

def marshal_SetPATRulesRequest(
    request: SetPATRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.gateway_id is not None:
        output["gateway_id"] = request.gateway_id
    else:
        output["gateway_id"] = str()

    if request.pat_rules is not None:
        output["pat_rules"] = [marshal_SetPATRulesRequestRule(item, defaults) for item in request.pat_rules]
    else:
        output["pat_rules"] = str()


    return output

def marshal_UpdateDHCPEntryRequest(
    request: UpdateDHCPEntryRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip_address is not None:
        output["ip_address"] = request.ip_address
    else:
        output["ip_address"] = None


    return output

def marshal_UpdateDHCPRequest(
    request: UpdateDHCPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.subnet is not None:
        output["subnet"] = request.subnet
    else:
        output["subnet"] = None

    if request.address is not None:
        output["address"] = request.address
    else:
        output["address"] = None

    if request.pool_low is not None:
        output["pool_low"] = request.pool_low
    else:
        output["pool_low"] = None

    if request.pool_high is not None:
        output["pool_high"] = request.pool_high
    else:
        output["pool_high"] = None

    if request.enable_dynamic is not None:
        output["enable_dynamic"] = request.enable_dynamic
    else:
        output["enable_dynamic"] = None

    if request.valid_lifetime is not None:
        output["valid_lifetime"] = request.valid_lifetime
    else:
        output["valid_lifetime"] = None

    if request.renew_timer is not None:
        output["renew_timer"] = request.renew_timer
    else:
        output["renew_timer"] = None

    if request.rebind_timer is not None:
        output["rebind_timer"] = request.rebind_timer
    else:
        output["rebind_timer"] = None

    if request.push_default_route is not None:
        output["push_default_route"] = request.push_default_route
    else:
        output["push_default_route"] = None

    if request.push_dns_server is not None:
        output["push_dns_server"] = request.push_dns_server
    else:
        output["push_dns_server"] = None

    if request.dns_servers_override is not None:
        output["dns_servers_override"] = request.dns_servers_override
    else:
        output["dns_servers_override"] = None

    if request.dns_search is not None:
        output["dns_search"] = request.dns_search
    else:
        output["dns_search"] = None

    if request.dns_local_name is not None:
        output["dns_local_name"] = request.dns_local_name
    else:
        output["dns_local_name"] = None


    return output

def marshal_UpdateGatewayNetworkRequestIpamConfig(
    request: UpdateGatewayNetworkRequestIpamConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.push_default_route is not None:
        output["push_default_route"] = request.push_default_route
    else:
        output["push_default_route"] = None

    if request.ipam_ip_id is not None:
        output["ipam_ip_id"] = request.ipam_ip_id
    else:
        output["ipam_ip_id"] = None


    return output

def marshal_UpdateGatewayNetworkRequest(
    request: UpdateGatewayNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="dhcp_id", value=request.dhcp_id,marshal_func=None
            ),
            OneOfPossibility(param="address", value=request.address,marshal_func=None
            ),
            OneOfPossibility(param="ipam_config", value=request.ipam_config,marshal_func=marshal_UpdateGatewayNetworkRequestIpamConfig
            ),
        ]),
    )

    if request.enable_masquerade is not None:
        output["enable_masquerade"] = request.enable_masquerade
    else:
        output["enable_masquerade"] = None

    if request.enable_dhcp is not None:
        output["enable_dhcp"] = request.enable_dhcp
    else:
        output["enable_dhcp"] = None


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

    if request.upstream_dns_servers is not None:
        output["upstream_dns_servers"] = request.upstream_dns_servers
    else:
        output["upstream_dns_servers"] = None

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

def marshal_UpdatePATRuleRequest(
    request: UpdatePATRuleRequest,
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
