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


class Arch(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ARCH = "unknown_arch"
    X86_64 = "x86_64"
    ARM = "arm"
    ARM64 = "arm64"

    def __str__(self) -> str:
        return str(self.value)


class AttachServerVolumeRequestVolumeType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_VOLUME_TYPE = "unknown_volume_type"
    L_SSD = "l_ssd"
    B_SSD = "b_ssd"
    SBS_VOLUME = "sbs_volume"

    def __str__(self) -> str:
        return str(self.value)


class BootType(str, Enum, metaclass=StrEnumMeta):
    LOCAL = "local"
    BOOTSCRIPT = "bootscript"
    RESCUE = "rescue"

    def __str__(self) -> str:
        return str(self.value)


class ImageState(str, Enum, metaclass=StrEnumMeta):
    AVAILABLE = "available"
    CREATING = "creating"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class IpState(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATE = "unknown_state"
    DETACHED = "detached"
    ATTACHED = "attached"
    PENDING = "pending"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class IpType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_IPTYPE = "unknown_iptype"
    ROUTED_IPV4 = "routed_ipv4"
    ROUTED_IPV6 = "routed_ipv6"

    def __str__(self) -> str:
        return str(self.value)


class ListServersRequestOrder(str, Enum, metaclass=StrEnumMeta):
    CREATION_DATE_DESC = "creation_date_desc"
    CREATION_DATE_ASC = "creation_date_asc"
    MODIFICATION_DATE_DESC = "modification_date_desc"
    MODIFICATION_DATE_ASC = "modification_date_asc"

    def __str__(self) -> str:
        return str(self.value)


class PlacementGroupPolicyMode(str, Enum, metaclass=StrEnumMeta):
    OPTIONAL = "optional"
    ENFORCED = "enforced"

    def __str__(self) -> str:
        return str(self.value)


class PlacementGroupPolicyType(str, Enum, metaclass=StrEnumMeta):
    MAX_AVAILABILITY = "max_availability"
    LOW_LATENCY = "low_latency"

    def __str__(self) -> str:
        return str(self.value)


class PrivateNICState(str, Enum, metaclass=StrEnumMeta):
    AVAILABLE = "available"
    SYNCING = "syncing"
    SYNCING_ERROR = "syncing_error"

    def __str__(self) -> str:
        return str(self.value)


class SecurityGroupPolicy(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_POLICY = "unknown_policy"
    ACCEPT = "accept"
    DROP = "drop"

    def __str__(self) -> str:
        return str(self.value)


class SecurityGroupRuleAction(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ACTION = "unknown_action"
    ACCEPT = "accept"
    DROP = "drop"

    def __str__(self) -> str:
        return str(self.value)


class SecurityGroupRuleDirection(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_DIRECTION = "unknown_direction"
    INBOUND = "inbound"
    OUTBOUND = "outbound"

    def __str__(self) -> str:
        return str(self.value)


class SecurityGroupRuleProtocol(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_PROTOCOL = "unknown_protocol"
    TCP = "tcp"
    UDP = "udp"
    ICMP = "icmp"
    ANY = "any"

    def __str__(self) -> str:
        return str(self.value)


class SecurityGroupState(str, Enum, metaclass=StrEnumMeta):
    AVAILABLE = "available"
    SYNCING = "syncing"
    SYNCING_ERROR = "syncing_error"

    def __str__(self) -> str:
        return str(self.value)


class ServerAction(str, Enum, metaclass=StrEnumMeta):
    POWERON = "poweron"
    BACKUP = "backup"
    STOP_IN_PLACE = "stop_in_place"
    POWEROFF = "poweroff"
    TERMINATE = "terminate"
    REBOOT = "reboot"
    ENABLE_ROUTED_IP = "enable_routed_ip"

    def __str__(self) -> str:
        return str(self.value)


class ServerFilesystemState(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATE = "unknown_state"
    ATTACHING = "attaching"
    AVAILABLE = "available"
    DETACHING = "detaching"

    def __str__(self) -> str:
        return str(self.value)


class ServerIpIpFamily(str, Enum, metaclass=StrEnumMeta):
    INET = "inet"
    INET6 = "inet6"

    def __str__(self) -> str:
        return str(self.value)


class ServerIpProvisioningMode(str, Enum, metaclass=StrEnumMeta):
    MANUAL = "manual"
    DHCP = "dhcp"
    SLAAC = "slaac"

    def __str__(self) -> str:
        return str(self.value)


class ServerIpState(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATE = "unknown_state"
    DETACHED = "detached"
    ATTACHED = "attached"
    PENDING = "pending"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class ServerState(str, Enum, metaclass=StrEnumMeta):
    RUNNING = "running"
    STOPPED = "stopped"
    STOPPED_IN_PLACE = "stopped_in_place"
    STARTING = "starting"
    STOPPING = "stopping"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class ServerTypesAvailability(str, Enum, metaclass=StrEnumMeta):
    AVAILABLE = "available"
    SCARCE = "scarce"
    SHORTAGE = "shortage"

    def __str__(self) -> str:
        return str(self.value)


class SnapshotState(str, Enum, metaclass=StrEnumMeta):
    AVAILABLE = "available"
    SNAPSHOTTING = "snapshotting"
    ERROR = "error"
    INVALID_DATA = "invalid_data"
    IMPORTING = "importing"
    EXPORTING = "exporting"

    def __str__(self) -> str:
        return str(self.value)


class SnapshotVolumeType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_VOLUME_TYPE = "unknown_volume_type"
    L_SSD = "l_ssd"
    B_SSD = "b_ssd"
    UNIFIED = "unified"

    def __str__(self) -> str:
        return str(self.value)


class TaskStatus(str, Enum, metaclass=StrEnumMeta):
    PENDING = "pending"
    STARTED = "started"
    SUCCESS = "success"
    FAILURE = "failure"
    RETRY = "retry"

    def __str__(self) -> str:
        return str(self.value)


class VolumeServerState(str, Enum, metaclass=StrEnumMeta):
    AVAILABLE = "available"
    SNAPSHOTTING = "snapshotting"
    RESIZING = "resizing"
    FETCHING = "fetching"
    SAVING = "saving"
    HOTSYNCING = "hotsyncing"
    ATTACHING = "attaching"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class VolumeServerVolumeType(str, Enum, metaclass=StrEnumMeta):
    L_SSD = "l_ssd"
    B_SSD = "b_ssd"
    SBS_VOLUME = "sbs_volume"
    SCRATCH = "scratch"

    def __str__(self) -> str:
        return str(self.value)


class VolumeState(str, Enum, metaclass=StrEnumMeta):
    AVAILABLE = "available"
    SNAPSHOTTING = "snapshotting"
    FETCHING = "fetching"
    SAVING = "saving"
    ATTACHING = "attaching"
    RESIZING = "resizing"
    HOTSYNCING = "hotsyncing"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class VolumeVolumeType(str, Enum, metaclass=StrEnumMeta):
    L_SSD = "l_ssd"
    B_SSD = "b_ssd"
    UNIFIED = "unified"
    SCRATCH = "scratch"
    SBS_VOLUME = "sbs_volume"
    SBS_SNAPSHOT = "sbs_snapshot"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class ServerSummary:
    id: str
    name: str


@dataclass
class Bootscript:
    architecture: Arch
    bootcmdargs: str
    default: bool
    dtb: str
    id: str
    initrd: str
    kernel: str
    organization: str
    public: bool
    title: str
    project: str
    zone: ScwZone
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class Volume:
    id: str
    """
    Volume unique ID.
    """

    name: str
    """
    Volume name.
    """

    export_uri: str
    """
    Show the volume NBD export URI (deprecated, will always be empty).
    """

    size: int
    """
    Volume disk size.
    """

    volume_type: VolumeVolumeType
    """
    Volume type.
    """

    organization: str
    """
    Volume Organization ID.
    """

    project: str
    """
    Volume Project ID.
    """

    tags: list[str]
    """
    Volume tags.
    """

    state: VolumeState
    """
    Volume state.
    """

    zone: ScwZone
    """
    Zone in which the volume is located.
    """

    creation_date: Optional[datetime] = None
    """
    Volume creation date.
    """

    modification_date: Optional[datetime] = None
    """
    Volume modification date.
    """

    server: Optional[ServerSummary] = None
    """
    Instance attached to the volume.
    """


@dataclass
class VolumeSummary:
    id: str
    name: str
    size: int
    volume_type: VolumeVolumeType


@dataclass
class ServerTypeNetworkInterface:
    internal_bandwidth: Optional[int] = 0
    """
    Maximum internal bandwidth in bits per seconds.
    """

    internet_bandwidth: Optional[int] = 0
    """
    Maximum internet bandwidth in bits per seconds.
    """


@dataclass
class ServerTypeVolumeConstraintSizes:
    min_size: int
    """
    Minimum volume size in bytes.
    """

    max_size: int
    """
    Maximum volume size in bytes.
    """


@dataclass
class Image:
    id: str
    name: str
    arch: Arch
    extra_volumes: dict[str, Volume]
    from_server: str
    organization: str
    public: bool
    state: ImageState
    project: str
    tags: list[str]
    zone: ScwZone
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    creation_date: Optional[datetime] = None
    modification_date: Optional[datetime] = None
    default_bootscript: Optional[Bootscript] = None
    root_volume: Optional[VolumeSummary] = None


@dataclass
class PlacementGroup:
    id: str
    """
    Placement group unique ID.
    """

    name: str
    """
    Placement group name.
    """

    organization: str
    """
    Placement group Organization ID.
    """

    project: str
    """
    Placement group Project ID.
    """

    tags: list[str]
    """
    Placement group tags.
    """

    policy_mode: PlacementGroupPolicyMode
    """
    Select the failure mode when the placement cannot be respected, either optional or enforced.
    """

    policy_type: PlacementGroupPolicyType
    """
    Select the behavior of the placement group, either low_latency (group) or max_availability (spread).
    """

    policy_respected: bool
    """
    In the server endpoints the value is always false as it is deprecated.
In the placement group endpoints the value is correct.
    """

    zone: ScwZone
    """
    Zone in which the placement group is located.
    """


@dataclass
class PrivateNIC:
    id: str
    """
    Private NIC unique ID.
    """

    server_id: str
    """
    Instance to which the private NIC is attached.
    """

    private_network_id: str
    """
    Private Network the private NIC is attached to.
    """

    mac_address: str
    """
    Private NIC MAC address.
    """

    state: PrivateNICState
    """
    Private NIC state.
    """

    tags: list[str]
    """
    Private NIC tags.
    """

    zone: ScwZone
    """
    The zone in which the Private NIC is located.
    """

    creation_date: Optional[datetime] = None
    """
    Private NIC creation date.
    """


@dataclass
class SecurityGroupSummary:
    id: str
    name: str


@dataclass
class ServerFilesystem:
    filesystem_id: str
    state: ServerFilesystemState


@dataclass
class ServerIp:
    id: str
    """
    Unique ID of the IP address.
    """

    address: str
    """
    Instance's public IP-Address.
    """

    gateway: str
    """
    Gateway's IP address.
    """

    netmask: str
    """
    CIDR netmask.
    """

    family: ServerIpIpFamily
    """
    IP address family (inet or inet6).
    """

    dynamic: bool
    """
    True if the IP address is dynamic.
    """

    provisioning_mode: ServerIpProvisioningMode
    """
    Information about this address provisioning mode.
    """

    tags: list[str]
    """
    Tags associated with the IP.
    """

    ipam_id: str
    """
    The ip_id of an IPAM ip if the ip is created from IPAM, null if not.
    """

    state: ServerIpState
    """
    IP address state.
    """


@dataclass
class ServerIpv6:
    address: str
    """
    Instance IPv6 IP-Address.
    """

    gateway: str
    """
    IPv6 IP-addresses gateway.
    """

    netmask: str
    """
    IPv6 IP-addresses CIDR netmask.
    """


@dataclass
class ServerLocation:
    cluster_id: str
    hypervisor_id: str
    node_id: str
    platform_id: str
    zone_id: str


@dataclass
class ServerMaintenance:
    reason: str
    start_date: Optional[datetime] = None


@dataclass
class VolumeServer:
    id: str
    volume_type: VolumeServerVolumeType
    boot: bool
    zone: ScwZone
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    export_uri: Optional[str] = None
    organization: Optional[str] = None
    server: Optional[ServerSummary] = None
    size: Optional[int] = None
    creation_date: Optional[datetime] = None
    modification_date: Optional[datetime] = None
    state: Optional[VolumeServerState] = None
    project: Optional[str] = None


@dataclass
class SnapshotBaseVolume:
    id: str
    """
    Volume ID on which the snapshot is based.
    """

    name: str
    """
    Volume name on which the snapshot is based on.
    """


@dataclass
class ServerTypeCapabilities:
    boot_types: list[BootType]
    """
    List of supported boot types.
    """

    max_file_systems: int
    """
    Max number of SFS (Scaleway File Systems) that can be attached to the Instance.
    """

    block_storage: Optional[bool] = False
    """
    Defines whether the Instance supports block storage.
    """


@dataclass
class ServerTypeGPUInfo:
    gpu_manufacturer: str
    """
    GPU manufacturer.
    """

    gpu_name: str
    """
    GPU model name.
    """

    gpu_memory: int
    """
    RAM of a single GPU, in bytes.
    """


@dataclass
class ServerTypeNetwork:
    interfaces: list[ServerTypeNetworkInterface]
    """
    List of available network interfaces.
    """

    ipv6_support: bool
    """
    True if IPv6 is enabled.
    """

    sum_internal_bandwidth: Optional[int] = 0
    """
    Total maximum internal bandwidth in bits per seconds.
    """

    sum_internet_bandwidth: Optional[int] = 0
    """
    Total maximum internet bandwidth in bits per seconds.
    """


@dataclass
class ServerTypeVolumeConstraintsByType:
    l_ssd: Optional[ServerTypeVolumeConstraintSizes] = None
    """
    Local SSD volumes.
    """


@dataclass
class VolumeTypeCapabilities:
    snapshot: bool


@dataclass
class VolumeTypeConstraints:
    min: int
    max: int


@dataclass
class Server:
    id: str
    """
    Instance unique ID.
    """

    name: str
    """
    Instance name.
    """

    organization: str
    """
    Instance Organization ID.
    """

    project: str
    """
    Instance Project ID.
    """

    allowed_actions: list[ServerAction]
    """
    List of allowed actions on the Instance.
    """

    tags: list[str]
    """
    Tags associated with the Instance.
    """

    commercial_type: str
    """
    Instance commercial type (eg. GP1-M).
    """

    dynamic_ip_required: bool
    """
    True if a dynamic IPv4 is required.
    """

    routed_ip_enabled: bool
    """
    True to configure the instance so it uses the routed IP mode. Use of `routed_ip_enabled` as `False` is deprecated.
    """

    enable_ipv6: bool
    """
    True if IPv6 is enabled (deprecated and always `False` when `routed_ip_enabled` is `True`).
    """

    hostname: str
    """
    Instance host name.
    """

    protected: bool
    """
    Defines whether the Instance protection option is activated.
    """

    public_ips: list[ServerIp]
    """
    Information about all the public IPs attached to the server.
    """

    mac_address: str
    """
    The server's MAC address.
    """

    state: ServerState
    """
    Instance state.
    """

    boot_type: BootType
    """
    Instance boot type.
    """

    volumes: dict[str, VolumeServer]
    """
    Instance volumes.
    """

    maintenances: list[ServerMaintenance]
    """
    Instance planned maintenance.
    """

    state_detail: str
    """
    Detailed information about the Instance state.
    """

    arch: Arch
    """
    Instance architecture.
    """

    private_nics: list[PrivateNIC]
    """
    Instance private NICs.
    """

    zone: ScwZone
    """
    Zone in which the Instance is located.
    """

    filesystems: list[ServerFilesystem]
    """
    List of attached filesystems.
    """

    end_of_service: bool
    """
    True if the Instance type has reached end of service.
    """

    creation_date: Optional[datetime] = None
    """
    Instance creation date.
    """

    image: Optional[Image] = None
    """
    Information about the Instance image.
    """

    private_ip: Optional[str] = None
    """
    Private IP address of the Instance (deprecated and always `null` when `routed_ip_enabled` is `True`).
    """

    public_ip: Optional[ServerIp] = None
    """
    Information about the public IP (deprecated in favor of `public_ips`).
    """

    modification_date: Optional[datetime] = None
    """
    Instance modification date.
    """

    location: Optional[ServerLocation] = None
    """
    Instance location.
    """

    ipv6: Optional[ServerIpv6] = None
    """
    Instance IPv6 address (deprecated when `routed_ip_enabled` is `True`).
    """

    security_group: Optional[SecurityGroupSummary] = None
    """
    Instance security group.
    """

    placement_group: Optional[PlacementGroup] = None
    """
    Instance placement group.
    """

    admin_password_encryption_ssh_key_id: Optional[str] = None
    """
    The public_key value of this key is used to encrypt the admin password. When set to an empty string, reset this value and admin_password_encrypted_value to an empty string so a new password may be generated.
    """

    admin_password_encrypted_value: Optional[str] = None
    """
    This value is reset when admin_password_encryption_ssh_key_id is set to an empty string.
    """

    dns: Optional[str] = None
    """
    Public DNS of the server.
    """


@dataclass
class VolumeTemplate:
    id: str
    """
    UUID of the volume.
    """

    name: str
    """
    Name of the volume.
    """

    size: int
    """
    Disk size of the volume, must be a multiple of 512.
    """

    volume_type: VolumeVolumeType
    """
    Type of the volume.
    """

    project: Optional[str] = None

    organization: Optional[str] = None


@dataclass
class Ip:
    id: str
    address: str
    organization: str
    tags: list[str]
    project: str
    type_: IpType
    state: IpState
    prefix: str
    ipam_id: str
    zone: ScwZone
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    reverse: Optional[str] = None
    server: Optional[ServerSummary] = None


@dataclass
class SecurityGroup:
    id: str
    """
    Security group unique ID.
    """

    name: str
    """
    Security group name.
    """

    description: str
    """
    Security group description.
    """

    enable_default_security: bool
    """
    True if SMTP is blocked on IPv4 and IPv6. This feature is read only, please open a support ticket if you need to make it configurable.
    """

    inbound_default_policy: SecurityGroupPolicy
    """
    Default inbound policy.
    """

    outbound_default_policy: SecurityGroupPolicy
    """
    Default outbound policy.
    """

    organization: str
    """
    Security group Organization ID.
    """

    project: str
    """
    Security group Project ID.
    """

    tags: list[str]
    """
    Security group tags.
    """

    organization_default: bool
    """
    True if it is your default security group for this Organization ID.
    """

    project_default: bool
    """
    True if it is your default security group for this Project ID.
    """

    servers: list[ServerSummary]
    """
    List of Instances attached to this security group.
    """

    stateful: bool
    """
    Defines whether the security group is stateful.
    """

    state: SecurityGroupState
    """
    Security group state.
    """

    zone: ScwZone
    """
    Zone in which the security group is located.
    """

    creation_date: Optional[datetime] = None
    """
    Security group creation date.
    """

    modification_date: Optional[datetime] = None
    """
    Security group modification date.
    """


@dataclass
class SecurityGroupRule:
    id: str
    protocol: SecurityGroupRuleProtocol
    direction: SecurityGroupRuleDirection
    action: SecurityGroupRuleAction
    ip_range: str
    position: int
    editable: bool
    zone: ScwZone
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    dest_port_from: Optional[int] = None
    dest_port_to: Optional[int] = None


@dataclass
class VolumeServerTemplate:
    volume_type: VolumeVolumeType
    """
    Type of the volume.
    """

    id: Optional[str] = None
    """
    UUID of the volume.
    """

    boot: Optional[bool] = False
    """
    Force the Instance to boot on this volume.
    """

    name: Optional[str] = None
    """
    Name of the volume.
    """

    size: Optional[int] = 0
    """
    Disk size of the volume, must be a multiple of 512.
    """

    base_snapshot: Optional[str] = None
    """
    ID of the snapshot on which this volume will be based.
    """

    organization: Optional[str] = None
    """
    Organization ID of the volume.
    """

    project: Optional[str] = None
    """
    Project ID of the volume.
    """


@dataclass
class Snapshot:
    id: str
    """
    Snapshot ID.
    """

    name: str
    """
    Snapshot name.
    """

    organization: str
    """
    Snapshot Organization ID.
    """

    project: str
    """
    Snapshot Project ID.
    """

    tags: list[str]
    """
    Snapshot tags.
    """

    volume_type: VolumeVolumeType
    """
    Snapshot volume type.
    """

    size: int
    """
    Snapshot size.
    """

    state: SnapshotState
    """
    Snapshot state.
    """

    zone: ScwZone
    """
    Snapshot zone.
    """

    base_volume: Optional[SnapshotBaseVolume] = None
    """
    Volume on which the snapshot is based on.
    """

    creation_date: Optional[datetime] = None
    """
    Snapshot creation date.
    """

    modification_date: Optional[datetime] = None
    """
    Snapshot modification date.
    """

    error_reason: Optional[str] = None
    """
    Reason for the failed snapshot import.
    """


@dataclass
class Task:
    id: str
    """
    Unique ID of the task.
    """

    description: str
    """
    Description of the task.
    """

    progress: int
    """
    Progress of the task in percent.
    """

    status: TaskStatus
    """
    Task status.
    """

    href_from: str
    href_result: str
    zone: ScwZone
    """
    Zone in which the task is executed.
    """

    started_at: Optional[datetime] = None
    """
    Task start date.
    """

    terminated_at: Optional[datetime] = None
    """
    Task end date.
    """


@dataclass
class Dashboard:
    volumes_count: int
    running_servers_count: int
    servers_by_types: dict[str, int]
    images_count: int
    snapshots_count: int
    servers_count: int
    ips_count: int
    security_groups_count: int
    ips_unused: int
    volumes_l_ssd_count: int
    volumes_l_ssd_total_size: int
    private_nics_count: int
    placement_groups_count: int
    volumes_scratch_count: int
    volumes_b_ssd_count: int
    volumes_b_ssd_total_size: int


@dataclass
class PlacementGroupServer:
    id: str
    """
    Instance UUID.
    """

    name: str
    """
    Instance name.
    """

    policy_respected: bool
    """
    Defines whether the placement group policy is respected (either 1 or 0).
    """


@dataclass
class GetServerTypesAvailabilityResponseAvailability:
    availability: ServerTypesAvailability


@dataclass
class ServerType:
    monthly_price: float
    """
    Estimated monthly price, for a 30 days month, in Euro.
    """

    hourly_price: float
    """
    Hourly price in Euro.
    """

    alt_names: list[str]
    """
    Alternative Instance name, if any.
    """

    ncpus: int
    """
    Number of CPU.
    """

    ram: int
    """
    Available RAM in bytes.
    """

    arch: Arch
    """
    CPU architecture.
    """

    scratch_storage_max_volumes_count: int
    """
    Maximum supported number of scratch volumes.
    """

    end_of_service: bool
    """
    True if this Instance type has reached end of service.
    """

    per_volume_constraint: Optional[ServerTypeVolumeConstraintsByType] = None
    """
    Additional volume constraints.
    """

    volumes_constraint: Optional[ServerTypeVolumeConstraintSizes] = None
    """
    Initial volume constraints.
    """

    gpu: Optional[int] = 0
    """
    Number of GPU.
    """

    gpu_info: Optional[ServerTypeGPUInfo] = None
    """
    GPU information.
    """

    network: Optional[ServerTypeNetwork] = None
    """
    Network available for the Instance.
    """

    capabilities: Optional[ServerTypeCapabilities] = None
    """
    Capabilities.
    """

    scratch_storage_max_size: Optional[int] = 0
    """
    Maximum available scratch storage.
    """

    block_bandwidth: Optional[int] = 0
    """
    The maximum bandwidth allocated to block storage access (in bytes per second).
    """


@dataclass
class VolumeType:
    display_name: str
    capabilities: Optional[VolumeTypeCapabilities] = None
    constraints: Optional[VolumeTypeConstraints] = None


@dataclass
class ServerActionRequestVolumeBackupTemplate:
    volume_type: SnapshotVolumeType
    """
    Overrides the `volume_type` of the snapshot for this volume.
If omitted, the volume type of the original volume will be used.
    """


@dataclass
class SetSecurityGroupRulesRequestRule:
    action: SecurityGroupRuleAction
    """
    Action to apply when the rule matches a packet.
    """

    protocol: SecurityGroupRuleProtocol
    """
    Protocol family this rule applies to.
    """

    direction: SecurityGroupRuleDirection
    """
    Direction the rule applies to.
    """

    ip_range: str
    """
    Range of IP addresses these rules apply to.
    """

    position: int
    """
    Position of this rule in the security group rules list. If several rules are passed with the same position, the resulting order is undefined.
    """

    id: Optional[str] = None
    """
    UUID of the security rule to update. If no value is provided, a new rule will be created.
    """

    dest_port_from: Optional[int] = 0
    """
    Beginning of the range of ports this rule applies to (inclusive). This value will be set to null if protocol is ICMP or ANY.
    """

    dest_port_to: Optional[int] = 0
    """
    End of the range of ports this rule applies to (inclusive). This value will be set to null if protocol is ICMP or ANY, or if it is equal to dest_port_from.
    """

    editable: Optional[bool] = False
    """
    Indicates if this rule is editable. Rules with the value false will be ignored.
    """

    zone: Optional[ScwZone] = None
    """
    Zone of the rule. This field is ignored.
    """


@dataclass
class VolumeImageUpdateTemplate:
    id: str
    """
    UUID of the snapshot.
    """


@dataclass
class SecurityGroupTemplate:
    id: str
    name: str


@dataclass
class ApplyBlockMigrationRequest:
    validation_key: str
    """
    A value to be retrieved from a call to the [Get a volume or snapshot's migration plan](#path-volumes-get-a-volume-or-snapshots-migration-plan) endpoint, to confirm that the volume and/or snapshots specified in said plan should be migrated.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_id: Optional[str] = None

    snapshot_id: Optional[str] = None


@dataclass
class AttachServerFileSystemRequest:
    server_id: str
    filesystem_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class AttachServerFileSystemResponse:
    server: Optional[Server] = None


@dataclass
class AttachServerVolumeRequest:
    server_id: str
    volume_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_type: Optional[AttachServerVolumeRequestVolumeType] = None
    boot: Optional[bool] = None


@dataclass
class AttachServerVolumeResponse:
    server: Optional[Server] = None


@dataclass
class CheckBlockMigrationOrganizationQuotasRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    organization: Optional[str] = None


@dataclass
class CreateImageRequest:
    root_volume: str
    """
    UUID of the snapshot.
    """

    arch: Arch
    """
    Architecture of the image.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    Name of the image.
    """

    extra_volumes: Optional[dict[str, VolumeTemplate]] = field(default_factory=dict)
    """
    Additional volumes of the image.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the image.
    """

    public: Optional[bool] = False
    """
    True to create a public image.
    """

    project: Optional[str] = None

    organization: Optional[str] = None


@dataclass
class CreateImageResponse:
    image: Optional[Image] = None


@dataclass
class CreateIpRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the IP.
    """

    server: Optional[str] = None
    """
    UUID of the Instance you want to attach the IP to.
    """

    type_: Optional[IpType] = IpType.UNKNOWN_IPTYPE
    """
    IP type to reserve (either 'routed_ipv4' or 'routed_ipv6').
    """

    project: Optional[str] = None

    organization: Optional[str] = None


@dataclass
class CreateIpResponse:
    ip: Optional[Ip] = None


@dataclass
class CreatePlacementGroupRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    Name of the placement group.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the placement group.
    """

    policy_mode: Optional[PlacementGroupPolicyMode] = PlacementGroupPolicyMode.OPTIONAL
    """
    Operating mode of the placement group.
    """

    policy_type: Optional[PlacementGroupPolicyType] = (
        PlacementGroupPolicyType.MAX_AVAILABILITY
    )
    """
    Policy type of the placement group.
    """

    project: Optional[str] = None

    organization: Optional[str] = None


@dataclass
class CreatePlacementGroupResponse:
    placement_group: Optional[PlacementGroup] = None


@dataclass
class CreatePrivateNICRequest:
    server_id: str
    """
    UUID of the Instance the private NIC will be attached to.
    """

    private_network_id: str
    """
    UUID of the private network where the private NIC will be attached.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Private NIC tags.
    """

    ip_ids: Optional[list[str]] = field(default_factory=list)
    """
    Ip_ids defined from IPAM.
    """

    ipam_ip_ids: Optional[list[str]] = field(default_factory=list)
    """
    UUID of IPAM ips, to be attached to the instance in the requested private network.
    """


@dataclass
class CreatePrivateNICResponse:
    private_nic: Optional[PrivateNIC] = None


@dataclass
class CreateSecurityGroupRequest:
    description: str
    """
    Description of the security group.
    """

    stateful: bool
    """
    Whether the security group is stateful or not.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    Name of the security group.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the security group.
    """

    inbound_default_policy: Optional[SecurityGroupPolicy] = (
        SecurityGroupPolicy.UNKNOWN_POLICY
    )
    """
    Default policy for inbound rules.
    """

    outbound_default_policy: Optional[SecurityGroupPolicy] = (
        SecurityGroupPolicy.UNKNOWN_POLICY
    )
    """
    Default policy for outbound rules.
    """

    enable_default_security: Optional[bool] = False
    """
    True to block SMTP on IPv4 and IPv6. This feature is read only, please open a support ticket if you need to make it configurable.
    """

    project: Optional[str] = None

    organization: Optional[str] = None

    organization_default: Optional[bool] = False

    project_default: Optional[bool] = False


@dataclass
class CreateSecurityGroupResponse:
    security_group: Optional[SecurityGroup] = None


@dataclass
class CreateSecurityGroupRuleRequest:
    security_group_id: str
    """
    UUID of the security group.
    """

    protocol: SecurityGroupRuleProtocol
    direction: SecurityGroupRuleDirection
    action: SecurityGroupRuleAction
    ip_range: str
    position: int
    """
    Position of this rule in the security group rules list.
    """

    editable: bool
    """
    Indicates if this rule is editable (will be ignored).
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    dest_port_from: Optional[int] = 0
    """
    Beginning of the range of ports to apply this rule to (inclusive).
    """

    dest_port_to: Optional[int] = 0
    """
    End of the range of ports to apply this rule to (inclusive).
    """


@dataclass
class CreateSecurityGroupRuleResponse:
    rule: Optional[SecurityGroupRule] = None


@dataclass
class CreateServerRequest:
    commercial_type: str
    """
    Define the Instance commercial type (i.e. GP1-S).
    """

    enable_ipv6: bool
    """
    True if IPv6 is enabled on the server (deprecated and always `False` when `routed_ip_enabled` is `True`).
    """

    protected: bool
    """
    True to activate server protection option.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    Instance name.
    """

    dynamic_ip_required: Optional[bool] = False
    """
    By default, `dynamic_ip_required` is true, a dynamic ip is attached to the instance (if no flexible ip is already attached).
    """

    routed_ip_enabled: Optional[bool] = False
    """
    If true, configure the Instance so it uses the new routed IP mode.
    """

    image: Optional[str] = None
    """
    Instance image ID or label.
    """

    volumes: Optional[dict[str, VolumeServerTemplate]] = field(default_factory=dict)
    """
    Volumes attached to the server.
    """

    public_ip: Optional[str] = None
    """
    ID of the reserved IP to attach to the Instance.
    """

    public_ips: Optional[list[str]] = field(default_factory=list)
    """
    A list of reserved IP IDs to attach to the Instance.
    """

    boot_type: Optional[BootType] = BootType.LOCAL
    """
    Boot type to use.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Instance tags.
    """

    security_group: Optional[str] = None
    """
    Security group ID.
    """

    placement_group: Optional[str] = None
    """
    Placement group ID if Instance must be part of a placement group.
    """

    admin_password_encryption_ssh_key_id: Optional[str] = None
    """
    The public_key value of this key is used to encrypt the admin password.
    """

    project: Optional[str] = None

    organization: Optional[str] = None


@dataclass
class CreateServerResponse:
    server: Optional[Server] = None


@dataclass
class CreateSnapshotRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    Name of the snapshot.
    """

    volume_id: Optional[str] = None
    """
    UUID of the volume.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the snapshot.
    """

    volume_type: Optional[SnapshotVolumeType] = SnapshotVolumeType.UNKNOWN_VOLUME_TYPE
    """
    Overrides the volume_type of the snapshot.
If omitted, the volume type of the original volume will be used.
    """

    bucket: Optional[str] = None
    """
    Bucket name for snapshot imports.
    """

    key: Optional[str] = None
    """
    Object key for snapshot imports.
    """

    size: Optional[int] = 0
    """
    Imported snapshot size, must be a multiple of 512.
    """

    project: Optional[str] = None

    organization: Optional[str] = None


@dataclass
class CreateSnapshotResponse:
    snapshot: Optional[Snapshot] = None
    task: Optional[Task] = None


@dataclass
class CreateVolumeRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    Volume name.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Volume tags.
    """

    volume_type: Optional[VolumeVolumeType] = VolumeVolumeType.L_SSD
    """
    Volume type.
    """

    project: Optional[str] = None

    organization: Optional[str] = None

    size: Optional[int] = 0

    base_snapshot: Optional[str] = None


@dataclass
class CreateVolumeResponse:
    volume: Optional[Volume] = None


@dataclass
class DeleteImageRequest:
    image_id: str
    """
    UUID of the image you want to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteIpRequest:
    ip: str
    """
    ID or address of the IP to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeletePlacementGroupRequest:
    placement_group_id: str
    """
    UUID of the placement group you want to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeletePrivateNICRequest:
    server_id: str
    """
    Instance to which the private NIC is attached.
    """

    private_nic_id: str
    """
    Private NIC unique ID.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteSecurityGroupRequest:
    security_group_id: str
    """
    UUID of the security group you want to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteSecurityGroupRuleRequest:
    security_group_id: str
    security_group_rule_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteServerRequest:
    server_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteServerUserDataRequest:
    server_id: str
    """
    UUID of the Instance.
    """

    key: str
    """
    Key of the user data to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteSnapshotRequest:
    snapshot_id: str
    """
    UUID of the snapshot you want to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteVolumeRequest:
    volume_id: str
    """
    UUID of the volume you want to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DetachServerFileSystemRequest:
    server_id: str
    filesystem_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DetachServerFileSystemResponse:
    server: Optional[Server] = None


@dataclass
class DetachServerVolumeRequest:
    server_id: str
    volume_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DetachServerVolumeResponse:
    server: Optional[Server] = None


@dataclass
class ExportSnapshotRequest:
    bucket: str
    """
    Object Storage bucket name.
    """

    key: str
    """
    Object key.
    """

    snapshot_id: str
    """
    Snapshot ID.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ExportSnapshotResponse:
    task: Optional[Task] = None


@dataclass
class GetDashboardRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    organization: Optional[str] = None
    project: Optional[str] = None


@dataclass
class GetDashboardResponse:
    dashboard: Optional[Dashboard] = None


@dataclass
class GetImageRequest:
    image_id: str
    """
    UUID of the image you want to get.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetImageResponse:
    image: Optional[Image] = None


@dataclass
class GetIpRequest:
    ip: str
    """
    IP ID or address to get.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetIpResponse:
    ip: Optional[Ip] = None


@dataclass
class GetPlacementGroupRequest:
    placement_group_id: str
    """
    UUID of the placement group you want to get.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetPlacementGroupResponse:
    placement_group: Optional[PlacementGroup] = None


@dataclass
class GetPlacementGroupServersRequest:
    placement_group_id: str
    """
    UUID of the placement group you want to get.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetPlacementGroupServersResponse:
    servers: list[PlacementGroupServer]
    """
    Instances attached to the placement group.
    """


@dataclass
class GetPrivateNICRequest:
    server_id: str
    """
    Instance to which the private NIC is attached.
    """

    private_nic_id: str
    """
    Private NIC unique ID.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetPrivateNICResponse:
    private_nic: Optional[PrivateNIC] = None


@dataclass
class GetSecurityGroupRequest:
    security_group_id: str
    """
    UUID of the security group you want to get.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetSecurityGroupResponse:
    security_group: Optional[SecurityGroup] = None


@dataclass
class GetSecurityGroupRuleRequest:
    security_group_id: str
    security_group_rule_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetSecurityGroupRuleResponse:
    rule: Optional[SecurityGroupRule] = None


@dataclass
class GetServerCompatibleTypesRequest:
    server_id: str
    """
    UUID of the Instance you want to get.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerRequest:
    server_id: str
    """
    UUID of the Instance you want to get.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerResponse:
    server: Optional[Server] = None


@dataclass
class GetServerTypesAvailabilityRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    per_page: Optional[int] = 0
    """
    A positive integer lower or equal to 100 to select the number of items to return.
    """

    page: Optional[int] = 0
    """
    A positive integer to choose the page to return.
    """


@dataclass
class GetServerTypesAvailabilityResponse:
    servers: dict[str, GetServerTypesAvailabilityResponseAvailability]
    """
    Map of server types.
    """

    total_count: int


@dataclass
class GetSnapshotRequest:
    snapshot_id: str
    """
    UUID of the snapshot you want to get.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetSnapshotResponse:
    snapshot: Optional[Snapshot] = None


@dataclass
class GetVolumeRequest:
    volume_id: str
    """
    UUID of the volume you want to get.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetVolumeResponse:
    volume: Optional[Volume] = None


@dataclass
class ListDefaultSecurityGroupRulesRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListImagesRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    organization: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    name: Optional[str] = None
    public: Optional[bool] = None
    arch: Optional[str] = None
    project: Optional[str] = None
    tags: Optional[str] = None


@dataclass
class ListImagesResponse:
    total_count: int
    """
    Total number of images.
    """

    images: list[Image]
    """
    List of images.
    """


@dataclass
class ListIpsRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project: Optional[str] = None
    """
    Project ID in which the IPs are reserved.
    """

    organization: Optional[str] = None
    """
    Organization ID in which the IPs are reserved.
    """

    tags: Optional[list[str]] = None
    """
    Filter IPs with these exact tags (to filter with several tags, use commas to separate them).
    """

    name: Optional[str] = None
    """
    Filter on the IP address (Works as a LIKE operation on the IP address).
    """

    per_page: Optional[int] = 0
    """
    A positive integer lower or equal to 100 to select the number of items to return.
    """

    page: Optional[int] = 0
    """
    A positive integer to choose the page to return.
    """

    type_: Optional[str] = None
    """
    Filter on the IP Mobility IP type (whose value should be either 'routed_ipv4' or 'routed_ipv6').
    """


@dataclass
class ListIpsResponse:
    total_count: int
    """
    Total number of ips.
    """

    ips: list[Ip]
    """
    List of ips.
    """


@dataclass
class ListPlacementGroupsRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    per_page: Optional[int] = 0
    """
    A positive integer lower or equal to 100 to select the number of items to return.
    """

    page: Optional[int] = 0
    """
    A positive integer to choose the page to return.
    """

    organization: Optional[str] = None
    """
    List only placement groups of this Organization ID.
    """

    project: Optional[str] = None
    """
    List only placement groups of this Project ID.
    """

    tags: Optional[list[str]] = None
    """
    List placement groups with these exact tags (to filter with several tags, use commas to separate them).
    """

    name: Optional[str] = None
    """
    Filter placement groups by name (for eg. "cluster1" will return "cluster100" and "cluster1" but not "foo").
    """


@dataclass
class ListPlacementGroupsResponse:
    total_count: int
    """
    Total number of placement groups.
    """

    placement_groups: list[PlacementGroup]
    """
    List of placement groups.
    """


@dataclass
class ListPrivateNICsRequest:
    server_id: str
    """
    Instance to which the private NIC is attached.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[list[str]] = None
    """
    Private NIC tags.
    """

    per_page: Optional[int] = 0
    """
    A positive integer lower or equal to 100 to select the number of items to return.
    """

    page: Optional[int] = 0
    """
    A positive integer to choose the page to return.
    """


@dataclass
class ListPrivateNICsResponse:
    private_nics: list[PrivateNIC]
    total_count: int


@dataclass
class ListSecurityGroupRulesRequest:
    security_group_id: str
    """
    UUID of the security group.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    per_page: Optional[int] = 0
    """
    A positive integer lower or equal to 100 to select the number of items to return.
    """

    page: Optional[int] = 0
    """
    A positive integer to choose the page to return.
    """


@dataclass
class ListSecurityGroupRulesResponse:
    total_count: int
    """
    Total number of security groups.
    """

    rules: list[SecurityGroupRule]
    """
    List of security rules.
    """


@dataclass
class ListSecurityGroupsRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    Name of the security group.
    """

    organization: Optional[str] = None
    """
    Security group Organization ID.
    """

    project: Optional[str] = None
    """
    Security group Project ID.
    """

    tags: Optional[list[str]] = None
    """
    List security groups with these exact tags (to filter with several tags, use commas to separate them).
    """

    project_default: Optional[bool] = False
    """
    Filter security groups with this value for project_default.
    """

    per_page: Optional[int] = 0
    """
    A positive integer lower or equal to 100 to select the number of items to return.
    """

    page: Optional[int] = 0
    """
    A positive integer to choose the page to return.
    """


@dataclass
class ListSecurityGroupsResponse:
    total_count: int
    """
    Total number of security groups.
    """

    security_groups: list[SecurityGroup]
    """
    List of security groups.
    """


@dataclass
class ListServerActionsRequest:
    server_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListServerActionsResponse:
    actions: list[ServerAction]


@dataclass
class ListServerUserDataRequest:
    server_id: str
    """
    UUID of the Instance.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListServerUserDataResponse:
    user_data: list[str]


@dataclass
class ListServersRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    per_page: Optional[int] = 0
    """
    A positive integer lower or equal to 100 to select the number of items to return.
    """

    page: Optional[int] = 0
    """
    A positive integer to choose the page to return.
    """

    organization: Optional[str] = None
    """
    List only Instances of this Organization ID.
    """

    project: Optional[str] = None
    """
    List only Instances of this Project ID.
    """

    name: Optional[str] = None
    """
    Filter Instances by name (eg. "server1" will return "server100" and "server1" but not "foo").
    """

    private_ip: Optional[str] = None
    """
    List Instances by private_ip.
    """

    without_ip: Optional[bool] = False
    """
    List Instances that are not attached to a public IP.
    """

    with_ip: Optional[str] = None
    """
    List Instances by IP (both private_ip and public_ip are supported).
    """

    commercial_type: Optional[str] = None
    """
    List Instances of this commercial type.
    """

    state: Optional[ServerState] = ServerState.RUNNING
    """
    List Instances in this state.
    """

    tags: Optional[list[str]] = None
    """
    List Instances with these exact tags (to filter with several tags, use commas to separate them).
    """

    private_network: Optional[str] = None
    """
    List Instances in this Private Network.
    """

    order: Optional[ListServersRequestOrder] = (
        ListServersRequestOrder.CREATION_DATE_DESC
    )
    """
    Define the order of the returned servers.
    """

    private_networks: Optional[list[str]] = None
    """
    List Instances from the given Private Networks (use commas to separate them).
    """

    private_nic_mac_address: Optional[str] = None
    """
    List Instances associated with the given private NIC MAC address.
    """

    servers: Optional[list[str]] = None
    """
    List Instances from these server ids (use commas to separate them).
    """


@dataclass
class ListServersResponse:
    total_count: int
    """
    Total number of Instances.
    """

    servers: list[Server]
    """
    List of Instances.
    """


@dataclass
class ListServersTypesRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    per_page: Optional[int] = None
    page: Optional[int] = None


@dataclass
class ListServersTypesResponse:
    total_count: int
    """
    Total number of Instance types.
    """

    servers: dict[str, ServerType]
    """
    List of Instance types.
    """


@dataclass
class ListSnapshotsRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    organization: Optional[str] = None
    """
    List snapshots only for this Organization ID.
    """

    project: Optional[str] = None
    """
    List snapshots only for this Project ID.
    """

    per_page: Optional[int] = 0
    """
    Number of snapshots returned per page (positive integer lower or equal to 100).
    """

    page: Optional[int] = 0
    """
    Page to be returned.
    """

    name: Optional[str] = None
    """
    List snapshots of the requested name.
    """

    tags: Optional[str] = None
    """
    List snapshots that have the requested tag.
    """

    base_volume_id: Optional[str] = None
    """
    List snapshots originating only from this volume.
    """


@dataclass
class ListSnapshotsResponse:
    total_count: int
    """
    Total number of snapshots.
    """

    snapshots: list[Snapshot]
    """
    List of snapshots.
    """


@dataclass
class ListVolumesRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_type: Optional[VolumeVolumeType] = VolumeVolumeType.L_SSD
    """
    Filter by volume type.
    """

    per_page: Optional[int] = 0
    """
    A positive integer lower or equal to 100 to select the number of items to return.
    """

    page: Optional[int] = 0
    """
    A positive integer to choose the page to return.
    """

    organization: Optional[str] = None
    """
    Filter volume by Organization ID.
    """

    project: Optional[str] = None
    """
    Filter volume by Project ID.
    """

    tags: Optional[list[str]] = None
    """
    Filter volumes with these exact tags (to filter with several tags, use commas to separate them).
    """

    name: Optional[str] = None
    """
    Filter volume by name (for eg. "vol" will return "myvolume" but not "data").
    """


@dataclass
class ListVolumesResponse:
    total_count: int
    """
    Total number of volumes.
    """

    volumes: list[Volume]
    """
    List of volumes.
    """


@dataclass
class ListVolumesTypesRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    per_page: Optional[int] = None
    page: Optional[int] = None


@dataclass
class ListVolumesTypesResponse:
    total_count: int
    """
    Total number of volume types.
    """

    volumes: dict[str, VolumeType]
    """
    Map of volume types.
    """


@dataclass
class MigrationPlan:
    snapshots: list[Snapshot]
    """
    A list of snapshots which will be migrated to SBS together and with the volume, if present.
    """

    validation_key: str
    """
    A value to be passed to the call to the [Migrate a volume and/or snapshots to SBS](#path-volumes-migrate-a-volume-andor-snapshots-to-sbs-scaleway-block-storage) endpoint, to confirm that the execution of the plan is being requested.
    """

    volume: Optional[Volume] = None
    """
    A volume which will be migrated to SBS together with the snapshots, if present.
    """


@dataclass
class PlanBlockMigrationRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_id: Optional[str] = None

    snapshot_id: Optional[str] = None


@dataclass
class ReleaseIpToIpamRequest:
    ip_id: str
    """
    ID of the IP you want to release from the Instance but retain in IPAM.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ServerActionRequest:
    server_id: str
    """
    UUID of the Instance.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    action: Optional[ServerAction] = ServerAction.POWERON
    """
    Action to perform on the Instance.
    """

    name: Optional[str] = None
    """
    Name of the backup you want to create.
This field should only be specified when performing a backup action.
    """

    volumes: Optional[dict[str, ServerActionRequestVolumeBackupTemplate]] = field(
        default_factory=dict
    )
    """
    For each volume UUID, the snapshot parameters of the volume.
This field should only be specified when performing a backup action.
    """

    disable_ipv6: Optional[bool] = False
    """
    Disable IPv6 on the Instance while performing migration to routed IPs.
This field should only be specified when performing a enable_routed_ip action.
    """


@dataclass
class ServerActionResponse:
    task: Optional[Task] = None


@dataclass
class ServerCompatibleTypes:
    compatible_types: list[str]
    """
    Instance compatible types.
    """


@dataclass
class SetImageRequest:
    id: str
    name: str
    from_server: str
    public: bool
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    arch: Optional[Arch] = None
    creation_date: Optional[datetime] = None
    modification_date: Optional[datetime] = None
    default_bootscript: Optional[Bootscript] = None
    extra_volumes: Optional[dict[str, Volume]] = field(default_factory=dict)
    organization: Optional[str] = None
    root_volume: Optional[VolumeSummary] = None
    state: Optional[ImageState] = None
    project: Optional[str] = None
    tags: Optional[list[str]] = field(default_factory=list)


@dataclass
class SetPlacementGroupRequest:
    placement_group_id: str
    name: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    organization: Optional[str] = None
    policy_mode: Optional[PlacementGroupPolicyMode] = None
    policy_type: Optional[PlacementGroupPolicyType] = None
    project: Optional[str] = None
    tags: Optional[list[str]] = field(default_factory=list)


@dataclass
class SetPlacementGroupResponse:
    placement_group: Optional[PlacementGroup] = None


@dataclass
class SetPlacementGroupServersRequest:
    placement_group_id: str
    """
    UUID of the placement group you want to set.
    """

    servers: list[str]
    """
    An array of the Instances' UUIDs you want to configure.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetPlacementGroupServersResponse:
    servers: list[PlacementGroupServer]
    """
    Instances attached to the placement group.
    """


@dataclass
class SetSecurityGroupRulesRequest:
    security_group_id: str
    """
    UUID of the security group to update the rules on.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    rules: Optional[list[SetSecurityGroupRulesRequestRule]] = field(
        default_factory=list
    )
    """
    List of rules to update in the security group.
    """


@dataclass
class SetSecurityGroupRulesResponse:
    rules: list[SecurityGroupRule]


@dataclass
class UpdateImageRequest:
    image_id: str
    """
    UUID of the image.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    Name of the image.
    """

    arch: Optional[Arch] = Arch.UNKNOWN_ARCH
    """
    Architecture of the image.
    """

    extra_volumes: Optional[dict[str, VolumeImageUpdateTemplate]] = field(
        default_factory=dict
    )
    """
    Additional snapshots of the image, with extra_volumeKey being the position of the snapshot in the image.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the image.
    """

    public: Optional[bool] = False
    """
    True to set the image as public.
    """


@dataclass
class UpdateImageResponse:
    image: Optional[Image] = None


@dataclass
class UpdateIpRequest:
    ip: str
    """
    IP ID or IP address.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    reverse: Optional[str] = None
    """
    Reverse domain name.
    """

    type_: Optional[IpType] = IpType.UNKNOWN_IPTYPE
    """
    Should have no effect.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    An array of keywords you want to tag this IP with.
    """

    server: Optional[str] = None


@dataclass
class UpdateIpResponse:
    ip: Optional[Ip] = None


@dataclass
class UpdatePlacementGroupRequest:
    placement_group_id: str
    """
    UUID of the placement group.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    Name of the placement group.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the placement group.
    """

    policy_mode: Optional[PlacementGroupPolicyMode] = PlacementGroupPolicyMode.OPTIONAL
    """
    Operating mode of the placement group.
    """

    policy_type: Optional[PlacementGroupPolicyType] = (
        PlacementGroupPolicyType.MAX_AVAILABILITY
    )
    """
    Policy type of the placement group.
    """


@dataclass
class UpdatePlacementGroupResponse:
    placement_group: Optional[PlacementGroup] = None


@dataclass
class UpdatePlacementGroupServersRequest:
    placement_group_id: str
    """
    UUID of the placement group you want to update.
    """

    servers: list[str]
    """
    An array of the Instances' UUIDs you want to configure.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class UpdatePlacementGroupServersResponse:
    servers: list[PlacementGroupServer]
    """
    Instances attached to the placement group.
    """


@dataclass
class UpdatePrivateNICRequest:
    server_id: str
    """
    UUID of the Instance the private NIC will be attached to.
    """

    private_nic_id: str
    """
    Private NIC unique ID.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags used to select private NIC/s.
    """


@dataclass
class UpdateSecurityGroupRequest:
    security_group_id: str
    """
    UUID of the security group.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    Name of the security group.
    """

    description: Optional[str] = None
    """
    Description of the security group.
    """

    enable_default_security: Optional[bool] = False
    """
    True to block SMTP on IPv4 and IPv6. This feature is read only, please open a support ticket if you need to make it configurable.
    """

    inbound_default_policy: Optional[SecurityGroupPolicy] = (
        SecurityGroupPolicy.UNKNOWN_POLICY
    )
    """
    Default inbound policy.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the security group.
    """

    organization_default: Optional[bool] = False
    """
    Please use project_default instead.
    """

    project_default: Optional[bool] = False
    """
    True use this security group for future Instances created in this project.
    """

    outbound_default_policy: Optional[SecurityGroupPolicy] = (
        SecurityGroupPolicy.UNKNOWN_POLICY
    )
    """
    Default outbound policy.
    """

    stateful: Optional[bool] = False
    """
    True to set the security group as stateful.
    """


@dataclass
class UpdateSecurityGroupResponse:
    security_group: Optional[SecurityGroup] = None


@dataclass
class UpdateSecurityGroupRuleRequest:
    security_group_id: str
    """
    UUID of the security group.
    """

    security_group_rule_id: str
    """
    UUID of the rule.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    protocol: Optional[SecurityGroupRuleProtocol] = (
        SecurityGroupRuleProtocol.UNKNOWN_PROTOCOL
    )
    """
    Protocol family this rule applies to.
    """

    direction: Optional[SecurityGroupRuleDirection] = (
        SecurityGroupRuleDirection.UNKNOWN_DIRECTION
    )
    """
    Direction the rule applies to.
    """

    action: Optional[SecurityGroupRuleAction] = SecurityGroupRuleAction.UNKNOWN_ACTION
    """
    Action to apply when the rule matches a packet.
    """

    ip_range: Optional[str] = None
    """
    Range of IP addresses these rules apply to.
    """

    dest_port_from: Optional[int] = 0
    """
    Beginning of the range of ports this rule applies to (inclusive). If 0 is provided, unset the parameter.
    """

    dest_port_to: Optional[int] = 0
    """
    End of the range of ports this rule applies to (inclusive). If 0 is provided, unset the parameter.
    """

    position: Optional[int] = 0
    """
    Position of this rule in the security group rules list.
    """


@dataclass
class UpdateSecurityGroupRuleResponse:
    rule: Optional[SecurityGroupRule] = None


@dataclass
class UpdateServerRequest:
    server_id: str
    """
    UUID of the Instance.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    Name of the Instance.
    """

    boot_type: Optional[BootType] = BootType.LOCAL
    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the Instance.
    """

    volumes: Optional[dict[str, VolumeServerTemplate]] = field(default_factory=dict)
    dynamic_ip_required: Optional[bool] = False
    routed_ip_enabled: Optional[bool] = False
    """
    True to configure the instance so it uses the new routed IP mode (once this is set to True you cannot set it back to False).
    """

    public_ips: Optional[list[str]] = field(default_factory=list)
    """
    A list of reserved IP IDs to attach to the Instance.
    """

    enable_ipv6: Optional[bool] = False
    protected: Optional[bool] = False
    """
    True to activate server protection option.
    """

    security_group: Optional[SecurityGroupTemplate] = None
    placement_group: Optional[str] = None
    """
    Placement group ID if Instance must be part of a placement group.
    """

    private_nics: Optional[list[str]] = field(default_factory=list)
    """
    Instance private NICs.
    """

    commercial_type: Optional[str] = None
    """
    Warning: This field has some restrictions:
- Cannot be changed if the Instance is not in `stopped` state.
- Cannot be changed if the Instance is in a placement group.
- Cannot be changed from/to a Windows offer to/from a Linux offer.
- Local storage requirements of the target commercial_types must be fulfilled (i.e. if an Instance has 80GB of local storage, it can be changed into a GP1-XS, which has a maximum of 150GB, but it cannot be changed into a DEV1-S, which has only 20GB).
    """

    admin_password_encryption_ssh_key_id: Optional[str] = None
    """
    The public_key value of this key is used to encrypt the admin password. When set to an empty string, reset this value and admin_password_encrypted_value to an empty string so a new password may be generated.
    """


@dataclass
class UpdateServerResponse:
    server: Optional[Server] = None


@dataclass
class UpdateSnapshotRequest:
    snapshot_id: str
    """
    UUID of the snapshot.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    Name of the snapshot.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the snapshot.
    """


@dataclass
class UpdateSnapshotResponse:
    snapshot: Optional[Snapshot] = None


@dataclass
class UpdateVolumeRequest:
    volume_id: str
    """
    UUID of the volume.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    Volume name.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the volume.
    """

    size: Optional[int] = 0
    """
    Volume disk size, must be a multiple of 512.
    """


@dataclass
class UpdateVolumeResponse:
    volume: Optional[Volume] = None
