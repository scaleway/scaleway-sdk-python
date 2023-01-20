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
    PlacementGroupPolicyMode,
    PlacementGroupPolicyType,
    PrivateNICState,
    SecurityGroupPolicy,
    SecurityGroupRuleAction,
    SecurityGroupRuleDirection,
    SecurityGroupRuleProtocol,
    ServerAction,
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

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    return ServerSummary(**args)


def unmarshal_Bootscript(data: Any) -> Bootscript:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Bootscript' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("arch")
    args["arch"] = field

    field = data.get("bootcmdargs")
    args["bootcmdargs"] = field

    field = data.get("default")
    args["default"] = field

    field = data.get("dtb")
    args["dtb"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("initrd")
    args["initrd"] = field

    field = data.get("kernel")
    args["kernel"] = field

    field = data.get("organization")
    args["organization"] = field

    field = data.get("project")
    args["project"] = field

    field = data.get("public")
    args["public"] = field

    field = data.get("title")
    args["title"] = field

    field = data.get("zone")
    args["zone"] = field

    return Bootscript(**args)


def unmarshal_ServerTypeNetworkInterface(data: Any) -> ServerTypeNetworkInterface:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerTypeNetworkInterface' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("internal_bandwidth")
    args["internal_bandwidth"] = field

    field = data.get("internet_bandwidth")
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

    field = data.get("max_size")
    args["max_size"] = field

    field = data.get("min_size")
    args["min_size"] = field

    return ServerTypeVolumeConstraintSizes(**args)


def unmarshal_Volume(data: Any) -> Volume:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Volume' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("creation_date")
    args["creation_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("export_uri")
    args["export_uri"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("modification_date")
    args["modification_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("name")
    args["name"] = field

    field = data.get("organization")
    args["organization"] = field

    field = data.get("project")
    args["project"] = field

    field = data.get("server")
    args["server"] = unmarshal_ServerSummary(field) if field is not None else None

    field = data.get("size")
    args["size"] = field

    field = data.get("state")
    args["state"] = field

    field = data.get("tags")
    args["tags"] = field

    field = data.get("volume_type")
    args["volume_type"] = field

    field = data.get("zone")
    args["zone"] = field

    return Volume(**args)


def unmarshal_VolumeSummary(data: Any) -> VolumeSummary:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'VolumeSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("size")
    args["size"] = field

    field = data.get("volume_type")
    args["volume_type"] = field

    return VolumeSummary(**args)


def unmarshal_Image(data: Any) -> Image:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Image' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("arch")
    args["arch"] = field

    field = data.get("creation_date")
    args["creation_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("default_bootscript")
    args["default_bootscript"] = (
        unmarshal_Bootscript(field) if field is not None else None
    )

    field = data.get("extra_volumes")
    args["extra_volumes"] = {
        k: unmarshal_Volume(v) for k, v in data["extra_volumes"].items()
    }

    field = data.get("from_server")
    args["from_server"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("modification_date")
    args["modification_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("name")
    args["name"] = field

    field = data.get("organization")
    args["organization"] = field

    field = data.get("project")
    args["project"] = field

    field = data.get("public")
    args["public"] = field

    field = data.get("root_volume")
    args["root_volume"] = unmarshal_VolumeSummary(field) if field is not None else None

    field = data.get("state")
    args["state"] = field

    field = data.get("tags")
    args["tags"] = field

    field = data.get("zone")
    args["zone"] = field

    return Image(**args)


def unmarshal_PlacementGroup(data: Any) -> PlacementGroup:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'PlacementGroup' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("organization")
    args["organization"] = field

    field = data.get("policy_mode")
    args["policy_mode"] = field

    field = data.get("policy_respected")
    args["policy_respected"] = field

    field = data.get("policy_type")
    args["policy_type"] = field

    field = data.get("project")
    args["project"] = field

    field = data.get("tags")
    args["tags"] = field

    field = data.get("zone")
    args["zone"] = field

    return PlacementGroup(**args)


def unmarshal_PrivateNIC(data: Any) -> PrivateNIC:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'PrivateNIC' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id")
    args["id"] = field

    field = data.get("mac_address")
    args["mac_address"] = field

    field = data.get("private_network_id")
    args["private_network_id"] = field

    field = data.get("server_id")
    args["server_id"] = field

    field = data.get("state")
    args["state"] = field

    return PrivateNIC(**args)


def unmarshal_SecurityGroupSummary(data: Any) -> SecurityGroupSummary:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SecurityGroupSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    return SecurityGroupSummary(**args)


def unmarshal_ServerIp(data: Any) -> ServerIp:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerIp' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("address")
    args["address"] = field

    field = data.get("dynamic")
    args["dynamic"] = field

    field = data.get("id")
    args["id"] = field

    return ServerIp(**args)


def unmarshal_ServerIpv6(data: Any) -> ServerIpv6:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerIpv6' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("address")
    args["address"] = field

    field = data.get("gateway")
    args["gateway"] = field

    field = data.get("netmask")
    args["netmask"] = field

    return ServerIpv6(**args)


def unmarshal_ServerLocation(data: Any) -> ServerLocation:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerLocation' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("cluster_id")
    args["cluster_id"] = field

    field = data.get("hypervisor_id")
    args["hypervisor_id"] = field

    field = data.get("node_id")
    args["node_id"] = field

    field = data.get("platform_id")
    args["platform_id"] = field

    field = data.get("zone_id")
    args["zone_id"] = field

    return ServerLocation(**args)


def unmarshal_ServerMaintenance(data: Any) -> ServerMaintenance:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerMaintenance' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("reason")
    args["reason"] = field

    return ServerMaintenance(**args)


def unmarshal_ServerTypeCapabilities(data: Any) -> ServerTypeCapabilities:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerTypeCapabilities' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("block_storage")
    args["block_storage"] = field

    field = data.get("boot_types")
    args["boot_types"] = field

    return ServerTypeCapabilities(**args)


def unmarshal_ServerTypeNetwork(data: Any) -> ServerTypeNetwork:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerTypeNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("interfaces")
    args["interfaces"] = [
        unmarshal_ServerTypeNetworkInterface(v) for v in data["interfaces"]
    ]

    field = data.get("ipv6_support")
    args["ipv6_support"] = field

    field = data.get("sum_internal_bandwidth")
    args["sum_internal_bandwidth"] = field

    field = data.get("sum_internet_bandwidth")
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

    field = data.get("l_ssd")
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

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    return SnapshotBaseVolume(**args)


def unmarshal_VolumeServer(data: Any) -> VolumeServer:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'VolumeServer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("boot")
    args["boot"] = field

    field = data.get("creation_date")
    args["creation_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("export_uri")
    args["export_uri"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("modification_date")
    args["modification_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("name")
    args["name"] = field

    field = data.get("organization")
    args["organization"] = field

    field = data.get("project")
    args["project"] = field

    field = data.get("server")
    args["server"] = unmarshal_ServerSummary(field) if field is not None else None

    field = data.get("size")
    args["size"] = field

    field = data.get("state")
    args["state"] = field

    field = data.get("volume_type")
    args["volume_type"] = field

    field = data.get("zone")
    args["zone"] = field

    return VolumeServer(**args)


def unmarshal_VolumeTypeCapabilities(data: Any) -> VolumeTypeCapabilities:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'VolumeTypeCapabilities' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshot")
    args["snapshot"] = field

    return VolumeTypeCapabilities(**args)


def unmarshal_VolumeTypeConstraints(data: Any) -> VolumeTypeConstraints:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'VolumeTypeConstraints' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("max")
    args["max"] = field

    field = data.get("min")
    args["min"] = field

    return VolumeTypeConstraints(**args)


def unmarshal_Dashboard(data: Any) -> Dashboard:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Dashboard' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("images_count")
    args["images_count"] = field

    field = data.get("ips_count")
    args["ips_count"] = field

    field = data.get("ips_unused")
    args["ips_unused"] = field

    field = data.get("placement_groups_count")
    args["placement_groups_count"] = field

    field = data.get("private_nics_count")
    args["private_nics_count"] = field

    field = data.get("running_servers_count")
    args["running_servers_count"] = field

    field = data.get("security_groups_count")
    args["security_groups_count"] = field

    field = data.get("servers_by_types")
    args["servers_by_types"] = field

    field = data.get("servers_count")
    args["servers_count"] = field

    field = data.get("snapshots_count")
    args["snapshots_count"] = field

    field = data.get("volumes_b_ssd_count")
    args["volumes_b_ssd_count"] = field

    field = data.get("volumes_b_ssd_total_size")
    args["volumes_b_ssd_total_size"] = field

    field = data.get("volumes_count")
    args["volumes_count"] = field

    field = data.get("volumes_l_ssd_count")
    args["volumes_l_ssd_count"] = field

    field = data.get("volumes_l_ssd_total_size")
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

    field = data.get("availability")
    args["availability"] = field

    return GetServerTypesAvailabilityResponseAvailability(**args)


def unmarshal_Ip(data: Any) -> Ip:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Ip' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("address")
    args["address"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("organization")
    args["organization"] = field

    field = data.get("project")
    args["project"] = field

    field = data.get("reverse")
    args["reverse"] = field

    field = data.get("server")
    args["server"] = unmarshal_ServerSummary(field) if field is not None else None

    field = data.get("tags")
    args["tags"] = field

    field = data.get("zone")
    args["zone"] = field

    return Ip(**args)


def unmarshal_PlacementGroupServer(data: Any) -> PlacementGroupServer:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'PlacementGroupServer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("policy_respected")
    args["policy_respected"] = field

    return PlacementGroupServer(**args)


def unmarshal_SecurityGroup(data: Any) -> SecurityGroup:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SecurityGroup' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("creation_date")
    args["creation_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description")
    args["description"] = field

    field = data.get("enable_default_security")
    args["enable_default_security"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("inbound_default_policy")
    args["inbound_default_policy"] = field

    field = data.get("modification_date")
    args["modification_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("name")
    args["name"] = field

    field = data.get("organization")
    args["organization"] = field

    field = data.get("organization_default")
    args["organization_default"] = field

    field = data.get("outbound_default_policy")
    args["outbound_default_policy"] = field

    field = data.get("project")
    args["project"] = field

    field = data.get("project_default")
    args["project_default"] = field

    field = data.get("servers")
    args["servers"] = [unmarshal_ServerSummary(v) for v in data["servers"]]

    field = data.get("state")
    args["state"] = field

    field = data.get("stateful")
    args["stateful"] = field

    field = data.get("tags")
    args["tags"] = field

    field = data.get("zone")
    args["zone"] = field

    return SecurityGroup(**args)


def unmarshal_SecurityGroupRule(data: Any) -> SecurityGroupRule:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SecurityGroupRule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("action")
    args["action"] = field

    field = data.get("dest_port_from")
    args["dest_port_from"] = field

    field = data.get("dest_port_to")
    args["dest_port_to"] = field

    field = data.get("direction")
    args["direction"] = field

    field = data.get("editable")
    args["editable"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("ip_range")
    args["ip_range"] = field

    field = data.get("position")
    args["position"] = field

    field = data.get("protocol")
    args["protocol"] = field

    field = data.get("zone")
    args["zone"] = field

    return SecurityGroupRule(**args)


def unmarshal_Server(data: Any) -> Server:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Server' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("allowed_actions")
    args["allowed_actions"] = field

    field = data.get("arch")
    args["arch"] = field

    field = data.get("boot_type")
    args["boot_type"] = field

    field = data.get("bootscript")
    args["bootscript"] = unmarshal_Bootscript(field) if field is not None else None

    field = data.get("commercial_type")
    args["commercial_type"] = field

    field = data.get("creation_date")
    args["creation_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("dynamic_ip_required")
    args["dynamic_ip_required"] = field

    field = data.get("enable_ipv6")
    args["enable_ipv6"] = field

    field = data.get("hostname")
    args["hostname"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("image")
    args["image"] = unmarshal_Image(field) if field is not None else None

    field = data.get("ipv6")
    args["ipv6"] = unmarshal_ServerIpv6(field) if field is not None else None

    field = data.get("location")
    args["location"] = unmarshal_ServerLocation(field) if field is not None else None

    field = data.get("maintenances")
    args["maintenances"] = [
        unmarshal_ServerMaintenance(v) for v in data["maintenances"]
    ]

    field = data.get("modification_date")
    args["modification_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("name")
    args["name"] = field

    field = data.get("organization")
    args["organization"] = field

    field = data.get("placement_group")
    args["placement_group"] = (
        unmarshal_PlacementGroup(field) if field is not None else None
    )

    field = data.get("private_ip")
    args["private_ip"] = field

    field = data.get("private_nics")
    args["private_nics"] = [unmarshal_PrivateNIC(v) for v in data["private_nics"]]

    field = data.get("project")
    args["project"] = field

    field = data.get("protected")
    args["protected"] = field

    field = data.get("public_ip")
    args["public_ip"] = unmarshal_ServerIp(field) if field is not None else None

    field = data.get("security_group")
    args["security_group"] = (
        unmarshal_SecurityGroupSummary(field) if field is not None else None
    )

    field = data.get("state")
    args["state"] = field

    field = data.get("state_detail")
    args["state_detail"] = field

    field = data.get("tags")
    args["tags"] = field

    field = data.get("volumes")
    args["volumes"] = {k: unmarshal_VolumeServer(v) for k, v in data["volumes"].items()}

    field = data.get("zone")
    args["zone"] = field

    return Server(**args)


def unmarshal_ServerType(data: Any) -> ServerType:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("alt_names")
    args["alt_names"] = field

    field = data.get("arch")
    args["arch"] = field

    field = data.get("baremetal")
    args["baremetal"] = field

    field = data.get("capabilities")
    args["capabilities"] = (
        unmarshal_ServerTypeCapabilities(field) if field is not None else None
    )

    field = data.get("gpu")
    args["gpu"] = field

    field = data.get("hourly_price")
    args["hourly_price"] = field

    field = data.get("monthly_price")
    args["monthly_price"] = field

    field = data.get("ncpus")
    args["ncpus"] = field

    field = data.get("network")
    args["network"] = unmarshal_ServerTypeNetwork(field) if field is not None else None

    field = data.get("per_volume_constraint")
    args["per_volume_constraint"] = (
        unmarshal_ServerTypeVolumeConstraintsByType(field)
        if field is not None
        else None
    )

    field = data.get("ram")
    args["ram"] = field

    field = data.get("volumes_constraint")
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

    field = data.get("base_volume")
    args["base_volume"] = (
        unmarshal_SnapshotBaseVolume(field) if field is not None else None
    )

    field = data.get("creation_date")
    args["creation_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("error_reason")
    args["error_reason"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("modification_date")
    args["modification_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("name")
    args["name"] = field

    field = data.get("organization")
    args["organization"] = field

    field = data.get("project")
    args["project"] = field

    field = data.get("size")
    args["size"] = field

    field = data.get("state")
    args["state"] = field

    field = data.get("tags")
    args["tags"] = field

    field = data.get("volume_type")
    args["volume_type"] = field

    field = data.get("zone")
    args["zone"] = field

    return Snapshot(**args)


def unmarshal_Task(data: Any) -> Task:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Task' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description")
    args["description"] = field

    field = data.get("href_from")
    args["href_from"] = field

    field = data.get("href_result")
    args["href_result"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("progress")
    args["progress"] = field

    field = data.get("started_at")
    args["started_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("status")
    args["status"] = field

    field = data.get("terminated_at")
    args["terminated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("zone")
    args["zone"] = field

    return Task(**args)


def unmarshal_VolumeType(data: Any) -> VolumeType:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'VolumeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("capabilities")
    args["capabilities"] = (
        unmarshal_VolumeTypeCapabilities(field) if field is not None else None
    )

    field = data.get("constraints")
    args["constraints"] = (
        unmarshal_VolumeTypeConstraints(field) if field is not None else None
    )

    field = data.get("display_name")
    args["display_name"] = field

    return VolumeType(**args)


def unmarshal_CreateImageResponse(data: Any) -> CreateImageResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreateImageResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("image")
    args["image"] = unmarshal_Image(field) if field is not None else None

    return CreateImageResponse(**args)


def unmarshal_CreateIpResponse(data: Any) -> CreateIpResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreateIpResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip")
    args["ip"] = unmarshal_Ip(field) if field is not None else None

    return CreateIpResponse(**args)


def unmarshal_CreatePlacementGroupResponse(data: Any) -> CreatePlacementGroupResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreatePlacementGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("placement_group")
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

    field = data.get("private_nic")
    args["private_nic"] = unmarshal_PrivateNIC(field) if field is not None else None

    return CreatePrivateNICResponse(**args)


def unmarshal_CreateSecurityGroupResponse(data: Any) -> CreateSecurityGroupResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreateSecurityGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("security_group")
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

    field = data.get("rule")
    args["rule"] = unmarshal_SecurityGroupRule(field) if field is not None else None

    return CreateSecurityGroupRuleResponse(**args)


def unmarshal_CreateServerResponse(data: Any) -> CreateServerResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreateServerResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server")
    args["server"] = unmarshal_Server(field) if field is not None else None

    return CreateServerResponse(**args)


def unmarshal_CreateSnapshotResponse(data: Any) -> CreateSnapshotResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreateSnapshotResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshot")
    args["snapshot"] = unmarshal_Snapshot(field) if field is not None else None

    field = data.get("task")
    args["task"] = unmarshal_Task(field) if field is not None else None

    return CreateSnapshotResponse(**args)


def unmarshal_CreateVolumeResponse(data: Any) -> CreateVolumeResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreateVolumeResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("volume")
    args["volume"] = unmarshal_Volume(field) if field is not None else None

    return CreateVolumeResponse(**args)


def unmarshal_ExportSnapshotResponse(data: Any) -> ExportSnapshotResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ExportSnapshotResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("task")
    args["task"] = unmarshal_Task(field) if field is not None else None

    return ExportSnapshotResponse(**args)


def unmarshal_GetBootscriptResponse(data: Any) -> GetBootscriptResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetBootscriptResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("bootscript")
    args["bootscript"] = unmarshal_Bootscript(field) if field is not None else None

    return GetBootscriptResponse(**args)


def unmarshal_GetDashboardResponse(data: Any) -> GetDashboardResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetDashboardResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dashboard")
    args["dashboard"] = unmarshal_Dashboard(field) if field is not None else None

    return GetDashboardResponse(**args)


def unmarshal_GetImageResponse(data: Any) -> GetImageResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetImageResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("image")
    args["image"] = unmarshal_Image(field) if field is not None else None

    return GetImageResponse(**args)


def unmarshal_GetIpResponse(data: Any) -> GetIpResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetIpResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip")
    args["ip"] = unmarshal_Ip(field) if field is not None else None

    return GetIpResponse(**args)


def unmarshal_GetPlacementGroupResponse(data: Any) -> GetPlacementGroupResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetPlacementGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("placement_group")
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

    field = data.get("servers")
    args["servers"] = [unmarshal_PlacementGroupServer(v) for v in data["servers"]]

    return GetPlacementGroupServersResponse(**args)


def unmarshal_GetPrivateNICResponse(data: Any) -> GetPrivateNICResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetPrivateNICResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_nic")
    args["private_nic"] = unmarshal_PrivateNIC(field) if field is not None else None

    return GetPrivateNICResponse(**args)


def unmarshal_GetSecurityGroupResponse(data: Any) -> GetSecurityGroupResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetSecurityGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("security_group")
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

    field = data.get("rule")
    args["rule"] = unmarshal_SecurityGroupRule(field) if field is not None else None

    return GetSecurityGroupRuleResponse(**args)


def unmarshal_GetServerResponse(data: Any) -> GetServerResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetServerResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server")
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

    field = data.get("servers")
    args["servers"] = {
        k: unmarshal_GetServerTypesAvailabilityResponseAvailability(v)
        for k, v in data["servers"].items()
    }

    return GetServerTypesAvailabilityResponse(**args)


def unmarshal_GetSnapshotResponse(data: Any) -> GetSnapshotResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetSnapshotResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshot")
    args["snapshot"] = unmarshal_Snapshot(field) if field is not None else None

    return GetSnapshotResponse(**args)


def unmarshal_GetVolumeResponse(data: Any) -> GetVolumeResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetVolumeResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("volume")
    args["volume"] = unmarshal_Volume(field) if field is not None else None

    return GetVolumeResponse(**args)


def unmarshal_ListBootscriptsResponse(data: Any) -> ListBootscriptsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListBootscriptsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("bootscripts")
    args["bootscripts"] = [unmarshal_Bootscript(v) for v in data["bootscripts"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListBootscriptsResponse(**args)


def unmarshal_ListImagesResponse(data: Any) -> ListImagesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListImagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("images")
    args["images"] = [unmarshal_Image(v) for v in data["images"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListImagesResponse(**args)


def unmarshal_ListIpsResponse(data: Any) -> ListIpsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListIpsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ips")
    args["ips"] = [unmarshal_Ip(v) for v in data["ips"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListIpsResponse(**args)


def unmarshal_ListPlacementGroupsResponse(data: Any) -> ListPlacementGroupsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListPlacementGroupsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("placement_groups")
    args["placement_groups"] = [
        unmarshal_PlacementGroup(v) for v in data["placement_groups"]
    ]

    field = data.get("total_count")
    args["total_count"] = field

    return ListPlacementGroupsResponse(**args)


def unmarshal_ListPrivateNICsResponse(data: Any) -> ListPrivateNICsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListPrivateNICsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_nics")
    args["private_nics"] = [unmarshal_PrivateNIC(v) for v in data["private_nics"]]

    return ListPrivateNICsResponse(**args)


def unmarshal_ListSecurityGroupRulesResponse(
    data: Any,
) -> ListSecurityGroupRulesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListSecurityGroupRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules")
    args["rules"] = [unmarshal_SecurityGroupRule(v) for v in data["rules"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListSecurityGroupRulesResponse(**args)


def unmarshal_ListSecurityGroupsResponse(data: Any) -> ListSecurityGroupsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListSecurityGroupsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("security_groups")
    args["security_groups"] = [
        unmarshal_SecurityGroup(v) for v in data["security_groups"]
    ]

    field = data.get("total_count")
    args["total_count"] = field

    return ListSecurityGroupsResponse(**args)


def unmarshal_ListServerActionsResponse(data: Any) -> ListServerActionsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListServerActionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("actions")
    args["actions"] = field

    return ListServerActionsResponse(**args)


def unmarshal_ListServerUserDataResponse(data: Any) -> ListServerUserDataResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListServerUserDataResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("user_data")
    args["user_data"] = field

    return ListServerUserDataResponse(**args)


def unmarshal_ListServersResponse(data: Any) -> ListServersResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListServersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("servers")
    args["servers"] = [unmarshal_Server(v) for v in data["servers"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListServersResponse(**args)


def unmarshal_ListServersTypesResponse(data: Any) -> ListServersTypesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListServersTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("servers")
    args["servers"] = {k: unmarshal_ServerType(v) for k, v in data["servers"].items()}

    field = data.get("total_count")
    args["total_count"] = field

    return ListServersTypesResponse(**args)


def unmarshal_ListSnapshotsResponse(data: Any) -> ListSnapshotsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListSnapshotsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshots")
    args["snapshots"] = [unmarshal_Snapshot(v) for v in data["snapshots"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListSnapshotsResponse(**args)


def unmarshal_ListVolumesResponse(data: Any) -> ListVolumesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListVolumesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count")
    args["total_count"] = field

    field = data.get("volumes")
    args["volumes"] = [unmarshal_Volume(v) for v in data["volumes"]]

    return ListVolumesResponse(**args)


def unmarshal_ListVolumesTypesResponse(data: Any) -> ListVolumesTypesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListVolumesTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count")
    args["total_count"] = field

    field = data.get("volumes")
    args["volumes"] = {k: unmarshal_VolumeType(v) for k, v in data["volumes"].items()}

    return ListVolumesTypesResponse(**args)


def unmarshal_ServerActionResponse(data: Any) -> ServerActionResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ServerActionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("task")
    args["task"] = unmarshal_Task(field) if field is not None else None

    return ServerActionResponse(**args)


def unmarshal_SetPlacementGroupResponse(data: Any) -> SetPlacementGroupResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SetPlacementGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("placement_group")
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

    field = data.get("servers")
    args["servers"] = [unmarshal_PlacementGroupServer(v) for v in data["servers"]]

    return SetPlacementGroupServersResponse(**args)


def unmarshal_SetSecurityGroupRulesResponse(data: Any) -> SetSecurityGroupRulesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SetSecurityGroupRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules")
    args["rules"] = [unmarshal_SecurityGroupRule(v) for v in data["rules"]]

    return SetSecurityGroupRulesResponse(**args)


def unmarshal_UpdateIpResponse(data: Any) -> UpdateIpResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'UpdateIpResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip")
    args["ip"] = unmarshal_Ip(field) if field is not None else None

    return UpdateIpResponse(**args)


def unmarshal_UpdatePlacementGroupResponse(data: Any) -> UpdatePlacementGroupResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'UpdatePlacementGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("placement_group")
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

    field = data.get("servers")
    args["servers"] = [unmarshal_PlacementGroupServer(v) for v in data["servers"]]

    return UpdatePlacementGroupServersResponse(**args)


def unmarshal_UpdateServerResponse(data: Any) -> UpdateServerResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'UpdateServerResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server")
    args["server"] = unmarshal_Server(field) if field is not None else None

    return UpdateServerResponse(**args)


def unmarshal_UpdateVolumeResponse(data: Any) -> UpdateVolumeResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'UpdateVolumeResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("volume")
    args["volume"] = unmarshal_Volume(field) if field is not None else None

    return UpdateVolumeResponse(**args)


def unmarshal__SetImageResponse(data: Any) -> _SetImageResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type '_SetImageResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("image")
    args["image"] = unmarshal_Image(field) if field is not None else None

    return _SetImageResponse(**args)


def unmarshal__SetSecurityGroupResponse(data: Any) -> _SetSecurityGroupResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type '_SetSecurityGroupResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("security_group")
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

    field = data.get("rule")
    args["rule"] = unmarshal_SecurityGroupRule(field) if field is not None else None

    return _SetSecurityGroupRuleResponse(**args)


def unmarshal__SetServerResponse(data: Any) -> _SetServerResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type '_SetServerResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("server")
    args["server"] = unmarshal_Server(field) if field is not None else None

    return _SetServerResponse(**args)


def unmarshal__SetSnapshotResponse(data: Any) -> _SetSnapshotResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type '_SetSnapshotResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshot")
    args["snapshot"] = unmarshal_Snapshot(field) if field is not None else None

    return _SetSnapshotResponse(**args)


def marshal_ServerSummary(
    request: ServerSummary,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "id": request.id,
        "name": request.name,
    }


def marshal_Bootscript(
    request: Bootscript,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "arch": Arch(request.arch),
        "bootcmdargs": request.bootcmdargs,
        "default": request.default,
        "dtb": request.dtb,
        "id": request.id,
        "initrd": request.initrd,
        "kernel": request.kernel,
        "organization": request.organization,
        "project": request.project,
        "public": request.public,
        "title": request.title,
        "zone": request.zone,
    }


def marshal_Volume(
    request: Volume,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "creation_date": request.creation_date,
        "export_uri": request.export_uri,
        "id": request.id,
        "modification_date": request.modification_date,
        "name": request.name,
        "organization": request.organization,
        "project": request.project,
        "server": marshal_ServerSummary(request.server, defaults)
        if request.server is not None
        else None,
        "size": request.size,
        "state": VolumeState(request.state),
        "tags": request.tags,
        "volume_type": VolumeVolumeType(request.volume_type),
        "zone": request.zone,
    }


def marshal_VolumeSummary(
    request: VolumeSummary,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "id": request.id,
        "name": request.name,
        "size": request.size,
        "volume_type": VolumeVolumeType(request.volume_type),
    }


def marshal_Image(
    request: Image,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "arch": Arch(request.arch),
        "creation_date": request.creation_date,
        "default_bootscript": marshal_Bootscript(request.default_bootscript, defaults)
        if request.default_bootscript is not None
        else None,
        "extra_volumes": {
            k: marshal_Volume(v, defaults) for k, v in request.extra_volumes.items()
        },
        "from_server": request.from_server,
        "id": request.id,
        "modification_date": request.modification_date,
        "name": request.name,
        "organization": request.organization,
        "project": request.project,
        "public": request.public,
        "root_volume": marshal_VolumeSummary(request.root_volume, defaults)
        if request.root_volume is not None
        else None,
        "state": ImageState(request.state),
        "tags": request.tags,
        "zone": request.zone,
    }


def marshal_PlacementGroup(
    request: PlacementGroup,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "id": request.id,
        "name": request.name,
        "organization": request.organization,
        "policy_mode": PlacementGroupPolicyMode(request.policy_mode),
        "policy_respected": request.policy_respected,
        "policy_type": PlacementGroupPolicyType(request.policy_type),
        "project": request.project,
        "tags": request.tags,
        "zone": request.zone,
    }


def marshal_PrivateNIC(
    request: PrivateNIC,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "id": request.id,
        "mac_address": request.mac_address,
        "private_network_id": request.private_network_id,
        "server_id": request.server_id,
        "state": PrivateNICState(request.state),
    }


def marshal_SecurityGroupSummary(
    request: SecurityGroupSummary,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "id": request.id,
        "name": request.name,
    }


def marshal_SecurityGroupTemplate(
    request: SecurityGroupTemplate,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "id": request.id,
        "name": request.name,
    }


def marshal_ServerActionRequestVolumeBackupTemplate(
    request: ServerActionRequestVolumeBackupTemplate,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "volume_type": SnapshotVolumeType(request.volume_type),
    }


def marshal_ServerIp(
    request: ServerIp,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "address": request.address,
        "dynamic": request.dynamic,
        "id": request.id,
    }


def marshal_ServerIpv6(
    request: ServerIpv6,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "address": request.address,
        "gateway": request.gateway,
        "netmask": request.netmask,
    }


def marshal_ServerLocation(
    request: ServerLocation,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "cluster_id": request.cluster_id,
        "hypervisor_id": request.hypervisor_id,
        "node_id": request.node_id,
        "platform_id": request.platform_id,
        "zone_id": request.zone_id,
    }


def marshal_ServerMaintenance(
    request: ServerMaintenance,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "reason": request.reason,
    }


def marshal_SetSecurityGroupRulesRequestRule(
    request: SetSecurityGroupRulesRequestRule,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "action": SecurityGroupRuleAction(request.action),
        "dest_port_from": request.dest_port_from,
        "dest_port_to": request.dest_port_to,
        "direction": SecurityGroupRuleDirection(request.direction),
        "editable": request.editable,
        "id": request.id,
        "ip_range": request.ip_range,
        "position": request.position,
        "protocol": SecurityGroupRuleProtocol(request.protocol),
        "zone": request.zone,
    }


def marshal_SnapshotBaseVolume(
    request: SnapshotBaseVolume,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "id": request.id,
        "name": request.name,
    }


def marshal_VolumeServerTemplate(
    request: VolumeServerTemplate,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "base_snapshot": request.base_snapshot,
        "boot": request.boot,
        "id": request.id,
        "name": request.name,
        "organization": request.organization,
        "project": request.project,
        "size": request.size,
        "volume_type": VolumeVolumeType(request.volume_type),
    }


def marshal_VolumeTemplate(
    request: VolumeTemplate,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "project", request.project, defaults.default_project_id
                ),
                OneOfPossibility(
                    "organization",
                    request.organization,
                    defaults.default_organization_id,
                ),
            ]
        ),
        "id": request.id,
        "name": request.name,
        "size": request.size,
        "volume_type": VolumeVolumeType(request.volume_type),
    }


def marshal_CreateImageRequest(
    request: CreateImageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "project", request.project, defaults.default_project_id
                ),
                OneOfPossibility(
                    "organization",
                    request.organization,
                    defaults.default_organization_id,
                ),
            ]
        ),
        "arch": Arch(request.arch) if request.arch is not None else None,
        "default_bootscript": request.default_bootscript,
        "extra_volumes": {
            k: marshal_VolumeTemplate(v, defaults)
            for k, v in request.extra_volumes.items()
        }
        if request.extra_volumes is not None
        else None,
        "name": request.name,
        "public": request.public,
        "root_volume": request.root_volume,
        "tags": request.tags,
    }


def marshal_CreateIpRequest(
    request: CreateIpRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "project", request.project, defaults.default_project_id
                ),
                OneOfPossibility(
                    "organization",
                    request.organization,
                    defaults.default_organization_id,
                ),
            ]
        ),
        "server": request.server,
        "tags": request.tags,
    }


def marshal_CreatePlacementGroupRequest(
    request: CreatePlacementGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "project", request.project, defaults.default_project_id
                ),
                OneOfPossibility(
                    "organization",
                    request.organization,
                    defaults.default_organization_id,
                ),
            ]
        ),
        "name": request.name,
        "policy_mode": PlacementGroupPolicyMode(request.policy_mode),
        "policy_type": PlacementGroupPolicyType(request.policy_type),
        "tags": request.tags,
    }


def marshal_CreatePrivateNICRequest(
    request: CreatePrivateNICRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "private_network_id": request.private_network_id,
    }


def marshal_CreateSecurityGroupRequest(
    request: CreateSecurityGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("organization_default", request.organization_default),
                OneOfPossibility("project_default", request.project_default),
            ]
        ),
        **resolve_one_of(
            [
                OneOfPossibility(
                    "project", request.project, defaults.default_project_id
                ),
                OneOfPossibility(
                    "organization",
                    request.organization,
                    defaults.default_organization_id,
                ),
            ]
        ),
        "description": request.description,
        "enable_default_security": request.enable_default_security,
        "inbound_default_policy": SecurityGroupPolicy(request.inbound_default_policy),
        "name": request.name,
        "outbound_default_policy": SecurityGroupPolicy(request.outbound_default_policy),
        "stateful": request.stateful,
        "tags": request.tags,
    }


def marshal_CreateSecurityGroupRuleRequest(
    request: CreateSecurityGroupRuleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "action": SecurityGroupRuleAction(request.action)
        if request.action is not None
        else None,
        "dest_port_from": request.dest_port_from,
        "dest_port_to": request.dest_port_to,
        "direction": SecurityGroupRuleDirection(request.direction)
        if request.direction is not None
        else None,
        "editable": request.editable,
        "ip_range": request.ip_range,
        "position": request.position,
        "protocol": SecurityGroupRuleProtocol(request.protocol)
        if request.protocol is not None
        else None,
    }


def marshal_CreateSnapshotRequest(
    request: CreateSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "project", request.project, defaults.default_project_id
                ),
                OneOfPossibility(
                    "organization",
                    request.organization,
                    defaults.default_organization_id,
                ),
            ]
        ),
        "bucket": request.bucket,
        "key": request.key,
        "name": request.name,
        "size": request.size,
        "tags": request.tags,
        "volume_id": request.volume_id,
        "volume_type": SnapshotVolumeType(request.volume_type),
    }


def marshal_CreateVolumeRequest(
    request: CreateVolumeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "project", request.project, defaults.default_project_id
                ),
                OneOfPossibility(
                    "organization",
                    request.organization,
                    defaults.default_organization_id,
                ),
            ]
        ),
        **resolve_one_of(
            [
                OneOfPossibility("size", request.size),
                OneOfPossibility("base_volume", request.base_volume),
                OneOfPossibility("base_snapshot", request.base_snapshot),
            ]
        ),
        "name": request.name,
        "tags": request.tags,
        "volume_type": VolumeVolumeType(request.volume_type),
    }


def marshal_ExportSnapshotRequest(
    request: ExportSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "bucket": request.bucket,
        "key": request.key,
    }


def marshal_ServerActionRequest(
    request: ServerActionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "action": ServerAction(request.action),
        "name": request.name,
        "volumes": {
            k: marshal_ServerActionRequestVolumeBackupTemplate(v, defaults)
            for k, v in request.volumes.items()
        }
        if request.volumes is not None
        else None,
    }


def marshal_SetPlacementGroupRequest(
    request: SetPlacementGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name": request.name,
        "organization": request.organization or defaults.default_organization_id,
        "policy_mode": PlacementGroupPolicyMode(request.policy_mode),
        "policy_type": PlacementGroupPolicyType(request.policy_type),
        "project": request.project or defaults.default_project_id,
        "tags": request.tags,
    }


def marshal_SetPlacementGroupServersRequest(
    request: SetPlacementGroupServersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "servers": request.servers,
    }


def marshal_SetSecurityGroupRulesRequest(
    request: SetSecurityGroupRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "rules": [
            marshal_SetSecurityGroupRulesRequestRule(v, defaults) for v in request.rules
        ]
        if request.rules is not None
        else None,
    }


def marshal_UpdateIpRequest(
    request: UpdateIpRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "reverse": request.reverse,
        "server": request.server,
        "tags": request.tags,
    }


def marshal_UpdatePlacementGroupRequest(
    request: UpdatePlacementGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name": request.name,
        "policy_mode": PlacementGroupPolicyMode(request.policy_mode)
        if request.policy_mode is not None
        else None,
        "policy_type": PlacementGroupPolicyType(request.policy_type)
        if request.policy_type is not None
        else None,
        "tags": request.tags,
    }


def marshal_UpdatePlacementGroupServersRequest(
    request: UpdatePlacementGroupServersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "servers": request.servers,
    }


def marshal_UpdateVolumeRequest(
    request: UpdateVolumeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name": request.name,
        "size": request.size,
        "tags": request.tags,
    }


def marshal__CreateServerRequest(
    request: _CreateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "project", request.project, defaults.default_project_id
                ),
                OneOfPossibility(
                    "organization",
                    request.organization,
                    defaults.default_organization_id,
                ),
            ]
        ),
        "boot_type": BootType(request.boot_type)
        if request.boot_type is not None
        else None,
        "bootscript": request.bootscript,
        "commercial_type": request.commercial_type,
        "dynamic_ip_required": request.dynamic_ip_required,
        "enable_ipv6": request.enable_ipv6,
        "image": request.image,
        "name": request.name,
        "placement_group": request.placement_group,
        "public_ip": request.public_ip,
        "security_group": request.security_group,
        "tags": request.tags,
        "volumes": {
            k: marshal_VolumeServerTemplate(v, defaults)
            for k, v in request.volumes.items()
        }
        if request.volumes is not None
        else None,
    }


def marshal__SetImageRequest(
    request: _SetImageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "arch": Arch(request.arch),
        "creation_date": request.creation_date,
        "default_bootscript": marshal_Bootscript(request.default_bootscript, defaults)
        if request.default_bootscript is not None
        else None,
        "extra_volumes": {
            k: marshal_Volume(v, defaults) for k, v in request.extra_volumes.items()
        }
        if request.extra_volumes is not None
        else None,
        "from_server": request.from_server,
        "modification_date": request.modification_date,
        "name": request.name,
        "organization": request.organization or defaults.default_organization_id,
        "project": request.project or defaults.default_project_id,
        "public": request.public,
        "root_volume": marshal_VolumeSummary(request.root_volume, defaults)
        if request.root_volume is not None
        else None,
        "state": ImageState(request.state),
        "tags": request.tags,
    }


def marshal__SetSecurityGroupRequest(
    request: _SetSecurityGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "creation_date": request.creation_date,
        "description": request.description,
        "enable_default_security": request.enable_default_security,
        "inbound_default_policy": SecurityGroupPolicy(request.inbound_default_policy),
        "modification_date": request.modification_date,
        "name": request.name,
        "organization": request.organization or defaults.default_organization_id,
        "organization_default": request.organization_default,
        "outbound_default_policy": SecurityGroupPolicy(request.outbound_default_policy),
        "project": request.project or defaults.default_project_id,
        "project_default": request.project_default,
        "servers": [marshal_ServerSummary(v, defaults) for v in request.servers]
        if request.servers is not None
        else None,
        "stateful": request.stateful,
        "tags": request.tags,
    }


def marshal__SetSecurityGroupRuleRequest(
    request: _SetSecurityGroupRuleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "action": SecurityGroupRuleAction(request.action),
        "dest_port_from": request.dest_port_from,
        "dest_port_to": request.dest_port_to,
        "direction": SecurityGroupRuleDirection(request.direction),
        "editable": request.editable,
        "id": request.id,
        "ip_range": request.ip_range,
        "position": request.position,
        "protocol": SecurityGroupRuleProtocol(request.protocol),
    }


def marshal__SetServerRequest(
    request: _SetServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "allowed_actions": [ServerAction(v) for v in request.allowed_actions]
        if request.allowed_actions is not None
        else None,
        "arch": Arch(request.arch),
        "boot_type": BootType(request.boot_type),
        "bootscript": marshal_Bootscript(request.bootscript, defaults)
        if request.bootscript is not None
        else None,
        "commercial_type": request.commercial_type,
        "creation_date": request.creation_date,
        "dynamic_ip_required": request.dynamic_ip_required,
        "enable_ipv6": request.enable_ipv6,
        "hostname": request.hostname,
        "image": marshal_Image(request.image, defaults)
        if request.image is not None
        else None,
        "ipv6": marshal_ServerIpv6(request.ipv6, defaults)
        if request.ipv6 is not None
        else None,
        "location": marshal_ServerLocation(request.location, defaults)
        if request.location is not None
        else None,
        "maintenances": [
            marshal_ServerMaintenance(v, defaults) for v in request.maintenances
        ]
        if request.maintenances is not None
        else None,
        "modification_date": request.modification_date,
        "name": request.name,
        "organization": request.organization or defaults.default_organization_id,
        "placement_group": marshal_PlacementGroup(request.placement_group, defaults)
        if request.placement_group is not None
        else None,
        "private_ip": request.private_ip,
        "private_nics": [marshal_PrivateNIC(v, defaults) for v in request.private_nics]
        if request.private_nics is not None
        else None,
        "project": request.project or defaults.default_project_id,
        "protected": request.protected,
        "public_ip": marshal_ServerIp(request.public_ip, defaults)
        if request.public_ip is not None
        else None,
        "security_group": marshal_SecurityGroupSummary(request.security_group, defaults)
        if request.security_group is not None
        else None,
        "state": ServerState(request.state),
        "state_detail": request.state_detail,
        "tags": request.tags,
        "volumes": {k: marshal_Volume(v, defaults) for k, v in request.volumes.items()}
        if request.volumes is not None
        else None,
    }


def marshal__SetSnapshotRequest(
    request: _SetSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "base_volume": marshal_SnapshotBaseVolume(request.base_volume, defaults)
        if request.base_volume is not None
        else None,
        "creation_date": request.creation_date,
        "id": request.id,
        "modification_date": request.modification_date,
        "name": request.name,
        "organization": request.organization or defaults.default_organization_id,
        "project": request.project or defaults.default_project_id,
        "size": request.size,
        "state": SnapshotState(request.state),
        "tags": request.tags,
        "volume_type": VolumeVolumeType(request.volume_type),
    }


def marshal__UpdateServerRequest(
    request: _UpdateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "boot_type": BootType(request.boot_type)
        if request.boot_type is not None
        else None,
        "bootscript": request.bootscript,
        "dynamic_ip_required": request.dynamic_ip_required,
        "enable_ipv6": request.enable_ipv6,
        "name": request.name,
        "placement_group": request.placement_group,
        "private_nics": [marshal_PrivateNIC(v, defaults) for v in request.private_nics]
        if request.private_nics is not None
        else None,
        "protected": request.protected,
        "security_group": marshal_SecurityGroupTemplate(
            request.security_group, defaults
        )
        if request.security_group is not None
        else None,
        "tags": request.tags,
        "volumes": {
            k: marshal_VolumeServerTemplate(v, defaults)
            for k, v in request.volumes.items()
        }
        if request.volumes is not None
        else None,
    }
