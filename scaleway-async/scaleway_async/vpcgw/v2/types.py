# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    Zone as ScwZone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class GatewayNetworkStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    CREATED = "created"
    ATTACHING = "attaching"
    CONFIGURING = "configuring"
    READY = "ready"
    DETACHING = "detaching"

    def __str__(self) -> str:
        return str(self.value)


class GatewayStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    STOPPED = "stopped"
    ALLOCATING = "allocating"
    CONFIGURING = "configuring"
    RUNNING = "running"
    STOPPING = "stopping"
    FAILED = "failed"
    DELETING = "deleting"
    LOCKED = "locked"

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
    ADDRESS_ASC = "address_asc"
    ADDRESS_DESC = "address_desc"
    REVERSE_ASC = "reverse_asc"
    REVERSE_DESC = "reverse_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPatRulesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    PUBLIC_PORT_ASC = "public_port_asc"
    PUBLIC_PORT_DESC = "public_port_desc"

    def __str__(self) -> str:
        return str(self.value)


class PatRuleProtocol(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_PROTOCOL = "unknown_protocol"
    BOTH = "both"
    TCP = "tcp"
    UDP = "udp"

    def __str__(self) -> str:
        return str(self.value)


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

    masquerade_enabled: bool
    """
    Defines whether the gateway masquerades traffic for this Private Network (Dynamic NAT).
    """

    status: GatewayNetworkStatus
    """
    Current status of the Public Gateway's connection to the Private Network.
    """

    push_default_route: bool
    """
    Enabling the default route also enables masquerading.
    """

    ipam_ip_id: str
    """
    Use this IPAM-booked IP ID as the Gateway's IP in this Private Network.
    """

    zone: ScwZone
    """
    Zone of the GatewayNetwork connection.
    """

    created_at: Optional[datetime] = None
    """
    Connection creation date.
    """

    updated_at: Optional[datetime] = None
    """
    Connection last modification date.
    """

    mac_address: Optional[str] = None
    """
    MAC address of the gateway in the Private Network (if the gateway is up and running).
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

    tags: list[str]
    """
    Tags associated with the IP address.
    """

    address: str
    """
    The IP address itself.
    """

    zone: ScwZone
    """
    Zone of the IP address.
    """

    created_at: Optional[datetime] = None
    """
    IP address creation date.
    """

    updated_at: Optional[datetime] = None
    """
    IP address last modification date.
    """

    reverse: Optional[str] = None
    """
    Reverse domain name for the IP address.
    """

    gateway_id: Optional[str] = None
    """
    Public Gateway associated with the IP address.
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

    zone: ScwZone
    """
    Zone the Public Gateway type is available in.
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

    type_: str
    """
    Gateway type name (commercial offer).
    """

    bandwidth: int
    """
    Bandwidth available of the gateway.
    """

    status: GatewayStatus
    """
    Current status of the gateway.
    """

    name: str
    """
    Name of the gateway.
    """

    tags: list[str]
    """
    Tags associated with the gateway.
    """

    gateway_networks: list[GatewayNetwork]
    """
    GatewayNetwork objects attached to the gateway (each one represents a connection to a Private Network).
    """

    bastion_enabled: bool
    """
    Defines whether SSH bastion is enabled on the gateway.
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

    bastion_allowed_ips: list[str]
    """
    Ranges of IP addresses allowed to connect to the gateway's SSH bastion.
    """

    zone: ScwZone
    """
    Zone of the gateway.
    """

    created_at: Optional[datetime] = None
    """
    Gateway creation date.
    """

    updated_at: Optional[datetime] = None
    """
    Gateway last modification date.
    """

    ipv4: Optional[IP] = None
    """
    Public IPv4 address of the gateway.
    """

    version: Optional[str] = None
    """
    Version of the running gateway software.
    """

    can_upgrade_to: Optional[str] = None
    """
    Newly available gateway software version that can be updated to.
    """


@dataclass
class PatRule:
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

    protocol: PatRuleProtocol
    """
    Protocol the rule applies to.
    """

    zone: ScwZone
    """
    Zone of the PAT rule.
    """

    created_at: Optional[datetime] = None
    """
    PAT rule creation date.
    """

    updated_at: Optional[datetime] = None
    """
    PAT rule last modification date.
    """


@dataclass
class SetPatRulesRequestRule:
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

    protocol: PatRuleProtocol
    """
    Protocol the rule should apply to.
    """


@dataclass
class AddBastionAllowedIPsRequest:
    gateway_id: str
    """
    ID of the gateway to add the allowed IP range to.
    """

    ip_range: str
    """
    IP range allowed to connect to the SSH bastion.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class AddBastionAllowedIPsResponse:
    ip_ranges: list[str]
    """
    Ranges of IP addresses allowed to connect to the gateway's SSH bastion.
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
    Defines whether to enable masquerade (dynamic NAT) on the GatewayNetwork.
    """

    push_default_route: bool
    """
    Enabling the default route also enables masquerading.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    ipam_ip_id: Optional[str] = None
    """
    Use this IPAM-booked IP ID as the Gateway's IP in this Private Network.
    """


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

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    """
    Scaleway Project to create the gateway in.
    """

    name: Optional[str] = None
    """
    Name for the gateway.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags for the gateway.
    """

    ip_id: Optional[str] = None
    """
    Existing IP address to attach to the gateway.
    """

    bastion_port: Optional[int] = 0
    """
    Port of the SSH bastion.
    """


@dataclass
class CreateIPRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    """
    Project to create the IP address in.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to give to the IP address.
    """


@dataclass
class CreatePatRuleRequest:
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

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    protocol: Optional[PatRuleProtocol] = PatRuleProtocol.UNKNOWN_PROTOCOL
    """
    Protocol the rule should apply to.
    """


@dataclass
class DeleteBastionAllowedIPsRequest:
    gateway_id: str
    """
    ID of the gateway on which to delete the allowed IP range.
    """

    ip_range: str
    """
    IP range to delete from SSH bastion's list of allowed IPs.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteGatewayNetworkRequest:
    gateway_network_id: str
    """
    ID of the GatewayNetwork to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteGatewayRequest:
    gateway_id: str
    """
    ID of the gateway to delete.
    """

    delete_ip: bool
    """
    Defines whether the PGW's IP should be deleted.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteIPRequest:
    ip_id: str
    """
    ID of the IP address to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeletePatRuleRequest:
    pat_rule_id: str
    """
    ID of the PAT rule to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetGatewayNetworkRequest:
    gateway_network_id: str
    """
    ID of the GatewayNetwork to fetch.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetGatewayRequest:
    gateway_id: str
    """
    ID of the gateway to fetch.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetIPRequest:
    ip_id: str
    """
    ID of the IP address to get.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetPatRuleRequest:
    pat_rule_id: str
    """
    ID of the PAT rule to get.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListGatewayNetworksRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListGatewayNetworksRequestOrderBy] = (
        ListGatewayNetworksRequestOrderBy.CREATED_AT_ASC
    )
    """
    Order in which to return results.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    GatewayNetworks per page.
    """

    status: Optional[list[GatewayNetworkStatus]] = field(default_factory=list)
    """
    Filter for GatewayNetworks with these status. Use `unknown` to include all statuses.
    """

    gateway_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter for GatewayNetworks connected to these gateways.
    """

    private_network_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter for GatewayNetworks connected to these Private Networks.
    """

    masquerade_enabled: Optional[bool] = False
    """
    Filter for GatewayNetworks with this `enable_masquerade` setting.
    """


@dataclass
class ListGatewayNetworksResponse:
    gateway_networks: list[GatewayNetwork]
    """
    GatewayNetworks on this page.
    """

    total_count: int
    """
    Total GatewayNetworks count matching the filter.
    """


@dataclass
class ListGatewayTypesRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListGatewayTypesResponse:
    types: list[GatewayType]
    """
    Available types of Public Gateway.
    """


@dataclass
class ListGatewaysRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListGatewaysRequestOrderBy] = (
        ListGatewaysRequestOrderBy.CREATED_AT_ASC
    )
    """
    Order in which to return results.
    """

    page: Optional[int] = 0
    """
    Page number to return.
    """

    page_size: Optional[int] = 0
    """
    Gateways per page.
    """

    organization_id: Optional[str] = None
    """
    Include only gateways in this Organization.
    """

    project_id: Optional[str] = None
    """
    Include only gateways in this Project.
    """

    name: Optional[str] = None
    """
    Filter for gateways which have this search term in their name.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Filter for gateways with these tags.
    """

    types: Optional[list[str]] = field(default_factory=list)
    """
    Filter for gateways of these types.
    """

    status: Optional[list[GatewayStatus]] = field(default_factory=list)
    """
    Filter for gateways with these status. Use `unknown` to include all statuses.
    """

    private_network_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter for gateways attached to these Private Networks.
    """

    include_legacy: Optional[bool] = False
    """
    Include also legacy gateways.
    """


@dataclass
class ListGatewaysResponse:
    gateways: list[Gateway]
    """
    Gateways on this page.
    """

    total_count: int
    """
    Total count of gateways matching the filter.
    """


@dataclass
class ListIPsRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListIPsRequestOrderBy] = ListIPsRequestOrderBy.CREATED_AT_ASC
    """
    Order in which to return results.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    IP addresses per page.
    """

    organization_id: Optional[str] = None
    """
    Include only gateways in this Organization.
    """

    project_id: Optional[str] = None
    """
    Filter for IP addresses in this Project.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Filter for IP addresses with these tags.
    """

    reverse: Optional[str] = None
    """
    Filter for IP addresses that have a reverse containing this string.
    """

    is_free: Optional[bool] = False
    """
    Filter based on whether the IP is attached to a gateway or not.
    """


@dataclass
class ListIPsResponse:
    ips: list[IP]
    """
    IP addresses on this page.
    """

    total_count: int
    """
    Total count of IP addresses matching the filter.
    """


@dataclass
class ListPatRulesRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListPatRulesRequestOrderBy] = (
        ListPatRulesRequestOrderBy.CREATED_AT_ASC
    )
    """
    Order in which to return results.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    PAT rules per page.
    """

    gateway_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter for PAT rules on these gateways.
    """

    private_ips: Optional[list[str]] = field(default_factory=list)
    """
    Filter for PAT rules targeting these private ips.
    """

    protocol: Optional[PatRuleProtocol] = PatRuleProtocol.UNKNOWN_PROTOCOL
    """
    Filter for PAT rules with this protocol.
    """


@dataclass
class ListPatRulesResponse:
    pat_rules: list[PatRule]
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

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetBastionAllowedIPsRequest:
    gateway_id: str
    """
    ID of the gateway on which to set the allowed IP range.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    ip_ranges: Optional[list[str]] = field(default_factory=list)
    """
    New list of IP ranges (each range in CIDR notation) allowed to connect to the SSH bastion.
    """


@dataclass
class SetBastionAllowedIPsResponse:
    ip_ranges: list[str]
    """
    Ranges of IP addresses allowed to connect to the gateway's SSH bastion.
    """


@dataclass
class SetPatRulesRequest:
    gateway_id: str
    """
    ID of the gateway on which to set the PAT rules.
    """

    pat_rules: list[SetPatRulesRequestRule]
    """
    New list of PAT rules.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetPatRulesResponse:
    pat_rules: list[PatRule]
    """
    List of PAT rules.
    """


@dataclass
class UpdateGatewayNetworkRequest:
    gateway_network_id: str
    """
    ID of the GatewayNetwork to update.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    enable_masquerade: Optional[bool] = False
    """
    Defines whether to enable masquerade (dynamic NAT) on the GatewayNetwork.
    """

    push_default_route: Optional[bool] = False
    """
    Enabling the default route also enables masquerading.
    """

    ipam_ip_id: Optional[str] = None
    """
    Use this IPAM-booked IP ID as the Gateway's IP in this Private Network.
    """


@dataclass
class UpdateGatewayRequest:
    gateway_id: str
    """
    ID of the gateway to update.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    Name for the gateway.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags for the gateway.
    """

    enable_bastion: Optional[bool] = False
    """
    Defines whether SSH bastion should be enabled the gateway.
    """

    bastion_port: Optional[int] = 0
    """
    Port of the SSH bastion.
    """

    enable_smtp: Optional[bool] = False
    """
    Defines whether SMTP traffic should be allowed to pass through the gateway.
    """


@dataclass
class UpdateIPRequest:
    ip_id: str
    """
    ID of the IP address to update.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to give to the IP address.
    """

    reverse: Optional[str] = None
    """
    Reverse to set on the address. Empty string to unset.
    """

    gateway_id: Optional[str] = None
    """
    Gateway to attach the IP address to. Empty string to detach.
    """


@dataclass
class UpdatePatRuleRequest:
    pat_rule_id: str
    """
    ID of the PAT rule to update.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    public_port: Optional[int] = 0
    """
    Public port to listen on.
    """

    private_ip: Optional[str] = None
    """
    Private IP to forward data to.
    """

    private_port: Optional[int] = 0
    """
    Private port to translate to.
    """

    protocol: Optional[PatRuleProtocol] = PatRuleProtocol.UNKNOWN_PROTOCOL
    """
    Protocol the rule should apply to.
    """


@dataclass
class UpgradeGatewayRequest:
    gateway_id: str
    """
    ID of the gateway to upgrade.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    type_: Optional[str] = None
    """
    Gateway type (commercial offer).
    """
