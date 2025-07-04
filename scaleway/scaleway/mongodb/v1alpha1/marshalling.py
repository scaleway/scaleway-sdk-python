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
    InstanceStatus,
    ListInstancesRequestOrderBy,
    ListSnapshotsRequestOrderBy,
    ListUsersRequestOrderBy,
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

    args: Dict[str, Any] = {}

    field = data.get("private_network_id", str())
    args["private_network_id"] = field

    return EndpointPrivateNetworkDetails(**args)

def unmarshal_EndpointPublicDetails(data: Any) -> EndpointPublicDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EndpointPublicDetails' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return EndpointPublicDetails(**args)

def unmarshal_Endpoint(data: Any) -> Endpoint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Endpoint' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("ips", [])
    args["ips"] = field

    field = data.get("dns_records", [])
    args["dns_records"] = field

    field = data.get("port", 0)
    args["port"] = field

    field = data.get("private_network", None)
    args["private_network"] = unmarshal_EndpointPrivateNetworkDetails(field) if field is not None else None

    field = data.get("public", None)
    args["public"] = unmarshal_EndpointPublicDetails(field) if field is not None else None

    return Endpoint(**args)

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

def unmarshal_InstanceSnapshotSchedule(data: Any) -> InstanceSnapshotSchedule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstanceSnapshotSchedule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("frequency_hours", str())
    args["frequency_hours"] = field

    field = data.get("retention_days", str())
    args["retention_days"] = field

    field = data.get("enabled", str())
    args["enabled"] = field

    field = data.get("next_update", None)
    args["next_update"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("last_run", None)
    args["last_run"] = parser.isoparse(field) if isinstance(field, str) else field

    return InstanceSnapshotSchedule(**args)

def unmarshal_Volume(data: Any) -> Volume:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Volume' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", getattr(VolumeType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("size", 0)
    args["size"] = field

    return Volume(**args)

def unmarshal_Instance(data: Any) -> Instance:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Instance' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("status", getattr(InstanceStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("version", str())
    args["version"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("settings", [])
    args["settings"] = [unmarshal_InstanceSetting(v) for v in field] if field is not None else None

    field = data.get("node_number", 0)
    args["node_number"] = field

    field = data.get("node_type", str())
    args["node_type"] = field

    field = data.get("endpoints", [])
    args["endpoints"] = [unmarshal_Endpoint(v) for v in field] if field is not None else None

    field = data.get("region", )
    args["region"] = field

    field = data.get("volume", None)
    args["volume"] = unmarshal_Volume(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("snapshot_schedule", None)
    args["snapshot_schedule"] = unmarshal_InstanceSnapshotSchedule(field) if field is not None else None

    return Instance(**args)

def unmarshal_SnapshotVolumeType(data: Any) -> SnapshotVolumeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SnapshotVolumeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", str())
    args["type_"] = field

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

    field = data.get("status", getattr(SnapshotStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("size", 0)
    args["size"] = field

    field = data.get("instance_name", str())
    args["instance_name"] = field

    field = data.get("node_type", str())
    args["node_type"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("volume_type", None)
    args["volume_type"] = unmarshal_SnapshotVolumeType(field) if field is not None else None

    return Snapshot(**args)

def unmarshal_UserRole(data: Any) -> UserRole:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UserRole' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("role", getattr(UserRoleRole, "UNKNOWN_ROLE"))
    args["role"] = field

    field = data.get("database", None)
    args["database"] = field

    field = data.get("any_database", None)
    args["any_database"] = field

    return UserRole(**args)

def unmarshal_User(data: Any) -> User:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'User' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("roles", [])
    args["roles"] = [unmarshal_UserRole(v) for v in field] if field is not None else None

    return User(**args)

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

def unmarshal_NodeTypeVolumeType(data: Any) -> NodeTypeVolumeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeTypeVolumeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", getattr(VolumeType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("min_size", 0)
    args["min_size"] = field

    field = data.get("max_size", 0)
    args["max_size"] = field

    field = data.get("chunk_size", 0)
    args["chunk_size"] = field

    return NodeTypeVolumeType(**args)

def unmarshal_NodeType(data: Any) -> NodeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("stock_status", getattr(NodeTypeStock, "UNKNOWN_STOCK"))
    args["stock_status"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("vcpus", 0)
    args["vcpus"] = field

    field = data.get("memory", 0)
    args["memory"] = field

    field = data.get("available_volume_types", [])
    args["available_volume_types"] = [unmarshal_NodeTypeVolumeType(v) for v in field] if field is not None else None

    field = data.get("disabled", False)
    args["disabled"] = field

    field = data.get("beta", False)
    args["beta"] = field

    field = data.get("instance_range", str())
    args["instance_range"] = field

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

def unmarshal_Setting(data: Any) -> Setting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Setting' failed as data isn't a dictionary."
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

    field = data.get("property_type", getattr(SettingPropertyType, "BOOLEAN"))
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

    return Setting(**args)

def unmarshal_Version(data: Any) -> Version:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Version' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("version", str())
    args["version"] = field

    field = data.get("available_settings", [])
    args["available_settings"] = [unmarshal_Setting(v) for v in field] if field is not None else None

    field = data.get("end_of_life_at", None)
    args["end_of_life_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Version(**args)

def unmarshal_ListVersionsResponse(data: Any) -> ListVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("versions", [])
    args["versions"] = [unmarshal_Version(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListVersionsResponse(**args)

def marshal_EndpointSpecPrivateNetworkDetails(
    request: EndpointSpecPrivateNetworkDetails,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id
    else:
        output["private_network_id"] = str()


    return output

def marshal_EndpointSpecPublicDetails(
    request: EndpointSpecPublicDetails,
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
        resolve_one_of([
            OneOfPossibility(param="public", value=request.public,marshal_func=marshal_EndpointSpecPublicDetails
            ),
            OneOfPossibility(param="private_network", value=request.private_network,marshal_func=marshal_EndpointSpecPrivateNetworkDetails
            ),
        ]),
    )


    return output

def marshal_CreateEndpointRequest(
    request: CreateEndpointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.instance_id is not None:
        output["instance_id"] = request.instance_id
    else:
        output["instance_id"] = str()

    if request.endpoint is not None:
        output["endpoint"] = marshal_EndpointSpec(request.endpoint, defaults)
    else:
        output["endpoint"] = str()


    return output

def marshal_CreateInstanceRequestVolumeDetails(
    request: CreateInstanceRequestVolumeDetails,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.volume_size is not None:
        output["volume_size"] = request.volume_size
    else:
        output["volume_size"] = 0

    if request.volume_type is not None:
        output["volume_type"] = str(request.volume_type)
    else:
        output["volume_type"] = getattr(VolumeType, "UNKNOWN_TYPE")


    return output

def marshal_CreateInstanceRequest(
    request: CreateInstanceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.version is not None:
        output["version"] = request.version
    else:
        output["version"] = str()

    if request.node_number is not None:
        output["node_number"] = request.node_number
    else:
        output["node_number"] = str()

    if request.node_type is not None:
        output["node_type"] = request.node_type
    else:
        output["node_type"] = str()

    if request.user_name is not None:
        output["user_name"] = request.user_name
    else:
        output["user_name"] = str()

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.volume is not None:
        output["volume"] = marshal_CreateInstanceRequestVolumeDetails(request.volume, defaults)
    else:
        output["volume"] = None

    if request.endpoints is not None:
        output["endpoints"] = [marshal_EndpointSpec(item, defaults) for item in request.endpoints]
    else:
        output["endpoints"] = None


    return output

def marshal_CreateSnapshotRequest(
    request: CreateSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

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


    return output

def marshal_RestoreSnapshotRequestVolumeDetails(
    request: RestoreSnapshotRequestVolumeDetails,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.volume_type is not None:
        output["volume_type"] = str(request.volume_type)
    else:
        output["volume_type"] = getattr(VolumeType, "UNKNOWN_TYPE")


    return output

def marshal_RestoreSnapshotRequest(
    request: RestoreSnapshotRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.instance_name is not None:
        output["instance_name"] = request.instance_name
    else:
        output["instance_name"] = str()

    if request.node_type is not None:
        output["node_type"] = request.node_type
    else:
        output["node_type"] = str()

    if request.node_number is not None:
        output["node_number"] = request.node_number
    else:
        output["node_number"] = str()

    if request.volume is not None:
        output["volume"] = marshal_RestoreSnapshotRequestVolumeDetails(request.volume, defaults)
    else:
        output["volume"] = str()


    return output

def marshal_UserRole(
    request: UserRole,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="database", value=request.database,marshal_func=None
            ),
            OneOfPossibility(param="any_database", value=request.any_database,marshal_func=None
            ),
        ]),
    )

    if request.role is not None:
        output["role"] = str(request.role)
    else:
        output["role"] = getattr(UserRoleRole, "UNKNOWN_ROLE")


    return output

def marshal_SetUserRoleRequest(
    request: SetUserRoleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.user_name is not None:
        output["user_name"] = request.user_name
    else:
        output["user_name"] = str()

    if request.roles is not None:
        output["roles"] = [marshal_UserRole(item, defaults) for item in request.roles]
    else:
        output["roles"] = None


    return output

def marshal_UpdateInstanceRequest(
    request: UpdateInstanceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


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


    return output

def marshal_UpgradeInstanceRequest(
    request: UpgradeInstanceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="volume_size", value=request.volume_size,marshal_func=None
            ),
        ]),
    )


    return output
