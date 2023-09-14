# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from dateutil import parser
from .types import (
    Arch,
    BootType,
    ImageState,
    IpType,
    PlacementGroupPolicyMode,
    PlacementGroupPolicyType,
    PrivateNICState,
    SecurityGroupPolicy,
    SecurityGroupRuleAction,
    SecurityGroupRuleDirection,
    SecurityGroupRuleProtocol,
    ServerAction,
    ServerIpIpFamily,
    ServerIpProvisioningMode,
    ServerState,
    SnapshotState,
    SnapshotVolumeType,
    VolumeState,
    VolumeVolumeType,
    Bootscript,
    CreateImageResponse,
    CreateIpResponse,
    CreatePlacementGroupResponse,
    CreatePrivateNICResponse,
    CreateSecurityGroupResponse,
    CreateSecurityGroupRuleResponse,
    CreateServerResponse,
    CreateSnapshotResponse,
    CreateVolumeResponse,
    Dashboard,
    ExportSnapshotResponse,
    GetBootscriptResponse,
    GetDashboardResponse,
    GetImageResponse,
    GetIpResponse,
    GetPlacementGroupResponse,
    GetPlacementGroupServersResponse,
    GetPrivateNICResponse,
    GetSecurityGroupResponse,
    GetSecurityGroupRuleResponse,
    GetServerResponse,
    GetServerTypesAvailabilityResponse,
    GetServerTypesAvailabilityResponseAvailability,
    GetSnapshotResponse,
    GetVolumeResponse,
    Image,
    Ip,
    ListBootscriptsResponse,
    ListImagesResponse,
    ListIpsResponse,
    ListPlacementGroupsResponse,
    ListPrivateNICsResponse,
    ListSecurityGroupRulesResponse,
    ListSecurityGroupsResponse,
    ListServerActionsResponse,
    ListServerUserDataResponse,
    ListServersResponse,
    ListServersTypesResponse,
    ListSnapshotsResponse,
    ListVolumesResponse,
    ListVolumesTypesResponse,
    MigrationPlan,
    PlacementGroup,
    PlacementGroupServer,
    PrivateNIC,
    SecurityGroup,
    SecurityGroupRule,
    SecurityGroupSummary,
    SecurityGroupTemplate,
    Server,
    ServerActionRequestVolumeBackupTemplate,
    ServerActionResponse,
    ServerIp,
    ServerIpv6,
    ServerLocation,
    ServerMaintenance,
    ServerSummary,
    ServerType,
    ServerTypeCapabilities,
    ServerTypeNetwork,
    ServerTypeNetworkInterface,
    ServerTypeVolumeConstraintSizes,
    ServerTypeVolumeConstraintsByType,
    SetPlacementGroupResponse,
    SetPlacementGroupServersResponse,
    SetSecurityGroupRulesRequestRule,
    SetSecurityGroupRulesResponse,
    Snapshot,
    SnapshotBaseVolume,
    Task,
    UpdateIpResponse,
    UpdatePlacementGroupResponse,
    UpdatePlacementGroupServersResponse,
    UpdateServerResponse,
    UpdateVolumeResponse,
    Volume,
    VolumeServer,
    VolumeServerTemplate,
    VolumeSummary,
    VolumeTemplate,
    VolumeType,
    VolumeTypeCapabilities,
    VolumeTypeConstraints,
    ServerActionRequest,
    CreateImageRequest,
    CreateSnapshotRequest,
    ExportSnapshotRequest,
    CreateVolumeRequest,
    UpdateVolumeRequest,
    CreateSecurityGroupRequest,
    CreateSecurityGroupRuleRequest,
    SetSecurityGroupRulesRequest,
    CreatePlacementGroupRequest,
    SetPlacementGroupRequest,
    UpdatePlacementGroupRequest,
    SetPlacementGroupServersRequest,
    UpdatePlacementGroupServersRequest,
    CreateIpRequest,
    UpdateIpRequest,
    CreatePrivateNICRequest,
    UpdatePrivateNICRequest,
    PlanBlockMigrationRequest,
    ApplyBlockMigrationRequest,
)
from .types_private import (
    _SetImageResponse,
    _SetSecurityGroupResponse,
    _SetSecurityGroupRuleResponse,
    _SetServerResponse,
    _SetSnapshotResponse,
    _CreateServerRequest,
    _SetServerRequest,
    _UpdateServerRequest,
    _SetImageRequest,
    _SetSnapshotRequest,
    _SetSecurityGroupRequest,
    _SetSecurityGroupRuleRequest,
)


def unmarshal_ServerSummary(data: Any) -> ServerSummary:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    return ServerSummary(**args)


def unmarshal_Bootscript(data: Any) -> Bootscript:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Bootscript' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("arch", None)
    args["arch"] = field

    field = data.get("bootcmdargs", None)
    args["bootcmdargs"] = field

    field = data.get("default", None)
    args["default"] = field

    field = data.get("dtb", None)
    args["dtb"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("initrd", None)
    args["initrd"] = field

    field = data.get("kernel", None)
    args["kernel"] = field

    field = data.get("organization", None)
    args["organization"] = field

    field = data.get("project", None)
    args["project"] = field

    field = data.get("public", None)
    args["public"] = field

    field = data.get("title", None)
    args["title"] = field

    field = data.get("zone", None)
    args["zone"] = field

    return Bootscript(**args)


def unmarshal_ServerTypeNetworkInterface(data: Any) -> ServerTypeNetworkInterface:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerTypeNetworkInterface' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("internal_bandwidth", None)
    args["internal_bandwidth"] = field

    field = data.get("internet_bandwidth", None)
    args["internet_bandwidth"] = field

    return ServerTypeNetworkInterface(**args)


def unmarshal_ServerTypeVolumeConstraintSizes(
    data: Any,
) -> ServerTypeVolumeConstraintSizes:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerTypeVolumeConstraintSizes' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("max_size", None)
    args["max_size"] = field

    field = data.get("min_size", None)
    args["min_size"] = field

    return ServerTypeVolumeConstraintSizes(**args)


def unmarshal_Volume(data: Any) -> Volume:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Volume' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("creation_date", None)
    args["creation_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("export_uri", None)
    args["export_uri"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("modification_date", None)
    args["modification_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("organization", None)
    args["organization"] = field

    field = data.get("project", None)
    args["project"] = field

    field = data.get("server", None)
    args["server"] = unmarshal_ServerSummary(field) if field is not None else None

    field = data.get("size", None)
    args["size"] = field

    field = data.get("state", None)
    args["state"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("volume_type", None)
    args["volume_type"] = field

    field = data.get("zone", None)
    args["zone"] = field

    return Volume(**args)


def unmarshal_VolumeSummary(data: Any) -> VolumeSummary:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'VolumeSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("size", None)
    args["size"] = field

    field = data.get("volume_type", None)
    args["volume_type"] = field

    return VolumeSummary(**args)


def unmarshal_Image(data: Any) -> Image:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Image' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("arch", None)
    args["arch"] = field

    field = data.get("creation_date", None)
    args["creation_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("default_bootscript", None)
    args["default_bootscript"] = (
        unmarshal_Bootscript(field) if field is not None else None
    )

    field = data.get("extra_volumes", None)
    args["extra_volumes"] = (
        {k: unmarshal_Volume(v) for k, v in field.items()}
        if field is not None
        else None
    )

    field = data.get("from_server", None)
    args["from_server"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("modification_date", None)
    args["modification_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("organization", None)
    args["organization"] = field

    field = data.get("project", None)
    args["project"] = field

    field = data.get("public", None)
    args["public"] = field

    field = data.get("root_volume", None)
    args["root_volume"] = unmarshal_VolumeSummary(field) if field is not None else None

    field = data.get("state", None)
    args["state"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("zone", None)
    args["zone"] = field

    return Image(**args)


def unmarshal_PlacementGroup(data: Any) -> PlacementGroup:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'PlacementGroup' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("organization", None)
    args["organization"] = field

    field = data.get("policy_mode", None)
    args["policy_mode"] = field

    field = data.get("policy_respected", None)
    args["policy_respected"] = field

    field = data.get("policy_type", None)
    args["policy_type"] = field

    field = data.get("project", None)
    args["project"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("zone", None)
    args["zone"] = field

    return PlacementGroup(**args)


def unmarshal_PrivateNIC(data: Any) -> PrivateNIC:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'PrivateNIC' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("mac_address", None)
    args["mac_address"] = field

    field = data.get("private_network_id", None)
    args["private_network_id"] = field

    field = data.get("server_id", None)
    args["server_id"] = field

    field = data.get("state", None)
    args["state"] = field

    field = data.get("tags", None)
    args["tags"] = field

    return PrivateNIC(**args)


def unmarshal_SecurityGroupSummary(data: Any) -> SecurityGroupSummary:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SecurityGroupSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    return SecurityGroupSummary(**args)


def unmarshal_ServerIp(data: Any) -> ServerIp:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerIp' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("address", None)
    args["address"] = field

    field = data.get("dynamic", None)
    args["dynamic"] = field

    field = data.get("family", None)
    args["family"] = field

    field = data.get("gateway", None)
    args["gateway"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("netmask", None)
    args["netmask"] = field

    field = data.get("provisioning_mode", None)
    args["provisioning_mode"] = field

    return ServerIp(**args)


def unmarshal_ServerIpv6(data: Any) -> ServerIpv6:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerIpv6' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("address", None)
    args["address"] = field

    field = data.get("gateway", None)
    args["gateway"] = field

    field = data.get("netmask", None)
    args["netmask"] = field

    return ServerIpv6(**args)


def unmarshal_ServerLocation(data: Any) -> ServerLocation:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerLocation' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("cluster_id", None)
    args["cluster_id"] = field

    field = data.get("hypervisor_id", None)
    args["hypervisor_id"] = field

    field = data.get("node_id", None)
    args["node_id"] = field

    field = data.get("platform_id", None)
    args["platform_id"] = field

    field = data.get("zone_id", None)
    args["zone_id"] = field

    return ServerLocation(**args)


def unmarshal_ServerMaintenance(data: Any) -> ServerMaintenance:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerMaintenance' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("reason", None)
    args["reason"] = field

    return ServerMaintenance(**args)


def unmarshal_ServerTypeCapabilities(data: Any) -> ServerTypeCapabilities:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerTypeCapabilities' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("block_storage", None)
    args["block_storage"] = field

    field = data.get("boot_types", None)
    args["boot_types"] = field

    return ServerTypeCapabilities(**args)


def unmarshal_ServerTypeNetwork(data: Any) -> ServerTypeNetwork:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerTypeNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("interfaces", None)
    args["interfaces"] = (
        [unmarshal_ServerTypeNetworkInterface(v) for v in field]
        if field is not None
        else None
    )

    field = data.get("ipv6_support", None)
    args["ipv6_support"] = field

    field = data.get("sum_internal_bandwidth", None)
    args["sum_internal_bandwidth"] = field

    field = data.get("sum_internet_bandwidth", None)
    args["sum_internet_bandwidth"] = field

    return ServerTypeNetwork(**args)


def unmarshal_ServerTypeVolumeConstraintsByType(
    data: Any,
) -> ServerTypeVolumeConstraintsByType:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerTypeVolumeConstraintsByType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("l_ssd", None)
    args["l_ssd"] = (
        unmarshal_ServerTypeVolumeConstraintSizes(field) if field is not None else None
    )

    return ServerTypeVolumeConstraintsByType(**args)


def unmarshal_SnapshotBaseVolume(data: Any) -> SnapshotBaseVolume:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SnapshotBaseVolume' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    return SnapshotBaseVolume(**args)


def unmarshal_VolumeServer(data: Any) -> VolumeServer:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'VolumeServer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("boot", None)
    args["boot"] = field

    field = data.get("creation_date", None)
    args["creation_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("export_uri", None)
    args["export_uri"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("modification_date", None)
    args["modification_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("organization", None)
    args["organization"] = field

    field = data.get("project", None)
    args["project"] = field

    field = data.get("server", None)
    args["server"] = unmarshal_ServerSummary(field) if field is not None else None

    field = data.get("size", None)
    args["size"] = field

    field = data.get("state", None)
    args["state"] = field

    field = data.get("volume_type", None)
    args["volume_type"] = field

    field = data.get("zone", None)
    args["zone"] = field

    return VolumeServer(**args)


def unmarshal_VolumeTypeCapabilities(data: Any) -> VolumeTypeCapabilities:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'VolumeTypeCapabilities' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshot", None)
    args["snapshot"] = field

    return VolumeTypeCapabilities(**args)


def unmarshal_VolumeTypeConstraints(data: Any) -> VolumeTypeConstraints:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'VolumeTypeConstraints' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("max", None)
    args["max"] = field

    field = data.get("min", None)
    args["min"] = field

    return VolumeTypeConstraints(**args)


def unmarshal_Dashboard(data: Any) -> Dashboard:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Dashboard' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("images_count", None)
    args["images_count"] = field

    field = data.get("ips_count", None)
    args["ips_count"] = field

    field = data.get("ips_unused", None)
    args["ips_unused"] = field

    field = data.get("placement_groups_count", None)
    args["placement_groups_count"] = field

    field = data.get("private_nics_count", None)
    args["private_nics_count"] = field

    field = data.get("running_servers_count", None)
    args["running_servers_count"] = field

    field = data.get("security_groups_count", None)
    args["security_groups_count"] = field

    field = data.get("servers_by_types", None)
    args["servers_by_types"] = field

    field = data.get("servers_count", None)
    args["servers_count"] = field

    field = data.get("snapshots_count", None)
    args["snapshots_count"] = field

    field = data.get("volumes_b_ssd_count", None)
    args["volumes_b_ssd_count"] = field

    field = data.get("volumes_b_ssd_total_size", None)
    args["volumes_b_ssd_total_size"] = field

    field = data.get("volumes_count", None)
    args["volumes_count"] = field

    field = data.get("volumes_l_ssd_count", None)
    args["volumes_l_ssd_count"] = field

    field = data.get("volumes_l_ssd_total_size", None)
    args["volumes_l_ssd_total_size"] = field

    return Dashboard(**args)


def unmarshal_GetServerTypesAvailabilityResponseAvailability(
    data: Any,
) -> GetServerTypesAvailabilityResponseAvailability:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetServerTypesAvailabilityResponseAvailability' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("availability", None)
    args["availability"] = field

    return GetServerTypesAvailabilityResponseAvailability(**args)


def unmarshal_Ip(data: Any) -> Ip:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Ip' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("address", None)
    args["address"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("organization", None)
    args["organization"] = field

    field = data.get("prefix", None)
    args["prefix"] = field

    field = data.get("project", None)
    args["project"] = field

    field = data.get("reverse", None)
    args["reverse"] = field

    field = data.get("server", None)
    args["server"] = unmarshal_ServerSummary(field) if field is not None else None

    field = data.get("state", None)
    args["state"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("type", None)
    args["type_"] = field

    field = data.get("zone", None)
    args["zone"] = field

    return Ip(**args)


def unmarshal_PlacementGroupServer(data: Any) -> PlacementGroupServer:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'PlacementGroupServer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("policy_respected", None)
    args["policy_respected"] = field

    return PlacementGroupServer(**args)


def unmarshal_SecurityGroup(data: Any) -> SecurityGroup:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SecurityGroup' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("creation_date", None)
    args["creation_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("enable_default_security", None)
    args["enable_default_security"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("inbound_default_policy", None)
    args["inbound_default_policy"] = field

    field = data.get("modification_date", None)
    args["modification_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("organization", None)
    args["organization"] = field

    field = data.get("organization_default", None)
    args["organization_default"] = field

    field = data.get("outbound_default_policy", None)
    args["outbound_default_policy"] = field

    field = data.get("project", None)
    args["project"] = field

    field = data.get("project_default", None)
    args["project_default"] = field

    field = data.get("servers", None)
    args["servers"] = (
        [unmarshal_ServerSummary(v) for v in field] if field is not None else None
    )

    field = data.get("state", None)
    args["state"] = field

    field = data.get("stateful", None)
    args["stateful"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("zone", None)
    args["zone"] = field

    return SecurityGroup(**args)


def unmarshal_SecurityGroupRule(data: Any) -> SecurityGroupRule:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SecurityGroupRule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("action", None)
    args["action"] = field

    field = data.get("dest_port_from", None)
    args["dest_port_from"] = field

    field = data.get("dest_port_to", None)
    args["dest_port_to"] = field

    field = data.get("direction", None)
    args["direction"] = field

    field = data.get("editable", None)
    args["editable"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("ip_range", None)
    args["ip_range"] = field

    field = data.get("position", None)
    args["position"] = field

    field = data.get("protocol", None)
    args["protocol"] = field

    field = data.get("zone", None)
    args["zone"] = field

    return SecurityGroupRule(**args)


def unmarshal_Server(data: Any) -> Server:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Server' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("allowed_actions", None)
    args["allowed_actions"] = field

    field = data.get("arch", None)
    args["arch"] = field

    field = data.get("boot_type", None)
    args["boot_type"] = field

    field = data.get("bootscript", None)
    args["bootscript"] = unmarshal_Bootscript(field) if field is not None else None

    field = data.get("commercial_type", None)
    args["commercial_type"] = field

    field = data.get("creation_date", None)
    args["creation_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("dynamic_ip_required", None)
    args["dynamic_ip_required"] = field

    field = data.get("enable_ipv6", None)
    args["enable_ipv6"] = field

    field = data.get("hostname", None)
    args["hostname"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("image", None)
    args["image"] = unmarshal_Image(field) if field is not None else None

    field = data.get("ipv6", None)
    args["ipv6"] = unmarshal_ServerIpv6(field) if field is not None else None

    field = data.get("location", None)
    args["location"] = unmarshal_ServerLocation(field) if field is not None else None

    field = data.get("mac_address", None)
    args["mac_address"] = field

    field = data.get("maintenances", None)
    args["maintenances"] = (
        [unmarshal_ServerMaintenance(v) for v in field] if field is not None else None
    )

    field = data.get("modification_date", None)
    args["modification_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("organization", None)
    args["organization"] = field

    field = data.get("placement_group", None)
    args["placement_group"] = (
        unmarshal_PlacementGroup(field) if field is not None else None
    )

    field = data.get("private_ip", None)
    args["private_ip"] = field

    field = data.get("private_nics", None)
    args["private_nics"] = (
        [unmarshal_PrivateNIC(v) for v in field] if field is not None else None
    )

    field = data.get("project", None)
    args["project"] = field

    field = data.get("protected", None)
    args["protected"] = field

    field = data.get("public_ip", None)
    args["public_ip"] = unmarshal_ServerIp(field) if field is not None else None

    field = data.get("public_ips", None)
    args["public_ips"] = (
        [unmarshal_ServerIp(v) for v in field] if field is not None else None
    )

    field = data.get("routed_ip_enabled", None)
    args["routed_ip_enabled"] = field

    field = data.get("security_group", None)
    args["security_group"] = (
        unmarshal_SecurityGroupSummary(field) if field is not None else None
    )

    field = data.get("state", None)
    args["state"] = field

    field = data.get("state_detail", None)
    args["state_detail"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("volumes", None)
    args["volumes"] = (
        {k: unmarshal_VolumeServer(v) for k, v in field.items()}
        if field is not None
        else None
    )

    field = data.get("zone", None)
    args["zone"] = field

    return Server(**args)


def unmarshal_ServerType(data: Any) -> ServerType:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("alt_names", None)
    args["alt_names"] = field

    field = data.get("arch", None)
    args["arch"] = field

    field = data.get("baremetal", None)
    args["baremetal"] = field

    field = data.get("capabilities", None)
    args["capabilities"] = (
        unmarshal_ServerTypeCapabilities(field) if field is not None else None
    )

    field = data.get("gpu", None)
    args["gpu"] = field

    field = data.get("hourly_price", None)
    args["hourly_price"] = field

    field = data.get("monthly_price", None)
    args["monthly_price"] = field

    field = data.get("ncpus", None)
    args["ncpus"] = field

    field = data.get("network", None)
    args["network"] = unmarshal_ServerTypeNetwork(field) if field is not None else None

    field = data.get("per_volume_constraint", None)
    args["per_volume_constraint"] = (
        unmarshal_ServerTypeVolumeConstraintsByType(field)
        if field is not None
        else None
    )

    field = data.get("ram", None)
    args["ram"] = field

    field = data.get("scratch_storage_max_size", None)
    args["scratch_storage_max_size"] = field

    field = data.get("volumes_constraint", None)
    args["volumes_constraint"] = (
        unmarshal_ServerTypeVolumeConstraintSizes(field) if field is not None else None
    )

    return ServerType(**args)


def unmarshal_Snapshot(data: Any) -> Snapshot:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Snapshot' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("base_volume", None)
    args["base_volume"] = (
        unmarshal_SnapshotBaseVolume(field) if field is not None else None
    )

    field = data.get("creation_date", None)
    args["creation_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("error_reason", None)
    args["error_reason"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("modification_date", None)
    args["modification_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("organization", None)
    args["organization"] = field

    field = data.get("project", None)
    args["project"] = field

    field = data.get("size", None)
    args["size"] = field

    field = data.get("state", None)
    args["state"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("volume_type", None)
    args["volume_type"] = field

    field = data.get("zone", None)
    args["zone"] = field

    return Snapshot(**args)


def unmarshal_Task(data: Any) -> Task:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Task' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description", None)
    args["description"] = field

    field = data.get("href_from", None)
    args["href_from"] = field

    field = data.get("href_result", None)
    args["href_result"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("progress", None)
    args["progress"] = field

    field = data.get("started_at", None)
    args["started_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("terminated_at", None)
    args["terminated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("zone", None)
    args["zone"] = field

    return Task(**args)


def unmarshal_VolumeType(data: Any) -> VolumeType:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'VolumeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("capabilities", None)
    args["capabilities"] = (
        unmarshal_VolumeTypeCapabilities(field) if field is not None else None
    )

    field = data.get("constraints", None)
    args["constraints"] = (
        unmarshal_VolumeTypeConstraints(field) if field is not None else None
    )

    field = data.get("display_name", None)
    args["display_name"] = field

    return VolumeType(**args)


def unmarshal_CreateImageResponse(data: Any) -> CreateImageResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreateImageResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("image", None)
    args["image"] = unmarshal_Image(field) if field is not None else None

    return CreateImageResponse(**args)


def unmarshal_CreateIpResponse(data: Any) -> CreateIpResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreateIpResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip", None)
    args["ip"] = unmarshal_Ip(field) if field is not None else None

    return CreateIpResponse(**args)


def unmarshal_CreatePlacementGroupResponse(data: Any) -> CreatePlacementGroupResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreatePlacementGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("placement_group", None)
    args["placement_group"] = (
        unmarshal_PlacementGroup(field) if field is not None else None
    )

    return CreatePlacementGroupResponse(**args)


def unmarshal_CreatePrivateNICResponse(data: Any) -> CreatePrivateNICResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreatePrivateNICResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_nic", None)
    args["private_nic"] = unmarshal_PrivateNIC(field) if field is not None else None

    return CreatePrivateNICResponse(**args)


def unmarshal_CreateSecurityGroupResponse(data: Any) -> CreateSecurityGroupResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreateSecurityGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("security_group", None)
    args["security_group"] = (
        unmarshal_SecurityGroup(field) if field is not None else None
    )

    return CreateSecurityGroupResponse(**args)


def unmarshal_CreateSecurityGroupRuleResponse(
    data: Any,
) -> CreateSecurityGroupRuleResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreateSecurityGroupRuleResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rule", None)
    args["rule"] = unmarshal_SecurityGroupRule(field) if field is not None else None

    return CreateSecurityGroupRuleResponse(**args)


def unmarshal_CreateServerResponse(data: Any) -> CreateServerResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreateServerResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server", None)
    args["server"] = unmarshal_Server(field) if field is not None else None

    return CreateServerResponse(**args)


def unmarshal_CreateSnapshotResponse(data: Any) -> CreateSnapshotResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreateSnapshotResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshot", None)
    args["snapshot"] = unmarshal_Snapshot(field) if field is not None else None

    field = data.get("task", None)
    args["task"] = unmarshal_Task(field) if field is not None else None

    return CreateSnapshotResponse(**args)


def unmarshal_CreateVolumeResponse(data: Any) -> CreateVolumeResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreateVolumeResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("volume", None)
    args["volume"] = unmarshal_Volume(field) if field is not None else None

    return CreateVolumeResponse(**args)


def unmarshal_ExportSnapshotResponse(data: Any) -> ExportSnapshotResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ExportSnapshotResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("task", None)
    args["task"] = unmarshal_Task(field) if field is not None else None

    return ExportSnapshotResponse(**args)


def unmarshal_GetBootscriptResponse(data: Any) -> GetBootscriptResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetBootscriptResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("bootscript", None)
    args["bootscript"] = unmarshal_Bootscript(field) if field is not None else None

    return GetBootscriptResponse(**args)


def unmarshal_GetDashboardResponse(data: Any) -> GetDashboardResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetDashboardResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dashboard", None)
    args["dashboard"] = unmarshal_Dashboard(field) if field is not None else None

    return GetDashboardResponse(**args)


def unmarshal_GetImageResponse(data: Any) -> GetImageResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetImageResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("image", None)
    args["image"] = unmarshal_Image(field) if field is not None else None

    return GetImageResponse(**args)


def unmarshal_GetIpResponse(data: Any) -> GetIpResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetIpResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip", None)
    args["ip"] = unmarshal_Ip(field) if field is not None else None

    return GetIpResponse(**args)


def unmarshal_GetPlacementGroupResponse(data: Any) -> GetPlacementGroupResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetPlacementGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("placement_group", None)
    args["placement_group"] = (
        unmarshal_PlacementGroup(field) if field is not None else None
    )

    return GetPlacementGroupResponse(**args)


def unmarshal_GetPlacementGroupServersResponse(
    data: Any,
) -> GetPlacementGroupServersResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetPlacementGroupServersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("servers", None)
    args["servers"] = (
        [unmarshal_PlacementGroupServer(v) for v in field]
        if field is not None
        else None
    )

    return GetPlacementGroupServersResponse(**args)


def unmarshal_GetPrivateNICResponse(data: Any) -> GetPrivateNICResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetPrivateNICResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_nic", None)
    args["private_nic"] = unmarshal_PrivateNIC(field) if field is not None else None

    return GetPrivateNICResponse(**args)


def unmarshal_GetSecurityGroupResponse(data: Any) -> GetSecurityGroupResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetSecurityGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("security_group", None)
    args["security_group"] = (
        unmarshal_SecurityGroup(field) if field is not None else None
    )

    return GetSecurityGroupResponse(**args)


def unmarshal_GetSecurityGroupRuleResponse(data: Any) -> GetSecurityGroupRuleResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetSecurityGroupRuleResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rule", None)
    args["rule"] = unmarshal_SecurityGroupRule(field) if field is not None else None

    return GetSecurityGroupRuleResponse(**args)


def unmarshal_GetServerResponse(data: Any) -> GetServerResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetServerResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server", None)
    args["server"] = unmarshal_Server(field) if field is not None else None

    return GetServerResponse(**args)


def unmarshal_GetServerTypesAvailabilityResponse(
    data: Any,
) -> GetServerTypesAvailabilityResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetServerTypesAvailabilityResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("servers", None)
    args["servers"] = (
        {
            k: unmarshal_GetServerTypesAvailabilityResponseAvailability(v)
            for k, v in field.items()
        }
        if field is not None
        else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return GetServerTypesAvailabilityResponse(**args)


def unmarshal_GetSnapshotResponse(data: Any) -> GetSnapshotResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetSnapshotResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshot", None)
    args["snapshot"] = unmarshal_Snapshot(field) if field is not None else None

    return GetSnapshotResponse(**args)


def unmarshal_GetVolumeResponse(data: Any) -> GetVolumeResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetVolumeResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("volume", None)
    args["volume"] = unmarshal_Volume(field) if field is not None else None

    return GetVolumeResponse(**args)


def unmarshal_ListBootscriptsResponse(data: Any) -> ListBootscriptsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListBootscriptsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("bootscripts", None)
    args["bootscripts"] = (
        [unmarshal_Bootscript(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListBootscriptsResponse(**args)


def unmarshal_ListImagesResponse(data: Any) -> ListImagesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListImagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("images", None)
    args["images"] = [unmarshal_Image(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListImagesResponse(**args)


def unmarshal_ListIpsResponse(data: Any) -> ListIpsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListIpsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ips", None)
    args["ips"] = [unmarshal_Ip(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListIpsResponse(**args)


def unmarshal_ListPlacementGroupsResponse(data: Any) -> ListPlacementGroupsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListPlacementGroupsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("placement_groups", None)
    args["placement_groups"] = (
        [unmarshal_PlacementGroup(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListPlacementGroupsResponse(**args)


def unmarshal_ListPrivateNICsResponse(data: Any) -> ListPrivateNICsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListPrivateNICsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_nics", None)
    args["private_nics"] = (
        [unmarshal_PrivateNIC(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListPrivateNICsResponse(**args)


def unmarshal_ListSecurityGroupRulesResponse(
    data: Any,
) -> ListSecurityGroupRulesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListSecurityGroupRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", None)
    args["rules"] = (
        [unmarshal_SecurityGroupRule(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListSecurityGroupRulesResponse(**args)


def unmarshal_ListSecurityGroupsResponse(data: Any) -> ListSecurityGroupsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListSecurityGroupsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("security_groups", None)
    args["security_groups"] = (
        [unmarshal_SecurityGroup(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListSecurityGroupsResponse(**args)


def unmarshal_ListServerActionsResponse(data: Any) -> ListServerActionsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListServerActionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("actions", None)
    args["actions"] = field

    return ListServerActionsResponse(**args)


def unmarshal_ListServerUserDataResponse(data: Any) -> ListServerUserDataResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListServerUserDataResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("user_data", None)
    args["user_data"] = field

    return ListServerUserDataResponse(**args)


def unmarshal_ListServersResponse(data: Any) -> ListServersResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListServersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("servers", None)
    args["servers"] = (
        [unmarshal_Server(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListServersResponse(**args)


def unmarshal_ListServersTypesResponse(data: Any) -> ListServersTypesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListServersTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("servers", None)
    args["servers"] = (
        {k: unmarshal_ServerType(v) for k, v in field.items()}
        if field is not None
        else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListServersTypesResponse(**args)


def unmarshal_ListSnapshotsResponse(data: Any) -> ListSnapshotsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListSnapshotsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshots", None)
    args["snapshots"] = (
        [unmarshal_Snapshot(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListSnapshotsResponse(**args)


def unmarshal_ListVolumesResponse(data: Any) -> ListVolumesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListVolumesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    args["total_count"] = field

    field = data.get("volumes", None)
    args["volumes"] = (
        [unmarshal_Volume(v) for v in field] if field is not None else None
    )

    return ListVolumesResponse(**args)


def unmarshal_ListVolumesTypesResponse(data: Any) -> ListVolumesTypesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListVolumesTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    args["total_count"] = field

    field = data.get("volumes", None)
    args["volumes"] = (
        {k: unmarshal_VolumeType(v) for k, v in field.items()}
        if field is not None
        else None
    )

    return ListVolumesTypesResponse(**args)


def unmarshal_MigrationPlan(data: Any) -> MigrationPlan:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'MigrationPlan' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshots", None)
    args["snapshots"] = (
        [unmarshal_Snapshot(v) for v in field] if field is not None else None
    )

    field = data.get("validation_key", None)
    args["validation_key"] = field

    field = data.get("volume", None)
    args["volume"] = unmarshal_Volume(field) if field is not None else None

    return MigrationPlan(**args)


def unmarshal_ServerActionResponse(data: Any) -> ServerActionResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerActionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("task", None)
    args["task"] = unmarshal_Task(field) if field is not None else None

    return ServerActionResponse(**args)


def unmarshal_SetPlacementGroupResponse(data: Any) -> SetPlacementGroupResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SetPlacementGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("placement_group", None)
    args["placement_group"] = (
        unmarshal_PlacementGroup(field) if field is not None else None
    )

    return SetPlacementGroupResponse(**args)


def unmarshal_SetPlacementGroupServersResponse(
    data: Any,
) -> SetPlacementGroupServersResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SetPlacementGroupServersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("servers", None)
    args["servers"] = (
        [unmarshal_PlacementGroupServer(v) for v in field]
        if field is not None
        else None
    )

    return SetPlacementGroupServersResponse(**args)


def unmarshal_SetSecurityGroupRulesResponse(data: Any) -> SetSecurityGroupRulesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SetSecurityGroupRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", None)
    args["rules"] = (
        [unmarshal_SecurityGroupRule(v) for v in field] if field is not None else None
    )

    return SetSecurityGroupRulesResponse(**args)


def unmarshal_UpdateIpResponse(data: Any) -> UpdateIpResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'UpdateIpResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip", None)
    args["ip"] = unmarshal_Ip(field) if field is not None else None

    return UpdateIpResponse(**args)


def unmarshal_UpdatePlacementGroupResponse(data: Any) -> UpdatePlacementGroupResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'UpdatePlacementGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("placement_group", None)
    args["placement_group"] = (
        unmarshal_PlacementGroup(field) if field is not None else None
    )

    return UpdatePlacementGroupResponse(**args)


def unmarshal_UpdatePlacementGroupServersResponse(
    data: Any,
) -> UpdatePlacementGroupServersResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'UpdatePlacementGroupServersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("servers", None)
    args["servers"] = (
        [unmarshal_PlacementGroupServer(v) for v in field]
        if field is not None
        else None
    )

    return UpdatePlacementGroupServersResponse(**args)


def unmarshal_UpdateServerResponse(data: Any) -> UpdateServerResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'UpdateServerResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server", None)
    args["server"] = unmarshal_Server(field) if field is not None else None

    return UpdateServerResponse(**args)


def unmarshal_UpdateVolumeResponse(data: Any) -> UpdateVolumeResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'UpdateVolumeResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("volume", None)
    args["volume"] = unmarshal_Volume(field) if field is not None else None

    return UpdateVolumeResponse(**args)


def unmarshal__SetImageResponse(data: Any) -> _SetImageResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type '_SetImageResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("image", None)
    args["image"] = unmarshal_Image(field) if field is not None else None

    return _SetImageResponse(**args)


def unmarshal__SetSecurityGroupResponse(data: Any) -> _SetSecurityGroupResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type '_SetSecurityGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("security_group", None)
    args["security_group"] = (
        unmarshal_SecurityGroup(field) if field is not None else None
    )

    return _SetSecurityGroupResponse(**args)


def unmarshal__SetSecurityGroupRuleResponse(data: Any) -> _SetSecurityGroupRuleResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type '_SetSecurityGroupRuleResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rule", None)
    args["rule"] = unmarshal_SecurityGroupRule(field) if field is not None else None

    return _SetSecurityGroupRuleResponse(**args)


def unmarshal__SetServerResponse(data: Any) -> _SetServerResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type '_SetServerResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server", None)
    args["server"] = unmarshal_Server(field) if field is not None else None

    return _SetServerResponse(**args)


def unmarshal__SetSnapshotResponse(data: Any) -> _SetSnapshotResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type '_SetSnapshotResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshot", None)
    args["snapshot"] = unmarshal_Snapshot(field) if field is not None else None

    return _SetSnapshotResponse(**args)


def marshal_ServerSummary(
    request: ServerSummary,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_Bootscript(
    request: Bootscript,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.arch is not None:
        output["arch"] = Arch(request.arch)

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

    if request.project is not None:
        output["project"] = request.project

    if request.public is not None:
        output["public"] = request.public

    if request.title is not None:
        output["title"] = request.title

    if request.zone is not None:
        output["zone"] = request.zone

    return output


def marshal_Volume(
    request: Volume,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date

    if request.export_uri is not None:
        output["export_uri"] = request.export_uri

    if request.id is not None:
        output["id"] = request.id

    if request.modification_date is not None:
        output["modification_date"] = request.modification_date

    if request.name is not None:
        output["name"] = request.name

    if request.organization is not None:
        output["organization"] = request.organization

    if request.project is not None:
        output["project"] = request.project

    if request.server is not None:
        output["server"] = marshal_ServerSummary(request.server, defaults)

    if request.size is not None:
        output["size"] = request.size

    if request.state is not None:
        output["state"] = VolumeState(request.state)

    if request.tags is not None:
        output["tags"] = request.tags

    if request.volume_type is not None:
        output["volume_type"] = VolumeVolumeType(request.volume_type)

    if request.zone is not None:
        output["zone"] = request.zone

    return output


def marshal_VolumeSummary(
    request: VolumeSummary,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.name is not None:
        output["name"] = request.name

    if request.size is not None:
        output["size"] = request.size

    if request.volume_type is not None:
        output["volume_type"] = VolumeVolumeType(request.volume_type)

    return output


def marshal_Image(
    request: Image,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.arch is not None:
        output["arch"] = Arch(request.arch)

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date

    if request.default_bootscript is not None:
        output["default_bootscript"] = marshal_Bootscript(
            request.default_bootscript, defaults
        )

    if request.extra_volumes is not None:
        output["extra_volumes"] = {
            k: marshal_Volume(v, defaults) for k, v in request.extra_volumes.items()
        }

    if request.from_server is not None:
        output["from_server"] = request.from_server

    if request.id is not None:
        output["id"] = request.id

    if request.modification_date is not None:
        output["modification_date"] = request.modification_date

    if request.name is not None:
        output["name"] = request.name

    if request.organization is not None:
        output["organization"] = request.organization

    if request.project is not None:
        output["project"] = request.project

    if request.public is not None:
        output["public"] = request.public

    if request.root_volume is not None:
        output["root_volume"] = marshal_VolumeSummary(request.root_volume, defaults)

    if request.state is not None:
        output["state"] = ImageState(request.state)

    if request.tags is not None:
        output["tags"] = request.tags

    if request.zone is not None:
        output["zone"] = request.zone

    return output


def marshal_PlacementGroup(
    request: PlacementGroup,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.name is not None:
        output["name"] = request.name

    if request.organization is not None:
        output["organization"] = request.organization

    if request.policy_mode is not None:
        output["policy_mode"] = PlacementGroupPolicyMode(request.policy_mode)

    if request.policy_respected is not None:
        output["policy_respected"] = request.policy_respected

    if request.policy_type is not None:
        output["policy_type"] = PlacementGroupPolicyType(request.policy_type)

    if request.project is not None:
        output["project"] = request.project

    if request.tags is not None:
        output["tags"] = request.tags

    if request.zone is not None:
        output["zone"] = request.zone

    return output


def marshal_PrivateNIC(
    request: PrivateNIC,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.mac_address is not None:
        output["mac_address"] = request.mac_address

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    if request.server_id is not None:
        output["server_id"] = request.server_id

    if request.state is not None:
        output["state"] = PrivateNICState(request.state)

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_SecurityGroupSummary(
    request: SecurityGroupSummary,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_SecurityGroupTemplate(
    request: SecurityGroupTemplate,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_ServerActionRequestVolumeBackupTemplate(
    request: ServerActionRequestVolumeBackupTemplate,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.volume_type is not None:
        output["volume_type"] = SnapshotVolumeType(request.volume_type)

    return output


def marshal_ServerIp(
    request: ServerIp,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.address is not None:
        output["address"] = request.address

    if request.dynamic is not None:
        output["dynamic"] = request.dynamic

    if request.family is not None:
        output["family"] = ServerIpIpFamily(request.family)

    if request.gateway is not None:
        output["gateway"] = request.gateway

    if request.id is not None:
        output["id"] = request.id

    if request.netmask is not None:
        output["netmask"] = request.netmask

    if request.provisioning_mode is not None:
        output["provisioning_mode"] = ServerIpProvisioningMode(
            request.provisioning_mode
        )

    return output


def marshal_ServerIpv6(
    request: ServerIpv6,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

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
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

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
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.reason is not None:
        output["reason"] = request.reason

    return output


def marshal_SetSecurityGroupRulesRequestRule(
    request: SetSecurityGroupRulesRequestRule,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = SecurityGroupRuleAction(request.action)

    if request.dest_port_from is not None:
        output["dest_port_from"] = request.dest_port_from

    if request.dest_port_to is not None:
        output["dest_port_to"] = request.dest_port_to

    if request.direction is not None:
        output["direction"] = SecurityGroupRuleDirection(request.direction)

    if request.editable is not None:
        output["editable"] = request.editable

    if request.id is not None:
        output["id"] = request.id

    if request.ip_range is not None:
        output["ip_range"] = request.ip_range

    if request.position is not None:
        output["position"] = request.position

    if request.protocol is not None:
        output["protocol"] = SecurityGroupRuleProtocol(request.protocol)

    if request.zone is not None:
        output["zone"] = request.zone

    return output


def marshal_SnapshotBaseVolume(
    request: SnapshotBaseVolume,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_VolumeServerTemplate(
    request: VolumeServerTemplate,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.base_snapshot is not None:
        output["base_snapshot"] = request.base_snapshot

    if request.boot is not None:
        output["boot"] = request.boot

    if request.id is not None:
        output["id"] = request.id

    if request.name is not None:
        output["name"] = request.name

    if request.organization is not None:
        output["organization"] = request.organization

    if request.project is not None:
        output["project"] = request.project

    if request.size is not None:
        output["size"] = request.size

    if request.volume_type is not None:
        output["volume_type"] = VolumeVolumeType(request.volume_type)

    return output


def marshal_VolumeTemplate(
    request: VolumeTemplate,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "project",
                    request.project if request.project is not None else None,
                    defaults.default_project_id,
                ),
                OneOfPossibility(
                    "organization",
                    request.organization if request.organization is not None else None,
                    defaults.default_organization_id,
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
        output["volume_type"] = VolumeVolumeType(request.volume_type)

    return output


def marshal_ApplyBlockMigrationRequest(
    request: ApplyBlockMigrationRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "volume_id",
                    request.volume_id if request.volume_id is not None else None,
                ),
                OneOfPossibility(
                    "snapshot_id",
                    request.snapshot_id if request.snapshot_id is not None else None,
                ),
            ]
        ),
    )

    if request.validation_key is not None:
        output["validation_key"] = request.validation_key

    return output


def marshal_CreateImageRequest(
    request: CreateImageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "project",
                    request.project or defaults.default_project_id
                    if request.project is not None
                    else None,
                    defaults.default_project_id,
                ),
                OneOfPossibility(
                    "organization",
                    request.organization or defaults.default_organization_id
                    if request.organization is not None
                    else None,
                    defaults.default_organization_id,
                ),
            ]
        ),
    )

    if request.arch is not None:
        output["arch"] = Arch(request.arch)

    if request.default_bootscript is not None:
        output["default_bootscript"] = request.default_bootscript

    if request.extra_volumes is not None:
        output["extra_volumes"] = {
            k: marshal_VolumeTemplate(v, defaults)
            for k, v in request.extra_volumes.items()
        }

    if request.name is not None:
        output["name"] = request.name

    if request.public is not None:
        output["public"] = request.public

    if request.root_volume is not None:
        output["root_volume"] = request.root_volume

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreateIpRequest(
    request: CreateIpRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "project",
                    request.project or defaults.default_project_id
                    if request.project is not None
                    else None,
                    defaults.default_project_id,
                ),
                OneOfPossibility(
                    "organization",
                    request.organization or defaults.default_organization_id
                    if request.organization is not None
                    else None,
                    defaults.default_organization_id,
                ),
            ]
        ),
    )

    if request.server is not None:
        output["server"] = request.server

    if request.tags is not None:
        output["tags"] = request.tags

    if request.type_ is not None:
        output["type"] = IpType(request.type_)

    return output


def marshal_CreatePlacementGroupRequest(
    request: CreatePlacementGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "project",
                    request.project or defaults.default_project_id
                    if request.project is not None
                    else None,
                    defaults.default_project_id,
                ),
                OneOfPossibility(
                    "organization",
                    request.organization or defaults.default_organization_id
                    if request.organization is not None
                    else None,
                    defaults.default_organization_id,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.policy_mode is not None:
        output["policy_mode"] = PlacementGroupPolicyMode(request.policy_mode)

    if request.policy_type is not None:
        output["policy_type"] = PlacementGroupPolicyType(request.policy_type)

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreatePrivateNICRequest(
    request: CreatePrivateNICRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip_ids is not None:
        output["ip_ids"] = request.ip_ids

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreateSecurityGroupRequest(
    request: CreateSecurityGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "organization_default",
                    request.organization_default
                    if request.organization_default is not None
                    else None,
                ),
                OneOfPossibility(
                    "project_default",
                    request.project_default
                    if request.project_default is not None
                    else None,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "project",
                    request.project or defaults.default_project_id
                    if request.project is not None
                    else None,
                    defaults.default_project_id,
                ),
                OneOfPossibility(
                    "organization",
                    request.organization or defaults.default_organization_id
                    if request.organization is not None
                    else None,
                    defaults.default_organization_id,
                ),
            ]
        ),
    )

    if request.description is not None:
        output["description"] = request.description

    if request.enable_default_security is not None:
        output["enable_default_security"] = request.enable_default_security

    if request.inbound_default_policy is not None:
        output["inbound_default_policy"] = SecurityGroupPolicy(
            request.inbound_default_policy
        )

    if request.name is not None:
        output["name"] = request.name

    if request.outbound_default_policy is not None:
        output["outbound_default_policy"] = SecurityGroupPolicy(
            request.outbound_default_policy
        )

    if request.stateful is not None:
        output["stateful"] = request.stateful

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreateSecurityGroupRuleRequest(
    request: CreateSecurityGroupRuleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = SecurityGroupRuleAction(request.action)

    if request.dest_port_from is not None:
        output["dest_port_from"] = request.dest_port_from

    if request.dest_port_to is not None:
        output["dest_port_to"] = request.dest_port_to

    if request.direction is not None:
        output["direction"] = SecurityGroupRuleDirection(request.direction)

    if request.editable is not None:
        output["editable"] = request.editable

    if request.ip_range is not None:
        output["ip_range"] = request.ip_range

    if request.position is not None:
        output["position"] = request.position

    if request.protocol is not None:
        output["protocol"] = SecurityGroupRuleProtocol(request.protocol)

    return output


def marshal_CreateSnapshotRequest(
    request: CreateSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "project",
                    request.project or defaults.default_project_id
                    if request.project is not None
                    else None,
                    defaults.default_project_id,
                ),
                OneOfPossibility(
                    "organization",
                    request.organization or defaults.default_organization_id
                    if request.organization is not None
                    else None,
                    defaults.default_organization_id,
                ),
            ]
        ),
    )

    if request.bucket is not None:
        output["bucket"] = request.bucket

    if request.key is not None:
        output["key"] = request.key

    if request.name is not None:
        output["name"] = request.name

    if request.size is not None:
        output["size"] = request.size

    if request.tags is not None:
        output["tags"] = request.tags

    if request.volume_id is not None:
        output["volume_id"] = request.volume_id

    if request.volume_type is not None:
        output["volume_type"] = SnapshotVolumeType(request.volume_type)

    return output


def marshal_CreateVolumeRequest(
    request: CreateVolumeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "project",
                    request.project or defaults.default_project_id
                    if request.project is not None
                    else None,
                    defaults.default_project_id,
                ),
                OneOfPossibility(
                    "organization",
                    request.organization or defaults.default_organization_id
                    if request.organization is not None
                    else None,
                    defaults.default_organization_id,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "size", request.size if request.size is not None else None
                ),
                OneOfPossibility(
                    "base_volume",
                    request.base_volume if request.base_volume is not None else None,
                ),
                OneOfPossibility(
                    "base_snapshot",
                    request.base_snapshot
                    if request.base_snapshot is not None
                    else None,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.volume_type is not None:
        output["volume_type"] = VolumeVolumeType(request.volume_type)

    return output


def marshal_ExportSnapshotRequest(
    request: ExportSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.bucket is not None:
        output["bucket"] = request.bucket

    if request.key is not None:
        output["key"] = request.key

    return output


def marshal_PlanBlockMigrationRequest(
    request: PlanBlockMigrationRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "volume_id",
                    request.volume_id if request.volume_id is not None else None,
                ),
                OneOfPossibility(
                    "snapshot_id",
                    request.snapshot_id if request.snapshot_id is not None else None,
                ),
            ]
        ),
    )

    return output


def marshal_ServerActionRequest(
    request: ServerActionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = ServerAction(request.action)

    if request.name is not None:
        output["name"] = request.name

    if request.volumes is not None:
        output["volumes"] = {
            k: marshal_ServerActionRequestVolumeBackupTemplate(v, defaults)
            for k, v in request.volumes.items()
        }

    return output


def marshal_SetPlacementGroupRequest(
    request: SetPlacementGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.organization is not None:
        output["organization"] = (
            request.organization or defaults.default_organization_id
        )

    if request.policy_mode is not None:
        output["policy_mode"] = PlacementGroupPolicyMode(request.policy_mode)

    if request.policy_type is not None:
        output["policy_type"] = PlacementGroupPolicyType(request.policy_type)

    if request.project is not None:
        output["project"] = request.project or defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_SetPlacementGroupServersRequest(
    request: SetPlacementGroupServersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.servers is not None:
        output["servers"] = request.servers

    return output


def marshal_SetSecurityGroupRulesRequest(
    request: SetSecurityGroupRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.rules is not None:
        output["rules"] = [
            marshal_SetSecurityGroupRulesRequestRule(v, defaults) for v in request.rules
        ]

    return output


def marshal_UpdateIpRequest(
    request: UpdateIpRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.reverse is not None:
        output["reverse"] = request.reverse

    if request.server is not None:
        output["server"] = request.server

    if request.tags is not None:
        output["tags"] = request.tags

    if request.type_ is not None:
        output["type"] = IpType(request.type_)

    return output


def marshal_UpdatePlacementGroupRequest(
    request: UpdatePlacementGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.policy_mode is not None:
        output["policy_mode"] = PlacementGroupPolicyMode(request.policy_mode)

    if request.policy_type is not None:
        output["policy_type"] = PlacementGroupPolicyType(request.policy_type)

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdatePlacementGroupServersRequest(
    request: UpdatePlacementGroupServersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.servers is not None:
        output["servers"] = request.servers

    return output


def marshal_UpdatePrivateNICRequest(
    request: UpdatePrivateNICRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateVolumeRequest(
    request: UpdateVolumeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.size is not None:
        output["size"] = request.size

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal__CreateServerRequest(
    request: _CreateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "project",
                    request.project or defaults.default_project_id
                    if request.project is not None
                    else None,
                    defaults.default_project_id,
                ),
                OneOfPossibility(
                    "organization",
                    request.organization or defaults.default_organization_id
                    if request.organization is not None
                    else None,
                    defaults.default_organization_id,
                ),
            ]
        ),
    )

    if request.boot_type is not None:
        output["boot_type"] = BootType(request.boot_type)

    if request.bootscript is not None:
        output["bootscript"] = request.bootscript

    if request.commercial_type is not None:
        output["commercial_type"] = request.commercial_type

    if request.dynamic_ip_required is not None:
        output["dynamic_ip_required"] = request.dynamic_ip_required

    if request.enable_ipv6 is not None:
        output["enable_ipv6"] = request.enable_ipv6

    if request.image is not None:
        output["image"] = request.image

    if request.name is not None:
        output["name"] = request.name

    if request.placement_group is not None:
        output["placement_group"] = request.placement_group

    if request.public_ip is not None:
        output["public_ip"] = request.public_ip

    if request.public_ips is not None:
        output["public_ips"] = request.public_ips

    if request.routed_ip_enabled is not None:
        output["routed_ip_enabled"] = request.routed_ip_enabled

    if request.security_group is not None:
        output["security_group"] = request.security_group

    if request.tags is not None:
        output["tags"] = request.tags

    if request.volumes is not None:
        output["volumes"] = {
            k: marshal_VolumeServerTemplate(v, defaults)
            for k, v in request.volumes.items()
        }

    return output


def marshal__SetImageRequest(
    request: _SetImageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.arch is not None:
        output["arch"] = Arch(request.arch)

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date

    if request.default_bootscript is not None:
        output["default_bootscript"] = marshal_Bootscript(
            request.default_bootscript, defaults
        )

    if request.extra_volumes is not None:
        output["extra_volumes"] = {
            k: marshal_Volume(v, defaults) for k, v in request.extra_volumes.items()
        }

    if request.from_server is not None:
        output["from_server"] = request.from_server

    if request.modification_date is not None:
        output["modification_date"] = request.modification_date

    if request.name is not None:
        output["name"] = request.name

    if request.organization is not None:
        output["organization"] = (
            request.organization or defaults.default_organization_id
        )

    if request.project is not None:
        output["project"] = request.project or defaults.default_project_id

    if request.public is not None:
        output["public"] = request.public

    if request.root_volume is not None:
        output["root_volume"] = marshal_VolumeSummary(request.root_volume, defaults)

    if request.state is not None:
        output["state"] = ImageState(request.state)

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal__SetSecurityGroupRequest(
    request: _SetSecurityGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date

    if request.description is not None:
        output["description"] = request.description

    if request.enable_default_security is not None:
        output["enable_default_security"] = request.enable_default_security

    if request.inbound_default_policy is not None:
        output["inbound_default_policy"] = SecurityGroupPolicy(
            request.inbound_default_policy
        )

    if request.modification_date is not None:
        output["modification_date"] = request.modification_date

    if request.name is not None:
        output["name"] = request.name

    if request.organization is not None:
        output["organization"] = (
            request.organization or defaults.default_organization_id
        )

    if request.organization_default is not None:
        output["organization_default"] = request.organization_default

    if request.outbound_default_policy is not None:
        output["outbound_default_policy"] = SecurityGroupPolicy(
            request.outbound_default_policy
        )

    if request.project is not None:
        output["project"] = request.project or defaults.default_project_id

    if request.project_default is not None:
        output["project_default"] = request.project_default

    if request.servers is not None:
        output["servers"] = [
            marshal_ServerSummary(v, defaults) for v in request.servers
        ]

    if request.stateful is not None:
        output["stateful"] = request.stateful

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal__SetSecurityGroupRuleRequest(
    request: _SetSecurityGroupRuleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = SecurityGroupRuleAction(request.action)

    if request.dest_port_from is not None:
        output["dest_port_from"] = request.dest_port_from

    if request.dest_port_to is not None:
        output["dest_port_to"] = request.dest_port_to

    if request.direction is not None:
        output["direction"] = SecurityGroupRuleDirection(request.direction)

    if request.editable is not None:
        output["editable"] = request.editable

    if request.id is not None:
        output["id"] = request.id

    if request.ip_range is not None:
        output["ip_range"] = request.ip_range

    if request.position is not None:
        output["position"] = request.position

    if request.protocol is not None:
        output["protocol"] = SecurityGroupRuleProtocol(request.protocol)

    return output


def marshal__SetServerRequest(
    request: _SetServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.allowed_actions is not None:
        output["allowed_actions"] = [ServerAction(v) for v in request.allowed_actions]

    if request.arch is not None:
        output["arch"] = Arch(request.arch)

    if request.boot_type is not None:
        output["boot_type"] = BootType(request.boot_type)

    if request.bootscript is not None:
        output["bootscript"] = marshal_Bootscript(request.bootscript, defaults)

    if request.commercial_type is not None:
        output["commercial_type"] = request.commercial_type

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date

    if request.dynamic_ip_required is not None:
        output["dynamic_ip_required"] = request.dynamic_ip_required

    if request.enable_ipv6 is not None:
        output["enable_ipv6"] = request.enable_ipv6

    if request.hostname is not None:
        output["hostname"] = request.hostname

    if request.image is not None:
        output["image"] = marshal_Image(request.image, defaults)

    if request.ipv6 is not None:
        output["ipv6"] = marshal_ServerIpv6(request.ipv6, defaults)

    if request.location is not None:
        output["location"] = marshal_ServerLocation(request.location, defaults)

    if request.maintenances is not None:
        output["maintenances"] = [
            marshal_ServerMaintenance(v, defaults) for v in request.maintenances
        ]

    if request.modification_date is not None:
        output["modification_date"] = request.modification_date

    if request.name is not None:
        output["name"] = request.name

    if request.organization is not None:
        output["organization"] = (
            request.organization or defaults.default_organization_id
        )

    if request.placement_group is not None:
        output["placement_group"] = marshal_PlacementGroup(
            request.placement_group, defaults
        )

    if request.private_ip is not None:
        output["private_ip"] = request.private_ip

    if request.private_nics is not None:
        output["private_nics"] = [
            marshal_PrivateNIC(v, defaults) for v in request.private_nics
        ]

    if request.project is not None:
        output["project"] = request.project or defaults.default_project_id

    if request.protected is not None:
        output["protected"] = request.protected

    if request.public_ip is not None:
        output["public_ip"] = marshal_ServerIp(request.public_ip, defaults)

    if request.public_ips is not None:
        output["public_ips"] = [
            marshal_ServerIp(v, defaults) for v in request.public_ips
        ]

    if request.routed_ip_enabled is not None:
        output["routed_ip_enabled"] = request.routed_ip_enabled

    if request.security_group is not None:
        output["security_group"] = marshal_SecurityGroupSummary(
            request.security_group, defaults
        )

    if request.state is not None:
        output["state"] = ServerState(request.state)

    if request.state_detail is not None:
        output["state_detail"] = request.state_detail

    if request.tags is not None:
        output["tags"] = request.tags

    if request.volumes is not None:
        output["volumes"] = {
            k: marshal_Volume(v, defaults) for k, v in request.volumes.items()
        }

    return output


def marshal__SetSnapshotRequest(
    request: _SetSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.base_volume is not None:
        output["base_volume"] = marshal_SnapshotBaseVolume(
            request.base_volume, defaults
        )

    if request.creation_date is not None:
        output["creation_date"] = request.creation_date

    if request.id is not None:
        output["id"] = request.id

    if request.modification_date is not None:
        output["modification_date"] = request.modification_date

    if request.name is not None:
        output["name"] = request.name

    if request.organization is not None:
        output["organization"] = (
            request.organization or defaults.default_organization_id
        )

    if request.project is not None:
        output["project"] = request.project or defaults.default_project_id

    if request.size is not None:
        output["size"] = request.size

    if request.state is not None:
        output["state"] = SnapshotState(request.state)

    if request.tags is not None:
        output["tags"] = request.tags

    if request.volume_type is not None:
        output["volume_type"] = VolumeVolumeType(request.volume_type)

    return output


def marshal__UpdateServerRequest(
    request: _UpdateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.boot_type is not None:
        output["boot_type"] = BootType(request.boot_type)

    if request.bootscript is not None:
        output["bootscript"] = request.bootscript

    if request.commercial_type is not None:
        output["commercial_type"] = request.commercial_type

    if request.dynamic_ip_required is not None:
        output["dynamic_ip_required"] = request.dynamic_ip_required

    if request.enable_ipv6 is not None:
        output["enable_ipv6"] = request.enable_ipv6

    if request.name is not None:
        output["name"] = request.name

    if request.placement_group is not None:
        output["placement_group"] = request.placement_group

    if request.private_nics is not None:
        output["private_nics"] = [
            marshal_PrivateNIC(v, defaults) for v in request.private_nics
        ]

    if request.protected is not None:
        output["protected"] = request.protected

    if request.public_ips is not None:
        output["public_ips"] = [
            marshal_ServerIp(v, defaults) for v in request.public_ips
        ]

    if request.routed_ip_enabled is not None:
        output["routed_ip_enabled"] = request.routed_ip_enabled

    if request.security_group is not None:
        output["security_group"] = marshal_SecurityGroupTemplate(
            request.security_group, defaults
        )

    if request.tags is not None:
        output["tags"] = request.tags

    if request.volumes is not None:
        output["volumes"] = {
            k: marshal_VolumeServerTemplate(v, defaults)
            for k, v in request.volumes.items()
        }

    return output
