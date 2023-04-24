# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional

from scaleway_core.bridge import (
    Zone,
)
from .types import (
    Arch,
    BootType,
    Bootscript,
    Image,
    ImageState,
    PlacementGroup,
    PrivateNIC,
    SecurityGroup,
    SecurityGroupPolicy,
    SecurityGroupRule,
    SecurityGroupRuleAction,
    SecurityGroupRuleDirection,
    SecurityGroupRuleProtocol,
    SecurityGroupSummary,
    SecurityGroupTemplate,
    Server,
    ServerAction,
    ServerIp,
    ServerIpv6,
    ServerLocation,
    ServerMaintenance,
    ServerState,
    ServerSummary,
    Snapshot,
    SnapshotBaseVolume,
    SnapshotState,
    Volume,
    VolumeServerTemplate,
    VolumeSummary,
    VolumeVolumeType,
)


@dataclass
class _SetImageResponse:
    """
    Set image response.
    """

    image: Optional[Image]


@dataclass
class _SetSecurityGroupResponse:
    """
    Set security group response.
    """

    security_group: Optional[SecurityGroup]


@dataclass
class _SetSecurityGroupRuleResponse:
    """
    Set security group rule response.
    """

    rule: Optional[SecurityGroupRule]


@dataclass
class _SetServerResponse:
    """
    Set server response.
    """

    server: Optional[Server]


@dataclass
class _SetSnapshotResponse:
    """
    Set snapshot response.
    """

    snapshot: Optional[Snapshot]


@dataclass
class _CreateServerRequest:
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
    Define if a dynamic IP is required for the Instance.
    """

    commercial_type: str
    """
    Define the Instance commercial type (i.e. GP1-S).
    """

    image: str
    """
    Instance image ID or label.
    """

    volumes: Optional[Dict[str, VolumeServerTemplate]]
    """
    Volumes attached to the server.
    """

    enable_ipv6: bool
    """
    True if IPv6 is enabled on the server.
    """

    public_ip: Optional[str]
    """
    ID of the reserved IP to attach to the server.
    """

    boot_type: Optional[BootType]
    """
    Boot type to use.
    """

    bootscript: Optional[str]
    """
    Bootscript ID to use when `boot_type` is set to `bootscript`.
    :deprecated
    """

    organization: Optional[str]
    """
    Instance Organization ID.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    :deprecated
    """

    project: Optional[str]
    """
    Instance Project ID.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
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


@dataclass
class _SetServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    id: str
    """
    Instance unique ID.
    """

    name: str
    """
    Instance name.
    """

    organization: Optional[str]
    """
    Instance Organization ID.
    """

    project: Optional[str]
    """
    Instance Project ID.
    """

    allowed_actions: Optional[List[ServerAction]]
    """
    Provide a list of allowed actions on the server.
    """

    tags: Optional[List[str]]
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
    Provide information on the Instance image.
    """

    protected: bool
    """
    Instance protection option is activated.
    """

    private_ip: Optional[str]
    """
    Instance private IP address.
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

    volumes: Optional[Dict[str, Volume]]
    """
    Instance volumes.
    """

    security_group: Optional[SecurityGroupSummary]
    """
    Instance security group.
    """

    maintenances: Optional[List[ServerMaintenance]]
    """
    Instance planned maintenances.
    """

    state_detail: str
    """
    Instance state_detail.
    """

    arch: Arch
    """
    Instance architecture (refers to the CPU architecture used for the Instance, e.g. x86_64, arm64).
    """

    placement_group: Optional[PlacementGroup]
    """
    Instance placement group.
    """

    private_nics: Optional[List[PrivateNIC]]
    """
    Instance private NICs.
    """


@dataclass
class _UpdateServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    server_id: str
    """
    UUID of the Instance.
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
    """
    :deprecated
    """

    dynamic_ip_required: Optional[bool]

    enable_ipv6: Optional[bool]

    protected: Optional[bool]

    security_group: Optional[SecurityGroupTemplate]

    placement_group: Optional[str]
    """
    Placement group ID if Instance must be part of a placement group.
    """

    private_nics: Optional[List[PrivateNIC]]
    """
    Instance private NICs.
    """


@dataclass
class _SetImageRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    id: str

    name: str

    arch: Arch

    creation_date: Optional[datetime]

    modification_date: Optional[datetime]

    default_bootscript: Optional[Bootscript]
    """
    :deprecated
    """

    extra_volumes: Optional[Dict[str, Volume]]

    from_server: str

    organization: Optional[str]

    public: bool

    root_volume: Optional[VolumeSummary]

    state: ImageState

    project: Optional[str]

    tags: Optional[List[str]]


@dataclass
class _SetSnapshotRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    snapshot_id: str

    id: str

    name: str

    organization: Optional[str]

    volume_type: VolumeVolumeType

    size: int

    state: SnapshotState

    base_volume: Optional[SnapshotBaseVolume]

    creation_date: Optional[datetime]

    modification_date: Optional[datetime]

    project: Optional[str]

    tags: Optional[List[str]]


@dataclass
class _SetSecurityGroupRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    id: str
    """
    ID of the security group (will be ignored).
    """

    name: str
    """
    Name of the security group.
    """

    tags: Optional[List[str]]
    """
    Tags of the security group.
    """

    creation_date: Optional[datetime]
    """
    Creation date of the security group (will be ignored).
    """

    modification_date: Optional[datetime]
    """
    Modification date of the security group (will be ignored).
    """

    description: str
    """
    Description of the security group.
    """

    enable_default_security: bool
    """
    True to block SMTP on IPv4 and IPv6. This feature is read only, please open a support ticket if you need to make it configurable.
    """

    inbound_default_policy: SecurityGroupPolicy
    """
    Default inbound policy.
    """

    outbound_default_policy: SecurityGroupPolicy
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
    :deprecated
    """

    project_default: bool
    """
    True use this security group for future Instances created in this project.
    """

    servers: Optional[List[ServerSummary]]
    """
    Instances attached to this security group.
    """

    stateful: bool
    """
    True to set the security group as stateful.
    """


@dataclass
class _SetSecurityGroupRuleRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    security_group_id: str

    security_group_rule_id: str

    id: str

    protocol: SecurityGroupRuleProtocol

    direction: SecurityGroupRuleDirection

    action: SecurityGroupRuleAction

    ip_range: str

    dest_port_from: Optional[int]

    dest_port_to: Optional[int]

    position: int

    editable: bool
