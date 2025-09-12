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


class ListServerPrivateNetworksRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ServerPrivateNetworkStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    ATTACHING = "attaching"
    ATTACHED = "attached"
    ERROR = "error"
    DETACHING = "detaching"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class ServerPrivateNetwork:
    id: str
    """
    UUID of the Server-to-Private Network mapping.
    """

    project_id: str
    """
    Private Network Project UUID.
    """

    server_id: str
    """
    Server UUID.
    """

    private_network_id: str
    """
    Private Network UUID.
    """

    status: ServerPrivateNetworkStatus
    """
    Configuration status of the Private Network.
    """

    ipam_ip_ids: list[str]
    """
    IPAM IP IDs of the server, if it has any.
    """

    vlan: Optional[int] = 0
    """
    VLAN UUID associated with the Private Network.
    """

    created_at: Optional[datetime] = None
    """
    Private Network creation date.
    """

    updated_at: Optional[datetime] = None
    """
    Date the Private Network was last modified.
    """


@dataclass
class ListServerPrivateNetworksResponse:
    server_private_networks: list[ServerPrivateNetwork]
    total_count: int


@dataclass
class PrivateNetworkApiAddServerPrivateNetworkRequest:
    server_id: str
    """
    UUID of the server.
    """

    private_network_id: str
    """
    UUID of the Private Network.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    ipam_ip_ids: Optional[list[str]] = field(default_factory=list)
    """
    IPAM IDs of an IPs to attach to the server.
    """


@dataclass
class PrivateNetworkApiDeleteServerPrivateNetworkRequest:
    server_id: str
    """
    UUID of the server.
    """

    private_network_id: str
    """
    UUID of the Private Network.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class PrivateNetworkApiListServerPrivateNetworksRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListServerPrivateNetworksRequestOrderBy] = (
        ListServerPrivateNetworksRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order for the returned Private Networks.
    """

    page: Optional[int] = 0
    """
    Page number for the returned Private Networks.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of Private Networks per page.
    """

    server_id: Optional[str] = None
    """
    Filter Private Networks by server UUID.
    """

    private_network_id: Optional[str] = None
    """
    Filter Private Networks by Private Network UUID.
    """

    organization_id: Optional[str] = None
    """
    Filter Private Networks by organization UUID.
    """

    project_id: Optional[str] = None
    """
    Filter Private Networks by project UUID.
    """

    ipam_ip_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter Private Networks by IPAM IP UUIDs.
    """


@dataclass
class PrivateNetworkApiSetServerPrivateNetworksRequest:
    server_id: str
    """
    UUID of the server.
    """

    per_private_network_ipam_ip_ids: dict[str, list[str]]
    """
    Object where the keys are the UUIDs of Private Networks and the values are arrays of IPAM IDs representing the IPs to assign to this Elastic Metal server on the Private Network. If the array supplied for a Private Network is empty, the next available IP from the Private Network's CIDR block will automatically be used for attachment.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetServerPrivateNetworksResponse:
    server_private_networks: list[ServerPrivateNetwork]
