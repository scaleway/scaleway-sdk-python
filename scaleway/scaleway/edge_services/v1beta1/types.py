# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    Zone as ScwZone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class DNSStageType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    AUTO = "auto"
    MANAGED = "managed"
    CUSTOM = "custom"

    def __str__(self) -> str:
        return str(self.value)


class LbOriginError(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    TIMEOUT = "timeout"
    CONNECTION_REFUSED = "connection_refused"
    TLS_ERROR = "tls_error"

    def __str__(self) -> str:
        return str(self.value)


class ListBackendStagesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListCacheStagesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListDNSStagesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPipelinesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPipelinesWithStagesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPurgeRequestsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRouteStagesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListTLSStagesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListWafStagesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class PipelineErrorCode(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_CODE = "unknown_code"
    DNS_INVALID_FORMAT = "dns_invalid_format"
    DNS_INVALID_TLD = "dns_invalid_tld"
    DNS_FORBIDDEN_ROOT_DOMAIN = "dns_forbidden_root_domain"
    DNS_FORBIDDEN_SCW_CLOUD = "dns_forbidden_scw_cloud"
    DNS_DOMAIN_DONT_EXIST = "dns_domain_dont_exist"
    DNS_CNAME_DONT_EXIST = "dns_cname_dont_exist"
    DNS_CNAME_RESOLVE = "dns_cname_resolve"
    DNS_FQDN_ALREADY_EXISTS = "dns_fqdn_already_exists"
    DNS_FQDN_ALREADY_IN_USE = "dns_fqdn_already_in_use"
    TLS_CERT_DELETED = "tls_cert_deleted"
    TLS_CERT_DISABLED = "tls_cert_disabled"
    TLS_CERT_EXPIRED = "tls_cert_expired"
    TLS_CERT_INVALID_FORMAT = "tls_cert_invalid_format"
    TLS_CERT_MISSING = "tls_cert_missing"
    TLS_CHAIN_ORDER = "tls_chain_order"
    TLS_KEY_INVALID_FORMAT = "tls_key_invalid_format"
    TLS_KEY_MISSING = "tls_key_missing"
    TLS_KEY_TOO_MANY = "tls_key_too_many"
    TLS_MANAGED_DOMAIN_RATE_LIMIT = "tls_managed_domain_rate_limit"
    TLS_MANAGED_INTERNAL = "tls_managed_internal"
    TLS_PAIR_MISMATCH = "tls_pair_mismatch"
    TLS_ROOT_INCONSISTENT = "tls_root_inconsistent"
    TLS_ROOT_INCORRECT = "tls_root_incorrect"
    TLS_ROOT_MISSING = "tls_root_missing"
    TLS_SAN_MISMATCH = "tls_san_mismatch"
    TLS_SELF_SIGNED = "tls_self_signed"
    TLS_CAA_MALFUNCTION = "tls_caa_malfunction"
    PIPELINE_INVALID_WORKFLOW = "pipeline_invalid_workflow"
    PIPELINE_MISSING_HEAD_STAGE = "pipeline_missing_head_stage"
    PIPELINE_WEBSOCKET_LIMIT = "pipeline_websocket_limit"

    def __str__(self) -> str:
        return str(self.value)


class PipelineErrorSeverity(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SEVERITY = "unknown_severity"
    WARNING = "warning"
    CRITICAL = "critical"

    def __str__(self) -> str:
        return str(self.value)


class PipelineErrorStage(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STAGE = "unknown_stage"
    DNS = "dns"
    TLS = "tls"
    CACHE = "cache"
    BACKEND = "backend"

    def __str__(self) -> str:
        return str(self.value)


class PipelineErrorType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    RUNTIME = "runtime"
    CONFIG = "config"

    def __str__(self) -> str:
        return str(self.value)


class PipelineStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    READY = "ready"
    ERROR = "error"
    PENDING = "pending"
    WARNING = "warning"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class PlanName(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_NAME = "unknown_name"
    STARTER = "starter"
    PROFESSIONAL = "professional"
    ADVANCED = "advanced"

    def __str__(self) -> str:
        return str(self.value)


class PurgeRequestStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    DONE = "done"
    ERROR = "error"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)


class RuleHttpMatchMethodFilter(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_METHOD_FILTER = "unknown_method_filter"
    GET = "get"
    POST = "post"
    PUT = "put"
    PATCH = "patch"
    DELETE = "delete"
    HEAD = "head"
    OPTIONS = "options"

    def __str__(self) -> str:
        return str(self.value)


class RuleHttpMatchPathFilterPathFilterType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_PATH_FILTER = "unknown_path_filter"
    REGEX = "regex"

    def __str__(self) -> str:
        return str(self.value)


class SearchBackendStagesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class SearchRouteRulesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class SearchWafStagesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class WafStageMode(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_MODE = "unknown_mode"
    DISABLE = "disable"
    LOG_ONLY = "log_only"
    ENABLE = "enable"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class ScalewayLb:
    id: str
    """
    ID of the Load Balancer.
    """

    zone: ScwZone
    """
    Zone of the Load Balancer.
    """

    frontend_id: str
    """
    ID of the frontend linked to the Load Balancer.
    """

    is_ssl: Optional[bool] = False
    """
    Defines whether the Load Balancer's frontend handles SSL connections.
    """

    domain_name: Optional[str] = None
    """
    Fully Qualified Domain Name (in the format subdomain.example.com) to use in HTTP requests sent towards your Load Balancer.
    """

    has_websocket: Optional[bool] = False
    """
    Defines whether to forward websocket requests to the load balancer.
    """


@dataclass
class RuleHttpMatchPathFilter:
    path_filter_type: RuleHttpMatchPathFilterPathFilterType
    """
    Type of filter to match for the HTTP URL path. For now, all path filters must be written in regex and use the `regex` type.
    """

    value: str
    """
    Value to be matched for the HTTP URL path.
    """


@dataclass
class ScalewayLbBackendConfig:
    lbs: list[ScalewayLb]
    """
    Load Balancer information.
    """


@dataclass
class ScalewayS3BackendConfig:
    bucket_name: Optional[str] = None
    """
    Name of the Bucket.
    """

    bucket_region: Optional[str] = None
    """
    Region of the Bucket.
    """

    is_website: Optional[bool] = False
    """
    Defines whether the bucket website feature is enabled.
    """


@dataclass
class ScalewayServerlessContainerBackendConfig:
    region: ScwRegion
    """
    Region to target. If none is passed will use default region from the config.
    """

    container_id: str


@dataclass
class ScalewayServerlessFunctionBackendConfig:
    region: ScwRegion
    """
    Region to target. If none is passed will use default region from the config.
    """

    function_id: str


@dataclass
class PipelineError:
    stage: PipelineErrorStage
    code: PipelineErrorCode
    severity: PipelineErrorSeverity
    message: str
    type_: PipelineErrorType


@dataclass
class TLSSecret:
    secret_id: str
    """
    ID of the Secret.
    """

    region: ScwRegion
    """
    Region of the Secret.
    """


@dataclass
class RuleHttpMatch:
    method_filters: list[RuleHttpMatchMethodFilter]
    """
    HTTP methods to filter for. A request using any of these methods will be considered to match the rule. Possible values are `get`, `post`, `put`, `patch`, `delete`, `head`, `options`. All methods will match if none is provided.
    """

    path_filter: Optional[RuleHttpMatchPathFilter] = None
    """
    HTTP URL path to filter for. A request whose path matches the given filter will be considered to match the rule. All paths will match if none is provided.
    """


@dataclass
class BackendStage:
    id: str
    """
    ID of the backend stage.
    """

    pipeline_id: str
    """
    Pipeline ID the backend stage belongs to.
    """

    created_at: Optional[datetime] = None
    """
    Date the backend stage was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date the backend stage was last updated.
    """

    scaleway_s3: Optional[ScalewayS3BackendConfig] = None

    scaleway_lb: Optional[ScalewayLbBackendConfig] = None

    scaleway_serverless_container: Optional[
        ScalewayServerlessContainerBackendConfig
    ] = None

    scaleway_serverless_function: Optional[ScalewayServerlessFunctionBackendConfig] = (
        None
    )


@dataclass
class CacheStage:
    id: str
    """
    ID of the cache stage.
    """

    pipeline_id: str
    """
    Pipeline ID the cache stage belongs to.
    """

    include_cookies: bool
    """
    Defines whether responses to requests with cookies must be stored in the cache.
    """

    fallback_ttl: Optional[str] = None
    """
    Time To Live (TTL) in seconds. Defines how long content is cached.
    """

    created_at: Optional[datetime] = None
    """
    Date the cache stage was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date the cache stage was last updated.
    """

    backend_stage_id: Optional[str] = None

    waf_stage_id: Optional[str] = None

    route_stage_id: Optional[str] = None


@dataclass
class DNSStage:
    id: str
    """
    ID of the DNS stage.
    """

    default_fqdn: str
    """
    Default Fully Qualified Domain Name attached to the stage.
    """

    fqdns: list[str]
    """
    List of additional (custom) Fully Qualified Domain Names attached to the stage.
    """

    type_: DNSStageType
    """
    Type of the stage.
    """

    pipeline_id: str
    """
    Pipeline ID the DNS stage belongs to.
    """

    created_at: Optional[datetime] = None
    """
    Date the DNS stage was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date the DNS stage was last updated.
    """

    tls_stage_id: Optional[str] = None

    cache_stage_id: Optional[str] = None

    backend_stage_id: Optional[str] = None


@dataclass
class Pipeline:
    id: str
    """
    ID of the pipeline.
    """

    name: str
    """
    Name of the pipeline.
    """

    description: str
    """
    Description of the pipeline.
    """

    status: PipelineStatus
    """
    Status of the pipeline.
    """

    errors: list[PipelineError]
    """
    Errors of the pipeline.
    """

    project_id: str
    """
    Project ID of the pipeline.
    """

    organization_id: str
    """
    Organization ID of the pipeline.
    """

    created_at: Optional[datetime] = None
    """
    Date the pipeline was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date the pipeline was last updated.
    """


@dataclass
class RouteStage:
    id: str
    """
    ID of the route stage.
    """

    pipeline_id: str
    """
    Pipeline ID the route stage belongs to.
    """

    created_at: Optional[datetime] = None
    """
    Date the route stage was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date the route stage was last updated.
    """

    waf_stage_id: Optional[str] = None


@dataclass
class TLSStage:
    id: str
    """
    ID of the TLS stage.
    """

    secrets: list[TLSSecret]
    """
    Secret (from Scaleway Secret Manager) containing your custom certificate.
    """

    managed_certificate: bool
    """
    True when Scaleway generates and manages a Let's Encrypt certificate for the TLS stage/custom endpoint.
    """

    pipeline_id: str
    """
    Pipeline ID the TLS stage belongs to.
    """

    certificate_expires_at: Optional[datetime] = None
    """
    Expiration date of the certificate.
    """

    created_at: Optional[datetime] = None
    """
    Date the TLS stage was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date the TLS stage was last updated.
    """

    cache_stage_id: Optional[str] = None

    backend_stage_id: Optional[str] = None

    waf_stage_id: Optional[str] = None

    route_stage_id: Optional[str] = None


@dataclass
class WafStage:
    id: str
    """
    ID of the WAF stage.
    """

    pipeline_id: str
    """
    Pipeline ID the WAF stage belongs to.
    """

    mode: WafStageMode
    """
    Mode defining WAF behavior (`disable`/`log_only`/`enable`).
    """

    paranoia_level: int
    """
    Sensitivity level (`1`,`2`,`3`,`4`) to use when classifying requests as malicious. With a high level, requests are more likely to be classed as malicious, and false positives are expected. With a lower level, requests are more likely to be classed as benign.
    """

    created_at: Optional[datetime] = None
    """
    Date the WAF stage was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date the WAF stage was last updated.
    """

    backend_stage_id: Optional[str] = None


@dataclass
class SetRouteRulesRequestRouteRule:
    rule_http_match: Optional[RuleHttpMatch] = None

    backend_stage_id: Optional[str] = None


@dataclass
class RouteRule:
    position: int
    """
    Position of the rule which determines the order of processing within the route stage.
    """

    route_stage_id: str
    """
    Route stage ID the route rule belongs to.
    """

    rule_http_match: Optional[RuleHttpMatch] = None

    backend_stage_id: Optional[str] = None


@dataclass
class CheckPEMChainRequestSecretChain:
    secret_id: str
    secret_region: str


@dataclass
class PlanDetails:
    plan_name: PlanName
    """
    Subscription plan name.
    """

    package_gb: int
    """
    Amount of egress data from cache included in subscription plan.
    """

    pipeline_limit: int
    """
    Number of pipelines included in subscription plan.
    """

    waf_requests: int
    """
    Number of WAF requests included in subscription plan.
    """

    backend_limit: int
    """
    Number of backends per pipeline included in subscription plan.
    """


@dataclass
class PlanUsageDetails:
    plan_cost: Optional[Money] = None
    """
    Cost to date (this month) for the corresponding Edge Services subscription plan.
    """


@dataclass
class HeadStageResponseHeadStage:
    dns_stage_id: Optional[str] = None


@dataclass
class ListHeadStagesResponseHeadStage:
    dns_stage_id: Optional[str] = None


@dataclass
class PipelineStages:
    dns_stages: list[DNSStage]
    tls_stages: list[TLSStage]
    cache_stages: list[CacheStage]
    backend_stages: list[BackendStage]
    waf_stages: list[WafStage]
    route_stages: list[RouteStage]
    pipeline: Optional[Pipeline] = None


@dataclass
class PurgeRequest:
    id: str
    """
    ID of the purge request.
    """

    pipeline_id: str
    """
    Pipeline ID the purge request belongs to.
    """

    status: PurgeRequestStatus
    """
    Status of the purge request.
    """

    created_at: Optional[datetime] = None
    """
    Date the purge request was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date the purge request was last updated.
    """

    assets: Optional[list[str]] = field(default_factory=list)

    all: Optional[bool] = False


@dataclass
class SetHeadStageRequestAddNewHeadStage:
    new_stage_id: str


@dataclass
class SetHeadStageRequestRemoveHeadStage:
    remove_stage_id: str


@dataclass
class SetHeadStageRequestSwapHeadStage:
    new_stage_id: str
    current_stage_id: str


@dataclass
class TLSSecretsConfig:
    tls_secrets: list[TLSSecret]
    """
    Secret information (from Secret Manager).
    """


@dataclass
class AddRouteRulesRequest:
    route_stage_id: str
    """
    ID of the route stage to update.
    """

    route_rules: Optional[list[SetRouteRulesRequestRouteRule]] = field(
        default_factory=list
    )
    """
    List of rules to be checked against every HTTP request. The first matching rule will forward the request to its specified backend stage. If no rules are matched, the request is forwarded to the WAF stage defined by `waf_stage_id`.
    """

    after_position: Optional[int] = 0

    before_position: Optional[int] = 0


@dataclass
class AddRouteRulesResponse:
    route_rules: list[RouteRule]
    """
    List of rules to be checked against every HTTP request. The first matching rule will forward the request to its specified backend stage. If no rules are matched, the request is forwarded to the WAF stage defined by `waf_stage_id`.
    """


@dataclass
class CheckDomainRequest:
    fqdn: str
    cname: str
    project_id: Optional[str] = None


@dataclass
class CheckDomainResponse:
    is_valid: bool


@dataclass
class CheckLbOriginRequest:
    lb: Optional[ScalewayLb] = None


@dataclass
class CheckLbOriginResponse:
    is_valid: bool
    error_type: LbOriginError


@dataclass
class CheckPEMChainRequest:
    fqdn: str
    project_id: Optional[str] = None
    secret: Optional[CheckPEMChainRequestSecretChain] = None

    raw: Optional[str] = None


@dataclass
class CheckPEMChainResponse:
    is_valid: bool


@dataclass
class CreateBackendStageRequest:
    pipeline_id: str
    """
    Pipeline ID the Backend stage belongs to.
    """

    scaleway_s3: Optional[ScalewayS3BackendConfig] = None

    scaleway_lb: Optional[ScalewayLbBackendConfig] = None

    scaleway_serverless_container: Optional[
        ScalewayServerlessContainerBackendConfig
    ] = None

    scaleway_serverless_function: Optional[ScalewayServerlessFunctionBackendConfig] = (
        None
    )


@dataclass
class CreateCacheStageRequest:
    pipeline_id: str
    """
    Pipeline ID the Cache stage belongs to.
    """

    fallback_ttl: Optional[str] = None
    """
    Time To Live (TTL) in seconds. Defines how long content is cached.
    """

    include_cookies: Optional[bool] = False
    """
    Defines whether responses to requests with cookies must be stored in the cache.
    """

    backend_stage_id: Optional[str] = None

    waf_stage_id: Optional[str] = None

    route_stage_id: Optional[str] = None


@dataclass
class CreateDNSStageRequest:
    pipeline_id: str
    """
    Pipeline ID the DNS stage belongs to.
    """

    fqdns: Optional[list[str]] = field(default_factory=list)
    """
    Fully Qualified Domain Name (in the format subdomain.example.com) to attach to the stage.
    """

    tls_stage_id: Optional[str] = None

    cache_stage_id: Optional[str] = None

    backend_stage_id: Optional[str] = None


@dataclass
class CreatePipelineRequest:
    name: str
    """
    Name of the pipeline.
    """

    description: str
    """
    Description of the pipeline.
    """

    project_id: Optional[str] = None
    """
    Project ID in which the pipeline will be created.
    """


@dataclass
class CreatePurgeRequestRequest:
    pipeline_id: str
    """
    Pipeline ID in which the purge request will be created.
    """

    assets: Optional[list[str]] = field(default_factory=list)

    all: Optional[bool] = False


@dataclass
class CreateRouteStageRequest:
    pipeline_id: str
    """
    Pipeline ID the route stage belongs to.
    """

    waf_stage_id: Optional[str] = None


@dataclass
class CreateTLSStageRequest:
    pipeline_id: str
    """
    Pipeline ID the TLS stage belongs to.
    """

    secrets: Optional[list[TLSSecret]] = field(default_factory=list)
    """
    Secret (from Scaleway Secret Manager) containing your custom certificate.
    """

    managed_certificate: Optional[bool] = False
    """
    True when Scaleway generates and manages a Let's Encrypt certificate for the TLS stage/custom endpoint.
    """

    cache_stage_id: Optional[str] = None

    backend_stage_id: Optional[str] = None

    route_stage_id: Optional[str] = None

    waf_stage_id: Optional[str] = None


@dataclass
class CreateWafStageRequest:
    pipeline_id: str
    """
    Pipeline ID the WAF stage belongs to.
    """

    paranoia_level: int
    """
    Sensitivity level (`1`,`2`,`3`,`4`) to use when classifying requests as malicious. With a high level, requests are more likely to be classed as malicious, and false positives are expected. With a lower level, requests are more likely to be classed as benign.
    """

    mode: Optional[WafStageMode] = WafStageMode.UNKNOWN_MODE
    """
    Mode defining WAF behavior (`disable`/`log_only`/`enable`).
    """

    backend_stage_id: Optional[str] = None


@dataclass
class DeleteBackendStageRequest:
    backend_stage_id: str
    """
    ID of the backend stage to delete.
    """


@dataclass
class DeleteCacheStageRequest:
    cache_stage_id: str
    """
    ID of the cache stage to delete.
    """


@dataclass
class DeleteCurrentPlanRequest:
    project_id: Optional[str] = None


@dataclass
class DeleteDNSStageRequest:
    dns_stage_id: str
    """
    ID of the DNS stage to delete.
    """


@dataclass
class DeletePipelineRequest:
    pipeline_id: str
    """
    ID of the pipeline to delete.
    """


@dataclass
class DeleteRouteStageRequest:
    route_stage_id: str
    """
    ID of the route stage to delete.
    """


@dataclass
class DeleteTLSStageRequest:
    tls_stage_id: str
    """
    ID of the TLS stage to delete.
    """


@dataclass
class DeleteWafStageRequest:
    waf_stage_id: str
    """
    ID of the WAF stage to delete.
    """


@dataclass
class GetBackendStageRequest:
    backend_stage_id: str
    """
    ID of the requested backend stage.
    """


@dataclass
class GetBillingRequest:
    project_id: Optional[str] = None


@dataclass
class GetBillingResponse:
    pipeline_number: int
    """
    Total number of pipelines currently configured.
    """

    current_plan_cache_usage: int
    """
    Total amount of data egressed from the cache in gigabytes from the beginning of the month, for the active subscription plan.
    """

    extra_cache_usage: int
    """
    Total amount of extra data egressed from cache in gigabytes from the beginning of the month, not included in the subscription plans.
    """

    current_plan_waf_usage: int
    """
    Total number of requests processed by the WAF since the beginning of the current month, for the active subscription plan.
    """

    extra_waf_usage: int
    """
    Total number of extra requests processed by the WAF from the beginning of the month, not included in the subscription plans.
    """

    plans_usage_details: dict[str, PlanUsageDetails]
    """
    Detailed costs and usage for all Edge Services subscription plans that were activated during the month.
    """

    current_plan: Optional[PlanDetails] = None
    """
    Information on the currently-selected, active Edge Services subscription plan.
    """

    plan_cost: Optional[Money] = None
    """
    Cost to date (this month) for Edge Service subscription plans. This comprises the pro-rata cost of the current subscription plan, and any previous subscription plans that were active earlier in the month.
    """

    extra_pipelines_cost: Optional[Money] = None
    """
    Cost to date (this month) of pipelines not included in the subscription plans.
    """

    extra_cache_cost: Optional[Money] = None
    """
    Cost to date (this month) of the data egressed from the cache that is not included in the subscription plans.
    """

    extra_waf_cost: Optional[Money] = None
    """
    Cost to date (this month) of the extra requests processed by the WAF that were not included in the subscription plans.
    """

    waf_add_on: Optional[Money] = None
    """
    Cost of activating WAF add-on (where subscription plan does not include WAF).
    """

    total_cost: Optional[Money] = None
    """
    Total cost to date (this month) of all Edge Services resources including active subscription plan, previously active plans, extra pipelines and extra egress cache data.
    """


@dataclass
class GetCacheStageRequest:
    cache_stage_id: str
    """
    ID of the requested cache stage.
    """


@dataclass
class GetCurrentPlanRequest:
    project_id: Optional[str] = None


@dataclass
class GetDNSStageRequest:
    dns_stage_id: str
    """
    ID of the requested DNS stage.
    """


@dataclass
class GetPipelineRequest:
    pipeline_id: str
    """
    ID of the requested pipeline.
    """


@dataclass
class GetPurgeRequestRequest:
    purge_request_id: str
    """
    ID of the requested purge request.
    """


@dataclass
class GetRouteStageRequest:
    route_stage_id: str
    """
    ID of the requested route stage.
    """


@dataclass
class GetTLSStageRequest:
    tls_stage_id: str
    """
    ID of the requested TLS stage.
    """


@dataclass
class GetWafStageRequest:
    waf_stage_id: str
    """
    ID of the requested WAF stage.
    """


@dataclass
class HeadStageResponse:
    head_stage: Optional[HeadStageResponseHeadStage] = None
    """
    Modified or created head stage.
    """


@dataclass
class ListBackendStagesRequest:
    pipeline_id: str
    """
    Pipeline ID to filter for. Only backend stages from this pipeline will be returned.
    """

    order_by: Optional[ListBackendStagesRequestOrderBy] = (
        ListBackendStagesRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order of backend stages in the response.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of backend stages to return per page.
    """

    bucket_name: Optional[str] = None
    """
    Bucket name to filter for. Only backend stages from this Bucket will be returned.
    """

    bucket_region: Optional[str] = None
    """
    Bucket region to filter for. Only backend stages with buckets in this region will be returned.
    """

    lb_id: Optional[str] = None
    """
    Load Balancer ID to filter for. Only backend stages with this Load Balancer will be returned.
    """


@dataclass
class ListBackendStagesResponse:
    stages: list[BackendStage]
    """
    Paginated list of backend stages.
    """

    total_count: int
    """
    Count of all backend stages matching the requested criteria.
    """


@dataclass
class ListCacheStagesRequest:
    pipeline_id: str
    """
    Pipeline ID to filter for. Only cache stages from this pipeline will be returned.
    """

    order_by: Optional[ListCacheStagesRequestOrderBy] = (
        ListCacheStagesRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order of cache stages in the response.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of cache stages to return per page.
    """


@dataclass
class ListCacheStagesResponse:
    stages: list[CacheStage]
    """
    Paginated list of cache stages.
    """

    total_count: int
    """
    Count of all cache stages matching the requested criteria.
    """


@dataclass
class ListDNSStagesRequest:
    pipeline_id: str
    """
    Pipeline ID to filter for. Only DNS stages from this pipeline will be returned.
    """

    order_by: Optional[ListDNSStagesRequestOrderBy] = (
        ListDNSStagesRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order of DNS stages in the response.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of DNS stages to return per page.
    """

    fqdn: Optional[str] = None
    """
    Fully Qualified Domain Name to filter for (in the format subdomain.example.com). Only DNS stages with this FQDN will be returned.
    """


@dataclass
class ListDNSStagesResponse:
    stages: list[DNSStage]
    """
    Paginated list of DNS stages.
    """

    total_count: int
    """
    Count of all DNS stages matching the requested criteria.
    """


@dataclass
class ListHeadStagesRequest:
    pipeline_id: str
    """
    ID of the pipeline to update.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of head stages to return per page.
    """


@dataclass
class ListHeadStagesResponse:
    head_stages: list[ListHeadStagesResponseHeadStage]
    """
    Number of head stages to return per page.
    """

    total_count: int
    """
    Count of all head stages matching the requested pipeline_id.
    """


@dataclass
class ListPipelinesRequest:
    order_by: Optional[ListPipelinesRequestOrderBy] = (
        ListPipelinesRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order of pipelines in the response.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of pipelines to return per page.
    """

    name: Optional[str] = None
    """
    Pipeline name to filter for. Only pipelines with this string within their name will be returned.
    """

    organization_id: Optional[str] = None
    """
    Organization ID to filter for. Only pipelines from this Organization will be returned.
    """

    project_id: Optional[str] = None
    """
    Project ID to filter for. Only pipelines from this Project will be returned.
    """

    has_backend_stage_lb: Optional[bool] = False
    """
    Filter on backend stage. Only pipelines with a Load Balancer origin will be returned.
    """


@dataclass
class ListPipelinesResponse:
    pipelines: list[Pipeline]
    """
    Paginated list of pipelines.
    """

    total_count: int
    """
    Count of all pipelines matching the requested criteria.
    """


@dataclass
class ListPipelinesWithStagesRequest:
    order_by: Optional[ListPipelinesWithStagesRequestOrderBy] = None
    page: Optional[int] = None
    page_size: Optional[int] = None
    name: Optional[str] = None
    organization_id: Optional[str] = None
    project_id: Optional[str] = None


@dataclass
class ListPipelinesWithStagesResponse:
    pipelines: list[PipelineStages]
    total_count: int


@dataclass
class ListPlansResponse:
    total_count: int
    plans: list[PlanDetails]


@dataclass
class ListPurgeRequestsRequest:
    order_by: Optional[ListPurgeRequestsRequestOrderBy] = (
        ListPurgeRequestsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order of purge requests in the response.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of purge requests to return per page.
    """

    organization_id: Optional[str] = None
    """
    Organization ID to filter for. Only purge requests from this Project will be returned.
    """

    project_id: Optional[str] = None
    """
    Project ID to filter for. Only purge requests from this Project will be returned.
    """

    pipeline_id: Optional[str] = None
    """
    Pipeline ID to filter for. Only purge requests from this pipeline will be returned.
    """


@dataclass
class ListPurgeRequestsResponse:
    purge_requests: list[PurgeRequest]
    """
    Paginated list of purge requests.
    """

    total_count: int
    """
    Count of all purge requests matching the requested criteria.
    """


@dataclass
class ListRouteRulesRequest:
    route_stage_id: str
    """
    Route stage ID to filter for. Only route rules from this route stage will be returned.
    """


@dataclass
class ListRouteRulesResponse:
    route_rules: list[RouteRule]
    """
    List of rules to be checked against every HTTP request. The first matching rule will forward the request to its specified backend stage. If no rules are matched, the request is forwarded to the WAF stage defined by `waf_stage_id`.
    """

    total_count: int
    """
    Count of all route rules matching the requested criteria.
    """


@dataclass
class ListRouteStagesRequest:
    pipeline_id: str
    """
    Pipeline ID to filter for. Only route stages from this pipeline will be returned.
    """

    order_by: Optional[ListRouteStagesRequestOrderBy] = (
        ListRouteStagesRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order of route stages in the response.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of route stages to return per page.
    """


@dataclass
class ListRouteStagesResponse:
    stages: list[RouteStage]
    """
    Paginated list of summarized route stages.
    """

    total_count: int
    """
    Count of all route stages matching the requested criteria.
    """


@dataclass
class ListTLSStagesRequest:
    pipeline_id: str
    """
    Pipeline ID to filter for. Only TLS stages from this pipeline will be returned.
    """

    order_by: Optional[ListTLSStagesRequestOrderBy] = (
        ListTLSStagesRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order of TLS stages in the response.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of TLS stages to return per page.
    """

    secret_id: Optional[str] = None
    """
    Secret ID to filter for. Only TLS stages with this Secret ID will be returned.
    """

    secret_region: Optional[str] = None
    """
    Secret region to filter for. Only TLS stages with a Secret in this region will be returned.
    """


@dataclass
class ListTLSStagesResponse:
    stages: list[TLSStage]
    """
    Paginated list of TLS stages.
    """

    total_count: int
    """
    Count of all TLS stages matching the requested criteria.
    """


@dataclass
class ListWafStagesRequest:
    pipeline_id: str
    """
    Pipeline ID to filter for. Only WAF stages from this pipeline will be returned.
    """

    order_by: Optional[ListWafStagesRequestOrderBy] = (
        ListWafStagesRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order of WAF stages in the response.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of WAF stages to return per page.
    """


@dataclass
class ListWafStagesResponse:
    stages: list[WafStage]
    """
    Paginated list of WAF stages.
    """

    total_count: int
    """
    Count of all WAF stages matching the requested criteria.
    """


@dataclass
class Plan:
    plan_name: PlanName


@dataclass
class SearchBackendStagesRequest:
    order_by: Optional[SearchBackendStagesRequestOrderBy] = None
    page: Optional[int] = None
    page_size: Optional[int] = None
    project_id: Optional[str] = None
    bucket_name: Optional[str] = None
    bucket_region: Optional[str] = None
    lb_id: Optional[str] = None


@dataclass
class SearchRouteRulesRequest:
    order_by: Optional[SearchRouteRulesRequestOrderBy] = None
    page: Optional[int] = None
    page_size: Optional[int] = None
    organization_id: Optional[str] = None
    project_id: Optional[str] = None


@dataclass
class SearchWafStagesRequest:
    order_by: Optional[SearchWafStagesRequestOrderBy] = None
    page: Optional[int] = None
    page_size: Optional[int] = None
    project_id: Optional[str] = None


@dataclass
class SelectPlanRequest:
    project_id: Optional[str] = None
    plan_name: Optional[PlanName] = None


@dataclass
class SetHeadStageRequest:
    pipeline_id: str
    """
    ID of the pipeline to update.
    """

    add_new_head_stage: Optional[SetHeadStageRequestAddNewHeadStage] = None

    remove_head_stage: Optional[SetHeadStageRequestRemoveHeadStage] = None

    swap_head_stage: Optional[SetHeadStageRequestSwapHeadStage] = None


@dataclass
class SetRouteRulesRequest:
    route_stage_id: str
    """
    ID of the route stage to update.
    """

    route_rules: Optional[list[SetRouteRulesRequestRouteRule]] = field(
        default_factory=list
    )
    """
    List of rules to be checked against every HTTP request. The first matching rule will forward the request to its specified backend stage. If no rules are matched, the request is forwarded to the WAF stage defined by `waf_stage_id`.
    """


@dataclass
class SetRouteRulesResponse:
    route_rules: list[RouteRule]
    """
    List of rules to be checked against every HTTP request. The first matching rule will forward the request to its specified backend stage. If no rules are matched, the request is forwarded to the WAF stage defined by `waf_stage_id`.
    """


@dataclass
class UpdateBackendStageRequest:
    backend_stage_id: str
    """
    ID of the backend stage to update.
    """

    pipeline_id: str
    """
    Pipeline ID the Backend stage belongs to.
    """

    scaleway_s3: Optional[ScalewayS3BackendConfig] = None

    scaleway_lb: Optional[ScalewayLbBackendConfig] = None

    scaleway_serverless_container: Optional[
        ScalewayServerlessContainerBackendConfig
    ] = None

    scaleway_serverless_function: Optional[ScalewayServerlessFunctionBackendConfig] = (
        None
    )


@dataclass
class UpdateCacheStageRequest:
    cache_stage_id: str
    """
    ID of the cache stage to update.
    """

    fallback_ttl: Optional[str] = None
    """
    Time To Live (TTL) in seconds. Defines how long content is cached.
    """

    include_cookies: Optional[bool] = False
    """
    Defines whether responses to requests with cookies must be stored in the cache.
    """

    backend_stage_id: Optional[str] = None

    waf_stage_id: Optional[str] = None

    route_stage_id: Optional[str] = None


@dataclass
class UpdateDNSStageRequest:
    dns_stage_id: str
    """
    ID of the DNS stage to update.
    """

    fqdns: Optional[list[str]] = field(default_factory=list)
    """
    Fully Qualified Domain Name (in the format subdomain.example.com) attached to the stage.
    """

    tls_stage_id: Optional[str] = None

    cache_stage_id: Optional[str] = None

    backend_stage_id: Optional[str] = None


@dataclass
class UpdatePipelineRequest:
    pipeline_id: str
    """
    ID of the pipeline to update.
    """

    name: Optional[str] = None
    """
    Name of the pipeline.
    """

    description: Optional[str] = None
    """
    Description of the pipeline.
    """


@dataclass
class UpdateRouteStageRequest:
    route_stage_id: str
    """
    ID of the route stage to update.
    """

    waf_stage_id: Optional[str] = None


@dataclass
class UpdateTLSStageRequest:
    tls_stage_id: str
    """
    ID of the TLS stage to update.
    """

    tls_secrets_config: Optional[TLSSecretsConfig] = None
    """
    Secret (from Scaleway Secret-Manager) containing your custom certificate.
    """

    managed_certificate: Optional[bool] = False
    """
    True when Scaleway generates and manages a Let's Encrypt certificate for the TLS stage/custom endpoint.
    """

    cache_stage_id: Optional[str] = None

    backend_stage_id: Optional[str] = None

    route_stage_id: Optional[str] = None

    waf_stage_id: Optional[str] = None


@dataclass
class UpdateWafStageRequest:
    waf_stage_id: str
    """
    ID of the WAF stage to update.
    """

    mode: Optional[WafStageMode] = WafStageMode.UNKNOWN_MODE
    """
    Mode defining WAF behavior (`disable`/`log_only`/`enable`).
    """

    paranoia_level: Optional[int] = 0
    """
    Sensitivity level (`1`,`2`,`3`,`4`) to use when classifying requests as malicious. With a high level, requests are more likely to be classed as malicious, and false positives are expected. With a lower level, requests are more likely to be classed as benign.
    """

    backend_stage_id: Optional[str] = None
