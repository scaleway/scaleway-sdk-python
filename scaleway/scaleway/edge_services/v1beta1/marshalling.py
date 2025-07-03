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
    DNSStageType,
    LbOriginError,
    ListBackendStagesRequestOrderBy,
    ListCacheStagesRequestOrderBy,
    ListDNSStagesRequestOrderBy,
    ListPipelinesRequestOrderBy,
    ListPipelinesWithStagesRequestOrderBy,
    ListPurgeRequestsRequestOrderBy,
    ListRouteStagesRequestOrderBy,
    ListTLSStagesRequestOrderBy,
    ListWafStagesRequestOrderBy,
    PipelineErrorCode,
    PipelineErrorSeverity,
    PipelineErrorStage,
    PipelineErrorType,
    PipelineStatus,
    PlanName,
    PurgeRequestStatus,
    RuleHttpMatchMethodFilter,
    RuleHttpMatchPathFilterPathFilterType,
    SearchBackendStagesRequestOrderBy,
    SearchWafStagesRequestOrderBy,
    WafStageMode,
    ScalewayLb,
    ScalewayLbBackendConfig,
    ScalewayS3BackendConfig,
    BackendStage,
    CacheStage,
    DNSStage,
    PipelineError,
    Pipeline,
    RouteStage,
    TLSSecret,
    TLSStage,
    WafStage,
    PipelineStages,
    PurgeRequest,
    RuleHttpMatchPathFilter,
    RuleHttpMatch,
    RouteRule,
    AddRouteRulesResponse,
    CheckDomainResponse,
    CheckLbOriginResponse,
    CheckPEMChainResponse,
    PlanDetails,
    PlanUsageDetails,
    GetBillingResponse,
    HeadStageResponseHeadStage,
    HeadStageResponse,
    ListBackendStagesResponse,
    ListCacheStagesResponse,
    ListDNSStagesResponse,
    ListHeadStagesResponseHeadStage,
    ListHeadStagesResponse,
    ListPipelinesResponse,
    ListPipelinesWithStagesResponse,
    ListPlansResponse,
    ListPurgeRequestsResponse,
    ListRouteRulesResponse,
    ListRouteStagesResponse,
    ListTLSStagesResponse,
    ListWafStagesResponse,
    Plan,
    SetRouteRulesResponse,
    SetRouteRulesRequestRouteRule,
    AddRouteRulesRequest,
    CheckDomainRequest,
    CheckLbOriginRequest,
    CheckPEMChainRequestSecretChain,
    CheckPEMChainRequest,
    CreateBackendStageRequest,
    CreateCacheStageRequest,
    CreateDNSStageRequest,
    CreatePipelineRequest,
    CreatePurgeRequestRequest,
    CreateRouteStageRequest,
    CreateTLSStageRequest,
    CreateWafStageRequest,
    SelectPlanRequest,
    SetHeadStageRequestAddNewHeadStage,
    SetHeadStageRequestRemoveHeadStage,
    SetHeadStageRequestSwapHeadStage,
    SetHeadStageRequest,
    SetRouteRulesRequest,
    UpdateBackendStageRequest,
    UpdateCacheStageRequest,
    UpdateDNSStageRequest,
    UpdatePipelineRequest,
    UpdateRouteStageRequest,
    TLSSecretsConfig,
    UpdateTLSStageRequest,
    UpdateWafStageRequest,
)

def unmarshal_ScalewayLb(data: Any) -> ScalewayLb:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ScalewayLb' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("zone", str())
    args["zone"] = field

    field = data.get("frontend_id", str())
    args["frontend_id"] = field

    field = data.get("is_ssl", None)
    args["is_ssl"] = field

    field = data.get("domain_name", None)
    args["domain_name"] = field

    return ScalewayLb(**args)

def unmarshal_ScalewayLbBackendConfig(data: Any) -> ScalewayLbBackendConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ScalewayLbBackendConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("lbs", [])
    args["lbs"] = [unmarshal_ScalewayLb(v) for v in field] if field is not None else None

    return ScalewayLbBackendConfig(**args)

def unmarshal_ScalewayS3BackendConfig(data: Any) -> ScalewayS3BackendConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ScalewayS3BackendConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("bucket_name", None)
    args["bucket_name"] = field

    field = data.get("bucket_region", None)
    args["bucket_region"] = field

    field = data.get("is_website", None)
    args["is_website"] = field

    return ScalewayS3BackendConfig(**args)

def unmarshal_BackendStage(data: Any) -> BackendStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BackendStage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("pipeline_id", str())
    args["pipeline_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("scaleway_s3", None)
    args["scaleway_s3"] = unmarshal_ScalewayS3BackendConfig(field) if field is not None else None

    field = data.get("scaleway_lb", None)
    args["scaleway_lb"] = unmarshal_ScalewayLbBackendConfig(field) if field is not None else None

    return BackendStage(**args)

def unmarshal_CacheStage(data: Any) -> CacheStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CacheStage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("pipeline_id", str())
    args["pipeline_id"] = field

    field = data.get("include_cookies", False)
    args["include_cookies"] = field

    field = data.get("fallback_ttl", None)
    args["fallback_ttl"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("backend_stage_id", None)
    args["backend_stage_id"] = field

    field = data.get("waf_stage_id", None)
    args["waf_stage_id"] = field

    field = data.get("route_stage_id", None)
    args["route_stage_id"] = field

    return CacheStage(**args)

def unmarshal_DNSStage(data: Any) -> DNSStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DNSStage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("fqdns", [])
    args["fqdns"] = field

    field = data.get("type", getattr(DNSStageType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("pipeline_id", str())
    args["pipeline_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("tls_stage_id", None)
    args["tls_stage_id"] = field

    field = data.get("cache_stage_id", None)
    args["cache_stage_id"] = field

    field = data.get("backend_stage_id", None)
    args["backend_stage_id"] = field

    return DNSStage(**args)

def unmarshal_PipelineError(data: Any) -> PipelineError:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PipelineError' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("stage", str())
    args["stage"] = field

    field = data.get("code", str())
    args["code"] = field

    field = data.get("severity", str())
    args["severity"] = field

    field = data.get("message", str())
    args["message"] = field

    field = data.get("type", str())
    args["type_"] = field

    return PipelineError(**args)

def unmarshal_Pipeline(data: Any) -> Pipeline:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Pipeline' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("status", getattr(PipelineStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("errors", [])
    args["errors"] = [unmarshal_PipelineError(v) for v in field] if field is not None else None

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Pipeline(**args)

def unmarshal_RouteStage(data: Any) -> RouteStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RouteStage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("pipeline_id", str())
    args["pipeline_id"] = field

    field = data.get("waf_stage_id", None)
    args["waf_stage_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return RouteStage(**args)

def unmarshal_TLSSecret(data: Any) -> TLSSecret:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TLSSecret' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("secret_id", str())
    args["secret_id"] = field

    field = data.get("region", str())
    args["region"] = field

    return TLSSecret(**args)

def unmarshal_TLSStage(data: Any) -> TLSStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TLSStage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("secrets", [])
    args["secrets"] = [unmarshal_TLSSecret(v) for v in field] if field is not None else None

    field = data.get("managed_certificate", False)
    args["managed_certificate"] = field

    field = data.get("pipeline_id", str())
    args["pipeline_id"] = field

    field = data.get("certificate_expires_at", None)
    args["certificate_expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("cache_stage_id", None)
    args["cache_stage_id"] = field

    field = data.get("backend_stage_id", None)
    args["backend_stage_id"] = field

    field = data.get("waf_stage_id", None)
    args["waf_stage_id"] = field

    field = data.get("route_stage_id", None)
    args["route_stage_id"] = field

    return TLSStage(**args)

def unmarshal_WafStage(data: Any) -> WafStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'WafStage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("pipeline_id", str())
    args["pipeline_id"] = field

    field = data.get("mode", getattr(WafStageMode, "UNKNOWN_MODE"))
    args["mode"] = field

    field = data.get("paranoia_level", 0)
    args["paranoia_level"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("backend_stage_id", None)
    args["backend_stage_id"] = field

    return WafStage(**args)

def unmarshal_PipelineStages(data: Any) -> PipelineStages:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PipelineStages' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dns_stages", str())
    args["dns_stages"] = [unmarshal_DNSStage(v) for v in field] if field is not None else None

    field = data.get("tls_stages", str())
    args["tls_stages"] = [unmarshal_TLSStage(v) for v in field] if field is not None else None

    field = data.get("cache_stages", str())
    args["cache_stages"] = [unmarshal_CacheStage(v) for v in field] if field is not None else None

    field = data.get("backend_stages", str())
    args["backend_stages"] = [unmarshal_BackendStage(v) for v in field] if field is not None else None

    field = data.get("waf_stages", str())
    args["waf_stages"] = [unmarshal_WafStage(v) for v in field] if field is not None else None

    field = data.get("route_stages", str())
    args["route_stages"] = [unmarshal_RouteStage(v) for v in field] if field is not None else None

    field = data.get("pipeline", None)
    args["pipeline"] = unmarshal_Pipeline(field) if field is not None else None

    return PipelineStages(**args)

def unmarshal_PurgeRequest(data: Any) -> PurgeRequest:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PurgeRequest' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("pipeline_id", str())
    args["pipeline_id"] = field

    field = data.get("status", getattr(PurgeRequestStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("assets", None)
    args["assets"] = field

    field = data.get("all", None)
    args["all"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return PurgeRequest(**args)

def unmarshal_RuleHttpMatchPathFilter(data: Any) -> RuleHttpMatchPathFilter:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RuleHttpMatchPathFilter' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("path_filter_type", getattr(RuleHttpMatchPathFilterPathFilterType, "UNKNOWN_PATH_FILTER"))
    args["path_filter_type"] = field

    field = data.get("value", str())
    args["value"] = field

    return RuleHttpMatchPathFilter(**args)

def unmarshal_RuleHttpMatch(data: Any) -> RuleHttpMatch:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RuleHttpMatch' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("method_filters", [])
    args["method_filters"] = [RuleHttpMatchMethodFilter(v) for v in field] if field is not None else None

    field = data.get("path_filter", None)
    args["path_filter"] = unmarshal_RuleHttpMatchPathFilter(field) if field is not None else None

    return RuleHttpMatch(**args)

def unmarshal_RouteRule(data: Any) -> RouteRule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RouteRule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("position", 0)
    args["position"] = field

    field = data.get("route_stage_id", str())
    args["route_stage_id"] = field

    field = data.get("rule_http_match", None)
    args["rule_http_match"] = unmarshal_RuleHttpMatch(field) if field is not None else None

    field = data.get("backend_stage_id", None)
    args["backend_stage_id"] = field

    return RouteRule(**args)

def unmarshal_AddRouteRulesResponse(data: Any) -> AddRouteRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddRouteRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("route_rules", [])
    args["route_rules"] = [unmarshal_RouteRule(v) for v in field] if field is not None else None

    return AddRouteRulesResponse(**args)

def unmarshal_CheckDomainResponse(data: Any) -> CheckDomainResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckDomainResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("is_valid", str())
    args["is_valid"] = field

    return CheckDomainResponse(**args)

def unmarshal_CheckLbOriginResponse(data: Any) -> CheckLbOriginResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckLbOriginResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("is_valid", str())
    args["is_valid"] = field

    field = data.get("error_type", str())
    args["error_type"] = field

    return CheckLbOriginResponse(**args)

def unmarshal_CheckPEMChainResponse(data: Any) -> CheckPEMChainResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckPEMChainResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("is_valid", str())
    args["is_valid"] = field

    return CheckPEMChainResponse(**args)

def unmarshal_PlanDetails(data: Any) -> PlanDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlanDetails' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("plan_name", getattr(PlanName, "UNKNOWN_NAME"))
    args["plan_name"] = field

    field = data.get("package_gb", 0)
    args["package_gb"] = field

    field = data.get("pipeline_limit", 0)
    args["pipeline_limit"] = field

    field = data.get("waf_requests", 0)
    args["waf_requests"] = field

    return PlanDetails(**args)

def unmarshal_PlanUsageDetails(data: Any) -> PlanUsageDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlanUsageDetails' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("plan_cost", None)
    args["plan_cost"] = unmarshal_Money(field) if field is not None else None

    return PlanUsageDetails(**args)

def unmarshal_GetBillingResponse(data: Any) -> GetBillingResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetBillingResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("current_plan", None)
    args["current_plan"] = unmarshal_PlanDetails(field) if field is not None else None

    field = data.get("pipeline_number", 0)
    args["pipeline_number"] = field

    field = data.get("current_plan_cache_usage", 0)
    args["current_plan_cache_usage"] = field

    field = data.get("extra_cache_usage", 0)
    args["extra_cache_usage"] = field

    field = data.get("current_plan_waf_usage", 0)
    args["current_plan_waf_usage"] = field

    field = data.get("extra_waf_usage", 0)
    args["extra_waf_usage"] = field

    field = data.get("plan_cost", None)
    args["plan_cost"] = unmarshal_Money(field) if field is not None else None

    field = data.get("extra_pipelines_cost", None)
    args["extra_pipelines_cost"] = unmarshal_Money(field) if field is not None else None

    field = data.get("plans_usage_details", {})
    args["plans_usage_details"] = {key: unmarshal_PlanUsageDetails(value)for key, value in field.items()
    } if field is not None else None

    field = data.get("extra_cache_cost", None)
    args["extra_cache_cost"] = unmarshal_Money(field) if field is not None else None

    field = data.get("extra_waf_cost", None)
    args["extra_waf_cost"] = unmarshal_Money(field) if field is not None else None

    field = data.get("waf_add_on", None)
    args["waf_add_on"] = unmarshal_Money(field) if field is not None else None

    field = data.get("total_cost", None)
    args["total_cost"] = unmarshal_Money(field) if field is not None else None

    return GetBillingResponse(**args)

def unmarshal_HeadStageResponseHeadStage(data: Any) -> HeadStageResponseHeadStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HeadStageResponseHeadStage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dns_stage_id", None)
    args["dns_stage_id"] = field

    return HeadStageResponseHeadStage(**args)

def unmarshal_HeadStageResponse(data: Any) -> HeadStageResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HeadStageResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("head_stage", None)
    args["head_stage"] = unmarshal_HeadStageResponseHeadStage(field) if field is not None else None

    return HeadStageResponse(**args)

def unmarshal_ListBackendStagesResponse(data: Any) -> ListBackendStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListBackendStagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("stages", [])
    args["stages"] = [unmarshal_BackendStage(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListBackendStagesResponse(**args)

def unmarshal_ListCacheStagesResponse(data: Any) -> ListCacheStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListCacheStagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("stages", [])
    args["stages"] = [unmarshal_CacheStage(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListCacheStagesResponse(**args)

def unmarshal_ListDNSStagesResponse(data: Any) -> ListDNSStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDNSStagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("stages", [])
    args["stages"] = [unmarshal_DNSStage(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListDNSStagesResponse(**args)

def unmarshal_ListHeadStagesResponseHeadStage(data: Any) -> ListHeadStagesResponseHeadStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListHeadStagesResponseHeadStage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dns_stage_id", None)
    args["dns_stage_id"] = field

    return ListHeadStagesResponseHeadStage(**args)

def unmarshal_ListHeadStagesResponse(data: Any) -> ListHeadStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListHeadStagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("head_stages", [])
    args["head_stages"] = [unmarshal_ListHeadStagesResponseHeadStage(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListHeadStagesResponse(**args)

def unmarshal_ListPipelinesResponse(data: Any) -> ListPipelinesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPipelinesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pipelines", [])
    args["pipelines"] = [unmarshal_Pipeline(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListPipelinesResponse(**args)

def unmarshal_ListPipelinesWithStagesResponse(data: Any) -> ListPipelinesWithStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPipelinesWithStagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pipelines", str())
    args["pipelines"] = [unmarshal_PipelineStages(v) for v in field] if field is not None else None

    field = data.get("total_count", str())
    args["total_count"] = field

    return ListPipelinesWithStagesResponse(**args)

def unmarshal_ListPlansResponse(data: Any) -> ListPlansResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPlansResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", str())
    args["total_count"] = field

    field = data.get("plans", str())
    args["plans"] = [unmarshal_PlanDetails(v) for v in field] if field is not None else None

    return ListPlansResponse(**args)

def unmarshal_ListPurgeRequestsResponse(data: Any) -> ListPurgeRequestsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPurgeRequestsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("purge_requests", [])
    args["purge_requests"] = [unmarshal_PurgeRequest(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListPurgeRequestsResponse(**args)

def unmarshal_ListRouteRulesResponse(data: Any) -> ListRouteRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRouteRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("route_rules", [])
    args["route_rules"] = [unmarshal_RouteRule(v) for v in field] if field is not None else None

    return ListRouteRulesResponse(**args)

def unmarshal_ListRouteStagesResponse(data: Any) -> ListRouteStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRouteStagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("stages", [])
    args["stages"] = [unmarshal_RouteStage(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListRouteStagesResponse(**args)

def unmarshal_ListTLSStagesResponse(data: Any) -> ListTLSStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTLSStagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("stages", [])
    args["stages"] = [unmarshal_TLSStage(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListTLSStagesResponse(**args)

def unmarshal_ListWafStagesResponse(data: Any) -> ListWafStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListWafStagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("stages", [])
    args["stages"] = [unmarshal_WafStage(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListWafStagesResponse(**args)

def unmarshal_Plan(data: Any) -> Plan:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Plan' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("plan_name", str())
    args["plan_name"] = field

    return Plan(**args)

def unmarshal_SetRouteRulesResponse(data: Any) -> SetRouteRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetRouteRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("route_rules", [])
    args["route_rules"] = [unmarshal_RouteRule(v) for v in field] if field is not None else None

    return SetRouteRulesResponse(**args)

def marshal_RuleHttpMatchPathFilter(
    request: RuleHttpMatchPathFilter,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.path_filter_type is not None:
        output["path_filter_type"] = str(request.path_filter_type)
    else:
        output["path_filter_type"] = getattr(RuleHttpMatchPathFilterPathFilterType, "UNKNOWN_PATH_FILTER")

    if request.value is not None:
        output["value"] = request.value
    else:
        output["value"] = str()


    return output

def marshal_RuleHttpMatch(
    request: RuleHttpMatch,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.method_filters is not None:
        output["method_filters"] = [str(item) for item in request.method_filters]
    else:
        output["method_filters"] = []

    if request.path_filter is not None:
        output["path_filter"] = marshal_RuleHttpMatchPathFilter(request.path_filter, defaults)
    else:
        output["path_filter"] = None


    return output

def marshal_SetRouteRulesRequestRouteRule(
    request: SetRouteRulesRequestRouteRule,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="rule_http_match", value=request.rule_http_match,marshal_func=marshal_RuleHttpMatch
            ),
        ]),
    )
    output.update(
        resolve_one_of([
            OneOfPossibility(param="backend_stage_id", value=request.backend_stage_id,marshal_func=None
            ),
        ]),
    )


    return output

def marshal_AddRouteRulesRequest(
    request: AddRouteRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="after_position", value=request.after_position,marshal_func=None
            ),
            OneOfPossibility(param="before_position", value=request.before_position,marshal_func=None
            ),
        ]),
    )

    if request.route_rules is not None:
        output["route_rules"] = [marshal_SetRouteRulesRequestRouteRule(item, defaults) for item in request.route_rules]
    else:
        output["route_rules"] = None


    return output

def marshal_CheckDomainRequest(
    request: CheckDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.fqdn is not None:
        output["fqdn"] = request.fqdn
    else:
        output["fqdn"] = str()

    if request.cname is not None:
        output["cname"] = request.cname
    else:
        output["cname"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_ScalewayLb(
    request: ScalewayLb,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.zone is not None:
        output["zone"] = request.zone or defaults.default_zone

    if request.frontend_id is not None:
        output["frontend_id"] = request.frontend_id
    else:
        output["frontend_id"] = str()

    if request.is_ssl is not None:
        output["is_ssl"] = request.is_ssl
    else:
        output["is_ssl"] = None

    if request.domain_name is not None:
        output["domain_name"] = request.domain_name
    else:
        output["domain_name"] = None


    return output

def marshal_CheckLbOriginRequest(
    request: CheckLbOriginRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.lb is not None:
        output["lb"] = marshal_ScalewayLb(request.lb, defaults)
    else:
        output["lb"] = None


    return output

def marshal_CheckPEMChainRequestSecretChain(
    request: CheckPEMChainRequestSecretChain,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.secret_id is not None:
        output["secret_id"] = request.secret_id
    else:
        output["secret_id"] = str()

    if request.secret_region is not None:
        output["secret_region"] = request.secret_region
    else:
        output["secret_region"] = str()


    return output

def marshal_CheckPEMChainRequest(
    request: CheckPEMChainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="secret", value=request.secret,marshal_func=marshal_CheckPEMChainRequestSecretChain
            ),
            OneOfPossibility(param="raw", value=request.raw,marshal_func=None
            ),
        ]),
    )

    if request.fqdn is not None:
        output["fqdn"] = request.fqdn
    else:
        output["fqdn"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_ScalewayLbBackendConfig(
    request: ScalewayLbBackendConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.lbs is not None:
        output["lbs"] = [marshal_ScalewayLb(item, defaults) for item in request.lbs]
    else:
        output["lbs"] = []


    return output

def marshal_ScalewayS3BackendConfig(
    request: ScalewayS3BackendConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.bucket_name is not None:
        output["bucket_name"] = request.bucket_name
    else:
        output["bucket_name"] = None

    if request.bucket_region is not None:
        output["bucket_region"] = request.bucket_region
    else:
        output["bucket_region"] = None

    if request.is_website is not None:
        output["is_website"] = request.is_website
    else:
        output["is_website"] = None


    return output

def marshal_CreateBackendStageRequest(
    request: CreateBackendStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="scaleway_s3", value=request.scaleway_s3,marshal_func=marshal_ScalewayS3BackendConfig
            ),
            OneOfPossibility(param="scaleway_lb", value=request.scaleway_lb,marshal_func=marshal_ScalewayLbBackendConfig
            ),
        ]),
    )


    return output

def marshal_CreateCacheStageRequest(
    request: CreateCacheStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="backend_stage_id", value=request.backend_stage_id,marshal_func=None
            ),
            OneOfPossibility(param="waf_stage_id", value=request.waf_stage_id,marshal_func=None
            ),
            OneOfPossibility(param="route_stage_id", value=request.route_stage_id,marshal_func=None
            ),
        ]),
    )

    if request.fallback_ttl is not None:
        output["fallback_ttl"] = request.fallback_ttl
    else:
        output["fallback_ttl"] = None

    if request.include_cookies is not None:
        output["include_cookies"] = request.include_cookies
    else:
        output["include_cookies"] = None


    return output

def marshal_CreateDNSStageRequest(
    request: CreateDNSStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="tls_stage_id", value=request.tls_stage_id,marshal_func=None
            ),
            OneOfPossibility(param="cache_stage_id", value=request.cache_stage_id,marshal_func=None
            ),
            OneOfPossibility(param="backend_stage_id", value=request.backend_stage_id,marshal_func=None
            ),
        ]),
    )

    if request.fqdns is not None:
        output["fqdns"] = request.fqdns
    else:
        output["fqdns"] = None


    return output

def marshal_CreatePipelineRequest(
    request: CreatePipelineRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_CreatePurgeRequestRequest(
    request: CreatePurgeRequestRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="assets", value=request.assets,marshal_func=None
            ),
            OneOfPossibility(param="all", value=request.all,marshal_func=None
            ),
        ]),
    )

    if request.pipeline_id is not None:
        output["pipeline_id"] = request.pipeline_id
    else:
        output["pipeline_id"] = str()


    return output

def marshal_CreateRouteStageRequest(
    request: CreateRouteStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="waf_stage_id", value=request.waf_stage_id,marshal_func=None
            ),
        ]),
    )


    return output

def marshal_TLSSecret(
    request: TLSSecret,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.secret_id is not None:
        output["secret_id"] = request.secret_id
    else:
        output["secret_id"] = str()

    if request.region is not None:
        output["region"] = request.region or defaults.default_region


    return output

def marshal_CreateTLSStageRequest(
    request: CreateTLSStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="cache_stage_id", value=request.cache_stage_id,marshal_func=None
            ),
            OneOfPossibility(param="backend_stage_id", value=request.backend_stage_id,marshal_func=None
            ),
            OneOfPossibility(param="route_stage_id", value=request.route_stage_id,marshal_func=None
            ),
            OneOfPossibility(param="waf_stage_id", value=request.waf_stage_id,marshal_func=None
            ),
        ]),
    )

    if request.secrets is not None:
        output["secrets"] = [marshal_TLSSecret(item, defaults) for item in request.secrets]
    else:
        output["secrets"] = None

    if request.managed_certificate is not None:
        output["managed_certificate"] = request.managed_certificate
    else:
        output["managed_certificate"] = None


    return output

def marshal_CreateWafStageRequest(
    request: CreateWafStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="backend_stage_id", value=request.backend_stage_id,marshal_func=None
            ),
        ]),
    )

    if request.paranoia_level is not None:
        output["paranoia_level"] = request.paranoia_level
    else:
        output["paranoia_level"] = 0

    if request.mode is not None:
        output["mode"] = str(request.mode)
    else:
        output["mode"] = None


    return output

def marshal_SelectPlanRequest(
    request: SelectPlanRequest,
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

def marshal_SetHeadStageRequestAddNewHeadStage(
    request: SetHeadStageRequestAddNewHeadStage,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.new_stage_id is not None:
        output["new_stage_id"] = request.new_stage_id
    else:
        output["new_stage_id"] = str()


    return output

def marshal_SetHeadStageRequestRemoveHeadStage(
    request: SetHeadStageRequestRemoveHeadStage,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.remove_stage_id is not None:
        output["remove_stage_id"] = request.remove_stage_id
    else:
        output["remove_stage_id"] = str()


    return output

def marshal_SetHeadStageRequestSwapHeadStage(
    request: SetHeadStageRequestSwapHeadStage,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.new_stage_id is not None:
        output["new_stage_id"] = request.new_stage_id
    else:
        output["new_stage_id"] = str()

    if request.current_stage_id is not None:
        output["current_stage_id"] = request.current_stage_id
    else:
        output["current_stage_id"] = str()


    return output

def marshal_SetHeadStageRequest(
    request: SetHeadStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="add_new_head_stage", value=request.add_new_head_stage,marshal_func=marshal_SetHeadStageRequestAddNewHeadStage
            ),
            OneOfPossibility(param="remove_head_stage", value=request.remove_head_stage,marshal_func=marshal_SetHeadStageRequestRemoveHeadStage
            ),
            OneOfPossibility(param="swap_head_stage", value=request.swap_head_stage,marshal_func=marshal_SetHeadStageRequestSwapHeadStage
            ),
        ]),
    )


    return output

def marshal_SetRouteRulesRequest(
    request: SetRouteRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.route_rules is not None:
        output["route_rules"] = [marshal_SetRouteRulesRequestRouteRule(item, defaults) for item in request.route_rules]
    else:
        output["route_rules"] = None


    return output

def marshal_UpdateBackendStageRequest(
    request: UpdateBackendStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="scaleway_s3", value=request.scaleway_s3,marshal_func=marshal_ScalewayS3BackendConfig
            ),
            OneOfPossibility(param="scaleway_lb", value=request.scaleway_lb,marshal_func=marshal_ScalewayLbBackendConfig
            ),
        ]),
    )

    if request.pipeline_id is not None:
        output["pipeline_id"] = request.pipeline_id
    else:
        output["pipeline_id"] = str()


    return output

def marshal_UpdateCacheStageRequest(
    request: UpdateCacheStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="backend_stage_id", value=request.backend_stage_id,marshal_func=None
            ),
            OneOfPossibility(param="waf_stage_id", value=request.waf_stage_id,marshal_func=None
            ),
            OneOfPossibility(param="route_stage_id", value=request.route_stage_id,marshal_func=None
            ),
        ]),
    )

    if request.fallback_ttl is not None:
        output["fallback_ttl"] = request.fallback_ttl
    else:
        output["fallback_ttl"] = None

    if request.include_cookies is not None:
        output["include_cookies"] = request.include_cookies
    else:
        output["include_cookies"] = None


    return output

def marshal_UpdateDNSStageRequest(
    request: UpdateDNSStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="tls_stage_id", value=request.tls_stage_id,marshal_func=None
            ),
            OneOfPossibility(param="cache_stage_id", value=request.cache_stage_id,marshal_func=None
            ),
            OneOfPossibility(param="backend_stage_id", value=request.backend_stage_id,marshal_func=None
            ),
        ]),
    )

    if request.fqdns is not None:
        output["fqdns"] = request.fqdns
    else:
        output["fqdns"] = None


    return output

def marshal_UpdatePipelineRequest(
    request: UpdatePipelineRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None


    return output

def marshal_UpdateRouteStageRequest(
    request: UpdateRouteStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="waf_stage_id", value=request.waf_stage_id,marshal_func=None
            ),
        ]),
    )


    return output

def marshal_TLSSecretsConfig(
    request: TLSSecretsConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.tls_secrets is not None:
        output["tls_secrets"] = [marshal_TLSSecret(item, defaults) for item in request.tls_secrets]
    else:
        output["tls_secrets"] = []


    return output

def marshal_UpdateTLSStageRequest(
    request: UpdateTLSStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="cache_stage_id", value=request.cache_stage_id,marshal_func=None
            ),
            OneOfPossibility(param="backend_stage_id", value=request.backend_stage_id,marshal_func=None
            ),
            OneOfPossibility(param="route_stage_id", value=request.route_stage_id,marshal_func=None
            ),
            OneOfPossibility(param="waf_stage_id", value=request.waf_stage_id,marshal_func=None
            ),
        ]),
    )

    if request.tls_secrets_config is not None:
        output["tls_secrets_config"] = marshal_TLSSecretsConfig(request.tls_secrets_config, defaults)
    else:
        output["tls_secrets_config"] = None

    if request.managed_certificate is not None:
        output["managed_certificate"] = request.managed_certificate
    else:
        output["managed_certificate"] = None


    return output

def marshal_UpdateWafStageRequest(
    request: UpdateWafStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="backend_stage_id", value=request.backend_stage_id,marshal_func=None
            ),
        ]),
    )

    if request.mode is not None:
        output["mode"] = str(request.mode)
    else:
        output["mode"] = None

    if request.paranoia_level is not None:
        output["paranoia_level"] = request.paranoia_level
    else:
        output["paranoia_level"] = None


    return output
