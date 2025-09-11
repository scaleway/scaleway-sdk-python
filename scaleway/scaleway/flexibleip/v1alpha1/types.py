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

    zone: ScwZone
    """
    MAC address IP Availability Zone.
    """

    updated_at: Optional[datetime] = None
    """
    Date on which the virtual MAC was last updated.
    """

    created_at: Optional[datetime] = None
    """
    Date on which the virtual MAC was created.
    """


@dataclass
class FlexibleIP:
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

    tags: list[str]
    """
    Flexible IP tags.
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

    ip_address: str
    """
    IP of the flexible IP.
    """

    reverse: str
    """
    Reverse DNS value.
    """

    zone: ScwZone
    """
    Availability Zone of the flexible IP.
    """

    updated_at: Optional[datetime] = None
    """
    Date on which the flexible IP was last updated.
    """

    created_at: Optional[datetime] = None
    """
    Date on which the flexible IP was created.
    """

    mac_address: Optional[MACAddress] = None
    """
    MAC address of the flexible IP.
    """

    server_id: Optional[str] = None
    """
    ID of the server linked to the flexible IP.
    """


@dataclass
class AttachFlexibleIPRequest:
    fips_ids: list[str]
    """
    Multiple IDs can be provided, but note that flexible IPs must belong to the same MAC group (see details about MAC groups).
    """

    server_id: str
    """
    ID of the server on which to attach the flexible IPs.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class AttachFlexibleIPsResponse:
    total_count: int
    """
    Total count of flexible IPs that are being updated.
    """

    flexible_ips: list[FlexibleIP]
    """
    List of flexible IPs in an updating state.
    """


@dataclass
class CreateFlexibleIPRequest:
    description: str
    """
    Flexible IP description (max. of 255 characters).
    """

    is_ipv6: bool
    """
    Defines whether the flexible IP has an IPv6 address.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the project to associate with the Flexible IP.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to associate to the flexible IP.
    """

    server_id: Optional[str] = None
    """
    ID of the server to which the newly created flexible IP will be attached.
    """

    reverse: Optional[str] = None
    """
    Value of the reverse DNS.
    """


@dataclass
class DeleteFlexibleIPRequest:
    fip_id: str
    """
    ID of the flexible IP to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteMACAddrRequest:
    fip_id: str
    """
    If the flexible IP belongs to a MAC group, the MAC will be removed from both the MAC group and flexible IP.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DetachFlexibleIPRequest:
    fips_ids: list[str]
    """
    List of flexible IP IDs to detach from a server. Multiple IDs can be provided. Note that flexible IPs must belong to the same MAC group.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DetachFlexibleIPsResponse:
    total_count: int
    """
    Total count of flexible IPs that are being detached.
    """

    flexible_ips: list[FlexibleIP]
    """
    List of flexible IPs in a detaching state.
    """


@dataclass
class DuplicateMACAddrRequest:
    fip_id: str
    """
    Note that the flexible IPs need to be attached to the same server.
    """

    duplicate_from_fip_id: str
    """
    Note that flexible IPs need to be attached to the same server.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GenerateMACAddrRequest:
    fip_id: str
    """
    ID of the flexible IP for which to generate a virtual MAC.
    """

    mac_type: MACAddressType
    """
    TODO.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetFlexibleIPRequest:
    fip_id: str
    """
    ID of the flexible IP.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListFlexibleIPsRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListFlexibleIPsRequestOrderBy] = (
        ListFlexibleIPsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order of the returned flexible IPs.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of flexible IPs per page.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Filter by tag, only flexible IPs with one or more matching tags will be returned.
    """

    status: Optional[list[FlexibleIPStatus]] = field(default_factory=list)
    """
    Filter by status, only flexible IPs with this status will be returned.
    """

    server_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter by server IDs, only flexible IPs with these server IDs will be returned.
    """

    organization_id: Optional[str] = None
    """
    Filter by Organization ID, only flexible IPs from this Organization will be returned.
    """

    project_id: Optional[str] = None
    """
    Filter by Project ID, only flexible IPs from this Project will be returned.
    """


@dataclass
class ListFlexibleIPsResponse:
    total_count: int
    """
    Total count of matching flexible IPs.
    """

    flexible_ips: list[FlexibleIP]
    """
    List of all flexible IPs.
    """


@dataclass
class MoveMACAddrRequest:
    fip_id: str
    dst_fip_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class UpdateFlexibleIPRequest:
    fip_id: str
    """
    ID of the flexible IP to update.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    description: Optional[str] = None
    """
    Flexible IP description (max. 255 characters).
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags associated with the flexible IP.
    """

    reverse: Optional[str] = None
    """
    Value of the reverse DNS.
    """
