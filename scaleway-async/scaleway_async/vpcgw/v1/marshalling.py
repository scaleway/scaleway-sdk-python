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
    PATRuleProtocol,
    DHCP,
    DHCPEntry,
    Gateway,
    GatewayNetwork,
    GatewayType,
    IP,
    ListDHCPEntriesResponse,
    ListDHCPsResponse,
    ListGatewayNetworksResponse,
    ListGatewayTypesResponse,
    ListGatewaysResponse,
    ListIPsResponse,
    ListPATRulesResponse,
    PATRule,
    SetDHCPEntriesRequestEntry,
    SetDHCPEntriesResponse,
    SetPATRulesRequestRule,
    SetPATRulesResponse,
    CreateGatewayRequest,
    UpdateGatewayRequest,
    CreateGatewayNetworkRequest,
    UpdateGatewayNetworkRequest,
    CreateDHCPRequest,
    UpdateDHCPRequest,
    CreateDHCPEntryRequest,
    UpdateDHCPEntryRequest,
    SetDHCPEntriesRequest,
    CreatePATRuleRequest,
    UpdatePATRuleRequest,
    SetPATRulesRequest,
    CreateIPRequest,
    UpdateIPRequest,
)


def unmarshal_DHCP(data: Any) -> DHCP:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DHCP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("address")
    args["address"] = field

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("dns_local_name")
    args["dns_local_name"] = field

    field = data.get("dns_search")
    args["dns_search"] = field

    field = data.get("dns_servers_override")
    args["dns_servers_override"] = field

    field = data.get("enable_dynamic")
    args["enable_dynamic"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("pool_high")
    args["pool_high"] = field

    field = data.get("pool_low")
    args["pool_low"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("push_default_route")
    args["push_default_route"] = field

    field = data.get("push_dns_server")
    args["push_dns_server"] = field

    field = data.get("rebind_timer")
    args["rebind_timer"] = field

    field = data.get("renew_timer")
    args["renew_timer"] = field

    field = data.get("subnet")
    args["subnet"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("valid_lifetime")
    args["valid_lifetime"] = field

    field = data.get("zone")
    args["zone"] = field

    return DHCP(**args)


def unmarshal_GatewayNetwork(data: Any) -> GatewayNetwork:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GatewayNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("address")
    args["address"] = field

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("dhcp")
    args["dhcp"] = unmarshal_DHCP(field) if field is not None else None

    field = data.get("enable_dhcp")
    args["enable_dhcp"] = field

    field = data.get("enable_masquerade")
    args["enable_masquerade"] = field

    field = data.get("gateway_id")
    args["gateway_id"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("mac_address")
    args["mac_address"] = field

    field = data.get("private_network_id")
    args["private_network_id"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("zone")
    args["zone"] = field

    return GatewayNetwork(**args)


def unmarshal_GatewayType(data: Any) -> GatewayType:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GatewayType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("bandwidth")
    args["bandwidth"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("zone")
    args["zone"] = field

    return GatewayType(**args)


def unmarshal_IP(data: Any) -> IP:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'IP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("address")
    args["address"] = field

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("gateway_id")
    args["gateway_id"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("reverse")
    args["reverse"] = field

    field = data.get("tags")
    args["tags"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("zone")
    args["zone"] = field

    return IP(**args)


def unmarshal_DHCPEntry(data: Any) -> DHCPEntry:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DHCPEntry' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("gateway_network_id")
    args["gateway_network_id"] = field

    field = data.get("hostname")
    args["hostname"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("ip_address")
    args["ip_address"] = field

    field = data.get("mac_address")
    args["mac_address"] = field

    field = data.get("type_")
    args["type_"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("zone")
    args["zone"] = field

    return DHCPEntry(**args)


def unmarshal_Gateway(data: Any) -> Gateway:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Gateway' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("bastion_enabled")
    args["bastion_enabled"] = field

    field = data.get("bastion_port")
    args["bastion_port"] = field

    field = data.get("can_upgrade_to")
    args["can_upgrade_to"] = field

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("gateway_networks")
    args["gateway_networks"] = [
        unmarshal_GatewayNetwork(v) for v in data["gateway_networks"]
    ]

    field = data.get("id")
    args["id"] = field

    field = data.get("ip")
    args["ip"] = unmarshal_IP(field) if field is not None else None

    field = data.get("name")
    args["name"] = field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("smtp_enabled")
    args["smtp_enabled"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("tags")
    args["tags"] = field

    field = data.get("type_")
    args["type_"] = unmarshal_GatewayType(field) if field is not None else None

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("upstream_dns_servers")
    args["upstream_dns_servers"] = field

    field = data.get("version")
    args["version"] = field

    field = data.get("zone")
    args["zone"] = field

    return Gateway(**args)


def unmarshal_PATRule(data: Any) -> PATRule:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'PATRule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("gateway_id")
    args["gateway_id"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("private_ip")
    args["private_ip"] = field

    field = data.get("private_port")
    args["private_port"] = field

    field = data.get("protocol")
    args["protocol"] = field

    field = data.get("public_port")
    args["public_port"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("zone")
    args["zone"] = field

    return PATRule(**args)


def unmarshal_ListDHCPEntriesResponse(data: Any) -> ListDHCPEntriesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDHCPEntriesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dhcp_entries")
    args["dhcp_entries"] = [unmarshal_DHCPEntry(v) for v in data["dhcp_entries"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListDHCPEntriesResponse(**args)


def unmarshal_ListDHCPsResponse(data: Any) -> ListDHCPsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDHCPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dhcps")
    args["dhcps"] = [unmarshal_DHCP(v) for v in data["dhcps"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListDHCPsResponse(**args)


def unmarshal_ListGatewayNetworksResponse(data: Any) -> ListGatewayNetworksResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListGatewayNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("gateway_networks")
    args["gateway_networks"] = [
        unmarshal_GatewayNetwork(v) for v in data["gateway_networks"]
    ]

    field = data.get("total_count")
    args["total_count"] = field

    return ListGatewayNetworksResponse(**args)


def unmarshal_ListGatewayTypesResponse(data: Any) -> ListGatewayTypesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListGatewayTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("types")
    args["types"] = [unmarshal_GatewayType(v) for v in data["types"]]

    return ListGatewayTypesResponse(**args)


def unmarshal_ListGatewaysResponse(data: Any) -> ListGatewaysResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListGatewaysResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("gateways")
    args["gateways"] = [unmarshal_Gateway(v) for v in data["gateways"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListGatewaysResponse(**args)


def unmarshal_ListIPsResponse(data: Any) -> ListIPsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ips")
    args["ips"] = [unmarshal_IP(v) for v in data["ips"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListIPsResponse(**args)


def unmarshal_ListPATRulesResponse(data: Any) -> ListPATRulesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListPATRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pat_rules")
    args["pat_rules"] = [unmarshal_PATRule(v) for v in data["pat_rules"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListPATRulesResponse(**args)


def unmarshal_SetDHCPEntriesResponse(data: Any) -> SetDHCPEntriesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SetDHCPEntriesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dhcp_entries")
    args["dhcp_entries"] = [unmarshal_DHCPEntry(v) for v in data["dhcp_entries"]]

    return SetDHCPEntriesResponse(**args)


def unmarshal_SetPATRulesResponse(data: Any) -> SetPATRulesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SetPATRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pat_rules")
    args["pat_rules"] = [unmarshal_PATRule(v) for v in data["pat_rules"]]

    return SetPATRulesResponse(**args)


def marshal_SetDHCPEntriesRequestEntry(
    request: SetDHCPEntriesRequestEntry,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "ip_address": request.ip_address,
        "mac_address": request.mac_address,
    }


def marshal_SetPATRulesRequestRule(
    request: SetPATRulesRequestRule,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "private_ip": request.private_ip,
        "private_port": request.private_port,
        "protocol": PATRuleProtocol(request.protocol),
        "public_port": request.public_port,
    }


def marshal_CreateDHCPEntryRequest(
    request: CreateDHCPEntryRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "gateway_network_id": request.gateway_network_id,
        "ip_address": request.ip_address,
        "mac_address": request.mac_address,
    }


def marshal_CreateDHCPRequest(
    request: CreateDHCPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "address": request.address,
        "dns_local_name": request.dns_local_name,
        "dns_search": request.dns_search,
        "dns_servers_override": request.dns_servers_override,
        "enable_dynamic": request.enable_dynamic,
        "pool_high": request.pool_high,
        "pool_low": request.pool_low,
        "project_id": request.project_id or defaults.default_project_id,
        "push_default_route": request.push_default_route,
        "push_dns_server": request.push_dns_server,
        "rebind_timer": request.rebind_timer,
        "renew_timer": request.renew_timer,
        "subnet": request.subnet,
        "valid_lifetime": request.valid_lifetime,
    }


def marshal_CreateGatewayNetworkRequest(
    request: CreateGatewayNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("dhcp_id", request.dhcp_id),
                OneOfPossibility("address", request.address),
            ]
        ),
        "enable_dhcp": request.enable_dhcp,
        "enable_masquerade": request.enable_masquerade,
        "gateway_id": request.gateway_id,
        "private_network_id": request.private_network_id,
    }


def marshal_CreateGatewayRequest(
    request: CreateGatewayRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "bastion_port": request.bastion_port,
        "enable_bastion": request.enable_bastion,
        "enable_smtp": request.enable_smtp,
        "ip_id": request.ip_id,
        "name": request.name,
        "project_id": request.project_id or defaults.default_project_id,
        "tags": request.tags,
        "type": request.type_,
        "upstream_dns_servers": request.upstream_dns_servers,
    }


def marshal_CreateIPRequest(
    request: CreateIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "project_id": request.project_id or defaults.default_project_id,
        "tags": request.tags,
    }


def marshal_CreatePATRuleRequest(
    request: CreatePATRuleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "gateway_id": request.gateway_id,
        "private_ip": request.private_ip,
        "private_port": request.private_port,
        "protocol": PATRuleProtocol(request.protocol),
        "public_port": request.public_port,
    }


def marshal_SetDHCPEntriesRequest(
    request: SetDHCPEntriesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "dhcp_entries": [
            marshal_SetDHCPEntriesRequestEntry(v, defaults)
            for v in request.dhcp_entries
        ]
        if request.dhcp_entries is not None
        else None,
        "gateway_network_id": request.gateway_network_id,
    }


def marshal_SetPATRulesRequest(
    request: SetPATRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "gateway_id": request.gateway_id,
        "pat_rules": [
            marshal_SetPATRulesRequestRule(v, defaults) for v in request.pat_rules
        ],
    }


def marshal_UpdateDHCPEntryRequest(
    request: UpdateDHCPEntryRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "ip_address": request.ip_address,
    }


def marshal_UpdateDHCPRequest(
    request: UpdateDHCPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "address": request.address,
        "dns_local_name": request.dns_local_name,
        "dns_search": request.dns_search,
        "dns_servers_override": request.dns_servers_override,
        "enable_dynamic": request.enable_dynamic,
        "pool_high": request.pool_high,
        "pool_low": request.pool_low,
        "push_default_route": request.push_default_route,
        "push_dns_server": request.push_dns_server,
        "rebind_timer": request.rebind_timer,
        "renew_timer": request.renew_timer,
        "subnet": request.subnet,
        "valid_lifetime": request.valid_lifetime,
    }


def marshal_UpdateGatewayNetworkRequest(
    request: UpdateGatewayNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("dhcp_id", request.dhcp_id),
                OneOfPossibility("address", request.address),
            ]
        ),
        "enable_dhcp": request.enable_dhcp,
        "enable_masquerade": request.enable_masquerade,
    }


def marshal_UpdateGatewayRequest(
    request: UpdateGatewayRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "bastion_port": request.bastion_port,
        "enable_bastion": request.enable_bastion,
        "enable_smtp": request.enable_smtp,
        "name": request.name,
        "tags": request.tags,
        "upstream_dns_servers": request.upstream_dns_servers,
    }


def marshal_UpdateIPRequest(
    request: UpdateIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "gateway_id": request.gateway_id,
        "reverse": request.reverse,
        "tags": request.tags,
    }


def marshal_UpdatePATRuleRequest(
    request: UpdatePATRuleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "private_ip": request.private_ip,
        "private_port": request.private_port,
        "protocol": PATRuleProtocol(request.protocol),
        "public_port": request.public_port,
    }
