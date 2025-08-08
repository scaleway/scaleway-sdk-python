# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    EndpointPrivateNetworkDetails,
    EndpointPublicNetworkDetails,
    Endpoint,
    InstanceSnapshotSchedule,
    Volume,
    Instance,
    Snapshot,
    UserRole,
    User,
    Database,
    ListDatabasesResponse,
    ListInstancesResponse,
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

    args: Dict[str, Any] = {}

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field

    return EndpointPrivateNetworkDetails(**args)


def unmarshal_EndpointPublicNetworkDetails(data: Any) -> EndpointPublicNetworkDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EndpointPublicNetworkDetails' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return EndpointPublicNetworkDetails(**args)


def unmarshal_Endpoint(data: Any) -> Endpoint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Endpoint' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("dns_record", None)
    if field is not None:
        args["dns_record"] = field

    field = data.get("port", None)
    if field is not None:
        args["port"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("frequency_hours", None)
    if field is not None:
        args["frequency_hours"] = field

    field = data.get("retention_days", None)
    if field is not None:
        args["retention_days"] = field

    field = data.get("enabled", None)
    if field is not None:
        args["enabled"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("size_bytes", None)
    if field is not None:
        args["size_bytes"] = field

    return Volume(**args)


def unmarshal_Instance(data: Any) -> Instance:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Instance' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("version", None)
    if field is not None:
        args["version"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("node_amount", None)
    if field is not None:
        args["node_amount"] = field

    field = data.get("node_type", None)
    if field is not None:
        args["node_type"] = field

    field = data.get("endpoints", None)
    if field is not None:
        args["endpoints"] = (
            [unmarshal_Endpoint(v) for v in field] if field is not None else None
        )

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

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


def unmarshal_Snapshot(data: Any) -> Snapshot:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Snapshot' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("size_bytes", None)
    if field is not None:
        args["size_bytes"] = field

    field = data.get("instance_name", None)
    if field is not None:
        args["instance_name"] = field

    field = data.get("node_type", None)
    if field is not None:
        args["node_type"] = field

    field = data.get("volume_type", None)
    if field is not None:
        args["volume_type"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("role", None)
    if field is not None:
        args["role"] = field

    field = data.get("database_name", None)
    if field is not None:
        args["database_name"] = field
    else:
        args["database_name"] = None

    field = data.get("any_database", None)
    if field is not None:
        args["any_database"] = field
    else:
        args["any_database"] = None

    return UserRole(**args)


def unmarshal_User(data: Any) -> User:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'User' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("roles", None)
    if field is not None:
        args["roles"] = (
            [unmarshal_UserRole(v) for v in field] if field is not None else None
        )

    return User(**args)


def unmarshal_Database(data: Any) -> Database:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Database' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    return Database(**args)


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

    field = data.get("min_size_bytes", None)
    if field is not None:
        args["min_size_bytes"] = field

    field = data.get("max_size_bytes", None)
    if field is not None:
        args["max_size_bytes"] = field

    field = data.get("chunk_size_bytes", None)
    if field is not None:
        args["chunk_size_bytes"] = field

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

    field = data.get("memory_bytes", None)
    if field is not None:
        args["memory_bytes"] = field

    field = data.get("available_volume_types", None)
    if field is not None:
        args["available_volume_types"] = (
            [unmarshal_NodeTypeVolumeType(v) for v in field]
            if field is not None
            else None
        )

    field = data.get("disabled", None)
    if field is not None:
        args["disabled"] = field

    field = data.get("beta", None)
    if field is not None:
        args["beta"] = field

    field = data.get("instance_range", None)
    if field is not None:
        args["instance_range"] = field

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


def unmarshal_Version(data: Any) -> Version:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Version' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("version", None)
    if field is not None:
        args["version"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("versions", None)
    if field is not None:
        args["versions"] = (
            [unmarshal_Version(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListVersionsResponse(**args)


def marshal_EndpointSpecPrivateNetworkDetails(
    request: EndpointSpecPrivateNetworkDetails,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    return output


def marshal_EndpointSpecPublicNetworkDetails(
    request: EndpointSpecPublicNetworkDetails,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    return output


def marshal_EndpointSpec(
    request: EndpointSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
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
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.instance_id is not None:
        output["instance_id"] = request.instance_id

    if request.endpoint is not None:
        output["endpoint"] = marshal_EndpointSpec(request.endpoint, defaults)

    return output


def marshal_Volume(
    request: Volume,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = str(request.type_)

    if request.size_bytes is not None:
        output["size_bytes"] = request.size_bytes

    return output


def marshal_CreateInstanceRequest(
    request: CreateInstanceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

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
        output["project_id"] = request.project_id or defaults.default_project_id

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
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

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
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_RestoreSnapshotRequest(
    request: RestoreSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.instance_name is not None:
        output["instance_name"] = request.instance_name

    if request.node_type is not None:
        output["node_type"] = request.node_type

    if request.node_amount is not None:
        output["node_amount"] = request.node_amount

    if request.volume_type is not None:
        output["volume_type"] = str(request.volume_type)

    return output


def marshal_UserRole(
    request: UserRole,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
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
        output["role"] = str(request.role)

    return output


def marshal_SetUserRoleRequest(
    request: SetUserRoleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.user_name is not None:
        output["user_name"] = request.user_name

    if request.roles is not None:
        output["roles"] = [marshal_UserRole(item, defaults) for item in request.roles]

    return output


def marshal_UpdateInstanceRequest(
    request: UpdateInstanceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

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

    return output


def marshal_UpgradeInstanceRequest(
    request: UpgradeInstanceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="volume_size_bytes",
                    value=request.volume_size_bytes,
                    marshal_func=None,
                ),
            ]
        ),
    )

    return output
