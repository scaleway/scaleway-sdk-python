# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from dateutil import parser
from .types import (
    DatasourceType,
    GrafanaUserRole,
    Cockpit,
    CockpitEndpoints,
    CockpitMetrics,
    ContactPoint,
    ContactPointEmail,
    Datasource,
    GrafanaUser,
    ListContactPointsResponse,
    ListGrafanaUsersResponse,
    ListPlansResponse,
    ListTokensResponse,
    Plan,
    SelectPlanResponse,
    Token,
    TokenScopes,
    ActivateCockpitRequest,
    DeactivateCockpitRequest,
    ResetCockpitGrafanaRequest,
    CreateDatasourceRequest,
    CreateTokenRequest,
    CreateContactPointRequest,
    DeleteContactPointRequest,
    EnableManagedAlertsRequest,
    DisableManagedAlertsRequest,
    TriggerTestAlertRequest,
    CreateGrafanaUserRequest,
    DeleteGrafanaUserRequest,
    ResetGrafanaUserPasswordRequest,
    SelectPlanRequest,
)


def unmarshal_ContactPointEmail(data: Any) -> ContactPointEmail:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ContactPointEmail' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("to", None)
    args["to"] = field

    return ContactPointEmail(**args)


def unmarshal_TokenScopes(data: Any) -> TokenScopes:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'TokenScopes' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("query_logs", None)
    args["query_logs"] = field

    field = data.get("query_metrics", None)
    args["query_metrics"] = field

    field = data.get("query_traces", None)
    args["query_traces"] = field

    field = data.get("setup_alerts", None)
    args["setup_alerts"] = field

    field = data.get("setup_logs_rules", None)
    args["setup_logs_rules"] = field

    field = data.get("setup_metrics_rules", None)
    args["setup_metrics_rules"] = field

    field = data.get("write_logs", None)
    args["write_logs"] = field

    field = data.get("write_metrics", None)
    args["write_metrics"] = field

    field = data.get("write_traces", None)
    args["write_traces"] = field

    return TokenScopes(**args)


def unmarshal_CockpitEndpoints(data: Any) -> CockpitEndpoints:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CockpitEndpoints' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("alertmanager_url", None)
    args["alertmanager_url"] = field

    field = data.get("grafana_url", None)
    args["grafana_url"] = field

    field = data.get("logs_url", None)
    args["logs_url"] = field

    field = data.get("metrics_url", None)
    args["metrics_url"] = field

    return CockpitEndpoints(**args)


def unmarshal_ContactPoint(data: Any) -> ContactPoint:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ContactPoint' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("email", None)
    args["email"] = unmarshal_ContactPointEmail(field) if field is not None else None

    return ContactPoint(**args)


def unmarshal_GrafanaUser(data: Any) -> GrafanaUser:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GrafanaUser' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("login", None)
    args["login"] = field

    field = data.get("password", None)
    args["password"] = field

    field = data.get("role", None)
    args["role"] = field

    return GrafanaUser(**args)


def unmarshal_Plan(data: Any) -> Plan:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Plan' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("logs_ingestion_price", None)
    args["logs_ingestion_price"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("retention_logs_interval", None)
    args["retention_logs_interval"] = field

    field = data.get("retention_metrics_interval", None)
    args["retention_metrics_interval"] = field

    field = data.get("retention_price", None)
    args["retention_price"] = field

    field = data.get("sample_ingestion_price", None)
    args["sample_ingestion_price"] = field

    return Plan(**args)


def unmarshal_Token(data: Any) -> Token:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Token' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("scopes", None)
    args["scopes"] = unmarshal_TokenScopes(field) if field is not None else None

    field = data.get("secret_key", None)
    args["secret_key"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return Token(**args)


def unmarshal_Cockpit(data: Any) -> Cockpit:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Cockpit' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("endpoints", None)
    args["endpoints"] = unmarshal_CockpitEndpoints(field) if field is not None else None

    field = data.get("managed_alerts_enabled", None)
    args["managed_alerts_enabled"] = field

    field = data.get("plan", None)
    args["plan"] = unmarshal_Plan(field) if field is not None else None

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return Cockpit(**args)


def unmarshal_CockpitMetrics(data: Any) -> CockpitMetrics:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CockpitMetrics' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("timeseries", None)
    args["timeseries"] = (
        [unmarshal_TimeSeries(v) for v in field] if field is not None else None
    )

    return CockpitMetrics(**args)


def unmarshal_Datasource(data: Any) -> Datasource:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Datasource' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("type", None)
    args["type_"] = field

    field = data.get("url", None)
    args["url"] = field

    return Datasource(**args)


def unmarshal_ListContactPointsResponse(data: Any) -> ListContactPointsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListContactPointsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("contact_points", None)
    args["contact_points"] = (
        [unmarshal_ContactPoint(v) for v in field] if field is not None else None
    )

    field = data.get("has_additional_contact_points", None)
    args["has_additional_contact_points"] = field

    field = data.get("has_additional_receivers", None)
    args["has_additional_receivers"] = field

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListContactPointsResponse(**args)


def unmarshal_ListGrafanaUsersResponse(data: Any) -> ListGrafanaUsersResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListGrafanaUsersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("grafana_users", None)
    args["grafana_users"] = (
        [unmarshal_GrafanaUser(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListGrafanaUsersResponse(**args)


def unmarshal_ListPlansResponse(data: Any) -> ListPlansResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListPlansResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("plans", None)
    args["plans"] = [unmarshal_Plan(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListPlansResponse(**args)


def unmarshal_ListTokensResponse(data: Any) -> ListTokensResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListTokensResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("tokens", None)
    args["tokens"] = [unmarshal_Token(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListTokensResponse(**args)


def unmarshal_SelectPlanResponse(data: Any) -> SelectPlanResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SelectPlanResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return SelectPlanResponse(**args)


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
                OneOfPossibility(
                    "email",
                    marshal_ContactPointEmail(request.email, defaults)
                    if request.email is not None
                    else None,
                ),
            ]
        ),
    )

    return output


def marshal_TokenScopes(
    request: TokenScopes,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.query_logs is not None:
        output["query_logs"] = request.query_logs

    if request.query_metrics is not None:
        output["query_metrics"] = request.query_metrics

    if request.query_traces is not None:
        output["query_traces"] = request.query_traces

    if request.setup_alerts is not None:
        output["setup_alerts"] = request.setup_alerts

    if request.setup_logs_rules is not None:
        output["setup_logs_rules"] = request.setup_logs_rules

    if request.setup_metrics_rules is not None:
        output["setup_metrics_rules"] = request.setup_metrics_rules

    if request.write_logs is not None:
        output["write_logs"] = request.write_logs

    if request.write_metrics is not None:
        output["write_metrics"] = request.write_metrics

    if request.write_traces is not None:
        output["write_traces"] = request.write_traces

    return output


def marshal_ActivateCockpitRequest(
    request: ActivateCockpitRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_CreateContactPointRequest(
    request: CreateContactPointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.contact_point is not None:
        output["contact_point"] = marshal_ContactPoint(request.contact_point, defaults)

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_CreateDatasourceRequest(
    request: CreateDatasourceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.type_ is not None:
        output["type"] = DatasourceType(request.type_)

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
        output["role"] = GrafanaUserRole(request.role)

    return output


def marshal_CreateTokenRequest(
    request: CreateTokenRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

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

    if request.contact_point is not None:
        output["contact_point"] = marshal_ContactPoint(request.contact_point, defaults)

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

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


def marshal_ResetCockpitGrafanaRequest(
    request: ResetCockpitGrafanaRequest,
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
