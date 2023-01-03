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
    Attach flexible i ps response
    """

    total_count: int
    """
    Total count of Flexible IPs being updated
    """

    flexible_ips: List[FlexibleIP]
    """
    Listing of Flexible IPs in updating state
    """


@dataclass
class DetachFlexibleIPsResponse:
    """
    Detach flexible i ps response
    """

    total_count: int
    """
    Total count of Flexible IPs being detached
    """

    flexible_ips: List[FlexibleIP]
    """
    Listing of Flexible IPs in detaching state
    """


@dataclass
class FlexibleIP:
    """
    Flexible ip
    """

    id: str
    """
    ID of the Flexible IP
    """

    organization_id: str
    """
    Organization ID the Flexible IP is attached to
    """

    project_id: str
    """
    Project ID the Flexible IP is attached to
    """

    description: str
    """
    Description of the Flexible IP
    """

    tags: List[str]
    """
    Tags associated with the Flexible IP
    """

    updated_at: Optional[datetime]
    """
    Date of last update of the Flexible IP
    """

    created_at: Optional[datetime]
    """
    Date of creation of the Flexible IP
    """

    status: FlexibleIPStatus
    """
    - ready : Flexible IP is created and ready to be attached to a server or to have a virtual MAC generated.
    - updating: Flexible IP is being attached to a server or a virtual MAC operation is ongoing
    - attached: Flexible IP is attached to a server
    - error: a Flexible IP operation resulted in an error
    - detaching: Flexible IP is being detached from a server
    - locked: Flexible IP resource is locked
    
    """

    ip_address: str
    """
    IP of the Flexible IP
    """

    mac_address: Optional[MACAddress]
    """
    MAC address of the Flexible IP
    """

    server_id: Optional[str]
    """
    ID of the server linked to the Flexible IP
    """

    reverse: str
    """
    Reverse DNS value
    """

    zone: Zone
    """
    Flexible IP Availability Zone
    """


@dataclass
class ListFlexibleIPsResponse:
    """
    List flexible i ps response
    """

    total_count: int
    """
    Total count of matching Flexible IPs
    """

    flexible_ips: List[FlexibleIP]
    """
    Listing of Flexible IPs
    """


@dataclass
class MACAddress:
    """
    Mac address
    """

    id: str
    """
    ID of the Flexible IP
    """

    mac_address: str
    """
    MAC address of the Virtual MAC
    """

    mac_type: MACAddressType
    """
    Virtual MAC type
    """

    status: MACAddressStatus
    """
    Virtual MAC status
    """

    updated_at: Optional[datetime]
    """
    Date of last update of the Virtual MAC
    """

    created_at: Optional[datetime]
    """
    Date of creation of the Virtual MAC
    """

    zone: Zone
    """
    MAC Addr IP Availability Zone
    """


@dataclass
class CreateFlexibleIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    project_id: Optional[str]
    """
    ID of the project to associate with the Flexible IP
    """

    description: str
    """
    Description to associate with the Flexible IP, max 255 characters
    """

    tags: Optional[List[str]]
    """
    Tags to associate to the Flexible IP
    """

    server_id: Optional[str]
    """
    Server ID on which to attach the created Flexible IP
    """

    reverse: Optional[str]
    """
    Reverse DNS value
    """

    is_ipv6: bool
    """
    If true, creates a Flexible IP with an ipv6 address
    """


@dataclass
class GetFlexibleIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    fip_id: str
    """
    Flexible IP ID
    """


@dataclass
class ListFlexibleIPsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    order_by: Optional[ListFlexibleIPsRequestOrderBy]
    """
    The sort order of the returned Flexible IPs
    """

    page: Optional[int]
    """
    The page number for the returned Flexible IPs
    """

    page_size: Optional[int]
    """
    The maximum number of Flexible IPs per page
    """

    tags: Optional[List[str]]
    """
    Filter Flexible IPs with one or more matching tags
    """

    status: Optional[List[FlexibleIPStatus]]
    """
    Filter Flexible IPs by status
    """

    server_ids: Optional[List[str]]
    """
    Filter Flexible IPs by server IDs
    """

    organization_id: Optional[str]
    """
    Filter Flexible IPs by organization ID
    """

    project_id: Optional[str]
    """
    Filter Flexible IPs by project ID
    """


@dataclass
class UpdateFlexibleIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    fip_id: str
    """
    ID of the Flexible IP to update
    """

    description: Optional[str]
    """
    Description to associate with the Flexible IP, max 255 characters
    """

    tags: Optional[List[str]]
    """
    Tags to associate with the Flexible IP
    """

    reverse: Optional[str]
    """
    Reverse DNS value
    """


@dataclass
class DeleteFlexibleIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    fip_id: str
    """
    ID of the Flexible IP to delete
    """


@dataclass
class AttachFlexibleIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    fips_ids: List[str]
    """
    Multiple IDs can be provided as long as Flexible IPs belong to the same MAC groups (see details about MAC groups).
    """

    server_id: str
    """
    A server ID on which to attach the Flexible IPs
    """


@dataclass
class DetachFlexibleIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    fips_ids: List[str]
    """
    Multiple IDs can be provided as long as Flexible IPs belong to the same MAC groups (see details about MAC groups).
    """


@dataclass
class GenerateMACAddrRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    fip_id: str
    """
    Flexible IP ID on which to generate a Virtual MAC
    """

    mac_type: Optional[MACAddressType]
    """
    TODO
    """


@dataclass
class DuplicateMACAddrRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    fip_id: str
    """
    Flexible IPs need to be attached to the same server.
    """

    duplicate_from_fip_id: str
    """
    Flexible IPs need to be attached to the same server.
    """


@dataclass
class MoveMACAddrRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    fip_id: str

    dst_fip_id: str


@dataclass
class DeleteMACAddrRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    fip_id: str
    """
    If the Flexible IP belongs to a MAC group, the MAC will be removed from the MAC group and from the Flexible IP.
    """
