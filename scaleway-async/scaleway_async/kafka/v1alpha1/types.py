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


class ClusterStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    READY = "ready"
    CREATING = "creating"
    CONFIGURING = "configuring"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)


class ListClustersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListUsersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class NodeTypeStock(str, Enum, metaclass=StrEnumMeta):
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
    """
    Private Network details.
    """

    private_network_id: str
    """
    UUID of the Private Network.
    """


@dataclass
class EndpointPublicDetails:
    """
    Public Access details.
    """

    pass


@dataclass
class VersionAvailableSettingBooleanProperty:
    default_value: bool


@dataclass
class VersionAvailableSettingFloatProperty:
    min: float
    max: float
    default_value: float
    unit: Optional[str] = None


@dataclass
class VersionAvailableSettingIntegerProperty:
    min: int
    max: int
    default_value: int
    unit: Optional[str] = None


@dataclass
class VersionAvailableSettingStringProperty:
    default_value: str
    string_constraint: Optional[str] = None


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
class ClusterSetting:
    name: str
    """
    Name of the setting.
    """

    bool_value: Optional[bool] = False

    string_value: Optional[str] = None

    int_value: Optional[int] = 0

    float_value: Optional[float] = 0.0


@dataclass
class Endpoint:
    id: str
    """
    UUID of the endpoint.
    """

    dns_records: list[str]
    """
    List of DNS records of the endpoint.
    """

    port: int
    """
    TCP port of the endpoint.
    """

    private_network: Optional[EndpointPrivateNetworkDetails] = None

    public_network: Optional[EndpointPublicDetails] = None


@dataclass
class Volume:
    type_: VolumeType
    """
    Type of volume where data is stored.
    """

    size_bytes: int
    """
    Volume size.
    """


@dataclass
class NodeTypeVolumeType:
    type_: VolumeType
    """
    Volume type.
    """

    description: str
    """
    The description of the volume.
    """

    min_size_bytes: int
    """
    Minimum size required for the volume.
    """

    max_size_bytes: int
    """
    Maximum size required for the volume.
    """

    chunk_size_bytes: int
    """
    Minimum increment level for a Block Storage volume size.
    """


@dataclass
class VersionAvailableSetting:
    name: str
    """
    Kafka cluster setting name.
    """

    hot_configurable: bool
    """
    Defines whether this setting can be applied without needing a restart.
    """

    description: str
    """
    Setting description.
    """

    bool_property: Optional[VersionAvailableSettingBooleanProperty] = None

    string_property: Optional[VersionAvailableSettingStringProperty] = None

    int_property: Optional[VersionAvailableSettingIntegerProperty] = None

    float_property: Optional[VersionAvailableSettingFloatProperty] = None


@dataclass
class CreateClusterRequestVolumeSpec:
    size_bytes: int
    """
    Volume size.
    """

    type_: VolumeType
    """
    Type of volume where data is stored.
    """


@dataclass
class EndpointSpec:
    public_network: Optional[EndpointSpecPublicDetails] = None

    private_network: Optional[EndpointSpecPrivateNetworkDetails] = None


@dataclass
class Cluster:
    id: str
    """
    UUID of the Kafka cluster.
    """

    name: str
    """
    Name of the Kafka cluster.
    """

    project_id: str
    """
    Project ID the Kafka cluster belongs to.
    """

    organization_id: str
    """
    Organisation ID the Kafka cluster belongs to.
    """

    status: ClusterStatus
    """
    Status of the Kafka cluster.
    """

    version: str
    """
    Kafka version of the Kafka cluster.
    """

    tags: list[str]
    """
    List of tags applied to the Kafka cluster.
    """

    settings: list[ClusterSetting]
    """
    Advanced settings of the Kafka cluster.
    """

    node_amount: int
    """
    Number of nodes in Kafka cluster.
    """

    node_type: str
    """
    Node type of the Kafka cluster.
    """

    endpoints: list[Endpoint]
    """
    List of Kafka cluster endpoints.
    """

    region: ScwRegion
    """
    Region the Kafka cluster is in.
    """

    volume: Optional[Volume] = None
    """
    Volumes of the Kafka cluster.
    """

    created_at: Optional[datetime] = None
    """
    Creation date (must follow the ISO 8601 format).
    """

    updated_at: Optional[datetime] = None
    """
    Last update date (must follow the ISO 8601 format).
    """


@dataclass
class NodeType:
    name: str
    """
    Node type name identifier.
    """

    stock_status: NodeTypeStock
    """
    Current stock status for the node type.
    """

    description: str
    """
    Current specifications of the node type offer.
    """

    vcpus: int
    """
    Number of virtual CPUs of the node type.
    """

    memory_bytes: int
    """
    Quantity of RAM.
    """

    available_volume_types: list[NodeTypeVolumeType]
    """
    Available storage options for the node type.
    """

    disabled: bool
    """
    Defines whether the node type is currently disabled.
    """

    beta: bool
    """
    Defines whether the node type is currently in beta.
    """

    cluster_range: str
    """
    Cluster range associated with the node type offer.
    """


@dataclass
class User:
    username: str


@dataclass
class Version:
    version: str
    """
    Kafka version.
    """

    available_settings: list[VersionAvailableSetting]
    """
    Cluster configuration settings you are able to change for clusters running this version. Each item in `available_settings` describes one configurable cluster setting.
    """

    end_of_life_at: Optional[datetime] = None
    """
    Date of End of Life for the version.
    """


@dataclass
class CreateClusterRequest:
    version: str
    """
    Version of Kafka.
    """

    node_amount: int
    """
    Number of nodes to use for the Kafka cluster.
    """

    node_type: str
    """
    Type of node to use for the Kafka cluster.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    The ID of the Project in which the Kafka cluster will be created.
    """

    name: Optional[str] = None
    """
    Name of the Kafka cluster.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to apply to the Kafka cluster.
    """

    volume: Optional[CreateClusterRequestVolumeSpec] = None
    """
    Kafka volume information.
    """

    endpoints: Optional[list[EndpointSpec]] = field(default_factory=list)
    """
    One or multiple EndpointSpec used to expose your Kafka cluster.
    """

    user_name: Optional[str] = None
    """
    Username for the kafka user.
    """

    password: Optional[str] = None
    """
    Password for the kafka user.
    """


@dataclass
class CreateEndpointRequest:
    cluster_id: str
    """
    UUID of the Kafka Cluster.
    """

    endpoint: EndpointSpec
    """
    Endpoint object (`EndpointSpec`) used to expose your Kafka EndpointSpec.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteClusterRequest:
    cluster_id: str
    """
    UUID of the Kafka Cluster to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteEndpointRequest:
    endpoint_id: str
    """
    UUID of the endpoint to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetClusterCertificateAuthorityRequest:
    cluster_id: str
    """
    UUID of the Kafka Cluster.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetClusterRequest:
    cluster_id: str
    """
    UUID of the Kafka Cluster.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListClustersRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List Kafka cluster with a given tag.
    """

    name: Optional[str] = None
    """
    Lists Kafka clusters that match a name pattern.
    """

    order_by: Optional[ListClustersRequestOrderBy] = (
        ListClustersRequestOrderBy.CREATED_AT_ASC
    )
    """
    Criteria to use when ordering Kafka cluster listings.
    """

    organization_id: Optional[str] = None
    """
    Organization ID of the Kafka cluster.
    """

    project_id: Optional[str] = None
    """
    Project ID.
    """

    page: Optional[int] = 0
    page_size: Optional[int] = 0


@dataclass
class ListClustersResponse:
    clusters: list[Cluster]
    """
    List of all Kafka cluster available in an Organization or Project.
    """

    total_count: int
    """
    Total count of Kafka cluster available in an Organization or Project.
    """


@dataclass
class ListNodeTypesRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    include_disabled_types: Optional[bool] = False
    """
    Defines whether or not to include disabled types.
    """

    page: Optional[int] = 0
    page_size: Optional[int] = 0


@dataclass
class ListNodeTypesResponse:
    node_types: list[NodeType]
    """
    Types of the node.
    """

    total_count: int
    """
    Total count of node types available.
    """


@dataclass
class ListUsersRequest:
    cluster_id: str
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
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    version: Optional[str] = None
    """
    Kafka version to filter for.
    """

    page: Optional[int] = 0
    """
    The page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    The number of items to return.
    """


@dataclass
class ListVersionsResponse:
    versions: list[Version]
    """
    Available Kafka versions.
    """

    total_count: int
    """
    Total count of Kafka versions available.
    """


@dataclass
class RenewClusterCertificateAuthorityRequest:
    cluster_id: str
    """
    UUID of the Kafka Cluster.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class UpdateClusterRequest:
    cluster_id: str
    """
    UUID of the Kafka Clusters to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the Kafka Cluster.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of a Kafka Cluster.
    """


@dataclass
class UpdateUserRequest:
    """
    Update a user of a Kafka cluster.
    """

    cluster_id: str
    """
    ID of the cluster in which to update the user's password.
    """

    username: str
    """
    Username of the Kafka cluster user.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    password: Optional[str] = None
    """
    New password for the Kafka cluster user.
    """
