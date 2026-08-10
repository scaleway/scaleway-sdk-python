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


class CreateServerRequestBookIPIPType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_IP_TYPE = "unknown_ip_type"
    ZONAL_IPV4 = "zonal_ipv4"
    ZONAL_IPV6 = "zonal_ipv6"

    def __str__(self) -> str:
        return str(self.value)


class CreateServerRequestServerVolumeVolumeType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_VOLUME_TYPE = "unknown_volume_type"
    L_SSD = "l_ssd"
    SBS = "sbs"
    SCRATCH = "scratch"

    def __str__(self) -> str:
        return str(self.value)


class CreateVolumeRequestVolumeType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_VOLUME_TYPE = "unknown_volume_type"
    L_SSD = "l_ssd"
    SCRATCH = "scratch"

    def __str__(self) -> str:
        return str(self.value)


class ListPlacementGroupsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListPrivateNetworkInterfacesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListSecurityGroupsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListServersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListSnapshotsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListTemplatesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListVolumesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class PlacementGroupPolicyType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_POLICY_TYPE = "unknown_policy_type"
    LOW_LATENCY = "low_latency"
    MAX_AVAILABILITY = "max_availability"

    def __str__(self) -> str:
        return str(self.value)


class PrivateNetworkInterfaceStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    AVAILABLE = "available"
    ATTACHING = "attaching"
    DETACHING = "detaching"
    SYNCING = "syncing"

    def __str__(self) -> str:
        return str(self.value)


class SecurityGroupAction(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ACTION = "unknown_action"
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
    BOTH = "both"

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


class ServerArchitecture(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ARCHITECTURE = "unknown_architecture"
    X86_64 = "x86_64"
    AARCH64 = "aarch64"

    def __str__(self) -> str:
        return str(self.value)


class ServerFilesystemStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    ATTACHING = "attaching"
    AVAILABLE = "available"
    DETACHING = "detaching"

    def __str__(self) -> str:
        return str(self.value)


class ServerIPStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    DETACHED = "detached"
    ATTACHED = "attached"
    PENDING = "pending"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class ServerPrivateNetworkInterfaceStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    AVAILABLE = "available"
    ATTACHING = "attaching"
    DETACHING = "detaching"
    SYNCING = "syncing"

    def __str__(self) -> str:
        return str(self.value)


class ServerPublicNetworkInterfaceStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    AVAILABLE = "available"
    SYNCING = "syncing"

    def __str__(self) -> str:
        return str(self.value)


class ServerStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    STARTED = "started"
    STOPPED = "stopped"
    PAUSED = "paused"
    STARTING = "starting"
    STOPPING = "stopping"
    PAUSING = "pausing"
    LOCKED = "locked"
    REBOOTING = "rebooting"

    def __str__(self) -> str:
        return str(self.value)


class ServerTypeArchitecture(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ARCHITECTURE = "unknown_architecture"
    X86_64 = "x86_64"
    AARCH64 = "aarch64"

    def __str__(self) -> str:
        return str(self.value)


class ServerTypeAvailability(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_AVAILABILITY = "unknown_availability"
    AVAILABLE = "available"
    LOW_STOCK = "low_stock"
    OUT_OF_STOCK = "out_of_stock"

    def __str__(self) -> str:
        return str(self.value)


class ServerVolumeVolumeType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_VOLUME_TYPE = "unknown_volume_type"
    L_SSD = "l_ssd"
    SBS = "sbs"
    SCRATCH = "scratch"

    def __str__(self) -> str:
        return str(self.value)


class SnapshotStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    AVAILABLE = "available"
    CREATING = "creating"
    ERROR = "error"
    INVALID_DATA = "invalid_data"
    EXPORTING = "exporting"

    def __str__(self) -> str:
        return str(self.value)


class SnapshotVolumeType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_VOLUME_TYPE = "unknown_volume_type"
    L_SSD = "l_ssd"

    def __str__(self) -> str:
        return str(self.value)


class VolumeStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    AVAILABLE = "available"
    SNAPSHOTTING = "snapshotting"
    ATTACHING = "attaching"
    DETACHING = "detaching"
    CREATING = "creating"
    MIGRATING = "migrating"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class VolumeVolumeType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_VOLUME_TYPE = "unknown_volume_type"
    L_SSD = "l_ssd"
    SCRATCH = "scratch"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class SecurityGroupRulePortRange:
    start: int
    """
    Start of the port range.
    """

    end: int
    """
    End of the port range.
    """


@dataclass
class CreateServerRequestBookIP:
    type_: CreateServerRequestBookIPIPType
    """
    Type of IP to book.
    """

    tags: list[str]
    """
    Tags to associate with the IP.
    """


@dataclass
class SecurityGroupRule:
    id: str
    """
    Unique ID of the rule.
    """

    protocol: SecurityGroupRuleProtocol
    """
    Protocol this rule applies to.
    """

    direction: SecurityGroupRuleDirection
    """
    Direction of traffic this rule applies to.
    """

    action: SecurityGroupRuleAction
    """
    Action to take when the rule matches.
    """

    source_ip_range: str
    """
    Source IP range for the rule.
    """

    destination_ip_range: str
    """
    Destination IP range for the rule.
    """

    position: int
    """
    Position of the rule in the list.
    """

    source_ports: Optional[SecurityGroupRulePortRange] = None
    """
    Source port range for the rule.
    """

    destination_ports: Optional[SecurityGroupRulePortRange] = None
    """
    Destination port range for the rule.
    """


@dataclass
class CreateServerRequestServerIP:
    ipam_ip_id: Optional[str] = None

    new_ip: Optional[CreateServerRequestBookIP] = None


@dataclass
class CreateServerRequestCreateVolume:
    name: str
    """
    Name of the volume.
    """

    tags: list[str]
    """
    Tags to associate with the volume.
    """

    size: Optional[int] = 0
    """
    Size of the volume.
    """

    perf_iops: Optional[int] = 0
    """
    Performance IOPS for the volume.
    """

    base_snapshot_id: Optional[str] = None

    image_label: Optional[str] = None


@dataclass
class ServerTypeGpuInfo:
    manufacturer: str
    """
    Manufacturer of the GPU.
    """

    name: str
    """
    Name of the GPU.
    """

    memory: int
    """
    Memory of the GPU.
    """


@dataclass
class ServerTypeLimits:
    private_network_count: int
    """
    Maximum number of Private Networks.
    """

    file_system_count: int
    """
    Maximum number of filesystems.
    """

    private_network_bandwidth: int
    """
    Maximum Private Network bandwidth.
    """

    block_bandwidth: int
    """
    Maximum block storage bandwidth.
    """

    internet_bandwidth: int
    """
    Maximum internet bandwidth.
    """

    l_ssd_size: int
    """
    Maximum size of local SSD.
    """

    scratch_size: int
    """
    Maximum size of scratch storage.
    """

    scratch_volumes_count: int
    """
    Maximum number of scratch volumes.
    """

    ip_count: int
    """
    Maximum number of IPs.
    """

    volume_count: int
    """
    Maximum number of volumes.
    """


@dataclass
class ServerIP:
    id: str
    dynamic: bool
    status: ServerIPStatus
    default: bool


@dataclass
class CreateTemplateRequestPrivateNetworkTemplate:
    private_network_id: str
    """
    ID of the private network.
    """


@dataclass
class CreateTemplateRequestVolumeTemplate:
    volume_type: CreateServerRequestServerVolumeVolumeType
    """
    Type of the volume.
    """

    name: str
    """
    Name of the volume.
    """

    tags: list[str]
    """
    Tags associated with the volume.
    """

    size: Optional[int] = 0
    """
    Size of the volume in bytes.
    """

    perf_iops: Optional[int] = 0
    """
    Performance IOPS for the volume.
    """

    base_snapshot_id: Optional[str] = None

    image_label: Optional[str] = None


@dataclass
class SecurityGroupRuleConfig:
    protocol: SecurityGroupRuleProtocol
    """
    Protocol for the rule.
    """

    direction: SecurityGroupRuleDirection
    """
    Direction of traffic for the rule.
    """

    action: SecurityGroupRuleAction
    """
    Action to take when the rule matches.
    """

    source_ip_range: str
    """
    Source IP range for the rule.
    """

    destination_ip_range: str
    """
    Destination IP range for the rule.
    """

    position: int
    """
    Position of the rule in the list.
    """

    source_ports: Optional[SecurityGroupRulePortRange] = None
    """
    Source port range for the rule.
    """

    destination_ports: Optional[SecurityGroupRulePortRange] = None
    """
    Destination port range for the rule.
    """


@dataclass
class SecurityGroup:
    id: str
    """
    Unique ID of the security group.
    """

    name: str
    """
    Name of the security group.
    """

    description: str
    """
    Description of the security group.
    """

    project_id: str
    """
    Project ID the security group belongs to.
    """

    tags: list[str]
    """
    Tags associated with the security group.
    """

    disable_default_rules: bool
    """
    True if default rules are disabled.
    """

    project_default: bool
    """
    True if this is the default security group for the project.
    """

    inbound_default_action: SecurityGroupAction
    """
    Default action for inbound rules.
    """

    outbound_default_action: SecurityGroupAction
    """
    Default action for outbound rules.
    """

    stateless: bool
    """
    True if the security group is stateless.
    """

    default_rules: list[SecurityGroupRule]
    """
    List of default rules applied to the security group.
    """

    rules: list[SecurityGroupRule]
    """
    List of custom rules applied to the security group.
    """

    zone: ScwZone
    """
    Zone in which the security group is located.
    """

    created_at: Optional[datetime] = None
    """
    Creation timestamp of the security group.
    """

    updated_at: Optional[datetime] = None
    """
    Last update timestamp of the security group.
    """


@dataclass
class CreateServerRequestPublicNetworkInterface:
    ips: list[CreateServerRequestServerIP]
    """
    List of IPs to attach to the interface.
    """

    security_group_id: Optional[str] = None
    """
    ID of the security group for the interface.
    """


@dataclass
class CreateServerRequestServerVolume:
    volume_type: CreateServerRequestServerVolumeVolumeType
    """
    Type of the volume.
    """

    volume_id: Optional[str] = None

    new_volume: Optional[CreateServerRequestCreateVolume] = None


@dataclass
class PlacementGroup:
    id: str
    """
    Placement group unique ID.
    """

    project_id: str
    """
    Placement group Project ID.
    """

    name: str
    """
    Placement group name.
    """

    policy_type: PlacementGroupPolicyType
    """
    Select the behavior of the placement group, either low_latency (group) or max_availability (spread).
    """

    tags: list[str]
    """
    Placement group tags.
    """

    zone: ScwZone
    """
    Zone in which the placement group is located.
    """

    created_at: Optional[datetime] = None
    """
    Placement group creation date.
    """

    updated_at: Optional[datetime] = None
    """
    Placement group modification date.
    """


@dataclass
class PrivateNetworkInterfaceSummary:
    id: str
    """
    Unique ID of the private network interface.
    """

    private_network_id: str
    """
    ID of the Private Network this interface is attached to.
    """

    project_id: str
    """
    Project ID the private network interface belongs to.
    """

    server_id: str
    """
    ID of the Instance this interface is attached to.
    """

    mac_address: str
    """
    MAC address of the private network interface.
    """

    status: PrivateNetworkInterfaceStatus
    """
    Current status of the private network interface.
    """

    ip_ids: list[str]
    """
    List of IP IDs attached to this interface.
    """

    tags: list[str]
    """
    Tags associated with the private network interface.
    """

    created_at: Optional[datetime] = None
    """
    Creation timestamp of the private network interface.
    """

    updated_at: Optional[datetime] = None
    """
    Last update timestamp of the private network interface.
    """


@dataclass
class SecurityGroupSummary:
    id: str
    """
    Unique ID of the security group.
    """

    name: str
    """
    Name of the security group.
    """

    description: str
    """
    Description of the security group.
    """

    project_id: str
    """
    Project ID the security group belongs to.
    """

    tags: list[str]
    """
    Tags associated with the security group.
    """

    disable_default_rules: bool
    """
    True if default rules are disabled.
    """

    project_default: bool
    """
    True if this is the default security group for the project.
    """

    inbound_default_action: SecurityGroupAction
    """
    Default action for inbound rules.
    """

    outbound_default_action: SecurityGroupAction
    """
    Default action for outbound rules.
    """

    stateless: bool
    """
    True if the security group is stateless.
    """

    created_at: Optional[datetime] = None
    """
    Creation timestamp of the security group.
    """

    updated_at: Optional[datetime] = None
    """
    Last update timestamp of the security group.
    """


@dataclass
class ServerType:
    name: str
    """
    Name of the server type.
    """

    vcpu_count: int
    """
    Number of vCPUs.
    """

    gpu_count: int
    """
    Number of GPUs.
    """

    memory: int
    """
    Amount of memory.
    """

    architecture: ServerTypeArchitecture
    """
    Architecture of the server type.
    """

    availability: ServerTypeAvailability
    """
    Availability status of the server type.
    """

    end_of_service: bool
    """
    Whether the server type has reached end of service.
    """

    limits: Optional[ServerTypeLimits] = None
    """
    Limits for the server type.
    """

    gpu_info: Optional[ServerTypeGpuInfo] = None
    """
    GPU information for the server type.
    """


@dataclass
class ServerSummary:
    id: str
    """
    Unique ID of the server.
    """

    name: str
    """
    Name of the server.
    """

    project_id: str
    """
    Project ID to which the server belongs.
    """

    tags: list[str]
    """
    Tags associated with the server.
    """

    server_type: str
    """
    Type of the server.
    """

    status: ServerStatus
    """
    Current status of the server.
    """

    architecture: ServerArchitecture
    """
    Architecture of the server.
    """

    rescue_mode: bool
    """
    Whether the server is in rescue mode.
    """

    placement_group_id: Optional[str] = None
    """
    ID of the placement group the server belongs to.
    """

    created_at: Optional[datetime] = None
    """
    Creation timestamp of the server.
    """

    updated_at: Optional[datetime] = None
    """
    Last update timestamp of the server.
    """


@dataclass
class Snapshot:
    id: str
    """
    Unique ID of the snapshot.
    """

    project_id: str
    """
    Project ID of the snapshot.
    """

    name: str
    """
    Name of the snapshot.
    """

    tags: list[str]
    """
    Tags associated with the snapshot.
    """

    size: int
    """
    Size of the snapshot in bytes.
    """

    status: SnapshotStatus
    """
    Current status of the snapshot.
    """

    volume_type: SnapshotVolumeType
    """
    Type of the volume.
    """

    zone: ScwZone
    """
    Zone in which the snapshot is located.
    """

    public: bool
    """
    Whether the snapshot is public.
    """

    base_volume_id: Optional[str] = None
    """
    ID of the base volume.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the snapshot.
    """

    updated_at: Optional[datetime] = None
    """
    Last update date of the snapshot.
    """


@dataclass
class TemplateSummary:
    project_id: str
    """
    Project ID associated with the template.
    """

    id: str
    """
    Unique ID of the template.
    """

    name: str
    """
    Name of the template.
    """

    tags: list[str]
    """
    Tags associated with the template.
    """

    server_tags: list[str]
    """
    Tags associated with servers created from this template.
    """

    server_type: str
    """
    Commercial type of the server defined by the template.
    """

    public_ip_v4_count: int
    """
    Number of IPv4 public IPs to attach to servers created from this template.
    """

    public_ip_v6_count: int
    """
    Number of IPv6 public IPs to attach to servers created from this template.
    """

    filesystem_ids: list[str]
    """
    List of Filesystem IDs associated with the template.
    """

    zone: ScwZone
    """
    Zone in which the template is located.
    """

    security_group_id: Optional[str] = None
    """
    Security group ID associated with the template.
    """

    placement_group_id: Optional[str] = None
    """
    Placement group ID associated with the template.
    """

    created_at: Optional[datetime] = None
    """
    Creation timestamp of the template.
    """

    updated_at: Optional[datetime] = None
    """
    Last update timestamp of the template.
    """


@dataclass
class VolumeType:
    name: VolumeVolumeType
    """
    Name of the volume type.
    """

    min_size: int
    """
    Minimum size of the volume in bytes.
    """

    max_size: int
    """
    Maximum size of the volume in bytes.
    """


@dataclass
class Volume:
    id: str
    """
    Unique ID of the volume.
    """

    project_id: str
    """
    Project ID to which the volume belongs.
    """

    name: str
    """
    Volume name.
    """

    tags: list[str]
    """
    Tags associated with the volume.
    """

    size: int
    """
    Volume size in bytes.
    """

    status: VolumeStatus
    """
    Current status of the volume.
    """

    volume_type: VolumeVolumeType
    """
    Type of the volume.
    """

    zone: ScwZone
    """
    Zone in which the volume is located.
    """

    base_snapshot_id: Optional[str] = None
    """
    ID of the base snapshot used for this volume.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the volume.
    """

    updated_at: Optional[datetime] = None
    """
    Last update date of the volume.
    """

    server_id: Optional[str] = None
    """
    ID of the Instance to which the volume is attached.
    """


@dataclass
class ServerFilesystem:
    id: str
    status: ServerFilesystemStatus


@dataclass
class ServerPrivateNetworkInterface:
    id: str
    private_network_id: str
    mac_address: str
    status: ServerPrivateNetworkInterfaceStatus
    ip_ids: list[str]
    security_group_id: str


@dataclass
class ServerPublicNetworkInterface:
    status: ServerPublicNetworkInterfaceStatus
    mac_address: str
    security_group_id: str
    ips: list[ServerIP]
    dns: str


@dataclass
class ServerRDPPassword:
    encrypted_password: str
    rdp_ssh_key_id: str


@dataclass
class ServerVolume:
    id: str
    volume_type: ServerVolumeVolumeType


@dataclass
class UpdateServerRequestPublicNetworkInterface:
    security_group_id: Optional[str] = None
    """
    ID of the security group for the interface.
    """


@dataclass
class UpdateTemplateRequestUpdatePrivateNetworks:
    private_networks: list[CreateTemplateRequestPrivateNetworkTemplate]
    """
    List of updated private networks.
    """


@dataclass
class UpdateTemplateRequestUpdateVolumes:
    volumes: list[CreateTemplateRequestVolumeTemplate]
    """
    List of updated volume templates.
    """


@dataclass
class AddSecurityGroupRulesRequest:
    security_group_id: str
    """
    ID of the security group to add rules to.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    security_group_rules: Optional[list[SecurityGroupRuleConfig]] = field(
        default_factory=list
    )
    """
    List of rules to add.
    """


@dataclass
class AddSecurityGroupRulesResponse:
    added_rules: list[SecurityGroupRule]
    """
    List of rules that were added.
    """

    security_group: Optional[SecurityGroup] = None
    """
    Updated security group.
    """


@dataclass
class AttachServerFileSystemRequest:
    server_id: str
    """
    ID of the server to attach the filesystem to.
    """

    filesystem_id: str
    """
    ID of the filesystem to attach.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class AttachServerIPRequest:
    server_id: str
    """
    ID of the server to attach the IP to.
    """

    ip_id: str
    """
    ID of the IP to attach.
    """

    default: bool
    """
    Whether the IP should be the default IP.
    """

    move_allowed: bool
    """
    Whether moving the IP is allowed.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class AttachServerPrivateNetworkInterfaceRequest:
    server_id: str
    """
    ID of the server to attach the private network interface to.
    """

    private_network_interface_id: str
    """
    ID of the private network interface to attach.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class AttachServerVolumeRequest:
    server_id: str
    """
    ID of the server to attach the volume to.
    """

    volume_id: str
    """
    ID of the volume to attach.
    """

    boot_volume: bool
    """
    Whether the volume should be used as the boot volume.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_type: Optional[ServerVolumeVolumeType] = (
        ServerVolumeVolumeType.UNKNOWN_VOLUME_TYPE
    )
    """
    Type of the volume.
    """


@dataclass
class CheckTemplateRequest:
    template_id: str
    """
    Unique ID of the template to check.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class CreatePlacementGroupRequest:
    name: str
    """
    Name of the placement group.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    """
    Project ID of the placement group.
    """

    policy_type: Optional[PlacementGroupPolicyType] = (
        PlacementGroupPolicyType.UNKNOWN_POLICY_TYPE
    )
    """
    Policy type of the placement group.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the placement group.
    """


@dataclass
class CreatePrivateNetworkInterfaceRequest:
    private_network_id: str
    """
    ID of the Private Network to attach to.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    """
    Project ID for the private network interface.
    """

    server_id: Optional[str] = None
    """
    ID of the Instance to attach the interface to.
    """

    ip_ids: Optional[list[str]] = field(default_factory=list)
    """
    List of IP IDs to attach to the interface.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to assign to the private network interface.
    """


@dataclass
class CreateSecurityGroupRequest:
    name: str
    """
    Name of the security group.
    """

    description: str
    """
    Description of the security group.
    """

    disable_default_rules: bool
    """
    Whether to disable default rules.
    """

    project_default: bool
    """
    Whether this should be the default security group for the project.
    """

    stateless: bool
    """
    Whether the security group should be stateless.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    """
    Project ID the security group belongs to.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags for the security group.
    """

    inbound_default_action: Optional[SecurityGroupAction] = (
        SecurityGroupAction.UNKNOWN_ACTION
    )
    """
    Default action for inbound rules.
    """

    outbound_default_action: Optional[SecurityGroupAction] = (
        SecurityGroupAction.UNKNOWN_ACTION
    )
    """
    Default action for outbound rules.
    """


@dataclass
class CreateServerFromTemplateRequest:
    template_id: str
    """
    Unique ID of the template to use.
    """

    name: str
    """
    Name of the new server.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class CreateServerRequest:
    name: str
    """
    Name of the server.
    """

    server_type: str
    """
    Type of the server.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    """
    Project ID for the server.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to associate with the server.
    """

    placement_group_id: Optional[str] = None
    """
    ID of the placement group the server belongs to.
    """

    volumes: Optional[list[CreateServerRequestServerVolume]] = field(
        default_factory=list
    )
    """
    Volumes to attach to the server.
    """

    windows_rdp_ssh_key_id: Optional[str] = None
    """
    IAM ID of the SSH key used to encrypt the Windows `Administrator` password for RDP use.
    """

    public_network_interface: Optional[CreateServerRequestPublicNetworkInterface] = None
    """
    Public network interface configuration.
    """


@dataclass
class CreateTemplateRequest:
    name: str
    """
    Name of the template.
    """

    server_type: str
    """
    Commercial type of the server defined by the template.
    """

    public_ip_v4_count: int
    """
    Number of IPv4 public IPs to attach to servers created from this template.
    """

    public_ip_v6_count: int
    """
    Number of IPv6 public IPs to attach to servers created from this template.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    """
    Project ID for the template.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to associate with the template.
    """

    server_tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to associate with servers created from the template.
    """

    security_group_id: Optional[str] = None
    """
    Security group ID for the template.
    """

    placement_group_id: Optional[str] = None
    """
    Placement group ID for the template.
    """

    volumes: Optional[list[CreateTemplateRequestVolumeTemplate]] = field(
        default_factory=list
    )
    """
    List of volume templates to define volumes for servers.
    """

    private_networks: Optional[list[CreateTemplateRequestPrivateNetworkTemplate]] = (
        field(default_factory=list)
    )
    """
    List of private networks to associate with the template.
    """

    filesystem_ids: Optional[list[str]] = field(default_factory=list)
    """
    List of filesystem IDs to associate with the template.
    """

    windows_rdp_ssh_key_id: Optional[str] = None
    """
    IAM ID of the SSH key used to encrypt the Windows `Administrator` password for RDP use.
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
class DeletePrivateNetworkInterfaceRequest:
    private_network_interface_id: str
    """
    ID of the private network interface to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteSecurityGroupRequest:
    security_group_id: str
    """
    ID of the security group to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteSecurityGroupRulesRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    security_group_rule_ids: Optional[list[str]] = field(default_factory=list)
    """
    List of rule IDs to delete.
    """


@dataclass
class DeleteServerRequest:
    server_id: str
    """
    ID of the server to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    delete_all_ips: Optional[bool] = False

    delete_ip_ids: Optional[list[str]] = field(default_factory=list)

    delete_all_volumes: Optional[bool] = False

    delete_volume_ids: Optional[list[str]] = field(default_factory=list)

    keep_all_private_nics: Optional[bool] = False

    delete_private_nic_ids: Optional[list[str]] = field(default_factory=list)


@dataclass
class DeleteTemplateRequest:
    template_id: str
    """
    Unique ID of the template to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteTemplateUserDataRequest:
    template_id: str
    """
    Unique ID of the template.
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
class DeleteUserDataRequest:
    server_id: str
    """
    The ID of the server.
    """

    key: str
    """
    The key of the user data to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DetachServerFileSystemRequest:
    server_id: str
    """
    ID of the server to detach the filesystem from.
    """

    filesystem_id: str
    """
    ID of the filesystem to detach.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DetachServerIPRequest:
    server_id: str
    """
    ID of the server to detach the IP from.
    """

    ip_id: str
    """
    ID of the IP to detach.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DetachServerPrivateNetworkInterfaceRequest:
    server_id: str
    """
    ID of the server to detach the private network interface from.
    """

    private_network_interface_id: str
    """
    ID of the private network interface to detach.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DetachServerVolumeRequest:
    server_id: str
    """
    ID of the server to detach the volume from.
    """

    volume_id: str
    """
    ID of the volume to detach.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


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
class GetPrivateNetworkInterfaceRequest:
    private_network_interface_id: str
    """
    ID of the private network interface to retrieve.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetResourceCountsRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    organization_id: Optional[str] = None

    project_id: Optional[str] = None


@dataclass
class GetSecurityGroupRequest:
    security_group_id: str
    """
    ID of the security group to retrieve.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerCloudInitRequest:
    server_id: str
    """
    The ID of the server.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerRequest:
    server_id: str
    """
    ID of the server to retrieve.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetTemplateCloudInitRequest:
    template_id: str
    """
    Unique ID of the template.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetTemplateRequest:
    template_id: str
    """
    Unique ID of the template to retrieve.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetTemplateUserDataRequest:
    template_id: str
    """
    Unique ID of the template.
    """

    key: str
    """
    Key of the user data to retrieve.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetUserDataRequest:
    server_id: str
    """
    The ID of the server.
    """

    key: str
    """
    The key of the user data to retrieve.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListPlacementGroupsRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    """
    The initial pagination token to start from.
    """

    page_size: Optional[int] = 0
    """
    The maximum number of placement groups to return.
    """

    order_by: Optional[ListPlacementGroupsRequestOrderBy] = (
        ListPlacementGroupsRequestOrderBy.CREATED_AT_DESC
    )
    """
    The field by which to order the result list.
    """

    project_id: Optional[str] = None
    """
    List only placement groups of this Project ID.
    """

    placement_group_ids: Optional[list[str]] = field(default_factory=list)
    """
    List only placement groups with these IDs.
    """

    name: Optional[str] = None
    """
    Filter placement groups by name.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List placement groups with these exact tags.
    """


@dataclass
class ListPlacementGroupsResponse:
    placement_groups: list[PlacementGroup]
    """
    List of placement groups.
    """

    total_count: int
    """
    Total number of placement groups.
    """

    next_page_token: Optional[str] = None
    """
    The pagination token, use it to get the next page of results.
    """


@dataclass
class ListPrivateNetworkInterfacesRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    """
    Token for pagination.
    """

    page_size: Optional[int] = 0
    """
    Number of items to return per page.
    """

    order_by: Optional[ListPrivateNetworkInterfacesRequestOrderBy] = (
        ListPrivateNetworkInterfacesRequestOrderBy.CREATED_AT_DESC
    )
    """
    Field to order results by.
    """

    project_id: Optional[str] = None
    """
    Filter by Project ID.
    """

    server_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter by server IDs.
    """

    private_network_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter by Private Network IDs.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Filter by tags.
    """


@dataclass
class ListPrivateNetworkInterfacesResponse:
    private_network_interfaces: list[PrivateNetworkInterfaceSummary]
    """
    List of private network interfaces.
    """

    total_count: int
    """
    Total number of items.
    """

    next_page_token: Optional[str] = None
    """
    Token for the next page.
    """


@dataclass
class ListSecurityGroupsRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    """
    Token for pagination.
    """

    page_size: Optional[int] = 0
    """
    Number of items to return per page.
    """

    order_by: Optional[ListSecurityGroupsRequestOrderBy] = (
        ListSecurityGroupsRequestOrderBy.CREATED_AT_DESC
    )
    """
    Field and direction to sort by.
    """

    project_id: Optional[str] = None
    """
    Filter by Project ID.
    """

    name: Optional[str] = None
    """
    Filter by name.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Filter by tags.
    """

    security_group_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter by specific security group IDs.
    """


@dataclass
class ListSecurityGroupsResponse:
    security_groups: list[SecurityGroupSummary]
    """
    List of security groups.
    """

    total_count: int
    """
    Total number of items.
    """

    next_page_token: Optional[str] = None
    """
    Token for the next page.
    """


@dataclass
class ListServerTypesRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    """
    Token for pagination.
    """

    page_size: Optional[int] = 0
    """
    Number of server types to return per page.
    """


@dataclass
class ListServerTypesResponse:
    server_types: list[ServerType]
    """
    List of server types.
    """

    total_count: int
    """
    Total number of server types.
    """

    next_page_token: Optional[str] = None
    """
    Token for the next page.
    """


@dataclass
class ListServersRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    """
    Token for pagination.
    """

    page_size: Optional[int] = 0
    """
    Number of servers to return per page.
    """

    order_by: Optional[ListServersRequestOrderBy] = (
        ListServersRequestOrderBy.CREATED_AT_DESC
    )
    """
    Order of the returned servers.
    """

    project_id: Optional[str] = None
    """
    Project ID to filter servers.
    """

    server_ids: Optional[list[str]] = field(default_factory=list)
    """
    List of server IDs to filter.
    """

    name: Optional[str] = None
    """
    Name to filter servers.
    """

    server_type: Optional[str] = None
    """
    Server type to filter.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to filter servers.
    """

    security_group_ids: Optional[list[str]] = field(default_factory=list)
    """
    Security group IDs to filter servers.
    """

    placement_group_ids: Optional[list[str]] = field(default_factory=list)
    """
    Placement group IDs to filter servers.
    """

    private_network_ids: Optional[list[str]] = field(default_factory=list)
    """
    Private Network IDs to filter servers.
    """

    mac_addresses: Optional[list[str]] = field(default_factory=list)
    """
    MAC addresses to filter servers.
    """


@dataclass
class ListServersResponse:
    servers: list[ServerSummary]
    """
    List of servers.
    """

    total_count: int
    """
    Total number of servers.
    """

    next_page_token: Optional[str] = None
    """
    Token for the next page.
    """


@dataclass
class ListSnapshotsResponse:
    snapshots: list[Snapshot]
    """
    List of snapshots.
    """

    total_count: int
    """
    Total number of items.
    """

    next_page_token: Optional[str] = None
    """
    Token for the next page.
    """


@dataclass
class ListTemplateUserDataKeysRequest:
    template_id: str
    """
    Unique ID of the template.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    """
    Token for pagination.
    """

    page_size: Optional[int] = 0
    """
    Number of items to return per page.
    """


@dataclass
class ListTemplateUserDataKeysResponse:
    keys: list[str]
    """
    List of user data keys associated with the template.
    """

    total_count: int
    """
    Total number of items.
    """

    next_page_token: Optional[str] = None
    """
    Token for the next page.
    """


@dataclass
class ListTemplatesRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    """
    Token for pagination.
    """

    page_size: Optional[int] = 0
    """
    Number of items to return per page.
    """

    order_by: Optional[ListTemplatesRequestOrderBy] = (
        ListTemplatesRequestOrderBy.CREATED_AT_DESC
    )
    """
    Field to sort results by.
    """

    project_id: Optional[str] = None
    """
    Filter by Project ID.
    """

    template_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter by specific template IDs.
    """

    name: Optional[str] = None
    """
    Filter by template name.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Filter by tags.
    """

    server_tags: Optional[list[str]] = field(default_factory=list)
    """
    Filter by server tags.
    """

    security_group_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter by security group IDs.
    """

    placement_group_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter by placement group IDs.
    """


@dataclass
class ListTemplatesResponse:
    templates: list[TemplateSummary]
    """
    List of template summaries.
    """

    total_count: int
    """
    Total number of items.
    """

    next_page_token: Optional[str] = None
    """
    Token for the next page.
    """


@dataclass
class ListUserDataKeysRequest:
    server_id: str
    """
    The ID of the server.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    """
    Page token for pagination.
    """

    page_size: Optional[int] = 0
    """
    Number of items to return per page.
    """


@dataclass
class ListUserDataKeysResponse:
    keys: list[str]
    """
    List of user data keys.
    """

    total_count: int
    """
    Total number of items.
    """

    next_page_token: Optional[str] = None
    """
    Token for the next page.
    """


@dataclass
class ListVolumeTypesResponse:
    volume_types: list[VolumeType]
    """
    List of volume types.
    """

    total_count: int
    """
    Total number of items.
    """

    next_page_token: Optional[str] = None
    """
    Token for the next page.
    """


@dataclass
class ListVolumesResponse:
    volumes: list[Volume]
    """
    List of volumes.
    """

    total_count: int
    """
    Total number of items.
    """

    next_page_token: Optional[str] = None
    """
    Token for the next page.
    """


@dataclass
class PauseServerRequest:
    server_id: str
    """
    ID of the server to pause.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class PrivateNetworkInterface:
    id: str
    """
    Unique ID of the private network interface.
    """

    private_network_id: str
    """
    ID of the Private Network this interface is attached to.
    """

    project_id: str
    """
    Project ID the private network interface belongs to.
    """

    server_id: str
    """
    ID of the Instance this interface is attached to.
    """

    mac_address: str
    """
    MAC address of the private network interface.
    """

    status: PrivateNetworkInterfaceStatus
    """
    Current status of the private network interface.
    """

    ip_ids: list[str]
    """
    List of IP IDs attached to this interface.
    """

    tags: list[str]
    """
    Tags associated with the private network interface.
    """

    created_at: Optional[datetime] = None
    """
    Creation timestamp of the private network interface.
    """

    updated_at: Optional[datetime] = None
    """
    Last update timestamp of the private network interface.
    """


@dataclass
class RebootServerRequest:
    server_id: str
    """
    ID of the server to reboot.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ResourceCounts:
    servers: int
    """
    Number of servers.
    """

    gpu_servers: int
    """
    Number of GPU servers.
    """

    servers_by_type: dict[str, int]
    """
    Map of server types with their counts.
    """

    security_groups: int
    """
    Number of security groups.
    """

    placement_groups: int
    """
    Number of placement groups.
    """

    snapshots: int
    """
    Number of snapshots.
    """

    volumes: int
    """
    Number of volumes.
    """

    volumes_l_ssd: int
    """
    Number of local SSD volumes.
    """

    volumes_l_ssd_total_size: int
    """
    Total size of local SSD volumes in bytes.
    """

    volumes_scratch: int
    """
    Number of scratch volumes.
    """

    private_network_interfaces: int
    """
    Number of private network interfaces.
    """

    templates: int
    """
    Number of templates.
    """

    flexible_ips: int
    """
    Number of flexible IPs.
    """

    unused_flexible_ips: int
    """
    Number of flexible IPs not attached to any server.
    """

    images: int
    """
    Number of images.
    """


@dataclass
class Server:
    id: str
    """
    Unique ID of the server.
    """

    name: str
    """
    Name of the server.
    """

    project_id: str
    """
    Project ID to which the server belongs.
    """

    tags: list[str]
    """
    Tags associated with the server.
    """

    server_type: str
    """
    Type of the server.
    """

    status: ServerStatus
    """
    Current status of the server.
    """

    volumes: list[ServerVolume]
    """
    List of volumes attached to the server.
    """

    filesystems: list[ServerFilesystem]
    """
    List of filesystems attached to the server.
    """

    architecture: ServerArchitecture
    """
    Architecture of the server.
    """

    private_network_interfaces: list[ServerPrivateNetworkInterface]
    """
    List of private network interfaces attached to the server.
    """

    rescue_mode: bool
    """
    Whether the server is in rescue mode.
    """

    status_detail: str
    """
    Detailed status information of the server.
    """

    zone: ScwZone
    """
    Zone in which the server is located.
    """

    placement_group_id: Optional[str] = None
    """
    ID of the placement group the server belongs to.
    """

    created_at: Optional[datetime] = None
    """
    Creation timestamp of the server.
    """

    updated_at: Optional[datetime] = None
    """
    Last update timestamp of the server.
    """

    boot_volume_id: Optional[str] = None
    """
    ID of the boot volume.
    """

    windows_rdp_password: Optional[ServerRDPPassword] = None
    """
    Encrypted RDP password for Windows servers. The encryption scheme is RSA-PKCS1-v1_5, using the public part of the SSH key supplied in `windows_rdp_ssh_key_id`.
    """

    public_network_interface: Optional[ServerPublicNetworkInterface] = None
    """
    Public network interface of the server.
    """


@dataclass
class SetSecurityGroupRulesRequest:
    security_group_id: str
    """
    ID of the security group to set rules for.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    security_group_rules: Optional[list[SecurityGroupRuleConfig]] = field(
        default_factory=list
    )
    """
    List of rules to set.
    """


@dataclass
class SetServerCloudInitRequest:
    server_id: str
    """
    The ID of the server.
    """

    content: str
    """
    The cloud-init configuration content.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetServerDefaultIPRequest:
    server_id: str
    """
    ID of the server to set the default IP for.
    """

    ip_id: str
    """
    ID of the IP to set as default.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetTemplateCloudInitRequest:
    template_id: str
    """
    Unique ID of the template.
    """

    content: str
    """
    Cloud-init configuration content.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetTemplateUserDataRequest:
    template_id: str
    """
    Unique ID of the template.
    """

    key: str
    """
    Key of the user data to set.
    """

    content: str
    """
    Content of the user data.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetUserDataRequest:
    server_id: str
    """
    The ID of the server.
    """

    key: str
    """
    The key of the user data to set.
    """

    content: str
    """
    The content to set for the user data.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class StartServerRequest:
    server_id: str
    """
    ID of the server to start.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class StopAndDeleteServerRequest:
    server_id: str
    """
    ID of the server to stop and delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    delete_all_ips: Optional[bool] = False

    delete_ip_ids: Optional[list[str]] = field(default_factory=list)

    delete_all_volumes: Optional[bool] = False

    delete_volume_ids: Optional[list[str]] = field(default_factory=list)

    keep_all_private_nics: Optional[bool] = False

    delete_private_nic_ids: Optional[list[str]] = field(default_factory=list)


@dataclass
class StopServerRequest:
    server_id: str
    """
    ID of the server to stop.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class Template:
    project_id: str
    """
    Project ID associated with the template.
    """

    id: str
    """
    Unique ID of the template.
    """

    name: str
    """
    Name of the template.
    """

    tags: list[str]
    """
    Tags associated with the template.
    """

    server_tags: list[str]
    """
    Tags associated with servers created from this template.
    """

    server_type: str
    """
    Commercial type of the server defined by the template.
    """

    public_ip_v4_count: int
    """
    Number of IPv4 public IPs to attach to servers created from this template.
    """

    public_ip_v6_count: int
    """
    Number of IPv6 public IPs to attach to servers created from this template.
    """

    volumes: list[CreateTemplateRequestVolumeTemplate]
    """
    List of volume templates used to create volumes for servers.
    """

    private_networks: list[CreateTemplateRequestPrivateNetworkTemplate]
    """
    List of private network associated with the template.
    """

    filesystem_ids: list[str]
    """
    List of filesystem IDs associated with the template.
    """

    zone: ScwZone
    """
    Zone in which the template is located.
    """

    security_group_id: Optional[str] = None
    """
    Security group ID associated with the template.
    """

    placement_group_id: Optional[str] = None
    """
    Placement group ID associated with the template.
    """

    created_at: Optional[datetime] = None
    """
    Creation timestamp of the template.
    """

    updated_at: Optional[datetime] = None
    """
    Last update timestamp of the template.
    """

    windows_rdp_ssh_key_id: Optional[str] = None
    """
    IAM ID of the SSH key used to encrypt the Windows `Administrator` password for RDP use.
    """


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

    policy_type: Optional[PlacementGroupPolicyType] = (
        PlacementGroupPolicyType.UNKNOWN_POLICY_TYPE
    )
    """
    Policy type of the placement group.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the placement group.
    """


@dataclass
class UpdatePrivateNetworkInterfaceRequest:
    private_network_interface_id: str
    """
    ID of the private network interface to update.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    New tags to assign to the private network interface.
    """


@dataclass
class UpdateSecurityGroupRequest:
    security_group_id: str
    """
    ID of the security group to update.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    New name for the security group.
    """

    description: Optional[str] = None
    """
    New description for the security group.
    """

    disable_default_rules: Optional[bool] = False
    """
    Whether to disable default rules.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    New tags for the security group.
    """

    project_default: Optional[bool] = False
    """
    Whether this should be the default security group for the project.
    """

    inbound_default_action: Optional[SecurityGroupAction] = (
        SecurityGroupAction.UNKNOWN_ACTION
    )
    """
    New default action for inbound rules.
    """

    outbound_default_action: Optional[SecurityGroupAction] = (
        SecurityGroupAction.UNKNOWN_ACTION
    )
    """
    New default action for outbound rules.
    """

    stateless: Optional[bool] = False
    """
    Whether the security group should be stateless.
    """


@dataclass
class UpdateSecurityGroupRuleRequest:
    security_group_rule_id: str
    """
    ID of the rule to update.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    protocol: Optional[SecurityGroupRuleProtocol] = (
        SecurityGroupRuleProtocol.UNKNOWN_PROTOCOL
    )
    """
    New protocol for the rule.
    """

    direction: Optional[SecurityGroupRuleDirection] = (
        SecurityGroupRuleDirection.UNKNOWN_DIRECTION
    )
    """
    New direction for the rule.
    """

    action: Optional[SecurityGroupRuleAction] = SecurityGroupRuleAction.UNKNOWN_ACTION
    """
    New action for the rule.
    """

    source_ip_range: Optional[str] = None
    """
    New source IP range for the rule.
    """

    destination_ip_range: Optional[str] = None
    """
    New destination IP range for the rule.
    """

    source_ports: Optional[SecurityGroupRulePortRange] = None
    """
    New source port range for the rule.
    """

    destination_ports: Optional[SecurityGroupRulePortRange] = None
    """
    New destination port range for the rule.
    """

    position: Optional[int] = 0
    """
    New position for the rule.
    """


@dataclass
class UpdateServerRequest:
    server_id: str
    """
    ID of the server to update.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    New name for the server.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    New tags for the server.
    """

    server_type: Optional[str] = None
    """
    New server type.
    """

    placement_group_id: Optional[str] = None
    """
    New placement group ID.
    """

    rescue_mode: Optional[bool] = False
    """
    New rescue mode setting.
    """

    boot_volume_id: Optional[str] = None
    """
    New boot volume ID.
    """

    windows_rdp_ssh_key_id: Optional[str] = None
    """
    New IAM ID of the SSH key used to encrypt the Windows `Administrator` password for RDP use.
    """

    protected: Optional[bool] = False
    """
    Protection status of the server.
    """

    public_network_interface: Optional[UpdateServerRequestPublicNetworkInterface] = None
    """
    New public network interface configuration.
    """


@dataclass
class UpdateTemplateRequest:
    template_id: str
    """
    Unique ID of the template to update.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    New name for the template.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    New tags for the template.
    """

    server_tags: Optional[list[str]] = field(default_factory=list)
    """
    New server tags for the template.
    """

    server_type: Optional[str] = None
    """
    New server type for the template.
    """

    security_group_id: Optional[str] = None
    """
    New security group ID for the template.
    """

    placement_group_id: Optional[str] = None
    """
    New placement group ID for the template.
    """

    update_volumes: Optional[UpdateTemplateRequestUpdateVolumes] = None
    """
    Updated volume templates for the template.
    """

    update_private_networks: Optional[UpdateTemplateRequestUpdatePrivateNetworks] = None
    """
    Updated private networks list for the template.
    """

    filesystem_ids: Optional[list[str]] = field(default_factory=list)
    """
    New list of filesystem IDs for the template.
    """

    public_ip_v4_count: Optional[int] = 0
    """
    New number of IPv4 public IPs to attach to servers.
    """

    public_ip_v6_count: Optional[int] = 0
    """
    New number of IPv6 public IPs to attach to servers.
    """

    windows_rdp_ssh_key_id: Optional[str] = None
    """
    New IAM ID of the SSH key used to encrypt the Windows `Administrator` password for RDP use.
    """


@dataclass
class UserData:
    key: str
    """
    The key of the user data.
    """

    content: str
    """
    The content of the user data.
    """


@dataclass
class VolumeApiCreateSnapshotRequest:
    name: str
    """
    Name of the snapshot.
    """

    base_volume_id: str
    """
    ID of the base volume.
    """

    public: bool
    """
    Whether the snapshot should be public.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    """
    Project ID of the snapshot.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags associated with the snapshot.
    """


@dataclass
class VolumeApiCreateVolumeRequest:
    name: str
    """
    Volume name.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    """
    Project ID to which the volume belongs.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags associated with the volume.
    """

    size: Optional[int] = 0
    """
    Volume size in bytes.
    """

    base_snapshot_id: Optional[str] = None
    """
    ID of the base snapshot used for this volume.
    """

    volume_type: Optional[CreateVolumeRequestVolumeType] = (
        CreateVolumeRequestVolumeType.UNKNOWN_VOLUME_TYPE
    )
    """
    Type of the volume.
    """


@dataclass
class VolumeApiDeleteSnapshotRequest:
    snapshot_id: str
    """
    ID of the snapshot to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class VolumeApiDeleteVolumeRequest:
    volume_id: str
    """
    ID of the volume to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class VolumeApiExportSnapshotToObjectStorageRequest:
    snapshot_id: str
    """
    ID of the snapshot to export.
    """

    bucket: str
    """
    Object Storage bucket name.
    """

    object_key: str
    """
    Object key.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class VolumeApiGetSnapshotRequest:
    snapshot_id: str
    """
    ID of the snapshot to retrieve.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class VolumeApiGetVolumeRequest:
    volume_id: str
    """
    ID of the volume to retrieve.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class VolumeApiImportSnapshotFromObjectStorageRequest:
    name: str
    """
    Name of the snapshot.
    """

    bucket: str
    """
    Object Storage bucket name.
    """

    object_key: str
    """
    Object key.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    """
    Project ID of the snapshot.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags associated with the snapshot.
    """

    size: Optional[int] = 0
    """
    Size of the imported snapshot in bytes.
    """

    volume_type: Optional[SnapshotVolumeType] = SnapshotVolumeType.UNKNOWN_VOLUME_TYPE
    """
    Volume type of the snapshot.
    """


@dataclass
class VolumeApiListSnapshotsRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    """
    Token for pagination.
    """

    page_size: Optional[int] = 0
    """
    Number of snapshots to return per page.
    """

    order_by: Optional[ListSnapshotsRequestOrderBy] = (
        ListSnapshotsRequestOrderBy.CREATED_AT_DESC
    )
    """
    Field to sort by.
    """

    project_id: Optional[str] = None
    """
    Filter by Project ID.
    """

    snapshot_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter by specific snapshot IDs.
    """

    name: Optional[str] = None
    """
    Filter by name.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Filter by tags.
    """

    base_volume_id: Optional[str] = None
    """
    Filter by base volume ID.
    """


@dataclass
class VolumeApiListVolumeTypesRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    """
    Token for pagination.
    """

    page_size: Optional[int] = 0
    """
    Number of items to return per page.
    """


@dataclass
class VolumeApiListVolumesRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    """
    Token for pagination.
    """

    page_size: Optional[int] = 0
    """
    Number of items to return per page.
    """

    order_by: Optional[ListVolumesRequestOrderBy] = (
        ListVolumesRequestOrderBy.CREATED_AT_DESC
    )
    """
    Field to order the results by.
    """

    project_id: Optional[str] = None
    """
    Filter by Project ID.
    """

    volume_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter by specific volume IDs.
    """

    name: Optional[str] = None
    """
    Filter by volume name.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Filter by tags.
    """

    volume_type: Optional[VolumeVolumeType] = VolumeVolumeType.UNKNOWN_VOLUME_TYPE
    """
    Filter by volume type.
    """


@dataclass
class VolumeApiUpdateSnapshotRequest:
    snapshot_id: str
    """
    ID of the snapshot to update.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    New name for the snapshot.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    New tags for the snapshot.
    """

    public: Optional[bool] = False
    """
    Whether the snapshot should be public.
    """


@dataclass
class VolumeApiUpdateVolumeRequest:
    volume_id: str
    """
    ID of the volume to update.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    New name for the volume.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    New tags for the volume.
    """

    size: Optional[int] = 0
    """
    New size for the volume.
    """
