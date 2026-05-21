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
    INITIALIZING = "initializing"
    UPGRADING = "upgrading"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"
    LOCKING = "locking"
    UNLOCKING = "unlocking"

    def __str__(self) -> str:
        return str(self.value)


class ListDeploymentsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListNodeTypesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    VCPUS_ASC = "vcpus_asc"
    VCPUS_DESC = "vcpus_desc"
    MEMORY_ASC = "memory_asc"
    MEMORY_DESC = "memory_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListUsersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListVersionsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    VERSION_ASC = "version_asc"
    VERSION_DESC = "version_desc"

    def __str__(self) -> str:
        return str(self.value)


class NodeTypeStockStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STOCK = "unknown_stock"
    LOW_STOCK = "low_stock"
    OUT_OF_STOCK = "out_of_stock"
    AVAILABLE = "available"

    def __str__(self) -> str:
        return str(self.value)


class VolumeType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    SBS_5K = "sbs_5k"
    SBS_15K = "sbs_15k"

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
    name: str
    port: int
    url: str


@dataclass
class EndpointSpecPrivateNetworkDetails:
    private_network_id: str


@dataclass
class EndpointSpecPublicDetails:
    pass


@dataclass
class Endpoint:
    id: str
    """
    Unique identifier of the endpoint.
    """

    services: list[EndpointService]
    """
    List of available services, their ports and URLs.
    """

    dns_record: Optional[str] = None
    """
    DNS record for service access. Now deprecated. Use the `url` field from `services` field instead.
    """

    public: Optional[EndpointPublicDetails] = None

    private_network: Optional[EndpointPrivateNetworkDetails] = None


@dataclass
class Volume:
    type_: VolumeType
    """
    Type of the Volume.
    """

    size_bytes: int
    """
    Size of the Volume.
    """


@dataclass
class NodeTypeVolumeType:
    type_: VolumeType
    description: str
    min_size_bytes: int
    max_size_bytes: int
    chunk_size_bytes: int


@dataclass
class EndpointSpec:
    public: Optional[EndpointSpecPublicDetails] = None

    private_network: Optional[EndpointSpecPrivateNetworkDetails] = None


@dataclass
class Deployment:
    id: str
    """
    Unique identifier of the deployment.
    """

    name: str
    """
    Name of the deployment.
    """

    organization_id: str
    """
    ID of the Organization containing the deployment.
    """

    project_id: str
    """
    ID of the Project containing the deployment.
    """

    status: DeploymentStatus
    """
    Status of the deployment.
    """

    tags: list[str]
    """
    Tags of the deployment.
    """

    node_count: int
    """
    Number of nodes.
    """

    node_type: str
    """
    Node type used.
    """

    endpoints: list[Endpoint]
    """
    Exposed endpoints.
    """

    version: str
    """
    MessageQ version of the deployment.
    """

    region: ScwRegion
    """
    Region of the deployment.
    """

    volume: Optional[Volume] = None
    """
    Volume type and size.
    """

    created_at: Optional[datetime] = None
    """
    Date the deployment was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date the deployment was last updated.
    """


@dataclass
class NodeType:
    stock_status: NodeTypeStockStatus
    """
    Stock status for the node type.
    """

    name: str
    """
    Name of the node type.
    """

    description: str
    """
    Description of the node type.
    """

    vcpus: int
    """
    Number of vCPUs available.
    """

    memory_bytes: int
    """
    Amount of memory available.
    """

    disabled: bool
    """
    Defines whether the node type is disabled.
    """

    beta: bool
    """
    Defines whether the node type is in beta.
    """

    instance_range: str
    """
    Instance range associated with the node type offer.
    """

    available_volume_types: list[NodeTypeVolumeType]
    """
    Available storage options for the node type.
    """


@dataclass
class User:
    username: str


@dataclass
class Version:
    version: str
    """
    MessageQ version.
    """

    disabled: bool
    """
    Defines whether the version is disabled.
    """

    beta: bool
    """
    Defines whether the version is in beta.
    """

    end_of_life: Optional[datetime] = None
    """
    Date the version support ends.
    """


@dataclass
class CreateDeploymentRequest:
    """
    Request to create a new deployment.
    """

    name: str
    """
    Name of the deployment.
    """

    node_count: int
    """
    Number of nodes.
    """

    node_type: str
    """
    Node type to use.
    """

    version: str
    """
    The MessageQ version to use.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    Project ID in which to create the deployment.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags.
    """

    user_name: Optional[str] = None
    """
    Username for the deployment user.
    """

    password: Optional[str] = None
    """
    Password for the deployment user.
    """

    volume: Optional[Volume] = None
    """
    Volume for storing data.
    """

    endpoints: Optional[list[EndpointSpec]] = field(default_factory=list)
    """
    Endpoints to access the deployment.
    """


@dataclass
class CreateEndpointRequest:
    """
    Create an endpoint for a specific deployment.
    """

    deployment_id: str
    """
    ID of the deployment.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    endpoint_spec: Optional[EndpointSpec] = None
    """
    Specification of the endpoint you want to create.
    """


@dataclass
class CreateUserRequest:
    """
    Create a user for a deployment.
    """

    deployment_id: str
    """
    ID of the deployment.
    """

    username: str
    """
    Username of the deployment user.
    """

    password: str
    """
    Password of the deployment user.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteDeploymentRequest:
    """
    Delete a deployment specified by the ID.
    """

    deployment_id: str
    """
    ID of the deployment.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteEndpointRequest:
    """
    Delete an endpoint from a specific deployment.
    """

    endpoint_id: str
    """
    ID of the endpoint.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteUserRequest:
    """
    Delete a user from a deployment.
    """

    deployment_id: str
    """
    ID of the deployment.
    """

    username: str
    """
    Username of the deployment user.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DownloadDeploymentCertificateAuthorityRequest:
    deployment_id: str
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetDeploymentRequest:
    """
    Retrieve a deployment specified by the ID.
    """

    deployment_id: str
    """
    ID of the deployment.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListDeploymentsRequest:
    """
    Retrieve a list of deployments.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str] = None
    """
    Organization ID to filter for, only deployments from this Organization will be returned.
    """

    project_id: Optional[str] = None
    """
    Project ID to filter for, only deployments from this Project will be returned.
    """

    order_by: Optional[ListDeploymentsRequestOrderBy] = (
        ListDeploymentsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order for deployments in the response.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of deployments to return per page.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to filter for, only deployments with one or more matching tags will be returned.
    """

    name: Optional[str] = None
    """
    Deployment name to filter for, only deployments with this string within their name will be returned.
    """


@dataclass
class ListDeploymentsResponse:
    deployments: list[Deployment]
    """
    List of deployments.
    """

    total_count: int
    """
    Number of deployments in result set.
    """


@dataclass
class ListNodeTypesRequest:
    """
    Retrieve a list of available node types for a MessageQ deployment.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListNodeTypesRequestOrderBy] = (
        ListNodeTypesRequestOrderBy.NAME_ASC
    )
    """
    Sort order for versions in the response.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of node types to return per page.
    """


@dataclass
class ListNodeTypesResponse:
    node_types: list[NodeType]
    """
    List of node types compatible.
    """

    total_count: int
    """
    Number of node types in result set.
    """


@dataclass
class ListUsersRequest:
    deployment_id: str
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = None
    page_size: Optional[int] = None
    order_by: Optional[ListUsersRequestOrderBy] = None
    name: Optional[str] = None


@dataclass
class ListUsersResponse:
    users: list[User]
    total_count: int


@dataclass
class ListVersionsRequest:
    """
    Retrieve a list of available versions.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListVersionsRequestOrderBy] = (
        ListVersionsRequestOrderBy.VERSION_ASC
    )
    """
    Sort order for versions in the response.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of versions to return per page.
    """

    version: Optional[str] = None
    """
    Engine version to filter for, only versions with this version will be returned.
    """


@dataclass
class ListVersionsResponse:
    versions: list[Version]
    """
    List of versions.
    """

    total_count: int
    """
    Number of versions in result set.
    """


@dataclass
class UpdateDeploymentRequest:
    deployment_id: str
    """
    ID of the deployment.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    New name for the deployment.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to update.
    """


@dataclass
class UpdateUserRequest:
    """
    Update a deployment user.
    """

    deployment_id: str
    """
    ID of the deployment.
    """

    username: str
    """
    Username of the deployment user.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    password: Optional[str] = None
    """
    Password of the deployment user.
    """


@dataclass
class UpgradeDeploymentRequest:
    deployment_id: str
    """
    ID of the deployment.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    node_count: Optional[int] = 0

    volume_size_bytes: Optional[int] = 0
