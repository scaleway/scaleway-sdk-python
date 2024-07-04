# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    TokenScope,
    ContactPointEmail,
    ContactPoint,
    DataSource,
    GrafanaProductDashboard,
    GrafanaUser,
    Plan,
    Token,
    AlertManager,
    Grafana,
    ListContactPointsResponse,
    ListDataSourcesResponse,
    ListGrafanaProductDashboardsResponse,
    ListGrafanaUsersResponse,
    Alert,
    ListManagedAlertsResponse,
    ListPlansResponse,
    ListTokensResponse,
    Usage,
    UsageOverview,
    GlobalApiCreateGrafanaUserRequest,
    GlobalApiResetGrafanaUserPasswordRequest,
    GlobalApiSelectPlanRequest,
    GlobalApiSyncGrafanaDataSourcesRequest,
    RegionalApiCreateContactPointRequest,
    RegionalApiCreateDataSourceRequest,
    RegionalApiCreateTokenRequest,
    RegionalApiDeleteContactPointRequest,
    RegionalApiDisableAlertManagerRequest,
    RegionalApiDisableManagedAlertsRequest,
    RegionalApiEnableAlertManagerRequest,
    RegionalApiEnableManagedAlertsRequest,
    RegionalApiTriggerTestAlertRequest,
    RegionalApiUpdateDataSourceRequest,
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

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("email", None)
    if field is not None:
        args["email"] = unmarshal_ContactPointEmail(field)
    else:
        args["email"] = None

    return ContactPoint(**args)


def unmarshal_DataSource(data: Any) -> DataSource:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DataSource' failed as data isn't a dictionary."
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

    field = data.get("origin", None)
    if field is not None:
        args["origin"] = field

    field = data.get("synchronized_with_grafana", None)
    if field is not None:
        args["synchronized_with_grafana"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

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

    return DataSource(**args)


def unmarshal_GrafanaProductDashboard(data: Any) -> GrafanaProductDashboard:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GrafanaProductDashboard' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

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


def unmarshal_Plan(data: Any) -> Plan:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Plan' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

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

    field = data.get("monthly_price", None)
    if field is not None:
        args["monthly_price"] = field

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

    field = data.get("scopes", None)
    if field is not None:
        args["scopes"] = [TokenScope(v) for v in field] if field is not None else None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

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

    field = data.get("secret_key", None)
    if field is not None:
        args["secret_key"] = field
    else:
        args["secret_key"] = None

    return Token(**args)


def unmarshal_AlertManager(data: Any) -> AlertManager:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AlertManager' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("alert_manager_enabled", None)
    if field is not None:
        args["alert_manager_enabled"] = field

    field = data.get("managed_alerts_enabled", None)
    if field is not None:
        args["managed_alerts_enabled"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("alert_manager_url", None)
    if field is not None:
        args["alert_manager_url"] = field
    else:
        args["alert_manager_url"] = None

    return AlertManager(**args)


def unmarshal_Grafana(data: Any) -> Grafana:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Grafana' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("grafana_url", None)
    if field is not None:
        args["grafana_url"] = field

    return Grafana(**args)


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


def unmarshal_ListDataSourcesResponse(data: Any) -> ListDataSourcesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDataSourcesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("data_sources", None)
    if field is not None:
        args["data_sources"] = (
            [unmarshal_DataSource(v) for v in field] if field is not None else None
        )

    return ListDataSourcesResponse(**args)


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


def unmarshal_Alert(data: Any) -> Alert:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Alert' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("product_family", None)
    if field is not None:
        args["product_family"] = field

    field = data.get("product", None)
    if field is not None:
        args["product"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("rule", None)
    if field is not None:
        args["rule"] = field

    field = data.get("description", None)
    if field is not None:
        args["description"] = field

    return Alert(**args)


def unmarshal_ListManagedAlertsResponse(data: Any) -> ListManagedAlertsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListManagedAlertsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("alerts", None)
    if field is not None:
        args["alerts"] = (
            [unmarshal_Alert(v) for v in field] if field is not None else None
        )

    return ListManagedAlertsResponse(**args)


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


def unmarshal_Usage(data: Any) -> Usage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Usage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("data_source_origin", None)
    if field is not None:
        args["data_source_origin"] = field

    field = data.get("data_source_type", None)
    if field is not None:
        args["data_source_type"] = field

    field = data.get("unit", None)
    if field is not None:
        args["unit"] = field

    field = data.get("quantity_over_interval", None)
    if field is not None:
        args["quantity_over_interval"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("data_source_id", None)
    if field is not None:
        args["data_source_id"] = field
    else:
        args["data_source_id"] = None

    field = data.get("interval", None)
    if field is not None:
        args["interval"] = field
    else:
        args["interval"] = None

    return Usage(**args)


def unmarshal_UsageOverview(data: Any) -> UsageOverview:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UsageOverview' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("scaleway_metrics_usage", None)
    if field is not None:
        args["scaleway_metrics_usage"] = unmarshal_Usage(field)
    else:
        args["scaleway_metrics_usage"] = None

    field = data.get("scaleway_logs_usage", None)
    if field is not None:
        args["scaleway_logs_usage"] = unmarshal_Usage(field)
    else:
        args["scaleway_logs_usage"] = None

    field = data.get("external_metrics_usage", None)
    if field is not None:
        args["external_metrics_usage"] = unmarshal_Usage(field)
    else:
        args["external_metrics_usage"] = None

    field = data.get("external_logs_usage", None)
    if field is not None:
        args["external_logs_usage"] = unmarshal_Usage(field)
    else:
        args["external_logs_usage"] = None

    field = data.get("external_traces_usage", None)
    if field is not None:
        args["external_traces_usage"] = unmarshal_Usage(field)
    else:
        args["external_traces_usage"] = None

    return UsageOverview(**args)


def marshal_GlobalApiCreateGrafanaUserRequest(
    request: GlobalApiCreateGrafanaUserRequest,
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


def marshal_GlobalApiResetGrafanaUserPasswordRequest(
    request: GlobalApiResetGrafanaUserPasswordRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_GlobalApiSelectPlanRequest(
    request: GlobalApiSelectPlanRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.plan_name is not None:
        output["plan_name"] = str(request.plan_name)

    return output


def marshal_GlobalApiSyncGrafanaDataSourcesRequest(
    request: GlobalApiSyncGrafanaDataSourcesRequest,
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


def marshal_RegionalApiCreateContactPointRequest(
    request: RegionalApiCreateContactPointRequest,
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

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_RegionalApiCreateDataSourceRequest(
    request: RegionalApiCreateDataSourceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.type_ is not None:
        output["type"] = str(request.type_)

    return output


def marshal_RegionalApiCreateTokenRequest(
    request: RegionalApiCreateTokenRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.token_scopes is not None:
        output["token_scopes"] = [str(item) for item in request.token_scopes]

    return output


def marshal_RegionalApiDeleteContactPointRequest(
    request: RegionalApiDeleteContactPointRequest,
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

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_RegionalApiDisableAlertManagerRequest(
    request: RegionalApiDisableAlertManagerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_RegionalApiDisableManagedAlertsRequest(
    request: RegionalApiDisableManagedAlertsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_RegionalApiEnableAlertManagerRequest(
    request: RegionalApiEnableAlertManagerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_RegionalApiEnableManagedAlertsRequest(
    request: RegionalApiEnableManagedAlertsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_RegionalApiTriggerTestAlertRequest(
    request: RegionalApiTriggerTestAlertRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_RegionalApiUpdateDataSourceRequest(
    request: RegionalApiUpdateDataSourceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    return output
