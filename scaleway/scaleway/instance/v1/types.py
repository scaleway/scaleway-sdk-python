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


class Arch(str, Enum):
    X86_64 = "x86_64"
    ARM = "arm"

    def __str__(self) -> str:
        return str(self.value)


class BootType(str, Enum):
    LOCAL = "local"
    BOOTSCRIPT = "bootscript"
    RESCUE = "rescue"

    def __str__(self) -> str:
        return str(self.value)


class ImageState(str, Enum):
    AVAILABLE = "available"
    CREATING = "creating"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class ListServersRequestOrder(str, Enum):
    CREATION_DATE_DESC = "creation_date_desc"
    CREATION_DATE_ASC = "creation_date_asc"
    MODIFICATION_DATE_DESC = "modification_date_desc"
    MODIFICATION_DATE_ASC = "modification_date_asc"

    def __str__(self) -> str:
        return str(self.value)


class PlacementGroupPolicyMode(str, Enum):
    OPTIONAL = "optional"
    ENFORCED = "enforced"

    def __str__(self) -> str:
        return str(self.value)


class PlacementGroupPolicyType(str, Enum):
    MAX_AVAILABILITY = "max_availability"
    LOW_LATENCY = "low_latency"

    def __str__(self) -> str:
        return str(self.value)


class PrivateNICState(str, Enum):
    AVAILABLE = "available"
    SYNCING = "syncing"
    SYNCING_ERROR = "syncing_error"

    def __str__(self) -> str:
        return str(self.value)


class SecurityGroupPolicy(str, Enum):
    ACCEPT = "accept"
    DROP = "drop"

    def __str__(self) -> str:
        return str(self.value)


class SecurityGroupRuleAction(str, Enum):
    ACCEPT = "accept"
    DROP = "drop"

    def __str__(self) -> str:
        return str(self.value)


class SecurityGroupRuleDirection(str, Enum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"

    def __str__(self) -> str:
        return str(self.value)


class SecurityGroupRuleProtocol(str, Enum):
    TCP = "TCP"
    UDP = "UDP"
    ICMP = "ICMP"
    ANY = "ANY"

    def __str__(self) -> str:
        return str(self.value)


class SecurityGroupState(str, Enum):
    AVAILABLE = "available"
    SYNCING = "syncing"
    SYNCING_ERROR = "syncing_error"

    def __str__(self) -> str:
        return str(self.value)


class ServerAction(str, Enum):
    POWERON = "poweron"
    BACKUP = "backup"
    STOP_IN_PLACE = "stop_in_place"
    POWEROFF = "poweroff"
    TERMINATE = "terminate"
    REBOOT = "reboot"

    def __str__(self) -> str:
        return str(self.value)


class ServerState(str, Enum):
    RUNNING = "running"
    STOPPED = "stopped"
    STOPPED_IN_PLACE = "stopped in place"
    STARTING = "starting"
    STOPPING = "stopping"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class ServerTypesAvailability(str, Enum):
    AVAILABLE = "available"
    SCARCE = "scarce"
    SHORTAGE = "shortage"

    def __str__(self) -> str:
        return str(self.value)


class SnapshotState(str, Enum):
    AVAILABLE = "available"
    SNAPSHOTTING = "snapshotting"
    ERROR = "error"
    INVALID_DATA = "invalid_data"
    IMPORTING = "importing"
    EXPORTING = "exporting"

    def __str__(self) -> str:
        return str(self.value)


class SnapshotVolumeType(str, Enum):
    UNKNOWN_VOLUME_TYPE = "unknown_volume_type"
    L_SSD = "l_ssd"
    B_SSD = "b_ssd"
    UNIFIED = "unified"

    def __str__(self) -> str:
        return str(self.value)


class TaskStatus(str, Enum):
    PENDING = "pending"
    STARTED = "started"
    SUCCESS = "success"
    FAILURE = "failure"
    RETRY = "retry"

    def __str__(self) -> str:
        return str(self.value)


class VolumeServerState(str, Enum):
    AVAILABLE = "available"
    SNAPSHOTTING = "snapshotting"
    ERROR = "error"
    FETCHING = "fetching"
    RESIZING = "resizing"
    SAVING = "saving"
    HOTSYNCING = "hotsyncing"

    def __str__(self) -> str:
        return str(self.value)


class VolumeServerVolumeType(str, Enum):
    L_SSD = "l_ssd"
    B_SSD = "b_ssd"

    def __str__(self) -> str:
        return str(self.value)


class VolumeState(str, Enum):
    AVAILABLE = "available"
    SNAPSHOTTING = "snapshotting"
    ERROR = "error"
    FETCHING = "fetching"
    RESIZING = "resizing"
    SAVING = "saving"
    HOTSYNCING = "hotsyncing"

    def __str__(self) -> str:
        return str(self.value)


class VolumeVolumeType(str, Enum):
    L_SSD = "l_ssd"
    B_SSD = "b_ssd"
    UNIFIED = "unified"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Bootscript:
    """
    Bootscript
    """

    bootcmdargs: str
    """
    The bootscript arguments
    """

    default: bool
    """
    Dispmay if the bootscript is the default bootscript if no other boot option is configured
    """

    dtb: str
    """
    Provide information regarding a Device Tree Binary (dtb) for use with C1 servers
    """

    id: str
    """
    The bootscript ID
    """

    initrd: str
    """
    The initrd (initial ramdisk) configuration
    """

    kernel: str
    """
    The server kernel version
    """

    organization: str
    """
    The bootscript organization ID
    """

    project: str
    """
    The bootscript project ID
    """

    public: bool
    """
    Provide information if the bootscript is public
    """

    title: str
    """
    The bootscript title
    """

    arch: Arch
    """
    The bootscript arch
    """

    zone: Zone
    """
    The zone in which is the bootscript
    """


@dataclass
class CreateImageResponse:
    image: Optional[Image]


@dataclass
class CreateIpResponse:
    ip: Optional[Ip]


@dataclass
class CreatePlacementGroupResponse:
    placement_group: Optional[PlacementGroup]


@dataclass
class CreatePrivateNICResponse:
    private_nic: Optional[PrivateNIC]


@dataclass
class CreateSecurityGroupResponse:
    security_group: Optional[SecurityGroup]


@dataclass
class CreateSecurityGroupRuleResponse:
    rule: Optional[SecurityGroupRule]


@dataclass
class CreateServerResponse:
    server: Optional[Server]


@dataclass
class CreateSnapshotResponse:
    snapshot: Optional[Snapshot]

    task: Optional[Task]


@dataclass
class CreateVolumeResponse:
    volume: Optional[Volume]


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
class ExportSnapshotResponse:
    task: Optional[Task]


@dataclass
class GetBootscriptResponse:
    bootscript: Optional[Bootscript]


@dataclass
class GetDashboardResponse:
    dashboard: Optional[Dashboard]


@dataclass
class GetImageResponse:
    image: Optional[Image]


@dataclass
class GetIpResponse:
    ip: Optional[Ip]


@dataclass
class GetPlacementGroupResponse:
    placement_group: Optional[PlacementGroup]


@dataclass
class GetPlacementGroupServersResponse:
    servers: List[PlacementGroupServer]


@dataclass
class GetPrivateNICResponse:
    private_nic: Optional[PrivateNIC]


@dataclass
class GetSecurityGroupResponse:
    security_group: Optional[SecurityGroup]


@dataclass
class GetSecurityGroupRuleResponse:
    rule: Optional[SecurityGroupRule]


@dataclass
class GetServerResponse:
    server: Optional[Server]


@dataclass
class GetServerTypesAvailabilityResponse:
    servers: Dict[str, GetServerTypesAvailabilityResponseAvailability]


@dataclass
class GetServerTypesAvailabilityResponseAvailability:
    availability: ServerTypesAvailability


@dataclass
class GetSnapshotResponse:
    snapshot: Optional[Snapshot]


@dataclass
class GetVolumeResponse:
    volume: Optional[Volume]


@dataclass
class Image:
    id: str

    name: str

    arch: Arch

    creation_date: Optional[datetime]

    modification_date: Optional[datetime]

    default_bootscript: Optional[Bootscript]

    extra_volumes: Dict[str, Volume]

    from_server: str

    organization: str

    public: bool

    root_volume: Optional[VolumeSummary]

    state: ImageState

    project: str

    tags: List[str]

    zone: Zone


@dataclass
class Ip:
    id: str

    address: str

    reverse: Optional[str]

    server: Optional[ServerSummary]

    organization: str

    tags: List[str]

    project: str

    zone: Zone


@dataclass
class ListBootscriptsResponse:
    """
    List bootscripts response
    """

    total_count: int
    """
    Total number of bootscripts
    """

    bootscripts: List[Bootscript]
    """
    List of bootscripts
    """


@dataclass
class ListImagesResponse:
    """
    List images response
    """

    total_count: int
    """
    Total number of images
    """

    images: List[Image]
    """
    List of images
    """


@dataclass
class ListIpsResponse:
    """
    List ips response
    """

    total_count: int
    """
    Total number of ips
    """

    ips: List[Ip]
    """
    List of ips
    """


@dataclass
class ListPlacementGroupsResponse:
    """
    List placement groups response
    """

    total_count: int
    """
    Total number of placement groups
    """

    placement_groups: List[PlacementGroup]
    """
    List of placement groups
    """


@dataclass
class ListPrivateNICsResponse:
    private_nics: List[PrivateNIC]


@dataclass
class ListSecurityGroupRulesResponse:
    """
    List security group rules response
    """

    total_count: int
    """
    Total number of security groups
    """

    rules: List[SecurityGroupRule]
    """
    List of security rules
    """


@dataclass
class ListSecurityGroupsResponse:
    """
    List security groups response
    """

    total_count: int
    """
    Total number of security groups
    """

    security_groups: List[SecurityGroup]
    """
    List of security groups
    """


@dataclass
class ListServerActionsResponse:
    actions: List[ServerAction]


@dataclass
class ListServerUserDataResponse:
    user_data: List[str]


@dataclass
class ListServersResponse:
    """
    List servers response
    """

    total_count: int
    """
    Total number of servers
    """

    servers: List[Server]
    """
    List of servers
    """


@dataclass
class ListServersTypesResponse:
    """
    List servers types response
    """

    total_count: int
    """
    Total number of server types
    """

    servers: Dict[str, ServerType]
    """
    List of server types
    """


@dataclass
class ListSnapshotsResponse:
    """
    List snapshots response
    """

    total_count: int
    """
    Total number of snapshots
    """

    snapshots: List[Snapshot]
    """
    List of snapshots
    """


@dataclass
class ListVolumesResponse:
    """
    List volumes response
    """

    total_count: int
    """
    Total number of volumes
    """

    volumes: List[Volume]
    """
    List of volumes
    """


@dataclass
class ListVolumesTypesResponse:
    """
    List volumes types response
    """

    total_count: int
    """
    Total number of volume types
    """

    volumes: Dict[str, VolumeType]
    """
    Map of volume types
    """


@dataclass
class PlacementGroup:
    """
    Placement group
    """

    id: str
    """
    The placement group unique ID
    """

    name: str
    """
    The placement group name
    """

    organization: str
    """
    The placement group organization ID
    """

    project: str
    """
    The placement group project ID
    """

    tags: List[str]
    """
    The placement group tags
    """

    policy_mode: PlacementGroupPolicyMode
    """
    Select the failling mode when the placement cannot be respected, either optional or enforced
    """

    policy_type: PlacementGroupPolicyType
    """
    Select the behavior of the placement group, either low_latency (group) or max_availability (spread)
    """

    policy_respected: bool
    """
    Returns true if the policy is respected, false otherwise
    """

    zone: Zone
    """
    The zone in which is the placement group
    """


@dataclass
class PlacementGroupServer:
    id: str

    name: str

    policy_respected: bool


@dataclass
class PrivateNIC:
    """
    Private nic
    """

    id: str
    """
    The private NIC unique ID
    """

    server_id: str
    """
    The server the private NIC is attached to
    """

    private_network_id: str
    """
    The private network where the private NIC is attached
    """

    mac_address: str
    """
    The private NIC MAC address
    """

    state: PrivateNICState
    """
    The private NIC state
    """


@dataclass
class SecurityGroup:
    """
    Security group
    """

    id: str
    """
    The security groups' unique ID
    """

    name: str
    """
    The security groups name
    """

    description: str
    """
    The security groups description
    """

    enable_default_security: bool
    """
    True if SMTP is blocked on IPv4 and IPv6
    """

    inbound_default_policy: SecurityGroupPolicy
    """
    The default inbound policy
    """

    outbound_default_policy: SecurityGroupPolicy
    """
    The default outbound policy
    """

    organization: str
    """
    The security groups organization ID
    """

    project: str
    """
    The security group project ID
    """

    tags: List[str]
    """
    The security group tags
    """

    organization_default: Optional[bool]
    """
    True if it is your default security group for this organization ID
    :deprecated
    """

    project_default: bool
    """
    True if it is your default security group for this project ID
    """

    creation_date: Optional[datetime]
    """
    The security group creation date
    """

    modification_date: Optional[datetime]
    """
    The security group modification date
    """

    servers: List[ServerSummary]
    """
    List of servers attached to this security group
    """

    stateful: bool
    """
    True if the security group is stateful
    """

    state: SecurityGroupState
    """
    Security group state
    """

    zone: Zone
    """
    The zone in which is the security group
    """


@dataclass
class SecurityGroupRule:
    id: str

    protocol: SecurityGroupRuleProtocol

    direction: SecurityGroupRuleDirection

    action: SecurityGroupRuleAction

    ip_range: str

    dest_port_from: Optional[int]

    dest_port_to: Optional[int]

    position: int

    editable: bool

    zone: Zone


@dataclass
class SecurityGroupSummary:
    id: str

    name: str


@dataclass
class SecurityGroupTemplate:
    id: str

    name: str


@dataclass
class Server:
    """
    Server
    """

    id: str
    """
    The server unique ID
    """

    name: str
    """
    The server name
    """

    organization: str
    """
    The server organization ID
    """

    project: str
    """
    The server project ID
    """

    allowed_actions: List[ServerAction]
    """
    Provide as list of allowed actions on the server
    """

    tags: List[str]
    """
    The server associated tags
    """

    commercial_type: str
    """
    The server commercial type (eg. GP1-M)
    """

    creation_date: Optional[datetime]
    """
    The server creation date
    """

    dynamic_ip_required: bool
    """
    True if a dynamic IP is required
    """

    enable_ipv6: bool
    """
    True if IPv6 is enabled
    """

    hostname: str
    """
    The server host name
    """

    image: Optional[Image]
    """
    Provide information on the server image
    """

    protected: bool
    """
    The server protection option is activated
    """

    private_ip: Optional[str]
    """
    The server private IP address
    """

    public_ip: Optional[ServerIp]
    """
    Information about the public IP
    """

    modification_date: Optional[datetime]
    """
    The server modification date
    """

    state: ServerState
    """
    The server state
    """

    location: Optional[ServerLocation]
    """
    The server location
    """

    ipv6: Optional[ServerIpv6]
    """
    The server IPv6 address
    """

    bootscript: Optional[Bootscript]
    """
    The server bootscript
    """

    boot_type: BootType
    """
    The server boot type
    """

    volumes: Dict[str, VolumeServer]
    """
    The server volumes
    """

    security_group: Optional[SecurityGroupSummary]
    """
    The server security group
    """

    maintenances: List[ServerMaintenance]
    """
    The server planned maintenances
    """

    state_detail: str
    """
    The server state_detail
    """

    arch: Arch
    """
    The server arch
    """

    placement_group: Optional[PlacementGroup]
    """
    The server placement group
    """

    private_nics: List[PrivateNIC]
    """
    The server private NICs
    """

    zone: Zone
    """
    The zone in which is the server
    """


@dataclass
class ServerActionRequestVolumeBackupTemplate:
    """
    Server action request. volume backup template
    """

    volume_type: SnapshotVolumeType
    """
    Overrides the volume_type of the snapshot for this volume.
    If omitted, the volume type of the original volume will be used.
    
    """


@dataclass
class ServerActionResponse:
    task: Optional[Task]


@dataclass
class ServerIp:
    """
    Server. ip
    """

    id: str
    """
    The unique ID of the IP address
    """

    address: str
    """
    The server public IPv4 IP-Address
    """

    dynamic: bool
    """
    True if the IP address is dynamic
    """


@dataclass
class ServerIpv6:
    """
    Server. ipv6
    """

    address: str
    """
    The server IPv6 IP-Address
    """

    gateway: str
    """
    The IPv6 IP-addresses gateway
    """

    netmask: str
    """
    The IPv6 IP-addresses CIDR netmask
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


@dataclass
class ServerSummary:
    id: str

    name: str


@dataclass
class ServerType:
    """
    Server type
    """

    monthly_price: Optional[float]
    """
    Estimated monthly price, for a 30 days month, in Euro
    :deprecated
    """

    hourly_price: float
    """
    Hourly price in Euro
    """

    alt_names: List[str]
    """
    Alternative instance name if any
    """

    per_volume_constraint: Optional[ServerTypeVolumeConstraintsByType]
    """
    Additional volume constraints
    """

    volumes_constraint: Optional[ServerTypeVolumeConstraintSizes]
    """
    Initial volume constraints
    """

    ncpus: int
    """
    Number of CPU
    """

    gpu: Optional[int]
    """
    Number of GPU
    """

    ram: int
    """
    Available RAM in bytes
    """

    arch: Arch
    """
    CPU architecture
    """

    baremetal: bool
    """
    True if it is a baremetal instance
    """

    network: Optional[ServerTypeNetwork]
    """
    Network available for the instance
    """

    capabilities: Optional[ServerTypeCapabilities]
    """
    Capabilities
    """


@dataclass
class ServerTypeCapabilities:
    """
    Server type. capabilities
    """

    block_storage: Optional[bool]
    """
    True if server supports block storage
    """

    boot_types: List[BootType]
    """
    List of supported boot types
    """


@dataclass
class ServerTypeNetwork:
    """
    Server type. network
    """

    interfaces: List[ServerTypeNetworkInterface]
    """
    List of available network interfaces
    """

    sum_internal_bandwidth: Optional[int]
    """
    Total maximum internal bandwidth in bits per seconds
    """

    sum_internet_bandwidth: Optional[int]
    """
    Total maximum internet bandwidth in bits per seconds
    """

    ipv6_support: bool
    """
    True if IPv6 is enabled
    """


@dataclass
class ServerTypeNetworkInterface:
    """
    Server type. network. interface
    """

    internal_bandwidth: Optional[int]
    """
    Maximum internal bandwidth in bits per seconds
    """

    internet_bandwidth: Optional[int]
    """
    Maximum internet bandwidth in bits per seconds
    """


@dataclass
class ServerTypeVolumeConstraintSizes:
    """
    Server type. volume constraint sizes
    """

    min_size: int
    """
    Minimum volume size in bytes
    """

    max_size: int
    """
    Maximum volume size in bytes
    """


@dataclass
class ServerTypeVolumeConstraintsByType:
    """
    Server type. volume constraints by type
    """

    l_ssd: Optional[ServerTypeVolumeConstraintSizes]
    """
    Local SSD volumes
    """


@dataclass
class SetPlacementGroupResponse:
    placement_group: Optional[PlacementGroup]


@dataclass
class SetPlacementGroupServersResponse:
    servers: List[PlacementGroupServer]


@dataclass
class SetSecurityGroupRulesRequestRule:
    """
    Set security group rules request. rule
    """

    id: Optional[str]
    """
    UUID of the security rule to update. If no value is provided, a new rule will be created
    """

    action: SecurityGroupRuleAction
    """
    Action to apply when the rule matches a packet
    """

    protocol: SecurityGroupRuleProtocol
    """
    Protocol family this rule applies to
    """

    direction: SecurityGroupRuleDirection
    """
    Direction the rule applies to
    """

    ip_range: str
    """
    The range of IP address this rules applies to
    """

    dest_port_from: Optional[int]
    """
    Beginning of the range of ports this rule applies to (inclusive). This value will be set to null if protocol is ICMP or ANY
    """

    dest_port_to: Optional[int]
    """
    End of the range of ports this rule applies to (inclusive). This value will be set to null if protocol is ICMP or ANY, or if it is equal to dest_port_from
    """

    position: int
    """
    Position of this rule in the security group rules list. If several rules are passed with the same position, the resulting order is undefined
    """

    editable: Optional[bool]
    """
    Indicates if this rule is editable. Rules with the value false will be ignored
    """

    zone: Zone
    """
    Zone of the rule. This field is ignored
    """


@dataclass
class SetSecurityGroupRulesResponse:
    rules: List[SecurityGroupRule]


@dataclass
class Snapshot:
    """
    Snapshot
    """

    id: str
    """
    The snapshot ID
    """

    name: str
    """
    The snapshot name
    """

    organization: str
    """
    The snapshot organization ID
    """

    project: str
    """
    The snapshot project ID
    """

    tags: List[str]
    """
    The snapshot tags
    """

    volume_type: VolumeVolumeType
    """
    The snapshot volume type
    """

    size: int
    """
    The snapshot size
    """

    state: SnapshotState
    """
    The snapshot state
    """

    base_volume: Optional[SnapshotBaseVolume]
    """
    The volume on which the snapshot is based on
    """

    creation_date: Optional[datetime]
    """
    The snapshot creation date
    """

    modification_date: Optional[datetime]
    """
    The snapshot modification date
    """

    zone: Zone
    """
    The snapshot zone
    """

    error_reason: Optional[str]
    """
    The reason for the failed snapshot import
    """


@dataclass
class SnapshotBaseVolume:
    """
    Snapshot. base volume
    """

    id: str
    """
    The volume ID on which the snapshot is based on
    """

    name: str
    """
    The volume name on which the snapshot is based on
    """


@dataclass
class Task:
    """
    Task
    """

    id: str
    """
    The unique ID of the task
    """

    description: str
    """
    The description of the task
    """

    progress: int
    """
    The progress of the task in percent
    """

    started_at: Optional[datetime]
    """
    The task start date
    """

    terminated_at: Optional[datetime]
    """
    The task end date
    """

    status: TaskStatus
    """
    The task status
    """

    href_from: str

    href_result: str

    zone: Zone
    """
    The zone in which is the task
    """


@dataclass
class UpdateIpResponse:
    ip: Optional[Ip]


@dataclass
class UpdatePlacementGroupResponse:
    placement_group: Optional[PlacementGroup]


@dataclass
class UpdatePlacementGroupServersResponse:
    servers: List[PlacementGroupServer]


@dataclass
class UpdateServerResponse:
    server: Optional[Server]


@dataclass
class UpdateVolumeResponse:
    volume: Optional[Volume]


@dataclass
class Volume:
    """
    Volume
    """

    id: str
    """
    The volume unique ID
    """

    name: str
    """
    The volume name
    """

    export_uri: Optional[str]
    """
    Show the volume NBD export URI
    :deprecated
    """

    size: int
    """
    The volume disk size
    """

    volume_type: VolumeVolumeType
    """
    The volume type
    """

    creation_date: Optional[datetime]
    """
    The volume creation date
    """

    modification_date: Optional[datetime]
    """
    The volume modification date
    """

    organization: str
    """
    The volume organization ID
    """

    project: str
    """
    The volume project ID
    """

    tags: List[str]
    """
    The volume tags
    """

    server: Optional[ServerSummary]
    """
    The server attached to the volume
    """

    state: VolumeState
    """
    The volume state
    """

    zone: Zone
    """
    The zone in which is the volume
    """


@dataclass
class VolumeServer:
    id: str

    name: str

    export_uri: str

    organization: str

    server: Optional[ServerSummary]

    size: int

    volume_type: VolumeServerVolumeType

    creation_date: Optional[datetime]

    modification_date: Optional[datetime]

    state: VolumeServerState

    project: str

    boot: bool

    zone: Zone


@dataclass
class VolumeServerTemplate:
    """
    Volume server template
    """

    id: str
    """
    UUID of the volume
    """

    boot: bool
    """
    Force the server to boot on this volume
    """

    name: str
    """
    Name of the volume
    """

    size: int
    """
    Disk size of the volume, must be a multiple of 512
    """

    volume_type: VolumeVolumeType
    """
    Type of the volume
    """

    base_snapshot: str
    """
    The ID of the snapshot on which this volume will be based
    """

    organization: str
    """
    Organization ID of the volume
    """

    project: str
    """
    Project ID of the volume
    """


@dataclass
class VolumeSummary:
    id: str

    name: str

    size: int

    volume_type: VolumeVolumeType


@dataclass
class VolumeTemplate:
    """
    Volume template
    """

    id: str
    """
    UUID of the volume
    """

    name: str
    """
    Name of the volume
    """

    size: int
    """
    Disk size of the volume, must be a multiple of 512
    """

    volume_type: VolumeVolumeType
    """
    Type of the volume
    """

    organization: Optional[str]
    """
    Organization ID of the volume.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    :deprecated
    """

    project: Optional[str]
    """
    Project ID of the volume.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    """


@dataclass
class VolumeType:
    display_name: str

    capabilities: Optional[VolumeTypeCapabilities]

    constraints: Optional[VolumeTypeConstraints]


@dataclass
class VolumeTypeCapabilities:
    snapshot: bool


@dataclass
class VolumeTypeConstraints:
    min: int

    max: int


@dataclass
class GetServerTypesAvailabilityRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    per_page: Optional[int]

    page: Optional[int]


@dataclass
class ListServersTypesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    per_page: Optional[int]

    page: Optional[int]


@dataclass
class ListVolumesTypesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    per_page: Optional[int]

    page: Optional[int]


@dataclass
class ListServersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    per_page: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to return
    """

    page: Optional[int]
    """
    A positive integer to choose the page to return
    """

    organization: Optional[str]
    """
    List only servers of this organization ID
    """

    project: Optional[str]
    """
    List only servers of this project ID
    """

    name: Optional[str]
    """
    Filter servers by name (for eg. "server1" will return "server100" and "server1" but not "foo")
    """

    private_ip: Optional[str]
    """
    List servers by private_ip
    """

    without_ip: Optional[bool]
    """
    List servers that are not attached to a public IP
    """

    commercial_type: Optional[str]
    """
    List servers of this commercial type
    """

    state: Optional[ServerState]
    """
    List servers in this state
    """

    tags: Optional[List[str]]
    """
    List servers with these exact tags (to filter with several tags, use commas to separate them)
    """

    private_network: Optional[str]
    """
    List servers in this Private Network
    """

    order: Optional[ListServersRequestOrder]
    """
    Define the order of the returned servers
    """


@dataclass
class DeleteServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str


@dataclass
class GetServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    UUID of the server you want to get
    """


@dataclass
class ListServerActionsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str


@dataclass
class ServerActionRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    UUID of the server
    """

    action: ServerAction
    """
    The action to perform on the server
    """

    name: Optional[str]
    """
    The name of the backup you want to create.
    This field should only be specified when performing a backup action.
    
    """

    volumes: Optional[Dict[str, ServerActionRequestVolumeBackupTemplate]]
    """
    For each volume UUID, the snapshot parameters of the volume.
    This field should only be specified when performing a backup action.
    
    """


@dataclass
class ListServerUserDataRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    UUID of the server
    """


@dataclass
class DeleteServerUserDataRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    UUID of the server
    """

    key: str
    """
    Key of the user data to delete
    """


@dataclass
class ListImagesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
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
class GetImageRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    image_id: str
    """
    UUID of the image you want to get
    """


@dataclass
class CreateImageRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    name: Optional[str]
    """
    Name of the image
    """

    root_volume: str
    """
    UUID of the snapshot
    """

    arch: Optional[Arch]
    """
    Architecture of the image
    """

    default_bootscript: Optional[str]
    """
    Default bootscript of the image
    """

    extra_volumes: Optional[Dict[str, VolumeTemplate]]
    """
    Additional volumes of the image
    """

    organization: Optional[str]
    """
    Organization ID of the image.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    :deprecated
    """

    project: Optional[str]
    """
    Project ID of the image.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    """

    tags: Optional[List[str]]
    """
    The tags of the image
    """

    public: Optional[bool]
    """
    True to create a public image
    """


@dataclass
class DeleteImageRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    image_id: str
    """
    UUID of the image you want to delete
    """


@dataclass
class ListSnapshotsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    organization: Optional[str]

    per_page: Optional[int]

    page: Optional[int]

    name: Optional[str]

    project: Optional[str]

    tags: Optional[str]


@dataclass
class CreateSnapshotRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    name: Optional[str]
    """
    Name of the snapshot
    """

    volume_id: Optional[str]
    """
    UUID of the volume
    """

    tags: Optional[List[str]]
    """
    The tags of the snapshot
    """

    organization: Optional[str]
    """
    Organization ID of the snapshot.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    :deprecated
    """

    project: Optional[str]
    """
    Project ID of the snapshot.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    """

    volume_type: SnapshotVolumeType
    """
    Overrides the volume_type of the snapshot.
    If omitted, the volume type of the original volume will be used.
    
    """

    bucket: Optional[str]
    """
    Bucket name for snapshot imports
    """

    key: Optional[str]
    """
    Object key for snapshot imports
    """

    size: Optional[int]
    """
    Imported snapshot size, must be a multiple of 512
    """


@dataclass
class GetSnapshotRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    snapshot_id: str
    """
    UUID of the snapshot you want to get
    """


@dataclass
class DeleteSnapshotRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    snapshot_id: str
    """
    UUID of the snapshot you want to delete
    """


@dataclass
class ExportSnapshotRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    snapshot_id: str
    """
    The snapshot ID
    """

    bucket: str
    """
    S3 bucket name
    """

    key: str
    """
    S3 object key
    """


@dataclass
class ListVolumesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    volume_type: Optional[VolumeVolumeType]
    """
    Filter by volume type
    """

    per_page: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to return
    """

    page: Optional[int]
    """
    A positive integer to choose the page to return
    """

    organization: Optional[str]
    """
    Filter volume by organization ID
    """

    project: Optional[str]
    """
    Filter volume by project ID
    """

    tags: Optional[List[str]]
    """
    Filter volumes with these exact tags (to filter with several tags, use commas to separate them)
    """

    name: Optional[str]
    """
    Filter volume by name (for eg. "vol" will return "myvolume" but not "data")
    """


@dataclass
class CreateVolumeRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    name: Optional[str]
    """
    The volume name
    """

    organization: Optional[str]
    """
    The volume organization ID.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    :deprecated
    """

    project: Optional[str]
    """
    The volume project ID.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    """

    tags: Optional[List[str]]
    """
    The volume tags
    """

    volume_type: VolumeVolumeType
    """
    The volume type
    """

    size: Optional[int]
    """
    The volume disk size, must be a multiple of 512.
    
    One-of ('from_'): at most one of 'size', 'base_volume', 'base_snapshot' could be set.
    """

    base_volume: Optional[str]
    """
    The ID of the volume on which this volume will be based.
    
    One-of ('from_'): at most one of 'size', 'base_volume', 'base_snapshot' could be set.
    """

    base_snapshot: Optional[str]
    """
    The ID of the snapshot on which this volume will be based.
    
    One-of ('from_'): at most one of 'size', 'base_volume', 'base_snapshot' could be set.
    """


@dataclass
class GetVolumeRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    volume_id: str
    """
    UUID of the volume you want to get
    """


@dataclass
class UpdateVolumeRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    volume_id: str
    """
    UUID of the volume
    """

    name: Optional[str]
    """
    The volume name
    """

    tags: Optional[List[str]]
    """
    The tags of the volume
    """

    size: Optional[int]
    """
    The volume disk size, must be a multiple of 512
    """


@dataclass
class DeleteVolumeRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    volume_id: str
    """
    UUID of the volume you want to delete
    """


@dataclass
class ListSecurityGroupsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    name: Optional[str]
    """
    Name of the security group
    """

    organization: Optional[str]
    """
    The security group organization ID
    """

    project: Optional[str]
    """
    The security group project ID
    """

    tags: Optional[List[str]]
    """
    List security groups with these exact tags (to filter with several tags, use commas to separate them)
    """

    project_default: Optional[bool]
    """
    Filter security groups with this value for project_default
    """

    per_page: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to return
    """

    page: Optional[int]
    """
    A positive integer to choose the page to return
    """


@dataclass
class CreateSecurityGroupRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    name: Optional[str]
    """
    Name of the security group
    """

    description: str
    """
    Description of the security group
    """

    organization: Optional[str]
    """
    Organization ID the security group belongs to.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    :deprecated
    """

    project: Optional[str]
    """
    Project ID the security group belong to.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    """

    tags: Optional[List[str]]
    """
    The tags of the security group
    """

    organization_default: Optional[bool]
    """
    Whether this security group becomes the default security group for new instances.
    
    One-of ('default_identifier'): at most one of 'organization_default', 'project_default' could be set.
    :deprecated
    """

    project_default: Optional[bool]
    """
    Whether this security group becomes the default security group for new instances.
    
    One-of ('default_identifier'): at most one of 'organization_default', 'project_default' could be set.
    """

    stateful: bool
    """
    Whether the security group is stateful or not
    """

    inbound_default_policy: SecurityGroupPolicy
    """
    Default policy for inbound rules
    """

    outbound_default_policy: SecurityGroupPolicy
    """
    Default policy for outbound rules
    """

    enable_default_security: Optional[bool]
    """
    True to block SMTP on IPv4 and IPv6
    """


@dataclass
class GetSecurityGroupRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    security_group_id: str
    """
    UUID of the security group you want to get
    """


@dataclass
class DeleteSecurityGroupRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    security_group_id: str
    """
    UUID of the security group you want to delete
    """


@dataclass
class ListDefaultSecurityGroupRulesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """


@dataclass
class ListSecurityGroupRulesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    security_group_id: str
    """
    UUID of the security group
    """

    per_page: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to return
    """

    page: Optional[int]
    """
    A positive integer to choose the page to return
    """


@dataclass
class CreateSecurityGroupRuleRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    security_group_id: str
    """
    UUID of the security group
    """

    protocol: Optional[SecurityGroupRuleProtocol]

    direction: Optional[SecurityGroupRuleDirection]

    action: Optional[SecurityGroupRuleAction]

    ip_range: str

    dest_port_from: Optional[int]
    """
    The beginning of the range of ports to apply this rule to (inclusive)
    """

    dest_port_to: Optional[int]
    """
    The end of the range of ports to apply this rule to (inclusive)
    """

    position: int
    """
    The position of this rule in the security group rules list
    """

    editable: bool
    """
    Indicates if this rule is editable (will be ignored)
    """


@dataclass
class SetSecurityGroupRulesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    security_group_id: str
    """
    UUID of the security group to update the rules on
    """

    rules: Optional[List[SetSecurityGroupRulesRequestRule]]
    """
    List of rules to update in the security group
    """


@dataclass
class DeleteSecurityGroupRuleRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    security_group_id: str

    security_group_rule_id: str


@dataclass
class GetSecurityGroupRuleRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    security_group_id: str

    security_group_rule_id: str


@dataclass
class ListPlacementGroupsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    per_page: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to return
    """

    page: Optional[int]
    """
    A positive integer to choose the page to return
    """

    organization: Optional[str]
    """
    List only placement groups of this organization ID
    """

    project: Optional[str]
    """
    List only placement groups of this project ID
    """

    tags: Optional[List[str]]
    """
    List placement groups with these exact tags (to filter with several tags, use commas to separate them)
    """

    name: Optional[str]
    """
    Filter placement groups by name (for eg. "cluster1" will return "cluster100" and "cluster1" but not "foo")
    """


@dataclass
class CreatePlacementGroupRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    name: Optional[str]
    """
    Name of the placement group
    """

    organization: Optional[str]
    """
    Organization ID of the placement group.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    :deprecated
    """

    project: Optional[str]
    """
    Project ID of the placement group.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    """

    tags: Optional[List[str]]
    """
    The tags of the placement group
    """

    policy_mode: PlacementGroupPolicyMode
    """
    The operating mode of the placement group
    """

    policy_type: PlacementGroupPolicyType
    """
    The policy type of the placement group
    """


@dataclass
class GetPlacementGroupRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    placement_group_id: str
    """
    UUID of the placement group you want to get
    """


@dataclass
class SetPlacementGroupRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    placement_group_id: str

    name: str

    organization: Optional[str]

    policy_mode: PlacementGroupPolicyMode

    policy_type: PlacementGroupPolicyType

    project: Optional[str]

    tags: Optional[List[str]]


@dataclass
class UpdatePlacementGroupRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    placement_group_id: str
    """
    UUID of the placement group
    """

    name: Optional[str]
    """
    Name of the placement group
    """

    tags: Optional[List[str]]
    """
    The tags of the placement group
    """

    policy_mode: Optional[PlacementGroupPolicyMode]
    """
    The operating mode of the placement group
    """

    policy_type: Optional[PlacementGroupPolicyType]
    """
    The policy type of the placement group
    """


@dataclass
class DeletePlacementGroupRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    placement_group_id: str
    """
    UUID of the placement group you want to delete
    """


@dataclass
class GetPlacementGroupServersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    placement_group_id: str


@dataclass
class SetPlacementGroupServersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    placement_group_id: str

    servers: Optional[List[str]]


@dataclass
class UpdatePlacementGroupServersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    placement_group_id: str
    """
    UUID of the placement group
    """

    servers: List[str]


@dataclass
class ListIpsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    project: Optional[str]
    """
    The project ID the IPs are reserved in
    """

    organization: Optional[str]
    """
    The organization ID the IPs are reserved in
    """

    tags: Optional[List[str]]
    """
    Filter IPs with these exact tags (to filter with several tags, use commas to separate them)
    """

    name: Optional[str]
    """
    Filter on the IP address (Works as a LIKE operation on the IP address)
    """

    per_page: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to return
    """

    page: Optional[int]
    """
    A positive integer to choose the page to return
    """


@dataclass
class CreateIpRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    organization: Optional[str]
    """
    The organization ID the IP is reserved in.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    :deprecated
    """

    project: Optional[str]
    """
    The project ID the IP is reserved in.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    """

    tags: Optional[List[str]]
    """
    The tags of the IP
    """

    server: Optional[str]
    """
    UUID of the server you want to attach the IP to
    """


@dataclass
class GetIpRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    ip: str
    """
    The IP ID or address to get
    """


@dataclass
class UpdateIpRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    ip: str
    """
    IP ID or IP address
    """

    reverse: Optional[str]
    """
    Reverse domain name
    """

    tags: Optional[List[str]]
    """
    An array of keywords you want to tag this IP with
    """

    server: Optional[str]


@dataclass
class DeleteIpRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    ip: str
    """
    The ID or the address of the IP to delete
    """


@dataclass
class ListPrivateNICsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    The server the private NIC is attached to
    """


@dataclass
class CreatePrivateNICRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    UUID of the server the private NIC will be attached to
    """

    private_network_id: str
    """
    UUID of the private network where the private NIC will be attached
    """


@dataclass
class GetPrivateNICRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    The server the private NIC is attached to
    """

    private_nic_id: str
    """
    The private NIC unique ID
    """


@dataclass
class DeletePrivateNICRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    The server the private NIC is attached to
    """

    private_nic_id: str
    """
    The private NIC unique ID
    """


@dataclass
class ListBootscriptsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    arch: Optional[str]

    title: Optional[str]

    default: Optional[bool]

    public: Optional[bool]

    per_page: Optional[int]

    page: Optional[int]


@dataclass
class GetBootscriptRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    bootscript_id: str


@dataclass
class GetDashboardRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    organization: Optional[str]

    project: Optional[str]
