# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Region,
    TimeSeries,
    Zone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class ACLRuleAction(str, Enum, metaclass=StrEnumMeta):
    ALLOW = "allow"
    DENY = "deny"

    def __str__(self) -> str:
        return str(self.value)


class ACLRuleDirection(str, Enum, metaclass=StrEnumMeta):
    INBOUND = "inbound"
    OUTBOUND = "outbound"

    def __str__(self) -> str:
        return str(self.value)


class ACLRuleProtocol(str, Enum, metaclass=StrEnumMeta):
    TCP = "tcp"
    UDP = "udp"
    ICMP = "icmp"

    def __str__(self) -> str:
        return str(self.value)


class DatabaseBackupStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    CREATING = "creating"
    READY = "ready"
    RESTORING = "restoring"
    DELETING = "deleting"
    ERROR = "error"
    EXPORTING = "exporting"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class EngineSettingPropertyType(str, Enum, metaclass=StrEnumMeta):
    BOOLEAN = "boolean"
    INT = "int"
    STRING = "string"
    FLOAT = "float"

    def __str__(self) -> str:
        return str(self.value)


class InstanceLogStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    READY = "ready"
    CREATING = "creating"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class InstanceStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    READY = "ready"
    PROVISIONING = "provisioning"
    CONFIGURING = "configuring"
    DELETING = "deleting"
    ERROR = "error"
    AUTOHEALING = "autohealing"
    LOCKED = "locked"
    INITIALIZING = "initializing"
    DISK_FULL = "disk_full"
    BACKUPING = "backuping"
    SNAPSHOTTING = "snapshotting"
    RESTARTING = "restarting"

    def __str__(self) -> str:
        return str(self.value)


class ListDatabaseBackupsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListDatabasesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    SIZE_ASC = "size_asc"
    SIZE_DESC = "size_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListInstanceLogsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListInstancesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    REGION = "region"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPrivilegesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    USER_NAME_ASC = "user_name_asc"
    USER_NAME_DESC = "user_name_desc"
    DATABASE_NAME_ASC = "database_name_asc"
    DATABASE_NAME_DESC = "database_name_desc"

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
    IS_ADMIN_ASC = "is_admin_asc"
    IS_ADMIN_DESC = "is_admin_desc"

    def __str__(self) -> str:
        return str(self.value)


class MaintenanceStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    PENDING = "pending"
    DONE = "done"
    CANCELED = "canceled"

    def __str__(self) -> str:
        return str(self.value)


class NodeTypeGeneration(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_GENERATION = "unknown_generation"
    GENERATION_V1 = "generation_v1"
    GENERATION_V2 = "generation_v2"

    def __str__(self) -> str:
        return str(self.value)


class NodeTypeStock(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    LOW_STOCK = "low_stock"
    OUT_OF_STOCK = "out_of_stock"
    AVAILABLE = "available"

    def __str__(self) -> str:
        return str(self.value)


class Permission(str, Enum, metaclass=StrEnumMeta):
    READONLY = "readonly"
    READWRITE = "readwrite"
    ALL = "all"
    CUSTOM = "custom"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)


class ReadReplicaStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    PROVISIONING = "provisioning"
    INITIALIZING = "initializing"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"
    CONFIGURING = "configuring"
    PROMOTING = "promoting"

    def __str__(self) -> str:
        return str(self.value)


class SnapshotStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    CREATING = "creating"
    READY = "ready"
    RESTORING = "restoring"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class VolumeType(str, Enum, metaclass=StrEnumMeta):
    LSSD = "lssd"
    BSSD = "bssd"
    SBS = "sbs"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class EndpointDirectAccessDetails:
    pass


@dataclass
class EndpointLoadBalancerDetails:
    pass


@dataclass
class EndpointPrivateNetworkDetails:
    zone: Zone
    """
    Private network zone.
    """

    service_ip: str
    """
    CIDR notation of the endpoint IPv4 address.
    """

    private_network_id: str
    """
    UUID of the private network.
    """


@dataclass
class EndpointSpecPrivateNetworkIpamConfig:
    pass


@dataclass
class ReadReplicaEndpointSpecPrivateNetworkIpamConfig:
    pass


@dataclass
class EngineSetting:
    property_type: EngineSettingPropertyType
    """
    Setting type.
    """

    description: str
    """
    Setting description.
    """

    hot_configurable: bool
    """
    Setting can be applied without restarting.
    """

    default_value: str
    """
    Value set when not specified.
    """

    name: str
    """
    Setting name from the database engine.
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
class Endpoint:
    port: int
    """
    TCP port of the endpoint.
    """

    id: str
    """
    UUID of the endpoint.
    """

    name: Optional[str]
    """
    Name of the endpoint.
    """

    ip: Optional[str]

    hostname: Optional[str]

    private_network: Optional[EndpointPrivateNetworkDetails]

    load_balancer: Optional[EndpointLoadBalancerDetails]

    direct_access: Optional[EndpointDirectAccessDetails]


@dataclass
class EndpointSpecLoadBalancer:
    pass


@dataclass
class EndpointSpecPrivateNetwork:
    private_network_id: str
    """
    UUID of the Private Network to be connected to the Database Instance.
    """

    service_ip: Optional[str]

    ipam_config: Optional[EndpointSpecPrivateNetworkIpamConfig]


@dataclass
class ReadReplicaEndpointSpecDirectAccess:
    pass


@dataclass
class ReadReplicaEndpointSpecPrivateNetwork:
    private_network_id: str
    """
    UUID of the Private Network to be connected to the Read Replica.
    """

    service_ip: Optional[str]

    ipam_config: Optional[ReadReplicaEndpointSpecPrivateNetworkIpamConfig]


@dataclass
class EngineVersion:
    available_init_settings: List[EngineSetting]
    """
    Engine settings available to be set at database initialization.
    """

    beta: bool
    """
    Beta status of engine version.
    """

    disabled: bool
    """
    Disabled versions cannot be created.
    """

    available_settings: List[EngineSetting]
    """
    Engine settings available to be set.
    """

    name: str
    """
    Database engine name.
    """

    version: str
    """
    Database engine version.
    """

    end_of_life: Optional[datetime]
    """
    End of life date.
    """


@dataclass
class BackupSchedule:
    disabled: bool
    """
    Defines whether the backup schedule feature is disabled.
    """

    retention: int
    """
    Default retention period of backups (in days).
    """

    frequency: int
    """
    Frequency of the backup schedule (in hours).
    """

    next_run_at: Optional[datetime]
    """
    Next run of the backup schedule (accurate to 10 minutes).
    """


@dataclass
class InstanceSetting:
    value: str

    name: str


@dataclass
class LogsPolicy:
    max_age_retention: Optional[int]
    """
    Max age (in days) of remote logs to keep on the Database Instance.
    """

    total_disk_retention: Optional[int]
    """
    Max disk size of remote logs to keep on the Database Instance.
    """


@dataclass
class Maintenance:
    status: MaintenanceStatus
    """
    Status of the maintenance.
    """

    reason: str
    """
    Maintenance information message.
    """

    starts_at: Optional[datetime]
    """
    Start date of the maintenance window.
    """

    stops_at: Optional[datetime]
    """
    End date of the maintenance window.
    """

    closed_at: Optional[datetime]
    """
    Closed maintenance date.
    """


@dataclass
class ReadReplica:
    same_zone: bool
    """
    Whether the replica is in the same availability zone as the main instance nodes or not.
    """

    region: Region
    """
    Region the Read Replica is in.
    """

    status: ReadReplicaStatus
    """
    Read replica status.
    """

    endpoints: List[Endpoint]
    """
    Display Read Replica connection information.
    """

    id: str
    """
    UUID of the Read Replica.
    """


@dataclass
class UpgradableVersion:
    minor_version: str

    version: str

    name: str

    id: str


@dataclass
class Volume:
    size: int

    type_: VolumeType


@dataclass
class NodeTypeVolumeConstraintSizes:
    max_size: int
    """
    [deprecated] Maximum size required for the Volume.
    """

    min_size: int
    """
    [deprecated] Mimimum size required for the Volume.
    """


@dataclass
class NodeTypeVolumeType:
    chunk_size: int
    """
    Minimum increment level for a Block Storage volume size.
    """

    max_size: int
    """
    Maximum size required for the Volume.
    """

    min_size: int
    """
    Mimimum size required for the Volume.
    """

    description: str
    """
    The description of the Volume.
    """

    type_: VolumeType
    """
    Volume Type.
    """


@dataclass
class ACLRuleRequest:
    description: str

    ip: str


@dataclass
class ACLRule:
    description: str

    action: ACLRuleAction

    direction: ACLRuleDirection

    protocol: ACLRuleProtocol

    ip: str

    port: Optional[int]


@dataclass
class EndpointSpec:
    load_balancer: Optional[EndpointSpecLoadBalancer]

    private_network: Optional[EndpointSpecPrivateNetwork]


@dataclass
class ReadReplicaEndpointSpec:
    direct_access: Optional[ReadReplicaEndpointSpecDirectAccess]

    private_network: Optional[ReadReplicaEndpointSpecPrivateNetwork]


@dataclass
class DatabaseBackup:
    region: Region
    """
    Region of the database backup.
    """

    same_region: bool
    """
    Store logical backups in the same region as the source Database Instance.
    """

    status: DatabaseBackupStatus
    """
    Status of the backup.
    """

    id: str
    """
    UUID of the database backup.
    """

    database_name: str
    """
    Name of backed up database.
    """

    instance_id: str
    """
    UUID of the Database Instance.
    """

    instance_name: str
    """
    Name of the Database Instance of the backup.
    """

    name: str
    """
    Name of the backup.
    """

    updated_at: Optional[datetime]
    """
    Updated date (must follow the ISO 8601 format).
    """

    created_at: Optional[datetime]
    """
    Creation date (must follow the ISO 8601 format).
    """

    download_url: Optional[str]
    """
    URL you can download the backup from.
    """

    download_url_expires_at: Optional[datetime]
    """
    Expiration date of the download link.
    """

    expires_at: Optional[datetime]
    """
    Expiration date (must follow the ISO 8601 format).
    """

    size: Optional[int]
    """
    Size of the database backup.
    """


@dataclass
class DatabaseEngine:
    region: Region
    """
    Region of this Database Instance.
    """

    versions: List[EngineVersion]
    """
    Available versions.
    """

    logo_url: str
    """
    Engine logo URL.
    """

    name: str
    """
    Engine name.
    """


@dataclass
class Database:
    size: int
    """
    Size of the database.
    """

    managed: bool
    """
    Defines whether the database is managed or not.
    """

    owner: str
    """
    Name of the database owner.
    """

    name: str
    """
    Name of the database.
    """


@dataclass
class ListInstanceLogsDetailsResponseInstanceLogDetail:
    size: int

    log_name: str


@dataclass
class InstanceLog:
    region: Region
    """
    Region the Database Instance is in.
    """

    node_name: str
    """
    Name of the underlying node.
    """

    status: InstanceLogStatus
    """
    Status of the logs in a Database Instance.
    """

    id: str
    """
    UUID of the Database Instance log.
    """

    download_url: Optional[str]
    """
    Presigned S3 URL to download your log file.
    """

    expires_at: Optional[datetime]
    """
    Expiration date (must follow the ISO 8601 format).
    """

    created_at: Optional[datetime]
    """
    Creation date (must follow the ISO 8601 format).
    """


@dataclass
class Instance:
    tags: List[str]
    """
    List of tags applied to the Database Instance.
    """

    upgradable_version: List[UpgradableVersion]
    """
    Available database engine versions for upgrade.
    """

    project_id: str
    """
    Project ID the Database Instance belongs to.
    """

    volume: Volume
    """
    Volumes of the Database Instance.
    """

    logs_policy: LogsPolicy
    """
    Logs policy of the Database Instance.
    """

    backup_schedule: BackupSchedule
    """
    Backup schedule of the Database Instance.
    """

    read_replicas: List[ReadReplica]
    """
    Read Replicas of the Database Instance.
    """

    name: str
    """
    Name of the Database Instance.
    """

    endpoints: List[Endpoint]
    """
    List of Database Instance endpoints.
    """

    backup_same_region: bool
    """
    Store logical backups in the same region as the Database Instance.
    """

    node_type: str
    """
    Node type of the Database Instance.
    """

    settings: List[InstanceSetting]
    """
    Advanced settings of the Database Instance.
    """

    is_ha_cluster: bool
    """
    Defines whether or not High-Availability is enabled.
    """

    region: Region
    """
    Region the Database Instance is in.
    """

    maintenances: List[Maintenance]
    """
    List of Database Instance maintenance events.
    """

    id: str
    """
    UUID of the Database Instance.
    """

    status: InstanceStatus
    """
    Status of the Database Instance.
    """

    init_settings: List[InstanceSetting]
    """
    List of engine settings to be set at database initialization.
    """

    engine: str
    """
    Database engine of the database (PostgreSQL, MySQL, ...).
    """

    organization_id: str
    """
    Organization ID the Database Instance belongs to.
    """

    endpoint: Optional[Endpoint]
    """
    Endpoint of the Database Instance.
    """

    created_at: Optional[datetime]
    """
    Creation date (must follow the ISO 8601 format).
    """


@dataclass
class NodeType:
    is_ha_required: bool
    """
    The Node Type can be used only with high availability option.
    """

    available_volume_types: List[NodeTypeVolumeType]
    """
    Available storage options for the Node Type.
    """

    beta: bool
    """
    The Node Type is currently in beta.
    """

    disabled: bool
    """
    The Node Type is currently disabled.
    """

    instance_range: str
    """
    Instance range associated with the NodeType offer.
    """

    region: Region
    """
    Region the Node Type is in.
    """

    memory: int
    """
    Quantity of RAM.
    """

    name: str
    """
    Node Type name identifier.
    """

    description: str
    """
    Current specs of the offer.
    """

    stock_status: NodeTypeStock
    """
    Current stock status for the Node Type.
    """

    generation: NodeTypeGeneration
    """
    Generation associated with the NodeType offer.
    """

    vcpus: int
    """
    Number of virtual CPUs.
    """

    is_bssd_compatible: Optional[bool]
    """
    The Node Type is compliant with Block Storage.
    """

    volume_constraint: Optional[NodeTypeVolumeConstraintSizes]
    """
    [deprecated] Node Type volume constraints.
    """


@dataclass
class Privilege:
    user_name: str
    """
    Name of the user.
    """

    database_name: str
    """
    Name of the database.
    """

    permission: Permission
    """
    Permission (Read, Read/Write, All, Custom).
    """


@dataclass
class Snapshot:
    region: Region
    """
    Region of this snapshot.
    """

    node_type: str
    """
    Source node type.
    """

    instance_name: str
    """
    Name of the Database Instance of the snapshot.
    """

    status: SnapshotStatus
    """
    Status of the snapshot.
    """

    name: str
    """
    Name of the snapshot.
    """

    instance_id: str
    """
    UUID of the Database Instance.
    """

    id: str
    """
    UUID of the snapshot.
    """

    size: Optional[int]
    """
    Size of the snapshot.
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


@dataclass
class User:
    is_admin: bool
    """
    Defines whether or not a user got administrative privileges on the Database Instance.
    """

    name: str
    """
    Name of the user (Length must be between 1 and 63 characters for PostgreSQL and between 1 and 32 characters for MySQL. First character must be an alphabet character (a-zA-Z). Your username cannot start with '_rdb' or in PostgreSQL, 'pg_'. Only a-zA-Z0-9_$- characters are accepted).
    """


@dataclass
class AddInstanceACLRulesRequest:
    instance_id: str
    """
    UUID of the Database Instance you want to add ACL rules to.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    rules: Optional[List[ACLRuleRequest]]
    """
    ACL rules to add to the Database Instance.
    """


@dataclass
class AddInstanceACLRulesResponse:
    rules: List[ACLRule]
    """
    ACL Rules enabled for the Database Instance.
    """


@dataclass
class AddInstanceSettingsRequest:
    instance_id: str
    """
    UUID of the Database Instance you want to add settings to.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    settings: Optional[List[InstanceSetting]]
    """
    Settings to add to the Database Instance.
    """


@dataclass
class AddInstanceSettingsResponse:
    settings: List[InstanceSetting]
    """
    Settings available on the Database Instance.
    """


@dataclass
class CloneInstanceRequest:
    name: str
    """
    Name of the Database Instance clone.
    """

    instance_id: str
    """
    UUID of the Database Instance you want to clone.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    node_type: Optional[str]
    """
    Node type of the clone.
    """


@dataclass
class CreateDatabaseBackupRequest:
    database_name: str
    """
    Name of the database you want to back up.
    """

    instance_id: str
    """
    UUID of the Database Instance.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the backup.
    """

    expires_at: Optional[datetime]
    """
    Expiration date (must follow the ISO 8601 format).
    """


@dataclass
class CreateDatabaseRequest:
    name: str
    """
    Name of the database.
    """

    instance_id: str
    """
    UUID of the Database Instance where to create the database.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class CreateEndpointRequest:
    instance_id: str
    """
    UUID of the Database Instance you to which you want to add an endpoint.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    endpoint_spec: Optional[EndpointSpec]
    """
    Specification of the endpoint you want to create.
    """


@dataclass
class CreateInstanceFromSnapshotRequest:
    instance_name: str
    """
    Name of the Database Instance created with the snapshot.
    """

    snapshot_id: str
    """
    Block snapshot of the Database Instance.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    is_ha_cluster: Optional[bool]
    """
    Defines whether or not High-Availability is enabled on the new Database Instance.
    """

    node_type: Optional[str]
    """
    The node type used to restore the snapshot.
    """


@dataclass
class CreateInstanceRequest:
    volume_size: int
    """
    Volume size when volume_type is not lssd.
    """

    node_type: str
    """
    Type of node to use for the Database Instance.
    """

    password: str
    """
    Password of the user.
    """

    user_name: str
    """
    Username created when the Database Instance is created.
    """

    engine: str
    """
    Database engine of the Database Instance (PostgreSQL, MySQL, ...).
    """

    backup_same_region: bool
    """
    Defines whether to or not to store logical backups in the same region as the Database Instance.
    """

    disable_backup: bool
    """
    Defines whether or not backups are disabled.
    """

    is_ha_cluster: bool
    """
    Defines whether or not High-Availability is enabled.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    tags: Optional[List[str]]
    """
    Tags to apply to the Database Instance.
    """

    init_settings: Optional[List[InstanceSetting]]
    """
    List of engine settings to be set upon Database Instance initialization.
    """

    volume_type: Optional[VolumeType]
    """
    Type of volume where data is stored (lssd, bssd, ...).
    """

    init_endpoints: Optional[List[EndpointSpec]]
    """
    One or multiple EndpointSpec used to expose your Database Instance. A load_balancer public endpoint is systematically created.
    """

    name: Optional[str]
    """
    Name of the Database Instance.
    """

    organization_id: Optional[str]

    project_id: Optional[str]


@dataclass
class CreateReadReplicaEndpointRequest:
    read_replica_id: str
    """
    UUID of the Read Replica.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    endpoint_spec: Optional[List[ReadReplicaEndpointSpec]]
    """
    Specification of the endpoint you want to create.
    """


@dataclass
class CreateReadReplicaRequest:
    instance_id: str
    """
    UUID of the Database Instance you want to create a Read Replica from.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    endpoint_spec: Optional[List[ReadReplicaEndpointSpec]]
    """
    Specification of the endpoint you want to create.
    """

    same_zone: Optional[bool]
    """
    Defines whether to create the replica in the same availability zone as the main instance nodes or not.
    """


@dataclass
class CreateSnapshotRequest:
    instance_id: str
    """
    UUID of the Database Instance.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the snapshot.
    """

    expires_at: Optional[datetime]
    """
    Expiration date (must follow the ISO 8601 format).
    """


@dataclass
class CreateUserRequest:
    is_admin: bool
    """
    Defines whether the user will have administrative privileges.
    """

    password: str
    """
    Password of the user you want to create.
    """

    name: str
    """
    Name of the user you want to create.
    """

    instance_id: str
    """
    UUID of the Database Instance in which you want to create a user.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteDatabaseBackupRequest:
    database_backup_id: str
    """
    UUID of the database backup to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteDatabaseRequest:
    name: str
    """
    Name of the database to delete.
    """

    instance_id: str
    """
    UUID of the Database Instance where to delete the database.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteEndpointRequest:
    endpoint_id: str
    """
    This endpoint can also be used to delete a Read Replica endpoint.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteInstanceACLRulesRequest:
    instance_id: str
    """
    UUID of the Database Instance you want to delete an ACL rule from.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    acl_rule_ips: Optional[List[str]]
    """
    IP addresses defined in the ACL rules of the Database Instance.
    """


@dataclass
class DeleteInstanceACLRulesResponse:
    rules: List[ACLRule]
    """
    IP addresses defined in the ACL rules of the Database Instance.
    """


@dataclass
class DeleteInstanceRequest:
    instance_id: str
    """
    UUID of the Database Instance to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteInstanceSettingsRequest:
    instance_id: str
    """
    UUID of the Database Instance to delete settings from.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    setting_names: Optional[List[str]]
    """
    Settings names to delete.
    """


@dataclass
class DeleteInstanceSettingsResponse:
    settings: List[InstanceSetting]
    """
    Settings names to delete from the Database Instance.
    """


@dataclass
class DeleteReadReplicaRequest:
    read_replica_id: str
    """
    UUID of the Read Replica.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteSnapshotRequest:
    snapshot_id: str
    """
    UUID of the snapshot to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteUserRequest:
    name: str
    """
    Name of the user.
    """

    instance_id: str
    """
    UUID of the Database Instance to delete the user from.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ExportDatabaseBackupRequest:
    database_backup_id: str
    """
    UUID of the database backup you want to export.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetDatabaseBackupRequest:
    database_backup_id: str
    """
    UUID of the database backup.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetEndpointRequest:
    endpoint_id: str
    """
    UUID of the endpoint you want to get.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetInstanceCertificateRequest:
    instance_id: str
    """
    UUID of the Database Instance.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetInstanceLogRequest:
    instance_log_id: str
    """
    UUID of the instance_log you want.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetInstanceMetricsRequest:
    instance_id: str
    """
    UUID of the Database Instance.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    start_date: Optional[datetime]
    """
    Start date to gather metrics from.
    """

    end_date: Optional[datetime]
    """
    End date to gather metrics from.
    """

    metric_name: Optional[str]
    """
    Name of the metric to gather.
    """


@dataclass
class GetInstanceRequest:
    instance_id: str
    """
    UUID of the Database Instance.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetReadReplicaRequest:
    read_replica_id: str
    """
    UUID of the Read Replica.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetSnapshotRequest:
    snapshot_id: str
    """
    UUID of the snapshot.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class InstanceMetrics:
    timeseries: List[TimeSeries]
    """
    Time series of metrics of a Database Instance.
    """


@dataclass
class ListDatabaseBackupsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the database backups.
    """

    order_by: Optional[ListDatabaseBackupsRequestOrderBy]
    """
    Criteria to use when ordering database backups listing.
    """

    instance_id: Optional[str]
    """
    UUID of the Database Instance.
    """

    organization_id: Optional[str]
    """
    Organization ID of the Organization the database backups belong to.
    """

    project_id: Optional[str]
    """
    Project ID of the Project the database backups belong to.
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class ListDatabaseBackupsResponse:
    total_count: int
    """
    Total count of database backups available.
    """

    database_backups: List[DatabaseBackup]
    """
    List of database backups.
    """


@dataclass
class ListDatabaseEnginesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the database engine.
    """

    version: Optional[str]
    """
    Version of the database engine.
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class ListDatabaseEnginesResponse:
    total_count: int
    """
    Total count of database engines available.
    """

    engines: List[DatabaseEngine]
    """
    List of the available database engines.
    """


@dataclass
class ListDatabasesRequest:
    instance_id: str
    """
    UUID of the Database Instance to list the databases of.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the database.
    """

    managed: Optional[bool]
    """
    Defines whether or not the database is managed.
    """

    owner: Optional[str]
    """
    User that owns this database.
    """

    order_by: Optional[ListDatabasesRequestOrderBy]
    """
    Criteria to use when ordering database listing.
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class ListDatabasesResponse:
    total_count: int
    """
    Total count of databases present on a Database Instance.
    """

    databases: List[Database]
    """
    List of the databases.
    """


@dataclass
class ListInstanceACLRulesRequest:
    instance_id: str
    """
    UUID of the Database Instance.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class ListInstanceACLRulesResponse:
    total_count: int
    """
    Total count of ACL rules present on a Database Instance.
    """

    rules: List[ACLRule]
    """
    List of ACL rules present on a Database Instance.
    """


@dataclass
class ListInstanceLogsDetailsRequest:
    instance_id: str
    """
    UUID of the Database Instance you want logs of.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListInstanceLogsDetailsResponse:
    details: List[ListInstanceLogsDetailsResponseInstanceLogDetail]
    """
    Remote Database Instance logs details.
    """


@dataclass
class ListInstanceLogsRequest:
    instance_id: str
    """
    UUID of the Database Instance you want logs of.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListInstanceLogsRequestOrderBy]
    """
    Criteria to use when ordering Database Instance logs listing.
    """


@dataclass
class ListInstanceLogsResponse:
    instance_logs: List[InstanceLog]
    """
    Available logs in a Database Instance.
    """


@dataclass
class ListInstancesRequest:
    region: Optional[Region]
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
    Please use project_id instead.
    """

    project_id: Optional[str]
    """
    Project ID to list the Database Instance of.
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class ListInstancesResponse:
    total_count: int
    """
    Total count of Database Instances available in a Organization or Project.
    """

    instances: List[Instance]
    """
    List of all Database Instances available in an Organization or Project.
    """


@dataclass
class ListNodeTypesRequest:
    include_disabled_types: bool
    """
    Defines whether or not to include disabled types.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class ListNodeTypesResponse:
    total_count: int
    """
    Total count of node-types available.
    """

    node_types: List[NodeType]
    """
    Types of the node.
    """


@dataclass
class ListPrivilegesRequest:
    instance_id: str
    """
    UUID of the Database Instance.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListPrivilegesRequestOrderBy]
    """
    Criteria to use when ordering privileges listing.
    """

    page: Optional[int]

    page_size: Optional[int]

    database_name: Optional[str]
    """
    Name of the database.
    """

    user_name: Optional[str]
    """
    Name of the user.
    """


@dataclass
class ListPrivilegesResponse:
    total_count: int
    """
    Total count of privileges present on a database.
    """

    privileges: List[Privilege]
    """
    Privileges of a user in a database in a Database Instance.
    """


@dataclass
class ListSnapshotsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the snapshot.
    """

    order_by: Optional[ListSnapshotsRequestOrderBy]
    """
    Criteria to use when ordering snapshot listing.
    """

    instance_id: Optional[str]
    """
    UUID of the Database Instance.
    """

    organization_id: Optional[str]
    """
    Organization ID the snapshots belongs to.
    """

    project_id: Optional[str]
    """
    Project ID the snapshots belongs to.
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class ListSnapshotsResponse:
    total_count: int
    """
    Total count of snapshots available.
    """

    snapshots: List[Snapshot]
    """
    List of snapshots.
    """


@dataclass
class ListUsersRequest:
    instance_id: str
    """
    UUID of the Database Instance.
    """

    region: Optional[Region]
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
    total_count: int
    """
    Total count of users present on a Database Instance.
    """

    users: List[User]
    """
    List of users in a Database Instance.
    """


@dataclass
class MigrateEndpointRequest:
    instance_id: str
    """
    UUID of the instance you want to attach the endpoint to.
    """

    endpoint_id: str
    """
    UUID of the endpoint you want to migrate.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class PrepareInstanceLogsRequest:
    instance_id: str
    """
    UUID of the Database Instance you want logs of.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    start_date: Optional[datetime]
    """
    Start datetime of your log. (RFC 3339 format).
    """

    end_date: Optional[datetime]
    """
    End datetime of your log. (RFC 3339 format).
    """


@dataclass
class PrepareInstanceLogsResponse:
    instance_logs: List[InstanceLog]
    """
    Instance logs for a Database Instance between a start and an end date.
    """


@dataclass
class PromoteReadReplicaRequest:
    read_replica_id: str
    """
    UUID of the Read Replica.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class PurgeInstanceLogsRequest:
    instance_id: str
    """
    UUID of the Database Instance you want logs of.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    log_name: Optional[str]
    """
    Given log name to purge.
    """


@dataclass
class RenewInstanceCertificateRequest:
    instance_id: str
    """
    UUID of the Database Instance you want logs of.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ResetReadReplicaRequest:
    read_replica_id: str
    """
    UUID of the Read Replica.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RestartInstanceRequest:
    instance_id: str
    """
    UUID of the Database Instance you want to restart.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RestoreDatabaseBackupRequest:
    instance_id: str
    """
    Defines the Database Instance where the backup has to be restored.
    """

    database_backup_id: str
    """
    Backup of a logical database.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    database_name: Optional[str]
    """
    Defines the destination database to restore into a specified database (the default destination is set to the origin database of the backup).
    """


@dataclass
class SetInstanceACLRulesRequest:
    instance_id: str
    """
    UUID of the Database Instance where the ACL rules must be set.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    rules: Optional[List[ACLRuleRequest]]
    """
    ACL rules to define for the Database Instance.
    """


@dataclass
class SetInstanceACLRulesResponse:
    rules: List[ACLRule]
    """
    ACLs rules configured for a Database Instance.
    """


@dataclass
class SetInstanceSettingsRequest:
    instance_id: str
    """
    UUID of the Database Instance where the settings must be set.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    settings: Optional[List[InstanceSetting]]
    """
    Settings to define for the Database Instance.
    """


@dataclass
class SetInstanceSettingsResponse:
    settings: List[InstanceSetting]
    """
    Settings configured for a Database Instance.
    """


@dataclass
class SetPrivilegeRequest:
    user_name: str
    """
    Name of the user.
    """

    database_name: str
    """
    Name of the database.
    """

    instance_id: str
    """
    UUID of the Database Instance.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    permission: Optional[Permission]
    """
    Permission to set (Read, Read/Write, All, Custom).
    """


@dataclass
class UpdateDatabaseBackupRequest:
    database_backup_id: str
    """
    UUID of the database backup to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the Database Backup.
    """

    expires_at: Optional[datetime]
    """
    Expiration date (must follow the ISO 8601 format).
    """


@dataclass
class UpdateInstanceRequest:
    instance_id: str
    """
    UUID of the Database Instance to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    backup_schedule_frequency: Optional[int]
    """
    In hours.
    """

    backup_schedule_retention: Optional[int]
    """
    In days.
    """

    is_backup_schedule_disabled: Optional[bool]
    """
    Defines whether or not the backup schedule is disabled.
    """

    name: Optional[str]
    """
    Name of the Database Instance.
    """

    tags: Optional[List[str]]
    """
    Tags of a Database Instance.
    """

    logs_policy: Optional[LogsPolicy]
    """
    Logs policy of the Database Instance.
    """

    backup_same_region: Optional[bool]
    """
    Store logical backups in the same region as the Database Instance.
    """

    backup_schedule_start_hour: Optional[int]
    """
    Defines the start time of the autobackup.
    """


@dataclass
class UpdateSnapshotRequest:
    snapshot_id: str
    """
    UUID of the snapshot to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the snapshot.
    """

    expires_at: Optional[datetime]
    """
    Expiration date (must follow the ISO 8601 format).
    """


@dataclass
class UpdateUserRequest:
    name: str
    """
    Name of the database user.
    """

    instance_id: str
    """
    UUID of the Database Instance the user belongs to.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    password: Optional[str]
    """
    Password of the database user.
    """

    is_admin: Optional[bool]
    """
    Defines whether or not this user got administrative privileges.
    """


@dataclass
class UpgradeInstanceRequest:
    instance_id: str
    """
    UUID of the Database Instance you want to upgrade.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    node_type: Optional[str]

    enable_ha: Optional[bool]

    volume_size: Optional[int]

    volume_type: Optional[VolumeType]

    upgradable_version_id: Optional[str]
