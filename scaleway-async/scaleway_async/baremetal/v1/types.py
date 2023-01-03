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


class IPReverseStatus(str, Enum):
    UNKNOWN = "unknown"
    PENDING = "pending"
    ACTIVE = "active"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class IPVersion(str, Enum):
    IPV4 = "IPv4"
    IPV6 = "IPv6"

    def __str__(self) -> str:
        return str(self.value)


class ListServerEventsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListServerPrivateNetworksRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListServersRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListSettingsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class OfferStock(str, Enum):
    EMPTY = "empty"
    LOW = "low"
    AVAILABLE = "available"

    def __str__(self) -> str:
        return str(self.value)


class OfferSubscriptionPeriod(str, Enum):
    UNKNOWN_SUBSCRIPTION_PERIOD = "unknown_subscription_period"
    HOURLY = "hourly"
    MONTHLY = "monthly"

    def __str__(self) -> str:
        return str(self.value)


class ServerBootType(str, Enum):
    UNKNOWN_BOOT_TYPE = "unknown_boot_type"
    NORMAL = "normal"
    RESCUE = "rescue"

    def __str__(self) -> str:
        return str(self.value)


class ServerInstallStatus(str, Enum):
    UNKNOWN = "unknown"
    TO_INSTALL = "to_install"
    INSTALLING = "installing"
    COMPLETED = "completed"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class ServerOptionOptionStatus(str, Enum):
    OPTION_STATUS_UNKNOWN = "option_status_unknown"
    OPTION_STATUS_ENABLE = "option_status_enable"
    OPTION_STATUS_ENABLING = "option_status_enabling"
    OPTION_STATUS_DISABLING = "option_status_disabling"
    OPTION_STATUS_ERROR = "option_status_error"

    def __str__(self) -> str:
        return str(self.value)


class ServerPingStatus(str, Enum):
    PING_STATUS_UNKNOWN = "ping_status_unknown"
    PING_STATUS_UP = "ping_status_up"
    PING_STATUS_DOWN = "ping_status_down"

    def __str__(self) -> str:
        return str(self.value)


class ServerPrivateNetworkStatus(str, Enum):
    UNKNOWN = "unknown"
    ATTACHING = "attaching"
    ATTACHED = "attached"
    ERROR = "error"
    DETACHING = "detaching"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class ServerStatus(str, Enum):
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


class SettingType(str, Enum):
    UNKNOWN = "unknown"
    SMTP = "smtp"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class BMCAccess:
    """
    Bmc access
    """

    url: str
    """
    URL to access to the server console
    """

    login: str
    """
    The login to use for the BMC (Baseboard Management Controller) access authentification
    """

    password: str
    """
    The password to use for the BMC (Baseboard Management Controller) access authentification
    """

    expires_at: Optional[datetime]
    """
    The date after which the BMC (Baseboard Management Controller) access will be closed
    """


@dataclass
class CPU:
    """
    Cpu
    """

    name: str
    """
    Name of the CPU
    """

    core_count: int
    """
    Number of cores of the CPU
    """

    thread_count: int
    """
    Number of threads of the CPU
    """

    frequency: int
    """
    Frequency of the CPU in MHz
    """

    benchmark: str
    """
    Benchmark of the CPU
    """


@dataclass
class CreateServerRequestInstall:
    """
    Create server request. install
    """

    os_id: str
    """
    ID of the OS to install on the server
    """

    hostname: str
    """
    Hostname of the server
    """

    ssh_key_ids: List[str]
    """
    SSH key IDs authorized on the server
    """

    user: Optional[str]
    """
    User used for the installation
    """

    password: Optional[str]
    """
    Password used for the installation
    """

    service_user: Optional[str]
    """
    User used for the service to install
    """

    service_password: Optional[str]
    """
    Password used for the service to install
    """


@dataclass
class Disk:
    """
    Disk
    """

    capacity: int
    """
    Capacity of the disk in bytes
    """

    type_: str
    """
    Type of the disk
    """


@dataclass
class GetServerMetricsResponse:
    """
    Get server metrics response
    """

    pings: Optional[TimeSeries]
    """
    Timeseries of ping on the server
    """


@dataclass
class IP:
    """
    Ip
    """

    id: str
    """
    ID of the IP
    """

    address: str
    """
    Address of the IP
    """

    reverse: str
    """
    Reverse IP value
    """

    version: IPVersion
    """
    Version of IP (v4 or v6)
    """

    reverse_status: IPReverseStatus
    """
    Status of the reverse
    """

    reverse_status_message: str
    """
    A message related to the reverse status, in case of an error for example
    """


@dataclass
class ListOSResponse:
    """
    List os response
    """

    total_count: int
    """
    Total count of matching OS
    """

    os: List[OS]
    """
    OS that match filters
    """


@dataclass
class ListOffersResponse:
    """
    List offers response
    """

    total_count: int
    """
    Total count of matching offers
    """

    offers: List[Offer]
    """
    Offers that match filters
    """


@dataclass
class ListOptionsResponse:
    """
    List options response
    """

    total_count: int
    """
    Total count of matching options
    """

    options: List[Option]
    """
    Options that match filters
    """


@dataclass
class ListServerEventsResponse:
    """
    List server events response
    """

    total_count: int
    """
    Total count of matching events
    """

    events: List[ServerEvent]
    """
    Server events that match filters
    """


@dataclass
class ListServerPrivateNetworksResponse:
    server_private_networks: List[ServerPrivateNetwork]

    total_count: int


@dataclass
class ListServersResponse:
    """
    List servers response
    """

    total_count: int
    """
    Total count of matching servers
    """

    servers: List[Server]
    """
    Servers that match filters
    """


@dataclass
class ListSettingsResponse:
    """
    List settings response
    """

    total_count: int
    """
    Total count of matching sttings
    """

    settings: List[Setting]
    """
    Settings that match filters
    """


@dataclass
class Memory:
    """
    Memory
    """

    capacity: int
    """
    Capacity of the memory in bytes
    """

    type_: str
    """
    Type of the memory
    """

    frequency: int
    """
    Frequency of the memory in MHz
    """

    is_ecc: bool
    """
    True if the memory is an error-correcting code memory
    """


@dataclass
class OS:
    """
    Os
    """

    id: str
    """
    ID of the OS
    """

    name: str
    """
    Name of the OS
    """

    version: str
    """
    Version of the OS
    """

    logo_url: str
    """
    URL of this os's logo
    """

    ssh: Optional[OSOSField]
    """
    Define the SSH requirements to install the OS
    """

    user: Optional[OSOSField]
    """
    Define the username requirements to install the OS
    """

    password: Optional[OSOSField]
    """
    Define the password requirements to install the OS
    """

    service_user: Optional[OSOSField]
    """
    Define the username requirements to install the service
    """

    service_password: Optional[OSOSField]
    """
    Define the password requirements to install the service
    """

    enabled: bool
    """
    State of OS
    """

    license_required: bool
    """
    License required (check server options for pricing details)
    """


@dataclass
class OSOSField:
    editable: bool

    required: bool

    default_value: Optional[str]


@dataclass
class Offer:
    """
    Offer
    """

    id: str
    """
    ID of the offer
    """

    name: str
    """
    Name of the offer
    """

    stock: OfferStock
    """
    Stock level
    """

    bandwidth: int
    """
    Bandwidth available in bits/s with the offer
    """

    commercial_range: str
    """
    Commercial range of the offer
    """

    price_per_hour: Optional[Money]
    """
    Price of the offer for the next 60 minutes (a server order at 11h32 will be payed until 12h32)
    """

    price_per_month: Optional[Money]
    """
    Price of the offer per months
    """

    disks: List[Disk]
    """
    Disks specifications of the offer
    """

    enable: bool
    """
    True if the offer is currently available
    """

    cpus: List[CPU]
    """
    CPU specifications of the offer
    """

    memories: List[Memory]
    """
    Memory specifications of the offer
    """

    quota_name: str
    """
    Name of the quota associated to the offer
    """

    persistent_memories: List[PersistentMemory]
    """
    Persistent memory specifications of the offer
    """

    raid_controllers: List[RaidController]
    """
    Raid controller specifications of the offer
    """

    incompatible_os_ids: List[str]
    """
    Array of incompatible OS ids
    """

    subscription_period: OfferSubscriptionPeriod
    """
    Period of subscription for the offer
    """

    operation_path: str
    """
    Operation path of the service
    """

    fee: Optional[Money]
    """
    Fee to pay on order
    """

    options: List[OfferOptionOffer]
    """
    Options available on offer
    """


@dataclass
class OfferOptionOffer:
    """
    Offer. option offer
    """

    id: str
    """
    ID of the option
    """

    name: str
    """
    Name of the option
    """

    enabled: bool
    """
    If true the option is enabled and included by default in the offer
    If false the option is available for the offer but not included by default
    
    """

    subscription_period: OfferSubscriptionPeriod
    """
    Period of subscription for the offer
    """

    price: Optional[Money]
    """
    Price of the option
    """

    manageable: bool
    """
    Boolean to know if option could be managed
    """

    os_id: Optional[str]
    """
    ID of the OS linked to the option
    """


@dataclass
class Option:
    """
    Option
    """

    id: str
    """
    ID of the option
    """

    name: str
    """
    Name of the option
    """

    manageable: bool
    """
    Is false if the option could not be added or removed
    """


@dataclass
class PersistentMemory:
    """
    Persistent memory
    """

    capacity: int
    """
    Capacity of the memory in bytes
    """

    type_: str
    """
    Type of the memory
    """

    frequency: int
    """
    Frequency of the memory in MHz
    """


@dataclass
class RaidController:
    model: str

    raid_level: List[str]


@dataclass
class Server:
    """
    Server
    """

    id: str
    """
    ID of the server
    """

    organization_id: str
    """
    Organization ID the server is attached to
    """

    project_id: str
    """
    Project ID the server is attached to
    """

    name: str
    """
    Name of the server
    """

    description: str
    """
    Description of the server
    """

    updated_at: Optional[datetime]
    """
    Date of last modification of the server
    """

    created_at: Optional[datetime]
    """
    Date of creation of the server
    """

    status: ServerStatus
    """
    Status of the server
    """

    offer_id: str
    """
    Offer ID of the server
    """

    offer_name: str
    """
    Offer name of the server
    """

    tags: List[str]
    """
    Array of customs tags attached to the server
    """

    ips: List[IP]
    """
    Array of IPs attached to the server
    """

    domain: str
    """
    Domain of the server
    """

    boot_type: ServerBootType
    """
    Boot type of the server
    """

    zone: Zone
    """
    The zone in which is the server
    """

    install: Optional[ServerInstall]
    """
    Configuration of installation
    """

    ping_status: ServerPingStatus
    """
    Server status of ping
    """

    options: List[ServerOption]
    """
    Options enabled on server
    """

    rescue_server: Optional[ServerRescueServer]
    """
    Configuration of rescue boot
    """


@dataclass
class ServerEvent:
    """
    Server event
    """

    id: str
    """
    ID of the server for whom the action will be applied
    """

    action: str
    """
    The action that will be applied to the server
    """

    updated_at: Optional[datetime]
    """
    Date of last modification of the action
    """

    created_at: Optional[datetime]
    """
    Date of creation of the action
    """


@dataclass
class ServerInstall:
    """
    Server. install
    """

    os_id: str
    """
    ID of the OS
    """

    hostname: str
    """
    Host defined in the server install
    """

    ssh_key_ids: List[str]
    """
    SSH public key IDs defined in the server install
    """

    status: ServerInstallStatus
    """
    Status of the server install
    """

    user: str
    """
    User defined in the server install or the default one if none were specified
    """

    service_user: str
    """
    Service user defined in the server install or the default one if none were specified
    """

    service_url: str
    """
    The address of the installed service
    """


@dataclass
class ServerOption:
    """
    Server. option
    """

    id: str
    """
    ID of the option
    """

    name: str
    """
    Name of the option
    """

    status: ServerOptionOptionStatus
    """
    Status of the option
    """

    manageable: bool
    """
    Is false if the option could not be added or removed
    """

    expires_at: Optional[datetime]
    """
    Auto expiration date for compatible options
    """


@dataclass
class ServerPrivateNetwork:
    """
    Server private network
    """

    id: str
    """
    The private network ID
    """

    project_id: str
    """
    The private network project ID
    """

    server_id: str
    """
    The server ID
    """

    private_network_id: str
    """
    The private network ID
    """

    vlan: Optional[int]
    """
    The VLAN ID associated to the private network
    """

    status: ServerPrivateNetworkStatus
    """
    The configuration status of the private network
    """

    created_at: Optional[datetime]
    """
    The private network creation date
    """

    updated_at: Optional[datetime]
    """
    The date the private network was last modified
    """


@dataclass
class ServerRescueServer:
    """
    Server. rescue server
    """

    user: str
    """
    Rescue user name
    """

    password: str
    """
    Rescue password
    """


@dataclass
class SetServerPrivateNetworksResponse:
    server_private_networks: List[ServerPrivateNetwork]


@dataclass
class Setting:
    """
    Setting
    """

    id: str
    """
    ID of the setting
    """

    type_: SettingType
    """
    Type of the setting
    """

    project_id: str
    """
    ID of the project ID
    """

    enabled: bool
    """
    The setting is enable or disable
    """


@dataclass
class ListServersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    Number of server per page
    """

    order_by: Optional[ListServersRequestOrderBy]
    """
    Order of the servers
    """

    tags: Optional[List[str]]
    """
    Filter by tags
    """

    status: Optional[List[str]]
    """
    Filter by status
    """

    name: Optional[str]
    """
    Filter by name
    """

    organization_id: Optional[str]
    """
    Filter by organization ID
    """

    project_id: Optional[str]
    """
    Filter by project ID
    """

    option_id: Optional[str]
    """
    Filter by option ID
    """


@dataclass
class GetServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    ID of the server
    """


@dataclass
class CreateServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    offer_id: str
    """
    Offer ID of the new server
    """

    organization_id: Optional[str]
    """
    Organization ID with which the server will be created.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    :deprecated
    """

    project_id: Optional[str]
    """
    Project ID with which the server will be created.
    
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    """

    name: str
    """
    Name of the server (≠hostname)
    """

    description: str
    """
    Description associated to the server, max 255 characters
    """

    tags: Optional[List[str]]
    """
    Tags to associate to the server
    """

    install: Optional[CreateServerRequestInstall]
    """
    Configuration of installation
    """

    option_ids: Optional[List[str]]
    """
    IDs of options to enable on server
    """


@dataclass
class UpdateServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    ID of the server to update
    """

    name: Optional[str]
    """
    Name of the server (≠hostname), not updated if null
    """

    description: Optional[str]
    """
    Description associated to the server, max 255 characters, not updated if null
    """

    tags: Optional[List[str]]
    """
    Tags associated to the server, not updated if null
    """


@dataclass
class InstallServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    Server ID to install
    """

    os_id: str
    """
    ID of the OS to install on the server
    """

    hostname: str
    """
    Hostname of the server
    """

    ssh_key_ids: List[str]
    """
    SSH key IDs authorized on the server
    """

    user: Optional[str]
    """
    User used for the installation
    """

    password: Optional[str]
    """
    Password used for the installation
    """

    service_user: Optional[str]
    """
    User used for the service to install
    """

    service_password: Optional[str]
    """
    Password used for the service to install
    """


@dataclass
class GetServerMetricsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    Server ID to get the metrics
    """


@dataclass
class DeleteServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    ID of the server to delete
    """


@dataclass
class RebootServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    ID of the server to reboot
    """

    boot_type: ServerBootType
    """
    The type of boot
    """


@dataclass
class StartServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    ID of the server to start
    """

    boot_type: ServerBootType
    """
    The type of boot
    """


@dataclass
class StopServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    ID of the server to stop
    """


@dataclass
class ListServerEventsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    ID of the server events searched
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    Number of server events per page
    """

    order_by: Optional[ListServerEventsRequestOrderBy]
    """
    Order of the server events
    """


@dataclass
class StartBMCAccessRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    ID of the server
    """

    ip: str
    """
    The IP authorized to connect to the given server
    """


@dataclass
class GetBMCAccessRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    ID of the server
    """


@dataclass
class StopBMCAccessRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    ID of the server
    """


@dataclass
class UpdateIPRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    ID of the server
    """

    ip_id: str
    """
    ID of the IP to update
    """

    reverse: Optional[str]
    """
    New reverse IP to update, not updated if null
    """


@dataclass
class AddOptionServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    ID of the server
    """

    option_id: str
    """
    ID of the option to add
    """

    expires_at: Optional[datetime]
    """
    Auto expire the option after this date
    """


@dataclass
class DeleteOptionServerRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    ID of the server
    """

    option_id: str
    """
    ID of the option to delete
    """


@dataclass
class ListOffersRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    Number of offers per page
    """

    subscription_period: Optional[OfferSubscriptionPeriod]
    """
    Period of subscription to filter offers
    """


@dataclass
class GetOfferRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    offer_id: str
    """
    ID of the researched Offer
    """


@dataclass
class GetOptionRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    option_id: str
    """
    ID of the option
    """


@dataclass
class ListOptionsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    Number of options per page
    """

    offer_id: Optional[str]
    """
    Filter options by offer_id
    """

    name: Optional[str]
    """
    Filter options by name
    """


@dataclass
class ListSettingsRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    Set the maximum list size
    """

    order_by: Optional[ListSettingsRequestOrderBy]
    """
    Order the response
    """

    project_id: Optional[str]
    """
    ID of the project
    """


@dataclass
class UpdateSettingRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    setting_id: str
    """
    ID of the setting
    """

    enabled: Optional[bool]
    """
    Enable/Disable the setting
    """


@dataclass
class ListOSRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    page: Optional[int]
    """
    Page number
    """

    page_size: Optional[int]
    """
    Number of OS per page
    """

    offer_id: Optional[str]
    """
    Filter OS by offer ID
    """


@dataclass
class GetOSRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    os_id: str
    """
    ID of the OS
    """


@dataclass
class PrivateNetworkApiAddServerPrivateNetworkRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    The ID of the server
    """

    private_network_id: str
    """
    The ID of the private network
    """


@dataclass
class PrivateNetworkApiSetServerPrivateNetworksRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    The ID of the server
    """

    private_network_ids: List[str]
    """
    The IDs of the private networks
    """


@dataclass
class PrivateNetworkApiListServerPrivateNetworksRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    order_by: Optional[ListServerPrivateNetworksRequestOrderBy]
    """
    The sort order for the returned private networks
    """

    page: Optional[int]
    """
    The page number for the returned private networks
    """

    page_size: Optional[int]
    """
    The maximum number of private networks per page
    """

    server_id: Optional[str]
    """
    Filter private networks by server ID
    """

    private_network_id: Optional[str]
    """
    Filter private networks by private network ID
    """

    organization_id: Optional[str]
    """
    Filter private networks by organization ID
    """

    project_id: Optional[str]
    """
    Filter private networks by project ID
    """


@dataclass
class PrivateNetworkApiDeleteServerPrivateNetworkRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config
    """

    server_id: str
    """
    The ID of the server
    """

    private_network_id: str
    """
    The ID of the private network
    """
