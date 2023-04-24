# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    TimeSeries,
)


class CockpitStatus(str, Enum):
    UNKNOWN_STATUS = "unknown_status"
    CREATING = "creating"
    READY = "ready"
    DELETING = "deleting"
    UPDATING = "updating"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class GrafanaUserRole(str, Enum):
    UNKNOWN_ROLE = "unknown_role"
    EDITOR = "editor"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)


class ListGrafanaUsersRequestOrderBy(str, Enum):
    LOGIN_ASC = "login_asc"
    LOGIN_DESC = "login_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPlansRequestOrderBy(str, Enum):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListTokensRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class PlanName(str, Enum):
    UNKNOWN_NAME = "unknown_name"
    FREE = "free"
    PREMIUM = "premium"
    CUSTOM = "custom"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Cockpit:
    """
    Cockpit.
    """

    project_id: str
    """
    ID of the Project the Cockpit belongs to.
    """

    created_at: Optional[datetime]
    """
    Date and time of the Cockpit's creation.
    """

    updated_at: Optional[datetime]
    """
    Date and time of the Cockpit's last update.
    """

    endpoints: Optional[CockpitEndpoints]
    """
    Endpoints of the Cockpit.
    """

    status: CockpitStatus
    """
    Status of the Cockpit.
    """

    managed_alerts_enabled: bool
    """
    Specifies whether managed alerts are enabled or disabled.
    """

    plan: Optional[Plan]
    """
    Pricing plan information.
    """


@dataclass
class CockpitEndpoints:
    """
    Cockpit. endpoints.
    """

    metrics_url: str
    """
    URL for metrics.
    """

    logs_url: str
    """
    URL for logs.
    """

    alertmanager_url: str
    """
    URL for the alert manager.
    """

    grafana_url: str
    """
    URL for the Grafana dashboard.
    """


@dataclass
class CockpitMetrics:
    """
    Metrics for a given Cockpit.
    Cockpit metrics.
    """

    timeseries: List[TimeSeries]
    """
    Time series array.
    """


@dataclass
class ContactPoint:
    """
    Contact point.
    """

    email: Optional[ContactPointEmail]
    """
    Contact point configuration.
    
    One-of ('configuration'): at most one of 'email' could be set.
    """


@dataclass
class ContactPointEmail:
    to: str


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
    The Grafana user's password.
    """


@dataclass
class ListContactPointsResponse:
    """
    Response returned when listing contact points.
    List contact points response.
    """

    total_count: int
    """
    Count of all contact points created.
    """

    contact_points: List[ContactPoint]
    """
    Array of contact points.
    """

    has_additional_receivers: bool
    """
    Specifies whether the contact point has other receivers than the default receiver.
    """

    has_additional_contact_points: bool
    """
    Specifies whether there are unmanaged contact points.
    """


@dataclass
class ListGrafanaUsersResponse:
    """
    Response returned when listing Grafana users.
    List grafana users response.
    """

    total_count: int
    """
    Count of all Grafana users.
    """

    grafana_users: List[GrafanaUser]
    """
    Information on all Grafana users.
    """


@dataclass
class ListPlansResponse:
    """
    Response returned when listing all pricing plans.
    List plans response.
    """

    total_count: int
    """
    Count of all pricing plans.
    """

    plans: List[Plan]
    """
    Information on plans.
    """


@dataclass
class ListTokensResponse:
    """
    List tokens response.
    """

    total_count: int
    """
    Count of all tokens created.
    """

    tokens: List[Token]
    """
    List of all tokens created.
    """


@dataclass
class Plan:
    """
    Pricing plan.
    Plan.
    """

    id: str
    """
    ID of a given pricing plan.
    """

    name: PlanName
    """
    Name of a given pricing plan.
    """

    retention_metrics_interval: Optional[str]
    """
    Retention for metrics.
    """

    retention_logs_interval: Optional[str]
    """
    Retention for logs.
    """

    sample_ingestion_price: int
    """
    Ingestion price for 1 million samples in cents.
    """

    logs_ingestion_price: int
    """
    Ingestion price for 1 GB of logs in cents.
    """

    retention_price: int
    """
    Retention price in euros per month.
    """


@dataclass
class SelectPlanResponse:
    """
    Response returned when selecting a pricing plan.
    Select plan response.
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
    ID of the Project.
    """

    name: str
    """
    Name of the token.
    """

    created_at: Optional[datetime]
    """
    Date and time of the token's creation.
    """

    updated_at: Optional[datetime]
    """
    Date and time of the token's last update.
    """

    scopes: Optional[TokenScopes]
    """
    Token's permissions.
    """

    secret_key: Optional[str]
    """
    Token's secret key.
    """


@dataclass
class TokenScopes:
    """
    Token scopes.
    """

    query_metrics: bool
    """
    Permission to fetch metrics.
    """

    write_metrics: bool
    """
    Permission to write metrics.
    """

    setup_metrics_rules: bool
    """
    Permission to setup metrics rules.
    """

    query_logs: bool
    """
    Permission to fetch logs.
    """

    write_logs: bool
    """
    Permission to write logs.
    """

    setup_logs_rules: bool
    """
    Permission to setup logs rules.
    """

    setup_alerts: bool
    """
    Permission to setup alerts.
    """


@dataclass
class ActivateCockpitRequest:
    project_id: Optional[str]
    """
    ID of the Project the Cockpit belongs to.
    """


@dataclass
class GetCockpitRequest:
    project_id: Optional[str]
    """
    ID of the Project the Cockpit belongs to.
    """


@dataclass
class GetCockpitMetricsRequest:
    project_id: Optional[str]
    """
    ID of the Project the Cockpit belongs to.
    """

    start_date: Optional[datetime]
    """
    Desired time range's start date for the metrics.
    """

    end_date: Optional[datetime]
    """
    Desired time range's end date for the metrics.
    """

    metric_name: Optional[str]
    """
    Name of the metric requested.
    """


@dataclass
class DeactivateCockpitRequest:
    project_id: Optional[str]
    """
    ID of the Project the Cockpit belongs to.
    """


@dataclass
class ResetCockpitGrafanaRequest:
    project_id: Optional[str]
    """
    ID of the Project the Cockpit belongs to.
    """


@dataclass
class CreateTokenRequest:
    project_id: Optional[str]
    """
    ID of the Project.
    """

    name: Optional[str]
    """
    Name of the token.
    """

    scopes: Optional[TokenScopes]
    """
    Token's permissions.
    """


@dataclass
class ListTokensRequest:
    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Page size.
    """

    order_by: Optional[ListTokensRequestOrderBy]

    project_id: Optional[str]
    """
    ID of the Project.
    """


@dataclass
class GetTokenRequest:
    token_id: str
    """
    ID of the token.
    """


@dataclass
class DeleteTokenRequest:
    token_id: str
    """
    ID of the token.
    """


@dataclass
class CreateContactPointRequest:
    project_id: Optional[str]
    """
    ID of the Project in which to create the contact point.
    """

    contact_point: Optional[ContactPoint]
    """
    Contact point to create.
    """


@dataclass
class ListContactPointsRequest:
    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Page size.
    """

    project_id: Optional[str]
    """
    ID of the Project from which to list the contact points.
    """


@dataclass
class DeleteContactPointRequest:
    project_id: Optional[str]
    """
    ID of the Project.
    """

    contact_point: Optional[ContactPoint]
    """
    Contact point to delete.
    """


@dataclass
class EnableManagedAlertsRequest:
    project_id: Optional[str]
    """
    ID of the Project.
    """


@dataclass
class DisableManagedAlertsRequest:
    project_id: Optional[str]
    """
    ID of the Project.
    """


@dataclass
class TriggerTestAlertRequest:
    project_id: Optional[str]


@dataclass
class CreateGrafanaUserRequest:
    project_id: Optional[str]
    """
    ID of the Project.
    """

    login: str
    """
    Username of the Grafana user.
    """

    role: GrafanaUserRole
    """
    Role assigned to the Grafana user.
    """


@dataclass
class ListGrafanaUsersRequest:
    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Page size.
    """

    order_by: Optional[ListGrafanaUsersRequestOrderBy]

    project_id: Optional[str]
    """
    ID of the Project.
    """


@dataclass
class DeleteGrafanaUserRequest:
    grafana_user_id: int
    """
    ID of the Grafana user.
    """

    project_id: Optional[str]
    """
    ID of the Project.
    """


@dataclass
class ResetGrafanaUserPasswordRequest:
    grafana_user_id: int
    """
    ID of the Grafana user.
    """

    project_id: Optional[str]
    """
    ID of the Project.
    """


@dataclass
class ListPlansRequest:
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
class SelectPlanRequest:
    project_id: Optional[str]
    """
    ID of the Project.
    """

    plan_id: str
    """
    ID of the pricing plan.
    """
