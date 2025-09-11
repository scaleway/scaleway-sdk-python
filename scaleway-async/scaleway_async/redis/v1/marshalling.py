# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
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
    AvailableClusterSettingPropertyType,
    ClusterStatus,
    NodeTypeStock,
    PrivateNetworkProvisioningMode,
    ACLRule,
    PrivateNetwork,
    PublicNetwork,
    Endpoint,
    ClusterSetting,
    Cluster,
    AddAclRulesResponse,
    AddEndpointsResponse,
    ClusterMetricsResponse,
    ClusterSettingsResponse,
    AvailableClusterSetting,
    ClusterVersion,
    ListClusterVersionsResponse,
    ListClustersResponse,
    NodeType,
    ListNodeTypesResponse,
    SetAclRulesResponse,
    SetEndpointsResponse,
    ACLRuleSpec,
    AddAclRulesRequest,
    AddClusterSettingsRequest,
    EndpointSpecPrivateNetworkSpecIpamConfig,
    EndpointSpecPrivateNetworkSpec,
    EndpointSpecPublicNetworkSpec,
    EndpointSpec,
    AddEndpointsRequest,
    CreateClusterRequest,
    MigrateClusterRequest,
    SetAclRulesRequest,
    SetClusterSettingsRequest,
    SetEndpointsRequest,
    UpdateClusterRequest,
    UpdateEndpointRequest,
)


def unmarshal_ACLRule(data: Any) -> ACLRule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ACLRule' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("ip_cidr", None)
    if field is not None:
        args["ip_cidr"] = field
    else:
        args["ip_cidr"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    return ACLRule(**args)


def unmarshal_PrivateNetwork(data: Any) -> PrivateNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetwork' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("service_ips", None)
    if field is not None:
        args["service_ips"] = field
    else:
        args["service_ips"] = []

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("provisioning_mode", None)
    if field is not None:
        args["provisioning_mode"] = field
    else:
        args["provisioning_mode"] = PrivateNetworkProvisioningMode.STATIC

    return PrivateNetwork(**args)


def unmarshal_PublicNetwork(data: Any) -> PublicNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicNetwork' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return PublicNetwork(**args)


def unmarshal_Endpoint(data: Any) -> Endpoint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Endpoint' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("port", None)
    if field is not None:
        args["port"] = field
    else:
        args["port"] = 0

    field = data.get("ips", None)
    if field is not None:
        args["ips"] = field
    else:
        args["ips"] = []

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("private_network", None)
    if field is not None:
        args["private_network"] = unmarshal_PrivateNetwork(field)
    else:
        args["private_network"] = None

    field = data.get("public_network", None)
    if field is not None:
        args["public_network"] = unmarshal_PublicNetwork(field)
    else:
        args["public_network"] = None

    return Endpoint(**args)


def unmarshal_ClusterSetting(data: Any) -> ClusterSetting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterSetting' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("value", None)
    if field is not None:
        args["value"] = field
    else:
        args["value"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return ClusterSetting(**args)


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

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = ClusterStatus.UNKNOWN

    field = data.get("version", None)
    if field is not None:
        args["version"] = field
    else:
        args["version"] = None

    field = data.get("endpoints", None)
    if field is not None:
        args["endpoints"] = (
            [unmarshal_Endpoint(v) for v in field] if field is not None else None
        )
    else:
        args["endpoints"] = []

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("node_type", None)
    if field is not None:
        args["node_type"] = field
    else:
        args["node_type"] = None

    field = data.get("tls_enabled", None)
    if field is not None:
        args["tls_enabled"] = field
    else:
        args["tls_enabled"] = False

    field = data.get("cluster_settings", None)
    if field is not None:
        args["cluster_settings"] = (
            [unmarshal_ClusterSetting(v) for v in field] if field is not None else None
        )
    else:
        args["cluster_settings"] = []

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

    field = data.get("acl_rules", None)
    if field is not None:
        args["acl_rules"] = (
            [unmarshal_ACLRule(v) for v in field] if field is not None else None
        )
    else:
        args["acl_rules"] = []

    field = data.get("cluster_size", None)
    if field is not None:
        args["cluster_size"] = field
    else:
        args["cluster_size"] = 0

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("user_name", None)
    if field is not None:
        args["user_name"] = field
    else:
        args["user_name"] = None

    field = data.get("upgradable_versions", None)
    if field is not None:
        args["upgradable_versions"] = field
    else:
        args["upgradable_versions"] = []

    return Cluster(**args)


def unmarshal_AddAclRulesResponse(data: Any) -> AddAclRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddAclRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("acl_rules", None)
    if field is not None:
        args["acl_rules"] = (
            [unmarshal_ACLRule(v) for v in field] if field is not None else None
        )
    else:
        args["acl_rules"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return AddAclRulesResponse(**args)


def unmarshal_AddEndpointsResponse(data: Any) -> AddEndpointsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddEndpointsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("endpoints", None)
    if field is not None:
        args["endpoints"] = (
            [unmarshal_Endpoint(v) for v in field] if field is not None else None
        )
    else:
        args["endpoints"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return AddEndpointsResponse(**args)


def unmarshal_ClusterMetricsResponse(data: Any) -> ClusterMetricsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterMetricsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("timeseries", None)
    if field is not None:
        args["timeseries"] = (
            [unmarshal_TimeSeries(v) for v in field] if field is not None else None
        )
    else:
        args["timeseries"] = []

    return ClusterMetricsResponse(**args)


def unmarshal_ClusterSettingsResponse(data: Any) -> ClusterSettingsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterSettingsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("settings", None)
    if field is not None:
        args["settings"] = (
            [unmarshal_ClusterSetting(v) for v in field] if field is not None else None
        )
    else:
        args["settings"] = []

    return ClusterSettingsResponse(**args)


def unmarshal_AvailableClusterSetting(data: Any) -> AvailableClusterSetting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AvailableClusterSetting' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = AvailableClusterSettingPropertyType.UNKNOWN

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("deprecated", None)
    if field is not None:
        args["deprecated"] = field
    else:
        args["deprecated"] = False

    field = data.get("default_value", None)
    if field is not None:
        args["default_value"] = field
    else:
        args["default_value"] = None

    field = data.get("max_value", None)
    if field is not None:
        args["max_value"] = field
    else:
        args["max_value"] = 0

    field = data.get("min_value", None)
    if field is not None:
        args["min_value"] = field
    else:
        args["min_value"] = 0

    field = data.get("regex", None)
    if field is not None:
        args["regex"] = field
    else:
        args["regex"] = None

    return AvailableClusterSetting(**args)


def unmarshal_ClusterVersion(data: Any) -> ClusterVersion:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterVersion' failed as data isn't a dictionary."
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
            [unmarshal_AvailableClusterSetting(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["available_settings"] = []

    field = data.get("logo_url", None)
    if field is not None:
        args["logo_url"] = field
    else:
        args["logo_url"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("end_of_life_at", None)
    if field is not None:
        args["end_of_life_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["end_of_life_at"] = None

    return ClusterVersion(**args)


def unmarshal_ListClusterVersionsResponse(data: Any) -> ListClusterVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClusterVersionsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("versions", None)
    if field is not None:
        args["versions"] = (
            [unmarshal_ClusterVersion(v) for v in field] if field is not None else None
        )
    else:
        args["versions"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListClusterVersionsResponse(**args)


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
        args["stock_status"] = NodeTypeStock.UNKNOWN

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

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

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


def unmarshal_SetAclRulesResponse(data: Any) -> SetAclRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetAclRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("acl_rules", None)
    if field is not None:
        args["acl_rules"] = (
            [unmarshal_ACLRule(v) for v in field] if field is not None else None
        )
    else:
        args["acl_rules"] = []

    return SetAclRulesResponse(**args)


def unmarshal_SetEndpointsResponse(data: Any) -> SetEndpointsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetEndpointsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("endpoints", None)
    if field is not None:
        args["endpoints"] = (
            [unmarshal_Endpoint(v) for v in field] if field is not None else None
        )
    else:
        args["endpoints"] = []

    return SetEndpointsResponse(**args)


def marshal_ACLRuleSpec(
    request: ACLRuleSpec,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ip_cidr is not None:
        output["ip_cidr"] = request.ip_cidr

    if request.description is not None:
        output["description"] = request.description

    return output


def marshal_AddAclRulesRequest(
    request: AddAclRulesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.acl_rules is not None:
        output["acl_rules"] = [
            marshal_ACLRuleSpec(item, defaults) for item in request.acl_rules
        ]

    return output


def marshal_ClusterSetting(
    request: ClusterSetting,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.value is not None:
        output["value"] = request.value

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_AddClusterSettingsRequest(
    request: AddClusterSettingsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.settings is not None:
        output["settings"] = [
            marshal_ClusterSetting(item, defaults) for item in request.settings
        ]

    return output


def marshal_EndpointSpecPrivateNetworkSpecIpamConfig(
    request: EndpointSpecPrivateNetworkSpecIpamConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    return output


def marshal_EndpointSpecPrivateNetworkSpec(
    request: EndpointSpecPrivateNetworkSpec,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.service_ips is not None:
        output["service_ips"] = request.service_ips

    if request.ipam_config is not None:
        output["ipam_config"] = marshal_EndpointSpecPrivateNetworkSpecIpamConfig(
            request.ipam_config, defaults
        )

    return output


def marshal_EndpointSpecPublicNetworkSpec(
    request: EndpointSpecPublicNetworkSpec,
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
                    param="private_network",
                    value=request.private_network,
                    marshal_func=marshal_EndpointSpecPrivateNetworkSpec,
                ),
                OneOfPossibility(
                    param="public_network",
                    value=request.public_network,
                    marshal_func=marshal_EndpointSpecPublicNetworkSpec,
                ),
            ]
        ),
    )

    return output


def marshal_AddEndpointsRequest(
    request: AddEndpointsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.endpoints is not None:
        output["endpoints"] = [
            marshal_EndpointSpec(item, defaults) for item in request.endpoints
        ]

    return output


def marshal_CreateClusterRequest(
    request: CreateClusterRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.version is not None:
        output["version"] = request.version

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

    if request.user_name is not None:
        output["user_name"] = request.user_name

    if request.password is not None:
        output["password"] = request.password

    if request.tls_enabled is not None:
        output["tls_enabled"] = request.tls_enabled

    if request.cluster_size is not None:
        output["cluster_size"] = request.cluster_size

    if request.acl_rules is not None:
        output["acl_rules"] = [
            marshal_ACLRuleSpec(item, defaults) for item in request.acl_rules
        ]

    if request.endpoints is not None:
        output["endpoints"] = [
            marshal_EndpointSpec(item, defaults) for item in request.endpoints
        ]

    if request.cluster_settings is not None:
        output["cluster_settings"] = [
            marshal_ClusterSetting(item, defaults) for item in request.cluster_settings
        ]

    return output


def marshal_MigrateClusterRequest(
    request: MigrateClusterRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="version", value=request.version, marshal_func=None
                ),
                OneOfPossibility(
                    param="node_type", value=request.node_type, marshal_func=None
                ),
                OneOfPossibility(
                    param="cluster_size", value=request.cluster_size, marshal_func=None
                ),
            ]
        ),
    )

    return output


def marshal_SetAclRulesRequest(
    request: SetAclRulesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.acl_rules is not None:
        output["acl_rules"] = [
            marshal_ACLRuleSpec(item, defaults) for item in request.acl_rules
        ]

    return output


def marshal_SetClusterSettingsRequest(
    request: SetClusterSettingsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.settings is not None:
        output["settings"] = [
            marshal_ClusterSetting(item, defaults) for item in request.settings
        ]

    return output


def marshal_SetEndpointsRequest(
    request: SetEndpointsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.endpoints is not None:
        output["endpoints"] = [
            marshal_EndpointSpec(item, defaults) for item in request.endpoints
        ]

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

    if request.user_name is not None:
        output["user_name"] = request.user_name

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_UpdateEndpointRequest(
    request: UpdateEndpointRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="private_network",
                    value=request.private_network,
                    marshal_func=marshal_EndpointSpecPrivateNetworkSpec,
                ),
                OneOfPossibility(
                    param="public_network",
                    value=request.public_network,
                    marshal_func=marshal_EndpointSpecPublicNetworkSpec,
                ),
            ]
        ),
    )

    return output
