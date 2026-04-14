# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


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
    UNKNOWN_STATUS = "unknown_status"
    UPDATING = "updating"
    DELETING = "deleting"
    LOCKING = "locking"
    READY = "ready"
    ERROR = "error"
    LOCKED = "locked"
    CREATING = "creating"
    UPGRADING = "upgrading"

    def __str__(self) -> str:
        return str(self.value)


class CreateTriggerRequestDestinationConfigHttpMethod(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_HTTP_METHOD = "unknown_http_method"
    GET = "get"
    POST = "post"
    PUT = "put"
    PATCH = "patch"
    DELETE = "delete"

    def __str__(self) -> str:
        return str(self.value)


class DomainStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    CREATING = "creating"
    UPDATING = "updating"
    DELETING = "deleting"
    READY = "ready"
    ERROR = "error"
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


class ListTriggersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class NamespaceStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    UPDATING = "updating"
    DELETING = "deleting"
    LOCKING = "locking"
    READY = "ready"
    ERROR = "error"
    LOCKED = "locked"
    CREATING = "creating"
    UPGRADING = "upgrading"

    def __str__(self) -> str:
        return str(self.value)


class TriggerDestinationConfigHttpMethod(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_HTTP_METHOD = "unknown_http_method"
    GET = "get"
    POST = "post"
    PUT = "put"
    PATCH = "patch"
    DELETE = "delete"

    def __str__(self) -> str:
        return str(self.value)


class TriggerSourceType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SOURCE_TYPE = "unknown_source_type"
    CRON = "cron"
    SQS = "sqs"
    NATS = "nats"

    def __str__(self) -> str:
        return str(self.value)


class TriggerStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    UPDATING = "updating"
    CREATING = "creating"
    LOCKING = "locking"
    LOCKED = "locked"
    UPGRADING = "upgrading"

    def __str__(self) -> str:
        return str(self.value)


class UpdateTriggerRequestDestinationConfigHttpMethod(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_HTTP_METHOD = "unknown_http_method"
    GET = "get"
    POST = "post"
    PUT = "put"
    PATCH = "patch"
    DELETE = "delete"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class ContainerProbeHTTPProbe:
    path: str
    """
    HTTP path to perform the check on.
    """


@dataclass
class ContainerProbeTCPProbe:
    pass


@dataclass
class ContainerProbe:
    failure_threshold: int
    """
    Unhealthy containers do not receive traffic from incoming requests.
    """

    interval: Optional[str] = None
    """
    Time interval between checks.
    """

    timeout: Optional[str] = None
    """
    Duration before the check times out.
    """

    tcp: Optional[ContainerProbeTCPProbe] = None

    http: Optional[ContainerProbeHTTPProbe] = None


@dataclass
class ContainerScalingOption:
    concurrent_requests_threshold: Optional[int] = 0

    cpu_usage_threshold: Optional[int] = 0

    memory_usage_threshold: Optional[int] = 0


@dataclass
class TriggerCronConfig:
    schedule: str
    """
    UNIX cron schedule to run job (e.g., "* * * * *").
    """

    timezone: str
    """
    Timezone for the cron schedule, in tz database format (e.g., "Europe/Paris").
    """

    body: str
    """
    Body to send to the container when the trigger is invoked.
    """

    headers: dict[str, str]
    """
    Additional headers to send to the container when the trigger is invoked.
    """


@dataclass
class TriggerDestinationConfig:
    http_path: str
    """
    The HTTP path to send the request to (e.g., "/my-webhook-endpoint").
    """

    http_method: TriggerDestinationConfigHttpMethod
    """
    The HTTP method to use when sending the request (e.g., get, post, put, patch, delete). Must be specified as lowercase.
    """


@dataclass
class TriggerNATSConfig:
    server_urls: list[str]
    """
    The URLs of the NATS servers (e.g., "nats://nats.mnq.fr-par.scaleway.com:4222").
    """

    subject: str
    """
    NATS subject to subscribe to (e.g., "my-subject").
    """


@dataclass
class TriggerSQSConfig:
    region: ScwRegion
    """
    The region where the SQS queue is hosted (e.g., "fr-par", "nl-ams").
    """

    endpoint: str
    """
    Endpoint URL to use to access SQS (e.g., "https://sqs.mnq.fr-par.scaleway.com").
    """

    access_key_id: str
    """
    The access key for accessing the SQS queue.
    """

    queue_url: str
    """
    The URL of the SQS queue to monitor for messages.
    """


@dataclass
class UpdateContainerRequestProbeHTTPProbe:
    path: Optional[str] = None


@dataclass
class UpdateContainerRequestProbeTCPProbe:
    pass


@dataclass
class CreateTriggerRequestCronConfig:
    schedule: str
    """
    UNIX cron schedule to run job (e.g., "* * * * *").
    """

    timezone: str
    """
    Timezone for the cron schedule, in tz database format (e.g., "Europe/Paris").
    """

    body: str
    """
    Body to send to the container when the trigger is invoked.
    """

    headers: dict[str, str]
    """
    Additional headers to send to the container when the trigger is invoked.
    """


@dataclass
class CreateTriggerRequestDestinationConfig:
    http_path: str
    """
    The HTTP path to send the request to (e.g., "/my-webhook-endpoint").
    """

    http_method: CreateTriggerRequestDestinationConfigHttpMethod
    """
    The HTTP method to use when sending the request (e.g., get, post, put, patch, delete). Must be specified as lowercase.
    """


@dataclass
class CreateTriggerRequestNATSConfig:
    server_urls: list[str]
    """
    The URLs of the NATS server (e.g., "nats://nats.mnq.fr-par.scaleway.com:4222").
    """

    subject: str
    """
    NATS subject to subscribe to (e.g., "my-subject").
    """

    credentials_file_content: str
    """
    The credentials from this file will be used to authenticate with the NATS server and subscribe to the specified subject.
    """


@dataclass
class CreateTriggerRequestSQSConfig:
    region: ScwRegion
    """
    The region where the SQS queue is hosted (e.g., "fr-par", "nl-ams").
    """

    endpoint: str
    """
    Endpoint URL to use to access SQS (e.g., "https://sqs.mnq.fr-par.scaleway.com").
    """

    access_key_id: str
    """
    The access key for accessing the SQS queue.
    """

    secret_access_key: str
    """
    The secret key for accessing the SQS queue.
    """

    queue_url: str
    """
    The URL of the SQS queue to monitor for messages.
    """


@dataclass
class Container:
    id: str
    """
    Container unique ID.
    """

    name: str
    """
    Container name.
    """

    namespace_id: str
    """
    Unique ID of the namespace the container belongs to.
    """

    description: str
    """
    Container description.
    """

    status: ContainerStatus
    """
    Container status.
    """

    environment_variables: dict[str, str]
    """
    Environment variables of the container.
    """

    secret_environment_variables: dict[str, str]
    """
    Secret environment variables of the container.
    """

    min_scale: int
    """
    Minimum number of instances to scale the container to.
    """

    max_scale: int
    """
    Maximum number of instances to scale the container to.
    """

    memory_limit_bytes: int
    """
    Memory limit of the container in bytes.
    """

    mvcpu_limit: int
    """
    CPU limit of the container in mvCPU.
    """

    local_storage_limit_bytes: int
    """
    Local storage limit of the container (in bytes).
    """

    privacy: ContainerPrivacy
    """
    Privacy policy of the container.
    """

    image: str
    """
    Image reference (e.g. "rg.fr-par.scw.cloud/my-registry-namespace/image:tag").
    """

    protocol: ContainerProtocol
    """
    Protocol the container uses.
    """

    port: int
    """
    Port the container listens on.
    """

    https_connections_only: bool
    """
    If true, it will allow only HTTPS connections to access your container to prevent it from being triggered by insecure connections (HTTP).
    """

    sandbox: ContainerSandbox
    """
    Execution environment of the container.
    """

    tags: list[str]
    """
    Tags of the Serverless Container.
    """

    command: list[str]
    """
    Command executed when the container starts. This overrides the default command defined in the container image. This is usually the main executable, or ENTRYPOINT script to run.
    """

    args: list[str]
    """
    Arguments passed to the command specified in the "command" field. These override the default arguments from the container image, and behave like command-line parameters.
    """

    public_endpoint: str
    """
    This is the default endpoint generated by Scaleway to access the container from the Internet.
    """

    region: ScwRegion
    """
    Region in which the container exists.
    """

    error_message: Optional[str] = None
    """
    Container last error message.
    """

    created_at: Optional[datetime] = None
    """
    Container creation date.
    """

    updated_at: Optional[datetime] = None
    """
    Container last update date.
    """

    timeout: Optional[str] = None
    """
    Processing time limit for the container.
    """

    scaling_option: Optional[ContainerScalingOption] = None
    """
    Parameter used to decide when to scale up or down.
    """

    liveness_probe: Optional[ContainerProbe] = None
    """
    If the liveness probe fails, the container will be restarted.
It is performed periodically during the container's lifetime. The liveness probe is not executed until the startup probe (if defined) is successful.

Possible check types:
- http: Perform HTTP check on the container with the specified path.
- tcp: Perform TCP check on the container.
    """

    startup_probe: Optional[ContainerProbe] = None
    """
    If the startup probe fails, the container will be restarted.
This check is useful for applications that might take a long time to start. It is only performed when the container is starting.

Possible check types:
- http: Perform HTTP check on the container with the specified path.
- tcp: Perform TCP check on the container.
    """

    private_network_id: Optional[str] = None
    """
    When connected to a Private Network, the container can access other Scaleway resources in this Private Network.
    """


@dataclass
class Domain:
    id: str
    """
    Domain unique ID.
    """

    container_id: str
    """
    Unique ID of the container the domain is assigned to.
    """

    hostname: str
    """
    Domain assigned to the container.
    """

    status: DomainStatus
    """
    Domain status.
    """

    tags: list[str]
    """
    A list of arbitrary tags associated with the domain.
    """

    error_message: Optional[str] = None
    """
    Domain last error message.
    """

    created_at: Optional[datetime] = None
    """
    Domain creation date.
    """

    updated_at: Optional[datetime] = None
    """
    Domain last update date.
    """


@dataclass
class Namespace:
    id: str
    """
    Namespace unique ID.
    """

    name: str
    """
    Namespace name.
    """

    organization_id: str
    """
    Unique ID of the Organization the namespace belongs to.
    """

    project_id: str
    """
    Unique ID of the Project the namespace belongs to.
    """

    description: str
    """
    Namespace description.
    """

    status: NamespaceStatus
    """
    Namespace status.
    """

    environment_variables: dict[str, str]
    """
    Namespace environment variables.
    """

    secret_environment_variables: dict[str, str]
    """
    Namespace secret environment variables.
    """

    tags: list[str]
    """
    A list of arbitrary tags associated with the namespace.
    """

    region: ScwRegion
    """
    Region in which the namespace will be created.
    """

    error_message: Optional[str] = None
    """
    Namespace last error message.
    """

    created_at: Optional[datetime] = None
    """
    Namespace creation date.
    """

    updated_at: Optional[datetime] = None
    """
    Namespace last update date.
    """


@dataclass
class Trigger:
    id: str
    """
    Trigger unique ID.
    """

    name: str
    """
    Name of the trigger.
    """

    description: str
    """
    Description of the trigger.
    """

    tags: list[str]
    """
    Tags of the trigger.
    """

    status: TriggerStatus
    """
    Trigger status.
    """

    container_id: str
    """
    ID of the container to trigger.
    """

    source_type: TriggerSourceType
    """
    Type of source that will trigger the container.
    """

    error_message: Optional[str] = None
    """
    Trigger last error message.
    """

    destination_config: Optional[TriggerDestinationConfig] = None
    """
    Configuration of the destination to trigger.
    """

    created_at: Optional[datetime] = None
    """
    Trigger creation date.
    """

    updated_at: Optional[datetime] = None
    """
    Trigger last update date.
    """

    cron_config: Optional[TriggerCronConfig] = None

    sqs_config: Optional[TriggerSQSConfig] = None

    nats_config: Optional[TriggerNATSConfig] = None


@dataclass
class UpdateContainerRequestProbe:
    failure_threshold: Optional[int] = None
    interval: Optional[str] = None
    timeout: Optional[str] = None
    http: Optional[UpdateContainerRequestProbeHTTPProbe] = None

    tcp: Optional[UpdateContainerRequestProbeTCPProbe] = None


@dataclass
class UpdateTriggerRequestCronConfig:
    schedule: Optional[str] = None
    """
    UNIX cron schedule to run job (e.g., "* * * * *").
    """

    timezone: Optional[str] = None
    """
    Timezone for the cron schedule, in tz database format (e.g., "Europe/Paris").
    """

    body: Optional[str] = None
    """
    Body to send to the container when the trigger is invoked.
    """

    headers: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Additional headers to send to the container when the trigger is invoked.
    """


@dataclass
class UpdateTriggerRequestDestinationConfig:
    http_path: Optional[str] = None
    """
    The HTTP path to send the request to (e.g., "/my-webhook-endpoint").
    """

    http_method: Optional[UpdateTriggerRequestDestinationConfigHttpMethod] = (
        UpdateTriggerRequestDestinationConfigHttpMethod.UNKNOWN_HTTP_METHOD
    )
    """
    The HTTP method to use when sending the request (e.g., get, post, put, patch, delete). Must be specified as lowercase.
    """


@dataclass
class UpdateTriggerRequestNATSConfig:
    server_urls: Optional[list[str]] = field(default_factory=list)
    """
    The URLs of the NATS server (e.g., "nats://nats.mnq.fr-par.scaleway.com:4222").
    """

    subject: Optional[str] = None
    """
    NATS subject to subscribe to (e.g., "my-subject").
    """

    credentials_file_content: Optional[str] = None
    """
    The credentials from this file will be used to authenticate with the NATS server and subscribe to the specified subject.
    """


@dataclass
class UpdateTriggerRequestSQSConfig:
    region: Optional[ScwRegion] = None
    """
    The region where the SQS queue is hosted (e.g., "fr-par", "nl-ams").
    """

    endpoint: Optional[str] = None
    """
    Endpoint URL to use to access SQS (e.g., "https://sqs.mnq.fr-par.scaleway.com").
    """

    access_key_id: Optional[str] = None
    """
    The access key for accessing the SQS queue.
    """

    secret_access_key: Optional[str] = None
    """
    The secret key for accessing the SQS queue.
    """

    queue_url: Optional[str] = None
    """
    The URL of the SQS queue to monitor for messages.
    """


@dataclass
class CreateContainerRequest:
    namespace_id: str
    """
    Unique ID of the namespace the container belongs to.
    """

    name: str
    """
    Container name.
    """

    image: str
    """
    Image reference (e.g. "rg.fr-par.scw.cloud/my-registry-namespace/image:tag").
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Environment variables of the container.
    """

    secret_environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Secret environment variables of the container.
    """

    min_scale: Optional[int] = 0
    """
    Minimum number of instances to scale the container to.
    """

    max_scale: Optional[int] = 0
    """
    Maximum number of instances to scale the container to.
    """

    memory_limit_bytes: Optional[int] = 0
    """
    Memory limit of the container in bytes.
    """

    mvcpu_limit: Optional[int] = 0
    """
    CPU limit of the container in mvCPU.
    """

    timeout: Optional[str] = None
    """
    Processing time limit for the container.
    """

    privacy: Optional[ContainerPrivacy] = ContainerPrivacy.UNKNOWN_PRIVACY
    """
    Privacy policy of the container.
    """

    description: Optional[str] = None
    """
    Container description.
    """

    protocol: Optional[ContainerProtocol] = ContainerProtocol.UNKNOWN_PROTOCOL
    """
    Protocol the container uses.
    """

    port: Optional[int] = 0
    """
    Port the container listens on.
    """

    https_connections_only: Optional[bool] = False
    """
    If true, it will allow only HTTPS connections to access your container to prevent it from being triggered by insecure connections (HTTP).
    """

    sandbox: Optional[ContainerSandbox] = ContainerSandbox.UNKNOWN_SANDBOX
    """
    Execution environment of the container.
    """

    local_storage_limit_bytes: Optional[int] = 0
    """
    Local storage limit of the container (in bytes).
    """

    scaling_option: Optional[ContainerScalingOption] = None
    """
    Parameter used to decide when to scale up or down.
    """

    liveness_probe: Optional[ContainerProbe] = None
    """
    If the liveness probe fails, the container will be restarted.
It is performed periodically during the container's lifetime. The liveness probe is not executed until the startup probe (if defined) is successful.

Possible check types:
- http: Perform HTTP check on the container with the specified path.
- tcp: Perform TCP check on the container.
    """

    startup_probe: Optional[ContainerProbe] = None
    """
    If the startup probe fails, the container will be restarted.
This check is useful for applications that might take a long time to start. It is only performed when the container is starting.

Possible check types:
- http: Perform HTTP check on the container with the specified path.
- tcp: Perform TCP check on the container.
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
    Command executed when the container starts. This overrides the default command defined in the container image. This is usually the main executable, or ENTRYPOINT script to run.
    """

    args: Optional[list[str]] = field(default_factory=list)
    """
    Arguments passed to the command specified in the "command" field. These override the default arguments from the container image, and behave like command-line parameters.
    """


@dataclass
class CreateDomainRequest:
    container_id: str
    """
    Unique ID of the container the domain will be assigned to.
    """

    hostname: str
    """
    Domain assigned to the container.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    A list of arbitrary tags associated with the domain.
    """


@dataclass
class CreateNamespaceRequest:
    name: str
    """
    Namespace name.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    Unique ID of the Project the namespace belongs to.
    """

    description: Optional[str] = None
    """
    Namespace description.
    """

    environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Namespace environment variables.
    """

    secret_environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Namespace secret environment variables.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    A list of arbitrary tags associated with the namespace.
    """


@dataclass
class CreateTriggerRequest:
    container_id: str
    """
    ID of the container to trigger.
    """

    name: str
    """
    Name of the trigger.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    description: Optional[str] = None
    """
    Description of the trigger.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the trigger.
    """

    destination_config: Optional[CreateTriggerRequestDestinationConfig] = None
    """
    Configuration of the destination to trigger.
    """

    cron_config: Optional[CreateTriggerRequestCronConfig] = None

    sqs_config: Optional[CreateTriggerRequestSQSConfig] = None

    nats_config: Optional[CreateTriggerRequestNATSConfig] = None


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
class GetContainerRequest:
    container_id: str
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetDomainRequest:
    domain_id: str
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetNamespaceRequest:
    namespace_id: str
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetServiceInfoRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetTriggerRequest:
    trigger_id: str
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListContainersRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = None
    page_size: Optional[int] = None
    order_by: Optional[ListContainersRequestOrderBy] = None
    organization_id: Optional[str] = None
    project_id: Optional[str] = None
    namespace_id: Optional[str] = None
    name: Optional[str] = None


@dataclass
class ListContainersResponse:
    containers: list[Container]
    total_count: int


@dataclass
class ListDomainsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = None
    page_size: Optional[int] = None
    order_by: Optional[ListDomainsRequestOrderBy] = None
    organization_id: Optional[str] = None
    project_id: Optional[str] = None
    namespace_id: Optional[str] = None
    container_id: Optional[str] = None


@dataclass
class ListDomainsResponse:
    domains: list[Domain]
    total_count: int


@dataclass
class ListNamespacesRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = None
    page_size: Optional[int] = None
    order_by: Optional[ListNamespacesRequestOrderBy] = None
    organization_id: Optional[str] = None
    project_id: Optional[str] = None
    name: Optional[str] = None


@dataclass
class ListNamespacesResponse:
    namespaces: list[Namespace]
    total_count: int


@dataclass
class ListTriggersRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = None
    page_size: Optional[int] = None
    order_by: Optional[ListTriggersRequestOrderBy] = None
    organization_id: Optional[str] = None
    project_id: Optional[str] = None
    namespace_id: Optional[str] = None
    container_id: Optional[str] = None


@dataclass
class ListTriggersResponse:
    triggers: list[Trigger]
    total_count: int


@dataclass
class RedeployContainerRequest:
    container_id: str
    """
    ID of the container to redeploy.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
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

    secret_environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Secret environment variables of the container.
    """

    min_scale: Optional[int] = 0
    """
    Minimum number of instances to scale the container to.
    """

    max_scale: Optional[int] = 0
    """
    Maximum number of instances to scale the container to.
    """

    memory_limit_bytes: Optional[int] = 0
    """
    Memory limit of the container in bytes.
    """

    mvcpu_limit: Optional[int] = 0
    """
    CPU limit of the container in mvCPU.
    """

    timeout: Optional[str] = None
    """
    Processing time limit for the container.
    """

    privacy: Optional[ContainerPrivacy] = ContainerPrivacy.UNKNOWN_PRIVACY
    """
    Privacy policy of the container.
    """

    description: Optional[str] = None
    """
    Container description.
    """

    image: Optional[str] = None
    """
    Image reference (e.g. "rg.fr-par.scw.cloud/my-registry-namespace/image:tag").
    """

    protocol: Optional[ContainerProtocol] = ContainerProtocol.UNKNOWN_PROTOCOL
    """
    Protocol the container uses.
    """

    port: Optional[int] = 0
    """
    Port the container listens on.
    """

    https_connection_only: Optional[bool] = False
    """
    If true, it will allow only HTTPS connections to access your container to prevent it from being triggered by insecure connections (HTTP).
    """

    sandbox: Optional[ContainerSandbox] = ContainerSandbox.UNKNOWN_SANDBOX
    """
    Execution environment of the container.
    """

    local_storage_limit_bytes: Optional[int] = 0
    """
    Local storage limit of the container (in bytes).
    """

    scaling_option: Optional[ContainerScalingOption] = None
    """
    Parameter used to decide when to scale up or down.
    """

    liveness_probe: Optional[ContainerProbe] = None
    """
    If the liveness probe fails, the container will be restarted.
It is performed periodically during the container's lifetime. The liveness probe is not executed until the startup probe (if defined) is successful.

Possible check types:
- http: Perform HTTP check on the container with the specified path.
- tcp: Perform TCP check on the container.
    """

    startup_probe: Optional[UpdateContainerRequestProbe] = None
    """
    If the startup probe fails, the container will be restarted.
This check is useful for applications that might take a long time to start. It is only performed when the container is starting.

Possible check types:
- http: Perform HTTP check on the container with the specified path.
- tcp: Perform TCP check on the container.
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
    Command executed when the container starts. This overrides the default command defined in the container image. This is usually the main executable, or ENTRYPOINT script to run.
    """

    args: Optional[list[str]] = field(default_factory=list)
    """
    Arguments passed to the command specified in the "command" field. These override the default arguments from the container image, and behave like command-line parameters.
    """


@dataclass
class UpdateDomainRequest:
    domain_id: str
    """
    UUID of the domain to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    A list of arbitrary tags associated with the domain.
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

    description: Optional[str] = None
    """
    Namespace description.
    """

    environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Namespace environment variables.
    """

    secret_environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Namespace secret environment variables.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    A list of arbitrary tags associated with the namespace.
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

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the trigger.
    """

    destination_config: Optional[UpdateTriggerRequestDestinationConfig] = None
    """
    Configuration of the destination to trigger.
    """

    cron_config: Optional[UpdateTriggerRequestCronConfig] = None

    sqs_config: Optional[UpdateTriggerRequestSQSConfig] = None

    nats_config: Optional[UpdateTriggerRequestNATSConfig] = None
