# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class DataSourceOrigin(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ORIGIN = "unknown_origin"
    SCALEWAY = "scaleway"
    EXTERNAL = "external"

    def __str__(self) -> str:
        return str(self.value)


class DataSourceType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    METRICS = "metrics"
    LOGS = "logs"
    TRACES = "traces"
    ALERTS = "alerts"

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


class ListManagedAlertsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    TYPE_ASC = "type_asc"
    TYPE_DESC = "type_desc"

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
class ContactPointEmail:
    to: str


@dataclass
class ContactPoint:
    """
    Contact point.
    """

    region: Region
    """
    Region to target. If none is passed will use default region from the config.
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

    region: Region
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
class Alert:
    product_family: str

    product: str

    name: str

    rule: str

    description: str


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

    region: Region
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

    region: Region
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

    region: Region
    """
    Regions where the Alert manager is enabled.
    """

    alert_manager_url: Optional[str]
    """
    Alert manager URL.
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
class ListManagedAlertsResponse:
    """
    Response returned when listing data sources.
    """

    total_count: int
    """
    Total count of data sources matching the request.
    """

    alerts: List[Alert]
    """
    Alerts matching the request within the pagination.
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

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project to create the contact point in.
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

    region: Optional[Region]
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


@dataclass
class RegionalApiCreateTokenRequest:
    """
    Create a token.
    """

    name: str
    """
    Name of the token.
    """

    region: Optional[Region]
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

    region: Optional[Region]
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

    region: Optional[Region]
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

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RegionalApiDisableAlertManagerRequest:
    """
    Disable the Alert manager.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project to disable the Alert manager in.
    """


@dataclass
class RegionalApiDisableManagedAlertsRequest:
    """
    Disable the sending of managed alerts.
    """

    region: Optional[Region]
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

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project to enable the Alert manager in.
    """


@dataclass
class RegionalApiEnableManagedAlertsRequest:
    """
    Enable the sending of managed alerts.
    """

    region: Optional[Region]
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

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project ID of the requested Alert manager.
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

    region: Optional[Region]
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

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RegionalApiGetUsageOverviewRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]

    interval: Optional[str]


@dataclass
class RegionalApiListContactPointsRequest:
    """
    List contact points.
    """

    region: Optional[Region]
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

    region: Optional[Region]
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
class RegionalApiListManagedAlertsRequest:
    """
    Enable the sending of managed alerts.
    """

    region: Optional[Region]
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

    order_by: Optional[ListManagedAlertsRequestOrderBy]
    """
    Sort order for data sources in the response.
    """

    project_id: Optional[str]
    """
    Project ID to filter for, only data sources from this Project will be returned.
    """


@dataclass
class RegionalApiListTokensRequest:
    """
    List tokens.
    """

    region: Optional[Region]
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

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project.
    """


@dataclass
class RegionalApiUpdateDataSourceRequest:
    """
    Update a data source name.
    """

    data_source_id: str
    """
    ID of the data source to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Updated name of the data source.
    """


@dataclass
class UsageOverview:
    scaleway_metrics_usage: Optional[Usage]

    scaleway_logs_usage: Optional[Usage]

    external_metrics_usage: Optional[Usage]

    external_logs_usage: Optional[Usage]

    external_traces_usage: Optional[Usage]
