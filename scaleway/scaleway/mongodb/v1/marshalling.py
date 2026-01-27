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
    InstanceStatus,
    MaintenanceAppliedBy,
    MaintenanceStatus,
    NodeTypeStock,
    SnapshotStatus,
    UserRoleRole,
    VolumeType,
    EndpointPrivateNetworkDetails,
    EndpointPublicNetworkDetails,
    Endpoint,
    InstanceSnapshotSchedule,
    Volume,
    Instance,
    EngineUpgrade,
    ServiceUpdate,
    Workflow,
    Maintenance,
    Snapshot,
    UserRole,
    User,
    Database,
    ListDatabasesResponse,
    ListInstancesResponse,
    ListMaintenancesResponse,
    NodeTypeVolumeType,
    NodeType,
    ListNodeTypesResponse,
    ListSnapshotsResponse,
    ListUsersResponse,
    Version,
    ListVersionsResponse,
    EndpointSpecPrivateNetworkDetails,
    EndpointSpecPublicNetworkDetails,
    EndpointSpec,
    CreateEndpointRequest,
    CreateInstanceRequest,
    CreateSnapshotRequest,
    CreateUserRequest,
    RestoreSnapshotRequest,
    SetUserRoleRequest,
    UpdateInstanceRequest,
    UpdateSnapshotRequest,
    UpdateUserRequest,
    UpgradeInstanceRequest,
)


def unmarshal_EndpointPrivateNetworkDetails(data: Any) -> EndpointPrivateNetworkDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EndpointPrivateNetworkDetails' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field
    else:
        args["private_network_id"] = None

    return EndpointPrivateNetworkDetails(**args)


def unmarshal_EndpointPublicNetworkDetails(data: Any) -> EndpointPublicNetworkDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EndpointPublicNetworkDetails' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return EndpointPublicNetworkDetails(**args)


def unmarshal_Endpoint(data: Any) -> Endpoint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Endpoint' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("dns_record", None)
    if field is not None:
        args["dns_record"] = field
    else:
        args["dns_record"] = None

    field = data.get("port", None)
    if field is not None:
        args["port"] = field
    else:
        args["port"] = 0

    field = data.get("private_network", None)
    if field is not None:
        args["private_network"] = unmarshal_EndpointPrivateNetworkDetails(field)
    else:
        args["private_network"] = None

    field = data.get("public_network", None)
    if field is not None:
        args["public_network"] = unmarshal_EndpointPublicNetworkDetails(field)
    else:
        args["public_network"] = None

    return Endpoint(**args)


def unmarshal_InstanceSnapshotSchedule(data: Any) -> InstanceSnapshotSchedule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstanceSnapshotSchedule' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("frequency_hours", None)
    if field is not None:
        args["frequency_hours"] = field
    else:
        args["frequency_hours"] = None

    field = data.get("retention_days", None)
    if field is not None:
        args["retention_days"] = field
    else:
        args["retention_days"] = None

    field = data.get("enabled", None)
    if field is not None:
        args["enabled"] = field
    else:
        args["enabled"] = None

    field = data.get("next_update", None)
    if field is not None:
        args["next_update"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["next_update"] = None

    field = data.get("last_run", None)
    if field is not None:
        args["last_run"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["last_run"] = None

    return InstanceSnapshotSchedule(**args)


def unmarshal_Volume(data: Any) -> Volume:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Volume' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = VolumeType.UNKNOWN_TYPE

    field = data.get("size_bytes", None)
    if field is not None:
        args["size_bytes"] = field
    else:
        args["size_bytes"] = 0

    return Volume(**args)


def unmarshal_Instance(data: Any) -> Instance:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Instance' failed as data isn't a dictionary."
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

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = InstanceStatus.UNKNOWN_STATUS

    field = data.get("version", None)
    if field is not None:
        args["version"] = field
    else:
        args["version"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("node_amount", None)
    if field is not None:
        args["node_amount"] = field
    else:
        args["node_amount"] = 0

    field = data.get("node_type", None)
    if field is not None:
        args["node_type"] = field
    else:
        args["node_type"] = None

    field = data.get("endpoints", None)
    if field is not None:
        args["endpoints"] = (
            [unmarshal_Endpoint(v) for v in field] if field is not None else None
        )
    else:
        args["endpoints"] = []

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("volume", None)
    if field is not None:
        args["volume"] = unmarshal_Volume(field)
    else:
        args["volume"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("snapshot_schedule", None)
    if field is not None:
        args["snapshot_schedule"] = unmarshal_InstanceSnapshotSchedule(field)
    else:
        args["snapshot_schedule"] = None

    return Instance(**args)


def unmarshal_EngineUpgrade(data: Any) -> EngineUpgrade:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EngineUpgrade' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("new_version_id", None)
    if field is not None:
        args["new_version_id"] = field
    else:
        args["new_version_id"] = None

    return EngineUpgrade(**args)


def unmarshal_ServiceUpdate(data: Any) -> ServiceUpdate:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServiceUpdate' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("service_name", None)
    if field is not None:
        args["service_name"] = field
    else:
        args["service_name"] = None

    return ServiceUpdate(**args)


def unmarshal_Workflow(data: Any) -> Workflow:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Workflow' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("engine_upgrade", None)
    if field is not None:
        args["engine_upgrade"] = unmarshal_EngineUpgrade(field)
    else:
        args["engine_upgrade"] = None

    field = data.get("service_update", None)
    if field is not None:
        args["service_update"] = unmarshal_ServiceUpdate(field)
    else:
        args["service_update"] = None

    return Workflow(**args)


def unmarshal_Maintenance(data: Any) -> Maintenance:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Maintenance' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("instance_id", None)
    if field is not None:
        args["instance_id"] = field
    else:
        args["instance_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = MaintenanceStatus.UNKNOWN_STATUS

    field = data.get("applied_by", None)
    if field is not None:
        args["applied_by"] = field
    else:
        args["applied_by"] = MaintenanceAppliedBy.UNKNOWN_APPLIED_BY

    field = data.get("reason", None)
    if field is not None:
        args["reason"] = field
    else:
        args["reason"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

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

    field = data.get("forced_at", None)
    if field is not None:
        args["forced_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["forced_at"] = None

    field = data.get("applied_at", None)
    if field is not None:
        args["applied_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["applied_at"] = None

    field = data.get("workflow", None)
    if field is not None:
        args["workflow"] = unmarshal_Workflow(field)
    else:
        args["workflow"] = None

    return Maintenance(**args)


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

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = SnapshotStatus.UNKNOWN_STATUS

    field = data.get("size_bytes", None)
    if field is not None:
        args["size_bytes"] = field
    else:
        args["size_bytes"] = 0

    field = data.get("instance_name", None)
    if field is not None:
        args["instance_name"] = field
    else:
        args["instance_name"] = None

    field = data.get("node_type", None)
    if field is not None:
        args["node_type"] = field
    else:
        args["node_type"] = None

    field = data.get("volume_type", None)
    if field is not None:
        args["volume_type"] = field
    else:
        args["volume_type"] = VolumeType.UNKNOWN_TYPE

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("instance_id", None)
    if field is not None:
        args["instance_id"] = field
    else:
        args["instance_id"] = None

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

    return Snapshot(**args)


def unmarshal_UserRole(data: Any) -> UserRole:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UserRole' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("role", None)
    if field is not None:
        args["role"] = field
    else:
        args["role"] = UserRoleRole.UNKNOWN_ROLE

    field = data.get("database_name", None)
    if field is not None:
        args["database_name"] = field
    else:
        args["database_name"] = None

    field = data.get("any_database", None)
    if field is not None:
        args["any_database"] = field
    else:
        args["any_database"] = False

    return UserRole(**args)


def unmarshal_User(data: Any) -> User:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'User' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("roles", None)
    if field is not None:
        args["roles"] = (
            [unmarshal_UserRole(v) for v in field] if field is not None else None
        )
    else:
        args["roles"] = []

    return User(**args)


def unmarshal_Database(data: Any) -> Database:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Database' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return Database(**args)


def unmarshal_ListDatabasesResponse(data: Any) -> ListDatabasesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatabasesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("databases", None)
    if field is not None:
        args["databases"] = (
            [unmarshal_Database(v) for v in field] if field is not None else None
        )
    else:
        args["databases"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListDatabasesResponse(**args)


def unmarshal_ListInstancesResponse(data: Any) -> ListInstancesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstancesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("instances", None)
    if field is not None:
        args["instances"] = (
            [unmarshal_Instance(v) for v in field] if field is not None else None
        )
    else:
        args["instances"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListInstancesResponse(**args)


def unmarshal_ListMaintenancesResponse(data: Any) -> ListMaintenancesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListMaintenancesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("maintenances", None)
    if field is not None:
        args["maintenances"] = (
            [unmarshal_Maintenance(v) for v in field] if field is not None else None
        )
    else:
        args["maintenances"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListMaintenancesResponse(**args)


def unmarshal_NodeTypeVolumeType(data: Any) -> NodeTypeVolumeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeTypeVolumeType' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = VolumeType.UNKNOWN_TYPE

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("min_size_bytes", None)
    if field is not None:
        args["min_size_bytes"] = field
    else:
        args["min_size_bytes"] = 0

    field = data.get("max_size_bytes", None)
    if field is not None:
        args["max_size_bytes"] = field
    else:
        args["max_size_bytes"] = 0

    field = data.get("chunk_size_bytes", None)
    if field is not None:
        args["chunk_size_bytes"] = field
    else:
        args["chunk_size_bytes"] = 0

    return NodeTypeVolumeType(**args)


def unmarshal_NodeType(data: Any) -> NodeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeType' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("stock_status", None)
    if field is not None:
        args["stock_status"] = field
    else:
        args["stock_status"] = NodeTypeStock.UNKNOWN_STOCK

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("vcpus", None)
    if field is not None:
        args["vcpus"] = field
    else:
        args["vcpus"] = 0

    field = data.get("memory_bytes", None)
    if field is not None:
        args["memory_bytes"] = field
    else:
        args["memory_bytes"] = 0

    field = data.get("available_volume_types", None)
    if field is not None:
        args["available_volume_types"] = (
            [unmarshal_NodeTypeVolumeType(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["available_volume_types"] = []

    field = data.get("disabled", None)
    if field is not None:
        args["disabled"] = field
    else:
        args["disabled"] = False

    field = data.get("beta", None)
    if field is not None:
        args["beta"] = field
    else:
        args["beta"] = False

    field = data.get("instance_range", None)
    if field is not None:
        args["instance_range"] = field
    else:
        args["instance_range"] = None

    return NodeType(**args)


def unmarshal_ListNodeTypesResponse(data: Any) -> ListNodeTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNodeTypesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("node_types", None)
    if field is not None:
        args["node_types"] = (
            [unmarshal_NodeType(v) for v in field] if field is not None else None
        )
    else:
        args["node_types"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListNodeTypesResponse(**args)


def unmarshal_ListSnapshotsResponse(data: Any) -> ListSnapshotsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSnapshotsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("snapshots", None)
    if field is not None:
        args["snapshots"] = (
            [unmarshal_Snapshot(v) for v in field] if field is not None else None
        )
    else:
        args["snapshots"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListSnapshotsResponse(**args)


def unmarshal_ListUsersResponse(data: Any) -> ListUsersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListUsersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("users", None)
    if field is not None:
        args["users"] = (
            [unmarshal_User(v) for v in field] if field is not None else None
        )
    else:
        args["users"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListUsersResponse(**args)


def unmarshal_Version(data: Any) -> Version:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Version' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("version", None)
    if field is not None:
        args["version"] = field
    else:
        args["version"] = None

    field = data.get("end_of_life_at", None)
    if field is not None:
        args["end_of_life_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["end_of_life_at"] = None

    return Version(**args)


def unmarshal_ListVersionsResponse(data: Any) -> ListVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVersionsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("versions", None)
    if field is not None:
        args["versions"] = (
            [unmarshal_Version(v) for v in field] if field is not None else None
        )
    else:
        args["versions"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListVersionsResponse(**args)


def marshal_EndpointSpecPrivateNetworkDetails(
    request: EndpointSpecPrivateNetworkDetails,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    return output


def marshal_EndpointSpecPublicNetworkDetails(
    request: EndpointSpecPublicNetworkDetails,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    return output


def marshal_EndpointSpec(
    request: EndpointSpec,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="public_network",
                    value=request.public_network,
                    marshal_func=marshal_EndpointSpecPublicNetworkDetails,
                ),
                OneOfPossibility(
                    param="private_network",
                    value=request.private_network,
                    marshal_func=marshal_EndpointSpecPrivateNetworkDetails,
                ),
            ]
        ),
    )

    return output


def marshal_CreateEndpointRequest(
    request: CreateEndpointRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.instance_id is not None:
        output["instance_id"] = request.instance_id

    if request.endpoint is not None:
        output["endpoint"] = marshal_EndpointSpec(request.endpoint, defaults)

    return output


def marshal_Volume(
    request: Volume,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    if request.size_bytes is not None:
        output["size_bytes"] = request.size_bytes

    return output


def marshal_CreateInstanceRequest(
    request: CreateInstanceRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.version is not None:
        output["version"] = request.version

    if request.node_amount is not None:
        output["node_amount"] = request.node_amount

    if request.node_type is not None:
        output["node_type"] = request.node_type

    if request.user_name is not None:
        output["user_name"] = request.user_name

    if request.password is not None:
        output["password"] = request.password

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.volume is not None:
        output["volume"] = marshal_Volume(request.volume, defaults)

    if request.endpoints is not None:
        output["endpoints"] = [
            marshal_EndpointSpec(item, defaults) for item in request.endpoints
        ]

    return output


def marshal_CreateSnapshotRequest(
    request: CreateSnapshotRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.instance_id is not None:
        output["instance_id"] = request.instance_id

    if request.name is not None:
        output["name"] = request.name

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()

    return output


def marshal_CreateUserRequest(
    request: CreateUserRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_RestoreSnapshotRequest(
    request: RestoreSnapshotRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.instance_name is not None:
        output["instance_name"] = request.instance_name

    if request.node_type is not None:
        output["node_type"] = request.node_type

    if request.node_amount is not None:
        output["node_amount"] = request.node_amount

    if request.volume_type is not None:
        output["volume_type"] = request.volume_type

    return output


def marshal_UserRole(
    request: UserRole,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="database_name",
                    value=request.database_name,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="any_database", value=request.any_database, marshal_func=None
                ),
            ]
        ),
    )

    if request.role is not None:
        output["role"] = request.role

    return output


def marshal_SetUserRoleRequest(
    request: SetUserRoleRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.user_name is not None:
        output["user_name"] = request.user_name

    if request.roles is not None:
        output["roles"] = [marshal_UserRole(item, defaults) for item in request.roles]

    return output


def marshal_UpdateInstanceRequest(
    request: UpdateInstanceRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.snapshot_schedule_frequency_hours is not None:
        output["snapshot_schedule_frequency_hours"] = (
            request.snapshot_schedule_frequency_hours
        )

    if request.snapshot_schedule_retention_days is not None:
        output["snapshot_schedule_retention_days"] = (
            request.snapshot_schedule_retention_days
        )

    if request.is_snapshot_schedule_enabled is not None:
        output["is_snapshot_schedule_enabled"] = request.is_snapshot_schedule_enabled

    return output


def marshal_UpdateSnapshotRequest(
    request: UpdateSnapshotRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()

    return output


def marshal_UpdateUserRequest(
    request: UpdateUserRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_UpgradeInstanceRequest(
    request: UpgradeInstanceRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="volume_size_bytes",
                    value=request.volume_size_bytes,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="version_id", value=request.version_id, marshal_func=None
                ),
            ]
        ),
    )

    return output
