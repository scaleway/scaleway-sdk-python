# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from dateutil import parser
from .types import (
    Permission,
    VolumeType,
    ACLRule,
    ACLRuleRequest,
    AddInstanceACLRulesResponse,
    AddInstanceSettingsResponse,
    BackupSchedule,
    Database,
    DatabaseBackup,
    DatabaseEngine,
    DeleteInstanceACLRulesResponse,
    DeleteInstanceSettingsResponse,
    Endpoint,
    EndpointDirectAccessDetails,
    EndpointLoadBalancerDetails,
    EndpointPrivateNetworkDetails,
    EndpointSpec,
    EndpointSpecLoadBalancer,
    EndpointSpecPrivateNetwork,
    EndpointSpecPrivateNetworkIpamConfig,
    EngineSetting,
    EngineVersion,
    Instance,
    InstanceLog,
    InstanceMetrics,
    InstanceSetting,
    ListDatabaseBackupsResponse,
    ListDatabaseEnginesResponse,
    ListDatabasesResponse,
    ListInstanceACLRulesResponse,
    ListInstanceLogsDetailsResponse,
    ListInstanceLogsDetailsResponseInstanceLogDetail,
    ListInstanceLogsResponse,
    ListInstancesResponse,
    ListNodeTypesResponse,
    ListPrivilegesResponse,
    ListSnapshotsResponse,
    ListUsersResponse,
    LogsPolicy,
    Maintenance,
    NodeType,
    NodeTypeVolumeConstraintSizes,
    NodeTypeVolumeType,
    PrepareInstanceLogsResponse,
    Privilege,
    ReadReplica,
    ReadReplicaEndpointSpec,
    ReadReplicaEndpointSpecDirectAccess,
    ReadReplicaEndpointSpecPrivateNetwork,
    ReadReplicaEndpointSpecPrivateNetworkIpamConfig,
    SetInstanceACLRulesResponse,
    SetInstanceSettingsResponse,
    Snapshot,
    UpgradableVersion,
    User,
    Volume,
    CreateDatabaseBackupRequest,
    UpdateDatabaseBackupRequest,
    RestoreDatabaseBackupRequest,
    UpgradeInstanceRequest,
    CreateInstanceRequest,
    UpdateInstanceRequest,
    CloneInstanceRequest,
    CreateReadReplicaRequest,
    CreateReadReplicaEndpointRequest,
    PrepareInstanceLogsRequest,
    PurgeInstanceLogsRequest,
    AddInstanceSettingsRequest,
    DeleteInstanceSettingsRequest,
    SetInstanceSettingsRequest,
    AddInstanceACLRulesRequest,
    SetInstanceACLRulesRequest,
    DeleteInstanceACLRulesRequest,
    CreateUserRequest,
    UpdateUserRequest,
    CreateDatabaseRequest,
    SetPrivilegeRequest,
    CreateSnapshotRequest,
    UpdateSnapshotRequest,
    CreateInstanceFromSnapshotRequest,
    CreateEndpointRequest,
    MigrateEndpointRequest,
)


def unmarshal_EndpointDirectAccessDetails(data: Any) -> EndpointDirectAccessDetails:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'EndpointDirectAccessDetails' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return EndpointDirectAccessDetails(**args)


def unmarshal_EndpointLoadBalancerDetails(data: Any) -> EndpointLoadBalancerDetails:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'EndpointLoadBalancerDetails' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return EndpointLoadBalancerDetails(**args)


def unmarshal_EndpointPrivateNetworkDetails(data: Any) -> EndpointPrivateNetworkDetails:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'EndpointPrivateNetworkDetails' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_network_id", None)
    args["private_network_id"] = field

    field = data.get("service_ip", None)
    args["service_ip"] = field

    field = data.get("zone", None)
    args["zone"] = field

    return EndpointPrivateNetworkDetails(**args)


def unmarshal_Endpoint(data: Any) -> Endpoint:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Endpoint' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("direct_access", None)
    args["direct_access"] = (
        unmarshal_EndpointDirectAccessDetails(field) if field is not None else None
    )

    field = data.get("hostname", None)
    args["hostname"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("ip", None)
    args["ip"] = field

    field = data.get("load_balancer", None)
    args["load_balancer"] = (
        unmarshal_EndpointLoadBalancerDetails(field) if field is not None else None
    )

    field = data.get("name", None)
    args["name"] = field

    field = data.get("port", None)
    args["port"] = field

    field = data.get("private_network", None)
    args["private_network"] = (
        unmarshal_EndpointPrivateNetworkDetails(field) if field is not None else None
    )

    return Endpoint(**args)


def unmarshal_EngineSetting(data: Any) -> EngineSetting:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'EngineSetting' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("default_value", None)
    args["default_value"] = field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("float_max", None)
    args["float_max"] = field

    field = data.get("float_min", None)
    args["float_min"] = field

    field = data.get("hot_configurable", None)
    args["hot_configurable"] = field

    field = data.get("int_max", None)
    args["int_max"] = field

    field = data.get("int_min", None)
    args["int_min"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("property_type", None)
    args["property_type"] = field

    field = data.get("string_constraint", None)
    args["string_constraint"] = field

    field = data.get("unit", None)
    args["unit"] = field

    return EngineSetting(**args)


def unmarshal_BackupSchedule(data: Any) -> BackupSchedule:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'BackupSchedule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("disabled", None)
    args["disabled"] = field

    field = data.get("frequency", None)
    args["frequency"] = field

    field = data.get("retention", None)
    args["retention"] = field

    return BackupSchedule(**args)


def unmarshal_EngineVersion(data: Any) -> EngineVersion:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'EngineVersion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("available_init_settings", None)
    args["available_init_settings"] = (
        [unmarshal_EngineSetting(v) for v in field] if field is not None else None
    )

    field = data.get("available_settings", None)
    args["available_settings"] = (
        [unmarshal_EngineSetting(v) for v in field] if field is not None else None
    )

    field = data.get("beta", None)
    args["beta"] = field

    field = data.get("disabled", None)
    args["disabled"] = field

    field = data.get("end_of_life", None)
    args["end_of_life"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("version", None)
    args["version"] = field

    return EngineVersion(**args)


def unmarshal_InstanceSetting(data: Any) -> InstanceSetting:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'InstanceSetting' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    args["name"] = field

    field = data.get("value", None)
    args["value"] = field

    return InstanceSetting(**args)


def unmarshal_LogsPolicy(data: Any) -> LogsPolicy:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'LogsPolicy' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("max_age_retention", None)
    args["max_age_retention"] = field

    field = data.get("total_disk_retention", None)
    args["total_disk_retention"] = field

    return LogsPolicy(**args)


def unmarshal_Maintenance(data: Any) -> Maintenance:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Maintenance' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("closed_at", None)
    args["closed_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("reason", None)
    args["reason"] = field

    field = data.get("starts_at", None)
    args["starts_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("stops_at", None)
    args["stops_at"] = parser.isoparse(field) if type(field) is str else field

    return Maintenance(**args)


def unmarshal_NodeTypeVolumeConstraintSizes(data: Any) -> NodeTypeVolumeConstraintSizes:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'NodeTypeVolumeConstraintSizes' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("max_size", None)
    args["max_size"] = field

    field = data.get("min_size", None)
    args["min_size"] = field

    return NodeTypeVolumeConstraintSizes(**args)


def unmarshal_NodeTypeVolumeType(data: Any) -> NodeTypeVolumeType:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'NodeTypeVolumeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("chunk_size", None)
    args["chunk_size"] = field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("max_size", None)
    args["max_size"] = field

    field = data.get("min_size", None)
    args["min_size"] = field

    field = data.get("type", None)
    args["type_"] = field

    return NodeTypeVolumeType(**args)


def unmarshal_ReadReplica(data: Any) -> ReadReplica:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ReadReplica' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("endpoints", None)
    args["endpoints"] = (
        [unmarshal_Endpoint(v) for v in field] if field is not None else None
    )

    field = data.get("id", None)
    args["id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("same_zone", None)
    args["same_zone"] = field

    field = data.get("status", None)
    args["status"] = field

    return ReadReplica(**args)


def unmarshal_UpgradableVersion(data: Any) -> UpgradableVersion:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'UpgradableVersion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("minor_version", None)
    args["minor_version"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("version", None)
    args["version"] = field

    return UpgradableVersion(**args)


def unmarshal_Volume(data: Any) -> Volume:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Volume' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("size", None)
    args["size"] = field

    field = data.get("type", None)
    args["type_"] = field

    return Volume(**args)


def unmarshal_ACLRule(data: Any) -> ACLRule:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ACLRule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("action", None)
    args["action"] = field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("direction", None)
    args["direction"] = field

    field = data.get("ip", None)
    args["ip"] = field

    field = data.get("port", None)
    args["port"] = field

    field = data.get("protocol", None)
    args["protocol"] = field

    return ACLRule(**args)


def unmarshal_Database(data: Any) -> Database:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Database' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("managed", None)
    args["managed"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("owner", None)
    args["owner"] = field

    field = data.get("size", None)
    args["size"] = field

    return Database(**args)


def unmarshal_DatabaseBackup(data: Any) -> DatabaseBackup:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DatabaseBackup' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("database_name", None)
    args["database_name"] = field

    field = data.get("download_url", None)
    args["download_url"] = field

    field = data.get("download_url_expires_at", None)
    args["download_url_expires_at"] = (
        parser.isoparse(field) if type(field) is str else field
    )

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("instance_id", None)
    args["instance_id"] = field

    field = data.get("instance_name", None)
    args["instance_name"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("same_region", None)
    args["same_region"] = field

    field = data.get("size", None)
    args["size"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return DatabaseBackup(**args)


def unmarshal_DatabaseEngine(data: Any) -> DatabaseEngine:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DatabaseEngine' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("logo_url", None)
    args["logo_url"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("versions", None)
    args["versions"] = (
        [unmarshal_EngineVersion(v) for v in field] if field is not None else None
    )

    return DatabaseEngine(**args)


def unmarshal_Instance(data: Any) -> Instance:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Instance' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("backup_same_region", None)
    args["backup_same_region"] = field

    field = data.get("backup_schedule", None)
    args["backup_schedule"] = (
        unmarshal_BackupSchedule(field) if field is not None else None
    )

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("endpoint", None)
    args["endpoint"] = unmarshal_Endpoint(field) if field is not None else None

    field = data.get("endpoints", None)
    args["endpoints"] = (
        [unmarshal_Endpoint(v) for v in field] if field is not None else None
    )

    field = data.get("engine", None)
    args["engine"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("init_settings", None)
    args["init_settings"] = (
        [unmarshal_InstanceSetting(v) for v in field] if field is not None else None
    )

    field = data.get("is_ha_cluster", None)
    args["is_ha_cluster"] = field

    field = data.get("logs_policy", None)
    args["logs_policy"] = unmarshal_LogsPolicy(field) if field is not None else None

    field = data.get("maintenances", None)
    args["maintenances"] = (
        [unmarshal_Maintenance(v) for v in field] if field is not None else None
    )

    field = data.get("name", None)
    args["name"] = field

    field = data.get("node_type", None)
    args["node_type"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("read_replicas", None)
    args["read_replicas"] = (
        [unmarshal_ReadReplica(v) for v in field] if field is not None else None
    )

    field = data.get("region", None)
    args["region"] = field

    field = data.get("settings", None)
    args["settings"] = (
        [unmarshal_InstanceSetting(v) for v in field] if field is not None else None
    )

    field = data.get("status", None)
    args["status"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("upgradable_version", None)
    args["upgradable_version"] = (
        [unmarshal_UpgradableVersion(v) for v in field] if field is not None else None
    )

    field = data.get("volume", None)
    args["volume"] = unmarshal_Volume(field) if field is not None else None

    return Instance(**args)


def unmarshal_InstanceLog(data: Any) -> InstanceLog:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'InstanceLog' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("download_url", None)
    args["download_url"] = field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("node_name", None)
    args["node_name"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("status", None)
    args["status"] = field

    return InstanceLog(**args)


def unmarshal_ListInstanceLogsDetailsResponseInstanceLogDetail(
    data: Any,
) -> ListInstanceLogsDetailsResponseInstanceLogDetail:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListInstanceLogsDetailsResponseInstanceLogDetail' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("log_name", None)
    args["log_name"] = field

    field = data.get("size", None)
    args["size"] = field

    return ListInstanceLogsDetailsResponseInstanceLogDetail(**args)


def unmarshal_NodeType(data: Any) -> NodeType:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'NodeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("available_volume_types", None)
    args["available_volume_types"] = (
        [unmarshal_NodeTypeVolumeType(v) for v in field] if field is not None else None
    )

    field = data.get("beta", None)
    args["beta"] = field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("disabled", None)
    args["disabled"] = field

    field = data.get("generation", None)
    args["generation"] = field

    field = data.get("is_bssd_compatible", None)
    args["is_bssd_compatible"] = field

    field = data.get("is_ha_required", None)
    args["is_ha_required"] = field

    field = data.get("memory", None)
    args["memory"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("stock_status", None)
    args["stock_status"] = field

    field = data.get("vcpus", None)
    args["vcpus"] = field

    field = data.get("volume_constraint", None)
    args["volume_constraint"] = (
        unmarshal_NodeTypeVolumeConstraintSizes(field) if field is not None else None
    )

    return NodeType(**args)


def unmarshal_Privilege(data: Any) -> Privilege:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Privilege' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("database_name", None)
    args["database_name"] = field

    field = data.get("permission", None)
    args["permission"] = field

    field = data.get("user_name", None)
    args["user_name"] = field

    return Privilege(**args)


def unmarshal_Snapshot(data: Any) -> Snapshot:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Snapshot' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("instance_id", None)
    args["instance_id"] = field

    field = data.get("instance_name", None)
    args["instance_name"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("node_type", None)
    args["node_type"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("size", None)
    args["size"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return Snapshot(**args)


def unmarshal_User(data: Any) -> User:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'User' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("is_admin", None)
    args["is_admin"] = field

    field = data.get("name", None)
    args["name"] = field

    return User(**args)


def unmarshal_AddInstanceACLRulesResponse(data: Any) -> AddInstanceACLRulesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'AddInstanceACLRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", None)
    args["rules"] = [unmarshal_ACLRule(v) for v in field] if field is not None else None

    return AddInstanceACLRulesResponse(**args)


def unmarshal_AddInstanceSettingsResponse(data: Any) -> AddInstanceSettingsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'AddInstanceSettingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("settings", None)
    args["settings"] = (
        [unmarshal_InstanceSetting(v) for v in field] if field is not None else None
    )

    return AddInstanceSettingsResponse(**args)


def unmarshal_DeleteInstanceACLRulesResponse(
    data: Any,
) -> DeleteInstanceACLRulesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DeleteInstanceACLRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", None)
    args["rules"] = [unmarshal_ACLRule(v) for v in field] if field is not None else None

    return DeleteInstanceACLRulesResponse(**args)


def unmarshal_DeleteInstanceSettingsResponse(
    data: Any,
) -> DeleteInstanceSettingsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DeleteInstanceSettingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("settings", None)
    args["settings"] = (
        [unmarshal_InstanceSetting(v) for v in field] if field is not None else None
    )

    return DeleteInstanceSettingsResponse(**args)


def unmarshal_InstanceMetrics(data: Any) -> InstanceMetrics:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'InstanceMetrics' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("timeseries", None)
    args["timeseries"] = (
        [unmarshal_TimeSeries(v) for v in field] if field is not None else None
    )

    return InstanceMetrics(**args)


def unmarshal_ListDatabaseBackupsResponse(data: Any) -> ListDatabaseBackupsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDatabaseBackupsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("database_backups", None)
    args["database_backups"] = (
        [unmarshal_DatabaseBackup(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListDatabaseBackupsResponse(**args)


def unmarshal_ListDatabaseEnginesResponse(data: Any) -> ListDatabaseEnginesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDatabaseEnginesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("engines", None)
    args["engines"] = (
        [unmarshal_DatabaseEngine(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListDatabaseEnginesResponse(**args)


def unmarshal_ListDatabasesResponse(data: Any) -> ListDatabasesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDatabasesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("databases", None)
    args["databases"] = (
        [unmarshal_Database(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListDatabasesResponse(**args)


def unmarshal_ListInstanceACLRulesResponse(data: Any) -> ListInstanceACLRulesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListInstanceACLRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", None)
    args["rules"] = [unmarshal_ACLRule(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListInstanceACLRulesResponse(**args)


def unmarshal_ListInstanceLogsDetailsResponse(
    data: Any,
) -> ListInstanceLogsDetailsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListInstanceLogsDetailsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("details", None)
    args["details"] = (
        [unmarshal_ListInstanceLogsDetailsResponseInstanceLogDetail(v) for v in field]
        if field is not None
        else None
    )

    return ListInstanceLogsDetailsResponse(**args)


def unmarshal_ListInstanceLogsResponse(data: Any) -> ListInstanceLogsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListInstanceLogsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("instance_logs", None)
    args["instance_logs"] = (
        [unmarshal_InstanceLog(v) for v in field] if field is not None else None
    )

    return ListInstanceLogsResponse(**args)


def unmarshal_ListInstancesResponse(data: Any) -> ListInstancesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListInstancesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("instances", None)
    args["instances"] = (
        [unmarshal_Instance(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListInstancesResponse(**args)


def unmarshal_ListNodeTypesResponse(data: Any) -> ListNodeTypesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListNodeTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("node_types", None)
    args["node_types"] = (
        [unmarshal_NodeType(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListNodeTypesResponse(**args)


def unmarshal_ListPrivilegesResponse(data: Any) -> ListPrivilegesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListPrivilegesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("privileges", None)
    args["privileges"] = (
        [unmarshal_Privilege(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListPrivilegesResponse(**args)


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


def unmarshal_ListUsersResponse(data: Any) -> ListUsersResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListUsersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    args["total_count"] = field

    field = data.get("users", None)
    args["users"] = [unmarshal_User(v) for v in field] if field is not None else None

    return ListUsersResponse(**args)


def unmarshal_PrepareInstanceLogsResponse(data: Any) -> PrepareInstanceLogsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'PrepareInstanceLogsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("instance_logs", None)
    args["instance_logs"] = (
        [unmarshal_InstanceLog(v) for v in field] if field is not None else None
    )

    return PrepareInstanceLogsResponse(**args)


def unmarshal_SetInstanceACLRulesResponse(data: Any) -> SetInstanceACLRulesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SetInstanceACLRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", None)
    args["rules"] = [unmarshal_ACLRule(v) for v in field] if field is not None else None

    return SetInstanceACLRulesResponse(**args)


def unmarshal_SetInstanceSettingsResponse(data: Any) -> SetInstanceSettingsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SetInstanceSettingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("settings", None)
    args["settings"] = (
        [unmarshal_InstanceSetting(v) for v in field] if field is not None else None
    )

    return SetInstanceSettingsResponse(**args)


def marshal_EndpointSpecPrivateNetworkIpamConfig(
    request: EndpointSpecPrivateNetworkIpamConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {}


def marshal_ReadReplicaEndpointSpecPrivateNetworkIpamConfig(
    request: ReadReplicaEndpointSpecPrivateNetworkIpamConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {}


def marshal_EndpointSpecLoadBalancer(
    request: EndpointSpecLoadBalancer,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {}


def marshal_EndpointSpecPrivateNetwork(
    request: EndpointSpecPrivateNetwork,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "service_ip",
                    request.service_ip if request.service_ip is not None else None,
                ),
                OneOfPossibility(
                    "ipam_config",
                    marshal_EndpointSpecPrivateNetworkIpamConfig(
                        request.ipam_config, defaults
                    )
                    if request.ipam_config is not None
                    else None,
                ),
            ]
        ),
        "private_network_id": request.private_network_id,
    }


def marshal_ReadReplicaEndpointSpecDirectAccess(
    request: ReadReplicaEndpointSpecDirectAccess,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {}


def marshal_ReadReplicaEndpointSpecPrivateNetwork(
    request: ReadReplicaEndpointSpecPrivateNetwork,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "service_ip",
                    request.service_ip if request.service_ip is not None else None,
                ),
                OneOfPossibility(
                    "ipam_config",
                    marshal_ReadReplicaEndpointSpecPrivateNetworkIpamConfig(
                        request.ipam_config, defaults
                    )
                    if request.ipam_config is not None
                    else None,
                ),
            ]
        ),
        "private_network_id": request.private_network_id,
    }


def marshal_ACLRuleRequest(
    request: ACLRuleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "ip": request.ip,
    }


def marshal_EndpointSpec(
    request: EndpointSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "load_balancer",
                    marshal_EndpointSpecLoadBalancer(request.load_balancer, defaults)
                    if request.load_balancer is not None
                    else None,
                ),
                OneOfPossibility(
                    "private_network",
                    marshal_EndpointSpecPrivateNetwork(
                        request.private_network, defaults
                    )
                    if request.private_network is not None
                    else None,
                ),
            ]
        ),
    }


def marshal_InstanceSetting(
    request: InstanceSetting,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name": request.name,
        "value": request.value,
    }


def marshal_LogsPolicy(
    request: LogsPolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "max_age_retention": request.max_age_retention,
        "total_disk_retention": request.total_disk_retention,
    }


def marshal_ReadReplicaEndpointSpec(
    request: ReadReplicaEndpointSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "direct_access",
                    marshal_ReadReplicaEndpointSpecDirectAccess(
                        request.direct_access, defaults
                    )
                    if request.direct_access is not None
                    else None,
                ),
                OneOfPossibility(
                    "private_network",
                    marshal_ReadReplicaEndpointSpecPrivateNetwork(
                        request.private_network, defaults
                    )
                    if request.private_network is not None
                    else None,
                ),
            ]
        ),
    }


def marshal_AddInstanceACLRulesRequest(
    request: AddInstanceACLRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "rules": [marshal_ACLRuleRequest(v, defaults) for v in request.rules],
    }


def marshal_AddInstanceSettingsRequest(
    request: AddInstanceSettingsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "settings": [marshal_InstanceSetting(v, defaults) for v in request.settings],
    }


def marshal_CloneInstanceRequest(
    request: CloneInstanceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name": request.name,
        "node_type": request.node_type,
    }


def marshal_CreateDatabaseBackupRequest(
    request: CreateDatabaseBackupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "database_name": request.database_name,
        "expires_at": request.expires_at,
        "instance_id": request.instance_id,
        "name": request.name,
    }


def marshal_CreateDatabaseRequest(
    request: CreateDatabaseRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name": request.name,
    }


def marshal_CreateEndpointRequest(
    request: CreateEndpointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "endpoint_spec": marshal_EndpointSpec(request.endpoint_spec, defaults)
        if request.endpoint_spec is not None
        else None,
    }


def marshal_CreateInstanceFromSnapshotRequest(
    request: CreateInstanceFromSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "instance_name": request.instance_name,
        "is_ha_cluster": request.is_ha_cluster,
        "node_type": request.node_type,
    }


def marshal_CreateInstanceRequest(
    request: CreateInstanceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "project_id",
                    request.project_id or defaults.default_project_id
                    if request.project_id is not None
                    else None,
                    defaults.default_project_id,
                ),
                OneOfPossibility(
                    "organization_id",
                    request.organization_id or defaults.default_organization_id
                    if request.organization_id is not None
                    else None,
                    defaults.default_organization_id,
                ),
            ]
        ),
        "backup_same_region": request.backup_same_region,
        "disable_backup": request.disable_backup,
        "engine": request.engine,
        "init_endpoints": [
            marshal_EndpointSpec(v, defaults) for v in request.init_endpoints
        ]
        if request.init_endpoints is not None
        else None,
        "init_settings": [
            marshal_InstanceSetting(v, defaults) for v in request.init_settings
        ]
        if request.init_settings is not None
        else None,
        "is_ha_cluster": request.is_ha_cluster,
        "name": request.name,
        "node_type": request.node_type,
        "password": request.password,
        "tags": request.tags,
        "user_name": request.user_name,
        "volume_size": request.volume_size,
        "volume_type": VolumeType(request.volume_type),
    }


def marshal_CreateReadReplicaEndpointRequest(
    request: CreateReadReplicaEndpointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "endpoint_spec": [
            marshal_ReadReplicaEndpointSpec(v, defaults) for v in request.endpoint_spec
        ],
    }


def marshal_CreateReadReplicaRequest(
    request: CreateReadReplicaRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "endpoint_spec": [
            marshal_ReadReplicaEndpointSpec(v, defaults) for v in request.endpoint_spec
        ]
        if request.endpoint_spec is not None
        else None,
        "instance_id": request.instance_id,
        "same_zone": request.same_zone,
    }


def marshal_CreateSnapshotRequest(
    request: CreateSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "expires_at": request.expires_at,
        "name": request.name,
    }


def marshal_CreateUserRequest(
    request: CreateUserRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "is_admin": request.is_admin,
        "name": request.name,
        "password": request.password,
    }


def marshal_DeleteInstanceACLRulesRequest(
    request: DeleteInstanceACLRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "acl_rule_ips": request.acl_rule_ips,
    }


def marshal_DeleteInstanceSettingsRequest(
    request: DeleteInstanceSettingsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "setting_names": request.setting_names,
    }


def marshal_MigrateEndpointRequest(
    request: MigrateEndpointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "instance_id": request.instance_id,
    }


def marshal_PrepareInstanceLogsRequest(
    request: PrepareInstanceLogsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "end_date": request.end_date,
        "start_date": request.start_date,
    }


def marshal_PurgeInstanceLogsRequest(
    request: PurgeInstanceLogsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "log_name": request.log_name,
    }


def marshal_RestoreDatabaseBackupRequest(
    request: RestoreDatabaseBackupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "database_name": request.database_name,
        "instance_id": request.instance_id,
    }


def marshal_SetInstanceACLRulesRequest(
    request: SetInstanceACLRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "rules": [marshal_ACLRuleRequest(v, defaults) for v in request.rules],
    }


def marshal_SetInstanceSettingsRequest(
    request: SetInstanceSettingsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "settings": [marshal_InstanceSetting(v, defaults) for v in request.settings],
    }


def marshal_SetPrivilegeRequest(
    request: SetPrivilegeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "database_name": request.database_name,
        "permission": Permission(request.permission),
        "user_name": request.user_name,
    }


def marshal_UpdateDatabaseBackupRequest(
    request: UpdateDatabaseBackupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "expires_at": request.expires_at,
        "name": request.name,
    }


def marshal_UpdateInstanceRequest(
    request: UpdateInstanceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "backup_same_region": request.backup_same_region,
        "backup_schedule_frequency": request.backup_schedule_frequency,
        "backup_schedule_retention": request.backup_schedule_retention,
        "is_backup_schedule_disabled": request.is_backup_schedule_disabled,
        "logs_policy": marshal_LogsPolicy(request.logs_policy, defaults)
        if request.logs_policy is not None
        else None,
        "name": request.name,
        "tags": request.tags,
    }


def marshal_UpdateSnapshotRequest(
    request: UpdateSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "expires_at": request.expires_at,
        "name": request.name,
    }


def marshal_UpdateUserRequest(
    request: UpdateUserRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "is_admin": request.is_admin,
        "password": request.password,
    }


def marshal_UpgradeInstanceRequest(
    request: UpgradeInstanceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "node_type",
                    request.node_type if request.node_type is not None else None,
                ),
                OneOfPossibility(
                    "enable_ha",
                    request.enable_ha if request.enable_ha is not None else None,
                ),
                OneOfPossibility(
                    "volume_size",
                    request.volume_size if request.volume_size is not None else None,
                ),
                OneOfPossibility(
                    "volume_type",
                    VolumeType(request.volume_type)
                    if request.volume_type is not None
                    else None,
                ),
                OneOfPossibility(
                    "upgradable_version_id",
                    request.upgradable_version_id
                    if request.upgradable_version_id is not None
                    else None,
                ),
            ]
        ),
    }
