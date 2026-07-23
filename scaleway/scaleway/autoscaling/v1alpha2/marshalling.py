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
    AlertAlertType,
    GroupGroupStatus,
    GroupSummaryScalingPolicyTargetType,
    LogLogLevel,
    GroupLoadBalancerConfigurationAutoHealing,
    GroupLoadBalancerConfigurationBackend,
    GroupScalingPolicyScalingPolicyCpuTarget,
    GroupScalingPolicyScalingPolicyFixedSize,
    GroupScalingPolicyScalingPolicyMemoryTarget,
    Alert,
    GroupLoadBalancerConfiguration,
    GroupScalingPolicy,
    Group,
    ListAlertsResponse,
    GroupSummary,
    ListGroupsResponse,
    Log,
    ListLogsResponse,
    Server,
    ListServersResponse,
    LoadBalancerConfigurationSpecAutoHealing,
    LoadBalancerConfigurationSpecBackend,
    LoadBalancerConfigurationSpec,
    ScalingPolicySpec,
    CreateGroupRequest,
    UpdateGroupRequest,
)


def unmarshal_GroupLoadBalancerConfigurationAutoHealing(
    data: Any,
) -> GroupLoadBalancerConfigurationAutoHealing:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GroupLoadBalancerConfigurationAutoHealing' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("enabled", None)
    if field is not None:
        args["enabled"] = field
    else:
        args["enabled"] = None

    field = data.get("grace_period", None)
    if field is not None:
        args["grace_period"] = field
    else:
        args["grace_period"] = None

    return GroupLoadBalancerConfigurationAutoHealing(**args)


def unmarshal_GroupLoadBalancerConfigurationBackend(
    data: Any,
) -> GroupLoadBalancerConfigurationBackend:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GroupLoadBalancerConfigurationBackend' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("backend_id", None)
    if field is not None:
        args["backend_id"] = field
    else:
        args["backend_id"] = None

    field = data.get("address_family", None)
    if field is not None:
        args["address_family"] = field
    else:
        args["address_family"] = None

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field
    else:
        args["private_network_id"] = None

    return GroupLoadBalancerConfigurationBackend(**args)


def unmarshal_GroupScalingPolicyScalingPolicyCpuTarget(
    data: Any,
) -> GroupScalingPolicyScalingPolicyCpuTarget:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GroupScalingPolicyScalingPolicyCpuTarget' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("target_avg_percent", None)
    if field is not None:
        args["target_avg_percent"] = field
    else:
        args["target_avg_percent"] = None

    return GroupScalingPolicyScalingPolicyCpuTarget(**args)


def unmarshal_GroupScalingPolicyScalingPolicyFixedSize(
    data: Any,
) -> GroupScalingPolicyScalingPolicyFixedSize:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GroupScalingPolicyScalingPolicyFixedSize' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = None

    return GroupScalingPolicyScalingPolicyFixedSize(**args)


def unmarshal_GroupScalingPolicyScalingPolicyMemoryTarget(
    data: Any,
) -> GroupScalingPolicyScalingPolicyMemoryTarget:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GroupScalingPolicyScalingPolicyMemoryTarget' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("target_avg_percent", None)
    if field is not None:
        args["target_avg_percent"] = field
    else:
        args["target_avg_percent"] = None

    return GroupScalingPolicyScalingPolicyMemoryTarget(**args)


def unmarshal_Alert(data: Any) -> Alert:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Alert' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = AlertAlertType.UNKNOWN_ALERT_TYPE

    field = data.get("group_id", None)
    if field is not None:
        args["group_id"] = field
    else:
        args["group_id"] = None

    field = data.get("failing_quotas", None)
    if field is not None:
        args["failing_quotas"] = field
    else:
        args["failing_quotas"] = []

    field = data.get("opened_at", None)
    if field is not None:
        args["opened_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["opened_at"] = None

    field = data.get("closed_at", None)
    if field is not None:
        args["closed_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["closed_at"] = None

    return Alert(**args)


def unmarshal_GroupLoadBalancerConfiguration(
    data: Any,
) -> GroupLoadBalancerConfiguration:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GroupLoadBalancerConfiguration' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("load_balancer_id", None)
    if field is not None:
        args["load_balancer_id"] = field
    else:
        args["load_balancer_id"] = None

    field = data.get("backends", None)
    if field is not None:
        args["backends"] = (
            [unmarshal_GroupLoadBalancerConfigurationBackend(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["backends"] = None

    field = data.get("auto_healing", None)
    if field is not None:
        args["auto_healing"] = unmarshal_GroupLoadBalancerConfigurationAutoHealing(
            field
        )
    else:
        args["auto_healing"] = None

    return GroupLoadBalancerConfiguration(**args)


def unmarshal_GroupScalingPolicy(data: Any) -> GroupScalingPolicy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GroupScalingPolicy' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("minimum_size", None)
    if field is not None:
        args["minimum_size"] = field
    else:
        args["minimum_size"] = None

    field = data.get("maximum_size", None)
    if field is not None:
        args["maximum_size"] = field
    else:
        args["maximum_size"] = None

    field = data.get("scale_in_step", None)
    if field is not None:
        args["scale_in_step"] = field
    else:
        args["scale_in_step"] = None

    field = data.get("scale_out_step", None)
    if field is not None:
        args["scale_out_step"] = field
    else:
        args["scale_out_step"] = None

    field = data.get("scale_out_cooldown", None)
    if field is not None:
        args["scale_out_cooldown"] = field
    else:
        args["scale_out_cooldown"] = None

    field = data.get("scale_in_cooldown", None)
    if field is not None:
        args["scale_in_cooldown"] = field
    else:
        args["scale_in_cooldown"] = None

    field = data.get("fixed_size", None)
    if field is not None:
        args["fixed_size"] = unmarshal_GroupScalingPolicyScalingPolicyFixedSize(field)
    else:
        args["fixed_size"] = None

    field = data.get("cpu_target", None)
    if field is not None:
        args["cpu_target"] = unmarshal_GroupScalingPolicyScalingPolicyCpuTarget(field)
    else:
        args["cpu_target"] = None

    field = data.get("memory_target", None)
    if field is not None:
        args["memory_target"] = unmarshal_GroupScalingPolicyScalingPolicyMemoryTarget(
            field
        )
    else:
        args["memory_target"] = None

    return GroupScalingPolicy(**args)


def unmarshal_Group(data: Any) -> Group:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Group' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

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

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = GroupGroupStatus.UNKNOWN_GROUP_STATUS

    field = data.get("open_alerts", None)
    if field is not None:
        args["open_alerts"] = (
            [unmarshal_Alert(v) for v in field] if field is not None else None
        )
    else:
        args["open_alerts"] = []

    field = data.get("current_size", None)
    if field is not None:
        args["current_size"] = field
    else:
        args["current_size"] = 0

    field = data.get("target_size", None)
    if field is not None:
        args["target_size"] = field
    else:
        args["target_size"] = 0

    field = data.get("template_id", None)
    if field is not None:
        args["template_id"] = field
    else:
        args["template_id"] = None

    field = data.get("last_scale_out_at", None)
    if field is not None:
        args["last_scale_out_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["last_scale_out_at"] = None

    field = data.get("last_scale_in_at", None)
    if field is not None:
        args["last_scale_in_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["last_scale_in_at"] = None

    field = data.get("scaling_policy", None)
    if field is not None:
        args["scaling_policy"] = unmarshal_GroupScalingPolicy(field)
    else:
        args["scaling_policy"] = None

    field = data.get("load_balancer_configuration", None)
    if field is not None:
        args["load_balancer_configuration"] = unmarshal_GroupLoadBalancerConfiguration(
            field
        )
    else:
        args["load_balancer_configuration"] = None

    return Group(**args)


def unmarshal_ListAlertsResponse(data: Any) -> ListAlertsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListAlertsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("alerts", None)
    if field is not None:
        args["alerts"] = (
            [unmarshal_Alert(v) for v in field] if field is not None else None
        )
    else:
        args["alerts"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("next_page_token", None)
    if field is not None:
        args["next_page_token"] = field
    else:
        args["next_page_token"] = None

    return ListAlertsResponse(**args)


def unmarshal_GroupSummary(data: Any) -> GroupSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GroupSummary' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

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

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = GroupGroupStatus.UNKNOWN_GROUP_STATUS

    field = data.get("template_id", None)
    if field is not None:
        args["template_id"] = field
    else:
        args["template_id"] = None

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

    field = data.get("load_balancer_id", None)
    if field is not None:
        args["load_balancer_id"] = field
    else:
        args["load_balancer_id"] = None

    field = data.get("current_size", None)
    if field is not None:
        args["current_size"] = field
    else:
        args["current_size"] = 0

    field = data.get("minimum_size", None)
    if field is not None:
        args["minimum_size"] = field
    else:
        args["minimum_size"] = 0

    field = data.get("maximum_size", None)
    if field is not None:
        args["maximum_size"] = field
    else:
        args["maximum_size"] = 0

    field = data.get("scaling_policy_target_type", None)
    if field is not None:
        args["scaling_policy_target_type"] = field
    else:
        args["scaling_policy_target_type"] = (
            GroupSummaryScalingPolicyTargetType.UNKNOWN_SCALING_POLICY_TARGET_TYPE
        )

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("latest_open_alert", None)
    if field is not None:
        args["latest_open_alert"] = unmarshal_Alert(field)
    else:
        args["latest_open_alert"] = None

    return GroupSummary(**args)


def unmarshal_ListGroupsResponse(data: Any) -> ListGroupsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListGroupsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("group_summaries", None)
    if field is not None:
        args["group_summaries"] = (
            [unmarshal_GroupSummary(v) for v in field] if field is not None else None
        )
    else:
        args["group_summaries"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("next_page_token", None)
    if field is not None:
        args["next_page_token"] = field
    else:
        args["next_page_token"] = None

    return ListGroupsResponse(**args)


def unmarshal_Log(data: Any) -> Log:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Log' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("level", None)
    if field is not None:
        args["level"] = field
    else:
        args["level"] = LogLogLevel.UNKNOWN_LOG_LEVEL

    field = data.get("message", None)
    if field is not None:
        args["message"] = field
    else:
        args["message"] = None

    field = data.get("timestamp", None)
    if field is not None:
        args["timestamp"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["timestamp"] = None

    return Log(**args)


def unmarshal_ListLogsResponse(data: Any) -> ListLogsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListLogsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("logs", None)
    if field is not None:
        args["logs"] = [unmarshal_Log(v) for v in field] if field is not None else None
    else:
        args["logs"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("next_page_token", None)
    if field is not None:
        args["next_page_token"] = field
    else:
        args["next_page_token"] = None

    return ListLogsResponse(**args)


def unmarshal_Server(data: Any) -> Server:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Server' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("server_id", None)
    if field is not None:
        args["server_id"] = field
    else:
        args["server_id"] = None

    return Server(**args)


def unmarshal_ListServersResponse(data: Any) -> ListServersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("servers", None)
    if field is not None:
        args["servers"] = (
            [unmarshal_Server(v) for v in field] if field is not None else None
        )
    else:
        args["servers"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("next_page_token", None)
    if field is not None:
        args["next_page_token"] = field
    else:
        args["next_page_token"] = None

    return ListServersResponse(**args)


def marshal_LoadBalancerConfigurationSpecAutoHealing(
    request: LoadBalancerConfigurationSpecAutoHealing,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.enabled is not None:
        output["enabled"] = request.enabled

    if request.grace_period is not None:
        output["grace_period"] = request.grace_period

    return output


def marshal_LoadBalancerConfigurationSpecBackend(
    request: LoadBalancerConfigurationSpecBackend,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id

    if request.address_family is not None:
        output["address_family"] = request.address_family

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    return output


def marshal_GroupScalingPolicyScalingPolicyCpuTarget(
    request: GroupScalingPolicyScalingPolicyCpuTarget,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.target_avg_percent is not None:
        output["target_avg_percent"] = request.target_avg_percent

    return output


def marshal_GroupScalingPolicyScalingPolicyFixedSize(
    request: GroupScalingPolicyScalingPolicyFixedSize,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.size is not None:
        output["size"] = request.size

    return output


def marshal_GroupScalingPolicyScalingPolicyMemoryTarget(
    request: GroupScalingPolicyScalingPolicyMemoryTarget,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.target_avg_percent is not None:
        output["target_avg_percent"] = request.target_avg_percent

    return output


def marshal_LoadBalancerConfigurationSpec(
    request: LoadBalancerConfigurationSpec,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.backends is not None:
        output["backends"] = [
            marshal_LoadBalancerConfigurationSpecBackend(item, defaults)
            for item in request.backends
        ]

    if request.load_balancer_id is not None:
        output["load_balancer_id"] = request.load_balancer_id

    if request.auto_healing is not None:
        output["auto_healing"] = marshal_LoadBalancerConfigurationSpecAutoHealing(
            request.auto_healing, defaults
        )

    return output


def marshal_ScalingPolicySpec(
    request: ScalingPolicySpec,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="fixed_size",
                    value=request.fixed_size,
                    marshal_func=marshal_GroupScalingPolicyScalingPolicyFixedSize,
                ),
                OneOfPossibility(
                    param="cpu_target",
                    value=request.cpu_target,
                    marshal_func=marshal_GroupScalingPolicyScalingPolicyCpuTarget,
                ),
                OneOfPossibility(
                    param="memory_target",
                    value=request.memory_target,
                    marshal_func=marshal_GroupScalingPolicyScalingPolicyMemoryTarget,
                ),
            ]
        ),
    )

    if request.minimum_size is not None:
        output["minimum_size"] = request.minimum_size

    if request.maximum_size is not None:
        output["maximum_size"] = request.maximum_size

    if request.scale_out_cooldown is not None:
        output["scale_out_cooldown"] = request.scale_out_cooldown

    if request.scale_in_cooldown is not None:
        output["scale_in_cooldown"] = request.scale_in_cooldown

    if request.scale_in_step is not None:
        output["scale_in_step"] = request.scale_in_step

    if request.scale_out_step is not None:
        output["scale_out_step"] = request.scale_out_step

    return output


def marshal_CreateGroupRequest(
    request: CreateGroupRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.template_id is not None:
        output["template_id"] = request.template_id

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.scaling_policy_spec is not None:
        output["scaling_policy_spec"] = marshal_ScalingPolicySpec(
            request.scaling_policy_spec, defaults
        )

    if request.load_balancer_configuration_spec is not None:
        output["load_balancer_configuration_spec"] = (
            marshal_LoadBalancerConfigurationSpec(
                request.load_balancer_configuration_spec, defaults
            )
        )

    return output


def marshal_UpdateGroupRequest(
    request: UpdateGroupRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.template_id is not None:
        output["template_id"] = request.template_id

    if request.scaling_policy_spec is not None:
        output["scaling_policy_spec"] = marshal_ScalingPolicySpec(
            request.scaling_policy_spec, defaults
        )

    if request.load_balancer_configuration_spec is not None:
        output["load_balancer_configuration_spec"] = (
            marshal_LoadBalancerConfigurationSpec(
                request.load_balancer_configuration_spec, defaults
            )
        )

    return output
