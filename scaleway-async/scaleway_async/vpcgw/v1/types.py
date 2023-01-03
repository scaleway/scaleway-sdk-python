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


class DHCPEntryType(str, Enum):
    UNKNOWN = "unknown"
    RESERVATION = "reservation"
    LEASE = "lease"

    def __str__(self) -> str:
        return str(self.value)


class GatewayNetworkStatus(str, Enum):
    UNKNOWN = "unknown"
    CREATED = "created"
    ATTACHING = "attaching"
    CONFIGURING = "configuring"
    READY = "ready"
    DETACHING = "detaching"
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)


class GatewayStatus(str, Enum):
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


class ListDHCPEntriesRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    IP_ADDRESS_ASC = "ip_address_asc"
    IP_ADDRESS_DESC = "ip_address_desc"
    HOSTNAME_ASC = "hostname_asc"
    HOSTNAME_DESC = "hostname_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListDHCPsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    SUBNET_ASC = "subnet_asc"
    SUBNET_DESC = "subnet_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListGatewayNetworksRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListGatewaysRequestOrderBy(str, Enum):
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


class ListIPsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    IP_ASC = "ip_asc"
    IP_DESC = "ip_desc"
    REVERSE_ASC = "reverse_asc"
    REVERSE_DESC = "reverse_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPATRulesRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    PUBLIC_PORT_ASC = "public_port_asc"
    PUBLIC_PORT_DESC = "public_port_desc"

    def __str__(self) -> str:
        return str(self.value)


class PATRuleProtocol(str, Enum):
    UNKNOWN = "unknown"
    BOTH = "both"
    TCP = "tcp"
    UDP = "udp"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class DHCP:
    """
    Dhcp
    """

    id: str
    """
    ID of the DHCP config
    """

    organization_id: str
    """
    Owning organization
    """

    project_id: str
    """
    Owning project
    """

    created_at: Optional[datetime]
    """
    Configuration creation date
    """

    updated_at: Optional[datetime]
    """
    Configuration last modification date
    """

    subnet: str
    """
    Subnet for the DHCP server
    """

    address: str
    """
    Address of the DHCP server. This will be the gateway's address in the private network. It must be part of config's subnet.
    
    """

    pool_low: str
    """
    Low IP (included) of the dynamic address pool. Must be in the config's subnet
    """

    pool_high: str
    """
    High IP (included) of the dynamic address pool. Must be in the config's subnet
    """

    enable_dynamic: bool
    """
    Whether to enable dynamic pooling of IPs. By turning the dynamic pool off, only pre-existing DHCP reservations will be handed out.
    
    """

    valid_lifetime: Optional[str]
    """
    How long, in seconds, DHCP entries will be valid for
    """

    renew_timer: Optional[str]
    """
    After how long, in seconds, a renew will be attempted. Must be 30s lower than `rebind_timer`.
    
    """

    rebind_timer: Optional[str]
    """
    After how long, in seconds, a DHCP client will query for a new lease if previous renews fail. Must be 30s lower than `valid_lifetime`.
    
    """

    push_default_route: bool
    """
    Whether the gateway should push a default route to DHCP clients or only hand out IPs
    """

    push_dns_server: bool
    """
    Whether the gateway should push custom DNS servers to clients. This allows for instance hostname -> IP resolution.
    
    """

    dns_servers_override: List[str]
    """
    Override the DNS server list pushed to DHCP clients, instead of the gateway itself
    """

    dns_search: List[str]
    """
    Add search paths to the pushed DNS configuration
    """

    dns_local_name: str
    """
    TLD given to hostnames in the Private Network. If an instance with hostname `foo` gets a lease, and this is set to `bar`, `foo.bar` will resolve.
    
    """

    zone: Zone
    """
    Zone this configuration is available in
    """


@dataclass
class DHCPEntry:
    """
    Dhcp entry
    """

    id: str
    """
    Entry ID
    """

    created_at: Optional[datetime]
    """
    Configuration creation date
    """

    updated_at: Optional[datetime]
    """
    Configuration last modification date
    """

    gateway_network_id: str
    """
    Owning GatewayNetwork
    """

    mac_address: str
    """
    MAC address of the client machine
    """

    ip_address: str
    """
    Assigned IP address
    """

    hostname: str
    """
    Hostname of the client machine
    """

    type_: DHCPEntryType
    """
    Entry type, either static (DHCP reservation) or dynamic (DHCP lease)
    """

    zone: Zone
    """
    Zone this entry is available in
    """


@dataclass
class Gateway:
    """
    Gateway
    """

    id: str
    """
    ID of the gateway
    """

    organization_id: str
    """
    Owning organization
    """

    project_id: str
    """
    Owning project
    """

    created_at: Optional[datetime]
    """
    Gateway creation date
    """

    updated_at: Optional[datetime]
    """
    Gateway last modification date
    """

    type_: Optional[GatewayType]
    """
    Gateway type
    """

    status: GatewayStatus
    """
    Gateway's current status
    """

    name: str
    """
    Name of the gateway
    """

    tags: List[str]
    """
    Tags of the gateway
    """

    ip: Optional[IP]
    """
    Public IP of the gateway
    """

    gateway_networks: List[GatewayNetwork]
    """
    GatewayNetworks attached to the gateway
    """

    upstream_dns_servers: List[str]
    """
    Override the gateway's default recursive DNS servers
    """

    version: Optional[str]
    """
    Version of the running gateway software
    """

    can_upgrade_to: Optional[str]
    """
    Newly available gateway software version that can be updated to
    """

    bastion_enabled: bool
    """
    Whether SSH bastion is enabled on the gateway
    """

    bastion_port: int
    """
    Port of the SSH bastion
    """

    smtp_enabled: bool
    """
    Whether SMTP traffic is allowed to pass through the gateway
    """

    zone: Zone
    """
    Zone the gateway is available in
    """


@dataclass
class GatewayNetwork:
    """
    Gateway network
    """

    id: str
    """
    ID of the connection
    """

    created_at: Optional[datetime]
    """
    Connection creation date
    """

    updated_at: Optional[datetime]
    """
    Connection last modification date
    """

    gateway_id: str
    """
    ID of the connected gateway
    """

    private_network_id: str
    """
    ID of the connected private network
    """

    mac_address: Optional[str]
    """
    MAC address of the gateway in the network (if the gateway is up and running)
    """

    enable_masquerade: bool
    """
    Whether the gateway masquerades traffic for this network
    """

    status: GatewayNetworkStatus
    """
    Current status of the gateway network connection
    """

    dhcp: Optional[DHCP]
    """
    DHCP configuration for the connected private network
    """

    enable_dhcp: bool
    """
    Whether DHCP is enabled on the connected Private Network
    """

    address: Optional[str]
    """
    Address of the Gateway in CIDR form to use when DHCP is not used
    """

    zone: Zone
    """
    Zone the connection lives in
    """


@dataclass
class GatewayType:
    """
    Gateway type
    """

    name: str
    """
    Type name
    """

    bandwidth: int
    """
    Bandwidth, in bps, the gateway has. This is the public bandwidth to the outer internet, and the internal bandwidth to each connected Private Networks.
    
    """

    zone: Zone
    """
    Zone the type is available in
    """


@dataclass
class IP:
    """
    Ip
    """

    id: str
    """
    IP ID
    """

    organization_id: str
    """
    Owning organization
    """

    project_id: str
    """
    Owning project
    """

    created_at: Optional[datetime]
    """
    Configuration creation date
    """

    updated_at: Optional[datetime]
    """
    Configuration last modification date
    """

    tags: List[str]
    """
    Tags associated with the IP
    """

    address: str
    """
    The IP itself
    """

    reverse: Optional[str]
    """
    Reverse domain name for the IP address
    """

    gateway_id: Optional[str]
    """
    Gateway associated to the IP
    """

    zone: Zone
    """
    Zone this IP is available in
    """


@dataclass
class ListDHCPEntriesResponse:
    """
    List dhcp entries response
    """

    dhcp_entries: List[DHCPEntry]
    """
    DHCP entries in this page
    """

    total_count: int
    """
    Total DHCP entries matching the filter
    """


@dataclass
class ListDHCPsResponse:
    """
    List dhc ps response
    """

    dhcps: List[DHCP]
    """
    First page of DHCP configs
    """

    total_count: int
    """
    Total DHCP configs matching the filter
    """


@dataclass
class ListGatewayNetworksResponse:
    """
    List gateway networks response
    """

    gateway_networks: List[GatewayNetwork]
    """
    GatewayNetworks in this page
    """

    total_count: int
    """
    Total GatewayNetworks count matching the filter
    """


@dataclass
class ListGatewayTypesResponse:
    """
    List gateway types response
    """

    types: List[GatewayType]
    """
    Available types of gateway
    """


@dataclass
class ListGatewaysResponse:
    """
    List gateways response
    """

    gateways: List[Gateway]
    """
    Gateways in this page
    """

    total_count: int
    """
    Total count of gateways matching the filter
    """


@dataclass
class ListIPsResponse:
    """
    List i ps response
    """

    ips: List[IP]
    """
    IPs in this page
    """

    total_count: int
    """
    Total IP count matching the filter
    """


@dataclass
class ListPATRulesResponse:
    """
    List pat rules response
    """

    pat_rules: List[PATRule]
    """
    This page of PAT rules matching the filter
    """

    total_count: int
    """
    Total PAT rules matching the filter
    """


@dataclass
class PATRule:
    """
    Pat rule
    """

    id: str
    """
    Rule ID
    """

    gateway_id: str
    """
    Gateway the PAT rule applies to
    """

    created_at: Optional[datetime]
    """
    Rule creation date
    """

    updated_at: Optional[datetime]
    """
    Rule last modification date
    """

    public_port: int
    """
    Public port to listen on
    """

    private_ip: str
    """
    Private IP to forward data to
    """

    private_port: int
    """
    Private port to translate to
    """

    protocol: PATRuleProtocol
    """
    Protocol the rule applies to
    """

    zone: Zone
    """
    Zone this rule is available in
    """


@dataclass
class SetDHCPEntriesRequestEntry:
    """
    Set dhcp entries request. entry
    """

    mac_address: str
    """
    MAC address to give a static entry to. A matching entry will be upgraded to a reservation, and a matching reservation will be updated.
    
    """

    ip_address: str
    """
    IP address to give to the machine
    """


@dataclass
class SetDHCPEntriesResponse:
    """
    Set dhcp entries response
    """

    dhcp_entries: List[DHCPEntry]
    """
    List of DHCP entries
    """


@dataclass
class SetPATRulesRequestRule:
    """
    Set pat rules request. rule
    """

    public_port: int
    """
    Public port to listen on. Uniquely identifies the rule, and a matching rule will be updated with the new parameters.
    
    """

    private_ip: str
    """
    Private IP to forward data to
    """

    private_port: int
    """
    Private port to translate to
    """

    protocol: PATRuleProtocol
    """
    Protocol the rule should apply to
    """


@dataclass
class SetPATRulesResponse:
    """
    Set pat rules response
    """

    pat_rules: List[PATRule]
    """
    List of PAT rules
    """


@dataclass
class ListGatewaysRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    order_by: Optional[ListGatewaysRequestOrderBy]
    """
    Order in which to return results
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    Gateways per page
    """

    organization_id: Optional[str]
    """
    Include only gateways in this organization
    """

    project_id: Optional[str]
    """
    Include only gateways in this project
    """

    name: Optional[str]
    """
    Filter gateways including this name
    """

    tags: Optional[List[str]]
    """
    Filter gateways with these tags
    """

    type_: Optional[str]
    """
    Filter gateways of this type
    """

    status: Optional[GatewayStatus]
    """
    Filter gateways in this status (unknown for any)
    """

    private_network_id: Optional[str]
    """
    Filter gateways attached to this private network
    """


@dataclass
class GetGatewayRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    gateway_id: str
    """
    ID of the gateway to fetch
    """


@dataclass
class CreateGatewayRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    project_id: Optional[str]
    """
    Project to create the gateway into
    """

    name: Optional[str]
    """
    Name of the gateway
    """

    tags: Optional[List[str]]
    """
    Tags for the gateway
    """

    type_: str
    """
    Gateway type
    """

    upstream_dns_servers: Optional[List[str]]
    """
    Override the gateway's default recursive DNS servers, if DNS features are enabled
    """

    ip_id: Optional[str]
    """
    Attach an existing IP to the gateway
    """

    enable_smtp: bool
    """
    Allow SMTP traffic to pass through the gateway
    """

    enable_bastion: bool
    """
    Enable SSH bastion on the gateway
    """

    bastion_port: Optional[int]
    """
    Port of the SSH bastion
    """


@dataclass
class UpdateGatewayRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    gateway_id: str
    """
    ID of the gateway to update
    """

    name: Optional[str]
    """
    Name fo the gateway
    """

    tags: Optional[List[str]]
    """
    Tags for the gateway
    """

    upstream_dns_servers: Optional[List[str]]
    """
    Override the gateway's default recursive DNS servers, if DNS features are enabled
    """

    enable_bastion: Optional[bool]
    """
    Enable SSH bastion on the gateway
    """

    bastion_port: Optional[int]
    """
    Port of the SSH bastion
    """

    enable_smtp: Optional[bool]
    """
    Allow SMTP traffic to pass through the gateway
    """


@dataclass
class DeleteGatewayRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    gateway_id: str
    """
    ID of the gateway to delete
    """

    cleanup_dhcp: bool
    """
    Whether to cleanup attached DHCP configurations (if any, and if not attached to another Gateway Network).
    
    """


@dataclass
class UpgradeGatewayRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    gateway_id: str
    """
    ID of the gateway to upgrade
    """


@dataclass
class ListGatewayNetworksRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    order_by: Optional[ListGatewayNetworksRequestOrderBy]
    """
    Order in which to return results
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    GatewayNetworks per page
    """

    gateway_id: Optional[str]
    """
    Filter by gateway
    """

    private_network_id: Optional[str]
    """
    Filter by private network
    """

    enable_masquerade: Optional[bool]
    """
    Filter by masquerade enablement
    """

    dhcp_id: Optional[str]
    """
    Filter by DHCP configuration
    """

    status: Optional[GatewayNetworkStatus]
    """
    Filter GatewayNetworks by this status (unknown for any)
    """


@dataclass
class GetGatewayNetworkRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    gateway_network_id: str
    """
    ID of the GatewayNetwork to fetch
    """


@dataclass
class CreateGatewayNetworkRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    gateway_id: str
    """
    Gateway to connect
    """

    private_network_id: str
    """
    Private Network to connect
    """

    enable_masquerade: bool
    """
    Whether to enable masquerade on this network
    """

    dhcp_id: Optional[str]
    """
    Existing configuration.
    
    One-of ('ip_config'): at most one of 'dhcp_id', 'address' could be set.
    """

    address: Optional[str]
    """
    Static IP address in CIDR format to to use without DHCP.
    
    One-of ('ip_config'): at most one of 'dhcp_id', 'address' could be set.
    """

    enable_dhcp: Optional[bool]
    """
    Whether to enable DHCP on this Private Network. Defaults to `true` if either `dhcp_id` or `dhcp` short: are present. If set to `true`, requires that either `dhcp_id` or `dhcp` to be present.
    
    """


@dataclass
class UpdateGatewayNetworkRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    gateway_network_id: str
    """
    ID of the GatewayNetwork to update
    """

    enable_masquerade: Optional[bool]
    """
    New masquerade enablement
    """

    dhcp_id: Optional[str]
    """
    New DHCP configuration.
    
    One-of ('ip_config'): at most one of 'dhcp_id', 'address' could be set.
    """

    enable_dhcp: Optional[bool]
    """
    Whether to enable DHCP on the connected Private Network
    """

    address: Optional[str]
    """
    New static IP address.
    
    One-of ('ip_config'): at most one of 'dhcp_id', 'address' could be set.
    """


@dataclass
class DeleteGatewayNetworkRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    gateway_network_id: str
    """
    GatewayNetwork to delete
    """

    cleanup_dhcp: bool
    """
    Whether to cleanup the attached DHCP configuration (if any, and if not attached to another gateway_network).
    
    """


@dataclass
class ListDHCPsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    order_by: Optional[ListDHCPsRequestOrderBy]
    """
    Order in which to return results
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    DHCP configurations per page
    """

    organization_id: Optional[str]
    """
    Include only DHCPs in this organization
    """

    project_id: Optional[str]
    """
    Include only DHCPs in this project
    """

    address: Optional[str]
    """
    Filter on gateway address
    """

    has_address: Optional[str]
    """
    Filter on subnets containing address
    """


@dataclass
class GetDHCPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    dhcp_id: str
    """
    ID of the DHCP config to fetch
    """


@dataclass
class CreateDHCPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    project_id: Optional[str]
    """
    Project to create the DHCP configuration in
    """

    subnet: str
    """
    Subnet for the DHCP server
    """

    address: Optional[str]
    """
    Address of the DHCP server. This will be the gateway's address in the private network. Defaults to the first address of the subnet
    """

    pool_low: Optional[str]
    """
    Low IP (included) of the dynamic address pool. Defaults to the second address of the subnet.
    """

    pool_high: Optional[str]
    """
    High IP (included) of the dynamic address pool. Defaults to the last address of the subnet.
    """

    enable_dynamic: Optional[bool]
    """
    Whether to enable dynamic pooling of IPs. By turning the dynamic pool off, only pre-existing DHCP reservations will be handed out. Defaults to true.
    
    """

    valid_lifetime: Optional[str]
    """
    For how long, in seconds, will DHCP entries will be valid. Defaults to 1h (3600s).
    """

    renew_timer: Optional[str]
    """
    After how long, in seconds, a renew will be attempted. Must be 30s lower than `rebind_timer`. Defaults to 50m (3000s).
    
    """

    rebind_timer: Optional[str]
    """
    After how long, in seconds, a DHCP client will query for a new lease if previous renews fail. Must be 30s lower than `valid_lifetime`. Defaults to 51m (3060s).
    
    """

    push_default_route: Optional[bool]
    """
    Whether the gateway should push a default route to DHCP clients or only hand out IPs. Defaults to true
    """

    push_dns_server: Optional[bool]
    """
    Whether the gateway should push custom DNS servers to clients. This allows for instance hostname -> IP resolution. Defaults to true.
    
    """

    dns_servers_override: Optional[List[str]]
    """
    Override the DNS server list pushed to DHCP clients, instead of the gateway itself
    """

    dns_search: Optional[List[str]]
    """
    Additional DNS search paths
    """

    dns_local_name: Optional[str]
    """
    TLD given to hostnames in the Private Network. Allowed characters are `a-z0-9-.`. Defaults to the slugified Private Network name if created along a GatewayNetwork, or else to `priv`.
    
    """


@dataclass
class UpdateDHCPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    dhcp_id: str
    """
    DHCP config to update
    """

    subnet: Optional[str]
    """
    Subnet for the DHCP server
    """

    address: Optional[str]
    """
    Address of the DHCP server. This will be the gateway's address in the private network
    """

    pool_low: Optional[str]
    """
    Low IP (included) of the dynamic address pool
    """

    pool_high: Optional[str]
    """
    High IP (included) of the dynamic address pool
    """

    enable_dynamic: Optional[bool]
    """
    Whether to enable dynamic pooling of IPs. By turning the dynamic pool off, only pre-existing DHCP reservations will be handed out. Defaults to true.
    
    """

    valid_lifetime: Optional[str]
    """
    How long, in seconds, DHCP entries will be valid for
    """

    renew_timer: Optional[str]
    """
    After how long, in seconds, a renew will be attempted. Must be 30s lower than `rebind_timer`.
    """

    rebind_timer: Optional[str]
    """
    After how long, in seconds, a DHCP client will query for a new lease if previous renews fail. Must be 30s lower than `valid_lifetime`.
    
    """

    push_default_route: Optional[bool]
    """
    Whether the gateway should push a default route to DHCP clients or only hand out IPs
    """

    push_dns_server: Optional[bool]
    """
    Whether the gateway should push custom DNS servers to clients. This allows for instance hostname -> IP resolution.
    
    """

    dns_servers_override: Optional[List[str]]
    """
    Override the DNS server list pushed to DHCP clients, instead of the gateway itself
    """

    dns_search: Optional[List[str]]
    """
    Additional DNS search paths
    """

    dns_local_name: Optional[str]
    """
    TLD given to hostnames in the Private Network. Allowed characters are `a-z0-9-.`.
    """


@dataclass
class DeleteDHCPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    dhcp_id: str
    """
    DHCP config id to delete
    """


@dataclass
class ListDHCPEntriesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    order_by: Optional[ListDHCPEntriesRequestOrderBy]
    """
    Order in which to return results
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    DHCP entries per page
    """

    gateway_network_id: Optional[str]
    """
    Filter entries based on the gateway network they are on
    """

    mac_address: Optional[str]
    """
    Filter entries on their MAC address
    """

    ip_address: Optional[str]
    """
    Filter entries on their IP address
    """

    hostname: Optional[str]
    """
    Filter entries on their hostname substring
    """

    type_: Optional[DHCPEntryType]
    """
    Filter entries on their type
    """


@dataclass
class GetDHCPEntryRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    dhcp_entry_id: str
    """
    ID of the DHCP entry to fetch
    """


@dataclass
class CreateDHCPEntryRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    gateway_network_id: str
    """
    GatewayNetwork on which to create a DHCP reservation
    """

    mac_address: str
    """
    MAC address to give a static entry to
    """

    ip_address: str
    """
    IP address to give to the machine
    """


@dataclass
class UpdateDHCPEntryRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    dhcp_entry_id: str
    """
    DHCP entry ID to update
    """

    ip_address: Optional[str]
    """
    New IP address to give to the machine
    """


@dataclass
class SetDHCPEntriesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    gateway_network_id: str
    """
    Gateway Network on which to set DHCP reservation list
    """

    dhcp_entries: Optional[List[SetDHCPEntriesRequestEntry]]
    """
    New list of DHCP reservations
    """


@dataclass
class DeleteDHCPEntryRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    dhcp_entry_id: str
    """
    DHCP entry ID to delete
    """


@dataclass
class ListPATRulesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    order_by: Optional[ListPATRulesRequestOrderBy]
    """
    Order in which to return results
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    PAT rules per page
    """

    gateway_id: Optional[str]
    """
    Fetch rules for this gateway
    """

    private_ip: Optional[str]
    """
    Fetch rules targeting this private ip
    """

    protocol: Optional[PATRuleProtocol]
    """
    Fetch rules for this protocol
    """


@dataclass
class GetPATRuleRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    pat_rule_id: str
    """
    PAT rule to get
    """


@dataclass
class CreatePATRuleRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    gateway_id: str
    """
    Gateway on which to attach the rule to
    """

    public_port: int
    """
    Public port to listen on
    """

    private_ip: str
    """
    Private IP to forward data to
    """

    private_port: int
    """
    Private port to translate to
    """

    protocol: PATRuleProtocol
    """
    Protocol the rule should apply to
    """


@dataclass
class UpdatePATRuleRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    pat_rule_id: str
    """
    PAT rule to update
    """

    public_port: Optional[int]
    """
    Public port to listen on
    """

    private_ip: Optional[str]
    """
    Private IP to forward data to
    """

    private_port: Optional[int]
    """
    Private port to translate to
    """

    protocol: PATRuleProtocol
    """
    Protocol the rule should apply to
    """


@dataclass
class SetPATRulesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    gateway_id: str
    """
    Gateway on which to set the PAT rules
    """

    pat_rules: List[SetPATRulesRequestRule]
    """
    New list of PAT rules
    """


@dataclass
class DeletePATRuleRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    pat_rule_id: str
    """
    PAT rule to delete
    """


@dataclass
class ListGatewayTypesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """


@dataclass
class ListIPsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    order_by: Optional[ListIPsRequestOrderBy]
    """
    Order in which to return results
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    IPs per page
    """

    organization_id: Optional[str]
    """
    Include only IPs in this organization
    """

    project_id: Optional[str]
    """
    Include only IPs in this project
    """

    tags: Optional[List[str]]
    """
    Filter IPs with these tags
    """

    reverse: Optional[str]
    """
    Filter by reverse containing this string
    """

    is_free: Optional[bool]
    """
    Filter whether the IP is attached to a gateway or not
    """


@dataclass
class GetIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    ip_id: str
    """
    ID of the IP to get
    """


@dataclass
class CreateIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    project_id: Optional[str]
    """
    Project to create the IP into
    """

    tags: Optional[List[str]]
    """
    Tags to give to the IP
    """


@dataclass
class UpdateIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    ip_id: str
    """
    ID of the IP to update
    """

    tags: Optional[List[str]]
    """
    Tags to give to the IP
    """

    reverse: Optional[str]
    """
    Reverse to set on the IP. Empty string to unset
    """

    gateway_id: Optional[str]
    """
    Gateway to attach the IP to. Empty string to detach
    """


@dataclass
class DeleteIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    ip_id: str
    """
    ID of the IP to delete
    """


@dataclass
class RefreshSSHKeysRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    gateway_id: str
