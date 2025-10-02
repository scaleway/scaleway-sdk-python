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
    InstanceGroupEventLevel,
    InstanceGroupEventSource,
    InstancePolicyAction,
    InstancePolicyType,
    InstanceTemplateStatus,
    MetricAggregate,
    MetricManagedMetric,
    MetricOperator,
    VolumeInstanceTemplateVolumeType,
    Capacity,
    Loadbalancer,
    InstanceGroup,
    Metric,
    InstancePolicy,
    VolumeInstanceTemplateFromEmpty,
    VolumeInstanceTemplateFromSnapshot,
    VolumeInstanceTemplate,
    InstanceTemplate,
    InstanceGroupEvent,
    ListInstanceGroupEventsResponse,
    ListInstanceGroupsResponse,
    ListInstancePoliciesResponse,
    ListInstanceTemplatesResponse,
    CreateInstanceGroupRequest,
    CreateInstancePolicyRequest,
    CreateInstanceTemplateRequest,
    UpdateInstanceGroupRequestCapacity,
    UpdateInstanceGroupRequestLoadbalancer,
    UpdateInstanceGroupRequest,
    UpdateInstancePolicyRequestMetric,
    UpdateInstancePolicyRequest,
    UpdateInstanceTemplateRequest,
)


def unmarshal_Capacity(data: Any) -> Capacity:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Capacity' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("max_replicas", None)
    if field is not None:
        args["max_replicas"] = field
    else:
        args["max_replicas"] = 0

    field = data.get("min_replicas", None)
    if field is not None:
        args["min_replicas"] = field
    else:
        args["min_replicas"] = 0

    field = data.get("cooldown_delay", None)
    if field is not None:
        args["cooldown_delay"] = field
    else:
        args["cooldown_delay"] = None

    return Capacity(**args)


def unmarshal_Loadbalancer(data: Any) -> Loadbalancer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Loadbalancer' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("backend_ids", None)
    if field is not None:
        args["backend_ids"] = field
    else:
        args["backend_ids"] = []

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field
    else:
        args["private_network_id"] = None

    return Loadbalancer(**args)


def unmarshal_InstanceGroup(data: Any) -> InstanceGroup:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstanceGroup' failed as data isn't a dictionary."
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

    field = data.get("instance_template_id", None)
    if field is not None:
        args["instance_template_id"] = field
    else:
        args["instance_template_id"] = None

    field = data.get("capacity", None)
    if field is not None:
        args["capacity"] = unmarshal_Capacity(field)
    else:
        args["capacity"] = None

    field = data.get("loadbalancer", None)
    if field is not None:
        args["loadbalancer"] = unmarshal_Loadbalancer(field)
    else:
        args["loadbalancer"] = None

    field = data.get("error_messages", None)
    if field is not None:
        args["error_messages"] = field
    else:
        args["error_messages"] = []

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

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

    return InstanceGroup(**args)


def unmarshal_Metric(data: Any) -> Metric:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Metric' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("operator", None)
    if field is not None:
        args["operator"] = field
    else:
        args["operator"] = MetricOperator.OPERATOR_UNKNOWN

    field = data.get("aggregate", None)
    if field is not None:
        args["aggregate"] = field
    else:
        args["aggregate"] = MetricAggregate.AGGREGATE_UNKNOWN

    field = data.get("sampling_range_min", None)
    if field is not None:
        args["sampling_range_min"] = field
    else:
        args["sampling_range_min"] = 0

    field = data.get("threshold", None)
    if field is not None:
        args["threshold"] = field
    else:
        args["threshold"] = 0.0

    field = data.get("managed_metric", None)
    if field is not None:
        args["managed_metric"] = field
    else:
        args["managed_metric"] = MetricManagedMetric.MANAGED_METRIC_UNKNOWN

    field = data.get("cockpit_metric_name", None)
    if field is not None:
        args["cockpit_metric_name"] = field
    else:
        args["cockpit_metric_name"] = None

    return Metric(**args)


def unmarshal_InstancePolicy(data: Any) -> InstancePolicy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstancePolicy' failed as data isn't a dictionary."
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

    field = data.get("action", None)
    if field is not None:
        args["action"] = field
    else:
        args["action"] = InstancePolicyAction.UNKNOWN_ACTION

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = InstancePolicyType.UNKNOWN_TYPE

    field = data.get("value", None)
    if field is not None:
        args["value"] = field
    else:
        args["value"] = 0

    field = data.get("priority", None)
    if field is not None:
        args["priority"] = field
    else:
        args["priority"] = 0

    field = data.get("instance_group_id", None)
    if field is not None:
        args["instance_group_id"] = field
    else:
        args["instance_group_id"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("metric", None)
    if field is not None:
        args["metric"] = unmarshal_Metric(field)
    else:
        args["metric"] = None

    return InstancePolicy(**args)


def unmarshal_VolumeInstanceTemplateFromEmpty(
    data: Any,
) -> VolumeInstanceTemplateFromEmpty:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeInstanceTemplateFromEmpty' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = None

    return VolumeInstanceTemplateFromEmpty(**args)


def unmarshal_VolumeInstanceTemplateFromSnapshot(
    data: Any,
) -> VolumeInstanceTemplateFromSnapshot:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeInstanceTemplateFromSnapshot' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("snapshot_id", None)
    if field is not None:
        args["snapshot_id"] = field
    else:
        args["snapshot_id"] = None

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = None

    return VolumeInstanceTemplateFromSnapshot(**args)


def unmarshal_VolumeInstanceTemplate(data: Any) -> VolumeInstanceTemplate:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeInstanceTemplate' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

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

    field = data.get("boot", None)
    if field is not None:
        args["boot"] = field
    else:
        args["boot"] = False

    field = data.get("volume_type", None)
    if field is not None:
        args["volume_type"] = field
    else:
        args["volume_type"] = VolumeInstanceTemplateVolumeType.UNKNOWN_VOLUME_TYPE

    field = data.get("perf_iops", None)
    if field is not None:
        args["perf_iops"] = field
    else:
        args["perf_iops"] = None

    field = data.get("from_empty", None)
    if field is not None:
        args["from_empty"] = unmarshal_VolumeInstanceTemplateFromEmpty(field)
    else:
        args["from_empty"] = None

    field = data.get("from_snapshot", None)
    if field is not None:
        args["from_snapshot"] = unmarshal_VolumeInstanceTemplateFromSnapshot(field)
    else:
        args["from_snapshot"] = None

    return VolumeInstanceTemplate(**args)


def unmarshal_InstanceTemplate(data: Any) -> InstanceTemplate:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstanceTemplate' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("commercial_type", None)
    if field is not None:
        args["commercial_type"] = field
    else:
        args["commercial_type"] = None

    field = data.get("volumes", None)
    if field is not None:
        args["volumes"] = (
            {
                key: unmarshal_VolumeInstanceTemplate(value)
                for key, value in field.items()
            }
            if field is not None
            else None
        )
    else:
        args["volumes"] = {}

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

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

    field = data.get("private_network_ids", None)
    if field is not None:
        args["private_network_ids"] = field
    else:
        args["private_network_ids"] = []

    field = data.get("image_id", None)
    if field is not None:
        args["image_id"] = field
    else:
        args["image_id"] = None

    field = data.get("security_group_id", None)
    if field is not None:
        args["security_group_id"] = field
    else:
        args["security_group_id"] = None

    field = data.get("placement_group_id", None)
    if field is not None:
        args["placement_group_id"] = field
    else:
        args["placement_group_id"] = None

    field = data.get("public_ips_v4_count", None)
    if field is not None:
        args["public_ips_v4_count"] = field
    else:
        args["public_ips_v4_count"] = 0

    field = data.get("public_ips_v6_count", None)
    if field is not None:
        args["public_ips_v6_count"] = field
    else:
        args["public_ips_v6_count"] = 0

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = InstanceTemplateStatus.UNKNOWN_STATUS

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("cloud_init", None)
    if field is not None:
        args["cloud_init"] = field
    else:
        args["cloud_init"] = None

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

    return InstanceTemplate(**args)


def unmarshal_InstanceGroupEvent(data: Any) -> InstanceGroupEvent:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstanceGroupEvent' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("source", None)
    if field is not None:
        args["source"] = field
    else:
        args["source"] = InstanceGroupEventSource.UNKNOWN_SOURCE

    field = data.get("level", None)
    if field is not None:
        args["level"] = field
    else:
        args["level"] = InstanceGroupEventLevel.INFO

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("details", None)
    if field is not None:
        args["details"] = field
    else:
        args["details"] = None

    return InstanceGroupEvent(**args)


def unmarshal_ListInstanceGroupEventsResponse(
    data: Any,
) -> ListInstanceGroupEventsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstanceGroupEventsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("instance_events", None)
    if field is not None:
        args["instance_events"] = (
            [unmarshal_InstanceGroupEvent(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["instance_events"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListInstanceGroupEventsResponse(**args)


def unmarshal_ListInstanceGroupsResponse(data: Any) -> ListInstanceGroupsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstanceGroupsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("instance_groups", None)
    if field is not None:
        args["instance_groups"] = (
            [unmarshal_InstanceGroup(v) for v in field] if field is not None else None
        )
    else:
        args["instance_groups"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListInstanceGroupsResponse(**args)


def unmarshal_ListInstancePoliciesResponse(data: Any) -> ListInstancePoliciesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstancePoliciesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("policies", None)
    if field is not None:
        args["policies"] = (
            [unmarshal_InstancePolicy(v) for v in field] if field is not None else None
        )
    else:
        args["policies"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListInstancePoliciesResponse(**args)


def unmarshal_ListInstanceTemplatesResponse(data: Any) -> ListInstanceTemplatesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstanceTemplatesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("instance_templates", None)
    if field is not None:
        args["instance_templates"] = (
            [unmarshal_InstanceTemplate(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["instance_templates"] = []

    return ListInstanceTemplatesResponse(**args)


def marshal_Capacity(
    request: Capacity,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.max_replicas is not None:
        output["max_replicas"] = request.max_replicas

    if request.min_replicas is not None:
        output["min_replicas"] = request.min_replicas

    if request.cooldown_delay is not None:
        output["cooldown_delay"] = request.cooldown_delay

    return output


def marshal_Loadbalancer(
    request: Loadbalancer,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.backend_ids is not None:
        output["backend_ids"] = request.backend_ids

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    return output


def marshal_CreateInstanceGroupRequest(
    request: CreateInstanceGroupRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.template_id is not None:
        output["template_id"] = request.template_id

    if request.capacity is not None:
        output["capacity"] = marshal_Capacity(request.capacity, defaults)

    if request.loadbalancer is not None:
        output["loadbalancer"] = marshal_Loadbalancer(request.loadbalancer, defaults)

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_Metric(
    request: Metric,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="managed_metric",
                    value=request.managed_metric,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="cockpit_metric_name",
                    value=request.cockpit_metric_name,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.operator is not None:
        output["operator"] = request.operator

    if request.aggregate is not None:
        output["aggregate"] = request.aggregate

    if request.sampling_range_min is not None:
        output["sampling_range_min"] = request.sampling_range_min

    if request.threshold is not None:
        output["threshold"] = request.threshold

    return output


def marshal_CreateInstancePolicyRequest(
    request: CreateInstancePolicyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="metric", value=request.metric, marshal_func=marshal_Metric
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.action is not None:
        output["action"] = request.action

    if request.type_ is not None:
        output["type"] = request.type_

    if request.value is not None:
        output["value"] = request.value

    if request.priority is not None:
        output["priority"] = request.priority

    if request.instance_group_id is not None:
        output["instance_group_id"] = request.instance_group_id

    return output


def marshal_VolumeInstanceTemplateFromEmpty(
    request: VolumeInstanceTemplateFromEmpty,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.size is not None:
        output["size"] = request.size

    return output


def marshal_VolumeInstanceTemplateFromSnapshot(
    request: VolumeInstanceTemplateFromSnapshot,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.snapshot_id is not None:
        output["snapshot_id"] = request.snapshot_id

    if request.size is not None:
        output["size"] = request.size

    return output


def marshal_VolumeInstanceTemplate(
    request: VolumeInstanceTemplate,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="from_empty",
                    value=request.from_empty,
                    marshal_func=marshal_VolumeInstanceTemplateFromEmpty,
                ),
                OneOfPossibility(
                    param="from_snapshot",
                    value=request.from_snapshot,
                    marshal_func=marshal_VolumeInstanceTemplateFromSnapshot,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="perf_iops", value=request.perf_iops, marshal_func=None
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.boot is not None:
        output["boot"] = request.boot

    if request.volume_type is not None:
        output["volume_type"] = request.volume_type

    return output


def marshal_CreateInstanceTemplateRequest(
    request: CreateInstanceTemplateRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.commercial_type is not None:
        output["commercial_type"] = request.commercial_type

    if request.volumes is not None:
        output["volumes"] = {
            key: marshal_VolumeInstanceTemplate(value, defaults)
            for key, value in request.volumes.items()
        }

    if request.image_id is not None:
        output["image_id"] = request.image_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.security_group_id is not None:
        output["security_group_id"] = request.security_group_id

    if request.name is not None:
        output["name"] = request.name

    if request.placement_group_id is not None:
        output["placement_group_id"] = request.placement_group_id

    if request.public_ips_v4_count is not None:
        output["public_ips_v4_count"] = request.public_ips_v4_count

    if request.public_ips_v6_count is not None:
        output["public_ips_v6_count"] = request.public_ips_v6_count

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.private_network_ids is not None:
        output["private_network_ids"] = request.private_network_ids

    if request.cloud_init is not None:
        output["cloud_init"] = request.cloud_init

    return output


def marshal_UpdateInstanceGroupRequestCapacity(
    request: UpdateInstanceGroupRequestCapacity,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.max_replicas is not None:
        output["max_replicas"] = request.max_replicas

    if request.min_replicas is not None:
        output["min_replicas"] = request.min_replicas

    if request.cooldown_delay is not None:
        output["cooldown_delay"] = request.cooldown_delay

    return output


def marshal_UpdateInstanceGroupRequestLoadbalancer(
    request: UpdateInstanceGroupRequestLoadbalancer,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.backend_ids is not None:
        output["backend_ids"] = request.backend_ids

    return output


def marshal_UpdateInstanceGroupRequest(
    request: UpdateInstanceGroupRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.capacity is not None:
        output["capacity"] = marshal_UpdateInstanceGroupRequestCapacity(
            request.capacity, defaults
        )

    if request.loadbalancer is not None:
        output["loadbalancer"] = marshal_UpdateInstanceGroupRequestLoadbalancer(
            request.loadbalancer, defaults
        )

    return output


def marshal_UpdateInstancePolicyRequestMetric(
    request: UpdateInstancePolicyRequestMetric,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="managed_metric",
                    value=request.managed_metric,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="cockpit_metric_name",
                    value=request.cockpit_metric_name,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.operator is not None:
        output["operator"] = request.operator

    if request.aggregate is not None:
        output["aggregate"] = request.aggregate

    if request.name is not None:
        output["name"] = request.name

    if request.sampling_range_min is not None:
        output["sampling_range_min"] = request.sampling_range_min

    if request.threshold is not None:
        output["threshold"] = request.threshold

    return output


def marshal_UpdateInstancePolicyRequest(
    request: UpdateInstancePolicyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="metric",
                    value=request.metric,
                    marshal_func=marshal_UpdateInstancePolicyRequestMetric,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.action is not None:
        output["action"] = request.action

    if request.type_ is not None:
        output["type"] = request.type_

    if request.value is not None:
        output["value"] = request.value

    if request.priority is not None:
        output["priority"] = request.priority

    return output


def marshal_UpdateInstanceTemplateRequest(
    request: UpdateInstanceTemplateRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.commercial_type is not None:
        output["commercial_type"] = request.commercial_type

    if request.image_id is not None:
        output["image_id"] = request.image_id

    if request.volumes is not None:
        output["volumes"] = {
            key: marshal_VolumeInstanceTemplate(value, defaults)
            for key, value in request.volumes.items()
        }

    if request.tags is not None:
        output["tags"] = request.tags

    if request.security_group_id is not None:
        output["security_group_id"] = request.security_group_id

    if request.placement_group_id is not None:
        output["placement_group_id"] = request.placement_group_id

    if request.public_ips_v4_count is not None:
        output["public_ips_v4_count"] = request.public_ips_v4_count

    if request.public_ips_v6_count is not None:
        output["public_ips_v6_count"] = request.public_ips_v6_count

    if request.name is not None:
        output["name"] = request.name

    if request.private_network_ids is not None:
        output["private_network_ids"] = request.private_network_ids

    if request.cloud_init is not None:
        output["cloud_init"] = request.cloud_init

    return output
