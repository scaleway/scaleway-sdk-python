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
    ClusterStatus,
    NodeTypeStock,
    VolumeType,
    EndpointPrivateNetworkDetails,
    EndpointPublicDetails,
    Endpoint,
    ClusterSetting,
    Volume,
    Cluster,
    User,
    ListClustersResponse,
    NodeTypeVolumeType,
    NodeType,
    ListNodeTypesResponse,
    ListUsersResponse,
    VersionAvailableSettingBooleanProperty,
    VersionAvailableSettingFloatProperty,
    VersionAvailableSettingIntegerProperty,
    VersionAvailableSettingStringProperty,
    VersionAvailableSetting,
    Version,
    ListVersionsResponse,
    EndpointSpecPrivateNetworkDetails,
    EndpointSpecPublicDetails,
    CreateClusterRequestVolumeSpec,
    EndpointSpec,
    CreateClusterRequest,
    CreateEndpointRequest,
    UpdateClusterRequest,
    UpdateUserRequest,
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

    field = data.get("public_network", None)
    if field is not None:
        args["public_network"] = unmarshal_EndpointPublicDetails(field)
    else:
        args["public_network"] = None

    return Endpoint(**args)


def unmarshal_ClusterSetting(data: Any) -> ClusterSetting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterSetting' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("bool_value", None)
    if field is not None:
        args["bool_value"] = field
    else:
        args["bool_value"] = False

    field = data.get("string_value", None)
    if field is not None:
        args["string_value"] = field
    else:
        args["string_value"] = None

    field = data.get("int_value", None)
    if field is not None:
        args["int_value"] = field
    else:
        args["int_value"] = 0

    field = data.get("float_value", None)
    if field is not None:
        args["float_value"] = field
    else:
        args["float_value"] = 0.0

    return ClusterSetting(**args)


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


def unmarshal_Cluster(data: Any) -> Cluster:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Cluster' failed as data isn't a dictionary."
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
        args["status"] = ClusterStatus.UNKNOWN_STATUS

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
            [unmarshal_ClusterSetting(v) for v in field] if field is not None else None
        )
    else:
        args["settings"] = []

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

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return Cluster(**args)


def unmarshal_User(data: Any) -> User:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'User' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("username", None)
    if field is not None:
        args["username"] = field
    else:
        args["username"] = None

    return User(**args)


def unmarshal_ListClustersResponse(data: Any) -> ListClustersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClustersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("clusters", None)
    if field is not None:
        args["clusters"] = (
            [unmarshal_Cluster(v) for v in field] if field is not None else None
        )
    else:
        args["clusters"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListClustersResponse(**args)


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

    field = data.get("cluster_range", None)
    if field is not None:
        args["cluster_range"] = field
    else:
        args["cluster_range"] = None

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
        args["users"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    return ListUsersResponse(**args)


def unmarshal_VersionAvailableSettingBooleanProperty(
    data: Any,
) -> VersionAvailableSettingBooleanProperty:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VersionAvailableSettingBooleanProperty' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("default_value", None)
    if field is not None:
        args["default_value"] = field
    else:
        args["default_value"] = None

    return VersionAvailableSettingBooleanProperty(**args)


def unmarshal_VersionAvailableSettingFloatProperty(
    data: Any,
) -> VersionAvailableSettingFloatProperty:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VersionAvailableSettingFloatProperty' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("min", None)
    if field is not None:
        args["min"] = field
    else:
        args["min"] = None

    field = data.get("max", None)
    if field is not None:
        args["max"] = field
    else:
        args["max"] = None

    field = data.get("default_value", None)
    if field is not None:
        args["default_value"] = field
    else:
        args["default_value"] = None

    field = data.get("unit", None)
    if field is not None:
        args["unit"] = field
    else:
        args["unit"] = None

    return VersionAvailableSettingFloatProperty(**args)


def unmarshal_VersionAvailableSettingIntegerProperty(
    data: Any,
) -> VersionAvailableSettingIntegerProperty:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VersionAvailableSettingIntegerProperty' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("min", None)
    if field is not None:
        args["min"] = field
    else:
        args["min"] = None

    field = data.get("max", None)
    if field is not None:
        args["max"] = field
    else:
        args["max"] = None

    field = data.get("default_value", None)
    if field is not None:
        args["default_value"] = field
    else:
        args["default_value"] = None

    field = data.get("unit", None)
    if field is not None:
        args["unit"] = field
    else:
        args["unit"] = None

    return VersionAvailableSettingIntegerProperty(**args)


def unmarshal_VersionAvailableSettingStringProperty(
    data: Any,
) -> VersionAvailableSettingStringProperty:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VersionAvailableSettingStringProperty' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("default_value", None)
    if field is not None:
        args["default_value"] = field
    else:
        args["default_value"] = None

    field = data.get("string_constraint", None)
    if field is not None:
        args["string_constraint"] = field
    else:
        args["string_constraint"] = None

    return VersionAvailableSettingStringProperty(**args)


def unmarshal_VersionAvailableSetting(data: Any) -> VersionAvailableSetting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VersionAvailableSetting' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

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

    field = data.get("bool_property", None)
    if field is not None:
        args["bool_property"] = unmarshal_VersionAvailableSettingBooleanProperty(field)
    else:
        args["bool_property"] = None

    field = data.get("string_property", None)
    if field is not None:
        args["string_property"] = unmarshal_VersionAvailableSettingStringProperty(field)
    else:
        args["string_property"] = None

    field = data.get("int_property", None)
    if field is not None:
        args["int_property"] = unmarshal_VersionAvailableSettingIntegerProperty(field)
    else:
        args["int_property"] = None

    field = data.get("float_property", None)
    if field is not None:
        args["float_property"] = unmarshal_VersionAvailableSettingFloatProperty(field)
    else:
        args["float_property"] = None

    return VersionAvailableSetting(**args)


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
            [unmarshal_VersionAvailableSetting(v) for v in field]
            if field is not None
            else None
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


def marshal_CreateClusterRequestVolumeSpec(
    request: CreateClusterRequestVolumeSpec,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.size_bytes is not None:
        output["size_bytes"] = request.size_bytes

    if request.type_ is not None:
        output["type"] = request.type_

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


def marshal_CreateClusterRequest(
    request: CreateClusterRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.version is not None:
        output["version"] = request.version

    if request.node_amount is not None:
        output["node_amount"] = request.node_amount

    if request.node_type is not None:
        output["node_type"] = request.node_type

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.volume is not None:
        output["volume"] = marshal_CreateClusterRequestVolumeSpec(
            request.volume, defaults
        )

    if request.endpoints is not None:
        output["endpoints"] = [
            marshal_EndpointSpec(item, defaults) for item in request.endpoints
        ]

    if request.user_name is not None:
        output["user_name"] = request.user_name

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_CreateEndpointRequest(
    request: CreateEndpointRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.cluster_id is not None:
        output["cluster_id"] = request.cluster_id

    if request.endpoint is not None:
        output["endpoint"] = marshal_EndpointSpec(request.endpoint, defaults)

    return output


def marshal_UpdateClusterRequest(
    request: UpdateClusterRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateUserRequest(
    request: UpdateUserRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.password is not None:
        output["password"] = request.password

    return output
