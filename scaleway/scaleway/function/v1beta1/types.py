# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
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
    GO123 = "go123"
    GO124 = "go124"
    PYTHON313 = "python313"
    RUST185 = "rust185"
    PHP84 = "php84"

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

    mnq_credential_id: Optional[str] = None
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

    mnq_credential_id: Optional[str] = None
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
    value: Optional[str] = None


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

    args: Optional[dict[str, Any]] = field(default_factory=dict)
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
    State of the domain.
    """

    error_message: Optional[str] = None
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

    environment_variables: dict[str, str]
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

    secret_environment_variables: list[SecretHashedValue]
    """
    Secret environment variables of the function.
    """

    region: ScwRegion
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

    tags: list[str]
    """
    List of tags applied to the Serverless Function.
    """

    timeout: Optional[str] = None
    """
    Request processing time limit for the function.
    """

    error_message: Optional[str] = None
    """
    Error message if the function is in "error" state.
    """

    build_message: Optional[str] = None
    """
    Description of the current build step.
    """

    description: Optional[str] = None
    """
    Description of the function.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the function.
    """

    updated_at: Optional[datetime] = None
    """
    Last update date of the function.
    """

    ready_at: Optional[datetime] = None
    """
    Last date when the function was successfully deployed and set to ready.
    """

    private_network_id: Optional[str] = None
    """
    When connected to a Private Network, the function can access other Scaleway resources in this Private Network.
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

    environment_variables: dict[str, str]
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

    secret_environment_variables: list[SecretHashedValue]
    """
    Secret environment variables of the namespace.
    """

    region: ScwRegion
    """
    Region in which the namespace is located.
    """

    tags: list[str]
    """
    List of tags applied to the Serverless Function Namespace.
    """

    vpc_integration_activated: bool
    """
    The value of this field doesn't matter anymore, and will be removed in a near future.
    """

    error_message: Optional[str] = None
    """
    Error message if the namespace is in "error" state.
    """

    description: Optional[str] = None
    """
    Description of the namespace.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the namespace.
    """

    updated_at: Optional[datetime] = None
    """
    Last update date of the namespace.
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

    public_key: str
    """
    Public key of the token.
    """

    status: TokenStatus
    """
    Status of the token.
    """

    description: Optional[str] = None
    """
    Description of the token.
    """

    expires_at: Optional[datetime] = None
    """
    Date on which the token expires.
    """

    function_id: Optional[str] = None

    namespace_id: Optional[str] = None


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

    error_message: Optional[str] = None
    """
    Error message of the trigger.
    """

    scw_sqs_config: Optional[TriggerMnqSqsClientConfig] = None

    scw_nats_config: Optional[TriggerMnqNatsClientConfig] = None

    sqs_config: Optional[TriggerSqsClientConfig] = None


@dataclass
class UpdateTriggerRequestSqsClientConfig:
    access_key: Optional[str] = None
    secret_key: Optional[str] = None


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

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    args: Optional[dict[str, Any]] = field(default_factory=dict)
    """
    Arguments to use with the cron.
    """

    name: Optional[str] = None
    """
    Name of the cron.
    """


@dataclass
class CreateDomainRequest:
    hostname: str
    """
    Hostname to create.
    """

    function_id: str
    """
    UUID of the function to associate the domain with.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class CreateFunctionRequest:
    namespace_id: str
    """
    UUID of the namespace the function will be created in.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the function to create.
    """

    environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Environment variables of the function.
    """

    min_scale: Optional[int] = 0
    """
    Minimum number of instances to scale the function to.
    """

    max_scale: Optional[int] = 0
    """
    Maximum number of instances to scale the function to.
    """

    runtime: Optional[FunctionRuntime] = FunctionRuntime.UNKNOWN_RUNTIME
    """
    Runtime to use with the function.
    """

    memory_limit: Optional[int] = 0
    """
    Memory limit of the function in MB.
    """

    timeout: Optional[str] = None
    """
    Request processing time limit for the function.
    """

    handler: Optional[str] = None
    """
    Handler to use with the function.
    """

    privacy: Optional[FunctionPrivacy] = FunctionPrivacy.UNKNOWN_PRIVACY
    """
    Privacy setting of the function.
    """

    description: Optional[str] = None
    """
    Description of the function.
    """

    secret_environment_variables: Optional[list[Secret]] = field(default_factory=list)
    http_option: Optional[FunctionHttpOption] = FunctionHttpOption.UNKNOWN_HTTP_OPTION
    """
    Possible values:
 - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
 - enabled: Serve both HTTP and HTTPS traffic.
    """

    sandbox: Optional[FunctionSandbox] = FunctionSandbox.UNKNOWN_SANDBOX
    """
    Execution environment of the function.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the Serverless Function.
    """

    private_network_id: Optional[str] = None
    """
    When connected to a Private Network, the function can access other Scaleway resources in this Private Network.
    """


@dataclass
class CreateNamespaceRequest:
    activate_vpc_integration: bool
    """
    Setting this field to true doesn't matter anymore. It will be removed in a near future.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Environment variables of the namespace.
    """

    project_id: Optional[str] = None
    """
    UUID of the project in which the namespace will be created.
    """

    description: Optional[str] = None
    """
    Description of the namespace.
    """

    secret_environment_variables: Optional[list[Secret]] = field(default_factory=list)
    """
    Secret environment variables of the namespace.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the Serverless Function Namespace.
    """


@dataclass
class CreateTokenRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    description: Optional[str] = None
    """
    Description of the token.
    """

    expires_at: Optional[datetime] = None
    """
    Date on which the token expires.
    """

    function_id: Optional[str] = None

    namespace_id: Optional[str] = None


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

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    description: Optional[str] = None
    """
    Description of the trigger.
    """

    scw_sqs_config: Optional[CreateTriggerRequestMnqSqsClientConfig] = None

    scw_nats_config: Optional[CreateTriggerRequestMnqNatsClientConfig] = None

    sqs_config: Optional[CreateTriggerRequestSqsClientConfig] = None


@dataclass
class DeleteCronRequest:
    cron_id: str
    """
    UUID of the cron to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteDomainRequest:
    domain_id: str
    """
    UUID of the domain to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteFunctionRequest:
    function_id: str
    """
    UUID of the function to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteNamespaceRequest:
    namespace_id: str
    """
    UUID of the namespace.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteTokenRequest:
    token_id: str
    """
    UUID of the token to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteTriggerRequest:
    trigger_id: str
    """
    ID of the trigger to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeployFunctionRequest:
    function_id: str
    """
    UUID of the function to deploy.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DownloadURL:
    url: str
    headers: dict[str, list[str]]


@dataclass
class GetCronRequest:
    cron_id: str
    """
    UUID of the cron to get.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetDomainRequest:
    domain_id: str
    """
    UUID of the domain to get.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetFunctionDownloadURLRequest:
    function_id: str
    """
    UUID of the function to get the download URL for.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetFunctionRequest:
    function_id: str
    """
    UUID of the function.
    """

    region: Optional[ScwRegion] = None
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

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetNamespaceRequest:
    namespace_id: str
    """
    UUID of the namespace.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetTokenRequest:
    token_id: str
    """
    UUID of the token to get.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetTriggerRequest:
    trigger_id: str
    """
    ID of the trigger to get.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListCronsRequest:
    function_id: str
    """
    UUID of the function.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Number of crons per page.
    """

    order_by: Optional[ListCronsRequestOrderBy] = ListCronsRequestOrderBy.CREATED_AT_ASC
    """
    Order of the crons.
    """


@dataclass
class ListCronsResponse:
    crons: list[Cron]
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
    UUID of the function the domain is associated with.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Number of domains per page.
    """

    order_by: Optional[ListDomainsRequestOrderBy] = (
        ListDomainsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Order of the domains.
    """


@dataclass
class ListDomainsResponse:
    domains: list[Domain]
    """
    Array of domains.
    """

    total_count: int
    """
    Total number of domains.
    """


@dataclass
class ListFunctionRuntimesRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListFunctionRuntimesResponse:
    runtimes: list[Runtime]
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

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Number of functions per page.
    """

    order_by: Optional[ListFunctionsRequestOrderBy] = (
        ListFunctionsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Order of the functions.
    """

    name: Optional[str] = None
    """
    Name of the function.
    """

    organization_id: Optional[str] = None
    """
    UUID of the Organization the function belongs to.
    """

    project_id: Optional[str] = None
    """
    UUID of the Project the function belongs to.
    """


@dataclass
class ListFunctionsResponse:
    functions: list[Function]
    """
    Array of functions.
    """

    total_count: int
    """
    Total number of functions.
    """


@dataclass
class ListNamespacesRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Number of namespaces per page.
    """

    order_by: Optional[ListNamespacesRequestOrderBy] = (
        ListNamespacesRequestOrderBy.CREATED_AT_ASC
    )
    """
    Order of the namespaces.
    """

    name: Optional[str] = None
    """
    Name of the namespace.
    """

    organization_id: Optional[str] = None
    """
    UUID of the Organization the namespace belongs to.
    """

    project_id: Optional[str] = None
    """
    UUID of the Project the namespace belongs to.
    """


@dataclass
class ListNamespacesResponse:
    namespaces: list[Namespace]
    total_count: int
    """
    Total number of namespaces.
    """


@dataclass
class ListTokensRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Number of tokens per page.
    """

    order_by: Optional[ListTokensRequestOrderBy] = (
        ListTokensRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order for the tokens.
    """

    function_id: Optional[str] = None
    """
    UUID of the function the token is associated with.
    """

    namespace_id: Optional[str] = None
    """
    UUID of the namespace the token is associated with.
    """


@dataclass
class ListTokensResponse:
    tokens: list[Token]
    total_count: int


@dataclass
class ListTriggersRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number to return.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of triggers to return per page.
    """

    order_by: Optional[ListTriggersRequestOrderBy] = (
        ListTriggersRequestOrderBy.CREATED_AT_ASC
    )
    """
    Order in which to return results.
    """

    function_id: Optional[str] = None

    namespace_id: Optional[str] = None

    project_id: Optional[str] = None


@dataclass
class ListTriggersResponse:
    total_count: int
    """
    Total count of existing triggers (matching any filters specified).
    """

    triggers: list[Trigger]
    """
    Triggers on this page.
    """


@dataclass
class UpdateCronRequest:
    cron_id: str
    """
    UUID of the cron to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    function_id: Optional[str] = None
    """
    UUID of the function to use the cron with.
    """

    schedule: Optional[str] = None
    """
    Schedule of the cron in UNIX cron format.
    """

    args: Optional[dict[str, Any]] = field(default_factory=dict)
    """
    Arguments to use with the cron.
    """

    name: Optional[str] = None
    """
    Name of the cron.
    """


@dataclass
class UpdateFunctionRequest:
    function_id: str
    """
    UUID of the function to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Environment variables of the function to update.
    """

    min_scale: Optional[int] = 0
    """
    Minimum number of instances to scale the function to.
    """

    max_scale: Optional[int] = 0
    """
    Maximum number of instances to scale the function to.
    """

    runtime: Optional[FunctionRuntime] = FunctionRuntime.UNKNOWN_RUNTIME
    """
    Runtime to use with the function.
    """

    memory_limit: Optional[int] = 0
    """
    Memory limit of the function in MB.
    """

    timeout: Optional[str] = None
    """
    Processing time limit for the function.
    """

    redeploy: Optional[bool] = False
    """
    Redeploy failed function.
    """

    handler: Optional[str] = None
    """
    Handler to use with the function.
    """

    privacy: Optional[FunctionPrivacy] = FunctionPrivacy.UNKNOWN_PRIVACY
    """
    Privacy setting of the function.
    """

    description: Optional[str] = None
    """
    Description of the function.
    """

    secret_environment_variables: Optional[list[Secret]] = field(default_factory=list)
    """
    During an update, secret environment variables that are not specified in this field will be kept unchanged.

In order to delete a specific secret environment variable, you must reference its key, but not provide any value for it.
For example, the following payload will delete the `TO_DELETE` secret environment variable:

```json
{
 "secret_environment_variables":[
   {"key":"TO_DELETE"}
 ]
}
```.
    """

    http_option: Optional[FunctionHttpOption] = FunctionHttpOption.UNKNOWN_HTTP_OPTION
    """
    Possible values:
 - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
 - enabled: Serve both HTTP and HTTPS traffic.
    """

    sandbox: Optional[FunctionSandbox] = FunctionSandbox.UNKNOWN_SANDBOX
    """
    Execution environment of the function.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the Serverless Function.
    """

    private_network_id: Optional[str] = None
    """
    When connected to a Private Network, the function can access other Scaleway resources in this Private Network.
    """


@dataclass
class UpdateNamespaceRequest:
    namespace_id: str
    """
    UUID of the namespapce.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Environment variables of the namespace.
    """

    description: Optional[str] = None
    """
    Description of the namespace.
    """

    secret_environment_variables: Optional[list[Secret]] = field(default_factory=list)
    """
    Secret environment variables of the namespace.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the Serverless Function Namespace.
    """


@dataclass
class UpdateTriggerRequest:
    trigger_id: str
    """
    ID of the trigger to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the trigger.
    """

    description: Optional[str] = None
    """
    Description of the trigger.
    """

    sqs_config: Optional[UpdateTriggerRequestSqsClientConfig] = None


@dataclass
class UploadURL:
    url: str
    """
    Upload URL to upload the function to.
    """

    headers: dict[str, list[str]]
    """
    HTTP headers.
    """
