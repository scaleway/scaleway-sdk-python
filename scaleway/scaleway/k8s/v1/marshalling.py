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
    AutoscalerEstimator,
    AutoscalerExpander,
    CNI,
    ClusterStatus,
    ClusterTypeAvailability,
    ClusterTypeResiliency,
    ListClustersRequestOrderBy,
    ListNodesRequestOrderBy,
    ListPoolsRequestOrderBy,
    MaintenanceWindowDayOfTheWeek,
    NodeStatus,
    PoolStatus,
    PoolVolumeType,
    Runtime,
    PoolUpgradePolicy,
    Pool,
    Version,
    MaintenanceWindow,
    ClusterAutoUpgrade,
    ClusterAutoscalerConfig,
    ClusterOpenIDConnectConfig,
    Cluster,
    Node,
    ACLRule,
    AddClusterACLRulesResponse,
    ExternalNodeCoreV1Taint,
    ExternalNode,
    ExternalNodeAuth,
    ListClusterACLRulesResponse,
    ClusterType,
    ListClusterAvailableTypesResponse,
    ListClusterAvailableVersionsResponse,
    ListClusterTypesResponse,
    ListClustersResponse,
    ListNodesResponse,
    ListPoolsResponse,
    ListVersionsResponse,
    NodeMetadataCoreV1Taint,
    NodeMetadata,
    SetClusterACLRulesResponse,
    ACLRuleRequest,
    AddClusterACLRulesRequest,
    CreateClusterRequestPoolConfigUpgradePolicy,
    CreateClusterRequestAutoUpgrade,
    CreateClusterRequestAutoscalerConfig,
    CreateClusterRequestOpenIDConnectConfig,
    CreateClusterRequestPoolConfig,
    CreateClusterRequest,
    CreatePoolRequestUpgradePolicy,
    CreatePoolRequest,
    MigratePoolsToNewImagesRequest,
    SetClusterACLRulesRequest,
    SetClusterTypeRequest,
    UpdateClusterRequestAutoUpgrade,
    UpdateClusterRequestAutoscalerConfig,
    UpdateClusterRequestOpenIDConnectConfig,
    UpdateClusterRequest,
    UpdatePoolRequestUpgradePolicy,
    UpdatePoolRequest,
    UpgradeClusterRequest,
    UpgradePoolRequest,
)

def unmarshal_PoolUpgradePolicy(data: Any) -> PoolUpgradePolicy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PoolUpgradePolicy' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("max_unavailable", str())
    args["max_unavailable"] = field

    field = data.get("max_surge", str())
    args["max_surge"] = field

    return PoolUpgradePolicy(**args)

def unmarshal_Pool(data: Any) -> Pool:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Pool' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("cluster_id", str())
    args["cluster_id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("status", getattr(PoolStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("version", str())
    args["version"] = field

    field = data.get("node_type", str())
    args["node_type"] = field

    field = data.get("autoscaling", False)
    args["autoscaling"] = field

    field = data.get("size", str())
    args["size"] = field

    field = data.get("min_size", 0)
    args["min_size"] = field

    field = data.get("max_size", 0)
    args["max_size"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("container_runtime", getattr(Runtime, "UNKNOWN_RUNTIME"))
    args["container_runtime"] = field

    field = data.get("autohealing", False)
    args["autohealing"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("kubelet_args", {})
    args["kubelet_args"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("root_volume_type", getattr(PoolVolumeType, "DEFAULT_VOLUME_TYPE"))
    args["root_volume_type"] = field

    field = data.get("public_ip_disabled", False)
    args["public_ip_disabled"] = field

    field = data.get("security_group_id", str())
    args["security_group_id"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("placement_group_id", None)
    args["placement_group_id"] = field

    field = data.get("upgrade_policy", None)
    args["upgrade_policy"] = unmarshal_PoolUpgradePolicy(field) if field is not None else None

    field = data.get("root_volume_size", None)
    args["root_volume_size"] = field

    field = data.get("new_images_enabled", None)
    args["new_images_enabled"] = field

    return Pool(**args)

def unmarshal_Version(data: Any) -> Version:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Version' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("label", str())
    args["label"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("available_cnis", [])
    args["available_cnis"] = [CNI(v) for v in field] if field is not None else None

    field = data.get("available_container_runtimes", [])
    args["available_container_runtimes"] = [Runtime(v) for v in field] if field is not None else None

    field = data.get("available_feature_gates", [])
    args["available_feature_gates"] = field

    field = data.get("available_admission_plugins", [])
    args["available_admission_plugins"] = field

    field = data.get("available_kubelet_args", {})
    args["available_kubelet_args"] = field

    return Version(**args)

def unmarshal_MaintenanceWindow(data: Any) -> MaintenanceWindow:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'MaintenanceWindow' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("start_hour", 0)
    args["start_hour"] = field

    field = data.get("day", getattr(MaintenanceWindowDayOfTheWeek, "ANY"))
    args["day"] = field

    return MaintenanceWindow(**args)

def unmarshal_ClusterAutoUpgrade(data: Any) -> ClusterAutoUpgrade:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterAutoUpgrade' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("enabled", False)
    args["enabled"] = field

    field = data.get("maintenance_window", None)
    args["maintenance_window"] = unmarshal_MaintenanceWindow(field) if field is not None else None

    return ClusterAutoUpgrade(**args)

def unmarshal_ClusterAutoscalerConfig(data: Any) -> ClusterAutoscalerConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterAutoscalerConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("scale_down_disabled", False)
    args["scale_down_disabled"] = field

    field = data.get("scale_down_delay_after_add", str())
    args["scale_down_delay_after_add"] = field

    field = data.get("estimator", getattr(AutoscalerEstimator, "UNKNOWN_ESTIMATOR"))
    args["estimator"] = field

    field = data.get("expander", getattr(AutoscalerExpander, "UNKNOWN_EXPANDER"))
    args["expander"] = field

    field = data.get("ignore_daemonsets_utilization", False)
    args["ignore_daemonsets_utilization"] = field

    field = data.get("balance_similar_node_groups", False)
    args["balance_similar_node_groups"] = field

    field = data.get("expendable_pods_priority_cutoff", 0)
    args["expendable_pods_priority_cutoff"] = field

    field = data.get("scale_down_unneeded_time", str())
    args["scale_down_unneeded_time"] = field

    field = data.get("scale_down_utilization_threshold", 0.0)
    args["scale_down_utilization_threshold"] = field

    field = data.get("max_graceful_termination_sec", 0)
    args["max_graceful_termination_sec"] = field

    return ClusterAutoscalerConfig(**args)

def unmarshal_ClusterOpenIDConnectConfig(data: Any) -> ClusterOpenIDConnectConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterOpenIDConnectConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("issuer_url", str())
    args["issuer_url"] = field

    field = data.get("client_id", str())
    args["client_id"] = field

    field = data.get("username_claim", str())
    args["username_claim"] = field

    field = data.get("username_prefix", str())
    args["username_prefix"] = field

    field = data.get("groups_claim", [])
    args["groups_claim"] = field

    field = data.get("groups_prefix", str())
    args["groups_prefix"] = field

    field = data.get("required_claim", [])
    args["required_claim"] = field

    return ClusterOpenIDConnectConfig(**args)

def unmarshal_Cluster(data: Any) -> Cluster:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Cluster' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("status", getattr(ClusterStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("version", str())
    args["version"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("cni", getattr(CNI, "UNKNOWN_CNI"))
    args["cni"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("cluster_url", str())
    args["cluster_url"] = field

    field = data.get("dns_wildcard", str())
    args["dns_wildcard"] = field

    field = data.get("upgrade_available", False)
    args["upgrade_available"] = field

    field = data.get("feature_gates", [])
    args["feature_gates"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("autoscaler_config", None)
    args["autoscaler_config"] = unmarshal_ClusterAutoscalerConfig(field) if field is not None else None

    field = data.get("auto_upgrade", None)
    args["auto_upgrade"] = unmarshal_ClusterAutoUpgrade(field) if field is not None else None

    field = data.get("admission_plugins", [])
    args["admission_plugins"] = field

    field = data.get("apiserver_cert_sans", [])
    args["apiserver_cert_sans"] = field

    field = data.get("iam_nodes_group_id", str())
    args["iam_nodes_group_id"] = field

    field = data.get("open_id_connect_config", None)
    args["open_id_connect_config"] = unmarshal_ClusterOpenIDConnectConfig(field) if field is not None else None

    field = data.get("private_network_id", None)
    args["private_network_id"] = field

    field = data.get("commitment_ends_at", None)
    args["commitment_ends_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("acl_available", None)
    args["acl_available"] = field

    field = data.get("new_images_enabled", None)
    args["new_images_enabled"] = field

    return Cluster(**args)

def unmarshal_Node(data: Any) -> Node:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Node' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("pool_id", str())
    args["pool_id"] = field

    field = data.get("cluster_id", str())
    args["cluster_id"] = field

    field = data.get("provider_id", str())
    args["provider_id"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("public_ip_v4", None)
    args["public_ip_v4"] = field

    field = data.get("public_ip_v6", None)
    args["public_ip_v6"] = field

    field = data.get("conditions", None)
    args["conditions"] = field

    field = data.get("status", getattr(NodeStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("error_message", None)
    args["error_message"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Node(**args)

def unmarshal_ACLRule(data: Any) -> ACLRule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ACLRule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("ip", None)
    args["ip"] = field

    field = data.get("scaleway_ranges", None)
    args["scaleway_ranges"] = field

    return ACLRule(**args)

def unmarshal_AddClusterACLRulesResponse(data: Any) -> AddClusterACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddClusterACLRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", [])
    args["rules"] = [unmarshal_ACLRule(v) for v in field] if field is not None else None

    return AddClusterACLRulesResponse(**args)

def unmarshal_ExternalNodeCoreV1Taint(data: Any) -> ExternalNodeCoreV1Taint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ExternalNodeCoreV1Taint' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("key", str())
    args["key"] = field

    field = data.get("value", str())
    args["value"] = field

    field = data.get("effect", str())
    args["effect"] = field

    return ExternalNodeCoreV1Taint(**args)

def unmarshal_ExternalNode(data: Any) -> ExternalNode:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ExternalNode' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("cluster_url", str())
    args["cluster_url"] = field

    field = data.get("pool_version", str())
    args["pool_version"] = field

    field = data.get("cluster_ca", str())
    args["cluster_ca"] = field

    field = data.get("kube_token", str())
    args["kube_token"] = field

    field = data.get("kubelet_config", str())
    args["kubelet_config"] = field

    field = data.get("external_ip", str())
    args["external_ip"] = field

    field = data.get("containerd_version", str())
    args["containerd_version"] = field

    field = data.get("runc_version", str())
    args["runc_version"] = field

    field = data.get("cni_plugins_version", str())
    args["cni_plugins_version"] = field

    field = data.get("node_labels", str())
    args["node_labels"] = field

    field = data.get("node_taints", str())
    args["node_taints"] = [unmarshal_ExternalNodeCoreV1Taint(v) for v in field] if field is not None else None

    field = data.get("iam_token", str())
    args["iam_token"] = field

    return ExternalNode(**args)

def unmarshal_ExternalNodeAuth(data: Any) -> ExternalNodeAuth:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ExternalNodeAuth' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("node_secret_key", str())
    args["node_secret_key"] = field

    field = data.get("metadata_url", str())
    args["metadata_url"] = field

    return ExternalNodeAuth(**args)

def unmarshal_ListClusterACLRulesResponse(data: Any) -> ListClusterACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClusterACLRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("rules", [])
    args["rules"] = [unmarshal_ACLRule(v) for v in field] if field is not None else None

    return ListClusterACLRulesResponse(**args)

def unmarshal_ClusterType(data: Any) -> ClusterType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("availability", getattr(ClusterTypeAvailability, "AVAILABLE"))
    args["availability"] = field

    field = data.get("max_nodes", 0)
    args["max_nodes"] = field

    field = data.get("sla", 0.0)
    args["sla"] = field

    field = data.get("resiliency", getattr(ClusterTypeResiliency, "UNKNOWN_RESILIENCY"))
    args["resiliency"] = field

    field = data.get("memory", 0)
    args["memory"] = field

    field = data.get("dedicated", False)
    args["dedicated"] = field

    field = data.get("audit_logs_supported", False)
    args["audit_logs_supported"] = field

    field = data.get("max_etcd_size", 0)
    args["max_etcd_size"] = field

    field = data.get("commitment_delay", None)
    args["commitment_delay"] = field

    return ClusterType(**args)

def unmarshal_ListClusterAvailableTypesResponse(data: Any) -> ListClusterAvailableTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClusterAvailableTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("cluster_types", [])
    args["cluster_types"] = [unmarshal_ClusterType(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListClusterAvailableTypesResponse(**args)

def unmarshal_ListClusterAvailableVersionsResponse(data: Any) -> ListClusterAvailableVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClusterAvailableVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("versions", [])
    args["versions"] = [unmarshal_Version(v) for v in field] if field is not None else None

    return ListClusterAvailableVersionsResponse(**args)

def unmarshal_ListClusterTypesResponse(data: Any) -> ListClusterTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClusterTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("cluster_types", [])
    args["cluster_types"] = [unmarshal_ClusterType(v) for v in field] if field is not None else None

    return ListClusterTypesResponse(**args)

def unmarshal_ListClustersResponse(data: Any) -> ListClustersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClustersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("clusters", [])
    args["clusters"] = [unmarshal_Cluster(v) for v in field] if field is not None else None

    return ListClustersResponse(**args)

def unmarshal_ListNodesResponse(data: Any) -> ListNodesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNodesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("nodes", [])
    args["nodes"] = [unmarshal_Node(v) for v in field] if field is not None else None

    return ListNodesResponse(**args)

def unmarshal_ListPoolsResponse(data: Any) -> ListPoolsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPoolsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("pools", [])
    args["pools"] = [unmarshal_Pool(v) for v in field] if field is not None else None

    return ListPoolsResponse(**args)

def unmarshal_ListVersionsResponse(data: Any) -> ListVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("versions", [])
    args["versions"] = [unmarshal_Version(v) for v in field] if field is not None else None

    return ListVersionsResponse(**args)

def unmarshal_NodeMetadataCoreV1Taint(data: Any) -> NodeMetadataCoreV1Taint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeMetadataCoreV1Taint' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("key", str())
    args["key"] = field

    field = data.get("value", str())
    args["value"] = field

    field = data.get("effect", str())
    args["effect"] = field

    return NodeMetadataCoreV1Taint(**args)

def unmarshal_NodeMetadata(data: Any) -> NodeMetadata:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeMetadata' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("cluster_url", str())
    args["cluster_url"] = field

    field = data.get("cluster_ca", str())
    args["cluster_ca"] = field

    field = data.get("credential_provider_config", str())
    args["credential_provider_config"] = field

    field = data.get("pool_version", str())
    args["pool_version"] = field

    field = data.get("kubelet_config", str())
    args["kubelet_config"] = field

    field = data.get("node_labels", str())
    args["node_labels"] = field

    field = data.get("node_taints", str())
    args["node_taints"] = [unmarshal_NodeMetadataCoreV1Taint(v) for v in field] if field is not None else None

    field = data.get("has_gpu", str())
    args["has_gpu"] = field

    field = data.get("external_ip", str())
    args["external_ip"] = field

    field = data.get("repo_uri", str())
    args["repo_uri"] = field

    return NodeMetadata(**args)

def unmarshal_SetClusterACLRulesResponse(data: Any) -> SetClusterACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetClusterACLRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", [])
    args["rules"] = [unmarshal_ACLRule(v) for v in field] if field is not None else None

    return SetClusterACLRulesResponse(**args)

def marshal_ACLRuleRequest(
    request: ACLRuleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="ip", value=request.ip,marshal_func=None
            ),
            OneOfPossibility(param="scaleway_ranges", value=request.scaleway_ranges,marshal_func=None
            ),
        ]),
    )

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()


    return output

def marshal_AddClusterACLRulesRequest(
    request: AddClusterACLRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.acls is not None:
        output["acls"] = [marshal_ACLRuleRequest(item, defaults) for item in request.acls]
    else:
        output["acls"] = None


    return output

def marshal_MaintenanceWindow(
    request: MaintenanceWindow,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.start_hour is not None:
        output["start_hour"] = request.start_hour
    else:
        output["start_hour"] = 0

    if request.day is not None:
        output["day"] = str(request.day)
    else:
        output["day"] = getattr(MaintenanceWindowDayOfTheWeek, "ANY")


    return output

def marshal_CreateClusterRequestPoolConfigUpgradePolicy(
    request: CreateClusterRequestPoolConfigUpgradePolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.max_unavailable is not None:
        output["max_unavailable"] = request.max_unavailable
    else:
        output["max_unavailable"] = None

    if request.max_surge is not None:
        output["max_surge"] = request.max_surge
    else:
        output["max_surge"] = None


    return output

def marshal_CreateClusterRequestAutoUpgrade(
    request: CreateClusterRequestAutoUpgrade,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.enable is not None:
        output["enable"] = request.enable
    else:
        output["enable"] = False

    if request.maintenance_window is not None:
        output["maintenance_window"] = marshal_MaintenanceWindow(request.maintenance_window, defaults)
    else:
        output["maintenance_window"] = None


    return output

def marshal_CreateClusterRequestAutoscalerConfig(
    request: CreateClusterRequestAutoscalerConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.estimator is not None:
        output["estimator"] = str(request.estimator)
    else:
        output["estimator"] = getattr(AutoscalerEstimator, "UNKNOWN_ESTIMATOR")

    if request.expander is not None:
        output["expander"] = str(request.expander)
    else:
        output["expander"] = getattr(AutoscalerExpander, "UNKNOWN_EXPANDER")

    if request.scale_down_disabled is not None:
        output["scale_down_disabled"] = request.scale_down_disabled
    else:
        output["scale_down_disabled"] = None

    if request.scale_down_delay_after_add is not None:
        output["scale_down_delay_after_add"] = request.scale_down_delay_after_add
    else:
        output["scale_down_delay_after_add"] = None

    if request.ignore_daemonsets_utilization is not None:
        output["ignore_daemonsets_utilization"] = request.ignore_daemonsets_utilization
    else:
        output["ignore_daemonsets_utilization"] = None

    if request.balance_similar_node_groups is not None:
        output["balance_similar_node_groups"] = request.balance_similar_node_groups
    else:
        output["balance_similar_node_groups"] = None

    if request.expendable_pods_priority_cutoff is not None:
        output["expendable_pods_priority_cutoff"] = request.expendable_pods_priority_cutoff
    else:
        output["expendable_pods_priority_cutoff"] = None

    if request.scale_down_unneeded_time is not None:
        output["scale_down_unneeded_time"] = request.scale_down_unneeded_time
    else:
        output["scale_down_unneeded_time"] = None

    if request.scale_down_utilization_threshold is not None:
        output["scale_down_utilization_threshold"] = request.scale_down_utilization_threshold
    else:
        output["scale_down_utilization_threshold"] = None

    if request.max_graceful_termination_sec is not None:
        output["max_graceful_termination_sec"] = request.max_graceful_termination_sec
    else:
        output["max_graceful_termination_sec"] = None


    return output

def marshal_CreateClusterRequestOpenIDConnectConfig(
    request: CreateClusterRequestOpenIDConnectConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.issuer_url is not None:
        output["issuer_url"] = request.issuer_url
    else:
        output["issuer_url"] = str()

    if request.client_id is not None:
        output["client_id"] = request.client_id
    else:
        output["client_id"] = str()

    if request.username_claim is not None:
        output["username_claim"] = request.username_claim
    else:
        output["username_claim"] = None

    if request.username_prefix is not None:
        output["username_prefix"] = request.username_prefix
    else:
        output["username_prefix"] = None

    if request.groups_claim is not None:
        output["groups_claim"] = request.groups_claim
    else:
        output["groups_claim"] = None

    if request.groups_prefix is not None:
        output["groups_prefix"] = request.groups_prefix
    else:
        output["groups_prefix"] = None

    if request.required_claim is not None:
        output["required_claim"] = request.required_claim
    else:
        output["required_claim"] = None


    return output

def marshal_CreateClusterRequestPoolConfig(
    request: CreateClusterRequestPoolConfig,
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
        output["node_type"] = str()

    if request.autoscaling is not None:
        output["autoscaling"] = request.autoscaling
    else:
        output["autoscaling"] = False

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = str()

    if request.container_runtime is not None:
        output["container_runtime"] = str(request.container_runtime)
    else:
        output["container_runtime"] = getattr(Runtime, "UNKNOWN_RUNTIME")

    if request.placement_group_id is not None:
        output["placement_group_id"] = request.placement_group_id
    else:
        output["placement_group_id"] = None

    if request.min_size is not None:
        output["min_size"] = request.min_size
    else:
        output["min_size"] = None

    if request.max_size is not None:
        output["max_size"] = request.max_size
    else:
        output["max_size"] = None

    if request.autohealing is not None:
        output["autohealing"] = request.autohealing
    else:
        output["autohealing"] = False

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = []

    if request.kubelet_args is not None:
        output["kubelet_args"] = {
            key: value
            for key, value in request.kubelet_args.items()
        }
    else:
        output["kubelet_args"] = {}

    if request.zone is not None:
        output["zone"] = request.zone or defaults.default_zone

    if request.root_volume_type is not None:
        output["root_volume_type"] = str(request.root_volume_type)
    else:
        output["root_volume_type"] = getattr(PoolVolumeType, "DEFAULT_VOLUME_TYPE")

    if request.public_ip_disabled is not None:
        output["public_ip_disabled"] = request.public_ip_disabled
    else:
        output["public_ip_disabled"] = False

    if request.upgrade_policy is not None:
        output["upgrade_policy"] = marshal_CreateClusterRequestPoolConfigUpgradePolicy(request.upgrade_policy, defaults)
    else:
        output["upgrade_policy"] = None

    if request.root_volume_size is not None:
        output["root_volume_size"] = request.root_volume_size
    else:
        output["root_volume_size"] = None

    if request.security_group_id is not None:
        output["security_group_id"] = request.security_group_id
    else:
        output["security_group_id"] = None


    return output

def marshal_CreateClusterRequest(
    request: CreateClusterRequest,
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

    if request.type_ is not None:
        output["type"] = request.type_
    else:
        output["type"] = str()

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.version is not None:
        output["version"] = request.version
    else:
        output["version"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.cni is not None:
        output["cni"] = str(request.cni)
    else:
        output["cni"] = str()

    if request.pools is not None:
        output["pools"] = [marshal_CreateClusterRequestPoolConfig(item, defaults) for item in request.pools]
    else:
        output["pools"] = None

    if request.autoscaler_config is not None:
        output["autoscaler_config"] = marshal_CreateClusterRequestAutoscalerConfig(request.autoscaler_config, defaults)
    else:
        output["autoscaler_config"] = None

    if request.auto_upgrade is not None:
        output["auto_upgrade"] = marshal_CreateClusterRequestAutoUpgrade(request.auto_upgrade, defaults)
    else:
        output["auto_upgrade"] = None

    if request.feature_gates is not None:
        output["feature_gates"] = request.feature_gates
    else:
        output["feature_gates"] = None

    if request.admission_plugins is not None:
        output["admission_plugins"] = request.admission_plugins
    else:
        output["admission_plugins"] = None

    if request.open_id_connect_config is not None:
        output["open_id_connect_config"] = marshal_CreateClusterRequestOpenIDConnectConfig(request.open_id_connect_config, defaults)
    else:
        output["open_id_connect_config"] = None

    if request.apiserver_cert_sans is not None:
        output["apiserver_cert_sans"] = request.apiserver_cert_sans
    else:
        output["apiserver_cert_sans"] = None

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id
    else:
        output["private_network_id"] = None


    return output

def marshal_CreatePoolRequestUpgradePolicy(
    request: CreatePoolRequestUpgradePolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.max_unavailable is not None:
        output["max_unavailable"] = request.max_unavailable
    else:
        output["max_unavailable"] = None

    if request.max_surge is not None:
        output["max_surge"] = request.max_surge
    else:
        output["max_surge"] = None


    return output

def marshal_CreatePoolRequest(
    request: CreatePoolRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.node_type is not None:
        output["node_type"] = request.node_type
    else:
        output["node_type"] = str()

    if request.autoscaling is not None:
        output["autoscaling"] = request.autoscaling
    else:
        output["autoscaling"] = False

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.placement_group_id is not None:
        output["placement_group_id"] = request.placement_group_id
    else:
        output["placement_group_id"] = None

    if request.min_size is not None:
        output["min_size"] = request.min_size
    else:
        output["min_size"] = None

    if request.autohealing is not None:
        output["autohealing"] = request.autohealing
    else:
        output["autohealing"] = False

    if request.public_ip_disabled is not None:
        output["public_ip_disabled"] = request.public_ip_disabled
    else:
        output["public_ip_disabled"] = False

    if request.max_size is not None:
        output["max_size"] = request.max_size
    else:
        output["max_size"] = None

    if request.container_runtime is not None:
        output["container_runtime"] = str(request.container_runtime)
    else:
        output["container_runtime"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.kubelet_args is not None:
        output["kubelet_args"] = {
            key: value
            for key, value in request.kubelet_args.items()
        }
    else:
        output["kubelet_args"] = None

    if request.upgrade_policy is not None:
        output["upgrade_policy"] = marshal_CreatePoolRequestUpgradePolicy(request.upgrade_policy, defaults)
    else:
        output["upgrade_policy"] = None

    if request.zone is not None:
        output["zone"] = request.zone or defaults.default_zone

    if request.root_volume_type is not None:
        output["root_volume_type"] = str(request.root_volume_type)
    else:
        output["root_volume_type"] = None

    if request.root_volume_size is not None:
        output["root_volume_size"] = request.root_volume_size
    else:
        output["root_volume_size"] = None

    if request.security_group_id is not None:
        output["security_group_id"] = request.security_group_id
    else:
        output["security_group_id"] = None


    return output

def marshal_MigratePoolsToNewImagesRequest(
    request: MigratePoolsToNewImagesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.pool_ids is not None:
        output["pool_ids"] = request.pool_ids
    else:
        output["pool_ids"] = None


    return output

def marshal_SetClusterACLRulesRequest(
    request: SetClusterACLRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.acls is not None:
        output["acls"] = [marshal_ACLRuleRequest(item, defaults) for item in request.acls]
    else:
        output["acls"] = None


    return output

def marshal_SetClusterTypeRequest(
    request: SetClusterTypeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_
    else:
        output["type"] = str()


    return output

def marshal_UpdateClusterRequestAutoUpgrade(
    request: UpdateClusterRequestAutoUpgrade,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.enable is not None:
        output["enable"] = request.enable
    else:
        output["enable"] = None

    if request.maintenance_window is not None:
        output["maintenance_window"] = marshal_MaintenanceWindow(request.maintenance_window, defaults)
    else:
        output["maintenance_window"] = None


    return output

def marshal_UpdateClusterRequestAutoscalerConfig(
    request: UpdateClusterRequestAutoscalerConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.estimator is not None:
        output["estimator"] = str(request.estimator)
    else:
        output["estimator"] = getattr(AutoscalerEstimator, "UNKNOWN_ESTIMATOR")

    if request.expander is not None:
        output["expander"] = str(request.expander)
    else:
        output["expander"] = getattr(AutoscalerExpander, "UNKNOWN_EXPANDER")

    if request.scale_down_disabled is not None:
        output["scale_down_disabled"] = request.scale_down_disabled
    else:
        output["scale_down_disabled"] = None

    if request.scale_down_delay_after_add is not None:
        output["scale_down_delay_after_add"] = request.scale_down_delay_after_add
    else:
        output["scale_down_delay_after_add"] = None

    if request.ignore_daemonsets_utilization is not None:
        output["ignore_daemonsets_utilization"] = request.ignore_daemonsets_utilization
    else:
        output["ignore_daemonsets_utilization"] = None

    if request.balance_similar_node_groups is not None:
        output["balance_similar_node_groups"] = request.balance_similar_node_groups
    else:
        output["balance_similar_node_groups"] = None

    if request.expendable_pods_priority_cutoff is not None:
        output["expendable_pods_priority_cutoff"] = request.expendable_pods_priority_cutoff
    else:
        output["expendable_pods_priority_cutoff"] = None

    if request.scale_down_unneeded_time is not None:
        output["scale_down_unneeded_time"] = request.scale_down_unneeded_time
    else:
        output["scale_down_unneeded_time"] = None

    if request.scale_down_utilization_threshold is not None:
        output["scale_down_utilization_threshold"] = request.scale_down_utilization_threshold
    else:
        output["scale_down_utilization_threshold"] = None

    if request.max_graceful_termination_sec is not None:
        output["max_graceful_termination_sec"] = request.max_graceful_termination_sec
    else:
        output["max_graceful_termination_sec"] = None


    return output

def marshal_UpdateClusterRequestOpenIDConnectConfig(
    request: UpdateClusterRequestOpenIDConnectConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.issuer_url is not None:
        output["issuer_url"] = request.issuer_url
    else:
        output["issuer_url"] = None

    if request.client_id is not None:
        output["client_id"] = request.client_id
    else:
        output["client_id"] = None

    if request.username_claim is not None:
        output["username_claim"] = request.username_claim
    else:
        output["username_claim"] = None

    if request.username_prefix is not None:
        output["username_prefix"] = request.username_prefix
    else:
        output["username_prefix"] = None

    if request.groups_claim is not None:
        output["groups_claim"] = request.groups_claim
    else:
        output["groups_claim"] = None

    if request.groups_prefix is not None:
        output["groups_prefix"] = request.groups_prefix
    else:
        output["groups_prefix"] = None

    if request.required_claim is not None:
        output["required_claim"] = request.required_claim
    else:
        output["required_claim"] = None


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

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.autoscaler_config is not None:
        output["autoscaler_config"] = marshal_UpdateClusterRequestAutoscalerConfig(request.autoscaler_config, defaults)
    else:
        output["autoscaler_config"] = None

    if request.auto_upgrade is not None:
        output["auto_upgrade"] = marshal_UpdateClusterRequestAutoUpgrade(request.auto_upgrade, defaults)
    else:
        output["auto_upgrade"] = None

    if request.feature_gates is not None:
        output["feature_gates"] = request.feature_gates
    else:
        output["feature_gates"] = None

    if request.admission_plugins is not None:
        output["admission_plugins"] = request.admission_plugins
    else:
        output["admission_plugins"] = None

    if request.open_id_connect_config is not None:
        output["open_id_connect_config"] = marshal_UpdateClusterRequestOpenIDConnectConfig(request.open_id_connect_config, defaults)
    else:
        output["open_id_connect_config"] = None

    if request.apiserver_cert_sans is not None:
        output["apiserver_cert_sans"] = request.apiserver_cert_sans
    else:
        output["apiserver_cert_sans"] = None


    return output

def marshal_UpdatePoolRequestUpgradePolicy(
    request: UpdatePoolRequestUpgradePolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.max_unavailable is not None:
        output["max_unavailable"] = request.max_unavailable
    else:
        output["max_unavailable"] = None

    if request.max_surge is not None:
        output["max_surge"] = request.max_surge
    else:
        output["max_surge"] = None


    return output

def marshal_UpdatePoolRequest(
    request: UpdatePoolRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.autoscaling is not None:
        output["autoscaling"] = request.autoscaling
    else:
        output["autoscaling"] = None

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = None

    if request.min_size is not None:
        output["min_size"] = request.min_size
    else:
        output["min_size"] = None

    if request.max_size is not None:
        output["max_size"] = request.max_size
    else:
        output["max_size"] = None

    if request.autohealing is not None:
        output["autohealing"] = request.autohealing
    else:
        output["autohealing"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.kubelet_args is not None:
        output["kubelet_args"] = request.kubelet_args
    else:
        output["kubelet_args"] = None

    if request.upgrade_policy is not None:
        output["upgrade_policy"] = marshal_UpdatePoolRequestUpgradePolicy(request.upgrade_policy, defaults)
    else:
        output["upgrade_policy"] = None


    return output

def marshal_UpgradeClusterRequest(
    request: UpgradeClusterRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.version is not None:
        output["version"] = request.version
    else:
        output["version"] = str()

    if request.upgrade_pools is not None:
        output["upgrade_pools"] = request.upgrade_pools
    else:
        output["upgrade_pools"] = False


    return output

def marshal_UpgradePoolRequest(
    request: UpgradePoolRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.version is not None:
        output["version"] = request.version
    else:
        output["version"] = str()


    return output
