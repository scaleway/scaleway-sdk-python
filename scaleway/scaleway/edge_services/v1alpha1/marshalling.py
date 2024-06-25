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
    ScalewayLb,
    ScalewayLbBackendConfig,
    ScalewayS3BackendConfig,
    BackendStage,
    CacheStage,
    DNSStage,
    PipelineError,
    Pipeline,
    PurgeRequest,
    TLSSecret,
    TLSStage,
    CheckDomainResponse,
    CheckLbOriginResponse,
    CheckPEMChainResponse,
    ListBackendStagesResponse,
    ListCacheStagesResponse,
    ListDNSStagesResponse,
    ListPipelinesResponse,
    ListPurgeRequestsResponse,
    ListTLSStagesResponse,
    CheckDomainRequest,
    CheckLbOriginRequest,
    CheckPEMChainRequestSecretChain,
    CheckPEMChainRequest,
    CreateBackendStageRequest,
    CreateCacheStageRequest,
    CreateDNSStageRequest,
    CreatePipelineRequest,
    CreatePurgeRequestRequest,
    CreateTLSStageRequest,
    UpdateBackendStageRequest,
    UpdateCacheStageRequest,
    UpdateDNSStageRequest,
    UpdatePipelineRequest,
    TLSSecretsConfig,
    UpdateTLSStageRequest,
)


def unmarshal_ScalewayLb(data: Any) -> ScalewayLb:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ScalewayLb' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field

    field = data.get("frontend_id", None)
    if field is not None:
        args["frontend_id"] = field

    field = data.get("is_ssl", None)
    if field is not None:
        args["is_ssl"] = field
    else:
        args["is_ssl"] = None

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

    args: Dict[str, Any] = {}

    field = data.get("lbs", None)
    if field is not None:
        args["lbs"] = (
            [unmarshal_ScalewayLb(v) for v in field] if field is not None else None
        )

    return ScalewayLbBackendConfig(**args)


def unmarshal_ScalewayS3BackendConfig(data: Any) -> ScalewayS3BackendConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ScalewayS3BackendConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

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
        args["is_website"] = None

    return ScalewayS3BackendConfig(**args)


def unmarshal_BackendStage(data: Any) -> BackendStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BackendStage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("pipeline_id", None)
    if field is not None:
        args["pipeline_id"] = field
    else:
        args["pipeline_id"] = None

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

    return CacheStage(**args)


def unmarshal_DNSStage(data: Any) -> DNSStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DNSStage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("fqdns", None)
    if field is not None:
        args["fqdns"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("stage", None)
    if field is not None:
        args["stage"] = field

    field = data.get("code", None)
    if field is not None:
        args["code"] = field

    field = data.get("severity", None)
    if field is not None:
        args["severity"] = field

    field = data.get("message", None)
    if field is not None:
        args["message"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    return PipelineError(**args)


def unmarshal_Pipeline(data: Any) -> Pipeline:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Pipeline' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("description", None)
    if field is not None:
        args["description"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("errors", None)
    if field is not None:
        args["errors"] = (
            [unmarshal_PipelineError(v) for v in field] if field is not None else None
        )

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

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

    field = data.get("dns_stage_id", None)
    if field is not None:
        args["dns_stage_id"] = field
    else:
        args["dns_stage_id"] = None

    return Pipeline(**args)


def unmarshal_PurgeRequest(data: Any) -> PurgeRequest:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PurgeRequest' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("pipeline_id", None)
    if field is not None:
        args["pipeline_id"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("assets", None)
    if field is not None:
        args["assets"] = field
    else:
        args["assets"] = None

    field = data.get("all", None)
    if field is not None:
        args["all"] = field
    else:
        args["all"] = None

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


def unmarshal_TLSSecret(data: Any) -> TLSSecret:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TLSSecret' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("secret_id", None)
    if field is not None:
        args["secret_id"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    return TLSSecret(**args)


def unmarshal_TLSStage(data: Any) -> TLSStage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TLSStage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("secrets", None)
    if field is not None:
        args["secrets"] = (
            [unmarshal_TLSSecret(v) for v in field] if field is not None else None
        )

    field = data.get("managed_certificate", None)
    if field is not None:
        args["managed_certificate"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

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

    return TLSStage(**args)


def unmarshal_CheckDomainResponse(data: Any) -> CheckDomainResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckDomainResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("is_valid", None)
    if field is not None:
        args["is_valid"] = field

    return CheckDomainResponse(**args)


def unmarshal_CheckLbOriginResponse(data: Any) -> CheckLbOriginResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckLbOriginResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("is_valid", None)
    if field is not None:
        args["is_valid"] = field

    field = data.get("error_type", None)
    if field is not None:
        args["error_type"] = field

    return CheckLbOriginResponse(**args)


def unmarshal_CheckPEMChainResponse(data: Any) -> CheckPEMChainResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckPEMChainResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("is_valid", None)
    if field is not None:
        args["is_valid"] = field

    return CheckPEMChainResponse(**args)


def unmarshal_ListBackendStagesResponse(data: Any) -> ListBackendStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListBackendStagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("stages", None)
    if field is not None:
        args["stages"] = (
            [unmarshal_BackendStage(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListBackendStagesResponse(**args)


def unmarshal_ListCacheStagesResponse(data: Any) -> ListCacheStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListCacheStagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("stages", None)
    if field is not None:
        args["stages"] = (
            [unmarshal_CacheStage(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListCacheStagesResponse(**args)


def unmarshal_ListDNSStagesResponse(data: Any) -> ListDNSStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDNSStagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("stages", None)
    if field is not None:
        args["stages"] = (
            [unmarshal_DNSStage(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListDNSStagesResponse(**args)


def unmarshal_ListPipelinesResponse(data: Any) -> ListPipelinesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPipelinesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pipelines", None)
    if field is not None:
        args["pipelines"] = (
            [unmarshal_Pipeline(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListPipelinesResponse(**args)


def unmarshal_ListPurgeRequestsResponse(data: Any) -> ListPurgeRequestsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPurgeRequestsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("purge_requests", None)
    if field is not None:
        args["purge_requests"] = (
            [unmarshal_PurgeRequest(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListPurgeRequestsResponse(**args)


def unmarshal_ListTLSStagesResponse(data: Any) -> ListTLSStagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTLSStagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("stages", None)
    if field is not None:
        args["stages"] = (
            [unmarshal_TLSStage(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListTLSStagesResponse(**args)


def marshal_CheckDomainRequest(
    request: CheckDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.fqdn is not None:
        output["fqdn"] = request.fqdn

    if request.cname is not None:
        output["cname"] = request.cname

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_ScalewayLb(
    request: ScalewayLb,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.zone is not None:
        output["zone"] = request.zone or defaults.default_zone

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
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.lb is not None:
        output["lb"] = marshal_ScalewayLb(request.lb, defaults)

    return output


def marshal_CheckPEMChainRequestSecretChain(
    request: CheckPEMChainRequestSecretChain,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.secret_id is not None:
        output["secret_id"] = request.secret_id

    if request.secret_region is not None:
        output["secret_region"] = request.secret_region

    return output


def marshal_CheckPEMChainRequest(
    request: CheckPEMChainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("secret", request.secret),
                OneOfPossibility("raw", request.raw),
            ]
        ),
    )

    if request.fqdn is not None:
        output["fqdn"] = request.fqdn

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_ScalewayLbBackendConfig(
    request: ScalewayLbBackendConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.lbs is not None:
        output["lbs"] = [marshal_ScalewayLb(item, defaults) for item in request.lbs]

    return output


def marshal_ScalewayS3BackendConfig(
    request: ScalewayS3BackendConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

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
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("scaleway_s3", request.scaleway_s3),
                OneOfPossibility("scaleway_lb", request.scaleway_lb),
            ]
        ),
    )

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_CreateCacheStageRequest(
    request: CreateCacheStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("backend_stage_id", request.backend_stage_id),
            ]
        ),
    )

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.fallback_ttl is not None:
        output["fallback_ttl"] = request.fallback_ttl

    return output


def marshal_CreateDNSStageRequest(
    request: CreateDNSStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("tls_stage_id", request.tls_stage_id),
                OneOfPossibility("cache_stage_id", request.cache_stage_id),
                OneOfPossibility("backend_stage_id", request.backend_stage_id),
            ]
        ),
    )

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.fqdns is not None:
        output["fqdns"] = request.fqdns

    return output


def marshal_CreatePipelineRequest(
    request: CreatePipelineRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("dns_stage_id", request.dns_stage_id),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_CreatePurgeRequestRequest(
    request: CreatePurgeRequestRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("assets", request.assets),
                OneOfPossibility("all", request.all),
            ]
        ),
    )

    if request.pipeline_id is not None:
        output["pipeline_id"] = request.pipeline_id

    return output


def marshal_TLSSecret(
    request: TLSSecret,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.secret_id is not None:
        output["secret_id"] = request.secret_id

    if request.region is not None:
        output["region"] = request.region or defaults.default_region

    return output


def marshal_CreateTLSStageRequest(
    request: CreateTLSStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("cache_stage_id", request.cache_stage_id),
                OneOfPossibility("backend_stage_id", request.backend_stage_id),
            ]
        ),
    )

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.secrets is not None:
        output["secrets"] = [
            marshal_TLSSecret(item, defaults) for item in request.secrets
        ]

    if request.managed_certificate is not None:
        output["managed_certificate"] = request.managed_certificate

    return output


def marshal_UpdateBackendStageRequest(
    request: UpdateBackendStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("scaleway_s3", request.scaleway_s3),
                OneOfPossibility("scaleway_lb", request.scaleway_lb),
            ]
        ),
    )

    return output


def marshal_UpdateCacheStageRequest(
    request: UpdateCacheStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("backend_stage_id", request.backend_stage_id),
            ]
        ),
    )

    if request.fallback_ttl is not None:
        output["fallback_ttl"] = request.fallback_ttl

    return output


def marshal_UpdateDNSStageRequest(
    request: UpdateDNSStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("tls_stage_id", request.tls_stage_id),
                OneOfPossibility("cache_stage_id", request.cache_stage_id),
                OneOfPossibility("backend_stage_id", request.backend_stage_id),
            ]
        ),
    )

    if request.fqdns is not None:
        output["fqdns"] = request.fqdns

    return output


def marshal_UpdatePipelineRequest(
    request: UpdatePipelineRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("dns_stage_id", request.dns_stage_id),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    return output


def marshal_TLSSecretsConfig(
    request: TLSSecretsConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.tls_secrets is not None:
        output["tls_secrets"] = [
            marshal_TLSSecret(item, defaults) for item in request.tls_secrets
        ]

    return output


def marshal_UpdateTLSStageRequest(
    request: UpdateTLSStageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("cache_stage_id", request.cache_stage_id),
                OneOfPossibility("backend_stage_id", request.backend_stage_id),
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
