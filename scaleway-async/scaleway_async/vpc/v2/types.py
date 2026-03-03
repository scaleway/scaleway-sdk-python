# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class AclRuleProtocol(str, Enum, metaclass=StrEnumMeta):
    ANY = "any"
    TCP = "tcp"
    UDP = "udp"
    ICMP = "icmp"

    def __str__(self) -> str:
        return str(self.value)


class Action(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ACTION = "unknown_action"
    ACCEPT = "accept"
    DROP = "drop"

    def __str__(self) -> str:
        return str(self.value)


class ListPrivateNetworksRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListSubnetsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListVPCsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class RouteType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ROUTE_TYPE = "unknown_route_type"
    SUBNET = "subnet"
    DEFAULT = "default"
    CUSTOM = "custom"
    INTERLINK = "interlink"
    S2S_VPN = "s2s_vpn"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Subnet:
    id: str
    """
    ID of the subnet.
    """

    subnet: str
    """
    Subnet CIDR.
    """

    project_id: str
    """
    Scaleway Project the subnet belongs to.
    """

    private_network_id: str
    """
    Private Network the subnet belongs to.
    """

    vpc_id: str
    """
    VPC the subnet belongs to.
    """

    created_at: Optional[datetime] = None
    """
    Subnet creation date.
    """

    updated_at: Optional[datetime] = None
    """
    Subnet last modification date.
    """


@dataclass
class PrivateNetwork:
    id: str
    """
    Private Network ID.
    """

    name: str
    """
    Private Network name.
    """

    organization_id: str
    """
    Scaleway Organization the Private Network belongs to.
    """

    project_id: str
    """
    Scaleway Project the Private Network belongs to.
    """

    region: ScwRegion
    """
    Region in which the Private Network is available.
    """

    tags: list[str]
    """
    Tags of the Private Network.
    """

    subnets: list[Subnet]
    """
    Private Network subnets.
    """

    vpc_id: str
    """
    VPC the Private Network belongs to.
    """

    dhcp_enabled: bool
    """
    Defines whether managed DHCP is enabled for this Private Network.
    """

    default_route_propagation_enabled: bool
    """
    Defines whether default v4 and v6 routes are propagated for this Private Network.
    """

    created_at: Optional[datetime] = None
    """
    Date the Private Network was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date the Private Network was last modified.
    """


@dataclass
class Route:
    id: str
    """
    Route ID.
    """

    description: str
    """
    Route description.
    """

    tags: list[str]
    """
    Tags of the Route.
    """

    vpc_id: str
    """
    VPC the Route belongs to.
    """

    destination: str
    """
    Destination of the Route.
    """

    is_read_only: bool
    """
    Defines whether the route can be modified or deleted by the user.
    """

    region: ScwRegion
    """
    Region of the Route.
    """

    nexthop_resource_id: Optional[str] = None
    """
    ID of the nexthop resource.
    """

    nexthop_private_network_id: Optional[str] = None
    """
    ID of the nexthop private network.
    """

    nexthop_vpc_connector_id: Optional[str] = None
    """
    ID of the nexthop VPC connector.
    """

    created_at: Optional[datetime] = None
    """
    Date the Route was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date the Route was last modified.
    """

    type_: Optional[RouteType] = RouteType.UNKNOWN_ROUTE_TYPE
    """
    Type of the Route.
    """


@dataclass
class AclRule:
    protocol: AclRuleProtocol
    """
    Protocol to which this rule applies.
    """

    source: str
    """
    Source IP range to which this rule applies (CIDR notation with subnet mask).
    """

    src_port_low: int
    """
    Starting port of the source port range to which this rule applies (inclusive).
    """

    src_port_high: int
    """
    Ending port of the source port range to which this rule applies (inclusive).
    """

    destination: str
    """
    Destination IP range to which this rule applies (CIDR notation with subnet mask).
    """

    dst_port_low: int
    """
    Starting port of the destination port range to which this rule applies (inclusive).
    """

    dst_port_high: int
    """
    Ending port of the destination port range to which this rule applies (inclusive).
    """

    action: Action
    """
    Policy to apply to the packet.
    """

    description: Optional[str] = None
    """
    Rule description.
    """


@dataclass
class VPC:
    id: str
    """
    VPC ID.
    """

    name: str
    """
    VPC name.
    """

    organization_id: str
    """
    Scaleway Organization the VPC belongs to.
    """

    project_id: str
    """
    Scaleway Project the VPC belongs to.
    """

    region: ScwRegion
    """
    Region of the VPC.
    """

    tags: list[str]
    """
    Tags for the VPC.
    """

    is_default: bool
    """
    Defines whether the VPC is the default one for its Project.
    """

    private_network_count: int
    """
    Number of Private Networks within this VPC.
    """

    routing_enabled: bool
    """
    Defines whether the VPC routes traffic between its Private Networks.
    """

    custom_routes_propagation_enabled: bool
    """
    Defines whether the VPC advertises custom routes between its Private Networks.
    """

    created_at: Optional[datetime] = None
    """
    Date the VPC was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date the VPC was last modified.
    """


@dataclass
class AddSubnetsRequest:
    private_network_id: str
    """
    Private Network ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    subnets: Optional[list[str]] = field(default_factory=list)
    """
    Private Network subnets CIDR.
    """


@dataclass
class AddSubnetsResponse:
    subnets: list[str]


@dataclass
class CreatePrivateNetworkRequest:
    default_route_propagation_enabled: bool
    """
    Defines whether default v4 and v6 routes are propagated for this Private Network.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name for the Private Network.
    """

    project_id: Optional[str] = None
    """
    Scaleway Project in which to create the Private Network.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags for the Private Network.
    """

    subnets: Optional[list[str]] = field(default_factory=list)
    """
    Private Network subnets CIDR.
    """

    vpc_id: Optional[str] = None
    """
    VPC in which to create the Private Network.
    """


@dataclass
class CreateRouteRequest:
    description: str
    """
    Route description.
    """

    vpc_id: str
    """
    VPC the Route belongs to.
    """

    destination: str
    """
    Destination of the Route.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the Route.
    """

    nexthop_resource_id: Optional[str] = None
    """
    ID of the nexthop resource.
    """

    nexthop_private_network_id: Optional[str] = None
    """
    ID of the nexthop private network.
    """

    nexthop_vpc_connector_id: Optional[str] = None
    """
    ID of the nexthop VPC Connector.
    """


@dataclass
class CreateVPCRequest:
    enable_routing: bool
    """
    Enable routing between Private Networks in the VPC.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name for the VPC.
    """

    project_id: Optional[str] = None
    """
    Scaleway Project in which to create the VPC.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags for the VPC.
    """


@dataclass
class DeletePrivateNetworkRequest:
    private_network_id: str
    """
    Private Network ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteRouteRequest:
    route_id: str
    """
    Route ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteSubnetsRequest:
    private_network_id: str
    """
    Private Network ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    subnets: Optional[list[str]] = field(default_factory=list)
    """
    Private Network subnets CIDR.
    """


@dataclass
class DeleteSubnetsResponse:
    subnets: list[str]


@dataclass
class DeleteVPCRequest:
    vpc_id: str
    """
    VPC ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class EnableCustomRoutesPropagationRequest:
    vpc_id: str
    """
    VPC ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class EnableDHCPRequest:
    private_network_id: str
    """
    Private Network ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class EnableRoutingRequest:
    vpc_id: str
    """
    VPC ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetAclRequest:
    vpc_id: str
    """
    ID of the Network ACL's VPC.
    """

    is_ipv6: bool
    """
    Defines whether this set of ACL rules is for IPv6 (false = IPv4). Each Network ACL can have rules for only one IP type.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetAclResponse:
    rules: list[AclRule]
    default_policy: Action


@dataclass
class GetPrivateNetworkRequest:
    private_network_id: str
    """
    Private Network ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetRouteRequest:
    route_id: str
    """
    Route ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetVPCRequest:
    vpc_id: str
    """
    VPC ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListPrivateNetworksRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListPrivateNetworksRequestOrderBy] = (
        ListPrivateNetworksRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order of the returned Private Networks.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of Private Networks to return per page.
    """

    name: Optional[str] = None
    """
    Name to filter for. Only Private Networks with names containing this string will be returned.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to filter for. Only Private Networks with one or more matching tags will be returned.
    """

    organization_id: Optional[str] = None
    """
    Organization ID to filter for. Only Private Networks belonging to this Organization will be returned.
    """

    project_id: Optional[str] = None
    """
    Project ID to filter for. Only Private Networks belonging to this Project will be returned.
    """

    private_network_ids: Optional[list[str]] = field(default_factory=list)
    """
    Private Network IDs to filter for. Only Private Networks with one of these IDs will be returned.
    """

    vpc_id: Optional[str] = None
    """
    VPC ID to filter for. Only Private Networks belonging to this VPC will be returned.
    """

    dhcp_enabled: Optional[bool] = False
    """
    DHCP status to filter for. When true, only Private Networks with managed DHCP enabled will be returned.
    """


@dataclass
class ListPrivateNetworksResponse:
    private_networks: list[PrivateNetwork]
    total_count: int


@dataclass
class ListSubnetsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListSubnetsRequestOrderBy] = (
        ListSubnetsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order of the returned subnets.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of Private Networks to return per page.
    """

    organization_id: Optional[str] = None
    """
    Organization ID to filter for. Only subnets belonging to this Organization will be returned.
    """

    project_id: Optional[str] = None
    """
    Project ID to filter for. Only subnets belonging to this Project will be returned.
    """

    subnet_ids: Optional[list[str]] = field(default_factory=list)
    """
    Subnet IDs to filter for. Only subnets matching the specified IDs will be returned.
    """

    vpc_id: Optional[str] = None
    """
    VPC ID to filter for. Only subnets belonging to this VPC will be returned.
    """


@dataclass
class ListSubnetsResponse:
    subnets: list[Subnet]
    total_count: int


@dataclass
class ListVPCsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListVPCsRequestOrderBy] = ListVPCsRequestOrderBy.CREATED_AT_ASC
    """
    Sort order of the returned VPCs.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of VPCs to return per page.
    """

    name: Optional[str] = None
    """
    Name to filter for. Only VPCs with names containing this string will be returned.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to filter for. Only VPCs with one or more matching tags will be returned.
    """

    organization_id: Optional[str] = None
    """
    Organization ID to filter for. Only VPCs belonging to this Organization will be returned.
    """

    project_id: Optional[str] = None
    """
    Project ID to filter for. Only VPCs belonging to this Project will be returned.
    """

    is_default: Optional[bool] = False
    """
    Defines whether to filter only for VPCs which are the default one for their Project.
    """

    routing_enabled: Optional[bool] = False
    """
    Defines whether to filter only for VPCs which route traffic between their Private Networks.
    """


@dataclass
class ListVPCsResponse:
    vpcs: list[VPC]
    total_count: int


@dataclass
class SetAclRequest:
    vpc_id: str
    """
    ID of the Network ACL's VPC.
    """

    rules: list[AclRule]
    """
    List of Network ACL rules.
    """

    is_ipv6: bool
    """
    Defines whether this set of ACL rules is for IPv6 (false = IPv4). Each Network ACL can have rules for only one IP type.
    """

    default_policy: Action
    """
    Action to take for packets which do not match any rules.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class SetAclResponse:
    rules: list[AclRule]
    default_policy: Action


@dataclass
class UpdatePrivateNetworkRequest:
    private_network_id: str
    """
    Private Network ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name for the Private Network.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags for the Private Network.
    """

    default_route_propagation_enabled: Optional[bool] = False
    """
    Defines whether default v4 and v6 routes are propagated for this Private Network.
    """


@dataclass
class UpdateRouteRequest:
    route_id: str
    """
    Route ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    description: Optional[str] = None
    """
    Route description.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the Route.
    """

    destination: Optional[str] = None
    """
    Destination of the Route.
    """

    nexthop_resource_id: Optional[str] = None
    """
    ID of the nexthop resource.
    """

    nexthop_private_network_id: Optional[str] = None
    """
    ID of the nexthop private network.
    """

    nexthop_vpc_connector_id: Optional[str] = None
    """
    ID of the nexthop VPC connector.
    """


@dataclass
class UpdateVPCRequest:
    vpc_id: str
    """
    VPC ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name for the VPC.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags for the VPC.
    """
