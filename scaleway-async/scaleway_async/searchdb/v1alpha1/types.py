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
    """
    Refers to an Endpoint.
    """

    id: str
    """
    Unique identifier of the Endpoint.
    """

    dns_record: str
    """
    DNS entry to access to the service. Now deprecated. Use the `url` field from `services` field instead.
    """

    services: list[EndpointService]
    """
    List of available services, their ports and URLs.
    """

    public: Optional[EndpointPublicDetails] = None

    private_network: Optional[EndpointPrivateNetworkDetails] = None


@dataclass
class Volume:
    """
    Volume.
    """

    type_: VolumeType
    """
    Define the type of the Volume.
    """

    size_bytes: int
    """
    Define the size of the Volume.
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
    """
    Refers to a Deployment.
    """

    id: str
    """
    Unique identifier of the Deployment.
    """

    name: str
    """
    Name of the Deployment.
    """

    organization_id: str
    """
    ID of the Organization containing the Deployment.
    """

    project_id: str
    """
    ID of the Project containing the Deployment.
    """

    status: DeploymentStatus
    """
    Status of the Deployment.
    """

    tags: list[str]
    """
    Tags of the Deployment.
    """

    node_amount: int
    """
    Number of nodes allocated per deployment.
    """

    node_type: str
    """
    Node type used in deployment.
    """

    endpoints: list[Endpoint]
    """
    Exposed endpoints.
    """

    version: str
    """
    Opensearch version of the Deployment.
    """

    region: ScwRegion
    """
    Region the Deployment is located.
    """

    volume: Optional[Volume] = None
    """
    Volume type and size.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the Deployment.
    """

    updated_at: Optional[datetime] = None
    """
    Date when last update was done to the Deployment.
    """


@dataclass
class NodeType:
    """
    Node type.
    """

    stock_status: NodeTypeStockStatus
    """
    Stock status of the node type.
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
    Instance range associated with the NodeType offer.
    """

    available_volume_types: list[NodeTypeVolumeType]
    """
    Available storage options for the Node Type.
    """


@dataclass
class User:
    username: str


@dataclass
class Version:
    """
    Opensearch Version.
    """

    version: str
    """
    Opensearch Version.
    """

    disabled: bool
    """
    Parameter that tell if the version is disabled.
    """

    beta: bool
    """
    Parameter that tell if the version is in beta.
    """

    end_of_life: Optional[datetime] = None
    """
    End of life date of the version.
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

    node_amount: int
    """
    Number of nodes.
    """

    node_type: str
    """
    Node type.
    """

    version: str
    """
    The Opensearch version to use.
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
    Volume.
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
    ID of the deployment for which to create an endpoint.
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
    Create a user in an deployment.
    """

    deployment_id: str
    """
    ID of the deployment in which to create the user.
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
    ID of the endpoint to delete.
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
    ID of the deployment in which to create the user.
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
class GetDeploymentCertificateAuthorityRequest:
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
    ID of the Organization containing the deployments.
    """

    project_id: Optional[str] = None
    """
    ID of the Project containing the deployments.
    """

    order_by: Optional[ListDeploymentsRequestOrderBy] = (
        ListDeploymentsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Define the order of the returned deployments.
    """

    page: Optional[int] = 0
    """
    The page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of deployments to return.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Filter by tag, only deployments with one or more matching tags will be returned.
    """

    name: Optional[str] = None
    """
    Deployment name to filter for.
    """

    version: Optional[str] = None
    """
    Engine version to filter for.
    """


@dataclass
class ListDeploymentsResponse:
    """
    Retrieve a list of deployments.
    """

    deployments: list[Deployment]
    """
    List of deployments available.
    """

    total_count: int
    """
    Total number of objects.
    """


@dataclass
class ListNodeTypesRequest:
    """
    Retrieve a list of available node types for a Cloud Essentials for OpenSearch cluster.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListNodeTypesRequestOrderBy] = (
        ListNodeTypesRequestOrderBy.NAME_ASC
    )
    """
    Sort order of nodes in the response (name, vcpus or memory).
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of node types to return.
    """


@dataclass
class ListNodeTypesResponse:
    """
    Returns a list of node types available for a Cloud Essentials for OpenSearch cluster.
    """

    node_types: list[NodeType]
    """
    Node types compatible with the cluster.
    """

    total_count: int
    """
    Number of available node types to return.
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
    Define the order of the returned version.
    """

    page: Optional[int] = 0
    """
    The page number to return, form the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Number of version to return.
    """

    version: Optional[str] = None
    """
    Filter by version.
    """


@dataclass
class ListVersionsResponse:
    """
    Retrieve a list of version.
    """

    versions: list[Version]
    """
    List of versions.
    """

    total_count: int
    """
    Number of versions in the list.
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


@dataclass
class UpdateUserRequest:
    """
    Update a user in an deployment.
    """

    deployment_id: str
    """
    ID of the deployment in which to create the user.
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
    UUID of the Deployment to upgrade.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    node_amount: Optional[int] = 0

    volume_size_bytes: Optional[int] = 0
