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
    SBS_SNAPSHOT = "sbs_snapshot"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class ServerSummary:
    id: str

    name: str


@dataclass
class Bootscript:
    bootcmdargs: str
    """
    Bootscript arguments.
    """

    default: bool
    """
    Display if the bootscript is the default bootscript (if no other boot option is configured).
    """

    dtb: str
    """
    Provide information regarding a Device Tree Binary (DTB) for use with C1 servers.
    """

    id: str
    """
    Bootscript ID.
    """

    initrd: str
    """
    Initrd (initial ramdisk) configuration.
    """

    kernel: str
    """
    Instance kernel version.
    """

    organization: str
    """
    Bootscript Organization ID.
    """

    project: str
    """
    Bootscript Project ID.
    """

    public: bool
    """
    Provide information if the bootscript is public.
    """

    title: str
    """
    Bootscript title.
    """

    architecture: Arch
    """
    Bootscript architecture.
    """

    zone: Zone
    """
    Zone in which the bootscript is located.
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

    export_uri: Optional[str]
    """
    Show the volume NBD export URI.
    """

    creation_date: Optional[datetime]
    """
    Volume creation date.
    """

    modification_date: Optional[datetime]
    """
    Volume modification date.
    """

    tags: List[str]
    """
    Volume tags.
    """

    state: VolumeState
    """
    Volume state.
    """

    zone: Zone
    """
    Zone in which the volume is located.
    """

    server: Optional[ServerSummary]
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

    extra_volumes: Dict[str, Volume]

    from_server: str

    organization: str

    creation_date: Optional[datetime]

    modification_date: Optional[datetime]

    default_bootscript: Optional[Bootscript]

    public: bool

    state: ImageState

    project: str

    tags: List[str]

    zone: Zone
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    root_volume: Optional[VolumeSummary]


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

    tags: List[str]
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
    Returns true if the policy is respected, false otherwise.
    """

    zone: Zone
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

    tags: List[str]
    """
    Private NIC tags.
    """


@dataclass
class SecurityGroupSummary:
    id: str

    name: str


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

    tags: List[str]
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

    start_date: Optional[datetime]


@dataclass
class VolumeServer:
    id: str

    name: str

    organization: str

    size: int

    export_uri: Optional[str]

    server: Optional[ServerSummary]

    volume_type: VolumeServerVolumeType

    state: VolumeServerState

    project: str

    boot: bool

    zone: Zone
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    creation_date: Optional[datetime]

    modification_date: Optional[datetime]


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
    interfaces: List[ServerTypeNetworkInterface]
    """
    List of available network interfaces.
    """

    ipv6_support: bool
    """
    True if IPv6 is enabled.
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
    l_ssd: Optional[ServerTypeVolumeConstraintSizes]
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

    allowed_actions: List[ServerAction]
    """
    List of allowed actions on the Instance.
    """

    tags: List[str]
    """
    Tags associated with the Instance.
    """

    commercial_type: str
    """
    Instance commercial type (eg. GP1-M).
    """

    creation_date: Optional[datetime]
    """
    Instance creation date.
    """

    dynamic_ip_required: bool
    """
    True if a dynamic IPv4 is required.
    """

    hostname: str
    """
    Instance host name.
    """

    protected: bool
    """
    Defines whether the Instance protection option is activated.
    """

    routed_ip_enabled: Optional[bool]
    """
    True to configure the instance so it uses the routed IP mode. Use of `routed_ip_enabled` as `False` is deprecated.
    """

    enable_ipv6: Optional[bool]
    """
    True if IPv6 is enabled (deprecated and always `False` when `routed_ip_enabled` is `True`).
    """

    image: Optional[Image]
    """
    Information about the Instance image.
    """

    private_ip: Optional[str]
    """
    Private IP address of the Instance (deprecated and always `null` when `routed_ip_enabled` is `True`).
    """

    public_ip: Optional[ServerIp]
    """
    Information about the public IP (deprecated in favor of `public_ips`).
    """

    public_ips: List[ServerIp]
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

    volumes: Dict[str, VolumeServer]
    """
    Instance volumes.
    """

    modification_date: Optional[datetime]
    """
    Instance modification date.
    """

    location: Optional[ServerLocation]
    """
    Instance location.
    """

    ipv6: Optional[ServerIpv6]
    """
    Instance IPv6 address (deprecated when `routed_ip_enabled` is `True`).
    """

    bootscript: Optional[Bootscript]
    """
    Instance bootscript.
    """

    maintenances: List[ServerMaintenance]
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

    private_nics: List[PrivateNIC]
    """
    Instance private NICs.
    """

    zone: Zone
    """
    Zone in which the Instance is located.
    """

    security_group: Optional[SecurityGroupSummary]
    """
    Instance security group.
    """

    placement_group: Optional[PlacementGroup]
    """
    Instance placement group.
    """

    admin_password_encryption_ssh_key_id: Optional[str]
    """
    The public_key value of this key is used to encrypt the admin password. When set to an empty string, reset this value and admin_password_encrypted_value to an empty string so a new password may be generated.
    """

    admin_password_encrypted_value: Optional[str]
    """
    This value is reset when admin_password_encryption_ssh_key_id is set to an empty string.
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

    project: Optional[str]

    organization: Optional[str]


@dataclass
class Ip:
    id: str

    address: str

    organization: str

    tags: List[str]

    project: str

    type_: IpType

    state: IpState

    prefix: str

    ipam_id: str

    zone: Zone
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    reverse: Optional[str]

    server: Optional[ServerSummary]


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

    tags: List[str]
    """
    Security group tags.
    """

    project_default: bool
    """
    True if it is your default security group for this Project ID.
    """

    servers: List[ServerSummary]
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

    zone: Zone
    """
    Zone in which the security group is located.
    """

    organization_default: Optional[bool]
    """
    True if it is your default security group for this Organization ID.
    """

    creation_date: Optional[datetime]
    """
    Security group creation date.
    """

    modification_date: Optional[datetime]
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

    zone: Zone
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    dest_port_from: Optional[int]

    dest_port_to: Optional[int]


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

    tags: List[str]
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

    zone: Zone
    """
    Snapshot zone.
    """

    base_volume: Optional[SnapshotBaseVolume]
    """
    Volume on which the snapshot is based on.
    """

    creation_date: Optional[datetime]
    """
    Snapshot creation date.
    """

    modification_date: Optional[datetime]
    """
    Snapshot modification date.
    """

    error_reason: Optional[str]
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

    zone: Zone
    """
    Zone in which the task is excecuted.
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
    volumes_count: int

    running_servers_count: int

    servers_by_types: Dict[str, int]

    images_count: int

    snapshots_count: int

    servers_count: int

    ips_count: int

    security_groups_count: int

    ips_unused: int

    volumes_l_ssd_count: int

    volumes_b_ssd_count: int

    volumes_l_ssd_total_size: int

    volumes_b_ssd_total_size: int

    private_nics_count: int

    placement_groups_count: int


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
    monthly_price: Optional[float]
    """
    Estimated monthly price, for a 30 days month, in Euro.
    """

    hourly_price: float
    """
    Hourly price in Euro.
    """

    alt_names: List[str]
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

    baremetal: bool
    """
    True if it is a baremetal Instance.
    """

    per_volume_constraint: Optional[ServerTypeVolumeConstraintsByType]
    """
    Additional volume constraints.
    """

    volumes_constraint: Optional[ServerTypeVolumeConstraintSizes]
    """
    Initial volume constraints.
    """

    gpu: Optional[int]
    """
    Number of GPU.
    """

    network: Optional[ServerTypeNetwork]
    """
    Network available for the Instance.
    """

    capabilities: Optional[ServerTypeCapabilities]
    """
    Capabilities.
    """

    scratch_storage_max_size: Optional[int]
    """
    Maximum available scratch storage.
    """

    block_bandwidth: Optional[int]
    """
    The maximum bandwidth allocated to block storage access (in bytes per second).
    """


@dataclass
class VolumeType:
    display_name: str

    capabilities: Optional[VolumeTypeCapabilities]

    constraints: Optional[VolumeTypeConstraints]


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
    A value to be retrieved from a call to the "Plan a migration" endpoint, to confirm that the volume and/or snapshots specified in said plan should be migrated.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_id: Optional[str]

    snapshot_id: Optional[str]


@dataclass
class AttachServerVolumeRequest:
    server_id: str

    volume_id: str

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_type: Optional[AttachServerVolumeRequestVolumeType]

    boot: Optional[bool]


@dataclass
class AttachServerVolumeResponse:
    server: Optional[Server]


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

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name of the image.
    """

    default_bootscript: Optional[str]
    """
    Default bootscript of the image.
    """

    extra_volumes: Optional[Dict[str, VolumeTemplate]]
    """
    Additional volumes of the image.
    """

    tags: Optional[List[str]]
    """
    Tags of the image.
    """

    public: Optional[bool]
    """
    True to create a public image.
    """

    project: Optional[str]

    organization: Optional[str]


@dataclass
class CreateImageResponse:
    image: Optional[Image]


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
    IP type to reserve (either 'routed_ipv4' or 'routed_ipv6', use of 'nat' is deprecated).
    """

    project: Optional[str]

    organization: Optional[str]


@dataclass
class CreateIpResponse:
    ip: Optional[Ip]


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

    project: Optional[str]

    organization: Optional[str]


@dataclass
class CreatePlacementGroupResponse:
    placement_group: Optional[PlacementGroup]


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

    ipam_ip_ids: Optional[List[str]]
    """
    UUID of IPAM ips, to be attached to the instance in the requested private network.
    """


@dataclass
class CreatePrivateNICResponse:
    private_nic: Optional[PrivateNIC]


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

    project: Optional[str]

    organization: Optional[str]

    organization_default: Optional[bool]

    project_default: Optional[bool]


@dataclass
class CreateSecurityGroupResponse:
    security_group: Optional[SecurityGroup]


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

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

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
    rule: Optional[SecurityGroupRule]


@dataclass
class CreateServerRequest:
    commercial_type: str
    """
    Define the Instance commercial type (i.e. GP1-S).
    """

    image: str
    """
    Instance image ID or label.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Instance name.
    """

    dynamic_ip_required: Optional[bool]
    """
    Define if a dynamic IPv4 is required for the Instance.
    """

    routed_ip_enabled: Optional[bool]
    """
    If true, configure the Instance so it uses the new routed IP mode.
    """

    volumes: Optional[Dict[str, VolumeServerTemplate]]
    """
    Volumes attached to the server.
    """

    enable_ipv6: Optional[bool]
    """
    True if IPv6 is enabled on the server (deprecated and always `False` when `routed_ip_enabled` is `True`).
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

    admin_password_encryption_ssh_key_id: Optional[str]
    """
    The public_key value of this key is used to encrypt the admin password.
    """

    project: Optional[str]

    organization: Optional[str]


@dataclass
class CreateServerResponse:
    server: Optional[Server]


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

    project: Optional[str]

    organization: Optional[str]


@dataclass
class CreateSnapshotResponse:
    snapshot: Optional[Snapshot]

    task: Optional[Task]


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

    project: Optional[str]

    organization: Optional[str]

    size: Optional[int]

    base_snapshot: Optional[str]


@dataclass
class CreateVolumeResponse:
    volume: Optional[Volume]


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
    server_id: str
    """
    Instance to which the private NIC is attached.
    """

    private_nic_id: str
    """
    Private NIC unique ID.
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
    security_group_id: str

    security_group_rule_id: str

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
    server_id: str
    """
    UUID of the Instance.
    """

    key: str
    """
    Key of the user data to delete.
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
class DetachServerVolumeRequest:
    server_id: str

    volume_id: str

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DetachServerVolumeResponse:
    server: Optional[Server]


@dataclass
class ExportSnapshotRequest:
    bucket: str
    """
    S3 bucket name.
    """

    key: str
    """
    S3 object key.
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
    task: Optional[Task]


@dataclass
class GetBootscriptRequest:
    bootscript_id: str

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetBootscriptResponse:
    bootscript: Optional[Bootscript]


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
    dashboard: Optional[Dashboard]


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
    image: Optional[Image]


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
    ip: Optional[Ip]


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
    placement_group: Optional[PlacementGroup]


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
    server_id: str
    """
    Instance to which the private NIC is attached.
    """

    private_nic_id: str
    """
    Private NIC unique ID.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetPrivateNICResponse:
    private_nic: Optional[PrivateNIC]


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
    security_group: Optional[SecurityGroup]


@dataclass
class GetSecurityGroupRuleRequest:
    security_group_id: str

    security_group_rule_id: str

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetSecurityGroupRuleResponse:
    rule: Optional[SecurityGroupRule]


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
    server: Optional[Server]


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
    servers: Dict[str, GetServerTypesAvailabilityResponseAvailability]
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

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetSnapshotResponse:
    snapshot: Optional[Snapshot]


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
    volume: Optional[Volume]


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
    total_count: int
    """
    Total number of bootscripts.
    """

    bootscripts: List[Bootscript]
    """
    List of bootscripts.
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
    total_count: int
    """
    Total number of images.
    """

    images: List[Image]
    """
    List of images.
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
    Filter on the IP Mobility IP type (whose value should be either 'routed_ipv4', 'routed_ipv6' or 'nat').
    """


@dataclass
class ListIpsResponse:
    total_count: int
    """
    Total number of ips.
    """

    ips: List[Ip]
    """
    List of ips.
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
    total_count: int
    """
    Total number of placement groups.
    """

    placement_groups: List[PlacementGroup]
    """
    List of placement groups.
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
    private_nics: List[PrivateNIC]

    total_count: int


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
    total_count: int
    """
    Total number of security groups.
    """

    rules: List[SecurityGroupRule]
    """
    List of security rules.
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
    total_count: int
    """
    Total number of security groups.
    """

    security_groups: List[SecurityGroup]
    """
    List of security groups.
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

    with_ip: Optional[str]
    """
    List Instances by IP (both private_ip and public_ip are supported).
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
    total_count: int
    """
    Total number of Instances.
    """

    servers: List[Server]
    """
    List of Instances.
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
    total_count: int
    """
    Total number of Instance types.
    """

    servers: Dict[str, ServerType]
    """
    List of Instance types.
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
    total_count: int
    """
    Total number of snapshots.
    """

    snapshots: List[Snapshot]
    """
    List of snapshots.
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
    total_count: int
    """
    Total number of volumes.
    """

    volumes: List[Volume]
    """
    List of volumes.
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
    total_count: int
    """
    Total number of volume types.
    """

    volumes: Dict[str, VolumeType]
    """
    Map of volume types.
    """


@dataclass
class MigrationPlan:
    snapshots: List[Snapshot]
    """
    A list of snapshots which will be migrated to SBS together and with the volume, if present.
    """

    validation_key: str
    """
    A value to be passed to the call to the "Apply a migration plan" endpoint, to confirm that the execution of the plan is being requested.
    """

    volume: Optional[Volume]
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

    volumes: Optional[Dict[str, ServerActionRequestVolumeBackupTemplate]]
    """
    For each volume UUID, the snapshot parameters of the volume.
This field should only be specified when performing a backup action.
    """


@dataclass
class ServerActionResponse:
    task: Optional[Task]


@dataclass
class SetImageRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    id: str

    name: str

    arch: Optional[Arch]

    creation_date: Optional[datetime]

    modification_date: Optional[datetime]

    from_server: str

    public: bool

    default_bootscript: Optional[Bootscript]

    extra_volumes: Optional[Dict[str, Volume]]

    organization: Optional[str]

    root_volume: Optional[VolumeSummary]

    state: Optional[ImageState]

    project: Optional[str]

    tags: Optional[List[str]]


@dataclass
class SetPlacementGroupRequest:
    placement_group_id: str

    name: str

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
    placement_group: Optional[PlacementGroup]


@dataclass
class SetPlacementGroupServersRequest:
    placement_group_id: str
    """
    UUID of the placement group you want to set.
    """

    servers: List[str]
    """
    An array of the Instances' UUIDs you want to configure.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
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
class UpdateImageRequest:
    image_id: str
    """
    UUID of the image.
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

    extra_volumes: Optional[Dict[str, VolumeImageUpdateTemplate]]
    """
    Additional snapshots of the image, with extra_volumeKey being the position of the snapshot in the image.
    """

    tags: Optional[List[str]]
    """
    Tags of the image.
    """

    public: Optional[bool]
    """
    True to set the image as public.
    """


@dataclass
class UpdateImageResponse:
    image: Optional[Image]


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
    ip: Optional[Ip]


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
    placement_group: Optional[PlacementGroup]


@dataclass
class UpdatePlacementGroupServersRequest:
    placement_group_id: str
    """
    UUID of the placement group you want to update.
    """

    servers: List[str]
    """
    An array of the Instances' UUIDs you want to configure.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class UpdatePlacementGroupServersResponse:
    servers: List[PlacementGroupServer]
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

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[List[str]]
    """
    Tags used to select private NIC/s.
    """


@dataclass
class UpdateSecurityGroupRequest:
    security_group_id: str
    """
    UUID of the security group.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name of the security group.
    """

    description: Optional[str]
    """
    Description of the security group.
    """

    enable_default_security: Optional[bool]
    """
    True to block SMTP on IPv4 and IPv6. This feature is read only, please open a support ticket if you need to make it configurable.
    """

    inbound_default_policy: Optional[SecurityGroupPolicy]
    """
    Default inbound policy.
    """

    tags: Optional[List[str]]
    """
    Tags of the security group.
    """

    organization_default: Optional[bool]
    """
    Please use project_default instead.
    """

    project_default: Optional[bool]
    """
    True use this security group for future Instances created in this project.
    """

    outbound_default_policy: Optional[SecurityGroupPolicy]
    """
    Default outbound policy.
    """

    stateful: Optional[bool]
    """
    True to set the security group as stateful.
    """


@dataclass
class UpdateSecurityGroupResponse:
    security_group: Optional[SecurityGroup]


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

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    protocol: Optional[SecurityGroupRuleProtocol]
    """
    Protocol family this rule applies to.
    """

    direction: Optional[SecurityGroupRuleDirection]
    """
    Direction the rule applies to.
    """

    action: Optional[SecurityGroupRuleAction]
    """
    Action to apply when the rule matches a packet.
    """

    ip_range: Optional[str]
    """
    Range of IP addresses these rules apply to.
    """

    dest_port_from: Optional[int]
    """
    Beginning of the range of ports this rule applies to (inclusive). If 0 is provided, unset the parameter.
    """

    dest_port_to: Optional[int]
    """
    End of the range of ports this rule applies to (inclusive). If 0 is provided, unset the parameter.
    """

    position: Optional[int]
    """
    Position of this rule in the security group rules list.
    """


@dataclass
class UpdateSecurityGroupRuleResponse:
    rule: Optional[SecurityGroupRule]


@dataclass
class UpdateServerRequest:
    server_id: str
    """
    UUID of the Instance.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name of the Instance.
    """

    boot_type: Optional[BootType]

    tags: Optional[List[str]]
    """
    Tags of the Instance.
    """

    volumes: Optional[Dict[str, VolumeServerTemplate]]

    bootscript: Optional[str]

    dynamic_ip_required: Optional[bool]

    routed_ip_enabled: Optional[bool]
    """
    True to configure the instance so it uses the new routed IP mode (once this is set to True you cannot set it back to False).
    """

    public_ips: Optional[List[str]]
    """
    A list of reserved IP IDs to attach to the Instance.
    """

    enable_ipv6: Optional[bool]

    protected: Optional[bool]

    security_group: Optional[SecurityGroupTemplate]

    placement_group: Optional[str]
    """
    Placement group ID if Instance must be part of a placement group.
    """

    private_nics: Optional[List[str]]
    """
    Instance private NICs.
    """

    commercial_type: Optional[str]
    """
    Warning: This field has some restrictions:
- Cannot be changed if the Instance is not in `stopped` state.
- Cannot be changed if the Instance is in a placement group.
- Cannot be changed from/to a Windows offer to/from a Linux offer.
- Local storage requirements of the target commercial_types must be fulfilled (i.e. if an Instance has 80GB of local storage, it can be changed into a GP1-XS, which has a maximum of 150GB, but it cannot be changed into a DEV1-S, which has only 20GB).
    """

    admin_password_encryption_ssh_key_id: Optional[str]
    """
    The public_key value of this key is used to encrypt the admin password. When set to an empty string, reset this value and admin_password_encrypted_value to an empty string so a new password may be generated.
    """


@dataclass
class UpdateServerResponse:
    server: Optional[Server]


@dataclass
class UpdateSnapshotRequest:
    snapshot_id: str
    """
    UUID of the snapshot.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name of the snapshot.
    """

    tags: Optional[List[str]]
    """
    Tags of the snapshot.
    """


@dataclass
class UpdateSnapshotResponse:
    snapshot: Optional[Snapshot]


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
    volume: Optional[Volume]
