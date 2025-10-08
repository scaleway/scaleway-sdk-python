# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    BgpSessionStatus,
    ConnectionInitiationPolicy,
    ConnectionStatus,
    TunnelStatus,
    VpnGatewayStatus,
    BgpSession,
    ConnectionCipher,
    Connection,
    CustomerGateway,
    RoutingPolicy,
    VpnGatewayPrivateConfig,
    VpnGatewayPublicConfig,
    VpnGateway,
    CreateConnectionResponse,
    ListConnectionsResponse,
    ListCustomerGatewaysResponse,
    ListRoutingPoliciesResponse,
    GatewayType,
    ListVpnGatewayTypesResponse,
    ListVpnGatewaysResponse,
    RenewConnectionPskResponse,
    CreateConnectionRequestBgpConfig,
    CreateConnectionRequest,
    CreateCustomerGatewayRequest,
    CreateRoutingPolicyRequest,
    CreateVpnGatewayRequestPublicConfig,
    CreateVpnGatewayRequest,
    DetachRoutingPolicyRequest,
    SetRoutingPolicyRequest,
    UpdateConnectionRequest,
    UpdateCustomerGatewayRequest,
    UpdateRoutingPolicyRequest,
    UpdateVpnGatewayRequest,
)


def unmarshal_BgpSession(data: Any) -> BgpSession:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BgpSession' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("routing_policy_id", None)
    if field is not None:
        args["routing_policy_id"] = field
    else:
        args["routing_policy_id"] = None

    field = data.get("private_ip", None)
    if field is not None:
        args["private_ip"] = field
    else:
        args["private_ip"] = None

    field = data.get("peer_private_ip", None)
    if field is not None:
        args["peer_private_ip"] = field
    else:
        args["peer_private_ip"] = None

    return BgpSession(**args)


def unmarshal_ConnectionCipher(data: Any) -> ConnectionCipher:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ConnectionCipher' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("encryption", None)
    if field is not None:
        args["encryption"] = field
    else:
        args["encryption"] = None

    field = data.get("integrity", None)
    if field is not None:
        args["integrity"] = field
    else:
        args["integrity"] = None

    field = data.get("dh_group", None)
    if field is not None:
        args["dh_group"] = field
    else:
        args["dh_group"] = None

    return ConnectionCipher(**args)


def unmarshal_Connection(data: Any) -> Connection:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Connection' failed as data isn't a dictionary."
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

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = ConnectionStatus.UNKNOWN_STATUS

    field = data.get("is_ipv6", None)
    if field is not None:
        args["is_ipv6"] = field
    else:
        args["is_ipv6"] = False

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

    field = data.get("initiation_policy", None)
    if field is not None:
        args["initiation_policy"] = field
    else:
        args["initiation_policy"] = ConnectionInitiationPolicy.UNKNOWN_INITIATION_POLICY

    field = data.get("ikev2_ciphers", None)
    if field is not None:
        args["ikev2_ciphers"] = (
            [unmarshal_ConnectionCipher(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["ikev2_ciphers"] = []

    field = data.get("esp_ciphers", None)
    if field is not None:
        args["esp_ciphers"] = (
            [unmarshal_ConnectionCipher(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["esp_ciphers"] = []

    field = data.get("route_propagation_enabled", None)
    if field is not None:
        args["route_propagation_enabled"] = field
    else:
        args["route_propagation_enabled"] = False

    field = data.get("vpn_gateway_id", None)
    if field is not None:
        args["vpn_gateway_id"] = field
    else:
        args["vpn_gateway_id"] = None

    field = data.get("customer_gateway_id", None)
    if field is not None:
        args["customer_gateway_id"] = field
    else:
        args["customer_gateway_id"] = None

    field = data.get("tunnel_status", None)
    if field is not None:
        args["tunnel_status"] = field
    else:
        args["tunnel_status"] = TunnelStatus.UNKNOWN_TUNNEL_STATUS

    field = data.get("bgp_status_ipv4", None)
    if field is not None:
        args["bgp_status_ipv4"] = field
    else:
        args["bgp_status_ipv4"] = BgpSessionStatus.UNKNOWN_STATUS

    field = data.get("bgp_status_ipv6", None)
    if field is not None:
        args["bgp_status_ipv6"] = field
    else:
        args["bgp_status_ipv6"] = BgpSessionStatus.UNKNOWN_STATUS

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("tunnel_status_ipv4", None)
    if field is not None:
        args["tunnel_status_ipv4"] = field
    else:
        args["tunnel_status_ipv4"] = TunnelStatus.UNKNOWN_TUNNEL_STATUS

    field = data.get("tunnel_status_ipv6", None)
    if field is not None:
        args["tunnel_status_ipv6"] = field
    else:
        args["tunnel_status_ipv6"] = TunnelStatus.UNKNOWN_TUNNEL_STATUS

    field = data.get("bgp_session_ipv4", None)
    if field is not None:
        args["bgp_session_ipv4"] = unmarshal_BgpSession(field)
    else:
        args["bgp_session_ipv4"] = None

    field = data.get("bgp_session_ipv6", None)
    if field is not None:
        args["bgp_session_ipv6"] = unmarshal_BgpSession(field)
    else:
        args["bgp_session_ipv6"] = None

    return Connection(**args)


def unmarshal_CustomerGateway(data: Any) -> CustomerGateway:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CustomerGateway' failed as data isn't a dictionary."
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

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("asn", None)
    if field is not None:
        args["asn"] = field
    else:
        args["asn"] = 0

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

    field = data.get("public_ipv4", None)
    if field is not None:
        args["public_ipv4"] = field
    else:
        args["public_ipv4"] = None

    field = data.get("public_ipv6", None)
    if field is not None:
        args["public_ipv6"] = field
    else:
        args["public_ipv6"] = None

    return CustomerGateway(**args)


def unmarshal_RoutingPolicy(data: Any) -> RoutingPolicy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RoutingPolicy' failed as data isn't a dictionary."
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

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("is_ipv6", None)
    if field is not None:
        args["is_ipv6"] = field
    else:
        args["is_ipv6"] = False

    field = data.get("prefix_filter_in", None)
    if field is not None:
        args["prefix_filter_in"] = field
    else:
        args["prefix_filter_in"] = []

    field = data.get("prefix_filter_out", None)
    if field is not None:
        args["prefix_filter_out"] = field
    else:
        args["prefix_filter_out"] = []

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

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

    return RoutingPolicy(**args)


def unmarshal_VpnGatewayPrivateConfig(data: Any) -> VpnGatewayPrivateConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VpnGatewayPrivateConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return VpnGatewayPrivateConfig(**args)


def unmarshal_VpnGatewayPublicConfig(data: Any) -> VpnGatewayPublicConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VpnGatewayPublicConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("ipam_ipv4_id", None)
    if field is not None:
        args["ipam_ipv4_id"] = field
    else:
        args["ipam_ipv4_id"] = None

    field = data.get("ipam_ipv6_id", None)
    if field is not None:
        args["ipam_ipv6_id"] = field
    else:
        args["ipam_ipv6_id"] = None

    return VpnGatewayPublicConfig(**args)


def unmarshal_VpnGateway(data: Any) -> VpnGateway:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VpnGateway' failed as data isn't a dictionary."
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

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = VpnGatewayStatus.UNKNOWN_STATUS

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

    field = data.get("gateway_type", None)
    if field is not None:
        args["gateway_type"] = field
    else:
        args["gateway_type"] = None

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field
    else:
        args["private_network_id"] = None

    field = data.get("ipam_private_ipv4_id", None)
    if field is not None:
        args["ipam_private_ipv4_id"] = field
    else:
        args["ipam_private_ipv4_id"] = None

    field = data.get("ipam_private_ipv6_id", None)
    if field is not None:
        args["ipam_private_ipv6_id"] = field
    else:
        args["ipam_private_ipv6_id"] = None

    field = data.get("asn", None)
    if field is not None:
        args["asn"] = field
    else:
        args["asn"] = 0

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("public_config", None)
    if field is not None:
        args["public_config"] = unmarshal_VpnGatewayPublicConfig(field)
    else:
        args["public_config"] = None

    field = data.get("private_config", None)
    if field is not None:
        args["private_config"] = unmarshal_VpnGatewayPrivateConfig(field)
    else:
        args["private_config"] = None

    return VpnGateway(**args)


def unmarshal_CreateConnectionResponse(data: Any) -> CreateConnectionResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateConnectionResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("pre_shared_key", None)
    if field is not None:
        args["pre_shared_key"] = field
    else:
        args["pre_shared_key"] = None

    field = data.get("connection", None)
    if field is not None:
        args["connection"] = unmarshal_Connection(field)
    else:
        args["connection"] = None

    return CreateConnectionResponse(**args)


def unmarshal_ListConnectionsResponse(data: Any) -> ListConnectionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListConnectionsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("connections", None)
    if field is not None:
        args["connections"] = (
            [unmarshal_Connection(v) for v in field] if field is not None else None
        )
    else:
        args["connections"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListConnectionsResponse(**args)


def unmarshal_ListCustomerGatewaysResponse(data: Any) -> ListCustomerGatewaysResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListCustomerGatewaysResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("gateways", None)
    if field is not None:
        args["gateways"] = (
            [unmarshal_CustomerGateway(v) for v in field] if field is not None else None
        )
    else:
        args["gateways"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListCustomerGatewaysResponse(**args)


def unmarshal_ListRoutingPoliciesResponse(data: Any) -> ListRoutingPoliciesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRoutingPoliciesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("routing_policies", None)
    if field is not None:
        args["routing_policies"] = (
            [unmarshal_RoutingPolicy(v) for v in field] if field is not None else None
        )
    else:
        args["routing_policies"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    return ListRoutingPoliciesResponse(**args)


def unmarshal_GatewayType(data: Any) -> GatewayType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GatewayType' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("bandwidth", None)
    if field is not None:
        args["bandwidth"] = field
    else:
        args["bandwidth"] = None

    field = data.get("allowed_connections", None)
    if field is not None:
        args["allowed_connections"] = field
    else:
        args["allowed_connections"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    return GatewayType(**args)


def unmarshal_ListVpnGatewayTypesResponse(data: Any) -> ListVpnGatewayTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVpnGatewayTypesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("gateway_types", None)
    if field is not None:
        args["gateway_types"] = (
            [unmarshal_GatewayType(v) for v in field] if field is not None else None
        )
    else:
        args["gateway_types"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListVpnGatewayTypesResponse(**args)


def unmarshal_ListVpnGatewaysResponse(data: Any) -> ListVpnGatewaysResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVpnGatewaysResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("gateways", None)
    if field is not None:
        args["gateways"] = (
            [unmarshal_VpnGateway(v) for v in field] if field is not None else None
        )
    else:
        args["gateways"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListVpnGatewaysResponse(**args)


def unmarshal_RenewConnectionPskResponse(data: Any) -> RenewConnectionPskResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RenewConnectionPskResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("pre_shared_key", None)
    if field is not None:
        args["pre_shared_key"] = field
    else:
        args["pre_shared_key"] = None

    field = data.get("connection", None)
    if field is not None:
        args["connection"] = unmarshal_Connection(field)
    else:
        args["connection"] = None

    return RenewConnectionPskResponse(**args)


def marshal_ConnectionCipher(
    request: ConnectionCipher,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.encryption is not None:
        output["encryption"] = request.encryption

    if request.integrity is not None:
        output["integrity"] = request.integrity

    if request.dh_group is not None:
        output["dh_group"] = request.dh_group

    return output


def marshal_CreateConnectionRequestBgpConfig(
    request: CreateConnectionRequestBgpConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.routing_policy_id is not None:
        output["routing_policy_id"] = request.routing_policy_id

    if request.private_ip is not None:
        output["private_ip"] = request.private_ip

    if request.peer_private_ip is not None:
        output["peer_private_ip"] = request.peer_private_ip

    return output


def marshal_CreateConnectionRequest(
    request: CreateConnectionRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.is_ipv6 is not None:
        output["is_ipv6"] = request.is_ipv6

    if request.initiation_policy is not None:
        output["initiation_policy"] = request.initiation_policy

    if request.ikev2_ciphers is not None:
        output["ikev2_ciphers"] = [
            marshal_ConnectionCipher(item, defaults) for item in request.ikev2_ciphers
        ]

    if request.esp_ciphers is not None:
        output["esp_ciphers"] = [
            marshal_ConnectionCipher(item, defaults) for item in request.esp_ciphers
        ]

    if request.enable_route_propagation is not None:
        output["enable_route_propagation"] = request.enable_route_propagation

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.vpn_gateway_id is not None:
        output["vpn_gateway_id"] = request.vpn_gateway_id

    if request.customer_gateway_id is not None:
        output["customer_gateway_id"] = request.customer_gateway_id

    if request.bgp_config_ipv4 is not None:
        output["bgp_config_ipv4"] = marshal_CreateConnectionRequestBgpConfig(
            request.bgp_config_ipv4, defaults
        )

    if request.bgp_config_ipv6 is not None:
        output["bgp_config_ipv6"] = marshal_CreateConnectionRequestBgpConfig(
            request.bgp_config_ipv6, defaults
        )

    return output


def marshal_CreateCustomerGatewayRequest(
    request: CreateCustomerGatewayRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.asn is not None:
        output["asn"] = request.asn

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.ipv4_public is not None:
        output["ipv4_public"] = request.ipv4_public

    if request.ipv6_public is not None:
        output["ipv6_public"] = request.ipv6_public

    return output


def marshal_CreateRoutingPolicyRequest(
    request: CreateRoutingPolicyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.is_ipv6 is not None:
        output["is_ipv6"] = request.is_ipv6

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.prefix_filter_in is not None:
        output["prefix_filter_in"] = request.prefix_filter_in

    if request.prefix_filter_out is not None:
        output["prefix_filter_out"] = request.prefix_filter_out

    return output


def marshal_CreateVpnGatewayRequestPublicConfig(
    request: CreateVpnGatewayRequestPublicConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ipam_ipv4_id is not None:
        output["ipam_ipv4_id"] = request.ipam_ipv4_id

    if request.ipam_ipv6_id is not None:
        output["ipam_ipv6_id"] = request.ipam_ipv6_id

    return output


def marshal_CreateVpnGatewayRequest(
    request: CreateVpnGatewayRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="public_config",
                    value=request.public_config,
                    marshal_func=marshal_CreateVpnGatewayRequestPublicConfig,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.gateway_type is not None:
        output["gateway_type"] = request.gateway_type

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.ipam_private_ipv4_id is not None:
        output["ipam_private_ipv4_id"] = request.ipam_private_ipv4_id

    if request.ipam_private_ipv6_id is not None:
        output["ipam_private_ipv6_id"] = request.ipam_private_ipv6_id

    if request.zone is not None:
        output["zone"] = request.zone

    return output


def marshal_DetachRoutingPolicyRequest(
    request: DetachRoutingPolicyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="routing_policy_v4",
                    value=request.routing_policy_v4,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="routing_policy_v6",
                    value=request.routing_policy_v6,
                    marshal_func=None,
                ),
            ]
        ),
    )

    return output


def marshal_SetRoutingPolicyRequest(
    request: SetRoutingPolicyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="routing_policy_v4",
                    value=request.routing_policy_v4,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="routing_policy_v6",
                    value=request.routing_policy_v6,
                    marshal_func=None,
                ),
            ]
        ),
    )

    return output


def marshal_UpdateConnectionRequest(
    request: UpdateConnectionRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.initiation_policy is not None:
        output["initiation_policy"] = request.initiation_policy

    if request.ikev2_ciphers is not None:
        output["ikev2_ciphers"] = [
            marshal_ConnectionCipher(item, defaults) for item in request.ikev2_ciphers
        ]

    if request.esp_ciphers is not None:
        output["esp_ciphers"] = [
            marshal_ConnectionCipher(item, defaults) for item in request.esp_ciphers
        ]

    return output


def marshal_UpdateCustomerGatewayRequest(
    request: UpdateCustomerGatewayRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.ipv4_public is not None:
        output["ipv4_public"] = request.ipv4_public

    if request.ipv6_public is not None:
        output["ipv6_public"] = request.ipv6_public

    if request.asn is not None:
        output["asn"] = request.asn

    return output


def marshal_UpdateRoutingPolicyRequest(
    request: UpdateRoutingPolicyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.prefix_filter_in is not None:
        output["prefix_filter_in"] = request.prefix_filter_in

    if request.prefix_filter_out is not None:
        output["prefix_filter_out"] = request.prefix_filter_out

    return output


def marshal_UpdateVpnGatewayRequest(
    request: UpdateVpnGatewayRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    return output
