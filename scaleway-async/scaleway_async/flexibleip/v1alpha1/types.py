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


class FlexibleIPStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    UPDATING = "updating"
    ATTACHED = "attached"
    ERROR = "error"
    DETACHING = "detaching"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class ListFlexibleIPsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class MACAddressStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    UPDATING = "updating"
    USED = "used"
    ERROR = "error"
    DELETING = "deleting"

    def __str__(self) -> str:
        return str(self.value)


class MACAddressType(str, Enum):
    UNKNOWN_TYPE = "unknown_type"
    VMWARE = "vmware"
    XEN = "xen"
    KVM = "kvm"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class AttachFlexibleIPsResponse:
    """
    Attach flexible i ps response.
    """

    total_count: int
    """
    Total count of flexible IPs that are being updated.
    """

    flexible_ips: List[FlexibleIP]
    """
    List of flexible IPs in an updating state.
    """


@dataclass
class DetachFlexibleIPsResponse:
    """
    Detach flexible i ps response.
    """

    total_count: int
    """
    Total count of flexible IPs that are being detached.
    """

    flexible_ips: List[FlexibleIP]
    """
    List of flexible IPs in a detaching state.
    """


@dataclass
class FlexibleIP:
    """
    Flexible ip.
    """

    id: str
    """
    ID of the flexible IP.
    """

    organization_id: str
    """
    ID of the Organization the flexible IP is attached to.
    """

    project_id: str
    """
    ID of the Project the flexible IP is attached to.
    """

    description: str
    """
    Flexible IP description.
    """

    tags: List[str]
    """
    Flexible IP tags.
    """

    updated_at: Optional[datetime]
    """
    Date on which the flexible IP was last updated.
    """

    created_at: Optional[datetime]
    """
    Date on which the flexible IP was created.
    """

    status: FlexibleIPStatus
    """
    Flexible IP status.
    - ready : flexible IP is created and ready to be attached to a server or to be associated with a virtual MAC.
    - updating: flexible IP is being attached to a server or a virtual MAC operation is ongoing
    - attached: flexible IP is attached to a server
    - error: a flexible IP operation resulted in an error
    - detaching: flexible IP is being detached from a server
    - locked: the resource of the flexible IP is locked.
    """

    ip_address: str
    """
    IP of the flexible IP.
    """

    mac_address: Optional[MACAddress]
    """
    MAC address of the flexible IP.
    """

    server_id: Optional[str]
    """
    ID of the server linked to the flexible IP.
    """

    reverse: str
    """
    Reverse DNS value.
    """

    zone: Zone
    """
    Availability Zone of the flexible IP.
    """


@dataclass
class ListFlexibleIPsResponse:
    """
    List flexible i ps response.
    """

    total_count: int
    """
    Total count of matching flexible IPs.
    """

    flexible_ips: List[FlexibleIP]
    """
    List of all flexible IPs.
    """


@dataclass
class MACAddress:
    """
    Mac address.
    """

    id: str
    """
    ID of the flexible IP.
    """

    mac_address: str
    """
    MAC address of the Virtual MAC.
    """

    mac_type: MACAddressType
    """
    Type of virtual MAC.
    """

    status: MACAddressStatus
    """
    Status of virtual MAC.
    """

    updated_at: Optional[datetime]
    """
    Date on which the virtual MAC was last updated.
    """

    created_at: Optional[datetime]
    """
    Date on which the virtual MAC was created.
    """

    zone: Zone
    """
    MAC address IP Availability Zone.
    """


@dataclass
class CreateFlexibleIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str]
    """
    ID of the project to associate with the Flexible IP.
    """

    description: str
    """
    Flexible IP description (max. of 255 characters).
    """

    tags: Optional[List[str]]
    """
    Tags to associate to the flexible IP.
    """

    server_id: Optional[str]
    """
    ID of the server to which the newly created flexible IP will be attached.
    """

    reverse: Optional[str]
    """
    Value of the reverse DNS.
    """

    is_ipv6: bool
    """
    Defines whether the flexible IP has an IPv6 address.
    """


@dataclass
class GetFlexibleIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    fip_id: str
    """
    ID of the flexible IP.
    """


@dataclass
class ListFlexibleIPsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListFlexibleIPsRequestOrderBy]
    """
    Sort order of the returned flexible IPs.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Maximum number of flexible IPs per page.
    """

    tags: Optional[List[str]]
    """
    Filter by tag, only flexible IPs with one or more matching tags will be returned.
    """

    status: Optional[List[FlexibleIPStatus]]
    """
    Filter by status, only flexible IPs with this status will be returned.
    """

    server_ids: Optional[List[str]]
    """
    Filter by server IDs, only flexible IPs with these server IDs will be returned.
    """

    organization_id: Optional[str]
    """
    Filter by Organization ID, only flexible IPs from this Organization will be returned.
    """

    project_id: Optional[str]
    """
    Filter by Project ID, only flexible IPs from this Project will be returned.
    """


@dataclass
class UpdateFlexibleIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    fip_id: str
    """
    ID of the flexible IP to update.
    """

    description: Optional[str]
    """
    Flexible IP description (max. 255 characters).
    """

    tags: Optional[List[str]]
    """
    Tags associated with the flexible IP.
    """

    reverse: Optional[str]
    """
    Value of the reverse DNS.
    """


@dataclass
class DeleteFlexibleIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    fip_id: str
    """
    ID of the flexible IP to delete.
    """


@dataclass
class AttachFlexibleIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    fips_ids: List[str]
    """
    List of flexible IP IDs to attach to a server.
    Multiple IDs can be provided, but note that flexible IPs must belong to the same MAC group (see details about MAC groups).
    """

    server_id: str
    """
    ID of the server on which to attach the flexible IPs.
    """


@dataclass
class DetachFlexibleIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    fips_ids: List[str]
    """
    List of flexible IP IDs to detach from a server. Multiple IDs can be provided. Note that flexible IPs must belong to the same MAC group.
    """


@dataclass
class GenerateMACAddrRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    fip_id: str
    """
    ID of the flexible IP for which to generate a virtual MAC.
    """

    mac_type: Optional[MACAddressType]
    """
    TODO.
    """


@dataclass
class DuplicateMACAddrRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    fip_id: str
    """
    ID of the flexible IP on which to duplicate the virtual MAC.
    Note that the flexible IPs need to be attached to the same server.
    """

    duplicate_from_fip_id: str
    """
    ID of the flexible IP to duplicate the Virtual MAC from.
    Note that flexible IPs need to be attached to the same server.
    """


@dataclass
class MoveMACAddrRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    fip_id: str

    dst_fip_id: str


@dataclass
class DeleteMACAddrRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    fip_id: str
    """
    ID of the flexible IP from which to delete the virtual MAC.
    If the flexible IP belongs to a MAC group, the MAC will be removed from both the MAC group and flexible IP.
    """
