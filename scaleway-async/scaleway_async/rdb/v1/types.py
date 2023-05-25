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


class ACLRuleAction(str, Enum):
    ALLOW = "allow"
    DENY = "deny"

    def __str__(self) -> str:
        return str(self.value)


class ACLRuleDirection(str, Enum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"

    def __str__(self) -> str:
        return str(self.value)


class ACLRuleProtocol(str, Enum):
    TCP = "tcp"
    UDP = "udp"
    ICMP = "icmp"

    def __str__(self) -> str:
        return str(self.value)


class DatabaseBackupStatus(str, Enum):
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


class EngineSettingPropertyType(str, Enum):
    BOOLEAN = "BOOLEAN"
    INT = "INT"
    STRING = "STRING"
    FLOAT = "FLOAT"

    def __str__(self) -> str:
        return str(self.value)


class InstanceLogStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    CREATING = "creating"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class InstanceStatus(str, Enum):
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


class ListDatabaseBackupsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListDatabasesRequestOrderBy(str, Enum):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    SIZE_ASC = "size_asc"
    SIZE_DESC = "size_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListInstanceLogsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListInstancesRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    REGION = "region"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPrivilegesRequestOrderBy(str, Enum):
    USER_NAME_ASC = "user_name_asc"
    USER_NAME_DESC = "user_name_desc"
    DATABASE_NAME_ASC = "database_name_asc"
    DATABASE_NAME_DESC = "database_name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListSnapshotsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    EXPIRES_AT_ASC = "expires_at_asc"
    EXPIRES_AT_DESC = "expires_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListUsersRequestOrderBy(str, Enum):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    IS_ADMIN_ASC = "is_admin_asc"
    IS_ADMIN_DESC = "is_admin_desc"

    def __str__(self) -> str:
        return str(self.value)


class MaintenanceStatus(str, Enum):
    UNKNOWN = "unknown"
    PENDING = "pending"
    DONE = "done"
    CANCELED = "canceled"

    def __str__(self) -> str:
        return str(self.value)


class NodeTypeGeneration(str, Enum):
    UNKNOWN_GENERATION = "unknown_generation"
    GENERATION_V1 = "generation_v1"
    GENERATION_V2 = "generation_v2"

    def __str__(self) -> str:
        return str(self.value)


class NodeTypeStock(str, Enum):
    UNKNOWN = "unknown"
    LOW_STOCK = "low_stock"
    OUT_OF_STOCK = "out_of_stock"
    AVAILABLE = "available"

    def __str__(self) -> str:
        return str(self.value)


class Permission(str, Enum):
    READONLY = "readonly"
    READWRITE = "readwrite"
    ALL = "all"
    CUSTOM = "custom"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)


class ReadReplicaStatus(str, Enum):
    """
    Read replica. status.
    """

    UNKNOWN = "unknown"
    PROVISIONING = "provisioning"
    INITIALIZING = "initializing"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"
    CONFIGURING = "configuring"

    def __str__(self) -> str:
        return str(self.value)


class SnapshotStatus(str, Enum):
    UNKNOWN = "unknown"
    CREATING = "creating"
    READY = "ready"
    RESTORING = "restoring"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class VolumeType(str, Enum):
    LSSD = "lssd"
    BSSD = "bssd"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class ACLRule:
    ip: str

    port: Optional[int]
    """
    :deprecated
    """

    protocol: ACLRuleProtocol

    direction: ACLRuleDirection

    action: ACLRuleAction

    description: str


@dataclass
class ACLRuleRequest:
    ip: str

    description: str


@dataclass
class AddInstanceACLRulesResponse:
    """
    Add instance acl rules response.
    """

    rules: List[ACLRule]
    """
    ACL Rules enabled for the Database Instance.
    """


@dataclass
class AddInstanceSettingsResponse:
    """
    Add instance settings response.
    """

    settings: List[InstanceSetting]
    """
    Settings available on the Database Instance.
    """


@dataclass
class BackupSchedule:
    frequency: int

    retention: int

    disabled: bool


@dataclass
class Database:
    """
    Database.
    """

    name: str
    """
    Name of the database.
    """

    owner: str
    """
    Name of the database owner.
    """

    managed: bool
    """
    Defines whether the database is managed or not.
    """

    size: int
    """
    Size of the database.
    """


@dataclass
class DatabaseBackup:
    """
    Database backup.
    """

    id: str
    """
    UUID of the database backup.
    """

    instance_id: str
    """
    UUID of the Database Instance.
    """

    database_name: str
    """
    Name of backed up database.
    """

    name: str
    """
    Name of the backup.
    """

    status: DatabaseBackupStatus
    """
    Status of the backup.
    """

    size: Optional[int]
    """
    Size of the database backup.
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

    instance_name: str
    """
    Name of the Database Instance of the backup.
    """

    download_url: Optional[str]
    """
    URL you can download the backup from.
    """

    download_url_expires_at: Optional[datetime]
    """
    Expiration date of the download link.
    """

    region: Region
    """
    Region of the database backup.
    """

    same_region: bool
    """
    Store logical backups in the same region as the source Database Instance.
    """


@dataclass
class DatabaseEngine:
    """
    Database engine.
    """

    name: str
    """
    Engine name.
    """

    logo_url: str
    """
    Engine logo URL.
    """

    versions: List[EngineVersion]
    """
    Available versions.
    """

    region: Region
    """
    Region of this Database Instance.
    """


@dataclass
class DeleteInstanceACLRulesResponse:
    """
    Delete instance acl rules response.
    """

    rules: List[ACLRule]
    """
    IP addresses defined in the ACL rules of the Database Instance.
    """


@dataclass
class DeleteInstanceSettingsResponse:
    """
    Delete instance settings response.
    """

    settings: List[InstanceSetting]
    """
    Settings names to delete from the Database Instance.
    """


@dataclass
class Endpoint:
    """
    Endpoint.
    """

    id: str
    """
    UUID of the endpoint.
    """

    ip: Optional[str]
    """
    IPv4 address of the endpoint.
    
    One-of ('address'): at most one of 'ip', 'hostname' could be set.
    """

    port: int
    """
    TCP port of the endpoint.
    """

    name: Optional[str]
    """
    Name of the endpoint.
    """

    private_network: Optional[EndpointPrivateNetworkDetails]
    """
    Private Network details. One maximum per Database Instance or Read Replica (a Database Instance and its Read Replica can have different Private Networks). Cannot be updated (has to be deleted and recreated).
    
    One-of ('details'): at most one of 'private_network', 'load_balancer', 'direct_access' could be set.
    """

    load_balancer: Optional[EndpointLoadBalancerDetails]
    """
    Load balancer details. Public endpoint for Database Instance which is systematically present. One per Database Instance.
    
    One-of ('details'): at most one of 'private_network', 'load_balancer', 'direct_access' could be set.
    """

    direct_access: Optional[EndpointDirectAccessDetails]
    """
    Direct access details. Public endpoint reserved for Read Replicas. One per Read Replica.
    
    One-of ('details'): at most one of 'private_network', 'load_balancer', 'direct_access' could be set.
    """

    hostname: Optional[str]
    """
    Hostname of the endpoint.
    
    One-of ('address'): at most one of 'ip', 'hostname' could be set.
    """


@dataclass
class EndpointDirectAccessDetails:
    pass


@dataclass
class EndpointLoadBalancerDetails:
    pass


@dataclass
class EndpointPrivateNetworkDetails:
    """
    Endpoint. private network details.
    """

    private_network_id: str
    """
    UUID of the private network.
    """

    service_ip: str
    """
    CIDR notation of the endpoint IPv4 address.
    """

    zone: Zone
    """
    Private network zone.
    """


@dataclass
class EndpointSpec:
    """
    Endpoint spec.
    """

    load_balancer: Optional[EndpointSpecLoadBalancer]
    """
    Load balancer endpoint specifications. Public endpoint for Database Instance which is systematically present. One per RDB instance.
    
    One-of ('spec'): at most one of 'load_balancer', 'private_network' could be set.
    """

    private_network: Optional[EndpointSpecPrivateNetwork]
    """
    Private Network endpoint specifications. One maximum per Database Instance or Read Replica (a Database Instance and its Read Replica can have different Private Networks). Cannot be updated (has to be deleted and recreated).
    
    One-of ('spec'): at most one of 'load_balancer', 'private_network' could be set.
    """


@dataclass
class EndpointSpecLoadBalancer:
    pass


@dataclass
class EndpointSpecPrivateNetwork:
    """
    Endpoint spec. private network.
    """

    private_network_id: str
    """
    UUID of the Private Network to be connected to the Database Instance.
    """

    service_ip: Optional[str]
    """
    Endpoint IPv4 address with a CIDR notation. Refer to the official Scaleway documentation to learn more about IP and subnet limitations.
    
    One-of ('config'): at most one of 'service_ip', 'ipam_config' could be set.
    """

    ipam_config: Optional[EndpointSpecPrivateNetworkIpamConfig]
    """
    Automated configuration of your Private Network endpoint with Scaleway IPAM service. One at the most per Database Instance or Read Replica (a Database Instance and its Read Replica can have different Private Networks). Cannot be updated (has to be deleted and recreated).
    
    One-of ('config'): at most one of 'service_ip', 'ipam_config' could be set.
    """


@dataclass
class EndpointSpecPrivateNetworkIpamConfig:
    pass


@dataclass
class EngineSetting:
    """
    Engine setting.
    """

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

    property_type: EngineSettingPropertyType
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
class EngineVersion:
    """
    Engine version.
    """

    version: str
    """
    Database engine version.
    """

    name: str
    """
    Database engine name.
    """

    end_of_life: Optional[datetime]
    """
    End of life date.
    """

    available_settings: List[EngineSetting]
    """
    Engine settings available to be set.
    """

    disabled: bool
    """
    Disabled versions cannot be created.
    """

    beta: bool
    """
    Beta status of engine version.
    """

    available_init_settings: List[EngineSetting]
    """
    Engine settings available to be set at database initialization.
    """


@dataclass
class Instance:
    """
    Instance.
    """

    created_at: Optional[datetime]
    """
    Creation date (must follow the ISO 8601 format).
    """

    volume: Optional[Volume]
    """
    Volumes of the Database Instance.
    """

    region: Region
    """
    Region the Database Instance is in.
    """

    id: str
    """
    UUID of the Database Instance.
    """

    name: str
    """
    Name of the Database Instance.
    """

    organization_id: str
    """
    Organization ID the Database Instance belongs to.
    """

    project_id: str
    """
    Project ID the Database Instance belongs to.
    """

    status: InstanceStatus
    """
    Status of the Database Instance.
    """

    engine: str
    """
    Database engine of the database (PostgreSQL, MySQL, ...).
    """

    upgradable_version: List[UpgradableVersion]
    """
    Available database engine versions for upgrade.
    """

    endpoint: Optional[Endpoint]
    """
    Endpoint of the Database Instance.
    :deprecated
    """

    tags: List[str]
    """
    List of tags applied to the Database Instance.
    """

    settings: List[InstanceSetting]
    """
    Advanced settings of the Database Instance.
    """

    backup_schedule: Optional[BackupSchedule]
    """
    Backup schedule of the Database Instance.
    """

    is_ha_cluster: bool
    """
    Defines whether or not High-Availability is enabled.
    """

    read_replicas: List[ReadReplica]
    """
    Read Replicas of the Database Instance.
    """

    node_type: str
    """
    Node type of the Database Instance.
    """

    init_settings: List[InstanceSetting]
    """
    List of engine settings to be set at database initialization.
    """

    endpoints: List[Endpoint]
    """
    List of Database Instance endpoints.
    """

    logs_policy: Optional[LogsPolicy]
    """
    Logs policy of the Database Instance.
    """

    backup_same_region: bool
    """
    Store logical backups in the same region as the Database Instance.
    """

    maintenances: List[Maintenance]
    """
    List of Database Instance maintenance events.
    """


@dataclass
class InstanceLog:
    """
    Instance log.
    """

    download_url: Optional[str]
    """
    Presigned S3 URL to download your log file.
    """

    id: str
    """
    UUID of the Database Instance log.
    """

    status: InstanceLogStatus
    """
    Status of the logs in a Database Instance.
    """

    node_name: str
    """
    Name of the underlying node.
    """

    expires_at: Optional[datetime]
    """
    Expiration date (must follow the ISO 8601 format).
    """

    created_at: Optional[datetime]
    """
    Creation date (must follow the ISO 8601 format).
    """

    region: Region
    """
    Region the Database Instance is in.
    """


@dataclass
class InstanceMetrics:
    """
    Instance metrics.
    """

    timeseries: List[TimeSeries]
    """
    Time series of metrics of a Database Instance.
    """


@dataclass
class InstanceSetting:
    name: str

    value: str


@dataclass
class ListDatabaseBackupsResponse:
    """
    List database backups response.
    """

    database_backups: List[DatabaseBackup]
    """
    List of database backups.
    """

    total_count: int
    """
    Total count of database backups available.
    """


@dataclass
class ListDatabaseEnginesResponse:
    """
    List database engines response.
    """

    engines: List[DatabaseEngine]
    """
    List of the available database engines.
    """

    total_count: int
    """
    Total count of database engines available.
    """


@dataclass
class ListDatabasesResponse:
    """
    List databases response.
    """

    databases: List[Database]
    """
    List of the databases.
    """

    total_count: int
    """
    Total count of databases present on a Database Instance.
    """


@dataclass
class ListInstanceACLRulesResponse:
    """
    List instance acl rules response.
    """

    rules: List[ACLRule]
    """
    List of ACL rules present on a Database Instance.
    """

    total_count: int
    """
    Total count of ACL rules present on a Database Instance.
    """


@dataclass
class ListInstanceLogsDetailsResponse:
    """
    List instance logs details response.
    """

    details: List[ListInstanceLogsDetailsResponseInstanceLogDetail]
    """
    Remote Database Instance logs details.
    """


@dataclass
class ListInstanceLogsDetailsResponseInstanceLogDetail:
    log_name: str

    size: int


@dataclass
class ListInstanceLogsResponse:
    """
    List instance logs response.
    """

    instance_logs: List[InstanceLog]
    """
    Available logs in a Database Instance.
    """


@dataclass
class ListInstancesResponse:
    """
    List instances response.
    """

    instances: List[Instance]
    """
    List of all Database Instances available in an Organization or Project.
    """

    total_count: int
    """
    Total count of Database Instances available in a Organization or Project.
    """


@dataclass
class ListNodeTypesResponse:
    """
    List node types response.
    """

    node_types: List[NodeType]
    """
    Types of the node.
    """

    total_count: int
    """
    Total count of node-types available.
    """


@dataclass
class ListPrivilegesResponse:
    """
    List privileges response.
    """

    privileges: List[Privilege]
    """
    Privileges of a user in a database in a Database Instance.
    """

    total_count: int
    """
    Total count of privileges present on a database.
    """


@dataclass
class ListSnapshotsResponse:
    """
    List snapshots response.
    """

    snapshots: List[Snapshot]
    """
    List of snapshots.
    """

    total_count: int
    """
    Total count of snapshots available.
    """


@dataclass
class ListUsersResponse:
    """
    List users response.
    """

    users: List[User]
    """
    List of users in a Database Instance.
    """

    total_count: int
    """
    Total count of users present on a Database Instance.
    """


@dataclass
class LogsPolicy:
    """
    Logs policy.
    """

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
    """
    Maintenance.
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

    reason: str
    """
    Maintenance information message.
    """

    status: MaintenanceStatus
    """
    Status of the maintenance.
    """


@dataclass
class NodeType:
    """
    Node type.
    """

    name: str
    """
    Node Type name identifier.
    """

    stock_status: NodeTypeStock
    """
    Current stock status for the Node Type.
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

    volume_constraint: Optional[NodeTypeVolumeConstraintSizes]
    """
    [deprecated] Node Type volume constraints.
    :deprecated
    """

    is_bssd_compatible: Optional[bool]
    """
    The Node Type is compliant with Block Storage.
    :deprecated
    """

    disabled: bool
    """
    The Node Type is currently disabled.
    """

    beta: bool
    """
    The Node Type is currently in beta.
    """

    available_volume_types: List[NodeTypeVolumeType]
    """
    Available storage options for the Node Type.
    """

    is_ha_required: bool
    """
    The Node Type can be used only with high availability option.
    """

    generation: NodeTypeGeneration
    """
    Generation associated the NodeType offer.
    """

    region: Region
    """
    Region the Node Type is in.
    """


@dataclass
class NodeTypeVolumeConstraintSizes:
    """
    Node type. volume constraint sizes.
    """

    min_size: int
    """
    [deprecated] Mimimum size required for the Volume.
    """

    max_size: int
    """
    [deprecated] Maximum size required for the Volume.
    """


@dataclass
class NodeTypeVolumeType:
    """
    Node type. volume type.
    """

    type_: VolumeType
    """
    Volume Type.
    """

    description: str
    """
    The description of the Volume.
    """

    min_size: int
    """
    Mimimum size required for the Volume.
    """

    max_size: int
    """
    Maximum size required for the Volume.
    """

    chunk_size: int
    """
    Minimum increment level for a Block Storage volume size.
    """


@dataclass
class PrepareInstanceLogsResponse:
    """
    Prepare instance logs response.
    """

    instance_logs: List[InstanceLog]
    """
    Instance logs for a Database Instance between a start and an end date.
    """


@dataclass
class Privilege:
    """
    Privilege.
    """

    permission: Permission
    """
    Permission (Read, Read/Write, All, Custom).
    """

    database_name: str
    """
    Name of the database.
    """

    user_name: str
    """
    Name of the user.
    """


@dataclass
class ReadReplica:
    """
    Read replica.
    """

    id: str
    """
    UUID of the Read Replica.
    """

    endpoints: List[Endpoint]
    """
    Display Read Replica connection information.
    """

    status: ReadReplicaStatus
    """
    Read replica status.
    """

    region: Region
    """
    Region the Read Replica is in.
    """

    same_zone: bool
    """
    Whether the replica is in the same availability zone as the main instance nodes or not.
    """


@dataclass
class ReadReplicaEndpointSpec:
    """
    Read replica endpoint spec.
    """

    direct_access: Optional[ReadReplicaEndpointSpecDirectAccess]
    """
    Direct access endpoint specifications. Public endpoint reserved for Read Replicas. One per Read Replica.
    
    One-of ('spec'): at most one of 'direct_access', 'private_network' could be set.
    """

    private_network: Optional[ReadReplicaEndpointSpecPrivateNetwork]
    """
    Private Network endpoint specifications. One at the most per Read Replica. Cannot be updated (has to be deleted and recreated).
    
    One-of ('spec'): at most one of 'direct_access', 'private_network' could be set.
    """


@dataclass
class ReadReplicaEndpointSpecDirectAccess:
    pass


@dataclass
class ReadReplicaEndpointSpecPrivateNetwork:
    """
    Read replica endpoint spec. private network.
    """

    private_network_id: str
    """
    UUID of the Private Network to be connected to the Read Replica.
    """

    service_ip: Optional[str]
    """
    Endpoint IPv4 address with a CIDR notation. Refer to the official Scaleway documentation to learn more about IP and subnet limitations.
    
    One-of ('config'): at most one of 'service_ip', 'ipam_config' could be set.
    """

    ipam_config: Optional[ReadReplicaEndpointSpecPrivateNetworkIpamConfig]
    """
    Automated configuration of your Private Network endpoint with Scaleway IPAM service. One at the most per Database Instance or Read Replica (a Database Instance and its Read Replica can have different private networks). Cannot be updated (has to be deleted and recreated).
    
    One-of ('config'): at most one of 'service_ip', 'ipam_config' could be set.
    """


@dataclass
class ReadReplicaEndpointSpecPrivateNetworkIpamConfig:
    pass


@dataclass
class SetInstanceACLRulesResponse:
    """
    Set instance acl rules response.
    """

    rules: List[ACLRule]
    """
    ACLs rules configured for a Database Instance.
    """


@dataclass
class SetInstanceSettingsResponse:
    """
    Set instance settings response.
    """

    settings: List[InstanceSetting]
    """
    Settings configured for a Database Instance.
    """


@dataclass
class Snapshot:
    """
    Snapshot.
    """

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

    instance_name: str
    """
    Name of the Database Instance of the snapshot.
    """

    node_type: str
    """
    Source node type.
    """

    region: Region
    """
    Region of this snapshot.
    """


@dataclass
class UpgradableVersion:
    id: str

    name: str

    version: str

    minor_version: str


@dataclass
class User:
    """
    User.
    """

    name: str
    """
    Name of the user (Length must be between 1 and 63 characters for PostgreSQL and between 1 and 32 characters for MySQL. First character must be an alphabet character (a-zA-Z). Your username cannot start with '_rdb' or in PostgreSQL, 'pg_'. Only a-zA-Z0-9_$- characters are accepted).
    """

    is_admin: bool
    """
    Defines whether or not a user got administrative privileges on the Database Instance.
    """


@dataclass
class Volume:
    type_: VolumeType

    size: int


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
class ListNodeTypesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    include_disabled_types: bool
    """
    Defines whether or not to include disabled types.
    """

    page: Optional[int]

    page_size: Optional[int]


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
class CreateDatabaseBackupRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance.
    """

    database_name: str
    """
    Name of the database you want to back up.
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
class GetDatabaseBackupRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    database_backup_id: str
    """
    UUID of the database backup.
    """


@dataclass
class UpdateDatabaseBackupRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    database_backup_id: str
    """
    UUID of the database backup to update.
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
class DeleteDatabaseBackupRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    database_backup_id: str
    """
    UUID of the database backup to delete.
    """


@dataclass
class RestoreDatabaseBackupRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    database_backup_id: str
    """
    Backup of a logical database.
    """

    database_name: Optional[str]
    """
    Defines the destination database to restore into a specified database (the default destination is set to the origin database of the backup).
    """

    instance_id: str
    """
    Defines the Database Instance where the backup has to be restored.
    """


@dataclass
class ExportDatabaseBackupRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    database_backup_id: str
    """
    UUID of the database backup you want to export.
    """


@dataclass
class UpgradeInstanceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance you want to upgrade.
    """

    node_type: Optional[str]
    """
    Node type of the Database Instance you want to upgrade to.
    
    One-of ('upgrade_target'): at most one of 'node_type', 'enable_ha', 'volume_size', 'volume_type', 'upgradable_version_id' could be set.
    """

    enable_ha: Optional[bool]
    """
    Defines whether or not high availability should be enabled on the Database Instance.
    
    One-of ('upgrade_target'): at most one of 'node_type', 'enable_ha', 'volume_size', 'volume_type', 'upgradable_version_id' could be set.
    """

    volume_size: Optional[int]
    """
    Increase your block storage volume size.
    
    One-of ('upgrade_target'): at most one of 'node_type', 'enable_ha', 'volume_size', 'volume_type', 'upgradable_version_id' could be set.
    """

    volume_type: Optional[VolumeType]
    """
    Change your Database Instance storage type.
    
    One-of ('upgrade_target'): at most one of 'node_type', 'enable_ha', 'volume_size', 'volume_type', 'upgradable_version_id' could be set.
    """

    upgradable_version_id: Optional[str]
    """
    Update your database engine to a newer version.
    This will create a new Database Instance with same specifications as the current one and perform a Database Engine upgrade.
    
    One-of ('upgrade_target'): at most one of 'node_type', 'enable_ha', 'volume_size', 'volume_type', 'upgradable_version_id' could be set.
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
class GetInstanceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance.
    """


@dataclass
class CreateInstanceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str]
    """
    Please use project_id instead.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    :deprecated
    """

    project_id: Optional[str]
    """
    The Project ID on which the Database Instance will be created.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    """

    name: Optional[str]
    """
    Name of the Database Instance.
    """

    engine: str
    """
    Database engine of the Database Instance (PostgreSQL, MySQL, ...).
    """

    user_name: str
    """
    Username created when the Database Instance is created.
    """

    password: str
    """
    Password of the user.
    """

    node_type: str
    """
    Type of node to use for the Database Instance.
    """

    is_ha_cluster: bool
    """
    Defines whether or not High-Availability is enabled.
    """

    disable_backup: bool
    """
    Defines whether or not backups are disabled.
    """

    tags: Optional[List[str]]
    """
    Tags to apply to the Database Instance.
    """

    init_settings: Optional[List[InstanceSetting]]
    """
    List of engine settings to be set upon Database Instance initialization.
    """

    volume_type: VolumeType
    """
    Type of volume where data is stored (lssd, bssd, ...).
    """

    volume_size: int
    """
    Volume size when volume_type is not lssd.
    """

    init_endpoints: Optional[List[EndpointSpec]]
    """
    One or multiple EndpointSpec used to expose your Database Instance. A load_balancer public endpoint is systematically created.
    """

    backup_same_region: bool
    """
    Defines whether to or not to store logical backups in the same region as the Database Instance.
    """


@dataclass
class UpdateInstanceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance to update.
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


@dataclass
class DeleteInstanceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance to delete.
    """


@dataclass
class CloneInstanceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance you want to clone.
    """

    name: str
    """
    Name of the Database Instance clone.
    """

    node_type: Optional[str]
    """
    Node type of the clone.
    """


@dataclass
class RestartInstanceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance you want to restart.
    """


@dataclass
class GetInstanceCertificateRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance.
    """


@dataclass
class RenewInstanceCertificateRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance you want logs of.
    """


@dataclass
class GetInstanceMetricsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance.
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
class CreateReadReplicaRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance you want to create a Read Replica from.
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
class GetReadReplicaRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    read_replica_id: str
    """
    UUID of the Read Replica.
    """


@dataclass
class DeleteReadReplicaRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    read_replica_id: str
    """
    UUID of the Read Replica.
    """


@dataclass
class ResetReadReplicaRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    read_replica_id: str
    """
    UUID of the Read Replica.
    """


@dataclass
class CreateReadReplicaEndpointRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    read_replica_id: str
    """
    UUID of the Read Replica.
    """

    endpoint_spec: List[ReadReplicaEndpointSpec]
    """
    Specification of the endpoint you want to create.
    """


@dataclass
class PrepareInstanceLogsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance you want logs of.
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
class ListInstanceLogsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance you want logs of.
    """

    order_by: ListInstanceLogsRequestOrderBy
    """
    Criteria to use when ordering Database Instance logs listing.
    """


@dataclass
class GetInstanceLogRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_log_id: str
    """
    UUID of the instance_log you want.
    """


@dataclass
class PurgeInstanceLogsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance you want logs of.
    """

    log_name: Optional[str]
    """
    Given log name to purge.
    """


@dataclass
class ListInstanceLogsDetailsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance you want logs of.
    """


@dataclass
class AddInstanceSettingsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance you want to add settings to.
    """

    settings: List[InstanceSetting]
    """
    Settings to add to the Database Instance.
    """


@dataclass
class DeleteInstanceSettingsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance to delete settings from.
    """

    setting_names: List[str]
    """
    Settings names to delete.
    """


@dataclass
class SetInstanceSettingsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance where the settings must be set.
    """

    settings: List[InstanceSetting]
    """
    Settings to define for the Database Instance.
    """


@dataclass
class ListInstanceACLRulesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance.
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class AddInstanceACLRulesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance you want to add ACL rules to.
    """

    rules: List[ACLRuleRequest]
    """
    ACL rules to add to the Database Instance.
    """


@dataclass
class SetInstanceACLRulesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance where the ACL rules must be set.
    """

    rules: List[ACLRuleRequest]
    """
    ACL rules to define for the Database Instance.
    """


@dataclass
class DeleteInstanceACLRulesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance you want to delete an ACL rule from.
    """

    acl_rule_ips: List[str]
    """
    IP addresses defined in the ACL rules of the Database Instance.
    """


@dataclass
class ListUsersRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance.
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
class CreateUserRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance in which you want to create a user.
    """

    name: str
    """
    Name of the user you want to create.
    """

    password: str
    """
    Password of the user you want to create.
    """

    is_admin: bool
    """
    Defines whether the user will have administrative privileges.
    """


@dataclass
class UpdateUserRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance the user belongs to.
    """

    name: str
    """
    Name of the database user.
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
class DeleteUserRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance to delete the user from.
    """

    name: str
    """
    Name of the user.
    """


@dataclass
class ListDatabasesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance to list the databases of.
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
class CreateDatabaseRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance where to create the database.
    """

    name: str
    """
    Name of the database.
    """


@dataclass
class DeleteDatabaseRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance where to delete the database.
    """

    name: str
    """
    Name of the database to delete.
    """


@dataclass
class ListPrivilegesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance.
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
class SetPrivilegeRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance.
    """

    database_name: str
    """
    Name of the database.
    """

    user_name: str
    """
    Name of the user.
    """

    permission: Permission
    """
    Permission to set (Read, Read/Write, All, Custom).
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
class GetSnapshotRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    snapshot_id: str
    """
    UUID of the snapshot.
    """


@dataclass
class CreateSnapshotRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance.
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
class UpdateSnapshotRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    snapshot_id: str
    """
    UUID of the snapshot to update.
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
class DeleteSnapshotRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    snapshot_id: str
    """
    UUID of the snapshot to delete.
    """


@dataclass
class CreateInstanceFromSnapshotRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    snapshot_id: str
    """
    Block snapshot of the Database Instance.
    """

    instance_name: str
    """
    Name of the Database Instance created with the snapshot.
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
class CreateEndpointRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    instance_id: str
    """
    UUID of the Database Instance you to which you want to add an endpoint.
    """

    endpoint_spec: Optional[EndpointSpec]
    """
    Specification of the endpoint you want to create.
    """


@dataclass
class DeleteEndpointRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    endpoint_id: str
    """
    UUID of the endpoint you want to delete.
    This endpoint can also be used to delete a Read Replica endpoint.
    """


@dataclass
class GetEndpointRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    endpoint_id: str
    """
    UUID of the endpoint you want to get.
    """


@dataclass
class MigrateEndpointRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    endpoint_id: str
    """
    UUID of the endpoint you want to migrate.
    """

    instance_id: str
    """
    UUID of the instance you want to attach the endpoint to.
    """
