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
    Set image response
    """

    image: Optional[Image]


@dataclass
class _SetSecurityGroupResponse:
    """
    Set security group response
    """

    security_group: Optional[SecurityGroup]


@dataclass
class _SetSecurityGroupRuleResponse:
    """
    Set security group rule response
    """

    rule: Optional[SecurityGroupRule]


@dataclass
class _SetServerResponse:
    """
    Set server response
    """

    server: Optional[Server]


@dataclass
class _SetSnapshotResponse:
    """
    Set snapshot response
    """

    snapshot: Optional[Snapshot]


@dataclass
class _CreateServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    name: Optional[str]
    """
    The server name
    """

    dynamic_ip_required: Optional[bool]
    """
    Define if a dynamic IP is required for the instance
    """

    commercial_type: str
    """
    Define the server commercial type (i.e. GP1-S)
    """

    image: str
    """
    The server image ID or label
    """

    volumes: Optional[Dict[str, VolumeServerTemplate]]
    """
    The volumes attached to the server
    """

    enable_ipv6: bool
    """
    True if IPv6 is enabled on the server
    """

    public_ip: Optional[str]
    """
    The ID of the reserved IP to attach to the server
    """

    boot_type: Optional[BootType]
    """
    The boot type to use
    """

    bootscript: Optional[str]
    """
    The bootscript ID to use when `boot_type` is set to `bootscript`
    """

    organization: Optional[str]
    """
    The server organization ID.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    :deprecated
    """

    project: Optional[str]
    """
    The server project ID.
    
    One-of ('project_identifier'): at most one of 'organization', 'project' could be set.
    """

    tags: Optional[List[str]]
    """
    The server tags
    """

    security_group: Optional[str]
    """
    The security group ID
    """

    placement_group: Optional[str]
    """
    Placement group ID if server must be part of a placement group
    """


@dataclass
class _SetServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    id: str
    """
    The server unique ID
    """

    name: str
    """
    The server name
    """

    organization: Optional[str]
    """
    The server organization ID
    """

    project: Optional[str]
    """
    The server project ID
    """

    allowed_actions: Optional[List[ServerAction]]
    """
    Provide as list of allowed actions on the server
    """

    tags: Optional[List[str]]
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

    volumes: Optional[Dict[str, Volume]]
    """
    The server volumes
    """

    security_group: Optional[SecurityGroupSummary]
    """
    The server security group
    """

    maintenances: Optional[List[ServerMaintenance]]
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

    private_nics: Optional[List[PrivateNIC]]
    """
    The server private NICs
    """


@dataclass
class _UpdateServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    UUID of the server
    """

    name: Optional[str]
    """
    Name of the server
    """

    boot_type: Optional[BootType]

    tags: Optional[List[str]]
    """
    Tags of the server
    """

    volumes: Optional[Dict[str, VolumeServerTemplate]]

    bootscript: Optional[str]

    dynamic_ip_required: Optional[bool]

    enable_ipv6: Optional[bool]

    protected: Optional[bool]

    security_group: Optional[SecurityGroupTemplate]

    placement_group: Optional[str]
    """
    Placement group ID if server must be part of a placement group
    """

    private_nics: Optional[List[PrivateNIC]]
    """
    The server private NICs
    """


@dataclass
class _SetImageRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    id: str

    name: str

    arch: Arch

    creation_date: Optional[datetime]

    modification_date: Optional[datetime]

    default_bootscript: Optional[Bootscript]

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
    Zone to target. If none is passed will use default zone from the config
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
    Zone to target. If none is passed will use default zone from the config
    """

    id: str
    """
    The ID of the security group (will be ignored)
    """

    name: str
    """
    The name of the security group
    """

    tags: Optional[List[str]]
    """
    The tags of the security group
    """

    creation_date: Optional[datetime]
    """
    The creation date of the security group (will be ignored)
    """

    modification_date: Optional[datetime]
    """
    The modification date of the security group (will be ignored)
    """

    description: str
    """
    The description of the security group
    """

    enable_default_security: bool
    """
    True to block SMTP on IPv4 and IPv6
    """

    inbound_default_policy: SecurityGroupPolicy
    """
    The default inbound policy
    """

    outbound_default_policy: SecurityGroupPolicy
    """
    The default outbound policy
    """

    organization: Optional[str]
    """
    The security groups organization ID
    """

    project: Optional[str]
    """
    The security group project ID
    """

    organization_default: Optional[bool]
    """
    Please use project_default instead
    :deprecated
    """

    project_default: bool
    """
    True use this security group for future instances created in this project
    """

    servers: Optional[List[ServerSummary]]
    """
    The servers attached to this security group
    """

    stateful: bool
    """
    True to set the security group as stateful
    """


@dataclass
class _SetSecurityGroupRuleRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
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
