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
    CNI,
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
    ExternalNodeCoreV1Taint,
    ExternalNode,
    ExternalNodeAuth,
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
    CreateClusterRequestPoolConfigUpgradePolicy,
    CreateClusterRequestAutoUpgrade,
    CreateClusterRequestAutoscalerConfig,
    CreateClusterRequestOpenIDConnectConfig,
    CreateClusterRequestPoolConfig,
    CreateClusterRequest,
    CreatePoolRequestUpgradePolicy,
    CreatePoolRequest,
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

    field = data.get("max_unavailable", None)
    if field is not None:
        args["max_unavailable"] = field

    field = data.get("max_surge", None)
    if field is not None:
        args["max_surge"] = field

    return PoolUpgradePolicy(**args)


def unmarshal_Pool(data: Any) -> Pool:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Pool' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("cluster_id", None)
    if field is not None:
        args["cluster_id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("version", None)
    if field is not None:
        args["version"] = field

    field = data.get("node_type", None)
    if field is not None:
        args["node_type"] = field

    field = data.get("autoscaling", None)
    if field is not None:
        args["autoscaling"] = field

    field = data.get("size", None)
    if field is not None:
        args["size"] = field

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

    field = data.get("min_size", None)
    if field is not None:
        args["min_size"] = field

    field = data.get("max_size", None)
    if field is not None:
        args["max_size"] = field

    field = data.get("container_runtime", None)
    if field is not None:
        args["container_runtime"] = field

    field = data.get("autohealing", None)
    if field is not None:
        args["autohealing"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("kubelet_args", None)
    if field is not None:
        args["kubelet_args"] = field

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field

    field = data.get("root_volume_type", None)
    if field is not None:
        args["root_volume_type"] = field

    field = data.get("public_ip_disabled", None)
    if field is not None:
        args["public_ip_disabled"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("placement_group_id", None)
    if field is not None:
        args["placement_group_id"] = field
    else:
        args["placement_group_id"] = None

    field = data.get("upgrade_policy", None)
    if field is not None:
        args["upgrade_policy"] = unmarshal_PoolUpgradePolicy(field)
    else:
        args["upgrade_policy"] = None

    field = data.get("root_volume_size", None)
    if field is not None:
        args["root_volume_size"] = field
    else:
        args["root_volume_size"] = None

    return Pool(**args)


def unmarshal_Version(data: Any) -> Version:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Version' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("label", None)
    if field is not None:
        args["label"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("available_cnis", None)
    if field is not None:
        args["available_cnis"] = [CNI(v) for v in field] if field is not None else None

    field = data.get("available_container_runtimes", None)
    if field is not None:
        args["available_container_runtimes"] = (
            [Runtime(v) for v in field] if field is not None else None
        )

    field = data.get("available_feature_gates", None)
    if field is not None:
        args["available_feature_gates"] = field

    field = data.get("available_admission_plugins", None)
    if field is not None:
        args["available_admission_plugins"] = field

    field = data.get("available_kubelet_args", None)
    if field is not None:
        args["available_kubelet_args"] = field

    return Version(**args)


def unmarshal_MaintenanceWindow(data: Any) -> MaintenanceWindow:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'MaintenanceWindow' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("start_hour", None)
    if field is not None:
        args["start_hour"] = field

    field = data.get("day", None)
    if field is not None:
        args["day"] = field

    return MaintenanceWindow(**args)


def unmarshal_ClusterAutoUpgrade(data: Any) -> ClusterAutoUpgrade:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterAutoUpgrade' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("enabled", None)
    if field is not None:
        args["enabled"] = field

    field = data.get("maintenance_window", None)
    if field is not None:
        args["maintenance_window"] = unmarshal_MaintenanceWindow(field)
    else:
        args["maintenance_window"] = None

    return ClusterAutoUpgrade(**args)


def unmarshal_ClusterAutoscalerConfig(data: Any) -> ClusterAutoscalerConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterAutoscalerConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("scale_down_disabled", None)
    if field is not None:
        args["scale_down_disabled"] = field

    field = data.get("scale_down_delay_after_add", None)
    if field is not None:
        args["scale_down_delay_after_add"] = field

    field = data.get("estimator", None)
    if field is not None:
        args["estimator"] = field

    field = data.get("expander", None)
    if field is not None:
        args["expander"] = field

    field = data.get("ignore_daemonsets_utilization", None)
    if field is not None:
        args["ignore_daemonsets_utilization"] = field

    field = data.get("balance_similar_node_groups", None)
    if field is not None:
        args["balance_similar_node_groups"] = field

    field = data.get("expendable_pods_priority_cutoff", None)
    if field is not None:
        args["expendable_pods_priority_cutoff"] = field

    field = data.get("scale_down_unneeded_time", None)
    if field is not None:
        args["scale_down_unneeded_time"] = field

    field = data.get("scale_down_utilization_threshold", None)
    if field is not None:
        args["scale_down_utilization_threshold"] = field

    field = data.get("max_graceful_termination_sec", None)
    if field is not None:
        args["max_graceful_termination_sec"] = field

    return ClusterAutoscalerConfig(**args)


def unmarshal_ClusterOpenIDConnectConfig(data: Any) -> ClusterOpenIDConnectConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterOpenIDConnectConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("issuer_url", None)
    if field is not None:
        args["issuer_url"] = field

    field = data.get("client_id", None)
    if field is not None:
        args["client_id"] = field

    field = data.get("username_claim", None)
    if field is not None:
        args["username_claim"] = field

    field = data.get("username_prefix", None)
    if field is not None:
        args["username_prefix"] = field

    field = data.get("groups_claim", None)
    if field is not None:
        args["groups_claim"] = field

    field = data.get("groups_prefix", None)
    if field is not None:
        args["groups_prefix"] = field

    field = data.get("required_claim", None)
    if field is not None:
        args["required_claim"] = field

    return ClusterOpenIDConnectConfig(**args)


def unmarshal_Cluster(data: Any) -> Cluster:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Cluster' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("version", None)
    if field is not None:
        args["version"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("cni", None)
    if field is not None:
        args["cni"] = field

    field = data.get("description", None)
    if field is not None:
        args["description"] = field

    field = data.get("cluster_url", None)
    if field is not None:
        args["cluster_url"] = field

    field = data.get("dns_wildcard", None)
    if field is not None:
        args["dns_wildcard"] = field

    field = data.get("upgrade_available", None)
    if field is not None:
        args["upgrade_available"] = field

    field = data.get("feature_gates", None)
    if field is not None:
        args["feature_gates"] = field

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

    field = data.get("autoscaler_config", None)
    if field is not None:
        args["autoscaler_config"] = unmarshal_ClusterAutoscalerConfig(field)
    else:
        args["autoscaler_config"] = None

    field = data.get("auto_upgrade", None)
    if field is not None:
        args["auto_upgrade"] = unmarshal_ClusterAutoUpgrade(field)
    else:
        args["auto_upgrade"] = None

    field = data.get("admission_plugins", None)
    if field is not None:
        args["admission_plugins"] = field

    field = data.get("apiserver_cert_sans", None)
    if field is not None:
        args["apiserver_cert_sans"] = field

    field = data.get("open_id_connect_config", None)
    if field is not None:
        args["open_id_connect_config"] = unmarshal_ClusterOpenIDConnectConfig(field)
    else:
        args["open_id_connect_config"] = None

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field
    else:
        args["private_network_id"] = None

    field = data.get("commitment_ends_at", None)
    if field is not None:
        args["commitment_ends_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["commitment_ends_at"] = None

    field = data.get("routed_ip_enabled", None)
    if field is not None:
        args["routed_ip_enabled"] = field
    else:
        args["routed_ip_enabled"] = None

    field = data.get("sbs_csi_enabled", None)
    if field is not None:
        args["sbs_csi_enabled"] = field
    else:
        args["sbs_csi_enabled"] = None

    return Cluster(**args)


def unmarshal_Node(data: Any) -> Node:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Node' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("pool_id", None)
    if field is not None:
        args["pool_id"] = field

    field = data.get("cluster_id", None)
    if field is not None:
        args["cluster_id"] = field

    field = data.get("provider_id", None)
    if field is not None:
        args["provider_id"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("public_ip_v4", None)
    if field is not None:
        args["public_ip_v4"] = field
    else:
        args["public_ip_v4"] = None

    field = data.get("public_ip_v6", None)
    if field is not None:
        args["public_ip_v6"] = field
    else:
        args["public_ip_v6"] = None

    field = data.get("conditions", None)
    if field is not None:
        args["conditions"] = field
    else:
        args["conditions"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

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

    return Node(**args)


def unmarshal_ExternalNodeCoreV1Taint(data: Any) -> ExternalNodeCoreV1Taint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ExternalNodeCoreV1Taint' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("key", None)
    if field is not None:
        args["key"] = field

    field = data.get("value", None)
    if field is not None:
        args["value"] = field

    field = data.get("effect", None)
    if field is not None:
        args["effect"] = field

    return ExternalNodeCoreV1Taint(**args)


def unmarshal_ExternalNode(data: Any) -> ExternalNode:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ExternalNode' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("cluster_url", None)
    if field is not None:
        args["cluster_url"] = field

    field = data.get("pool_version", None)
    if field is not None:
        args["pool_version"] = field

    field = data.get("cluster_ca", None)
    if field is not None:
        args["cluster_ca"] = field

    field = data.get("kube_token", None)
    if field is not None:
        args["kube_token"] = field

    field = data.get("kubelet_config", None)
    if field is not None:
        args["kubelet_config"] = field

    field = data.get("external_ip", None)
    if field is not None:
        args["external_ip"] = field

    field = data.get("containerd_version", None)
    if field is not None:
        args["containerd_version"] = field

    field = data.get("runc_version", None)
    if field is not None:
        args["runc_version"] = field

    field = data.get("cni_plugins_version", None)
    if field is not None:
        args["cni_plugins_version"] = field

    field = data.get("node_labels", None)
    if field is not None:
        args["node_labels"] = field

    field = data.get("node_taints", None)
    if field is not None:
        args["node_taints"] = (
            [unmarshal_ExternalNodeCoreV1Taint(v) for v in field]
            if field is not None
            else None
        )

    return ExternalNode(**args)


def unmarshal_ExternalNodeAuth(data: Any) -> ExternalNodeAuth:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ExternalNodeAuth' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("node_token", None)
    if field is not None:
        args["node_token"] = field

    field = data.get("api_url", None)
    if field is not None:
        args["api_url"] = field

    return ExternalNodeAuth(**args)


def unmarshal_ClusterType(data: Any) -> ClusterType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("availability", None)
    if field is not None:
        args["availability"] = field

    field = data.get("max_nodes", None)
    if field is not None:
        args["max_nodes"] = field

    field = data.get("sla", None)
    if field is not None:
        args["sla"] = field

    field = data.get("resiliency", None)
    if field is not None:
        args["resiliency"] = field

    field = data.get("memory", None)
    if field is not None:
        args["memory"] = field

    field = data.get("dedicated", None)
    if field is not None:
        args["dedicated"] = field

    field = data.get("audit_logs_supported", None)
    if field is not None:
        args["audit_logs_supported"] = field

    field = data.get("max_etcd_size", None)
    if field is not None:
        args["max_etcd_size"] = field

    field = data.get("commitment_delay", None)
    if field is not None:
        args["commitment_delay"] = field
    else:
        args["commitment_delay"] = None

    return ClusterType(**args)


def unmarshal_ListClusterAvailableTypesResponse(
    data: Any,
) -> ListClusterAvailableTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClusterAvailableTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("cluster_types", None)
    if field is not None:
        args["cluster_types"] = (
            [unmarshal_ClusterType(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListClusterAvailableTypesResponse(**args)


def unmarshal_ListClusterAvailableVersionsResponse(
    data: Any,
) -> ListClusterAvailableVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClusterAvailableVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("versions", None)
    if field is not None:
        args["versions"] = (
            [unmarshal_Version(v) for v in field] if field is not None else None
        )

    return ListClusterAvailableVersionsResponse(**args)


def unmarshal_ListClusterTypesResponse(data: Any) -> ListClusterTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClusterTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("cluster_types", None)
    if field is not None:
        args["cluster_types"] = (
            [unmarshal_ClusterType(v) for v in field] if field is not None else None
        )

    return ListClusterTypesResponse(**args)


def unmarshal_ListClustersResponse(data: Any) -> ListClustersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClustersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("clusters", None)
    if field is not None:
        args["clusters"] = (
            [unmarshal_Cluster(v) for v in field] if field is not None else None
        )

    return ListClustersResponse(**args)


def unmarshal_ListNodesResponse(data: Any) -> ListNodesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNodesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("nodes", None)
    if field is not None:
        args["nodes"] = (
            [unmarshal_Node(v) for v in field] if field is not None else None
        )

    return ListNodesResponse(**args)


def unmarshal_ListPoolsResponse(data: Any) -> ListPoolsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPoolsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("pools", None)
    if field is not None:
        args["pools"] = (
            [unmarshal_Pool(v) for v in field] if field is not None else None
        )

    return ListPoolsResponse(**args)


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

    return ListVersionsResponse(**args)


def unmarshal_NodeMetadataCoreV1Taint(data: Any) -> NodeMetadataCoreV1Taint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeMetadataCoreV1Taint' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("key", None)
    if field is not None:
        args["key"] = field

    field = data.get("value", None)
    if field is not None:
        args["value"] = field

    field = data.get("effect", None)
    if field is not None:
        args["effect"] = field

    return NodeMetadataCoreV1Taint(**args)


def unmarshal_NodeMetadata(data: Any) -> NodeMetadata:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeMetadata' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("cluster_url", None)
    if field is not None:
        args["cluster_url"] = field

    field = data.get("cluster_ca", None)
    if field is not None:
        args["cluster_ca"] = field

    field = data.get("credential_provider_config", None)
    if field is not None:
        args["credential_provider_config"] = field

    field = data.get("pool_version", None)
    if field is not None:
        args["pool_version"] = field

    field = data.get("kubelet_config", None)
    if field is not None:
        args["kubelet_config"] = field

    field = data.get("node_labels", None)
    if field is not None:
        args["node_labels"] = field

    field = data.get("node_taints", None)
    if field is not None:
        args["node_taints"] = (
            [unmarshal_NodeMetadataCoreV1Taint(v) for v in field]
            if field is not None
            else None
        )

    field = data.get("private_network_mode", None)
    if field is not None:
        args["private_network_mode"] = field

    field = data.get("kapsule_iface_mac", None)
    if field is not None:
        args["kapsule_iface_mac"] = field

    field = data.get("full_isolation", None)
    if field is not None:
        args["full_isolation"] = field

    field = data.get("has_gpu", None)
    if field is not None:
        args["has_gpu"] = field

    field = data.get("external_ip", None)
    if field is not None:
        args["external_ip"] = field

    return NodeMetadata(**args)


def marshal_MaintenanceWindow(
    request: MaintenanceWindow,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.start_hour is not None:
        output["start_hour"] = request.start_hour

    if request.day is not None:
        output["day"] = str(request.day)

    return output


def marshal_CreateClusterRequestPoolConfigUpgradePolicy(
    request: CreateClusterRequestPoolConfigUpgradePolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.max_unavailable is not None:
        output["max_unavailable"] = request.max_unavailable

    if request.max_surge is not None:
        output["max_surge"] = request.max_surge

    return output


def marshal_CreateClusterRequestAutoUpgrade(
    request: CreateClusterRequestAutoUpgrade,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.enable is not None:
        output["enable"] = request.enable

    if request.maintenance_window is not None:
        output["maintenance_window"] = marshal_MaintenanceWindow(
            request.maintenance_window, defaults
        )

    return output


def marshal_CreateClusterRequestAutoscalerConfig(
    request: CreateClusterRequestAutoscalerConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.estimator is not None:
        output["estimator"] = str(request.estimator)

    if request.expander is not None:
        output["expander"] = str(request.expander)

    if request.scale_down_disabled is not None:
        output["scale_down_disabled"] = request.scale_down_disabled

    if request.scale_down_delay_after_add is not None:
        output["scale_down_delay_after_add"] = request.scale_down_delay_after_add

    if request.ignore_daemonsets_utilization is not None:
        output["ignore_daemonsets_utilization"] = request.ignore_daemonsets_utilization

    if request.balance_similar_node_groups is not None:
        output["balance_similar_node_groups"] = request.balance_similar_node_groups

    if request.expendable_pods_priority_cutoff is not None:
        output["expendable_pods_priority_cutoff"] = (
            request.expendable_pods_priority_cutoff
        )

    if request.scale_down_unneeded_time is not None:
        output["scale_down_unneeded_time"] = request.scale_down_unneeded_time

    if request.scale_down_utilization_threshold is not None:
        output["scale_down_utilization_threshold"] = (
            request.scale_down_utilization_threshold
        )

    if request.max_graceful_termination_sec is not None:
        output["max_graceful_termination_sec"] = request.max_graceful_termination_sec

    return output


def marshal_CreateClusterRequestOpenIDConnectConfig(
    request: CreateClusterRequestOpenIDConnectConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.issuer_url is not None:
        output["issuer_url"] = request.issuer_url

    if request.client_id is not None:
        output["client_id"] = request.client_id

    if request.username_claim is not None:
        output["username_claim"] = request.username_claim

    if request.username_prefix is not None:
        output["username_prefix"] = request.username_prefix

    if request.groups_claim is not None:
        output["groups_claim"] = request.groups_claim

    if request.groups_prefix is not None:
        output["groups_prefix"] = request.groups_prefix

    if request.required_claim is not None:
        output["required_claim"] = request.required_claim

    return output


def marshal_CreateClusterRequestPoolConfig(
    request: CreateClusterRequestPoolConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.node_type is not None:
        output["node_type"] = request.node_type

    if request.autoscaling is not None:
        output["autoscaling"] = request.autoscaling

    if request.size is not None:
        output["size"] = request.size

    if request.container_runtime is not None:
        output["container_runtime"] = str(request.container_runtime)

    if request.placement_group_id is not None:
        output["placement_group_id"] = request.placement_group_id

    if request.min_size is not None:
        output["min_size"] = request.min_size

    if request.max_size is not None:
        output["max_size"] = request.max_size

    if request.autohealing is not None:
        output["autohealing"] = request.autohealing

    if request.tags is not None:
        output["tags"] = request.tags

    if request.kubelet_args is not None:
        output["kubelet_args"] = {
            key: value for key, value in request.kubelet_args.items()
        }

    if request.zone is not None:
        output["zone"] = request.zone or defaults.default_zone

    if request.root_volume_type is not None:
        output["root_volume_type"] = str(request.root_volume_type)

    if request.public_ip_disabled is not None:
        output["public_ip_disabled"] = request.public_ip_disabled

    if request.upgrade_policy is not None:
        output["upgrade_policy"] = marshal_CreateClusterRequestPoolConfigUpgradePolicy(
            request.upgrade_policy, defaults
        )

    if request.root_volume_size is not None:
        output["root_volume_size"] = request.root_volume_size

    return output


def marshal_CreateClusterRequest(
    request: CreateClusterRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "project_id", request.project_id, defaults.default_project_id
                ),
                OneOfPossibility(
                    "organization_id",
                    request.organization_id,
                    defaults.default_organization_id,
                ),
            ]
        ),
    )

    if request.type_ is not None:
        output["type"] = request.type_

    if request.description is not None:
        output["description"] = request.description

    if request.version is not None:
        output["version"] = request.version

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.cni is not None:
        output["cni"] = str(request.cni)

    if request.pools is not None:
        output["pools"] = [
            marshal_CreateClusterRequestPoolConfig(item, defaults)
            for item in request.pools
        ]

    if request.autoscaler_config is not None:
        output["autoscaler_config"] = marshal_CreateClusterRequestAutoscalerConfig(
            request.autoscaler_config, defaults
        )

    if request.auto_upgrade is not None:
        output["auto_upgrade"] = marshal_CreateClusterRequestAutoUpgrade(
            request.auto_upgrade, defaults
        )

    if request.feature_gates is not None:
        output["feature_gates"] = request.feature_gates

    if request.admission_plugins is not None:
        output["admission_plugins"] = request.admission_plugins

    if request.open_id_connect_config is not None:
        output["open_id_connect_config"] = (
            marshal_CreateClusterRequestOpenIDConnectConfig(
                request.open_id_connect_config, defaults
            )
        )

    if request.apiserver_cert_sans is not None:
        output["apiserver_cert_sans"] = request.apiserver_cert_sans

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    return output


def marshal_CreatePoolRequestUpgradePolicy(
    request: CreatePoolRequestUpgradePolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.max_unavailable is not None:
        output["max_unavailable"] = request.max_unavailable

    if request.max_surge is not None:
        output["max_surge"] = request.max_surge

    return output


def marshal_CreatePoolRequest(
    request: CreatePoolRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.node_type is not None:
        output["node_type"] = request.node_type

    if request.autoscaling is not None:
        output["autoscaling"] = request.autoscaling

    if request.size is not None:
        output["size"] = request.size

    if request.name is not None:
        output["name"] = request.name

    if request.placement_group_id is not None:
        output["placement_group_id"] = request.placement_group_id

    if request.min_size is not None:
        output["min_size"] = request.min_size

    if request.autohealing is not None:
        output["autohealing"] = request.autohealing

    if request.public_ip_disabled is not None:
        output["public_ip_disabled"] = request.public_ip_disabled

    if request.max_size is not None:
        output["max_size"] = request.max_size

    if request.container_runtime is not None:
        output["container_runtime"] = str(request.container_runtime)

    if request.tags is not None:
        output["tags"] = request.tags

    if request.kubelet_args is not None:
        output["kubelet_args"] = {
            key: value for key, value in request.kubelet_args.items()
        }

    if request.upgrade_policy is not None:
        output["upgrade_policy"] = marshal_CreatePoolRequestUpgradePolicy(
            request.upgrade_policy, defaults
        )

    if request.zone is not None:
        output["zone"] = request.zone or defaults.default_zone

    if request.root_volume_type is not None:
        output["root_volume_type"] = str(request.root_volume_type)

    if request.root_volume_size is not None:
        output["root_volume_size"] = request.root_volume_size

    return output


def marshal_SetClusterTypeRequest(
    request: SetClusterTypeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    return output


def marshal_UpdateClusterRequestAutoUpgrade(
    request: UpdateClusterRequestAutoUpgrade,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.enable is not None:
        output["enable"] = request.enable

    if request.maintenance_window is not None:
        output["maintenance_window"] = marshal_MaintenanceWindow(
            request.maintenance_window, defaults
        )

    return output


def marshal_UpdateClusterRequestAutoscalerConfig(
    request: UpdateClusterRequestAutoscalerConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.estimator is not None:
        output["estimator"] = str(request.estimator)

    if request.expander is not None:
        output["expander"] = str(request.expander)

    if request.scale_down_disabled is not None:
        output["scale_down_disabled"] = request.scale_down_disabled

    if request.scale_down_delay_after_add is not None:
        output["scale_down_delay_after_add"] = request.scale_down_delay_after_add

    if request.ignore_daemonsets_utilization is not None:
        output["ignore_daemonsets_utilization"] = request.ignore_daemonsets_utilization

    if request.balance_similar_node_groups is not None:
        output["balance_similar_node_groups"] = request.balance_similar_node_groups

    if request.expendable_pods_priority_cutoff is not None:
        output["expendable_pods_priority_cutoff"] = (
            request.expendable_pods_priority_cutoff
        )

    if request.scale_down_unneeded_time is not None:
        output["scale_down_unneeded_time"] = request.scale_down_unneeded_time

    if request.scale_down_utilization_threshold is not None:
        output["scale_down_utilization_threshold"] = (
            request.scale_down_utilization_threshold
        )

    if request.max_graceful_termination_sec is not None:
        output["max_graceful_termination_sec"] = request.max_graceful_termination_sec

    return output


def marshal_UpdateClusterRequestOpenIDConnectConfig(
    request: UpdateClusterRequestOpenIDConnectConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.issuer_url is not None:
        output["issuer_url"] = request.issuer_url

    if request.client_id is not None:
        output["client_id"] = request.client_id

    if request.username_claim is not None:
        output["username_claim"] = request.username_claim

    if request.username_prefix is not None:
        output["username_prefix"] = request.username_prefix

    if request.groups_claim is not None:
        output["groups_claim"] = request.groups_claim

    if request.groups_prefix is not None:
        output["groups_prefix"] = request.groups_prefix

    if request.required_claim is not None:
        output["required_claim"] = request.required_claim

    return output


def marshal_UpdateClusterRequest(
    request: UpdateClusterRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.tags is not None:
        output["tags"] = request.tags

    if request.autoscaler_config is not None:
        output["autoscaler_config"] = marshal_UpdateClusterRequestAutoscalerConfig(
            request.autoscaler_config, defaults
        )

    if request.auto_upgrade is not None:
        output["auto_upgrade"] = marshal_UpdateClusterRequestAutoUpgrade(
            request.auto_upgrade, defaults
        )

    if request.feature_gates is not None:
        output["feature_gates"] = request.feature_gates

    if request.admission_plugins is not None:
        output["admission_plugins"] = request.admission_plugins

    if request.open_id_connect_config is not None:
        output["open_id_connect_config"] = (
            marshal_UpdateClusterRequestOpenIDConnectConfig(
                request.open_id_connect_config, defaults
            )
        )

    if request.apiserver_cert_sans is not None:
        output["apiserver_cert_sans"] = request.apiserver_cert_sans

    return output


def marshal_UpdatePoolRequestUpgradePolicy(
    request: UpdatePoolRequestUpgradePolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.max_unavailable is not None:
        output["max_unavailable"] = request.max_unavailable

    if request.max_surge is not None:
        output["max_surge"] = request.max_surge

    return output


def marshal_UpdatePoolRequest(
    request: UpdatePoolRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.autoscaling is not None:
        output["autoscaling"] = request.autoscaling

    if request.size is not None:
        output["size"] = request.size

    if request.min_size is not None:
        output["min_size"] = request.min_size

    if request.max_size is not None:
        output["max_size"] = request.max_size

    if request.autohealing is not None:
        output["autohealing"] = request.autohealing

    if request.tags is not None:
        output["tags"] = request.tags

    if request.kubelet_args is not None:
        output["kubelet_args"] = request.kubelet_args

    if request.upgrade_policy is not None:
        output["upgrade_policy"] = marshal_UpdatePoolRequestUpgradePolicy(
            request.upgrade_policy, defaults
        )

    return output


def marshal_UpgradeClusterRequest(
    request: UpgradeClusterRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.version is not None:
        output["version"] = request.version

    if request.upgrade_pools is not None:
        output["upgrade_pools"] = request.upgrade_pools

    return output


def marshal_UpgradePoolRequest(
    request: UpgradePoolRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.version is not None:
        output["version"] = request.version

    return output
