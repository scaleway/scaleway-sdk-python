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


class UserRoleRole(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ROLE = "unknown_role"
    READ = "read"
    READ_WRITE = "read_write"
    DB_ADMIN = "db_admin"
    SYNC = "sync"

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

    ips: list[str]
    """
    List of IPv4 addresses of the endpoint.
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

    public: Optional[EndpointPublicDetails] = None


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
class InstanceSnapshotSchedule:
    frequency_hours: int
    retention_days: int
    enabled: bool
    next_update: Optional[datetime] = None
    last_run: Optional[datetime] = None


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
    Minimum size required for the volume.
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
class UserRole:
    role: UserRoleRole
    """
    Name of the preset role.
    """

    database: Optional[str] = None

    any_database: Optional[bool] = False


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

    unit: Optional[str] = None
    """
    Setting base unit.
    """

    string_constraint: Optional[str] = None
    """
    Validation regex for string type settings.
    """

    int_min: Optional[int] = 0
    """
    Minimum value for int types.
    """

    int_max: Optional[int] = 0
    """
    Maximum value for int types.
    """

    float_min: Optional[float] = 0.0
    """
    Minimum value for float types.
    """

    float_max: Optional[float] = 0.0
    """
    Maximum value for float types.
    """


@dataclass
class EndpointSpec:
    public: Optional[EndpointSpecPublicDetails] = None

    private_network: Optional[EndpointSpecPrivateNetworkDetails] = None


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

    tags: list[str]
    """
    List of tags applied to the Database Instance.
    """

    settings: list[InstanceSetting]
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

    endpoints: list[Endpoint]
    """
    List of Database Instance endpoints.
    """

    region: ScwRegion
    """
    Region the Database Instance is in.
    """

    volume: Optional[Volume] = None
    """
    Volumes of the Database Instance.
    """

    created_at: Optional[datetime] = None
    """
    Creation date (must follow the ISO 8601 format).
    """

    snapshot_schedule: Optional[InstanceSnapshotSchedule] = None
    """
    Snapshot schedule configuration of the Database Instance.
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

    available_volume_types: list[NodeTypeVolumeType]
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

    expires_at: Optional[datetime] = None
    """
    Expiration date (must follow the ISO 8601 format).
    """

    created_at: Optional[datetime] = None
    """
    Creation date (must follow the ISO 8601 format).
    """

    updated_at: Optional[datetime] = None
    """
    Updated date (must follow the ISO 8601 format).
    """

    volume_type: Optional[SnapshotVolumeType] = None
    """
    Type of volume where data is stored - sbs_5k or sbs_15k.
    """


@dataclass
class User:
    name: str
    """
    Name of the user (Length must be between 1 and 63 characters. First character must be an alphabet character (a-zA-Z). Only a-zA-Z0-9_$- characters are accepted).
    """

    roles: list[UserRole]
    """
    List of roles assigned to the user, along with the corresponding database where each role is granted.
    """


@dataclass
class Version:
    version: str
    """
    MongoDB® engine version.
    """

    available_settings: list[Setting]
    """
    Instance settings available to be updated.
    """

    end_of_life_at: Optional[datetime] = None
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

    region: Optional[ScwRegion] = None
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

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    The Project ID on which the Database Instance will be created.
    """

    name: Optional[str] = None
    """
    Name of the Database Instance.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to apply to the Database Instance.
    """

    volume: Optional[CreateInstanceRequestVolumeDetails] = None
    """
    Instance volume information.
    """

    endpoints: Optional[list[EndpointSpec]] = field(default_factory=list)
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

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    expires_at: Optional[datetime] = None
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
class DeleteInstanceRequest:
    instance_id: str
    """
    UUID of the Database Instance to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteSnapshotRequest:
    snapshot_id: str
    """
    UUID of the snapshot.
    """

    region: Optional[ScwRegion] = None
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

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetInstanceCertificateRequest:
    instance_id: str
    """
    UUID of the Database Instance.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetInstanceRequest:
    instance_id: str
    """
    UUID of the Database Instance.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetSnapshotRequest:
    snapshot_id: str
    """
    UUID of the snapshot.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListInstancesRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List Database Instances that have a given tag.
    """

    name: Optional[str] = None
    """
    Lists Database Instances that match a name pattern.
    """

    order_by: Optional[ListInstancesRequestOrderBy] = (
        ListInstancesRequestOrderBy.CREATED_AT_ASC
    )
    """
    Criteria to use when ordering Database Instance listings.
    """

    organization_id: Optional[str] = None
    """
    Organization ID of the Database Instance.
    """

    project_id: Optional[str] = None
    """
    Project ID.
    """

    page: Optional[int] = 0
    page_size: Optional[int] = 0


@dataclass
class ListInstancesResponse:
    instances: list[Instance]
    """
    List of all Database Instances available in an Organization or Project.
    """

    total_count: int
    """
    Total count of Database Instances available in an Organization or Project.
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
    Total count of node-types available.
    """


@dataclass
class ListSnapshotsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: Optional[str] = None
    """
    Instance ID the snapshots belongs to.
    """

    name: Optional[str] = None
    """
    Lists database snapshots that match a name pattern.
    """

    order_by: Optional[ListSnapshotsRequestOrderBy] = (
        ListSnapshotsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Criteria to use when ordering snapshot listings.
    """

    organization_id: Optional[str] = None
    """
    Organization ID the snapshots belongs to.
    """

    project_id: Optional[str] = None
    """
    Project ID to list the snapshots of.
    """

    page: Optional[int] = 0
    page_size: Optional[int] = 0


@dataclass
class ListSnapshotsResponse:
    snapshots: list[Snapshot]
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

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the user.
    """

    order_by: Optional[ListUsersRequestOrderBy] = ListUsersRequestOrderBy.NAME_ASC
    """
    Criteria to use when requesting user listing.
    """

    page: Optional[int] = 0
    page_size: Optional[int] = 0


@dataclass
class ListUsersResponse:
    users: list[User]
    """
    List of users in a Database Instance.
    """

    total_count: int
    """
    Total count of users present on a Database Instance.
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

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class SetUserRoleRequest:
    instance_id: str
    """
    UUID of the Database Instance the user belongs to.
    """

    user_name: str
    """
    Name of the database user.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    roles: Optional[list[UserRole]] = field(default_factory=list)
    """
    List of roles assigned to the user, along with the corresponding database where each role is granted.
    """


@dataclass
class UpdateInstanceRequest:
    instance_id: str
    """
    UUID of the Database Instance to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the Database Instance.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of a Database Instance.
    """


@dataclass
class UpdateSnapshotRequest:
    snapshot_id: str
    """
    UUID of the Snapshot.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the snapshot.
    """

    expires_at: Optional[datetime] = None
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

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    password: Optional[str] = None
    """
    Password of the database user.
    """


@dataclass
class UpgradeInstanceRequest:
    instance_id: str
    """
    UUID of the Database Instance you want to upgrade.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    volume_size: Optional[int] = 0
