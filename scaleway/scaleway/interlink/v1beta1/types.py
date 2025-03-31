# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class BgpStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_BGP_STATUS = "unknown_bgp_status"
    UP = "up"
    DOWN = "down"

    def __str__(self) -> str:
        return str(self.value)


class DedicatedConnectionStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    CREATED = "created"
    CONFIGURING = "configuring"
    FAILED = "failed"
    ACTIVE = "active"
    DISABLED = "disabled"
    DELETED = "deleted"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class LinkKind(str, Enum, metaclass=StrEnumMeta):
    HOSTED = "hosted"
    SELF_HOSTED = "self_hosted"

    def __str__(self) -> str:
        return str(self.value)


class LinkStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_LINK_STATUS = "unknown_link_status"
    CONFIGURING = "configuring"
    FAILED = "failed"
    REQUESTED = "requested"
    REFUSED = "refused"
    EXPIRED = "expired"
    PROVISIONING = "provisioning"
    ACTIVE = "active"
    LIMITED_CONNECTIVITY = "limited_connectivity"
    ALL_DOWN = "all_down"
    DEPROVISIONING = "deprovisioning"
    DELETED = "deleted"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class ListDedicatedConnectionsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListLinksRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPartnersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPopsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
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


@dataclass
class BgpConfig:
    asn: int
    """
    AS Number of the BGP peer.
    """

    ipv4: str
    """
    IPv4 address of the BGP peer.
    """

    ipv6: str
    """
    IPv6 address of the BGP peer.
    """


@dataclass
class PartnerHost:
    partner_id: str
    """
    ID of the partner facilitating the link.
    """

    pairing_key: str
    """
    Used to identify a link from a user or partner's point of view.
    """

    disapproved_reason: Optional[str]
    """
    Reason given by partner to explain why they did not approve the request for a hosted link.
    """


@dataclass
class SelfHost:
    connection_id: str
    """
    Dedicated physical connection supporting the link.
    """


@dataclass
class DedicatedConnection:
    id: str
    """
    Unique identifier of the dedicated connection.
    """

    project_id: str
    """
    Project ID.
    """

    organization_id: str
    """
    Organization ID.
    """

    status: DedicatedConnectionStatus
    """
    Status of the dedicated connection.
    """

    name: str
    """
    Name of the dedicated connection.
    """

    tags: List[str]
    """
    List of tags associated with the dedicated connection.
    """

    pop_id: str
    """
    ID of the PoP where the dedicated connection is located.
    """

    bandwidth_mbps: int
    """
    Bandwidth size of the dedicated connection.
    """

    available_link_bandwidths: List[int]
    """
    Size of the links supported on this dedicated connection.
    """

    region: ScwRegion
    """
    Region of the dedicated connection.
    """

    created_at: Optional[datetime]
    """
    Creation date of the dedicated connection.
    """

    updated_at: Optional[datetime]
    """
    Last modification date of the dedicated connection.
    """

    demarcation_info: Optional[str]
    """
    Demarcation details required by the data center to set up the supporting Cross Connect. This generally includes the physical space in the facility, the cabinet or rack the connection should land in, the patch panel to go in, the port designation, and the media type.
    """


@dataclass
class Link:
    id: str
    """
    Unique identifier of the link.
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
    Name of the link.
    """

    tags: List[str]
    """
    List of tags associated with the link.
    """

    pop_id: str
    """
    ID of the PoP where the link's corresponding connection is located.
    """

    bandwidth_mbps: int
    """
    Rate limited bandwidth of the link.
    """

    status: LinkStatus
    """
    Status of the link.
    """

    bgp_v4_status: BgpStatus
    """
    Status of the link's BGP IPv4 session.
    """

    bgp_v6_status: BgpStatus
    """
    Status of the link's BGP IPv6 session.
    """

    enable_route_propagation: bool
    """
    Defines whether route propagation is enabled or not. To enable or disable route propagation, use the dedicated endpoint.
    """

    vlan: int
    """
    VLAN of the link.
    """

    region: ScwRegion
    """
    Region of the link.
    """

    vpc_id: Optional[str]
    """
    ID of the Scaleway VPC attached to the link.
    """

    routing_policy_id: Optional[str]
    """
    ID of the routing policy attached to the link.
    """

    created_at: Optional[datetime]
    """
    Creation date of the link.
    """

    updated_at: Optional[datetime]
    """
    Last modification date of the link.
    """

    scw_bgp_config: Optional[BgpConfig]
    """
    BGP configuration on Scaleway's side.
    """

    peer_bgp_config: Optional[BgpConfig]
    """
    BGP configuration on peer's side (on-premises or other hosting provider).
    """

    partner: Optional[PartnerHost]

    self_: Optional[SelfHost]


@dataclass
class Partner:
    id: str
    """
    Unique identifier of the partner.
    """

    name: str
    """
    Name of the partner.
    """

    contact_email: str
    """
    Contact email address of partner.
    """

    logo_url: str
    """
    Image URL of the partner's logo.
    """

    portal_url: str
    """
    URL of the partner's portal.
    """

    created_at: Optional[datetime]
    """
    Creation date of the partner.
    """

    updated_at: Optional[datetime]
    """
    Last modification date of the partner.
    """


@dataclass
class Pop:
    id: str
    """
    Unique identifier of the PoP.
    """

    name: str
    """
    Name of the PoP. It is the common reference of Hosting DC (ex: TH2).
    """

    hosting_provider_name: str
    """
    Name of the PoP's hosting provider, e.g. Telehouse for TH2 or OpCore for DC3.
    """

    address: str
    """
    Physical address of the PoP.
    """

    city: str
    """
    City where PoP is located.
    """

    logo_url: str
    """
    Image URL of the PoP's logo.
    """

    available_link_bandwidths_mbps: List[int]
    """
    Available bandwidth in Mbits/s for future hosted links from available connections in this PoP.
    """

    region: ScwRegion
    """
    Region of the PoP.
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

    tags: List[str]
    """
    List of tags associated with the routing policy.
    """

    prefix_filter_in: List[str]
    """
    IP prefixes to accept from the peer (ranges of route announcements to accept).
    """

    prefix_filter_out: List[str]
    """
    IP prefix filters to advertise to the peer (ranges of routes to advertise).
    """

    region: ScwRegion
    """
    Region of the routing policy.
    """

    created_at: Optional[datetime]
    """
    Creation date of the routing policy.
    """

    updated_at: Optional[datetime]
    """
    Last modification date of the routing policy.
    """


@dataclass
class AttachRoutingPolicyRequest:
    link_id: str
    """
    ID of the link to attach a routing policy to.
    """

    routing_policy_id: str
    """
    ID of the routing policy to be attached.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class AttachVpcRequest:
    link_id: str
    """
    ID of the link to attach VPC to.
    """

    vpc_id: str
    """
    ID of the VPC to attach.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class CreateLinkRequest:
    name: str
    """
    Name of the link.
    """

    pop_id: str
    """
    PoP (location) where the link will be created.
    """

    bandwidth_mbps: int
    """
    Desired bandwidth for the link. Must be compatible with available link bandwidths and remaining bandwidth capacity of the connection.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project to create the link in.
    """

    tags: Optional[List[str]]
    """
    List of tags to apply to the link.
    """

    connection_id: Optional[str]

    partner_id: Optional[str]


@dataclass
class CreateRoutingPolicyRequest:
    name: str
    """
    Name of the routing policy.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project to create the routing policy in.
    """

    tags: Optional[List[str]]
    """
    List of tags to apply to the routing policy.
    """

    prefix_filter_in: Optional[List[str]]
    """
    IP prefixes to accept from the peer (ranges of route announcements to accept).
    """

    prefix_filter_out: Optional[List[str]]
    """
    IP prefix filters to advertise to the peer (ranges of routes to advertise).
    """


@dataclass
class DeleteLinkRequest:
    link_id: str
    """
    ID of the link to delete.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteRoutingPolicyRequest:
    routing_policy_id: str
    """
    ID of the routing policy to delete.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DetachRoutingPolicyRequest:
    link_id: str
    """
    ID of the link to detach a routing policy from.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DetachVpcRequest:
    link_id: str
    """
    ID of the link to detach the VPC from.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DisableRoutePropagationRequest:
    link_id: str
    """
    ID of the link on which to disable route propagation.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class EnableRoutePropagationRequest:
    link_id: str
    """
    ID of the link on which to enable route propagation.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetDedicatedConnectionRequest:
    connection_id: str
    """
    ID of connection to get.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetLinkRequest:
    link_id: str
    """
    ID of the link to get.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetPartnerRequest:
    partner_id: str
    """
    ID of partner to get.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetPopRequest:
    pop_id: str
    """
    ID of PoP to get.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetRoutingPolicyRequest:
    routing_policy_id: str
    """
    ID of the routing policy to get.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListDedicatedConnectionsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListDedicatedConnectionsRequestOrderBy]
    """
    Order in which to return results.
    """

    page: Optional[int]
    """
    Page number to return.
    """

    page_size: Optional[int]
    """
    Maximum number of connections to return per page.
    """

    project_id: Optional[str]
    """
    Project ID to filter for.
    """

    organization_id: Optional[str]
    """
    Organization ID to filter for.
    """

    name: Optional[str]
    """
    Link name to filter for.
    """

    tags: Optional[List[str]]
    """
    Tags to filter for.
    """

    status: Optional[DedicatedConnectionStatus]
    """
    Connection status to filter for.
    """

    bandwidth_mbps: Optional[int]
    """
    Filter for dedicated connections with this bandwidth size.
    """

    pop_id: Optional[str]
    """
    Filter for dedicated connections present in this PoP.
    """


@dataclass
class ListDedicatedConnectionsResponse:
    connections: List[DedicatedConnection]
    """
    List of connections on current page.
    """

    total_count: int
    """
    Total number of connections returned.
    """


@dataclass
class ListLinksRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListLinksRequestOrderBy]
    """
    Order in which to return results.
    """

    page: Optional[int]
    """
    Page number to return.
    """

    page_size: Optional[int]
    """
    Maximum number of links to return per page.
    """

    project_id: Optional[str]
    """
    Project ID to filter for.
    """

    organization_id: Optional[str]
    """
    Organization ID to filter for.
    """

    name: Optional[str]
    """
    Link name to filter for.
    """

    tags: Optional[List[str]]
    """
    Tags to filter for.
    """

    status: Optional[LinkStatus]
    """
    Link status to filter for.
    """

    bgp_v4_status: Optional[BgpStatus]
    """
    BGP IPv4 status to filter for.
    """

    bgp_v6_status: Optional[BgpStatus]
    """
    BGP IPv6 status to filter for.
    """

    pop_id: Optional[str]
    """
    Filter for links attached to this PoP (via connections).
    """

    bandwidth_mbps: Optional[int]
    """
    Filter for link bandwidth (in Mbps).
    """

    partner_id: Optional[str]
    """
    Filter for links hosted by this partner.
    """

    vpc_id: Optional[str]
    """
    Filter for links attached to this VPC.
    """

    routing_policy_id: Optional[str]
    """
    Filter for links using this routing policy.
    """

    pairing_key: Optional[str]
    """
    Filter for the link with this pairing_key.
    """

    kind: Optional[LinkKind]
    """
    Filter for hosted or self-hosted links.
    """

    connection_id: Optional[str]
    """
    Filter for links self-hosted on this connection.
    """


@dataclass
class ListLinksResponse:
    links: List[Link]
    """
    List of links on the current page.
    """

    total_count: int
    """
    Total number of links.
    """


@dataclass
class ListPartnersRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListPartnersRequestOrderBy]
    """
    Order in which to return results.
    """

    page: Optional[int]
    """
    Page number to return.
    """

    page_size: Optional[int]
    """
    Maximum number of partners to return per page.
    """

    pop_ids: Optional[List[str]]
    """
    Filter for partners present (offering a connection) in one of these PoPs.
    """


@dataclass
class ListPartnersResponse:
    partners: List[Partner]
    """
    List of partners on current page.
    """

    total_count: int
    """
    Total number of partners returned.
    """


@dataclass
class ListPopsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListPopsRequestOrderBy]
    """
    Order in which to return results.
    """

    page: Optional[int]
    """
    Page number to return.
    """

    page_size: Optional[int]
    """
    Maximum number of PoPs to return per page.
    """

    name: Optional[str]
    """
    PoP name to filter for.
    """

    hosting_provider_name: Optional[str]
    """
    Hosting provider name to filter for.
    """

    partner_id: Optional[str]
    """
    Filter for PoPs hosting an available shared connection from this partner.
    """

    link_bandwidth_mbps: Optional[int]
    """
    Filter for PoPs with a shared connection allowing this bandwidth size. Note that we cannot guarantee that PoPs returned will have available capacity.
    """

    dedicated_available: Optional[bool]
    """
    Filter for PoPs with a dedicated connection available for self-hosted links.
    """


@dataclass
class ListPopsResponse:
    pops: List[Pop]
    """
    List of PoPs on the current page.
    """

    total_count: int
    """
    Total number of PoPs.
    """


@dataclass
class ListRoutingPoliciesRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListRoutingPoliciesRequestOrderBy]
    """
    Order in which to return results.
    """

    page: Optional[int]
    """
    Page number to return.
    """

    page_size: Optional[int]
    """
    Maximum number of routing policies to return per page.
    """

    project_id: Optional[str]
    """
    Project ID to filter for.
    """

    organization_id: Optional[str]
    """
    Organization ID to filter for.
    """

    name: Optional[str]
    """
    Routing policy name to filter for.
    """

    tags: Optional[List[str]]
    """
    Tags to filter for.
    """


@dataclass
class ListRoutingPoliciesResponse:
    routing_policies: List[RoutingPolicy]

    total_count: int


@dataclass
class UpdateLinkRequest:
    link_id: str
    """
    ID of the link to update.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the link.
    """

    tags: Optional[List[str]]
    """
    List of tags to apply to the link.
    """


@dataclass
class UpdateRoutingPolicyRequest:
    routing_policy_id: str
    """
    ID of the routing policy to update.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the routing policy.
    """

    tags: Optional[List[str]]
    """
    List of tags to apply to the routing policy.
    """

    prefix_filter_in: Optional[List[str]]
    """
    IP prefixes to accept from the peer (ranges of route announcements to accept).
    """

    prefix_filter_out: Optional[List[str]]
    """
    IP prefix filters for routes to advertise to the peer (ranges of routes to advertise).
    """
