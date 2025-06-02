# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class AlertState(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATE = "unknown_state"
    INACTIVE = "inactive"
    PENDING = "pending"
    FIRING = "firing"

    def __str__(self) -> str:
        return str(self.value)


class DataSourceOrigin(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ORIGIN = "unknown_origin"
    SCALEWAY = "scaleway"
    EXTERNAL = "external"
    CUSTOM = "custom"

    def __str__(self) -> str:
        return str(self.value)


class DataSourceType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    METRICS = "metrics"
    LOGS = "logs"
    TRACES = "traces"

    def __str__(self) -> str:
        return str(self.value)


class GrafanaUserRole(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ROLE = "unknown_role"
    EDITOR = "editor"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)


class ListDataSourcesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    TYPE_ASC = "type_asc"
    TYPE_DESC = "type_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListGrafanaUsersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    LOGIN_ASC = "login_asc"
    LOGIN_DESC = "login_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPlansRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListTokensRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class PlanName(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_NAME = "unknown_name"
    FREE = "free"
    PREMIUM = "premium"
    CUSTOM = "custom"

    def __str__(self) -> str:
        return str(self.value)


class TokenScope(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SCOPE = "unknown_scope"
    READ_ONLY_METRICS = "read_only_metrics"
    WRITE_ONLY_METRICS = "write_only_metrics"
    FULL_ACCESS_METRICS_RULES = "full_access_metrics_rules"
    READ_ONLY_LOGS = "read_only_logs"
    WRITE_ONLY_LOGS = "write_only_logs"
    FULL_ACCESS_LOGS_RULES = "full_access_logs_rules"
    FULL_ACCESS_ALERT_MANAGER = "full_access_alert_manager"
    READ_ONLY_TRACES = "read_only_traces"
    WRITE_ONLY_TRACES = "write_only_traces"

    def __str__(self) -> str:
        return str(self.value)


class UsageUnit(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_UNIT = "unknown_unit"
    BYTES = "bytes"
    SAMPLES = "samples"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class PreconfiguredAlertData:
    """
    Structure for additional data relative to preconfigured alerts.
    """

    preconfigured_rule_id: str
    """
    ID of the preconfigured rule if the alert is preconfigured.
    """

    display_name: str
    """
    Human readable name of the alert.
    """

    display_description: str
    """
    Human readable description of the alert.
    """

    product_name: str
    """
    Product associated with the alert.
    """

    product_family: str
    """
    Family of the product associated with the alert.
    """


@dataclass
class ContactPointEmail:
    to: str


@dataclass
class GetConfigResponseRetention:
    min_days: int

    max_days: int

    default_days: int


@dataclass
class Alert:
    """
    Structure representing an alert.
    """

    region: ScwRegion
    """
    The region in which the alert is defined.
    """

    preconfigured: bool
    """
    Indicates if the alert is preconfigured or custom.
    """

    name: str
    """
    Name of the alert.
    """

    rule: str
    """
    Rule defining the alert condition.
    """

    duration: str
    """
    Duration for which the alert must be active before firing. The format of this duration follows the prometheus duration format.
    """

    enabled: bool
    """
    Indicates if the alert is enabled or disabled. Only preconfigured alerts can be disabled.
    """

    annotations: Dict[str, str]
    """
    Annotations for the alert, used to provide additional information about the alert.
    """

    data_source_id: str
    """
    ID of the data source containing the alert rule.
    """

    state: Optional[AlertState]
    """
    Current state of the alert. Possible states are `inactive`, `pending`, and `firing`.
    """

    preconfigured_data: Optional[PreconfiguredAlertData]
    """
    Contains additional data for preconfigured alerts, such as the rule ID, display name, and description. Only present if the alert is preconfigured.
    """


@dataclass
class ContactPoint:
    """
    Contact point.
    """

    region: ScwRegion
    """
    Region.
    """

    send_resolved_notifications: bool
    """
    Send an email notification when an alert is marked as resolved.
    """

    email: Optional[ContactPointEmail]


@dataclass
class DataSource:
    """
    Data source.
    """

    id: str
    """
    ID of the data source.
    """

    project_id: str
    """
    ID of the Project the data source belongs to.
    """

    name: str
    """
    Data source name.
    """

    url: str
    """
    Data source URL.
    """

    type_: DataSourceType
    """
    Data source type.
    """

    origin: DataSourceOrigin
    """
    Data source origin.
    """

    synchronized_with_grafana: bool
    """
    Indicates whether the data source is synchronized with Grafana.
    """

    retention_days: int
    """
    BETA - Duration for which the data will be retained in the data source.
    """

    region: ScwRegion
    """
    Region of the data source.
    """

    created_at: Optional[datetime]
    """
    Date the data source was created.
    """

    updated_at: Optional[datetime]
    """
    Date the data source was last updated.
    """


@dataclass
class GrafanaProductDashboard:
    """
    Grafana dashboard.
    """

    name: str
    """
    Dashboard name.
    """

    title: str
    """
    Dashboard title.
    """

    url: str
    """
    Dashboard URL.
    """

    tags: List[str]
    """
    Dashboard tags.
    """

    variables: List[str]
    """
    Dashboard variables.
    """


@dataclass
class GrafanaUser:
    """
    Grafana user.
    """

    id: int
    """
    ID of the Grafana user.
    """

    login: str
    """
    Username of the Grafana user.
    """

    role: GrafanaUserRole
    """
    Role assigned to the Grafana user.
    """

    password: Optional[str]
    """
    Grafana user's password.
    """


@dataclass
class Plan:
    """
    Type of pricing plan.
    """

    name: PlanName
    """
    Name of a given pricing plan.
    """

    sample_ingestion_price: int
    """
    Ingestion price in cents for 1 million samples.
    """

    logs_ingestion_price: int
    """
    Ingestion price in cents for 1 GB of logs.
    """

    traces_ingestion_price: int
    """
    Ingestion price in cents for 1 GB of traces.
    """

    monthly_price: int
    """
    Retention price in euros per month.
    """

    retention_metrics_interval: Optional[str]
    """
    Interval of time during which Scaleway's Cockpit keeps your metrics.
    """

    retention_logs_interval: Optional[str]
    """
    Interval of time during which Scaleway's Cockpit keeps your logs.
    """

    retention_traces_interval: Optional[str]
    """
    Interval of time during which Scaleway's Cockpit keeps your traces.
    """


@dataclass
class Token:
    """
    Token.
    """

    id: str
    """
    ID of the token.
    """

    project_id: str
    """
    ID of the Project the token belongs to.
    """

    name: str
    """
    Name of the token.
    """

    scopes: List[TokenScope]
    """
    Token permission scopes.
    """

    region: ScwRegion
    """
    Regions where the token is located.
    """

    created_at: Optional[datetime]
    """
    Token creation date.
    """

    updated_at: Optional[datetime]
    """
    Token last modification date.
    """

    secret_key: Optional[str]
    """
    Token secret key.
    """


@dataclass
class Usage:
    """
    Data source usage.
    """

    project_id: str
    """
    ID of the Project the data source belongs to.
    """

    data_source_origin: DataSourceOrigin
    """
    Origin of the data source.
    """

    data_source_type: DataSourceType
    """
    Type of the data source.
    """

    unit: UsageUnit
    """
    Unit of the data source usage.
    """

    quantity_over_interval: int
    """
    Data source usage for the given interval.
    """

    region: ScwRegion
    """
    Region of the data source usage.
    """

    data_source_id: Optional[str]
    """
    ID of the data source.
    """

    interval: Optional[str]
    """
    Interval for the data source usage.
    """


@dataclass
class AlertManager:
    """
    Alert manager information.
    """

    alert_manager_enabled: bool
    """
    The Alert manager is enabled.
    """

    managed_alerts_enabled: bool
    """
    Managed alerts are enabled.
    """

    region: ScwRegion
    """
    Regions where the Alert manager is enabled.
    """

    alert_manager_url: Optional[str]
    """
    Alert manager URL.
    """


@dataclass
class DisableAlertRulesResponse:
    disabled_rule_ids: List[str]


@dataclass
class EnableAlertRulesResponse:
    enabled_rule_ids: List[str]


@dataclass
class GetConfigResponse:
    """
    Cockpit configuration.
    """

    custom_metrics_retention: Optional[GetConfigResponseRetention]
    """
    Custom metrics retention configuration.
    """

    custom_logs_retention: Optional[GetConfigResponseRetention]
    """
    Custom logs retention configuration.
    """

    custom_traces_retention: Optional[GetConfigResponseRetention]
    """
    Custom traces retention configuration.
    """

    product_metrics_retention: Optional[GetConfigResponseRetention]
    """
    Scaleway metrics retention configuration.
    """

    product_logs_retention: Optional[GetConfigResponseRetention]
    """
    Scaleway logs retention configuration.
    """


@dataclass
class GlobalApiCreateGrafanaUserRequest:
    """
    Create a Grafana user.
    """

    login: str
    """
    Username of the Grafana user. Note that the `admin` username is not available for creation.
    """

    project_id: Optional[str]
    """
    ID of the Project in which to create the Grafana user.
    """

    role: Optional[GrafanaUserRole]
    """
    Role assigned to the Grafana user.
    """


@dataclass
class GlobalApiDeleteGrafanaUserRequest:
    """
    Delete a Grafana user.
    """

    project_id: Optional[str]
    """
    ID of the Project to target.
    """

    grafana_user_id: int
    """
    ID of the Grafana user.
    """


@dataclass
class GlobalApiGetCurrentPlanRequest:
    """
    Retrieve a pricing plan for the given Project.
    """

    project_id: Optional[str]
    """
    ID of the Project.
    """


@dataclass
class GlobalApiGetGrafanaProductDashboardRequest:
    """
    Retrieve a specific dashboard.
    """

    project_id: Optional[str]
    """
    ID of the Project the dashboard belongs to.
    """

    dashboard_name: str
    """
    Name of the dashboard.
    """


@dataclass
class GlobalApiGetGrafanaRequest:
    """
    Request a Grafana.
    """

    project_id: Optional[str]
    """
    ID of the Project.
    """


@dataclass
class GlobalApiListGrafanaProductDashboardsRequest:
    """
    Retrieve a list of available product dashboards.
    """

    project_id: Optional[str]
    """
    ID of the Project to target.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Page size.
    """

    tags: Optional[List[str]]
    """
    Tags to filter for.
    """


@dataclass
class GlobalApiListGrafanaUsersRequest:
    """
    List all Grafana users.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Page size.
    """

    order_by: Optional[ListGrafanaUsersRequestOrderBy]
    """
    Order of the Grafana users.
    """

    project_id: Optional[str]
    """
    ID of the Project to target.
    """


@dataclass
class GlobalApiListPlansRequest:
    """
    Retrieve a list of available pricing plans.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Page size.
    """

    order_by: Optional[ListPlansRequestOrderBy]


@dataclass
class GlobalApiResetGrafanaUserPasswordRequest:
    """
    Reset a Grafana user's password.
    """

    project_id: Optional[str]
    """
    ID of the Project to target.
    """

    grafana_user_id: int
    """
    ID of the Grafana user.
    """


@dataclass
class GlobalApiSelectPlanRequest:
    """
    Select a specific pricing plan.
    """

    project_id: Optional[str]
    """
    ID of the Project.
    """

    plan_name: Optional[PlanName]
    """
    Name of the pricing plan.
    """


@dataclass
class GlobalApiSyncGrafanaDataSourcesRequest:
    """
    Trigger the synchronization of all data sources created in the relevant regions.
    """

    project_id: Optional[str]
    """
    ID of the Project to target.
    """


@dataclass
class Grafana:
    """
    Grafana user.
    """

    grafana_url: str
    """
    URL to access your Cockpit's Grafana.
    """


@dataclass
class ListAlertsResponse:
    """
    Retrieve a list of alerts matching the request.
    """

    total_count: int
    """
    Total count of alerts matching the request.
    """

    alerts: List[Alert]
    """
    List of alerts matching the applied filters.
    """


@dataclass
class ListContactPointsResponse:
    """
    Response returned when listing contact points.
    """

    total_count: int
    """
    Total count of contact points associated with the default receiver.
    """

    contact_points: List[ContactPoint]
    """
    List of contact points associated with the default receiver.
    """

    has_additional_receivers: bool
    """
    Indicates whether the Alert manager has other receivers than the default one.
    """

    has_additional_contact_points: bool
    """
    Indicates whether there are unmanaged contact points on the default receiver.
    """


@dataclass
class ListDataSourcesResponse:
    """
    Response returned when listing data sources.
    """

    total_count: int
    """
    Total count of data sources matching the request.
    """

    data_sources: List[DataSource]
    """
    Data sources matching the request within the pagination.
    """


@dataclass
class ListGrafanaProductDashboardsResponse:
    """
    Output returned when listing dashboards.
    """

    total_count: int
    """
    Total count of Grafana dashboards.
    """

    dashboards: List[GrafanaProductDashboard]
    """
    Grafana dashboards information.
    """


@dataclass
class ListGrafanaUsersResponse:
    """
    Ouptut returned when listing Grafana users.
    """

    total_count: int
    """
    Total count of Grafana users.
    """

    grafana_users: List[GrafanaUser]
    """
    Grafana users information.
    """


@dataclass
class ListPlansResponse:
    """
    Output returned when listing pricing plans.
    """

    total_count: int
    """
    Total count of available pricing plans.
    """

    plans: List[Plan]
    """
    Plan types information.
    """


@dataclass
class ListTokensResponse:
    """
    Response returned when listing tokens.
    """

    total_count: int
    """
    Total count of tokens matching the request.
    """

    tokens: List[Token]
    """
    Tokens matching the request within the pagination.
    """


@dataclass
class RegionalApiCreateContactPointRequest:
    """
    Create a contact point.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project to create the contact point in.
    """

    send_resolved_notifications: Optional[bool]
    """
    Send an email notification when an alert is marked as resolved.
    """

    email: Optional[ContactPointEmail]


@dataclass
class RegionalApiCreateDataSourceRequest:
    """
    Create a data source.
    """

    name: str
    """
    Data source name.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project the data source belongs to.
    """

    type_: Optional[DataSourceType]
    """
    Data source type.
    """

    retention_days: Optional[int]
    """
    Default values are 30 days for metrics, 7 days for logs and traces.
    """


@dataclass
class RegionalApiCreateTokenRequest:
    """
    Create a token.
    """

    name: str
    """
    Name of the token.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project the token belongs to.
    """

    token_scopes: Optional[List[TokenScope]]
    """
    Token permission scopes.
    """


@dataclass
class RegionalApiDeleteContactPointRequest:
    """
    Delete a contact point.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project containing the contact point to delete.
    """

    email: Optional[ContactPointEmail]


@dataclass
class RegionalApiDeleteDataSourceRequest:
    """
    Delete a data source.
    """

    data_source_id: str
    """
    ID of the data source to delete.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RegionalApiDeleteTokenRequest:
    """
    Delete a token.
    """

    token_id: str
    """
    ID of the token to delete.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RegionalApiDisableAlertManagerRequest:
    """
    Disable the Alert manager.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project to disable the Alert manager in.
    """


@dataclass
class RegionalApiDisableAlertRulesRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]

    rule_ids: Optional[List[str]]


@dataclass
class RegionalApiDisableManagedAlertsRequest:
    """
    Disable the sending of managed alerts.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project.
    """


@dataclass
class RegionalApiEnableAlertManagerRequest:
    """
    Enable the Alert manager.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project to enable the Alert manager in.
    """


@dataclass
class RegionalApiEnableAlertRulesRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]

    rule_ids: Optional[List[str]]


@dataclass
class RegionalApiEnableManagedAlertsRequest:
    """
    Enable the sending of managed alerts.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project.
    """


@dataclass
class RegionalApiGetAlertManagerRequest:
    """
    Get the Alert manager.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project ID of the requested Alert manager.
    """


@dataclass
class RegionalApiGetConfigRequest:
    """
    Get Cockpit configuration.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RegionalApiGetDataSourceRequest:
    """
    Retrieve a data source.
    """

    data_source_id: str
    """
    ID of the relevant data source.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RegionalApiGetTokenRequest:
    """
    Get a token.
    """

    token_id: str
    """
    Token ID.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RegionalApiGetUsageOverviewRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]

    interval: Optional[str]


@dataclass
class RegionalApiListAlertsRequest:
    """
    Retrieve a list of alerts.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project ID to filter for, only alerts from this Project will be returned.
    """

    is_enabled: Optional[bool]
    """
    True returns only enabled alerts. False returns only disabled alerts. If omitted, no alert filtering is applied. Other filters may still apply.
    """

    is_preconfigured: Optional[bool]
    """
    True returns only preconfigured alerts. False returns only custom alerts. If omitted, no filtering is applied on alert types. Other filters may still apply.
    """

    state: Optional[AlertState]
    """
    Valid values to filter on are `inactive`, `pending` and `firing`. If omitted, no filtering is applied on alert states. Other filters may still apply.
    """

    data_source_id: Optional[str]
    """
    If omitted, only alerts from the default Scaleway metrics data source will be listed.
    """


@dataclass
class RegionalApiListContactPointsRequest:
    """
    List contact points.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Total count of contact points to return per page.
    """

    project_id: Optional[str]
    """
    ID of the Project containing the contact points to list.
    """


@dataclass
class RegionalApiListDataSourcesRequest:
    """
    List data sources.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Number of data sources to return per page.
    """

    order_by: Optional[ListDataSourcesRequestOrderBy]
    """
    Sort order for data sources in the response.
    """

    project_id: Optional[str]
    """
    Project ID to filter for, only data sources from this Project will be returned.
    """

    origin: Optional[DataSourceOrigin]
    """
    Origin to filter for, only data sources with matching origin will be returned.
    """

    types: Optional[List[DataSourceType]]
    """
    Types to filter for, only data sources with matching types will be returned.
    """


@dataclass
class RegionalApiListTokensRequest:
    """
    List tokens.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Number of tokens to return per page.
    """

    order_by: Optional[ListTokensRequestOrderBy]
    """
    Order in which to return results.
    """

    project_id: Optional[str]
    """
    ID of the Project the tokens belong to.
    """

    token_scopes: Optional[List[TokenScope]]
    """
    Token scopes to filter for.
    """


@dataclass
class RegionalApiTriggerTestAlertRequest:
    """
    Request to trigger a test alert.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project.
    """


@dataclass
class RegionalApiUpdateContactPointRequest:
    """
    Update a contact point.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project containing the contact point to update.
    """

    send_resolved_notifications: Optional[bool]
    """
    Enable or disable notifications when alert is resolved.
    """

    email: Optional[ContactPointEmail]


@dataclass
class RegionalApiUpdateDataSourceRequest:
    """
    Update a data source name.
    """

    data_source_id: str
    """
    ID of the data source to update.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Updated name of the data source.
    """

    retention_days: Optional[int]
    """
    BETA - Duration for which the data will be retained in the data source.
    """


@dataclass
class UsageOverview:
    scaleway_metrics_usage: Optional[Usage]

    scaleway_logs_usage: Optional[Usage]

    external_metrics_usage: Optional[Usage]

    external_logs_usage: Optional[Usage]

    external_traces_usage: Optional[Usage]
