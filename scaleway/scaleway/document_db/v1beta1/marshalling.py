# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    EndpointDirectAccessDetails,
    EndpointLoadBalancerDetails,
    EndpointPrivateNetworkDetails,
    Endpoint,
    Maintenance,
    ReadReplica,
    Database,
    InstanceLog,
    BackupSchedule,
    InstanceSetting,
    LogsPolicy,
    UpgradableVersion,
    Volume,
    Instance,
    Privilege,
    SnapshotVolumeType,
    Snapshot,
    User,
    ACLRule,
    AddInstanceACLRulesResponse,
    AddInstanceSettingsResponse,
    DeleteInstanceACLRulesResponse,
    DeleteInstanceSettingsResponse,
    InstanceMetrics,
    EngineSetting,
    EngineVersion,
    DatabaseEngine,
    ListDatabaseEnginesResponse,
    ListDatabasesResponse,
    ListInstanceACLRulesResponse,
    ListInstanceLogsDetailsResponseInstanceLogDetail,
    ListInstanceLogsDetailsResponse,
    ListInstanceLogsResponse,
    ListInstancesResponse,
    NodeTypeVolumeConstraintSizes,
    NodeTypeVolumeType,
    NodeType,
    ListNodeTypesResponse,
    ListPrivilegesResponse,
    ListSnapshotsResponse,
    ListUsersResponse,
    SetInstanceACLRulesResponse,
    SetInstanceSettingsResponse,
    ACLRuleRequest,
    AddInstanceACLRulesRequest,
    AddInstanceSettingsRequest,
    CloneInstanceRequest,
    CreateDatabaseRequest,
    EndpointSpecPrivateNetworkIpamConfig,
    EndpointSpecLoadBalancer,
    EndpointSpecPrivateNetwork,
    EndpointSpec,
    CreateEndpointRequest,
    CreateInstanceFromSnapshotRequest,
    CreateInstanceRequest,
    ReadReplicaEndpointSpecPrivateNetworkIpamConfig,
    ReadReplicaEndpointSpecDirectAccess,
    ReadReplicaEndpointSpecPrivateNetwork,
    ReadReplicaEndpointSpec,
    CreateReadReplicaEndpointRequest,
    CreateReadReplicaRequest,
    CreateSnapshotRequest,
    CreateUserRequest,
    DeleteInstanceACLRulesRequest,
    DeleteInstanceSettingsRequest,
    MigrateEndpointRequest,
    PurgeInstanceLogsRequest,
    SetInstanceACLRulesRequest,
    SetInstanceSettingsRequest,
    SetPrivilegeRequest,
    UpdateInstanceRequest,
    UpdateSnapshotRequest,
    UpdateUserRequest,
    UpgradeInstanceRequestMajorUpgradeWorkflow,
    UpgradeInstanceRequest,
)


def unmarshal_EndpointDirectAccessDetails(data: Any) -> EndpointDirectAccessDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EndpointDirectAccessDetails' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return EndpointDirectAccessDetails(**args)


def unmarshal_EndpointLoadBalancerDetails(data: Any) -> EndpointLoadBalancerDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EndpointLoadBalancerDetails' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return EndpointLoadBalancerDetails(**args)


def unmarshal_EndpointPrivateNetworkDetails(data: Any) -> EndpointPrivateNetworkDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EndpointPrivateNetworkDetails' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field

    field = data.get("service_ip", None)
    if field is not None:
        args["service_ip"] = field

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field

    return EndpointPrivateNetworkDetails(**args)


def unmarshal_Endpoint(data: Any) -> Endpoint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Endpoint' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("port", None)
    if field is not None:
        args["port"] = field

    field = data.get("ip", None)
    if field is not None:
        args["ip"] = field
    else:
        args["ip"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("private_network", None)
    if field is not None:
        args["private_network"] = unmarshal_EndpointPrivateNetworkDetails(field)
    else:
        args["private_network"] = None

    field = data.get("load_balancer", None)
    if field is not None:
        args["load_balancer"] = unmarshal_EndpointLoadBalancerDetails(field)
    else:
        args["load_balancer"] = None

    field = data.get("direct_access", None)
    if field is not None:
        args["direct_access"] = unmarshal_EndpointDirectAccessDetails(field)
    else:
        args["direct_access"] = None

    field = data.get("hostname", None)
    if field is not None:
        args["hostname"] = field
    else:
        args["hostname"] = None

    return Endpoint(**args)


def unmarshal_Maintenance(data: Any) -> Maintenance:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Maintenance' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("reason", None)
    if field is not None:
        args["reason"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("starts_at", None)
    if field is not None:
        args["starts_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["starts_at"] = None

    field = data.get("stops_at", None)
    if field is not None:
        args["stops_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["stops_at"] = None

    field = data.get("closed_at", None)
    if field is not None:
        args["closed_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["closed_at"] = None

    field = data.get("forced_at", None)
    if field is not None:
        args["forced_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["forced_at"] = None

    return Maintenance(**args)


def unmarshal_ReadReplica(data: Any) -> ReadReplica:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ReadReplica' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("endpoints", None)
    if field is not None:
        args["endpoints"] = (
            [unmarshal_Endpoint(v) for v in field] if field is not None else None
        )

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("same_zone", None)
    if field is not None:
        args["same_zone"] = field

    return ReadReplica(**args)


def unmarshal_Database(data: Any) -> Database:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Database' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("owner", None)
    if field is not None:
        args["owner"] = field

    field = data.get("managed", None)
    if field is not None:
        args["managed"] = field

    field = data.get("size", None)
    if field is not None:
        args["size"] = field

    return Database(**args)


def unmarshal_InstanceLog(data: Any) -> InstanceLog:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstanceLog' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("node_name", None)
    if field is not None:
        args["node_name"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("download_url", None)
    if field is not None:
        args["download_url"] = field
    else:
        args["download_url"] = None

    field = data.get("expires_at", None)
    if field is not None:
        args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["expires_at"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    return InstanceLog(**args)


def unmarshal_BackupSchedule(data: Any) -> BackupSchedule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BackupSchedule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("frequency", None)
    if field is not None:
        args["frequency"] = field

    field = data.get("retention", None)
    if field is not None:
        args["retention"] = field

    field = data.get("disabled", None)
    if field is not None:
        args["disabled"] = field

    field = data.get("next_run_at", None)
    if field is not None:
        args["next_run_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["next_run_at"] = None

    return BackupSchedule(**args)


def unmarshal_InstanceSetting(data: Any) -> InstanceSetting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstanceSetting' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("value", None)
    if field is not None:
        args["value"] = field

    return InstanceSetting(**args)


def unmarshal_LogsPolicy(data: Any) -> LogsPolicy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LogsPolicy' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("max_age_retention", None)
    if field is not None:
        args["max_age_retention"] = field
    else:
        args["max_age_retention"] = None

    field = data.get("total_disk_retention", None)
    if field is not None:
        args["total_disk_retention"] = field
    else:
        args["total_disk_retention"] = None

    return LogsPolicy(**args)


def unmarshal_UpgradableVersion(data: Any) -> UpgradableVersion:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpgradableVersion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("version", None)
    if field is not None:
        args["version"] = field

    field = data.get("minor_version", None)
    if field is not None:
        args["minor_version"] = field

    return UpgradableVersion(**args)


def unmarshal_Volume(data: Any) -> Volume:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Volume' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("size", None)
    if field is not None:
        args["size"] = field

    field = data.get("class", None)
    if field is not None:
        args["class_"] = field

    return Volume(**args)


def unmarshal_Instance(data: Any) -> Instance:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Instance' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("volume", None)
    if field is not None:
        args["volume"] = unmarshal_Volume(field)
    else:
        args["volume"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("engine", None)
    if field is not None:
        args["engine"] = field

    field = data.get("upgradable_version", None)
    if field is not None:
        args["upgradable_version"] = (
            [unmarshal_UpgradableVersion(v) for v in field]
            if field is not None
            else None
        )

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("settings", None)
    if field is not None:
        args["settings"] = (
            [unmarshal_InstanceSetting(v) for v in field] if field is not None else None
        )

    field = data.get("is_ha_cluster", None)
    if field is not None:
        args["is_ha_cluster"] = field

    field = data.get("endpoint", None)
    if field is not None:
        args["endpoint"] = unmarshal_Endpoint(field)
    else:
        args["endpoint"] = None

    field = data.get("backup_schedule", None)
    if field is not None:
        args["backup_schedule"] = unmarshal_BackupSchedule(field)
    else:
        args["backup_schedule"] = None

    field = data.get("read_replicas", None)
    if field is not None:
        args["read_replicas"] = (
            [unmarshal_ReadReplica(v) for v in field] if field is not None else None
        )

    field = data.get("node_type", None)
    if field is not None:
        args["node_type"] = field

    field = data.get("init_settings", None)
    if field is not None:
        args["init_settings"] = (
            [unmarshal_InstanceSetting(v) for v in field] if field is not None else None
        )

    field = data.get("endpoints", None)
    if field is not None:
        args["endpoints"] = (
            [unmarshal_Endpoint(v) for v in field] if field is not None else None
        )

    field = data.get("backup_same_region", None)
    if field is not None:
        args["backup_same_region"] = field

    field = data.get("maintenances", None)
    if field is not None:
        args["maintenances"] = (
            [unmarshal_Maintenance(v) for v in field] if field is not None else None
        )

    field = data.get("logs_policy", None)
    if field is not None:
        args["logs_policy"] = unmarshal_LogsPolicy(field)
    else:
        args["logs_policy"] = None

    return Instance(**args)


def unmarshal_Privilege(data: Any) -> Privilege:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Privilege' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("permission", None)
    if field is not None:
        args["permission"] = field

    field = data.get("database_name", None)
    if field is not None:
        args["database_name"] = field

    field = data.get("user_name", None)
    if field is not None:
        args["user_name"] = field

    return Privilege(**args)


def unmarshal_SnapshotVolumeType(data: Any) -> SnapshotVolumeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SnapshotVolumeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("class", None)
    if field is not None:
        args["class_"] = field

    return SnapshotVolumeType(**args)


def unmarshal_Snapshot(data: Any) -> Snapshot:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Snapshot' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("instance_id", None)
    if field is not None:
        args["instance_id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("instance_name", None)
    if field is not None:
        args["instance_name"] = field

    field = data.get("node_type", None)
    if field is not None:
        args["node_type"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = None

    field = data.get("expires_at", None)
    if field is not None:
        args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["expires_at"] = None

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

    field = data.get("volume_type", None)
    if field is not None:
        args["volume_type"] = unmarshal_SnapshotVolumeType(field)
    else:
        args["volume_type"] = None

    return Snapshot(**args)


def unmarshal_User(data: Any) -> User:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'User' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("is_admin", None)
    if field is not None:
        args["is_admin"] = field

    return User(**args)


def unmarshal_ACLRule(data: Any) -> ACLRule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ACLRule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip", None)
    if field is not None:
        args["ip"] = field

    field = data.get("protocol", None)
    if field is not None:
        args["protocol"] = field

    field = data.get("direction", None)
    if field is not None:
        args["direction"] = field

    field = data.get("action", None)
    if field is not None:
        args["action"] = field

    field = data.get("description", None)
    if field is not None:
        args["description"] = field

    field = data.get("port", None)
    if field is not None:
        args["port"] = field
    else:
        args["port"] = None

    return ACLRule(**args)


def unmarshal_AddInstanceACLRulesResponse(data: Any) -> AddInstanceACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddInstanceACLRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", None)
    if field is not None:
        args["rules"] = (
            [unmarshal_ACLRule(v) for v in field] if field is not None else None
        )

    return AddInstanceACLRulesResponse(**args)


def unmarshal_AddInstanceSettingsResponse(data: Any) -> AddInstanceSettingsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddInstanceSettingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("settings", None)
    if field is not None:
        args["settings"] = (
            [unmarshal_InstanceSetting(v) for v in field] if field is not None else None
        )

    return AddInstanceSettingsResponse(**args)


def unmarshal_DeleteInstanceACLRulesResponse(
    data: Any,
) -> DeleteInstanceACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeleteInstanceACLRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", None)
    if field is not None:
        args["rules"] = (
            [unmarshal_ACLRule(v) for v in field] if field is not None else None
        )

    return DeleteInstanceACLRulesResponse(**args)


def unmarshal_DeleteInstanceSettingsResponse(
    data: Any,
) -> DeleteInstanceSettingsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeleteInstanceSettingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("settings", None)
    if field is not None:
        args["settings"] = (
            [unmarshal_InstanceSetting(v) for v in field] if field is not None else None
        )

    return DeleteInstanceSettingsResponse(**args)


def unmarshal_InstanceMetrics(data: Any) -> InstanceMetrics:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstanceMetrics' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("timeseries", None)
    if field is not None:
        args["timeseries"] = (
            [unmarshal_TimeSeries(v) for v in field] if field is not None else None
        )

    return InstanceMetrics(**args)


def unmarshal_EngineSetting(data: Any) -> EngineSetting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EngineSetting' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("default_value", None)
    if field is not None:
        args["default_value"] = field

    field = data.get("hot_configurable", None)
    if field is not None:
        args["hot_configurable"] = field

    field = data.get("description", None)
    if field is not None:
        args["description"] = field

    field = data.get("property_type", None)
    if field is not None:
        args["property_type"] = field

    field = data.get("unit", None)
    if field is not None:
        args["unit"] = field
    else:
        args["unit"] = None

    field = data.get("string_constraint", None)
    if field is not None:
        args["string_constraint"] = field
    else:
        args["string_constraint"] = None

    field = data.get("int_min", None)
    if field is not None:
        args["int_min"] = field
    else:
        args["int_min"] = None

    field = data.get("int_max", None)
    if field is not None:
        args["int_max"] = field
    else:
        args["int_max"] = None

    field = data.get("float_min", None)
    if field is not None:
        args["float_min"] = field
    else:
        args["float_min"] = None

    field = data.get("float_max", None)
    if field is not None:
        args["float_max"] = field
    else:
        args["float_max"] = None

    return EngineSetting(**args)


def unmarshal_EngineVersion(data: Any) -> EngineVersion:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EngineVersion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("version", None)
    if field is not None:
        args["version"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("available_settings", None)
    if field is not None:
        args["available_settings"] = (
            [unmarshal_EngineSetting(v) for v in field] if field is not None else None
        )

    field = data.get("disabled", None)
    if field is not None:
        args["disabled"] = field

    field = data.get("beta", None)
    if field is not None:
        args["beta"] = field

    field = data.get("available_init_settings", None)
    if field is not None:
        args["available_init_settings"] = (
            [unmarshal_EngineSetting(v) for v in field] if field is not None else None
        )

    field = data.get("end_of_life", None)
    if field is not None:
        args["end_of_life"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["end_of_life"] = None

    return EngineVersion(**args)


def unmarshal_DatabaseEngine(data: Any) -> DatabaseEngine:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DatabaseEngine' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("logo_url", None)
    if field is not None:
        args["logo_url"] = field

    field = data.get("versions", None)
    if field is not None:
        args["versions"] = (
            [unmarshal_EngineVersion(v) for v in field] if field is not None else None
        )

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    return DatabaseEngine(**args)


def unmarshal_ListDatabaseEnginesResponse(data: Any) -> ListDatabaseEnginesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatabaseEnginesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("engines", None)
    if field is not None:
        args["engines"] = (
            [unmarshal_DatabaseEngine(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListDatabaseEnginesResponse(**args)


def unmarshal_ListDatabasesResponse(data: Any) -> ListDatabasesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatabasesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("databases", None)
    if field is not None:
        args["databases"] = (
            [unmarshal_Database(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListDatabasesResponse(**args)


def unmarshal_ListInstanceACLRulesResponse(data: Any) -> ListInstanceACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstanceACLRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", None)
    if field is not None:
        args["rules"] = (
            [unmarshal_ACLRule(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListInstanceACLRulesResponse(**args)


def unmarshal_ListInstanceLogsDetailsResponseInstanceLogDetail(
    data: Any,
) -> ListInstanceLogsDetailsResponseInstanceLogDetail:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstanceLogsDetailsResponseInstanceLogDetail' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("log_name", None)
    if field is not None:
        args["log_name"] = field

    field = data.get("size", None)
    if field is not None:
        args["size"] = field

    return ListInstanceLogsDetailsResponseInstanceLogDetail(**args)


def unmarshal_ListInstanceLogsDetailsResponse(
    data: Any,
) -> ListInstanceLogsDetailsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstanceLogsDetailsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("details", None)
    if field is not None:
        args["details"] = (
            [
                unmarshal_ListInstanceLogsDetailsResponseInstanceLogDetail(v)
                for v in field
            ]
            if field is not None
            else None
        )

    return ListInstanceLogsDetailsResponse(**args)


def unmarshal_ListInstanceLogsResponse(data: Any) -> ListInstanceLogsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstanceLogsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("instance_logs", None)
    if field is not None:
        args["instance_logs"] = (
            [unmarshal_InstanceLog(v) for v in field] if field is not None else None
        )

    return ListInstanceLogsResponse(**args)


def unmarshal_ListInstancesResponse(data: Any) -> ListInstancesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstancesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("instances", None)
    if field is not None:
        args["instances"] = (
            [unmarshal_Instance(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListInstancesResponse(**args)


def unmarshal_NodeTypeVolumeConstraintSizes(data: Any) -> NodeTypeVolumeConstraintSizes:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeTypeVolumeConstraintSizes' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("min_size", None)
    if field is not None:
        args["min_size"] = field

    field = data.get("max_size", None)
    if field is not None:
        args["max_size"] = field

    return NodeTypeVolumeConstraintSizes(**args)


def unmarshal_NodeTypeVolumeType(data: Any) -> NodeTypeVolumeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeTypeVolumeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("description", None)
    if field is not None:
        args["description"] = field

    field = data.get("min_size", None)
    if field is not None:
        args["min_size"] = field

    field = data.get("max_size", None)
    if field is not None:
        args["max_size"] = field

    field = data.get("chunk_size", None)
    if field is not None:
        args["chunk_size"] = field

    field = data.get("class", None)
    if field is not None:
        args["class_"] = field

    return NodeTypeVolumeType(**args)


def unmarshal_NodeType(data: Any) -> NodeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("stock_status", None)
    if field is not None:
        args["stock_status"] = field

    field = data.get("description", None)
    if field is not None:
        args["description"] = field

    field = data.get("vcpus", None)
    if field is not None:
        args["vcpus"] = field

    field = data.get("memory", None)
    if field is not None:
        args["memory"] = field

    field = data.get("disabled", None)
    if field is not None:
        args["disabled"] = field

    field = data.get("beta", None)
    if field is not None:
        args["beta"] = field

    field = data.get("volume_constraint", None)
    if field is not None:
        args["volume_constraint"] = unmarshal_NodeTypeVolumeConstraintSizes(field)
    else:
        args["volume_constraint"] = None

    field = data.get("is_bssd_compatible", None)
    if field is not None:
        args["is_bssd_compatible"] = field
    else:
        args["is_bssd_compatible"] = None

    field = data.get("available_volume_types", None)
    if field is not None:
        args["available_volume_types"] = (
            [unmarshal_NodeTypeVolumeType(v) for v in field]
            if field is not None
            else None
        )

    field = data.get("is_ha_required", None)
    if field is not None:
        args["is_ha_required"] = field

    field = data.get("generation", None)
    if field is not None:
        args["generation"] = field

    field = data.get("instance_range", None)
    if field is not None:
        args["instance_range"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    return NodeType(**args)


def unmarshal_ListNodeTypesResponse(data: Any) -> ListNodeTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNodeTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("node_types", None)
    if field is not None:
        args["node_types"] = (
            [unmarshal_NodeType(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListNodeTypesResponse(**args)


def unmarshal_ListPrivilegesResponse(data: Any) -> ListPrivilegesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPrivilegesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("privileges", None)
    if field is not None:
        args["privileges"] = (
            [unmarshal_Privilege(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListPrivilegesResponse(**args)


def unmarshal_ListSnapshotsResponse(data: Any) -> ListSnapshotsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSnapshotsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshots", None)
    if field is not None:
        args["snapshots"] = (
            [unmarshal_Snapshot(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListSnapshotsResponse(**args)


def unmarshal_ListUsersResponse(data: Any) -> ListUsersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListUsersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("users", None)
    if field is not None:
        args["users"] = (
            [unmarshal_User(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListUsersResponse(**args)


def unmarshal_SetInstanceACLRulesResponse(data: Any) -> SetInstanceACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetInstanceACLRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", None)
    if field is not None:
        args["rules"] = (
            [unmarshal_ACLRule(v) for v in field] if field is not None else None
        )

    return SetInstanceACLRulesResponse(**args)


def unmarshal_SetInstanceSettingsResponse(data: Any) -> SetInstanceSettingsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetInstanceSettingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("settings", None)
    if field is not None:
        args["settings"] = (
            [unmarshal_InstanceSetting(v) for v in field] if field is not None else None
        )

    return SetInstanceSettingsResponse(**args)


def marshal_ACLRuleRequest(
    request: ACLRuleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip is not None:
        output["ip"] = request.ip

    if request.description is not None:
        output["description"] = request.description

    return output


def marshal_AddInstanceACLRulesRequest(
    request: AddInstanceACLRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.rules is not None:
        output["rules"] = [
            marshal_ACLRuleRequest(item, defaults) for item in request.rules
        ]

    return output


def marshal_InstanceSetting(
    request: InstanceSetting,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.value is not None:
        output["value"] = request.value

    return output


def marshal_AddInstanceSettingsRequest(
    request: AddInstanceSettingsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.settings is not None:
        output["settings"] = [
            marshal_InstanceSetting(item, defaults) for item in request.settings
        ]

    return output


def marshal_CloneInstanceRequest(
    request: CloneInstanceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.node_type is not None:
        output["node_type"] = request.node_type

    return output


def marshal_CreateDatabaseRequest(
    request: CreateDatabaseRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_EndpointSpecPrivateNetworkIpamConfig(
    request: EndpointSpecPrivateNetworkIpamConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    return output


def marshal_EndpointSpecLoadBalancer(
    request: EndpointSpecLoadBalancer,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    return output


def marshal_EndpointSpecPrivateNetwork(
    request: EndpointSpecPrivateNetwork,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("service_ip", request.service_ip),
                OneOfPossibility("ipam_config", request.ipam_config),
            ]
        ),
    )

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    return output


def marshal_EndpointSpec(
    request: EndpointSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("load_balancer", request.load_balancer),
                OneOfPossibility("private_network", request.private_network),
            ]
        ),
    )

    return output


def marshal_CreateEndpointRequest(
    request: CreateEndpointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.endpoint_spec is not None:
        output["endpoint_spec"] = marshal_EndpointSpec(request.endpoint_spec, defaults)

    return output


def marshal_CreateInstanceFromSnapshotRequest(
    request: CreateInstanceFromSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.instance_name is not None:
        output["instance_name"] = request.instance_name

    if request.is_ha_cluster is not None:
        output["is_ha_cluster"] = request.is_ha_cluster

    if request.node_type is not None:
        output["node_type"] = request.node_type

    return output


def marshal_CreateInstanceRequest(
    request: CreateInstanceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "organization_id",
                    request.organization_id,
                    defaults.default_organization_id,
                ),
                OneOfPossibility(
                    "project_id", request.project_id, defaults.default_project_id
                ),
            ]
        ),
    )

    if request.engine is not None:
        output["engine"] = request.engine

    if request.user_name is not None:
        output["user_name"] = request.user_name

    if request.password is not None:
        output["password"] = request.password

    if request.node_type is not None:
        output["node_type"] = request.node_type

    if request.name is not None:
        output["name"] = request.name

    if request.is_ha_cluster is not None:
        output["is_ha_cluster"] = request.is_ha_cluster

    if request.disable_backup is not None:
        output["disable_backup"] = request.disable_backup

    if request.volume_size is not None:
        output["volume_size"] = request.volume_size

    if request.backup_same_region is not None:
        output["backup_same_region"] = request.backup_same_region

    if request.tags is not None:
        output["tags"] = request.tags

    if request.init_settings is not None:
        output["init_settings"] = [
            marshal_InstanceSetting(item, defaults) for item in request.init_settings
        ]

    if request.volume_type is not None:
        output["volume_type"] = str(request.volume_type)

    if request.init_endpoints is not None:
        output["init_endpoints"] = [
            marshal_EndpointSpec(item, defaults) for item in request.init_endpoints
        ]

    return output


def marshal_ReadReplicaEndpointSpecPrivateNetworkIpamConfig(
    request: ReadReplicaEndpointSpecPrivateNetworkIpamConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    return output


def marshal_ReadReplicaEndpointSpecDirectAccess(
    request: ReadReplicaEndpointSpecDirectAccess,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    return output


def marshal_ReadReplicaEndpointSpecPrivateNetwork(
    request: ReadReplicaEndpointSpecPrivateNetwork,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("service_ip", request.service_ip),
                OneOfPossibility("ipam_config", request.ipam_config),
            ]
        ),
    )

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    return output


def marshal_ReadReplicaEndpointSpec(
    request: ReadReplicaEndpointSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("direct_access", request.direct_access),
                OneOfPossibility("private_network", request.private_network),
            ]
        ),
    )

    return output


def marshal_CreateReadReplicaEndpointRequest(
    request: CreateReadReplicaEndpointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.endpoint_spec is not None:
        output["endpoint_spec"] = [
            marshal_ReadReplicaEndpointSpec(item, defaults)
            for item in request.endpoint_spec
        ]

    return output


def marshal_CreateReadReplicaRequest(
    request: CreateReadReplicaRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.instance_id is not None:
        output["instance_id"] = request.instance_id

    if request.endpoint_spec is not None:
        output["endpoint_spec"] = [
            marshal_ReadReplicaEndpointSpec(item, defaults)
            for item in request.endpoint_spec
        ]

    if request.same_zone is not None:
        output["same_zone"] = request.same_zone

    return output


def marshal_CreateSnapshotRequest(
    request: CreateSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()

    return output


def marshal_CreateUserRequest(
    request: CreateUserRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.password is not None:
        output["password"] = request.password

    if request.is_admin is not None:
        output["is_admin"] = request.is_admin

    return output


def marshal_DeleteInstanceACLRulesRequest(
    request: DeleteInstanceACLRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.acl_rule_ips is not None:
        output["acl_rule_ips"] = request.acl_rule_ips

    return output


def marshal_DeleteInstanceSettingsRequest(
    request: DeleteInstanceSettingsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.setting_names is not None:
        output["setting_names"] = request.setting_names

    return output


def marshal_MigrateEndpointRequest(
    request: MigrateEndpointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.instance_id is not None:
        output["instance_id"] = request.instance_id

    return output


def marshal_PurgeInstanceLogsRequest(
    request: PurgeInstanceLogsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.log_name is not None:
        output["log_name"] = request.log_name

    return output


def marshal_SetInstanceACLRulesRequest(
    request: SetInstanceACLRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.rules is not None:
        output["rules"] = [
            marshal_ACLRuleRequest(item, defaults) for item in request.rules
        ]

    return output


def marshal_SetInstanceSettingsRequest(
    request: SetInstanceSettingsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.settings is not None:
        output["settings"] = [
            marshal_InstanceSetting(item, defaults) for item in request.settings
        ]

    return output


def marshal_SetPrivilegeRequest(
    request: SetPrivilegeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.database_name is not None:
        output["database_name"] = request.database_name

    if request.user_name is not None:
        output["user_name"] = request.user_name

    if request.permission is not None:
        output["permission"] = str(request.permission)

    return output


def marshal_LogsPolicy(
    request: LogsPolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.max_age_retention is not None:
        output["max_age_retention"] = request.max_age_retention

    if request.total_disk_retention is not None:
        output["total_disk_retention"] = request.total_disk_retention

    return output


def marshal_UpdateInstanceRequest(
    request: UpdateInstanceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.backup_schedule_frequency is not None:
        output["backup_schedule_frequency"] = request.backup_schedule_frequency

    if request.backup_schedule_retention is not None:
        output["backup_schedule_retention"] = request.backup_schedule_retention

    if request.is_backup_schedule_disabled is not None:
        output["is_backup_schedule_disabled"] = request.is_backup_schedule_disabled

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.logs_policy is not None:
        output["logs_policy"] = marshal_LogsPolicy(request.logs_policy, defaults)

    if request.backup_same_region is not None:
        output["backup_same_region"] = request.backup_same_region

    if request.backup_schedule_start_hour is not None:
        output["backup_schedule_start_hour"] = request.backup_schedule_start_hour

    return output


def marshal_UpdateSnapshotRequest(
    request: UpdateSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()

    return output


def marshal_UpdateUserRequest(
    request: UpdateUserRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.password is not None:
        output["password"] = request.password

    if request.is_admin is not None:
        output["is_admin"] = request.is_admin

    return output


def marshal_UpgradeInstanceRequestMajorUpgradeWorkflow(
    request: UpgradeInstanceRequestMajorUpgradeWorkflow,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.upgradable_version_id is not None:
        output["upgradable_version_id"] = request.upgradable_version_id

    if request.with_endpoints is not None:
        output["with_endpoints"] = request.with_endpoints

    return output


def marshal_UpgradeInstanceRequest(
    request: UpgradeInstanceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("node_type", request.node_type),
                OneOfPossibility("enable_ha", request.enable_ha),
                OneOfPossibility("volume_size", request.volume_size),
                OneOfPossibility("volume_type", request.volume_type),
                OneOfPossibility(
                    "upgradable_version_id", request.upgradable_version_id
                ),
                OneOfPossibility(
                    "major_upgrade_workflow", request.major_upgrade_workflow
                ),
            ]
        ),
    )

    return output
