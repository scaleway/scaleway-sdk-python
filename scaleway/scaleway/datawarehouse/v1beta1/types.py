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


class DeploymentStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    READY = "ready"
    CREATING = "creating"
    CONFIGURING = "configuring"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"
    LOCKING = "locking"
    UNLOCKING = "unlocking"

    def __str__(self) -> str:
        return str(self.value)


class EndpointServiceProtocol(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_PROTOCOL = "unknown_protocol"
    TCP = "tcp"
    HTTPS = "https"
    MYSQL = "mysql"

    def __str__(self) -> str:
        return str(self.value)


class ListDatabasesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    SIZE_ASC = "size_asc"
    SIZE_DESC = "size_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListDeploymentsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListUsersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class EndpointPrivateNetworkDetails:
    private_network_id: str


@dataclass
class EndpointPublicDetails:
    pass


@dataclass
class EndpointService:
    protocol: EndpointServiceProtocol
    port: int


@dataclass
class EndpointSpecPrivateNetworkDetails:
    private_network_id: str
    """
    UUID of the Private Network.
    """


@dataclass
class EndpointSpecPublicDetails:
    pass


@dataclass
class Endpoint:
    id: str
    """
    Unique identifier of the endpoint.
    """

    dns_record: str
    """
    DNS record associated with the endpoint.
    """

    services: list[EndpointService]
    """
    List of services associated with the endpoint.
    """

    private_network: Optional[EndpointPrivateNetworkDetails] = None

    public: Optional[EndpointPublicDetails] = None


@dataclass
class EndpointSpec:
    public: Optional[EndpointSpecPublicDetails] = None

    private_network: Optional[EndpointSpecPrivateNetworkDetails] = None


@dataclass
class Database:
    name: str
    """
    Name of the database.
    """

    size: int
    """
    Size of the database.
    """


@dataclass
class Deployment:
    id: str
    """
    Unique identifier.
    """

    name: str
    """
    Name of the deployment.
    """

    organization_id: str
    """
    Organization ID.
    """

    project_id: str
    """
    Project ID.
    """

    status: DeploymentStatus
    """
    Status of the deployment.
    """

    tags: list[str]
    """
    List of tags applied to the deployment.
    """

    version: str
    """
    Clickhouse version.
    """

    replica_count: int
    """
    Number of replicas for the deployment.
    """

    cpu_min: int
    """
    Minimum CPU count for the deployment.
    """

    cpu_max: int
    """
    Maximum CPU count for the deployment.
    """

    endpoints: list[Endpoint]
    """
    List of endpoints associated with the deployment.
    """

    ram_per_cpu: int
    """
    RAM per CPU count for the deployment (in GB).
    """

    region: ScwRegion
    """
    Region of the deployment.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the deployment.
    """

    updated_at: Optional[datetime] = None
    """
    Last modification date of the deployment.
    """


@dataclass
class Preset:
    name: str
    """
    Name of the preset.
    """

    category: str
    """
    Category of the preset.
    """

    cpu_min: int
    """
    Minimum CPU count for the preset.
    """

    cpu_max: int
    """
    Maximum CPU count for the preset.
    """

    ram_per_cpu: int
    """
    RAM per CPU count for the preset (in GB).
    """

    replica_count: int
    """
    Number of replicas for the preset.
    """


@dataclass
class User:
    name: str
    """
    Name of the user.
    """

    is_admin: bool
    """
    Indicates if the user is an administrator.
    """


@dataclass
class Version:
    version: str
    """
    Deployment version.
    """

    end_of_life_at: Optional[datetime] = None
    """
    Date of End of Life.
    """


@dataclass
class CreateDatabaseRequest:
    deployment_id: str
    """
    UUID of the deployment.
    """

    name: str
    """
    Name of the database.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class CreateDeploymentRequest:
    name: str
    """
    Name of the deployment.
    """

    version: str
    """
    Clickhouse version to use for the deployment.
    """

    replica_count: int
    """
    Number of replicas for the deployment.
    """

    password: str
    """
    Password for the initial user.
    """

    cpu_min: int
    """
    Minimum CPU count for the deployment.
    """

    cpu_max: int
    """
    Maximum CPU count for the deployment.
    """

    ram_per_cpu: int
    """
    RAM per CPU count for the deployment (in GB).
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    The Project ID on which the deployment will be created.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to apply to the deployment.
    """

    endpoints: Optional[list[EndpointSpec]] = field(default_factory=list)
    """
    Endpoints to associate with the deployment.
    """


@dataclass
class CreateEndpointRequest:
    deployment_id: str
    """
    UUID of the deployment.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    endpoint: Optional[EndpointSpec] = None
    """
    Endpoint specification.
    """


@dataclass
class CreateUserRequest:
    deployment_id: str
    """
    UUID of the deployment.
    """

    name: str
    """
    Name of the user.
    """

    password: str
    """
    Password for the user.
    """

    is_admin: bool
    """
    Indicates if the user is an administrator.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteDatabaseRequest:
    deployment_id: str
    """
    UUID of the deployment.
    """

    name: str
    """
    Name of the database to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteDeploymentRequest:
    deployment_id: str
    """
    UUID of the deployment to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteEndpointRequest:
    endpoint_id: str
    """
    UUID of the Endpoint to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteUserRequest:
    deployment_id: str
    """
    UUID of the deployment.
    """

    name: str
    """
    Name of the user to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetDeploymentCertificateRequest:
    deployment_id: str
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetDeploymentRequest:
    deployment_id: str
    """
    UUID of the deployment.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListDatabasesRequest:
    deployment_id: str
    """
    UUID of the deployment.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the database to filter by.
    """

    order_by: Optional[ListDatabasesRequestOrderBy] = (
        ListDatabasesRequestOrderBy.NAME_ASC
    )
    """
    Criteria to use when ordering database listings.
    """

    page: Optional[int] = 0
    page_size: Optional[int] = 0


@dataclass
class ListDatabasesResponse:
    databases: list[Database]
    """
    List of databases associated with the deployment.
    """

    total_count: int
    """
    Total count of databases associated with the deployment.
    """


@dataclass
class ListDeploymentsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List deployments with a given tag.
    """

    name: Optional[str] = None
    """
    Lists deployments that match a name pattern.
    """

    order_by: Optional[ListDeploymentsRequestOrderBy] = (
        ListDeploymentsRequestOrderBy.CREATED_AT_DESC
    )
    """
    Criteria to use when ordering deployment listings.
    """

    organization_id: Optional[str] = None
    """
    Organization ID the deployment belongs to.
    """

    project_id: Optional[str] = None
    """
    Project ID the deployment belongs to.
    """

    page: Optional[int] = 0
    page_size: Optional[int] = 0


@dataclass
class ListDeploymentsResponse:
    deployments: list[Deployment]
    """
    List of all deployments available in an Organization or Project.
    """

    total_count: int
    """
    Total count of deployments available in an Organization or Project.
    """


@dataclass
class ListPresetsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    page_size: Optional[int] = 0


@dataclass
class ListPresetsResponse:
    presets: list[Preset]
    """
    List of available presets.
    """

    total_count: int
    """
    Total count of presets available.
    """


@dataclass
class ListUsersRequest:
    deployment_id: str
    """
    UUID of the deployment.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the user to filter by.
    """

    order_by: Optional[ListUsersRequestOrderBy] = ListUsersRequestOrderBy.NAME_ASC
    """
    Criteria to use when ordering user listings.
    """

    page: Optional[int] = 0
    page_size: Optional[int] = 0


@dataclass
class ListUsersResponse:
    users: list[User]
    """
    List of users associated with the deployment.
    """

    total_count: int
    """
    Total count of users associated with the deployment.
    """


@dataclass
class ListVersionsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    version: Optional[str] = None
    page: Optional[int] = 0
    page_size: Optional[int] = 0


@dataclass
class ListVersionsResponse:
    versions: list[Version]
    """
    Available deployment version.
    """

    total_count: int
    """
    Total count of deployment version available.
    """


@dataclass
class UpdateDeploymentRequest:
    deployment_id: str
    """
    UUID of the deployment to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the deployment.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of a deployment.
    """

    cpu_min: Optional[int] = 0
    """
    Minimum CPU count for the deployment.
    """

    cpu_max: Optional[int] = 0
    """
    Maximum CPU count for the deployment.
    """

    replica_count: Optional[int] = 0
    """
    Number of replicas for the deployment.
    """


@dataclass
class UpdateUserRequest:
    deployment_id: str
    """
    UUID of the deployment.
    """

    name: str
    """
    Name of the user.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    password: Optional[str] = None
    """
    New password for the user.
    """

    is_admin: Optional[bool] = False
    """
    Updates the user administrator permissions.
    """
