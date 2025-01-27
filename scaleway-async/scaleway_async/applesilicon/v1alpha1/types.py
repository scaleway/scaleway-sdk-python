# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from scaleway_core.bridge import (
    Zone as ScwZone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class ConnectivityDiagnosticActionType(str, Enum, metaclass=StrEnumMeta):
    REBOOT_SERVER = "reboot_server"
    REINSTALL_SERVER = "reinstall_server"

    def __str__(self) -> str:
        return str(self.value)


class ConnectivityDiagnosticDiagnosticStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    PROCESSING = "processing"
    ERROR = "error"
    COMPLETED = "completed"

    def __str__(self) -> str:
        return str(self.value)


class ListServerPrivateNetworksRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListServersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ServerPrivateNetworkServerStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    ATTACHING = "attaching"
    ATTACHED = "attached"
    ERROR = "error"
    DETACHING = "detaching"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class ServerPrivateNetworkStatus(str, Enum, metaclass=StrEnumMeta):
    VPC_UNKNOWN_STATUS = "vpc_unknown_status"
    VPC_ENABLED = "vpc_enabled"
    VPC_UPDATING = "vpc_updating"
    VPC_DISABLED = "vpc_disabled"

    def __str__(self) -> str:
        return str(self.value)


class ServerStatus(str, Enum, metaclass=StrEnumMeta):
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
    BUSY = "busy"

    def __str__(self) -> str:
        return str(self.value)


class ServerTypeStock(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STOCK = "unknown_stock"
    NO_STOCK = "no_stock"
    LOW_STOCK = "low_stock"
    HIGH_STOCK = "high_stock"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class OS:
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

    family: str
    """
    The OS family to which this OS belongs, eg. 13 or 14.
    """

    is_beta: bool
    """
    Describes if the OS is in beta.
    """

    version: str
    """
    The OS version number, eg. Sonoma has version number 14.3.
    """

    xcode_version: str
    """
    The current xcode version for this OS.
    """

    compatible_server_types: List[str]
    """
    List of compatible server types.
    """


@dataclass
class ServerTypeCPU:
    name: str

    core_count: int

    frequency: int


@dataclass
class ServerTypeDisk:
    capacity: int

    type_: str


@dataclass
class ServerTypeGPU:
    count: int


@dataclass
class ServerTypeMemory:
    capacity: int

    type_: str


@dataclass
class ServerTypeNetwork:
    public_bandwidth_bps: int


@dataclass
class ConnectivityDiagnosticServerHealth:
    is_server_alive: bool

    is_agent_alive: bool

    is_mdm_alive: bool

    is_ssh_port_up: bool

    is_vnc_port_up: bool

    last_checkin_date: Optional[datetime]


@dataclass
class ServerPrivateNetwork:
    id: str
    """
    ID of the Server-to-Private Network mapping.
    """

    project_id: str
    """
    Private Network Project ID.
    """

    server_id: str
    """
    Apple silicon server ID.
    """

    private_network_id: str
    """
    Private Network ID.
    """

    status: ServerPrivateNetworkServerStatus
    """
    Configuration status of the Private Network.
    """

    ipam_ip_ids: List[str]
    """
    IPAM IP IDs of the server, if it has any.
    """

    vlan: Optional[int]
    """
    ID of the VLAN associated with the Private Network.
    """

    created_at: Optional[datetime]
    """
    Private Network creation date.
    """

    updated_at: Optional[datetime]
    """
    Date the Private Network was last modified.
    """


@dataclass
class ServerType:
    name: str
    """
    Name of the type.
    """

    stock: ServerTypeStock
    """
    Current stock.
    """

    cpu: Optional[ServerTypeCPU]
    """
    CPU description.
    """

    disk: Optional[ServerTypeDisk]
    """
    Size of the local disk of the server.
    """

    memory: Optional[ServerTypeMemory]
    """
    Size of memory available.
    """

    minimum_lease_duration: Optional[str]
    """
    Minimum duration of the lease in seconds (example. 3.4s).
    """

    gpu: Optional[ServerTypeGPU]
    """
    GPU description.
    """

    network: Optional[ServerTypeNetwork]
    """
    Network description.
    """

    default_os: Optional[OS]
    """
    The default OS for this server type.
    """


@dataclass
class Server:
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
    Vnc:// URL to access Apple Remote Desktop.
    """

    ssh_username: str
    """
    SSH Username for remote shell.
    """

    sudo_password: str
    """
    Admin password required to execute commands.
    """

    vnc_port: int
    """
    VNC port to use for remote desktop connection.
    """

    status: ServerStatus
    """
    Current status of the server.
    """

    deletion_scheduled: bool
    """
    Set to true to mark the server for automatic deletion depending on `deletable_at` date. Set to false to cancel an existing deletion schedule. Leave unset otherwise.
    """

    zone: ScwZone
    """
    Zone of the server.
    """

    delivered: bool
    """
    Set to true once the server has completed its provisioning steps and is ready to use. Some OS configurations might require a reinstallation of the server before delivery depending on the available stock. A reinstallation after the initial delivery will not change this flag and can be tracked using the server status.
    """

    vpc_status: ServerPrivateNetworkStatus
    """
    Activation status of optional Private Network feature support for this server.
    """

    os: Optional[OS]
    """
    Initially installed OS, this does not necessarily reflect the current OS version.
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
    Date from which the server can be deleted.
    """


@dataclass
class ConnectivityDiagnostic:
    id: str

    status: ConnectivityDiagnosticDiagnosticStatus

    is_healthy: bool

    supported_actions: List[ConnectivityDiagnosticActionType]

    error_message: str

    health_details: Optional[ConnectivityDiagnosticServerHealth]


@dataclass
class CreateServerRequest:
    type_: str
    """
    Create a server of the given type.
    """

    enable_vpc: bool
    """
    Activate the Private Network feature for this server. This feature is configured through the Apple Silicon - Private Networks API.
    """

    zone: Optional[ScwZone]
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

    os_id: Optional[str]
    """
    Create a server & install the given os_id, when no os_id provided the default OS for this server type is chosen. Requesting a non-default OS will induce an extended delivery time.
    """


@dataclass
class DeleteServerRequest:
    server_id: str
    """
    UUID of the server you want to delete.
    """

    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetConnectivityDiagnosticRequest:
    diagnostic_id: str

    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetOSRequest:
    os_id: str
    """
    UUID of the OS you want to get.
    """

    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerRequest:
    server_id: str
    """
    UUID of the server you want to get.
    """

    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerTypeRequest:
    server_type: str
    """
    Server type identifier.
    """

    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListOSRequest:
    zone: Optional[ScwZone]
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
class ListOSResponse:
    total_count: int
    """
    Total number of OS.
    """

    os: List[OS]
    """
    List of OS.
    """


@dataclass
class ListServerPrivateNetworksResponse:
    server_private_networks: List[ServerPrivateNetwork]

    total_count: int


@dataclass
class ListServerTypesRequest:
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListServerTypesResponse:
    server_types: List[ServerType]
    """
    Available server types.
    """


@dataclass
class ListServersRequest:
    zone: Optional[ScwZone]
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
class ListServersResponse:
    total_count: int
    """
    Total number of servers.
    """

    servers: List[Server]
    """
    Paginated returned servers.
    """


@dataclass
class PrivateNetworkApiAddServerPrivateNetworkRequest:
    server_id: str
    """
    ID of the server.
    """

    private_network_id: str
    """
    ID of the Private Network.
    """

    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    ipam_ip_ids: Optional[List[str]]
    """
    IPAM IDs of IPs to attach to the server.
    """


@dataclass
class PrivateNetworkApiDeleteServerPrivateNetworkRequest:
    server_id: str
    """
    ID of the server.
    """

    private_network_id: str
    """
    ID of the Private Network.
    """

    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class PrivateNetworkApiGetServerPrivateNetworkRequest:
    server_id: str

    private_network_id: str

    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class PrivateNetworkApiListServerPrivateNetworksRequest:
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListServerPrivateNetworksRequestOrderBy]
    """
    Sort order for the returned Private Networks.
    """

    page: Optional[int]
    """
    Page number for the returned Private Networks.
    """

    page_size: Optional[int]
    """
    Maximum number of Private Networks per page.
    """

    server_id: Optional[str]
    """
    Filter Private Networks by server ID.
    """

    private_network_id: Optional[str]
    """
    Filter Private Networks by Private Network ID.
    """

    organization_id: Optional[str]
    """
    Filter Private Networks by Organization ID.
    """

    project_id: Optional[str]
    """
    Filter Private Networks by Project ID.
    """

    ipam_ip_ids: Optional[List[str]]
    """
    Filter Private Networks by IPAM IP IDs.
    """


@dataclass
class PrivateNetworkApiSetServerPrivateNetworksRequest:
    server_id: str
    """
    ID of the server.
    """

    per_private_network_ipam_ip_ids: Dict[str, List[str]]
    """
    Object where the keys are the IDs of Private Networks and the values are arrays of IPAM IDs representing the IPs to assign to this Apple silicon server on the Private Network. If the array supplied for a Private Network is empty, the next available IP from the Private Network's CIDR block will automatically be used for attachment.
    """

    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class RebootServerRequest:
    server_id: str
    """
    UUID of the server you want to reboot.
    """

    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ReinstallServerRequest:
    server_id: str
    """
    UUID of the server you want to reinstall.
    """

    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    os_id: Optional[str]
    """
    Reinstall the server with the target OS, when no os_id provided the default OS for the server type is used.
    """


@dataclass
class SetServerPrivateNetworksResponse:
    server_private_networks: List[ServerPrivateNetwork]


@dataclass
class StartConnectivityDiagnosticRequest:
    server_id: str

    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class StartConnectivityDiagnosticResponse:
    diagnostic_id: str


@dataclass
class UpdateServerRequest:
    server_id: str
    """
    UUID of the server you want to update.
    """

    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Updated name for your server.
    """

    schedule_deletion: Optional[bool]
    """
    Specify whether the server should be flagged for automatic deletion.
    """

    enable_vpc: Optional[bool]
    """
    Activate or deactivate Private Network support for this server.
    """
