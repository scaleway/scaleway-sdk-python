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
    AutoscalerEstimator,
    AutoscalerExpander,
    CNI,
    ClusterStatus,
    ClusterTypeAvailability,
    ClusterTypeResiliency,
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

    args: dict[str, Any] = {}

    field = data.get("max_unavailable", None)
    if field is not None:
        args["max_unavailable"] = field
    else:
        args["max_unavailable"] = None

    field = data.get("max_surge", None)
    if field is not None:
        args["max_surge"] = field
    else:
        args["max_surge"] = None

    return PoolUpgradePolicy(**args)


def unmarshal_Pool(data: Any) -> Pool:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Pool' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("cluster_id", None)
    if field is not None:
        args["cluster_id"] = field
    else:
        args["cluster_id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = PoolStatus.UNKNOWN

    field = data.get("version", None)
    if field is not None:
        args["version"] = field
    else:
        args["version"] = None

    field = data.get("node_type", None)
    if field is not None:
        args["node_type"] = field
    else:
        args["node_type"] = None

    field = data.get("autoscaling", None)
    if field is not None:
        args["autoscaling"] = field
    else:
        args["autoscaling"] = False

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = None

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

    field = data.get("container_runtime", None)
    if field is not None:
        args["container_runtime"] = field
    else:
        args["container_runtime"] = Runtime.UNKNOWN_RUNTIME

    field = data.get("autohealing", None)
    if field is not None:
        args["autohealing"] = field
    else:
        args["autohealing"] = False

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("kubelet_args", None)
    if field is not None:
        args["kubelet_args"] = field
    else:
        args["kubelet_args"] = {}

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("root_volume_type", None)
    if field is not None:
        args["root_volume_type"] = field
    else:
        args["root_volume_type"] = PoolVolumeType.DEFAULT_VOLUME_TYPE

    field = data.get("public_ip_disabled", None)
    if field is not None:
        args["public_ip_disabled"] = field
    else:
        args["public_ip_disabled"] = False

    field = data.get("security_group_id", None)
    if field is not None:
        args["security_group_id"] = field
    else:
        args["security_group_id"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

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
        args["root_volume_size"] = 0

    field = data.get("new_images_enabled", None)
    if field is not None:
        args["new_images_enabled"] = field
    else:
        args["new_images_enabled"] = False

    return Pool(**args)


def unmarshal_Version(data: Any) -> Version:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Version' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("label", None)
    if field is not None:
        args["label"] = field
    else:
        args["label"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("available_cnis", None)
    if field is not None:
        args["available_cnis"] = [CNI(v) for v in field] if field is not None else None
    else:
        args["available_cnis"] = []

    field = data.get("available_container_runtimes", None)
    if field is not None:
        args["available_container_runtimes"] = (
            [Runtime(v) for v in field] if field is not None else None
        )
    else:
        args["available_container_runtimes"] = []

    field = data.get("available_feature_gates", None)
    if field is not None:
        args["available_feature_gates"] = field
    else:
        args["available_feature_gates"] = []

    field = data.get("available_admission_plugins", None)
    if field is not None:
        args["available_admission_plugins"] = field
    else:
        args["available_admission_plugins"] = []

    field = data.get("available_kubelet_args", None)
    if field is not None:
        args["available_kubelet_args"] = field
    else:
        args["available_kubelet_args"] = {}

    field = data.get("deprecated_at", None)
    if field is not None:
        args["deprecated_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["deprecated_at"] = None

    field = data.get("end_of_life_at", None)
    if field is not None:
        args["end_of_life_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["end_of_life_at"] = None

    return Version(**args)


def unmarshal_MaintenanceWindow(data: Any) -> MaintenanceWindow:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'MaintenanceWindow' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("start_hour", None)
    if field is not None:
        args["start_hour"] = field
    else:
        args["start_hour"] = 0

    field = data.get("day", None)
    if field is not None:
        args["day"] = field
    else:
        args["day"] = MaintenanceWindowDayOfTheWeek.ANY

    return MaintenanceWindow(**args)


def unmarshal_ClusterAutoUpgrade(data: Any) -> ClusterAutoUpgrade:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterAutoUpgrade' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("enabled", None)
    if field is not None:
        args["enabled"] = field
    else:
        args["enabled"] = False

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

    args: dict[str, Any] = {}

    field = data.get("scale_down_disabled", None)
    if field is not None:
        args["scale_down_disabled"] = field
    else:
        args["scale_down_disabled"] = False

    field = data.get("scale_down_delay_after_add", None)
    if field is not None:
        args["scale_down_delay_after_add"] = field
    else:
        args["scale_down_delay_after_add"] = None

    field = data.get("estimator", None)
    if field is not None:
        args["estimator"] = field
    else:
        args["estimator"] = AutoscalerEstimator.UNKNOWN_ESTIMATOR

    field = data.get("expander", None)
    if field is not None:
        args["expander"] = field
    else:
        args["expander"] = AutoscalerExpander.UNKNOWN_EXPANDER

    field = data.get("ignore_daemonsets_utilization", None)
    if field is not None:
        args["ignore_daemonsets_utilization"] = field
    else:
        args["ignore_daemonsets_utilization"] = False

    field = data.get("balance_similar_node_groups", None)
    if field is not None:
        args["balance_similar_node_groups"] = field
    else:
        args["balance_similar_node_groups"] = False

    field = data.get("expendable_pods_priority_cutoff", None)
    if field is not None:
        args["expendable_pods_priority_cutoff"] = field
    else:
        args["expendable_pods_priority_cutoff"] = 0

    field = data.get("scale_down_unneeded_time", None)
    if field is not None:
        args["scale_down_unneeded_time"] = field
    else:
        args["scale_down_unneeded_time"] = None

    field = data.get("scale_down_utilization_threshold", None)
    if field is not None:
        args["scale_down_utilization_threshold"] = field
    else:
        args["scale_down_utilization_threshold"] = 0.0

    field = data.get("max_graceful_termination_sec", None)
    if field is not None:
        args["max_graceful_termination_sec"] = field
    else:
        args["max_graceful_termination_sec"] = 0

    return ClusterAutoscalerConfig(**args)


def unmarshal_ClusterOpenIDConnectConfig(data: Any) -> ClusterOpenIDConnectConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterOpenIDConnectConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("issuer_url", None)
    if field is not None:
        args["issuer_url"] = field
    else:
        args["issuer_url"] = None

    field = data.get("client_id", None)
    if field is not None:
        args["client_id"] = field
    else:
        args["client_id"] = None

    field = data.get("username_claim", None)
    if field is not None:
        args["username_claim"] = field
    else:
        args["username_claim"] = None

    field = data.get("username_prefix", None)
    if field is not None:
        args["username_prefix"] = field
    else:
        args["username_prefix"] = None

    field = data.get("groups_claim", None)
    if field is not None:
        args["groups_claim"] = field
    else:
        args["groups_claim"] = []

    field = data.get("groups_prefix", None)
    if field is not None:
        args["groups_prefix"] = field
    else:
        args["groups_prefix"] = None

    field = data.get("required_claim", None)
    if field is not None:
        args["required_claim"] = field
    else:
        args["required_claim"] = []

    return ClusterOpenIDConnectConfig(**args)


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

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

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

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("cni", None)
    if field is not None:
        args["cni"] = field
    else:
        args["cni"] = CNI.UNKNOWN_CNI

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("cluster_url", None)
    if field is not None:
        args["cluster_url"] = field
    else:
        args["cluster_url"] = None

    field = data.get("dns_wildcard", None)
    if field is not None:
        args["dns_wildcard"] = field
    else:
        args["dns_wildcard"] = None

    field = data.get("upgrade_available", None)
    if field is not None:
        args["upgrade_available"] = field
    else:
        args["upgrade_available"] = False

    field = data.get("feature_gates", None)
    if field is not None:
        args["feature_gates"] = field
    else:
        args["feature_gates"] = []

    field = data.get("admission_plugins", None)
    if field is not None:
        args["admission_plugins"] = field
    else:
        args["admission_plugins"] = []

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

    field = data.get("open_id_connect_config", None)
    if field is not None:
        args["open_id_connect_config"] = unmarshal_ClusterOpenIDConnectConfig(field)
    else:
        args["open_id_connect_config"] = None

    field = data.get("apiserver_cert_sans", None)
    if field is not None:
        args["apiserver_cert_sans"] = field
    else:
        args["apiserver_cert_sans"] = []

    field = data.get("iam_nodes_group_id", None)
    if field is not None:
        args["iam_nodes_group_id"] = field
    else:
        args["iam_nodes_group_id"] = None

    field = data.get("pod_cidr", None)
    if field is not None:
        args["pod_cidr"] = field
    else:
        args["pod_cidr"] = None

    field = data.get("service_cidr", None)
    if field is not None:
        args["service_cidr"] = field
    else:
        args["service_cidr"] = None

    field = data.get("service_dns_ip", None)
    if field is not None:
        args["service_dns_ip"] = field
    else:
        args["service_dns_ip"] = None

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

    field = data.get("acl_available", None)
    if field is not None:
        args["acl_available"] = field
    else:
        args["acl_available"] = False

    field = data.get("new_images_enabled", None)
    if field is not None:
        args["new_images_enabled"] = field
    else:
        args["new_images_enabled"] = False

    return Cluster(**args)


def unmarshal_Node(data: Any) -> Node:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Node' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("pool_id", None)
    if field is not None:
        args["pool_id"] = field
    else:
        args["pool_id"] = None

    field = data.get("cluster_id", None)
    if field is not None:
        args["cluster_id"] = field
    else:
        args["cluster_id"] = None

    field = data.get("provider_id", None)
    if field is not None:
        args["provider_id"] = field
    else:
        args["provider_id"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

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
        args["conditions"] = {}

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = NodeStatus.UNKNOWN

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

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("ip", None)
    if field is not None:
        args["ip"] = field
    else:
        args["ip"] = None

    field = data.get("scaleway_ranges", None)
    if field is not None:
        args["scaleway_ranges"] = field
    else:
        args["scaleway_ranges"] = False

    return ACLRule(**args)


def unmarshal_AddClusterACLRulesResponse(data: Any) -> AddClusterACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddClusterACLRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("rules", None)
    if field is not None:
        args["rules"] = (
            [unmarshal_ACLRule(v) for v in field] if field is not None else None
        )
    else:
        args["rules"] = []

    return AddClusterACLRulesResponse(**args)


def unmarshal_ExternalNodeCoreV1Taint(data: Any) -> ExternalNodeCoreV1Taint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ExternalNodeCoreV1Taint' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("key", None)
    if field is not None:
        args["key"] = field
    else:
        args["key"] = None

    field = data.get("value", None)
    if field is not None:
        args["value"] = field
    else:
        args["value"] = None

    field = data.get("effect", None)
    if field is not None:
        args["effect"] = field
    else:
        args["effect"] = None

    return ExternalNodeCoreV1Taint(**args)


def unmarshal_ExternalNode(data: Any) -> ExternalNode:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ExternalNode' failed as data isn't a dictionary."
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

    field = data.get("cluster_url", None)
    if field is not None:
        args["cluster_url"] = field
    else:
        args["cluster_url"] = None

    field = data.get("pool_version", None)
    if field is not None:
        args["pool_version"] = field
    else:
        args["pool_version"] = None

    field = data.get("cluster_ca", None)
    if field is not None:
        args["cluster_ca"] = field
    else:
        args["cluster_ca"] = None

    field = data.get("kube_token", None)
    if field is not None:
        args["kube_token"] = field
    else:
        args["kube_token"] = None

    field = data.get("kubelet_config", None)
    if field is not None:
        args["kubelet_config"] = field
    else:
        args["kubelet_config"] = None

    field = data.get("external_ip", None)
    if field is not None:
        args["external_ip"] = field
    else:
        args["external_ip"] = None

    field = data.get("containerd_version", None)
    if field is not None:
        args["containerd_version"] = field
    else:
        args["containerd_version"] = None

    field = data.get("runc_version", None)
    if field is not None:
        args["runc_version"] = field
    else:
        args["runc_version"] = None

    field = data.get("cni_plugins_version", None)
    if field is not None:
        args["cni_plugins_version"] = field
    else:
        args["cni_plugins_version"] = None

    field = data.get("node_labels", None)
    if field is not None:
        args["node_labels"] = field
    else:
        args["node_labels"] = None

    field = data.get("node_taints", None)
    if field is not None:
        args["node_taints"] = (
            [unmarshal_ExternalNodeCoreV1Taint(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["node_taints"] = None

    field = data.get("iam_token", None)
    if field is not None:
        args["iam_token"] = field
    else:
        args["iam_token"] = None

    return ExternalNode(**args)


def unmarshal_ExternalNodeAuth(data: Any) -> ExternalNodeAuth:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ExternalNodeAuth' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("node_secret_key", None)
    if field is not None:
        args["node_secret_key"] = field
    else:
        args["node_secret_key"] = None

    field = data.get("metadata_url", None)
    if field is not None:
        args["metadata_url"] = field
    else:
        args["metadata_url"] = None

    return ExternalNodeAuth(**args)


def unmarshal_ListClusterACLRulesResponse(data: Any) -> ListClusterACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClusterACLRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("rules", None)
    if field is not None:
        args["rules"] = (
            [unmarshal_ACLRule(v) for v in field] if field is not None else None
        )
    else:
        args["rules"] = []

    return ListClusterACLRulesResponse(**args)


def unmarshal_ClusterType(data: Any) -> ClusterType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterType' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("availability", None)
    if field is not None:
        args["availability"] = field
    else:
        args["availability"] = ClusterTypeAvailability.AVAILABLE

    field = data.get("max_nodes", None)
    if field is not None:
        args["max_nodes"] = field
    else:
        args["max_nodes"] = 0

    field = data.get("sla", None)
    if field is not None:
        args["sla"] = field
    else:
        args["sla"] = 0.0

    field = data.get("resiliency", None)
    if field is not None:
        args["resiliency"] = field
    else:
        args["resiliency"] = ClusterTypeResiliency.UNKNOWN_RESILIENCY

    field = data.get("memory", None)
    if field is not None:
        args["memory"] = field
    else:
        args["memory"] = 0

    field = data.get("dedicated", None)
    if field is not None:
        args["dedicated"] = field
    else:
        args["dedicated"] = False

    field = data.get("audit_logs_supported", None)
    if field is not None:
        args["audit_logs_supported"] = field
    else:
        args["audit_logs_supported"] = False

    field = data.get("max_etcd_size", None)
    if field is not None:
        args["max_etcd_size"] = field
    else:
        args["max_etcd_size"] = 0

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

    args: dict[str, Any] = {}

    field = data.get("cluster_types", None)
    if field is not None:
        args["cluster_types"] = (
            [unmarshal_ClusterType(v) for v in field] if field is not None else None
        )
    else:
        args["cluster_types"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListClusterAvailableTypesResponse(**args)


def unmarshal_ListClusterAvailableVersionsResponse(
    data: Any,
) -> ListClusterAvailableVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClusterAvailableVersionsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("versions", None)
    if field is not None:
        args["versions"] = (
            [unmarshal_Version(v) for v in field] if field is not None else None
        )
    else:
        args["versions"] = []

    return ListClusterAvailableVersionsResponse(**args)


def unmarshal_ListClusterTypesResponse(data: Any) -> ListClusterTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClusterTypesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("cluster_types", None)
    if field is not None:
        args["cluster_types"] = (
            [unmarshal_ClusterType(v) for v in field] if field is not None else None
        )
    else:
        args["cluster_types"] = []

    return ListClusterTypesResponse(**args)


def unmarshal_ListClustersResponse(data: Any) -> ListClustersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClustersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("clusters", None)
    if field is not None:
        args["clusters"] = (
            [unmarshal_Cluster(v) for v in field] if field is not None else None
        )
    else:
        args["clusters"] = []

    return ListClustersResponse(**args)


def unmarshal_ListNodesResponse(data: Any) -> ListNodesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNodesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("nodes", None)
    if field is not None:
        args["nodes"] = (
            [unmarshal_Node(v) for v in field] if field is not None else None
        )
    else:
        args["nodes"] = []

    return ListNodesResponse(**args)


def unmarshal_ListPoolsResponse(data: Any) -> ListPoolsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPoolsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("pools", None)
    if field is not None:
        args["pools"] = (
            [unmarshal_Pool(v) for v in field] if field is not None else None
        )
    else:
        args["pools"] = []

    return ListPoolsResponse(**args)


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

    return ListVersionsResponse(**args)


def unmarshal_NodeMetadataCoreV1Taint(data: Any) -> NodeMetadataCoreV1Taint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeMetadataCoreV1Taint' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("key", None)
    if field is not None:
        args["key"] = field
    else:
        args["key"] = None

    field = data.get("value", None)
    if field is not None:
        args["value"] = field
    else:
        args["value"] = None

    field = data.get("effect", None)
    if field is not None:
        args["effect"] = field
    else:
        args["effect"] = None

    return NodeMetadataCoreV1Taint(**args)


def unmarshal_NodeMetadata(data: Any) -> NodeMetadata:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeMetadata' failed as data isn't a dictionary."
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

    field = data.get("cluster_url", None)
    if field is not None:
        args["cluster_url"] = field
    else:
        args["cluster_url"] = None

    field = data.get("cluster_ca", None)
    if field is not None:
        args["cluster_ca"] = field
    else:
        args["cluster_ca"] = None

    field = data.get("credential_provider_config", None)
    if field is not None:
        args["credential_provider_config"] = field
    else:
        args["credential_provider_config"] = None

    field = data.get("pool_version", None)
    if field is not None:
        args["pool_version"] = field
    else:
        args["pool_version"] = None

    field = data.get("kubelet_config", None)
    if field is not None:
        args["kubelet_config"] = field
    else:
        args["kubelet_config"] = None

    field = data.get("node_labels", None)
    if field is not None:
        args["node_labels"] = field
    else:
        args["node_labels"] = None

    field = data.get("node_taints", None)
    if field is not None:
        args["node_taints"] = (
            [unmarshal_NodeMetadataCoreV1Taint(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["node_taints"] = None

    field = data.get("provider_id", None)
    if field is not None:
        args["provider_id"] = field
    else:
        args["provider_id"] = None

    field = data.get("resolvconf_path", None)
    if field is not None:
        args["resolvconf_path"] = field
    else:
        args["resolvconf_path"] = None

    field = data.get("template_args", None)
    if field is not None:
        args["template_args"] = field
    else:
        args["template_args"] = None

    field = data.get("has_gpu", None)
    if field is not None:
        args["has_gpu"] = field
    else:
        args["has_gpu"] = None

    field = data.get("external_ip", None)
    if field is not None:
        args["external_ip"] = field
    else:
        args["external_ip"] = None

    field = data.get("repo_uri", None)
    if field is not None:
        args["repo_uri"] = field
    else:
        args["repo_uri"] = None

    field = data.get("installer_tags", None)
    if field is not None:
        args["installer_tags"] = field
    else:
        args["installer_tags"] = None

    field = data.get("updater_bin_url", None)
    if field is not None:
        args["updater_bin_url"] = field
    else:
        args["updater_bin_url"] = None

    field = data.get("updater_bin_version", None)
    if field is not None:
        args["updater_bin_version"] = field
    else:
        args["updater_bin_version"] = None

    field = data.get("updater_bin_path", None)
    if field is not None:
        args["updater_bin_path"] = field
    else:
        args["updater_bin_path"] = None

    return NodeMetadata(**args)


def unmarshal_SetClusterACLRulesResponse(data: Any) -> SetClusterACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetClusterACLRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("rules", None)
    if field is not None:
        args["rules"] = (
            [unmarshal_ACLRule(v) for v in field] if field is not None else None
        )
    else:
        args["rules"] = []

    return SetClusterACLRulesResponse(**args)


def marshal_ACLRuleRequest(
    request: ACLRuleRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(param="ip", value=request.ip, marshal_func=None),
                OneOfPossibility(
                    param="scaleway_ranges",
                    value=request.scaleway_ranges,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.description is not None:
        output["description"] = request.description

    return output


def marshal_AddClusterACLRulesRequest(
    request: AddClusterACLRulesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.acls is not None:
        output["acls"] = [
            marshal_ACLRuleRequest(item, defaults) for item in request.acls
        ]

    return output


def marshal_MaintenanceWindow(
    request: MaintenanceWindow,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.start_hour is not None:
        output["start_hour"] = request.start_hour

    if request.day is not None:
        output["day"] = request.day

    return output


def marshal_CreateClusterRequestPoolConfigUpgradePolicy(
    request: CreateClusterRequestPoolConfigUpgradePolicy,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.max_unavailable is not None:
        output["max_unavailable"] = request.max_unavailable

    if request.max_surge is not None:
        output["max_surge"] = request.max_surge

    return output


def marshal_CreateClusterRequestAutoUpgrade(
    request: CreateClusterRequestAutoUpgrade,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

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
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.estimator is not None:
        output["estimator"] = request.estimator

    if request.expander is not None:
        output["expander"] = request.expander

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
) -> dict[str, Any]:
    output: dict[str, Any] = {}

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
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.node_type is not None:
        output["node_type"] = request.node_type

    if request.autoscaling is not None:
        output["autoscaling"] = request.autoscaling

    if request.size is not None:
        output["size"] = request.size

    if request.container_runtime is not None:
        output["container_runtime"] = request.container_runtime

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
        output["zone"] = request.zone
    else:
        output["zone"] = defaults.default_zone

    if request.root_volume_type is not None:
        output["root_volume_type"] = request.root_volume_type

    if request.public_ip_disabled is not None:
        output["public_ip_disabled"] = request.public_ip_disabled

    if request.upgrade_policy is not None:
        output["upgrade_policy"] = marshal_CreateClusterRequestPoolConfigUpgradePolicy(
            request.upgrade_policy, defaults
        )

    if request.root_volume_size is not None:
        output["root_volume_size"] = request.root_volume_size

    if request.security_group_id is not None:
        output["security_group_id"] = request.security_group_id

    return output


def marshal_CreateClusterRequest(
    request: CreateClusterRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="project_id",
                    value=request.project_id,
                    default=defaults.default_project_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="organization_id",
                    value=request.organization_id,
                    default=defaults.default_organization_id,
                    marshal_func=None,
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

    if request.cni is not None:
        output["cni"] = request.cni

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

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

    if request.pod_cidr is not None:
        output["pod_cidr"] = request.pod_cidr

    if request.service_cidr is not None:
        output["service_cidr"] = request.service_cidr

    if request.service_dns_ip is not None:
        output["service_dns_ip"] = request.service_dns_ip

    return output


def marshal_CreatePoolRequestUpgradePolicy(
    request: CreatePoolRequestUpgradePolicy,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.max_unavailable is not None:
        output["max_unavailable"] = request.max_unavailable

    if request.max_surge is not None:
        output["max_surge"] = request.max_surge

    return output


def marshal_CreatePoolRequest(
    request: CreatePoolRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

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
        output["container_runtime"] = request.container_runtime

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
        output["zone"] = request.zone
    else:
        output["zone"] = defaults.default_zone

    if request.root_volume_type is not None:
        output["root_volume_type"] = request.root_volume_type

    if request.root_volume_size is not None:
        output["root_volume_size"] = request.root_volume_size

    if request.security_group_id is not None:
        output["security_group_id"] = request.security_group_id

    return output


def marshal_MigratePoolsToNewImagesRequest(
    request: MigratePoolsToNewImagesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.pool_ids is not None:
        output["pool_ids"] = request.pool_ids

    return output


def marshal_SetClusterACLRulesRequest(
    request: SetClusterACLRulesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.acls is not None:
        output["acls"] = [
            marshal_ACLRuleRequest(item, defaults) for item in request.acls
        ]

    return output


def marshal_SetClusterTypeRequest(
    request: SetClusterTypeRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    return output


def marshal_UpdateClusterRequestAutoUpgrade(
    request: UpdateClusterRequestAutoUpgrade,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

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
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.estimator is not None:
        output["estimator"] = request.estimator

    if request.expander is not None:
        output["expander"] = request.expander

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
) -> dict[str, Any]:
    output: dict[str, Any] = {}

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
) -> dict[str, Any]:
    output: dict[str, Any] = {}

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
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.max_unavailable is not None:
        output["max_unavailable"] = request.max_unavailable

    if request.max_surge is not None:
        output["max_surge"] = request.max_surge

    return output


def marshal_UpdatePoolRequest(
    request: UpdatePoolRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

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
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.version is not None:
        output["version"] = request.version

    if request.upgrade_pools is not None:
        output["upgrade_pools"] = request.upgrade_pools

    return output


def marshal_UpgradePoolRequest(
    request: UpgradePoolRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.version is not None:
        output["version"] = request.version

    return output
