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

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("subnet", None)
    if field is not None:
        args["subnet"] = field

    field = data.get("address", None)
    if field is not None:
        args["address"] = field

    field = data.get("pool_low", None)
    if field is not None:
        args["pool_low"] = field

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

    field = data.get("pool_high", None)
    if field is not None:
        args["pool_high"] = field

    field = data.get("enable_dynamic", None)
    if field is not None:
        args["enable_dynamic"] = field

    field = data.get("push_default_route", None)
    if field is not None:
        args["push_default_route"] = field

    field = data.get("push_dns_server", None)
    if field is not None:
        args["push_dns_server"] = field

    field = data.get("dns_servers_override", None)
    if field is not None:
        args["dns_servers_override"] = field

    field = data.get("dns_search", None)
    if field is not None:
        args["dns_search"] = field

    field = data.get("dns_local_name", None)
    if field is not None:
        args["dns_local_name"] = field

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field

    field = data.get("valid_lifetime", None)
    if field is not None:
        args["valid_lifetime"] = field
    else:
        args["valid_lifetime"] = None

    field = data.get("renew_timer", None)
    if field is not None:
        args["renew_timer"] = field
    else:
        args["renew_timer"] = None

    field = data.get("rebind_timer", None)
    if field is not None:
        args["rebind_timer"] = field
    else:
        args["rebind_timer"] = None

    return DHCP(**args)


def unmarshal_IpamConfig(data: Any) -> IpamConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'IpamConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("push_default_route", None)
    if field is not None:
        args["push_default_route"] = field

    field = data.get("ipam_ip_id", None)
    if field is not None:
        args["ipam_ip_id"] = field

    return IpamConfig(**args)


def unmarshal_GatewayNetwork(data: Any) -> GatewayNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GatewayNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("gateway_id", None)
    if field is not None:
        args["gateway_id"] = field

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field

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

    field = data.get("mac_address", None)
    if field is not None:
        args["mac_address"] = field
    else:
        args["mac_address"] = None

    field = data.get("enable_masquerade", None)
    if field is not None:
        args["enable_masquerade"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("enable_dhcp", None)
    if field is not None:
        args["enable_dhcp"] = field

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field

    field = data.get("dhcp", None)
    if field is not None:
        args["dhcp"] = unmarshal_DHCP(field)
    else:
        args["dhcp"] = None

    field = data.get("address", None)
    if field is not None:
        args["address"] = field
    else:
        args["address"] = None

    field = data.get("ipam_config", None)
    if field is not None:
        args["ipam_config"] = unmarshal_IpamConfig(field)
    else:
        args["ipam_config"] = None

    return GatewayNetwork(**args)


def unmarshal_IP(data: Any) -> IP:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'IP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("address", None)
    if field is not None:
        args["address"] = field

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field

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

    field = data.get("reverse", None)
    if field is not None:
        args["reverse"] = field
    else:
        args["reverse"] = None

    field = data.get("gateway_id", None)
    if field is not None:
        args["gateway_id"] = field
    else:
        args["gateway_id"] = None

    return IP(**args)


def unmarshal_DHCPEntry(data: Any) -> DHCPEntry:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DHCPEntry' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("gateway_network_id", None)
    if field is not None:
        args["gateway_network_id"] = field

    field = data.get("mac_address", None)
    if field is not None:
        args["mac_address"] = field

    field = data.get("ip_address", None)
    if field is not None:
        args["ip_address"] = field

    field = data.get("hostname", None)
    if field is not None:
        args["hostname"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field

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

    return DHCPEntry(**args)


def unmarshal_GatewayType(data: Any) -> GatewayType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GatewayType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("bandwidth", None)
    if field is not None:
        args["bandwidth"] = field

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field

    return GatewayType(**args)


def unmarshal_Gateway(data: Any) -> Gateway:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Gateway' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

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

    field = data.get("type", None)
    if field is not None:
        args["type_"] = unmarshal_GatewayType(field)
    else:
        args["type_"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("gateway_networks", None)
    if field is not None:
        args["gateway_networks"] = (
            [unmarshal_GatewayNetwork(v) for v in field] if field is not None else None
        )

    field = data.get("upstream_dns_servers", None)
    if field is not None:
        args["upstream_dns_servers"] = field

    field = data.get("bastion_enabled", None)
    if field is not None:
        args["bastion_enabled"] = field

    field = data.get("ip", None)
    if field is not None:
        args["ip"] = unmarshal_IP(field)
    else:
        args["ip"] = None

    field = data.get("version", None)
    if field is not None:
        args["version"] = field
    else:
        args["version"] = None

    field = data.get("can_upgrade_to", None)
    if field is not None:
        args["can_upgrade_to"] = field
    else:
        args["can_upgrade_to"] = None

    field = data.get("bastion_port", None)
    if field is not None:
        args["bastion_port"] = field

    field = data.get("smtp_enabled", None)
    if field is not None:
        args["smtp_enabled"] = field

    field = data.get("is_legacy", None)
    if field is not None:
        args["is_legacy"] = field

    field = data.get("ip_mobility_enabled", None)
    if field is not None:
        args["ip_mobility_enabled"] = field

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field

    return Gateway(**args)


def unmarshal_PATRule(data: Any) -> PATRule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PATRule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("gateway_id", None)
    if field is not None:
        args["gateway_id"] = field

    field = data.get("public_port", None)
    if field is not None:
        args["public_port"] = field

    field = data.get("private_ip", None)
    if field is not None:
        args["private_ip"] = field

    field = data.get("private_port", None)
    if field is not None:
        args["private_port"] = field

    field = data.get("protocol", None)
    if field is not None:
        args["protocol"] = field

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field

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

    return PATRule(**args)


def unmarshal_ListDHCPEntriesResponse(data: Any) -> ListDHCPEntriesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDHCPEntriesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dhcp_entries", None)
    if field is not None:
        args["dhcp_entries"] = (
            [unmarshal_DHCPEntry(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListDHCPEntriesResponse(**args)


def unmarshal_ListDHCPsResponse(data: Any) -> ListDHCPsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDHCPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dhcps", None)
    if field is not None:
        args["dhcps"] = (
            [unmarshal_DHCP(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListDHCPsResponse(**args)


def unmarshal_ListGatewayNetworksResponse(data: Any) -> ListGatewayNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListGatewayNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("gateway_networks", None)
    if field is not None:
        args["gateway_networks"] = (
            [unmarshal_GatewayNetwork(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListGatewayNetworksResponse(**args)


def unmarshal_ListGatewayTypesResponse(data: Any) -> ListGatewayTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListGatewayTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("types", None)
    if field is not None:
        args["types"] = (
            [unmarshal_GatewayType(v) for v in field] if field is not None else None
        )

    return ListGatewayTypesResponse(**args)


def unmarshal_ListGatewaysResponse(data: Any) -> ListGatewaysResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListGatewaysResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("gateways", None)
    if field is not None:
        args["gateways"] = (
            [unmarshal_Gateway(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListGatewaysResponse(**args)


def unmarshal_ListIPsResponse(data: Any) -> ListIPsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ips", None)
    if field is not None:
        args["ips"] = [unmarshal_IP(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListIPsResponse(**args)


def unmarshal_ListPATRulesResponse(data: Any) -> ListPATRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPATRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pat_rules", None)
    if field is not None:
        args["pat_rules"] = (
            [unmarshal_PATRule(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListPATRulesResponse(**args)


def unmarshal_SetDHCPEntriesResponse(data: Any) -> SetDHCPEntriesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetDHCPEntriesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dhcp_entries", None)
    if field is not None:
        args["dhcp_entries"] = (
            [unmarshal_DHCPEntry(v) for v in field] if field is not None else None
        )

    return SetDHCPEntriesResponse(**args)


def unmarshal_SetPATRulesResponse(data: Any) -> SetPATRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetPATRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pat_rules", None)
    if field is not None:
        args["pat_rules"] = (
            [unmarshal_PATRule(v) for v in field] if field is not None else None
        )

    return SetPATRulesResponse(**args)


def marshal_CreateDHCPRequest(
    request: CreateDHCPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.subnet is not None:
        output["subnet"] = request.subnet

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.address is not None:
        output["address"] = request.address

    if request.pool_low is not None:
        output["pool_low"] = request.pool_low

    if request.pool_high is not None:
        output["pool_high"] = request.pool_high

    if request.enable_dynamic is not None:
        output["enable_dynamic"] = request.enable_dynamic

    if request.valid_lifetime is not None:
        output["valid_lifetime"] = request.valid_lifetime

    if request.renew_timer is not None:
        output["renew_timer"] = request.renew_timer

    if request.rebind_timer is not None:
        output["rebind_timer"] = request.rebind_timer

    if request.push_default_route is not None:
        output["push_default_route"] = request.push_default_route

    if request.push_dns_server is not None:
        output["push_dns_server"] = request.push_dns_server

    if request.dns_servers_override is not None:
        output["dns_servers_override"] = request.dns_servers_override

    if request.dns_search is not None:
        output["dns_search"] = request.dns_search

    if request.dns_local_name is not None:
        output["dns_local_name"] = request.dns_local_name

    return output


def marshal_CreateDHCPEntryRequest(
    request: CreateDHCPEntryRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.gateway_network_id is not None:
        output["gateway_network_id"] = request.gateway_network_id

    if request.mac_address is not None:
        output["mac_address"] = request.mac_address

    if request.ip_address is not None:
        output["ip_address"] = request.ip_address

    return output


def marshal_CreateGatewayNetworkRequestIpamConfig(
    request: CreateGatewayNetworkRequestIpamConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.push_default_route is not None:
        output["push_default_route"] = request.push_default_route

    if request.ipam_ip_id is not None:
        output["ipam_ip_id"] = request.ipam_ip_id

    return output


def marshal_CreateGatewayNetworkRequest(
    request: CreateGatewayNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("dhcp_id", request.dhcp_id),
                OneOfPossibility("dhcp", request.dhcp),
                OneOfPossibility("address", request.address),
                OneOfPossibility("ipam_config", request.ipam_config),
            ]
        ),
    )

    if request.gateway_id is not None:
        output["gateway_id"] = request.gateway_id

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    if request.enable_masquerade is not None:
        output["enable_masquerade"] = request.enable_masquerade

    if request.enable_dhcp is not None:
        output["enable_dhcp"] = request.enable_dhcp

    return output


def marshal_CreateGatewayRequest(
    request: CreateGatewayRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    if request.enable_smtp is not None:
        output["enable_smtp"] = request.enable_smtp

    if request.enable_bastion is not None:
        output["enable_bastion"] = request.enable_bastion

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.upstream_dns_servers is not None:
        output["upstream_dns_servers"] = request.upstream_dns_servers

    if request.ip_id is not None:
        output["ip_id"] = request.ip_id

    if request.bastion_port is not None:
        output["bastion_port"] = request.bastion_port

    return output


def marshal_CreateIPRequest(
    request: CreateIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreatePATRuleRequest(
    request: CreatePATRuleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.gateway_id is not None:
        output["gateway_id"] = request.gateway_id

    if request.public_port is not None:
        output["public_port"] = request.public_port

    if request.private_ip is not None:
        output["private_ip"] = request.private_ip

    if request.private_port is not None:
        output["private_port"] = request.private_port

    if request.protocol is not None:
        output["protocol"] = str(request.protocol)

    return output


def marshal_SetDHCPEntriesRequestEntry(
    request: SetDHCPEntriesRequestEntry,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.mac_address is not None:
        output["mac_address"] = request.mac_address

    if request.ip_address is not None:
        output["ip_address"] = request.ip_address

    return output


def marshal_SetDHCPEntriesRequest(
    request: SetDHCPEntriesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.gateway_network_id is not None:
        output["gateway_network_id"] = request.gateway_network_id

    if request.dhcp_entries is not None:
        output["dhcp_entries"] = [
            marshal_SetDHCPEntriesRequestEntry(item, defaults)
            for item in request.dhcp_entries
        ]

    return output


def marshal_SetPATRulesRequestRule(
    request: SetPATRulesRequestRule,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.public_port is not None:
        output["public_port"] = request.public_port

    if request.private_ip is not None:
        output["private_ip"] = request.private_ip

    if request.private_port is not None:
        output["private_port"] = request.private_port

    if request.protocol is not None:
        output["protocol"] = str(request.protocol)

    return output


def marshal_SetPATRulesRequest(
    request: SetPATRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.gateway_id is not None:
        output["gateway_id"] = request.gateway_id

    if request.pat_rules is not None:
        output["pat_rules"] = [
            marshal_SetPATRulesRequestRule(item, defaults) for item in request.pat_rules
        ]

    return output


def marshal_UpdateDHCPEntryRequest(
    request: UpdateDHCPEntryRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip_address is not None:
        output["ip_address"] = request.ip_address

    return output


def marshal_UpdateDHCPRequest(
    request: UpdateDHCPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.subnet is not None:
        output["subnet"] = request.subnet

    if request.address is not None:
        output["address"] = request.address

    if request.pool_low is not None:
        output["pool_low"] = request.pool_low

    if request.pool_high is not None:
        output["pool_high"] = request.pool_high

    if request.enable_dynamic is not None:
        output["enable_dynamic"] = request.enable_dynamic

    if request.valid_lifetime is not None:
        output["valid_lifetime"] = request.valid_lifetime

    if request.renew_timer is not None:
        output["renew_timer"] = request.renew_timer

    if request.rebind_timer is not None:
        output["rebind_timer"] = request.rebind_timer

    if request.push_default_route is not None:
        output["push_default_route"] = request.push_default_route

    if request.push_dns_server is not None:
        output["push_dns_server"] = request.push_dns_server

    if request.dns_servers_override is not None:
        output["dns_servers_override"] = request.dns_servers_override

    if request.dns_search is not None:
        output["dns_search"] = request.dns_search

    if request.dns_local_name is not None:
        output["dns_local_name"] = request.dns_local_name

    return output


def marshal_UpdateGatewayNetworkRequestIpamConfig(
    request: UpdateGatewayNetworkRequestIpamConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.push_default_route is not None:
        output["push_default_route"] = request.push_default_route

    if request.ipam_ip_id is not None:
        output["ipam_ip_id"] = request.ipam_ip_id

    return output


def marshal_UpdateGatewayNetworkRequest(
    request: UpdateGatewayNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("dhcp_id", request.dhcp_id),
                OneOfPossibility("address", request.address),
                OneOfPossibility("ipam_config", request.ipam_config),
            ]
        ),
    )

    if request.enable_masquerade is not None:
        output["enable_masquerade"] = request.enable_masquerade

    if request.enable_dhcp is not None:
        output["enable_dhcp"] = request.enable_dhcp

    return output


def marshal_UpdateGatewayRequest(
    request: UpdateGatewayRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.upstream_dns_servers is not None:
        output["upstream_dns_servers"] = request.upstream_dns_servers

    if request.enable_bastion is not None:
        output["enable_bastion"] = request.enable_bastion

    if request.bastion_port is not None:
        output["bastion_port"] = request.bastion_port

    if request.enable_smtp is not None:
        output["enable_smtp"] = request.enable_smtp

    return output


def marshal_UpdateIPRequest(
    request: UpdateIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.tags is not None:
        output["tags"] = request.tags

    if request.reverse is not None:
        output["reverse"] = request.reverse

    if request.gateway_id is not None:
        output["gateway_id"] = request.gateway_id

    return output


def marshal_UpdatePATRuleRequest(
    request: UpdatePATRuleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.public_port is not None:
        output["public_port"] = request.public_port

    if request.private_ip is not None:
        output["private_ip"] = request.private_ip

    if request.private_port is not None:
        output["private_port"] = request.private_port

    if request.protocol is not None:
        output["protocol"] = str(request.protocol)

    return output


def marshal_UpgradeGatewayRequest(
    request: UpgradeGatewayRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    return output
