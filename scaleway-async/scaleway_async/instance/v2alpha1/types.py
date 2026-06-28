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


class ListTemplatesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
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


@dataclass
class SecurityGroupRulePortRange:
    start: int
    end: int


@dataclass
class CreateServerRequestBookIP:
    type_: CreateServerRequestBookIPIPType
    tags: list[str]


@dataclass
class SecurityGroupRule:
    id: str
    protocol: SecurityGroupRuleProtocol
    direction: SecurityGroupRuleDirection
    action: SecurityGroupRuleAction
    source_ip_range: str
    destination_ip_range: str
    position: int
    source_ports: Optional[SecurityGroupRulePortRange] = None
    destination_ports: Optional[SecurityGroupRulePortRange] = None


@dataclass
class CreateServerRequestServerIP:
    ipam_ip_id: Optional[str] = None

    new_ip: Optional[CreateServerRequestBookIP] = None


@dataclass
class CreateServerRequestCreateVolume:
    name: str
    tags: list[str]
    size: Optional[int] = None
    perf_iops: Optional[int] = None
    base_snapshot_id: Optional[str] = None

    image_label: Optional[str] = None


@dataclass
class ServerTypeGpuInfo:
    manufacturer: str
    name: str
    memory: int


@dataclass
class ServerTypeLimits:
    private_network_count: int
    file_system_count: int
    private_network_bandwidth: int
    block_bandwidth: int
    internet_bandwidth: int
    l_ssd_size: int
    scratch_size: int
    ip_count: int
    volume_count: int
    scratch_volumes_count: int


@dataclass
class ServerIP:
    id: str
    dynamic: bool
    status: ServerIPStatus
    default: bool


@dataclass
class CreateTemplateRequestVolumeTemplate:
    volume_type: CreateServerRequestServerVolumeVolumeType
    name: str
    tags: list[str]
    size: Optional[int] = None
    perf_iops: Optional[int] = None
    base_snapshot_id: Optional[str] = None

    image_label: Optional[str] = None


@dataclass
class SecurityGroupRuleConfig:
    protocol: SecurityGroupRuleProtocol
    direction: SecurityGroupRuleDirection
    action: SecurityGroupRuleAction
    source_ip_range: str
    destination_ip_range: str
    position: int
    source_ports: Optional[SecurityGroupRulePortRange] = None
    destination_ports: Optional[SecurityGroupRulePortRange] = None


@dataclass
class SecurityGroup:
    id: str
    name: str
    description: str
    project_id: str
    tags: list[str]
    disable_default_rules: bool
    project_default: bool
    inbound_default_action: SecurityGroupAction
    outbound_default_action: SecurityGroupAction
    stateless: bool
    default_rules: list[SecurityGroupRule]
    rules: list[SecurityGroupRule]
    zone: ScwZone
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class CreateServerRequestPublicNetworkInterface:
    ips: list[CreateServerRequestServerIP]
    security_group_id: Optional[str] = None


@dataclass
class CreateServerRequestServerVolume:
    volume_type: CreateServerRequestServerVolumeVolumeType
    volume_id: Optional[str] = None

    new_volume: Optional[CreateServerRequestCreateVolume] = None


@dataclass
class PlacementGroup:
    project_id: str
    name: str
    id: str
    policy_type: PlacementGroupPolicyType
    tags: list[str]
    zone: ScwZone
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class PrivateNetworkInterface:
    id: str
    private_network_id: str
    project_id: str
    server_id: str
    security_group_id: str
    mac_address: str
    status: PrivateNetworkInterfaceStatus
    ip_ids: list[str]
    tags: list[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class SecurityGroupSummary:
    id: str
    name: str
    description: str
    project_id: str
    tags: list[str]
    disable_default_rules: bool
    project_default: bool
    inbound_default_action: SecurityGroupAction
    outbound_default_action: SecurityGroupAction
    stateless: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class ServerType:
    name: str
    vcpu_count: int
    gpu_count: int
    memory: int
    architecture: ServerTypeArchitecture
    availability: ServerTypeAvailability
    end_of_service: bool
    limits: Optional[ServerTypeLimits] = None
    gpu_info: Optional[ServerTypeGpuInfo] = None


@dataclass
class ServerSummary:
    project_id: str
    id: str
    name: str
    tags: list[str]
    server_type: str
    status: ServerStatus
    architecture: ServerArchitecture
    rescue_mode: bool
    placement_group_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class TemplateSummary:
    project_id: str
    id: str
    name: str
    tags: list[str]
    server_tags: list[str]
    server_type: str
    public_ip_v4_count: int
    public_ip_v6_count: int
    private_network_ids: list[str]
    filesystem_ids: list[str]
    zone: ScwZone
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    security_group_id: Optional[str] = None
    placement_group_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


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


@dataclass
class UpdateTemplateRequestUpdateVolumes:
    volumes: list[CreateTemplateRequestVolumeTemplate]


@dataclass
class AddSecurityGroupRulesRequest:
    security_group_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    security_group_rules: Optional[list[SecurityGroupRuleConfig]] = field(
        default_factory=list
    )


@dataclass
class AddSecurityGroupRulesResponse:
    added_rules: list[SecurityGroupRule]
    security_group: Optional[SecurityGroup] = None


@dataclass
class AttachServerFileSystemRequest:
    server_id: str
    filesystem_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class AttachServerIPRequest:
    server_id: str
    ip_id: str
    default: bool
    move_allowed: bool
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class AttachServerPrivateNetworkInterfaceRequest:
    server_id: str
    private_network_interface_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class AttachServerVolumeRequest:
    server_id: str
    volume_id: str
    boot_volume: bool
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    volume_type: Optional[ServerVolumeVolumeType] = None


@dataclass
class CheckTemplateRequest:
    template_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class CreatePlacementGroupRequest:
    name: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    policy_type: Optional[PlacementGroupPolicyType] = None
    tags: Optional[list[str]] = field(default_factory=list)


@dataclass
class CreatePrivateNetworkInterfaceRequest:
    private_network_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    server_id: Optional[str] = None
    security_group_id: Optional[str] = None
    ip_ids: Optional[list[str]] = field(default_factory=list)
    tags: Optional[list[str]] = field(default_factory=list)


@dataclass
class CreateSecurityGroupRequest:
    name: str
    description: str
    disable_default_rules: bool
    project_default: bool
    stateless: bool
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    tags: Optional[list[str]] = field(default_factory=list)
    inbound_default_action: Optional[SecurityGroupAction] = None
    outbound_default_action: Optional[SecurityGroupAction] = None


@dataclass
class CreateServerFromTemplateRequest:
    template_id: str
    name: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class CreateServerRequest:
    name: str
    server_type: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    tags: Optional[list[str]] = field(default_factory=list)
    placement_group_id: Optional[str] = None
    volumes: Optional[list[CreateServerRequestServerVolume]] = field(
        default_factory=list
    )
    windows_rdp_ssh_key_id: Optional[str] = None
    public_network_interface: Optional[CreateServerRequestPublicNetworkInterface] = None


@dataclass
class CreateTemplateRequest:
    name: str
    server_type: str
    public_ip_v4_count: int
    public_ip_v6_count: int
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    tags: Optional[list[str]] = field(default_factory=list)
    server_tags: Optional[list[str]] = field(default_factory=list)
    security_group_id: Optional[str] = None
    placement_group_id: Optional[str] = None
    volumes: Optional[list[CreateTemplateRequestVolumeTemplate]] = field(
        default_factory=list
    )
    private_network_ids: Optional[list[str]] = field(default_factory=list)
    windows_rdp_ssh_key_id: Optional[str] = None
    filesystem_ids: Optional[list[str]] = field(default_factory=list)


@dataclass
class DeletePlacementGroupRequest:
    placement_group_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeletePrivateNetworkInterfaceRequest:
    private_network_interface_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteSecurityGroupRequest:
    security_group_id: str
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


@dataclass
class DeleteServerRequest:
    server_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    delete_all_ips: Optional[bool] = None

    delete_ip_ids: Optional[list[str]] = field(default_factory=list)

    delete_all_volumes: Optional[bool] = None

    delete_volume_ids: Optional[list[str]] = field(default_factory=list)

    keep_all_private_nics: Optional[bool] = None

    delete_private_nic_ids: Optional[list[str]] = field(default_factory=list)


@dataclass
class DeleteTemplateRequest:
    template_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteTemplateUserDataRequest:
    template_id: str
    key: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteUserDataRequest:
    server_id: str
    key: str
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
class DetachServerIPRequest:
    server_id: str
    ip_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DetachServerPrivateNetworkInterfaceRequest:
    server_id: str
    private_network_interface_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DetachServerVolumeRequest:
    server_id: str
    volume_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetPlacementGroupRequest:
    placement_group_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetPrivateNetworkInterfaceRequest:
    private_network_interface_id: str
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
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerCloudInitRequest:
    server_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerRequest:
    server_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetTemplateCloudInitRequest:
    template_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetTemplateRequest:
    template_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetTemplateUserDataRequest:
    template_id: str
    key: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetUserDataRequest:
    server_id: str
    key: str
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
    page_size: Optional[int] = None
    order_by: Optional[ListPlacementGroupsRequestOrderBy] = None
    project_id: Optional[str] = None
    placement_group_ids: Optional[list[str]] = field(default_factory=list)
    name: Optional[str] = None
    tags: Optional[list[str]] = field(default_factory=list)


@dataclass
class ListPlacementGroupsResponse:
    placement_groups: list[PlacementGroup]
    total_count: int
    next_page_token: Optional[str] = None


@dataclass
class ListPrivateNetworkInterfacesRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    page_size: Optional[int] = None
    order_by: Optional[ListPrivateNetworkInterfacesRequestOrderBy] = None
    project_id: Optional[str] = None
    server_ids: Optional[list[str]] = field(default_factory=list)
    security_group_ids: Optional[list[str]] = field(default_factory=list)
    private_network_ids: Optional[list[str]] = field(default_factory=list)
    tags: Optional[list[str]] = field(default_factory=list)


@dataclass
class ListPrivateNetworkInterfacesResponse:
    private_network_interfaces: list[PrivateNetworkInterface]
    total_count: int
    next_page_token: Optional[str] = None


@dataclass
class ListSecurityGroupsRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    page_size: Optional[int] = None
    order_by: Optional[ListSecurityGroupsRequestOrderBy] = None
    project_id: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[list[str]] = field(default_factory=list)
    security_group_ids: Optional[list[str]] = field(default_factory=list)


@dataclass
class ListSecurityGroupsResponse:
    security_groups: list[SecurityGroupSummary]
    total_count: int
    next_page_token: Optional[str] = None


@dataclass
class ListServerTypesRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    page_size: Optional[int] = None


@dataclass
class ListServerTypesResponse:
    server_types: list[ServerType]
    total_count: int
    next_page_token: Optional[str] = None


@dataclass
class ListServersRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    page_size: Optional[int] = None
    order_by: Optional[ListServersRequestOrderBy] = None
    project_id: Optional[str] = None
    server_ids: Optional[list[str]] = field(default_factory=list)
    name: Optional[str] = None
    server_type: Optional[str] = None
    tags: Optional[list[str]] = field(default_factory=list)
    security_group_ids: Optional[list[str]] = field(default_factory=list)
    placement_group_ids: Optional[list[str]] = field(default_factory=list)
    private_network_ids: Optional[list[str]] = field(default_factory=list)
    mac_addresses: Optional[list[str]] = field(default_factory=list)


@dataclass
class ListServersResponse:
    servers: list[ServerSummary]
    total_count: int
    next_page_token: Optional[str] = None


@dataclass
class ListTemplateUserDataKeysRequest:
    template_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    page_size: Optional[int] = None


@dataclass
class ListTemplateUserDataKeysResponse:
    keys: list[str]
    total_count: int
    next_page_token: Optional[str] = None


@dataclass
class ListTemplatesRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    page_size: Optional[int] = None
    order_by: Optional[ListTemplatesRequestOrderBy] = None
    project_id: Optional[str] = None
    template_ids: Optional[list[str]] = field(default_factory=list)
    name: Optional[str] = None
    tags: Optional[list[str]] = field(default_factory=list)
    server_tags: Optional[list[str]] = field(default_factory=list)
    security_group_ids: Optional[list[str]] = field(default_factory=list)
    placement_group_ids: Optional[list[str]] = field(default_factory=list)


@dataclass
class ListTemplatesResponse:
    templates: list[TemplateSummary]
    total_count: int
    next_page_token: Optional[str] = None


@dataclass
class ListUserDataKeysRequest:
    server_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    page_size: Optional[int] = None


@dataclass
class ListUserDataKeysResponse:
    keys: list[str]
    total_count: int
    next_page_token: Optional[str] = None


@dataclass
class PauseServerRequest:
    server_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class RebootServerRequest:
    server_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ResourceCounts:
    servers: int
    gpu_servers: int
    servers_by_type: dict[str, int]
    security_groups: int
    placement_groups: int
    snapshots: int
    volumes: int
    volumes_l_ssd_total_size: int
    private_network_interfaces: int
    volumes_scratch: int
    volumes_l_ssd: int


@dataclass
class Server:
    project_id: str
    id: str
    name: str
    tags: list[str]
    server_type: str
    status: ServerStatus
    volumes: list[ServerVolume]
    architecture: ServerArchitecture
    private_network_interfaces: list[ServerPrivateNetworkInterface]
    rescue_mode: bool
    status_detail: str
    filesystems: list[ServerFilesystem]
    zone: ScwZone
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    placement_group_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    boot_volume_id: Optional[str] = None
    windows_rdp_password: Optional[ServerRDPPassword] = None
    public_network_interface: Optional[ServerPublicNetworkInterface] = None


@dataclass
class SetSecurityGroupRulesRequest:
    security_group_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    security_group_rules: Optional[list[SecurityGroupRuleConfig]] = field(
        default_factory=list
    )


@dataclass
class SetServerCloudInitRequest:
    server_id: str
    content: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetServerDefaultIPRequest:
    server_id: str
    ip_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetTemplateCloudInitRequest:
    template_id: str
    content: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetTemplateUserDataRequest:
    template_id: str
    key: str
    content: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SetUserDataRequest:
    server_id: str
    key: str
    content: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class StartServerRequest:
    server_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class StopAndDeleteServerRequest:
    server_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    delete_all_ips: Optional[bool] = None

    delete_ip_ids: Optional[list[str]] = field(default_factory=list)

    delete_all_volumes: Optional[bool] = None

    delete_volume_ids: Optional[list[str]] = field(default_factory=list)

    keep_all_private_nics: Optional[bool] = None

    delete_private_nic_ids: Optional[list[str]] = field(default_factory=list)


@dataclass
class StopServerRequest:
    server_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class Template:
    project_id: str
    id: str
    name: str
    tags: list[str]
    server_tags: list[str]
    server_type: str
    public_ip_v4_count: int
    public_ip_v6_count: int
    volumes: list[CreateTemplateRequestVolumeTemplate]
    private_network_ids: list[str]
    filesystem_ids: list[str]
    zone: ScwZone
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    security_group_id: Optional[str] = None
    placement_group_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    windows_rdp_ssh_key_id: Optional[str] = None


@dataclass
class UpdatePlacementGroupRequest:
    placement_group_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    policy_type: Optional[PlacementGroupPolicyType] = None
    tags: Optional[list[str]] = field(default_factory=list)


@dataclass
class UpdatePrivateNetworkInterfaceRequest:
    private_network_interface_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    security_group_id: Optional[str] = None
    tags: Optional[list[str]] = field(default_factory=list)


@dataclass
class UpdateSecurityGroupRequest:
    security_group_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    description: Optional[str] = None
    disable_default_rules: Optional[bool] = None
    tags: Optional[list[str]] = field(default_factory=list)
    project_default: Optional[bool] = None
    inbound_default_action: Optional[SecurityGroupAction] = None
    outbound_default_action: Optional[SecurityGroupAction] = None
    stateless: Optional[bool] = None


@dataclass
class UpdateSecurityGroupRuleRequest:
    security_group_rule_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    protocol: Optional[SecurityGroupRuleProtocol] = None
    direction: Optional[SecurityGroupRuleDirection] = None
    action: Optional[SecurityGroupRuleAction] = None
    source_ip_range: Optional[str] = None
    destination_ip_range: Optional[str] = None
    source_ports: Optional[SecurityGroupRulePortRange] = None
    destination_ports: Optional[SecurityGroupRulePortRange] = None
    position: Optional[int] = None


@dataclass
class UpdateServerRequest:
    server_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    tags: Optional[list[str]] = field(default_factory=list)
    server_type: Optional[str] = None
    placement_group_id: Optional[str] = None
    rescue_mode: Optional[bool] = None
    boot_volume_id: Optional[str] = None
    windows_rdp_ssh_key_id: Optional[str] = None
    protected: Optional[bool] = None
    public_network_interface: Optional[UpdateServerRequestPublicNetworkInterface] = None


@dataclass
class UpdateTemplateRequest:
    template_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    tags: Optional[list[str]] = field(default_factory=list)
    server_tags: Optional[list[str]] = field(default_factory=list)
    server_type: Optional[str] = None
    security_group_id: Optional[str] = None
    placement_group_id: Optional[str] = None
    update_volumes: Optional[UpdateTemplateRequestUpdateVolumes] = None
    private_network_ids: Optional[list[str]] = field(default_factory=list)
    public_ip_v4_count: Optional[int] = None
    public_ip_v6_count: Optional[int] = None
    windows_rdp_ssh_key_id: Optional[str] = None
    filesystem_ids: Optional[list[str]] = field(default_factory=list)


@dataclass
class UserData:
    key: str
    content: str
