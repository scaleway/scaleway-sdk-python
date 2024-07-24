# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Region,
    Zone,
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


class ListPurgeRequestsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListTLSStagesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
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

    def __str__(self) -> str:
        return str(self.value)


class PurgeRequestStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    DONE = "done"
    ERROR = "error"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class ScalewayLb:
    id: str
    """
    ID of the Load Balancer.
    """

    zone: Zone
    """
    Zone of the Load Balancer.
    """

    frontend_id: str
    """
    ID of the frontend linked to the Load Balancer.
    """

    is_ssl: Optional[bool]
    """
    Defines whether the Load Balancer's frontend handles SSL connections.
    """

    domain_name: Optional[str]
    """
    Fully Qualified Domain Name (in the format subdomain.example.com) to use in HTTP requests sent towards your Load Balancer.
    """


@dataclass
class ScalewayLbBackendConfig:
    lbs: List[ScalewayLb]
    """
    Load Balancer information.
    """


@dataclass
class ScalewayS3BackendConfig:
    bucket_name: Optional[str]
    """
    Name of the Bucket.
    """

    bucket_region: Optional[str]
    """
    Region of the Bucket.
    """

    is_website: Optional[bool]
    """
    Defines whether the bucket website feature is enabled.
    """


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

    region: Region
    """
    Region of the Secret.
    """


@dataclass
class CheckPEMChainRequestSecretChain:
    secret_id: str

    secret_region: str


@dataclass
class BackendStage:
    id: str
    """
    ID of the backend stage.
    """

    project_id: str
    """
    Project ID of the backend stage.
    """

    pipeline_id: Optional[str]
    """
    Pipeline ID the backend stage belongs to.
    """

    created_at: Optional[datetime]
    """
    Date the backend stage was created.
    """

    updated_at: Optional[datetime]
    """
    Date the backend stage was last updated.
    """

    scaleway_s3: Optional[ScalewayS3BackendConfig]

    scaleway_lb: Optional[ScalewayLbBackendConfig]


@dataclass
class CacheStage:
    id: str
    """
    ID of the cache stage.
    """

    project_id: str
    """
    Project ID of the cache stage.
    """

    pipeline_id: Optional[str]
    """
    Pipeline ID the cache stage belongs to.
    """

    fallback_ttl: Optional[str]
    """
    Time To Live (TTL) in seconds. Defines how long content is cached.
    """

    created_at: Optional[datetime]
    """
    Date the cache stage was created.
    """

    updated_at: Optional[datetime]
    """
    Date the cache stage was last updated.
    """

    backend_stage_id: Optional[str]


@dataclass
class DNSStage:
    id: str
    """
    ID of the DNS stage.
    """

    fqdns: List[str]
    """
    List of Fully Qualified Domain Names attached to the stage.
    """

    type_: DNSStageType
    """
    Type of the stage.
    """

    project_id: str
    """
    Project ID of the DNS stage.
    """

    pipeline_id: Optional[str]
    """
    Pipeline ID the DNS stage belongs to.
    """

    created_at: Optional[datetime]
    """
    Date the DNS stage was created.
    """

    updated_at: Optional[datetime]
    """
    Date the DNS stage was last updated.
    """

    tls_stage_id: Optional[str]

    cache_stage_id: Optional[str]

    backend_stage_id: Optional[str]


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

    errors: List[PipelineError]
    """
    Errors of the pipeline.
    """

    project_id: str
    """
    Project ID of the pipeline.
    """

    created_at: Optional[datetime]
    """
    Date the pipeline was created.
    """

    updated_at: Optional[datetime]
    """
    Date the pipeline was last updated.
    """

    dns_stage_id: Optional[str]


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

    created_at: Optional[datetime]
    """
    Date the purge request was created.
    """

    updated_at: Optional[datetime]
    """
    Date the purge request was last updated.
    """

    assets: Optional[List[str]]

    all: Optional[bool]


@dataclass
class TLSStage:
    id: str
    """
    ID of the TLS stage.
    """

    secrets: List[TLSSecret]
    """
    Secret (from Scaleway Secret Manager) containing your custom certificate.
    """

    managed_certificate: bool
    """
    True when Scaleway generates and manages a Let's Encrypt certificate for the TLS stage/custom endpoint.
    """

    project_id: str
    """
    Project ID of the TLS stage.
    """

    pipeline_id: Optional[str]
    """
    Pipeline ID the TLS stage belongs to.
    """

    certificate_expires_at: Optional[datetime]
    """
    Expiration date of the certificate.
    """

    created_at: Optional[datetime]
    """
    Date the TLS stage was created.
    """

    updated_at: Optional[datetime]
    """
    Date the TLS stage was last updated.
    """

    cache_stage_id: Optional[str]

    backend_stage_id: Optional[str]


@dataclass
class TLSSecretsConfig:
    tls_secrets: List[TLSSecret]
    """
    Secret information (from Secret Manager).
    """


@dataclass
class CheckDomainRequest:
    fqdn: str

    cname: str

    project_id: Optional[str]


@dataclass
class CheckDomainResponse:
    is_valid: bool


@dataclass
class CheckLbOriginRequest:
    lb: Optional[ScalewayLb]


@dataclass
class CheckLbOriginResponse:
    is_valid: bool

    error_type: LbOriginError


@dataclass
class CheckPEMChainRequest:
    fqdn: str

    project_id: Optional[str]

    secret: Optional[CheckPEMChainRequestSecretChain]

    raw: Optional[str]


@dataclass
class CheckPEMChainResponse:
    is_valid: bool


@dataclass
class CreateBackendStageRequest:
    project_id: Optional[str]
    """
    Project ID in which the backend stage will be created.
    """

    scaleway_s3: Optional[ScalewayS3BackendConfig]

    scaleway_lb: Optional[ScalewayLbBackendConfig]


@dataclass
class CreateCacheStageRequest:
    project_id: Optional[str]
    """
    Project ID in which the cache stage will be created.
    """

    fallback_ttl: Optional[str]
    """
    Time To Live (TTL) in seconds. Defines how long content is cached.
    """

    backend_stage_id: Optional[str]


@dataclass
class CreateDNSStageRequest:
    project_id: Optional[str]
    """
    Project ID in which the DNS stage will be created.
    """

    fqdns: Optional[List[str]]
    """
    Fully Qualified Domain Name (in the format subdomain.example.com) to attach to the stage.
    """

    tls_stage_id: Optional[str]

    cache_stage_id: Optional[str]

    backend_stage_id: Optional[str]


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

    project_id: Optional[str]
    """
    Project ID in which the pipeline will be created.
    """

    dns_stage_id: Optional[str]


@dataclass
class CreatePurgeRequestRequest:
    pipeline_id: str
    """
    Pipeline ID in which the purge request will be created.
    """

    assets: Optional[List[str]]

    all: Optional[bool]


@dataclass
class CreateTLSStageRequest:
    project_id: Optional[str]
    """
    Project ID in which the TLS stage will be created.
    """

    secrets: Optional[List[TLSSecret]]
    """
    Secret (from Scaleway Secret Manager) containing your custom certificate.
    """

    managed_certificate: Optional[bool]
    """
    True when Scaleway generates and manages a Let's Encrypt certificate for the TLS stage/custom endpoint.
    """

    cache_stage_id: Optional[str]

    backend_stage_id: Optional[str]


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
class DeleteTLSStageRequest:
    tls_stage_id: str
    """
    ID of the TLS stage to delete.
    """


@dataclass
class GetBackendStageRequest:
    backend_stage_id: str
    """
    ID of the requested backend stage.
    """


@dataclass
class GetCacheStageRequest:
    cache_stage_id: str
    """
    ID of the requested cache stage.
    """


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
class GetTLSStageRequest:
    tls_stage_id: str
    """
    ID of the requested TLS stage.
    """


@dataclass
class ListBackendStagesRequest:
    order_by: Optional[ListBackendStagesRequestOrderBy]
    """
    Sort order of backend stages in the response.
    """

    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Number of backend stages to return per page.
    """

    pipeline_id: Optional[str]
    """
    Pipeline ID to filter for, only backend stages from this pipeline will be returned.
    """

    project_id: Optional[str]
    """
    Project ID to filter for, only backend stages from this Project will be returned.
    """

    bucket_name: Optional[str]
    """
    Bucket name to filter for, only backend stages from this Bucket will be returned.
    """

    bucket_region: Optional[str]
    """
    Bucket region to filter for, only backend stages with buckets in this region will be returned.
    """

    lb_id: Optional[str]
    """
    Load Balancer ID to filter for, only backend stages with this Load Balancer will be returned.
    """


@dataclass
class ListBackendStagesResponse:
    stages: List[BackendStage]
    """
    Paginated list of backend stages.
    """

    total_count: int
    """
    Count of all backend stages matching the requested criteria.
    """


@dataclass
class ListCacheStagesRequest:
    order_by: Optional[ListCacheStagesRequestOrderBy]
    """
    Sort order of cache stages in the response.
    """

    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Number of cache stages to return per page.
    """

    pipeline_id: Optional[str]
    """
    Pipeline ID to filter for, only cache stages from this pipeline will be returned.
    """

    project_id: Optional[str]
    """
    Project ID to filter for, only cache stages from this Project will be returned.
    """


@dataclass
class ListCacheStagesResponse:
    stages: List[CacheStage]
    """
    Paginated list of cache stages.
    """

    total_count: int
    """
    Count of all cache stages matching the requested criteria.
    """


@dataclass
class ListDNSStagesRequest:
    order_by: Optional[ListDNSStagesRequestOrderBy]
    """
    Sort order of DNS stages in the response.
    """

    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Number of DNS stages to return per page.
    """

    pipeline_id: Optional[str]
    """
    Pipeline ID to filter for, only DNS stages from this pipeline will be returned.
    """

    project_id: Optional[str]
    """
    Project ID to filter for, only DNS stages from this Project will be returned.
    """

    fqdn: Optional[str]
    """
    Fully Qualified Domain Name to filter for (in the format subdomain.example.com), only DNS stages with this FQDN will be returned.
    """


@dataclass
class ListDNSStagesResponse:
    stages: List[DNSStage]
    """
    Paginated list of DNS stages.
    """

    total_count: int
    """
    Count of all DNS stages matching the requested criteria.
    """


@dataclass
class ListPipelinesRequest:
    order_by: Optional[ListPipelinesRequestOrderBy]
    """
    Sort order of pipelines in the response.
    """

    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Number of pipelines to return per page.
    """

    name: Optional[str]
    """
    Pipeline name to filter for, only pipelines with this string within their name will be returned.
    """

    organization_id: Optional[str]
    """
    Organization ID to filter for, only pipelines from this Organization will be returned.
    """

    project_id: Optional[str]
    """
    Project ID to filter for, only pipelines from this Project will be returned.
    """

    has_backend_stage_lb: Optional[bool]
    """
    Filter on backend stage, only pipelines with a Load Balancer origin will be returned.
    """


@dataclass
class ListPipelinesResponse:
    pipelines: List[Pipeline]
    """
    Paginated list of pipelines.
    """

    total_count: int
    """
    Count of all pipelines matching the requested criteria.
    """


@dataclass
class ListPurgeRequestsRequest:
    order_by: Optional[ListPurgeRequestsRequestOrderBy]
    """
    Sort order of purge requests in the response.
    """

    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Number of purge requests to return per page.
    """

    organization_id: Optional[str]
    """
    Organization ID to filter for, only purge requests from this Project will be returned.
    """

    project_id: Optional[str]
    """
    Project ID to filter for, only purge requests from this Project will be returned.
    """

    pipeline_id: Optional[str]
    """
    Pipeline ID to filter for, only purge requests from this pipeline will be returned.
    """


@dataclass
class ListPurgeRequestsResponse:
    purge_requests: List[PurgeRequest]
    """
    Paginated list of purge requests.
    """

    total_count: int
    """
    Count of all purge requests matching the requested criteria.
    """


@dataclass
class ListTLSStagesRequest:
    order_by: Optional[ListTLSStagesRequestOrderBy]
    """
    Sort order of TLS stages in the response.
    """

    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Number of TLS stages to return per page.
    """

    pipeline_id: Optional[str]
    """
    Pipeline ID to filter for, only TLS stages from this pipeline will be returned.
    """

    project_id: Optional[str]
    """
    Project ID to filter for, only TLS stages from this Project will be returned.
    """

    secret_id: Optional[str]
    """
    Secret ID to filter for, only TLS stages with this Secret ID will be returned.
    """

    secret_region: Optional[str]
    """
    Secret region to filter for, only TLS stages with a Secret in this region will be returned.
    """


@dataclass
class ListTLSStagesResponse:
    stages: List[TLSStage]
    """
    Paginated list of TLS stages.
    """

    total_count: int
    """
    Count of all TLS stages matching the requested criteria.
    """


@dataclass
class UpdateBackendStageRequest:
    backend_stage_id: str
    """
    ID of the backend stage to update.
    """

    scaleway_s3: Optional[ScalewayS3BackendConfig]

    scaleway_lb: Optional[ScalewayLbBackendConfig]


@dataclass
class UpdateCacheStageRequest:
    cache_stage_id: str
    """
    ID of the cache stage to update.
    """

    fallback_ttl: Optional[str]
    """
    Time To Live (TTL) in seconds. Defines how long content is cached.
    """

    backend_stage_id: Optional[str]


@dataclass
class UpdateDNSStageRequest:
    dns_stage_id: str
    """
    ID of the DNS stage to update.
    """

    fqdns: Optional[List[str]]
    """
    Fully Qualified Domain Name (in the format subdomain.example.com) attached to the stage.
    """

    tls_stage_id: Optional[str]

    cache_stage_id: Optional[str]

    backend_stage_id: Optional[str]


@dataclass
class UpdatePipelineRequest:
    pipeline_id: str
    """
    ID of the pipeline to update.
    """

    name: Optional[str]
    """
    Name of the pipeline.
    """

    description: Optional[str]
    """
    Description of the pipeline.
    """

    dns_stage_id: Optional[str]


@dataclass
class UpdateTLSStageRequest:
    tls_stage_id: str
    """
    ID of the TLS stage to update.
    """

    tls_secrets_config: Optional[TLSSecretsConfig]
    """
    Secret (from Scaleway Secret-Manager) containing your custom certificate.
    """

    managed_certificate: Optional[bool]
    """
    True when Scaleway generates and manages a Let's Encrypt certificate for the TLS stage/custom endpoint.
    """

    cache_stage_id: Optional[str]

    backend_stage_id: Optional[str]
