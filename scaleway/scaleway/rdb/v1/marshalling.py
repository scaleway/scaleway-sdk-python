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
from .types import (
    ACLRuleAction,
    ACLRuleDirection,
    ACLRuleProtocol,
    DatabaseBackupStatus,
    EndpointPrivateNetworkDetailsProvisioningMode,
    EngineSettingPropertyType,
    InstanceLogStatus,
    InstanceStatus,
    ListDatabaseBackupsRequestOrderBy,
    ListDatabasesRequestOrderBy,
    ListInstanceLogsRequestOrderBy,
    ListInstancesRequestOrderBy,
    ListPrivilegesRequestOrderBy,
    ListSnapshotsRequestOrderBy,
    ListUsersRequestOrderBy,
    MaintenanceStatus,
    NodeTypeGeneration,
    NodeTypeStock,
    Permission,
    ReadReplicaStatus,
    SnapshotStatus,
    StorageClass,
    VolumeType,
    EndpointDirectAccessDetails,
    EndpointLoadBalancerDetails,
    EndpointPrivateNetworkDetails,
    Endpoint,
    Maintenance,
    ReadReplica,
    DatabaseBackup,
    Database,
    InstanceLog,
    BackupSchedule,
    EncryptionAtRest,
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
    ListDatabaseBackupsResponse,
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
    PrepareInstanceLogsResponse,
    SetInstanceACLRulesResponse,
    SetInstanceSettingsResponse,
    ACLRuleRequest,
    AddInstanceACLRulesRequest,
    AddInstanceSettingsRequest,
    CloneInstanceRequest,
    CreateDatabaseBackupRequest,
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
    PrepareInstanceLogsRequest,
    PurgeInstanceLogsRequest,
    RestoreDatabaseBackupRequest,
    SetInstanceACLRulesRequest,
    SetInstanceSettingsRequest,
    SetPrivilegeRequest,
    UpdateDatabaseBackupRequest,
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

    field = data.get("private_network_id", str())
    args["private_network_id"] = field

    field = data.get("service_ip", str())
    args["service_ip"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("provisioning_mode", getattr(EndpointPrivateNetworkDetailsProvisioningMode, "STATIC"))
    args["provisioning_mode"] = field

    return EndpointPrivateNetworkDetails(**args)

def unmarshal_Endpoint(data: Any) -> Endpoint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Endpoint' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("port", 0)
    args["port"] = field

    field = data.get("ip", None)
    args["ip"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("private_network", None)
    args["private_network"] = unmarshal_EndpointPrivateNetworkDetails(field) if field is not None else None

    field = data.get("load_balancer", None)
    args["load_balancer"] = unmarshal_EndpointLoadBalancerDetails(field) if field is not None else None

    field = data.get("direct_access", None)
    args["direct_access"] = unmarshal_EndpointDirectAccessDetails(field) if field is not None else None

    field = data.get("hostname", None)
    args["hostname"] = field

    return Endpoint(**args)

def unmarshal_Maintenance(data: Any) -> Maintenance:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Maintenance' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("reason", str())
    args["reason"] = field

    field = data.get("status", getattr(MaintenanceStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("is_applicable", False)
    args["is_applicable"] = field

    field = data.get("starts_at", None)
    args["starts_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("stops_at", None)
    args["stops_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("closed_at", None)
    args["closed_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("forced_at", None)
    args["forced_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Maintenance(**args)

def unmarshal_ReadReplica(data: Any) -> ReadReplica:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ReadReplica' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("endpoints", [])
    args["endpoints"] = [unmarshal_Endpoint(v) for v in field] if field is not None else None

    field = data.get("status", getattr(ReadReplicaStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("same_zone", False)
    args["same_zone"] = field

    field = data.get("instance_id", str())
    args["instance_id"] = field

    return ReadReplica(**args)

def unmarshal_DatabaseBackup(data: Any) -> DatabaseBackup:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DatabaseBackup' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("instance_id", str())
    args["instance_id"] = field

    field = data.get("database_name", str())
    args["database_name"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("status", getattr(DatabaseBackupStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("size", None)
    args["size"] = field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("instance_name", str())
    args["instance_name"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("same_region", False)
    args["same_region"] = field

    field = data.get("download_url", None)
    args["download_url"] = field

    field = data.get("download_url_expires_at", None)
    args["download_url_expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return DatabaseBackup(**args)

def unmarshal_Database(data: Any) -> Database:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Database' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("owner", str())
    args["owner"] = field

    field = data.get("managed", False)
    args["managed"] = field

    field = data.get("size", 0)
    args["size"] = field

    return Database(**args)

def unmarshal_InstanceLog(data: Any) -> InstanceLog:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstanceLog' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("status", getattr(InstanceLogStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("node_name", str())
    args["node_name"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("download_url", None)
    args["download_url"] = field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return InstanceLog(**args)

def unmarshal_BackupSchedule(data: Any) -> BackupSchedule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BackupSchedule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("frequency", 0)
    args["frequency"] = field

    field = data.get("retention", 0)
    args["retention"] = field

    field = data.get("disabled", False)
    args["disabled"] = field

    field = data.get("next_run_at", None)
    args["next_run_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return BackupSchedule(**args)

def unmarshal_EncryptionAtRest(data: Any) -> EncryptionAtRest:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EncryptionAtRest' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("enabled", str())
    args["enabled"] = field

    return EncryptionAtRest(**args)

def unmarshal_InstanceSetting(data: Any) -> InstanceSetting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstanceSetting' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("value", str())
    args["value"] = field

    return InstanceSetting(**args)

def unmarshal_LogsPolicy(data: Any) -> LogsPolicy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LogsPolicy' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("max_age_retention", None)
    args["max_age_retention"] = field

    field = data.get("total_disk_retention", None)
    args["total_disk_retention"] = field

    return LogsPolicy(**args)

def unmarshal_UpgradableVersion(data: Any) -> UpgradableVersion:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpgradableVersion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("version", str())
    args["version"] = field

    field = data.get("minor_version", str())
    args["minor_version"] = field

    return UpgradableVersion(**args)

def unmarshal_Volume(data: Any) -> Volume:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Volume' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("size", str())
    args["size"] = field

    field = data.get("class", str())
    args["class_"] = field

    return Volume(**args)

def unmarshal_Instance(data: Any) -> Instance:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Instance' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("region", )
    args["region"] = field

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("volume", None)
    args["volume"] = unmarshal_Volume(field) if field is not None else None

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("status", getattr(InstanceStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("engine", str())
    args["engine"] = field

    field = data.get("upgradable_version", [])
    args["upgradable_version"] = [unmarshal_UpgradableVersion(v) for v in field] if field is not None else None

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("settings", [])
    args["settings"] = [unmarshal_InstanceSetting(v) for v in field] if field is not None else None

    field = data.get("is_ha_cluster", False)
    args["is_ha_cluster"] = field

    field = data.get("endpoint", None)
    args["endpoint"] = unmarshal_Endpoint(field) if field is not None else None

    field = data.get("backup_schedule", None)
    args["backup_schedule"] = unmarshal_BackupSchedule(field) if field is not None else None

    field = data.get("read_replicas", [])
    args["read_replicas"] = [unmarshal_ReadReplica(v) for v in field] if field is not None else None

    field = data.get("node_type", str())
    args["node_type"] = field

    field = data.get("init_settings", [])
    args["init_settings"] = [unmarshal_InstanceSetting(v) for v in field] if field is not None else None

    field = data.get("endpoints", [])
    args["endpoints"] = [unmarshal_Endpoint(v) for v in field] if field is not None else None

    field = data.get("backup_same_region", False)
    args["backup_same_region"] = field

    field = data.get("maintenances", [])
    args["maintenances"] = [unmarshal_Maintenance(v) for v in field] if field is not None else None

    field = data.get("logs_policy", None)
    args["logs_policy"] = unmarshal_LogsPolicy(field) if field is not None else None

    field = data.get("encryption", None)
    args["encryption"] = unmarshal_EncryptionAtRest(field) if field is not None else None

    return Instance(**args)

def unmarshal_Privilege(data: Any) -> Privilege:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Privilege' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("permission", getattr(Permission, "READONLY"))
    args["permission"] = field

    field = data.get("database_name", str())
    args["database_name"] = field

    field = data.get("user_name", str())
    args["user_name"] = field

    return Privilege(**args)

def unmarshal_SnapshotVolumeType(data: Any) -> SnapshotVolumeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SnapshotVolumeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("class", str())
    args["class_"] = field

    return SnapshotVolumeType(**args)

def unmarshal_Snapshot(data: Any) -> Snapshot:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Snapshot' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("instance_id", str())
    args["instance_id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("status", getattr(SnapshotStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("instance_name", str())
    args["instance_name"] = field

    field = data.get("node_type", str())
    args["node_type"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("size", None)
    args["size"] = field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("volume_type", None)
    args["volume_type"] = unmarshal_SnapshotVolumeType(field) if field is not None else None

    return Snapshot(**args)

def unmarshal_User(data: Any) -> User:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'User' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("is_admin", False)
    args["is_admin"] = field

    return User(**args)

def unmarshal_ACLRule(data: Any) -> ACLRule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ACLRule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip", str())
    args["ip"] = field

    field = data.get("protocol", str())
    args["protocol"] = field

    field = data.get("direction", str())
    args["direction"] = field

    field = data.get("action", str())
    args["action"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("port", None)
    args["port"] = field

    return ACLRule(**args)

def unmarshal_AddInstanceACLRulesResponse(data: Any) -> AddInstanceACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddInstanceACLRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", [])
    args["rules"] = [unmarshal_ACLRule(v) for v in field] if field is not None else None

    return AddInstanceACLRulesResponse(**args)

def unmarshal_AddInstanceSettingsResponse(data: Any) -> AddInstanceSettingsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddInstanceSettingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("settings", [])
    args["settings"] = [unmarshal_InstanceSetting(v) for v in field] if field is not None else None

    return AddInstanceSettingsResponse(**args)

def unmarshal_DeleteInstanceACLRulesResponse(data: Any) -> DeleteInstanceACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeleteInstanceACLRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", [])
    args["rules"] = [unmarshal_ACLRule(v) for v in field] if field is not None else None

    return DeleteInstanceACLRulesResponse(**args)

def unmarshal_DeleteInstanceSettingsResponse(data: Any) -> DeleteInstanceSettingsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeleteInstanceSettingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("settings", [])
    args["settings"] = [unmarshal_InstanceSetting(v) for v in field] if field is not None else None

    return DeleteInstanceSettingsResponse(**args)

def unmarshal_InstanceMetrics(data: Any) -> InstanceMetrics:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstanceMetrics' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("timeseries", [])
    args["timeseries"] = [unmarshal_TimeSeries(v) for v in field] if field is not None else None

    return InstanceMetrics(**args)

def unmarshal_ListDatabaseBackupsResponse(data: Any) -> ListDatabaseBackupsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatabaseBackupsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("database_backups", [])
    args["database_backups"] = [unmarshal_DatabaseBackup(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListDatabaseBackupsResponse(**args)

def unmarshal_EngineSetting(data: Any) -> EngineSetting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EngineSetting' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("default_value", str())
    args["default_value"] = field

    field = data.get("hot_configurable", False)
    args["hot_configurable"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("property_type", getattr(EngineSettingPropertyType, "BOOLEAN"))
    args["property_type"] = field

    field = data.get("unit", None)
    args["unit"] = field

    field = data.get("string_constraint", None)
    args["string_constraint"] = field

    field = data.get("int_min", None)
    args["int_min"] = field

    field = data.get("int_max", None)
    args["int_max"] = field

    field = data.get("float_min", None)
    args["float_min"] = field

    field = data.get("float_max", None)
    args["float_max"] = field

    return EngineSetting(**args)

def unmarshal_EngineVersion(data: Any) -> EngineVersion:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EngineVersion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("version", str())
    args["version"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("available_settings", [])
    args["available_settings"] = [unmarshal_EngineSetting(v) for v in field] if field is not None else None

    field = data.get("disabled", False)
    args["disabled"] = field

    field = data.get("beta", False)
    args["beta"] = field

    field = data.get("available_init_settings", [])
    args["available_init_settings"] = [unmarshal_EngineSetting(v) for v in field] if field is not None else None

    field = data.get("end_of_life", None)
    args["end_of_life"] = parser.isoparse(field) if isinstance(field, str) else field

    return EngineVersion(**args)

def unmarshal_DatabaseEngine(data: Any) -> DatabaseEngine:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DatabaseEngine' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("logo_url", str())
    args["logo_url"] = field

    field = data.get("versions", [])
    args["versions"] = [unmarshal_EngineVersion(v) for v in field] if field is not None else None

    field = data.get("region", )
    args["region"] = field

    return DatabaseEngine(**args)

def unmarshal_ListDatabaseEnginesResponse(data: Any) -> ListDatabaseEnginesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatabaseEnginesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("engines", [])
    args["engines"] = [unmarshal_DatabaseEngine(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListDatabaseEnginesResponse(**args)

def unmarshal_ListDatabasesResponse(data: Any) -> ListDatabasesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatabasesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("databases", [])
    args["databases"] = [unmarshal_Database(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListDatabasesResponse(**args)

def unmarshal_ListInstanceACLRulesResponse(data: Any) -> ListInstanceACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstanceACLRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", [])
    args["rules"] = [unmarshal_ACLRule(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListInstanceACLRulesResponse(**args)

def unmarshal_ListInstanceLogsDetailsResponseInstanceLogDetail(data: Any) -> ListInstanceLogsDetailsResponseInstanceLogDetail:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstanceLogsDetailsResponseInstanceLogDetail' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("log_name", str())
    args["log_name"] = field

    field = data.get("size", str())
    args["size"] = field

    return ListInstanceLogsDetailsResponseInstanceLogDetail(**args)

def unmarshal_ListInstanceLogsDetailsResponse(data: Any) -> ListInstanceLogsDetailsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstanceLogsDetailsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("details", [])
    args["details"] = [unmarshal_ListInstanceLogsDetailsResponseInstanceLogDetail(v) for v in field] if field is not None else None

    return ListInstanceLogsDetailsResponse(**args)

def unmarshal_ListInstanceLogsResponse(data: Any) -> ListInstanceLogsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstanceLogsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("instance_logs", [])
    args["instance_logs"] = [unmarshal_InstanceLog(v) for v in field] if field is not None else None

    return ListInstanceLogsResponse(**args)

def unmarshal_ListInstancesResponse(data: Any) -> ListInstancesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstancesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("instances", [])
    args["instances"] = [unmarshal_Instance(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListInstancesResponse(**args)

def unmarshal_NodeTypeVolumeConstraintSizes(data: Any) -> NodeTypeVolumeConstraintSizes:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeTypeVolumeConstraintSizes' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("min_size", 0)
    args["min_size"] = field

    field = data.get("max_size", 0)
    args["max_size"] = field

    return NodeTypeVolumeConstraintSizes(**args)

def unmarshal_NodeTypeVolumeType(data: Any) -> NodeTypeVolumeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeTypeVolumeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", getattr(VolumeType, "LSSD"))
    args["type_"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("min_size", 0)
    args["min_size"] = field

    field = data.get("max_size", 0)
    args["max_size"] = field

    field = data.get("chunk_size", 0)
    args["chunk_size"] = field

    field = data.get("class", getattr(StorageClass, "UNKNOWN_STORAGE_CLASS"))
    args["class_"] = field

    return NodeTypeVolumeType(**args)

def unmarshal_NodeType(data: Any) -> NodeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("stock_status", getattr(NodeTypeStock, "UNKNOWN"))
    args["stock_status"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("vcpus", 0)
    args["vcpus"] = field

    field = data.get("memory", 0)
    args["memory"] = field

    field = data.get("disabled", False)
    args["disabled"] = field

    field = data.get("beta", False)
    args["beta"] = field

    field = data.get("volume_constraint", None)
    args["volume_constraint"] = unmarshal_NodeTypeVolumeConstraintSizes(field) if field is not None else None

    field = data.get("is_bssd_compatible", None)
    args["is_bssd_compatible"] = field

    field = data.get("available_volume_types", [])
    args["available_volume_types"] = [unmarshal_NodeTypeVolumeType(v) for v in field] if field is not None else None

    field = data.get("is_ha_required", False)
    args["is_ha_required"] = field

    field = data.get("generation", getattr(NodeTypeGeneration, "UNKNOWN_GENERATION"))
    args["generation"] = field

    field = data.get("instance_range", str())
    args["instance_range"] = field

    field = data.get("region", )
    args["region"] = field

    return NodeType(**args)

def unmarshal_ListNodeTypesResponse(data: Any) -> ListNodeTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNodeTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("node_types", [])
    args["node_types"] = [unmarshal_NodeType(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListNodeTypesResponse(**args)

def unmarshal_ListPrivilegesResponse(data: Any) -> ListPrivilegesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPrivilegesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("privileges", [])
    args["privileges"] = [unmarshal_Privilege(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListPrivilegesResponse(**args)

def unmarshal_ListSnapshotsResponse(data: Any) -> ListSnapshotsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSnapshotsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshots", [])
    args["snapshots"] = [unmarshal_Snapshot(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListSnapshotsResponse(**args)

def unmarshal_ListUsersResponse(data: Any) -> ListUsersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListUsersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("users", [])
    args["users"] = [unmarshal_User(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListUsersResponse(**args)

def unmarshal_PrepareInstanceLogsResponse(data: Any) -> PrepareInstanceLogsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrepareInstanceLogsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("instance_logs", [])
    args["instance_logs"] = [unmarshal_InstanceLog(v) for v in field] if field is not None else None

    return PrepareInstanceLogsResponse(**args)

def unmarshal_SetInstanceACLRulesResponse(data: Any) -> SetInstanceACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetInstanceACLRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", [])
    args["rules"] = [unmarshal_ACLRule(v) for v in field] if field is not None else None

    return SetInstanceACLRulesResponse(**args)

def unmarshal_SetInstanceSettingsResponse(data: Any) -> SetInstanceSettingsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetInstanceSettingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("settings", [])
    args["settings"] = [unmarshal_InstanceSetting(v) for v in field] if field is not None else None

    return SetInstanceSettingsResponse(**args)

def marshal_ACLRuleRequest(
    request: ACLRuleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip is not None:
        output["ip"] = request.ip
    else:
        output["ip"] = str()

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()


    return output

def marshal_AddInstanceACLRulesRequest(
    request: AddInstanceACLRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.rules is not None:
        output["rules"] = [marshal_ACLRuleRequest(item, defaults) for item in request.rules]
    else:
        output["rules"] = str()


    return output

def marshal_InstanceSetting(
    request: InstanceSetting,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.value is not None:
        output["value"] = request.value
    else:
        output["value"] = str()


    return output

def marshal_AddInstanceSettingsRequest(
    request: AddInstanceSettingsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.settings is not None:
        output["settings"] = [marshal_InstanceSetting(item, defaults) for item in request.settings]
    else:
        output["settings"] = str()


    return output

def marshal_CloneInstanceRequest(
    request: CloneInstanceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.node_type is not None:
        output["node_type"] = request.node_type
    else:
        output["node_type"] = None


    return output

def marshal_CreateDatabaseBackupRequest(
    request: CreateDatabaseBackupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.instance_id is not None:
        output["instance_id"] = request.instance_id
    else:
        output["instance_id"] = str()

    if request.database_name is not None:
        output["database_name"] = request.database_name
    else:
        output["database_name"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()
    else:
        output["expires_at"] = None


    return output

def marshal_CreateDatabaseRequest(
    request: CreateDatabaseRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()


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
        resolve_one_of([
            OneOfPossibility(param="service_ip", value=request.service_ip,marshal_func=None
            ),
            OneOfPossibility(param="ipam_config", value=request.ipam_config,marshal_func=marshal_EndpointSpecPrivateNetworkIpamConfig
            ),
        ]),
    )

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id
    else:
        output["private_network_id"] = str()


    return output

def marshal_EndpointSpec(
    request: EndpointSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="load_balancer", value=request.load_balancer,marshal_func=marshal_EndpointSpecLoadBalancer
            ),
            OneOfPossibility(param="private_network", value=request.private_network,marshal_func=marshal_EndpointSpecPrivateNetwork
            ),
        ]),
    )


    return output

def marshal_CreateEndpointRequest(
    request: CreateEndpointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.endpoint_spec is not None:
        output["endpoint_spec"] = marshal_EndpointSpec(request.endpoint_spec, defaults)
    else:
        output["endpoint_spec"] = None


    return output

def marshal_CreateInstanceFromSnapshotRequest(
    request: CreateInstanceFromSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.instance_name is not None:
        output["instance_name"] = request.instance_name
    else:
        output["instance_name"] = str()

    if request.is_ha_cluster is not None:
        output["is_ha_cluster"] = request.is_ha_cluster
    else:
        output["is_ha_cluster"] = None

    if request.node_type is not None:
        output["node_type"] = request.node_type
    else:
        output["node_type"] = None


    return output

def marshal_EncryptionAtRest(
    request: EncryptionAtRest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.enabled is not None:
        output["enabled"] = request.enabled
    else:
        output["enabled"] = str()


    return output

def marshal_CreateInstanceRequest(
    request: CreateInstanceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="project_id", value=request.project_id, default=defaults.default_project_id,marshal_func=None
            ),
            OneOfPossibility(param="organization_id", value=request.organization_id,default=defaults.default_organization_id,marshal_func=None
            ),
        ]),
    )

    if request.engine is not None:
        output["engine"] = request.engine
    else:
        output["engine"] = str()

    if request.user_name is not None:
        output["user_name"] = request.user_name
    else:
        output["user_name"] = str()

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = str()

    if request.node_type is not None:
        output["node_type"] = request.node_type
    else:
        output["node_type"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.is_ha_cluster is not None:
        output["is_ha_cluster"] = request.is_ha_cluster
    else:
        output["is_ha_cluster"] = False

    if request.disable_backup is not None:
        output["disable_backup"] = request.disable_backup
    else:
        output["disable_backup"] = False

    if request.volume_size is not None:
        output["volume_size"] = request.volume_size
    else:
        output["volume_size"] = 0

    if request.backup_same_region is not None:
        output["backup_same_region"] = request.backup_same_region
    else:
        output["backup_same_region"] = False

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.init_settings is not None:
        output["init_settings"] = [marshal_InstanceSetting(item, defaults) for item in request.init_settings]
    else:
        output["init_settings"] = None

    if request.volume_type is not None:
        output["volume_type"] = str(request.volume_type)
    else:
        output["volume_type"] = None

    if request.init_endpoints is not None:
        output["init_endpoints"] = [marshal_EndpointSpec(item, defaults) for item in request.init_endpoints]
    else:
        output["init_endpoints"] = None

    if request.encryption is not None:
        output["encryption"] = marshal_EncryptionAtRest(request.encryption, defaults)
    else:
        output["encryption"] = None


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
        resolve_one_of([
            OneOfPossibility(param="service_ip", value=request.service_ip,marshal_func=None
            ),
            OneOfPossibility(param="ipam_config", value=request.ipam_config,marshal_func=marshal_ReadReplicaEndpointSpecPrivateNetworkIpamConfig
            ),
        ]),
    )

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id
    else:
        output["private_network_id"] = str()


    return output

def marshal_ReadReplicaEndpointSpec(
    request: ReadReplicaEndpointSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="direct_access", value=request.direct_access,marshal_func=marshal_ReadReplicaEndpointSpecDirectAccess
            ),
            OneOfPossibility(param="private_network", value=request.private_network,marshal_func=marshal_ReadReplicaEndpointSpecPrivateNetwork
            ),
        ]),
    )


    return output

def marshal_CreateReadReplicaEndpointRequest(
    request: CreateReadReplicaEndpointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.endpoint_spec is not None:
        output["endpoint_spec"] = [marshal_ReadReplicaEndpointSpec(item, defaults) for item in request.endpoint_spec]
    else:
        output["endpoint_spec"] = str()


    return output

def marshal_CreateReadReplicaRequest(
    request: CreateReadReplicaRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.instance_id is not None:
        output["instance_id"] = request.instance_id
    else:
        output["instance_id"] = str()

    if request.endpoint_spec is not None:
        output["endpoint_spec"] = [marshal_ReadReplicaEndpointSpec(item, defaults) for item in request.endpoint_spec]
    else:
        output["endpoint_spec"] = None

    if request.same_zone is not None:
        output["same_zone"] = request.same_zone
    else:
        output["same_zone"] = None


    return output

def marshal_CreateSnapshotRequest(
    request: CreateSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()
    else:
        output["expires_at"] = None


    return output

def marshal_CreateUserRequest(
    request: CreateUserRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = str()

    if request.is_admin is not None:
        output["is_admin"] = request.is_admin
    else:
        output["is_admin"] = False


    return output

def marshal_DeleteInstanceACLRulesRequest(
    request: DeleteInstanceACLRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.acl_rule_ips is not None:
        output["acl_rule_ips"] = request.acl_rule_ips
    else:
        output["acl_rule_ips"] = str()


    return output

def marshal_DeleteInstanceSettingsRequest(
    request: DeleteInstanceSettingsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.setting_names is not None:
        output["setting_names"] = request.setting_names
    else:
        output["setting_names"] = str()


    return output

def marshal_MigrateEndpointRequest(
    request: MigrateEndpointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.instance_id is not None:
        output["instance_id"] = request.instance_id
    else:
        output["instance_id"] = str()


    return output

def marshal_PrepareInstanceLogsRequest(
    request: PrepareInstanceLogsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.start_date is not None:
        output["start_date"] = request.start_date.isoformat()
    else:
        output["start_date"] = None

    if request.end_date is not None:
        output["end_date"] = request.end_date.isoformat()
    else:
        output["end_date"] = None


    return output

def marshal_PurgeInstanceLogsRequest(
    request: PurgeInstanceLogsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.log_name is not None:
        output["log_name"] = request.log_name
    else:
        output["log_name"] = None


    return output

def marshal_RestoreDatabaseBackupRequest(
    request: RestoreDatabaseBackupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.instance_id is not None:
        output["instance_id"] = request.instance_id
    else:
        output["instance_id"] = str()

    if request.database_name is not None:
        output["database_name"] = request.database_name
    else:
        output["database_name"] = None


    return output

def marshal_SetInstanceACLRulesRequest(
    request: SetInstanceACLRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.rules is not None:
        output["rules"] = [marshal_ACLRuleRequest(item, defaults) for item in request.rules]
    else:
        output["rules"] = str()


    return output

def marshal_SetInstanceSettingsRequest(
    request: SetInstanceSettingsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.settings is not None:
        output["settings"] = [marshal_InstanceSetting(item, defaults) for item in request.settings]
    else:
        output["settings"] = str()


    return output

def marshal_SetPrivilegeRequest(
    request: SetPrivilegeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.database_name is not None:
        output["database_name"] = request.database_name
    else:
        output["database_name"] = str()

    if request.user_name is not None:
        output["user_name"] = request.user_name
    else:
        output["user_name"] = str()

    if request.permission is not None:
        output["permission"] = str(request.permission)
    else:
        output["permission"] = None


    return output

def marshal_UpdateDatabaseBackupRequest(
    request: UpdateDatabaseBackupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()
    else:
        output["expires_at"] = None


    return output

def marshal_LogsPolicy(
    request: LogsPolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.max_age_retention is not None:
        output["max_age_retention"] = request.max_age_retention
    else:
        output["max_age_retention"] = None

    if request.total_disk_retention is not None:
        output["total_disk_retention"] = request.total_disk_retention
    else:
        output["total_disk_retention"] = None


    return output

def marshal_UpdateInstanceRequest(
    request: UpdateInstanceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.backup_schedule_frequency is not None:
        output["backup_schedule_frequency"] = request.backup_schedule_frequency
    else:
        output["backup_schedule_frequency"] = None

    if request.backup_schedule_retention is not None:
        output["backup_schedule_retention"] = request.backup_schedule_retention
    else:
        output["backup_schedule_retention"] = None

    if request.is_backup_schedule_disabled is not None:
        output["is_backup_schedule_disabled"] = request.is_backup_schedule_disabled
    else:
        output["is_backup_schedule_disabled"] = None

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.logs_policy is not None:
        output["logs_policy"] = marshal_LogsPolicy(request.logs_policy, defaults)
    else:
        output["logs_policy"] = None

    if request.backup_same_region is not None:
        output["backup_same_region"] = request.backup_same_region
    else:
        output["backup_same_region"] = None

    if request.backup_schedule_start_hour is not None:
        output["backup_schedule_start_hour"] = request.backup_schedule_start_hour
    else:
        output["backup_schedule_start_hour"] = None


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

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()
    else:
        output["expires_at"] = None


    return output

def marshal_UpdateUserRequest(
    request: UpdateUserRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = None

    if request.is_admin is not None:
        output["is_admin"] = request.is_admin
    else:
        output["is_admin"] = None


    return output

def marshal_UpgradeInstanceRequestMajorUpgradeWorkflow(
    request: UpgradeInstanceRequestMajorUpgradeWorkflow,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.upgradable_version_id is not None:
        output["upgradable_version_id"] = request.upgradable_version_id
    else:
        output["upgradable_version_id"] = str()

    if request.with_endpoints is not None:
        output["with_endpoints"] = request.with_endpoints
    else:
        output["with_endpoints"] = False


    return output

def marshal_UpgradeInstanceRequest(
    request: UpgradeInstanceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="node_type", value=request.node_type,marshal_func=None
            ),
            OneOfPossibility(param="enable_ha", value=request.enable_ha,marshal_func=None
            ),
            OneOfPossibility(param="volume_size", value=request.volume_size,marshal_func=None
            ),
            OneOfPossibility(param="volume_type", value=request.volume_type,marshal_func=marshal_VolumeType
            ),
            OneOfPossibility(param="upgradable_version_id", value=request.upgradable_version_id,marshal_func=None
            ),
            OneOfPossibility(param="major_upgrade_workflow", value=request.major_upgrade_workflow,marshal_func=marshal_UpgradeInstanceRequestMajorUpgradeWorkflow
            ),
            OneOfPossibility(param="enable_encryption", value=request.enable_encryption,marshal_func=None
            ),
        ]),
    )


    return output
