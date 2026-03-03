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


class ContainerSandbox(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SANDBOX = "unknown_sandbox"
    V1 = "v1"
    V2 = "v2"

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
    LOCKING = "locking"
    UPGRADING = "upgrading"

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
    LOCKING = "locking"
    UPGRADING = "upgrading"
    REBALANCING = "rebalancing"

    def __str__(self) -> str:
        return str(self.value)


class DomainStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    CREATING = "creating"
    PENDING = "pending"
    LOCKED = "locked"
    LOCKING = "locking"
    UPGRADING = "upgrading"

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
    LOCKING = "locking"
    UPGRADING = "upgrading"

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
    LOCKED = "locked"
    LOCKING = "locking"
    UPGRADING = "upgrading"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class ContainerHealthCheckSpecHTTPProbe:
    path: str
    """
    Path to use for the HTTP health check.
    """


@dataclass
class ContainerHealthCheckSpecTCPProbe:
    pass


@dataclass
class ContainerHealthCheckSpec:
    failure_threshold: int
    """
    During a deployment, if a newly created container fails to pass the health check, the deployment is aborted. 
As a result, lowering this value can help to reduce the time it takes to detect a failed deployment.
    """

    interval: Optional[str] = None
    """
    Period between health checks.
    """

    http: Optional[ContainerHealthCheckSpecHTTPProbe] = None

    tcp: Optional[ContainerHealthCheckSpecTCPProbe] = None


@dataclass
class ContainerScalingOption:
    concurrent_requests_threshold: Optional[int] = None

    cpu_usage_threshold: Optional[int] = None

    memory_usage_threshold: Optional[int] = None


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
class Container:
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

    environment_variables: dict[str, str]
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

    privacy: ContainerPrivacy
    """
    Privacy setting of the container.
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

    secret_environment_variables: list[SecretHashedValue]
    """
    Secret environment variables of the container.
    """

    http_option: ContainerHttpOption
    """
    Possible values:
 - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
 - enabled: Serve both HTTP and HTTPS traffic.
    """

    sandbox: ContainerSandbox
    """
    Execution environment of the container.
    """

    local_storage_limit: int
    """
    Local storage limit of the container (in MB).
    """

    region: ScwRegion
    """
    Region in which the container will be deployed.
    """

    tags: list[str]
    """
    List of tags applied to the Serverless Container.
    """

    command: list[str]
    """
    Command executed when the container starts. This overrides the default command defined in the container image. This is usually the main executable, or entry point script to run.
    """

    args: list[str]
    """
    Arguments passed to the command specified in the "command" field. These override the default arguments from the container image, and behave like command-line parameters.
    """

    timeout: Optional[str] = None
    """
    Processing time limit for the container.
    """

    error_message: Optional[str] = None
    """
    Last error message of the container.
    """

    description: Optional[str] = None
    """
    Description of the container.
    """

    scaling_option: Optional[ContainerScalingOption] = None
    """
    Possible values:
- concurrent_requests_threshold: Scale depending on the number of concurrent requests being processed per container instance.
- cpu_usage_threshold: Scale depending on the CPU usage of a container instance.
- memory_usage_threshold: Scale depending on the memory usage of a container instance.
    """

    health_check: Optional[ContainerHealthCheckSpec] = None
    """
    Health check configuration of the container.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the container.
    """

    updated_at: Optional[datetime] = None
    """
    Last update date of the container.
    """

    ready_at: Optional[datetime] = None
    """
    Last date when the container was successfully deployed and set to ready.
    """

    private_network_id: Optional[str] = None
    """
    When connected to a Private Network, the container can access other Scaleway resources in this Private Network.
    """


@dataclass
class Cron:
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
    UNIX cron schedule.
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

    error_message: Optional[str] = None
    """
    Last error message of the domain.
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
    Region in which the namespace will be created.
    """

    tags: list[str]
    """
    List of tags applied to the Serverless Container Namespace.
    """

    vpc_integration_activated: bool
    """
    The value of this field doesn't matter anymore, and will be removed in a near future.
    """

    error_message: Optional[str] = None
    """
    Last error message of the namesace.
    """

    description: Optional[str] = None
    """
    Description of the endpoint.
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
    Identifier of the token.
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
    Expiry date of the token.
    """

    container_id: Optional[str] = None

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

    container_id: str
    """
    ID of the container to trigger.
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
class CreateContainerRequest:
    namespace_id: str
    """
    UUID of the namespace the container belongs to.
    """

    name: str
    """
    Name of the container.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Environment variables of the container.
    """

    min_scale: Optional[int] = 0
    """
    Minimum number of instances to scale the container to.
    """

    max_scale: Optional[int] = 0
    """
    Maximum number of instances to scale the container to.
    """

    memory_limit: Optional[int] = 0
    """
    Memory limit of the container in MB.
    """

    cpu_limit: Optional[int] = 0
    """
    CPU limit of the container in mvCPU.
    """

    timeout: Optional[str] = None
    """
    Processing time limit for the container.
    """

    privacy: Optional[ContainerPrivacy] = ContainerPrivacy.UNKNOWN_PRIVACY
    """
    Privacy setting of the container.
    """

    description: Optional[str] = None
    """
    Description of the container.
    """

    registry_image: Optional[str] = None
    """
    Name of the registry image (e.g. "rg.fr-par.scw.cloud/something/image:tag").
    """

    max_concurrency: Optional[int] = 0
    """
    Number of maximum concurrent executions of the container.
    """

    protocol: Optional[ContainerProtocol] = ContainerProtocol.UNKNOWN_PROTOCOL
    """
    Protocol the container uses.
    """

    port: Optional[int] = 0
    """
    Port the container listens on.
    """

    secret_environment_variables: Optional[list[Secret]] = field(default_factory=list)
    """
    Secret environment variables of the container.
    """

    http_option: Optional[ContainerHttpOption] = ContainerHttpOption.UNKNOWN_HTTP_OPTION
    """
    Possible values:
 - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
 - enabled: Serve both HTTP and HTTPS traffic.
    """

    sandbox: Optional[ContainerSandbox] = ContainerSandbox.UNKNOWN_SANDBOX
    """
    Execution environment of the container.
    """

    local_storage_limit: Optional[int] = 0
    """
    Local storage limit of the container (in MB).
    """

    scaling_option: Optional[ContainerScalingOption] = None
    """
    Possible values:
- concurrent_requests_threshold: Scale depending on the number of concurrent requests being processed per container instance.
- cpu_usage_threshold: Scale depending on the CPU usage of a container instance.
- memory_usage_threshold: Scale depending on the memory usage of a container instance.
    """

    health_check: Optional[ContainerHealthCheckSpec] = None
    """
    Health check configuration of the container.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the Serverless Container.
    """

    private_network_id: Optional[str] = None
    """
    When connected to a Private Network, the container can access other Scaleway resources in this Private Network.
    """

    command: Optional[list[str]] = field(default_factory=list)
    """
    Command executed when the container starts. This overrides the default command defined in the container image. This is usually the main executable, or entry point script to run.
    """

    args: Optional[list[str]] = field(default_factory=list)
    """
    Arguments passed to the command specified in the "command" field. These override the default arguments from the container image, and behave like command-line parameters.
    """


@dataclass
class CreateCronRequest:
    container_id: str
    """
    UUID of the container to invoke by the cron.
    """

    schedule: str
    """
    UNIX cron schedule.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    args: Optional[dict[str, Any]] = field(default_factory=dict)
    """
    Arguments to pass with the cron.
    """

    name: Optional[str] = None
    """
    Name of the cron to create.
    """


@dataclass
class CreateDomainRequest:
    hostname: str
    """
    Domain to assign.
    """

    container_id: str
    """
    UUID of the container to assign the domain to.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
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
    """
    Name of the namespace to create.
    """

    environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Environment variables of the namespace to create.
    """

    project_id: Optional[str] = None
    """
    UUID of the Project in which the namespace will be created.
    """

    description: Optional[str] = None
    """
    Description of the namespace to create.
    """

    secret_environment_variables: Optional[list[Secret]] = field(default_factory=list)
    """
    Secret environment variables of the namespace to create.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the Serverless Container Namespace.
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
    Expiry date of the token.
    """

    container_id: Optional[str] = None

    namespace_id: Optional[str] = None


@dataclass
class CreateTriggerRequest:
    name: str
    """
    Name of the trigger.
    """

    container_id: str
    """
    ID of the container to trigger.
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
class DeleteContainerRequest:
    container_id: str
    """
    UUID of the container to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


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
class DeleteNamespaceRequest:
    namespace_id: str
    """
    UUID of the namespace to delete.
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
class DeployContainerRequest:
    container_id: str
    """
    UUID of the container to deploy.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetContainerRequest:
    container_id: str
    """
    UUID of the container to get.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


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
class GetNamespaceRequest:
    namespace_id: str
    """
    UUID of the namespace to get.
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
class ListContainersRequest:
    namespace_id: str
    """
    UUID of the namespace the container belongs to.
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
    Number of containers per page.
    """

    order_by: Optional[ListContainersRequestOrderBy] = (
        ListContainersRequestOrderBy.CREATED_AT_ASC
    )
    """
    Order of the containers.
    """

    name: Optional[str] = None
    """
    Name of the container.
    """

    organization_id: Optional[str] = None
    """
    UUID of the Organization the container belongs to.
    """

    project_id: Optional[str] = None
    """
    UUID of the Project the container belongs to.
    """


@dataclass
class ListContainersResponse:
    containers: list[Container]
    """
    Array of containers.
    """

    total_count: int
    """
    Total number of containers.
    """


@dataclass
class ListCronsRequest:
    container_id: str
    """
    UUID of the container invoked by the cron.
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
    container_id: str
    """
    UUID of the container the domain belongs to.
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
    Name of the namespaces.
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
    """
    Array of the namespaces.
    """

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
    Order of the tokens.
    """

    container_id: Optional[str] = None
    """
    UUID of the container the token belongs to.
    """

    namespace_id: Optional[str] = None
    """
    UUID of the namespace the token belongs to.
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

    container_id: Optional[str] = None

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
class UpdateContainerRequest:
    container_id: str
    """
    UUID of the container to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Environment variables of the container.
    """

    min_scale: Optional[int] = 0
    """
    Minimum number of instances to scale the container to.
    """

    max_scale: Optional[int] = 0
    """
    Maximum number of instances to scale the container to.
    """

    memory_limit: Optional[int] = 0
    """
    Memory limit of the container in MB.
    """

    cpu_limit: Optional[int] = 0
    """
    CPU limit of the container in mvCPU.
    """

    timeout: Optional[str] = None
    """
    Processing time limit for the container.
    """

    redeploy: Optional[bool] = False
    """
    Deprecated: future versions of this API will systematically redeploy containers when needed. As such,
passing `redeploy: false` will be ignored. Relying on this field is discouraged.

To force the redeployment of a container, even if no configuration has changed, use the `DeployContainer` method instead.
    """

    privacy: Optional[ContainerPrivacy] = ContainerPrivacy.UNKNOWN_PRIVACY
    """
    Privacy settings of the container.
    """

    description: Optional[str] = None
    """
    Description of the container.
    """

    registry_image: Optional[str] = None
    """
    Name of the registry image (e.g. "rg.fr-par.scw.cloud/something/image:tag").
    """

    max_concurrency: Optional[int] = 0
    """
    Number of maximum concurrent executions of the container.
    """

    protocol: Optional[ContainerProtocol] = ContainerProtocol.UNKNOWN_PROTOCOL
    """
    Protocol the container uses.
    """

    port: Optional[int] = 0
    """
    Port the container listens on.
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

    http_option: Optional[ContainerHttpOption] = ContainerHttpOption.UNKNOWN_HTTP_OPTION
    """
    Possible values:
 - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
 - enabled: Serve both HTTP and HTTPS traffic.
    """

    sandbox: Optional[ContainerSandbox] = ContainerSandbox.UNKNOWN_SANDBOX
    """
    Execution environment of the container.
    """

    local_storage_limit: Optional[int] = 0
    """
    Local storage limit of the container (in MB).
    """

    scaling_option: Optional[ContainerScalingOption] = None
    """
    Possible values:
- concurrent_requests_threshold: Scale depending on the number of concurrent requests being processed per container instance.
- cpu_usage_threshold: Scale depending on the CPU usage of a container instance.
- memory_usage_threshold: Scale depending on the memory usage of a container instance.
    """

    health_check: Optional[ContainerHealthCheckSpec] = None
    """
    Health check configuration of the container.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the Serverless Container.
    """

    private_network_id: Optional[str] = None
    """
    When connected to a Private Network, the container can access other Scaleway resources in this Private Network.
    """

    command: Optional[list[str]] = field(default_factory=list)
    """
    Command executed when the container starts. This overrides the default command defined in the container image. This is usually the main executable, or entry point script to run.
    """

    args: Optional[list[str]] = field(default_factory=list)
    """
    Arguments passed to the command specified in the "command" field. These override the default arguments from the container image, and behave like command-line parameters.
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

    container_id: Optional[str] = None
    """
    UUID of the container invoked by the cron.
    """

    schedule: Optional[str] = None
    """
    UNIX cron schedule.
    """

    args: Optional[dict[str, Any]] = field(default_factory=dict)
    """
    Arguments to pass with the cron.
    """

    name: Optional[str] = None
    """
    Name of the cron.
    """


@dataclass
class UpdateNamespaceRequest:
    namespace_id: str
    """
    UUID of the namespace to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Environment variables of the namespace to update.
    """

    description: Optional[str] = None
    """
    Description of the namespace to update.
    """

    secret_environment_variables: Optional[list[Secret]] = field(default_factory=list)
    """
    Secret environment variables of the namespace to update.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the Serverless Container Namespace.
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
