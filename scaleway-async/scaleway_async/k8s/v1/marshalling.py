# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from dateutil import parser
from .types import (
    AutoscalerEstimator,
    AutoscalerExpander,
    CNI,
    Ingress,
    MaintenanceWindowDayOfTheWeek,
    PoolVolumeType,
    Runtime,
    Cluster,
    ClusterAutoUpgrade,
    ClusterAutoscalerConfig,
    ClusterOpenIDConnectConfig,
    ClusterType,
    CreateClusterRequestAutoUpgrade,
    CreateClusterRequestAutoscalerConfig,
    CreateClusterRequestOpenIDConnectConfig,
    CreateClusterRequestPoolConfig,
    CreateClusterRequestPoolConfigUpgradePolicy,
    CreatePoolRequestUpgradePolicy,
    ExternalNode,
    ListClusterAvailableTypesResponse,
    ListClusterAvailableVersionsResponse,
    ListClusterTypesResponse,
    ListClustersResponse,
    ListNodesResponse,
    ListPoolsResponse,
    ListVersionsResponse,
    MaintenanceWindow,
    Node,
    Pool,
    PoolUpgradePolicy,
    UpdateClusterRequestAutoUpgrade,
    UpdateClusterRequestAutoscalerConfig,
    UpdateClusterRequestOpenIDConnectConfig,
    UpdatePoolRequestUpgradePolicy,
    Version,
    CreateClusterRequest,
    UpdateClusterRequest,
    UpgradeClusterRequest,
    SetClusterTypeRequest,
    MigrateToPrivateNetworkClusterRequest,
    CreatePoolRequest,
    UpgradePoolRequest,
    UpdatePoolRequest,
)


def unmarshal_MaintenanceWindow(data: Any) -> MaintenanceWindow:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'MaintenanceWindow' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("day", None)
    args["day"] = field

    field = data.get("start_hour", None)
    args["start_hour"] = field

    return MaintenanceWindow(**args)


def unmarshal_ClusterAutoUpgrade(data: Any) -> ClusterAutoUpgrade:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterAutoUpgrade' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("enabled", None)
    args["enabled"] = field

    field = data.get("maintenance_window", None)
    args["maintenance_window"] = (
        unmarshal_MaintenanceWindow(field) if field is not None else None
    )

    return ClusterAutoUpgrade(**args)


def unmarshal_ClusterAutoscalerConfig(data: Any) -> ClusterAutoscalerConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterAutoscalerConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("balance_similar_node_groups", None)
    args["balance_similar_node_groups"] = field

    field = data.get("estimator", None)
    args["estimator"] = field

    field = data.get("expander", None)
    args["expander"] = field

    field = data.get("expendable_pods_priority_cutoff", None)
    args["expendable_pods_priority_cutoff"] = field

    field = data.get("ignore_daemonsets_utilization", None)
    args["ignore_daemonsets_utilization"] = field

    field = data.get("max_graceful_termination_sec", None)
    args["max_graceful_termination_sec"] = field

    field = data.get("scale_down_delay_after_add", None)
    args["scale_down_delay_after_add"] = field

    field = data.get("scale_down_disabled", None)
    args["scale_down_disabled"] = field

    field = data.get("scale_down_unneeded_time", None)
    args["scale_down_unneeded_time"] = field

    field = data.get("scale_down_utilization_threshold", None)
    args["scale_down_utilization_threshold"] = field

    return ClusterAutoscalerConfig(**args)


def unmarshal_ClusterOpenIDConnectConfig(data: Any) -> ClusterOpenIDConnectConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterOpenIDConnectConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("client_id", None)
    args["client_id"] = field

    field = data.get("groups_claim", None)
    args["groups_claim"] = field

    field = data.get("groups_prefix", None)
    args["groups_prefix"] = field

    field = data.get("issuer_url", None)
    args["issuer_url"] = field

    field = data.get("required_claim", None)
    args["required_claim"] = field

    field = data.get("username_claim", None)
    args["username_claim"] = field

    field = data.get("username_prefix", None)
    args["username_prefix"] = field

    return ClusterOpenIDConnectConfig(**args)


def unmarshal_PoolUpgradePolicy(data: Any) -> PoolUpgradePolicy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PoolUpgradePolicy' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("max_surge", None)
    args["max_surge"] = field

    field = data.get("max_unavailable", None)
    args["max_unavailable"] = field

    return PoolUpgradePolicy(**args)


def unmarshal_Cluster(data: Any) -> Cluster:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Cluster' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("admission_plugins", None)
    args["admission_plugins"] = field

    field = data.get("apiserver_cert_sans", None)
    args["apiserver_cert_sans"] = field

    field = data.get("auto_upgrade", None)
    args["auto_upgrade"] = (
        unmarshal_ClusterAutoUpgrade(field) if field is not None else None
    )

    field = data.get("autoscaler_config", None)
    args["autoscaler_config"] = (
        unmarshal_ClusterAutoscalerConfig(field) if field is not None else None
    )

    field = data.get("cluster_url", None)
    args["cluster_url"] = field

    field = data.get("cni", None)
    args["cni"] = field

    field = data.get("commitment_ends_at", None)
    args["commitment_ends_at"] = (
        parser.isoparse(field) if isinstance(field, str) else field
    )

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("dashboard_enabled", None)
    args["dashboard_enabled"] = field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("dns_wildcard", None)
    args["dns_wildcard"] = field

    field = data.get("feature_gates", None)
    args["feature_gates"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("ingress", None)
    args["ingress"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("open_id_connect_config", None)
    args["open_id_connect_config"] = (
        unmarshal_ClusterOpenIDConnectConfig(field) if field is not None else None
    )

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("private_network_id", None)
    args["private_network_id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("type", None)
    args["type_"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("upgrade_available", None)
    args["upgrade_available"] = field

    field = data.get("version", None)
    args["version"] = field

    return Cluster(**args)


def unmarshal_ClusterType(data: Any) -> ClusterType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("availability", None)
    args["availability"] = field

    field = data.get("commitment_delay", None)
    args["commitment_delay"] = field

    field = data.get("dedicated", None)
    args["dedicated"] = field

    field = data.get("max_nodes", None)
    args["max_nodes"] = field

    field = data.get("memory", None)
    args["memory"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("resiliency", None)
    args["resiliency"] = field

    field = data.get("sla", None)
    args["sla"] = field

    return ClusterType(**args)


def unmarshal_Node(data: Any) -> Node:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Node' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("cluster_id", None)
    args["cluster_id"] = field

    field = data.get("conditions", None)
    args["conditions"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("error_message", None)
    args["error_message"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("pool_id", None)
    args["pool_id"] = field

    field = data.get("provider_id", None)
    args["provider_id"] = field

    field = data.get("public_ip_v4", None)
    args["public_ip_v4"] = field

    field = data.get("public_ip_v6", None)
    args["public_ip_v6"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Node(**args)


def unmarshal_Pool(data: Any) -> Pool:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Pool' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("autohealing", None)
    args["autohealing"] = field

    field = data.get("autoscaling", None)
    args["autoscaling"] = field

    field = data.get("cluster_id", None)
    args["cluster_id"] = field

    field = data.get("container_runtime", None)
    args["container_runtime"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("kubelet_args", None)
    args["kubelet_args"] = field

    field = data.get("max_size", None)
    args["max_size"] = field

    field = data.get("min_size", None)
    args["min_size"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("node_type", None)
    args["node_type"] = field

    field = data.get("placement_group_id", None)
    args["placement_group_id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("root_volume_size", None)
    args["root_volume_size"] = field

    field = data.get("root_volume_type", None)
    args["root_volume_type"] = field

    field = data.get("size", None)
    args["size"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("upgrade_policy", None)
    args["upgrade_policy"] = (
        unmarshal_PoolUpgradePolicy(field) if field is not None else None
    )

    field = data.get("version", None)
    args["version"] = field

    field = data.get("zone", None)
    args["zone"] = field

    return Pool(**args)


def unmarshal_Version(data: Any) -> Version:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Version' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("available_admission_plugins", None)
    args["available_admission_plugins"] = field

    field = data.get("available_cnis", None)
    args["available_cnis"] = field

    field = data.get("available_container_runtimes", None)
    args["available_container_runtimes"] = field

    field = data.get("available_feature_gates", None)
    args["available_feature_gates"] = field

    field = data.get("available_ingresses", None)
    args["available_ingresses"] = field

    field = data.get("available_kubelet_args", None)
    args["available_kubelet_args"] = field

    field = data.get("label", None)
    args["label"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("region", None)
    args["region"] = field

    return Version(**args)


def unmarshal_ExternalNode(data: Any) -> ExternalNode:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ExternalNode' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("cluster_ca", None)
    args["cluster_ca"] = field

    field = data.get("cluster_url", None)
    args["cluster_url"] = field

    field = data.get("external_ip", None)
    args["external_ip"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("kube_token", None)
    args["kube_token"] = field

    field = data.get("kubelet_config", None)
    args["kubelet_config"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("pool_version", None)
    args["pool_version"] = field

    return ExternalNode(**args)


def unmarshal_ListClusterAvailableTypesResponse(
    data: Any,
) -> ListClusterAvailableTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClusterAvailableTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("cluster_types", None)
    args["cluster_types"] = (
        [unmarshal_ClusterType(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
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

    field = data.get("cluster_types", None)
    args["cluster_types"] = (
        [unmarshal_ClusterType(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListClusterTypesResponse(**args)


def unmarshal_ListClustersResponse(data: Any) -> ListClustersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClustersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("clusters", None)
    args["clusters"] = (
        [unmarshal_Cluster(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListClustersResponse(**args)


def unmarshal_ListNodesResponse(data: Any) -> ListNodesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNodesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("nodes", None)
    args["nodes"] = [unmarshal_Node(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListNodesResponse(**args)


def unmarshal_ListPoolsResponse(data: Any) -> ListPoolsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPoolsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pools", None)
    args["pools"] = [unmarshal_Pool(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListPoolsResponse(**args)


def unmarshal_ListVersionsResponse(data: Any) -> ListVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("versions", None)
    args["versions"] = (
        [unmarshal_Version(v) for v in field] if field is not None else None
    )

    return ListVersionsResponse(**args)


def marshal_CreateClusterRequestPoolConfigUpgradePolicy(
    request: CreateClusterRequestPoolConfigUpgradePolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.max_surge is not None:
        output["max_surge"] = request.max_surge

    if request.max_unavailable is not None:
        output["max_unavailable"] = request.max_unavailable

    return output


def marshal_MaintenanceWindow(
    request: MaintenanceWindow,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.day is not None:
        output["day"] = MaintenanceWindowDayOfTheWeek(request.day)

    if request.start_hour is not None:
        output["start_hour"] = request.start_hour

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

    if request.balance_similar_node_groups is not None:
        output["balance_similar_node_groups"] = request.balance_similar_node_groups

    if request.estimator is not None:
        output["estimator"] = AutoscalerEstimator(request.estimator)

    if request.expander is not None:
        output["expander"] = AutoscalerExpander(request.expander)

    if request.expendable_pods_priority_cutoff is not None:
        output[
            "expendable_pods_priority_cutoff"
        ] = request.expendable_pods_priority_cutoff

    if request.ignore_daemonsets_utilization is not None:
        output["ignore_daemonsets_utilization"] = request.ignore_daemonsets_utilization

    if request.max_graceful_termination_sec is not None:
        output["max_graceful_termination_sec"] = request.max_graceful_termination_sec

    if request.scale_down_delay_after_add is not None:
        output["scale_down_delay_after_add"] = request.scale_down_delay_after_add

    if request.scale_down_disabled is not None:
        output["scale_down_disabled"] = request.scale_down_disabled

    if request.scale_down_unneeded_time is not None:
        output["scale_down_unneeded_time"] = request.scale_down_unneeded_time

    if request.scale_down_utilization_threshold is not None:
        output[
            "scale_down_utilization_threshold"
        ] = request.scale_down_utilization_threshold

    return output


def marshal_CreateClusterRequestOpenIDConnectConfig(
    request: CreateClusterRequestOpenIDConnectConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.client_id is not None:
        output["client_id"] = request.client_id

    if request.groups_claim is not None:
        output["groups_claim"] = request.groups_claim

    if request.groups_prefix is not None:
        output["groups_prefix"] = request.groups_prefix

    if request.issuer_url is not None:
        output["issuer_url"] = request.issuer_url

    if request.required_claim is not None:
        output["required_claim"] = request.required_claim

    if request.username_claim is not None:
        output["username_claim"] = request.username_claim

    if request.username_prefix is not None:
        output["username_prefix"] = request.username_prefix

    return output


def marshal_CreateClusterRequestPoolConfig(
    request: CreateClusterRequestPoolConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.autohealing is not None:
        output["autohealing"] = request.autohealing

    if request.autoscaling is not None:
        output["autoscaling"] = request.autoscaling

    if request.container_runtime is not None:
        output["container_runtime"] = Runtime(request.container_runtime)

    if request.kubelet_args is not None:
        output["kubelet_args"] = request.kubelet_args

    if request.max_size is not None:
        output["max_size"] = request.max_size

    if request.min_size is not None:
        output["min_size"] = request.min_size

    if request.name is not None:
        output["name"] = request.name

    if request.node_type is not None:
        output["node_type"] = request.node_type

    if request.placement_group_id is not None:
        output["placement_group_id"] = request.placement_group_id

    if request.root_volume_size is not None:
        output["root_volume_size"] = request.root_volume_size

    if request.root_volume_type is not None:
        output["root_volume_type"] = PoolVolumeType(request.root_volume_type)

    if request.size is not None:
        output["size"] = request.size

    if request.tags is not None:
        output["tags"] = request.tags

    if request.upgrade_policy is not None:
        output["upgrade_policy"] = marshal_CreateClusterRequestPoolConfigUpgradePolicy(
            request.upgrade_policy, defaults
        )

    if request.zone is not None:
        output["zone"] = request.zone

    return output


def marshal_CreatePoolRequestUpgradePolicy(
    request: CreatePoolRequestUpgradePolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.max_surge is not None:
        output["max_surge"] = request.max_surge

    if request.max_unavailable is not None:
        output["max_unavailable"] = request.max_unavailable

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

    if request.balance_similar_node_groups is not None:
        output["balance_similar_node_groups"] = request.balance_similar_node_groups

    if request.estimator is not None:
        output["estimator"] = AutoscalerEstimator(request.estimator)

    if request.expander is not None:
        output["expander"] = AutoscalerExpander(request.expander)

    if request.expendable_pods_priority_cutoff is not None:
        output[
            "expendable_pods_priority_cutoff"
        ] = request.expendable_pods_priority_cutoff

    if request.ignore_daemonsets_utilization is not None:
        output["ignore_daemonsets_utilization"] = request.ignore_daemonsets_utilization

    if request.max_graceful_termination_sec is not None:
        output["max_graceful_termination_sec"] = request.max_graceful_termination_sec

    if request.scale_down_delay_after_add is not None:
        output["scale_down_delay_after_add"] = request.scale_down_delay_after_add

    if request.scale_down_disabled is not None:
        output["scale_down_disabled"] = request.scale_down_disabled

    if request.scale_down_unneeded_time is not None:
        output["scale_down_unneeded_time"] = request.scale_down_unneeded_time

    if request.scale_down_utilization_threshold is not None:
        output[
            "scale_down_utilization_threshold"
        ] = request.scale_down_utilization_threshold

    return output


def marshal_UpdateClusterRequestOpenIDConnectConfig(
    request: UpdateClusterRequestOpenIDConnectConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.client_id is not None:
        output["client_id"] = request.client_id

    if request.groups_claim is not None:
        output["groups_claim"] = request.groups_claim

    if request.groups_prefix is not None:
        output["groups_prefix"] = request.groups_prefix

    if request.issuer_url is not None:
        output["issuer_url"] = request.issuer_url

    if request.required_claim is not None:
        output["required_claim"] = request.required_claim

    if request.username_claim is not None:
        output["username_claim"] = request.username_claim

    if request.username_prefix is not None:
        output["username_prefix"] = request.username_prefix

    return output


def marshal_UpdatePoolRequestUpgradePolicy(
    request: UpdatePoolRequestUpgradePolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.max_surge is not None:
        output["max_surge"] = request.max_surge

    if request.max_unavailable is not None:
        output["max_unavailable"] = request.max_unavailable

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
                    "project_id",
                    request.project_id or defaults.default_project_id
                    if request.project_id is not None
                    else None,
                    defaults.default_project_id,
                ),
                OneOfPossibility(
                    "organization_id",
                    request.organization_id or defaults.default_organization_id
                    if request.organization_id is not None
                    else None,
                    defaults.default_organization_id,
                ),
            ]
        ),
    )

    if request.admission_plugins is not None:
        output["admission_plugins"] = request.admission_plugins

    if request.apiserver_cert_sans is not None:
        output["apiserver_cert_sans"] = request.apiserver_cert_sans

    if request.auto_upgrade is not None:
        output["auto_upgrade"] = marshal_CreateClusterRequestAutoUpgrade(
            request.auto_upgrade, defaults
        )

    if request.autoscaler_config is not None:
        output["autoscaler_config"] = marshal_CreateClusterRequestAutoscalerConfig(
            request.autoscaler_config, defaults
        )

    if request.cni is not None:
        output["cni"] = CNI(request.cni)

    if request.description is not None:
        output["description"] = request.description

    if request.enable_dashboard is not None:
        output["enable_dashboard"] = request.enable_dashboard

    if request.feature_gates is not None:
        output["feature_gates"] = request.feature_gates

    if request.ingress is not None:
        output["ingress"] = Ingress(request.ingress)

    if request.name is not None:
        output["name"] = request.name

    if request.open_id_connect_config is not None:
        output[
            "open_id_connect_config"
        ] = marshal_CreateClusterRequestOpenIDConnectConfig(
            request.open_id_connect_config, defaults
        )

    if request.pools is not None:
        output["pools"] = [
            marshal_CreateClusterRequestPoolConfig(v, defaults) for v in request.pools
        ]

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.type_ is not None:
        output["type"] = request.type_

    if request.version is not None:
        output["version"] = request.version

    return output


def marshal_CreatePoolRequest(
    request: CreatePoolRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.autohealing is not None:
        output["autohealing"] = request.autohealing

    if request.autoscaling is not None:
        output["autoscaling"] = request.autoscaling

    if request.container_runtime is not None:
        output["container_runtime"] = Runtime(request.container_runtime)

    if request.kubelet_args is not None:
        output["kubelet_args"] = request.kubelet_args

    if request.max_size is not None:
        output["max_size"] = request.max_size

    if request.min_size is not None:
        output["min_size"] = request.min_size

    if request.name is not None:
        output["name"] = request.name

    if request.node_type is not None:
        output["node_type"] = request.node_type

    if request.placement_group_id is not None:
        output["placement_group_id"] = request.placement_group_id

    if request.root_volume_size is not None:
        output["root_volume_size"] = request.root_volume_size

    if request.root_volume_type is not None:
        output["root_volume_type"] = PoolVolumeType(request.root_volume_type)

    if request.size is not None:
        output["size"] = request.size

    if request.tags is not None:
        output["tags"] = request.tags

    if request.upgrade_policy is not None:
        output["upgrade_policy"] = marshal_CreatePoolRequestUpgradePolicy(
            request.upgrade_policy, defaults
        )

    if request.zone is not None:
        output["zone"] = request.zone or defaults.default_zone

    return output


def marshal_MigrateToPrivateNetworkClusterRequest(
    request: MigrateToPrivateNetworkClusterRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    return output


def marshal_SetClusterTypeRequest(
    request: SetClusterTypeRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    return output


def marshal_UpdateClusterRequest(
    request: UpdateClusterRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.admission_plugins is not None:
        output["admission_plugins"] = request.admission_plugins

    if request.apiserver_cert_sans is not None:
        output["apiserver_cert_sans"] = request.apiserver_cert_sans

    if request.auto_upgrade is not None:
        output["auto_upgrade"] = marshal_UpdateClusterRequestAutoUpgrade(
            request.auto_upgrade, defaults
        )

    if request.autoscaler_config is not None:
        output["autoscaler_config"] = marshal_UpdateClusterRequestAutoscalerConfig(
            request.autoscaler_config, defaults
        )

    if request.description is not None:
        output["description"] = request.description

    if request.enable_dashboard is not None:
        output["enable_dashboard"] = request.enable_dashboard

    if request.feature_gates is not None:
        output["feature_gates"] = request.feature_gates

    if request.ingress is not None:
        output["ingress"] = Ingress(request.ingress)

    if request.name is not None:
        output["name"] = request.name

    if request.open_id_connect_config is not None:
        output[
            "open_id_connect_config"
        ] = marshal_UpdateClusterRequestOpenIDConnectConfig(
            request.open_id_connect_config, defaults
        )

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdatePoolRequest(
    request: UpdatePoolRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.autohealing is not None:
        output["autohealing"] = request.autohealing

    if request.autoscaling is not None:
        output["autoscaling"] = request.autoscaling

    if request.kubelet_args is not None:
        output["kubelet_args"] = request.kubelet_args

    if request.max_size is not None:
        output["max_size"] = request.max_size

    if request.min_size is not None:
        output["min_size"] = request.min_size

    if request.size is not None:
        output["size"] = request.size

    if request.tags is not None:
        output["tags"] = request.tags

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

    if request.upgrade_pools is not None:
        output["upgrade_pools"] = request.upgrade_pools

    if request.version is not None:
        output["version"] = request.version

    return output


def marshal_UpgradePoolRequest(
    request: UpgradePoolRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.version is not None:
        output["version"] = request.version

    return output
