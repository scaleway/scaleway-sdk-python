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
    AvailableClusterSettingPropertyType,
    ClusterStatus,
    ListClustersRequestOrderBy,
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

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("ip_cidr", None)
    args["ip_cidr"] = field

    field = data.get("description", None)
    args["description"] = field

    return ACLRule(**args)

def unmarshal_PrivateNetwork(data: Any) -> PrivateNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("service_ips", [])
    args["service_ips"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("provisioning_mode", getattr(PrivateNetworkProvisioningMode, "STATIC"))
    args["provisioning_mode"] = field

    return PrivateNetwork(**args)

def unmarshal_PublicNetwork(data: Any) -> PublicNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return PublicNetwork(**args)

def unmarshal_Endpoint(data: Any) -> Endpoint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Endpoint' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("port", 0)
    args["port"] = field

    field = data.get("ips", [])
    args["ips"] = field

    field = data.get("id", str())
    args["id"] = field

    field = data.get("private_network", None)
    args["private_network"] = unmarshal_PrivateNetwork(field) if field is not None else None

    field = data.get("public_network", None)
    args["public_network"] = unmarshal_PublicNetwork(field) if field is not None else None

    return Endpoint(**args)

def unmarshal_ClusterSetting(data: Any) -> ClusterSetting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterSetting' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("value", str())
    args["value"] = field

    field = data.get("name", str())
    args["name"] = field

    return ClusterSetting(**args)

def unmarshal_Cluster(data: Any) -> Cluster:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Cluster' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("status", getattr(ClusterStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("version", str())
    args["version"] = field

    field = data.get("endpoints", [])
    args["endpoints"] = [unmarshal_Endpoint(v) for v in field] if field is not None else None

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("node_type", str())
    args["node_type"] = field

    field = data.get("tls_enabled", False)
    args["tls_enabled"] = field

    field = data.get("cluster_settings", [])
    args["cluster_settings"] = [unmarshal_ClusterSetting(v) for v in field] if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("acl_rules", [])
    args["acl_rules"] = [unmarshal_ACLRule(v) for v in field] if field is not None else None

    field = data.get("cluster_size", 0)
    args["cluster_size"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("user_name", str())
    args["user_name"] = field

    field = data.get("upgradable_versions", [])
    args["upgradable_versions"] = field

    return Cluster(**args)

def unmarshal_AddAclRulesResponse(data: Any) -> AddAclRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddAclRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("acl_rules", [])
    args["acl_rules"] = [unmarshal_ACLRule(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return AddAclRulesResponse(**args)

def unmarshal_AddEndpointsResponse(data: Any) -> AddEndpointsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddEndpointsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("endpoints", [])
    args["endpoints"] = [unmarshal_Endpoint(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return AddEndpointsResponse(**args)

def unmarshal_ClusterMetricsResponse(data: Any) -> ClusterMetricsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterMetricsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("timeseries", [])
    args["timeseries"] = [unmarshal_TimeSeries(v) for v in field] if field is not None else None

    return ClusterMetricsResponse(**args)

def unmarshal_ClusterSettingsResponse(data: Any) -> ClusterSettingsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterSettingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("settings", [])
    args["settings"] = [unmarshal_ClusterSetting(v) for v in field] if field is not None else None

    return ClusterSettingsResponse(**args)

def unmarshal_AvailableClusterSetting(data: Any) -> AvailableClusterSetting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AvailableClusterSetting' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("type", getattr(AvailableClusterSettingPropertyType, "UNKNOWN"))
    args["type_"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("deprecated", False)
    args["deprecated"] = field

    field = data.get("default_value", None)
    args["default_value"] = field

    field = data.get("max_value", None)
    args["max_value"] = field

    field = data.get("min_value", None)
    args["min_value"] = field

    field = data.get("regex", None)
    args["regex"] = field

    return AvailableClusterSetting(**args)

def unmarshal_ClusterVersion(data: Any) -> ClusterVersion:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterVersion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("version", str())
    args["version"] = field

    field = data.get("available_settings", [])
    args["available_settings"] = [unmarshal_AvailableClusterSetting(v) for v in field] if field is not None else None

    field = data.get("logo_url", str())
    args["logo_url"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("end_of_life_at", None)
    args["end_of_life_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return ClusterVersion(**args)

def unmarshal_ListClusterVersionsResponse(data: Any) -> ListClusterVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClusterVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("versions", [])
    args["versions"] = [unmarshal_ClusterVersion(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListClusterVersionsResponse(**args)

def unmarshal_ListClustersResponse(data: Any) -> ListClustersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClustersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("clusters", [])
    args["clusters"] = [unmarshal_Cluster(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListClustersResponse(**args)

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

    field = data.get("zone", )
    args["zone"] = field

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

def unmarshal_SetAclRulesResponse(data: Any) -> SetAclRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetAclRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("acl_rules", [])
    args["acl_rules"] = [unmarshal_ACLRule(v) for v in field] if field is not None else None

    return SetAclRulesResponse(**args)

def unmarshal_SetEndpointsResponse(data: Any) -> SetEndpointsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetEndpointsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("endpoints", [])
    args["endpoints"] = [unmarshal_Endpoint(v) for v in field] if field is not None else None

    return SetEndpointsResponse(**args)

def marshal_ACLRuleSpec(
    request: ACLRuleSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip_cidr is not None:
        output["ip_cidr"] = request.ip_cidr
    else:
        output["ip_cidr"] = str()

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()


    return output

def marshal_AddAclRulesRequest(
    request: AddAclRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.acl_rules is not None:
        output["acl_rules"] = [marshal_ACLRuleSpec(item, defaults) for item in request.acl_rules]
    else:
        output["acl_rules"] = str()


    return output

def marshal_ClusterSetting(
    request: ClusterSetting,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.value is not None:
        output["value"] = request.value
    else:
        output["value"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()


    return output

def marshal_AddClusterSettingsRequest(
    request: AddClusterSettingsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.settings is not None:
        output["settings"] = [marshal_ClusterSetting(item, defaults) for item in request.settings]
    else:
        output["settings"] = str()


    return output

def marshal_EndpointSpecPrivateNetworkSpecIpamConfig(
    request: EndpointSpecPrivateNetworkSpecIpamConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}


    return output

def marshal_EndpointSpecPrivateNetworkSpec(
    request: EndpointSpecPrivateNetworkSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.service_ips is not None:
        output["service_ips"] = request.service_ips
    else:
        output["service_ips"] = []

    if request.ipam_config is not None:
        output["ipam_config"] = marshal_EndpointSpecPrivateNetworkSpecIpamConfig(request.ipam_config, defaults)
    else:
        output["ipam_config"] = None


    return output

def marshal_EndpointSpecPublicNetworkSpec(
    request: EndpointSpecPublicNetworkSpec,
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
            OneOfPossibility(param="private_network", value=request.private_network,marshal_func=marshal_EndpointSpecPrivateNetworkSpec
            ),
            OneOfPossibility(param="public_network", value=request.public_network,marshal_func=marshal_EndpointSpecPublicNetworkSpec
            ),
        ]),
    )


    return output

def marshal_AddEndpointsRequest(
    request: AddEndpointsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.endpoints is not None:
        output["endpoints"] = [marshal_EndpointSpec(item, defaults) for item in request.endpoints]
    else:
        output["endpoints"] = str()


    return output

def marshal_CreateClusterRequest(
    request: CreateClusterRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.version is not None:
        output["version"] = request.version
    else:
        output["version"] = str()

    if request.node_type is not None:
        output["node_type"] = request.node_type
    else:
        output["node_type"] = str()

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

    if request.user_name is not None:
        output["user_name"] = request.user_name
    else:
        output["user_name"] = str()

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = str()

    if request.tls_enabled is not None:
        output["tls_enabled"] = request.tls_enabled
    else:
        output["tls_enabled"] = False

    if request.cluster_size is not None:
        output["cluster_size"] = request.cluster_size
    else:
        output["cluster_size"] = None

    if request.acl_rules is not None:
        output["acl_rules"] = [marshal_ACLRuleSpec(item, defaults) for item in request.acl_rules]
    else:
        output["acl_rules"] = None

    if request.endpoints is not None:
        output["endpoints"] = [marshal_EndpointSpec(item, defaults) for item in request.endpoints]
    else:
        output["endpoints"] = None

    if request.cluster_settings is not None:
        output["cluster_settings"] = [marshal_ClusterSetting(item, defaults) for item in request.cluster_settings]
    else:
        output["cluster_settings"] = None


    return output

def marshal_MigrateClusterRequest(
    request: MigrateClusterRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="version", value=request.version,marshal_func=None
            ),
            OneOfPossibility(param="node_type", value=request.node_type,marshal_func=None
            ),
            OneOfPossibility(param="cluster_size", value=request.cluster_size,marshal_func=None
            ),
        ]),
    )


    return output

def marshal_SetAclRulesRequest(
    request: SetAclRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.acl_rules is not None:
        output["acl_rules"] = [marshal_ACLRuleSpec(item, defaults) for item in request.acl_rules]
    else:
        output["acl_rules"] = str()


    return output

def marshal_SetClusterSettingsRequest(
    request: SetClusterSettingsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.settings is not None:
        output["settings"] = [marshal_ClusterSetting(item, defaults) for item in request.settings]
    else:
        output["settings"] = str()


    return output

def marshal_SetEndpointsRequest(
    request: SetEndpointsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.endpoints is not None:
        output["endpoints"] = [marshal_EndpointSpec(item, defaults) for item in request.endpoints]
    else:
        output["endpoints"] = str()


    return output

def marshal_UpdateClusterRequest(
    request: UpdateClusterRequest,
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

    if request.user_name is not None:
        output["user_name"] = request.user_name
    else:
        output["user_name"] = None

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = None


    return output

def marshal_UpdateEndpointRequest(
    request: UpdateEndpointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="private_network", value=request.private_network,marshal_func=marshal_EndpointSpecPrivateNetworkSpec
            ),
            OneOfPossibility(param="public_network", value=request.public_network,marshal_func=marshal_EndpointSpecPublicNetworkSpec
            ),
        ]),
    )


    return output
