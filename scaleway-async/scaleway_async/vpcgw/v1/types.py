# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Zone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class DHCPEntryType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    RESERVATION = "reservation"
    LEASE = "lease"

    def __str__(self) -> str:
        return str(self.value)


class GatewayNetworkStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    CREATED = "created"
    ATTACHING = "attaching"
    CONFIGURING = "configuring"
    READY = "ready"
    DETACHING = "detaching"
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)


class GatewayStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    STOPPED = "stopped"
    ALLOCATING = "allocating"
    CONFIGURING = "configuring"
    RUNNING = "running"
    STOPPING = "stopping"
    FAILED = "failed"
    DELETING = "deleting"
    DELETED = "deleted"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class ListDHCPEntriesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    IP_ADDRESS_ASC = "ip_address_asc"
    IP_ADDRESS_DESC = "ip_address_desc"
    HOSTNAME_ASC = "hostname_asc"
    HOSTNAME_DESC = "hostname_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListDHCPsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    SUBNET_ASC = "subnet_asc"
    SUBNET_DESC = "subnet_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListGatewayNetworksRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListGatewaysRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
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


class ListIPsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    IP_ASC = "ip_asc"
    IP_DESC = "ip_desc"
    REVERSE_ASC = "reverse_asc"
    REVERSE_DESC = "reverse_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPATRulesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    PUBLIC_PORT_ASC = "public_port_asc"
    PUBLIC_PORT_DESC = "public_port_desc"

    def __str__(self) -> str:
        return str(self.value)


class PATRuleProtocol(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    BOTH = "both"
    TCP = "tcp"
    UDP = "udp"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class DHCP:
    id: str
    """
    ID of the DHCP config.
    """

    organization_id: str
    """
    Owning Organization.
    """

    project_id: str
    """
    Owning Project.
    """

    subnet: str
    """
    Subnet for the DHCP server.
    """

    address: str
    """
    IP address of the DHCP server. This will be the Public Gateway's address in the Private Network. It must be part of config's subnet.
    """

    pool_low: str
    """
    Low IP (inclusive) of the dynamic address pool. Must be in the config's subnet.
    """

    created_at: Optional[datetime]
    """
    Date the DHCP configuration was created.
    """

    updated_at: Optional[datetime]
    """
    Configuration last modification date.
    """

    pool_high: str
    """
    High IP (inclusive) of the dynamic address pool. Must be in the config's subnet.
    """

    enable_dynamic: bool
    """
    Defines whether to enable dynamic pooling of IPs. When false, only pre-existing DHCP reservations will be handed out.
    """

    push_default_route: bool
    """
    Defines whether the gateway should push a default route to DHCP clients, or only hand out IPs.
    """

    push_dns_server: bool
    """
    Defines whether the gateway should push custom DNS servers to clients. This allows for instance hostname -> IP resolution.
    """

    dns_servers_override: List[str]
    """
    Array of DNS server IP addresses used to override the DNS server list pushed to DHCP clients, instead of the gateway itself.
    """

    dns_search: List[str]
    """
    Array of search paths in addition to the pushed DNS configuration.
    """

    dns_local_name: str
    """
    TLD given to hostnames in the Private Networks. If an Instance with hostname `foo` gets a lease, and this is set to `bar`, `foo.bar` will resolve.
    """

    zone: Zone
    """
    Zone of this DHCP configuration.
    """

    valid_lifetime: Optional[str]
    """
    How long DHCP entries will be valid for.
    """

    renew_timer: Optional[str]
    """
    After how long a renew will be attempted. Must be 30s lower than `rebind_timer`.
    """

    rebind_timer: Optional[str]
    """
    After how long a DHCP client will query for a new lease if previous renews fail. Must be 30s lower than `valid_lifetime`.
    """


@dataclass
class IpamConfig:
    push_default_route: bool
    """
    Defines whether the default route is enabled on that Gateway Network.
    """

    ipam_ip_id: str
    """
    IPAM-booked IP ID as the Gateway's IP in this Private Network.
    """


@dataclass
class GatewayNetwork:
    id: str
    """
    ID of the Public Gateway-Private Network connection.
    """

    gateway_id: str
    """
    ID of the connected Public Gateway.
    """

    private_network_id: str
    """
    ID of the connected Private Network.
    """

    created_at: Optional[datetime]
    """
    Connection creation date.
    """

    updated_at: Optional[datetime]
    """
    Connection last modification date.
    """

    mac_address: Optional[str]
    """
    MAC address of the gateway in the Private Network (if the gateway is up and running).
    """

    enable_masquerade: bool
    """
    Defines whether the gateway masquerades traffic for this Private Network (Dynamic NAT).
    """

    status: GatewayNetworkStatus
    """
    Current status of the Public Gateway's connection to the Private Network.
    """

    enable_dhcp: bool
    """
    Defines whether DHCP is enabled on the connected Private Network.
    """

    zone: Zone
    """
    Zone of the GatewayNetwork connection.
    """

    dhcp: Optional[DHCP]
    """
    DHCP configuration for the connected Private Network.
    """

    address: Optional[str]
    """
    Address of the Gateway (in CIDR form) to use when DHCP is not used.
    """

    ipam_config: Optional[IpamConfig]
    """
    IPAM IP configuration used.
    """


@dataclass
class GatewayType:
    name: str
    """
    Public Gateway type name.
    """

    bandwidth: int
    """
    Bandwidth, in bps, of the Public Gateway. This is the public bandwidth to the outer Internet, and the internal bandwidth to each connected Private Networks.
    """

    zone: Zone
    """
    Zone the Public Gateway type is available in.
    """


@dataclass
class IP:
    id: str
    """
    IP address ID.
    """

    organization_id: str
    """
    Owning Organization.
    """

    project_id: str
    """
    Owning Project.
    """

    tags: List[str]
    """
    Tags associated with the IP address.
    """

    address: str
    """
    The IP address itself.
    """

    zone: Zone
    """
    Zone of the IP address.
    """

    created_at: Optional[datetime]
    """
    IP address creation date.
    """

    updated_at: Optional[datetime]
    """
    IP address last modification date.
    """

    reverse: Optional[str]
    """
    Reverse domain name for the IP address.
    """

    gateway_id: Optional[str]
    """
    Public Gateway associated with the IP address.
    """


@dataclass
class CreateDHCPRequest:
    subnet: str
    """
    Subnet for the DHCP server.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str]
    """
    Project to create the DHCP configuration in.
    """

    address: Optional[str]
    """
    IP address of the DHCP server. This will be the gateway's address in the Private Network. Defaults to the first address of the subnet.
    """

    pool_low: Optional[str]
    """
    Low IP (inclusive) of the dynamic address pool. Must be in the config's subnet. Defaults to the second address of the subnet.
    """

    pool_high: Optional[str]
    """
    High IP (inclusive) of the dynamic address pool. Must be in the config's subnet. Defaults to the last address of the subnet.
    """

    enable_dynamic: Optional[bool]
    """
    Defines whether to enable dynamic pooling of IPs. When false, only pre-existing DHCP reservations will be handed out. Defaults to true.
    """

    valid_lifetime: Optional[str]
    """
    How long DHCP entries will be valid for. Defaults to 1h (3600s).
    """

    renew_timer: Optional[str]
    """
    After how long a renew will be attempted. Must be 30s lower than `rebind_timer`. Defaults to 50m (3000s).
    """

    rebind_timer: Optional[str]
    """
    After how long a DHCP client will query for a new lease if previous renews fail. Must be 30s lower than `valid_lifetime`. Defaults to 51m (3060s).
    """

    push_default_route: Optional[bool]
    """
    Defines whether the gateway should push a default route to DHCP clients or only hand out IPs. Defaults to true.
    """

    push_dns_server: Optional[bool]
    """
    Defines whether the gateway should push custom DNS servers to clients. This allows for Instance hostname -> IP resolution. Defaults to true.
    """

    dns_servers_override: Optional[List[str]]
    """
    Array of DNS server IP addresses used to override the DNS server list pushed to DHCP clients, instead of the gateway itself.
    """

    dns_search: Optional[List[str]]
    """
    Array of search paths in addition to the pushed DNS configuration.
    """

    dns_local_name: Optional[str]
    """
    TLD given to hostnames in the Private Network. Allowed characters are `a-z0-9-.`. Defaults to the slugified Private Network name if created along a GatewayNetwork, or else to `priv`.
    """


@dataclass
class CreateGatewayNetworkRequestIpamConfig:
    push_default_route: bool
    """
    Enabling the default route also enables masquerading.
    """

    ipam_ip_id: Optional[str]
    """
    Use this IPAM-booked IP ID as the Gateway's IP in this Private Network.
    """


@dataclass
class DHCPEntry:
    id: str
    """
    DHCP entry ID.
    """

    gateway_network_id: str
    """
    Owning GatewayNetwork.
    """

    mac_address: str
    """
    MAC address of the client device.
    """

    ip_address: str
    """
    Assigned IP address.
    """

    hostname: str
    """
    Hostname of the client device.
    """

    type_: DHCPEntryType
    """
    Entry type, either static (DHCP reservation) or dynamic (DHCP lease).
    """

    zone: Zone
    """
    Zone of this DHCP entry.
    """

    created_at: Optional[datetime]
    """
    DHCP entry creation date.
    """

    updated_at: Optional[datetime]
    """
    DHCP entry last modification date.
    """


@dataclass
class Gateway:
    id: str
    """
    ID of the gateway.
    """

    organization_id: str
    """
    Owning Organization.
    """

    project_id: str
    """
    Owning Project.
    """

    created_at: Optional[datetime]
    """
    Gateway creation date.
    """

    updated_at: Optional[datetime]
    """
    Gateway last modification date.
    """

    type_: Optional[GatewayType]
    """
    Gateway type (commercial offer).
    """

    status: GatewayStatus
    """
    Current status of the gateway.
    """

    name: str
    """
    Name of the gateway.
    """

    tags: List[str]
    """
    Tags associated with the gateway.
    """

    gateway_networks: List[GatewayNetwork]
    """
    GatewayNetwork objects attached to the gateway (each one represents a connection to a Private Network).
    """

    upstream_dns_servers: List[str]
    """
    Array of DNS server IP addresses to override the gateway's default recursive DNS servers.
    """

    bastion_enabled: bool
    """
    Defines whether SSH bastion is enabled on the gateway.
    """

    ip: Optional[IP]
    """
    Public IP address of the gateway.
    """

    version: Optional[str]
    """
    Version of the running gateway software.
    """

    can_upgrade_to: Optional[str]
    """
    Newly available gateway software version that can be updated to.
    """

    bastion_port: int
    """
    Port of the SSH bastion.
    """

    smtp_enabled: bool
    """
    Defines whether SMTP traffic is allowed to pass through the gateway.
    """

    is_legacy: bool
    """
    Defines whether the gateway uses non-IPAM IP configurations.
    """

    ip_mobility_enabled: bool
    """
    Defines whether the gateway uses routed IPs (IP mobility) instead of NAT IPs.
    """

    zone: Zone
    """
    Zone of the gateway.
    """


@dataclass
class PATRule:
    id: str
    """
    PAT rule ID.
    """

    gateway_id: str
    """
    Gateway the PAT rule applies to.
    """

    public_port: int
    """
    Public port to listen on.
    """

    private_ip: str
    """
    Private IP address to forward data to.
    """

    private_port: int
    """
    Private port to translate to.
    """

    protocol: PATRuleProtocol
    """
    Protocol the rule applies to.
    """

    zone: Zone
    """
    Zone of the PAT rule.
    """

    created_at: Optional[datetime]
    """
    PAT rule creation date.
    """

    updated_at: Optional[datetime]
    """
    PAT rule last modification date.
    """


@dataclass
class SetDHCPEntriesRequestEntry:
    mac_address: str
    """
    MAC address to give a static entry to. A matching entry will be upgraded to a reservation, and a matching reservation will be updated.
    """

    ip_address: str
    """
    IP address to give to the device.
    """


@dataclass
class SetPATRulesRequestRule:
    public_port: int
    """
    Public port to listen on. Uniquely identifies the rule, and a matching rule will be updated with the new parameters.
    """

    private_ip: str
    """
    Private IP to forward data to.
    """

    private_port: int
    """
    Private port to translate to.
    """

    protocol: PATRuleProtocol
    """
    Protocol the rule should apply to.
    """


@dataclass
class UpdateGatewayNetworkRequestIpamConfig:
    push_default_route: Optional[bool]
    """
    Enabling the default route also enables masquerading.
    """

    ipam_ip_id: Optional[str]
    """
    Use this IPAM-booked IP ID as the Gateway's IP in this Private Network.
    """


@dataclass
class CreateDHCPEntryRequest:
    gateway_network_id: str
    """
    GatewayNetwork on which to create a DHCP reservation.
    """

    mac_address: str
    """
    MAC address to give a static entry to.
    """

    ip_address: str
    """
    IP address to give to the device.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class CreateGatewayNetworkRequest:
    gateway_id: str
    """
    Public Gateway to connect.
    """

    private_network_id: str
    """
    Private Network to connect.
    """

    enable_masquerade: bool
    """
    Note: this setting is ignored when passing `ipam_config`.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    enable_dhcp: Optional[bool]
    """
    Defaults to `true` if either `dhcp_id` or `dhcp` are present. If set to `true`, either `dhcp_id` or `dhcp` must be present.
Note: this setting is ignored when passing `ipam_config`.
    """

    dhcp_id: Optional[str]

    dhcp: Optional[CreateDHCPRequest]

    address: Optional[str]

    ipam_config: Optional[CreateGatewayNetworkRequestIpamConfig]


@dataclass
class CreateGatewayRequest:
    type_: str
    """
    Gateway type (commercial offer type).
    """

    enable_smtp: bool
    """
    Defines whether SMTP traffic should be allowed pass through the gateway.
    """

    enable_bastion: bool
    """
    Defines whether SSH bastion should be enabled the gateway.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str]
    """
    Scaleway Project to create the gateway in.
    """

    name: Optional[str]
    """
    Name for the gateway.
    """

    tags: Optional[List[str]]
    """
    Tags for the gateway.
    """

    upstream_dns_servers: Optional[List[str]]
    """
    Array of DNS server IP addresses to override the gateway's default recursive DNS servers.
    """

    ip_id: Optional[str]
    """
    Existing IP address to attach to the gateway.
    """

    bastion_port: Optional[int]
    """
    Port of the SSH bastion.
    """


@dataclass
class CreateIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str]
    """
    Project to create the IP address in.
    """

    tags: Optional[List[str]]
    """
    Tags to give to the IP address.
    """


@dataclass
class CreatePATRuleRequest:
    gateway_id: str
    """
    ID of the Gateway on which to create the rule.
    """

    public_port: int
    """
    Public port to listen on.
    """

    private_ip: str
    """
    Private IP to forward data to.
    """

    private_port: int
    """
    Private port to translate to.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    protocol: Optional[PATRuleProtocol]
    """
    Protocol the rule should apply to.
    """


@dataclass
class DeleteDHCPEntryRequest:
    dhcp_entry_id: str
    """
    ID of the DHCP entry to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteDHCPRequest:
    dhcp_id: str
    """
    DHCP configuration ID to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteGatewayNetworkRequest:
    gateway_network_id: str
    """
    ID of the GatewayNetwork to delete.
    """

    cleanup_dhcp: bool
    """
    Defines whether to clean up attached DHCP configurations (if any, and if not attached to another Gateway Network).
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteGatewayRequest:
    gateway_id: str
    """
    ID of the gateway to delete.
    """

    cleanup_dhcp: bool
    """
    Defines whether to clean up attached DHCP configurations (if any, and if not attached to another Gateway Network).
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteIPRequest:
    ip_id: str
    """
    ID of the IP address to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeletePATRuleRequest:
    pat_rule_id: str
    """
    ID of the PAT rule to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class EnableIPMobilityRequest:
    gateway_id: str
    """
    ID of the gateway to upgrade to IP mobility.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetDHCPEntryRequest:
    dhcp_entry_id: str
    """
    ID of the DHCP entry to fetch.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetDHCPRequest:
    dhcp_id: str
    """
    ID of the DHCP configuration to fetch.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetGatewayNetworkRequest:
    gateway_network_id: str
    """
    ID of the GatewayNetwork to fetch.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetGatewayRequest:
    gateway_id: str
    """
    ID of the gateway to fetch.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetIPRequest:
    ip_id: str
    """
    ID of the IP address to get.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetPATRuleRequest:
    pat_rule_id: str
    """
    ID of the PAT rule to get.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListDHCPEntriesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListDHCPEntriesRequestOrderBy]
    """
    Order in which to return results.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    DHCP entries per page.
    """

    gateway_network_id: Optional[str]
    """
    Filter for entries on this GatewayNetwork.
    """

    mac_address: Optional[str]
    """
    Filter for entries with this MAC address.
    """

    ip_address: Optional[str]
    """
    Filter for entries with this IP address.
    """

    hostname: Optional[str]
    """
    Filter for entries with this hostname substring.
    """

    type_: Optional[DHCPEntryType]
    """
    Filter for entries of this type.
    """


@dataclass
class ListDHCPEntriesResponse:
    dhcp_entries: List[DHCPEntry]
    """
    DHCP entries in this page.
    """

    total_count: int
    """
    Total count of DHCP entries matching the filter.
    """


@dataclass
class ListDHCPsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListDHCPsRequestOrderBy]
    """
    Order in which to return results.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    DHCP configurations per page.
    """

    organization_id: Optional[str]
    """
    Include only DHCP configuration objects in this Organization.
    """

    project_id: Optional[str]
    """
    Include only DHCP configuration objects in this Project.
    """

    address: Optional[str]
    """
    Filter for DHCP configuration objects with this DHCP server IP address (the gateway's address in the Private Network).
    """

    has_address: Optional[str]
    """
    Filter for DHCP configuration objects with subnets containing this IP address.
    """


@dataclass
class ListDHCPsResponse:
    dhcps: List[DHCP]
    """
    First page of DHCP configuration objects.
    """

    total_count: int
    """
    Total count of DHCP configuration objects matching the filter.
    """


@dataclass
class ListGatewayNetworksRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListGatewayNetworksRequestOrderBy]
    """
    Order in which to return results.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    GatewayNetworks per page.
    """

    gateway_id: Optional[str]
    """
    Filter for GatewayNetworks connected to this gateway.
    """

    private_network_id: Optional[str]
    """
    Filter for GatewayNetworks connected to this Private Network.
    """

    enable_masquerade: Optional[bool]
    """
    Filter for GatewayNetworks with this `enable_masquerade` setting.
    """

    dhcp_id: Optional[str]
    """
    Filter for GatewayNetworks using this DHCP configuration.
    """

    status: Optional[GatewayNetworkStatus]
    """
    Filter for GatewayNetworks with this current status this status. Use `unknown` to include all statuses.
    """


@dataclass
class ListGatewayNetworksResponse:
    gateway_networks: List[GatewayNetwork]
    """
    GatewayNetworks on this page.
    """

    total_count: int
    """
    Total GatewayNetworks count matching the filter.
    """


@dataclass
class ListGatewayTypesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListGatewayTypesResponse:
    types: List[GatewayType]
    """
    Available types of Public Gateway.
    """


@dataclass
class ListGatewaysRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListGatewaysRequestOrderBy]
    """
    Order in which to return results.
    """

    page: Optional[int]
    """
    Page number to return.
    """

    page_size: Optional[int]
    """
    Gateways per page.
    """

    organization_id: Optional[str]
    """
    Include only gateways in this Organization.
    """

    project_id: Optional[str]
    """
    Include only gateways in this Project.
    """

    name: Optional[str]
    """
    Filter for gateways which have this search term in their name.
    """

    tags: Optional[List[str]]
    """
    Filter for gateways with these tags.
    """

    type_: Optional[str]
    """
    Filter for gateways of this type.
    """

    status: Optional[GatewayStatus]
    """
    Filter for gateways with this current status. Use `unknown` to include all statuses.
    """

    private_network_id: Optional[str]
    """
    Filter for gateways attached to this Private nNetwork.
    """


@dataclass
class ListGatewaysResponse:
    gateways: List[Gateway]
    """
    Gateways on this page.
    """

    total_count: int
    """
    Total count of gateways matching the filter.
    """


@dataclass
class ListIPsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListIPsRequestOrderBy]
    """
    Order in which to return results.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    IP addresses per page.
    """

    organization_id: Optional[str]
    """
    Filter for IP addresses in this Organization.
    """

    project_id: Optional[str]
    """
    Filter for IP addresses in this Project.
    """

    tags: Optional[List[str]]
    """
    Filter for IP addresses with these tags.
    """

    reverse: Optional[str]
    """
    Filter for IP addresses that have a reverse containing this string.
    """

    is_free: Optional[bool]
    """
    Filter based on whether the IP is attached to a gateway or not.
    """


@dataclass
class ListIPsResponse:
    ips: List[IP]
    """
    IP addresses on this page.
    """

    total_count: int
    """
    Total count of IP addresses matching the filter.
    """


@dataclass
class ListPATRulesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListPATRulesRequestOrderBy]
    """
    Order in which to return results.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    PAT rules per page.
    """

    gateway_id: Optional[str]
    """
    Filter for PAT rules on this Gateway.
    """

    private_ip: Optional[str]
    """
    Filter for PAT rules targeting this private ip.
    """

    protocol: Optional[PATRuleProtocol]
    """
    Filter for PAT rules with this protocol.
    """


@dataclass
class ListPATRulesResponse:
    pat_rules: List[PATRule]
    """
    Array of PAT rules matching the filter.
    """

    total_count: int
    """
    Total count of PAT rules matching the filter.
    """


@dataclass
class RefreshSSHKeysRequest:
    gateway_id: str
    """
    ID of the gateway to refresh SSH keys on.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetDHCPEntriesRequest:
    gateway_network_id: str
    """
    ID of the Gateway Network on which to set DHCP reservation list.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    dhcp_entries: Optional[List[SetDHCPEntriesRequestEntry]]
    """
    New list of DHCP reservations.
    """


@dataclass
class SetDHCPEntriesResponse:
    dhcp_entries: List[DHCPEntry]
    """
    List of DHCP entries.
    """


@dataclass
class SetPATRulesRequest:
    gateway_id: str
    """
    ID of the gateway on which to set the PAT rules.
    """

    pat_rules: List[SetPATRulesRequestRule]
    """
    New list of PAT rules.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetPATRulesResponse:
    pat_rules: List[PATRule]
    """
    List of PAT rules.
    """


@dataclass
class UpdateDHCPEntryRequest:
    dhcp_entry_id: str
    """
    ID of the DHCP entry to update.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    ip_address: Optional[str]
    """
    New IP address to give to the device.
    """


@dataclass
class UpdateDHCPRequest:
    dhcp_id: str
    """
    DHCP configuration to update.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    subnet: Optional[str]
    """
    Subnet for the DHCP server.
    """

    address: Optional[str]
    """
    IP address of the DHCP server. This will be the Public Gateway's address in the Private Network. It must be part of config's subnet.
    """

    pool_low: Optional[str]
    """
    Low IP (inclusive) of the dynamic address pool. Must be in the config's subnet.
    """

    pool_high: Optional[str]
    """
    High IP (inclusive) of the dynamic address pool. Must be in the config's subnet.
    """

    enable_dynamic: Optional[bool]
    """
    Defines whether to enable dynamic pooling of IPs. When false, only pre-existing DHCP reservations will be handed out. Defaults to true.
    """

    valid_lifetime: Optional[str]
    """
    How long DHCP entries will be valid for.
    """

    renew_timer: Optional[str]
    """
    After how long a renew will be attempted. Must be 30s lower than `rebind_timer`.
    """

    rebind_timer: Optional[str]
    """
    After how long a DHCP client will query for a new lease if previous renews fail. Must be 30s lower than `valid_lifetime`.
    """

    push_default_route: Optional[bool]
    """
    Defines whether the gateway should push a default route to DHCP clients, or only hand out IPs.
    """

    push_dns_server: Optional[bool]
    """
    Defines whether the gateway should push custom DNS servers to clients. This allows for instance hostname -> IP resolution.
    """

    dns_servers_override: Optional[List[str]]
    """
    Array of DNS server IP addresses used to override the DNS server list pushed to DHCP clients, instead of the gateway itself.
    """

    dns_search: Optional[List[str]]
    """
    Array of search paths in addition to the pushed DNS configuration.
    """

    dns_local_name: Optional[str]
    """
    TLD given to hostnames in the Private Networks. If an instance with hostname `foo` gets a lease, and this is set to `bar`, `foo.bar` will resolve. Allowed characters are `a-z0-9-.`.
    """


@dataclass
class UpdateGatewayNetworkRequest:
    gateway_network_id: str
    """
    ID of the GatewayNetwork to update.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    enable_masquerade: Optional[bool]
    """
    Note: this setting is ignored when passing `ipam_config`.
    """

    enable_dhcp: Optional[bool]
    """
    Defaults to `true` if `dhcp_id` is present. If set to `true`, `dhcp_id` must be present.
Note: this setting is ignored when passing `ipam_config`.
    """

    dhcp_id: Optional[str]

    address: Optional[str]

    ipam_config: Optional[UpdateGatewayNetworkRequestIpamConfig]


@dataclass
class UpdateGatewayRequest:
    gateway_id: str
    """
    ID of the gateway to update.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name for the gateway.
    """

    tags: Optional[List[str]]
    """
    Tags for the gateway.
    """

    upstream_dns_servers: Optional[List[str]]
    """
    Array of DNS server IP addresses to override the gateway's default recursive DNS servers.
    """

    enable_bastion: Optional[bool]
    """
    Defines whether SSH bastion should be enabled the gateway.
    """

    bastion_port: Optional[int]
    """
    Port of the SSH bastion.
    """

    enable_smtp: Optional[bool]
    """
    Defines whether SMTP traffic should be allowed to pass through the gateway.
    """


@dataclass
class UpdateIPRequest:
    ip_id: str
    """
    ID of the IP address to update.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[List[str]]
    """
    Tags to give to the IP address.
    """

    reverse: Optional[str]
    """
    Reverse to set on the address. Empty string to unset.
    """

    gateway_id: Optional[str]
    """
    Gateway to attach the IP address to. Empty string to detach.
    """


@dataclass
class UpdatePATRuleRequest:
    pat_rule_id: str
    """
    ID of the PAT rule to update.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    public_port: Optional[int]
    """
    Public port to listen on.
    """

    private_ip: Optional[str]
    """
    Private IP to forward data to.
    """

    private_port: Optional[int]
    """
    Private port to translate to.
    """

    protocol: Optional[PATRuleProtocol]
    """
    Protocol the rule should apply to.
    """


@dataclass
class UpgradeGatewayRequest:
    gateway_id: str
    """
    ID of the gateway to upgrade.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    type_: Optional[str]
    """
    Gateway type (commercial offer).
    """
