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
    NODE22 = "node22"
    PYTHON312 = "python312"
    PHP83 = "php83"
    GO122 = "go122"
    RUST179 = "rust179"

    def __str__(self) -> str:
        return str(self.value)


class FunctionSandbox(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SANDBOX = "unknown_sandbox"
    V1 = "v1"
    V2 = "v2"

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
    key: str

    hashed_value: str


@dataclass
class TriggerMnqNatsClientConfig:
    subject: str
    """
    Name of the NATS subject the trigger listens to.
    """

    mnq_nats_account_id: str
    """
    ID of the Messaging and Queuing NATS account.
    """

    mnq_project_id: str
    """
    ID of the Messaging and Queuing project.
    """

    mnq_region: str
    """
    Currently, only the `fr-par` and `nl-ams` regions are available.
    """

    mnq_credential_id: Optional[str]
    """
    ID of the Messaging and Queuing credentials used to subscribe to the NATS subject.
    """


@dataclass
class TriggerMnqSqsClientConfig:
    queue: str
    """
    Name of the SQS queue the trigger listens to.
    """

    mnq_project_id: str
    """
    ID of the Messaging and Queuing project.
    """

    mnq_region: str
    """
    Currently, only the `fr-par` and `nl-ams` regions are available.
    """

    mnq_credential_id: Optional[str]
    """
    ID of the Messaging and Queuing credentials used to read from the SQS queue.
    """


@dataclass
class TriggerSqsClientConfig:
    endpoint: str

    queue_url: str

    access_key: str

    secret_key: str


@dataclass
class Secret:
    key: str

    value: Optional[str]


@dataclass
class CreateTriggerRequestMnqNatsClientConfig:
    subject: str
    """
    Name of the NATS subject the trigger should listen to.
    """

    mnq_nats_account_id: str
    """
    ID of the Messaging and Queuing NATS account.
    """

    mnq_project_id: str
    """
    ID of the Messaging and Queuing project.
    """

    mnq_region: str
    """
    Currently, only the `fr-par` and `nl-ams` regions are available.
    """


@dataclass
class CreateTriggerRequestMnqSqsClientConfig:
    queue: str
    """
    Name of the SQS queue the trigger should listen to.
    """

    mnq_project_id: str
    """
    You must have activated SQS on this project.
    """

    mnq_region: str
    """
    Currently, only the `fr-par` and `nl-ams` regions are available.
    """


@dataclass
class CreateTriggerRequestSqsClientConfig:
    endpoint: str

    queue_url: str

    access_key: str

    secret_key: str


@dataclass
class Cron:
    id: str
    """
    UUID of the cron.
    """

    function_id: str
    """
    UUID of the function the cron applies to.
    """

    schedule: str
    """
    Schedule of the cron.
    """

    status: CronStatus
    """
    Status of the cron.
    """

    name: str
    """
    Name of the cron.
    """

    args: Optional[Dict[str, Any]]
    """
    Arguments to pass with the cron.
    """


@dataclass
class Domain:
    id: str
    """
    UUID of the domain.
    """

    hostname: str
    """
    Hostname associated with the function.
    """

    function_id: str
    """
    UUID of the function the domain is associated with.
    """

    url: str
    """
    URL of the function.
    """

    status: DomainStatus
    """
    State of the doamin.
    """

    error_message: Optional[str]
    """
    Error message if the domain is in "error" state.
    """


@dataclass
class Runtime:
    name: str

    language: str

    version: str

    default_handler: str

    code_sample: str

    status: RuntimeStatus

    status_message: str

    extension: str

    implementation: str

    logo_url: str


@dataclass
class Function:
    id: str
    """
    UUID of the function.
    """

    name: str
    """
    Name of the function.
    """

    namespace_id: str
    """
    UUID of the namespace the function belongs to.
    """

    status: FunctionStatus
    """
    Status of the function.
    """

    environment_variables: Dict[str, str]
    """
    Environment variables of the function.
    """

    min_scale: int
    """
    Minimum number of instances to scale the function to.
    """

    max_scale: int
    """
    Maximum number of instances to scale the function to.
    """

    runtime: FunctionRuntime
    """
    Runtime of the function.
    """

    memory_limit: int
    """
    Memory limit of the function in MB.
    """

    cpu_limit: int
    """
    CPU limit of the function.
    """

    handler: str
    """
    Handler to use for the function.
    """

    privacy: FunctionPrivacy
    """
    Privacy setting of the function.
    """

    domain_name: str
    """
    Domain name associated with the function.
    """

    secret_environment_variables: List[SecretHashedValue]
    """
    Secret environment variables of the function.
    """

    region: Region
    """
    Region in which the function is deployed.
    """

    http_option: FunctionHttpOption
    """
    Possible values:
 - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
 - enabled: Serve both HTTP and HTTPS traffic.
    """

    runtime_message: str

    sandbox: FunctionSandbox
    """
    Execution environment of the function.
    """

    timeout: Optional[str]
    """
    Request processing time limit for the function.
    """

    error_message: Optional[str]
    """
    Error message if the function is in "error" state.
    """

    build_message: Optional[str]
    """
    Description of the current build step.
    """

    description: Optional[str]
    """
    Description of the function.
    """


@dataclass
class Namespace:
    id: str
    """
    UUID of the namespace.
    """

    name: str
    """
    Name of the namespace.
    """

    environment_variables: Dict[str, str]
    """
    Environment variables of the namespace.
    """

    organization_id: str
    """
    UUID of the Organization the namespace belongs to.
    """

    project_id: str
    """
    UUID of the Project the namespace belongs to.
    """

    status: NamespaceStatus
    """
    Status of the namespace.
    """

    registry_namespace_id: str
    """
    UUID of the registry namespace.
    """

    registry_endpoint: str
    """
    Registry endpoint of the namespace.
    """

    secret_environment_variables: List[SecretHashedValue]
    """
    Secret environment variables of the namespace.
    """

    region: Region
    """
    Region in which the namespace is located.
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
    id: str
    """
    UUID of the token.
    """

    token: str
    """
    String of the token.
    """

    status: TokenStatus
    """
    Status of the token.
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
    id: str
    """
    ID of the trigger.
    """

    name: str
    """
    Name of the trigger.
    """

    description: str
    """
    Description of the trigger.
    """

    function_id: str
    """
    ID of the function to trigger.
    """

    input_type: TriggerInputType
    """
    Type of the input.
    """

    status: TriggerStatus
    """
    Status of the trigger.
    """

    error_message: Optional[str]
    """
    Error message of the trigger.
    """

    scw_sqs_config: Optional[TriggerMnqSqsClientConfig]

    scw_nats_config: Optional[TriggerMnqNatsClientConfig]

    sqs_config: Optional[TriggerSqsClientConfig]


@dataclass
class UpdateTriggerRequestSqsClientConfig:
    access_key: Optional[str]

    secret_key: Optional[str]


@dataclass
class CreateCronRequest:
    function_id: str
    """
    UUID of the function to use the cron with.
    """

    schedule: str
    """
    Schedule of the cron in UNIX cron format.
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
    hostname: str
    """
    Hostame to create.
    """

    function_id: str
    """
    UUID of the function to associate the domain with.
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

    name: Optional[str]
    """
    Name of the function to create.
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

    runtime: Optional[FunctionRuntime]
    """
    Runtime to use with the function.
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

    sandbox: Optional[FunctionSandbox]
    """
    Execution environment of the function.
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
    name: str
    """
    Name of the trigger.
    """

    function_id: str
    """
    ID of the function to trigger.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    description: Optional[str]
    """
    Description of the trigger.
    """

    scw_sqs_config: Optional[CreateTriggerRequestMnqSqsClientConfig]

    scw_nats_config: Optional[CreateTriggerRequestMnqNatsClientConfig]

    sqs_config: Optional[CreateTriggerRequestSqsClientConfig]


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
    """
    ID of the trigger to delete.
    """

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
    url: str

    headers: Dict[str, List[str]]


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
    function_id: str
    """
    UUID of the function to get the upload URL for.
    """

    content_length: int
    """
    Size of the archive to upload in bytes.
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
    """
    ID of the trigger to get.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


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
    crons: List[Cron]
    """
    Array of crons.
    """

    total_count: int
    """
    Total number of crons.
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
    domains: List[Domain]
    """
    Array of domains.
    """

    total_count: int
    """
    Total number of domains.
    """


@dataclass
class ListFunctionRuntimesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListFunctionRuntimesResponse:
    runtimes: List[Runtime]
    """
    Array of runtimes available.
    """

    total_count: int
    """
    Total number of runtimes.
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
    functions: List[Function]
    """
    Array of functions.
    """

    total_count: int
    """
    Total number of functions.
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
    namespaces: List[Namespace]

    total_count: int
    """
    Total number of namespaces.
    """


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
    tokens: List[Token]

    total_count: int


@dataclass
class ListTriggersRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number to return.
    """

    page_size: Optional[int]
    """
    Maximum number of triggers to return per page.
    """

    order_by: Optional[ListTriggersRequestOrderBy]
    """
    Order in which to return results.
    """

    function_id: Optional[str]

    namespace_id: Optional[str]

    project_id: Optional[str]


@dataclass
class ListTriggersResponse:
    total_count: int
    """
    Total count of existing triggers (matching any filters specified).
    """

    triggers: List[Trigger]
    """
    Triggers on this page.
    """


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

    environment_variables: Optional[Dict[str, str]]
    """
    Environment variables of the function to update.
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

    memory_limit: Optional[int]
    """
    Memory limit of the function in MB.
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

    sandbox: Optional[FunctionSandbox]
    """
    Execution environment of the function.
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
    """
    ID of the trigger to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the trigger.
    """

    description: Optional[str]
    """
    Description of the trigger.
    """

    sqs_config: Optional[UpdateTriggerRequestSqsClientConfig]


@dataclass
class UploadURL:
    url: str
    """
    Upload URL to upload the function to.
    """

    headers: Dict[str, List[str]]
    """
    HTTP headers.
    """
