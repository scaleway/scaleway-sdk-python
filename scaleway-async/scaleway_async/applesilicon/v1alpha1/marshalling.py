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
    ConnectivityDiagnosticActionType,
    ServerPrivateNetworkServerStatus,
    ServerPrivateNetworkStatus,
    ServerStatus,
    ServerTypeStock,
    OSSupportedServerType,
    OS,
    Commitment,
    RunnerConfiguration,
    Server,
    GithubRunnerConfiguration,
    GitlabRunnerConfiguration,
    RunnerConfigurationV2,
    Runner,
    ServerPrivateNetwork,
    ServerTypeCPU,
    ServerTypeDisk,
    ServerTypeGPU,
    ServerTypeMemory,
    ServerTypeNPU,
    ServerTypeNetwork,
    ServerType,
    BatchCreateServersResponse,
    ConnectivityDiagnosticServerHealth,
    ConnectivityDiagnostic,
    ListOSResponse,
    ListRunnersResponse,
    ListServerPrivateNetworksResponse,
    ListServerTypesResponse,
    ListServersResponse,
    SetServerPrivateNetworksResponse,
    StartConnectivityDiagnosticResponse,
    BatchCreateServersRequestBatchInnerCreateServerRequest,
    BatchCreateServersRequest,
    CreateRunnerRequest,
    AppliedRunnerConfigurations,
    CreateServerRequest,
    PrivateNetworkApiAddServerPrivateNetworkRequest,
    PrivateNetworkApiSetServerPrivateNetworksRequest,
    ReinstallServerRequest,
    StartConnectivityDiagnosticRequest,
    UpdateRunnerRequest,
    CommitmentTypeValue,
    UpdateServerRequest,
)


def unmarshal_OSSupportedServerType(data: Any) -> OSSupportedServerType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OSSupportedServerType' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("server_type", None)
    if field is not None:
        args["server_type"] = field
    else:
        args["server_type"] = None

    field = data.get("fast_delivery_available", None)
    if field is not None:
        args["fast_delivery_available"] = field
    else:
        args["fast_delivery_available"] = None

    return OSSupportedServerType(**args)


def unmarshal_OS(data: Any) -> OS:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OS' failed as data isn't a dictionary."
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

    field = data.get("label", None)
    if field is not None:
        args["label"] = field
    else:
        args["label"] = None

    field = data.get("image_url", None)
    if field is not None:
        args["image_url"] = field
    else:
        args["image_url"] = None

    field = data.get("family", None)
    if field is not None:
        args["family"] = field
    else:
        args["family"] = None

    field = data.get("is_beta", None)
    if field is not None:
        args["is_beta"] = field
    else:
        args["is_beta"] = False

    field = data.get("version", None)
    if field is not None:
        args["version"] = field
    else:
        args["version"] = None

    field = data.get("xcode_version", None)
    if field is not None:
        args["xcode_version"] = field
    else:
        args["xcode_version"] = None

    field = data.get("compatible_server_types", None)
    if field is not None:
        args["compatible_server_types"] = field
    else:
        args["compatible_server_types"] = []

    field = data.get("release_notes_url", None)
    if field is not None:
        args["release_notes_url"] = field
    else:
        args["release_notes_url"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("supported_server_types", None)
    if field is not None:
        args["supported_server_types"] = (
            [unmarshal_OSSupportedServerType(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["supported_server_types"] = []

    return OS(**args)


def unmarshal_Commitment(data: Any) -> Commitment:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Commitment' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    field = data.get("cancelled", None)
    if field is not None:
        args["cancelled"] = field
    else:
        args["cancelled"] = None

    return Commitment(**args)


def unmarshal_RunnerConfiguration(data: Any) -> RunnerConfiguration:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RunnerConfiguration' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("url", None)
    if field is not None:
        args["url"] = field
    else:
        args["url"] = None

    field = data.get("token", None)
    if field is not None:
        args["token"] = field
    else:
        args["token"] = None

    field = data.get("provider", None)
    if field is not None:
        args["provider"] = field
    else:
        args["provider"] = None

    return RunnerConfiguration(**args)


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

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("ip", None)
    if field is not None:
        args["ip"] = field
    else:
        args["ip"] = None

    field = data.get("vnc_url", None)
    if field is not None:
        args["vnc_url"] = field
    else:
        args["vnc_url"] = None

    field = data.get("ssh_username", None)
    if field is not None:
        args["ssh_username"] = field
    else:
        args["ssh_username"] = None

    field = data.get("sudo_password", None)
    if field is not None:
        args["sudo_password"] = field
    else:
        args["sudo_password"] = None

    field = data.get("vnc_port", None)
    if field is not None:
        args["vnc_port"] = field
    else:
        args["vnc_port"] = 0

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = ServerStatus.UNKNOWN_STATUS

    field = data.get("deletion_scheduled", None)
    if field is not None:
        args["deletion_scheduled"] = field
    else:
        args["deletion_scheduled"] = False

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("delivered", None)
    if field is not None:
        args["delivered"] = field
    else:
        args["delivered"] = False

    field = data.get("os", None)
    if field is not None:
        args["os"] = unmarshal_OS(field)
    else:
        args["os"] = None

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

    field = data.get("deletable_at", None)
    if field is not None:
        args["deletable_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["deletable_at"] = None

    field = data.get("vpc_status", None)
    if field is not None:
        args["vpc_status"] = field
    else:
        args["vpc_status"] = ServerPrivateNetworkStatus.VPC_UNKNOWN_STATUS

    field = data.get("public_bandwidth_bps", None)
    if field is not None:
        args["public_bandwidth_bps"] = field
    else:
        args["public_bandwidth_bps"] = 0

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("applied_runner_configuration_ids", None)
    if field is not None:
        args["applied_runner_configuration_ids"] = field
    else:
        args["applied_runner_configuration_ids"] = []

    field = data.get("commitment", None)
    if field is not None:
        args["commitment"] = unmarshal_Commitment(field)
    else:
        args["commitment"] = None

    field = data.get("runner_configuration", None)
    if field is not None:
        args["runner_configuration"] = unmarshal_RunnerConfiguration(field)
    else:
        args["runner_configuration"] = None

    return Server(**args)


def unmarshal_GithubRunnerConfiguration(data: Any) -> GithubRunnerConfiguration:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GithubRunnerConfiguration' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("url", None)
    if field is not None:
        args["url"] = field
    else:
        args["url"] = None

    field = data.get("token", None)
    if field is not None:
        args["token"] = field
    else:
        args["token"] = None

    field = data.get("labels", None)
    if field is not None:
        args["labels"] = field
    else:
        args["labels"] = None

    return GithubRunnerConfiguration(**args)


def unmarshal_GitlabRunnerConfiguration(data: Any) -> GitlabRunnerConfiguration:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GitlabRunnerConfiguration' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("url", None)
    if field is not None:
        args["url"] = field
    else:
        args["url"] = None

    field = data.get("token", None)
    if field is not None:
        args["token"] = field
    else:
        args["token"] = None

    return GitlabRunnerConfiguration(**args)


def unmarshal_RunnerConfigurationV2(data: Any) -> RunnerConfigurationV2:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RunnerConfigurationV2' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("provider", None)
    if field is not None:
        args["provider"] = field
    else:
        args["provider"] = None

    field = data.get("github_configuration", None)
    if field is not None:
        args["github_configuration"] = unmarshal_GithubRunnerConfiguration(field)
    else:
        args["github_configuration"] = None

    field = data.get("gitlab_configuration", None)
    if field is not None:
        args["gitlab_configuration"] = unmarshal_GitlabRunnerConfiguration(field)
    else:
        args["gitlab_configuration"] = None

    return RunnerConfigurationV2(**args)


def unmarshal_Runner(data: Any) -> Runner:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Runner' failed as data isn't a dictionary."
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

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

    field = data.get("configuration", None)
    if field is not None:
        args["configuration"] = unmarshal_RunnerConfigurationV2(field)
    else:
        args["configuration"] = None

    return Runner(**args)


def unmarshal_ServerPrivateNetwork(data: Any) -> ServerPrivateNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerPrivateNetwork' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

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

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field
    else:
        args["private_network_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = ServerPrivateNetworkServerStatus.UNKNOWN_STATUS

    field = data.get("ipam_ip_ids", None)
    if field is not None:
        args["ipam_ip_ids"] = field
    else:
        args["ipam_ip_ids"] = []

    field = data.get("vlan", None)
    if field is not None:
        args["vlan"] = field
    else:
        args["vlan"] = 0

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

    return ServerPrivateNetwork(**args)


def unmarshal_ServerTypeCPU(data: Any) -> ServerTypeCPU:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeCPU' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("core_count", None)
    if field is not None:
        args["core_count"] = field
    else:
        args["core_count"] = None

    field = data.get("frequency", None)
    if field is not None:
        args["frequency"] = field
    else:
        args["frequency"] = None

    field = data.get("sockets", None)
    if field is not None:
        args["sockets"] = field
    else:
        args["sockets"] = None

    field = data.get("threads_per_core", None)
    if field is not None:
        args["threads_per_core"] = field
    else:
        args["threads_per_core"] = None

    return ServerTypeCPU(**args)


def unmarshal_ServerTypeDisk(data: Any) -> ServerTypeDisk:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeDisk' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("capacity", None)
    if field is not None:
        args["capacity"] = field
    else:
        args["capacity"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    return ServerTypeDisk(**args)


def unmarshal_ServerTypeGPU(data: Any) -> ServerTypeGPU:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeGPU' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("count", None)
    if field is not None:
        args["count"] = field
    else:
        args["count"] = None

    return ServerTypeGPU(**args)


def unmarshal_ServerTypeMemory(data: Any) -> ServerTypeMemory:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeMemory' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("capacity", None)
    if field is not None:
        args["capacity"] = field
    else:
        args["capacity"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    return ServerTypeMemory(**args)


def unmarshal_ServerTypeNPU(data: Any) -> ServerTypeNPU:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeNPU' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("count", None)
    if field is not None:
        args["count"] = field
    else:
        args["count"] = None

    return ServerTypeNPU(**args)


def unmarshal_ServerTypeNetwork(data: Any) -> ServerTypeNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerTypeNetwork' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("public_bandwidth_bps", None)
    if field is not None:
        args["public_bandwidth_bps"] = field
    else:
        args["public_bandwidth_bps"] = None

    field = data.get("supported_bandwidth", None)
    if field is not None:
        args["supported_bandwidth"] = field
    else:
        args["supported_bandwidth"] = None

    field = data.get("default_public_bandwidth", None)
    if field is not None:
        args["default_public_bandwidth"] = field
    else:
        args["default_public_bandwidth"] = None

    return ServerTypeNetwork(**args)


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

    field = data.get("stock", None)
    if field is not None:
        args["stock"] = field
    else:
        args["stock"] = ServerTypeStock.UNKNOWN_STOCK

    field = data.get("cpu", None)
    if field is not None:
        args["cpu"] = unmarshal_ServerTypeCPU(field)
    else:
        args["cpu"] = None

    field = data.get("disk", None)
    if field is not None:
        args["disk"] = unmarshal_ServerTypeDisk(field)
    else:
        args["disk"] = None

    field = data.get("memory", None)
    if field is not None:
        args["memory"] = unmarshal_ServerTypeMemory(field)
    else:
        args["memory"] = None

    field = data.get("minimum_lease_duration", None)
    if field is not None:
        args["minimum_lease_duration"] = field
    else:
        args["minimum_lease_duration"] = None

    field = data.get("gpu", None)
    if field is not None:
        args["gpu"] = unmarshal_ServerTypeGPU(field)
    else:
        args["gpu"] = None

    field = data.get("network", None)
    if field is not None:
        args["network"] = unmarshal_ServerTypeNetwork(field)
    else:
        args["network"] = None

    field = data.get("default_os", None)
    if field is not None:
        args["default_os"] = unmarshal_OS(field)
    else:
        args["default_os"] = None

    field = data.get("npu", None)
    if field is not None:
        args["npu"] = unmarshal_ServerTypeNPU(field)
    else:
        args["npu"] = None

    return ServerType(**args)


def unmarshal_BatchCreateServersResponse(data: Any) -> BatchCreateServersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BatchCreateServersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("servers", None)
    if field is not None:
        args["servers"] = (
            [unmarshal_Server(v) for v in field] if field is not None else None
        )
    else:
        args["servers"] = []

    return BatchCreateServersResponse(**args)


def unmarshal_ConnectivityDiagnosticServerHealth(
    data: Any,
) -> ConnectivityDiagnosticServerHealth:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ConnectivityDiagnosticServerHealth' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("is_server_alive", None)
    if field is not None:
        args["is_server_alive"] = field
    else:
        args["is_server_alive"] = None

    field = data.get("is_agent_alive", None)
    if field is not None:
        args["is_agent_alive"] = field
    else:
        args["is_agent_alive"] = None

    field = data.get("is_mdm_alive", None)
    if field is not None:
        args["is_mdm_alive"] = field
    else:
        args["is_mdm_alive"] = None

    field = data.get("is_ssh_port_up", None)
    if field is not None:
        args["is_ssh_port_up"] = field
    else:
        args["is_ssh_port_up"] = None

    field = data.get("is_vnc_port_up", None)
    if field is not None:
        args["is_vnc_port_up"] = field
    else:
        args["is_vnc_port_up"] = None

    field = data.get("last_checkin_date", None)
    if field is not None:
        args["last_checkin_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["last_checkin_date"] = None

    return ConnectivityDiagnosticServerHealth(**args)


def unmarshal_ConnectivityDiagnostic(data: Any) -> ConnectivityDiagnostic:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ConnectivityDiagnostic' failed as data isn't a dictionary."
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

    field = data.get("is_healthy", None)
    if field is not None:
        args["is_healthy"] = field
    else:
        args["is_healthy"] = None

    field = data.get("supported_actions", None)
    if field is not None:
        args["supported_actions"] = (
            [ConnectivityDiagnosticActionType(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["supported_actions"] = None

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

    field = data.get("health_details", None)
    if field is not None:
        args["health_details"] = unmarshal_ConnectivityDiagnosticServerHealth(field)
    else:
        args["health_details"] = None

    return ConnectivityDiagnostic(**args)


def unmarshal_ListOSResponse(data: Any) -> ListOSResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOSResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("os", None)
    if field is not None:
        args["os"] = [unmarshal_OS(v) for v in field] if field is not None else None
    else:
        args["os"] = []

    return ListOSResponse(**args)


def unmarshal_ListRunnersResponse(data: Any) -> ListRunnersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRunnersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("runners", None)
    if field is not None:
        args["runners"] = (
            [unmarshal_Runner(v) for v in field] if field is not None else None
        )
    else:
        args["runners"] = None

    return ListRunnersResponse(**args)


def unmarshal_ListServerPrivateNetworksResponse(
    data: Any,
) -> ListServerPrivateNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServerPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("server_private_networks", None)
    if field is not None:
        args["server_private_networks"] = (
            [unmarshal_ServerPrivateNetwork(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["server_private_networks"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    return ListServerPrivateNetworksResponse(**args)


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
        args["server_types"] = []

    return ListServerTypesResponse(**args)


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


def unmarshal_SetServerPrivateNetworksResponse(
    data: Any,
) -> SetServerPrivateNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetServerPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("server_private_networks", None)
    if field is not None:
        args["server_private_networks"] = (
            [unmarshal_ServerPrivateNetwork(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["server_private_networks"] = None

    return SetServerPrivateNetworksResponse(**args)


def unmarshal_StartConnectivityDiagnosticResponse(
    data: Any,
) -> StartConnectivityDiagnosticResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'StartConnectivityDiagnosticResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("diagnostic_id", None)
    if field is not None:
        args["diagnostic_id"] = field
    else:
        args["diagnostic_id"] = None

    return StartConnectivityDiagnosticResponse(**args)


def marshal_BatchCreateServersRequestBatchInnerCreateServerRequest(
    request: BatchCreateServersRequestBatchInnerCreateServerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_BatchCreateServersRequest(
    request: BatchCreateServersRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    if request.enable_vpc is not None:
        output["enable_vpc"] = request.enable_vpc

    if request.public_bandwidth_bps is not None:
        output["public_bandwidth_bps"] = request.public_bandwidth_bps

    if request.enable_kext is not None:
        output["enable_kext"] = request.enable_kext

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.os_id is not None:
        output["os_id"] = request.os_id

    if request.commitment_type is not None:
        output["commitment_type"] = request.commitment_type

    if request.requests is not None:
        output["requests"] = [
            marshal_BatchCreateServersRequestBatchInnerCreateServerRequest(
                item, defaults
            )
            for item in request.requests
        ]

    return output


def marshal_GithubRunnerConfiguration(
    request: GithubRunnerConfiguration,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.url is not None:
        output["url"] = request.url

    if request.token is not None:
        output["token"] = request.token

    if request.labels is not None:
        output["labels"] = request.labels

    return output


def marshal_GitlabRunnerConfiguration(
    request: GitlabRunnerConfiguration,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.url is not None:
        output["url"] = request.url

    if request.token is not None:
        output["token"] = request.token

    return output


def marshal_RunnerConfigurationV2(
    request: RunnerConfigurationV2,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="github_configuration",
                    value=request.github_configuration,
                    marshal_func=marshal_GithubRunnerConfiguration,
                ),
                OneOfPossibility(
                    param="gitlab_configuration",
                    value=request.gitlab_configuration,
                    marshal_func=marshal_GitlabRunnerConfiguration,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.provider is not None:
        output["provider"] = request.provider

    return output


def marshal_CreateRunnerRequest(
    request: CreateRunnerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.runner_configuration is not None:
        output["runner_configuration"] = marshal_RunnerConfigurationV2(
            request.runner_configuration, defaults
        )

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_AppliedRunnerConfigurations(
    request: AppliedRunnerConfigurations,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.runner_configuration_ids is not None:
        output["runner_configuration_ids"] = request.runner_configuration_ids

    return output


def marshal_RunnerConfiguration(
    request: RunnerConfiguration,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.url is not None:
        output["url"] = request.url

    if request.token is not None:
        output["token"] = request.token

    if request.provider is not None:
        output["provider"] = request.provider

    return output


def marshal_CreateServerRequest(
    request: CreateServerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    if request.enable_vpc is not None:
        output["enable_vpc"] = request.enable_vpc

    if request.public_bandwidth_bps is not None:
        output["public_bandwidth_bps"] = request.public_bandwidth_bps

    if request.enable_kext is not None:
        output["enable_kext"] = request.enable_kext

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.os_id is not None:
        output["os_id"] = request.os_id

    if request.commitment_type is not None:
        output["commitment_type"] = request.commitment_type

    if request.runner_configuration is not None:
        output["runner_configuration"] = marshal_RunnerConfiguration(
            request.runner_configuration, defaults
        )

    if request.applied_runner_configurations is not None:
        output["applied_runner_configurations"] = marshal_AppliedRunnerConfigurations(
            request.applied_runner_configurations, defaults
        )

    return output


def marshal_PrivateNetworkApiAddServerPrivateNetworkRequest(
    request: PrivateNetworkApiAddServerPrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    if request.ipam_ip_ids is not None:
        output["ipam_ip_ids"] = request.ipam_ip_ids

    return output


def marshal_PrivateNetworkApiSetServerPrivateNetworksRequest(
    request: PrivateNetworkApiSetServerPrivateNetworksRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.per_private_network_ipam_ip_ids is not None:
        output["per_private_network_ipam_ip_ids"] = {
            key: value for key, value in request.per_private_network_ipam_ip_ids.items()
        }

    return output


def marshal_ReinstallServerRequest(
    request: ReinstallServerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.enable_kext is not None:
        output["enable_kext"] = request.enable_kext

    if request.os_id is not None:
        output["os_id"] = request.os_id

    return output


def marshal_StartConnectivityDiagnosticRequest(
    request: StartConnectivityDiagnosticRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.server_id is not None:
        output["server_id"] = request.server_id

    return output


def marshal_UpdateRunnerRequest(
    request: UpdateRunnerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.runner_configuration is not None:
        output["runner_configuration"] = marshal_RunnerConfigurationV2(
            request.runner_configuration, defaults
        )

    return output


def marshal_CommitmentTypeValue(
    request: CommitmentTypeValue,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.commitment_type is not None:
        output["commitment_type"] = request.commitment_type

    return output


def marshal_UpdateServerRequest(
    request: UpdateServerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.schedule_deletion is not None:
        output["schedule_deletion"] = request.schedule_deletion

    if request.enable_vpc is not None:
        output["enable_vpc"] = request.enable_vpc

    if request.commitment_type is not None:
        output["commitment_type"] = marshal_CommitmentTypeValue(
            request.commitment_type, defaults
        )

    if request.public_bandwidth_bps is not None:
        output["public_bandwidth_bps"] = request.public_bandwidth_bps

    if request.applied_runner_configurations is not None:
        output["applied_runner_configurations"] = marshal_AppliedRunnerConfigurations(
            request.applied_runner_configurations, defaults
        )

    return output
