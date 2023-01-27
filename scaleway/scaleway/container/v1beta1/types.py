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
    Container
    """

    id: str

    name: str

    namespace_id: str

    status: ContainerStatus

    environment_variables: Dict[str, str]

    min_scale: int

    max_scale: int

    memory_limit: int

    cpu_limit: int

    timeout: Optional[str]

    error_message: Optional[str]

    privacy: ContainerPrivacy

    description: Optional[str]

    registry_image: str

    max_concurrency: int

    domain_name: str

    protocol: ContainerProtocol

    port: int

    secret_environment_variables: List[SecretHashedValue]

    http_option: ContainerHttpOption
    """
    possible values:
     - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
     - enabled: Serve both HTTP and HTTPS traffic.
    
    """

    region: Region


@dataclass
class Cron:
    """
    Cron
    """

    id: str

    container_id: str

    schedule: str

    args: Optional[Dict[str, Any]]

    status: CronStatus

    name: str


@dataclass
class Domain:
    """
    Domain
    """

    id: str

    hostname: str

    container_id: str

    url: str

    status: DomainStatus

    error_message: Optional[str]


@dataclass
class ListContainersResponse:
    """
    List containers response
    """

    containers: List[Container]

    total_count: int


@dataclass
class ListCronsResponse:
    """
    List crons response
    """

    crons: List[Cron]

    total_count: int


@dataclass
class ListDomainsResponse:
    """
    List domains response
    """

    domains: List[Domain]

    total_count: int


@dataclass
class ListLogsResponse:
    """
    List logs response
    """

    logs: List[Log]

    total_count: int


@dataclass
class ListNamespacesResponse:
    """
    List namespaces response
    """

    namespaces: List[Namespace]

    total_count: int


@dataclass
class ListTokensResponse:
    tokens: List[Token]

    total_count: int


@dataclass
class Log:
    """
    Log
    """

    message: str

    timestamp: Optional[datetime]

    id: str

    level: str
    """
    Contains the severity of the log (info, debug, error, ...)
    """

    source: str
    """
    Source of the log (core runtime or user code)
    """

    stream: LogStream
    """
    Can be stdout or stderr
    """


@dataclass
class Namespace:
    """
    Namespace
    """

    id: str

    name: str

    environment_variables: Dict[str, str]

    organization_id: str

    project_id: str

    status: NamespaceStatus

    registry_namespace_id: str

    error_message: Optional[str]

    registry_endpoint: str

    description: Optional[str]

    secret_environment_variables: List[SecretHashedValue]

    region: Region


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
    Token
    """

    id: str

    token: str

    container_id: Optional[str]
    """
    One-of ('scope'): at most one of 'container_id', 'namespace_id' could be set.
    """

    namespace_id: Optional[str]
    """
    One-of ('scope'): at most one of 'container_id', 'namespace_id' could be set.
    """

    public_key: Optional[str]
    """
    :deprecated
    """

    status: TokenStatus

    description: Optional[str]

    expires_at: Optional[datetime]


@dataclass
class ListNamespacesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListNamespacesRequestOrderBy]

    name: Optional[str]

    organization_id: Optional[str]

    project_id: Optional[str]


@dataclass
class GetNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    namespace_id: str


@dataclass
class CreateNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    name: Optional[str]

    environment_variables: Optional[Dict[str, str]]

    project_id: Optional[str]

    description: Optional[str]

    secret_environment_variables: Optional[List[Secret]]


@dataclass
class UpdateNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    namespace_id: str

    environment_variables: Optional[Dict[str, str]]

    description: Optional[str]

    secret_environment_variables: Optional[List[Secret]]


@dataclass
class DeleteNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    namespace_id: str


@dataclass
class ListContainersRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListContainersRequestOrderBy]

    namespace_id: str

    name: Optional[str]

    organization_id: Optional[str]

    project_id: Optional[str]


@dataclass
class GetContainerRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    container_id: str


@dataclass
class CreateContainerRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    namespace_id: str

    name: Optional[str]

    environment_variables: Optional[Dict[str, str]]

    min_scale: Optional[int]

    max_scale: Optional[int]

    memory_limit: Optional[int]

    timeout: Optional[str]

    privacy: ContainerPrivacy

    description: Optional[str]

    registry_image: Optional[str]

    max_concurrency: Optional[int]

    protocol: ContainerProtocol

    port: Optional[int]

    secret_environment_variables: Optional[List[Secret]]

    http_option: ContainerHttpOption
    """
    possible values:
     - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
     - enabled: Serve both HTTP and HTTPS traffic.
    
    """


@dataclass
class UpdateContainerRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    container_id: str

    environment_variables: Optional[Dict[str, str]]

    min_scale: Optional[int]

    max_scale: Optional[int]

    memory_limit: Optional[int]

    timeout: Optional[str]

    redeploy: Optional[bool]

    privacy: ContainerPrivacy

    description: Optional[str]

    registry_image: Optional[str]

    max_concurrency: Optional[int]

    protocol: ContainerProtocol

    port: Optional[int]

    secret_environment_variables: Optional[List[Secret]]

    http_option: ContainerHttpOption
    """
    possible values:
     - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
     - enabled: Serve both HTTP and HTTPS traffic.
    
    """


@dataclass
class DeleteContainerRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    container_id: str


@dataclass
class DeployContainerRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    container_id: str


@dataclass
class ListCronsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListCronsRequestOrderBy]

    container_id: str


@dataclass
class GetCronRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    cron_id: str


@dataclass
class CreateCronRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    container_id: str

    schedule: str

    args: Optional[Dict[str, Any]]

    name: Optional[str]


@dataclass
class UpdateCronRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    cron_id: str

    container_id: Optional[str]

    schedule: Optional[str]

    args: Optional[Dict[str, Any]]

    name: Optional[str]


@dataclass
class DeleteCronRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    cron_id: str


@dataclass
class ListLogsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    container_id: str

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListLogsRequestOrderBy]


@dataclass
class ListDomainsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListDomainsRequestOrderBy]

    container_id: str


@dataclass
class GetDomainRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    domain_id: str


@dataclass
class CreateDomainRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    hostname: str

    container_id: str


@dataclass
class DeleteDomainRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    domain_id: str


@dataclass
class IssueJWTRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
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
    Region to target. If none is passed will use default region from the config
    """

    container_id: Optional[str]
    """
    One-of ('scope'): at most one of 'container_id', 'namespace_id' could be set.
    """

    namespace_id: Optional[str]
    """
    One-of ('scope'): at most one of 'container_id', 'namespace_id' could be set.
    """

    description: Optional[str]

    expires_at: Optional[datetime]


@dataclass
class GetTokenRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    token_id: str


@dataclass
class ListTokensRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListTokensRequestOrderBy]

    container_id: Optional[str]

    namespace_id: Optional[str]


@dataclass
class DeleteTokenRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    token_id: str
