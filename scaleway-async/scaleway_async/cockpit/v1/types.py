# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

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


class AlertStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    ENABLED = "enabled"
    DISABLED = "disabled"
    ENABLING = "enabling"
    DISABLING = "disabling"

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


class ExporterStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    CREATING = "creating"
    READY = "ready"
    ERROR = "error"

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


class ListExportersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

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


class ListProductsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    DISPLAY_NAME_ASC = "display_name_asc"
    DISPLAY_NAME_DESC = "display_name_desc"
    FAMILY_NAME_ASC = "family_name_asc"
    FAMILY_NAME_DESC = "family_name_desc"

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
class ExporterDatadogDestination:
    api_key: Optional[str] = None
    endpoint: Optional[str] = None


@dataclass
class ExporterOTLPDestination:
    endpoint: str
    headers: dict[str, str]


@dataclass
class GetConfigResponseRetention:
    min_days: int
    max_days: int
    default_days: int


@dataclass
class RulesCount:
    data_source_id: str
    """
    ID of the data source.
    """

    data_source_name: str
    """
    Name of the data source.
    """

    rules_count: int
    """
    Total count of rules associated with this data source.
    """


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

    rule_status: AlertStatus
    """
    Indicates if the alert is enabled, enabling, disabled or disabling. Preconfigured alerts can have any of these values, whereas custom alerts can only have the status "enabled".
    """

    annotations: dict[str, str]
    """
    Annotations for the alert, used to provide additional information about the alert.
    """

    data_source_id: str
    """
    ID of the data source containing the alert rule.
    """

    state: Optional[AlertState] = AlertState.UNKNOWN_STATE
    """
    Current state of the alert. Possible states are `inactive`, `pending`, and `firing`.
    """

    preconfigured_data: Optional[PreconfiguredAlertData] = None
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

    email: Optional[ContactPointEmail] = None


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
    Duration for which the data will be retained in the data source.
    """

    region: ScwRegion
    """
    Region of the data source.
    """

    created_at: Optional[datetime] = None
    """
    Date the data source was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date the data source was last updated.
    """

    current_month_usage: Optional[int] = 0
    """
    Usage of the month in bytes.
    """


@dataclass
class Exporter:
    """
    Data exporter.
    """

    id: str
    """
    ID of the data export.
    """

    name: str
    """
    Name of the data export.
    """

    description: str
    """
    Description of the data export.
    """

    datasource_id: str
    """
    ID of the data source linked to the data export.
    """

    status: ExporterStatus
    """
    Status of the data export.
    """

    exported_products: list[str]
    """
    List of Scaleway products name exported by the data export.
    """

    created_at: Optional[datetime] = None
    """
    A timestamp of the creation date of the data export.
    """

    updated_at: Optional[datetime] = None
    """
    A timestamp of the last update date of the data export.
    """

    datadog_destination: Optional[ExporterDatadogDestination] = None

    otlp_destination: Optional[ExporterOTLPDestination] = None


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

    tags: list[str]
    """
    Dashboard tags.
    """

    variables: list[str]
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

    password: Optional[str] = None
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

    retention_metrics_interval: Optional[str] = None
    """
    Interval of time during which Scaleway's Cockpit keeps your metrics.
    """

    retention_logs_interval: Optional[str] = None
    """
    Interval of time during which Scaleway's Cockpit keeps your logs.
    """

    retention_traces_interval: Optional[str] = None
    """
    Interval of time during which Scaleway's Cockpit keeps your traces.
    """


@dataclass
class Product:
    name: str
    display_name: str
    family_name: str
    resource_types: list[str]


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

    scopes: list[TokenScope]
    """
    Token permission scopes.
    """

    region: ScwRegion
    """
    Regions where the token is located.
    """

    created_at: Optional[datetime] = None
    """
    Token creation date.
    """

    updated_at: Optional[datetime] = None
    """
    Token last modification date.
    """

    secret_key: Optional[str] = None
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

    data_source_id: Optional[str] = None
    """
    ID of the data source.
    """

    interval: Optional[str] = None
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

    alert_manager_url: Optional[str] = None
    """
    Alert manager URL.
    """


@dataclass
class DisableAlertRulesResponse:
    """
    Output returned when alert rules are disabled.
    """

    disabled_rule_ids: list[str]
    """
    Only newly disabled rules are listed. Rules that were already disabled are not returned in the output.
    """


@dataclass
class EnableAlertRulesResponse:
    """
    Output returned when alert rules are enabled.
    """

    enabled_rule_ids: list[str]
    """
    Only newly enabled rules are listed. Rules that were already enabled are not returned in the output.
    """


@dataclass
class GetConfigResponse:
    """
    Cockpit configuration.
    """

    custom_metrics_retention: Optional[GetConfigResponseRetention] = None
    """
    Custom metrics retention configuration.
    """

    custom_logs_retention: Optional[GetConfigResponseRetention] = None
    """
    Custom logs retention configuration.
    """

    custom_traces_retention: Optional[GetConfigResponseRetention] = None
    """
    Custom traces retention configuration.
    """

    product_metrics_retention: Optional[GetConfigResponseRetention] = None
    """
    Scaleway metrics retention configuration.
    """

    product_logs_retention: Optional[GetConfigResponseRetention] = None
    """
    Scaleway logs retention configuration.
    """


@dataclass
class GetRulesCountResponse:
    rules_count_by_datasource: list[RulesCount]
    """
    Total count of rules grouped by data source.
    """

    preconfigured_rules_count: int
    """
    Total count of preconfigured rules.
    """

    custom_rules_count: int
    """
    Total count of custom rules.
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

    project_id: Optional[str] = None
    """
    ID of the Project in which to create the Grafana user.
    """

    role: Optional[GrafanaUserRole] = GrafanaUserRole.UNKNOWN_ROLE
    """
    Role assigned to the Grafana user.
    """


@dataclass
class GlobalApiDeleteGrafanaUserRequest:
    """
    Delete a Grafana user.
    """

    grafana_user_id: int
    """
    ID of the Grafana user.
    """

    project_id: Optional[str] = None
    """
    ID of the Project to target.
    """


@dataclass
class GlobalApiGetCurrentPlanRequest:
    """
    Retrieve a pricing plan for the given Project.
    """

    project_id: Optional[str] = None
    """
    ID of the Project.
    """


@dataclass
class GlobalApiGetGrafanaProductDashboardRequest:
    """
    Retrieve a specific dashboard.
    """

    dashboard_name: str
    """
    Name of the dashboard.
    """

    project_id: Optional[str] = None
    """
    ID of the Project the dashboard belongs to.
    """


@dataclass
class GlobalApiGetGrafanaRequest:
    """
    Request a Grafana.
    """

    project_id: Optional[str] = None
    """
    ID of the Project.
    """


@dataclass
class GlobalApiListGrafanaProductDashboardsRequest:
    """
    Retrieve a list of available product dashboards.
    """

    project_id: Optional[str] = None
    """
    ID of the Project to target.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Page size.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to filter for.
    """


@dataclass
class GlobalApiListGrafanaUsersRequest:
    """
    List all Grafana users.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Page size.
    """

    order_by: Optional[ListGrafanaUsersRequestOrderBy] = (
        ListGrafanaUsersRequestOrderBy.LOGIN_ASC
    )
    """
    Order of the Grafana users.
    """

    project_id: Optional[str] = None
    """
    ID of the Project to target.
    """


@dataclass
class GlobalApiListPlansRequest:
    """
    Retrieve a list of available pricing plans.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Page size.
    """

    order_by: Optional[ListPlansRequestOrderBy] = ListPlansRequestOrderBy.NAME_ASC


@dataclass
class GlobalApiResetGrafanaUserPasswordRequest:
    """
    Reset a Grafana user's password.
    """

    grafana_user_id: int
    """
    ID of the Grafana user.
    """

    project_id: Optional[str] = None
    """
    ID of the Project to target.
    """


@dataclass
class GlobalApiSelectPlanRequest:
    """
    Select a specific pricing plan.
    """

    project_id: Optional[str] = None
    """
    ID of the Project.
    """

    plan_name: Optional[PlanName] = PlanName.UNKNOWN_NAME
    """
    Name of the pricing plan.
    """


@dataclass
class GlobalApiSyncGrafanaDataSourcesRequest:
    """
    Trigger the synchronization of all data sources created in the relevant regions.
    """

    project_id: Optional[str] = None
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

    alerts: list[Alert]
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

    contact_points: list[ContactPoint]
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

    data_sources: list[DataSource]
    """
    Data sources matching the request within the pagination.
    """


@dataclass
class ListExportersResponse:
    """
    Response returned when listing data exports.
    """

    total_count: int
    """
    Total count of data exports matching the request.
    """

    exporters: list[Exporter]
    """
    Data exports matching the request within the pagination.
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

    dashboards: list[GrafanaProductDashboard]
    """
    Grafana dashboards information.
    """


@dataclass
class ListGrafanaUsersResponse:
    """
    Output returned when listing Grafana users.
    """

    total_count: int
    """
    Total count of Grafana users.
    """

    grafana_users: list[GrafanaUser]
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

    plans: list[Plan]
    """
    Plan types information.
    """


@dataclass
class ListProductsResponse:
    products_list: list[Product]
    total_count: int


@dataclass
class ListTokensResponse:
    """
    Response returned when listing tokens.
    """

    total_count: int
    """
    Total count of tokens matching the request.
    """

    tokens: list[Token]
    """
    Tokens matching the request within the pagination.
    """


@dataclass
class RegionalApiCreateContactPointRequest:
    """
    Create a contact point.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project to create the contact point in.
    """

    send_resolved_notifications: Optional[bool] = False
    """
    Send an email notification when an alert is marked as resolved.
    """

    email: Optional[ContactPointEmail] = None


@dataclass
class RegionalApiCreateDataSourceRequest:
    """
    Create a data source.
    """

    name: str
    """
    Data source name.
    """

    type_: DataSourceType
    """
    Data source type.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project the data source belongs to.
    """

    retention_days: Optional[int] = 0
    """
    Default values are 31 days for metrics, 7 days for logs and traces.
    """


@dataclass
class RegionalApiCreateExporterRequest:
    """
    Create a data export.
    """

    datasource_id: str
    """
    ID of the data source linked to the data export.
    """

    exported_products: list[str]
    """
    To include all products in your data export, you can use an array containing "all"
You can retrieve the complete list of product names using the `ListProducts` endpoint.
    """

    name: str
    """
    Name of the data export.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    description: Optional[str] = None
    """
    Description of the data export.
    """

    datadog_destination: Optional[ExporterDatadogDestination] = None

    otlp_destination: Optional[ExporterOTLPDestination] = None


@dataclass
class RegionalApiCreateTokenRequest:
    """
    Create a token.
    """

    name: str
    """
    Name of the token.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project the token belongs to.
    """

    token_scopes: Optional[list[TokenScope]] = field(default_factory=list)
    """
    Token permission scopes.
    """


@dataclass
class RegionalApiDeleteContactPointRequest:
    """
    Delete a contact point.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project containing the contact point to delete.
    """

    email: Optional[ContactPointEmail] = None


@dataclass
class RegionalApiDeleteDataSourceRequest:
    """
    Delete a data source.
    """

    data_source_id: str
    """
    ID of the data source to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RegionalApiDeleteExporterRequest:
    """
    Delete a data export.
    """

    exporter_id: str
    """
    ID of the data export to update.
    """

    region: Optional[ScwRegion] = None
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

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RegionalApiDisableAlertManagerRequest:
    """
    Disable the Alert manager.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project to disable the Alert manager in.
    """


@dataclass
class RegionalApiDisableAlertRulesRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project.
    """

    rule_ids: Optional[list[str]] = field(default_factory=list)
    """
    List of IDs of the rules to enable. If empty, disables all preconfigured rules.
    """


@dataclass
class RegionalApiDisableManagedAlertsRequest:
    """
    Disable the sending of managed alerts.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project.
    """


@dataclass
class RegionalApiEnableAlertManagerRequest:
    """
    Enable the Alert manager.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project to enable the Alert manager in.
    """


@dataclass
class RegionalApiEnableAlertRulesRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project.
    """

    rule_ids: Optional[list[str]] = field(default_factory=list)
    """
    List of IDs of the rules to enable. If empty, enables all preconfigured rules.
    """


@dataclass
class RegionalApiEnableManagedAlertsRequest:
    """
    Enable the sending of managed alerts.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project.
    """


@dataclass
class RegionalApiGetAlertManagerRequest:
    """
    Get the Alert manager.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    Project ID of the requested Alert manager.
    """


@dataclass
class RegionalApiGetConfigRequest:
    """
    Get Cockpit configuration.
    """

    region: Optional[ScwRegion] = None
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

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RegionalApiGetExporterRequest:
    """
    Retrieve a specific data export.
    """

    exporter_id: str
    """
    ID of the data export to retrieve.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RegionalApiGetRulesCountRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project to retrieve the rule count for.
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

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RegionalApiGetUsageOverviewRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    interval: Optional[str] = None


@dataclass
class RegionalApiListAlertsRequest:
    """
    Retrieve a list of alerts.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    Project ID to filter for, only alerts from this Project will be returned.
    """

    rule_status: Optional[AlertStatus] = AlertStatus.UNKNOWN_STATUS
    """
    Returns only alerts with the given activation status. If omitted, no alert filtering is applied. Other filters may still apply.
    """

    is_preconfigured: Optional[bool] = False
    """
    True returns only preconfigured alerts. False returns only custom alerts. If omitted, no filtering is applied on alert types. Other filters may still apply.
    """

    state: Optional[AlertState] = AlertState.UNKNOWN_STATE
    """
    Valid values to filter on are `inactive`, `pending` and `firing`. If omitted, no filtering is applied on alert states. Other filters may still apply.
    """

    data_source_id: Optional[str] = None
    """
    If omitted, only alerts from the default Scaleway metrics data source will be listed.
    """


@dataclass
class RegionalApiListContactPointsRequest:
    """
    List contact points.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project containing the contact points to list.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Total count of contact points to return per page.
    """


@dataclass
class RegionalApiListDataSourcesRequest:
    """
    List data sources.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    Project ID to filter for, only data sources from this Project will be returned.
    """

    origin: Optional[DataSourceOrigin] = DataSourceOrigin.UNKNOWN_ORIGIN
    """
    Origin to filter for, only data sources with matching origin will be returned. If omitted, all types will be returned.
    """

    types: Optional[list[DataSourceType]] = field(default_factory=list)
    """
    Types to filter for (metrics, logs, traces), only data sources with matching types will be returned. If omitted, all types will be returned.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of data sources to return per page.
    """

    order_by: Optional[ListDataSourcesRequestOrderBy] = (
        ListDataSourcesRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order for data sources in the response.
    """


@dataclass
class RegionalApiListExportersRequest:
    """
    List all data exports.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    Project ID to filter for. Only data exports from this Project will be returned.
    """

    datasource_id: Optional[str] = None
    """
    Data source ID to filter for. Only data exports linked to this data source will be returned.
    """

    page: Optional[int] = 0
    """
    Page number to return from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of data exports to return per page.
    """

    order_by: Optional[ListExportersRequestOrderBy] = (
        ListExportersRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order for data exports in the response.
    """


@dataclass
class RegionalApiListProductsRequest:
    """
    List all Scaleway products that send metrics and/or logs to Cockpit.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number to return from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of products to return per page.
    """

    order_by: Optional[ListProductsRequestOrderBy] = (
        ListProductsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order for products in the response.
    """


@dataclass
class RegionalApiListTokensRequest:
    """
    List tokens.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project the tokens belong to.
    """

    token_scopes: Optional[list[TokenScope]] = field(default_factory=list)
    """
    Token scopes to filter for.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of tokens to return per page.
    """

    order_by: Optional[ListTokensRequestOrderBy] = (
        ListTokensRequestOrderBy.CREATED_AT_ASC
    )
    """
    Order in which to return results.
    """


@dataclass
class RegionalApiTriggerTestAlertRequest:
    """
    Request to trigger a test alert.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project.
    """


@dataclass
class RegionalApiUpdateContactPointRequest:
    """
    Update a contact point.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project containing the contact point to update.
    """

    send_resolved_notifications: Optional[bool] = False
    """
    Enable or disable notifications when alert is resolved.
    """

    email: Optional[ContactPointEmail] = None


@dataclass
class RegionalApiUpdateDataSourceRequest:
    """
    Update a data source name.
    """

    data_source_id: str
    """
    ID of the data source to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Updated name of the data source.
    """

    retention_days: Optional[int] = 0
    """
    Duration for which the data will be retained in the data source.
    """


@dataclass
class RegionalApiUpdateExporterRequest:
    """
    Update an existing data export.
    """

    exporter_id: str
    """
    ID of the data export to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Updated name of the data export.
    """

    description: Optional[str] = None
    """
    Updated description of the data export.
    """

    exported_products: Optional[list[str]] = field(default_factory=list)
    """
    To include all products in your data export, you can use an array containing "all"
You can retrieve the complete list of product names using the `ListProducts` endpoint.
    """

    datadog_destination: Optional[ExporterDatadogDestination] = None

    otlp_destination: Optional[ExporterOTLPDestination] = None


@dataclass
class UsageOverview:
    scaleway_metrics_usage: Optional[Usage] = None
    scaleway_logs_usage: Optional[Usage] = None
    external_metrics_usage: Optional[Usage] = None
    external_logs_usage: Optional[Usage] = None
    external_traces_usage: Optional[Usage] = None
