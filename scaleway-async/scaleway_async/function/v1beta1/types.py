# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class CronStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"
    CREATING = "creating"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)


class DomainStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    CREATING = "creating"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)


class FunctionHttpOption(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_HTTP_OPTION = "unknown_http_option"
    ENABLED = "enabled"
    REDIRECTED = "redirected"

    def __str__(self) -> str:
        return str(self.value)


class FunctionPrivacy(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_PRIVACY = "unknown_privacy"
    PUBLIC = "public"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)


class FunctionRuntime(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_RUNTIME = "unknown_runtime"
    GOLANG = "golang"
    PYTHON = "python"
    PYTHON3 = "python3"
    NODE8 = "node8"
    NODE10 = "node10"
    NODE14 = "node14"
    NODE16 = "node16"
    NODE17 = "node17"
    PYTHON37 = "python37"
    PYTHON38 = "python38"
    PYTHON39 = "python39"
    PYTHON310 = "python310"
    GO113 = "go113"
    GO117 = "go117"
    GO118 = "go118"
    NODE18 = "node18"
    RUST165 = "rust165"
    GO119 = "go119"
    PYTHON311 = "python311"
    PHP82 = "php82"
    NODE19 = "node19"
    GO120 = "go120"
    NODE20 = "node20"
    GO121 = "go121"

    def __str__(self) -> str:
        return str(self.value)


class FunctionStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"
    CREATING = "creating"
    PENDING = "pending"
    CREATED = "created"

    def __str__(self) -> str:
        return str(self.value)


class ListCronsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListDomainsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    HOSTNAME_ASC = "hostname_asc"
    HOSTNAME_DESC = "hostname_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListFunctionsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListLogsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    TIMESTAMP_DESC = "timestamp_desc"
    TIMESTAMP_ASC = "timestamp_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListNamespacesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListTokensRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListTriggersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class LogStream(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    STDOUT = "stdout"
    STDERR = "stderr"

    def __str__(self) -> str:
        return str(self.value)


class NamespaceStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"
    CREATING = "creating"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)


class RuntimeStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    BETA = "beta"
    AVAILABLE = "available"
    DEPRECATED = "deprecated"
    END_OF_SUPPORT = "end_of_support"
    END_OF_LIFE = "end_of_life"

    def __str__(self) -> str:
        return str(self.value)


class TokenStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    CREATING = "creating"

    def __str__(self) -> str:
        return str(self.value)


class TriggerInputType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_INPUT_TYPE = "unknown_input_type"
    SQS = "sqs"
    SCW_SQS = "scw_sqs"
    NATS = "nats"
    SCW_NATS = "scw_nats"

    def __str__(self) -> str:
        return str(self.value)


class TriggerStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    CREATING = "creating"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class SecretHashedValue:
    hashed_value: str

    key: str


@dataclass
class TriggerMnqNatsClientConfig:
    mnq_region: str

    mnq_project_id: str

    subject: str

    mnq_namespace_id: str

    mnq_credential_id: Optional[str]


@dataclass
class TriggerMnqSqsClientConfig:
    mnq_region: str

    mnq_project_id: str

    queue: str

    mnq_namespace_id: str

    mnq_credential_id: Optional[str]


@dataclass
class TriggerSqsClientConfig:
    secret_key: str

    access_key: str

    queue_url: str

    endpoint: str


@dataclass
class Secret:
    key: str

    value: Optional[str]


@dataclass
class CreateTriggerRequestMnqNatsClientConfig:
    mnq_nats_account_id: str

    mnq_region: str

    mnq_project_id: str

    subject: str

    mnq_namespace_id: str


@dataclass
class CreateTriggerRequestMnqSqsClientConfig:
    mnq_region: str

    mnq_project_id: str

    queue: str

    mnq_namespace_id: str


@dataclass
class CreateTriggerRequestSqsClientConfig:
    secret_key: str

    access_key: str

    queue_url: str

    endpoint: str


@dataclass
class Cron:
    name: str
    """
    Name of the cron.
    """

    status: CronStatus
    """
    Status of the cron.
    """

    schedule: str
    """
    Schedule of the cron.
    """

    function_id: str
    """
    UUID of the function the cron applies to.
    """

    id: str
    """
    UUID of the cron.
    """

    args: Optional[Dict[str, Any]]
    """
    Arguments to pass with the cron.
    """


@dataclass
class Domain:
    status: DomainStatus
    """
    State of the doamin.
    """

    url: str
    """
    URL of the function.
    """

    function_id: str
    """
    UUID of the function the domain is associated with.
    """

    hostname: str
    """
    Hostname associated with the function.
    """

    id: str
    """
    UUID of the domain.
    """

    error_message: Optional[str]
    """
    Error message if the domain is in "error" state.
    """


@dataclass
class Runtime:
    logo_url: str

    implementation: str

    extension: str

    status_message: str

    status: RuntimeStatus

    code_sample: str

    default_handler: str

    version: str

    language: str

    name: str


@dataclass
class Function:
    handler: str
    """
    Handler to use for the function.
    """

    id: str
    """
    UUID of the function.
    """

    max_scale: int
    """
    Maximum number of instances to scale the function to.
    """

    domain_name: str
    """
    Domain name associated with the function.
    """

    secret_environment_variables: List[SecretHashedValue]
    """
    Secret environment variables of the function.
    """

    http_option: FunctionHttpOption
    """
    Possible values:
 - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
 - enabled: Serve both HTTP and HTTPS traffic.
    """

    region: Region
    """
    Region in which the function is deployed.
    """

    environment_variables: Dict[str, str]
    """
    Environment variables of the function.
    """

    name: str
    """
    Name of the function.
    """

    namespace_id: str
    """
    UUID of the namespace the function belongs to.
    """

    runtime: FunctionRuntime
    """
    Runtime of the function.
    """

    runtime_message: str

    privacy: FunctionPrivacy
    """
    Privacy setting of the function.
    """

    cpu_limit: int
    """
    CPU limit of the function.
    """

    min_scale: int
    """
    Minimum number of instances to scale the function to.
    """

    status: FunctionStatus
    """
    Status of the function.
    """

    memory_limit: int
    """
    Memory limit of the function in MB.
    """

    timeout: Optional[str]
    """
    Request processing time limit for the function.
    """

    description: Optional[str]
    """
    Description of the function.
    """

    build_message: Optional[str]
    """
    Description of the current build step.
    """

    error_message: Optional[str]
    """
    Error message if the function is in "error" state.
    """


@dataclass
class Log:
    stream: LogStream
    """
    Can be stdout or stderr.
    """

    source: str
    """
    Source of the log (core runtime or user code).
    """

    level: str
    """
    Severity of the log (info, debug, error etc.).
    """

    id: str
    """
    UUID of the log.
    """

    message: str
    """
    Message of the log.
    """

    timestamp: Optional[datetime]
    """
    Timestamp of the log.
    """


@dataclass
class Namespace:
    region: Region
    """
    Region in which the namespace is located.
    """

    secret_environment_variables: List[SecretHashedValue]
    """
    Secret environment variables of the namespace.
    """

    registry_endpoint: str
    """
    Registry endpoint of the namespace.
    """

    registry_namespace_id: str
    """
    UUID of the registry namespace.
    """

    status: NamespaceStatus
    """
    Status of the namespace.
    """

    project_id: str
    """
    UUID of the Project the namespace belongs to.
    """

    organization_id: str
    """
    UUID of the Organization the namespace belongs to.
    """

    environment_variables: Dict[str, str]
    """
    Environment variables of the namespace.
    """

    name: str
    """
    Name of the namespace.
    """

    id: str
    """
    UUID of the namespace.
    """

    error_message: Optional[str]
    """
    Error message if the namespace is in "error" state.
    """

    description: Optional[str]
    """
    Description of the namespace.
    """


@dataclass
class Token:
    status: TokenStatus
    """
    Status of the token.
    """

    token: str
    """
    String of the token.
    """

    id: str
    """
    UUID of the token.
    """

    public_key: Optional[str]
    """
    Public key of the token.
    """

    description: Optional[str]
    """
    Description of the token.
    """

    expires_at: Optional[datetime]
    """
    Date on which the token expires.
    """

    function_id: Optional[str]

    namespace_id: Optional[str]


@dataclass
class Trigger:
    function_id: str

    status: TriggerStatus

    input_type: TriggerInputType

    description: str

    name: str

    id: str

    error_message: Optional[str]

    scw_sqs_config: Optional[TriggerMnqSqsClientConfig]

    sqs_config: Optional[TriggerSqsClientConfig]

    scw_nats_config: Optional[TriggerMnqNatsClientConfig]


@dataclass
class UpdateTriggerRequestSqsClientConfig:
    access_key: Optional[str]

    secret_key: Optional[str]


@dataclass
class CreateCronRequest:
    schedule: str
    """
    Schedule of the cron in UNIX cron format.
    """

    function_id: str
    """
    UUID of the function to use the cron with.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    args: Optional[Dict[str, Any]]
    """
    Arguments to use with the cron.
    """

    name: Optional[str]
    """
    Name of the cron.
    """


@dataclass
class CreateDomainRequest:
    function_id: str
    """
    UUID of the function to associate the domain with.
    """

    hostname: str
    """
    Hostame to create.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class CreateFunctionRequest:
    namespace_id: str
    """
    UUID of the namespace the function will be created in.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    runtime: Optional[FunctionRuntime]
    """
    Runtime to use with the function.
    """

    environment_variables: Optional[Dict[str, str]]
    """
    Environment variables of the function.
    """

    min_scale: Optional[int]
    """
    Minumum number of instances to scale the function to.
    """

    max_scale: Optional[int]
    """
    Maximum number of instances to scale the function to.
    """

    name: Optional[str]
    """
    Name of the function to create.
    """

    memory_limit: Optional[int]
    """
    Memory limit of the function in MB.
    """

    timeout: Optional[str]
    """
    Request processing time limit for the function.
    """

    handler: Optional[str]
    """
    Handler to use with the function.
    """

    privacy: Optional[FunctionPrivacy]
    """
    Privacy setting of the function.
    """

    description: Optional[str]
    """
    Description of the function.
    """

    secret_environment_variables: Optional[List[Secret]]

    http_option: Optional[FunctionHttpOption]
    """
    Possible values:
 - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
 - enabled: Serve both HTTP and HTTPS traffic.
    """


@dataclass
class CreateNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]

    environment_variables: Optional[Dict[str, str]]
    """
    Environment variables of the namespace.
    """

    project_id: Optional[str]
    """
    UUID of the project in which the namespace will be created.
    """

    description: Optional[str]
    """
    Description of the namespace.
    """

    secret_environment_variables: Optional[List[Secret]]
    """
    Secret environment variables of the namespace.
    """


@dataclass
class CreateTokenRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    description: Optional[str]
    """
    Description of the token.
    """

    expires_at: Optional[datetime]
    """
    Date on which the token expires.
    """

    function_id: Optional[str]

    namespace_id: Optional[str]


@dataclass
class CreateTriggerRequest:
    function_id: str

    name: str

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    description: Optional[str]

    scw_sqs_config: Optional[CreateTriggerRequestMnqSqsClientConfig]

    sqs_config: Optional[CreateTriggerRequestSqsClientConfig]

    scw_nats_config: Optional[CreateTriggerRequestMnqNatsClientConfig]


@dataclass
class DeleteCronRequest:
    cron_id: str
    """
    UUID of the cron to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteDomainRequest:
    domain_id: str
    """
    UUID of the domain to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteFunctionRequest:
    function_id: str
    """
    UUID of the function to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteNamespaceRequest:
    namespace_id: str
    """
    UUID of the namespace.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteTokenRequest:
    token_id: str
    """
    UUID of the token to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteTriggerRequest:
    trigger_id: str

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeployFunctionRequest:
    function_id: str
    """
    UUID of the function to deploy.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DownloadURL:
    headers: Dict[str, List[str]]

    url: str


@dataclass
class GetCronRequest:
    cron_id: str
    """
    UUID of the cron to get.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetDomainRequest:
    domain_id: str
    """
    UUID of the domain to get.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetFunctionDownloadURLRequest:
    function_id: str
    """
    UUID of the function to get the the download URL for.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetFunctionRequest:
    function_id: str
    """
    UUID of the function.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetFunctionUploadURLRequest:
    content_length: int
    """
    Size of the archive to upload in bytes.
    """

    function_id: str
    """
    UUID of the function to get the upload URL for.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetNamespaceRequest:
    namespace_id: str
    """
    UUID of the namespace.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetTokenRequest:
    token_id: str
    """
    UUID of the token to get.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetTriggerRequest:
    trigger_id: str

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class IssueJWTRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    expires_at: Optional[datetime]

    function_id: Optional[str]

    namespace_id: Optional[str]


@dataclass
class ListCronsRequest:
    function_id: str
    """
    UUID of the function.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of crons per page.
    """

    order_by: Optional[ListCronsRequestOrderBy]
    """
    Order of the crons.
    """


@dataclass
class ListCronsResponse:
    total_count: int
    """
    Total number of crons.
    """

    crons: List[Cron]
    """
    Array of crons.
    """


@dataclass
class ListDomainsRequest:
    function_id: str
    """
    UUID of the function the domain is assoicated with.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of domains per page.
    """

    order_by: Optional[ListDomainsRequestOrderBy]
    """
    Order of the domains.
    """


@dataclass
class ListDomainsResponse:
    total_count: int
    """
    Total number of domains.
    """

    domains: List[Domain]
    """
    Array of domains.
    """


@dataclass
class ListFunctionRuntimesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListFunctionRuntimesResponse:
    total_count: int
    """
    Total number of runtimes.
    """

    runtimes: List[Runtime]
    """
    Array of runtimes available.
    """


@dataclass
class ListFunctionsRequest:
    namespace_id: str
    """
    UUID of the namespace the function belongs to.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of functions per page.
    """

    order_by: Optional[ListFunctionsRequestOrderBy]
    """
    Order of the functions.
    """

    name: Optional[str]
    """
    Name of the function.
    """

    organization_id: Optional[str]
    """
    UUID of the Organziation the function belongs to.
    """

    project_id: Optional[str]
    """
    UUID of the Project the function belongs to.
    """


@dataclass
class ListFunctionsResponse:
    total_count: int
    """
    Total number of functions.
    """

    functions: List[Function]
    """
    Array of functions.
    """


@dataclass
class ListLogsRequest:
    function_id: str
    """
    UUID of the function to get the logs for.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of logs per page.
    """

    order_by: Optional[ListLogsRequestOrderBy]
    """
    Order of the logs.
    """


@dataclass
class ListLogsResponse:
    total_count: int
    """
    Total number of logs.
    """

    logs: List[Log]
    """
    Array of logs.
    """


@dataclass
class ListNamespacesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of namespaces per page.
    """

    order_by: Optional[ListNamespacesRequestOrderBy]
    """
    Order of the namespaces.
    """

    name: Optional[str]
    """
    Name of the namespace.
    """

    organization_id: Optional[str]
    """
    UUID of the Organization the namespace belongs to.
    """

    project_id: Optional[str]
    """
    UUID of the Project the namespace belongs to.
    """


@dataclass
class ListNamespacesResponse:
    total_count: int
    """
    Total number of namespaces.
    """

    namespaces: List[Namespace]


@dataclass
class ListTokensRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of tokens per page.
    """

    order_by: Optional[ListTokensRequestOrderBy]
    """
    Sort order for the tokens.
    """

    function_id: Optional[str]
    """
    UUID of the function the token is assoicated with.
    """

    namespace_id: Optional[str]
    """
    UUID of the namespace the token is associated with.
    """


@dataclass
class ListTokensResponse:
    total_count: int

    tokens: List[Token]


@dataclass
class ListTriggersRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListTriggersRequestOrderBy]

    function_id: Optional[str]

    namespace_id: Optional[str]

    project_id: Optional[str]


@dataclass
class ListTriggersResponse:
    total_count: int

    triggers: List[Trigger]


@dataclass
class UpdateCronRequest:
    cron_id: str
    """
    UUID of the cron to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    function_id: Optional[str]
    """
    UUID of the function to use the cron with.
    """

    schedule: Optional[str]
    """
    Schedule of the cron in UNIX cron format.
    """

    args: Optional[Dict[str, Any]]
    """
    Arguments to use with the cron.
    """

    name: Optional[str]
    """
    Name of the cron.
    """


@dataclass
class UpdateFunctionRequest:
    function_id: str
    """
    UUID of the function to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    memory_limit: Optional[int]
    """
    Memory limit of the function in MB.
    """

    min_scale: Optional[int]
    """
    Minumum number of instances to scale the function to.
    """

    max_scale: Optional[int]
    """
    Maximum number of instances to scale the function to.
    """

    runtime: Optional[FunctionRuntime]
    """
    Runtime to use with the function.
    """

    environment_variables: Optional[Dict[str, str]]
    """
    Environment variables of the function to update.
    """

    timeout: Optional[str]
    """
    Processing time limit for the function.
    """

    redeploy: Optional[bool]
    """
    Redeploy failed function.
    """

    handler: Optional[str]
    """
    Handler to use with the function.
    """

    privacy: Optional[FunctionPrivacy]
    """
    Privacy setting of the function.
    """

    description: Optional[str]
    """
    Description of the function.
    """

    secret_environment_variables: Optional[List[Secret]]
    """
    Secret environment variables of the function.
    """

    http_option: Optional[FunctionHttpOption]
    """
    Possible values:
 - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
 - enabled: Serve both HTTP and HTTPS traffic.
    """


@dataclass
class UpdateNamespaceRequest:
    namespace_id: str
    """
    UUID of the namespapce.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    environment_variables: Optional[Dict[str, str]]
    """
    Environment variables of the namespace.
    """

    description: Optional[str]
    """
    Description of the namespace.
    """

    secret_environment_variables: Optional[List[Secret]]
    """
    Secret environment variables of the namespace.
    """


@dataclass
class UpdateTriggerRequest:
    trigger_id: str

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]

    description: Optional[str]

    sqs_config: Optional[UpdateTriggerRequestSqsClientConfig]


@dataclass
class UploadURL:
    headers: Dict[str, List[str]]
    """
    HTTP headers.
    """

    url: str
    """
    Upload URL to upload the function to.
    """
