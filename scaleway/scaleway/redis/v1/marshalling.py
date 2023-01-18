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
    ACLRule,
    ACLRuleSpec,
    AddAclRulesResponse,
    AddEndpointsResponse,
    AvailableClusterSetting,
    Cluster,
    ClusterMetricsResponse,
    ClusterSetting,
    ClusterSettingsResponse,
    ClusterVersion,
    Endpoint,
    EndpointSpec,
    EndpointSpecPrivateNetworkSpec,
    EndpointSpecPublicNetworkSpec,
    ListClusterVersionsResponse,
    ListClustersResponse,
    ListNodeTypesResponse,
    NodeType,
    PrivateNetwork,
    PublicNetwork,
    SetAclRulesResponse,
    SetEndpointsResponse,
    CreateClusterRequest,
    UpdateClusterRequest,
    MigrateClusterRequest,
    AddClusterSettingsRequest,
    SetClusterSettingsRequest,
    SetAclRulesRequest,
    AddAclRulesRequest,
    SetEndpointsRequest,
    AddEndpointsRequest,
    UpdateEndpointRequest,
)


def unmarshal_PrivateNetwork(data: Any) -> PrivateNetwork:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'PrivateNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id")
    args["id"] = field

    field = data.get("service_ips")
    args["service_ips"] = field

    field = data.get("zone")
    args["zone"] = field

    return PrivateNetwork(**args)


def unmarshal_PublicNetwork(data: Any) -> PublicNetwork:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'PublicNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return PublicNetwork(**args)


def unmarshal_ACLRule(data: Any) -> ACLRule:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ACLRule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description")
    args["description"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("ip_cidr")
    args["ip_cidr"] = field

    return ACLRule(**args)


def unmarshal_AvailableClusterSetting(data: Any) -> AvailableClusterSetting:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'AvailableClusterSetting' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("default_value")
    args["default_value"] = field

    field = data.get("deprecated")
    args["deprecated"] = field

    field = data.get("description")
    args["description"] = field

    field = data.get("max_value")
    args["max_value"] = field

    field = data.get("min_value")
    args["min_value"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("regex")
    args["regex"] = field

    field = data.get("type_")
    args["type_"] = field

    return AvailableClusterSetting(**args)


def unmarshal_ClusterSetting(data: Any) -> ClusterSetting:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ClusterSetting' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name")
    args["name"] = field

    field = data.get("value")
    args["value"] = field

    return ClusterSetting(**args)


def unmarshal_Endpoint(data: Any) -> Endpoint:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Endpoint' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id")
    args["id"] = field

    field = data.get("ips")
    args["ips"] = field

    field = data.get("port")
    args["port"] = field

    field = data.get("private_network")
    args["private_network"] = (
        unmarshal_PrivateNetwork(field) if field is not None else None
    )

    field = data.get("public_network")
    args["public_network"] = (
        unmarshal_PublicNetwork(field) if field is not None else None
    )

    return Endpoint(**args)


def unmarshal_Cluster(data: Any) -> Cluster:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Cluster' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("acl_rules")
    args["acl_rules"] = [unmarshal_ACLRule(v) for v in data["acl_rules"]]

    field = data.get("cluster_settings")
    args["cluster_settings"] = [
        unmarshal_ClusterSetting(v) for v in data["cluster_settings"]
    ]

    field = data.get("cluster_size")
    args["cluster_size"] = field

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("endpoints")
    args["endpoints"] = [unmarshal_Endpoint(v) for v in data["endpoints"]]

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("node_type")
    args["node_type"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("tags")
    args["tags"] = field

    field = data.get("tls_enabled")
    args["tls_enabled"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("upgradable_versions")
    args["upgradable_versions"] = field

    field = data.get("user_name")
    args["user_name"] = field

    field = data.get("version")
    args["version"] = field

    field = data.get("zone")
    args["zone"] = field

    return Cluster(**args)


def unmarshal_ClusterVersion(data: Any) -> ClusterVersion:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ClusterVersion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("available_settings")
    args["available_settings"] = [
        unmarshal_AvailableClusterSetting(v) for v in data["available_settings"]
    ]

    field = data.get("end_of_life_at")
    args["end_of_life_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("logo_url")
    args["logo_url"] = field

    field = data.get("version")
    args["version"] = field

    field = data.get("zone")
    args["zone"] = field

    return ClusterVersion(**args)


def unmarshal_NodeType(data: Any) -> NodeType:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'NodeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("beta")
    args["beta"] = field

    field = data.get("description")
    args["description"] = field

    field = data.get("disabled")
    args["disabled"] = field

    field = data.get("memory")
    args["memory"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("stock_status")
    args["stock_status"] = field

    field = data.get("vcpus")
    args["vcpus"] = field

    field = data.get("zone")
    args["zone"] = field

    return NodeType(**args)


def unmarshal_AddAclRulesResponse(data: Any) -> AddAclRulesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'AddAclRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("acl_rules")
    args["acl_rules"] = [unmarshal_ACLRule(v) for v in data["acl_rules"]]

    field = data.get("total_count")
    args["total_count"] = field

    return AddAclRulesResponse(**args)


def unmarshal_AddEndpointsResponse(data: Any) -> AddEndpointsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'AddEndpointsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("endpoints")
    args["endpoints"] = [unmarshal_Endpoint(v) for v in data["endpoints"]]

    field = data.get("total_count")
    args["total_count"] = field

    return AddEndpointsResponse(**args)


def unmarshal_ClusterMetricsResponse(data: Any) -> ClusterMetricsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ClusterMetricsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("timeseries")
    args["timeseries"] = [unmarshal_TimeSeries(v) for v in data["timeseries"]]

    return ClusterMetricsResponse(**args)


def unmarshal_ClusterSettingsResponse(data: Any) -> ClusterSettingsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ClusterSettingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("settings")
    args["settings"] = [unmarshal_ClusterSetting(v) for v in data["settings"]]

    return ClusterSettingsResponse(**args)


def unmarshal_ListClusterVersionsResponse(data: Any) -> ListClusterVersionsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListClusterVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count")
    args["total_count"] = field

    field = data.get("versions")
    args["versions"] = [unmarshal_ClusterVersion(v) for v in data["versions"]]

    return ListClusterVersionsResponse(**args)


def unmarshal_ListClustersResponse(data: Any) -> ListClustersResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListClustersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("clusters")
    args["clusters"] = [unmarshal_Cluster(v) for v in data["clusters"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListClustersResponse(**args)


def unmarshal_ListNodeTypesResponse(data: Any) -> ListNodeTypesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListNodeTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("node_types")
    args["node_types"] = [unmarshal_NodeType(v) for v in data["node_types"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListNodeTypesResponse(**args)


def unmarshal_SetAclRulesResponse(data: Any) -> SetAclRulesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SetAclRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("acl_rules")
    args["acl_rules"] = [unmarshal_ACLRule(v) for v in data["acl_rules"]]

    return SetAclRulesResponse(**args)


def unmarshal_SetEndpointsResponse(data: Any) -> SetEndpointsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SetEndpointsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("endpoints")
    args["endpoints"] = [unmarshal_Endpoint(v) for v in data["endpoints"]]

    return SetEndpointsResponse(**args)


def marshal_EndpointSpecPrivateNetworkSpec(
    request: EndpointSpecPrivateNetworkSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "id": request.id,
        "service_ips": request.service_ips,
    }


def marshal_EndpointSpecPublicNetworkSpec(
    request: EndpointSpecPublicNetworkSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {}


def marshal_ACLRuleSpec(
    request: ACLRuleSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "ip_cidr": request.ip_cidr,
    }


def marshal_ClusterSetting(
    request: ClusterSetting,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name": request.name,
        "value": request.value,
    }


def marshal_EndpointSpec(
    request: EndpointSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("private_network", request.private_network),
                OneOfPossibility("public_network", request.public_network),
            ]
        ),
    }


def marshal_AddAclRulesRequest(
    request: AddAclRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "acl_rules": [marshal_ACLRuleSpec(v, defaults) for v in request.acl_rules],
    }


def marshal_AddClusterSettingsRequest(
    request: AddClusterSettingsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "settings": [marshal_ClusterSetting(v, defaults) for v in request.settings],
    }


def marshal_AddEndpointsRequest(
    request: AddEndpointsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "endpoints": [marshal_EndpointSpec(v, defaults) for v in request.endpoints],
    }


def marshal_CreateClusterRequest(
    request: CreateClusterRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "acl_rules": [marshal_ACLRuleSpec(v, defaults) for v in request.acl_rules]
        if request.acl_rules is not None
        else None,
        "cluster_settings": [
            marshal_ClusterSetting(v, defaults) for v in request.cluster_settings
        ]
        if request.cluster_settings is not None
        else None,
        "cluster_size": request.cluster_size,
        "endpoints": [marshal_EndpointSpec(v, defaults) for v in request.endpoints]
        if request.endpoints is not None
        else None,
        "name": request.name,
        "node_type": request.node_type,
        "password": request.password,
        "project_id": request.project_id or defaults.default_project_id,
        "tags": request.tags,
        "tls_enabled": request.tls_enabled,
        "user_name": request.user_name,
        "version": request.version,
    }


def marshal_MigrateClusterRequest(
    request: MigrateClusterRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("version", request.version),
                OneOfPossibility("node_type", request.node_type),
                OneOfPossibility("cluster_size", request.cluster_size),
            ]
        ),
    }


def marshal_SetAclRulesRequest(
    request: SetAclRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "acl_rules": [marshal_ACLRuleSpec(v, defaults) for v in request.acl_rules],
    }


def marshal_SetClusterSettingsRequest(
    request: SetClusterSettingsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "settings": [marshal_ClusterSetting(v, defaults) for v in request.settings],
    }


def marshal_SetEndpointsRequest(
    request: SetEndpointsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "endpoints": [marshal_EndpointSpec(v, defaults) for v in request.endpoints],
    }


def marshal_UpdateClusterRequest(
    request: UpdateClusterRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name": request.name,
        "password": request.password,
        "tags": request.tags,
        "user_name": request.user_name,
    }


def marshal_UpdateEndpointRequest(
    request: UpdateEndpointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("private_network", request.private_network),
                OneOfPossibility("public_network", request.public_network),
            ]
        ),
    }
