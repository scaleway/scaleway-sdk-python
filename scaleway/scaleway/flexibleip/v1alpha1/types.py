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


class FlexibleIPStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    READY = "ready"
    UPDATING = "updating"
    ATTACHED = "attached"
    ERROR = "error"
    DETACHING = "detaching"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class ListFlexibleIPsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class MACAddressStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    READY = "ready"
    UPDATING = "updating"
    USED = "used"
    ERROR = "error"
    DELETING = "deleting"

    def __str__(self) -> str:
        return str(self.value)


class MACAddressType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    VMWARE = "vmware"
    XEN = "xen"
    KVM = "kvm"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class MACAddress:
    zone: Zone
    """
    MAC address IP Availability Zone.
    """

    status: MACAddressStatus
    """
    Status of virtual MAC.
    """

    mac_type: MACAddressType
    """
    Type of virtual MAC.
    """

    mac_address: str
    """
    MAC address of the Virtual MAC.
    """

    id: str
    """
    ID of the flexible IP.
    """

    updated_at: Optional[datetime]
    """
    Date on which the virtual MAC was last updated.
    """

    created_at: Optional[datetime]
    """
    Date on which the virtual MAC was created.
    """


@dataclass
class FlexibleIP:
    ip_address: str
    """
    IP of the flexible IP.
    """

    status: FlexibleIPStatus
    """
    - ready : flexible IP is created and ready to be attached to a server or to be associated with a virtual MAC.
- updating: flexible IP is being attached to a server or a virtual MAC operation is ongoing
- attached: flexible IP is attached to a server
- error: a flexible IP operation resulted in an error
- detaching: flexible IP is being detached from a server
- locked: the resource of the flexible IP is locked.
    """

    reverse: str
    """
    Reverse DNS value.
    """

    zone: Zone
    """
    Availability Zone of the flexible IP.
    """

    tags: List[str]
    """
    Flexible IP tags.
    """

    id: str
    """
    ID of the flexible IP.
    """

    project_id: str
    """
    ID of the Project the flexible IP is attached to.
    """

    organization_id: str
    """
    ID of the Organization the flexible IP is attached to.
    """

    mac_address: MACAddress
    """
    MAC address of the flexible IP.
    """

    description: str
    """
    Flexible IP description.
    """

    server_id: Optional[str]
    """
    ID of the server linked to the flexible IP.
    """

    created_at: Optional[datetime]
    """
    Date on which the flexible IP was created.
    """

    updated_at: Optional[datetime]
    """
    Date on which the flexible IP was last updated.
    """


@dataclass
class AttachFlexibleIPRequest:
    server_id: str
    """
    ID of the server on which to attach the flexible IPs.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    fips_ids: Optional[List[str]]
    """
    Multiple IDs can be provided, but note that flexible IPs must belong to the same MAC group (see details about MAC groups).
    """


@dataclass
class AttachFlexibleIPsResponse:
    flexible_ips: List[FlexibleIP]
    """
    List of flexible IPs in an updating state.
    """

    total_count: int
    """
    Total count of flexible IPs that are being updated.
    """


@dataclass
class CreateFlexibleIPRequest:
    is_ipv6: bool
    """
    Defines whether the flexible IP has an IPv6 address.
    """

    description: str
    """
    Flexible IP description (max. of 255 characters).
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str]
    """
    ID of the project to associate with the Flexible IP.
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


@dataclass
class DeleteFlexibleIPRequest:
    fip_id: str
    """
    ID of the flexible IP to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteMACAddrRequest:
    fip_id: str
    """
    If the flexible IP belongs to a MAC group, the MAC will be removed from both the MAC group and flexible IP.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DetachFlexibleIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    fips_ids: Optional[List[str]]
    """
    List of flexible IP IDs to detach from a server. Multiple IDs can be provided. Note that flexible IPs must belong to the same MAC group.
    """


@dataclass
class DetachFlexibleIPsResponse:
    flexible_ips: List[FlexibleIP]
    """
    List of flexible IPs in a detaching state.
    """

    total_count: int
    """
    Total count of flexible IPs that are being detached.
    """


@dataclass
class DuplicateMACAddrRequest:
    duplicate_from_fip_id: str
    """
    Note that flexible IPs need to be attached to the same server.
    """

    fip_id: str
    """
    Note that the flexible IPs need to be attached to the same server.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GenerateMACAddrRequest:
    fip_id: str
    """
    ID of the flexible IP for which to generate a virtual MAC.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    mac_type: Optional[MACAddressType]
    """
    TODO.
    """


@dataclass
class GetFlexibleIPRequest:
    fip_id: str
    """
    ID of the flexible IP.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
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
class ListFlexibleIPsResponse:
    flexible_ips: List[FlexibleIP]
    """
    List of all flexible IPs.
    """

    total_count: int
    """
    Total count of matching flexible IPs.
    """


@dataclass
class MoveMACAddrRequest:
    dst_fip_id: str

    fip_id: str

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class UpdateFlexibleIPRequest:
    fip_id: str
    """
    ID of the flexible IP to update.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
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
