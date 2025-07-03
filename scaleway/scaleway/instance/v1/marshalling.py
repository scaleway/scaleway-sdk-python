# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from decimal import Decimal
from datetime import datetime
from typing import Any, Dict, List, Optional
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
    unmarshal_Money,
    marshal_Money,
    marshal_ScwFile,
    marshal_ServiceInfo,
    marshal_TimeSeries,
    unmarshal_TimeSeries,
)
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
    AttachServerVolumeRequestVolumeType,
    BootType,
    ImageState,
    IpState,
    IpType,
    ListServersRequestOrder,
    PlacementGroupPolicyMode,
    PlacementGroupPolicyType,
    PrivateNICState,
    SecurityGroupPolicy,
    SecurityGroupRuleAction,
    SecurityGroupRuleDirection,
    SecurityGroupRuleProtocol,
    SecurityGroupState,
    ServerAction,
    ServerFilesystemState,
    ServerIpIpFamily,
    ServerIpProvisioningMode,
    ServerIpState,
    ServerState,
    ServerTypesAvailability,
    SnapshotState,
    SnapshotVolumeType,
    TaskStatus,
    VolumeServerState,
    VolumeServerVolumeType,
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

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("server_id", str())
    args["server_id"] = field

    field = data.get("private_network_id", str())
    args["private_network_id"] = field

    field = data.get("mac_address", str())
    args["mac_address"] = field

    field = data.get("state", getattr(PrivateNICState, "AVAILABLE"))
    args["state"] = field

    field = data.get("tags", [])
    args["tags"] = field

    return PrivateNIC(**args)

def unmarshal_ServerSummary(data: Any) -> ServerSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    return ServerSummary(**args)

def unmarshal_Bootscript(data: Any) -> Bootscript:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Bootscript' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("architecture", str())
    args["architecture"] = field

    field = data.get("bootcmdargs", str())
    args["bootcmdargs"] = field

    field = data.get("default", str())
    args["default"] = field

    field = data.get("dtb", str())
    args["dtb"] = field

    field = data.get("id", str())
    args["id"] = field

    field = data.get("initrd", str())
    args["initrd"] = field

    field = data.get("kernel", str())
    args["kernel"] = field

    field = data.get("organization", str())
    args["organization"] = field

    field = data.get("public", str())
    args["public"] = field

    field = data.get("title", str())
    args["title"] = field

    field = data.get("project", str())
    args["project"] = field

    field = data.get("zone", str())
    args["zone"] = field

    return Bootscript(**args)

def unmarshal_Volume(data: Any) -> Volume:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Volume' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("size", 0)
    args["size"] = field

    field = data.get("volume_type", getattr(VolumeVolumeType, "L_SSD"))
    args["volume_type"] = field

    field = data.get("organization", str())
    args["organization"] = field

    field = data.get("project", str())
    args["project"] = field

    field = data.get("export_uri", None)
    args["export_uri"] = field

    field = data.get("creation_date", None)
    args["creation_date"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("modification_date", None)
    args["modification_date"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("state", getattr(VolumeState, "AVAILABLE"))
    args["state"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("server", None)
    args["server"] = unmarshal_ServerSummary(field) if field is not None else None

    return Volume(**args)

def unmarshal_VolumeSummary(data: Any) -> VolumeSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("size", str())
    args["size"] = field

    field = data.get("volume_type", str())
    args["volume_type"] = field

    return VolumeSummary(**args)

def unmarshal_Image(data: Any) -> Image:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Image' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("arch", str())
    args["arch"] = field

    field = data.get("extra_volumes", str())
    args["extra_volumes"] = {key: unmarshal_Volume(value)for key, value in field.items()
    } if field is not None else None

    field = data.get("from_server", str())
    args["from_server"] = field

    field = data.get("organization", str())
    args["organization"] = field

    field = data.get("creation_date", None)
    args["creation_date"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("modification_date", None)
    args["modification_date"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("default_bootscript", None)
    args["default_bootscript"] = unmarshal_Bootscript(field) if field is not None else None

    field = data.get("public", str())
    args["public"] = field

    field = data.get("state", str())
    args["state"] = field

    field = data.get("project", str())
    args["project"] = field

    field = data.get("tags", str())
    args["tags"] = field

    field = data.get("zone", str())
    args["zone"] = field

    field = data.get("root_volume", None)
    args["root_volume"] = unmarshal_VolumeSummary(field) if field is not None else None

    return Image(**args)

def unmarshal_PlacementGroup(data: Any) -> PlacementGroup:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlacementGroup' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("organization", str())
    args["organization"] = field

    field = data.get("project", str())
    args["project"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("policy_mode", getattr(PlacementGroupPolicyMode, "OPTIONAL"))
    args["policy_mode"] = field

    field = data.get("policy_type", getattr(PlacementGroupPolicyType, "MAX_AVAILABILITY"))
    args["policy_type"] = field

    field = data.get("policy_respected", False)
    args["policy_respected"] = field

    field = data.get("zone", )
    args["zone"] = field

    return PlacementGroup(**args)

def unmarshal_SecurityGroupSummary(data: Any) -> SecurityGroupSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecurityGroupSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    return SecurityGroupSummary(**args)

def unmarshal_ServerFilesystem(data: Any) -> ServerFilesystem:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerFilesystem' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("filesystem_id", str())
    args["filesystem_id"] = field

    field = data.get("state", str())
    args["state"] = field

    return ServerFilesystem(**args)

def unmarshal_ServerIp(data: Any) -> ServerIp:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerIp' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("address", str())
    args["address"] = field

    field = data.get("gateway", str())
    args["gateway"] = field

    field = data.get("netmask", str())
    args["netmask"] = field

    field = data.get("family", getattr(ServerIpIpFamily, "INET"))
    args["family"] = field

    field = data.get("dynamic", False)
    args["dynamic"] = field

    field = data.get("provisioning_mode", getattr(ServerIpProvisioningMode, "MANUAL"))
    args["provisioning_mode"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("ipam_id", str())
    args["ipam_id"] = field

    field = data.get("state", getattr(ServerIpState, "UNKNOWN_STATE"))
    args["state"] = field

    return ServerIp(**args)

def unmarshal_ServerIpv6(data: Any) -> ServerIpv6:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerIpv6' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("address", str())
    args["address"] = field

    field = data.get("gateway", str())
    args["gateway"] = field

    field = data.get("netmask", str())
    args["netmask"] = field

    return ServerIpv6(**args)

def unmarshal_ServerLocation(data: Any) -> ServerLocation:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerLocation' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("cluster_id", str())
    args["cluster_id"] = field

    field = data.get("hypervisor_id", str())
    args["hypervisor_id"] = field

    field = data.get("node_id", str())
    args["node_id"] = field

    field = data.get("platform_id", str())
    args["platform_id"] = field

    field = data.get("zone_id", str())
    args["zone_id"] = field

    return ServerLocation(**args)

def unmarshal_ServerMaintenance(data: Any) -> ServerMaintenance:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerMaintenance' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("reason", str())
    args["reason"] = field

    field = data.get("start_date", None)
    args["start_date"] = parser.isoparse(field) if isinstance(field, str) else field

    return ServerMaintenance(**args)

def unmarshal_VolumeServer(data: Any) -> VolumeServer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeServer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("export_uri", None)
    args["export_uri"] = field

    field = data.get("organization", None)
    args["organization"] = field

    field = data.get("server", None)
    args["server"] = unmarshal_ServerSummary(field) if field is not None else None

    field = data.get("size", None)
    args["size"] = field

    field = data.get("volume_type", str())
    args["volume_type"] = field

    field = data.get("boot", str())
    args["boot"] = field

    field = data.get("zone", str())
    args["zone"] = field

    field = data.get("creation_date", None)
    args["creation_date"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("modification_date", None)
    args["modification_date"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("state", None)
    args["state"] = field

    field = data.get("project", None)
    args["project"] = field

    return VolumeServer(**args)

def unmarshal_Server(data: Any) -> Server:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Server' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("organization", str())
    args["organization"] = field

    field = data.get("project", str())
    args["project"] = field

    field = data.get("allowed_actions", [])
    args["allowed_actions"] = [ServerAction(v) for v in field] if field is not None else None

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("commercial_type", str())
    args["commercial_type"] = field

    field = data.get("creation_date", None)
    args["creation_date"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("dynamic_ip_required", False)
    args["dynamic_ip_required"] = field

    field = data.get("hostname", str())
    args["hostname"] = field

    field = data.get("protected", False)
    args["protected"] = field

    field = data.get("routed_ip_enabled", None)
    args["routed_ip_enabled"] = field

    field = data.get("enable_ipv6", None)
    args["enable_ipv6"] = field

    field = data.get("image", None)
    args["image"] = unmarshal_Image(field) if field is not None else None

    field = data.get("private_ip", None)
    args["private_ip"] = field

    field = data.get("public_ip", None)
    args["public_ip"] = unmarshal_ServerIp(field) if field is not None else None

    field = data.get("public_ips", [])
    args["public_ips"] = [unmarshal_ServerIp(v) for v in field] if field is not None else None

    field = data.get("mac_address", str())
    args["mac_address"] = field

    field = data.get("state", getattr(ServerState, "RUNNING"))
    args["state"] = field

    field = data.get("boot_type", getattr(BootType, "LOCAL"))
    args["boot_type"] = field

    field = data.get("volumes", {})
    args["volumes"] = {key: unmarshal_VolumeServer(value)for key, value in field.items()
    } if field is not None else None

    field = data.get("maintenances", [])
    args["maintenances"] = [unmarshal_ServerMaintenance(v) for v in field] if field is not None else None

    field = data.get("state_detail", str())
    args["state_detail"] = field

    field = data.get("arch", getattr(Arch, "UNKNOWN_ARCH"))
    args["arch"] = field

    field = data.get("modification_date", None)
    args["modification_date"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("location", None)
    args["location"] = unmarshal_ServerLocation(field) if field is not None else None

    field = data.get("ipv6", None)
    args["ipv6"] = unmarshal_ServerIpv6(field) if field is not None else None

    field = data.get("security_group", None)
    args["security_group"] = unmarshal_SecurityGroupSummary(field) if field is not None else None

    field = data.get("placement_group", None)
    args["placement_group"] = unmarshal_PlacementGroup(field) if field is not None else None

    field = data.get("private_nics", [])
    args["private_nics"] = [unmarshal_PrivateNIC(v) for v in field] if field is not None else None

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("filesystems", [])
    args["filesystems"] = [unmarshal_ServerFilesystem(v) for v in field] if field is not None else None

    field = data.get("end_of_service", False)
    args["end_of_service"] = field

    field = data.get("admin_password_encryption_ssh_key_id", None)
    args["admin_password_encryption_ssh_key_id"] = field

    field = data.get("admin_password_encrypted_value", None)
    args["admin_password_encrypted_value"] = field

    return Server(**args)

def unmarshal_AttachServerFileSystemResponse(data: Any) -> AttachServerFileSystemResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AttachServerFileSystemResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server", None)
    args["server"] = unmarshal_Server(field) if field is not None else None

    return AttachServerFileSystemResponse(**args)

def unmarshal_AttachServerVolumeResponse(data: Any) -> AttachServerVolumeResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AttachServerVolumeResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server", None)
    args["server"] = unmarshal_Server(field) if field is not None else None

    return AttachServerVolumeResponse(**args)

def unmarshal_CreateImageResponse(data: Any) -> CreateImageResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateImageResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("image", None)
    args["image"] = unmarshal_Image(field) if field is not None else None

    return CreateImageResponse(**args)

def unmarshal_Ip(data: Any) -> Ip:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Ip' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("address", str())
    args["address"] = field

    field = data.get("organization", str())
    args["organization"] = field

    field = data.get("tags", str())
    args["tags"] = field

    field = data.get("project", str())
    args["project"] = field

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("state", str())
    args["state"] = field

    field = data.get("prefix", str())
    args["prefix"] = field

    field = data.get("ipam_id", str())
    args["ipam_id"] = field

    field = data.get("zone", str())
    args["zone"] = field

    field = data.get("reverse", None)
    args["reverse"] = field

    field = data.get("server", None)
    args["server"] = unmarshal_ServerSummary(field) if field is not None else None

    return Ip(**args)

def unmarshal_CreateIpResponse(data: Any) -> CreateIpResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateIpResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip", None)
    args["ip"] = unmarshal_Ip(field) if field is not None else None

    return CreateIpResponse(**args)

def unmarshal_CreatePlacementGroupResponse(data: Any) -> CreatePlacementGroupResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreatePlacementGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("placement_group", None)
    args["placement_group"] = unmarshal_PlacementGroup(field) if field is not None else None

    return CreatePlacementGroupResponse(**args)

def unmarshal_CreatePrivateNICResponse(data: Any) -> CreatePrivateNICResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreatePrivateNICResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_nic", None)
    args["private_nic"] = unmarshal_PrivateNIC(field) if field is not None else None

    return CreatePrivateNICResponse(**args)

def unmarshal_SecurityGroup(data: Any) -> SecurityGroup:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecurityGroup' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("enable_default_security", False)
    args["enable_default_security"] = field

    field = data.get("inbound_default_policy", getattr(SecurityGroupPolicy, "UNKNOWN_POLICY"))
    args["inbound_default_policy"] = field

    field = data.get("outbound_default_policy", getattr(SecurityGroupPolicy, "UNKNOWN_POLICY"))
    args["outbound_default_policy"] = field

    field = data.get("organization", str())
    args["organization"] = field

    field = data.get("project", str())
    args["project"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("project_default", False)
    args["project_default"] = field

    field = data.get("servers", [])
    args["servers"] = [unmarshal_ServerSummary(v) for v in field] if field is not None else None

    field = data.get("stateful", False)
    args["stateful"] = field

    field = data.get("state", getattr(SecurityGroupState, "AVAILABLE"))
    args["state"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("organization_default", None)
    args["organization_default"] = field

    field = data.get("creation_date", None)
    args["creation_date"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("modification_date", None)
    args["modification_date"] = parser.isoparse(field) if isinstance(field, str) else field

    return SecurityGroup(**args)

def unmarshal_CreateSecurityGroupResponse(data: Any) -> CreateSecurityGroupResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateSecurityGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("security_group", None)
    args["security_group"] = unmarshal_SecurityGroup(field) if field is not None else None

    return CreateSecurityGroupResponse(**args)

def unmarshal_SecurityGroupRule(data: Any) -> SecurityGroupRule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecurityGroupRule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("protocol", str())
    args["protocol"] = field

    field = data.get("direction", str())
    args["direction"] = field

    field = data.get("action", str())
    args["action"] = field

    field = data.get("ip_range", str())
    args["ip_range"] = field

    field = data.get("position", str())
    args["position"] = field

    field = data.get("editable", str())
    args["editable"] = field

    field = data.get("zone", str())
    args["zone"] = field

    field = data.get("dest_port_from", None)
    args["dest_port_from"] = field

    field = data.get("dest_port_to", None)
    args["dest_port_to"] = field

    return SecurityGroupRule(**args)

def unmarshal_CreateSecurityGroupRuleResponse(data: Any) -> CreateSecurityGroupRuleResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateSecurityGroupRuleResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rule", None)
    args["rule"] = unmarshal_SecurityGroupRule(field) if field is not None else None

    return CreateSecurityGroupRuleResponse(**args)

def unmarshal_CreateServerResponse(data: Any) -> CreateServerResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateServerResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server", None)
    args["server"] = unmarshal_Server(field) if field is not None else None

    return CreateServerResponse(**args)

def unmarshal_SnapshotBaseVolume(data: Any) -> SnapshotBaseVolume:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SnapshotBaseVolume' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    return SnapshotBaseVolume(**args)

def unmarshal_Snapshot(data: Any) -> Snapshot:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Snapshot' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("organization", str())
    args["organization"] = field

    field = data.get("project", str())
    args["project"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("volume_type", getattr(VolumeVolumeType, "L_SSD"))
    args["volume_type"] = field

    field = data.get("size", 0)
    args["size"] = field

    field = data.get("state", getattr(SnapshotState, "AVAILABLE"))
    args["state"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("base_volume", None)
    args["base_volume"] = unmarshal_SnapshotBaseVolume(field) if field is not None else None

    field = data.get("creation_date", None)
    args["creation_date"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("modification_date", None)
    args["modification_date"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("error_reason", None)
    args["error_reason"] = field

    return Snapshot(**args)

def unmarshal_Task(data: Any) -> Task:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Task' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("progress", 0)
    args["progress"] = field

    field = data.get("status", getattr(TaskStatus, "PENDING"))
    args["status"] = field

    field = data.get("href_from", str())
    args["href_from"] = field

    field = data.get("href_result", str())
    args["href_result"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("started_at", None)
    args["started_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("terminated_at", None)
    args["terminated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Task(**args)

def unmarshal_CreateSnapshotResponse(data: Any) -> CreateSnapshotResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateSnapshotResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshot", None)
    args["snapshot"] = unmarshal_Snapshot(field) if field is not None else None

    field = data.get("task", None)
    args["task"] = unmarshal_Task(field) if field is not None else None

    return CreateSnapshotResponse(**args)

def unmarshal_CreateVolumeResponse(data: Any) -> CreateVolumeResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateVolumeResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("volume", None)
    args["volume"] = unmarshal_Volume(field) if field is not None else None

    return CreateVolumeResponse(**args)

def unmarshal_DetachServerFileSystemResponse(data: Any) -> DetachServerFileSystemResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DetachServerFileSystemResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server", None)
    args["server"] = unmarshal_Server(field) if field is not None else None

    return DetachServerFileSystemResponse(**args)

def unmarshal_DetachServerVolumeResponse(data: Any) -> DetachServerVolumeResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DetachServerVolumeResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server", None)
    args["server"] = unmarshal_Server(field) if field is not None else None

    return DetachServerVolumeResponse(**args)

def unmarshal_ExportSnapshotResponse(data: Any) -> ExportSnapshotResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ExportSnapshotResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("task", None)
    args["task"] = unmarshal_Task(field) if field is not None else None

    return ExportSnapshotResponse(**args)

def unmarshal_Dashboard(data: Any) -> Dashboard:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Dashboard' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("volumes_count", str())
    args["volumes_count"] = field

    field = data.get("running_servers_count", str())
    args["running_servers_count"] = field

    field = data.get("servers_by_types", str())
    args["servers_by_types"] = field

    field = data.get("images_count", str())
    args["images_count"] = field

    field = data.get("snapshots_count", str())
    args["snapshots_count"] = field

    field = data.get("servers_count", str())
    args["servers_count"] = field

    field = data.get("ips_count", str())
    args["ips_count"] = field

    field = data.get("security_groups_count", str())
    args["security_groups_count"] = field

    field = data.get("ips_unused", str())
    args["ips_unused"] = field

    field = data.get("volumes_l_ssd_count", str())
    args["volumes_l_ssd_count"] = field

    field = data.get("volumes_l_ssd_total_size", str())
    args["volumes_l_ssd_total_size"] = field

    field = data.get("private_nics_count", str())
    args["private_nics_count"] = field

    field = data.get("placement_groups_count", str())
    args["placement_groups_count"] = field

    field = data.get("volumes_b_ssd_count", None)
    args["volumes_b_ssd_count"] = field

    field = data.get("volumes_b_ssd_total_size", None)
    args["volumes_b_ssd_total_size"] = field

    return Dashboard(**args)

def unmarshal_GetDashboardResponse(data: Any) -> GetDashboardResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetDashboardResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dashboard", None)
    args["dashboard"] = unmarshal_Dashboard(field) if field is not None else None

    return GetDashboardResponse(**args)

def unmarshal_GetImageResponse(data: Any) -> GetImageResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetImageResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("image", None)
    args["image"] = unmarshal_Image(field) if field is not None else None

    return GetImageResponse(**args)

def unmarshal_GetIpResponse(data: Any) -> GetIpResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetIpResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip", None)
    args["ip"] = unmarshal_Ip(field) if field is not None else None

    return GetIpResponse(**args)

def unmarshal_GetPlacementGroupResponse(data: Any) -> GetPlacementGroupResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetPlacementGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("placement_group", None)
    args["placement_group"] = unmarshal_PlacementGroup(field) if field is not None else None

    return GetPlacementGroupResponse(**args)

def unmarshal_PlacementGroupServer(data: Any) -> PlacementGroupServer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlacementGroupServer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("policy_respected", False)
    args["policy_respected"] = field

    return PlacementGroupServer(**args)

def unmarshal_GetPlacementGroupServersResponse(data: Any) -> GetPlacementGroupServersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetPlacementGroupServersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("servers", [])
    args["servers"] = [unmarshal_PlacementGroupServer(v) for v in field] if field is not None else None

    return GetPlacementGroupServersResponse(**args)

def unmarshal_GetPrivateNICResponse(data: Any) -> GetPrivateNICResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetPrivateNICResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_nic", None)
    args["private_nic"] = unmarshal_PrivateNIC(field) if field is not None else None

    return GetPrivateNICResponse(**args)

def unmarshal_GetSecurityGroupResponse(data: Any) -> GetSecurityGroupResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetSecurityGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("security_group", None)
    args["security_group"] = unmarshal_SecurityGroup(field) if field is not None else None

    return GetSecurityGroupResponse(**args)

def unmarshal_GetSecurityGroupRuleResponse(data: Any) -> GetSecurityGroupRuleResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetSecurityGroupRuleResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rule", None)
    args["rule"] = unmarshal_SecurityGroupRule(field) if field is not None else None

    return GetSecurityGroupRuleResponse(**args)

def unmarshal_GetServerResponse(data: Any) -> GetServerResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetServerResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server", None)
    args["server"] = unmarshal_Server(field) if field is not None else None

    return GetServerResponse(**args)

def unmarshal_GetServerTypesAvailabilityResponseAvailability(data: Any) -> GetServerTypesAvailabilityResponseAvailability:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetServerTypesAvailabilityResponseAvailability' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("availability", str())
    args["availability"] = field

    return GetServerTypesAvailabilityResponseAvailability(**args)

def unmarshal_GetServerTypesAvailabilityResponse(data: Any) -> GetServerTypesAvailabilityResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetServerTypesAvailabilityResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("servers", {})
    args["servers"] = {key: unmarshal_GetServerTypesAvailabilityResponseAvailability(value)for key, value in field.items()
    } if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return GetServerTypesAvailabilityResponse(**args)

def unmarshal_GetSnapshotResponse(data: Any) -> GetSnapshotResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetSnapshotResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshot", None)
    args["snapshot"] = unmarshal_Snapshot(field) if field is not None else None

    return GetSnapshotResponse(**args)

def unmarshal_GetVolumeResponse(data: Any) -> GetVolumeResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetVolumeResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("volume", None)
    args["volume"] = unmarshal_Volume(field) if field is not None else None

    return GetVolumeResponse(**args)

def unmarshal_ListImagesResponse(data: Any) -> ListImagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListImagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("images", [])
    args["images"] = [unmarshal_Image(v) for v in field] if field is not None else None

    return ListImagesResponse(**args)

def unmarshal_ListIpsResponse(data: Any) -> ListIpsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListIpsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("ips", [])
    args["ips"] = [unmarshal_Ip(v) for v in field] if field is not None else None

    return ListIpsResponse(**args)

def unmarshal_ListPlacementGroupsResponse(data: Any) -> ListPlacementGroupsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPlacementGroupsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("placement_groups", [])
    args["placement_groups"] = [unmarshal_PlacementGroup(v) for v in field] if field is not None else None

    return ListPlacementGroupsResponse(**args)

def unmarshal_ListPrivateNICsResponse(data: Any) -> ListPrivateNICsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPrivateNICsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_nics", str())
    args["private_nics"] = [unmarshal_PrivateNIC(v) for v in field] if field is not None else None

    field = data.get("total_count", str())
    args["total_count"] = field

    return ListPrivateNICsResponse(**args)

def unmarshal_ListSecurityGroupRulesResponse(data: Any) -> ListSecurityGroupRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSecurityGroupRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("rules", [])
    args["rules"] = [unmarshal_SecurityGroupRule(v) for v in field] if field is not None else None

    return ListSecurityGroupRulesResponse(**args)

def unmarshal_ListSecurityGroupsResponse(data: Any) -> ListSecurityGroupsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSecurityGroupsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("security_groups", [])
    args["security_groups"] = [unmarshal_SecurityGroup(v) for v in field] if field is not None else None

    return ListSecurityGroupsResponse(**args)

def unmarshal_ListServerActionsResponse(data: Any) -> ListServerActionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServerActionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("actions", str())
    args["actions"] = [ServerAction(v) for v in field] if field is not None else None

    return ListServerActionsResponse(**args)

def unmarshal_ListServerUserDataResponse(data: Any) -> ListServerUserDataResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServerUserDataResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("user_data", str())
    args["user_data"] = field

    return ListServerUserDataResponse(**args)

def unmarshal_ListServersResponse(data: Any) -> ListServersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("servers", [])
    args["servers"] = [unmarshal_Server(v) for v in field] if field is not None else None

    return ListServersResponse(**args)

def unmarshal_ServerTypeNetworkInterface(data: Any) -> ServerTypeNetworkInterface:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeNetworkInterface' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("internal_bandwidth", None)
    args["internal_bandwidth"] = field

    field = data.get("internet_bandwidth", None)
    args["internet_bandwidth"] = field

    return ServerTypeNetworkInterface(**args)

def unmarshal_ServerTypeVolumeConstraintSizes(data: Any) -> ServerTypeVolumeConstraintSizes:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeVolumeConstraintSizes' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("min_size", 0)
    args["min_size"] = field

    field = data.get("max_size", 0)
    args["max_size"] = field

    return ServerTypeVolumeConstraintSizes(**args)

def unmarshal_ServerTypeCapabilities(data: Any) -> ServerTypeCapabilities:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeCapabilities' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("boot_types", [])
    args["boot_types"] = [BootType(v) for v in field] if field is not None else None

    field = data.get("max_file_systems", 0)
    args["max_file_systems"] = field

    field = data.get("block_storage", None)
    args["block_storage"] = field

    return ServerTypeCapabilities(**args)

def unmarshal_ServerTypeGPUInfo(data: Any) -> ServerTypeGPUInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeGPUInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("gpu_manufacturer", str())
    args["gpu_manufacturer"] = field

    field = data.get("gpu_name", str())
    args["gpu_name"] = field

    field = data.get("gpu_memory", 0)
    args["gpu_memory"] = field

    return ServerTypeGPUInfo(**args)

def unmarshal_ServerTypeNetwork(data: Any) -> ServerTypeNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("interfaces", [])
    args["interfaces"] = [unmarshal_ServerTypeNetworkInterface(v) for v in field] if field is not None else None

    field = data.get("ipv6_support", False)
    args["ipv6_support"] = field

    field = data.get("sum_internal_bandwidth", None)
    args["sum_internal_bandwidth"] = field

    field = data.get("sum_internet_bandwidth", None)
    args["sum_internet_bandwidth"] = field

    return ServerTypeNetwork(**args)

def unmarshal_ServerTypeVolumeConstraintsByType(data: Any) -> ServerTypeVolumeConstraintsByType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeVolumeConstraintsByType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("l_ssd", None)
    args["l_ssd"] = unmarshal_ServerTypeVolumeConstraintSizes(field) if field is not None else None

    return ServerTypeVolumeConstraintsByType(**args)

def unmarshal_ServerType(data: Any) -> ServerType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("monthly_price", None)
    args["monthly_price"] = field

    field = data.get("hourly_price", 0.0)
    args["hourly_price"] = field

    field = data.get("alt_names", [])
    args["alt_names"] = field

    field = data.get("ncpus", 0)
    args["ncpus"] = field

    field = data.get("ram", 0)
    args["ram"] = field

    field = data.get("arch", getattr(Arch, "UNKNOWN_ARCH"))
    args["arch"] = field

    field = data.get("end_of_service", False)
    args["end_of_service"] = field

    field = data.get("per_volume_constraint", None)
    args["per_volume_constraint"] = unmarshal_ServerTypeVolumeConstraintsByType(field) if field is not None else None

    field = data.get("volumes_constraint", None)
    args["volumes_constraint"] = unmarshal_ServerTypeVolumeConstraintSizes(field) if field is not None else None

    field = data.get("gpu", None)
    args["gpu"] = field

    field = data.get("gpu_info", None)
    args["gpu_info"] = unmarshal_ServerTypeGPUInfo(field) if field is not None else None

    field = data.get("network", None)
    args["network"] = unmarshal_ServerTypeNetwork(field) if field is not None else None

    field = data.get("capabilities", None)
    args["capabilities"] = unmarshal_ServerTypeCapabilities(field) if field is not None else None

    field = data.get("scratch_storage_max_size", None)
    args["scratch_storage_max_size"] = field

    field = data.get("block_bandwidth", None)
    args["block_bandwidth"] = field

    return ServerType(**args)

def unmarshal_ListServersTypesResponse(data: Any) -> ListServersTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServersTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("servers", {})
    args["servers"] = {key: unmarshal_ServerType(value)for key, value in field.items()
    } if field is not None else None

    return ListServersTypesResponse(**args)

def unmarshal_ListSnapshotsResponse(data: Any) -> ListSnapshotsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSnapshotsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("snapshots", [])
    args["snapshots"] = [unmarshal_Snapshot(v) for v in field] if field is not None else None

    return ListSnapshotsResponse(**args)

def unmarshal_ListVolumesResponse(data: Any) -> ListVolumesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVolumesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("volumes", [])
    args["volumes"] = [unmarshal_Volume(v) for v in field] if field is not None else None

    return ListVolumesResponse(**args)

def unmarshal_VolumeTypeCapabilities(data: Any) -> VolumeTypeCapabilities:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeTypeCapabilities' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshot", str())
    args["snapshot"] = field

    return VolumeTypeCapabilities(**args)

def unmarshal_VolumeTypeConstraints(data: Any) -> VolumeTypeConstraints:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeTypeConstraints' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("min", str())
    args["min"] = field

    field = data.get("max", str())
    args["max"] = field

    return VolumeTypeConstraints(**args)

def unmarshal_VolumeType(data: Any) -> VolumeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("display_name", str())
    args["display_name"] = field

    field = data.get("capabilities", None)
    args["capabilities"] = unmarshal_VolumeTypeCapabilities(field) if field is not None else None

    field = data.get("constraints", None)
    args["constraints"] = unmarshal_VolumeTypeConstraints(field) if field is not None else None

    return VolumeType(**args)

def unmarshal_ListVolumesTypesResponse(data: Any) -> ListVolumesTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVolumesTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("volumes", {})
    args["volumes"] = {key: unmarshal_VolumeType(value)for key, value in field.items()
    } if field is not None else None

    return ListVolumesTypesResponse(**args)

def unmarshal_MigrationPlan(data: Any) -> MigrationPlan:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'MigrationPlan' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshots", [])
    args["snapshots"] = [unmarshal_Snapshot(v) for v in field] if field is not None else None

    field = data.get("validation_key", str())
    args["validation_key"] = field

    field = data.get("volume", None)
    args["volume"] = unmarshal_Volume(field) if field is not None else None

    return MigrationPlan(**args)

def unmarshal_ServerActionResponse(data: Any) -> ServerActionResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerActionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("task", None)
    args["task"] = unmarshal_Task(field) if field is not None else None

    return ServerActionResponse(**args)

def unmarshal_ServerCompatibleTypes(data: Any) -> ServerCompatibleTypes:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerCompatibleTypes' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("compatible_types", [])
    args["compatible_types"] = field

    return ServerCompatibleTypes(**args)

def unmarshal_SetPlacementGroupResponse(data: Any) -> SetPlacementGroupResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetPlacementGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("placement_group", None)
    args["placement_group"] = unmarshal_PlacementGroup(field) if field is not None else None

    return SetPlacementGroupResponse(**args)

def unmarshal_SetPlacementGroupServersResponse(data: Any) -> SetPlacementGroupServersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetPlacementGroupServersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("servers", [])
    args["servers"] = [unmarshal_PlacementGroupServer(v) for v in field] if field is not None else None

    return SetPlacementGroupServersResponse(**args)

def unmarshal_SetSecurityGroupRulesResponse(data: Any) -> SetSecurityGroupRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetSecurityGroupRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", str())
    args["rules"] = [unmarshal_SecurityGroupRule(v) for v in field] if field is not None else None

    return SetSecurityGroupRulesResponse(**args)

def unmarshal_UpdateImageResponse(data: Any) -> UpdateImageResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateImageResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("image", None)
    args["image"] = unmarshal_Image(field) if field is not None else None

    return UpdateImageResponse(**args)

def unmarshal_UpdateIpResponse(data: Any) -> UpdateIpResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateIpResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip", None)
    args["ip"] = unmarshal_Ip(field) if field is not None else None

    return UpdateIpResponse(**args)

def unmarshal_UpdatePlacementGroupResponse(data: Any) -> UpdatePlacementGroupResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdatePlacementGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("placement_group", None)
    args["placement_group"] = unmarshal_PlacementGroup(field) if field is not None else None

    return UpdatePlacementGroupResponse(**args)

def unmarshal_UpdatePlacementGroupServersResponse(data: Any) -> UpdatePlacementGroupServersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdatePlacementGroupServersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("servers", [])
    args["servers"] = [unmarshal_PlacementGroupServer(v) for v in field] if field is not None else None

    return UpdatePlacementGroupServersResponse(**args)

def unmarshal_UpdateSecurityGroupResponse(data: Any) -> UpdateSecurityGroupResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateSecurityGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("security_group", None)
    args["security_group"] = unmarshal_SecurityGroup(field) if field is not None else None

    return UpdateSecurityGroupResponse(**args)

def unmarshal_UpdateSecurityGroupRuleResponse(data: Any) -> UpdateSecurityGroupRuleResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateSecurityGroupRuleResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rule", None)
    args["rule"] = unmarshal_SecurityGroupRule(field) if field is not None else None

    return UpdateSecurityGroupRuleResponse(**args)

def unmarshal_UpdateServerResponse(data: Any) -> UpdateServerResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateServerResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server", None)
    args["server"] = unmarshal_Server(field) if field is not None else None

    return UpdateServerResponse(**args)

def unmarshal_UpdateSnapshotResponse(data: Any) -> UpdateSnapshotResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateSnapshotResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshot", None)
    args["snapshot"] = unmarshal_Snapshot(field) if field is not None else None

    return UpdateSnapshotResponse(**args)

def unmarshal_UpdateVolumeResponse(data: Any) -> UpdateVolumeResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateVolumeResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("volume", None)
    args["volume"] = unmarshal_Volume(field) if field is not None else None

    return UpdateVolumeResponse(**args)

def unmarshal__SetImageResponse(data: Any) -> _SetImageResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type '_SetImageResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("image", None)
    args["image"] = unmarshal_Image(field) if field is not None else None

    return _SetImageResponse(**args)

def unmarshal__SetSecurityGroupResponse(data: Any) -> _SetSecurityGroupResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type '_SetSecurityGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("security_group", None)
    args["security_group"] = unmarshal_SecurityGroup(field) if field is not None else None

    return _SetSecurityGroupResponse(**args)

def unmarshal__SetSecurityGroupRuleResponse(data: Any) -> _SetSecurityGroupRuleResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type '_SetSecurityGroupRuleResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rule", None)
    args["rule"] = unmarshal_SecurityGroupRule(field) if field is not None else None

    return _SetSecurityGroupRuleResponse(**args)

def unmarshal__SetServerResponse(data: Any) -> _SetServerResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type '_SetServerResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server", None)
    args["server"] = unmarshal_Server(field) if field is not None else None

    return _SetServerResponse(**args)

def unmarshal__SetSnapshotResponse(data: Any) -> _SetSnapshotResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type '_SetSnapshotResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshot", None)
    args["snapshot"] = unmarshal_Snapshot(field) if field is not None else None

    return _SetSnapshotResponse(**args)

def marshal_ApplyBlockMigrationRequest(
    request: ApplyBlockMigrationRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="volume_id", value=request.volume_id,marshal_func=None
            ),
            OneOfPossibility(param="snapshot_id", value=request.snapshot_id,marshal_func=None
            ),
        ]),
    )

    if request.validation_key is not None:
        output["validation_key"] = request.validation_key
    else:
        output["validation_key"] = str()


    return output

def marshal_AttachServerFileSystemRequest(
    request: AttachServerFileSystemRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.filesystem_id is not None:
        output["filesystem_id"] = request.filesystem_id
    else:
        output["filesystem_id"] = str()


    return output

def marshal_AttachServerVolumeRequest(
    request: AttachServerVolumeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.volume_id is not None:
        output["volume_id"] = request.volume_id
    else:
        output["volume_id"] = str()

    if request.volume_type is not None:
        output["volume_type"] = str(request.volume_type)
    else:
        output["volume_type"] = None

    if request.boot is not None:
        output["boot"] = request.boot
    else:
        output["boot"] = None


    return output

def marshal_CheckBlockMigrationOrganizationQuotasRequest(
    request: CheckBlockMigrationOrganizationQuotasRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.organization is not None:
        output["organization"] = request.organization or defaults.default_organization_id
    else:
        output["organization"] = None


    return output

def marshal_VolumeTemplate(
    request: VolumeTemplate,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="project", value=request.project,default=defaults.default_project_id,marshal_func=None
            ),
            OneOfPossibility(param="organization", value=request.organization,default=defaults.default_organization_id,marshal_func=None
            ),
        ]),
    )

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = 0

    if request.volume_type is not None:
        output["volume_type"] = str(request.volume_type)
    else:
        output["volume_type"] = getattr(VolumeVolumeType, "L_SSD")


    return output

def marshal_CreateImageRequest(
    request: CreateImageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="project", value=request.project,default=defaults.default_project_id,marshal_func=None
            ),
            OneOfPossibility(param="organization", value=request.organization,default=defaults.default_organization_id,marshal_func=None
            ),
        ]),
    )

    if request.root_volume is not None:
        output["root_volume"] = request.root_volume
    else:
        output["root_volume"] = str()

    if request.arch is not None:
        output["arch"] = str(request.arch)
    else:
        output["arch"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.extra_volumes is not None:
        output["extra_volumes"] = {
            key: marshal_VolumeTemplate(value, defaults)
            for key, value in request.extra_volumes.items()
        }
    else:
        output["extra_volumes"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.public is not None:
        output["public"] = request.public
    else:
        output["public"] = None


    return output

def marshal_CreateIpRequest(
    request: CreateIpRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="project", value=request.project,default=defaults.default_project_id,marshal_func=None
            ),
            OneOfPossibility(param="organization", value=request.organization,default=defaults.default_organization_id,marshal_func=None
            ),
        ]),
    )

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.server is not None:
        output["server"] = request.server
    else:
        output["server"] = None

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = None


    return output

def marshal_CreatePlacementGroupRequest(
    request: CreatePlacementGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="project", value=request.project,default=defaults.default_project_id,marshal_func=None
            ),
            OneOfPossibility(param="organization", value=request.organization,default=defaults.default_organization_id,marshal_func=None
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.policy_mode is not None:
        output["policy_mode"] = str(request.policy_mode)
    else:
        output["policy_mode"] = None

    if request.policy_type is not None:
        output["policy_type"] = str(request.policy_type)
    else:
        output["policy_type"] = None


    return output

def marshal_CreatePrivateNICRequest(
    request: CreatePrivateNICRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id
    else:
        output["private_network_id"] = str()

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.ip_ids is not None:
        output["ip_ids"] = request.ip_ids
    else:
        output["ip_ids"] = None

    if request.ipam_ip_ids is not None:
        output["ipam_ip_ids"] = request.ipam_ip_ids
    else:
        output["ipam_ip_ids"] = None


    return output

def marshal_CreateSecurityGroupRequest(
    request: CreateSecurityGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="project", value=request.project,default=defaults.default_project_id,marshal_func=None
            ),
            OneOfPossibility(param="organization", value=request.organization,default=defaults.default_organization_id,marshal_func=None
            ),
        ]),
    )
    output.update(
        resolve_one_of([
            OneOfPossibility(param="organization_default", value=request.organization_default,marshal_func=None
            ),
            OneOfPossibility(param="project_default", value=request.project_default,marshal_func=None
            ),
        ]),
    )

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.stateful is not None:
        output["stateful"] = request.stateful
    else:
        output["stateful"] = False

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.inbound_default_policy is not None:
        output["inbound_default_policy"] = str(request.inbound_default_policy)
    else:
        output["inbound_default_policy"] = None

    if request.outbound_default_policy is not None:
        output["outbound_default_policy"] = str(request.outbound_default_policy)
    else:
        output["outbound_default_policy"] = None

    if request.enable_default_security is not None:
        output["enable_default_security"] = request.enable_default_security
    else:
        output["enable_default_security"] = None


    return output

def marshal_CreateSecurityGroupRuleRequest(
    request: CreateSecurityGroupRuleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.protocol is not None:
        output["protocol"] = str(request.protocol)
    else:
        output["protocol"] = str()

    if request.direction is not None:
        output["direction"] = str(request.direction)
    else:
        output["direction"] = str()

    if request.action is not None:
        output["action"] = str(request.action)
    else:
        output["action"] = str()

    if request.ip_range is not None:
        output["ip_range"] = request.ip_range
    else:
        output["ip_range"] = str()

    if request.position is not None:
        output["position"] = request.position
    else:
        output["position"] = 0

    if request.editable is not None:
        output["editable"] = request.editable
    else:
        output["editable"] = False

    if request.dest_port_from is not None:
        output["dest_port_from"] = request.dest_port_from
    else:
        output["dest_port_from"] = None

    if request.dest_port_to is not None:
        output["dest_port_to"] = request.dest_port_to
    else:
        output["dest_port_to"] = None


    return output

def marshal_VolumeServerTemplate(
    request: VolumeServerTemplate,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.volume_type is not None:
        output["volume_type"] = str(request.volume_type)
    else:
        output["volume_type"] = getattr(VolumeVolumeType, "L_SSD")

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = None

    if request.boot is not None:
        output["boot"] = request.boot
    else:
        output["boot"] = None

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = None

    if request.base_snapshot is not None:
        output["base_snapshot"] = request.base_snapshot
    else:
        output["base_snapshot"] = None

    if request.organization is not None:
        output["organization"] = request.organization
    else:
        output["organization"] = None

    if request.project is not None:
        output["project"] = request.project
    else:
        output["project"] = None


    return output

def marshal_CreateServerRequest(
    request: CreateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="project", value=request.project,default=defaults.default_project_id,marshal_func=None
            ),
            OneOfPossibility(param="organization", value=request.organization,default=defaults.default_organization_id,marshal_func=None
            ),
        ]),
    )

    if request.commercial_type is not None:
        output["commercial_type"] = request.commercial_type
    else:
        output["commercial_type"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.dynamic_ip_required is not None:
        output["dynamic_ip_required"] = request.dynamic_ip_required
    else:
        output["dynamic_ip_required"] = None

    if request.routed_ip_enabled is not None:
        output["routed_ip_enabled"] = request.routed_ip_enabled
    else:
        output["routed_ip_enabled"] = None

    if request.image is not None:
        output["image"] = request.image
    else:
        output["image"] = None

    if request.volumes is not None:
        output["volumes"] = {
            key: marshal_VolumeServerTemplate(value, defaults)
            for key, value in request.volumes.items()
        }
    else:
        output["volumes"] = None

    if request.enable_ipv6 is not None:
        output["enable_ipv6"] = request.enable_ipv6
    else:
        output["enable_ipv6"] = None

    if request.protected is not None:
        output["protected"] = request.protected
    else:
        output["protected"] = False

    if request.public_ip is not None:
        output["public_ip"] = request.public_ip
    else:
        output["public_ip"] = None

    if request.public_ips is not None:
        output["public_ips"] = request.public_ips
    else:
        output["public_ips"] = None

    if request.boot_type is not None:
        output["boot_type"] = str(request.boot_type)
    else:
        output["boot_type"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.security_group is not None:
        output["security_group"] = request.security_group
    else:
        output["security_group"] = None

    if request.placement_group is not None:
        output["placement_group"] = request.placement_group
    else:
        output["placement_group"] = None

    if request.admin_password_encryption_ssh_key_id is not None:
        output["admin_password_encryption_ssh_key_id"] = request.admin_password_encryption_ssh_key_id
    else:
        output["admin_password_encryption_ssh_key_id"] = None


    return output

def marshal_CreateSnapshotRequest(
    request: CreateSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="project", value=request.project,default=defaults.default_project_id,marshal_func=None
            ),
            OneOfPossibility(param="organization", value=request.organization,default=defaults.default_organization_id,marshal_func=None
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.volume_id is not None:
        output["volume_id"] = request.volume_id
    else:
        output["volume_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.volume_type is not None:
        output["volume_type"] = str(request.volume_type)
    else:
        output["volume_type"] = None

    if request.bucket is not None:
        output["bucket"] = request.bucket
    else:
        output["bucket"] = None

    if request.key is not None:
        output["key"] = request.key
    else:
        output["key"] = None

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = None


    return output

def marshal_CreateVolumeRequest(
    request: CreateVolumeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="project", value=request.project,default=defaults.default_project_id,marshal_func=None
            ),
            OneOfPossibility(param="organization", value=request.organization,default=defaults.default_organization_id,marshal_func=None
            ),
        ]),
    )
    output.update(
        resolve_one_of([
            OneOfPossibility(param="size", value=request.size,marshal_func=None
            ),
            OneOfPossibility(param="base_snapshot", value=request.base_snapshot,marshal_func=None
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.volume_type is not None:
        output["volume_type"] = str(request.volume_type)
    else:
        output["volume_type"] = None


    return output

def marshal_DetachServerFileSystemRequest(
    request: DetachServerFileSystemRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.filesystem_id is not None:
        output["filesystem_id"] = request.filesystem_id
    else:
        output["filesystem_id"] = str()


    return output

def marshal_DetachServerVolumeRequest(
    request: DetachServerVolumeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.volume_id is not None:
        output["volume_id"] = request.volume_id
    else:
        output["volume_id"] = str()


    return output

def marshal_ExportSnapshotRequest(
    request: ExportSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.bucket is not None:
        output["bucket"] = request.bucket
    else:
        output["bucket"] = str()

    if request.key is not None:
        output["key"] = request.key
    else:
        output["key"] = str()


    return output

def marshal_PlanBlockMigrationRequest(
    request: PlanBlockMigrationRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="volume_id", value=request.volume_id,marshal_func=None
            ),
            OneOfPossibility(param="snapshot_id", value=request.snapshot_id,marshal_func=None
            ),
        ]),
    )


    return output

def marshal_ServerActionRequestVolumeBackupTemplate(
    request: ServerActionRequestVolumeBackupTemplate,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.volume_type is not None:
        output["volume_type"] = str(request.volume_type)
    else:
        output["volume_type"] = getattr(SnapshotVolumeType, "UNKNOWN_VOLUME_TYPE")


    return output

def marshal_ServerActionRequest(
    request: ServerActionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = str(request.action)
    else:
        output["action"] = None

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.volumes is not None:
        output["volumes"] = {
            key: marshal_ServerActionRequestVolumeBackupTemplate(value, defaults)
            for key, value in request.volumes.items()
        }
    else:
        output["volumes"] = None

    if request.disable_ipv6 is not None:
        output["disable_ipv6"] = request.disable_ipv6
    else:
        output["disable_ipv6"] = None


    return output

def marshal_ServerSummary(
    request: ServerSummary,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()


    return output

def marshal_Bootscript(
    request: Bootscript,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.architecture is not None:
        output["architecture"] = str(request.architecture)
    else:
        output["architecture"] = str()

    if request.bootcmdargs is not None:
        output["bootcmdargs"] = request.bootcmdargs
    else:
        output["bootcmdargs"] = str()

    if request.default is not None:
        output["default"] = request.default
    else:
        output["default"] = str()

    if request.dtb is not None:
        output["dtb"] = request.dtb
    else:
        output["dtb"] = str()

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.initrd is not None:
        output["initrd"] = request.initrd
    else:
        output["initrd"] = str()

    if request.kernel is not None:
        output["kernel"] = request.kernel
    else:
        output["kernel"] = str()

    if request.organization is not None:
        output["organization"] = request.organization or defaults.default_organization_id
    else:
        output["organization"] = str()

    if request.public is not None:
        output["public"] = request.public
    else:
        output["public"] = str()

    if request.title is not None:
        output["title"] = request.title
    else:
        output["title"] = str()

    if request.project is not None:
        output["project"] = request.project or defaults.default_project_id
    else:
        output["project"] = str()

    if request.zone is not None:
        output["zone"] = request.zone or defaults.default_zone


    return output

def marshal_Volume(
    request: Volume,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = 0

    if request.volume_type is not None:
        output["volume_type"] = str(request.volume_type)
    else:
        output["volume_type"] = getattr(VolumeVolumeType, "L_SSD")

    if request.organization is not None:
        output["organization"] = request.organization or defaults.default_organization_id
    else:
        output["organization"] = str()

    if request.project is not None:
        output["project"] = request.project or defaults.default_project_id
    else:
        output["project"] = str()

    if request.export_uri is not None:
        output["export_uri"] = request.export_uri
    else:
        output["export_uri"] = None

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date.isoformat()
    else:
        output["creation_date"] = None

    if request.modification_date is not None:
        output["modification_date"] = request.modification_date.isoformat()
    else:
        output["modification_date"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = []

    if request.state is not None:
        output["state"] = str(request.state)
    else:
        output["state"] = getattr(VolumeState, "AVAILABLE")

    if request.zone is not None:
        output["zone"] = request.zone or defaults.default_zone

    if request.server is not None:
        output["server"] = marshal_ServerSummary(request.server, defaults)
    else:
        output["server"] = None


    return output

def marshal_VolumeSummary(
    request: VolumeSummary,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = str()

    if request.volume_type is not None:
        output["volume_type"] = str(request.volume_type)
    else:
        output["volume_type"] = str()


    return output

def marshal_SetImageRequest(
    request: SetImageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.arch is not None:
        output["arch"] = str(request.arch)
    else:
        output["arch"] = None

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date.isoformat()
    else:
        output["creation_date"] = None

    if request.modification_date is not None:
        output["modification_date"] = request.modification_date.isoformat()
    else:
        output["modification_date"] = None

    if request.from_server is not None:
        output["from_server"] = request.from_server
    else:
        output["from_server"] = str()

    if request.public is not None:
        output["public"] = request.public
    else:
        output["public"] = str()

    if request.default_bootscript is not None:
        output["default_bootscript"] = marshal_Bootscript(request.default_bootscript, defaults)
    else:
        output["default_bootscript"] = None

    if request.extra_volumes is not None:
        output["extra_volumes"] = {
            key: marshal_Volume(value, defaults)
            for key, value in request.extra_volumes.items()
        }
    else:
        output["extra_volumes"] = None

    if request.organization is not None:
        output["organization"] = request.organization or defaults.default_organization_id
    else:
        output["organization"] = None

    if request.root_volume is not None:
        output["root_volume"] = marshal_VolumeSummary(request.root_volume, defaults)
    else:
        output["root_volume"] = None

    if request.state is not None:
        output["state"] = str(request.state)
    else:
        output["state"] = None

    if request.project is not None:
        output["project"] = request.project or defaults.default_project_id
    else:
        output["project"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_SetPlacementGroupRequest(
    request: SetPlacementGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.organization is not None:
        output["organization"] = request.organization or defaults.default_organization_id
    else:
        output["organization"] = None

    if request.policy_mode is not None:
        output["policy_mode"] = str(request.policy_mode)
    else:
        output["policy_mode"] = None

    if request.policy_type is not None:
        output["policy_type"] = str(request.policy_type)
    else:
        output["policy_type"] = None

    if request.project is not None:
        output["project"] = request.project or defaults.default_project_id
    else:
        output["project"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_SetPlacementGroupServersRequest(
    request: SetPlacementGroupServersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.servers is not None:
        output["servers"] = request.servers
    else:
        output["servers"] = str()


    return output

def marshal_SetSecurityGroupRulesRequestRule(
    request: SetSecurityGroupRulesRequestRule,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = str(request.action)
    else:
        output["action"] = getattr(SecurityGroupRuleAction, "UNKNOWN_ACTION")

    if request.protocol is not None:
        output["protocol"] = str(request.protocol)
    else:
        output["protocol"] = getattr(SecurityGroupRuleProtocol, "UNKNOWN_PROTOCOL")

    if request.direction is not None:
        output["direction"] = str(request.direction)
    else:
        output["direction"] = getattr(SecurityGroupRuleDirection, "UNKNOWN_DIRECTION")

    if request.ip_range is not None:
        output["ip_range"] = request.ip_range
    else:
        output["ip_range"] = str()

    if request.position is not None:
        output["position"] = request.position
    else:
        output["position"] = 0

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = None

    if request.dest_port_from is not None:
        output["dest_port_from"] = request.dest_port_from
    else:
        output["dest_port_from"] = None

    if request.dest_port_to is not None:
        output["dest_port_to"] = request.dest_port_to
    else:
        output["dest_port_to"] = None

    if request.editable is not None:
        output["editable"] = request.editable
    else:
        output["editable"] = None

    if request.zone is not None:
        output["zone"] = request.zone


    return output

def marshal_SetSecurityGroupRulesRequest(
    request: SetSecurityGroupRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.rules is not None:
        output["rules"] = [marshal_SetSecurityGroupRulesRequestRule(item, defaults) for item in request.rules]
    else:
        output["rules"] = None


    return output

def marshal_VolumeImageUpdateTemplate(
    request: VolumeImageUpdateTemplate,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()


    return output

def marshal_UpdateImageRequest(
    request: UpdateImageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.arch is not None:
        output["arch"] = str(request.arch)
    else:
        output["arch"] = None

    if request.extra_volumes is not None:
        output["extra_volumes"] = {
            key: marshal_VolumeImageUpdateTemplate(value, defaults)
            for key, value in request.extra_volumes.items()
        }
    else:
        output["extra_volumes"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.public is not None:
        output["public"] = request.public
    else:
        output["public"] = None


    return output

def marshal_UpdateIpRequest(
    request: UpdateIpRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.reverse is not None:
        output["reverse"] = request.reverse
    else:
        output["reverse"] = None

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.server is not None:
        output["server"] = request.server
    else:
        output["server"] = None


    return output

def marshal_UpdatePlacementGroupRequest(
    request: UpdatePlacementGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.policy_mode is not None:
        output["policy_mode"] = str(request.policy_mode)
    else:
        output["policy_mode"] = None

    if request.policy_type is not None:
        output["policy_type"] = str(request.policy_type)
    else:
        output["policy_type"] = None


    return output

def marshal_UpdatePlacementGroupServersRequest(
    request: UpdatePlacementGroupServersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.servers is not None:
        output["servers"] = request.servers
    else:
        output["servers"] = str()


    return output

def marshal_UpdatePrivateNICRequest(
    request: UpdatePrivateNICRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_UpdateSecurityGroupRequest(
    request: UpdateSecurityGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.enable_default_security is not None:
        output["enable_default_security"] = request.enable_default_security
    else:
        output["enable_default_security"] = None

    if request.inbound_default_policy is not None:
        output["inbound_default_policy"] = str(request.inbound_default_policy)
    else:
        output["inbound_default_policy"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.organization_default is not None:
        output["organization_default"] = request.organization_default
    else:
        output["organization_default"] = None

    if request.project_default is not None:
        output["project_default"] = request.project_default
    else:
        output["project_default"] = None

    if request.outbound_default_policy is not None:
        output["outbound_default_policy"] = str(request.outbound_default_policy)
    else:
        output["outbound_default_policy"] = None

    if request.stateful is not None:
        output["stateful"] = request.stateful
    else:
        output["stateful"] = None


    return output

def marshal_UpdateSecurityGroupRuleRequest(
    request: UpdateSecurityGroupRuleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.protocol is not None:
        output["protocol"] = str(request.protocol)
    else:
        output["protocol"] = None

    if request.direction is not None:
        output["direction"] = str(request.direction)
    else:
        output["direction"] = None

    if request.action is not None:
        output["action"] = str(request.action)
    else:
        output["action"] = None

    if request.ip_range is not None:
        output["ip_range"] = request.ip_range
    else:
        output["ip_range"] = None

    if request.dest_port_from is not None:
        output["dest_port_from"] = request.dest_port_from
    else:
        output["dest_port_from"] = None

    if request.dest_port_to is not None:
        output["dest_port_to"] = request.dest_port_to
    else:
        output["dest_port_to"] = None

    if request.position is not None:
        output["position"] = request.position
    else:
        output["position"] = None


    return output

def marshal_SecurityGroupTemplate(
    request: SecurityGroupTemplate,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()


    return output

def marshal_UpdateServerRequest(
    request: UpdateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.boot_type is not None:
        output["boot_type"] = str(request.boot_type)
    else:
        output["boot_type"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.volumes is not None:
        output["volumes"] = {
            key: marshal_VolumeServerTemplate(value, defaults)
            for key, value in request.volumes.items()
        }
    else:
        output["volumes"] = None

    if request.dynamic_ip_required is not None:
        output["dynamic_ip_required"] = request.dynamic_ip_required
    else:
        output["dynamic_ip_required"] = None

    if request.routed_ip_enabled is not None:
        output["routed_ip_enabled"] = request.routed_ip_enabled
    else:
        output["routed_ip_enabled"] = None

    if request.public_ips is not None:
        output["public_ips"] = request.public_ips
    else:
        output["public_ips"] = None

    if request.enable_ipv6 is not None:
        output["enable_ipv6"] = request.enable_ipv6
    else:
        output["enable_ipv6"] = None

    if request.protected is not None:
        output["protected"] = request.protected
    else:
        output["protected"] = None

    if request.security_group is not None:
        output["security_group"] = marshal_SecurityGroupTemplate(request.security_group, defaults)
    else:
        output["security_group"] = None

    if request.placement_group is not None:
        output["placement_group"] = request.placement_group
    else:
        output["placement_group"] = None

    if request.private_nics is not None:
        output["private_nics"] = request.private_nics
    else:
        output["private_nics"] = None

    if request.commercial_type is not None:
        output["commercial_type"] = request.commercial_type
    else:
        output["commercial_type"] = None

    if request.admin_password_encryption_ssh_key_id is not None:
        output["admin_password_encryption_ssh_key_id"] = request.admin_password_encryption_ssh_key_id
    else:
        output["admin_password_encryption_ssh_key_id"] = None


    return output

def marshal_UpdateSnapshotRequest(
    request: UpdateSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_UpdateVolumeRequest(
    request: UpdateVolumeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = None


    return output

def marshal__SetSecurityGroupRequest(
    request: _SetSecurityGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.enable_default_security is not None:
        output["enable_default_security"] = request.enable_default_security
    else:
        output["enable_default_security"] = False

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date.isoformat()
    else:
        output["creation_date"] = None

    if request.modification_date is not None:
        output["modification_date"] = request.modification_date.isoformat()
    else:
        output["modification_date"] = None

    if request.project_default is not None:
        output["project_default"] = request.project_default
    else:
        output["project_default"] = False

    if request.stateful is not None:
        output["stateful"] = request.stateful
    else:
        output["stateful"] = False

    if request.inbound_default_policy is not None:
        output["inbound_default_policy"] = str(request.inbound_default_policy)
    else:
        output["inbound_default_policy"] = None

    if request.outbound_default_policy is not None:
        output["outbound_default_policy"] = str(request.outbound_default_policy)
    else:
        output["outbound_default_policy"] = None

    if request.organization is not None:
        output["organization"] = request.organization or defaults.default_organization_id
    else:
        output["organization"] = None

    if request.project is not None:
        output["project"] = request.project or defaults.default_project_id
    else:
        output["project"] = None

    if request.organization_default is not None:
        output["organization_default"] = request.organization_default
    else:
        output["organization_default"] = None

    if request.servers is not None:
        output["servers"] = [marshal_ServerSummary(item, defaults) for item in request.servers]
    else:
        output["servers"] = None


    return output

def marshal__SetSecurityGroupRuleRequest(
    request: _SetSecurityGroupRuleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.ip_range is not None:
        output["ip_range"] = request.ip_range
    else:
        output["ip_range"] = str()

    if request.position is not None:
        output["position"] = request.position
    else:
        output["position"] = str()

    if request.editable is not None:
        output["editable"] = request.editable
    else:
        output["editable"] = str()

    if request.protocol is not None:
        output["protocol"] = str(request.protocol)
    else:
        output["protocol"] = None

    if request.direction is not None:
        output["direction"] = str(request.direction)
    else:
        output["direction"] = None

    if request.action is not None:
        output["action"] = str(request.action)
    else:
        output["action"] = None

    if request.dest_port_from is not None:
        output["dest_port_from"] = request.dest_port_from
    else:
        output["dest_port_from"] = None

    if request.dest_port_to is not None:
        output["dest_port_to"] = request.dest_port_to
    else:
        output["dest_port_to"] = None


    return output

def marshal_Image(
    request: Image,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.arch is not None:
        output["arch"] = str(request.arch)
    else:
        output["arch"] = str()

    if request.extra_volumes is not None:
        output["extra_volumes"] = {
            key: marshal_Volume(value, defaults)
            for key, value in request.extra_volumes.items()
        }
    else:
        output["extra_volumes"] = str()

    if request.from_server is not None:
        output["from_server"] = request.from_server
    else:
        output["from_server"] = str()

    if request.organization is not None:
        output["organization"] = request.organization or defaults.default_organization_id
    else:
        output["organization"] = str()

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date.isoformat()
    else:
        output["creation_date"] = None

    if request.modification_date is not None:
        output["modification_date"] = request.modification_date.isoformat()
    else:
        output["modification_date"] = None

    if request.default_bootscript is not None:
        output["default_bootscript"] = marshal_Bootscript(request.default_bootscript, defaults)
    else:
        output["default_bootscript"] = None

    if request.public is not None:
        output["public"] = request.public
    else:
        output["public"] = str()

    if request.state is not None:
        output["state"] = str(request.state)
    else:
        output["state"] = str()

    if request.project is not None:
        output["project"] = request.project or defaults.default_project_id
    else:
        output["project"] = str()

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = str()

    if request.zone is not None:
        output["zone"] = request.zone or defaults.default_zone

    if request.root_volume is not None:
        output["root_volume"] = marshal_VolumeSummary(request.root_volume, defaults)
    else:
        output["root_volume"] = None


    return output

def marshal_PlacementGroup(
    request: PlacementGroup,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.organization is not None:
        output["organization"] = request.organization or defaults.default_organization_id
    else:
        output["organization"] = str()

    if request.project is not None:
        output["project"] = request.project or defaults.default_project_id
    else:
        output["project"] = str()

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = []

    if request.policy_mode is not None:
        output["policy_mode"] = str(request.policy_mode)
    else:
        output["policy_mode"] = getattr(PlacementGroupPolicyMode, "OPTIONAL")

    if request.policy_type is not None:
        output["policy_type"] = str(request.policy_type)
    else:
        output["policy_type"] = getattr(PlacementGroupPolicyType, "MAX_AVAILABILITY")

    if request.policy_respected is not None:
        output["policy_respected"] = request.policy_respected
    else:
        output["policy_respected"] = False

    if request.zone is not None:
        output["zone"] = request.zone or defaults.default_zone


    return output

def marshal_PrivateNIC(
    request: PrivateNIC,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.server_id is not None:
        output["server_id"] = request.server_id
    else:
        output["server_id"] = str()

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id
    else:
        output["private_network_id"] = str()

    if request.mac_address is not None:
        output["mac_address"] = request.mac_address
    else:
        output["mac_address"] = str()

    if request.state is not None:
        output["state"] = str(request.state)
    else:
        output["state"] = getattr(PrivateNICState, "AVAILABLE")

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = []


    return output

def marshal_SecurityGroupSummary(
    request: SecurityGroupSummary,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()


    return output

def marshal_ServerIp(
    request: ServerIp,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.address is not None:
        output["address"] = request.address
    else:
        output["address"] = str()

    if request.gateway is not None:
        output["gateway"] = request.gateway
    else:
        output["gateway"] = str()

    if request.netmask is not None:
        output["netmask"] = request.netmask
    else:
        output["netmask"] = str()

    if request.family is not None:
        output["family"] = str(request.family)
    else:
        output["family"] = getattr(ServerIpIpFamily, "INET")

    if request.dynamic is not None:
        output["dynamic"] = request.dynamic
    else:
        output["dynamic"] = False

    if request.provisioning_mode is not None:
        output["provisioning_mode"] = str(request.provisioning_mode)
    else:
        output["provisioning_mode"] = getattr(ServerIpProvisioningMode, "MANUAL")

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = []

    if request.ipam_id is not None:
        output["ipam_id"] = request.ipam_id
    else:
        output["ipam_id"] = str()

    if request.state is not None:
        output["state"] = str(request.state)
    else:
        output["state"] = getattr(ServerIpState, "UNKNOWN_STATE")


    return output

def marshal_ServerIpv6(
    request: ServerIpv6,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.address is not None:
        output["address"] = request.address
    else:
        output["address"] = str()

    if request.gateway is not None:
        output["gateway"] = request.gateway
    else:
        output["gateway"] = str()

    if request.netmask is not None:
        output["netmask"] = request.netmask
    else:
        output["netmask"] = str()


    return output

def marshal_ServerLocation(
    request: ServerLocation,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.cluster_id is not None:
        output["cluster_id"] = request.cluster_id
    else:
        output["cluster_id"] = str()

    if request.hypervisor_id is not None:
        output["hypervisor_id"] = request.hypervisor_id
    else:
        output["hypervisor_id"] = str()

    if request.node_id is not None:
        output["node_id"] = request.node_id
    else:
        output["node_id"] = str()

    if request.platform_id is not None:
        output["platform_id"] = request.platform_id
    else:
        output["platform_id"] = str()

    if request.zone_id is not None:
        output["zone_id"] = request.zone_id
    else:
        output["zone_id"] = str()


    return output

def marshal_ServerMaintenance(
    request: ServerMaintenance,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.reason is not None:
        output["reason"] = request.reason
    else:
        output["reason"] = str()

    if request.start_date is not None:
        output["start_date"] = request.start_date.isoformat()
    else:
        output["start_date"] = None


    return output

def marshal__SetServerRequest(
    request: _SetServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.commercial_type is not None:
        output["commercial_type"] = request.commercial_type
    else:
        output["commercial_type"] = str()

    if request.organization is not None:
        output["organization"] = request.organization or defaults.default_organization_id
    else:
        output["organization"] = None

    if request.dynamic_ip_required is not None:
        output["dynamic_ip_required"] = request.dynamic_ip_required
    else:
        output["dynamic_ip_required"] = False

    if request.hostname is not None:
        output["hostname"] = request.hostname
    else:
        output["hostname"] = str()

    if request.protected is not None:
        output["protected"] = request.protected
    else:
        output["protected"] = False

    if request.state_detail is not None:
        output["state_detail"] = request.state_detail
    else:
        output["state_detail"] = str()

    if request.project is not None:
        output["project"] = request.project or defaults.default_project_id
    else:
        output["project"] = None

    if request.allowed_actions is not None:
        output["allowed_actions"] = [str(item) for item in request.allowed_actions]
    else:
        output["allowed_actions"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date.isoformat()
    else:
        output["creation_date"] = None

    if request.routed_ip_enabled is not None:
        output["routed_ip_enabled"] = request.routed_ip_enabled
    else:
        output["routed_ip_enabled"] = None

    if request.enable_ipv6 is not None:
        output["enable_ipv6"] = request.enable_ipv6
    else:
        output["enable_ipv6"] = None

    if request.image is not None:
        output["image"] = marshal_Image(request.image, defaults)
    else:
        output["image"] = None

    if request.private_ip is not None:
        output["private_ip"] = request.private_ip
    else:
        output["private_ip"] = None

    if request.public_ip is not None:
        output["public_ip"] = marshal_ServerIp(request.public_ip, defaults)
    else:
        output["public_ip"] = None

    if request.public_ips is not None:
        output["public_ips"] = [marshal_ServerIp(item, defaults) for item in request.public_ips]
    else:
        output["public_ips"] = None

    if request.modification_date is not None:
        output["modification_date"] = request.modification_date.isoformat()
    else:
        output["modification_date"] = None

    if request.state is not None:
        output["state"] = str(request.state)
    else:
        output["state"] = None

    if request.location is not None:
        output["location"] = marshal_ServerLocation(request.location, defaults)
    else:
        output["location"] = None

    if request.ipv6 is not None:
        output["ipv6"] = marshal_ServerIpv6(request.ipv6, defaults)
    else:
        output["ipv6"] = None

    if request.boot_type is not None:
        output["boot_type"] = str(request.boot_type)
    else:
        output["boot_type"] = None

    if request.volumes is not None:
        output["volumes"] = {
            key: marshal_Volume(value, defaults)
            for key, value in request.volumes.items()
        }
    else:
        output["volumes"] = None

    if request.security_group is not None:
        output["security_group"] = marshal_SecurityGroupSummary(request.security_group, defaults)
    else:
        output["security_group"] = None

    if request.maintenances is not None:
        output["maintenances"] = [marshal_ServerMaintenance(item, defaults) for item in request.maintenances]
    else:
        output["maintenances"] = None

    if request.arch is not None:
        output["arch"] = str(request.arch)
    else:
        output["arch"] = None

    if request.placement_group is not None:
        output["placement_group"] = marshal_PlacementGroup(request.placement_group, defaults)
    else:
        output["placement_group"] = None

    if request.private_nics is not None:
        output["private_nics"] = [marshal_PrivateNIC(item, defaults) for item in request.private_nics]
    else:
        output["private_nics"] = None

    if request.admin_password_encryption_ssh_key_id is not None:
        output["admin_password_encryption_ssh_key_id"] = request.admin_password_encryption_ssh_key_id
    else:
        output["admin_password_encryption_ssh_key_id"] = None


    return output

def marshal_SnapshotBaseVolume(
    request: SnapshotBaseVolume,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()


    return output

def marshal__SetSnapshotRequest(
    request: _SetSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.organization is not None:
        output["organization"] = request.organization or defaults.default_organization_id
    else:
        output["organization"] = None

    if request.volume_type is not None:
        output["volume_type"] = str(request.volume_type)
    else:
        output["volume_type"] = None

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = str()

    if request.state is not None:
        output["state"] = str(request.state)
    else:
        output["state"] = None

    if request.base_volume is not None:
        output["base_volume"] = marshal_SnapshotBaseVolume(request.base_volume, defaults)
    else:
        output["base_volume"] = None

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date.isoformat()
    else:
        output["creation_date"] = None

    if request.modification_date is not None:
        output["modification_date"] = request.modification_date.isoformat()
    else:
        output["modification_date"] = None

    if request.project is not None:
        output["project"] = request.project or defaults.default_project_id
    else:
        output["project"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output
