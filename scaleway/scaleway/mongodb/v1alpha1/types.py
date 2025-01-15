# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class InstanceStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    READY = "ready"
    PROVISIONING = "provisioning"
    CONFIGURING = "configuring"
    DELETING = "deleting"
    ERROR = "error"
    INITIALIZING = "initializing"
    LOCKED = "locked"
    SNAPSHOTTING = "snapshotting"

    def __str__(self) -> str:
        return str(self.value)


class ListInstancesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListSnapshotsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    EXPIRES_AT_ASC = "expires_at_asc"
    EXPIRES_AT_DESC = "expires_at_desc"

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


class SettingPropertyType(str, Enum, metaclass=StrEnumMeta):
    BOOLEAN = "boolean"
    INT = "int"
    STRING = "string"
    FLOAT = "float"

    def __str__(self) -> str:
        return str(self.value)


class SnapshotStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    CREATING = "creating"
    READY = "ready"
    RESTORING = "restoring"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"

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
    pass


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
    UUID of the endpoint.
    """

    ips: List[str]
    """
    List of IPv4 addresses of the endpoint.
    """

    dns_records: List[str]
    """
    List of DNS records of the endpoint.
    """

    port: int
    """
    TCP port of the endpoint.
    """

    private_network: Optional[EndpointPrivateNetworkDetails]

    public: Optional[EndpointPublicDetails]


@dataclass
class InstanceSetting:
    name: str
    """
    Name of the settings.
    """

    value: str
    """
    Value of the settings.
    """


@dataclass
class Volume:
    type_: VolumeType
    """
    Type of volume where data is stored.
    """

    size: int
    """
    Volume size.
    """


@dataclass
class NodeTypeVolumeType:
    type_: VolumeType
    """
    Volume Type.
    """

    description: str
    """
    The description of the volume.
    """

    min_size: int
    """
    Mimimum size required for the volume.
    """

    max_size: int
    """
    Maximum size required for the volume.
    """

    chunk_size: int
    """
    Minimum increment level for a Block Storage volume size.
    """


@dataclass
class SnapshotVolumeType:
    type_: VolumeType


@dataclass
class Setting:
    name: str
    """
    Setting name from the database engine.
    """

    default_value: str
    """
    Value set when not specified.
    """

    hot_configurable: bool
    """
    Setting can be applied without restarting.
    """

    description: str
    """
    Setting description.
    """

    property_type: SettingPropertyType
    """
    Setting type.
    """

    unit: Optional[str]
    """
    Setting base unit.
    """

    string_constraint: Optional[str]
    """
    Validation regex for string type settings.
    """

    int_min: Optional[int]
    """
    Minimum value for int types.
    """

    int_max: Optional[int]
    """
    Maximum value for int types.
    """

    float_min: Optional[float]
    """
    Minimum value for float types.
    """

    float_max: Optional[float]
    """
    Maximum value for float types.
    """


@dataclass
class EndpointSpec:
    public: Optional[EndpointSpecPublicDetails]

    private_network: Optional[EndpointSpecPrivateNetworkDetails]


@dataclass
class CreateInstanceRequestVolumeDetails:
    volume_size: int
    """
    Volume size.
    """

    volume_type: VolumeType
    """
    Type of volume where data is stored.
    """


@dataclass
class Instance:
    id: str
    """
    UUID of the Database Instance.
    """

    name: str
    """
    Name of the Database Instance.
    """

    project_id: str
    """
    Project ID the Database Instance belongs to.
    """

    status: InstanceStatus
    """
    Status of the Database Instance.
    """

    version: str
    """
    MongoDB® engine version of the Database Instance.
    """

    tags: List[str]
    """
    List of tags applied to the Database Instance.
    """

    settings: List[InstanceSetting]
    """
    Advanced settings of the Database Instance.
    """

    node_number: int
    """
    Number of node in the Database Instance.
    """

    node_type: str
    """
    Node type of the Database Instance.
    """

    endpoints: List[Endpoint]
    """
    List of Database Instance endpoints.
    """

    region: ScwRegion
    """
    Region the Database Instance is in.
    """

    volume: Optional[Volume]
    """
    Volumes of the Database Instance.
    """

    created_at: Optional[datetime]
    """
    Creation date (must follow the ISO 8601 format).
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
    Current specs of the offer.
    """

    vcpus: int
    """
    Number of virtual CPUs.
    """

    memory: int
    """
    Quantity of RAM.
    """

    available_volume_types: List[NodeTypeVolumeType]
    """
    Available storage options for the node type.
    """

    disabled: bool
    """
    The node type is currently disabled.
    """

    beta: bool
    """
    The node type is currently in beta.
    """

    instance_range: str
    """
    Instance range associated with the node type offer.
    """


@dataclass
class Snapshot:
    id: str
    """
    UUID of the snapshot.
    """

    instance_id: str
    """
    UUID of the Database Instance.
    """

    name: str
    """
    Name of the snapshot.
    """

    status: SnapshotStatus
    """
    Status of the snapshot.
    """

    size: int
    """
    Size of the snapshot.
    """

    instance_name: str
    """
    Name of the Database Instance of the snapshot.
    """

    node_type: str
    """
    Source node type.
    """

    region: ScwRegion
    """
    Region of the snapshot.
    """

    expires_at: Optional[datetime]
    """
    Expiration date (must follow the ISO 8601 format).
    """

    created_at: Optional[datetime]
    """
    Creation date (must follow the ISO 8601 format).
    """

    updated_at: Optional[datetime]
    """
    Updated date (must follow the ISO 8601 format).
    """

    volume_type: Optional[SnapshotVolumeType]
    """
    Type of volume where data is stored - sbs_5k or sbs_15k.
    """


@dataclass
class User:
    name: str
    """
    Name of the user (Length must be between 1 and 63 characters. First character must be an alphabet character (a-zA-Z). Only a-zA-Z0-9_$- characters are accepted).
    """


@dataclass
class Version:
    version: str
    """
    MongoDB® engine version.
    """

    available_settings: List[Setting]
    """
    Instance settings available to be updated.
    """

    end_of_life_at: Optional[datetime]
    """
    Date of End of Life.
    """


@dataclass
class RestoreSnapshotRequestVolumeDetails:
    volume_type: VolumeType
    """
    Type of volume where data is stored.
    """


@dataclass
class CreateEndpointRequest:
    instance_id: str
    """
    UUID of the Database Instance.
    """

    endpoint: EndpointSpec
    """
    EndpointSpec used to expose your Database Instance.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class CreateInstanceRequest:
    version: str
    """
    Version of the MongoDB® engine.
    """

    node_number: int
    """
    Number of node to use for the Database Instance.
    """

    node_type: str
    """
    Type of node to use for the Database Instance.
    """

    user_name: str
    """
    Username created when the Database Instance is created.
    """

    password: str
    """
    Password of the initial user.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    The Project ID on which the Database Instance will be created.
    """

    name: Optional[str]
    """
    Name of the Database Instance.
    """

    tags: Optional[List[str]]
    """
    Tags to apply to the Database Instance.
    """

    volume: Optional[CreateInstanceRequestVolumeDetails]
    """
    Instance volume information.
    """

    endpoints: Optional[List[EndpointSpec]]
    """
    One or multiple EndpointSpec used to expose your Database Instance.
    """


@dataclass
class CreateSnapshotRequest:
    instance_id: str
    """
    UUID of the Database Instance to snapshot.
    """

    name: str
    """
    Name of the snapshot.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    expires_at: Optional[datetime]
    """
    Expiration date of the snapshot (must follow the ISO 8601 format).
    """


@dataclass
class CreateUserRequest:
    instance_id: str
    """
    UUID of the Database Instance the user belongs to.
    """

    name: str
    """
    Name of the database user.
    """

    password: str
    """
    Password of the database user.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteEndpointRequest:
    endpoint_id: str
    """
    UUID of the Endpoint to delete.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteInstanceRequest:
    instance_id: str
    """
    UUID of the Database Instance to delete.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteSnapshotRequest:
    snapshot_id: str
    """
    UUID of the snapshot.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteUserRequest:
    instance_id: str
    """
    UUID of the Database Instance the user belongs to.
    """

    name: str
    """
    Name of the database user.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetInstanceCertificateRequest:
    instance_id: str
    """
    UUID of the Database Instance.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetInstanceRequest:
    instance_id: str
    """
    UUID of the Database Instance.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetSnapshotRequest:
    snapshot_id: str
    """
    UUID of the snapshot.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListInstancesRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    tags: Optional[List[str]]
    """
    List Database Instances that have a given tag.
    """

    name: Optional[str]
    """
    Lists Database Instances that match a name pattern.
    """

    order_by: Optional[ListInstancesRequestOrderBy]
    """
    Criteria to use when ordering Database Instance listings.
    """

    organization_id: Optional[str]
    """
    Organization ID of the Database Instance.
    """

    project_id: Optional[str]
    """
    Project ID.
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class ListInstancesResponse:
    instances: List[Instance]
    """
    List of all Database Instances available in an Organization or Project.
    """

    total_count: int
    """
    Total count of Database Instances available in an Organization or Project.
    """


@dataclass
class ListNodeTypesRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    include_disabled_types: Optional[bool]
    """
    Defines whether or not to include disabled types.
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class ListNodeTypesResponse:
    node_types: List[NodeType]
    """
    Types of the node.
    """

    total_count: int
    """
    Total count of node-types available.
    """


@dataclass
class ListSnapshotsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: Optional[str]
    """
    Instance ID the snapshots belongs to.
    """

    name: Optional[str]
    """
    Lists database snapshots that match a name pattern.
    """

    order_by: Optional[ListSnapshotsRequestOrderBy]
    """
    Criteria to use when ordering snapshot listings.
    """

    organization_id: Optional[str]
    """
    Organization ID the snapshots belongs to.
    """

    project_id: Optional[str]
    """
    Project ID to list the snapshots of.
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class ListSnapshotsResponse:
    snapshots: List[Snapshot]
    """
    List of all database snapshots available in an Organization or Project.
    """

    total_count: int
    """
    Total count of database snapshots available in a Organization or Project.
    """


@dataclass
class ListUsersRequest:
    instance_id: str
    """
    UUID of the Database Instance.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the user.
    """

    order_by: Optional[ListUsersRequestOrderBy]
    """
    Criteria to use when requesting user listing.
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class ListUsersResponse:
    users: List[User]
    """
    List of users in a Database Instance.
    """

    total_count: int
    """
    Total count of users present on a Database Instance.
    """


@dataclass
class ListVersionsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    version: Optional[str]

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class ListVersionsResponse:
    versions: List[Version]
    """
    Available MongoDB® engine version.
    """

    total_count: int
    """
    Total count of MongoDB® engine version available.
    """


@dataclass
class RestoreSnapshotRequest:
    snapshot_id: str
    """
    UUID of the snapshot.
    """

    instance_name: str
    """
    Name of the new Database Instance.
    """

    node_type: str
    """
    Node type to use for the new Database Instance.
    """

    node_number: int
    """
    Number of nodes to use for the new Database Instance.
    """

    volume: RestoreSnapshotRequestVolumeDetails
    """
    Instance volume information.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class UpdateInstanceRequest:
    instance_id: str
    """
    UUID of the Database Instance to update.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the Database Instance.
    """

    tags: Optional[List[str]]
    """
    Tags of a Database Instance.
    """


@dataclass
class UpdateSnapshotRequest:
    snapshot_id: str
    """
    UUID of the Snapshot.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the snapshot.
    """

    expires_at: Optional[datetime]
    """
    Expiration date of the snapshot (must follow the ISO 8601 format).
    """


@dataclass
class UpdateUserRequest:
    instance_id: str
    """
    UUID of the Database Instance the user belongs to.
    """

    name: str
    """
    Name of the database user.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    password: Optional[str]
    """
    Password of the database user.
    """


@dataclass
class UpgradeInstanceRequest:
    instance_id: str
    """
    UUID of the Database Instance you want to upgrade.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    volume_size: Optional[int]
