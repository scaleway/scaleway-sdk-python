# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    SecurityGroupRulePortRange,
    SecurityGroupRule,
    SecurityGroup,
    PlacementGroup,
    PrivateNetworkInterface,
    AddSecurityGroupRulesResponse,
    ListPlacementGroupsResponse,
    ListPrivateNetworkInterfacesResponse,
    SecurityGroupSummary,
    ListSecurityGroupsResponse,
    ServerTypeGpuInfo,
    ServerTypeLimits,
    ServerType,
    ListServerTypesResponse,
    ServerSummary,
    ListServersResponse,
    ListTemplateUserDataKeysResponse,
    TemplateSummary,
    ListTemplatesResponse,
    ListUserDataKeysResponse,
    ResourceCounts,
    ServerIP,
    ServerFilesystem,
    ServerPrivateNetworkInterface,
    ServerPublicNetworkInterface,
    ServerRDPPassword,
    ServerVolume,
    Server,
    CreateTemplateRequestVolumeTemplate,
    Template,
    UserData,
    SecurityGroupRuleConfig,
    AddSecurityGroupRulesRequest,
    AttachServerFileSystemRequest,
    AttachServerIPRequest,
    AttachServerPrivateNetworkInterfaceRequest,
    AttachServerVolumeRequest,
    CreatePlacementGroupRequest,
    CreatePrivateNetworkInterfaceRequest,
    CreateSecurityGroupRequest,
    CreateServerFromTemplateRequest,
    CreateServerRequestBookIP,
    CreateServerRequestServerIP,
    CreateServerRequestCreateVolume,
    CreateServerRequestPublicNetworkInterface,
    CreateServerRequestServerVolume,
    CreateServerRequest,
    CreateTemplateRequest,
    DeleteSecurityGroupRulesRequest,
    DetachServerFileSystemRequest,
    DetachServerIPRequest,
    DetachServerPrivateNetworkInterfaceRequest,
    DetachServerVolumeRequest,
    SetSecurityGroupRulesRequest,
    SetServerCloudInitRequest,
    SetServerDefaultIPRequest,
    SetTemplateCloudInitRequest,
    SetTemplateUserDataRequest,
    SetUserDataRequest,
    StopAndDeleteServerRequest,
    UpdatePlacementGroupRequest,
    UpdatePrivateNetworkInterfaceRequest,
    UpdateSecurityGroupRequest,
    UpdateSecurityGroupRuleRequest,
    UpdateServerRequestPublicNetworkInterface,
    UpdateServerRequest,
    UpdateTemplateRequestUpdateVolumes,
    UpdateTemplateRequest,
)


def unmarshal_SecurityGroupRulePortRange(data: Any) -> SecurityGroupRulePortRange:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecurityGroupRulePortRange' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("start", None)
    if field is not None:
        args["start"] = field
    else:
        args["start"] = None

    field = data.get("end", None)
    if field is not None:
        args["end"] = field
    else:
        args["end"] = None

    return SecurityGroupRulePortRange(**args)


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

    field = data.get("source_ip_range", None)
    if field is not None:
        args["source_ip_range"] = field
    else:
        args["source_ip_range"] = None

    field = data.get("destination_ip_range", None)
    if field is not None:
        args["destination_ip_range"] = field
    else:
        args["destination_ip_range"] = None

    field = data.get("position", None)
    if field is not None:
        args["position"] = field
    else:
        args["position"] = None

    field = data.get("source_ports", None)
    if field is not None:
        args["source_ports"] = unmarshal_SecurityGroupRulePortRange(field)
    else:
        args["source_ports"] = None

    field = data.get("destination_ports", None)
    if field is not None:
        args["destination_ports"] = unmarshal_SecurityGroupRulePortRange(field)
    else:
        args["destination_ports"] = None

    return SecurityGroupRule(**args)


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

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = None

    field = data.get("disable_default_rules", None)
    if field is not None:
        args["disable_default_rules"] = field
    else:
        args["disable_default_rules"] = None

    field = data.get("project_default", None)
    if field is not None:
        args["project_default"] = field
    else:
        args["project_default"] = None

    field = data.get("inbound_default_action", None)
    if field is not None:
        args["inbound_default_action"] = field
    else:
        args["inbound_default_action"] = None

    field = data.get("outbound_default_action", None)
    if field is not None:
        args["outbound_default_action"] = field
    else:
        args["outbound_default_action"] = None

    field = data.get("stateless", None)
    if field is not None:
        args["stateless"] = field
    else:
        args["stateless"] = None

    field = data.get("default_rules", None)
    if field is not None:
        args["default_rules"] = (
            [unmarshal_SecurityGroupRule(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["default_rules"] = None

    field = data.get("rules", None)
    if field is not None:
        args["rules"] = (
            [unmarshal_SecurityGroupRule(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["rules"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return SecurityGroup(**args)


def unmarshal_PlacementGroup(data: Any) -> PlacementGroup:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlacementGroup' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("policy_type", None)
    if field is not None:
        args["policy_type"] = field
    else:
        args["policy_type"] = None

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

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return PlacementGroup(**args)


def unmarshal_PrivateNetworkInterface(data: Any) -> PrivateNetworkInterface:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetworkInterface' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field
    else:
        args["private_network_id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("server_id", None)
    if field is not None:
        args["server_id"] = field
    else:
        args["server_id"] = None

    field = data.get("security_group_id", None)
    if field is not None:
        args["security_group_id"] = field
    else:
        args["security_group_id"] = None

    field = data.get("mac_address", None)
    if field is not None:
        args["mac_address"] = field
    else:
        args["mac_address"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = None

    field = data.get("ip_ids", None)
    if field is not None:
        args["ip_ids"] = field
    else:
        args["ip_ids"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return PrivateNetworkInterface(**args)


def unmarshal_AddSecurityGroupRulesResponse(data: Any) -> AddSecurityGroupRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddSecurityGroupRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("added_rules", None)
    if field is not None:
        args["added_rules"] = (
            [unmarshal_SecurityGroupRule(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["added_rules"] = None

    field = data.get("security_group", None)
    if field is not None:
        args["security_group"] = unmarshal_SecurityGroup(field)
    else:
        args["security_group"] = None

    return AddSecurityGroupRulesResponse(**args)


def unmarshal_ListPlacementGroupsResponse(data: Any) -> ListPlacementGroupsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPlacementGroupsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("placement_groups", None)
    if field is not None:
        args["placement_groups"] = (
            [unmarshal_PlacementGroup(v) for v in field] if field is not None else None
        )
    else:
        args["placement_groups"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("next_page_token", None)
    if field is not None:
        args["next_page_token"] = field
    else:
        args["next_page_token"] = None

    return ListPlacementGroupsResponse(**args)


def unmarshal_ListPrivateNetworkInterfacesResponse(
    data: Any,
) -> ListPrivateNetworkInterfacesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPrivateNetworkInterfacesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("private_network_interfaces", None)
    if field is not None:
        args["private_network_interfaces"] = (
            [unmarshal_PrivateNetworkInterface(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["private_network_interfaces"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("next_page_token", None)
    if field is not None:
        args["next_page_token"] = field
    else:
        args["next_page_token"] = None

    return ListPrivateNetworkInterfacesResponse(**args)


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

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = None

    field = data.get("disable_default_rules", None)
    if field is not None:
        args["disable_default_rules"] = field
    else:
        args["disable_default_rules"] = None

    field = data.get("project_default", None)
    if field is not None:
        args["project_default"] = field
    else:
        args["project_default"] = None

    field = data.get("inbound_default_action", None)
    if field is not None:
        args["inbound_default_action"] = field
    else:
        args["inbound_default_action"] = None

    field = data.get("outbound_default_action", None)
    if field is not None:
        args["outbound_default_action"] = field
    else:
        args["outbound_default_action"] = None

    field = data.get("stateless", None)
    if field is not None:
        args["stateless"] = field
    else:
        args["stateless"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return SecurityGroupSummary(**args)


def unmarshal_ListSecurityGroupsResponse(data: Any) -> ListSecurityGroupsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSecurityGroupsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("security_groups", None)
    if field is not None:
        args["security_groups"] = (
            [unmarshal_SecurityGroupSummary(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["security_groups"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("next_page_token", None)
    if field is not None:
        args["next_page_token"] = field
    else:
        args["next_page_token"] = None

    return ListSecurityGroupsResponse(**args)


def unmarshal_ServerTypeGpuInfo(data: Any) -> ServerTypeGpuInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeGpuInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("manufacturer", None)
    if field is not None:
        args["manufacturer"] = field
    else:
        args["manufacturer"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("memory", None)
    if field is not None:
        args["memory"] = field
    else:
        args["memory"] = None

    return ServerTypeGpuInfo(**args)


def unmarshal_ServerTypeLimits(data: Any) -> ServerTypeLimits:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeLimits' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("private_network_count", None)
    if field is not None:
        args["private_network_count"] = field
    else:
        args["private_network_count"] = None

    field = data.get("file_system_count", None)
    if field is not None:
        args["file_system_count"] = field
    else:
        args["file_system_count"] = None

    field = data.get("private_network_bandwidth", None)
    if field is not None:
        args["private_network_bandwidth"] = field
    else:
        args["private_network_bandwidth"] = None

    field = data.get("block_bandwidth", None)
    if field is not None:
        args["block_bandwidth"] = field
    else:
        args["block_bandwidth"] = None

    field = data.get("internet_bandwidth", None)
    if field is not None:
        args["internet_bandwidth"] = field
    else:
        args["internet_bandwidth"] = None

    field = data.get("l_ssd_size", None)
    if field is not None:
        args["l_ssd_size"] = field
    else:
        args["l_ssd_size"] = None

    field = data.get("scratch_size", None)
    if field is not None:
        args["scratch_size"] = field
    else:
        args["scratch_size"] = None

    field = data.get("ip_count", None)
    if field is not None:
        args["ip_count"] = field
    else:
        args["ip_count"] = None

    field = data.get("volume_count", None)
    if field is not None:
        args["volume_count"] = field
    else:
        args["volume_count"] = None

    field = data.get("scratch_volumes_count", None)
    if field is not None:
        args["scratch_volumes_count"] = field
    else:
        args["scratch_volumes_count"] = None

    return ServerTypeLimits(**args)


def unmarshal_ServerType(data: Any) -> ServerType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerType' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("vcpu_count", None)
    if field is not None:
        args["vcpu_count"] = field
    else:
        args["vcpu_count"] = None

    field = data.get("gpu_count", None)
    if field is not None:
        args["gpu_count"] = field
    else:
        args["gpu_count"] = None

    field = data.get("memory", None)
    if field is not None:
        args["memory"] = field
    else:
        args["memory"] = None

    field = data.get("architecture", None)
    if field is not None:
        args["architecture"] = field
    else:
        args["architecture"] = None

    field = data.get("availability", None)
    if field is not None:
        args["availability"] = field
    else:
        args["availability"] = None

    field = data.get("end_of_service", None)
    if field is not None:
        args["end_of_service"] = field
    else:
        args["end_of_service"] = None

    field = data.get("limits", None)
    if field is not None:
        args["limits"] = unmarshal_ServerTypeLimits(field)
    else:
        args["limits"] = None

    field = data.get("gpu_info", None)
    if field is not None:
        args["gpu_info"] = unmarshal_ServerTypeGpuInfo(field)
    else:
        args["gpu_info"] = None

    return ServerType(**args)


def unmarshal_ListServerTypesResponse(data: Any) -> ListServerTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServerTypesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("server_types", None)
    if field is not None:
        args["server_types"] = (
            [unmarshal_ServerType(v) for v in field] if field is not None else None
        )
    else:
        args["server_types"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("next_page_token", None)
    if field is not None:
        args["next_page_token"] = field
    else:
        args["next_page_token"] = None

    return ListServerTypesResponse(**args)


def unmarshal_ServerSummary(data: Any) -> ServerSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerSummary' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

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

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = None

    field = data.get("server_type", None)
    if field is not None:
        args["server_type"] = field
    else:
        args["server_type"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = None

    field = data.get("architecture", None)
    if field is not None:
        args["architecture"] = field
    else:
        args["architecture"] = None

    field = data.get("rescue_mode", None)
    if field is not None:
        args["rescue_mode"] = field
    else:
        args["rescue_mode"] = None

    field = data.get("placement_group_id", None)
    if field is not None:
        args["placement_group_id"] = field
    else:
        args["placement_group_id"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return ServerSummary(**args)


def unmarshal_ListServersResponse(data: Any) -> ListServersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("servers", None)
    if field is not None:
        args["servers"] = (
            [unmarshal_ServerSummary(v) for v in field] if field is not None else None
        )
    else:
        args["servers"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("next_page_token", None)
    if field is not None:
        args["next_page_token"] = field
    else:
        args["next_page_token"] = None

    return ListServersResponse(**args)


def unmarshal_ListTemplateUserDataKeysResponse(
    data: Any,
) -> ListTemplateUserDataKeysResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTemplateUserDataKeysResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("keys", None)
    if field is not None:
        args["keys"] = field
    else:
        args["keys"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("next_page_token", None)
    if field is not None:
        args["next_page_token"] = field
    else:
        args["next_page_token"] = None

    return ListTemplateUserDataKeysResponse(**args)


def unmarshal_TemplateSummary(data: Any) -> TemplateSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TemplateSummary' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

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

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = None

    field = data.get("server_tags", None)
    if field is not None:
        args["server_tags"] = field
    else:
        args["server_tags"] = None

    field = data.get("server_type", None)
    if field is not None:
        args["server_type"] = field
    else:
        args["server_type"] = None

    field = data.get("public_ip_v4_count", None)
    if field is not None:
        args["public_ip_v4_count"] = field
    else:
        args["public_ip_v4_count"] = None

    field = data.get("security_group_id", None)
    if field is not None:
        args["security_group_id"] = field
    else:
        args["security_group_id"] = None

    field = data.get("placement_group_id", None)
    if field is not None:
        args["placement_group_id"] = field
    else:
        args["placement_group_id"] = None

    field = data.get("public_ip_v6_count", None)
    if field is not None:
        args["public_ip_v6_count"] = field
    else:
        args["public_ip_v6_count"] = None

    field = data.get("private_network_ids", None)
    if field is not None:
        args["private_network_ids"] = field
    else:
        args["private_network_ids"] = None

    field = data.get("filesystem_ids", None)
    if field is not None:
        args["filesystem_ids"] = field
    else:
        args["filesystem_ids"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return TemplateSummary(**args)


def unmarshal_ListTemplatesResponse(data: Any) -> ListTemplatesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTemplatesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("templates", None)
    if field is not None:
        args["templates"] = (
            [unmarshal_TemplateSummary(v) for v in field] if field is not None else None
        )
    else:
        args["templates"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("next_page_token", None)
    if field is not None:
        args["next_page_token"] = field
    else:
        args["next_page_token"] = None

    return ListTemplatesResponse(**args)


def unmarshal_ListUserDataKeysResponse(data: Any) -> ListUserDataKeysResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListUserDataKeysResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("keys", None)
    if field is not None:
        args["keys"] = field
    else:
        args["keys"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("next_page_token", None)
    if field is not None:
        args["next_page_token"] = field
    else:
        args["next_page_token"] = None

    return ListUserDataKeysResponse(**args)


def unmarshal_ResourceCounts(data: Any) -> ResourceCounts:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ResourceCounts' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("servers", None)
    if field is not None:
        args["servers"] = field
    else:
        args["servers"] = None

    field = data.get("gpu_servers", None)
    if field is not None:
        args["gpu_servers"] = field
    else:
        args["gpu_servers"] = None

    field = data.get("servers_by_type", None)
    if field is not None:
        args["servers_by_type"] = field
    else:
        args["servers_by_type"] = None

    field = data.get("security_groups", None)
    if field is not None:
        args["security_groups"] = field
    else:
        args["security_groups"] = None

    field = data.get("placement_groups", None)
    if field is not None:
        args["placement_groups"] = field
    else:
        args["placement_groups"] = None

    field = data.get("snapshots", None)
    if field is not None:
        args["snapshots"] = field
    else:
        args["snapshots"] = None

    field = data.get("volumes", None)
    if field is not None:
        args["volumes"] = field
    else:
        args["volumes"] = None

    field = data.get("volumes_l_ssd_total_size", None)
    if field is not None:
        args["volumes_l_ssd_total_size"] = field
    else:
        args["volumes_l_ssd_total_size"] = None

    field = data.get("private_network_interfaces", None)
    if field is not None:
        args["private_network_interfaces"] = field
    else:
        args["private_network_interfaces"] = None

    field = data.get("volumes_scratch", None)
    if field is not None:
        args["volumes_scratch"] = field
    else:
        args["volumes_scratch"] = None

    field = data.get("volumes_l_ssd", None)
    if field is not None:
        args["volumes_l_ssd"] = field
    else:
        args["volumes_l_ssd"] = None

    return ResourceCounts(**args)


def unmarshal_ServerIP(data: Any) -> ServerIP:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerIP' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("dynamic", None)
    if field is not None:
        args["dynamic"] = field
    else:
        args["dynamic"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = None

    field = data.get("default", None)
    if field is not None:
        args["default"] = field
    else:
        args["default"] = None

    return ServerIP(**args)


def unmarshal_ServerFilesystem(data: Any) -> ServerFilesystem:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerFilesystem' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = None

    return ServerFilesystem(**args)


def unmarshal_ServerPrivateNetworkInterface(data: Any) -> ServerPrivateNetworkInterface:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerPrivateNetworkInterface' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

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

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = None

    field = data.get("ip_ids", None)
    if field is not None:
        args["ip_ids"] = field
    else:
        args["ip_ids"] = None

    field = data.get("security_group_id", None)
    if field is not None:
        args["security_group_id"] = field
    else:
        args["security_group_id"] = None

    return ServerPrivateNetworkInterface(**args)


def unmarshal_ServerPublicNetworkInterface(data: Any) -> ServerPublicNetworkInterface:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerPublicNetworkInterface' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = None

    field = data.get("mac_address", None)
    if field is not None:
        args["mac_address"] = field
    else:
        args["mac_address"] = None

    field = data.get("security_group_id", None)
    if field is not None:
        args["security_group_id"] = field
    else:
        args["security_group_id"] = None

    field = data.get("ips", None)
    if field is not None:
        args["ips"] = (
            [unmarshal_ServerIP(v) for v in field] if field is not None else None
        )
    else:
        args["ips"] = None

    field = data.get("dns", None)
    if field is not None:
        args["dns"] = field
    else:
        args["dns"] = None

    return ServerPublicNetworkInterface(**args)


def unmarshal_ServerRDPPassword(data: Any) -> ServerRDPPassword:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerRDPPassword' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("encrypted_password", None)
    if field is not None:
        args["encrypted_password"] = field
    else:
        args["encrypted_password"] = None

    field = data.get("rdp_ssh_key_id", None)
    if field is not None:
        args["rdp_ssh_key_id"] = field
    else:
        args["rdp_ssh_key_id"] = None

    return ServerRDPPassword(**args)


def unmarshal_ServerVolume(data: Any) -> ServerVolume:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerVolume' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("volume_type", None)
    if field is not None:
        args["volume_type"] = field
    else:
        args["volume_type"] = None

    return ServerVolume(**args)


def unmarshal_Server(data: Any) -> Server:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Server' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

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

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = None

    field = data.get("server_type", None)
    if field is not None:
        args["server_type"] = field
    else:
        args["server_type"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = None

    field = data.get("volumes", None)
    if field is not None:
        args["volumes"] = (
            [unmarshal_ServerVolume(v) for v in field] if field is not None else None
        )
    else:
        args["volumes"] = None

    field = data.get("placement_group_id", None)
    if field is not None:
        args["placement_group_id"] = field
    else:
        args["placement_group_id"] = None

    field = data.get("architecture", None)
    if field is not None:
        args["architecture"] = field
    else:
        args["architecture"] = None

    field = data.get("private_network_interfaces", None)
    if field is not None:
        args["private_network_interfaces"] = (
            [unmarshal_ServerPrivateNetworkInterface(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["private_network_interfaces"] = None

    field = data.get("rescue_mode", None)
    if field is not None:
        args["rescue_mode"] = field
    else:
        args["rescue_mode"] = None

    field = data.get("status_detail", None)
    if field is not None:
        args["status_detail"] = field
    else:
        args["status_detail"] = None

    field = data.get("filesystems", None)
    if field is not None:
        args["filesystems"] = (
            [unmarshal_ServerFilesystem(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["filesystems"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("boot_volume_id", None)
    if field is not None:
        args["boot_volume_id"] = field
    else:
        args["boot_volume_id"] = None

    field = data.get("windows_rdp_password", None)
    if field is not None:
        args["windows_rdp_password"] = unmarshal_ServerRDPPassword(field)
    else:
        args["windows_rdp_password"] = None

    field = data.get("public_network_interface", None)
    if field is not None:
        args["public_network_interface"] = unmarshal_ServerPublicNetworkInterface(field)
    else:
        args["public_network_interface"] = None

    return Server(**args)


def unmarshal_CreateTemplateRequestVolumeTemplate(
    data: Any,
) -> CreateTemplateRequestVolumeTemplate:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateTemplateRequestVolumeTemplate' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("volume_type", None)
    if field is not None:
        args["volume_type"] = field
    else:
        args["volume_type"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = None

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = None

    field = data.get("base_snapshot_id", None)
    if field is not None:
        args["base_snapshot_id"] = field
    else:
        args["base_snapshot_id"] = None

    field = data.get("image_label", None)
    if field is not None:
        args["image_label"] = field
    else:
        args["image_label"] = None

    field = data.get("perf_iops", None)
    if field is not None:
        args["perf_iops"] = field
    else:
        args["perf_iops"] = None

    return CreateTemplateRequestVolumeTemplate(**args)


def unmarshal_Template(data: Any) -> Template:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Template' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

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

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = None

    field = data.get("server_tags", None)
    if field is not None:
        args["server_tags"] = field
    else:
        args["server_tags"] = None

    field = data.get("server_type", None)
    if field is not None:
        args["server_type"] = field
    else:
        args["server_type"] = None

    field = data.get("security_group_id", None)
    if field is not None:
        args["security_group_id"] = field
    else:
        args["security_group_id"] = None

    field = data.get("placement_group_id", None)
    if field is not None:
        args["placement_group_id"] = field
    else:
        args["placement_group_id"] = None

    field = data.get("public_ip_v4_count", None)
    if field is not None:
        args["public_ip_v4_count"] = field
    else:
        args["public_ip_v4_count"] = None

    field = data.get("public_ip_v6_count", None)
    if field is not None:
        args["public_ip_v6_count"] = field
    else:
        args["public_ip_v6_count"] = None

    field = data.get("volumes", None)
    if field is not None:
        args["volumes"] = (
            [unmarshal_CreateTemplateRequestVolumeTemplate(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["volumes"] = None

    field = data.get("private_network_ids", None)
    if field is not None:
        args["private_network_ids"] = field
    else:
        args["private_network_ids"] = None

    field = data.get("filesystem_ids", None)
    if field is not None:
        args["filesystem_ids"] = field
    else:
        args["filesystem_ids"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("windows_rdp_ssh_key_id", None)
    if field is not None:
        args["windows_rdp_ssh_key_id"] = field
    else:
        args["windows_rdp_ssh_key_id"] = None

    return Template(**args)


def unmarshal_UserData(data: Any) -> UserData:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UserData' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("key", None)
    if field is not None:
        args["key"] = field
    else:
        args["key"] = None

    field = data.get("content", None)
    if field is not None:
        args["content"] = field
    else:
        args["content"] = None

    return UserData(**args)


def marshal_SecurityGroupRulePortRange(
    request: SecurityGroupRulePortRange,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.start is not None:
        output["start"] = request.start

    if request.end is not None:
        output["end"] = request.end

    return output


def marshal_SecurityGroupRuleConfig(
    request: SecurityGroupRuleConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.protocol is not None:
        output["protocol"] = request.protocol

    if request.direction is not None:
        output["direction"] = request.direction

    if request.action is not None:
        output["action"] = request.action

    if request.source_ip_range is not None:
        output["source_ip_range"] = request.source_ip_range

    if request.destination_ip_range is not None:
        output["destination_ip_range"] = request.destination_ip_range

    if request.position is not None:
        output["position"] = request.position

    if request.source_ports is not None:
        output["source_ports"] = marshal_SecurityGroupRulePortRange(
            request.source_ports, defaults
        )

    if request.destination_ports is not None:
        output["destination_ports"] = marshal_SecurityGroupRulePortRange(
            request.destination_ports, defaults
        )

    return output


def marshal_AddSecurityGroupRulesRequest(
    request: AddSecurityGroupRulesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.security_group_id is not None:
        output["security_group_id"] = request.security_group_id

    if request.security_group_rules is not None:
        output["security_group_rules"] = [
            marshal_SecurityGroupRuleConfig(item, defaults)
            for item in request.security_group_rules
        ]

    return output


def marshal_AttachServerFileSystemRequest(
    request: AttachServerFileSystemRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.filesystem_id is not None:
        output["filesystem_id"] = request.filesystem_id

    return output


def marshal_AttachServerIPRequest(
    request: AttachServerIPRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ip_id is not None:
        output["ip_id"] = request.ip_id

    if request.default is not None:
        output["default"] = request.default

    if request.move_allowed is not None:
        output["move_allowed"] = request.move_allowed

    return output


def marshal_AttachServerPrivateNetworkInterfaceRequest(
    request: AttachServerPrivateNetworkInterfaceRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.private_network_interface_id is not None:
        output["private_network_interface_id"] = request.private_network_interface_id

    return output


def marshal_AttachServerVolumeRequest(
    request: AttachServerVolumeRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.volume_id is not None:
        output["volume_id"] = request.volume_id

    if request.boot_volume is not None:
        output["boot_volume"] = request.boot_volume

    if request.volume_type is not None:
        output["volume_type"] = request.volume_type

    return output


def marshal_CreatePlacementGroupRequest(
    request: CreatePlacementGroupRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.policy_type is not None:
        output["policy_type"] = request.policy_type

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreatePrivateNetworkInterfaceRequest(
    request: CreatePrivateNetworkInterfaceRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.server_id is not None:
        output["server_id"] = request.server_id

    if request.security_group_id is not None:
        output["security_group_id"] = request.security_group_id

    if request.ip_ids is not None:
        output["ip_ids"] = request.ip_ids

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreateSecurityGroupRequest(
    request: CreateSecurityGroupRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.disable_default_rules is not None:
        output["disable_default_rules"] = request.disable_default_rules

    if request.project_default is not None:
        output["project_default"] = request.project_default

    if request.stateless is not None:
        output["stateless"] = request.stateless

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.inbound_default_action is not None:
        output["inbound_default_action"] = request.inbound_default_action

    if request.outbound_default_action is not None:
        output["outbound_default_action"] = request.outbound_default_action

    return output


def marshal_CreateServerFromTemplateRequest(
    request: CreateServerFromTemplateRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_CreateServerRequestBookIP(
    request: CreateServerRequestBookIP,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreateServerRequestServerIP(
    request: CreateServerRequestServerIP,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="ipam_ip_id", value=request.ipam_ip_id, marshal_func=None
                ),
                OneOfPossibility(
                    param="new_ip",
                    value=request.new_ip,
                    marshal_func=marshal_CreateServerRequestBookIP,
                ),
            ]
        ),
    )

    return output


def marshal_CreateServerRequestCreateVolume(
    request: CreateServerRequestCreateVolume,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="base_snapshot_id",
                    value=request.base_snapshot_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="image_label", value=request.image_label, marshal_func=None
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.size is not None:
        output["size"] = request.size

    if request.perf_iops is not None:
        output["perf_iops"] = request.perf_iops

    return output


def marshal_CreateServerRequestPublicNetworkInterface(
    request: CreateServerRequestPublicNetworkInterface,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ips is not None:
        output["ips"] = [
            marshal_CreateServerRequestServerIP(item, defaults) for item in request.ips
        ]

    if request.security_group_id is not None:
        output["security_group_id"] = request.security_group_id

    return output


def marshal_CreateServerRequestServerVolume(
    request: CreateServerRequestServerVolume,
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
                    param="new_volume",
                    value=request.new_volume,
                    marshal_func=marshal_CreateServerRequestCreateVolume,
                ),
            ]
        ),
    )

    if request.volume_type is not None:
        output["volume_type"] = request.volume_type

    return output


def marshal_CreateServerRequest(
    request: CreateServerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.server_type is not None:
        output["server_type"] = request.server_type

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.placement_group_id is not None:
        output["placement_group_id"] = request.placement_group_id

    if request.volumes is not None:
        output["volumes"] = [
            marshal_CreateServerRequestServerVolume(item, defaults)
            for item in request.volumes
        ]

    if request.windows_rdp_ssh_key_id is not None:
        output["windows_rdp_ssh_key_id"] = request.windows_rdp_ssh_key_id

    if request.public_network_interface is not None:
        output["public_network_interface"] = (
            marshal_CreateServerRequestPublicNetworkInterface(
                request.public_network_interface, defaults
            )
        )

    return output


def marshal_CreateTemplateRequestVolumeTemplate(
    request: CreateTemplateRequestVolumeTemplate,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="base_snapshot_id",
                    value=request.base_snapshot_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="image_label", value=request.image_label, marshal_func=None
                ),
            ]
        ),
    )

    if request.volume_type is not None:
        output["volume_type"] = request.volume_type

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.size is not None:
        output["size"] = request.size

    if request.perf_iops is not None:
        output["perf_iops"] = request.perf_iops

    return output


def marshal_CreateTemplateRequest(
    request: CreateTemplateRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.server_type is not None:
        output["server_type"] = request.server_type

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.server_tags is not None:
        output["server_tags"] = request.server_tags

    if request.public_ip_v4_count is not None:
        output["public_ip_v4_count"] = request.public_ip_v4_count

    if request.public_ip_v6_count is not None:
        output["public_ip_v6_count"] = request.public_ip_v6_count

    if request.security_group_id is not None:
        output["security_group_id"] = request.security_group_id

    if request.placement_group_id is not None:
        output["placement_group_id"] = request.placement_group_id

    if request.volumes is not None:
        output["volumes"] = [
            marshal_CreateTemplateRequestVolumeTemplate(item, defaults)
            for item in request.volumes
        ]

    if request.private_network_ids is not None:
        output["private_network_ids"] = request.private_network_ids

    if request.windows_rdp_ssh_key_id is not None:
        output["windows_rdp_ssh_key_id"] = request.windows_rdp_ssh_key_id

    if request.filesystem_ids is not None:
        output["filesystem_ids"] = request.filesystem_ids

    return output


def marshal_DeleteSecurityGroupRulesRequest(
    request: DeleteSecurityGroupRulesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.security_group_rule_ids is not None:
        output["security_group_rule_ids"] = request.security_group_rule_ids

    return output


def marshal_DetachServerFileSystemRequest(
    request: DetachServerFileSystemRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.filesystem_id is not None:
        output["filesystem_id"] = request.filesystem_id

    return output


def marshal_DetachServerIPRequest(
    request: DetachServerIPRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ip_id is not None:
        output["ip_id"] = request.ip_id

    return output


def marshal_DetachServerPrivateNetworkInterfaceRequest(
    request: DetachServerPrivateNetworkInterfaceRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.private_network_interface_id is not None:
        output["private_network_interface_id"] = request.private_network_interface_id

    return output


def marshal_DetachServerVolumeRequest(
    request: DetachServerVolumeRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.volume_id is not None:
        output["volume_id"] = request.volume_id

    return output


def marshal_SetSecurityGroupRulesRequest(
    request: SetSecurityGroupRulesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.security_group_id is not None:
        output["security_group_id"] = request.security_group_id

    if request.security_group_rules is not None:
        output["security_group_rules"] = [
            marshal_SecurityGroupRuleConfig(item, defaults)
            for item in request.security_group_rules
        ]

    return output


def marshal_SetServerCloudInitRequest(
    request: SetServerCloudInitRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.content is not None:
        output["content"] = request.content

    return output


def marshal_SetServerDefaultIPRequest(
    request: SetServerDefaultIPRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ip_id is not None:
        output["ip_id"] = request.ip_id

    return output


def marshal_SetTemplateCloudInitRequest(
    request: SetTemplateCloudInitRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.content is not None:
        output["content"] = request.content

    return output


def marshal_SetTemplateUserDataRequest(
    request: SetTemplateUserDataRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.content is not None:
        output["content"] = request.content

    return output


def marshal_SetUserDataRequest(
    request: SetUserDataRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.content is not None:
        output["content"] = request.content

    return output


def marshal_StopAndDeleteServerRequest(
    request: StopAndDeleteServerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="delete_all_ips",
                    value=request.delete_all_ips,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="delete_ip_ids",
                    value=request.delete_ip_ids,
                    marshal_func=None,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="delete_all_volumes",
                    value=request.delete_all_volumes,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="delete_volume_ids",
                    value=request.delete_volume_ids,
                    marshal_func=None,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="keep_all_private_nics",
                    value=request.keep_all_private_nics,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="delete_private_nic_ids",
                    value=request.delete_private_nic_ids,
                    marshal_func=None,
                ),
            ]
        ),
    )

    return output


def marshal_UpdatePlacementGroupRequest(
    request: UpdatePlacementGroupRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.policy_type is not None:
        output["policy_type"] = request.policy_type

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdatePrivateNetworkInterfaceRequest(
    request: UpdatePrivateNetworkInterfaceRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.security_group_id is not None:
        output["security_group_id"] = request.security_group_id

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

    if request.disable_default_rules is not None:
        output["disable_default_rules"] = request.disable_default_rules

    if request.tags is not None:
        output["tags"] = request.tags

    if request.project_default is not None:
        output["project_default"] = request.project_default

    if request.inbound_default_action is not None:
        output["inbound_default_action"] = request.inbound_default_action

    if request.outbound_default_action is not None:
        output["outbound_default_action"] = request.outbound_default_action

    if request.stateless is not None:
        output["stateless"] = request.stateless

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

    if request.source_ip_range is not None:
        output["source_ip_range"] = request.source_ip_range

    if request.destination_ip_range is not None:
        output["destination_ip_range"] = request.destination_ip_range

    if request.source_ports is not None:
        output["source_ports"] = marshal_SecurityGroupRulePortRange(
            request.source_ports, defaults
        )

    if request.destination_ports is not None:
        output["destination_ports"] = marshal_SecurityGroupRulePortRange(
            request.destination_ports, defaults
        )

    if request.position is not None:
        output["position"] = request.position

    return output


def marshal_UpdateServerRequestPublicNetworkInterface(
    request: UpdateServerRequestPublicNetworkInterface,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.security_group_id is not None:
        output["security_group_id"] = request.security_group_id

    return output


def marshal_UpdateServerRequest(
    request: UpdateServerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.server_type is not None:
        output["server_type"] = request.server_type

    if request.placement_group_id is not None:
        output["placement_group_id"] = request.placement_group_id

    if request.rescue_mode is not None:
        output["rescue_mode"] = request.rescue_mode

    if request.boot_volume_id is not None:
        output["boot_volume_id"] = request.boot_volume_id

    if request.windows_rdp_ssh_key_id is not None:
        output["windows_rdp_ssh_key_id"] = request.windows_rdp_ssh_key_id

    if request.protected is not None:
        output["protected"] = request.protected

    if request.public_network_interface is not None:
        output["public_network_interface"] = (
            marshal_UpdateServerRequestPublicNetworkInterface(
                request.public_network_interface, defaults
            )
        )

    return output


def marshal_UpdateTemplateRequestUpdateVolumes(
    request: UpdateTemplateRequestUpdateVolumes,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.volumes is not None:
        output["volumes"] = [
            marshal_CreateTemplateRequestVolumeTemplate(item, defaults)
            for item in request.volumes
        ]

    return output


def marshal_UpdateTemplateRequest(
    request: UpdateTemplateRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.server_tags is not None:
        output["server_tags"] = request.server_tags

    if request.server_type is not None:
        output["server_type"] = request.server_type

    if request.security_group_id is not None:
        output["security_group_id"] = request.security_group_id

    if request.placement_group_id is not None:
        output["placement_group_id"] = request.placement_group_id

    if request.update_volumes is not None:
        output["update_volumes"] = marshal_UpdateTemplateRequestUpdateVolumes(
            request.update_volumes, defaults
        )

    if request.private_network_ids is not None:
        output["private_network_ids"] = request.private_network_ids

    if request.public_ip_v4_count is not None:
        output["public_ip_v4_count"] = request.public_ip_v4_count

    if request.public_ip_v6_count is not None:
        output["public_ip_v6_count"] = request.public_ip_v6_count

    if request.windows_rdp_ssh_key_id is not None:
        output["windows_rdp_ssh_key_id"] = request.windows_rdp_ssh_key_id

    if request.filesystem_ids is not None:
        output["filesystem_ids"] = request.filesystem_ids

    return output
