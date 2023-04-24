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
    Bootscript.
    """

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

    arch: Arch
    """
    Bootscript architecture.
    """

    zone: Zone
    """
    Zone in which the bootscript is located.
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
    """
    Get placement group servers response.
    """

    servers: List[PlacementGroupServer]
    """
    Instances attached to the placement group.
    """


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
    """
    :deprecated
    """

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
    List bootscripts response.
    """

    total_count: int
    """
    Total number of bootscripts.
    """

    bootscripts: List[Bootscript]
    """
    List of bootscripts.
    """


@dataclass
class ListImagesResponse:
    """
    List images response.
    """

    total_count: int
    """
    Total number of images.
    """

    images: List[Image]
    """
    List of images.
    """


@dataclass
class ListIpsResponse:
    """
    List ips response.
    """

    total_count: int
    """
    Total number of ips.
    """

    ips: List[Ip]
    """
    List of ips.
    """


@dataclass
class ListPlacementGroupsResponse:
    """
    List placement groups response.
    """

    total_count: int
    """
    Total number of placement groups.
    """

    placement_groups: List[PlacementGroup]
    """
    List of placement groups.
    """


@dataclass
class ListPrivateNICsResponse:
    private_nics: List[PrivateNIC]

    total_count: int


@dataclass
class ListSecurityGroupRulesResponse:
    """
    List security group rules response.
    """

    total_count: int
    """
    Total number of security groups.
    """

    rules: List[SecurityGroupRule]
    """
    List of security rules.
    """


@dataclass
class ListSecurityGroupsResponse:
    """
    List security groups response.
    """

    total_count: int
    """
    Total number of security groups.
    """

    security_groups: List[SecurityGroup]
    """
    List of security groups.
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
    List servers response.
    """

    total_count: int
    """
    Total number of Instances.
    """

    servers: List[Server]
    """
    List of Instances.
    """


@dataclass
class ListServersTypesResponse:
    """
    List servers types response.
    """

    total_count: int
    """
    Total number of Instance types.
    """

    servers: Dict[str, ServerType]
    """
    List of Instance types.
    """


@dataclass
class ListSnapshotsResponse:
    """
    List snapshots response.
    """

    total_count: int
    """
    Total number of snapshots.
    """

    snapshots: List[Snapshot]
    """
    List of snapshots.
    """


@dataclass
class ListVolumesResponse:
    """
    List volumes response.
    """

    total_count: int
    """
    Total number of volumes.
    """

    volumes: List[Volume]
    """
    List of volumes.
    """


@dataclass
class ListVolumesTypesResponse:
    """
    List volumes types response.
    """

    total_count: int
    """
    Total number of volume types.
    """

    volumes: Dict[str, VolumeType]
    """
    Map of volume types.
    """


@dataclass
class PlacementGroup:
    """
    Placement group.
    """

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
class PlacementGroupServer:
    """
    Placement group server.
    """

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
class PrivateNIC:
    """
    Private nic.
    """

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
class SecurityGroup:
    """
    Security group.
    """

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

    organization_default: Optional[bool]
    """
    True if it is your default security group for this Organization ID.
    :deprecated
    """

    project_default: bool
    """
    True if it is your default security group for this Project ID.
    """

    creation_date: Optional[datetime]
    """
    Security group creation date.
    """

    modification_date: Optional[datetime]
    """
    Security group modification date.
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
    Server.
    """

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
    True if a dynamic IP is required.
    """

    enable_ipv6: bool
    """
    True if IPv6 is enabled.
    """

    hostname: str
    """
    Instance host name.
    """

    image: Optional[Image]
    """
    Information about the Instance image.
    """

    protected: bool
    """
    Defines whether the Instance protection option is activated.
    """

    private_ip: Optional[str]
    """
    Private IP address of the Instance.
    """

    public_ip: Optional[ServerIp]
    """
    Information about the public IP.
    """

    modification_date: Optional[datetime]
    """
    Instance modification date.
    """

    state: ServerState
    """
    Instance state.
    """

    location: Optional[ServerLocation]
    """
    Instance location.
    """

    ipv6: Optional[ServerIpv6]
    """
    Instance IPv6 address.
    """

    bootscript: Optional[Bootscript]
    """
    Instance bootscript.
    :deprecated
    """

    boot_type: BootType
    """
    Instance boot type.
    """

    volumes: Dict[str, VolumeServer]
    """
    Instance volumes.
    """

    security_group: Optional[SecurityGroupSummary]
    """
    Instance security group.
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

    placement_group: Optional[PlacementGroup]
    """
    Instance placement group.
    """

    private_nics: List[PrivateNIC]
    """
    Instance private NICs.
    """

    zone: Zone
    """
    Zone in which the Instance is located.
    """


@dataclass
class ServerActionRequestVolumeBackupTemplate:
    """
    Server action request. volume backup template.
    """

    volume_type: SnapshotVolumeType
    """
    Snapshot's volume type.
    Overrides the `volume_type` of the snapshot for this volume.
    If omitted, the volume type of the original volume will be used.
    """


@dataclass
class ServerActionResponse:
    task: Optional[Task]


@dataclass
class ServerIp:
    """
    Server. ip.
    """

    id: str
    """
    Unique ID of the IP address.
    """

    address: str
    """
    Instance public IPv4 IP-Address.
    """

    dynamic: bool
    """
    True if the IP address is dynamic.
    """


@dataclass
class ServerIpv6:
    """
    Server. ipv6.
    """

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


@dataclass
class ServerSummary:
    id: str

    name: str


@dataclass
class ServerType:
    """
    Server type.
    """

    monthly_price: Optional[float]
    """
    Estimated monthly price, for a 30 days month, in Euro.
    :deprecated
    """

    hourly_price: float
    """
    Hourly price in Euro.
    """

    alt_names: List[str]
    """
    Alternative Instance name, if any.
    """

    per_volume_constraint: Optional[ServerTypeVolumeConstraintsByType]
    """
    Additional volume constraints.
    """

    volumes_constraint: Optional[ServerTypeVolumeConstraintSizes]
    """
    Initial volume constraints.
    """

    ncpus: int
    """
    Number of CPU.
    """

    gpu: Optional[int]
    """
    Number of GPU.
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

    network: Optional[ServerTypeNetwork]
    """
    Network available for the Instance.
    """

    capabilities: Optional[ServerTypeCapabilities]
    """
    Capabilities.
    """


@dataclass
class ServerTypeCapabilities:
    """
    Server type. capabilities.
    """

    block_storage: Optional[bool]
    """
    Defines whether the Instance supports block storage.
    """

    boot_types: List[BootType]
    """
    List of supported boot types.
    """


@dataclass
class ServerTypeNetwork:
    """
    Server type. network.
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

    ipv6_support: bool
    """
    True if IPv6 is enabled.
    """


@dataclass
class ServerTypeNetworkInterface:
    """
    Server type. network. interface.
    """

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
    """
    Server type. volume constraint sizes.
    """

    min_size: int
    """
    Minimum volume size in bytes.
    """

    max_size: int
    """
    Maximum volume size in bytes.
    """


@dataclass
class ServerTypeVolumeConstraintsByType:
    """
    Server type. volume constraints by type.
    """

    l_ssd: Optional[ServerTypeVolumeConstraintSizes]
    """
    Local SSD volumes.
    """


@dataclass
class SetPlacementGroupResponse:
    placement_group: Optional[PlacementGroup]


@dataclass
class SetPlacementGroupServersResponse:
    """
    Set placement group servers response.
    """

    servers: List[PlacementGroupServer]
    """
    Instances attached to the placement group.
    """


@dataclass
class SetSecurityGroupRulesRequestRule:
    """
    Set security group rules request. rule.
    """

    id: Optional[str]
    """
    UUID of the security rule to update. If no value is provided, a new rule will be created.
    """

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

    dest_port_from: Optional[int]
    """
    Beginning of the range of ports this rule applies to (inclusive). This value will be set to null if protocol is ICMP or ANY.
    """

    dest_port_to: Optional[int]
    """
    End of the range of ports this rule applies to (inclusive). This value will be set to null if protocol is ICMP or ANY, or if it is equal to dest_port_from.
    """

    position: int
    """
    Position of this rule in the security group rules list. If several rules are passed with the same position, the resulting order is undefined.
    """

    editable: Optional[bool]
    """
    Indicates if this rule is editable. Rules with the value false will be ignored.
    """

    zone: Zone
    """
    Zone of the rule. This field is ignored.
    """


@dataclass
class SetSecurityGroupRulesResponse:
    rules: List[SecurityGroupRule]


@dataclass
class Snapshot:
    """
    Snapshot.
    """

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

    zone: Zone
    """
    Snapshot zone.
    """

    error_reason: Optional[str]
    """
    Reason for the failed snapshot import.
    """


@dataclass
class SnapshotBaseVolume:
    """
    Snapshot. base volume.
    """

    id: str
    """
    Volume ID on which the snapshot is based.
    """

    name: str
    """
    Volume name on which the snapshot is based on.
    """


@dataclass
class Task:
    """
    Task.
    """

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

    started_at: Optional[datetime]
    """
    Task start date.
    """

    terminated_at: Optional[datetime]
    """
    Task end date.
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


@dataclass
class UpdateIpResponse:
    ip: Optional[Ip]


@dataclass
class UpdatePlacementGroupResponse:
    placement_group: Optional[PlacementGroup]


@dataclass
class UpdatePlacementGroupServersResponse:
    """
    Update placement group servers response.
    """

    servers: List[PlacementGroupServer]
    """
    Instances attached to the placement group.
    """


@dataclass
class UpdateServerResponse:
    server: Optional[Server]


@dataclass
class UpdateVolumeResponse:
    volume: Optional[Volume]


@dataclass
class Volume:
    """
    Volume.
    """

    id: str
    """
    Volume unique ID.
    """

    name: str
    """
    Volume name.
    """

    export_uri: Optional[str]
    """
    Show the volume NBD export URI.
    :deprecated
    """

    size: int
    """
    Volume disk size.
    """

    volume_type: VolumeVolumeType
    """
    Volume type.
    """

    creation_date: Optional[datetime]
    """
    Volume creation date.
    """

    modification_date: Optional[datetime]
    """
    Volume modification date.
    """

    organization: str
    """
    Volume Organization ID.
    """

    project: str
    """
    Volume Project ID.
    """

    tags: List[str]
    """
    Volume tags.
    """

    server: Optional[ServerSummary]
    """
    Instance attached to the volume.
    """

    state: VolumeState
    """
    Volume state.
    """

    zone: Zone
    """
    Zone in which the volume is located.
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
    Volume server template.
    """

    id: str
    """
    UUID of the volume.
    """

    boot: bool
    """
    Force the Instance to boot on this volume.
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

    base_snapshot: str
    """
    ID of the snapshot on which this volume will be based.
    """

    organization: str
    """
    Organization ID of the volume.
    """

    project: str
    """
    Project ID of the volume.
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
    Volume template.
    """

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
    Zone to target. If none is passed will use default zone from the config.
    """

    per_page: Optional[int]

    page: Optional[int]


@dataclass
class ListServersTypesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    per_page: Optional[int]

    page: Optional[int]


@dataclass
class ListVolumesTypesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    per_page: Optional[int]

    page: Optional[int]


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


@dataclass
class DeleteServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_id: str


@dataclass
class GetServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_id: str
    """
    UUID of the Instance you want to get.
    """


@dataclass
class ListServerActionsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_id: str


@dataclass
class ServerActionRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_id: str
    """
    UUID of the Instance.
    """

    action: ServerAction
    """
    Action to perform on the Instance.
    """

    name: Optional[str]
    """
    Name of the backup you want to create.
    Name of the backup you want to create.
    This field should only be specified when performing a backup action.
    """

    volumes: Optional[Dict[str, ServerActionRequestVolumeBackupTemplate]]
    """
    For each volume UUID, the snapshot parameters of the volume.
    For each volume UUID, the snapshot parameters of the volume.
    This field should only be specified when performing a backup action.
    """


@dataclass
class ListServerUserDataRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_id: str
    """
    UUID of the Instance.
    """


@dataclass
class DeleteServerUserDataRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_id: str
    """
    UUID of the Instance.
    """

    key: str
    """
    Key of the user data to delete.
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
class GetImageRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    image_id: str
    """
    UUID of the image you want to get.
    """


@dataclass
class CreateImageRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name of the image.
    """

    root_volume: str
    """
    UUID of the snapshot.
    """

    arch: Optional[Arch]
    """
    Architecture of the image.
    """

    default_bootscript: Optional[str]
    """
    Default bootscript of the image.
    :deprecated
    """

    extra_volumes: Optional[Dict[str, VolumeTemplate]]
    """
    Additional volumes of the image.
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
    Tags of the image.
    """

    public: Optional[bool]
    """
    True to create a public image.
    """


@dataclass
class DeleteImageRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    image_id: str
    """
    UUID of the image you want to delete.
    """


@dataclass
class ListSnapshotsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
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
    Volume type of the snapshot.
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


@dataclass
class GetSnapshotRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    snapshot_id: str
    """
    UUID of the snapshot you want to get.
    """


@dataclass
class DeleteSnapshotRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    snapshot_id: str
    """
    UUID of the snapshot you want to delete.
    """


@dataclass
class ExportSnapshotRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    snapshot_id: str
    """
    Snapshot ID.
    """

    bucket: str
    """
    S3 bucket name.
    """

    key: str
    """
    S3 object key.
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
class CreateVolumeRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Volume name.
    """

    organization: Optional[str]
    """
    Volume Organization ID.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    :deprecated
    """

    project: Optional[str]
    """
    Volume Project ID.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    """

    tags: Optional[List[str]]
    """
    Volume tags.
    """

    volume_type: VolumeVolumeType
    """
    Volume type.
    """

    size: Optional[int]
    """
    Volume disk size, must be a multiple of 512.
    
    One-of ('from_'): at most one of 'size', 'base_volume', 'base_snapshot' could be set.
    """

    base_volume: Optional[str]
    """
    ID of the volume on which this volume will be based.
    
    One-of ('from_'): at most one of 'size', 'base_volume', 'base_snapshot' could be set.
    """

    base_snapshot: Optional[str]
    """
    ID of the snapshot on which this volume will be based.
    
    One-of ('from_'): at most one of 'size', 'base_volume', 'base_snapshot' could be set.
    """


@dataclass
class GetVolumeRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_id: str
    """
    UUID of the volume you want to get.
    """


@dataclass
class UpdateVolumeRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_id: str
    """
    UUID of the volume.
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
class DeleteVolumeRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_id: str
    """
    UUID of the volume you want to delete.
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
class CreateSecurityGroupRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name of the security group.
    """

    description: str
    """
    Description of the security group.
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
    Tags of the security group.
    """

    organization_default: Optional[bool]
    """
    Defines whether this security group becomes the default security group for new Instances.
    
    One-of ('default_identifier'): at most one of 'organization_default', 'project_default' could be set.
    :deprecated
    """

    project_default: Optional[bool]
    """
    Whether this security group becomes the default security group for new Instances.
    
    One-of ('default_identifier'): at most one of 'organization_default', 'project_default' could be set.
    """

    stateful: bool
    """
    Whether the security group is stateful or not.
    """

    inbound_default_policy: SecurityGroupPolicy
    """
    Default policy for inbound rules.
    """

    outbound_default_policy: SecurityGroupPolicy
    """
    Default policy for outbound rules.
    """

    enable_default_security: Optional[bool]
    """
    True to block SMTP on IPv4 and IPv6. This feature is read only, please open a support ticket if you need to make it configurable.
    """


@dataclass
class GetSecurityGroupRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    security_group_id: str
    """
    UUID of the security group you want to get.
    """


@dataclass
class DeleteSecurityGroupRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    security_group_id: str
    """
    UUID of the security group you want to delete.
    """


@dataclass
class ListDefaultSecurityGroupRulesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListSecurityGroupRulesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    security_group_id: str
    """
    UUID of the security group.
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
class CreateSecurityGroupRuleRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    security_group_id: str
    """
    UUID of the security group.
    """

    protocol: Optional[SecurityGroupRuleProtocol]

    direction: Optional[SecurityGroupRuleDirection]

    action: Optional[SecurityGroupRuleAction]

    ip_range: str

    dest_port_from: Optional[int]
    """
    Beginning of the range of ports to apply this rule to (inclusive).
    """

    dest_port_to: Optional[int]
    """
    End of the range of ports to apply this rule to (inclusive).
    """

    position: int
    """
    Position of this rule in the security group rules list.
    """

    editable: bool
    """
    Indicates if this rule is editable (will be ignored).
    """


@dataclass
class SetSecurityGroupRulesRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    security_group_id: str
    """
    UUID of the security group to update the rules on.
    """

    rules: Optional[List[SetSecurityGroupRulesRequestRule]]
    """
    List of rules to update in the security group.
    """


@dataclass
class DeleteSecurityGroupRuleRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    security_group_id: str

    security_group_rule_id: str


@dataclass
class GetSecurityGroupRuleRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    security_group_id: str

    security_group_rule_id: str


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
class CreatePlacementGroupRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name of the placement group.
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
    Tags of the placement group.
    """

    policy_mode: PlacementGroupPolicyMode
    """
    Operating mode of the placement group.
    """

    policy_type: PlacementGroupPolicyType
    """
    Policy type of the placement group.
    """


@dataclass
class GetPlacementGroupRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    placement_group_id: str
    """
    UUID of the placement group you want to get.
    """


@dataclass
class SetPlacementGroupRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
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
    Zone to target. If none is passed will use default zone from the config.
    """

    placement_group_id: str
    """
    UUID of the placement group.
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
class DeletePlacementGroupRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    placement_group_id: str
    """
    UUID of the placement group you want to delete.
    """


@dataclass
class GetPlacementGroupServersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    placement_group_id: str
    """
    UUID of the placement group you want to get.
    """


@dataclass
class SetPlacementGroupServersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    placement_group_id: str
    """
    UUID of the placement group you want to set.
    """

    servers: List[str]
    """
    An array of the Instances' UUIDs you want to configure.
    """


@dataclass
class UpdatePlacementGroupServersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    placement_group_id: str
    """
    UUID of the placement group you want to update.
    """

    servers: List[str]
    """
    An array of the Instances' UUIDs you want to configure.
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


@dataclass
class CreateIpRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    organization: Optional[str]
    """
    Organization ID in which the IP is reserved.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    :deprecated
    """

    project: Optional[str]
    """
    Project ID in which the IP is reserved.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    """

    tags: Optional[List[str]]
    """
    Tags of the IP.
    """

    server: Optional[str]
    """
    UUID of the Instance you want to attach the IP to.
    """


@dataclass
class GetIpRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    ip: str
    """
    IP ID or address to get.
    """


@dataclass
class UpdateIpRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    ip: str
    """
    IP ID or IP address.
    """

    reverse: Optional[str]
    """
    Reverse domain name.
    """

    tags: Optional[List[str]]
    """
    An array of keywords you want to tag this IP with.
    """

    server: Optional[str]


@dataclass
class DeleteIpRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    ip: str
    """
    ID or address of the IP to delete.
    """


@dataclass
class ListPrivateNICsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_id: str
    """
    Instance to which the private NIC is attached.
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
class CreatePrivateNICRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_id: str
    """
    UUID of the Instance the private NIC will be attached to.
    """

    private_network_id: str
    """
    UUID of the private network where the private NIC will be attached.
    """

    tags: Optional[List[str]]
    """
    Private NIC tags.
    """


@dataclass
class GetPrivateNICRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_id: str
    """
    Instance to which the private NIC is attached.
    """

    private_nic_id: str
    """
    Private NIC unique ID.
    """


@dataclass
class UpdatePrivateNICRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_id: str
    """
    UUID of the Instance the private NIC will be attached to.
    """

    private_nic_id: str
    """
    Private NIC unique ID.
    """

    tags: Optional[List[str]]
    """
    Tags used to select private NIC/s.
    """


@dataclass
class DeletePrivateNICRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_id: str
    """
    Instance to which the private NIC is attached.
    """

    private_nic_id: str
    """
    Private NIC unique ID.
    """


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
class GetBootscriptRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    bootscript_id: str


@dataclass
class GetDashboardRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    organization: Optional[str]

    project: Optional[str]
