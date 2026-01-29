# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    AlertState,
    AlertStatus,
    DataSourceOrigin,
    DataSourceType,
    ExporterStatus,
    GrafanaUserRole,
    PlanName,
    TokenScope,
    UsageUnit,
    ContactPointEmail,
    ContactPoint,
    DataSource,
    ExporterDatadogDestination,
    ExporterOTLPDestination,
    Exporter,
    GrafanaProductDashboard,
    GrafanaUser,
    Plan,
    Token,
    AlertManager,
    DisableAlertRulesResponse,
    EnableAlertRulesResponse,
    GetConfigResponseRetention,
    GetConfigResponse,
    RulesCount,
    GetRulesCountResponse,
    Grafana,
    PreconfiguredAlertData,
    Alert,
    ListAlertsResponse,
    ListContactPointsResponse,
    ListDataSourcesResponse,
    ListExportersResponse,
    ListGrafanaProductDashboardsResponse,
    ListGrafanaUsersResponse,
    ListPlansResponse,
    Product,
    ListProductsResponse,
    ListTokensResponse,
    Usage,
    UsageOverview,
    GlobalApiCreateGrafanaUserRequest,
    GlobalApiResetGrafanaUserPasswordRequest,
    GlobalApiSelectPlanRequest,
    GlobalApiSyncGrafanaDataSourcesRequest,
    RegionalApiCreateContactPointRequest,
    RegionalApiCreateDataSourceRequest,
    RegionalApiCreateExporterRequest,
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
    RegionalApiUpdateExporterRequest,
)


def unmarshal_ContactPointEmail(data: Any) -> ContactPointEmail:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactPointEmail' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("to", None)
    if field is not None:
        args["to"] = field
    else:
        args["to"] = None

    return ContactPointEmail(**args)


def unmarshal_ContactPoint(data: Any) -> ContactPoint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactPoint' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("send_resolved_notifications", None)
    if field is not None:
        args["send_resolved_notifications"] = field
    else:
        args["send_resolved_notifications"] = False

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

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("url", None)
    if field is not None:
        args["url"] = field
    else:
        args["url"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = DataSourceType.UNKNOWN_TYPE

    field = data.get("origin", None)
    if field is not None:
        args["origin"] = field
    else:
        args["origin"] = DataSourceOrigin.UNKNOWN_ORIGIN

    field = data.get("synchronized_with_grafana", None)
    if field is not None:
        args["synchronized_with_grafana"] = field
    else:
        args["synchronized_with_grafana"] = False

    field = data.get("retention_days", None)
    if field is not None:
        args["retention_days"] = field
    else:
        args["retention_days"] = 0

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

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

    field = data.get("current_month_usage", None)
    if field is not None:
        args["current_month_usage"] = field
    else:
        args["current_month_usage"] = 0

    return DataSource(**args)


def unmarshal_ExporterDatadogDestination(data: Any) -> ExporterDatadogDestination:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ExporterDatadogDestination' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("api_key", None)
    if field is not None:
        args["api_key"] = field
    else:
        args["api_key"] = None

    field = data.get("endpoint", None)
    if field is not None:
        args["endpoint"] = field
    else:
        args["endpoint"] = None

    return ExporterDatadogDestination(**args)


def unmarshal_ExporterOTLPDestination(data: Any) -> ExporterOTLPDestination:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ExporterOTLPDestination' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("endpoint", None)
    if field is not None:
        args["endpoint"] = field
    else:
        args["endpoint"] = None

    field = data.get("headers", None)
    if field is not None:
        args["headers"] = field
    else:
        args["headers"] = None

    return ExporterOTLPDestination(**args)


def unmarshal_Exporter(data: Any) -> Exporter:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Exporter' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("datasource_id", None)
    if field is not None:
        args["datasource_id"] = field
    else:
        args["datasource_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = ExporterStatus.UNKNOWN_STATUS

    field = data.get("exported_products", None)
    if field is not None:
        args["exported_products"] = field
    else:
        args["exported_products"] = []

    field = data.get("datadog_destination", None)
    if field is not None:
        args["datadog_destination"] = unmarshal_ExporterDatadogDestination(field)
    else:
        args["datadog_destination"] = None

    field = data.get("otlp_destination", None)
    if field is not None:
        args["otlp_destination"] = unmarshal_ExporterOTLPDestination(field)
    else:
        args["otlp_destination"] = None

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

    return Exporter(**args)


def unmarshal_GrafanaProductDashboard(data: Any) -> GrafanaProductDashboard:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GrafanaProductDashboard' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("title", None)
    if field is not None:
        args["title"] = field
    else:
        args["title"] = None

    field = data.get("url", None)
    if field is not None:
        args["url"] = field
    else:
        args["url"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("variables", None)
    if field is not None:
        args["variables"] = field
    else:
        args["variables"] = []

    return GrafanaProductDashboard(**args)


def unmarshal_GrafanaUser(data: Any) -> GrafanaUser:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GrafanaUser' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = 0

    field = data.get("login", None)
    if field is not None:
        args["login"] = field
    else:
        args["login"] = None

    field = data.get("role", None)
    if field is not None:
        args["role"] = field
    else:
        args["role"] = GrafanaUserRole.UNKNOWN_ROLE

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

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = PlanName.UNKNOWN_NAME

    field = data.get("sample_ingestion_price", None)
    if field is not None:
        args["sample_ingestion_price"] = field
    else:
        args["sample_ingestion_price"] = 0

    field = data.get("logs_ingestion_price", None)
    if field is not None:
        args["logs_ingestion_price"] = field
    else:
        args["logs_ingestion_price"] = 0

    field = data.get("traces_ingestion_price", None)
    if field is not None:
        args["traces_ingestion_price"] = field
    else:
        args["traces_ingestion_price"] = 0

    field = data.get("monthly_price", None)
    if field is not None:
        args["monthly_price"] = field
    else:
        args["monthly_price"] = 0

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

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("scopes", None)
    if field is not None:
        args["scopes"] = [TokenScope(v) for v in field] if field is not None else None
    else:
        args["scopes"] = []

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

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

    args: dict[str, Any] = {}

    field = data.get("alert_manager_enabled", None)
    if field is not None:
        args["alert_manager_enabled"] = field
    else:
        args["alert_manager_enabled"] = False

    field = data.get("managed_alerts_enabled", None)
    if field is not None:
        args["managed_alerts_enabled"] = field
    else:
        args["managed_alerts_enabled"] = False

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("alert_manager_url", None)
    if field is not None:
        args["alert_manager_url"] = field
    else:
        args["alert_manager_url"] = None

    return AlertManager(**args)


def unmarshal_DisableAlertRulesResponse(data: Any) -> DisableAlertRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DisableAlertRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("disabled_rule_ids", None)
    if field is not None:
        args["disabled_rule_ids"] = field
    else:
        args["disabled_rule_ids"] = []

    return DisableAlertRulesResponse(**args)


def unmarshal_EnableAlertRulesResponse(data: Any) -> EnableAlertRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EnableAlertRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("enabled_rule_ids", None)
    if field is not None:
        args["enabled_rule_ids"] = field
    else:
        args["enabled_rule_ids"] = []

    return EnableAlertRulesResponse(**args)


def unmarshal_GetConfigResponseRetention(data: Any) -> GetConfigResponseRetention:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetConfigResponseRetention' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("min_days", None)
    if field is not None:
        args["min_days"] = field
    else:
        args["min_days"] = None

    field = data.get("max_days", None)
    if field is not None:
        args["max_days"] = field
    else:
        args["max_days"] = None

    field = data.get("default_days", None)
    if field is not None:
        args["default_days"] = field
    else:
        args["default_days"] = None

    return GetConfigResponseRetention(**args)


def unmarshal_GetConfigResponse(data: Any) -> GetConfigResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetConfigResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("custom_metrics_retention", None)
    if field is not None:
        args["custom_metrics_retention"] = unmarshal_GetConfigResponseRetention(field)
    else:
        args["custom_metrics_retention"] = None

    field = data.get("custom_logs_retention", None)
    if field is not None:
        args["custom_logs_retention"] = unmarshal_GetConfigResponseRetention(field)
    else:
        args["custom_logs_retention"] = None

    field = data.get("custom_traces_retention", None)
    if field is not None:
        args["custom_traces_retention"] = unmarshal_GetConfigResponseRetention(field)
    else:
        args["custom_traces_retention"] = None

    field = data.get("product_metrics_retention", None)
    if field is not None:
        args["product_metrics_retention"] = unmarshal_GetConfigResponseRetention(field)
    else:
        args["product_metrics_retention"] = None

    field = data.get("product_logs_retention", None)
    if field is not None:
        args["product_logs_retention"] = unmarshal_GetConfigResponseRetention(field)
    else:
        args["product_logs_retention"] = None

    return GetConfigResponse(**args)


def unmarshal_RulesCount(data: Any) -> RulesCount:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RulesCount' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("data_source_id", None)
    if field is not None:
        args["data_source_id"] = field
    else:
        args["data_source_id"] = None

    field = data.get("data_source_name", None)
    if field is not None:
        args["data_source_name"] = field
    else:
        args["data_source_name"] = None

    field = data.get("rules_count", None)
    if field is not None:
        args["rules_count"] = field
    else:
        args["rules_count"] = 0

    return RulesCount(**args)


def unmarshal_GetRulesCountResponse(data: Any) -> GetRulesCountResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetRulesCountResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("rules_count_by_datasource", None)
    if field is not None:
        args["rules_count_by_datasource"] = (
            [unmarshal_RulesCount(v) for v in field] if field is not None else None
        )
    else:
        args["rules_count_by_datasource"] = []

    field = data.get("preconfigured_rules_count", None)
    if field is not None:
        args["preconfigured_rules_count"] = field
    else:
        args["preconfigured_rules_count"] = 0

    field = data.get("custom_rules_count", None)
    if field is not None:
        args["custom_rules_count"] = field
    else:
        args["custom_rules_count"] = 0

    return GetRulesCountResponse(**args)


def unmarshal_Grafana(data: Any) -> Grafana:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Grafana' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("grafana_url", None)
    if field is not None:
        args["grafana_url"] = field
    else:
        args["grafana_url"] = None

    return Grafana(**args)


def unmarshal_PreconfiguredAlertData(data: Any) -> PreconfiguredAlertData:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PreconfiguredAlertData' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("preconfigured_rule_id", None)
    if field is not None:
        args["preconfigured_rule_id"] = field
    else:
        args["preconfigured_rule_id"] = None

    field = data.get("display_name", None)
    if field is not None:
        args["display_name"] = field
    else:
        args["display_name"] = None

    field = data.get("display_description", None)
    if field is not None:
        args["display_description"] = field
    else:
        args["display_description"] = None

    field = data.get("product_name", None)
    if field is not None:
        args["product_name"] = field
    else:
        args["product_name"] = None

    field = data.get("product_family", None)
    if field is not None:
        args["product_family"] = field
    else:
        args["product_family"] = None

    return PreconfiguredAlertData(**args)


def unmarshal_Alert(data: Any) -> Alert:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Alert' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("preconfigured", None)
    if field is not None:
        args["preconfigured"] = field
    else:
        args["preconfigured"] = False

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("rule", None)
    if field is not None:
        args["rule"] = field
    else:
        args["rule"] = None

    field = data.get("duration", None)
    if field is not None:
        args["duration"] = field
    else:
        args["duration"] = None

    field = data.get("rule_status", None)
    if field is not None:
        args["rule_status"] = field
    else:
        args["rule_status"] = AlertStatus.UNKNOWN_STATUS

    field = data.get("annotations", None)
    if field is not None:
        args["annotations"] = field
    else:
        args["annotations"] = {}

    field = data.get("data_source_id", None)
    if field is not None:
        args["data_source_id"] = field
    else:
        args["data_source_id"] = None

    field = data.get("state", None)
    if field is not None:
        args["state"] = field
    else:
        args["state"] = AlertState.UNKNOWN_STATE

    field = data.get("preconfigured_data", None)
    if field is not None:
        args["preconfigured_data"] = unmarshal_PreconfiguredAlertData(field)
    else:
        args["preconfigured_data"] = None

    return Alert(**args)


def unmarshal_ListAlertsResponse(data: Any) -> ListAlertsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListAlertsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("alerts", None)
    if field is not None:
        args["alerts"] = (
            [unmarshal_Alert(v) for v in field] if field is not None else None
        )
    else:
        args["alerts"] = []

    return ListAlertsResponse(**args)


def unmarshal_ListContactPointsResponse(data: Any) -> ListContactPointsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListContactPointsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("contact_points", None)
    if field is not None:
        args["contact_points"] = (
            [unmarshal_ContactPoint(v) for v in field] if field is not None else None
        )
    else:
        args["contact_points"] = []

    field = data.get("has_additional_receivers", None)
    if field is not None:
        args["has_additional_receivers"] = field
    else:
        args["has_additional_receivers"] = False

    field = data.get("has_additional_contact_points", None)
    if field is not None:
        args["has_additional_contact_points"] = field
    else:
        args["has_additional_contact_points"] = False

    return ListContactPointsResponse(**args)


def unmarshal_ListDataSourcesResponse(data: Any) -> ListDataSourcesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDataSourcesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("data_sources", None)
    if field is not None:
        args["data_sources"] = (
            [unmarshal_DataSource(v) for v in field] if field is not None else None
        )
    else:
        args["data_sources"] = []

    return ListDataSourcesResponse(**args)


def unmarshal_ListExportersResponse(data: Any) -> ListExportersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListExportersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("exporters", None)
    if field is not None:
        args["exporters"] = (
            [unmarshal_Exporter(v) for v in field] if field is not None else None
        )
    else:
        args["exporters"] = []

    return ListExportersResponse(**args)


def unmarshal_ListGrafanaProductDashboardsResponse(
    data: Any,
) -> ListGrafanaProductDashboardsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListGrafanaProductDashboardsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("dashboards", None)
    if field is not None:
        args["dashboards"] = (
            [unmarshal_GrafanaProductDashboard(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["dashboards"] = []

    return ListGrafanaProductDashboardsResponse(**args)


def unmarshal_ListGrafanaUsersResponse(data: Any) -> ListGrafanaUsersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListGrafanaUsersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("grafana_users", None)
    if field is not None:
        args["grafana_users"] = (
            [unmarshal_GrafanaUser(v) for v in field] if field is not None else None
        )
    else:
        args["grafana_users"] = []

    return ListGrafanaUsersResponse(**args)


def unmarshal_ListPlansResponse(data: Any) -> ListPlansResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPlansResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("plans", None)
    if field is not None:
        args["plans"] = (
            [unmarshal_Plan(v) for v in field] if field is not None else None
        )
    else:
        args["plans"] = []

    return ListPlansResponse(**args)


def unmarshal_Product(data: Any) -> Product:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Product' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("display_name", None)
    if field is not None:
        args["display_name"] = field
    else:
        args["display_name"] = None

    field = data.get("family_name", None)
    if field is not None:
        args["family_name"] = field
    else:
        args["family_name"] = None

    field = data.get("resource_types", None)
    if field is not None:
        args["resource_types"] = field
    else:
        args["resource_types"] = None

    return Product(**args)


def unmarshal_ListProductsResponse(data: Any) -> ListProductsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListProductsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("products_list", None)
    if field is not None:
        args["products_list"] = (
            [unmarshal_Product(v) for v in field] if field is not None else None
        )
    else:
        args["products_list"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    return ListProductsResponse(**args)


def unmarshal_ListTokensResponse(data: Any) -> ListTokensResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTokensResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("tokens", None)
    if field is not None:
        args["tokens"] = (
            [unmarshal_Token(v) for v in field] if field is not None else None
        )
    else:
        args["tokens"] = []

    return ListTokensResponse(**args)


def unmarshal_Usage(data: Any) -> Usage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Usage' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("data_source_origin", None)
    if field is not None:
        args["data_source_origin"] = field
    else:
        args["data_source_origin"] = DataSourceOrigin.UNKNOWN_ORIGIN

    field = data.get("data_source_type", None)
    if field is not None:
        args["data_source_type"] = field
    else:
        args["data_source_type"] = DataSourceType.UNKNOWN_TYPE

    field = data.get("unit", None)
    if field is not None:
        args["unit"] = field
    else:
        args["unit"] = UsageUnit.UNKNOWN_UNIT

    field = data.get("quantity_over_interval", None)
    if field is not None:
        args["quantity_over_interval"] = field
    else:
        args["quantity_over_interval"] = 0

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

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

    args: dict[str, Any] = {}

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
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.login is not None:
        output["login"] = request.login

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.role is not None:
        output["role"] = request.role

    return output


def marshal_GlobalApiResetGrafanaUserPasswordRequest(
    request: GlobalApiResetGrafanaUserPasswordRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_GlobalApiSelectPlanRequest(
    request: GlobalApiSelectPlanRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.plan_name is not None:
        output["plan_name"] = request.plan_name

    return output


def marshal_GlobalApiSyncGrafanaDataSourcesRequest(
    request: GlobalApiSyncGrafanaDataSourcesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_ContactPointEmail(
    request: ContactPointEmail,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.to is not None:
        output["to"] = request.to

    return output


def marshal_RegionalApiCreateContactPointRequest(
    request: RegionalApiCreateContactPointRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="email",
                    value=request.email,
                    marshal_func=marshal_ContactPointEmail,
                ),
            ]
        ),
    )

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.send_resolved_notifications is not None:
        output["send_resolved_notifications"] = request.send_resolved_notifications

    return output


def marshal_RegionalApiCreateDataSourceRequest(
    request: RegionalApiCreateDataSourceRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.type_ is not None:
        output["type"] = request.type_

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.retention_days is not None:
        output["retention_days"] = request.retention_days

    return output


def marshal_ExporterDatadogDestination(
    request: ExporterDatadogDestination,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.api_key is not None:
        output["api_key"] = request.api_key

    if request.endpoint is not None:
        output["endpoint"] = request.endpoint

    return output


def marshal_ExporterOTLPDestination(
    request: ExporterOTLPDestination,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.endpoint is not None:
        output["endpoint"] = request.endpoint

    if request.headers is not None:
        output["headers"] = {key: value for key, value in request.headers.items()}

    return output


def marshal_RegionalApiCreateExporterRequest(
    request: RegionalApiCreateExporterRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="datadog_destination",
                    value=request.datadog_destination,
                    marshal_func=marshal_ExporterDatadogDestination,
                ),
                OneOfPossibility(
                    param="otlp_destination",
                    value=request.otlp_destination,
                    marshal_func=marshal_ExporterOTLPDestination,
                ),
            ]
        ),
    )

    if request.datasource_id is not None:
        output["datasource_id"] = request.datasource_id

    if request.exported_products is not None:
        output["exported_products"] = request.exported_products

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    return output


def marshal_RegionalApiCreateTokenRequest(
    request: RegionalApiCreateTokenRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.token_scopes is not None:
        output["token_scopes"] = [str(item) for item in request.token_scopes]

    return output


def marshal_RegionalApiDeleteContactPointRequest(
    request: RegionalApiDeleteContactPointRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="email",
                    value=request.email,
                    marshal_func=marshal_ContactPointEmail,
                ),
            ]
        ),
    )

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_RegionalApiDisableAlertManagerRequest(
    request: RegionalApiDisableAlertManagerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_RegionalApiDisableAlertRulesRequest(
    request: RegionalApiDisableAlertRulesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.rule_ids is not None:
        output["rule_ids"] = request.rule_ids

    return output


def marshal_RegionalApiDisableManagedAlertsRequest(
    request: RegionalApiDisableManagedAlertsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_RegionalApiEnableAlertManagerRequest(
    request: RegionalApiEnableAlertManagerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_RegionalApiEnableAlertRulesRequest(
    request: RegionalApiEnableAlertRulesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.rule_ids is not None:
        output["rule_ids"] = request.rule_ids

    return output


def marshal_RegionalApiEnableManagedAlertsRequest(
    request: RegionalApiEnableManagedAlertsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_RegionalApiTriggerTestAlertRequest(
    request: RegionalApiTriggerTestAlertRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_RegionalApiUpdateContactPointRequest(
    request: RegionalApiUpdateContactPointRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="email",
                    value=request.email,
                    marshal_func=marshal_ContactPointEmail,
                ),
            ]
        ),
    )

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.send_resolved_notifications is not None:
        output["send_resolved_notifications"] = request.send_resolved_notifications

    return output


def marshal_RegionalApiUpdateDataSourceRequest(
    request: RegionalApiUpdateDataSourceRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.retention_days is not None:
        output["retention_days"] = request.retention_days

    return output


def marshal_RegionalApiUpdateExporterRequest(
    request: RegionalApiUpdateExporterRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="datadog_destination",
                    value=request.datadog_destination,
                    marshal_func=marshal_ExporterDatadogDestination,
                ),
                OneOfPossibility(
                    param="otlp_destination",
                    value=request.otlp_destination,
                    marshal_func=marshal_ExporterOTLPDestination,
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.exported_products is not None:
        output["exported_products"] = request.exported_products

    return output
