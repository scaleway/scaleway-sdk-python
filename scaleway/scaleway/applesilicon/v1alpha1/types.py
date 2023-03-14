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


class ListServersRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ServerStatus(str, Enum):
    UNKNOWN_STATUS = "unknown_status"
    STARTING = "starting"
    READY = "ready"
    ERROR = "error"
    REBOOTING = "rebooting"
    UPDATING = "updating"
    LOCKING = "locking"
    LOCKED = "locked"
    UNLOCKING = "unlocking"
    REINSTALLING = "reinstalling"

    def __str__(self) -> str:
        return str(self.value)


class ServerTypeStock(str, Enum):
    UNKNOWN_STOCK = "unknown_stock"
    NO_STOCK = "no_stock"
    LOW_STOCK = "low_stock"
    HIGH_STOCK = "high_stock"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class ListOSResponse:
    """
    List os response.
    """

    total_count: int
    """
    Total number of OS.
    """

    os: List[OS]
    """
    List of OS.
    """


@dataclass
class ListServerTypesResponse:
    """
    List server types response.
    """

    server_types: List[ServerType]
    """
    Available server types.
    """


@dataclass
class ListServersResponse:
    """
    List servers response.
    """

    total_count: int
    """
    Total number of servers.
    """

    servers: List[Server]
    """
    Paginated returned servers.
    """


@dataclass
class OS:
    """
    Os.
    """

    id: str
    """
    Unique ID of the OS.
    """

    name: str
    """
    OS name.
    """

    label: str
    """
    OS name as it should be displayed.
    """

    image_url: str
    """
    URL of the image.
    """

    compatible_server_types: List[str]
    """
    List of compatible server types.
    """


@dataclass
class Server:
    """
    Server.
    """

    id: str
    """
    UUID of the server.
    """

    type_: str
    """
    Type of the server.
    """

    name: str
    """
    Name of the server.
    """

    project_id: str
    """
    Project this server is associated with.
    """

    organization_id: str
    """
    Organization this server is associated with.
    """

    ip: str
    """
    IPv4 address of the server.
    """

    vnc_url: str
    """
    URL of the VNC.
    """

    status: ServerStatus
    """
    Current status of the server.
    """

    created_at: Optional[datetime]
    """
    Date on which the server was created.
    """

    updated_at: Optional[datetime]
    """
    Date on which the server was last updated.
    """

    deletable_at: Optional[datetime]
    """
    Date on which the server was last deleted.
    """

    zone: Zone
    """
    Zone of the server.
    """


@dataclass
class ServerType:
    """
    Server type.
    """

    cpu: Optional[ServerTypeCPU]
    """
    CPU description.
    """

    disk: Optional[ServerTypeDisk]
    """
    Size of the local disk of the server.
    """

    name: str
    """
    Name of the type.
    """

    memory: Optional[ServerTypeMemory]
    """
    Size of memory available.
    """

    stock: ServerTypeStock
    """
    Current stock.
    """

    minimum_lease_duration: Optional[str]
    """
    Minimum duration of the lease in seconds.
    Minimum duration of the lease in seconds (example. 3.4s).
    """


@dataclass
class ServerTypeCPU:
    name: str

    core_count: int


@dataclass
class ServerTypeDisk:
    capacity: int

    type_: str


@dataclass
class ServerTypeMemory:
    capacity: int

    type_: str


@dataclass
class ListServerTypesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerTypeRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_type: str
    """
    Server type identifier.
    """


@dataclass
class CreateServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Create a server with this given name.
    """

    project_id: Optional[str]
    """
    Create a server in the given project ID.
    """

    type_: str
    """
    Create a server of the given type.
    """


@dataclass
class ListServersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListServersRequestOrderBy]
    """
    Sort order of the returned servers.
    """

    project_id: Optional[str]
    """
    Only list servers of this project ID.
    """

    organization_id: Optional[str]
    """
    Only list servers of this Organization ID.
    """

    page: Optional[int]
    """
    Positive integer to choose the page to return.
    """

    page_size: Optional[int]
    """
    Positive integer lower or equal to 100 to select the number of items to return.
    """


@dataclass
class ListOSRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int]
    """
    Positive integer to choose the page to return.
    """

    page_size: Optional[int]
    """
    Positive integer lower or equal to 100 to select the number of items to return.
    """

    server_type: Optional[str]
    """
    List of compatible server types.
    """

    name: Optional[str]
    """
    Filter OS by name (note that "11.1" will return "11.1.2" and "11.1" but not "12")).
    """


@dataclass
class GetOSRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    os_id: str
    """
    UUID of the OS you want to get.
    """


@dataclass
class GetServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_id: str
    """
    UUID of the server you want to get.
    """


@dataclass
class UpdateServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_id: str
    """
    UUID of the server you want to update.
    """

    name: str
    """
    Updated name for your server.
    """


@dataclass
class DeleteServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_id: str
    """
    UUID of the server you want to delete.
    """


@dataclass
class RebootServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_id: str
    """
    UUID of the server you want to reboot.
    """


@dataclass
class ReinstallServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_id: str
    """
    UUID of the server you want to reinstall.
    """
