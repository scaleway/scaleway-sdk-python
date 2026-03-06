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


class CommitmentType(str, Enum, metaclass=StrEnumMeta):
    DURATION_24H = "duration_24h"
    RENEWED_MONTHLY = "renewed_monthly"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)


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


class RunnerConfigurationProvider(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_PROVIDER = "unknown_provider"
    GITHUB = "github"
    GITLAB = "gitlab"

    def __str__(self) -> str:
        return str(self.value)


class RunnerConfigurationV2Provider(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_PROVIDER = "unknown_provider"
    GITHUB = "github"
    GITLAB = "gitlab"

    def __str__(self) -> str:
        return str(self.value)


class RunnerStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    WAITING = "waiting"
    ENABLED = "enabled"
    DISABLED = "disabled"
    ERROR = "error"

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
class OSSupportedServerType:
    server_type: str
    fast_delivery_available: bool


@dataclass
class GithubRunnerConfiguration:
    url: str
    token: str
    labels: list[str]


@dataclass
class GitlabRunnerConfiguration:
    url: str
    token: str


@dataclass
class Commitment:
    type_: CommitmentType
    cancelled: bool


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

    compatible_server_types: list[str]
    """
    List of compatible server types. Deprecated.
    """

    release_notes_url: str
    """
    Url of the release notes for the OS image or software pre-installed.
    """

    description: str
    """
    A summary of the OS image content and configuration.
    """

    tags: list[str]
    """
    List of tags for the OS configuration.
    """

    supported_server_types: list[OSSupportedServerType]
    """
    List of server types which supports the OS configuration. Also gives information about immediate stock availability.
    """


@dataclass
class RunnerConfiguration:
    name: str
    url: str
    token: str
    provider: RunnerConfigurationProvider


@dataclass
class RunnerConfigurationV2:
    name: str
    provider: RunnerConfigurationV2Provider
    github_configuration: Optional[GithubRunnerConfiguration] = None

    gitlab_configuration: Optional[GitlabRunnerConfiguration] = None


@dataclass
class ServerTypeCPU:
    name: str
    core_count: int
    frequency: int
    sockets: int
    threads_per_core: int


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
class ServerTypeNPU:
    count: int


@dataclass
class ServerTypeNetwork:
    public_bandwidth_bps: int
    supported_bandwidth: list[int]
    default_public_bandwidth: int


@dataclass
class BatchCreateServersRequestBatchInnerCreateServerRequest:
    name: str


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

    public_bandwidth_bps: int
    """
    Public bandwidth configured for this server. Expressed in bits per second.
    """

    tags: list[str]
    """
    A list of tags attached to the server.
    """

    applied_runner_configuration_ids: list[str]
    """
    Runner configurations applied on the server, optional.
    """

    os: Optional[OS] = None
    """
    Initially installed OS, this does not necessarily reflect the current OS version.
    """

    created_at: Optional[datetime] = None
    """
    Date on which the server was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date on which the server was last updated.
    """

    deletable_at: Optional[datetime] = None
    """
    Date from which the server can be deleted.
    """

    commitment: Optional[Commitment] = None
    """
    Commitment scheme applied to this server.
    """

    runner_configuration: Optional[RunnerConfiguration] = None
    """
    Current runner configuration, empty if none is installed.
    """


@dataclass
class ConnectivityDiagnosticServerHealth:
    is_server_alive: bool
    is_agent_alive: bool
    is_mdm_alive: bool
    is_ssh_port_up: bool
    is_vnc_port_up: bool
    last_checkin_date: Optional[datetime] = None


@dataclass
class AppliedRunnerConfigurations:
    runner_configuration_ids: list[str]


@dataclass
class Runner:
    id: str
    status: RunnerStatus
    error_message: str
    configuration: Optional[RunnerConfigurationV2] = None


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

    ipam_ip_ids: list[str]
    """
    IPAM IP IDs of the server, if it has any.
    """

    vlan: Optional[int] = 0
    """
    ID of the VLAN associated with the Private Network.
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
class ServerType:
    name: str
    """
    Name of the type.
    """

    stock: ServerTypeStock
    """
    Current stock.
    """

    cpu: Optional[ServerTypeCPU] = None
    """
    CPU description.
    """

    disk: Optional[ServerTypeDisk] = None
    """
    Size of the local disk of the server.
    """

    memory: Optional[ServerTypeMemory] = None
    """
    Size of memory available.
    """

    minimum_lease_duration: Optional[str] = None
    """
    Minimum duration of the lease in seconds (example. 3.4s).
    """

    gpu: Optional[ServerTypeGPU] = None
    """
    GPU description.
    """

    network: Optional[ServerTypeNetwork] = None
    """
    Network description.
    """

    default_os: Optional[OS] = None
    """
    The default OS for this server type.
    """

    npu: Optional[ServerTypeNPU] = None
    """
    NPU description.
    """


@dataclass
class CommitmentTypeValue:
    commitment_type: CommitmentType


@dataclass
class BatchCreateServersRequest:
    type_: str
    """
    Create servers of the given type.
    """

    enable_vpc: bool
    """
    Activate the Private Network feature for these servers. This feature is configured through the Apple Silicon - Private Networks API.
    """

    public_bandwidth_bps: int
    """
    Public bandwidth to configure for these servers. This defaults to the minimum bandwidth for the corresponding server type. For compatible server types, the bandwidth can be increased which incurs additional costs.
    """

    enable_kext: bool
    """
    Enable kernel extensions in this install of mac OS.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    """
    Create servers in the given project ID.
    """

    os_id: Optional[str] = None
    """
    Create servers & install the given os_id, when no os_id provided the default OS for this server type is chosen. Requesting a non-default OS will induce an extended delivery time.
    """

    commitment_type: Optional[CommitmentType] = CommitmentType.DURATION_24H
    """
    Activate commitment for these servers. If not specified, there is a 24h commitment due to Apple licensing (commitment_type `duration_24h`). It can be updated with the Update Server request. Available commitment depends on server type.
    """

    requests: Optional[list[BatchCreateServersRequestBatchInnerCreateServerRequest]] = (
        field(default_factory=list)
    )
    """
    List of servers to create.
    """


@dataclass
class BatchCreateServersResponse:
    servers: list[Server]
    """
    List of created servers.
    """


@dataclass
class ConnectivityDiagnostic:
    id: str
    status: ConnectivityDiagnosticDiagnosticStatus
    is_healthy: bool
    supported_actions: list[ConnectivityDiagnosticActionType]
    error_message: str
    health_details: Optional[ConnectivityDiagnosticServerHealth] = None


@dataclass
class CreateRunnerRequest:
    runner_configuration: RunnerConfigurationV2
    """
    Configuration details for the runner.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    """
    Creates a runner in the given project_id.
    """


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

    public_bandwidth_bps: int
    """
    Public bandwidth to configure for this server. This defaults to the minimum bandwidth for this server type. For compatible server types, the bandwidth can be increased which incurs additional costs.
    """

    enable_kext: bool
    """
    Enable kernel extensions in this install of mac OS.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    Create a server with this given name.
    """

    project_id: Optional[str] = None
    """
    Create a server in the given project ID.
    """

    os_id: Optional[str] = None
    """
    Create a server & install the given os_id, when no os_id provided the default OS for this server type is chosen. Requesting a non-default OS will induce an extended delivery time.
    """

    commitment_type: Optional[CommitmentType] = CommitmentType.DURATION_24H
    """
    Activate commitment for this server. If not specified, there is a 24h commitment due to Apple licensing (commitment_type `duration_24h`). It can be updated with the Update Server request. Available commitment depends on server type.
    """

    runner_configuration: Optional[RunnerConfiguration] = None
    """
    Specify the configuration to install an optional CICD runner on the server during installation.
    """

    applied_runner_configurations: Optional[AppliedRunnerConfigurations] = None
    """
    Runner configurations to apply on the server, existing ones missing from the specified configuration will be removed from the server.
    """


@dataclass
class DeleteRunnerRequest:
    runner_id: str
    """
    ID of the runner configuration to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteServerRequest:
    server_id: str
    """
    UUID of the server you want to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetConnectivityDiagnosticRequest:
    diagnostic_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetOSRequest:
    os_id: str
    """
    UUID of the OS you want to get.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetRunnerRequest:
    runner_id: str
    """
    ID of the runner configuration to get.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerRequest:
    server_id: str
    """
    UUID of the server you want to get.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerTypeRequest:
    server_type: str
    """
    Server type identifier.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListOSRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int] = 0
    """
    Positive integer to choose the page to return.
    """

    page_size: Optional[int] = 0
    """
    Positive integer lower or equal to 100 to select the number of items to return.
    """

    server_type: Optional[str] = None
    """
    List of compatible server types.
    """

    name: Optional[str] = None
    """
    Filter OS by name (note that "11.1" will return "11.1.2" and "11.1" but not "12")).
    """


@dataclass
class ListOSResponse:
    total_count: int
    """
    Total number of OS.
    """

    os: list[OS]
    """
    List of OS.
    """


@dataclass
class ListRunnersRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_id: Optional[str] = None
    """
    ID of the server for which to list applied runner configurations.
    """

    project_id: Optional[str] = None
    """
    Only list servers of this project ID.
    """

    organization_id: Optional[str] = None
    """
    Only list servers of this Organization ID.
    """

    page: Optional[int] = 0
    """
    Positive integer to choose the page to return.
    """

    page_size: Optional[int] = 0
    """
    Positive integer lower or equal to 100 to select the number of items to return.
    """


@dataclass
class ListRunnersResponse:
    total_count: int
    runners: list[Runner]


@dataclass
class ListServerPrivateNetworksResponse:
    server_private_networks: list[ServerPrivateNetwork]
    total_count: int


@dataclass
class ListServerTypesRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListServerTypesResponse:
    server_types: list[ServerType]
    """
    Available server types.
    """


@dataclass
class ListServersRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListServersRequestOrderBy] = (
        ListServersRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order of the returned servers.
    """

    project_id: Optional[str] = None
    """
    Only list servers of this project ID.
    """

    organization_id: Optional[str] = None
    """
    Only list servers of this Organization ID.
    """

    page: Optional[int] = 0
    """
    Positive integer to choose the page to return.
    """

    page_size: Optional[int] = 0
    """
    Positive integer lower or equal to 100 to select the number of items to return.
    """


@dataclass
class ListServersResponse:
    total_count: int
    """
    Total number of servers.
    """

    servers: list[Server]
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

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    ipam_ip_ids: Optional[list[str]] = field(default_factory=list)
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

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class PrivateNetworkApiGetServerPrivateNetworkRequest:
    server_id: str
    private_network_id: str
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
    Filter Private Networks by server ID.
    """

    private_network_id: Optional[str] = None
    """
    Filter Private Networks by Private Network ID.
    """

    organization_id: Optional[str] = None
    """
    Filter Private Networks by Organization ID.
    """

    project_id: Optional[str] = None
    """
    Filter Private Networks by Project ID.
    """

    ipam_ip_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter Private Networks by IPAM IP IDs.
    """


@dataclass
class PrivateNetworkApiSetServerPrivateNetworksRequest:
    server_id: str
    """
    ID of the server.
    """

    per_private_network_ipam_ip_ids: dict[str, list[str]]
    """
    Object where the keys are the IDs of Private Networks and the values are arrays of IPAM IDs representing the IPs to assign to this Apple silicon server on the Private Network. If the array supplied for a Private Network is empty, the next available IP from the Private Network's CIDR block will automatically be used for attachment.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class RebootServerRequest:
    server_id: str
    """
    UUID of the server you want to reboot.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ReinstallServerRequest:
    server_id: str
    """
    UUID of the server you want to reinstall.
    """

    enable_kext: bool
    """
    Enable kernel extensions in this install of mac OS.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    os_id: Optional[str] = None
    """
    Reinstall the server with the target OS, when no os_id provided the default OS for the server type is used.
    """


@dataclass
class SetServerPrivateNetworksResponse:
    server_private_networks: list[ServerPrivateNetwork]


@dataclass
class StartConnectivityDiagnosticRequest:
    server_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class StartConnectivityDiagnosticResponse:
    diagnostic_id: str


@dataclass
class UpdateRunnerRequest:
    runner_id: str
    """
    ID of the runner configuration to update.
    """

    runner_configuration: RunnerConfigurationV2
    """
    Configuration details for the runner.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class UpdateServerRequest:
    server_id: str
    """
    UUID of the server you want to update.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    Updated name for your server.
    """

    schedule_deletion: Optional[bool] = False
    """
    Specify whether the server should be flagged for automatic deletion.
    """

    enable_vpc: Optional[bool] = False
    """
    Activate or deactivate Private Network support for this server.
    """

    commitment_type: Optional[CommitmentTypeValue] = None
    """
    Change commitment. Use 'none' to automatically cancel a renewing commitment.
    """

    public_bandwidth_bps: Optional[int] = 0
    """
    Public bandwidth to configure for this server. Setting an higher bandwidth incurs additional costs. Supported bandwidth levels depends on server type and can be queried using the `/server-types` endpoint.
    """

    applied_runner_configurations: Optional[AppliedRunnerConfigurations] = None
    """
    Runner configurations to apply on the server, existing ones missing from the specified configuration will be removed from the server.
    """
