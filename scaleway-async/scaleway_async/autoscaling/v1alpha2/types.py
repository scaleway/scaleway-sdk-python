# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    Zone as ScwZone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class AlertAlertType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ALERT_TYPE = "unknown_alert_type"
    QUOTAS_EXCEEDED = "quotas_exceeded"
    OUT_OF_STOCK = "out_of_stock"
    INVALID_TEMPLATE = "invalid_template"
    TEMPLATE_NOT_FOUND = "template_not_found"
    INVALID_INSTANCE = "invalid_instance"
    TEMPLATE_PERMISSIONS_DENIED = "template_permissions_denied"
    LOAD_BALANCER_NOT_FOUND = "load_balancer_not_found"
    LOAD_BALANCER_PERMISSIONS_DENIED = "load_balancer_permissions_denied"
    BACKEND_NOT_FOUND = "backend_not_found"
    BACKEND_PERMISSIONS_DENIED = "backend_permissions_denied"

    def __str__(self) -> str:
        return str(self.value)


class GroupGroupStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_GROUP_STATUS = "unknown_group_status"
    ACTIVE = "active"
    SCALING_OUT = "scaling_out"
    SCALING_IN = "scaling_in"
    REFRESHING = "refreshing"
    HEALING = "healing"
    SCALING_FAILURE = "scaling_failure"
    DELETING = "deleting"

    def __str__(self) -> str:
        return str(self.value)


class GroupLoadBalancerConfigurationBackendAddressFamily(
    str, Enum, metaclass=StrEnumMeta
):
    UNKNOWN_ADDRESS_FAMILY = "unknown_address_family"
    IPV4 = "ipv4"
    IPV6 = "ipv6"

    def __str__(self) -> str:
        return str(self.value)


class GroupSummaryScalingPolicyTargetType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SCALING_POLICY_TARGET_TYPE = "unknown_scaling_policy_target_type"
    FIXED_SIZE = "fixed_size"
    CPU_TARGET = "cpu_target"
    MEMORY_TARGET = "memory_target"

    def __str__(self) -> str:
        return str(self.value)


class ListGroupsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class LogLogLevel(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_LOG_LEVEL = "unknown_log_level"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class LoadBalancerConfigurationSpecAutoHealing:
    enabled: Optional[bool] = False
    """
    Whether auto-healing is enabled.
    """

    grace_period: Optional[str] = None
    """
    Grace period for health checks.
    """


@dataclass
class LoadBalancerConfigurationSpecBackend:
    backend_id: str
    """
    ID of the load balancer backend.
    """

    address_family: GroupLoadBalancerConfigurationBackendAddressFamily
    """
    IP address family (IPv4 or IPv6).
    """

    private_network_id: Optional[str] = None
    """
    Optional private network ID.
    """


@dataclass
class GroupScalingPolicyScalingPolicyCpuTarget:
    target_avg_percent: int


@dataclass
class GroupScalingPolicyScalingPolicyFixedSize:
    size: int


@dataclass
class GroupScalingPolicyScalingPolicyMemoryTarget:
    target_avg_percent: int


@dataclass
class GroupLoadBalancerConfigurationAutoHealing:
    enabled: bool
    grace_period: Optional[str] = None


@dataclass
class GroupLoadBalancerConfigurationBackend:
    backend_id: str
    address_family: GroupLoadBalancerConfigurationBackendAddressFamily
    private_network_id: Optional[str] = None


@dataclass
class Alert:
    type_: AlertAlertType
    """
    Type of alert.
    """

    group_id: str
    """
    ID of the group.
    """

    failing_quotas: list[str]
    """
    List of quota names that are exceeded (for quotas_exceeded alerts).
    """

    opened_at: Optional[datetime] = None
    """
    Timestamp when the alert was opened.
    """

    closed_at: Optional[datetime] = None
    """
    Optional timestamp when the alert was closed.
    """


@dataclass
class LoadBalancerConfigurationSpec:
    backends: list[LoadBalancerConfigurationSpecBackend]
    """
    List of load balancer backend configurations.
    """

    load_balancer_id: Optional[str] = None
    """
    ID of the load balancer (set to empty to disable).
    """

    auto_healing: Optional[LoadBalancerConfigurationSpecAutoHealing] = None
    """
    Auto-healing configuration.
    """


@dataclass
class ScalingPolicySpec:
    minimum_size: Optional[int] = 0
    """
    Minimum number of instances in the group.
    """

    maximum_size: Optional[int] = 0
    """
    Maximum number of instances in the group.
    """

    scale_out_cooldown: Optional[str] = None
    """
    Cooldown period after a scale out event.
    """

    scale_in_cooldown: Optional[str] = None
    """
    Cooldown period after a scale in event.
    """

    scale_in_step: Optional[int] = 0
    """
    Number of instances to remove in a single scale in event.
    """

    scale_out_step: Optional[int] = 0
    """
    Number of instances to add in a single scale out event.
    """

    fixed_size: Optional[GroupScalingPolicyScalingPolicyFixedSize] = None

    cpu_target: Optional[GroupScalingPolicyScalingPolicyCpuTarget] = None

    memory_target: Optional[GroupScalingPolicyScalingPolicyMemoryTarget] = None


@dataclass
class GroupLoadBalancerConfiguration:
    load_balancer_id: str
    backends: list[GroupLoadBalancerConfigurationBackend]
    auto_healing: Optional[GroupLoadBalancerConfigurationAutoHealing] = None


@dataclass
class GroupScalingPolicy:
    minimum_size: int
    maximum_size: int
    scale_in_step: int
    scale_out_step: int
    scale_out_cooldown: Optional[str] = None
    scale_in_cooldown: Optional[str] = None
    fixed_size: Optional[GroupScalingPolicyScalingPolicyFixedSize] = None

    cpu_target: Optional[GroupScalingPolicyScalingPolicyCpuTarget] = None

    memory_target: Optional[GroupScalingPolicyScalingPolicyMemoryTarget] = None


@dataclass
class GroupSummary:
    project_id: str
    """
    Project ID owning this group.
    """

    id: str
    """
    Unique identifier of the autoscaling group.
    """

    name: str
    """
    Name of the autoscaling group.
    """

    tags: list[str]
    """
    Tags associated with the group.
    """

    status: GroupGroupStatus
    """
    Current status of the autoscaling group.
    """

    template_id: str
    """
    The Instance template ID used to create instances in this group.
    """

    current_size: int
    """
    Current number of instances in the group.
    """

    minimum_size: int
    """
    The minimum number of instances in the group.
    """

    maximum_size: int
    """
    The maximum number of instances in the group.
    """

    scaling_policy_target_type: GroupSummaryScalingPolicyTargetType
    """
    Defines which metric the group uses for scaling (cpu, memory, or fixed size).
    """

    zone: ScwZone
    """
    Availability zone of the group.
    """

    created_at: Optional[datetime] = None
    """
    Creation timestamp of the group.
    """

    updated_at: Optional[datetime] = None
    """
    Last update timestamp of the group.
    """

    load_balancer_id: Optional[str] = None
    """
    Optional load balancer ID.
    """

    latest_open_alert: Optional[Alert] = None
    """
    Most recent active alert if any.
    """


@dataclass
class Log:
    level: LogLogLevel
    """
    Log level (info, warning, error).
    """

    message: str
    """
    Log message content.
    """

    timestamp: Optional[datetime] = None
    """
    Timestamp of the log entry.
    """


@dataclass
class Server:
    server_id: str
    """
    ID of the instance server.
    """


@dataclass
class CreateGroupRequest:
    name: str
    """
    Name of the autoscaling group.
    """

    template_id: str
    """
    Template ID for instances in this group.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str] = None
    """
    Project ID to create the group in.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags associated with the group.
    """

    scaling_policy_spec: Optional[ScalingPolicySpec] = None
    """
    Scaling policy configuration.
    """

    load_balancer_configuration_spec: Optional[LoadBalancerConfigurationSpec] = None
    """
    Optional load balancer configuration.
    """


@dataclass
class DeleteGroupRequest:
    group_id: str
    """
    ID of the group to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetGroupRequest:
    group_id: str
    """
    ID of the group to get.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class Group:
    id: str
    """
    Unique identifier of the autoscaling group.
    """

    project_id: str
    """
    Project ID owning this group.
    """

    name: str
    """
    Name of the autoscaling group.
    """

    tags: list[str]
    """
    Tags associated with the group.
    """

    status: GroupGroupStatus
    """
    Current status of the autoscaling group.
    """

    open_alerts: list[Alert]
    """
    List of active alerts on the group.
    """

    current_size: int
    """
    Current number of instances in the group.
    """

    target_size: int
    """
    Target number of instances the group is scaling to.
    """

    template_id: str
    """
    The Instance template ID used to create instances in this group.
    """

    created_at: Optional[datetime] = None
    """
    Creation timestamp of the group.
    """

    updated_at: Optional[datetime] = None
    """
    Last update timestamp of the group.
    """

    last_scale_out_at: Optional[datetime] = None
    """
    Timestamp of the last scale out event.
    """

    last_scale_in_at: Optional[datetime] = None
    """
    Timestamp of the last scale in event.
    """

    scaling_policy: Optional[GroupScalingPolicy] = None
    """
    Scaling policy configuration.
    """

    load_balancer_configuration: Optional[GroupLoadBalancerConfiguration] = None
    """
    Optional load balancer configuration.
    """


@dataclass
class ListAlertsRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    page_size: Optional[int] = None
    group_id: Optional[str] = None

    project_id: Optional[str] = None


@dataclass
class ListAlertsResponse:
    alerts: list[Alert]
    """
    List of alerts.
    """

    total_count: int
    """
    Total number of alerts.
    """

    next_page_token: Optional[str] = None
    """
    Token for the next page of results.
    """


@dataclass
class ListGroupsRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListGroupsRequestOrderBy] = (
        ListGroupsRequestOrderBy.CREATED_AT_DESC
    )
    """
    Order criteria for listing groups.
    """

    page_size: Optional[int] = 0
    """
    Page size for pagination.
    """

    page_token: Optional[str] = None
    """
    Token for pagination.
    """

    project_id: Optional[str] = None
    """
    Project ID to filter groups.
    """

    template_id: Optional[str] = None
    """
    Template ID to filter groups.
    """

    load_balancer_id: Optional[str] = None
    """
    Load balancer ID to filter groups.
    """


@dataclass
class ListGroupsResponse:
    group_summaries: list[GroupSummary]
    """
    List of group summaries.
    """

    total_count: int
    """
    Total number of groups.
    """

    next_page_token: Optional[str] = None
    """
    Token for the next page of results.
    """


@dataclass
class ListLogsRequest:
    group_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    page_size: Optional[int] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None


@dataclass
class ListLogsResponse:
    logs: list[Log]
    """
    List of log entries.
    """

    total_count: int
    """
    Total number of logs.
    """

    next_page_token: Optional[str] = None
    """
    Token for the next page of results.
    """


@dataclass
class ListServersRequest:
    group_id: str
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page_token: Optional[str] = None
    page_size: Optional[int] = None


@dataclass
class ListServersResponse:
    servers: list[Server]
    """
    List of servers.
    """

    total_count: int
    """
    Total number of servers.
    """

    next_page_token: Optional[str] = None
    """
    Token for the next page of results.
    """


@dataclass
class UpdateGroupRequest:
    group_id: str
    """
    ID of the group to update.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    New name for the group.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    New tags for the group.
    """

    template_id: Optional[str] = None
    """
    New template ID for instances.
    """

    scaling_policy_spec: Optional[ScalingPolicySpec] = None
    """
    New scaling policy configuration.
    """

    load_balancer_configuration_spec: Optional[LoadBalancerConfigurationSpec] = None
    """
    New load balancer configuration.
    """
