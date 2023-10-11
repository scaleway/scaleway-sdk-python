# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from scaleway_core.bridge import (
    Zone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class Arch(str, Enum, metaclass=StrEnumMeta):
    X86_64 = "x86_64"
    ARM = "arm"
    ARM64 = "arm64"

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
    NAT = "nat"
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
    ACCEPT = "accept"
    DROP = "drop"

    def __str__(self) -> str:
        return str(self.value)


class SecurityGroupRuleAction(str, Enum, metaclass=StrEnumMeta):
    ACCEPT = "accept"
    DROP = "drop"

    def __str__(self) -> str:
        return str(self.value)


class SecurityGroupRuleDirection(str, Enum, metaclass=StrEnumMeta):
    INBOUND = "inbound"
    OUTBOUND = "outbound"

    def __str__(self) -> str:
        return str(self.value)


class SecurityGroupRuleProtocol(str, Enum, metaclass=StrEnumMeta):
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
    FETCHING = "fetching"
    RESIZING = "resizing"
    SAVING = "saving"
    HOTSYNCING = "hotsyncing"
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
    RESIZING = "resizing"
    SAVING = "saving"
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

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class ServerSummary:
    name: str

    id: str


@dataclass
class Bootscript:
    zone: Zone
    """
    Zone in which the bootscript is located.
    """

    arch: Arch
    """
    Bootscript architecture.
    """

    title: str
    """
    Bootscript title.
    """

    public: bool
    """
    Provide information if the bootscript is public.
    """

    project: str
    """
    Bootscript Project ID.
    """

    organization: str
    """
    Bootscript Organization ID.
    """

    kernel: str
    """
    Instance kernel version.
    """

    initrd: str
    """
    Initrd (initial ramdisk) configuration.
    """

    id: str
    """
    Bootscript ID.
    """

    dtb: str
    """
    Provide information regarding a Device Tree Binary (DTB) for use with C1 servers.
    """

    default: bool
    """
    Display if the bootscript is the default bootscript (if no other boot option is configured).
    """

    bootcmdargs: str
    """
    Bootscript arguments.
    """


@dataclass
class Volume:
    project: str
    """
    Volume Project ID.
    """

    organization: str
    """
    Volume Organization ID.
    """

    server: ServerSummary
    """
    Instance attached to the volume.
    """

    state: VolumeState
    """
    Volume state.
    """

    volume_type: VolumeVolumeType
    """
    Volume type.
    """

    id: str
    """
    Volume unique ID.
    """

    zone: Zone
    """
    Zone in which the volume is located.
    """

    name: str
    """
    Volume name.
    """

    tags: List[str]
    """
    Volume tags.
    """

    size: int
    """
    Volume disk size.
    """

    modification_date: Optional[datetime]
    """
    Volume modification date.
    """

    creation_date: Optional[datetime]
    """
    Volume creation date.
    """

    export_uri: Optional[str]
    """
    Show the volume NBD export URI.
    """


@dataclass
class VolumeSummary:
    volume_type: VolumeVolumeType

    size: int

    name: str

    id: str


@dataclass
class ServerTypeNetworkInterface:
    internal_bandwidth: Optional[int]
    """
    Maximum internal bandwidth in bits per seconds.
    """

    internet_bandwidth: Optional[int]
    """
    Maximum internet bandwidth in bits per seconds.
    """


@dataclass
class ServerTypeVolumeConstraintSizes:
    max_size: int
    """
    Maximum volume size in bytes.
    """

    min_size: int
    """
    Minimum volume size in bytes.
    """


@dataclass
class Image:
    root_volume: VolumeSummary

    public: bool

    organization: str

    from_server: str

    id: str

    project: str

    tags: List[str]

    zone: Zone
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    arch: Arch

    name: str

    state: ImageState

    extra_volumes: Dict[str, Volume]

    default_bootscript: Optional[Bootscript]

    modification_date: Optional[datetime]

    creation_date: Optional[datetime]


@dataclass
class PlacementGroup:
    zone: Zone
    """
    Zone in which the placement group is located.
    """

    policy_respected: bool
    """
    Returns true if the policy is respected, false otherwise.
    """

    policy_type: PlacementGroupPolicyType
    """
    Select the behavior of the placement group, either low_latency (group) or max_availability (spread).
    """

    policy_mode: PlacementGroupPolicyMode
    """
    Select the failure mode when the placement cannot be respected, either optional or enforced.
    """

    tags: List[str]
    """
    Placement group tags.
    """

    project: str
    """
    Placement group Project ID.
    """

    organization: str
    """
    Placement group Organization ID.
    """

    name: str
    """
    Placement group name.
    """

    id: str
    """
    Placement group unique ID.
    """


@dataclass
class PrivateNIC:
    tags: List[str]
    """
    Private NIC tags.
    """

    state: PrivateNICState
    """
    Private NIC state.
    """

    mac_address: str
    """
    Private NIC MAC address.
    """

    private_network_id: str
    """
    Private Network the private NIC is attached to.
    """

    server_id: str
    """
    Instance to which the private NIC is attached.
    """

    id: str
    """
    Private NIC unique ID.
    """


@dataclass
class SecurityGroupSummary:
    name: str

    id: str


@dataclass
class ServerIp:
    provisioning_mode: ServerIpProvisioningMode
    """
    Information about this address provisioning mode.
    """

    dynamic: bool
    """
    True if the IP address is dynamic.
    """

    family: ServerIpIpFamily
    """
    IP address family (inet or inet6).
    """

    netmask: str
    """
    CIDR netmask.
    """

    gateway: str
    """
    Gateway's IP address.
    """

    address: str
    """
    Instance's public IP-Address.
    """

    id: str
    """
    Unique ID of the IP address.
    """


@dataclass
class ServerIpv6:
    netmask: str
    """
    IPv6 IP-addresses CIDR netmask.
    """

    gateway: str
    """
    IPv6 IP-addresses gateway.
    """

    address: str
    """
    Instance IPv6 IP-Address.
    """


@dataclass
class ServerLocation:
    zone_id: str

    platform_id: str

    node_id: str

    hypervisor_id: str

    cluster_id: str


@dataclass
class ServerMaintenance:
    reason: str


@dataclass
class VolumeServer:
    state: VolumeServerState

    boot: bool

    zone: Zone
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    id: str

    size: int

    server: ServerSummary

    organization: str

    export_uri: str

    name: str

    project: str

    volume_type: VolumeServerVolumeType

    modification_date: Optional[datetime]

    creation_date: Optional[datetime]


@dataclass
class SnapshotBaseVolume:
    name: str
    """
    Volume name on which the snapshot is based on.
    """

    id: str
    """
    Volume ID on which the snapshot is based.
    """


@dataclass
class ServerTypeCapabilities:
    boot_types: List[BootType]
    """
    List of supported boot types.
    """

    block_storage: Optional[bool]
    """
    Defines whether the Instance supports block storage.
    """


@dataclass
class ServerTypeNetwork:
    ipv6_support: bool
    """
    True if IPv6 is enabled.
    """

    interfaces: List[ServerTypeNetworkInterface]
    """
    List of available network interfaces.
    """

    sum_internal_bandwidth: Optional[int]
    """
    Total maximum internal bandwidth in bits per seconds.
    """

    sum_internet_bandwidth: Optional[int]
    """
    Total maximum internet bandwidth in bits per seconds.
    """


@dataclass
class ServerTypeVolumeConstraintsByType:
    l_ssd: ServerTypeVolumeConstraintSizes
    """
    Local SSD volumes.
    """


@dataclass
class VolumeTypeCapabilities:
    snapshot: bool


@dataclass
class VolumeTypeConstraints:
    max: int

    min: int


@dataclass
class VolumeTemplate:
    volume_type: VolumeVolumeType
    """
    Type of the volume.
    """

    size: int
    """
    Disk size of the volume, must be a multiple of 512.
    """

    name: str
    """
    Name of the volume.
    """

    id: str
    """
    UUID of the volume.
    """

    organization: Optional[str]

    project: Optional[str]


@dataclass
class Ip:
    zone: Zone
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    prefix: str

    state: IpState

    type_: IpType

    project: str

    tags: List[str]

    organization: str

    server: ServerSummary

    address: str

    id: str

    reverse: Optional[str]


@dataclass
class SecurityGroup:
    state: SecurityGroupState
    """
    Security group state.
    """

    project_default: bool
    """
    True if it is your default security group for this Project ID.
    """

    zone: Zone
    """
    Zone in which the security group is located.
    """

    id: str
    """
    Security group unique ID.
    """

    project: str
    """
    Security group Project ID.
    """

    servers: List[ServerSummary]
    """
    List of Instances attached to this security group.
    """

    outbound_default_policy: SecurityGroupPolicy
    """
    Default outbound policy.
    """

    inbound_default_policy: SecurityGroupPolicy
    """
    Default inbound policy.
    """

    enable_default_security: bool
    """
    True if SMTP is blocked on IPv4 and IPv6. This feature is read only, please open a support ticket if you need to make it configurable.
    """

    description: str
    """
    Security group description.
    """

    name: str
    """
    Security group name.
    """

    stateful: bool
    """
    Defines whether the security group is stateful.
    """

    organization: str
    """
    Security group Organization ID.
    """

    tags: List[str]
    """
    Security group tags.
    """

    modification_date: Optional[datetime]
    """
    Security group modification date.
    """

    creation_date: Optional[datetime]
    """
    Security group creation date.
    """

    organization_default: Optional[bool]
    """
    True if it is your default security group for this Organization ID.
    """


@dataclass
class SecurityGroupRule:
    zone: Zone
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    editable: bool

    position: int

    ip_range: str

    action: SecurityGroupRuleAction

    direction: SecurityGroupRuleDirection

    protocol: SecurityGroupRuleProtocol

    id: str

    dest_port_from: Optional[int]

    dest_port_to: Optional[int]


@dataclass
class Server:
    placement_group: PlacementGroup
    """
    Instance placement group.
    """

    boot_type: BootType
    """
    Instance boot type.
    """

    allowed_actions: List[ServerAction]
    """
    List of allowed actions on the Instance.
    """

    id: str
    """
    Instance unique ID.
    """

    name: str
    """
    Instance name.
    """

    commercial_type: str
    """
    Instance commercial type (eg. GP1-M).
    """

    state: ServerState
    """
    Instance state.
    """

    routed_ip_enabled: bool
    """
    True to configure the instance so it uses the new routed IP mode.
    """

    zone: Zone
    """
    Zone in which the Instance is located.
    """

    tags: List[str]
    """
    Tags associated with the Instance.
    """

    public_ip: ServerIp
    """
    Information about the public IP.
    """

    maintenances: List[ServerMaintenance]
    """
    Instance planned maintenance.
    """

    dynamic_ip_required: bool
    """
    True if a dynamic IPv4 is required.
    """

    mac_address: str
    """
    The server's MAC address.
    """

    state_detail: str
    """
    Detailed information about the Instance state.
    """

    enable_ipv6: bool
    """
    True if IPv6 is enabled.
    """

    volumes: Dict[str, VolumeServer]
    """
    Instance volumes.
    """

    location: ServerLocation
    """
    Instance location.
    """

    organization: str
    """
    Instance Organization ID.
    """

    private_nics: List[PrivateNIC]
    """
    Instance private NICs.
    """

    arch: Arch
    """
    Instance architecture.
    """

    ipv6: ServerIpv6
    """
    Instance IPv6 address.
    """

    protected: bool
    """
    Defines whether the Instance protection option is activated.
    """

    project: str
    """
    Instance Project ID.
    """

    hostname: str
    """
    Instance host name.
    """

    security_group: SecurityGroupSummary
    """
    Instance security group.
    """

    image: Image
    """
    Information about the Instance image.
    """

    public_ips: List[ServerIp]
    """
    Information about all the public IPs attached to the server.
    """

    bootscript: Optional[Bootscript]
    """
    Instance bootscript.
    """

    modification_date: Optional[datetime]
    """
    Instance modification date.
    """

    private_ip: Optional[str]
    """
    Private IP address of the Instance.
    """

    creation_date: Optional[datetime]
    """
    Instance creation date.
    """


@dataclass
class Snapshot:
    base_volume: SnapshotBaseVolume
    """
    Volume on which the snapshot is based on.
    """

    state: SnapshotState
    """
    Snapshot state.
    """

    id: str
    """
    Snapshot ID.
    """

    volume_type: VolumeVolumeType
    """
    Snapshot volume type.
    """

    tags: List[str]
    """
    Snapshot tags.
    """

    project: str
    """
    Snapshot Project ID.
    """

    organization: str
    """
    Snapshot Organization ID.
    """

    name: str
    """
    Snapshot name.
    """

    zone: Zone
    """
    Snapshot zone.
    """

    size: int
    """
    Snapshot size.
    """

    modification_date: Optional[datetime]
    """
    Snapshot modification date.
    """

    creation_date: Optional[datetime]
    """
    Snapshot creation date.
    """

    error_reason: Optional[str]
    """
    Reason for the failed snapshot import.
    """


@dataclass
class Task:
    zone: Zone
    """
    Zone in which the task is excecuted.
    """

    href_result: str

    href_from: str

    status: TaskStatus
    """
    Task status.
    """

    progress: int
    """
    Progress of the task in percent.
    """

    description: str
    """
    Description of the task.
    """

    id: str
    """
    Unique ID of the task.
    """

    started_at: Optional[datetime]
    """
    Task start date.
    """

    terminated_at: Optional[datetime]
    """
    Task end date.
    """


@dataclass
class Dashboard:
    volumes_l_ssd_total_size: int

    volumes_b_ssd_count: int

    volumes_l_ssd_count: int

    ips_unused: int

    security_groups_count: int

    private_nics_count: int

    servers_count: int

    snapshots_count: int

    images_count: int

    servers_by_types: Dict[str, int]

    running_servers_count: int

    volumes_b_ssd_total_size: int

    placement_groups_count: int

    volumes_count: int

    ips_count: int


@dataclass
class PlacementGroupServer:
    policy_respected: bool
    """
    Defines whether the placement group policy is respected (either 1 or 0).
    """

    name: str
    """
    Instance name.
    """

    id: str
    """
    Instance UUID.
    """


@dataclass
class GetServerTypesAvailabilityResponseAvailability:
    availability: ServerTypesAvailability


@dataclass
class ServerType:
    arch: Arch
    """
    CPU architecture.
    """

    ram: int
    """
    Available RAM in bytes.
    """

    network: ServerTypeNetwork
    """
    Network available for the Instance.
    """

    ncpus: int
    """
    Number of CPU.
    """

    volumes_constraint: ServerTypeVolumeConstraintSizes
    """
    Initial volume constraints.
    """

    capabilities: ServerTypeCapabilities
    """
    Capabilities.
    """

    alt_names: List[str]
    """
    Alternative Instance name, if any.
    """

    hourly_price: float
    """
    Hourly price in Euro.
    """

    baremetal: bool
    """
    True if it is a baremetal Instance.
    """

    per_volume_constraint: ServerTypeVolumeConstraintsByType
    """
    Additional volume constraints.
    """

    gpu: Optional[int]
    """
    Number of GPU.
    """

    monthly_price: Optional[float]
    """
    Estimated monthly price, for a 30 days month, in Euro.
    """

    scratch_storage_max_size: Optional[int]
    """
    Maximum available scratch storage.
    """


@dataclass
class VolumeType:
    constraints: VolumeTypeConstraints

    capabilities: VolumeTypeCapabilities

    display_name: str


@dataclass
class ServerActionRequestVolumeBackupTemplate:
    volume_type: SnapshotVolumeType
    """
    Overrides the `volume_type` of the snapshot for this volume.
If omitted, the volume type of the original volume will be used.
    """


@dataclass
class SetSecurityGroupRulesRequestRule:
    position: int
    """
    Position of this rule in the security group rules list. If several rules are passed with the same position, the resulting order is undefined.
    """

    ip_range: str
    """
    Range of IP addresses these rules apply to.
    """

    direction: SecurityGroupRuleDirection
    """
    Direction the rule applies to.
    """

    protocol: SecurityGroupRuleProtocol
    """
    Protocol family this rule applies to.
    """

    action: SecurityGroupRuleAction
    """
    Action to apply when the rule matches a packet.
    """

    id: Optional[str]
    """
    UUID of the security rule to update. If no value is provided, a new rule will be created.
    """

    dest_port_from: Optional[int]
    """
    Beginning of the range of ports this rule applies to (inclusive). This value will be set to null if protocol is ICMP or ANY.
    """

    dest_port_to: Optional[int]
    """
    End of the range of ports this rule applies to (inclusive). This value will be set to null if protocol is ICMP or ANY, or if it is equal to dest_port_from.
    """

    editable: Optional[bool]
    """
    Indicates if this rule is editable. Rules with the value false will be ignored.
    """

    zone: Optional[Zone]
    """
    Zone of the rule. This field is ignored.
    """


@dataclass
class VolumeServerTemplate:
    volume_type: VolumeVolumeType
    """
    Type of the volume.
    """

    id: Optional[str]
    """
    UUID of the volume.
    """

    boot: Optional[bool]
    """
    Force the Instance to boot on this volume.
    """

    name: Optional[str]
    """
    Name of the volume.
    """

    size: Optional[int]
    """
    Disk size of the volume, must be a multiple of 512.
    """

    base_snapshot: Optional[str]
    """
    ID of the snapshot on which this volume will be based.
    """

    organization: Optional[str]
    """
    Organization ID of the volume.
    """

    project: Optional[str]
    """
    Project ID of the volume.
    """


@dataclass
class SecurityGroupTemplate:
    name: str

    id: str


@dataclass
class ApplyBlockMigrationRequest:
    validation_key: str
    """
    A value to be retrieved from a call to PlanBlockMigration, to confirm that the volume and/or snapshots specified in said plan should be migrated.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_id: Optional[str]

    snapshot_id: Optional[str]


@dataclass
class CreateImageRequest:
    extra_volumes: Dict[str, VolumeTemplate]
    """
    Additional volumes of the image.
    """

    root_volume: str
    """
    UUID of the snapshot.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name of the image.
    """

    arch: Optional[Arch]
    """
    Architecture of the image.
    """

    default_bootscript: Optional[str]
    """
    Default bootscript of the image.
    """

    tags: Optional[List[str]]
    """
    Tags of the image.
    """

    public: Optional[bool]
    """
    True to create a public image.
    """

    organization: Optional[str]

    project: Optional[str]


@dataclass
class CreateImageResponse:
    image: Image


@dataclass
class CreateIpRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[List[str]]
    """
    Tags of the IP.
    """

    server: Optional[str]
    """
    UUID of the Instance you want to attach the IP to.
    """

    type_: Optional[IpType]
    """
    IP type to reserve (either 'nat', 'routed_ipv4' or 'routed_ipv6').
    """

    organization: Optional[str]

    project: Optional[str]


@dataclass
class CreateIpResponse:
    ip: Ip


@dataclass
class CreatePlacementGroupRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name of the placement group.
    """

    tags: Optional[List[str]]
    """
    Tags of the placement group.
    """

    policy_mode: Optional[PlacementGroupPolicyMode]
    """
    Operating mode of the placement group.
    """

    policy_type: Optional[PlacementGroupPolicyType]
    """
    Policy type of the placement group.
    """

    organization: Optional[str]

    project: Optional[str]


@dataclass
class CreatePlacementGroupResponse:
    placement_group: PlacementGroup


@dataclass
class CreatePrivateNICRequest:
    private_network_id: str
    """
    UUID of the private network where the private NIC will be attached.
    """

    server_id: str
    """
    UUID of the Instance the private NIC will be attached to.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[List[str]]
    """
    Private NIC tags.
    """

    ip_ids: Optional[List[str]]
    """
    Ip_ids defined from IPAM.
    """


@dataclass
class CreatePrivateNICResponse:
    private_nic: PrivateNIC


@dataclass
class CreateSecurityGroupRequest:
    stateful: bool
    """
    Whether the security group is stateful or not.
    """

    description: str
    """
    Description of the security group.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name of the security group.
    """

    tags: Optional[List[str]]
    """
    Tags of the security group.
    """

    inbound_default_policy: Optional[SecurityGroupPolicy]
    """
    Default policy for inbound rules.
    """

    outbound_default_policy: Optional[SecurityGroupPolicy]
    """
    Default policy for outbound rules.
    """

    enable_default_security: Optional[bool]
    """
    True to block SMTP on IPv4 and IPv6. This feature is read only, please open a support ticket if you need to make it configurable.
    """

    organization: Optional[str]

    project: Optional[str]

    organization_default: Optional[bool]

    project_default: Optional[bool]


@dataclass
class CreateSecurityGroupResponse:
    security_group: SecurityGroup


@dataclass
class CreateSecurityGroupRuleRequest:
    editable: bool
    """
    Indicates if this rule is editable (will be ignored).
    """

    position: int
    """
    Position of this rule in the security group rules list.
    """

    ip_range: str

    security_group_id: str
    """
    UUID of the security group.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    protocol: Optional[SecurityGroupRuleProtocol]

    direction: Optional[SecurityGroupRuleDirection]

    action: Optional[SecurityGroupRuleAction]

    dest_port_from: Optional[int]
    """
    Beginning of the range of ports to apply this rule to (inclusive).
    """

    dest_port_to: Optional[int]
    """
    End of the range of ports to apply this rule to (inclusive).
    """


@dataclass
class CreateSecurityGroupRuleResponse:
    rule: SecurityGroupRule


@dataclass
class CreateServerResponse:
    server: Server


@dataclass
class CreateSnapshotRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name of the snapshot.
    """

    volume_id: Optional[str]
    """
    UUID of the volume.
    """

    tags: Optional[List[str]]
    """
    Tags of the snapshot.
    """

    volume_type: Optional[SnapshotVolumeType]
    """
    Overrides the volume_type of the snapshot.
If omitted, the volume type of the original volume will be used.
    """

    bucket: Optional[str]
    """
    Bucket name for snapshot imports.
    """

    key: Optional[str]
    """
    Object key for snapshot imports.
    """

    size: Optional[int]
    """
    Imported snapshot size, must be a multiple of 512.
    """

    organization: Optional[str]

    project: Optional[str]


@dataclass
class CreateSnapshotResponse:
    task: Task

    snapshot: Snapshot


@dataclass
class CreateVolumeRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Volume name.
    """

    tags: Optional[List[str]]
    """
    Volume tags.
    """

    volume_type: Optional[VolumeVolumeType]
    """
    Volume type.
    """

    organization: Optional[str]

    project: Optional[str]

    size: Optional[int]

    base_volume: Optional[str]

    base_snapshot: Optional[str]


@dataclass
class CreateVolumeResponse:
    volume: Volume


@dataclass
class DeleteImageRequest:
    image_id: str
    """
    UUID of the image you want to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteIpRequest:
    ip: str
    """
    ID or address of the IP to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeletePlacementGroupRequest:
    placement_group_id: str
    """
    UUID of the placement group you want to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeletePrivateNICRequest:
    private_nic_id: str
    """
    Private NIC unique ID.
    """

    server_id: str
    """
    Instance to which the private NIC is attached.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteSecurityGroupRequest:
    security_group_id: str
    """
    UUID of the security group you want to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteSecurityGroupRuleRequest:
    security_group_rule_id: str

    security_group_id: str

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteServerRequest:
    server_id: str

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteServerUserDataRequest:
    key: str
    """
    Key of the user data to delete.
    """

    server_id: str
    """
    UUID of the Instance.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteSnapshotRequest:
    snapshot_id: str
    """
    UUID of the snapshot you want to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteVolumeRequest:
    volume_id: str
    """
    UUID of the volume you want to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ExportSnapshotRequest:
    key: str
    """
    S3 object key.
    """

    bucket: str
    """
    S3 bucket name.
    """

    snapshot_id: str
    """
    Snapshot ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ExportSnapshotResponse:
    task: Task


@dataclass
class GetBootscriptRequest:
    bootscript_id: str

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetBootscriptResponse:
    bootscript: Bootscript


@dataclass
class GetDashboardRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    organization: Optional[str]

    project: Optional[str]


@dataclass
class GetDashboardResponse:
    dashboard: Dashboard


@dataclass
class GetImageRequest:
    image_id: str
    """
    UUID of the image you want to get.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetImageResponse:
    image: Image


@dataclass
class GetIpRequest:
    ip: str
    """
    IP ID or address to get.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetIpResponse:
    ip: Ip


@dataclass
class GetPlacementGroupRequest:
    placement_group_id: str
    """
    UUID of the placement group you want to get.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetPlacementGroupResponse:
    placement_group: PlacementGroup


@dataclass
class GetPlacementGroupServersRequest:
    placement_group_id: str
    """
    UUID of the placement group you want to get.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetPlacementGroupServersResponse:
    servers: List[PlacementGroupServer]
    """
    Instances attached to the placement group.
    """


@dataclass
class GetPrivateNICRequest:
    private_nic_id: str
    """
    Private NIC unique ID.
    """

    server_id: str
    """
    Instance to which the private NIC is attached.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetPrivateNICResponse:
    private_nic: PrivateNIC


@dataclass
class GetSecurityGroupRequest:
    security_group_id: str
    """
    UUID of the security group you want to get.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetSecurityGroupResponse:
    security_group: SecurityGroup


@dataclass
class GetSecurityGroupRuleRequest:
    security_group_rule_id: str

    security_group_id: str

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetSecurityGroupRuleResponse:
    rule: SecurityGroupRule


@dataclass
class GetServerRequest:
    server_id: str
    """
    UUID of the Instance you want to get.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerResponse:
    server: Server


@dataclass
class GetServerTypesAvailabilityRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    per_page: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to return.
    """

    page: Optional[int]
    """
    A positive integer to choose the page to return.
    """


@dataclass
class GetServerTypesAvailabilityResponse:
    total_count: int

    servers: Dict[str, GetServerTypesAvailabilityResponseAvailability]
    """
    Map of server types.
    """


@dataclass
class GetSnapshotRequest:
    snapshot_id: str
    """
    UUID of the snapshot you want to get.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetSnapshotResponse:
    snapshot: Snapshot


@dataclass
class GetVolumeRequest:
    volume_id: str
    """
    UUID of the volume you want to get.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetVolumeResponse:
    volume: Volume


@dataclass
class ListBootscriptsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    arch: Optional[str]

    title: Optional[str]

    default: Optional[bool]

    public: Optional[bool]

    per_page: Optional[int]

    page: Optional[int]


@dataclass
class ListBootscriptsResponse:
    bootscripts: List[Bootscript]
    """
    List of bootscripts.
    """

    total_count: int
    """
    Total number of bootscripts.
    """


@dataclass
class ListDefaultSecurityGroupRulesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListImagesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    organization: Optional[str]

    per_page: Optional[int]

    page: Optional[int]

    name: Optional[str]

    public: Optional[bool]

    arch: Optional[str]

    project: Optional[str]

    tags: Optional[str]


@dataclass
class ListImagesResponse:
    images: List[Image]
    """
    List of images.
    """

    total_count: int
    """
    Total number of images.
    """


@dataclass
class ListIpsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project: Optional[str]
    """
    Project ID in which the IPs are reserved.
    """

    organization: Optional[str]
    """
    Organization ID in which the IPs are reserved.
    """

    tags: Optional[List[str]]
    """
    Filter IPs with these exact tags (to filter with several tags, use commas to separate them).
    """

    name: Optional[str]
    """
    Filter on the IP address (Works as a LIKE operation on the IP address).
    """

    per_page: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to return.
    """

    page: Optional[int]
    """
    A positive integer to choose the page to return.
    """

    type_: Optional[str]
    """
    Filter on the IP Mobility IP type (whose value should be either 'nat', 'routed_ipv4' or 'routed_ipv6').
    """


@dataclass
class ListIpsResponse:
    ips: List[Ip]
    """
    List of ips.
    """

    total_count: int
    """
    Total number of ips.
    """


@dataclass
class ListPlacementGroupsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    per_page: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to return.
    """

    page: Optional[int]
    """
    A positive integer to choose the page to return.
    """

    organization: Optional[str]
    """
    List only placement groups of this Organization ID.
    """

    project: Optional[str]
    """
    List only placement groups of this Project ID.
    """

    tags: Optional[List[str]]
    """
    List placement groups with these exact tags (to filter with several tags, use commas to separate them).
    """

    name: Optional[str]
    """
    Filter placement groups by name (for eg. "cluster1" will return "cluster100" and "cluster1" but not "foo").
    """


@dataclass
class ListPlacementGroupsResponse:
    placement_groups: List[PlacementGroup]
    """
    List of placement groups.
    """

    total_count: int
    """
    Total number of placement groups.
    """


@dataclass
class ListPrivateNICsRequest:
    server_id: str
    """
    Instance to which the private NIC is attached.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[List[str]]
    """
    Private NIC tags.
    """

    per_page: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to return.
    """

    page: Optional[int]
    """
    A positive integer to choose the page to return.
    """


@dataclass
class ListPrivateNICsResponse:
    total_count: int

    private_nics: List[PrivateNIC]


@dataclass
class ListSecurityGroupRulesRequest:
    security_group_id: str
    """
    UUID of the security group.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    per_page: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to return.
    """

    page: Optional[int]
    """
    A positive integer to choose the page to return.
    """


@dataclass
class ListSecurityGroupRulesResponse:
    rules: List[SecurityGroupRule]
    """
    List of security rules.
    """

    total_count: int
    """
    Total number of security groups.
    """


@dataclass
class ListSecurityGroupsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name of the security group.
    """

    organization: Optional[str]
    """
    Security group Organization ID.
    """

    project: Optional[str]
    """
    Security group Project ID.
    """

    tags: Optional[List[str]]
    """
    List security groups with these exact tags (to filter with several tags, use commas to separate them).
    """

    project_default: Optional[bool]
    """
    Filter security groups with this value for project_default.
    """

    per_page: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to return.
    """

    page: Optional[int]
    """
    A positive integer to choose the page to return.
    """


@dataclass
class ListSecurityGroupsResponse:
    security_groups: List[SecurityGroup]
    """
    List of security groups.
    """

    total_count: int
    """
    Total number of security groups.
    """


@dataclass
class ListServerActionsRequest:
    server_id: str

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListServerActionsResponse:
    actions: List[ServerAction]


@dataclass
class ListServerUserDataRequest:
    server_id: str
    """
    UUID of the Instance.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListServerUserDataResponse:
    user_data: List[str]


@dataclass
class ListServersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    per_page: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to return.
    """

    page: Optional[int]
    """
    A positive integer to choose the page to return.
    """

    organization: Optional[str]
    """
    List only Instances of this Organization ID.
    """

    project: Optional[str]
    """
    List only Instances of this Project ID.
    """

    name: Optional[str]
    """
    Filter Instances by name (eg. "server1" will return "server100" and "server1" but not "foo").
    """

    private_ip: Optional[str]
    """
    List Instances by private_ip.
    """

    without_ip: Optional[bool]
    """
    List Instances that are not attached to a public IP.
    """

    commercial_type: Optional[str]
    """
    List Instances of this commercial type.
    """

    state: Optional[ServerState]
    """
    List Instances in this state.
    """

    tags: Optional[List[str]]
    """
    List Instances with these exact tags (to filter with several tags, use commas to separate them).
    """

    private_network: Optional[str]
    """
    List Instances in this Private Network.
    """

    order: Optional[ListServersRequestOrder]
    """
    Define the order of the returned servers.
    """

    private_networks: Optional[List[str]]
    """
    List Instances from the given Private Networks (use commas to separate them).
    """

    private_nic_mac_address: Optional[str]
    """
    List Instances associated with the given private NIC MAC address.
    """

    servers: Optional[List[str]]
    """
    List Instances from these server ids (use commas to separate them).
    """


@dataclass
class ListServersResponse:
    servers: List[Server]
    """
    List of Instances.
    """

    total_count: int
    """
    Total number of Instances.
    """


@dataclass
class ListServersTypesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    per_page: Optional[int]

    page: Optional[int]


@dataclass
class ListServersTypesResponse:
    servers: Dict[str, ServerType]
    """
    List of Instance types.
    """

    total_count: int
    """
    Total number of Instance types.
    """


@dataclass
class ListSnapshotsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    organization: Optional[str]
    """
    List snapshots only for this Organization ID.
    """

    project: Optional[str]
    """
    List snapshots only for this Project ID.
    """

    per_page: Optional[int]
    """
    Number of snapshots returned per page (positive integer lower or equal to 100).
    """

    page: Optional[int]
    """
    Page to be returned.
    """

    name: Optional[str]
    """
    List snapshots of the requested name.
    """

    tags: Optional[str]
    """
    List snapshots that have the requested tag.
    """

    base_volume_id: Optional[str]
    """
    List snapshots originating only from this volume.
    """


@dataclass
class ListSnapshotsResponse:
    snapshots: List[Snapshot]
    """
    List of snapshots.
    """

    total_count: int
    """
    Total number of snapshots.
    """


@dataclass
class ListVolumesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_type: Optional[VolumeVolumeType]
    """
    Filter by volume type.
    """

    per_page: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to return.
    """

    page: Optional[int]
    """
    A positive integer to choose the page to return.
    """

    organization: Optional[str]
    """
    Filter volume by Organization ID.
    """

    project: Optional[str]
    """
    Filter volume by Project ID.
    """

    tags: Optional[List[str]]
    """
    Filter volumes with these exact tags (to filter with several tags, use commas to separate them).
    """

    name: Optional[str]
    """
    Filter volume by name (for eg. "vol" will return "myvolume" but not "data").
    """


@dataclass
class ListVolumesResponse:
    volumes: List[Volume]
    """
    List of volumes.
    """

    total_count: int
    """
    Total number of volumes.
    """


@dataclass
class ListVolumesTypesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    per_page: Optional[int]

    page: Optional[int]


@dataclass
class ListVolumesTypesResponse:
    volumes: Dict[str, VolumeType]
    """
    Map of volume types.
    """

    total_count: int
    """
    Total number of volume types.
    """


@dataclass
class MigrationPlan:
    validation_key: str
    """
    A value to be passed to ApplyBlockMigrationRequest, to confirm that the execution of the plan is being requested.
    """

    snapshots: List[Snapshot]
    """
    A list of snapshots which will be migrated to SBS together and with the volume, if present.
    """

    volume: Volume
    """
    A volume which will be migrated to SBS together with the snapshots, if present.
    """


@dataclass
class PlanBlockMigrationRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_id: Optional[str]

    snapshot_id: Optional[str]


@dataclass
class ServerActionRequest:
    volumes: Dict[str, ServerActionRequestVolumeBackupTemplate]
    """
    For each volume UUID, the snapshot parameters of the volume.
This field should only be specified when performing a backup action.
    """

    server_id: str
    """
    UUID of the Instance.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    action: Optional[ServerAction]
    """
    Action to perform on the Instance.
    """

    name: Optional[str]
    """
    Name of the backup you want to create.
This field should only be specified when performing a backup action.
    """


@dataclass
class ServerActionResponse:
    task: Task


@dataclass
class SetPlacementGroupRequest:
    name: str

    placement_group_id: str

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    organization: Optional[str]

    policy_mode: Optional[PlacementGroupPolicyMode]

    policy_type: Optional[PlacementGroupPolicyType]

    project: Optional[str]

    tags: Optional[List[str]]


@dataclass
class SetPlacementGroupResponse:
    placement_group: PlacementGroup


@dataclass
class SetPlacementGroupServersRequest:
    placement_group_id: str
    """
    UUID of the placement group you want to set.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    servers: Optional[List[str]]
    """
    An array of the Instances' UUIDs you want to configure.
    """


@dataclass
class SetPlacementGroupServersResponse:
    servers: List[PlacementGroupServer]
    """
    Instances attached to the placement group.
    """


@dataclass
class SetSecurityGroupRulesRequest:
    security_group_id: str
    """
    UUID of the security group to update the rules on.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    rules: Optional[List[SetSecurityGroupRulesRequestRule]]
    """
    List of rules to update in the security group.
    """


@dataclass
class SetSecurityGroupRulesResponse:
    rules: List[SecurityGroupRule]


@dataclass
class UpdateIpRequest:
    ip: str
    """
    IP ID or IP address.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    reverse: Optional[str]
    """
    Reverse domain name.
    """

    type_: Optional[IpType]
    """
    Convert a 'nat' IP to a 'routed_ipv4'.
    """

    tags: Optional[List[str]]
    """
    An array of keywords you want to tag this IP with.
    """

    server: Optional[str]


@dataclass
class UpdateIpResponse:
    ip: Ip


@dataclass
class UpdatePlacementGroupRequest:
    placement_group_id: str
    """
    UUID of the placement group.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name of the placement group.
    """

    tags: Optional[List[str]]
    """
    Tags of the placement group.
    """

    policy_mode: Optional[PlacementGroupPolicyMode]
    """
    Operating mode of the placement group.
    """

    policy_type: Optional[PlacementGroupPolicyType]
    """
    Policy type of the placement group.
    """


@dataclass
class UpdatePlacementGroupResponse:
    placement_group: PlacementGroup


@dataclass
class UpdatePlacementGroupServersRequest:
    placement_group_id: str
    """
    UUID of the placement group you want to update.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    servers: Optional[List[str]]
    """
    An array of the Instances' UUIDs you want to configure.
    """


@dataclass
class UpdatePlacementGroupServersResponse:
    servers: List[PlacementGroupServer]
    """
    Instances attached to the placement group.
    """


@dataclass
class UpdatePrivateNICRequest:
    private_nic_id: str
    """
    Private NIC unique ID.
    """

    server_id: str
    """
    UUID of the Instance the private NIC will be attached to.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[List[str]]
    """
    Tags used to select private NIC/s.
    """


@dataclass
class UpdateServerResponse:
    server: Server


@dataclass
class UpdateVolumeRequest:
    volume_id: str
    """
    UUID of the volume.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Volume name.
    """

    tags: Optional[List[str]]
    """
    Tags of the volume.
    """

    size: Optional[int]
    """
    Volume disk size, must be a multiple of 512.
    """


@dataclass
class UpdateVolumeResponse:
    volume: Volume


@dataclass
class _CreateServerRequest:
    commercial_type: str
    """
    Define the Instance commercial type (i.e. GP1-S).
    """

    volumes: Dict[str, VolumeServerTemplate]
    """
    Volumes attached to the server.
    """

    enable_ipv6: bool
    """
    True if IPv6 is enabled on the server.
    """

    image: str
    """
    Instance image ID or label.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    routed_ip_enabled: Optional[bool]
    """
    If true, configure the Instance so it uses the new routed IP mode.
    """

    dynamic_ip_required: Optional[bool]
    """
    Define if a dynamic IPv4 is required for the Instance.
    """

    name: Optional[str]
    """
    Instance name.
    """

    public_ip: Optional[str]
    """
    ID of the reserved IP to attach to the Instance.
    """

    public_ips: Optional[List[str]]
    """
    A list of reserved IP IDs to attach to the Instance.
    """

    boot_type: Optional[BootType]
    """
    Boot type to use.
    """

    bootscript: Optional[str]
    """
    Bootscript ID to use when `boot_type` is set to `bootscript`.
    """

    tags: Optional[List[str]]
    """
    Instance tags.
    """

    security_group: Optional[str]
    """
    Security group ID.
    """

    placement_group: Optional[str]
    """
    Placement group ID if Instance must be part of a placement group.
    """

    organization: Optional[str]

    project: Optional[str]


@dataclass
class _SetImageRequest:
    from_server: str

    public: bool

    root_volume: VolumeSummary

    name: str

    id: str

    extra_volumes: Dict[str, Volume]

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    default_bootscript: Optional[Bootscript]

    modification_date: Optional[datetime]

    organization: Optional[str]

    creation_date: Optional[datetime]

    arch: Optional[Arch]

    state: Optional[ImageState]

    project: Optional[str]

    tags: Optional[List[str]]


@dataclass
class _SetImageResponse:
    image: Image


@dataclass
class _SetSecurityGroupRequest:
    description: str
    """
    Description of the security group.
    """

    project_default: bool
    """
    True use this security group for future Instances created in this project.
    """

    stateful: bool
    """
    True to set the security group as stateful.
    """

    name: str
    """
    Name of the security group.
    """

    id: str
    """
    ID of the security group (will be ignored).
    """

    enable_default_security: bool
    """
    True to block SMTP on IPv4 and IPv6. This feature is read only, please open a support ticket if you need to make it configurable.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    inbound_default_policy: Optional[SecurityGroupPolicy]
    """
    Default inbound policy.
    """

    modification_date: Optional[datetime]
    """
    Modification date of the security group (will be ignored).
    """

    outbound_default_policy: Optional[SecurityGroupPolicy]
    """
    Default outbound policy.
    """

    organization: Optional[str]
    """
    Security groups Organization ID.
    """

    project: Optional[str]
    """
    Security group Project ID.
    """

    organization_default: Optional[bool]
    """
    Please use project_default instead.
    """

    creation_date: Optional[datetime]
    """
    Creation date of the security group (will be ignored).
    """

    servers: Optional[List[ServerSummary]]
    """
    Instances attached to this security group.
    """

    tags: Optional[List[str]]
    """
    Tags of the security group.
    """


@dataclass
class _SetSecurityGroupResponse:
    security_group: SecurityGroup


@dataclass
class _SetSecurityGroupRuleRequest:
    editable: bool

    position: int

    ip_range: str

    id: str

    security_group_rule_id: str

    security_group_id: str

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    protocol: Optional[SecurityGroupRuleProtocol]

    direction: Optional[SecurityGroupRuleDirection]

    action: Optional[SecurityGroupRuleAction]

    dest_port_from: Optional[int]

    dest_port_to: Optional[int]


@dataclass
class _SetSecurityGroupRuleResponse:
    rule: SecurityGroupRule


@dataclass
class _SetServerRequest:
    enable_ipv6: bool
    """
    True if IPv6 is enabled.
    """

    location: ServerLocation
    """
    Instance location.
    """

    dynamic_ip_required: bool
    """
    True if a dynamic IPv4 is required.
    """

    ipv6: ServerIpv6
    """
    Instance IPv6 address.
    """

    commercial_type: str
    """
    Instance commercial type (eg. GP1-M).
    """

    image: Image
    """
    Provide information on the Instance image.
    """

    security_group: SecurityGroupSummary
    """
    Instance security group.
    """

    state_detail: str
    """
    Instance state_detail.
    """

    placement_group: PlacementGroup
    """
    Instance placement group.
    """

    name: str
    """
    Instance name.
    """

    id: str
    """
    Instance unique ID.
    """

    hostname: str
    """
    Instance host name.
    """

    public_ip: ServerIp
    """
    Information about the public IP.
    """

    volumes: Dict[str, Volume]
    """
    Instance volumes.
    """

    protected: bool
    """
    Instance protection option is activated.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    boot_type: Optional[BootType]
    """
    Instance boot type.
    """

    tags: Optional[List[str]]
    """
    Tags associated with the Instance.
    """

    modification_date: Optional[datetime]
    """
    Instance modification date.
    """

    state: Optional[ServerState]
    """
    Instance state.
    """

    routed_ip_enabled: Optional[bool]
    """
    True to configure the instance so it uses the new routed IP mode (once this is set to True you cannot set it back to False).
    """

    creation_date: Optional[datetime]
    """
    Instance creation date.
    """

    public_ips: Optional[List[ServerIp]]
    """
    Information about all the public IPs attached to the server.
    """

    private_ip: Optional[str]
    """
    Instance private IP address.
    """

    bootscript: Optional[Bootscript]
    """
    Instance bootscript.
    """

    allowed_actions: Optional[List[ServerAction]]
    """
    Provide a list of allowed actions on the server.
    """

    maintenances: Optional[List[ServerMaintenance]]
    """
    Instance planned maintenances.
    """

    project: Optional[str]
    """
    Instance Project ID.
    """

    arch: Optional[Arch]
    """
    Instance architecture (refers to the CPU architecture used for the Instance, e.g. x86_64, arm64).
    """

    organization: Optional[str]
    """
    Instance Organization ID.
    """

    private_nics: Optional[List[PrivateNIC]]
    """
    Instance private NICs.
    """


@dataclass
class _SetServerResponse:
    server: Server


@dataclass
class _SetSnapshotRequest:
    name: str

    id: str

    snapshot_id: str

    base_volume: SnapshotBaseVolume

    size: int

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_type: Optional[VolumeVolumeType]

    state: Optional[SnapshotState]

    organization: Optional[str]

    creation_date: Optional[datetime]

    modification_date: Optional[datetime]

    project: Optional[str]

    tags: Optional[List[str]]


@dataclass
class _SetSnapshotResponse:
    snapshot: Snapshot


@dataclass
class _UpdateServerRequest:
    security_group: SecurityGroupTemplate

    server_id: str
    """
    UUID of the Instance.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[List[str]]
    """
    Tags of the Instance.
    """

    boot_type: Optional[BootType]

    volumes: Optional[Dict[str, VolumeServerTemplate]]

    bootscript: Optional[str]

    dynamic_ip_required: Optional[bool]

    routed_ip_enabled: Optional[bool]
    """
    True to configure the instance so it uses the new routed IP mode (once this is set to True you cannot set it back to False).
    """

    public_ips: Optional[List[ServerIp]]

    enable_ipv6: Optional[bool]

    protected: Optional[bool]

    name: Optional[str]
    """
    Name of the Instance.
    """

    placement_group: Optional[str]
    """
    Placement group ID if Instance must be part of a placement group.
    """

    private_nics: Optional[List[PrivateNIC]]
    """
    Instance private NICs.
    """

    commercial_type: Optional[str]
    """
    Warning: This field has some restrictions:
- Cannot be changed if the Instance is not in `stopped` state.
- Cannot be changed if the Instance is in a placement group.
- Local storage requirements of the target commercial_types must be fulfilled (i.e. if an Instance has 80GB of local storage, it can be changed into a GP1-XS, which has a maximum of 150GB, but it cannot be changed into a DEV1-S, which has only 20GB).
    """
