# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    Money,
    TimeSeries,
    Zone as ScwZone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class IPReverseStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    PENDING = "pending"
    ACTIVE = "active"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class IPVersion(str, Enum, metaclass=StrEnumMeta):
    I_PV4 = "i_pv4"
    I_PV6 = "i_pv6"

    def __str__(self) -> str:
        return str(self.value)


class ListServerEventsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListServerPrivateNetworksRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListServersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListSettingsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class OfferStock(str, Enum, metaclass=StrEnumMeta):
    EMPTY = "empty"
    LOW = "low"
    AVAILABLE = "available"

    def __str__(self) -> str:
        return str(self.value)


class OfferSubscriptionPeriod(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SUBSCRIPTION_PERIOD = "unknown_subscription_period"
    HOURLY = "hourly"
    MONTHLY = "monthly"

    def __str__(self) -> str:
        return str(self.value)


class SchemaFilesystemFormat(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_FORMAT = "unknown_format"
    FAT32 = "fat32"
    EXT4 = "ext4"
    SWAP = "swap"
    ZFS = "zfs"
    XFS = "xfs"

    def __str__(self) -> str:
        return str(self.value)


class SchemaPartitionLabel(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_PARTITION_LABEL = "unknown_partition_label"
    UEFI = "uefi"
    LEGACY = "legacy"
    ROOT = "root"
    BOOT = "boot"
    SWAP = "swap"
    DATA = "data"
    HOME = "home"
    RAID = "raid"
    ZFS = "zfs"

    def __str__(self) -> str:
        return str(self.value)


class SchemaPoolType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    NO_RAID = "no_raid"
    MIRROR = "mirror"
    RAIDZ1 = "raidz1"
    RAIDZ2 = "raidz2"

    def __str__(self) -> str:
        return str(self.value)


class SchemaRAIDLevel(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_RAID_LEVEL = "unknown_raid_level"
    RAID_LEVEL_0 = "raid_level_0"
    RAID_LEVEL_1 = "raid_level_1"
    RAID_LEVEL_5 = "raid_level_5"
    RAID_LEVEL_6 = "raid_level_6"
    RAID_LEVEL_10 = "raid_level_10"

    def __str__(self) -> str:
        return str(self.value)


class ServerBootType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_BOOT_TYPE = "unknown_boot_type"
    NORMAL = "normal"
    RESCUE = "rescue"

    def __str__(self) -> str:
        return str(self.value)


class ServerInstallStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    TO_INSTALL = "to_install"
    INSTALLING = "installing"
    COMPLETED = "completed"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class ServerOptionOptionStatus(str, Enum, metaclass=StrEnumMeta):
    OPTION_STATUS_UNKNOWN = "option_status_unknown"
    OPTION_STATUS_ENABLE = "option_status_enable"
    OPTION_STATUS_ENABLING = "option_status_enabling"
    OPTION_STATUS_DISABLING = "option_status_disabling"
    OPTION_STATUS_ERROR = "option_status_error"

    def __str__(self) -> str:
        return str(self.value)


class ServerPingStatus(str, Enum, metaclass=StrEnumMeta):
    PING_STATUS_UNKNOWN = "ping_status_unknown"
    PING_STATUS_UP = "ping_status_up"
    PING_STATUS_DOWN = "ping_status_down"

    def __str__(self) -> str:
        return str(self.value)


class ServerPrivateNetworkStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    ATTACHING = "attaching"
    ATTACHED = "attached"
    ERROR = "error"
    DETACHING = "detaching"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class ServerStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    DELIVERING = "delivering"
    READY = "ready"
    STOPPING = "stopping"
    STOPPED = "stopped"
    STARTING = "starting"
    ERROR = "error"
    DELETING = "deleting"
    LOCKED = "locked"
    OUT_OF_STOCK = "out_of_stock"
    ORDERED = "ordered"
    RESETTING = "resetting"
    MIGRATING = "migrating"

    def __str__(self) -> str:
        return str(self.value)


class SettingType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    SMTP = "smtp"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class SchemaPartition:
    label: SchemaPartitionLabel
    number: int
    size: int
    use_all_available_space: bool


@dataclass
class SchemaPool:
    name: str
    type_: SchemaPoolType
    devices: list[str]
    options: list[str]
    filesystem_options: list[str]


@dataclass
class SchemaDisk:
    device: str
    partitions: list[SchemaPartition]


@dataclass
class SchemaFilesystem:
    device: str
    format: SchemaFilesystemFormat
    mountpoint: str


@dataclass
class SchemaRAID:
    name: str
    level: SchemaRAIDLevel
    devices: list[str]


@dataclass
class SchemaZFS:
    pools: list[SchemaPool]


@dataclass
class Schema:
    disks: list[SchemaDisk]
    raids: list[SchemaRAID]
    filesystems: list[SchemaFilesystem]
    zfs: Optional[SchemaZFS] = None


@dataclass
class CertificationOption:
    pass


@dataclass
class LicenseOption:
    os_id: str


@dataclass
class PrivateNetworkOption:
    bandwidth_in_bps: int


@dataclass
class PublicBandwidthOption:
    bandwidth_in_bps: int


@dataclass
class RemoteAccessOption:
    pass


@dataclass
class CreateServerRequestInstall:
    os_id: str
    """
    ID of the OS to installation on the server.
    """

    hostname: str
    """
    Hostname of the server.
    """

    ssh_key_ids: list[str]
    """
    SSH key IDs authorized on the server.
    """

    user: Optional[str] = None
    """
    User for the installation.
    """

    password: Optional[str] = None
    """
    Password for the installation.
    """

    service_user: Optional[str] = None
    """
    Regular user that runs the service to be installed on the server.
    """

    service_password: Optional[str] = None
    """
    Password used for the service to install.
    """

    partitioning_schema: Optional[Schema] = None
    """
    Partitioning schema.
    """


@dataclass
class IP:
    id: str
    """
    ID of the IP.
    """

    address: str
    """
    Address of the IP.
    """

    reverse: str
    """
    Reverse IP value.
    """

    version: IPVersion
    """
    Version of IP (v4 or v6).
    """

    reverse_status: IPReverseStatus
    """
    Status of the reverse.
    """

    reverse_status_message: str
    """
    A message related to the reverse status, e.g. in case of an error.
    """


@dataclass
class ServerInstall:
    os_id: str
    """
    ID of the OS.
    """

    hostname: str
    """
    Host defined during the server installation.
    """

    ssh_key_ids: list[str]
    """
    SSH public key IDs defined during server installation.
    """

    status: ServerInstallStatus
    """
    Status of the server installation.
    """

    user: str
    """
    User defined in the server installation, or the default user if none were specified.
    """

    service_user: str
    """
    Service user defined in the server installation, or the default user if none were specified.
    """

    service_url: str
    """
    Address of the installed service.
    """

    partitioning_schema: Optional[Schema] = None
    """
    Partitioning schema.
    """


@dataclass
class ServerOption:
    id: str
    """
    ID of the option.
    """

    name: str
    """
    Name of the option.
    """

    status: ServerOptionOptionStatus
    """
    Status of the option on this server.
    """

    manageable: bool
    """
    Defines whether the option can be managed (added or removed).
    """

    expires_at: Optional[datetime] = None
    """
    Auto expiration date for compatible options.
    """

    license: Optional[LicenseOption] = None

    public_bandwidth: Optional[PublicBandwidthOption] = None

    private_network: Optional[PrivateNetworkOption] = None

    remote_access: Optional[RemoteAccessOption] = None

    certification: Optional[CertificationOption] = None


@dataclass
class ServerRescueServer:
    user: str
    """
    Rescue user name.
    """

    password: str
    """
    Rescue password.
    """


@dataclass
class OSOSField:
    editable: bool
    required: bool
    default_value: Optional[str] = None


@dataclass
class CPU:
    name: str
    """
    Name of the CPU.
    """

    core_count: int
    """
    Number of CPU cores.
    """

    thread_count: int
    """
    Number CPU threads.
    """

    frequency: int
    """
    Frequency of the CPU in MHz.
    """

    benchmark: str
    """
    Benchmark of the CPU.
    """


@dataclass
class Disk:
    capacity: int
    """
    Capacity of the disk in bytes.
    """

    type_: str
    """
    Type of the disk.
    """


@dataclass
class GPU:
    name: str
    """
    Name of the GPU.
    """

    vram: int
    """
    Capacity of the vram in bytes.
    """


@dataclass
class Memory:
    capacity: int
    """
    Capacity of the memory in bytes.
    """

    type_: str
    """
    Type of the memory.
    """

    frequency: int
    """
    Frequency of the memory in MHz.
    """

    is_ecc: bool
    """
    True if the memory is an error-correcting code memory.
    """


@dataclass
class OfferOptionOffer:
    id: str
    """
    ID of the option.
    """

    name: str
    """
    Name of the option.
    """

    enabled: bool
    """
    If true the option is enabled and included by default in the offer
If false the option is available for the offer but not included by default.
    """

    subscription_period: OfferSubscriptionPeriod
    """
    Period of subscription for the offer.
    """

    manageable: bool
    """
    Boolean to know if option could be managed.
    """

    price: Optional[Money] = None
    """
    Price of the option.
    """

    os_id: Optional[str] = None
    """
    Deprecated, use LicenseOptionVars.os_id instead.
    """

    license: Optional[LicenseOption] = None

    public_bandwidth: Optional[PublicBandwidthOption] = None

    private_network: Optional[PrivateNetworkOption] = None

    remote_access: Optional[RemoteAccessOption] = None

    certification: Optional[CertificationOption] = None


@dataclass
class PersistentMemory:
    capacity: int
    """
    Capacity of the memory in bytes.
    """

    type_: str
    """
    Type of the memory.
    """

    frequency: int
    """
    Frequency of the memory in MHz.
    """


@dataclass
class RaidController:
    model: str
    raid_level: list[str]


@dataclass
class CreateServerRequest:
    offer_id: str
    """
    Offer ID of the new server.
    """

    name: str
    """
    Name of the server (≠hostname).
    """

    description: str
    """
    Description associated with the server, max 255 characters.
    """

    protected: bool
    """
    If enabled, the server can not be deleted.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to associate to the server.
    """

    install: Optional[CreateServerRequestInstall] = None
    """
    Object describing the configuration details of the OS installation on the server.
    """

    option_ids: Optional[list[str]] = field(default_factory=list)
    """
    IDs of options to enable on server.
    """

    project_id: Optional[str] = None

    organization_id: Optional[str] = None


@dataclass
class Server:
    id: str
    """
    ID of the server.
    """

    organization_id: str
    """
    Organization ID the server is attached to.
    """

    project_id: str
    """
    Project ID the server is attached to.
    """

    name: str
    """
    Name of the server.
    """

    description: str
    """
    Description of the server.
    """

    status: ServerStatus
    """
    Status of the server.
    """

    offer_id: str
    """
    Offer ID of the server.
    """

    offer_name: str
    """
    Offer name of the server.
    """

    tags: list[str]
    """
    Array of custom tags attached to the server.
    """

    ips: list[IP]
    """
    Array of IPs attached to the server.
    """

    domain: str
    """
    Domain of the server.
    """

    boot_type: ServerBootType
    """
    Boot type of the server.
    """

    zone: ScwZone
    """
    Zone in which is the server located.
    """

    ping_status: ServerPingStatus
    """
    Status of server ping.
    """

    options: list[ServerOption]
    """
    Options enabled on the server.
    """

    protected: bool
    """
    If enabled, the server can not be deleted.
    """

    updated_at: Optional[datetime] = None
    """
    Last modification date of the server.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the server.
    """

    install: Optional[ServerInstall] = None
    """
    Configuration of the installation.
    """

    rescue_server: Optional[ServerRescueServer] = None
    """
    Configuration of rescue boot.
    """


@dataclass
class OS:
    id: str
    """
    ID of the OS.
    """

    name: str
    """
    Name of the OS.
    """

    version: str
    """
    Version of the OS.
    """

    logo_url: str
    """
    URL of this OS's logo.
    """

    enabled: bool
    """
    Defines if the operating system is enabled or not.
    """

    license_required: bool
    """
    License required (check server options for pricing details).
    """

    allowed: bool
    """
    Defines if a specific Organization is allowed to install this OS type.
    """

    custom_partitioning_supported: bool
    """
    Defines if custom partitioning is supported by this OS.
    """

    ssh: Optional[OSOSField] = None
    """
    Object defining the SSH requirements to install the OS.
    """

    user: Optional[OSOSField] = None
    """
    Object defining the username requirements to install the OS.
    """

    password: Optional[OSOSField] = None
    """
    Object defining the password requirements to install the OS.
    """

    service_user: Optional[OSOSField] = None
    """
    Object defining the username requirements to install the service.
    """

    service_password: Optional[OSOSField] = None
    """
    Object defining the password requirements to install the service.
    """


@dataclass
class Offer:
    id: str
    """
    ID of the offer.
    """

    name: str
    """
    Name of the offer.
    """

    stock: OfferStock
    """
    Stock level.
    """

    bandwidth: int
    """
    Public bandwidth available (in bits/s) with the offer.
    """

    max_bandwidth: int
    """
    Maximum public bandwidth available (in bits/s) depending on available options.
    """

    commercial_range: str
    """
    Commercial range of the offer.
    """

    disks: list[Disk]
    """
    Disks specifications of the offer.
    """

    enable: bool
    """
    Defines whether the offer is currently available.
    """

    cpus: list[CPU]
    """
    CPU specifications of the offer.
    """

    memories: list[Memory]
    """
    Memory specifications of the offer.
    """

    quota_name: str
    """
    Name of the quota associated to the offer.
    """

    persistent_memories: list[PersistentMemory]
    """
    Persistent memory specifications of the offer.
    """

    raid_controllers: list[RaidController]
    """
    Raid controller specifications of the offer.
    """

    incompatible_os_ids: list[str]
    """
    Array of OS images IDs incompatible with the server.
    """

    subscription_period: OfferSubscriptionPeriod
    """
    Period of subscription for the offer.
    """

    operation_path: str
    """
    Operation path of the service.
    """

    options: list[OfferOptionOffer]
    """
    Available options for customization of the server.
    """

    private_bandwidth: int
    """
    Private bandwidth available in bits/s with the offer.
    """

    shared_bandwidth: bool
    """
    Defines whether the offer's bandwidth is shared or not.
    """

    tags: list[str]
    """
    Array of tags attached to the offer.
    """

    gpus: list[GPU]
    """
    GPU specifications of the offer.
    """

    price_per_hour: Optional[Money] = None
    """
    Price of the offer for the next 60 minutes (a server order at 11h32 will be paid until 12h32).
    """

    price_per_month: Optional[Money] = None
    """
    Monthly price of the offer, if subscribing on a monthly basis.
    """

    fee: Optional[Money] = None
    """
    One time fee invoiced by Scaleway for the setup and activation of the server.
    """

    monthly_offer_id: Optional[str] = None
    """
    Exist only for hourly offers, to migrate to the monthly offer.
    """


@dataclass
class Option:
    id: str
    """
    ID of the option.
    """

    name: str
    """
    Name of the option.
    """

    manageable: bool
    """
    Defines whether the option is manageable (could be added or removed).
    """

    license: Optional[LicenseOption] = None

    public_bandwidth: Optional[PublicBandwidthOption] = None

    private_network: Optional[PrivateNetworkOption] = None

    remote_access: Optional[RemoteAccessOption] = None

    certification: Optional[CertificationOption] = None


@dataclass
class ServerEvent:
    id: str
    """
    ID of the server to which the action will be applied.
    """

    action: str
    """
    The action that will be applied to the server.
    """

    updated_at: Optional[datetime] = None
    """
    Date of last modification of the action.
    """

    created_at: Optional[datetime] = None
    """
    Date of creation of the action.
    """


@dataclass
class ServerPrivateNetwork:
    id: str
    """
    The Private Network ID.
    """

    project_id: str
    """
    The Private Network Project ID.
    """

    server_id: str
    """
    The server ID.
    """

    private_network_id: str
    """
    The Private Network ID.
    """

    status: ServerPrivateNetworkStatus
    """
    The configuration status of the Private Network.
    """

    vlan: Optional[int] = 0
    """
    The VLAN ID associated to the Private Network.
    """

    created_at: Optional[datetime] = None
    """
    The Private Network creation date.
    """

    updated_at: Optional[datetime] = None
    """
    The date the Private Network was last modified.
    """


@dataclass
class Setting:
    id: str
    """
    ID of the setting.
    """

    type_: SettingType
    """
    Type of the setting.
    """

    project_id: str
    """
    ID of the Project ID.
    """

    enabled: bool
    """
    Defines whether the setting is enabled.
    """


@dataclass
class AddOptionServerRequest:
    server_id: str
    """
    ID of the server.
    """

    option_id: str
    """
    ID of the option to add.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    expires_at: Optional[datetime] = None
    """
    Auto expire the option after this date.
    """


@dataclass
class BMCAccess:
    url: str
    """
    URL to access to the server console.
    """

    login: str
    """
    The login to use for the BMC (Baseboard Management Controller) access authentification.
    """

    password: str
    """
    The password to use for the BMC (Baseboard Management Controller) access authentification.
    """

    expires_at: Optional[datetime] = None
    """
    The date after which the BMC (Baseboard Management Controller) access will be closed.
    """


@dataclass
class DeleteOptionServerRequest:
    server_id: str
    """
    ID of the server.
    """

    option_id: str
    """
    ID of the option to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteServerRequest:
    server_id: str
    """
    ID of the server to delete.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetBMCAccessRequest:
    server_id: str
    """
    ID of the server.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetDefaultPartitioningSchemaRequest:
    offer_id: str
    """
    ID of the offer.
    """

    os_id: str
    """
    ID of the OS.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetOSRequest:
    os_id: str
    """
    ID of the OS.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetOfferRequest:
    offer_id: str
    """
    ID of the researched Offer.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetOptionRequest:
    option_id: str
    """
    ID of the option.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerMetricsRequest:
    server_id: str
    """
    Server ID to get the metrics.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerMetricsResponse:
    pings: Optional[TimeSeries] = None
    """
    Timeseries object representing pings on the server.
    """


@dataclass
class GetServerRequest:
    server_id: str
    """
    ID of the server.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class InstallServerRequest:
    server_id: str
    """
    Server ID to install.
    """

    os_id: str
    """
    ID of the OS to installation on the server.
    """

    hostname: str
    """
    Hostname of the server.
    """

    ssh_key_ids: list[str]
    """
    SSH key IDs authorized on the server.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    user: Optional[str] = None
    """
    User used for the installation.
    """

    password: Optional[str] = None
    """
    Password used for the installation.
    """

    service_user: Optional[str] = None
    """
    User used for the service to install.
    """

    service_password: Optional[str] = None
    """
    Password used for the service to install.
    """

    partitioning_schema: Optional[Schema] = None
    """
    Partitioning schema.
    """


@dataclass
class ListOSRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Number of OS per page.
    """

    offer_id: Optional[str] = None
    """
    Offer IDs to filter OSes for.
    """


@dataclass
class ListOSResponse:
    total_count: int
    """
    Total count of matching OS.
    """

    os: list[OS]
    """
    OS that match filters.
    """


@dataclass
class ListOffersRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Number of offers per page.
    """

    subscription_period: Optional[OfferSubscriptionPeriod] = (
        OfferSubscriptionPeriod.UNKNOWN_SUBSCRIPTION_PERIOD
    )
    """
    Subscription period type to filter offers by.
    """

    name: Optional[str] = None
    """
    Offer name to filter offers by.
    """


@dataclass
class ListOffersResponse:
    total_count: int
    """
    Total count of matching offers.
    """

    offers: list[Offer]
    """
    Offers that match filters.
    """


@dataclass
class ListOptionsRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Number of options per page.
    """

    offer_id: Optional[str] = None
    """
    Offer ID to filter options for.
    """

    name: Optional[str] = None
    """
    Name to filter options for.
    """


@dataclass
class ListOptionsResponse:
    total_count: int
    """
    Total count of matching options.
    """

    options: list[Option]
    """
    Options that match filters.
    """


@dataclass
class ListServerEventsRequest:
    server_id: str
    """
    ID of the server events searched.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Number of server events per page.
    """

    order_by: Optional[ListServerEventsRequestOrderBy] = (
        ListServerEventsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Order of the server events.
    """


@dataclass
class ListServerEventsResponse:
    total_count: int
    """
    Total count of matching events.
    """

    events: list[ServerEvent]
    """
    Server events that match filters.
    """


@dataclass
class ListServerPrivateNetworksResponse:
    server_private_networks: list[ServerPrivateNetwork]
    total_count: int


@dataclass
class ListServersRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Number of servers per page.
    """

    order_by: Optional[ListServersRequestOrderBy] = (
        ListServersRequestOrderBy.CREATED_AT_ASC
    )
    """
    Order of the servers.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to filter for.
    """

    status: Optional[list[str]] = field(default_factory=list)
    """
    Status to filter for.
    """

    name: Optional[str] = None
    """
    Names to filter for.
    """

    organization_id: Optional[str] = None
    """
    Organization ID to filter for.
    """

    project_id: Optional[str] = None
    """
    Project ID to filter for.
    """

    option_id: Optional[str] = None
    """
    Option ID to filter for.
    """


@dataclass
class ListServersResponse:
    total_count: int
    """
    Total count of matching servers.
    """

    servers: list[Server]
    """
    Array of Elastic Metal server objects matching the filters in the request.
    """


@dataclass
class ListSettingsRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Set the maximum list size.
    """

    order_by: Optional[ListSettingsRequestOrderBy] = (
        ListSettingsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order for items in the response.
    """

    project_id: Optional[str] = None
    """
    ID of the Project.
    """


@dataclass
class ListSettingsResponse:
    total_count: int
    """
    Total count of matching settings.
    """

    settings: list[Setting]
    """
    Settings that match filters.
    """


@dataclass
class MigrateServerToMonthlyOfferRequest:
    server_id: str
    """
    ID of the server.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class PrivateNetworkApiAddServerPrivateNetworkRequest:
    server_id: str
    """
    The ID of the server.
    """

    private_network_id: str
    """
    The ID of the Private Network.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class PrivateNetworkApiDeleteServerPrivateNetworkRequest:
    server_id: str
    """
    The ID of the server.
    """

    private_network_id: str
    """
    The ID of the Private Network.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class PrivateNetworkApiListServerPrivateNetworksRequest:
    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListServerPrivateNetworksRequestOrderBy] = (
        ListServerPrivateNetworksRequestOrderBy.CREATED_AT_ASC
    )
    """
    The sort order for the returned Private Networks.
    """

    page: Optional[int] = 0
    """
    The page number for the returned Private Networks.
    """

    page_size: Optional[int] = 0
    """
    The maximum number of Private Networks per page.
    """

    server_id: Optional[str] = None
    """
    Filter Private Networks by server ID.
    """

    private_network_id: Optional[str] = None
    """
    Filter Private Networks by Private Network ID.
    """

    organization_id: Optional[str] = None
    """
    Filter Private Networks by Organization ID.
    """

    project_id: Optional[str] = None
    """
    Filter Private Networks by Project ID.
    """


@dataclass
class PrivateNetworkApiSetServerPrivateNetworksRequest:
    server_id: str
    """
    The ID of the server.
    """

    private_network_ids: list[str]
    """
    The IDs of the Private Networks.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class RebootServerRequest:
    server_id: str
    """
    ID of the server to reboot.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    boot_type: Optional[ServerBootType] = ServerBootType.UNKNOWN_BOOT_TYPE
    """
    The type of boot.
    """

    ssh_key_ids: Optional[list[str]] = field(default_factory=list)
    """
    Additional SSH public key IDs to configure on rescue image.
    """


@dataclass
class SetServerPrivateNetworksResponse:
    server_private_networks: list[ServerPrivateNetwork]


@dataclass
class StartBMCAccessRequest:
    server_id: str
    """
    ID of the server.
    """

    ip: str
    """
    The IP authorized to connect to the server.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class StartServerRequest:
    server_id: str
    """
    ID of the server to start.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    boot_type: Optional[ServerBootType] = ServerBootType.UNKNOWN_BOOT_TYPE
    """
    The type of boot.
    """

    ssh_key_ids: Optional[list[str]] = field(default_factory=list)
    """
    Additional SSH public key IDs to configure on rescue image.
    """


@dataclass
class StopBMCAccessRequest:
    server_id: str
    """
    ID of the server.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class StopServerRequest:
    server_id: str
    """
    ID of the server to stop.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class UpdateIPRequest:
    server_id: str
    """
    ID of the server.
    """

    ip_id: str
    """
    ID of the IP to update.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    reverse: Optional[str] = None
    """
    New reverse IP to update, not updated if null.
    """


@dataclass
class UpdateServerRequest:
    server_id: str
    """
    ID of the server to update.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str] = None
    """
    Name of the server (≠hostname), not updated if null.
    """

    description: Optional[str] = None
    """
    Description associated with the server, max 255 characters, not updated if null.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags associated with the server, not updated if null.
    """

    protected: Optional[bool] = False
    """
    If enabled, the server can not be deleted.
    """


@dataclass
class UpdateSettingRequest:
    setting_id: str
    """
    ID of the setting.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    enabled: Optional[bool] = False
    """
    Defines whether the setting is enabled.
    """


@dataclass
class ValidatePartitioningSchemaRequest:
    offer_id: str
    """
    Offer ID of the server.
    """

    os_id: str
    """
    OS ID.
    """

    zone: Optional[ScwZone] = None
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    partitioning_schema: Optional[Schema] = None
    """
    Partitioning schema.
    """
