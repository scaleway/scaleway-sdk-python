# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Money,
    TimeSeries,
    Zone,
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

    def __str__(self) -> str:
        return str(self.value)


class SettingType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    SMTP = "smtp"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class CertificationOption:
    pass


@dataclass
class LicenseOption:
    os_id: str


@dataclass
class PrivateNetworkOption:
    pass


@dataclass
class PublicBandwidthOption:
    bandwidth_in_bps: int


@dataclass
class RemoteAccessOption:
    pass


@dataclass
class OSOSField:
    editable: bool

    required: bool

    default_value: Optional[str]


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

    price: Optional[Money]
    """
    Price of the option.
    """

    os_id: Optional[str]
    """
    Deprecated, use LicenseOptionVars.os_id instead.
    """

    license: Optional[LicenseOption]

    public_bandwidth: Optional[PublicBandwidthOption]

    private_network: Optional[PrivateNetworkOption]

    remote_access: Optional[RemoteAccessOption]

    certification: Optional[CertificationOption]


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

    raid_level: List[str]


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

    ssh_key_ids: List[str]
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

    expires_at: Optional[datetime]
    """
    Auto expiration date for compatible options.
    """

    license: Optional[LicenseOption]

    public_bandwidth: Optional[PublicBandwidthOption]

    private_network: Optional[PrivateNetworkOption]

    remote_access: Optional[RemoteAccessOption]

    certification: Optional[CertificationOption]


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
class CreateServerRequestInstall:
    os_id: str
    """
    ID of the OS to installation on the server.
    """

    hostname: str
    """
    Hostname of the server.
    """

    ssh_key_ids: List[str]
    """
    SSH key IDs authorized on the server.
    """

    user: Optional[str]
    """
    User for the installation.
    """

    password: Optional[str]
    """
    Password for the installation.
    """

    service_user: Optional[str]
    """
    Regular user that runs the service to be installed on the server.
    """

    service_password: Optional[str]
    """
    Password used for the service to install.
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

    ssh: Optional[OSOSField]
    """
    Object defining the SSH requirements to install the OS.
    """

    user: Optional[OSOSField]
    """
    Object defining the username requirements to install the OS.
    """

    password: Optional[OSOSField]
    """
    Object defining the password requirements to install the OS.
    """

    service_user: Optional[OSOSField]
    """
    Object defining the username requirements to install the service.
    """

    service_password: Optional[OSOSField]
    """
    Object defining the password requirements to install the service.
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

    disks: List[Disk]
    """
    Disks specifications of the offer.
    """

    enable: bool
    """
    Defines whether the offer is currently available.
    """

    price_per_hour: Optional[Money]
    """
    Price of the offer for the next 60 minutes (a server order at 11h32 will be payed until 12h32).
    """

    price_per_month: Optional[Money]
    """
    Monthly price of the offer, if subscribing on a monthly basis.
    """

    cpus: List[CPU]
    """
    CPU specifications of the offer.
    """

    memories: List[Memory]
    """
    Memory specifications of the offer.
    """

    quota_name: str
    """
    Name of the quota associated to the offer.
    """

    persistent_memories: List[PersistentMemory]
    """
    Persistent memory specifications of the offer.
    """

    raid_controllers: List[RaidController]
    """
    Raid controller specifications of the offer.
    """

    incompatible_os_ids: List[str]
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

    options: List[OfferOptionOffer]
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

    tags: List[str]
    """
    Array of tags attached to the offer.
    """

    fee: Optional[Money]
    """
    One time fee invoiced by Scaleway for the setup and activation of the server.
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

    license: Optional[LicenseOption]

    public_bandwidth: Optional[PublicBandwidthOption]

    private_network: Optional[PrivateNetworkOption]

    remote_access: Optional[RemoteAccessOption]

    certification: Optional[CertificationOption]


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

    updated_at: Optional[datetime]
    """
    Date of last modification of the action.
    """

    created_at: Optional[datetime]
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

    vlan: Optional[int]
    """
    The VLAN ID associated to the Private Network.
    """

    created_at: Optional[datetime]
    """
    The Private Network creation date.
    """

    updated_at: Optional[datetime]
    """
    The date the Private Network was last modified.
    """


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

    updated_at: Optional[datetime]
    """
    Last modification date of the server.
    """

    created_at: Optional[datetime]
    """
    Creation date of the server.
    """

    offer_id: str
    """
    Offer ID of the server.
    """

    offer_name: str
    """
    Offer name of the server.
    """

    tags: List[str]
    """
    Array of custom tags attached to the server.
    """

    ips: List[IP]
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

    zone: Zone
    """
    Zone in which is the server located.
    """

    ping_status: ServerPingStatus
    """
    Status of server ping.
    """

    options: List[ServerOption]
    """
    Options enabled on the server.
    """

    install: Optional[ServerInstall]
    """
    Configuration of the installation.
    """

    rescue_server: Optional[ServerRescueServer]
    """
    Configuration of rescue boot.
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

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    expires_at: Optional[datetime]
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

    expires_at: Optional[datetime]
    """
    The date after which the BMC (Baseboard Management Controller) access will be closed.
    """


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

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[List[str]]
    """
    Tags to associate to the server.
    """

    install: Optional[CreateServerRequestInstall]
    """
    Object describing the configuration details of the OS installation on the server.
    """

    option_ids: Optional[List[str]]
    """
    IDs of options to enable on server.
    """

    project_id: Optional[str]

    organization_id: Optional[str]


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

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteServerRequest:
    server_id: str
    """
    ID of the server to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetBMCAccessRequest:
    server_id: str
    """
    ID of the server.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetOSRequest:
    os_id: str
    """
    ID of the OS.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetOfferRequest:
    offer_id: str
    """
    ID of the researched Offer.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetOptionRequest:
    option_id: str
    """
    ID of the option.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerMetricsRequest:
    server_id: str
    """
    Server ID to get the metrics.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerMetricsResponse:
    pings: Optional[TimeSeries]
    """
    Timeseries object representing pings on the server.
    """


@dataclass
class GetServerRequest:
    server_id: str
    """
    ID of the server.
    """

    zone: Optional[Zone]
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

    ssh_key_ids: List[str]
    """
    SSH key IDs authorized on the server.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    user: Optional[str]
    """
    User used for the installation.
    """

    password: Optional[str]
    """
    Password used for the installation.
    """

    service_user: Optional[str]
    """
    User used for the service to install.
    """

    service_password: Optional[str]
    """
    Password used for the service to install.
    """


@dataclass
class ListOSRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of OS per page.
    """

    offer_id: Optional[str]
    """
    Offer IDs to filter OSes for.
    """


@dataclass
class ListOSResponse:
    total_count: int
    """
    Total count of matching OS.
    """

    os: List[OS]
    """
    OS that match filters.
    """


@dataclass
class ListOffersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of offers per page.
    """

    subscription_period: Optional[OfferSubscriptionPeriod]
    """
    Subscription period type to filter offers by.
    """

    name: Optional[str]
    """
    Offer name to filter offers by.
    """


@dataclass
class ListOffersResponse:
    total_count: int
    """
    Total count of matching offers.
    """

    offers: List[Offer]
    """
    Offers that match filters.
    """


@dataclass
class ListOptionsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of options per page.
    """

    offer_id: Optional[str]
    """
    Offer ID to filter options for.
    """

    name: Optional[str]
    """
    Name to filter options for.
    """


@dataclass
class ListOptionsResponse:
    total_count: int
    """
    Total count of matching options.
    """

    options: List[Option]
    """
    Options that match filters.
    """


@dataclass
class ListServerEventsRequest:
    server_id: str
    """
    ID of the server events searched.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of server events per page.
    """

    order_by: Optional[ListServerEventsRequestOrderBy]
    """
    Order of the server events.
    """


@dataclass
class ListServerEventsResponse:
    total_count: int
    """
    Total count of matching events.
    """

    events: List[ServerEvent]
    """
    Server events that match filters.
    """


@dataclass
class ListServerPrivateNetworksResponse:
    server_private_networks: List[ServerPrivateNetwork]

    total_count: int


@dataclass
class ListServersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of servers per page.
    """

    order_by: Optional[ListServersRequestOrderBy]
    """
    Order of the servers.
    """

    tags: Optional[List[str]]
    """
    Tags to filter for.
    """

    status: Optional[List[str]]
    """
    Status to filter for.
    """

    name: Optional[str]
    """
    Names to filter for.
    """

    organization_id: Optional[str]
    """
    Organization ID to filter for.
    """

    project_id: Optional[str]
    """
    Project ID to filter for.
    """

    option_id: Optional[str]
    """
    Option ID to filter for.
    """


@dataclass
class ListServersResponse:
    total_count: int
    """
    Total count of matching servers.
    """

    servers: List[Server]
    """
    Array of Elastic Metal server objects matching the filters in the request.
    """


@dataclass
class ListSettingsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Set the maximum list size.
    """

    order_by: Optional[ListSettingsRequestOrderBy]
    """
    Sort order for items in the response.
    """

    project_id: Optional[str]
    """
    ID of the Project.
    """


@dataclass
class ListSettingsResponse:
    total_count: int
    """
    Total count of matching settings.
    """

    settings: List[Setting]
    """
    Settings that match filters.
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

    zone: Optional[Zone]
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

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class PrivateNetworkApiListServerPrivateNetworksRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    order_by: Optional[ListServerPrivateNetworksRequestOrderBy]
    """
    The sort order for the returned Private Networks.
    """

    page: Optional[int]
    """
    The page number for the returned Private Networks.
    """

    page_size: Optional[int]
    """
    The maximum number of Private Networks per page.
    """

    server_id: Optional[str]
    """
    Filter Private Networks by server ID.
    """

    private_network_id: Optional[str]
    """
    Filter Private Networks by Private Network ID.
    """

    organization_id: Optional[str]
    """
    Filter Private Networks by Organization ID.
    """

    project_id: Optional[str]
    """
    Filter Private Networks by Project ID.
    """


@dataclass
class PrivateNetworkApiSetServerPrivateNetworksRequest:
    server_id: str
    """
    The ID of the server.
    """

    private_network_ids: List[str]
    """
    The IDs of the Private Networks.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class RebootServerRequest:
    server_id: str
    """
    ID of the server to reboot.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    boot_type: Optional[ServerBootType]
    """
    The type of boot.
    """


@dataclass
class SetServerPrivateNetworksResponse:
    server_private_networks: List[ServerPrivateNetwork]


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

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class StartServerRequest:
    server_id: str
    """
    ID of the server to start.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    boot_type: Optional[ServerBootType]
    """
    The type of boot.
    """


@dataclass
class StopBMCAccessRequest:
    server_id: str
    """
    ID of the server.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class StopServerRequest:
    server_id: str
    """
    ID of the server to stop.
    """

    zone: Optional[Zone]
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

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    reverse: Optional[str]
    """
    New reverse IP to update, not updated if null.
    """


@dataclass
class UpdateServerRequest:
    server_id: str
    """
    ID of the server to update.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    name: Optional[str]
    """
    Name of the server (≠hostname), not updated if null.
    """

    description: Optional[str]
    """
    Description associated with the server, max 255 characters, not updated if null.
    """

    tags: Optional[List[str]]
    """
    Tags associated with the server, not updated if null.
    """


@dataclass
class UpdateSettingRequest:
    setting_id: str
    """
    ID of the setting.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    enabled: Optional[bool]
    """
    Defines whether the setting is enabled.
    """
