# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
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

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("gateway_id", None)
    if field is not None:
        args["gateway_id"] = field

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field

    field = data.get("masquerade_enabled", None)
    if field is not None:
        args["masquerade_enabled"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("push_default_route", None)
    if field is not None:
        args["push_default_route"] = field

    field = data.get("ipam_ip_id", None)
    if field is not None:
        args["ipam_ip_id"] = field

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

    field = data.get("mac_address", None)
    if field is not None:
        args["mac_address"] = field
    else:
        args["mac_address"] = None

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

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("bandwidth", None)
    if field is not None:
        args["bandwidth"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

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

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("gateway_networks", None)
    if field is not None:
        args["gateway_networks"] = (
            [unmarshal_GatewayNetwork(v) for v in field] if field is not None else None
        )

    field = data.get("bastion_enabled", None)
    if field is not None:
        args["bastion_enabled"] = field

    field = data.get("ipv4", None)
    if field is not None:
        args["ipv4"] = unmarshal_IP(field)
    else:
        args["ipv4"] = None

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

    field = data.get("bastion_allowed_ips", None)
    if field is not None:
        args["bastion_allowed_ips"] = field

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field

    return Gateway(**args)


def unmarshal_PatRule(data: Any) -> PatRule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PatRule' failed as data isn't a dictionary."
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

    return PatRule(**args)


def unmarshal_AddBastionAllowedIPsResponse(data: Any) -> AddBastionAllowedIPsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddBastionAllowedIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip_ranges", None)
    if field is not None:
        args["ip_ranges"] = field

    return AddBastionAllowedIPsResponse(**args)


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


def unmarshal_ListPatRulesResponse(data: Any) -> ListPatRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPatRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pat_rules", None)
    if field is not None:
        args["pat_rules"] = (
            [unmarshal_PatRule(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListPatRulesResponse(**args)


def unmarshal_SetBastionAllowedIPsResponse(data: Any) -> SetBastionAllowedIPsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetBastionAllowedIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip_ranges", None)
    if field is not None:
        args["ip_ranges"] = field

    return SetBastionAllowedIPsResponse(**args)


def unmarshal_SetPatRulesResponse(data: Any) -> SetPatRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetPatRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pat_rules", None)
    if field is not None:
        args["pat_rules"] = (
            [unmarshal_PatRule(v) for v in field] if field is not None else None
        )

    return SetPatRulesResponse(**args)


def marshal_AddBastionAllowedIPsRequest(
    request: AddBastionAllowedIPsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip_range is not None:
        output["ip_range"] = request.ip_range

    return output


def marshal_CreateGatewayNetworkRequest(
    request: CreateGatewayNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.gateway_id is not None:
        output["gateway_id"] = request.gateway_id

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    if request.enable_masquerade is not None:
        output["enable_masquerade"] = request.enable_masquerade

    if request.push_default_route is not None:
        output["push_default_route"] = request.push_default_route

    if request.ipam_ip_id is not None:
        output["ipam_ip_id"] = request.ipam_ip_id

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


def marshal_CreatePatRuleRequest(
    request: CreatePatRuleRequest,
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


def marshal_SetBastionAllowedIPsRequest(
    request: SetBastionAllowedIPsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip_ranges is not None:
        output["ip_ranges"] = request.ip_ranges

    return output


def marshal_SetPatRulesRequestRule(
    request: SetPatRulesRequestRule,
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


def marshal_SetPatRulesRequest(
    request: SetPatRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.gateway_id is not None:
        output["gateway_id"] = request.gateway_id

    if request.pat_rules is not None:
        output["pat_rules"] = [
            marshal_SetPatRulesRequestRule(item, defaults) for item in request.pat_rules
        ]

    return output


def marshal_UpdateGatewayNetworkRequest(
    request: UpdateGatewayNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.enable_masquerade is not None:
        output["enable_masquerade"] = request.enable_masquerade

    if request.push_default_route is not None:
        output["push_default_route"] = request.push_default_route

    if request.ipam_ip_id is not None:
        output["ipam_ip_id"] = request.ipam_ip_id

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


def marshal_UpdatePatRuleRequest(
    request: UpdatePatRuleRequest,
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
