# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional


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


class ListTokensRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Cockpit:
    """
    Cockpit
    """

    project_id: str
    """
    Project ID
    """

    created_at: Optional[datetime]
    """
    Created at
    """

    updated_at: Optional[datetime]
    """
    Updated at
    """

    endpoints: Optional[CockpitEndpoints]
    """
    Endpoints
    """

    status: CockpitStatus
    """
    Status
    """

    managed_alerts_enabled: bool
    """
    Managed alerts enabled
    """


@dataclass
class CockpitEndpoints:
    """
    Cockpit. endpoints
    """

    metrics_url: str

    logs_url: str

    alertmanager_url: str

    grafana_url: str


@dataclass
class ContactPoint:
    """
    Alert contact point
    """

    email: Optional[ContactPointEmail]
    """
    Alert contact point configuration.
    
    One-of ('configuration'): at most one of 'email' could be set.
    """


@dataclass
class ContactPointEmail:
    to: str


@dataclass
class GrafanaUser:
    """
    Grafana user
    """

    id: int

    login: str

    role: GrafanaUserRole

    password: Optional[str]


@dataclass
class ListContactPointsResponse:
    """
    List contact points response
    """

    total_count: int
    """
    Total count of contact points
    """

    contact_points: List[ContactPoint]
    """
    Contact points array
    """

    has_additional_receivers: bool
    """
    Has receivers other than default
    """

    has_additional_contact_points: bool
    """
    Has unmanaged contact points
    """


@dataclass
class ListGrafanaUsersResponse:
    """
    List grafana users response
    """

    total_count: int

    grafana_users: List[GrafanaUser]


@dataclass
class ListTokensResponse:
    """
    List tokens response
    """

    total_count: int

    tokens: List[Token]


@dataclass
class Token:
    """
    Token
    """

    id: str

    project_id: str

    name: str

    created_at: Optional[datetime]

    updated_at: Optional[datetime]

    scopes: Optional[TokenScopes]

    secret_key: Optional[str]


@dataclass
class TokenScopes:
    """
    Token scopes
    """

    query_metrics: bool

    write_metrics: bool

    setup_metrics_rules: bool

    query_logs: bool

    write_logs: bool

    setup_logs_rules: bool

    setup_alerts: bool


@dataclass
class ActivateCockpitRequest:
    project_id: Optional[str]


@dataclass
class GetCockpitRequest:
    project_id: Optional[str]


@dataclass
class DeactivateCockpitRequest:
    project_id: Optional[str]


@dataclass
class ResetCockpitGrafanaRequest:
    project_id: Optional[str]


@dataclass
class CreateTokenRequest:
    project_id: Optional[str]

    name: str

    scopes: Optional[TokenScopes]


@dataclass
class ListTokensRequest:
    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListTokensRequestOrderBy]

    project_id: Optional[str]


@dataclass
class GetTokenRequest:
    token_id: str


@dataclass
class DeleteTokenRequest:
    token_id: str


@dataclass
class CreateContactPointRequest:
    project_id: Optional[str]
    """
    Project ID
    """

    contact_point: Optional[ContactPoint]
    """
    Contact point to create
    """


@dataclass
class ListContactPointsRequest:
    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    Page size
    """

    project_id: Optional[str]
    """
    Project ID
    """


@dataclass
class DeleteContactPointRequest:
    project_id: Optional[str]

    contact_point: Optional[ContactPoint]
    """
    Contact point to delete
    """


@dataclass
class EnableManagedAlertsRequest:
    project_id: Optional[str]


@dataclass
class DisableManagedAlertsRequest:
    project_id: Optional[str]


@dataclass
class TriggerTestAlertRequest:
    project_id: Optional[str]


@dataclass
class CreateGrafanaUserRequest:
    project_id: Optional[str]

    login: str

    role: GrafanaUserRole


@dataclass
class ListGrafanaUsersRequest:
    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListGrafanaUsersRequestOrderBy]

    project_id: Optional[str]


@dataclass
class DeleteGrafanaUserRequest:
    grafana_user_id: int

    project_id: Optional[str]


@dataclass
class ResetGrafanaUserPasswordRequest:
    grafana_user_id: int

    project_id: Optional[str]
