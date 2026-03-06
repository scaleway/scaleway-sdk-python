# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types_private import (
    _SetImageResponse,
    _SetSecurityGroupResponse,
    _SetSecurityGroupRuleResponse,
    _SetServerResponse,
    _SetSnapshotResponse,
    _SetSecurityGroupRequest,
    _SetSecurityGroupRuleRequest,
    _SetServerRequest,
    _SetSnapshotRequest,
)
from .types import (
    Arch,
    BootType,
    PlacementGroupPolicyMode,
    PlacementGroupPolicyType,
    PrivateNICState,
    SecurityGroupPolicy,
    SecurityGroupState,
    ServerAction,
    ServerIpIpFamily,
    ServerIpProvisioningMode,
    ServerIpState,
    ServerState,
    SnapshotState,
    TaskStatus,
    VolumeState,
    VolumeVolumeType,
    PrivateNIC,
    ServerSummary,
    Bootscript,
    Volume,
    VolumeSummary,
    Image,
    PlacementGroup,
    SecurityGroupSummary,
    ServerFilesystem,
    ServerIp,
    ServerIpv6,
    ServerLocation,
    ServerMaintenance,
    VolumeServer,
    Server,
    AttachServerFileSystemResponse,
    AttachServerVolumeResponse,
    CreateImageResponse,
    Ip,
    CreateIpResponse,
    CreatePlacementGroupResponse,
    CreatePrivateNICResponse,
    SecurityGroup,
    CreateSecurityGroupResponse,
    SecurityGroupRule,
    CreateSecurityGroupRuleResponse,
    CreateServerResponse,
    SnapshotBaseVolume,
    Snapshot,
    Task,
    CreateSnapshotResponse,
    CreateVolumeResponse,
    DetachServerFileSystemResponse,
    DetachServerVolumeResponse,
    ExportSnapshotResponse,
    Dashboard,
    GetDashboardResponse,
    GetImageResponse,
    GetIpResponse,
    GetPlacementGroupResponse,
    PlacementGroupServer,
    GetPlacementGroupServersResponse,
    GetPrivateNICResponse,
    GetSecurityGroupResponse,
    GetSecurityGroupRuleResponse,
    GetServerResponse,
    GetServerTypesAvailabilityResponseAvailability,
    GetServerTypesAvailabilityResponse,
    GetSnapshotResponse,
    GetVolumeResponse,
    ListImagesResponse,
    ListIpsResponse,
    ListPlacementGroupsResponse,
    ListPrivateNICsResponse,
    ListSecurityGroupRulesResponse,
    ListSecurityGroupsResponse,
    ListServerActionsResponse,
    ListServerUserDataResponse,
    ListServersResponse,
    ServerTypeNetworkInterface,
    ServerTypeVolumeConstraintSizes,
    ServerTypeCapabilities,
    ServerTypeGPUInfo,
    ServerTypeNetwork,
    ServerTypeVolumeConstraintsByType,
    ServerType,
    ListServersTypesResponse,
    ListSnapshotsResponse,
    ListVolumesResponse,
    VolumeTypeCapabilities,
    VolumeTypeConstraints,
    VolumeType,
    ListVolumesTypesResponse,
    MigrationPlan,
    ServerActionResponse,
    ServerCompatibleTypes,
    SetPlacementGroupResponse,
    SetPlacementGroupServersResponse,
    SetSecurityGroupRulesResponse,
    UpdateImageResponse,
    UpdateIpResponse,
    UpdatePlacementGroupResponse,
    UpdatePlacementGroupServersResponse,
    UpdateSecurityGroupResponse,
    UpdateSecurityGroupRuleResponse,
    UpdateServerResponse,
    UpdateSnapshotResponse,
    UpdateVolumeResponse,
    ApplyBlockMigrationRequest,
    AttachServerFileSystemRequest,
    AttachServerVolumeRequest,
    CheckBlockMigrationOrganizationQuotasRequest,
    VolumeTemplate,
    CreateImageRequest,
    CreateIpRequest,
    CreatePlacementGroupRequest,
    CreatePrivateNICRequest,
    CreateSecurityGroupRequest,
    CreateSecurityGroupRuleRequest,
    VolumeServerTemplate,
    CreateServerRequest,
    CreateSnapshotRequest,
    CreateVolumeRequest,
    DetachServerFileSystemRequest,
    DetachServerVolumeRequest,
    ExportSnapshotRequest,
    PlanBlockMigrationRequest,
    ServerActionRequestVolumeBackupTemplate,
    ServerActionRequest,
    SetImageRequest,
    SetPlacementGroupRequest,
    SetPlacementGroupServersRequest,
    SetSecurityGroupRulesRequestRule,
    SetSecurityGroupRulesRequest,
    VolumeImageUpdateTemplate,
    UpdateImageRequest,
    UpdateIpRequest,
    UpdatePlacementGroupRequest,
    UpdatePlacementGroupServersRequest,
    UpdatePrivateNICRequest,
    UpdateSecurityGroupRequest,
    UpdateSecurityGroupRuleRequest,
    SecurityGroupTemplate,
    UpdateServerRequest,
    UpdateSnapshotRequest,
    UpdateVolumeRequest,
)


def unmarshal_PrivateNIC(data: Any) -> PrivateNIC:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNIC' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("server_id", None)
    if field is not None:
        args["server_id"] = field
    else:
        args["server_id"] = None

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field
    else:
        args["private_network_id"] = None

    field = data.get("mac_address", None)
    if field is not None:
        args["mac_address"] = field
    else:
        args["mac_address"] = None

    field = data.get("state", None)
    if field is not None:
        args["state"] = field
    else:
        args["state"] = PrivateNICState.AVAILABLE

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("creation_date", None)
    if field is not None:
        args["creation_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["creation_date"] = None

    return PrivateNIC(**args)


def unmarshal_ServerSummary(data: Any) -> ServerSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerSummary' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return ServerSummary(**args)


def unmarshal_Bootscript(data: Any) -> Bootscript:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Bootscript' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("architecture", None)
    if field is not None:
        args["architecture"] = field
    else:
        args["architecture"] = None

    field = data.get("bootcmdargs", None)
    if field is not None:
        args["bootcmdargs"] = field
    else:
        args["bootcmdargs"] = None

    field = data.get("default", None)
    if field is not None:
        args["default"] = field
    else:
        args["default"] = None

    field = data.get("dtb", None)
    if field is not None:
        args["dtb"] = field
    else:
        args["dtb"] = None

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("initrd", None)
    if field is not None:
        args["initrd"] = field
    else:
        args["initrd"] = None

    field = data.get("kernel", None)
    if field is not None:
        args["kernel"] = field
    else:
        args["kernel"] = None

    field = data.get("organization", None)
    if field is not None:
        args["organization"] = field
    else:
        args["organization"] = None

    field = data.get("public", None)
    if field is not None:
        args["public"] = field
    else:
        args["public"] = None

    field = data.get("title", None)
    if field is not None:
        args["title"] = field
    else:
        args["title"] = None

    field = data.get("project", None)
    if field is not None:
        args["project"] = field
    else:
        args["project"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    return Bootscript(**args)


def unmarshal_Volume(data: Any) -> Volume:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Volume' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("export_uri", None)
    if field is not None:
        args["export_uri"] = field
    else:
        args["export_uri"] = None

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = 0

    field = data.get("volume_type", None)
    if field is not None:
        args["volume_type"] = field
    else:
        args["volume_type"] = VolumeVolumeType.L_SSD

    field = data.get("organization", None)
    if field is not None:
        args["organization"] = field
    else:
        args["organization"] = None

    field = data.get("project", None)
    if field is not None:
        args["project"] = field
    else:
        args["project"] = None

    field = data.get("creation_date", None)
    if field is not None:
        args["creation_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["creation_date"] = None

    field = data.get("modification_date", None)
    if field is not None:
        args["modification_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["modification_date"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("state", None)
    if field is not None:
        args["state"] = field
    else:
        args["state"] = VolumeState.AVAILABLE

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("server", None)
    if field is not None:
        args["server"] = unmarshal_ServerSummary(field)
    else:
        args["server"] = None

    return Volume(**args)


def unmarshal_VolumeSummary(data: Any) -> VolumeSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeSummary' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = None

    field = data.get("volume_type", None)
    if field is not None:
        args["volume_type"] = field
    else:
        args["volume_type"] = None

    return VolumeSummary(**args)


def unmarshal_Image(data: Any) -> Image:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Image' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("arch", None)
    if field is not None:
        args["arch"] = field
    else:
        args["arch"] = None

    field = data.get("extra_volumes", None)
    if field is not None:
        args["extra_volumes"] = (
            {key: unmarshal_Volume(value) for key, value in field.items()}
            if field is not None
            else None
        )
    else:
        args["extra_volumes"] = None

    field = data.get("from_server", None)
    if field is not None:
        args["from_server"] = field
    else:
        args["from_server"] = None

    field = data.get("organization", None)
    if field is not None:
        args["organization"] = field
    else:
        args["organization"] = None

    field = data.get("creation_date", None)
    if field is not None:
        args["creation_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["creation_date"] = None

    field = data.get("modification_date", None)
    if field is not None:
        args["modification_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["modification_date"] = None

    field = data.get("default_bootscript", None)
    if field is not None:
        args["default_bootscript"] = unmarshal_Bootscript(field)
    else:
        args["default_bootscript"] = None

    field = data.get("public", None)
    if field is not None:
        args["public"] = field
    else:
        args["public"] = None

    field = data.get("state", None)
    if field is not None:
        args["state"] = field
    else:
        args["state"] = None

    field = data.get("project", None)
    if field is not None:
        args["project"] = field
    else:
        args["project"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("root_volume", None)
    if field is not None:
        args["root_volume"] = unmarshal_VolumeSummary(field)
    else:
        args["root_volume"] = None

    return Image(**args)


def unmarshal_PlacementGroup(data: Any) -> PlacementGroup:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlacementGroup' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("organization", None)
    if field is not None:
        args["organization"] = field
    else:
        args["organization"] = None

    field = data.get("project", None)
    if field is not None:
        args["project"] = field
    else:
        args["project"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("policy_mode", None)
    if field is not None:
        args["policy_mode"] = field
    else:
        args["policy_mode"] = PlacementGroupPolicyMode.OPTIONAL

    field = data.get("policy_type", None)
    if field is not None:
        args["policy_type"] = field
    else:
        args["policy_type"] = PlacementGroupPolicyType.MAX_AVAILABILITY

    field = data.get("policy_respected", None)
    if field is not None:
        args["policy_respected"] = field
    else:
        args["policy_respected"] = False

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    return PlacementGroup(**args)


def unmarshal_SecurityGroupSummary(data: Any) -> SecurityGroupSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecurityGroupSummary' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return SecurityGroupSummary(**args)


def unmarshal_ServerFilesystem(data: Any) -> ServerFilesystem:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerFilesystem' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("filesystem_id", None)
    if field is not None:
        args["filesystem_id"] = field
    else:
        args["filesystem_id"] = None

    field = data.get("state", None)
    if field is not None:
        args["state"] = field
    else:
        args["state"] = None

    return ServerFilesystem(**args)


def unmarshal_ServerIp(data: Any) -> ServerIp:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerIp' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("address", None)
    if field is not None:
        args["address"] = field
    else:
        args["address"] = None

    field = data.get("gateway", None)
    if field is not None:
        args["gateway"] = field
    else:
        args["gateway"] = None

    field = data.get("netmask", None)
    if field is not None:
        args["netmask"] = field
    else:
        args["netmask"] = None

    field = data.get("family", None)
    if field is not None:
        args["family"] = field
    else:
        args["family"] = ServerIpIpFamily.INET

    field = data.get("dynamic", None)
    if field is not None:
        args["dynamic"] = field
    else:
        args["dynamic"] = False

    field = data.get("provisioning_mode", None)
    if field is not None:
        args["provisioning_mode"] = field
    else:
        args["provisioning_mode"] = ServerIpProvisioningMode.MANUAL

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("ipam_id", None)
    if field is not None:
        args["ipam_id"] = field
    else:
        args["ipam_id"] = None

    field = data.get("state", None)
    if field is not None:
        args["state"] = field
    else:
        args["state"] = ServerIpState.UNKNOWN_STATE

    return ServerIp(**args)


def unmarshal_ServerIpv6(data: Any) -> ServerIpv6:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerIpv6' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("address", None)
    if field is not None:
        args["address"] = field
    else:
        args["address"] = None

    field = data.get("gateway", None)
    if field is not None:
        args["gateway"] = field
    else:
        args["gateway"] = None

    field = data.get("netmask", None)
    if field is not None:
        args["netmask"] = field
    else:
        args["netmask"] = None

    return ServerIpv6(**args)


def unmarshal_ServerLocation(data: Any) -> ServerLocation:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerLocation' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("cluster_id", None)
    if field is not None:
        args["cluster_id"] = field
    else:
        args["cluster_id"] = None

    field = data.get("hypervisor_id", None)
    if field is not None:
        args["hypervisor_id"] = field
    else:
        args["hypervisor_id"] = None

    field = data.get("node_id", None)
    if field is not None:
        args["node_id"] = field
    else:
        args["node_id"] = None

    field = data.get("platform_id", None)
    if field is not None:
        args["platform_id"] = field
    else:
        args["platform_id"] = None

    field = data.get("zone_id", None)
    if field is not None:
        args["zone_id"] = field
    else:
        args["zone_id"] = None

    return ServerLocation(**args)


def unmarshal_ServerMaintenance(data: Any) -> ServerMaintenance:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerMaintenance' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("reason", None)
    if field is not None:
        args["reason"] = field
    else:
        args["reason"] = None

    field = data.get("start_date", None)
    if field is not None:
        args["start_date"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["start_date"] = None

    return ServerMaintenance(**args)


def unmarshal_VolumeServer(data: Any) -> VolumeServer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeServer' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("export_uri", None)
    if field is not None:
        args["export_uri"] = field
    else:
        args["export_uri"] = None

    field = data.get("organization", None)
    if field is not None:
        args["organization"] = field
    else:
        args["organization"] = None

    field = data.get("server", None)
    if field is not None:
        args["server"] = unmarshal_ServerSummary(field)
    else:
        args["server"] = None

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = None

    field = data.get("volume_type", None)
    if field is not None:
        args["volume_type"] = field
    else:
        args["volume_type"] = None

    field = data.get("boot", None)
    if field is not None:
        args["boot"] = field
    else:
        args["boot"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("creation_date", None)
    if field is not None:
        args["creation_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["creation_date"] = None

    field = data.get("modification_date", None)
    if field is not None:
        args["modification_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["modification_date"] = None

    field = data.get("state", None)
    if field is not None:
        args["state"] = field
    else:
        args["state"] = None

    field = data.get("project", None)
    if field is not None:
        args["project"] = field
    else:
        args["project"] = None

    return VolumeServer(**args)


def unmarshal_Server(data: Any) -> Server:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Server' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("organization", None)
    if field is not None:
        args["organization"] = field
    else:
        args["organization"] = None

    field = data.get("project", None)
    if field is not None:
        args["project"] = field
    else:
        args["project"] = None

    field = data.get("allowed_actions", None)
    if field is not None:
        args["allowed_actions"] = (
            [ServerAction(v) for v in field] if field is not None else None
        )
    else:
        args["allowed_actions"] = []

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("commercial_type", None)
    if field is not None:
        args["commercial_type"] = field
    else:
        args["commercial_type"] = None

    field = data.get("dynamic_ip_required", None)
    if field is not None:
        args["dynamic_ip_required"] = field
    else:
        args["dynamic_ip_required"] = False

    field = data.get("routed_ip_enabled", None)
    if field is not None:
        args["routed_ip_enabled"] = field
    else:
        args["routed_ip_enabled"] = False

    field = data.get("creation_date", None)
    if field is not None:
        args["creation_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["creation_date"] = None

    field = data.get("enable_ipv6", None)
    if field is not None:
        args["enable_ipv6"] = field
    else:
        args["enable_ipv6"] = False

    field = data.get("hostname", None)
    if field is not None:
        args["hostname"] = field
    else:
        args["hostname"] = None

    field = data.get("protected", None)
    if field is not None:
        args["protected"] = field
    else:
        args["protected"] = False

    field = data.get("public_ips", None)
    if field is not None:
        args["public_ips"] = (
            [unmarshal_ServerIp(v) for v in field] if field is not None else None
        )
    else:
        args["public_ips"] = []

    field = data.get("mac_address", None)
    if field is not None:
        args["mac_address"] = field
    else:
        args["mac_address"] = None

    field = data.get("state", None)
    if field is not None:
        args["state"] = field
    else:
        args["state"] = ServerState.RUNNING

    field = data.get("boot_type", None)
    if field is not None:
        args["boot_type"] = field
    else:
        args["boot_type"] = BootType.LOCAL

    field = data.get("volumes", None)
    if field is not None:
        args["volumes"] = (
            {key: unmarshal_VolumeServer(value) for key, value in field.items()}
            if field is not None
            else None
        )
    else:
        args["volumes"] = {}

    field = data.get("maintenances", None)
    if field is not None:
        args["maintenances"] = (
            [unmarshal_ServerMaintenance(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["maintenances"] = []

    field = data.get("state_detail", None)
    if field is not None:
        args["state_detail"] = field
    else:
        args["state_detail"] = None

    field = data.get("image", None)
    if field is not None:
        args["image"] = unmarshal_Image(field)
    else:
        args["image"] = None

    field = data.get("private_ip", None)
    if field is not None:
        args["private_ip"] = field
    else:
        args["private_ip"] = None

    field = data.get("public_ip", None)
    if field is not None:
        args["public_ip"] = unmarshal_ServerIp(field)
    else:
        args["public_ip"] = None

    field = data.get("modification_date", None)
    if field is not None:
        args["modification_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["modification_date"] = None

    field = data.get("location", None)
    if field is not None:
        args["location"] = unmarshal_ServerLocation(field)
    else:
        args["location"] = None

    field = data.get("ipv6", None)
    if field is not None:
        args["ipv6"] = unmarshal_ServerIpv6(field)
    else:
        args["ipv6"] = None

    field = data.get("security_group", None)
    if field is not None:
        args["security_group"] = unmarshal_SecurityGroupSummary(field)
    else:
        args["security_group"] = None

    field = data.get("arch", None)
    if field is not None:
        args["arch"] = field
    else:
        args["arch"] = Arch.UNKNOWN_ARCH

    field = data.get("private_nics", None)
    if field is not None:
        args["private_nics"] = (
            [unmarshal_PrivateNIC(v) for v in field] if field is not None else None
        )
    else:
        args["private_nics"] = []

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("filesystems", None)
    if field is not None:
        args["filesystems"] = (
            [unmarshal_ServerFilesystem(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["filesystems"] = []

    field = data.get("end_of_service", None)
    if field is not None:
        args["end_of_service"] = field
    else:
        args["end_of_service"] = False

    field = data.get("placement_group", None)
    if field is not None:
        args["placement_group"] = unmarshal_PlacementGroup(field)
    else:
        args["placement_group"] = None

    field = data.get("admin_password_encryption_ssh_key_id", None)
    if field is not None:
        args["admin_password_encryption_ssh_key_id"] = field
    else:
        args["admin_password_encryption_ssh_key_id"] = None

    field = data.get("admin_password_encrypted_value", None)
    if field is not None:
        args["admin_password_encrypted_value"] = field
    else:
        args["admin_password_encrypted_value"] = None

    field = data.get("dns", None)
    if field is not None:
        args["dns"] = field
    else:
        args["dns"] = None

    return Server(**args)


def unmarshal_AttachServerFileSystemResponse(
    data: Any,
) -> AttachServerFileSystemResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AttachServerFileSystemResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("server", None)
    if field is not None:
        args["server"] = unmarshal_Server(field)
    else:
        args["server"] = None

    return AttachServerFileSystemResponse(**args)


def unmarshal_AttachServerVolumeResponse(data: Any) -> AttachServerVolumeResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AttachServerVolumeResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("server", None)
    if field is not None:
        args["server"] = unmarshal_Server(field)
    else:
        args["server"] = None

    return AttachServerVolumeResponse(**args)


def unmarshal_CreateImageResponse(data: Any) -> CreateImageResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateImageResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("image", None)
    if field is not None:
        args["image"] = unmarshal_Image(field)
    else:
        args["image"] = None

    return CreateImageResponse(**args)


def unmarshal_Ip(data: Any) -> Ip:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Ip' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("address", None)
    if field is not None:
        args["address"] = field
    else:
        args["address"] = None

    field = data.get("organization", None)
    if field is not None:
        args["organization"] = field
    else:
        args["organization"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = None

    field = data.get("project", None)
    if field is not None:
        args["project"] = field
    else:
        args["project"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    field = data.get("state", None)
    if field is not None:
        args["state"] = field
    else:
        args["state"] = None

    field = data.get("prefix", None)
    if field is not None:
        args["prefix"] = field
    else:
        args["prefix"] = None

    field = data.get("ipam_id", None)
    if field is not None:
        args["ipam_id"] = field
    else:
        args["ipam_id"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("reverse", None)
    if field is not None:
        args["reverse"] = field
    else:
        args["reverse"] = None

    field = data.get("server", None)
    if field is not None:
        args["server"] = unmarshal_ServerSummary(field)
    else:
        args["server"] = None

    return Ip(**args)


def unmarshal_CreateIpResponse(data: Any) -> CreateIpResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateIpResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("ip", None)
    if field is not None:
        args["ip"] = unmarshal_Ip(field)
    else:
        args["ip"] = None

    return CreateIpResponse(**args)


def unmarshal_CreatePlacementGroupResponse(data: Any) -> CreatePlacementGroupResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreatePlacementGroupResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("placement_group", None)
    if field is not None:
        args["placement_group"] = unmarshal_PlacementGroup(field)
    else:
        args["placement_group"] = None

    return CreatePlacementGroupResponse(**args)


def unmarshal_CreatePrivateNICResponse(data: Any) -> CreatePrivateNICResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreatePrivateNICResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("private_nic", None)
    if field is not None:
        args["private_nic"] = unmarshal_PrivateNIC(field)
    else:
        args["private_nic"] = None

    return CreatePrivateNICResponse(**args)


def unmarshal_SecurityGroup(data: Any) -> SecurityGroup:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecurityGroup' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("enable_default_security", None)
    if field is not None:
        args["enable_default_security"] = field
    else:
        args["enable_default_security"] = False

    field = data.get("inbound_default_policy", None)
    if field is not None:
        args["inbound_default_policy"] = field
    else:
        args["inbound_default_policy"] = SecurityGroupPolicy.UNKNOWN_POLICY

    field = data.get("outbound_default_policy", None)
    if field is not None:
        args["outbound_default_policy"] = field
    else:
        args["outbound_default_policy"] = SecurityGroupPolicy.UNKNOWN_POLICY

    field = data.get("organization", None)
    if field is not None:
        args["organization"] = field
    else:
        args["organization"] = None

    field = data.get("project", None)
    if field is not None:
        args["project"] = field
    else:
        args["project"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("organization_default", None)
    if field is not None:
        args["organization_default"] = field
    else:
        args["organization_default"] = False

    field = data.get("project_default", None)
    if field is not None:
        args["project_default"] = field
    else:
        args["project_default"] = False

    field = data.get("servers", None)
    if field is not None:
        args["servers"] = (
            [unmarshal_ServerSummary(v) for v in field] if field is not None else None
        )
    else:
        args["servers"] = []

    field = data.get("stateful", None)
    if field is not None:
        args["stateful"] = field
    else:
        args["stateful"] = False

    field = data.get("state", None)
    if field is not None:
        args["state"] = field
    else:
        args["state"] = SecurityGroupState.AVAILABLE

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("creation_date", None)
    if field is not None:
        args["creation_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["creation_date"] = None

    field = data.get("modification_date", None)
    if field is not None:
        args["modification_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["modification_date"] = None

    return SecurityGroup(**args)


def unmarshal_CreateSecurityGroupResponse(data: Any) -> CreateSecurityGroupResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateSecurityGroupResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("security_group", None)
    if field is not None:
        args["security_group"] = unmarshal_SecurityGroup(field)
    else:
        args["security_group"] = None

    return CreateSecurityGroupResponse(**args)


def unmarshal_SecurityGroupRule(data: Any) -> SecurityGroupRule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecurityGroupRule' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("protocol", None)
    if field is not None:
        args["protocol"] = field
    else:
        args["protocol"] = None

    field = data.get("direction", None)
    if field is not None:
        args["direction"] = field
    else:
        args["direction"] = None

    field = data.get("action", None)
    if field is not None:
        args["action"] = field
    else:
        args["action"] = None

    field = data.get("ip_range", None)
    if field is not None:
        args["ip_range"] = field
    else:
        args["ip_range"] = None

    field = data.get("position", None)
    if field is not None:
        args["position"] = field
    else:
        args["position"] = None

    field = data.get("editable", None)
    if field is not None:
        args["editable"] = field
    else:
        args["editable"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("dest_port_from", None)
    if field is not None:
        args["dest_port_from"] = field
    else:
        args["dest_port_from"] = None

    field = data.get("dest_port_to", None)
    if field is not None:
        args["dest_port_to"] = field
    else:
        args["dest_port_to"] = None

    return SecurityGroupRule(**args)


def unmarshal_CreateSecurityGroupRuleResponse(
    data: Any,
) -> CreateSecurityGroupRuleResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateSecurityGroupRuleResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("rule", None)
    if field is not None:
        args["rule"] = unmarshal_SecurityGroupRule(field)
    else:
        args["rule"] = None

    return CreateSecurityGroupRuleResponse(**args)


def unmarshal_CreateServerResponse(data: Any) -> CreateServerResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateServerResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("server", None)
    if field is not None:
        args["server"] = unmarshal_Server(field)
    else:
        args["server"] = None

    return CreateServerResponse(**args)


def unmarshal_SnapshotBaseVolume(data: Any) -> SnapshotBaseVolume:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SnapshotBaseVolume' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return SnapshotBaseVolume(**args)


def unmarshal_Snapshot(data: Any) -> Snapshot:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Snapshot' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("organization", None)
    if field is not None:
        args["organization"] = field
    else:
        args["organization"] = None

    field = data.get("project", None)
    if field is not None:
        args["project"] = field
    else:
        args["project"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("volume_type", None)
    if field is not None:
        args["volume_type"] = field
    else:
        args["volume_type"] = VolumeVolumeType.L_SSD

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = 0

    field = data.get("state", None)
    if field is not None:
        args["state"] = field
    else:
        args["state"] = SnapshotState.AVAILABLE

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("base_volume", None)
    if field is not None:
        args["base_volume"] = unmarshal_SnapshotBaseVolume(field)
    else:
        args["base_volume"] = None

    field = data.get("creation_date", None)
    if field is not None:
        args["creation_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["creation_date"] = None

    field = data.get("modification_date", None)
    if field is not None:
        args["modification_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["modification_date"] = None

    field = data.get("error_reason", None)
    if field is not None:
        args["error_reason"] = field
    else:
        args["error_reason"] = None

    return Snapshot(**args)


def unmarshal_Task(data: Any) -> Task:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Task' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("progress", None)
    if field is not None:
        args["progress"] = field
    else:
        args["progress"] = 0

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = TaskStatus.PENDING

    field = data.get("href_from", None)
    if field is not None:
        args["href_from"] = field
    else:
        args["href_from"] = None

    field = data.get("href_result", None)
    if field is not None:
        args["href_result"] = field
    else:
        args["href_result"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("started_at", None)
    if field is not None:
        args["started_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["started_at"] = None

    field = data.get("terminated_at", None)
    if field is not None:
        args["terminated_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["terminated_at"] = None

    return Task(**args)


def unmarshal_CreateSnapshotResponse(data: Any) -> CreateSnapshotResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateSnapshotResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("snapshot", None)
    if field is not None:
        args["snapshot"] = unmarshal_Snapshot(field)
    else:
        args["snapshot"] = None

    field = data.get("task", None)
    if field is not None:
        args["task"] = unmarshal_Task(field)
    else:
        args["task"] = None

    return CreateSnapshotResponse(**args)


def unmarshal_CreateVolumeResponse(data: Any) -> CreateVolumeResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateVolumeResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("volume", None)
    if field is not None:
        args["volume"] = unmarshal_Volume(field)
    else:
        args["volume"] = None

    return CreateVolumeResponse(**args)


def unmarshal_DetachServerFileSystemResponse(
    data: Any,
) -> DetachServerFileSystemResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DetachServerFileSystemResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("server", None)
    if field is not None:
        args["server"] = unmarshal_Server(field)
    else:
        args["server"] = None

    return DetachServerFileSystemResponse(**args)


def unmarshal_DetachServerVolumeResponse(data: Any) -> DetachServerVolumeResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DetachServerVolumeResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("server", None)
    if field is not None:
        args["server"] = unmarshal_Server(field)
    else:
        args["server"] = None

    return DetachServerVolumeResponse(**args)


def unmarshal_ExportSnapshotResponse(data: Any) -> ExportSnapshotResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ExportSnapshotResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("task", None)
    if field is not None:
        args["task"] = unmarshal_Task(field)
    else:
        args["task"] = None

    return ExportSnapshotResponse(**args)


def unmarshal_Dashboard(data: Any) -> Dashboard:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Dashboard' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("volumes_count", None)
    if field is not None:
        args["volumes_count"] = field
    else:
        args["volumes_count"] = 0

    field = data.get("running_servers_count", None)
    if field is not None:
        args["running_servers_count"] = field
    else:
        args["running_servers_count"] = 0

    field = data.get("servers_by_types", None)
    if field is not None:
        args["servers_by_types"] = field
    else:
        args["servers_by_types"] = {}

    field = data.get("images_count", None)
    if field is not None:
        args["images_count"] = field
    else:
        args["images_count"] = 0

    field = data.get("snapshots_count", None)
    if field is not None:
        args["snapshots_count"] = field
    else:
        args["snapshots_count"] = 0

    field = data.get("servers_count", None)
    if field is not None:
        args["servers_count"] = field
    else:
        args["servers_count"] = 0

    field = data.get("ips_count", None)
    if field is not None:
        args["ips_count"] = field
    else:
        args["ips_count"] = 0

    field = data.get("security_groups_count", None)
    if field is not None:
        args["security_groups_count"] = field
    else:
        args["security_groups_count"] = 0

    field = data.get("ips_unused", None)
    if field is not None:
        args["ips_unused"] = field
    else:
        args["ips_unused"] = 0

    field = data.get("volumes_l_ssd_count", None)
    if field is not None:
        args["volumes_l_ssd_count"] = field
    else:
        args["volumes_l_ssd_count"] = 0

    field = data.get("volumes_l_ssd_total_size", None)
    if field is not None:
        args["volumes_l_ssd_total_size"] = field
    else:
        args["volumes_l_ssd_total_size"] = 0

    field = data.get("private_nics_count", None)
    if field is not None:
        args["private_nics_count"] = field
    else:
        args["private_nics_count"] = 0

    field = data.get("placement_groups_count", None)
    if field is not None:
        args["placement_groups_count"] = field
    else:
        args["placement_groups_count"] = 0

    field = data.get("volumes_scratch_count", None)
    if field is not None:
        args["volumes_scratch_count"] = field
    else:
        args["volumes_scratch_count"] = 0

    field = data.get("volumes_b_ssd_count", None)
    if field is not None:
        args["volumes_b_ssd_count"] = field
    else:
        args["volumes_b_ssd_count"] = 0

    field = data.get("volumes_b_ssd_total_size", None)
    if field is not None:
        args["volumes_b_ssd_total_size"] = field
    else:
        args["volumes_b_ssd_total_size"] = 0

    return Dashboard(**args)


def unmarshal_GetDashboardResponse(data: Any) -> GetDashboardResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetDashboardResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("dashboard", None)
    if field is not None:
        args["dashboard"] = unmarshal_Dashboard(field)
    else:
        args["dashboard"] = None

    return GetDashboardResponse(**args)


def unmarshal_GetImageResponse(data: Any) -> GetImageResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetImageResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("image", None)
    if field is not None:
        args["image"] = unmarshal_Image(field)
    else:
        args["image"] = None

    return GetImageResponse(**args)


def unmarshal_GetIpResponse(data: Any) -> GetIpResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetIpResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("ip", None)
    if field is not None:
        args["ip"] = unmarshal_Ip(field)
    else:
        args["ip"] = None

    return GetIpResponse(**args)


def unmarshal_GetPlacementGroupResponse(data: Any) -> GetPlacementGroupResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetPlacementGroupResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("placement_group", None)
    if field is not None:
        args["placement_group"] = unmarshal_PlacementGroup(field)
    else:
        args["placement_group"] = None

    return GetPlacementGroupResponse(**args)


def unmarshal_PlacementGroupServer(data: Any) -> PlacementGroupServer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlacementGroupServer' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("policy_respected", None)
    if field is not None:
        args["policy_respected"] = field
    else:
        args["policy_respected"] = False

    return PlacementGroupServer(**args)


def unmarshal_GetPlacementGroupServersResponse(
    data: Any,
) -> GetPlacementGroupServersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetPlacementGroupServersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("servers", None)
    if field is not None:
        args["servers"] = (
            [unmarshal_PlacementGroupServer(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["servers"] = []

    return GetPlacementGroupServersResponse(**args)


def unmarshal_GetPrivateNICResponse(data: Any) -> GetPrivateNICResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetPrivateNICResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("private_nic", None)
    if field is not None:
        args["private_nic"] = unmarshal_PrivateNIC(field)
    else:
        args["private_nic"] = None

    return GetPrivateNICResponse(**args)


def unmarshal_GetSecurityGroupResponse(data: Any) -> GetSecurityGroupResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetSecurityGroupResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("security_group", None)
    if field is not None:
        args["security_group"] = unmarshal_SecurityGroup(field)
    else:
        args["security_group"] = None

    return GetSecurityGroupResponse(**args)


def unmarshal_GetSecurityGroupRuleResponse(data: Any) -> GetSecurityGroupRuleResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetSecurityGroupRuleResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("rule", None)
    if field is not None:
        args["rule"] = unmarshal_SecurityGroupRule(field)
    else:
        args["rule"] = None

    return GetSecurityGroupRuleResponse(**args)


def unmarshal_GetServerResponse(data: Any) -> GetServerResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetServerResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("server", None)
    if field is not None:
        args["server"] = unmarshal_Server(field)
    else:
        args["server"] = None

    return GetServerResponse(**args)


def unmarshal_GetServerTypesAvailabilityResponseAvailability(
    data: Any,
) -> GetServerTypesAvailabilityResponseAvailability:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetServerTypesAvailabilityResponseAvailability' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("availability", None)
    if field is not None:
        args["availability"] = field
    else:
        args["availability"] = None

    return GetServerTypesAvailabilityResponseAvailability(**args)


def unmarshal_GetServerTypesAvailabilityResponse(
    data: Any,
) -> GetServerTypesAvailabilityResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetServerTypesAvailabilityResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("servers", None)
    if field is not None:
        args["servers"] = (
            {
                key: unmarshal_GetServerTypesAvailabilityResponseAvailability(value)
                for key, value in field.items()
            }
            if field is not None
            else None
        )
    else:
        args["servers"] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return GetServerTypesAvailabilityResponse(**args)


def unmarshal_GetSnapshotResponse(data: Any) -> GetSnapshotResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetSnapshotResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("snapshot", None)
    if field is not None:
        args["snapshot"] = unmarshal_Snapshot(field)
    else:
        args["snapshot"] = None

    return GetSnapshotResponse(**args)


def unmarshal_GetVolumeResponse(data: Any) -> GetVolumeResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetVolumeResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("volume", None)
    if field is not None:
        args["volume"] = unmarshal_Volume(field)
    else:
        args["volume"] = None

    return GetVolumeResponse(**args)


def unmarshal_ListImagesResponse(data: Any) -> ListImagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListImagesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("images", None)
    if field is not None:
        args["images"] = (
            [unmarshal_Image(v) for v in field] if field is not None else None
        )
    else:
        args["images"] = []

    return ListImagesResponse(**args)


def unmarshal_ListIpsResponse(data: Any) -> ListIpsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListIpsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("ips", None)
    if field is not None:
        args["ips"] = [unmarshal_Ip(v) for v in field] if field is not None else None
    else:
        args["ips"] = []

    return ListIpsResponse(**args)


def unmarshal_ListPlacementGroupsResponse(data: Any) -> ListPlacementGroupsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPlacementGroupsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("placement_groups", None)
    if field is not None:
        args["placement_groups"] = (
            [unmarshal_PlacementGroup(v) for v in field] if field is not None else None
        )
    else:
        args["placement_groups"] = []

    return ListPlacementGroupsResponse(**args)


def unmarshal_ListPrivateNICsResponse(data: Any) -> ListPrivateNICsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPrivateNICsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("private_nics", None)
    if field is not None:
        args["private_nics"] = (
            [unmarshal_PrivateNIC(v) for v in field] if field is not None else None
        )
    else:
        args["private_nics"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    return ListPrivateNICsResponse(**args)


def unmarshal_ListSecurityGroupRulesResponse(
    data: Any,
) -> ListSecurityGroupRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSecurityGroupRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("rules", None)
    if field is not None:
        args["rules"] = (
            [unmarshal_SecurityGroupRule(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["rules"] = []

    return ListSecurityGroupRulesResponse(**args)


def unmarshal_ListSecurityGroupsResponse(data: Any) -> ListSecurityGroupsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSecurityGroupsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("security_groups", None)
    if field is not None:
        args["security_groups"] = (
            [unmarshal_SecurityGroup(v) for v in field] if field is not None else None
        )
    else:
        args["security_groups"] = []

    return ListSecurityGroupsResponse(**args)


def unmarshal_ListServerActionsResponse(data: Any) -> ListServerActionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServerActionsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("actions", None)
    if field is not None:
        args["actions"] = (
            [ServerAction(v) for v in field] if field is not None else None
        )
    else:
        args["actions"] = None

    return ListServerActionsResponse(**args)


def unmarshal_ListServerUserDataResponse(data: Any) -> ListServerUserDataResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServerUserDataResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("user_data", None)
    if field is not None:
        args["user_data"] = field
    else:
        args["user_data"] = None

    return ListServerUserDataResponse(**args)


def unmarshal_ListServersResponse(data: Any) -> ListServersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("servers", None)
    if field is not None:
        args["servers"] = (
            [unmarshal_Server(v) for v in field] if field is not None else None
        )
    else:
        args["servers"] = []

    return ListServersResponse(**args)


def unmarshal_ServerTypeNetworkInterface(data: Any) -> ServerTypeNetworkInterface:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeNetworkInterface' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("internal_bandwidth", None)
    if field is not None:
        args["internal_bandwidth"] = field
    else:
        args["internal_bandwidth"] = 0

    field = data.get("internet_bandwidth", None)
    if field is not None:
        args["internet_bandwidth"] = field
    else:
        args["internet_bandwidth"] = 0

    return ServerTypeNetworkInterface(**args)


def unmarshal_ServerTypeVolumeConstraintSizes(
    data: Any,
) -> ServerTypeVolumeConstraintSizes:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeVolumeConstraintSizes' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("min_size", None)
    if field is not None:
        args["min_size"] = field
    else:
        args["min_size"] = 0

    field = data.get("max_size", None)
    if field is not None:
        args["max_size"] = field
    else:
        args["max_size"] = 0

    return ServerTypeVolumeConstraintSizes(**args)


def unmarshal_ServerTypeCapabilities(data: Any) -> ServerTypeCapabilities:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeCapabilities' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("boot_types", None)
    if field is not None:
        args["boot_types"] = [BootType(v) for v in field] if field is not None else None
    else:
        args["boot_types"] = []

    field = data.get("max_file_systems", None)
    if field is not None:
        args["max_file_systems"] = field
    else:
        args["max_file_systems"] = 0

    field = data.get("block_storage", None)
    if field is not None:
        args["block_storage"] = field
    else:
        args["block_storage"] = False

    return ServerTypeCapabilities(**args)


def unmarshal_ServerTypeGPUInfo(data: Any) -> ServerTypeGPUInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeGPUInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("gpu_manufacturer", None)
    if field is not None:
        args["gpu_manufacturer"] = field
    else:
        args["gpu_manufacturer"] = None

    field = data.get("gpu_name", None)
    if field is not None:
        args["gpu_name"] = field
    else:
        args["gpu_name"] = None

    field = data.get("gpu_memory", None)
    if field is not None:
        args["gpu_memory"] = field
    else:
        args["gpu_memory"] = 0

    return ServerTypeGPUInfo(**args)


def unmarshal_ServerTypeNetwork(data: Any) -> ServerTypeNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeNetwork' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("interfaces", None)
    if field is not None:
        args["interfaces"] = (
            [unmarshal_ServerTypeNetworkInterface(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["interfaces"] = []

    field = data.get("ipv6_support", None)
    if field is not None:
        args["ipv6_support"] = field
    else:
        args["ipv6_support"] = False

    field = data.get("sum_internal_bandwidth", None)
    if field is not None:
        args["sum_internal_bandwidth"] = field
    else:
        args["sum_internal_bandwidth"] = 0

    field = data.get("sum_internet_bandwidth", None)
    if field is not None:
        args["sum_internet_bandwidth"] = field
    else:
        args["sum_internet_bandwidth"] = 0

    return ServerTypeNetwork(**args)


def unmarshal_ServerTypeVolumeConstraintsByType(
    data: Any,
) -> ServerTypeVolumeConstraintsByType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeVolumeConstraintsByType' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("l_ssd", None)
    if field is not None:
        args["l_ssd"] = unmarshal_ServerTypeVolumeConstraintSizes(field)
    else:
        args["l_ssd"] = None

    return ServerTypeVolumeConstraintsByType(**args)


def unmarshal_ServerType(data: Any) -> ServerType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerType' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("monthly_price", None)
    if field is not None:
        args["monthly_price"] = field
    else:
        args["monthly_price"] = 0.0

    field = data.get("hourly_price", None)
    if field is not None:
        args["hourly_price"] = field
    else:
        args["hourly_price"] = 0.0

    field = data.get("alt_names", None)
    if field is not None:
        args["alt_names"] = field
    else:
        args["alt_names"] = []

    field = data.get("ncpus", None)
    if field is not None:
        args["ncpus"] = field
    else:
        args["ncpus"] = 0

    field = data.get("ram", None)
    if field is not None:
        args["ram"] = field
    else:
        args["ram"] = 0

    field = data.get("arch", None)
    if field is not None:
        args["arch"] = field
    else:
        args["arch"] = Arch.UNKNOWN_ARCH

    field = data.get("per_volume_constraint", None)
    if field is not None:
        args["per_volume_constraint"] = unmarshal_ServerTypeVolumeConstraintsByType(
            field
        )
    else:
        args["per_volume_constraint"] = None

    field = data.get("volumes_constraint", None)
    if field is not None:
        args["volumes_constraint"] = unmarshal_ServerTypeVolumeConstraintSizes(field)
    else:
        args["volumes_constraint"] = None

    field = data.get("gpu", None)
    if field is not None:
        args["gpu"] = field
    else:
        args["gpu"] = 0

    field = data.get("scratch_storage_max_volumes_count", None)
    if field is not None:
        args["scratch_storage_max_volumes_count"] = field
    else:
        args["scratch_storage_max_volumes_count"] = 0

    field = data.get("end_of_service", None)
    if field is not None:
        args["end_of_service"] = field
    else:
        args["end_of_service"] = False

    field = data.get("gpu_info", None)
    if field is not None:
        args["gpu_info"] = unmarshal_ServerTypeGPUInfo(field)
    else:
        args["gpu_info"] = None

    field = data.get("network", None)
    if field is not None:
        args["network"] = unmarshal_ServerTypeNetwork(field)
    else:
        args["network"] = None

    field = data.get("capabilities", None)
    if field is not None:
        args["capabilities"] = unmarshal_ServerTypeCapabilities(field)
    else:
        args["capabilities"] = None

    field = data.get("scratch_storage_max_size", None)
    if field is not None:
        args["scratch_storage_max_size"] = field
    else:
        args["scratch_storage_max_size"] = 0

    field = data.get("block_bandwidth", None)
    if field is not None:
        args["block_bandwidth"] = field
    else:
        args["block_bandwidth"] = 0

    return ServerType(**args)


def unmarshal_ListServersTypesResponse(data: Any) -> ListServersTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServersTypesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("servers", None)
    if field is not None:
        args["servers"] = (
            {key: unmarshal_ServerType(value) for key, value in field.items()}
            if field is not None
            else None
        )
    else:
        args["servers"] = {}

    return ListServersTypesResponse(**args)


def unmarshal_ListSnapshotsResponse(data: Any) -> ListSnapshotsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSnapshotsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("snapshots", None)
    if field is not None:
        args["snapshots"] = (
            [unmarshal_Snapshot(v) for v in field] if field is not None else None
        )
    else:
        args["snapshots"] = []

    return ListSnapshotsResponse(**args)


def unmarshal_ListVolumesResponse(data: Any) -> ListVolumesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVolumesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("volumes", None)
    if field is not None:
        args["volumes"] = (
            [unmarshal_Volume(v) for v in field] if field is not None else None
        )
    else:
        args["volumes"] = []

    return ListVolumesResponse(**args)


def unmarshal_VolumeTypeCapabilities(data: Any) -> VolumeTypeCapabilities:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeTypeCapabilities' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("snapshot", None)
    if field is not None:
        args["snapshot"] = field
    else:
        args["snapshot"] = None

    return VolumeTypeCapabilities(**args)


def unmarshal_VolumeTypeConstraints(data: Any) -> VolumeTypeConstraints:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeTypeConstraints' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("min", None)
    if field is not None:
        args["min"] = field
    else:
        args["min"] = None

    field = data.get("max", None)
    if field is not None:
        args["max"] = field
    else:
        args["max"] = None

    return VolumeTypeConstraints(**args)


def unmarshal_VolumeType(data: Any) -> VolumeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeType' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("display_name", None)
    if field is not None:
        args["display_name"] = field
    else:
        args["display_name"] = None

    field = data.get("capabilities", None)
    if field is not None:
        args["capabilities"] = unmarshal_VolumeTypeCapabilities(field)
    else:
        args["capabilities"] = None

    field = data.get("constraints", None)
    if field is not None:
        args["constraints"] = unmarshal_VolumeTypeConstraints(field)
    else:
        args["constraints"] = None

    return VolumeType(**args)


def unmarshal_ListVolumesTypesResponse(data: Any) -> ListVolumesTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVolumesTypesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("volumes", None)
    if field is not None:
        args["volumes"] = (
            {key: unmarshal_VolumeType(value) for key, value in field.items()}
            if field is not None
            else None
        )
    else:
        args["volumes"] = {}

    return ListVolumesTypesResponse(**args)


def unmarshal_MigrationPlan(data: Any) -> MigrationPlan:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'MigrationPlan' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("snapshots", None)
    if field is not None:
        args["snapshots"] = (
            [unmarshal_Snapshot(v) for v in field] if field is not None else None
        )
    else:
        args["snapshots"] = []

    field = data.get("validation_key", None)
    if field is not None:
        args["validation_key"] = field
    else:
        args["validation_key"] = None

    field = data.get("volume", None)
    if field is not None:
        args["volume"] = unmarshal_Volume(field)
    else:
        args["volume"] = None

    return MigrationPlan(**args)


def unmarshal_ServerActionResponse(data: Any) -> ServerActionResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerActionResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("task", None)
    if field is not None:
        args["task"] = unmarshal_Task(field)
    else:
        args["task"] = None

    return ServerActionResponse(**args)


def unmarshal_ServerCompatibleTypes(data: Any) -> ServerCompatibleTypes:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerCompatibleTypes' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("compatible_types", None)
    if field is not None:
        args["compatible_types"] = field
    else:
        args["compatible_types"] = []

    return ServerCompatibleTypes(**args)


def unmarshal_SetPlacementGroupResponse(data: Any) -> SetPlacementGroupResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetPlacementGroupResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("placement_group", None)
    if field is not None:
        args["placement_group"] = unmarshal_PlacementGroup(field)
    else:
        args["placement_group"] = None

    return SetPlacementGroupResponse(**args)


def unmarshal_SetPlacementGroupServersResponse(
    data: Any,
) -> SetPlacementGroupServersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetPlacementGroupServersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("servers", None)
    if field is not None:
        args["servers"] = (
            [unmarshal_PlacementGroupServer(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["servers"] = []

    return SetPlacementGroupServersResponse(**args)


def unmarshal_SetSecurityGroupRulesResponse(data: Any) -> SetSecurityGroupRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetSecurityGroupRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("rules", None)
    if field is not None:
        args["rules"] = (
            [unmarshal_SecurityGroupRule(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["rules"] = None

    return SetSecurityGroupRulesResponse(**args)


def unmarshal_UpdateImageResponse(data: Any) -> UpdateImageResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateImageResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("image", None)
    if field is not None:
        args["image"] = unmarshal_Image(field)
    else:
        args["image"] = None

    return UpdateImageResponse(**args)


def unmarshal_UpdateIpResponse(data: Any) -> UpdateIpResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateIpResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("ip", None)
    if field is not None:
        args["ip"] = unmarshal_Ip(field)
    else:
        args["ip"] = None

    return UpdateIpResponse(**args)


def unmarshal_UpdatePlacementGroupResponse(data: Any) -> UpdatePlacementGroupResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdatePlacementGroupResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("placement_group", None)
    if field is not None:
        args["placement_group"] = unmarshal_PlacementGroup(field)
    else:
        args["placement_group"] = None

    return UpdatePlacementGroupResponse(**args)


def unmarshal_UpdatePlacementGroupServersResponse(
    data: Any,
) -> UpdatePlacementGroupServersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdatePlacementGroupServersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("servers", None)
    if field is not None:
        args["servers"] = (
            [unmarshal_PlacementGroupServer(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["servers"] = []

    return UpdatePlacementGroupServersResponse(**args)


def unmarshal_UpdateSecurityGroupResponse(data: Any) -> UpdateSecurityGroupResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateSecurityGroupResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("security_group", None)
    if field is not None:
        args["security_group"] = unmarshal_SecurityGroup(field)
    else:
        args["security_group"] = None

    return UpdateSecurityGroupResponse(**args)


def unmarshal_UpdateSecurityGroupRuleResponse(
    data: Any,
) -> UpdateSecurityGroupRuleResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateSecurityGroupRuleResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("rule", None)
    if field is not None:
        args["rule"] = unmarshal_SecurityGroupRule(field)
    else:
        args["rule"] = None

    return UpdateSecurityGroupRuleResponse(**args)


def unmarshal_UpdateServerResponse(data: Any) -> UpdateServerResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateServerResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("server", None)
    if field is not None:
        args["server"] = unmarshal_Server(field)
    else:
        args["server"] = None

    return UpdateServerResponse(**args)


def unmarshal_UpdateSnapshotResponse(data: Any) -> UpdateSnapshotResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateSnapshotResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("snapshot", None)
    if field is not None:
        args["snapshot"] = unmarshal_Snapshot(field)
    else:
        args["snapshot"] = None

    return UpdateSnapshotResponse(**args)


def unmarshal_UpdateVolumeResponse(data: Any) -> UpdateVolumeResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateVolumeResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("volume", None)
    if field is not None:
        args["volume"] = unmarshal_Volume(field)
    else:
        args["volume"] = None

    return UpdateVolumeResponse(**args)


def unmarshal__SetImageResponse(data: Any) -> _SetImageResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type '_SetImageResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("image", None)
    if field is not None:
        args["image"] = unmarshal_Image(field)
    else:
        args["image"] = None

    return _SetImageResponse(**args)


def unmarshal__SetSecurityGroupResponse(data: Any) -> _SetSecurityGroupResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type '_SetSecurityGroupResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("security_group", None)
    if field is not None:
        args["security_group"] = unmarshal_SecurityGroup(field)
    else:
        args["security_group"] = None

    return _SetSecurityGroupResponse(**args)


def unmarshal__SetSecurityGroupRuleResponse(data: Any) -> _SetSecurityGroupRuleResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type '_SetSecurityGroupRuleResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("rule", None)
    if field is not None:
        args["rule"] = unmarshal_SecurityGroupRule(field)
    else:
        args["rule"] = None

    return _SetSecurityGroupRuleResponse(**args)


def unmarshal__SetServerResponse(data: Any) -> _SetServerResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type '_SetServerResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("server", None)
    if field is not None:
        args["server"] = unmarshal_Server(field)
    else:
        args["server"] = None

    return _SetServerResponse(**args)


def unmarshal__SetSnapshotResponse(data: Any) -> _SetSnapshotResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type '_SetSnapshotResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("snapshot", None)
    if field is not None:
        args["snapshot"] = unmarshal_Snapshot(field)
    else:
        args["snapshot"] = None

    return _SetSnapshotResponse(**args)


def marshal_ApplyBlockMigrationRequest(
    request: ApplyBlockMigrationRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="volume_id", value=request.volume_id, marshal_func=None
                ),
                OneOfPossibility(
                    param="snapshot_id", value=request.snapshot_id, marshal_func=None
                ),
            ]
        ),
    )

    if request.validation_key is not None:
        output["validation_key"] = request.validation_key

    return output


def marshal_AttachServerFileSystemRequest(
    request: AttachServerFileSystemRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.filesystem_id is not None:
        output["filesystem_id"] = request.filesystem_id

    return output


def marshal_AttachServerVolumeRequest(
    request: AttachServerVolumeRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.volume_id is not None:
        output["volume_id"] = request.volume_id

    if request.volume_type is not None:
        output["volume_type"] = request.volume_type

    if request.boot is not None:
        output["boot"] = request.boot

    return output


def marshal_CheckBlockMigrationOrganizationQuotasRequest(
    request: CheckBlockMigrationOrganizationQuotasRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.organization is not None:
        output["organization"] = request.organization
    else:
        output["organization"] = defaults.default_organization_id

    return output


def marshal_VolumeTemplate(
    request: VolumeTemplate,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="project",
                    value=request.project,
                    default=defaults.default_project_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="organization",
                    value=request.organization,
                    default=defaults.default_organization_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.id is not None:
        output["id"] = request.id

    if request.name is not None:
        output["name"] = request.name

    if request.size is not None:
        output["size"] = request.size

    if request.volume_type is not None:
        output["volume_type"] = request.volume_type

    return output


def marshal_CreateImageRequest(
    request: CreateImageRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="project",
                    value=request.project,
                    default=defaults.default_project_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="organization",
                    value=request.organization,
                    default=defaults.default_organization_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.root_volume is not None:
        output["root_volume"] = request.root_volume

    if request.arch is not None:
        output["arch"] = request.arch

    if request.name is not None:
        output["name"] = request.name

    if request.extra_volumes is not None:
        output["extra_volumes"] = {
            key: marshal_VolumeTemplate(value, defaults)
            for key, value in request.extra_volumes.items()
        }

    if request.tags is not None:
        output["tags"] = request.tags

    if request.public is not None:
        output["public"] = request.public

    return output


def marshal_CreateIpRequest(
    request: CreateIpRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="project",
                    value=request.project,
                    default=defaults.default_project_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="organization",
                    value=request.organization,
                    default=defaults.default_organization_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.tags is not None:
        output["tags"] = request.tags

    if request.server is not None:
        output["server"] = request.server

    if request.type_ is not None:
        output["type"] = request.type_

    return output


def marshal_CreatePlacementGroupRequest(
    request: CreatePlacementGroupRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="project",
                    value=request.project,
                    default=defaults.default_project_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="organization",
                    value=request.organization,
                    default=defaults.default_organization_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.policy_mode is not None:
        output["policy_mode"] = request.policy_mode

    if request.policy_type is not None:
        output["policy_type"] = request.policy_type

    return output


def marshal_CreatePrivateNICRequest(
    request: CreatePrivateNICRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.ip_ids is not None:
        output["ip_ids"] = request.ip_ids

    if request.ipam_ip_ids is not None:
        output["ipam_ip_ids"] = request.ipam_ip_ids

    return output


def marshal_CreateSecurityGroupRequest(
    request: CreateSecurityGroupRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="project",
                    value=request.project,
                    default=defaults.default_project_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="organization",
                    value=request.organization,
                    default=defaults.default_organization_id,
                    marshal_func=None,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="organization_default",
                    value=request.organization_default,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="project_default",
                    value=request.project_default,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.description is not None:
        output["description"] = request.description

    if request.stateful is not None:
        output["stateful"] = request.stateful

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.inbound_default_policy is not None:
        output["inbound_default_policy"] = request.inbound_default_policy

    if request.outbound_default_policy is not None:
        output["outbound_default_policy"] = request.outbound_default_policy

    if request.enable_default_security is not None:
        output["enable_default_security"] = request.enable_default_security

    return output


def marshal_CreateSecurityGroupRuleRequest(
    request: CreateSecurityGroupRuleRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.protocol is not None:
        output["protocol"] = request.protocol

    if request.direction is not None:
        output["direction"] = request.direction

    if request.action is not None:
        output["action"] = request.action

    if request.ip_range is not None:
        output["ip_range"] = request.ip_range

    if request.position is not None:
        output["position"] = request.position

    if request.editable is not None:
        output["editable"] = request.editable

    if request.dest_port_from is not None:
        output["dest_port_from"] = request.dest_port_from

    if request.dest_port_to is not None:
        output["dest_port_to"] = request.dest_port_to

    return output


def marshal_VolumeServerTemplate(
    request: VolumeServerTemplate,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.volume_type is not None:
        output["volume_type"] = request.volume_type

    if request.id is not None:
        output["id"] = request.id

    if request.boot is not None:
        output["boot"] = request.boot

    if request.name is not None:
        output["name"] = request.name

    if request.size is not None:
        output["size"] = request.size

    if request.base_snapshot is not None:
        output["base_snapshot"] = request.base_snapshot

    if request.organization is not None:
        output["organization"] = request.organization

    if request.project is not None:
        output["project"] = request.project

    return output


def marshal_CreateServerRequest(
    request: CreateServerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="project",
                    value=request.project,
                    default=defaults.default_project_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="organization",
                    value=request.organization,
                    default=defaults.default_organization_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.commercial_type is not None:
        output["commercial_type"] = request.commercial_type

    if request.enable_ipv6 is not None:
        output["enable_ipv6"] = request.enable_ipv6

    if request.name is not None:
        output["name"] = request.name

    if request.dynamic_ip_required is not None:
        output["dynamic_ip_required"] = request.dynamic_ip_required

    if request.routed_ip_enabled is not None:
        output["routed_ip_enabled"] = request.routed_ip_enabled

    if request.image is not None:
        output["image"] = request.image

    if request.volumes is not None:
        output["volumes"] = {
            key: marshal_VolumeServerTemplate(value, defaults)
            for key, value in request.volumes.items()
        }

    if request.protected is not None:
        output["protected"] = request.protected

    if request.public_ip is not None:
        output["public_ip"] = request.public_ip

    if request.public_ips is not None:
        output["public_ips"] = request.public_ips

    if request.boot_type is not None:
        output["boot_type"] = request.boot_type

    if request.tags is not None:
        output["tags"] = request.tags

    if request.security_group is not None:
        output["security_group"] = request.security_group

    if request.placement_group is not None:
        output["placement_group"] = request.placement_group

    if request.admin_password_encryption_ssh_key_id is not None:
        output["admin_password_encryption_ssh_key_id"] = (
            request.admin_password_encryption_ssh_key_id
        )

    return output


def marshal_CreateSnapshotRequest(
    request: CreateSnapshotRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="project",
                    value=request.project,
                    default=defaults.default_project_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="organization",
                    value=request.organization,
                    default=defaults.default_organization_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.volume_id is not None:
        output["volume_id"] = request.volume_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.volume_type is not None:
        output["volume_type"] = request.volume_type

    if request.bucket is not None:
        output["bucket"] = request.bucket

    if request.key is not None:
        output["key"] = request.key

    if request.size is not None:
        output["size"] = request.size

    return output


def marshal_CreateVolumeRequest(
    request: CreateVolumeRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="project",
                    value=request.project,
                    default=defaults.default_project_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="organization",
                    value=request.organization,
                    default=defaults.default_organization_id,
                    marshal_func=None,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(param="size", value=request.size, marshal_func=None),
                OneOfPossibility(
                    param="base_snapshot",
                    value=request.base_snapshot,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.volume_type is not None:
        output["volume_type"] = request.volume_type

    return output


def marshal_DetachServerFileSystemRequest(
    request: DetachServerFileSystemRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.filesystem_id is not None:
        output["filesystem_id"] = request.filesystem_id

    return output


def marshal_DetachServerVolumeRequest(
    request: DetachServerVolumeRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.volume_id is not None:
        output["volume_id"] = request.volume_id

    return output


def marshal_ExportSnapshotRequest(
    request: ExportSnapshotRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.bucket is not None:
        output["bucket"] = request.bucket

    if request.key is not None:
        output["key"] = request.key

    return output


def marshal_PlanBlockMigrationRequest(
    request: PlanBlockMigrationRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="volume_id", value=request.volume_id, marshal_func=None
                ),
                OneOfPossibility(
                    param="snapshot_id", value=request.snapshot_id, marshal_func=None
                ),
            ]
        ),
    )

    return output


def marshal_ServerActionRequestVolumeBackupTemplate(
    request: ServerActionRequestVolumeBackupTemplate,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.volume_type is not None:
        output["volume_type"] = request.volume_type

    return output


def marshal_ServerActionRequest(
    request: ServerActionRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.action is not None:
        output["action"] = request.action

    if request.name is not None:
        output["name"] = request.name

    if request.volumes is not None:
        output["volumes"] = {
            key: marshal_ServerActionRequestVolumeBackupTemplate(value, defaults)
            for key, value in request.volumes.items()
        }

    if request.disable_ipv6 is not None:
        output["disable_ipv6"] = request.disable_ipv6

    return output


def marshal_ServerSummary(
    request: ServerSummary,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_Bootscript(
    request: Bootscript,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.architecture is not None:
        output["architecture"] = request.architecture

    if request.bootcmdargs is not None:
        output["bootcmdargs"] = request.bootcmdargs

    if request.default is not None:
        output["default"] = request.default

    if request.dtb is not None:
        output["dtb"] = request.dtb

    if request.id is not None:
        output["id"] = request.id

    if request.initrd is not None:
        output["initrd"] = request.initrd

    if request.kernel is not None:
        output["kernel"] = request.kernel

    if request.organization is not None:
        output["organization"] = request.organization
    else:
        output["organization"] = defaults.default_organization_id

    if request.public is not None:
        output["public"] = request.public

    if request.title is not None:
        output["title"] = request.title

    if request.project is not None:
        output["project"] = request.project
    else:
        output["project"] = defaults.default_project_id

    if request.zone is not None:
        output["zone"] = request.zone
    else:
        output["zone"] = defaults.default_zone

    return output


def marshal_Volume(
    request: Volume,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.name is not None:
        output["name"] = request.name

    if request.export_uri is not None:
        output["export_uri"] = request.export_uri

    if request.size is not None:
        output["size"] = request.size

    if request.volume_type is not None:
        output["volume_type"] = request.volume_type

    if request.organization is not None:
        output["organization"] = request.organization
    else:
        output["organization"] = defaults.default_organization_id

    if request.project is not None:
        output["project"] = request.project
    else:
        output["project"] = defaults.default_project_id

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date.isoformat()

    if request.modification_date is not None:
        output["modification_date"] = request.modification_date.isoformat()

    if request.tags is not None:
        output["tags"] = request.tags

    if request.state is not None:
        output["state"] = request.state

    if request.zone is not None:
        output["zone"] = request.zone
    else:
        output["zone"] = defaults.default_zone

    if request.server is not None:
        output["server"] = marshal_ServerSummary(request.server, defaults)

    return output


def marshal_VolumeSummary(
    request: VolumeSummary,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.name is not None:
        output["name"] = request.name

    if request.size is not None:
        output["size"] = request.size

    if request.volume_type is not None:
        output["volume_type"] = request.volume_type

    return output


def marshal_SetImageRequest(
    request: SetImageRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.arch is not None:
        output["arch"] = request.arch

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date.isoformat()

    if request.modification_date is not None:
        output["modification_date"] = request.modification_date.isoformat()

    if request.from_server is not None:
        output["from_server"] = request.from_server

    if request.public is not None:
        output["public"] = request.public

    if request.default_bootscript is not None:
        output["default_bootscript"] = marshal_Bootscript(
            request.default_bootscript, defaults
        )

    if request.extra_volumes is not None:
        output["extra_volumes"] = {
            key: marshal_Volume(value, defaults)
            for key, value in request.extra_volumes.items()
        }

    if request.organization is not None:
        output["organization"] = request.organization
    else:
        output["organization"] = defaults.default_organization_id

    if request.root_volume is not None:
        output["root_volume"] = marshal_VolumeSummary(request.root_volume, defaults)

    if request.state is not None:
        output["state"] = request.state

    if request.project is not None:
        output["project"] = request.project
    else:
        output["project"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_SetPlacementGroupRequest(
    request: SetPlacementGroupRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.organization is not None:
        output["organization"] = request.organization
    else:
        output["organization"] = defaults.default_organization_id

    if request.policy_mode is not None:
        output["policy_mode"] = request.policy_mode

    if request.policy_type is not None:
        output["policy_type"] = request.policy_type

    if request.project is not None:
        output["project"] = request.project
    else:
        output["project"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_SetPlacementGroupServersRequest(
    request: SetPlacementGroupServersRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.servers is not None:
        output["servers"] = request.servers

    return output


def marshal_SetSecurityGroupRulesRequestRule(
    request: SetSecurityGroupRulesRequestRule,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.action is not None:
        output["action"] = request.action

    if request.protocol is not None:
        output["protocol"] = request.protocol

    if request.direction is not None:
        output["direction"] = request.direction

    if request.ip_range is not None:
        output["ip_range"] = request.ip_range

    if request.position is not None:
        output["position"] = request.position

    if request.id is not None:
        output["id"] = request.id

    if request.dest_port_from is not None:
        output["dest_port_from"] = request.dest_port_from

    if request.dest_port_to is not None:
        output["dest_port_to"] = request.dest_port_to

    if request.editable is not None:
        output["editable"] = request.editable

    if request.zone is not None:
        output["zone"] = request.zone

    return output


def marshal_SetSecurityGroupRulesRequest(
    request: SetSecurityGroupRulesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.rules is not None:
        output["rules"] = [
            marshal_SetSecurityGroupRulesRequestRule(item, defaults)
            for item in request.rules
        ]

    return output


def marshal_VolumeImageUpdateTemplate(
    request: VolumeImageUpdateTemplate,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    return output


def marshal_UpdateImageRequest(
    request: UpdateImageRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.arch is not None:
        output["arch"] = request.arch

    if request.extra_volumes is not None:
        output["extra_volumes"] = {
            key: marshal_VolumeImageUpdateTemplate(value, defaults)
            for key, value in request.extra_volumes.items()
        }

    if request.tags is not None:
        output["tags"] = request.tags

    if request.public is not None:
        output["public"] = request.public

    return output


def marshal_UpdateIpRequest(
    request: UpdateIpRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.reverse is not None:
        output["reverse"] = request.reverse

    if request.type_ is not None:
        output["type"] = request.type_

    if request.tags is not None:
        output["tags"] = request.tags

    if request.server is not None:
        output["server"] = request.server

    return output


def marshal_UpdatePlacementGroupRequest(
    request: UpdatePlacementGroupRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.policy_mode is not None:
        output["policy_mode"] = request.policy_mode

    if request.policy_type is not None:
        output["policy_type"] = request.policy_type

    return output


def marshal_UpdatePlacementGroupServersRequest(
    request: UpdatePlacementGroupServersRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.servers is not None:
        output["servers"] = request.servers

    return output


def marshal_UpdatePrivateNICRequest(
    request: UpdatePrivateNICRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateSecurityGroupRequest(
    request: UpdateSecurityGroupRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.enable_default_security is not None:
        output["enable_default_security"] = request.enable_default_security

    if request.inbound_default_policy is not None:
        output["inbound_default_policy"] = request.inbound_default_policy

    if request.tags is not None:
        output["tags"] = request.tags

    if request.organization_default is not None:
        output["organization_default"] = request.organization_default

    if request.project_default is not None:
        output["project_default"] = request.project_default

    if request.outbound_default_policy is not None:
        output["outbound_default_policy"] = request.outbound_default_policy

    if request.stateful is not None:
        output["stateful"] = request.stateful

    return output


def marshal_UpdateSecurityGroupRuleRequest(
    request: UpdateSecurityGroupRuleRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.protocol is not None:
        output["protocol"] = request.protocol

    if request.direction is not None:
        output["direction"] = request.direction

    if request.action is not None:
        output["action"] = request.action

    if request.ip_range is not None:
        output["ip_range"] = request.ip_range

    if request.dest_port_from is not None:
        output["dest_port_from"] = request.dest_port_from

    if request.dest_port_to is not None:
        output["dest_port_to"] = request.dest_port_to

    if request.position is not None:
        output["position"] = request.position

    return output


def marshal_SecurityGroupTemplate(
    request: SecurityGroupTemplate,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_UpdateServerRequest(
    request: UpdateServerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.boot_type is not None:
        output["boot_type"] = request.boot_type

    if request.tags is not None:
        output["tags"] = request.tags

    if request.volumes is not None:
        output["volumes"] = {
            key: marshal_VolumeServerTemplate(value, defaults)
            for key, value in request.volumes.items()
        }

    if request.dynamic_ip_required is not None:
        output["dynamic_ip_required"] = request.dynamic_ip_required

    if request.routed_ip_enabled is not None:
        output["routed_ip_enabled"] = request.routed_ip_enabled

    if request.public_ips is not None:
        output["public_ips"] = request.public_ips

    if request.enable_ipv6 is not None:
        output["enable_ipv6"] = request.enable_ipv6

    if request.protected is not None:
        output["protected"] = request.protected

    if request.security_group is not None:
        output["security_group"] = marshal_SecurityGroupTemplate(
            request.security_group, defaults
        )

    if request.placement_group is not None:
        output["placement_group"] = request.placement_group

    if request.private_nics is not None:
        output["private_nics"] = request.private_nics

    if request.commercial_type is not None:
        output["commercial_type"] = request.commercial_type

    if request.admin_password_encryption_ssh_key_id is not None:
        output["admin_password_encryption_ssh_key_id"] = (
            request.admin_password_encryption_ssh_key_id
        )

    return output


def marshal_UpdateSnapshotRequest(
    request: UpdateSnapshotRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateVolumeRequest(
    request: UpdateVolumeRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.size is not None:
        output["size"] = request.size

    return output


def marshal__SetSecurityGroupRequest(
    request: _SetSecurityGroupRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.enable_default_security is not None:
        output["enable_default_security"] = request.enable_default_security

    if request.tags is not None:
        output["tags"] = request.tags

    if request.organization_default is not None:
        output["organization_default"] = request.organization_default

    if request.project_default is not None:
        output["project_default"] = request.project_default

    if request.stateful is not None:
        output["stateful"] = request.stateful

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date.isoformat()

    if request.modification_date is not None:
        output["modification_date"] = request.modification_date.isoformat()

    if request.inbound_default_policy is not None:
        output["inbound_default_policy"] = request.inbound_default_policy

    if request.outbound_default_policy is not None:
        output["outbound_default_policy"] = request.outbound_default_policy

    if request.organization is not None:
        output["organization"] = request.organization
    else:
        output["organization"] = defaults.default_organization_id

    if request.project is not None:
        output["project"] = request.project
    else:
        output["project"] = defaults.default_project_id

    if request.servers is not None:
        output["servers"] = [
            marshal_ServerSummary(item, defaults) for item in request.servers
        ]

    return output


def marshal__SetSecurityGroupRuleRequest(
    request: _SetSecurityGroupRuleRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.ip_range is not None:
        output["ip_range"] = request.ip_range

    if request.position is not None:
        output["position"] = request.position

    if request.editable is not None:
        output["editable"] = request.editable

    if request.protocol is not None:
        output["protocol"] = request.protocol

    if request.direction is not None:
        output["direction"] = request.direction

    if request.action is not None:
        output["action"] = request.action

    if request.dest_port_from is not None:
        output["dest_port_from"] = request.dest_port_from

    if request.dest_port_to is not None:
        output["dest_port_to"] = request.dest_port_to

    return output


def marshal_Image(
    request: Image,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.name is not None:
        output["name"] = request.name

    if request.arch is not None:
        output["arch"] = request.arch

    if request.extra_volumes is not None:
        output["extra_volumes"] = {
            key: marshal_Volume(value, defaults)
            for key, value in request.extra_volumes.items()
        }

    if request.from_server is not None:
        output["from_server"] = request.from_server

    if request.organization is not None:
        output["organization"] = request.organization
    else:
        output["organization"] = defaults.default_organization_id

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date.isoformat()

    if request.modification_date is not None:
        output["modification_date"] = request.modification_date.isoformat()

    if request.default_bootscript is not None:
        output["default_bootscript"] = marshal_Bootscript(
            request.default_bootscript, defaults
        )

    if request.public is not None:
        output["public"] = request.public

    if request.state is not None:
        output["state"] = request.state

    if request.project is not None:
        output["project"] = request.project
    else:
        output["project"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.zone is not None:
        output["zone"] = request.zone
    else:
        output["zone"] = defaults.default_zone

    if request.root_volume is not None:
        output["root_volume"] = marshal_VolumeSummary(request.root_volume, defaults)

    return output


def marshal_PlacementGroup(
    request: PlacementGroup,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.name is not None:
        output["name"] = request.name

    if request.organization is not None:
        output["organization"] = request.organization
    else:
        output["organization"] = defaults.default_organization_id

    if request.project is not None:
        output["project"] = request.project
    else:
        output["project"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.policy_mode is not None:
        output["policy_mode"] = request.policy_mode

    if request.policy_type is not None:
        output["policy_type"] = request.policy_type

    if request.policy_respected is not None:
        output["policy_respected"] = request.policy_respected

    if request.zone is not None:
        output["zone"] = request.zone
    else:
        output["zone"] = defaults.default_zone

    return output


def marshal_PrivateNIC(
    request: PrivateNIC,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.server_id is not None:
        output["server_id"] = request.server_id

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    if request.mac_address is not None:
        output["mac_address"] = request.mac_address

    if request.state is not None:
        output["state"] = request.state

    if request.tags is not None:
        output["tags"] = request.tags

    if request.zone is not None:
        output["zone"] = request.zone
    else:
        output["zone"] = defaults.default_zone

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date.isoformat()

    return output


def marshal_SecurityGroupSummary(
    request: SecurityGroupSummary,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_ServerIp(
    request: ServerIp,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.address is not None:
        output["address"] = request.address

    if request.gateway is not None:
        output["gateway"] = request.gateway

    if request.netmask is not None:
        output["netmask"] = request.netmask

    if request.family is not None:
        output["family"] = request.family

    if request.dynamic is not None:
        output["dynamic"] = request.dynamic

    if request.provisioning_mode is not None:
        output["provisioning_mode"] = request.provisioning_mode

    if request.tags is not None:
        output["tags"] = request.tags

    if request.ipam_id is not None:
        output["ipam_id"] = request.ipam_id

    if request.state is not None:
        output["state"] = request.state

    return output


def marshal_ServerIpv6(
    request: ServerIpv6,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.address is not None:
        output["address"] = request.address

    if request.gateway is not None:
        output["gateway"] = request.gateway

    if request.netmask is not None:
        output["netmask"] = request.netmask

    return output


def marshal_ServerLocation(
    request: ServerLocation,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.cluster_id is not None:
        output["cluster_id"] = request.cluster_id

    if request.hypervisor_id is not None:
        output["hypervisor_id"] = request.hypervisor_id

    if request.node_id is not None:
        output["node_id"] = request.node_id

    if request.platform_id is not None:
        output["platform_id"] = request.platform_id

    if request.zone_id is not None:
        output["zone_id"] = request.zone_id

    return output


def marshal_ServerMaintenance(
    request: ServerMaintenance,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.reason is not None:
        output["reason"] = request.reason

    if request.start_date is not None:
        output["start_date"] = request.start_date.isoformat()

    return output


def marshal__SetServerRequest(
    request: _SetServerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.commercial_type is not None:
        output["commercial_type"] = request.commercial_type

    if request.dynamic_ip_required is not None:
        output["dynamic_ip_required"] = request.dynamic_ip_required

    if request.organization is not None:
        output["organization"] = request.organization
    else:
        output["organization"] = defaults.default_organization_id

    if request.enable_ipv6 is not None:
        output["enable_ipv6"] = request.enable_ipv6

    if request.hostname is not None:
        output["hostname"] = request.hostname

    if request.protected is not None:
        output["protected"] = request.protected

    if request.state_detail is not None:
        output["state_detail"] = request.state_detail

    if request.project is not None:
        output["project"] = request.project
    else:
        output["project"] = defaults.default_project_id

    if request.allowed_actions is not None:
        output["allowed_actions"] = [str(item) for item in request.allowed_actions]

    if request.tags is not None:
        output["tags"] = request.tags

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date.isoformat()

    if request.routed_ip_enabled is not None:
        output["routed_ip_enabled"] = request.routed_ip_enabled

    if request.image is not None:
        output["image"] = marshal_Image(request.image, defaults)

    if request.private_ip is not None:
        output["private_ip"] = request.private_ip

    if request.public_ip is not None:
        output["public_ip"] = marshal_ServerIp(request.public_ip, defaults)

    if request.public_ips is not None:
        output["public_ips"] = [
            marshal_ServerIp(item, defaults) for item in request.public_ips
        ]

    if request.modification_date is not None:
        output["modification_date"] = request.modification_date.isoformat()

    if request.state is not None:
        output["state"] = request.state

    if request.location is not None:
        output["location"] = marshal_ServerLocation(request.location, defaults)

    if request.ipv6 is not None:
        output["ipv6"] = marshal_ServerIpv6(request.ipv6, defaults)

    if request.boot_type is not None:
        output["boot_type"] = request.boot_type

    if request.volumes is not None:
        output["volumes"] = {
            key: marshal_Volume(value, defaults)
            for key, value in request.volumes.items()
        }

    if request.security_group is not None:
        output["security_group"] = marshal_SecurityGroupSummary(
            request.security_group, defaults
        )

    if request.maintenances is not None:
        output["maintenances"] = [
            marshal_ServerMaintenance(item, defaults) for item in request.maintenances
        ]

    if request.arch is not None:
        output["arch"] = request.arch

    if request.placement_group is not None:
        output["placement_group"] = marshal_PlacementGroup(
            request.placement_group, defaults
        )

    if request.private_nics is not None:
        output["private_nics"] = [
            marshal_PrivateNIC(item, defaults) for item in request.private_nics
        ]

    if request.admin_password_encryption_ssh_key_id is not None:
        output["admin_password_encryption_ssh_key_id"] = (
            request.admin_password_encryption_ssh_key_id
        )

    return output


def marshal_SnapshotBaseVolume(
    request: SnapshotBaseVolume,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal__SetSnapshotRequest(
    request: _SetSnapshotRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.name is not None:
        output["name"] = request.name

    if request.organization is not None:
        output["organization"] = request.organization
    else:
        output["organization"] = defaults.default_organization_id

    if request.volume_type is not None:
        output["volume_type"] = request.volume_type

    if request.size is not None:
        output["size"] = request.size

    if request.state is not None:
        output["state"] = request.state

    if request.base_volume is not None:
        output["base_volume"] = marshal_SnapshotBaseVolume(
            request.base_volume, defaults
        )

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date.isoformat()

    if request.modification_date is not None:
        output["modification_date"] = request.modification_date.isoformat()

    if request.project is not None:
        output["project"] = request.project
    else:
        output["project"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output
