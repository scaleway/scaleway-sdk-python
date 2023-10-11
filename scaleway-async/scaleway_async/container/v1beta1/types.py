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


class ContainerHttpOption(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_HTTP_OPTION = "unknown_http_option"
    ENABLED = "enabled"
    REDIRECTED = "redirected"

    def __str__(self) -> str:
        return str(self.value)


class ContainerPrivacy(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_PRIVACY = "unknown_privacy"
    PUBLIC = "public"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)


class ContainerProtocol(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_PROTOCOL = "unknown_protocol"
    HTTP1 = "http1"
    H2C = "h2c"

    def __str__(self) -> str:
        return str(self.value)


class ContainerStatus(str, Enum, metaclass=StrEnumMeta):
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


class ListContainersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

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
class Container:
    privacy: ContainerPrivacy
    """
    Privacy setting of the container.
    """

    http_option: ContainerHttpOption
    """
    Possible values:
 - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
 - enabled: Serve both HTTP and HTTPS traffic.
    """

    max_scale: int
    """
    Maximum number of instances to scale the container to.
    """

    protocol: ContainerProtocol
    """
    Protocol the container uses.
    """

    port: int
    """
    Port the container listens on.
    """

    registry_image: str
    """
    Name of the registry image (e.g. "rg.fr-par.scw.cloud/something/image:tag").
    """

    domain_name: str
    """
    Domain name attributed to the contaioner.
    """

    environment_variables: Dict[str, str]
    """
    Environment variables of the container.
    """

    name: str
    """
    Name of the container.
    """

    namespace_id: str
    """
    UUID of the namespace the container belongs to.
    """

    memory_limit: int
    """
    Memory limit of the container in MB.
    """

    secret_environment_variables: List[SecretHashedValue]
    """
    Secret environment variables of the container.
    """

    max_concurrency: int
    """
    Number of maximum concurrent executions of the container.
    """

    region: Region
    """
    Region in which the container will be deployed.
    """

    id: str
    """
    UUID of the container.
    """

    status: ContainerStatus
    """
    Status of the container.
    """

    cpu_limit: int
    """
    CPU limit of the container in mvCPU.
    """

    min_scale: int
    """
    Minimum number of instances to scale the container to.
    """

    description: Optional[str]
    """
    Description of the container.
    """

    error_message: Optional[str]
    """
    Last error message of the container.
    """

    timeout: Optional[str]
    """
    Processing time limit for the container.
    """


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
    UNIX cron shedule.
    """

    container_id: str
    """
    UUID of the container invoked by this cron.
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
    Status of the domain.
    """

    url: str
    """
    URL (TBD).
    """

    container_id: str
    """
    UUID of the container.
    """

    hostname: str
    """
    Domain assigned to the container.
    """

    id: str
    """
    UUID of the domain.
    """

    error_message: Optional[str]
    """
    Last error message of the domain.
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
    Contains the severity of the log (info, debug, error, ...).
    """

    id: str

    message: str

    timestamp: Optional[datetime]


@dataclass
class Namespace:
    region: Region
    """
    Region in which the namespace will be created.
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
    Last error message of the namesace.
    """

    description: Optional[str]
    """
    Description of the endpoint.
    """


@dataclass
class Token:
    status: TokenStatus
    """
    Status of the token.
    """

    token: str
    """
    Identifier of the token.
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
    Expiry date of the token.
    """

    container_id: Optional[str]

    namespace_id: Optional[str]


@dataclass
class Trigger:
    container_id: str

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
class CreateContainerRequest:
    name: str
    """
    Name of the container.
    """

    namespace_id: str
    """
    UUID of the namespace the container belongs to.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    timeout: Optional[str]
    """
    Processing time limit for the container.
    """

    description: Optional[str]
    """
    Description of the container.
    """

    max_scale: Optional[int]
    """
    Maximum number of instances to scale the container to.
    """

    memory_limit: Optional[int]
    """
    Memory limit of the container in MB.
    """

    cpu_limit: Optional[int]
    """
    CPU limit of the container in mvCPU.
    """

    environment_variables: Optional[Dict[str, str]]
    """
    Environment variables of the container.
    """

    privacy: Optional[ContainerPrivacy]
    """
    Privacy setting of the container.
    """

    min_scale: Optional[int]
    """
    Minimum number of instances to scale the container to.
    """

    registry_image: Optional[str]
    """
    Name of the registry image (e.g. "rg.fr-par.scw.cloud/something/image:tag").
    """

    max_concurrency: Optional[int]
    """
    Number of maximum concurrent executions of the container.
    """

    protocol: Optional[ContainerProtocol]
    """
    Protocol the container uses.
    """

    port: Optional[int]
    """
    Port the container listens on.
    """

    secret_environment_variables: Optional[List[Secret]]
    """
    Secret environment variables of the container.
    """

    http_option: Optional[ContainerHttpOption]
    """
    Possible values:
 - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
 - enabled: Serve both HTTP and HTTPS traffic.
    """


@dataclass
class CreateCronRequest:
    schedule: str
    """
    UNIX cron shedule.
    """

    container_id: str
    """
    UUID of the container to invoke by the cron.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    args: Optional[Dict[str, Any]]
    """
    Arguments to pass with the cron.
    """

    name: Optional[str]
    """
    Name of the cron to create.
    """


@dataclass
class CreateDomainRequest:
    container_id: str
    """
    UUID of the container to assign the domain to.
    """

    hostname: str
    """
    Domain to assign.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class CreateNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the namespace to create.
    """

    environment_variables: Optional[Dict[str, str]]
    """
    Environment variables of the namespace to create.
    """

    project_id: Optional[str]
    """
    UUID of the Project in which the namespace will be created.
    """

    description: Optional[str]
    """
    Description of the namespace to create.
    """

    secret_environment_variables: Optional[List[Secret]]
    """
    Secret environment variables of the namespace to create.
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
    Expiry date of the token.
    """

    container_id: Optional[str]

    namespace_id: Optional[str]


@dataclass
class CreateTriggerRequest:
    container_id: str

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
class DeleteContainerRequest:
    container_id: str
    """
    UUID of the container to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


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
class DeleteNamespaceRequest:
    namespace_id: str
    """
    UUID of the namespace to delete.
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
class DeployContainerRequest:
    container_id: str
    """
    UUID of the container to deploy.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetContainerRequest:
    container_id: str
    """
    UUID of the container to get.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


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
class GetNamespaceRequest:
    namespace_id: str
    """
    UUID of the namespace to get.
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

    container_id: Optional[str]

    namespace_id: Optional[str]


@dataclass
class ListContainersRequest:
    namespace_id: str
    """
    UUID of the namespace the container belongs to.
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
    Number of containers per page.
    """

    order_by: Optional[ListContainersRequestOrderBy]
    """
    Order of the containers.
    """

    name: Optional[str]
    """
    Name of the container.
    """

    organization_id: Optional[str]
    """
    UUID of the Organization the container belongs to.
    """

    project_id: Optional[str]
    """
    UUID of the Project the container belongs to.
    """


@dataclass
class ListContainersResponse:
    total_count: int
    """
    Total number of containers.
    """

    containers: List[Container]
    """
    Array of containers.
    """


@dataclass
class ListCronsRequest:
    container_id: str
    """
    UUID of the container invoked by the cron.
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
    container_id: str
    """
    UUID of the container the domain belongs to.
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
class ListLogsRequest:
    container_id: str
    """
    UUID of the container.
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

    logs: List[Log]


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
    Name of the namespaces.
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
    """
    Array of the namespaces.
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
    Order of the tokens.
    """

    container_id: Optional[str]
    """
    UUID of the container the token belongs to.
    """

    namespace_id: Optional[str]
    """
    UUID of the namespace the token belongs to.
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

    container_id: Optional[str]

    namespace_id: Optional[str]

    project_id: Optional[str]


@dataclass
class ListTriggersResponse:
    total_count: int

    triggers: List[Trigger]


@dataclass
class UpdateContainerRequest:
    container_id: str
    """
    UUID of the container to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    redeploy: Optional[bool]
    """
    Defines whether to redeploy failed containers.
    """

    privacy: Optional[ContainerPrivacy]
    """
    Privacy settings of the container.
    """

    max_scale: Optional[int]
    """
    Maximum number of instances to scale the container to.
    """

    memory_limit: Optional[int]
    """
    Memory limit of the container in MB.
    """

    cpu_limit: Optional[int]
    """
    CPU limit of the container in mvCPU.
    """

    timeout: Optional[str]
    """
    Processing time limit for the container.
    """

    environment_variables: Optional[Dict[str, str]]
    """
    Environment variables of the container.
    """

    min_scale: Optional[int]
    """
    Minimum number of instances to scale the container to.
    """

    description: Optional[str]
    """
    Description of the container.
    """

    registry_image: Optional[str]
    """
    Name of the registry image (e.g. "rg.fr-par.scw.cloud/something/image:tag").
    """

    max_concurrency: Optional[int]
    """
    Number of maximum concurrent executions of the container.
    """

    protocol: Optional[ContainerProtocol]

    port: Optional[int]

    secret_environment_variables: Optional[List[Secret]]

    http_option: Optional[ContainerHttpOption]
    """
    Possible values:
 - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
 - enabled: Serve both HTTP and HTTPS traffic.
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

    container_id: Optional[str]
    """
    UUID of the container invoked by the cron.
    """

    schedule: Optional[str]
    """
    UNIX cron schedule.
    """

    args: Optional[Dict[str, Any]]
    """
    Arguments to pass with the cron.
    """

    name: Optional[str]
    """
    Name of the cron.
    """


@dataclass
class UpdateNamespaceRequest:
    namespace_id: str
    """
    UUID of the namespace to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    environment_variables: Optional[Dict[str, str]]
    """
    Environment variables of the namespace to update.
    """

    description: Optional[str]
    """
    Description of the namespace to update.
    """

    secret_environment_variables: Optional[List[Secret]]
    """
    Secret environment variables of the namespace to update.
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
