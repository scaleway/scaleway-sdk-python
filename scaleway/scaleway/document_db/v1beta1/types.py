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
    ONGOING = "ongoing"

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


class StorageClass(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STORAGE_CLASS = "unknown_storage_class"
    LSSD = "lssd"
    BSSD = "bssd"
    SBS = "sbs"

    def __str__(self) -> str:
        return str(self.value)


class VolumeType(str, Enum, metaclass=StrEnumMeta):
    LSSD = "lssd"
    BSSD = "bssd"
    SBS_5K = "sbs_5k"
    SBS_15K = "sbs_15k"

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
    private_network_id: str
    """
    UUID of the Private Network.
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
class EndpointSpecPrivateNetworkIpamConfig:
    pass


@dataclass
class ReadReplicaEndpointSpecPrivateNetworkIpamConfig:
    pass


@dataclass
class EngineSetting:
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
class Endpoint:
    id: str
    """
    UUID of the endpoint.
    """

    port: int
    """
    TCP port of the endpoint.
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
    version: str
    """
    Database engine version.
    """

    name: str
    """
    Database engine name.
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

    end_of_life: Optional[datetime]
    """
    End of life date.
    """


@dataclass
class BackupSchedule:
    frequency: int
    """
    Frequency of the backup schedule (in hours).
    """

    retention: int
    """
    Default retention period of backups (in days).
    """

    disabled: bool
    """
    Defines whether the backup schedule feature is disabled.
    """

    next_run_at: Optional[datetime]
    """
    Next run of the backup schedule (accurate to 10 minutes).
    """


@dataclass
class InstanceSetting:
    name: str

    value: str


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
    reason: str
    """
    Maintenance information message.
    """

    status: MaintenanceStatus
    """
    Status of the maintenance.
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

    forced_at: Optional[datetime]
    """
    Time when Scaleway-side maintenance will be applied.
    """


@dataclass
class ReadReplica:
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
    Whether the replica is in the same Availability Zone as the main Database Instance nodes or not.
    """


@dataclass
class UpgradableVersion:
    id: str

    name: str

    version: str

    minor_version: str


@dataclass
class Volume:
    type_: VolumeType

    size: int

    class_: StorageClass


@dataclass
class NodeTypeVolumeConstraintSizes:
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

    class_: StorageClass
    """
    The storage class of the volume.
    """


@dataclass
class SnapshotVolumeType:
    type_: VolumeType

    class_: StorageClass


@dataclass
class ACLRuleRequest:
    ip: str

    description: str


@dataclass
class ACLRule:
    ip: str

    protocol: ACLRuleProtocol

    direction: ACLRuleDirection

    action: ACLRuleAction

    description: str

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
class DatabaseEngine:
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
class Database:
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
class ListInstanceLogsDetailsResponseInstanceLogDetail:
    log_name: str

    size: int


@dataclass
class InstanceLog:
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

    region: Region
    """
    Region the Database Instance is in.
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

    created_at: Optional[datetime]
    """
    Creation date (must follow the ISO 8601 format).
    """

    volume: Optional[Volume]
    """
    Volumes of the Database Instance.
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
    Database engine of the database.
    """

    upgradable_version: List[UpgradableVersion]
    """
    Available database engine versions for upgrade.
    """

    tags: List[str]
    """
    List of tags applied to the Database Instance.
    """

    settings: List[InstanceSetting]
    """
    Advanced settings of the Database Instance.
    """

    is_ha_cluster: bool
    """
    Defines whether or not High-Availability is enabled.
    """

    endpoint: Optional[Endpoint]
    """
    Endpoint of the Database Instance.
    """

    backup_schedule: Optional[BackupSchedule]
    """
    Backup schedule of the Database Instance.
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
    List of engine settings to be set at Database Instance initialization.
    """

    endpoints: List[Endpoint]
    """
    List of Database Instance endpoints.
    """

    backup_same_region: bool
    """
    Store logical backups in the same region as the Database Instance.
    """

    maintenances: List[Maintenance]
    """
    List of Database Instance maintenance events.
    """

    logs_policy: Optional[LogsPolicy]
    """
    Logs policy of the Database Instance.
    """


@dataclass
class NodeType:
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

    disabled: bool
    """
    The Node Type is currently disabled.
    """

    beta: bool
    """
    The Node Type is currently in beta.
    """

    volume_constraint: Optional[NodeTypeVolumeConstraintSizes]
    """
    [deprecated] Node Type volume constraints.
    """

    is_bssd_compatible: Optional[bool]
    """
    The Node Type is compliant with Block Storage.
    """

    available_volume_types: List[NodeTypeVolumeType]
    """
    Available storage options for the Node Type.
    """

    is_ha_required: bool
    """
    The Node Type can be used only with the High Availability option.
    """

    generation: NodeTypeGeneration
    """
    Generation associated the NodeType offer.
    """

    instance_range: str
    """
    Instance range associated with the NodeType offer.
    """

    region: Region
    """
    Region the Node Type is in.
    """


@dataclass
class Privilege:
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

    volume_type: Optional[SnapshotVolumeType]
    """
    Type of volume where data is stored (lssd, bssd or sbs).
    """


@dataclass
class User:
    name: str
    """
    Name of the user (Length must be between 1 and 63 characters. First character must be an alphabet character (a-zA-Z). Your username cannot start with '_rdb' or 'pg_'. Only a-zA-Z0-9_$- characters are accepted).
    """

    is_admin: bool
    """
    Defines whether or not a user got administrative privileges on the Database Instance.
    """


@dataclass
class UpgradeInstanceRequestMajorUpgradeWorkflow:
    upgradable_version_id: str
    """
    This will create a new Database Instance with same specifications as the current one and perform a Database Engine upgrade.
    """

    with_endpoints: bool
    """
    At the end of the migration procedure this option let you migrate all your database endpoint to the upgraded instance.
    """


@dataclass
class AddInstanceACLRulesRequest:
    instance_id: str
    """
    UUID of the Database Instance you want to add ACL rules to.
    """

    rules: List[ACLRuleRequest]
    """
    ACL rules to add to the Database Instance.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
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

    settings: List[InstanceSetting]
    """
    Settings to add to the Database Instance.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class AddInstanceSettingsResponse:
    settings: List[InstanceSetting]
    """
    Settings available on the Database Instance.
    """


@dataclass
class ApplyInstanceMaintenanceRequest:
    instance_id: str
    """
    UUID of the Database Instance to which you want to apply maintenance.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class CloneInstanceRequest:
    instance_id: str
    """
    UUID of the Database Instance you want to clone.
    """

    name: str
    """
    Name of the Database Instance clone.
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
class CreateDatabaseRequest:
    instance_id: str
    """
    UUID of the Database Instance where to create the database.
    """

    name: str
    """
    Name of the database.
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
    snapshot_id: str
    """
    Block snapshot of the Database Instance.
    """

    instance_name: str
    """
    Name of the Database Instance created with the snapshot.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    is_ha_cluster: Optional[bool]
    """
    Defines whether or not High Availability is enabled on the new Database Instance.
    """

    node_type: Optional[str]
    """
    The node type used to restore the snapshot.
    """


@dataclass
class CreateInstanceRequest:
    engine: str
    """
    Database engine of the Database Instance.
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

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the Database Instance.
    """

    is_ha_cluster: bool
    """
    Defines whether or not High-Availability is enabled.
    """

    disable_backup: bool
    """
    Defines whether or not backups are disabled.
    """

    volume_size: int
    """
    Volume size when volume_type is not lssd.
    """

    backup_same_region: bool
    """
    Defines whether to or not to store logical backups in the same region as the Database Instance.
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

    organization_id: Optional[str]

    project_id: Optional[str]


@dataclass
class CreateReadReplicaEndpointRequest:
    read_replica_id: str
    """
    UUID of the Read Replica.
    """

    endpoint_spec: List[ReadReplicaEndpointSpec]
    """
    Specification of the endpoint you want to create.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
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
    Defines whether or not to create the replica in the same Availability Zone as the main Database Instance nodes.
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

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteDatabaseRequest:
    instance_id: str
    """
    UUID of the Database Instance where to delete the database.
    """

    name: str
    """
    Name of the database to delete.
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

    acl_rule_ips: List[str]
    """
    IP addresses defined in the ACL rules of the Database Instance.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
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

    setting_names: List[str]
    """
    Settings names to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
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
    instance_id: str
    """
    UUID of the Database Instance to delete the user from.
    """

    name: str
    """
    Name of the user.
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
    engines: List[DatabaseEngine]
    """
    List of the available database engines.
    """

    total_count: int
    """
    Total count of database engines available.
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
    databases: List[Database]
    """
    List of the databases.
    """

    total_count: int
    """
    Total count of databases present on a Database Instance.
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
    rules: List[ACLRule]
    """
    List of ACL rules present on a Database Instance.
    """

    total_count: int
    """
    Total count of ACL rules present on a Database Instance.
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
    instances: List[Instance]
    """
    List of all Database Instances available in an Organization or Project.
    """

    total_count: int
    """
    Total count of Database Instances available in a Organization or Project.
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
    node_types: List[NodeType]
    """
    Types of the node.
    """

    total_count: int
    """
    Total count of node-types available.
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
    privileges: List[Privilege]
    """
    Privileges of a user in a database in a Database Instance.
    """

    total_count: int
    """
    Total count of privileges present on a database.
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
    snapshots: List[Snapshot]
    """
    List of snapshots.
    """

    total_count: int
    """
    Total count of snapshots available.
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
    users: List[User]
    """
    List of users in a Database Instance.
    """

    total_count: int
    """
    Total count of users present on a Database Instance.
    """


@dataclass
class MigrateEndpointRequest:
    endpoint_id: str
    """
    UUID of the endpoint you want to migrate.
    """

    instance_id: str
    """
    UUID of the instance you want to attach the endpoint to.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
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
class SetInstanceACLRulesRequest:
    instance_id: str
    """
    UUID of the Database Instance where the ACL rules must be set.
    """

    rules: List[ACLRuleRequest]
    """
    ACL rules to define for the Database Instance.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
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

    settings: List[InstanceSetting]
    """
    Settings to define for the Database Instance.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class SetInstanceSettingsResponse:
    settings: List[InstanceSetting]
    """
    Settings configured for a Database Instance.
    """


@dataclass
class SetPrivilegeRequest:
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

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    permission: Optional[Permission]
    """
    Permission to set (Read, Read/Write, All, Custom).
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
    instance_id: str
    """
    UUID of the Database Instance the user belongs to.
    """

    name: str
    """
    Name of the database user.
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

    major_upgrade_workflow: Optional[UpgradeInstanceRequestMajorUpgradeWorkflow]
