# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    ContactPointEmail,
    ContactPoint,
    Datasource,
    GrafanaProductDashboard,
    GrafanaUser,
    TokenScopes,
    Token,
    CockpitEndpoints,
    Plan,
    Cockpit,
    CockpitMetrics,
    ListContactPointsResponse,
    ListDatasourcesResponse,
    ListGrafanaProductDashboardsResponse,
    ListGrafanaUsersResponse,
    ListPlansResponse,
    ListTokensResponse,
    SelectPlanResponse,
    ActivateCockpitRequest,
    CreateContactPointRequest,
    CreateDatasourceRequest,
    CreateGrafanaUserRequest,
    CreateTokenRequest,
    DeactivateCockpitRequest,
    DeleteContactPointRequest,
    DeleteGrafanaUserRequest,
    DisableManagedAlertsRequest,
    EnableManagedAlertsRequest,
    ResetGrafanaUserPasswordRequest,
    SelectPlanRequest,
    TriggerTestAlertRequest,
)


def unmarshal_ContactPointEmail(data: Any) -> ContactPointEmail:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactPointEmail' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("to", None)
    if field is not None:
        args["to"] = field

    return ContactPointEmail(**args)


def unmarshal_ContactPoint(data: Any) -> ContactPoint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactPoint' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("email", None)
    if field is not None:
        args["email"] = unmarshal_ContactPointEmail(field)
    else:
        args["email"] = None

    return ContactPoint(**args)


def unmarshal_Datasource(data: Any) -> Datasource:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Datasource' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("url", None)
    if field is not None:
        args["url"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("is_managed_by_scaleway", None)
    if field is not None:
        args["is_managed_by_scaleway"] = field

    return Datasource(**args)


def unmarshal_GrafanaProductDashboard(data: Any) -> GrafanaProductDashboard:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GrafanaProductDashboard' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dashboard_name", None)
    if field is not None:
        args["dashboard_name"] = field

    field = data.get("title", None)
    if field is not None:
        args["title"] = field

    field = data.get("url", None)
    if field is not None:
        args["url"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("variables", None)
    if field is not None:
        args["variables"] = field

    return GrafanaProductDashboard(**args)


def unmarshal_GrafanaUser(data: Any) -> GrafanaUser:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GrafanaUser' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("login", None)
    if field is not None:
        args["login"] = field

    field = data.get("role", None)
    if field is not None:
        args["role"] = field

    field = data.get("password", None)
    if field is not None:
        args["password"] = field
    else:
        args["password"] = None

    return GrafanaUser(**args)


def unmarshal_TokenScopes(data: Any) -> TokenScopes:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TokenScopes' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("query_metrics", None)
    if field is not None:
        args["query_metrics"] = field

    field = data.get("write_metrics", None)
    if field is not None:
        args["write_metrics"] = field

    field = data.get("setup_metrics_rules", None)
    if field is not None:
        args["setup_metrics_rules"] = field

    field = data.get("query_logs", None)
    if field is not None:
        args["query_logs"] = field

    field = data.get("write_logs", None)
    if field is not None:
        args["write_logs"] = field

    field = data.get("setup_logs_rules", None)
    if field is not None:
        args["setup_logs_rules"] = field

    field = data.get("setup_alerts", None)
    if field is not None:
        args["setup_alerts"] = field

    field = data.get("query_traces", None)
    if field is not None:
        args["query_traces"] = field

    field = data.get("write_traces", None)
    if field is not None:
        args["write_traces"] = field

    return TokenScopes(**args)


def unmarshal_Token(data: Any) -> Token:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Token' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

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

    field = data.get("scopes", None)
    if field is not None:
        args["scopes"] = unmarshal_TokenScopes(field)
    else:
        args["scopes"] = None

    field = data.get("secret_key", None)
    if field is not None:
        args["secret_key"] = field
    else:
        args["secret_key"] = None

    return Token(**args)


def unmarshal_CockpitEndpoints(data: Any) -> CockpitEndpoints:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CockpitEndpoints' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("metrics_url", None)
    if field is not None:
        args["metrics_url"] = field

    field = data.get("logs_url", None)
    if field is not None:
        args["logs_url"] = field

    field = data.get("traces_url", None)
    if field is not None:
        args["traces_url"] = field

    field = data.get("alertmanager_url", None)
    if field is not None:
        args["alertmanager_url"] = field

    field = data.get("grafana_url", None)
    if field is not None:
        args["grafana_url"] = field

    return CockpitEndpoints(**args)


def unmarshal_Plan(data: Any) -> Plan:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Plan' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("sample_ingestion_price", None)
    if field is not None:
        args["sample_ingestion_price"] = field

    field = data.get("logs_ingestion_price", None)
    if field is not None:
        args["logs_ingestion_price"] = field

    field = data.get("traces_ingestion_price", None)
    if field is not None:
        args["traces_ingestion_price"] = field

    field = data.get("retention_price", None)
    if field is not None:
        args["retention_price"] = field

    field = data.get("retention_metrics_interval", None)
    if field is not None:
        args["retention_metrics_interval"] = field
    else:
        args["retention_metrics_interval"] = None

    field = data.get("retention_logs_interval", None)
    if field is not None:
        args["retention_logs_interval"] = field
    else:
        args["retention_logs_interval"] = None

    field = data.get("retention_traces_interval", None)
    if field is not None:
        args["retention_traces_interval"] = field
    else:
        args["retention_traces_interval"] = None

    return Plan(**args)


def unmarshal_Cockpit(data: Any) -> Cockpit:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Cockpit' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("managed_alerts_enabled", None)
    if field is not None:
        args["managed_alerts_enabled"] = field

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

    field = data.get("endpoints", None)
    if field is not None:
        args["endpoints"] = unmarshal_CockpitEndpoints(field)
    else:
        args["endpoints"] = None

    field = data.get("plan", None)
    if field is not None:
        args["plan"] = unmarshal_Plan(field)
    else:
        args["plan"] = None

    return Cockpit(**args)


def unmarshal_CockpitMetrics(data: Any) -> CockpitMetrics:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CockpitMetrics' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("timeseries", None)
    if field is not None:
        args["timeseries"] = (
            [unmarshal_TimeSeries(v) for v in field] if field is not None else None
        )

    return CockpitMetrics(**args)


def unmarshal_ListContactPointsResponse(data: Any) -> ListContactPointsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListContactPointsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("contact_points", None)
    if field is not None:
        args["contact_points"] = (
            [unmarshal_ContactPoint(v) for v in field] if field is not None else None
        )

    field = data.get("has_additional_receivers", None)
    if field is not None:
        args["has_additional_receivers"] = field

    field = data.get("has_additional_contact_points", None)
    if field is not None:
        args["has_additional_contact_points"] = field

    return ListContactPointsResponse(**args)


def unmarshal_ListDatasourcesResponse(data: Any) -> ListDatasourcesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatasourcesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("datasources", None)
    if field is not None:
        args["datasources"] = (
            [unmarshal_Datasource(v) for v in field] if field is not None else None
        )

    return ListDatasourcesResponse(**args)


def unmarshal_ListGrafanaProductDashboardsResponse(
    data: Any,
) -> ListGrafanaProductDashboardsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListGrafanaProductDashboardsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("dashboards", None)
    if field is not None:
        args["dashboards"] = (
            [unmarshal_GrafanaProductDashboard(v) for v in field]
            if field is not None
            else None
        )

    return ListGrafanaProductDashboardsResponse(**args)


def unmarshal_ListGrafanaUsersResponse(data: Any) -> ListGrafanaUsersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListGrafanaUsersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("grafana_users", None)
    if field is not None:
        args["grafana_users"] = (
            [unmarshal_GrafanaUser(v) for v in field] if field is not None else None
        )

    return ListGrafanaUsersResponse(**args)


def unmarshal_ListPlansResponse(data: Any) -> ListPlansResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPlansResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("plans", None)
    if field is not None:
        args["plans"] = (
            [unmarshal_Plan(v) for v in field] if field is not None else None
        )

    return ListPlansResponse(**args)


def unmarshal_ListTokensResponse(data: Any) -> ListTokensResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTokensResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("tokens", None)
    if field is not None:
        args["tokens"] = (
            [unmarshal_Token(v) for v in field] if field is not None else None
        )

    return ListTokensResponse(**args)


def unmarshal_SelectPlanResponse(data: Any) -> SelectPlanResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SelectPlanResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return SelectPlanResponse(**args)


def marshal_ActivateCockpitRequest(
    request: ActivateCockpitRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_ContactPointEmail(
    request: ContactPointEmail,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.to is not None:
        output["to"] = request.to

    return output


def marshal_ContactPoint(
    request: ContactPoint,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("email", request.email),
            ]
        ),
    )

    return output


def marshal_CreateContactPointRequest(
    request: CreateContactPointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.contact_point is not None:
        output["contact_point"] = marshal_ContactPoint(request.contact_point, defaults)

    return output


def marshal_CreateDatasourceRequest(
    request: CreateDatasourceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.is_default is not None:
        output["is_default"] = request.is_default

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.type_ is not None:
        output["type"] = str(request.type_)

    return output


def marshal_CreateGrafanaUserRequest(
    request: CreateGrafanaUserRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.login is not None:
        output["login"] = request.login

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.role is not None:
        output["role"] = str(request.role)

    return output


def marshal_TokenScopes(
    request: TokenScopes,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.query_metrics is not None:
        output["query_metrics"] = request.query_metrics

    if request.write_metrics is not None:
        output["write_metrics"] = request.write_metrics

    if request.setup_metrics_rules is not None:
        output["setup_metrics_rules"] = request.setup_metrics_rules

    if request.query_logs is not None:
        output["query_logs"] = request.query_logs

    if request.write_logs is not None:
        output["write_logs"] = request.write_logs

    if request.setup_logs_rules is not None:
        output["setup_logs_rules"] = request.setup_logs_rules

    if request.setup_alerts is not None:
        output["setup_alerts"] = request.setup_alerts

    if request.query_traces is not None:
        output["query_traces"] = request.query_traces

    if request.write_traces is not None:
        output["write_traces"] = request.write_traces

    return output


def marshal_CreateTokenRequest(
    request: CreateTokenRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.name is not None:
        output["name"] = request.name

    if request.scopes is not None:
        output["scopes"] = marshal_TokenScopes(request.scopes, defaults)

    return output


def marshal_DeactivateCockpitRequest(
    request: DeactivateCockpitRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_DeleteContactPointRequest(
    request: DeleteContactPointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.contact_point is not None:
        output["contact_point"] = marshal_ContactPoint(request.contact_point, defaults)

    return output


def marshal_DeleteGrafanaUserRequest(
    request: DeleteGrafanaUserRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_DisableManagedAlertsRequest(
    request: DisableManagedAlertsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_EnableManagedAlertsRequest(
    request: EnableManagedAlertsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_ResetGrafanaUserPasswordRequest(
    request: ResetGrafanaUserPasswordRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_SelectPlanRequest(
    request: SelectPlanRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.plan_id is not None:
        output["plan_id"] = request.plan_id

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_TriggerTestAlertRequest(
    request: TriggerTestAlertRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output
