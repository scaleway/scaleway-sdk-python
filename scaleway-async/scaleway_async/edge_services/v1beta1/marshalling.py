# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    unmarshal_Money,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    DNSStageType,
    PipelineStatus,
    PlanName,
    PurgeRequestStatus,
    RuleHttpMatchMethodFilter,
    RuleHttpMatchPathFilterPathFilterType,
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

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("frontend_id", None)
    if field is not None:
        args["frontend_id"] = field
    else:
        args["frontend_id"] = None

    field = data.get("is_ssl", None)
    if field is not None:
        args["is_ssl"] = field
    else:
        args["is_ssl"] = False

    field = data.get("domain_name", None)
    if field is not None:
        args["domain_name"] = field
    else:
        args["domain_name"] = None

    return ScalewayLb(**args)


def unmarshal_ScalewayLbBackendConfig(data: Any) -> ScalewayLbBackendConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ScalewayLbBackendConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("lbs", None)
    if field is not None:
        args["lbs"] = (
            [unmarshal_ScalewayLb(v) for v in field] if field is not None else None
        )
    else:
        args["lbs"] = []

    return ScalewayLbBackendConfig(**args)


def unmarshal_ScalewayS3BackendConfig(data: Any) -> ScalewayS3BackendConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ScalewayS3BackendConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("bucket_name", None)
    if field is not None:
        args["bucket_name"] = field
    else:
        args["bucket_name"] = None

    field = data.get("bucket_region", None)
    if field is not None:
        args["bucket_region"] = field
    else:
        args["bucket_region"] = None

    field = data.get("is_website", None)
    if field is not None:
        args["is_website"] = field
    else:
        args["is_website"] = False

    return ScalewayS3BackendConfig(**args)


def unmarshal_BackendStage(data: Any) -> BackendStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BackendStage' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("pipeline_id", None)
    if field is not None:
        args["pipeline_id"] = field
    else:
        args["pipeline_id"] = None

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

    field = data.get("scaleway_s3", None)
    if field is not None:
        args["scaleway_s3"] = unmarshal_ScalewayS3BackendConfig(field)
    else:
        args["scaleway_s3"] = None

    field = data.get("scaleway_lb", None)
    if field is not None:
        args["scaleway_lb"] = unmarshal_ScalewayLbBackendConfig(field)
    else:
        args["scaleway_lb"] = None

    return BackendStage(**args)


def unmarshal_CacheStage(data: Any) -> CacheStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CacheStage' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("pipeline_id", None)
    if field is not None:
        args["pipeline_id"] = field
    else:
        args["pipeline_id"] = None

    field = data.get("include_cookies", None)
    if field is not None:
        args["include_cookies"] = field
    else:
        args["include_cookies"] = False

    field = data.get("fallback_ttl", None)
    if field is not None:
        args["fallback_ttl"] = field
    else:
        args["fallback_ttl"] = None

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

    field = data.get("backend_stage_id", None)
    if field is not None:
        args["backend_stage_id"] = field
    else:
        args["backend_stage_id"] = None

    field = data.get("waf_stage_id", None)
    if field is not None:
        args["waf_stage_id"] = field
    else:
        args["waf_stage_id"] = None

    field = data.get("route_stage_id", None)
    if field is not None:
        args["route_stage_id"] = field
    else:
        args["route_stage_id"] = None

    return CacheStage(**args)


def unmarshal_DNSStage(data: Any) -> DNSStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DNSStage' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("fqdns", None)
    if field is not None:
        args["fqdns"] = field
    else:
        args["fqdns"] = []

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = DNSStageType.UNKNOWN_TYPE

    field = data.get("pipeline_id", None)
    if field is not None:
        args["pipeline_id"] = field
    else:
        args["pipeline_id"] = None

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

    field = data.get("tls_stage_id", None)
    if field is not None:
        args["tls_stage_id"] = field
    else:
        args["tls_stage_id"] = None

    field = data.get("cache_stage_id", None)
    if field is not None:
        args["cache_stage_id"] = field
    else:
        args["cache_stage_id"] = None

    field = data.get("backend_stage_id", None)
    if field is not None:
        args["backend_stage_id"] = field
    else:
        args["backend_stage_id"] = None

    return DNSStage(**args)


def unmarshal_PipelineError(data: Any) -> PipelineError:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PipelineError' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("stage", None)
    if field is not None:
        args["stage"] = field
    else:
        args["stage"] = None

    field = data.get("code", None)
    if field is not None:
        args["code"] = field
    else:
        args["code"] = None

    field = data.get("severity", None)
    if field is not None:
        args["severity"] = field
    else:
        args["severity"] = None

    field = data.get("message", None)
    if field is not None:
        args["message"] = field
    else:
        args["message"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    return PipelineError(**args)


def unmarshal_Pipeline(data: Any) -> Pipeline:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Pipeline' failed as data isn't a dictionary."
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

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = PipelineStatus.UNKNOWN_STATUS

    field = data.get("errors", None)
    if field is not None:
        args["errors"] = (
            [unmarshal_PipelineError(v) for v in field] if field is not None else None
        )
    else:
        args["errors"] = []

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

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

    return Pipeline(**args)


def unmarshal_RouteStage(data: Any) -> RouteStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RouteStage' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("pipeline_id", None)
    if field is not None:
        args["pipeline_id"] = field
    else:
        args["pipeline_id"] = None

    field = data.get("waf_stage_id", None)
    if field is not None:
        args["waf_stage_id"] = field
    else:
        args["waf_stage_id"] = None

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

    return RouteStage(**args)


def unmarshal_TLSSecret(data: Any) -> TLSSecret:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TLSSecret' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("secret_id", None)
    if field is not None:
        args["secret_id"] = field
    else:
        args["secret_id"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    return TLSSecret(**args)


def unmarshal_TLSStage(data: Any) -> TLSStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TLSStage' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("secrets", None)
    if field is not None:
        args["secrets"] = (
            [unmarshal_TLSSecret(v) for v in field] if field is not None else None
        )
    else:
        args["secrets"] = []

    field = data.get("managed_certificate", None)
    if field is not None:
        args["managed_certificate"] = field
    else:
        args["managed_certificate"] = False

    field = data.get("pipeline_id", None)
    if field is not None:
        args["pipeline_id"] = field
    else:
        args["pipeline_id"] = None

    field = data.get("certificate_expires_at", None)
    if field is not None:
        args["certificate_expires_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["certificate_expires_at"] = None

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

    field = data.get("cache_stage_id", None)
    if field is not None:
        args["cache_stage_id"] = field
    else:
        args["cache_stage_id"] = None

    field = data.get("backend_stage_id", None)
    if field is not None:
        args["backend_stage_id"] = field
    else:
        args["backend_stage_id"] = None

    field = data.get("waf_stage_id", None)
    if field is not None:
        args["waf_stage_id"] = field
    else:
        args["waf_stage_id"] = None

    field = data.get("route_stage_id", None)
    if field is not None:
        args["route_stage_id"] = field
    else:
        args["route_stage_id"] = None

    return TLSStage(**args)


def unmarshal_WafStage(data: Any) -> WafStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'WafStage' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("pipeline_id", None)
    if field is not None:
        args["pipeline_id"] = field
    else:
        args["pipeline_id"] = None

    field = data.get("mode", None)
    if field is not None:
        args["mode"] = field
    else:
        args["mode"] = WafStageMode.UNKNOWN_MODE

    field = data.get("paranoia_level", None)
    if field is not None:
        args["paranoia_level"] = field
    else:
        args["paranoia_level"] = 0

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

    field = data.get("backend_stage_id", None)
    if field is not None:
        args["backend_stage_id"] = field
    else:
        args["backend_stage_id"] = None

    return WafStage(**args)


def unmarshal_PipelineStages(data: Any) -> PipelineStages:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PipelineStages' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("dns_stages", None)
    if field is not None:
        args["dns_stages"] = (
            [unmarshal_DNSStage(v) for v in field] if field is not None else None
        )
    else:
        args["dns_stages"] = None

    field = data.get("tls_stages", None)
    if field is not None:
        args["tls_stages"] = (
            [unmarshal_TLSStage(v) for v in field] if field is not None else None
        )
    else:
        args["tls_stages"] = None

    field = data.get("cache_stages", None)
    if field is not None:
        args["cache_stages"] = (
            [unmarshal_CacheStage(v) for v in field] if field is not None else None
        )
    else:
        args["cache_stages"] = None

    field = data.get("backend_stages", None)
    if field is not None:
        args["backend_stages"] = (
            [unmarshal_BackendStage(v) for v in field] if field is not None else None
        )
    else:
        args["backend_stages"] = None

    field = data.get("waf_stages", None)
    if field is not None:
        args["waf_stages"] = (
            [unmarshal_WafStage(v) for v in field] if field is not None else None
        )
    else:
        args["waf_stages"] = None

    field = data.get("route_stages", None)
    if field is not None:
        args["route_stages"] = (
            [unmarshal_RouteStage(v) for v in field] if field is not None else None
        )
    else:
        args["route_stages"] = None

    field = data.get("pipeline", None)
    if field is not None:
        args["pipeline"] = unmarshal_Pipeline(field)
    else:
        args["pipeline"] = None

    return PipelineStages(**args)


def unmarshal_PurgeRequest(data: Any) -> PurgeRequest:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PurgeRequest' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("pipeline_id", None)
    if field is not None:
        args["pipeline_id"] = field
    else:
        args["pipeline_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = PurgeRequestStatus.UNKNOWN_STATUS

    field = data.get("assets", None)
    if field is not None:
        args["assets"] = field
    else:
        args["assets"] = []

    field = data.get("all", None)
    if field is not None:
        args["all"] = field
    else:
        args["all"] = False

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

    return PurgeRequest(**args)


def unmarshal_RuleHttpMatchPathFilter(data: Any) -> RuleHttpMatchPathFilter:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RuleHttpMatchPathFilter' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("path_filter_type", None)
    if field is not None:
        args["path_filter_type"] = field
    else:
        args["path_filter_type"] = (
            RuleHttpMatchPathFilterPathFilterType.UNKNOWN_PATH_FILTER
        )

    field = data.get("value", None)
    if field is not None:
        args["value"] = field
    else:
        args["value"] = None

    return RuleHttpMatchPathFilter(**args)


def unmarshal_RuleHttpMatch(data: Any) -> RuleHttpMatch:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RuleHttpMatch' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("method_filters", None)
    if field is not None:
        args["method_filters"] = (
            [RuleHttpMatchMethodFilter(v) for v in field] if field is not None else None
        )
    else:
        args["method_filters"] = []

    field = data.get("path_filter", None)
    if field is not None:
        args["path_filter"] = unmarshal_RuleHttpMatchPathFilter(field)
    else:
        args["path_filter"] = None

    return RuleHttpMatch(**args)


def unmarshal_RouteRule(data: Any) -> RouteRule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RouteRule' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("position", None)
    if field is not None:
        args["position"] = field
    else:
        args["position"] = 0

    field = data.get("route_stage_id", None)
    if field is not None:
        args["route_stage_id"] = field
    else:
        args["route_stage_id"] = None

    field = data.get("rule_http_match", None)
    if field is not None:
        args["rule_http_match"] = unmarshal_RuleHttpMatch(field)
    else:
        args["rule_http_match"] = None

    field = data.get("backend_stage_id", None)
    if field is not None:
        args["backend_stage_id"] = field
    else:
        args["backend_stage_id"] = None

    return RouteRule(**args)


def unmarshal_AddRouteRulesResponse(data: Any) -> AddRouteRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddRouteRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("route_rules", None)
    if field is not None:
        args["route_rules"] = (
            [unmarshal_RouteRule(v) for v in field] if field is not None else None
        )
    else:
        args["route_rules"] = []

    return AddRouteRulesResponse(**args)


def unmarshal_CheckDomainResponse(data: Any) -> CheckDomainResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckDomainResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("is_valid", None)
    if field is not None:
        args["is_valid"] = field
    else:
        args["is_valid"] = None

    return CheckDomainResponse(**args)


def unmarshal_CheckLbOriginResponse(data: Any) -> CheckLbOriginResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckLbOriginResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("is_valid", None)
    if field is not None:
        args["is_valid"] = field
    else:
        args["is_valid"] = None

    field = data.get("error_type", None)
    if field is not None:
        args["error_type"] = field
    else:
        args["error_type"] = None

    return CheckLbOriginResponse(**args)


def unmarshal_CheckPEMChainResponse(data: Any) -> CheckPEMChainResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckPEMChainResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("is_valid", None)
    if field is not None:
        args["is_valid"] = field
    else:
        args["is_valid"] = None

    return CheckPEMChainResponse(**args)


def unmarshal_PlanDetails(data: Any) -> PlanDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlanDetails' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("plan_name", None)
    if field is not None:
        args["plan_name"] = field
    else:
        args["plan_name"] = PlanName.UNKNOWN_NAME

    field = data.get("package_gb", None)
    if field is not None:
        args["package_gb"] = field
    else:
        args["package_gb"] = 0

    field = data.get("pipeline_limit", None)
    if field is not None:
        args["pipeline_limit"] = field
    else:
        args["pipeline_limit"] = 0

    field = data.get("waf_requests", None)
    if field is not None:
        args["waf_requests"] = field
    else:
        args["waf_requests"] = 0

    return PlanDetails(**args)


def unmarshal_PlanUsageDetails(data: Any) -> PlanUsageDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlanUsageDetails' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("plan_cost", None)
    if field is not None:
        args["plan_cost"] = unmarshal_Money(field)
    else:
        args["plan_cost"] = None

    return PlanUsageDetails(**args)


def unmarshal_GetBillingResponse(data: Any) -> GetBillingResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetBillingResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("current_plan", None)
    if field is not None:
        args["current_plan"] = unmarshal_PlanDetails(field)
    else:
        args["current_plan"] = None

    field = data.get("pipeline_number", None)
    if field is not None:
        args["pipeline_number"] = field
    else:
        args["pipeline_number"] = 0

    field = data.get("current_plan_cache_usage", None)
    if field is not None:
        args["current_plan_cache_usage"] = field
    else:
        args["current_plan_cache_usage"] = 0

    field = data.get("extra_cache_usage", None)
    if field is not None:
        args["extra_cache_usage"] = field
    else:
        args["extra_cache_usage"] = 0

    field = data.get("current_plan_waf_usage", None)
    if field is not None:
        args["current_plan_waf_usage"] = field
    else:
        args["current_plan_waf_usage"] = 0

    field = data.get("extra_waf_usage", None)
    if field is not None:
        args["extra_waf_usage"] = field
    else:
        args["extra_waf_usage"] = 0

    field = data.get("plan_cost", None)
    if field is not None:
        args["plan_cost"] = unmarshal_Money(field)
    else:
        args["plan_cost"] = None

    field = data.get("extra_pipelines_cost", None)
    if field is not None:
        args["extra_pipelines_cost"] = unmarshal_Money(field)
    else:
        args["extra_pipelines_cost"] = None

    field = data.get("plans_usage_details", None)
    if field is not None:
        args["plans_usage_details"] = (
            {key: unmarshal_PlanUsageDetails(value) for key, value in field.items()}
            if field is not None
            else None
        )
    else:
        args["plans_usage_details"] = {}

    field = data.get("extra_cache_cost", None)
    if field is not None:
        args["extra_cache_cost"] = unmarshal_Money(field)
    else:
        args["extra_cache_cost"] = None

    field = data.get("extra_waf_cost", None)
    if field is not None:
        args["extra_waf_cost"] = unmarshal_Money(field)
    else:
        args["extra_waf_cost"] = None

    field = data.get("waf_add_on", None)
    if field is not None:
        args["waf_add_on"] = unmarshal_Money(field)
    else:
        args["waf_add_on"] = None

    field = data.get("total_cost", None)
    if field is not None:
        args["total_cost"] = unmarshal_Money(field)
    else:
        args["total_cost"] = None

    return GetBillingResponse(**args)


def unmarshal_HeadStageResponseHeadStage(data: Any) -> HeadStageResponseHeadStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HeadStageResponseHeadStage' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("dns_stage_id", None)
    if field is not None:
        args["dns_stage_id"] = field
    else:
        args["dns_stage_id"] = None

    return HeadStageResponseHeadStage(**args)


def unmarshal_HeadStageResponse(data: Any) -> HeadStageResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HeadStageResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("head_stage", None)
    if field is not None:
        args["head_stage"] = unmarshal_HeadStageResponseHeadStage(field)
    else:
        args["head_stage"] = None

    return HeadStageResponse(**args)


def unmarshal_ListBackendStagesResponse(data: Any) -> ListBackendStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListBackendStagesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("stages", None)
    if field is not None:
        args["stages"] = (
            [unmarshal_BackendStage(v) for v in field] if field is not None else None
        )
    else:
        args["stages"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListBackendStagesResponse(**args)


def unmarshal_ListCacheStagesResponse(data: Any) -> ListCacheStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListCacheStagesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("stages", None)
    if field is not None:
        args["stages"] = (
            [unmarshal_CacheStage(v) for v in field] if field is not None else None
        )
    else:
        args["stages"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListCacheStagesResponse(**args)


def unmarshal_ListDNSStagesResponse(data: Any) -> ListDNSStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDNSStagesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("stages", None)
    if field is not None:
        args["stages"] = (
            [unmarshal_DNSStage(v) for v in field] if field is not None else None
        )
    else:
        args["stages"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListDNSStagesResponse(**args)


def unmarshal_ListHeadStagesResponseHeadStage(
    data: Any,
) -> ListHeadStagesResponseHeadStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListHeadStagesResponseHeadStage' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("dns_stage_id", None)
    if field is not None:
        args["dns_stage_id"] = field
    else:
        args["dns_stage_id"] = None

    return ListHeadStagesResponseHeadStage(**args)


def unmarshal_ListHeadStagesResponse(data: Any) -> ListHeadStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListHeadStagesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("head_stages", None)
    if field is not None:
        args["head_stages"] = (
            [unmarshal_ListHeadStagesResponseHeadStage(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["head_stages"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListHeadStagesResponse(**args)


def unmarshal_ListPipelinesResponse(data: Any) -> ListPipelinesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPipelinesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("pipelines", None)
    if field is not None:
        args["pipelines"] = (
            [unmarshal_Pipeline(v) for v in field] if field is not None else None
        )
    else:
        args["pipelines"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListPipelinesResponse(**args)


def unmarshal_ListPipelinesWithStagesResponse(
    data: Any,
) -> ListPipelinesWithStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPipelinesWithStagesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("pipelines", None)
    if field is not None:
        args["pipelines"] = (
            [unmarshal_PipelineStages(v) for v in field] if field is not None else None
        )
    else:
        args["pipelines"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    return ListPipelinesWithStagesResponse(**args)


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
        args["total_count"] = None

    field = data.get("plans", None)
    if field is not None:
        args["plans"] = (
            [unmarshal_PlanDetails(v) for v in field] if field is not None else None
        )
    else:
        args["plans"] = None

    return ListPlansResponse(**args)


def unmarshal_ListPurgeRequestsResponse(data: Any) -> ListPurgeRequestsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPurgeRequestsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("purge_requests", None)
    if field is not None:
        args["purge_requests"] = (
            [unmarshal_PurgeRequest(v) for v in field] if field is not None else None
        )
    else:
        args["purge_requests"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListPurgeRequestsResponse(**args)


def unmarshal_ListRouteRulesResponse(data: Any) -> ListRouteRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRouteRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("route_rules", None)
    if field is not None:
        args["route_rules"] = (
            [unmarshal_RouteRule(v) for v in field] if field is not None else None
        )
    else:
        args["route_rules"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListRouteRulesResponse(**args)


def unmarshal_ListRouteStagesResponse(data: Any) -> ListRouteStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRouteStagesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("stages", None)
    if field is not None:
        args["stages"] = (
            [unmarshal_RouteStage(v) for v in field] if field is not None else None
        )
    else:
        args["stages"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListRouteStagesResponse(**args)


def unmarshal_ListTLSStagesResponse(data: Any) -> ListTLSStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTLSStagesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("stages", None)
    if field is not None:
        args["stages"] = (
            [unmarshal_TLSStage(v) for v in field] if field is not None else None
        )
    else:
        args["stages"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListTLSStagesResponse(**args)


def unmarshal_ListWafStagesResponse(data: Any) -> ListWafStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListWafStagesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("stages", None)
    if field is not None:
        args["stages"] = (
            [unmarshal_WafStage(v) for v in field] if field is not None else None
        )
    else:
        args["stages"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListWafStagesResponse(**args)


def unmarshal_Plan(data: Any) -> Plan:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Plan' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("plan_name", None)
    if field is not None:
        args["plan_name"] = field
    else:
        args["plan_name"] = None

    return Plan(**args)


def unmarshal_SetRouteRulesResponse(data: Any) -> SetRouteRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetRouteRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("route_rules", None)
    if field is not None:
        args["route_rules"] = (
            [unmarshal_RouteRule(v) for v in field] if field is not None else None
        )
    else:
        args["route_rules"] = []

    return SetRouteRulesResponse(**args)


def marshal_RuleHttpMatchPathFilter(
    request: RuleHttpMatchPathFilter,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.path_filter_type is not None:
        output["path_filter_type"] = request.path_filter_type

    if request.value is not None:
        output["value"] = request.value

    return output


def marshal_RuleHttpMatch(
    request: RuleHttpMatch,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.method_filters is not None:
        output["method_filters"] = [str(item) for item in request.method_filters]

    if request.path_filter is not None:
        output["path_filter"] = marshal_RuleHttpMatchPathFilter(
            request.path_filter, defaults
        )

    return output


def marshal_SetRouteRulesRequestRouteRule(
    request: SetRouteRulesRequestRouteRule,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="rule_http_match",
                    value=request.rule_http_match,
                    marshal_func=marshal_RuleHttpMatch,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="backend_stage_id",
                    value=request.backend_stage_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    return output


def marshal_AddRouteRulesRequest(
    request: AddRouteRulesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="after_position",
                    value=request.after_position,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="before_position",
                    value=request.before_position,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.route_rules is not None:
        output["route_rules"] = [
            marshal_SetRouteRulesRequestRouteRule(item, defaults)
            for item in request.route_rules
        ]

    return output


def marshal_CheckDomainRequest(
    request: CheckDomainRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.fqdn is not None:
        output["fqdn"] = request.fqdn

    if request.cname is not None:
        output["cname"] = request.cname

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_ScalewayLb(
    request: ScalewayLb,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.zone is not None:
        output["zone"] = request.zone
    else:
        output["zone"] = defaults.default_zone

    if request.frontend_id is not None:
        output["frontend_id"] = request.frontend_id

    if request.is_ssl is not None:
        output["is_ssl"] = request.is_ssl

    if request.domain_name is not None:
        output["domain_name"] = request.domain_name

    return output


def marshal_CheckLbOriginRequest(
    request: CheckLbOriginRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.lb is not None:
        output["lb"] = marshal_ScalewayLb(request.lb, defaults)

    return output


def marshal_CheckPEMChainRequestSecretChain(
    request: CheckPEMChainRequestSecretChain,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.secret_id is not None:
        output["secret_id"] = request.secret_id

    if request.secret_region is not None:
        output["secret_region"] = request.secret_region

    return output


def marshal_CheckPEMChainRequest(
    request: CheckPEMChainRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="secret",
                    value=request.secret,
                    marshal_func=marshal_CheckPEMChainRequestSecretChain,
                ),
                OneOfPossibility(param="raw", value=request.raw, marshal_func=None),
            ]
        ),
    )

    if request.fqdn is not None:
        output["fqdn"] = request.fqdn

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_ScalewayLbBackendConfig(
    request: ScalewayLbBackendConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.lbs is not None:
        output["lbs"] = [marshal_ScalewayLb(item, defaults) for item in request.lbs]

    return output


def marshal_ScalewayS3BackendConfig(
    request: ScalewayS3BackendConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.bucket_name is not None:
        output["bucket_name"] = request.bucket_name

    if request.bucket_region is not None:
        output["bucket_region"] = request.bucket_region

    if request.is_website is not None:
        output["is_website"] = request.is_website

    return output


def marshal_CreateBackendStageRequest(
    request: CreateBackendStageRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="scaleway_s3",
                    value=request.scaleway_s3,
                    marshal_func=marshal_ScalewayS3BackendConfig,
                ),
                OneOfPossibility(
                    param="scaleway_lb",
                    value=request.scaleway_lb,
                    marshal_func=marshal_ScalewayLbBackendConfig,
                ),
            ]
        ),
    )

    return output


def marshal_CreateCacheStageRequest(
    request: CreateCacheStageRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="backend_stage_id",
                    value=request.backend_stage_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="waf_stage_id", value=request.waf_stage_id, marshal_func=None
                ),
                OneOfPossibility(
                    param="route_stage_id",
                    value=request.route_stage_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.fallback_ttl is not None:
        output["fallback_ttl"] = request.fallback_ttl

    if request.include_cookies is not None:
        output["include_cookies"] = request.include_cookies

    return output


def marshal_CreateDNSStageRequest(
    request: CreateDNSStageRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="tls_stage_id", value=request.tls_stage_id, marshal_func=None
                ),
                OneOfPossibility(
                    param="cache_stage_id",
                    value=request.cache_stage_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="backend_stage_id",
                    value=request.backend_stage_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.fqdns is not None:
        output["fqdns"] = request.fqdns

    return output


def marshal_CreatePipelineRequest(
    request: CreatePipelineRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_CreatePurgeRequestRequest(
    request: CreatePurgeRequestRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="assets", value=request.assets, marshal_func=None
                ),
                OneOfPossibility(param="all", value=request.all, marshal_func=None),
            ]
        ),
    )

    if request.pipeline_id is not None:
        output["pipeline_id"] = request.pipeline_id

    return output


def marshal_CreateRouteStageRequest(
    request: CreateRouteStageRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="waf_stage_id", value=request.waf_stage_id, marshal_func=None
                ),
            ]
        ),
    )

    return output


def marshal_TLSSecret(
    request: TLSSecret,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.secret_id is not None:
        output["secret_id"] = request.secret_id

    if request.region is not None:
        output["region"] = request.region
    else:
        output["region"] = defaults.default_region

    return output


def marshal_CreateTLSStageRequest(
    request: CreateTLSStageRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="cache_stage_id",
                    value=request.cache_stage_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="backend_stage_id",
                    value=request.backend_stage_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="route_stage_id",
                    value=request.route_stage_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="waf_stage_id", value=request.waf_stage_id, marshal_func=None
                ),
            ]
        ),
    )

    if request.secrets is not None:
        output["secrets"] = [
            marshal_TLSSecret(item, defaults) for item in request.secrets
        ]

    if request.managed_certificate is not None:
        output["managed_certificate"] = request.managed_certificate

    return output


def marshal_CreateWafStageRequest(
    request: CreateWafStageRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="backend_stage_id",
                    value=request.backend_stage_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.paranoia_level is not None:
        output["paranoia_level"] = request.paranoia_level

    if request.mode is not None:
        output["mode"] = request.mode

    return output


def marshal_SelectPlanRequest(
    request: SelectPlanRequest,
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


def marshal_SetHeadStageRequestAddNewHeadStage(
    request: SetHeadStageRequestAddNewHeadStage,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.new_stage_id is not None:
        output["new_stage_id"] = request.new_stage_id

    return output


def marshal_SetHeadStageRequestRemoveHeadStage(
    request: SetHeadStageRequestRemoveHeadStage,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.remove_stage_id is not None:
        output["remove_stage_id"] = request.remove_stage_id

    return output


def marshal_SetHeadStageRequestSwapHeadStage(
    request: SetHeadStageRequestSwapHeadStage,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.new_stage_id is not None:
        output["new_stage_id"] = request.new_stage_id

    if request.current_stage_id is not None:
        output["current_stage_id"] = request.current_stage_id

    return output


def marshal_SetHeadStageRequest(
    request: SetHeadStageRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="add_new_head_stage",
                    value=request.add_new_head_stage,
                    marshal_func=marshal_SetHeadStageRequestAddNewHeadStage,
                ),
                OneOfPossibility(
                    param="remove_head_stage",
                    value=request.remove_head_stage,
                    marshal_func=marshal_SetHeadStageRequestRemoveHeadStage,
                ),
                OneOfPossibility(
                    param="swap_head_stage",
                    value=request.swap_head_stage,
                    marshal_func=marshal_SetHeadStageRequestSwapHeadStage,
                ),
            ]
        ),
    )

    return output


def marshal_SetRouteRulesRequest(
    request: SetRouteRulesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.route_rules is not None:
        output["route_rules"] = [
            marshal_SetRouteRulesRequestRouteRule(item, defaults)
            for item in request.route_rules
        ]

    return output


def marshal_UpdateBackendStageRequest(
    request: UpdateBackendStageRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="scaleway_s3",
                    value=request.scaleway_s3,
                    marshal_func=marshal_ScalewayS3BackendConfig,
                ),
                OneOfPossibility(
                    param="scaleway_lb",
                    value=request.scaleway_lb,
                    marshal_func=marshal_ScalewayLbBackendConfig,
                ),
            ]
        ),
    )

    if request.pipeline_id is not None:
        output["pipeline_id"] = request.pipeline_id

    return output


def marshal_UpdateCacheStageRequest(
    request: UpdateCacheStageRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="backend_stage_id",
                    value=request.backend_stage_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="waf_stage_id", value=request.waf_stage_id, marshal_func=None
                ),
                OneOfPossibility(
                    param="route_stage_id",
                    value=request.route_stage_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.fallback_ttl is not None:
        output["fallback_ttl"] = request.fallback_ttl

    if request.include_cookies is not None:
        output["include_cookies"] = request.include_cookies

    return output


def marshal_UpdateDNSStageRequest(
    request: UpdateDNSStageRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="tls_stage_id", value=request.tls_stage_id, marshal_func=None
                ),
                OneOfPossibility(
                    param="cache_stage_id",
                    value=request.cache_stage_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="backend_stage_id",
                    value=request.backend_stage_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.fqdns is not None:
        output["fqdns"] = request.fqdns

    return output


def marshal_UpdatePipelineRequest(
    request: UpdatePipelineRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    return output


def marshal_UpdateRouteStageRequest(
    request: UpdateRouteStageRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="waf_stage_id", value=request.waf_stage_id, marshal_func=None
                ),
            ]
        ),
    )

    return output


def marshal_TLSSecretsConfig(
    request: TLSSecretsConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.tls_secrets is not None:
        output["tls_secrets"] = [
            marshal_TLSSecret(item, defaults) for item in request.tls_secrets
        ]

    return output


def marshal_UpdateTLSStageRequest(
    request: UpdateTLSStageRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="cache_stage_id",
                    value=request.cache_stage_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="backend_stage_id",
                    value=request.backend_stage_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="route_stage_id",
                    value=request.route_stage_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="waf_stage_id", value=request.waf_stage_id, marshal_func=None
                ),
            ]
        ),
    )

    if request.tls_secrets_config is not None:
        output["tls_secrets_config"] = marshal_TLSSecretsConfig(
            request.tls_secrets_config, defaults
        )

    if request.managed_certificate is not None:
        output["managed_certificate"] = request.managed_certificate

    return output


def marshal_UpdateWafStageRequest(
    request: UpdateWafStageRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="backend_stage_id",
                    value=request.backend_stage_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.mode is not None:
        output["mode"] = request.mode

    if request.paranoia_level is not None:
        output["paranoia_level"] = request.paranoia_level

    return output
