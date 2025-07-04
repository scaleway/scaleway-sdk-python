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
    AlertState,
    DataSourceOrigin,
    DataSourceType,
    GrafanaUserRole,
    ListDataSourcesRequestOrderBy,
    ListGrafanaUsersRequestOrderBy,
    ListPlansRequestOrderBy,
    ListTokensRequestOrderBy,
    PlanName,
    TokenScope,
    UsageUnit,
    ContactPointEmail,
    ContactPoint,
    DataSource,
    GrafanaProductDashboard,
    GrafanaUser,
    Plan,
    Token,
    AlertManager,
    DisableAlertRulesResponse,
    EnableAlertRulesResponse,
    GetConfigResponseRetention,
    GetConfigResponse,
    Grafana,
    PreconfiguredAlertData,
    Alert,
    ListAlertsResponse,
    ListContactPointsResponse,
    ListDataSourcesResponse,
    ListGrafanaProductDashboardsResponse,
    ListGrafanaUsersResponse,
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
    RegionalApiDisableAlertRulesRequest,
    RegionalApiDisableManagedAlertsRequest,
    RegionalApiEnableAlertManagerRequest,
    RegionalApiEnableAlertRulesRequest,
    RegionalApiEnableManagedAlertsRequest,
    RegionalApiTriggerTestAlertRequest,
    RegionalApiUpdateContactPointRequest,
    RegionalApiUpdateDataSourceRequest,
)

def unmarshal_ContactPointEmail(data: Any) -> ContactPointEmail:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactPointEmail' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("to", str())
    args["to"] = field

    return ContactPointEmail(**args)

def unmarshal_ContactPoint(data: Any) -> ContactPoint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactPoint' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("region", )
    args["region"] = field

    field = data.get("send_resolved_notifications", False)
    args["send_resolved_notifications"] = field

    field = data.get("email", None)
    args["email"] = unmarshal_ContactPointEmail(field) if field is not None else None

    return ContactPoint(**args)

def unmarshal_DataSource(data: Any) -> DataSource:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DataSource' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("url", str())
    args["url"] = field

    field = data.get("type", getattr(DataSourceType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("origin", getattr(DataSourceOrigin, "UNKNOWN_ORIGIN"))
    args["origin"] = field

    field = data.get("synchronized_with_grafana", False)
    args["synchronized_with_grafana"] = field

    field = data.get("retention_days", 0)
    args["retention_days"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return DataSource(**args)

def unmarshal_GrafanaProductDashboard(data: Any) -> GrafanaProductDashboard:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GrafanaProductDashboard' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("title", str())
    args["title"] = field

    field = data.get("url", str())
    args["url"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("variables", [])
    args["variables"] = field

    return GrafanaProductDashboard(**args)

def unmarshal_GrafanaUser(data: Any) -> GrafanaUser:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GrafanaUser' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("login", str())
    args["login"] = field

    field = data.get("role", getattr(GrafanaUserRole, "UNKNOWN_ROLE"))
    args["role"] = field

    field = data.get("password", None)
    args["password"] = field

    return GrafanaUser(**args)

def unmarshal_Plan(data: Any) -> Plan:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Plan' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", getattr(PlanName, "UNKNOWN_NAME"))
    args["name"] = field

    field = data.get("sample_ingestion_price", 0)
    args["sample_ingestion_price"] = field

    field = data.get("logs_ingestion_price", 0)
    args["logs_ingestion_price"] = field

    field = data.get("traces_ingestion_price", 0)
    args["traces_ingestion_price"] = field

    field = data.get("monthly_price", 0)
    args["monthly_price"] = field

    field = data.get("retention_metrics_interval", None)
    args["retention_metrics_interval"] = field

    field = data.get("retention_logs_interval", None)
    args["retention_logs_interval"] = field

    field = data.get("retention_traces_interval", None)
    args["retention_traces_interval"] = field

    return Plan(**args)

def unmarshal_Token(data: Any) -> Token:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Token' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("scopes", [])
    args["scopes"] = [TokenScope(v) for v in field] if field is not None else None

    field = data.get("region", )
    args["region"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("secret_key", None)
    args["secret_key"] = field

    return Token(**args)

def unmarshal_AlertManager(data: Any) -> AlertManager:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AlertManager' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("alert_manager_enabled", False)
    args["alert_manager_enabled"] = field

    field = data.get("managed_alerts_enabled", False)
    args["managed_alerts_enabled"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("alert_manager_url", None)
    args["alert_manager_url"] = field

    return AlertManager(**args)

def unmarshal_DisableAlertRulesResponse(data: Any) -> DisableAlertRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DisableAlertRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("disabled_rule_ids", [])
    args["disabled_rule_ids"] = field

    return DisableAlertRulesResponse(**args)

def unmarshal_EnableAlertRulesResponse(data: Any) -> EnableAlertRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EnableAlertRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("enabled_rule_ids", [])
    args["enabled_rule_ids"] = field

    return EnableAlertRulesResponse(**args)

def unmarshal_GetConfigResponseRetention(data: Any) -> GetConfigResponseRetention:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetConfigResponseRetention' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("min_days", str())
    args["min_days"] = field

    field = data.get("max_days", str())
    args["max_days"] = field

    field = data.get("default_days", str())
    args["default_days"] = field

    return GetConfigResponseRetention(**args)

def unmarshal_GetConfigResponse(data: Any) -> GetConfigResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetConfigResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("custom_metrics_retention", None)
    args["custom_metrics_retention"] = unmarshal_GetConfigResponseRetention(field) if field is not None else None

    field = data.get("custom_logs_retention", None)
    args["custom_logs_retention"] = unmarshal_GetConfigResponseRetention(field) if field is not None else None

    field = data.get("custom_traces_retention", None)
    args["custom_traces_retention"] = unmarshal_GetConfigResponseRetention(field) if field is not None else None

    field = data.get("product_metrics_retention", None)
    args["product_metrics_retention"] = unmarshal_GetConfigResponseRetention(field) if field is not None else None

    field = data.get("product_logs_retention", None)
    args["product_logs_retention"] = unmarshal_GetConfigResponseRetention(field) if field is not None else None

    return GetConfigResponse(**args)

def unmarshal_Grafana(data: Any) -> Grafana:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Grafana' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("grafana_url", str())
    args["grafana_url"] = field

    return Grafana(**args)

def unmarshal_PreconfiguredAlertData(data: Any) -> PreconfiguredAlertData:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PreconfiguredAlertData' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("preconfigured_rule_id", str())
    args["preconfigured_rule_id"] = field

    field = data.get("display_name", str())
    args["display_name"] = field

    field = data.get("display_description", str())
    args["display_description"] = field

    field = data.get("product_name", str())
    args["product_name"] = field

    field = data.get("product_family", str())
    args["product_family"] = field

    return PreconfiguredAlertData(**args)

def unmarshal_Alert(data: Any) -> Alert:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Alert' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("region", )
    args["region"] = field

    field = data.get("preconfigured", False)
    args["preconfigured"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("rule", str())
    args["rule"] = field

    field = data.get("duration", str())
    args["duration"] = field

    field = data.get("enabled", False)
    args["enabled"] = field

    field = data.get("annotations", {})
    args["annotations"] = field

    field = data.get("data_source_id", str())
    args["data_source_id"] = field

    field = data.get("state", None)
    args["state"] = field

    field = data.get("preconfigured_data", None)
    args["preconfigured_data"] = unmarshal_PreconfiguredAlertData(field) if field is not None else None

    return Alert(**args)

def unmarshal_ListAlertsResponse(data: Any) -> ListAlertsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListAlertsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("alerts", [])
    args["alerts"] = [unmarshal_Alert(v) for v in field] if field is not None else None

    return ListAlertsResponse(**args)

def unmarshal_ListContactPointsResponse(data: Any) -> ListContactPointsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListContactPointsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("contact_points", [])
    args["contact_points"] = [unmarshal_ContactPoint(v) for v in field] if field is not None else None

    field = data.get("has_additional_receivers", False)
    args["has_additional_receivers"] = field

    field = data.get("has_additional_contact_points", False)
    args["has_additional_contact_points"] = field

    return ListContactPointsResponse(**args)

def unmarshal_ListDataSourcesResponse(data: Any) -> ListDataSourcesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDataSourcesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("data_sources", [])
    args["data_sources"] = [unmarshal_DataSource(v) for v in field] if field is not None else None

    return ListDataSourcesResponse(**args)

def unmarshal_ListGrafanaProductDashboardsResponse(data: Any) -> ListGrafanaProductDashboardsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListGrafanaProductDashboardsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("dashboards", [])
    args["dashboards"] = [unmarshal_GrafanaProductDashboard(v) for v in field] if field is not None else None

    return ListGrafanaProductDashboardsResponse(**args)

def unmarshal_ListGrafanaUsersResponse(data: Any) -> ListGrafanaUsersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListGrafanaUsersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("grafana_users", [])
    args["grafana_users"] = [unmarshal_GrafanaUser(v) for v in field] if field is not None else None

    return ListGrafanaUsersResponse(**args)

def unmarshal_ListPlansResponse(data: Any) -> ListPlansResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPlansResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("plans", [])
    args["plans"] = [unmarshal_Plan(v) for v in field] if field is not None else None

    return ListPlansResponse(**args)

def unmarshal_ListTokensResponse(data: Any) -> ListTokensResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTokensResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("tokens", [])
    args["tokens"] = [unmarshal_Token(v) for v in field] if field is not None else None

    return ListTokensResponse(**args)

def unmarshal_Usage(data: Any) -> Usage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Usage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("data_source_origin", getattr(DataSourceOrigin, "UNKNOWN_ORIGIN"))
    args["data_source_origin"] = field

    field = data.get("data_source_type", getattr(DataSourceType, "UNKNOWN_TYPE"))
    args["data_source_type"] = field

    field = data.get("unit", getattr(UsageUnit, "UNKNOWN_UNIT"))
    args["unit"] = field

    field = data.get("quantity_over_interval", 0)
    args["quantity_over_interval"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("data_source_id", None)
    args["data_source_id"] = field

    field = data.get("interval", None)
    args["interval"] = field

    return Usage(**args)

def unmarshal_UsageOverview(data: Any) -> UsageOverview:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UsageOverview' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("scaleway_metrics_usage", None)
    args["scaleway_metrics_usage"] = unmarshal_Usage(field) if field is not None else None

    field = data.get("scaleway_logs_usage", None)
    args["scaleway_logs_usage"] = unmarshal_Usage(field) if field is not None else None

    field = data.get("external_metrics_usage", None)
    args["external_metrics_usage"] = unmarshal_Usage(field) if field is not None else None

    field = data.get("external_logs_usage", None)
    args["external_logs_usage"] = unmarshal_Usage(field) if field is not None else None

    field = data.get("external_traces_usage", None)
    args["external_traces_usage"] = unmarshal_Usage(field) if field is not None else None

    return UsageOverview(**args)

def marshal_GlobalApiCreateGrafanaUserRequest(
    request: GlobalApiCreateGrafanaUserRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.login is not None:
        output["login"] = request.login
    else:
        output["login"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.role is not None:
        output["role"] = str(request.role)
    else:
        output["role"] = None


    return output

def marshal_GlobalApiResetGrafanaUserPasswordRequest(
    request: GlobalApiResetGrafanaUserPasswordRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_GlobalApiSelectPlanRequest(
    request: GlobalApiSelectPlanRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.plan_name is not None:
        output["plan_name"] = str(request.plan_name)
    else:
        output["plan_name"] = None


    return output

def marshal_GlobalApiSyncGrafanaDataSourcesRequest(
    request: GlobalApiSyncGrafanaDataSourcesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_ContactPointEmail(
    request: ContactPointEmail,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.to is not None:
        output["to"] = request.to
    else:
        output["to"] = str()


    return output

def marshal_RegionalApiCreateContactPointRequest(
    request: RegionalApiCreateContactPointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="email", value=request.email,marshal_func=marshal_ContactPointEmail
            ),
        ]),
    )

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.send_resolved_notifications is not None:
        output["send_resolved_notifications"] = request.send_resolved_notifications
    else:
        output["send_resolved_notifications"] = None


    return output

def marshal_RegionalApiCreateDataSourceRequest(
    request: RegionalApiCreateDataSourceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = None

    if request.retention_days is not None:
        output["retention_days"] = request.retention_days
    else:
        output["retention_days"] = None


    return output

def marshal_RegionalApiCreateTokenRequest(
    request: RegionalApiCreateTokenRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.token_scopes is not None:
        output["token_scopes"] = [str(item) for item in request.token_scopes]
    else:
        output["token_scopes"] = None


    return output

def marshal_RegionalApiDeleteContactPointRequest(
    request: RegionalApiDeleteContactPointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="email", value=request.email,marshal_func=marshal_ContactPointEmail
            ),
        ]),
    )

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_RegionalApiDisableAlertManagerRequest(
    request: RegionalApiDisableAlertManagerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_RegionalApiDisableAlertRulesRequest(
    request: RegionalApiDisableAlertRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.rule_ids is not None:
        output["rule_ids"] = request.rule_ids
    else:
        output["rule_ids"] = None


    return output

def marshal_RegionalApiDisableManagedAlertsRequest(
    request: RegionalApiDisableManagedAlertsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_RegionalApiEnableAlertManagerRequest(
    request: RegionalApiEnableAlertManagerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_RegionalApiEnableAlertRulesRequest(
    request: RegionalApiEnableAlertRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.rule_ids is not None:
        output["rule_ids"] = request.rule_ids
    else:
        output["rule_ids"] = None


    return output

def marshal_RegionalApiEnableManagedAlertsRequest(
    request: RegionalApiEnableManagedAlertsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_RegionalApiTriggerTestAlertRequest(
    request: RegionalApiTriggerTestAlertRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_RegionalApiUpdateContactPointRequest(
    request: RegionalApiUpdateContactPointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="email", value=request.email,marshal_func=marshal_ContactPointEmail
            ),
        ]),
    )

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.send_resolved_notifications is not None:
        output["send_resolved_notifications"] = request.send_resolved_notifications
    else:
        output["send_resolved_notifications"] = None


    return output

def marshal_RegionalApiUpdateDataSourceRequest(
    request: RegionalApiUpdateDataSourceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.retention_days is not None:
        output["retention_days"] = request.retention_days
    else:
        output["retention_days"] = None


    return output
