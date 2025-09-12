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
    NodeTypeStock,
    SettingPropertyType,
    SnapshotStatus,
    UserRoleRole,
    VolumeType,
    EndpointPrivateNetworkDetails,
    EndpointPublicDetails,
    Endpoint,
    InstanceSetting,
    InstanceSnapshotSchedule,
    Volume,
    Instance,
    SnapshotVolumeType,
    Snapshot,
    UserRole,
    User,
    ListInstancesResponse,
    NodeTypeVolumeType,
    NodeType,
    ListNodeTypesResponse,
    ListSnapshotsResponse,
    ListUsersResponse,
    Setting,
    Version,
    ListVersionsResponse,
    EndpointSpecPrivateNetworkDetails,
    EndpointSpecPublicDetails,
    EndpointSpec,
    CreateEndpointRequest,
    CreateInstanceRequestVolumeDetails,
    CreateInstanceRequest,
    CreateSnapshotRequest,
    CreateUserRequest,
    RestoreSnapshotRequestVolumeDetails,
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


def unmarshal_EndpointPublicDetails(data: Any) -> EndpointPublicDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EndpointPublicDetails' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return EndpointPublicDetails(**args)


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

    field = data.get("ips", None)
    if field is not None:
        args["ips"] = field
    else:
        args["ips"] = []

    field = data.get("dns_records", None)
    if field is not None:
        args["dns_records"] = field
    else:
        args["dns_records"] = []

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

    field = data.get("public", None)
    if field is not None:
        args["public"] = unmarshal_EndpointPublicDetails(field)
    else:
        args["public"] = None

    return Endpoint(**args)


def unmarshal_InstanceSetting(data: Any) -> InstanceSetting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstanceSetting' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("value", None)
    if field is not None:
        args["value"] = field
    else:
        args["value"] = None

    return InstanceSetting(**args)


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

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = 0

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

    field = data.get("settings", None)
    if field is not None:
        args["settings"] = (
            [unmarshal_InstanceSetting(v) for v in field] if field is not None else None
        )
    else:
        args["settings"] = []

    field = data.get("node_number", None)
    if field is not None:
        args["node_number"] = field
    else:
        args["node_number"] = 0

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


def unmarshal_SnapshotVolumeType(data: Any) -> SnapshotVolumeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SnapshotVolumeType' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    return SnapshotVolumeType(**args)


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

    field = data.get("instance_id", None)
    if field is not None:
        args["instance_id"] = field
    else:
        args["instance_id"] = None

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

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = 0

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

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

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

    field = data.get("database", None)
    if field is not None:
        args["database"] = field
    else:
        args["database"] = None

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

    field = data.get("min_size", None)
    if field is not None:
        args["min_size"] = field
    else:
        args["min_size"] = 0

    field = data.get("max_size", None)
    if field is not None:
        args["max_size"] = field
    else:
        args["max_size"] = 0

    field = data.get("chunk_size", None)
    if field is not None:
        args["chunk_size"] = field
    else:
        args["chunk_size"] = 0

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

    field = data.get("memory", None)
    if field is not None:
        args["memory"] = field
    else:
        args["memory"] = 0

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


def unmarshal_Setting(data: Any) -> Setting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Setting' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("default_value", None)
    if field is not None:
        args["default_value"] = field
    else:
        args["default_value"] = None

    field = data.get("hot_configurable", None)
    if field is not None:
        args["hot_configurable"] = field
    else:
        args["hot_configurable"] = False

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("property_type", None)
    if field is not None:
        args["property_type"] = field
    else:
        args["property_type"] = SettingPropertyType.BOOLEAN

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
        args["int_min"] = 0

    field = data.get("int_max", None)
    if field is not None:
        args["int_max"] = field
    else:
        args["int_max"] = 0

    field = data.get("float_min", None)
    if field is not None:
        args["float_min"] = field
    else:
        args["float_min"] = 0.0

    field = data.get("float_max", None)
    if field is not None:
        args["float_max"] = field
    else:
        args["float_max"] = 0.0

    return Setting(**args)


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

    field = data.get("available_settings", None)
    if field is not None:
        args["available_settings"] = (
            [unmarshal_Setting(v) for v in field] if field is not None else None
        )
    else:
        args["available_settings"] = []

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


def marshal_EndpointSpecPublicDetails(
    request: EndpointSpecPublicDetails,
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
                    param="public",
                    value=request.public,
                    marshal_func=marshal_EndpointSpecPublicDetails,
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


def marshal_CreateInstanceRequestVolumeDetails(
    request: CreateInstanceRequestVolumeDetails,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.volume_size is not None:
        output["volume_size"] = request.volume_size

    if request.volume_type is not None:
        output["volume_type"] = request.volume_type

    return output


def marshal_CreateInstanceRequest(
    request: CreateInstanceRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.version is not None:
        output["version"] = request.version

    if request.node_number is not None:
        output["node_number"] = request.node_number

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
        output["volume"] = marshal_CreateInstanceRequestVolumeDetails(
            request.volume, defaults
        )

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


def marshal_RestoreSnapshotRequestVolumeDetails(
    request: RestoreSnapshotRequestVolumeDetails,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.volume_type is not None:
        output["volume_type"] = request.volume_type

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

    if request.node_number is not None:
        output["node_number"] = request.node_number

    if request.volume is not None:
        output["volume"] = marshal_RestoreSnapshotRequestVolumeDetails(
            request.volume, defaults
        )

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
                    param="database", value=request.database, marshal_func=None
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
                    param="volume_size", value=request.volume_size, marshal_func=None
                ),
            ]
        ),
    )

    return output
