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


class ContainerHttpOption(str, Enum):
    UNKNOWN_HTTP_OPTION = "unknown_http_option"
    ENABLED = "enabled"
    REDIRECTED = "redirected"

    def __str__(self) -> str:
        return str(self.value)


class ContainerPrivacy(str, Enum):
    UNKNOWN_PRIVACY = "unknown_privacy"
    PUBLIC = "public"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)


class ContainerProtocol(str, Enum):
    UNKNOWN_PROTOCOL = "unknown_protocol"
    HTTP1 = "http1"
    H2C = "h2c"

    def __str__(self) -> str:
        return str(self.value)


class ContainerStatus(str, Enum):
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


class CronStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"
    CREATING = "creating"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)


class DomainStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    CREATING = "creating"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)


class ListContainersRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListCronsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListDomainsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    HOSTNAME_ASC = "hostname_asc"
    HOSTNAME_DESC = "hostname_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListLogsRequestOrderBy(str, Enum):
    TIMESTAMP_DESC = "timestamp_desc"
    TIMESTAMP_ASC = "timestamp_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListNamespacesRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListTokensRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class LogStream(str, Enum):
    UNKNOWN = "unknown"
    STDOUT = "stdout"
    STDERR = "stderr"

    def __str__(self) -> str:
        return str(self.value)


class NamespaceStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"
    CREATING = "creating"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)


class NullValue(str, Enum):
    NULL_VALUE = "NULL_VALUE"

    def __str__(self) -> str:
        return str(self.value)


class TokenStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    CREATING = "creating"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Container:
    """
    Container.
    """

    id: str
    """
    UUID of the container.
    """

    name: str
    """
    Name of the container.
    """

    namespace_id: str
    """
    UUID of the namespace the container belongs to.
    """

    status: ContainerStatus
    """
    Status of the container.
    """

    environment_variables: Dict[str, str]
    """
    Environment variables of the container.
    """

    min_scale: int
    """
    Minimum number of instances to scale the container to.
    """

    max_scale: int
    """
    Maximum number of instances to scale the container to.
    """

    memory_limit: int
    """
    Memory limit of the container in MB.
    """

    cpu_limit: int
    """
    CPU limit of the container in mvCPU.
    """

    timeout: Optional[str]
    """
    Processing time limit for the container.
    """

    error_message: Optional[str]
    """
    Last error message of the container.
    """

    privacy: ContainerPrivacy
    """
    Privacy setting of the container.
    """

    description: Optional[str]
    """
    Description of the container.
    """

    registry_image: str
    """
    Name of the registry image (e.g. "rg.fr-par.scw.cloud/something/image:tag").
    """

    max_concurrency: int
    """
    Number of maximum concurrent executions of the container.
    """

    domain_name: str
    """
    Domain name attributed to the contaioner.
    """

    protocol: ContainerProtocol
    """
    Protocol the container uses.
    """

    port: int
    """
    Port the container listens on.
    """

    secret_environment_variables: List[SecretHashedValue]
    """
    Secret environment variables of the container.
    """

    http_option: ContainerHttpOption
    """
    Configuration for the handling of HTTP and HTTPS requests.
    Possible values:
     - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
     - enabled: Serve both HTTP and HTTPS traffic.
    """

    region: Region
    """
    Region in which the container will be deployed.
    """


@dataclass
class Cron:
    """
    Cron.
    """

    id: str
    """
    UUID of the cron.
    """

    container_id: str
    """
    UUID of the container invoked by this cron.
    """

    schedule: str
    """
    UNIX cron shedule.
    """

    args: Optional[Dict[str, Any]]
    """
    Arguments to pass with the cron.
    """

    status: CronStatus
    """
    Status of the cron.
    """

    name: str
    """
    Name of the cron.
    """


@dataclass
class Domain:
    """
    Domain.
    """

    id: str
    """
    UUID of the domain.
    """

    hostname: str
    """
    Domain assigned to the container.
    """

    container_id: str
    """
    UUID of the container.
    """

    url: str
    """
    URL (TBD).
    """

    status: DomainStatus
    """
    Status of the domain.
    """

    error_message: Optional[str]
    """
    Last error message of the domain.
    """


@dataclass
class ListContainersResponse:
    """
    List containers response.
    """

    containers: List[Container]
    """
    Array of containers.
    """

    total_count: int
    """
    Total number of containers.
    """


@dataclass
class ListCronsResponse:
    """
    List crons response.
    """

    crons: List[Cron]
    """
    Array of crons.
    """

    total_count: int
    """
    Total number of crons.
    """


@dataclass
class ListDomainsResponse:
    """
    List domains response.
    """

    domains: List[Domain]
    """
    Array of domains.
    """

    total_count: int
    """
    Total number of domains.
    """


@dataclass
class ListLogsResponse:
    """
    List logs response.
    """

    logs: List[Log]

    total_count: int


@dataclass
class ListNamespacesResponse:
    """
    List namespaces response.
    """

    namespaces: List[Namespace]
    """
    Array of the namespaces.
    """

    total_count: int
    """
    Total number of namespaces.
    """


@dataclass
class ListTokensResponse:
    tokens: List[Token]

    total_count: int


@dataclass
class Log:
    """
    Log.
    """

    message: str

    timestamp: Optional[datetime]

    id: str

    level: str
    """
    Contains the severity of the log (info, debug, error, ...).
    """

    source: str
    """
    Source of the log (core runtime or user code).
    """

    stream: LogStream
    """
    Can be stdout or stderr.
    """


@dataclass
class Namespace:
    """
    Namespace.
    """

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

    error_message: Optional[str]
    """
    Last error message of the namesace.
    """

    registry_endpoint: str
    """
    Registry endpoint of the namespace.
    """

    description: Optional[str]
    """
    Description of the endpoint.
    """

    secret_environment_variables: List[SecretHashedValue]
    """
    Secret environment variables of the namespace.
    """

    region: Region
    """
    Region in which the namespace will be created.
    """


@dataclass
class Secret:
    key: str

    value: Optional[str]


@dataclass
class SecretHashedValue:
    key: str

    hashed_value: str


@dataclass
class Token:
    """
    Token.
    """

    id: str
    """
    UUID of the token.
    """

    token: str
    """
    Identifier of the token.
    """

    container_id: Optional[str]
    """
    UUID of the container the token belongs to.
    
    One-of ('scope'): at most one of 'container_id', 'namespace_id' could be set.
    """

    namespace_id: Optional[str]
    """
    UUID of the namespace the token belongs to.
    
    One-of ('scope'): at most one of 'container_id', 'namespace_id' could be set.
    """

    public_key: Optional[str]
    """
    Public key of the token.
    :deprecated
    """

    status: TokenStatus
    """
    Status of the token.
    """

    description: Optional[str]
    """
    Description of the token.
    """

    expires_at: Optional[datetime]
    """
    Expiry date of the token.
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
class GetNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    namespace_id: str
    """
    UUID of the namespace to get.
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
class UpdateNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    namespace_id: str
    """
    UUID of the namespace to update.
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
class DeleteNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    namespace_id: str
    """
    UUID of the namespace to delete.
    """


@dataclass
class ListContainersRequest:
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

    namespace_id: str
    """
    UUID of the namespace the container belongs to.
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
class GetContainerRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    container_id: str
    """
    UUID of the container to get.
    """


@dataclass
class CreateContainerRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    namespace_id: str
    """
    UUID of the namespace the container belongs to.
    """

    name: str
    """
    Name of the container.
    """

    environment_variables: Optional[Dict[str, str]]
    """
    Environment variables of the container.
    """

    min_scale: Optional[int]
    """
    Minimum number of instances to scale the container to.
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

    privacy: ContainerPrivacy
    """
    Privacy setting of the container.
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

    protocol: ContainerProtocol
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

    http_option: ContainerHttpOption
    """
    Configure how HTTP and HTTPS requests are handled.
    Possible values:
     - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
     - enabled: Serve both HTTP and HTTPS traffic.
    """


@dataclass
class UpdateContainerRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    container_id: str
    """
    UUID of the container to update.
    """

    environment_variables: Optional[Dict[str, str]]
    """
    Environment variables of the container.
    """

    min_scale: Optional[int]
    """
    Minimum number of instances to scale the container to.
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

    redeploy: Optional[bool]
    """
    Defines whether to redeploy failed containers.
    """

    privacy: ContainerPrivacy
    """
    Privacy settings of the container.
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

    protocol: ContainerProtocol

    port: Optional[int]

    secret_environment_variables: Optional[List[Secret]]

    http_option: ContainerHttpOption
    """
    Configure how HTTP and HTTPS requests are handled.
    Possible values:
     - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
     - enabled: Serve both HTTP and HTTPS traffic.
    """


@dataclass
class DeleteContainerRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    container_id: str
    """
    UUID of the container to delete.
    """


@dataclass
class DeployContainerRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    container_id: str
    """
    UUID of the container to deploy.
    """


@dataclass
class ListCronsRequest:
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

    container_id: str
    """
    UUID of the container invoked by the cron.
    """


@dataclass
class GetCronRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    cron_id: str
    """
    UUID of the cron to get.
    """


@dataclass
class CreateCronRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    container_id: str
    """
    UUID of the container to invoke by the cron.
    """

    schedule: str
    """
    UNIX cron shedule.
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
class UpdateCronRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    cron_id: str
    """
    UUID of the cron to update.
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
class DeleteCronRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    cron_id: str
    """
    UUID of the cron to delete.
    """


@dataclass
class ListLogsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    container_id: str
    """
    UUID of the container.
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
class ListDomainsRequest:
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

    container_id: str
    """
    UUID of the container the domain belongs to.
    """


@dataclass
class GetDomainRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    domain_id: str
    """
    UUID of the domain to get.
    """


@dataclass
class CreateDomainRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    hostname: str
    """
    Domain to assign.
    """

    container_id: str
    """
    UUID of the container to assign the domain to.
    """


@dataclass
class DeleteDomainRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    domain_id: str
    """
    UUID of the domain to delete.
    """


@dataclass
class IssueJWTRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    container_id: Optional[str]
    """
    One-of ('scope'): at most one of 'container_id', 'namespace_id' could be set.
    """

    namespace_id: Optional[str]
    """
    One-of ('scope'): at most one of 'container_id', 'namespace_id' could be set.
    """

    expires_at: Optional[datetime]


@dataclass
class CreateTokenRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    container_id: Optional[str]
    """
    UUID of the container to create the token for.
    
    One-of ('scope'): at most one of 'container_id', 'namespace_id' could be set.
    """

    namespace_id: Optional[str]
    """
    UUID of the namespace to create the token for.
    
    One-of ('scope'): at most one of 'container_id', 'namespace_id' could be set.
    """

    description: Optional[str]
    """
    Description of the token.
    """

    expires_at: Optional[datetime]
    """
    Expiry date of the token.
    """


@dataclass
class GetTokenRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    token_id: str
    """
    UUID of the token to get.
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
class DeleteTokenRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    token_id: str
    """
    UUID of the token to delete.
    """
