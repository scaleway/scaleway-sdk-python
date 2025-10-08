# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
    Zone as ScwZone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class BgpSessionStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    UP = "up"
    DOWN = "down"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)


class ConnectionDhGroup(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_DHGROUP = "unknown_dhgroup"
    MODP2048 = "modp2048"
    MODP3072 = "modp3072"
    MODP4096 = "modp4096"
    ECP256 = "ecp256"
    ECP384 = "ecp384"
    ECP521 = "ecp521"
    CURVE25519 = "curve25519"

    def __str__(self) -> str:
        return str(self.value)


class ConnectionEncryption(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ENCRYPTION = "unknown_encryption"
    AES128 = "aes128"
    AES192 = "aes192"
    AES256 = "aes256"
    AES128GCM = "aes128gcm"
    AES192GCM = "aes192gcm"
    AES256GCM = "aes256gcm"
    AES128CCM = "aes128ccm"
    AES256CCM = "aes256ccm"
    CHACHA20POLY1305 = "chacha20poly1305"

    def __str__(self) -> str:
        return str(self.value)


class ConnectionInitiationPolicy(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_INITIATION_POLICY = "unknown_initiation_policy"
    VPN_GATEWAY = "vpn_gateway"
    CUSTOMER_GATEWAY = "customer_gateway"

    def __str__(self) -> str:
        return str(self.value)


class ConnectionIntegrity(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_INTEGRITY = "unknown_integrity"
    SHA256 = "sha256"
    SHA384 = "sha384"
    SHA512 = "sha512"

    def __str__(self) -> str:
        return str(self.value)


class ConnectionStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    ACTIVE = "active"
    LIMITED_CONNECTIVITY = "limited_connectivity"
    DOWN = "down"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class CreateConnectionRequestInitiationPolicy(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_INITIATION_POLICY = "unknown_initiation_policy"
    VPN_GATEWAY = "vpn_gateway"
    CUSTOMER_GATEWAY = "customer_gateway"

    def __str__(self) -> str:
        return str(self.value)


class ListConnectionsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListCustomerGatewaysRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRoutingPoliciesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListVpnGatewaysRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    TYPE_ASC = "type_asc"
    TYPE_DESC = "type_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"

    def __str__(self) -> str:
        return str(self.value)


class TunnelStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TUNNEL_STATUS = "unknown_tunnel_status"
    UP = "up"
    DOWN = "down"

    def __str__(self) -> str:
        return str(self.value)


class VpnGatewayStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    CONFIGURING = "configuring"
    FAILED = "failed"
    PROVISIONING = "provisioning"
    ACTIVE = "active"
    DEPROVISIONING = "deprovisioning"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class BgpSession:
    routing_policy_id: str
    private_ip: str
    peer_private_ip: str


@dataclass
class ConnectionCipher:
    encryption: ConnectionEncryption
    integrity: Optional[ConnectionIntegrity] = None
    dh_group: Optional[ConnectionDhGroup] = None


@dataclass
class VpnGatewayPrivateConfig:
    pass


@dataclass
class VpnGatewayPublicConfig:
    ipam_ipv4_id: Optional[str] = None
    ipam_ipv6_id: Optional[str] = None


@dataclass
class CreateConnectionRequestBgpConfig:
    routing_policy_id: str
    private_ip: Optional[str] = None
    peer_private_ip: Optional[str] = None


@dataclass
class Connection:
    id: str
    """
    Unique identifier of the connection.
    """

    project_id: str
    """
    Project ID.
    """

    organization_id: str
    """
    Organization ID.
    """

    name: str
    """
    Name of the connection.
    """

    tags: list[str]
    """
    List of tags applied to the connection.
    """

    status: ConnectionStatus
    """
    Status of the connection.
    """

    is_ipv6: bool
    """
    IP version of the IPSec Tunnel.
    """

    initiation_policy: ConnectionInitiationPolicy
    """
    Who initiates the IPsec tunnel.
    """

    ikev2_ciphers: list[ConnectionCipher]
    """
    List of IKE v2 ciphers proposed for the IPsec tunnel.
    """

    esp_ciphers: list[ConnectionCipher]
    """
    List of ESP ciphers proposed for the IPsec tunnel.
    """

    route_propagation_enabled: bool
    """
    Defines whether route propagation is enabled or not.
    """

    vpn_gateway_id: str
    """
    ID of the VPN gateway attached to the connection.
    """

    customer_gateway_id: str
    """
    ID of the customer gateway attached to the connection.
    """

    tunnel_status: TunnelStatus
    """
    Status of the IPsec tunnel.
    """

    bgp_status_ipv4: BgpSessionStatus
    """
    Status of the BGP IPv4 session.
    """

    bgp_status_ipv6: BgpSessionStatus
    """
    Status of the BGP IPv6 session.
    """

    region: ScwRegion
    """
    Region of the connection.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the connection.
    """

    updated_at: Optional[datetime] = None
    """
    Last modification date of the connection.
    """

    tunnel_status_ipv4: Optional[TunnelStatus] = TunnelStatus.UNKNOWN_TUNNEL_STATUS
    """
    Status of the IPv4 IPsec tunnel.
    """

    tunnel_status_ipv6: Optional[TunnelStatus] = TunnelStatus.UNKNOWN_TUNNEL_STATUS
    """
    Status of the IPv6 IPsec tunnel.
    """

    bgp_session_ipv4: Optional[BgpSession] = None
    """
    BGP IPv4 session, including status, interco private IPv4 subnet and attached routing policy.
    """

    bgp_session_ipv6: Optional[BgpSession] = None
    """
    BGP IPv6 session, including status, interco private IPv6 subnet and attached routing policy.
    """


@dataclass
class CreateVpnGatewayRequestPublicConfig:
    ipam_ipv4_id: Optional[str] = None
    ipam_ipv6_id: Optional[str] = None


@dataclass
class CustomerGateway:
    id: str
    """
    Unique identifier of the customer gateway.
    """

    project_id: str
    """
    Project ID.
    """

    organization_id: str
    """
    Organization ID.
    """

    name: str
    """
    Name of the customer gateway.
    """

    tags: list[str]
    """
    List of tags applied to the customer gateway.
    """

    asn: int
    """
    AS Number of the customer gateway.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the customer gateway.
    """

    updated_at: Optional[datetime] = None
    """
    Last modification date of the customer gateway.
    """

    public_ipv4: Optional[str] = None
    """
    Public IPv4 address of the customer gateway.
    """

    public_ipv6: Optional[str] = None
    """
    Public IPv6 address of the customer gateway.
    """


@dataclass
class RoutingPolicy:
    id: str
    """
    Unique identifier of the routing policy.
    """

    project_id: str
    """
    Project ID.
    """

    organization_id: str
    """
    Organization ID.
    """

    name: str
    """
    Name of the routing policy.
    """

    tags: list[str]
    """
    List of tags associated with the routing policy.
    """

    is_ipv6: bool
    """
    IP prefixes version of the routing policy.
    """

    prefix_filter_in: list[str]
    """
    IP prefixes to accept from the peer (ranges of route announcements to accept).
    """

    prefix_filter_out: list[str]
    """
    IP prefix filters to advertise to the peer (ranges of routes to advertise).
    """

    region: ScwRegion
    """
    Region of the routing policy.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the routing policy.
    """

    updated_at: Optional[datetime] = None
    """
    Last modification date of the routing policy.
    """


@dataclass
class GatewayType:
    name: str
    bandwidth: int
    allowed_connections: int
    region: ScwRegion
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class VpnGateway:
    id: str
    """
    Unique identifier of the VPN gateway.
    """

    project_id: str
    """
    Project ID.
    """

    organization_id: str
    """
    Organization ID.
    """

    name: str
    """
    Name of the VPN gateway.
    """

    tags: list[str]
    """
    List of tags applied to the VPN gateway.
    """

    status: VpnGatewayStatus
    """
    Status of the VPN gateway.
    """

    gateway_type: str
    """
    Gateway type of the VPN gateway.
    """

    private_network_id: str
    """
    ID of the Private Network attached to the VPN gateway.
    """

    ipam_private_ipv4_id: str
    """
    ID of the IPAM private IPv4 address attached to the VPN gateway.
    """

    ipam_private_ipv6_id: str
    """
    ID of the IPAM private IPv6 address attached to the VPN gateway.
    """

    asn: int
    """
    Autonomous System Number (ASN) of the VPN gateway, used by Border Gateway Protocol (BGP) to exchange routing information with the customer gateway.
    """

    zone: ScwZone
    """
    Zone where the VPN gateway resource is currently provisioned.
    """

    region: ScwRegion
    """
    Region of the VPN gateway.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the VPN gateway.
    """

    updated_at: Optional[datetime] = None
    """
    Last modification date of the VPN gateway.
    """

    public_config: Optional[VpnGatewayPublicConfig] = None

    private_config: Optional[VpnGatewayPrivateConfig] = None


@dataclass
class CreateConnectionRequest:
    name: str
    """
    Name of the connection.
    """

    is_ipv6: bool
    """
    Defines IP version of the IPSec Tunnel.
    """

    initiation_policy: CreateConnectionRequestInitiationPolicy
    """
    Who initiates the IPsec tunnel.
    """

    ikev2_ciphers: list[ConnectionCipher]
    """
    List of IKE v2 ciphers proposed for the IPsec tunnel.
    """

    esp_ciphers: list[ConnectionCipher]
    """
    List of ESP ciphers proposed for the IPsec tunnel.
    """

    enable_route_propagation: bool
    """
    Defines whether route propagation is enabled or not.
    """

    vpn_gateway_id: str
    """
    ID of the VPN gateway to attach to the connection.
    """

    customer_gateway_id: str
    """
    ID of the customer gateway to attach to the connection.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project to create the connection in.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List of tags to apply to the connection.
    """

    bgp_config_ipv4: Optional[CreateConnectionRequestBgpConfig] = None
    """
    BGP config of IPv4 session, including interco private IPv4 subnet (first IP assigned to the VPN Gateway, second IP to the Customer Gateway) and attached routing policy.
    """

    bgp_config_ipv6: Optional[CreateConnectionRequestBgpConfig] = None
    """
    BGP config of IPv6 session, including interco private IPv6 subnet (first IP assigned to the VPN Gateway, second IP to the Customer Gateway) and attached routing policy.
    """


@dataclass
class CreateConnectionResponse:
    pre_shared_key: str
    """
    New PSK generated for this connection.
    """

    connection: Optional[Connection] = None
    """
    This connection.
    """


@dataclass
class CreateCustomerGatewayRequest:
    name: str
    """
    Name of the customer gateway.
    """

    asn: int
    """
    AS Number of the customer gateway.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project to create the customer gateway in.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List of tags to apply to the customer gateway.
    """

    ipv4_public: Optional[str] = None
    """
    Public IPv4 address of the customer gateway.
    """

    ipv6_public: Optional[str] = None
    """
    Public IPv6 address of the customer gateway.
    """


@dataclass
class CreateRoutingPolicyRequest:
    name: str
    """
    Name of the routing policy.
    """

    is_ipv6: bool
    """
    IP prefixes version of the routing policy.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project to create the routing policy in.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List of tags to apply to the routing policy.
    """

    prefix_filter_in: Optional[list[str]] = field(default_factory=list)
    """
    IP prefixes to accept from the peer (ranges of route announcements to accept).
    """

    prefix_filter_out: Optional[list[str]] = field(default_factory=list)
    """
    IP prefix filters to advertise to the peer (ranges of routes to advertise).
    """


@dataclass
class CreateVpnGatewayRequest:
    name: str
    """
    Name of the VPN gateway.
    """

    gateway_type: str
    """
    VPN gateway type (commercial offer type).
    """

    private_network_id: str
    """
    ID of the Private Network to attach to the VPN gateway.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project to create the VPN gateway in.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List of tags to apply to the VPN gateway.
    """

    ipam_private_ipv4_id: Optional[str] = None
    """
    ID of the IPAM private IPv4 address to attach to the VPN gateway.
    """

    ipam_private_ipv6_id: Optional[str] = None
    """
    ID of the IPAM private IPv6 address to attach to the VPN gateway.
    """

    zone: Optional[ScwZone] = None
    """
    Availability Zone where the VPN gateway should be provisioned. If no zone is specified, the VPN gateway will be automatically placed.
    """

    public_config: Optional[CreateVpnGatewayRequestPublicConfig] = None


@dataclass
class DeleteConnectionRequest:
    connection_id: str
    """
    ID of the connection to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteCustomerGatewayRequest:
    gateway_id: str
    """
    ID of the customer gateway to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteRoutingPolicyRequest:
    routing_policy_id: str
    """
    ID of the routing policy to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteVpnGatewayRequest:
    gateway_id: str
    """
    ID of the VPN gateway to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DetachRoutingPolicyRequest:
    connection_id: str
    """
    ID of the connection from which routing policy is being detached.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    routing_policy_v4: Optional[str] = None

    routing_policy_v6: Optional[str] = None


@dataclass
class DisableRoutePropagationRequest:
    connection_id: str
    """
    ID of the connection on which to disable route propagation.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class EnableRoutePropagationRequest:
    connection_id: str
    """
    ID of the connection on which to enable route propagation.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetConnectionRequest:
    connection_id: str
    """
    ID of the requested connection.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetCustomerGatewayRequest:
    gateway_id: str
    """
    ID of the requested customer gateway.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetRoutingPolicyRequest:
    routing_policy_id: str
    """
    ID of the routing policy to get.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetVpnGatewayRequest:
    gateway_id: str
    """
    ID of the requested VPN gateway.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListConnectionsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number to return.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of connections to return per page.
    """

    order_by: Optional[ListConnectionsRequestOrderBy] = (
        ListConnectionsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Order in which to return results.
    """

    project_id: Optional[str] = None
    """
    Project ID to filter for.
    """

    name: Optional[str] = None
    """
    Connection name to filter for.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to filter for.
    """

    statuses: Optional[list[ConnectionStatus]] = field(default_factory=list)
    """
    Connection statuses to filter for.
    """

    is_ipv6: Optional[bool] = False
    """
    Filter connections with IP version of IPSec tunnel.
    """

    routing_policy_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter for connections using these routing policies.
    """

    route_propagation_enabled: Optional[bool] = False
    """
    Filter for connections with route propagation enabled.
    """

    vpn_gateway_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter for connections attached to these VPN gateways.
    """

    customer_gateway_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter for connections attached to these customer gateways.
    """


@dataclass
class ListConnectionsResponse:
    connections: list[Connection]
    """
    List of connections on the current page.
    """

    total_count: int
    """
    Total number of connections.
    """


@dataclass
class ListCustomerGatewaysRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number to return.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of customer gateways to return per page.
    """

    order_by: Optional[ListCustomerGatewaysRequestOrderBy] = (
        ListCustomerGatewaysRequestOrderBy.CREATED_AT_ASC
    )
    """
    Order in which to return results.
    """

    project_id: Optional[str] = None
    """
    Project ID to filter for.
    """

    name: Optional[str] = None
    """
    Customer gateway name to filter for.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to filter for.
    """


@dataclass
class ListCustomerGatewaysResponse:
    gateways: list[CustomerGateway]
    """
    List of customer gateways on the current page.
    """

    total_count: int
    """
    Total number of customer gateways.
    """


@dataclass
class ListRoutingPoliciesRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number to return.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of routing policies to return per page.
    """

    order_by: Optional[ListRoutingPoliciesRequestOrderBy] = (
        ListRoutingPoliciesRequestOrderBy.CREATED_AT_ASC
    )
    """
    Order in which to return results.
    """

    project_id: Optional[str] = None
    """
    Project ID to filter for.
    """

    name: Optional[str] = None
    """
    Routing policy name to filter for.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to filter for.
    """

    ipv6: Optional[bool] = False
    """
    Filter for the routing policies based on IP prefixes version.
    """


@dataclass
class ListRoutingPoliciesResponse:
    routing_policies: list[RoutingPolicy]
    total_count: int


@dataclass
class ListVpnGatewayTypesRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number to return.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of VPN gateway types to return per page.
    """


@dataclass
class ListVpnGatewayTypesResponse:
    gateway_types: list[GatewayType]
    """
    List of VPN gateway types on the current page.
    """

    total_count: int
    """
    Total number of gateway types.
    """


@dataclass
class ListVpnGatewaysRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number to return.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of VPN gateways to return per page.
    """

    order_by: Optional[ListVpnGatewaysRequestOrderBy] = (
        ListVpnGatewaysRequestOrderBy.CREATED_AT_ASC
    )
    """
    Order in which to return results.
    """

    project_id: Optional[str] = None
    """
    Project ID to filter for.
    """

    name: Optional[str] = None
    """
    VPN gateway name to filter for.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to filter for.
    """

    statuses: Optional[list[VpnGatewayStatus]] = field(default_factory=list)
    """
    VPN gateway statuses to filter for.
    """

    gateway_types: Optional[list[str]] = field(default_factory=list)
    """
    Filter for VPN gateways of these types.
    """

    private_network_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter for VPN gateways attached to these private networks.
    """


@dataclass
class ListVpnGatewaysResponse:
    gateways: list[VpnGateway]
    """
    List of VPN gateways on the current page.
    """

    total_count: int
    """
    Total number of VPN gateways.
    """


@dataclass
class RenewConnectionPskRequest:
    connection_id: str
    """
    ID of the connection to renew the PSK.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RenewConnectionPskResponse:
    pre_shared_key: str
    """
    New PSK generated for this connection.
    """

    connection: Optional[Connection] = None
    """
    This connection.
    """


@dataclass
class SetRoutingPolicyRequest:
    connection_id: str
    """
    ID of the connection whose routing policy is being updated.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    routing_policy_v4: Optional[str] = None

    routing_policy_v6: Optional[str] = None


@dataclass
class UpdateConnectionRequest:
    connection_id: str
    """
    ID of the connection to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the connection.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List of tags to apply to the connection.
    """

    initiation_policy: Optional[CreateConnectionRequestInitiationPolicy] = (
        CreateConnectionRequestInitiationPolicy.UNKNOWN_INITIATION_POLICY
    )
    """
    Who initiates the IPsec tunnel.
    """

    ikev2_ciphers: Optional[list[ConnectionCipher]] = field(default_factory=list)
    """
    List of IKE v2 ciphers proposed for the IPsec tunnel.
    """

    esp_ciphers: Optional[list[ConnectionCipher]] = field(default_factory=list)
    """
    List of ESP ciphers proposed for the IPsec tunnel.
    """


@dataclass
class UpdateCustomerGatewayRequest:
    gateway_id: str
    """
    ID of the customer gateway to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the customer gateway.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List of tags to apply to the customer gateway.
    """

    ipv4_public: Optional[str] = None
    """
    Public IPv4 address of the customer gateway.
    """

    ipv6_public: Optional[str] = None
    """
    Public IPv6 address of the customer gateway.
    """

    asn: Optional[int] = 0
    """
    AS Number of the customer gateway.
    """


@dataclass
class UpdateRoutingPolicyRequest:
    routing_policy_id: str
    """
    ID of the routing policy to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the routing policy.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List of tags to apply to the routing policy.
    """

    prefix_filter_in: Optional[list[str]] = field(default_factory=list)
    """
    IP prefixes to accept from the peer (ranges of route announcements to accept).
    """

    prefix_filter_out: Optional[list[str]] = field(default_factory=list)
    """
    IP prefix filters for routes to advertise to the peer (ranges of routes to advertise).
    """


@dataclass
class UpdateVpnGatewayRequest:
    gateway_id: str
    """
    ID of the VPN gateway to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the VPN gateway.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List of tags to apply to the VPN Gateway.
    """
