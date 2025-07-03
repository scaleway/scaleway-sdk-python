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
    InstanceGroupEventLevel,
    InstanceGroupEventSource,
    InstancePolicyAction,
    InstancePolicyType,
    InstanceTemplateStatus,
    ListInstanceGroupEventsRequestOrderBy,
    ListInstanceGroupsRequestOrderBy,
    ListInstancePoliciesRequestOrderBy,
    ListInstanceTemplatesRequestOrderBy,
    MetricAggregate,
    MetricManagedMetric,
    MetricOperator,
    UpdateInstancePolicyRequestMetricAggregate,
    UpdateInstancePolicyRequestMetricManagedMetric,
    UpdateInstancePolicyRequestMetricOperator,
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

    args: Dict[str, Any] = {}

    field = data.get("max_replicas", 0)
    args["max_replicas"] = field

    field = data.get("min_replicas", 0)
    args["min_replicas"] = field

    field = data.get("cooldown_delay", None)
    args["cooldown_delay"] = field

    return Capacity(**args)

def unmarshal_Loadbalancer(data: Any) -> Loadbalancer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Loadbalancer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("backend_ids", [])
    args["backend_ids"] = field

    field = data.get("private_network_id", str())
    args["private_network_id"] = field

    return Loadbalancer(**args)

def unmarshal_InstanceGroup(data: Any) -> InstanceGroup:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstanceGroup' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("instance_template_id", str())
    args["instance_template_id"] = field

    field = data.get("capacity", str())
    args["capacity"] = unmarshal_Capacity(field) if field is not None else None

    field = data.get("loadbalancer", str())
    args["loadbalancer"] = unmarshal_Loadbalancer(field) if field is not None else None

    field = data.get("error_messages", [])
    args["error_messages"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return InstanceGroup(**args)

def unmarshal_Metric(data: Any) -> Metric:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Metric' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("operator", getattr(MetricOperator, "OPERATOR_UNKNOWN"))
    args["operator"] = field

    field = data.get("aggregate", getattr(MetricAggregate, "AGGREGATE_UNKNOWN"))
    args["aggregate"] = field

    field = data.get("sampling_range_min", 0)
    args["sampling_range_min"] = field

    field = data.get("threshold", 0.0)
    args["threshold"] = field

    field = data.get("managed_metric", None)
    args["managed_metric"] = field

    field = data.get("cockpit_metric_name", None)
    args["cockpit_metric_name"] = field

    return Metric(**args)

def unmarshal_InstancePolicy(data: Any) -> InstancePolicy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstancePolicy' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("action", getattr(InstancePolicyAction, "UNKNOWN_ACTION"))
    args["action"] = field

    field = data.get("type", getattr(InstancePolicyType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("value", 0)
    args["value"] = field

    field = data.get("priority", 0)
    args["priority"] = field

    field = data.get("instance_group_id", str())
    args["instance_group_id"] = field

    field = data.get("metric", None)
    args["metric"] = unmarshal_Metric(field) if field is not None else None

    return InstancePolicy(**args)

def unmarshal_VolumeInstanceTemplateFromEmpty(data: Any) -> VolumeInstanceTemplateFromEmpty:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeInstanceTemplateFromEmpty' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("size", str())
    args["size"] = field

    return VolumeInstanceTemplateFromEmpty(**args)

def unmarshal_VolumeInstanceTemplateFromSnapshot(data: Any) -> VolumeInstanceTemplateFromSnapshot:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeInstanceTemplateFromSnapshot' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("snapshot_id", str())
    args["snapshot_id"] = field

    field = data.get("size", None)
    args["size"] = field

    return VolumeInstanceTemplateFromSnapshot(**args)

def unmarshal_VolumeInstanceTemplate(data: Any) -> VolumeInstanceTemplate:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VolumeInstanceTemplate' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("boot", False)
    args["boot"] = field

    field = data.get("volume_type", getattr(VolumeInstanceTemplateVolumeType, "UNKNOWN_VOLUME_TYPE"))
    args["volume_type"] = field

    field = data.get("perf_iops", None)
    args["perf_iops"] = field

    field = data.get("from_empty", None)
    args["from_empty"] = unmarshal_VolumeInstanceTemplateFromEmpty(field) if field is not None else None

    field = data.get("from_snapshot", None)
    args["from_snapshot"] = unmarshal_VolumeInstanceTemplateFromSnapshot(field) if field is not None else None

    return VolumeInstanceTemplate(**args)

def unmarshal_InstanceTemplate(data: Any) -> InstanceTemplate:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstanceTemplate' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("commercial_type", str())
    args["commercial_type"] = field

    field = data.get("volumes", {})
    args["volumes"] = {key: unmarshal_VolumeInstanceTemplate(value)for key, value in field.items()
    } if field is not None else None

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("private_network_ids", [])
    args["private_network_ids"] = field

    field = data.get("image_id", None)
    args["image_id"] = field

    field = data.get("security_group_id", None)
    args["security_group_id"] = field

    field = data.get("placement_group_id", None)
    args["placement_group_id"] = field

    field = data.get("public_ips_v4_count", None)
    args["public_ips_v4_count"] = field

    field = data.get("public_ips_v6_count", None)
    args["public_ips_v6_count"] = field

    field = data.get("status", getattr(InstanceTemplateStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("cloud_init", None)
    args["cloud_init"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return InstanceTemplate(**args)

def unmarshal_InstanceGroupEvent(data: Any) -> InstanceGroupEvent:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstanceGroupEvent' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("source", getattr(InstanceGroupEventSource, "UNKNOWN_SOURCE"))
    args["source"] = field

    field = data.get("level", getattr(InstanceGroupEventLevel, "INFO"))
    args["level"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("details", None)
    args["details"] = field

    return InstanceGroupEvent(**args)

def unmarshal_ListInstanceGroupEventsResponse(data: Any) -> ListInstanceGroupEventsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstanceGroupEventsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("instance_events", [])
    args["instance_events"] = [unmarshal_InstanceGroupEvent(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListInstanceGroupEventsResponse(**args)

def unmarshal_ListInstanceGroupsResponse(data: Any) -> ListInstanceGroupsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstanceGroupsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("instance_groups", [])
    args["instance_groups"] = [unmarshal_InstanceGroup(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListInstanceGroupsResponse(**args)

def unmarshal_ListInstancePoliciesResponse(data: Any) -> ListInstancePoliciesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstancePoliciesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("policies", [])
    args["policies"] = [unmarshal_InstancePolicy(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListInstancePoliciesResponse(**args)

def unmarshal_ListInstanceTemplatesResponse(data: Any) -> ListInstanceTemplatesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInstanceTemplatesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("instance_templates", [])
    args["instance_templates"] = [unmarshal_InstanceTemplate(v) for v in field] if field is not None else None

    return ListInstanceTemplatesResponse(**args)

def marshal_Capacity(
    request: Capacity,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.max_replicas is not None:
        output["max_replicas"] = request.max_replicas
    else:
        output["max_replicas"] = 0

    if request.min_replicas is not None:
        output["min_replicas"] = request.min_replicas
    else:
        output["min_replicas"] = 0

    if request.cooldown_delay is not None:
        output["cooldown_delay"] = request.cooldown_delay
    else:
        output["cooldown_delay"] = None


    return output

def marshal_Loadbalancer(
    request: Loadbalancer,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.backend_ids is not None:
        output["backend_ids"] = request.backend_ids
    else:
        output["backend_ids"] = []

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id
    else:
        output["private_network_id"] = str()


    return output

def marshal_CreateInstanceGroupRequest(
    request: CreateInstanceGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.template_id is not None:
        output["template_id"] = request.template_id
    else:
        output["template_id"] = str()

    if request.capacity is not None:
        output["capacity"] = marshal_Capacity(request.capacity, defaults)
    else:
        output["capacity"] = str()

    if request.loadbalancer is not None:
        output["loadbalancer"] = marshal_Loadbalancer(request.loadbalancer, defaults)
    else:
        output["loadbalancer"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_Metric(
    request: Metric,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="managed_metric", value=request.managed_metric,marshal_func=marshal_MetricManagedMetric
            ),
            OneOfPossibility(param="cockpit_metric_name", value=request.cockpit_metric_name,marshal_func=None
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.operator is not None:
        output["operator"] = str(request.operator)
    else:
        output["operator"] = getattr(MetricOperator, "OPERATOR_UNKNOWN")

    if request.aggregate is not None:
        output["aggregate"] = str(request.aggregate)
    else:
        output["aggregate"] = getattr(MetricAggregate, "AGGREGATE_UNKNOWN")

    if request.sampling_range_min is not None:
        output["sampling_range_min"] = request.sampling_range_min
    else:
        output["sampling_range_min"] = 0

    if request.threshold is not None:
        output["threshold"] = request.threshold
    else:
        output["threshold"] = 0.0


    return output

def marshal_CreateInstancePolicyRequest(
    request: CreateInstancePolicyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="metric", value=request.metric,marshal_func=marshal_Metric
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.action is not None:
        output["action"] = str(request.action)
    else:
        output["action"] = str()

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = str()

    if request.value is not None:
        output["value"] = request.value
    else:
        output["value"] = str()

    if request.priority is not None:
        output["priority"] = request.priority
    else:
        output["priority"] = 0

    if request.instance_group_id is not None:
        output["instance_group_id"] = request.instance_group_id
    else:
        output["instance_group_id"] = str()


    return output

def marshal_VolumeInstanceTemplateFromEmpty(
    request: VolumeInstanceTemplateFromEmpty,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = str()


    return output

def marshal_VolumeInstanceTemplateFromSnapshot(
    request: VolumeInstanceTemplateFromSnapshot,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.snapshot_id is not None:
        output["snapshot_id"] = request.snapshot_id
    else:
        output["snapshot_id"] = str()

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = None


    return output

def marshal_VolumeInstanceTemplate(
    request: VolumeInstanceTemplate,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="from_empty", value=request.from_empty,marshal_func=marshal_VolumeInstanceTemplateFromEmpty
            ),
            OneOfPossibility(param="from_snapshot", value=request.from_snapshot,marshal_func=marshal_VolumeInstanceTemplateFromSnapshot
            ),
        ]),
    )
    output.update(
        resolve_one_of([
            OneOfPossibility(param="perf_iops", value=request.perf_iops,marshal_func=None
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = []

    if request.boot is not None:
        output["boot"] = request.boot
    else:
        output["boot"] = False

    if request.volume_type is not None:
        output["volume_type"] = str(request.volume_type)
    else:
        output["volume_type"] = getattr(VolumeInstanceTemplateVolumeType, "UNKNOWN_VOLUME_TYPE")


    return output

def marshal_CreateInstanceTemplateRequest(
    request: CreateInstanceTemplateRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.commercial_type is not None:
        output["commercial_type"] = request.commercial_type
    else:
        output["commercial_type"] = str()

    if request.volumes is not None:
        output["volumes"] = {
            key: marshal_VolumeInstanceTemplate(value, defaults)
            for key, value in request.volumes.items()
        }
    else:
        output["volumes"] = str()

    if request.image_id is not None:
        output["image_id"] = request.image_id
    else:
        output["image_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.security_group_id is not None:
        output["security_group_id"] = request.security_group_id
    else:
        output["security_group_id"] = None

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.placement_group_id is not None:
        output["placement_group_id"] = request.placement_group_id
    else:
        output["placement_group_id"] = None

    if request.public_ips_v4_count is not None:
        output["public_ips_v4_count"] = request.public_ips_v4_count
    else:
        output["public_ips_v4_count"] = None

    if request.public_ips_v6_count is not None:
        output["public_ips_v6_count"] = request.public_ips_v6_count
    else:
        output["public_ips_v6_count"] = None

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.private_network_ids is not None:
        output["private_network_ids"] = request.private_network_ids
    else:
        output["private_network_ids"] = None

    if request.cloud_init is not None:
        output["cloud_init"] = request.cloud_init
    else:
        output["cloud_init"] = None


    return output

def marshal_UpdateInstanceGroupRequestCapacity(
    request: UpdateInstanceGroupRequestCapacity,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.max_replicas is not None:
        output["max_replicas"] = request.max_replicas
    else:
        output["max_replicas"] = None

    if request.min_replicas is not None:
        output["min_replicas"] = request.min_replicas
    else:
        output["min_replicas"] = None

    if request.cooldown_delay is not None:
        output["cooldown_delay"] = request.cooldown_delay
    else:
        output["cooldown_delay"] = None


    return output

def marshal_UpdateInstanceGroupRequestLoadbalancer(
    request: UpdateInstanceGroupRequestLoadbalancer,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.backend_ids is not None:
        output["backend_ids"] = request.backend_ids
    else:
        output["backend_ids"] = None


    return output

def marshal_UpdateInstanceGroupRequest(
    request: UpdateInstanceGroupRequest,
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

    if request.capacity is not None:
        output["capacity"] = marshal_UpdateInstanceGroupRequestCapacity(request.capacity, defaults)
    else:
        output["capacity"] = None

    if request.loadbalancer is not None:
        output["loadbalancer"] = marshal_UpdateInstanceGroupRequestLoadbalancer(request.loadbalancer, defaults)
    else:
        output["loadbalancer"] = None


    return output

def marshal_UpdateInstancePolicyRequestMetric(
    request: UpdateInstancePolicyRequestMetric,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="managed_metric", value=request.managed_metric,marshal_func=marshal_UpdateInstancePolicyRequestMetricManagedMetric
            ),
            OneOfPossibility(param="cockpit_metric_name", value=request.cockpit_metric_name,marshal_func=None
            ),
        ]),
    )

    if request.operator is not None:
        output["operator"] = str(request.operator)
    else:
        output["operator"] = getattr(UpdateInstancePolicyRequestMetricOperator, "OPERATOR_UNKNOWN")

    if request.aggregate is not None:
        output["aggregate"] = str(request.aggregate)
    else:
        output["aggregate"] = getattr(UpdateInstancePolicyRequestMetricAggregate, "AGGREGATE_UNKNOWN")

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.sampling_range_min is not None:
        output["sampling_range_min"] = request.sampling_range_min
    else:
        output["sampling_range_min"] = None

    if request.threshold is not None:
        output["threshold"] = request.threshold
    else:
        output["threshold"] = None


    return output

def marshal_UpdateInstancePolicyRequest(
    request: UpdateInstancePolicyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="metric", value=request.metric,marshal_func=marshal_UpdateInstancePolicyRequestMetric
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.action is not None:
        output["action"] = str(request.action)
    else:
        output["action"] = None

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = None

    if request.value is not None:
        output["value"] = request.value
    else:
        output["value"] = None

    if request.priority is not None:
        output["priority"] = request.priority
    else:
        output["priority"] = None


    return output

def marshal_UpdateInstanceTemplateRequest(
    request: UpdateInstanceTemplateRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.commercial_type is not None:
        output["commercial_type"] = request.commercial_type
    else:
        output["commercial_type"] = None

    if request.image_id is not None:
        output["image_id"] = request.image_id
    else:
        output["image_id"] = None

    if request.volumes is not None:
        output["volumes"] = {
            key: marshal_VolumeInstanceTemplate(value, defaults)
            for key, value in request.volumes.items()
        }
    else:
        output["volumes"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.security_group_id is not None:
        output["security_group_id"] = request.security_group_id
    else:
        output["security_group_id"] = None

    if request.placement_group_id is not None:
        output["placement_group_id"] = request.placement_group_id
    else:
        output["placement_group_id"] = None

    if request.public_ips_v4_count is not None:
        output["public_ips_v4_count"] = request.public_ips_v4_count
    else:
        output["public_ips_v4_count"] = None

    if request.public_ips_v6_count is not None:
        output["public_ips_v6_count"] = request.public_ips_v6_count
    else:
        output["public_ips_v6_count"] = None

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.private_network_ids is not None:
        output["private_network_ids"] = request.private_network_ids
    else:
        output["private_network_ids"] = None

    if request.cloud_init is not None:
        output["cloud_init"] = request.cloud_init
    else:
        output["cloud_init"] = None


    return output
