# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional

from scaleway_core.utils import (
    StrEnumMeta,
)


class ManageServerPowerRequestAction(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ACTION = "unknown_action"
    POWER_OFF = "power_off"
    POWER_ON = "power_on"
    REBOOT = "reboot"

    def __str__(self) -> str:
        return str(self.value)


class ServerStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    ORDERED = "ordered"
    INSTALLING = "installing"
    ACTIVE = "active"
    STOPPED = "stopped"
    LOCKED = "locked"
    SUSPENDED = "suspended"
    STOPPING = "stopping"
    STARTING = "starting"
    DELETING = "deleting"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class HardwareSpecs:
    core_count: int
    """
    Number of cores.
    """

    storage_bytes: int
    """
    Storage size.
    """

    ram_bytes: int
    """
    RAM size.
    """


@dataclass
class NetworkSpecs:
    bandwidth_max: int
    """
    Network bandwidth (GB).
    """

    bandwidth_speed_gbps: int
    """
    Bandwidth speed.
    """


@dataclass
class Location:
    id: str
    """
    ID.
    """

    geographic_area: str
    """
    Geographic area.
    """

    country_code: str
    """
    Country code.
    """

    city_name: str
    """
    City name.
    """

    available_offer_ids: list[str]
    """
    Available offer IDs.
    """

    srn: str
    """
    SRN of the location.
    """


@dataclass
class OS:
    id: str
    """
    ID.
    """

    name: str
    """
    Name.
    """

    main_os: str
    """
    OS family.
    """

    srn: str
    """
    SRN of the OS.
    """

    description: Optional[str] = None
    """
    Description.
    """


@dataclass
class Offer:
    id: str
    """
    ID of the offer.
    """

    name: str
    """
    Name of the offer.
    """

    available: bool
    """
    Whether the offer is available.
    """

    srn: str
    """
    SRN of the offer.
    """

    hardware_specs: Optional[HardwareSpecs] = None
    """
    Hardware specifications.
    """

    network_specs: Optional[NetworkSpecs] = None
    """
    Network specifications.
    """


@dataclass
class Server:
    id: str
    """
    ID of the server.
    """

    hostname: str
    """
    Hostname of the server.
    """

    os_id: str
    """
    OS ID installed on server.
    """

    location_id: str
    """
    Location ID of the server.
    """

    status: ServerStatus
    """
    Status of the server.
    """

    ips: list[str]
    """
    List of IPs of the server.
    """

    organization_id: str
    """
    Organization ID owning the server.
    """

    project_id: str
    """
    Project ID of the server.
    """

    offer_id: str
    """
    Offer ID of the server.
    """

    srn: str
    """
    SRN of the server.
    """


@dataclass
class ListLocationsResponse:
    total_count: int
    """
    Total count.
    """

    locations: list[Location]
    """
    List of locations available for the given offer.
    """


@dataclass
class ListOSResponse:
    total_count: int
    """
    Total count.
    """

    os: list[OS]
    """
    List of OS.
    """


@dataclass
class ListOffersResponse:
    total_count: int
    """
    Total count of matching offers.
    """

    offers: list[Offer]
    """
    List of offers.
    """


@dataclass
class ListServersResponse:
    total_count: int
    """
    Total count of matching servers.
    """

    servers: list[Server]
    """
    Servers that match filters.
    """


@dataclass
class VpsApiChangeServerHostnameRequest:
    server_id: str
    """
    ID of the server.
    """

    hostname: str
    """
    New hostname of the server.
    """


@dataclass
class VpsApiChangeServerPasswordRequest:
    server_id: str
    """
    ID of the server.
    """

    password: str
    """
    New root password of the server.
    """


@dataclass
class VpsApiCreateServerRequest:
    offer_id: str
    """
    Offer ID of the server.
    """

    os_id: str
    """
    OS ID to install on the server.
    """

    location_id: str
    """
    Location ID of the server.
    """

    hostname: str
    """
    Hostname of the server.
    """

    project_id: Optional[str] = None
    """
    Project ID.
    """

    ssh_key_id: Optional[str] = None
    """
    SSH key to install on the server.
    """


@dataclass
class VpsApiDeleteServerRequest:
    server_id: str
    """
    ID of the server to delete.
    """


@dataclass
class VpsApiGetOfferRequest:
    offer_id: str
    """
    ID of the offer.
    """


@dataclass
class VpsApiGetServerRequest:
    server_id: str
    """
    ID of the server.
    """


@dataclass
class VpsApiListLocationsRequest:
    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Number of locations per page.
    """


@dataclass
class VpsApiListOSRequest:
    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Number of OS per page.
    """


@dataclass
class VpsApiListOffersRequest:
    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Number of offers per page.
    """


@dataclass
class VpsApiListServersRequest:
    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Number of servers per page.
    """

    organization_id: Optional[str] = None

    project_id: Optional[str] = None


@dataclass
class VpsApiManageServerPowerRequest:
    server_id: str
    """
    ID of the server.
    """

    action: ManageServerPowerRequestAction
    """
    Action to perform (power_off, power_on, reboot).
    """


@dataclass
class VpsApiReinstallServerRequest:
    server_id: str
    """
    ID of the server.
    """

    os_id: str
    """
    OS ID to reinstall on the server.
    """

    ssh_key_id: Optional[str] = None
    """
    SSH key to install on the server.
    """
