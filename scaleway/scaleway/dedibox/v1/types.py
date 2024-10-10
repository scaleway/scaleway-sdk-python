# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from scaleway_core.bridge import (
    Money,
    Zone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class AttachFailoverIPToMacAddressRequestMacType(str, Enum, metaclass=StrEnumMeta):
    MAC_TYPE_UNKNOWN = "mac_type_unknown"
    VMWARE = "vmware"
    KVM = "kvm"
    XEN = "xen"

    def __str__(self) -> str:
        return str(self.value)


class BMCAccessStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    CREATING = "creating"
    CREATED = "created"
    DELETING = "deleting"

    def __str__(self) -> str:
        return str(self.value)


class BackupStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_BACKUP_STATUS = "unknown_backup_status"
    UNINITIALIZED = "uninitialized"
    INACTIVE = "inactive"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)


class FailoverBlockVersion(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_VERSION = "unknown_version"
    IPV4 = "ipv4"
    IPV6 = "ipv6"

    def __str__(self) -> str:
        return str(self.value)


class FailoverIPInterfaceType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    NORMAL = "normal"
    IPMI = "ipmi"
    VIRTUAL = "virtual"

    def __str__(self) -> str:
        return str(self.value)


class FailoverIPStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    READY = "ready"
    BUSY = "busy"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class FailoverIPVersion(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_VERSION = "unknown_version"
    IPV4 = "ipv4"
    IPV6 = "ipv6"

    def __str__(self) -> str:
        return str(self.value)


class GetRpnStatusResponseStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    BUSY = "busy"
    OPERATIONAL = "operational"

    def __str__(self) -> str:
        return str(self.value)


class IPSemantic(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    PROXAD = "proxad"
    EXT = "ext"
    PUBLIC = "public"
    PRIVATE = "private"
    IPMI = "ipmi"
    ADM = "adm"
    REDIRECT = "redirect"
    MIGRATION = "migration"

    def __str__(self) -> str:
        return str(self.value)


class IPStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    READY = "ready"
    BUSY = "busy"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class IPVersion(str, Enum, metaclass=StrEnumMeta):
    IPV4 = "ipv4"
    IPV6 = "ipv6"

    def __str__(self) -> str:
        return str(self.value)


class IPv6BlockDelegationStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    UPDATING = "updating"
    DONE = "done"

    def __str__(self) -> str:
        return str(self.value)


class InvoicePaymentMethod(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_PAYMENT_METHOD = "unknown_payment_method"
    CREDIT_CARD = "credit_card"
    AMEX = "amex"
    PAYPAL = "paypal"
    TRANSFER = "transfer"
    DIRECT_DEBIT = "direct_debit"

    def __str__(self) -> str:
        return str(self.value)


class InvoiceStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_INVOICE_STATUS = "unknown_invoice_status"
    UNPAID = "unpaid"
    PAID = "paid"
    ERRORED = "errored"

    def __str__(self) -> str:
        return str(self.value)


class ListFailoverIPsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    IP_ASC = "ip_asc"
    IP_DESC = "ip_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListInvoicesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListOSRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    RELEASED_AT_ASC = "released_at_asc"
    RELEASED_AT_DESC = "released_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListOffersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    PRICE_ASC = "price_asc"
    PRICE_DESC = "price_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRefundsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRpnCapableSanServersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRpnCapableServersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRpnGroupMembersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRpnGroupsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRpnInvitesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRpnSansRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRpnServerCapabilitiesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRpnV2CapableResourcesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRpnV2GroupLogsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRpnV2GroupsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRpnV2MembersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRpnV2MembersRequestType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    RPNV1_GROUP = "rpnv1_group"
    SERVER = "server"

    def __str__(self) -> str:
        return str(self.value)


class ListServerDisksRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListServerEventsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListServersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListServicesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class LogAction(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_LOG_ACTION = "unknown_log_action"
    GROUP_CREATED = "group_created"
    GROUP_DELETED = "group_deleted"
    MEMBERS_ADDED = "members_added"
    MEMBERS_DELETED = "members_deleted"
    DESCRIPTION_UPDATED = "description_updated"
    RPNV1_MEMBERS_ADDED = "rpnv1_members_added"
    RPNV1_MEMBERS_DELETED = "rpnv1_members_deleted"
    VLAN_UPDATED = "vlan_updated"
    VLAN_UPDATED_ON_ALL_SERVERS = "vlan_updated_on_all_servers"

    def __str__(self) -> str:
        return str(self.value)


class LogStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_LOG_STATUS = "unknown_log_status"
    SUCCESS = "success"
    IN_PROGRESS = "in_progress"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class MemoryType(str, Enum, metaclass=StrEnumMeta):
    DDR2 = "ddr2"
    DDR3 = "ddr3"
    DDR4 = "ddr4"

    def __str__(self) -> str:
        return str(self.value)


class NetworkInterfaceInterfaceType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    NORMAL = "normal"
    IPMI = "ipmi"
    VIRTUAL = "virtual"

    def __str__(self) -> str:
        return str(self.value)


class OSArch(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ARCH = "unknown_arch"
    AMD64 = "amd64"
    X86 = "x86"
    ARM = "arm"
    ARM64 = "arm64"

    def __str__(self) -> str:
        return str(self.value)


class OSType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    SERVER = "server"
    VIRTU = "virtu"
    PANEL = "panel"
    DESKTOP = "desktop"
    CUSTOM = "custom"
    RESCUE = "rescue"

    def __str__(self) -> str:
        return str(self.value)


class OfferAntiDosInfoType(str, Enum, metaclass=StrEnumMeta):
    MINIMAL = "minimal"
    PREVENTIVE = "preventive"
    CURATIVE = "curative"

    def __str__(self) -> str:
        return str(self.value)


class OfferCatalog(str, Enum, metaclass=StrEnumMeta):
    ALL = "all"
    DEFAULT = "default"
    BETA = "beta"
    RESELLER = "reseller"
    PREMIUM = "premium"
    VOLUME = "volume"
    ADMIN = "admin"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)


class OfferPaymentFrequency(str, Enum, metaclass=StrEnumMeta):
    MONTHLY = "monthly"
    ONESHOT = "oneshot"

    def __str__(self) -> str:
        return str(self.value)


class OfferSANInfoType(str, Enum, metaclass=StrEnumMeta):
    HDD = "hdd"
    SSD = "ssd"

    def __str__(self) -> str:
        return str(self.value)


class OfferServerInfoStock(str, Enum, metaclass=StrEnumMeta):
    EMPTY = "empty"
    LOW = "low"
    AVAILABLE = "available"

    def __str__(self) -> str:
        return str(self.value)


class PartitionFileSystem(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    EFI = "efi"
    SWAP = "swap"
    EXT4 = "ext4"
    EXT3 = "ext3"
    EXT2 = "ext2"
    XFS = "xfs"
    NTFS = "ntfs"
    FAT32 = "fat32"
    UFS = "ufs"

    def __str__(self) -> str:
        return str(self.value)


class PartitionType(str, Enum, metaclass=StrEnumMeta):
    PRIMARY = "primary"
    EXTENDED = "extended"
    LOGICAL = "logical"

    def __str__(self) -> str:
        return str(self.value)


class RaidArrayRaidLevel(str, Enum, metaclass=StrEnumMeta):
    NO_RAID = "no_raid"
    RAID0 = "raid0"
    RAID1 = "raid1"
    RAID5 = "raid5"
    RAID6 = "raid6"
    RAID10 = "raid10"

    def __str__(self) -> str:
        return str(self.value)


class RefundMethod(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_REFUND_METHOD = "unknown_refund_method"
    CREDIT_CARD = "credit_card"
    AMEX = "amex"
    PAYPAL = "paypal"
    TRANSFER = "transfer"

    def __str__(self) -> str:
        return str(self.value)


class RefundStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_REFUND_STATUS = "unknown_refund_status"
    UNPAID = "unpaid"
    PAID = "paid"
    ERRORED = "errored"

    def __str__(self) -> str:
        return str(self.value)


class RescueProtocol(str, Enum, metaclass=StrEnumMeta):
    VNC = "vnc"
    SSH = "ssh"

    def __str__(self) -> str:
        return str(self.value)


class RpnGroupMemberStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_RPN_MEMBER_STATUS = "unknown_rpn_member_status"
    PENDING_INVITATION = "pending_invitation"
    ACTIVE = "active"
    CREATING = "creating"
    DELETING = "deleting"
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)


class RpnGroupType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    LOCAL = "local"
    SHARED = "shared"

    def __str__(self) -> str:
        return str(self.value)


class RpnSanIpType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    SERVER_IP = "server_ip"
    RPNV2_SUBNET = "rpnv2_subnet"

    def __str__(self) -> str:
        return str(self.value)


class RpnSanStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    CREATING = "creating"
    ACTIVE = "active"
    DELETING = "deleting"
    MAINTENANCE = "maintenance"

    def __str__(self) -> str:
        return str(self.value)


class RpnV2GroupStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_GROUP_STATUS = "unknown_group_status"
    CREATING = "creating"
    ACTIVE = "active"
    UPDATING = "updating"
    DELETING = "deleting"

    def __str__(self) -> str:
        return str(self.value)


class RpnV2GroupType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    STANDARD = "standard"
    QINQ = "qinq"

    def __str__(self) -> str:
        return str(self.value)


class RpnV2MemberStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_MEMBER_STATUS = "unknown_member_status"
    CREATING = "creating"
    ACTIVE = "active"
    UPDATING = "updating"
    DELETING = "deleting"

    def __str__(self) -> str:
        return str(self.value)


class ServerDiskType(str, Enum, metaclass=StrEnumMeta):
    SATA = "sata"
    SSD = "ssd"
    SAS = "sas"
    SSHD = "sshd"
    USB = "usb"
    NVME = "nvme"

    def __str__(self) -> str:
        return str(self.value)


class ServerInstallStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    BOOTING = "booting"
    SETTING_UP_RAID = "setting_up_raid"
    PARTITIONING = "partitioning"
    FORMATTING = "formatting"
    INSTALLING = "installing"
    CONFIGURING = "configuring"
    CONFIGURING_BOOTLOADER = "configuring_bootloader"
    REBOOTING = "rebooting"
    INSTALLED = "installed"

    def __str__(self) -> str:
        return str(self.value)


class ServerStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    DELIVERING = "delivering"
    INSTALLING = "installing"
    READY = "ready"
    STOPPED = "stopped"
    ERROR = "error"
    LOCKED = "locked"
    RESCUE = "rescue"
    BUSY = "busy"

    def __str__(self) -> str:
        return str(self.value)


class ServiceLevelLevel(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    BASIC = "basic"
    BUSINESS = "business"

    def __str__(self) -> str:
        return str(self.value)


class ServiceProvisioningStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    DELIVERING = "delivering"
    READY = "ready"
    ERROR = "error"
    EXPIRING = "expiring"
    EXPIRED = "expired"

    def __str__(self) -> str:
        return str(self.value)


class ServiceType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    SERVICE = "service"
    ORDER = "order"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class OfferAntiDosInfo:
    type_: OfferAntiDosInfoType


@dataclass
class OfferBackupInfo:
    size: int


@dataclass
class OfferBandwidthInfo:
    speed: int


@dataclass
class OfferLicenseInfo:
    bound_to_ip: bool


@dataclass
class OfferRPNInfo:
    speed: int


@dataclass
class OfferSANInfo:
    size: int
    """
    SAN size (in bytes).
    """

    ha: bool
    """
    High availabilty offer.
    """

    device_type: OfferSANInfoType
    """
    Type of SAN device (hdd / ssd).
    """


@dataclass
class OfferStorageInfo:
    max_quota: int

    size: int


@dataclass
class IP:
    ip_id: int
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

    cidr: int
    """
    Classless InterDomain Routing notation of the IP.
    """

    netmask: str
    """
    Network mask of IP.
    """

    semantic: IPSemantic
    """
    Semantic of IP.
    """

    gateway: str
    """
    Gateway of IP.
    """

    status: IPStatus
    """
    Status of the IP.
    """


@dataclass
class Offer:
    id: int
    """
    ID of the offer.
    """

    name: str
    """
    Name of the offer.
    """

    catalog: OfferCatalog
    """
    Catalog of the offer.
    """

    payment_frequency: OfferPaymentFrequency
    """
    Payment frequency of the offer.
    """

    pricing: Optional[Money]
    """
    Price of the offer.
    """

    server_info: Optional[OfferServerInfo]

    service_level_info: Optional[OfferServiceLevelInfo]

    rpn_info: Optional[OfferRPNInfo]

    san_info: Optional[OfferSANInfo]

    antidos_info: Optional[OfferAntiDosInfo]

    backup_info: Optional[OfferBackupInfo]

    usb_storage_info: Optional[OfferStorageInfo]

    storage_info: Optional[OfferStorageInfo]

    license_info: Optional[OfferLicenseInfo]

    failover_ip_info: Optional[OfferFailoverIpInfo]

    failover_block_info: Optional[OfferFailoverBlockInfo]

    bandwidth_info: Optional[OfferBandwidthInfo]


@dataclass
class NetworkInterface:
    card_id: int
    """
    Card ID of the network interface.
    """

    device_id: int
    """
    Device ID of the network interface.
    """

    mac: str
    """
    MAC address of the network interface.
    """

    type_: NetworkInterfaceInterfaceType
    """
    Network interface type.
    """

    ips: List[IP]
    """
    IPs of the network interface.
    """


@dataclass
class OS:
    id: int
    """
    ID of the OS.
    """

    name: str
    """
    Name of the OS.
    """

    type_: OSType
    """
    Type of the OS.
    """

    version: str
    """
    Version of the OS.
    """

    arch: OSArch
    """
    Architecture of the OS.
    """

    allow_custom_partitioning: bool
    """
    True if the OS allow custom partitioning.
    """

    allow_ssh_keys: bool
    """
    True if the OS allow SSH Keys.
    """

    requires_user: bool
    """
    True if the OS requires user.
    """

    requires_admin_password: bool
    """
    True if the OS requires admin password.
    """

    requires_panel_password: bool
    """
    True if the OS requires panel password.
    """

    allowed_filesystems: List[PartitionFileSystem]
    """
    True if the OS allow file systems.
    """

    requires_license: bool
    """
    True if the OS requires license.
    """

    license_offers: List[Offer]
    """
    License offers available with the OS.
    """

    display_name: str
    """
    Display name of the OS.
    """

    password_regex: str
    """
    Regex used to validate the installation passwords.
    """

    hostname_max_length: int
    """
    Hostname max length.
    """

    max_partitions: Optional[int]
    """
    Maximum number of partitions which can be created.
    """

    panel_password_regex: Optional[str]
    """
    Regex used to validate the panel installation password.
    """

    requires_valid_hostname: Optional[bool]
    """
    If both requires_valid_hostname & hostname_regex are set, it means that at least one of the criterias must be valid.
    """

    hostname_regex: Optional[str]
    """
    If both requires_valid_hostname & hostname_regex are set, it means that at least one of the criterias must be valid.
    """

    released_at: Optional[datetime]
    """
    OS release date.
    """


@dataclass
class ServerLocation:
    rack: str

    room: str

    datacenter_name: str


@dataclass
class ServerOption:
    options: List[ServerOption]

    offer: Optional[Offer]

    created_at: Optional[datetime]

    updated_at: Optional[datetime]

    expired_at: Optional[datetime]


@dataclass
class ServiceLevel:
    offer_id: int
    """
    Offer ID of service level.
    """

    level: ServiceLevelLevel
    """
    Level type of service level.
    """


@dataclass
class RpnSan:
    id: int
    """
    RPN SAN  ID.
    """

    datacenter_name: str
    """
    Datacenter location.
    """

    organization_id: str
    """
    Organization ID.
    """

    project_id: str
    """
    Project ID.
    """

    server_hostname: str
    """
    RPN SAN server hostname.
    """

    iqn_suffix: str
    """
    IQN suffix.
    """

    offer_id: int
    """
    Offer ID.
    """

    created_at: Optional[datetime]
    """
    Date of creation of the RPN SAN.
    """

    offer_name: str
    """
    Offer description.
    """

    status: RpnSanStatus
    """
    Status.
    """

    storage_size: int
    """
    RPN SAN storage size.
    """

    iqn: str

    rpnv1_compatible: bool
    """
    True if the SAN is compatible with the RPNv1 technology.
    """

    rpnv1_implicit: bool
    """
    True if the offer supports the RPNv1 implicitly, false if it must to be added to a group to support RPNv1.
    """

    offer: Optional[Offer]

    delivered_at: Optional[datetime]
    """
    RPN SAN delivery date.
    """

    terminated_at: Optional[datetime]
    """
    RPN SAN termination date.
    """

    expires_at: Optional[datetime]
    """
    RPN SAN expiration date.
    """


@dataclass
class RpnGroup:
    id: int
    """
    Rpn group member ID.
    """

    name: str
    """
    Rpn group name.
    """

    type_: RpnGroupType
    """
    Rpn group type (local or shared).
    """

    active: bool
    """
    Whether the group is active or not.
    """

    owner: str
    """
    RPN group owner.
    """

    members_count: int
    """
    Total number of members.
    """

    organization_id: str
    """
    Rpn group organization ID.
    """

    project_id: str
    """
    Rpn group project ID.
    """

    created_at: Optional[datetime]
    """
    Rpn group creation date.
    """


@dataclass
class RpnV2GroupSubnet:
    address: str

    cidr: int


@dataclass
class Server:
    id: int
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

    hostname: str
    """
    Hostname of the server.
    """

    rebooted_at: Optional[datetime]
    """
    Date of last reboot of the server.
    """

    status: ServerStatus
    """
    Status of the server.
    """

    abuse_contact: str
    """
    Abuse contact of the server.
    """

    interfaces: List[NetworkInterface]
    """
    Network interfaces of the server.
    """

    zone: Zone
    """
    The zone in which is the server.
    """

    options: List[ServerOption]
    """
    Options subscribe on the server.
    """

    has_bmc: bool
    """
    Boolean if the server has a BMC.
    """

    tags: List[str]
    """
    Array of customs tags attached to the server.
    """

    is_outsourced: bool
    """
    Whether the server is outsourced or not.
    """

    ipv6_slaac: bool
    """
    Whether or not you can enable/disable the IPv6.
    """

    qinq: bool
    """
    Whether the server is compatible with QinQ.
    """

    is_rpnv2_member: bool
    """
    Whether or not the server is already part of an rpnv2 group.
    """

    created_at: Optional[datetime]
    """
    Date of creation of the server.
    """

    updated_at: Optional[datetime]
    """
    Date of last modification of the server.
    """

    expired_at: Optional[datetime]
    """
    Date of release of the server.
    """

    offer: Optional[Offer]
    """
    Offer of the server.
    """

    location: Optional[ServerLocation]
    """
    Location of the server.
    """

    os: Optional[OS]
    """
    OS installed on the server.
    """

    level: Optional[ServiceLevel]
    """
    Service level of the server.
    """

    rescue_os: Optional[OS]
    """
    Rescue OS of the server.
    """


@dataclass
class FailoverBlock:
    id: int
    """
    ID of the failover block.
    """

    address: str
    """
    IP of the failover block.
    """

    nameservers: List[str]
    """
    Name servers.
    """

    ip_version: FailoverBlockVersion
    """
    IP version of the failover block.
    """

    cidr: int
    """
    Classless InterDomain Routing notation of the failover block.
    """

    netmask: str
    """
    Netmask of the failover block.
    """

    gateway_ip: str
    """
    Gateway IP of the failover block.
    """


@dataclass
class RpnSanIpRpnV2Group:
    id: int

    name: str


@dataclass
class RpnSanIpServer:
    id: int

    hostname: str

    datacenter_name: str


@dataclass
class RpnSanServer:
    id: int
    """
    The RPN SAN server ID.
    """

    datacenter_name: str
    """
    The RPN SAN server datacenter name.
    """

    hostname: str
    """
    The RPN SAN server hostname.
    """

    sans: List[RpnSan]
    """
    RPN SANs linked to the RPN SAN server.
    """

    zone: Zone
    """
    The RPN SAN server zone.
    """


@dataclass
class RpnV2Group:
    id: int
    """
    RPN V2 group ID.
    """

    name: str
    """
    RPN V2 group name.
    """

    compatible_rpnv1: bool
    """
    Whether or not the RPN V1 compatibility was enabled.
    """

    organization_id: str
    """
    Organization ID of the RPN V2 group.
    """

    project_id: str
    """
    Project ID of the RPN V2 group.
    """

    type_: RpnV2GroupType
    """
    RPN V2 group type (qing / standard).
    """

    status: RpnV2GroupStatus
    """
    RPN V2 group status.
    """

    owner: str
    """
    RPN V2 group owner.
    """

    members_count: int
    """
    Total number of members.
    """

    gateway: str
    """
    RPN V2 gateway.
    """

    subnet: Optional[RpnV2GroupSubnet]
    """
    RPN V2 subnet.
    """

    rpnv1_group: Optional[RpnGroup]
    """
    The RPNv1 group (if the compatibility was enabled).
    """


@dataclass
class RpnV2Member:
    id: int
    """
    RPN V2 member ID.
    """

    status: RpnV2MemberStatus
    """
    RPN V2 member status.
    """

    vlan: str
    """
    RPN V2 member VLAN.
    """

    speed: Optional[int]
    """
    RPN speed.
    """

    server: Optional[Server]

    rpnv1_group: Optional[RpnGroup]


@dataclass
class ServerDisk:
    id: int

    connector: str

    type_: ServerDiskType

    capacity: int

    is_addon: bool


@dataclass
class Service:
    id: int
    """
    ID of the service.
    """

    provisioning_status: ServiceProvisioningStatus
    """
    Provisioning status of the service.
    """

    type_: ServiceType
    """
    Service type, either order or service.
    """

    resource_id: Optional[int]
    """
    Resource ID of the service.
    """

    offer: Optional[Offer]
    """
    Offer of the service.
    """

    created_at: Optional[datetime]
    """
    Creation date of the service.
    """

    delivered_at: Optional[datetime]
    """
    Delivery date of the service.
    """

    terminated_at: Optional[datetime]
    """
    Terminatation date of the service.
    """

    expires_at: Optional[datetime]
    """
    Expiration date of the service.
    """


@dataclass
class GetIPv6BlockQuotasResponseQuota:
    quota: int

    cidr: int


@dataclass
class InstallPartition:
    file_system: PartitionFileSystem
    """
    File system of the installation partition.
    """

    raid_level: RaidArrayRaidLevel
    """
    RAID level of the installation partition.
    """

    capacity: int
    """
    Capacity of the installation partition.
    """

    connectors: List[str]
    """
    Connectors of the installation partition.
    """

    mount_point: Optional[str]
    """
    Mount point of the installation partition.
    """


@dataclass
class FailoverIP:
    id: int
    """
    ID of the failover IP.
    """

    address: str
    """
    IP of the failover IP.
    """

    reverse: str
    """
    Reverse IP value.
    """

    ip_version: FailoverIPVersion
    """
    IP version of the failover IP.
    """

    cidr: int
    """
    Classless InterDomain Routing notation of the failover IP.
    """

    netmask: str
    """
    Netmask of the failover IP.
    """

    gateway_ip: str
    """
    Gateway IP of the failover IP.
    """

    status: FailoverIPStatus
    """
    Status of the IP failover.
    """

    type_: FailoverIPInterfaceType
    """
    The interface type.
    """

    mac: Optional[str]
    """
    MAC address of the IP failover.
    """

    server_id: Optional[int]
    """
    Server ID linked to the IP failover.
    """

    block: Optional[FailoverBlock]
    """
    Block of the IP failover.
    """

    server_zone: Optional[str]
    """
    The server zone (if assigned).
    """


@dataclass
class ListIPv6BlockSubnetsAvailableResponseSubnet:
    address: str

    cidr: int


@dataclass
class InvoiceSummary:
    id: int

    status: InvoiceStatus

    payment_method: InvoicePaymentMethod

    transaction_id: int

    total_with_taxes: Optional[Money]

    total_without_taxes: Optional[Money]

    created_at: Optional[datetime]

    paid_at: Optional[datetime]


@dataclass
class RpnSanIp:
    type_: RpnSanIpType
    """
    IP type (server | rpnv2_subnet).
    """

    ip: Optional[IP]
    """
    An IP object.
    """

    server: Optional[RpnSanIpServer]

    rpnv2_group: Optional[RpnSanIpRpnV2Group]


@dataclass
class RefundSummary:
    id: int

    status: RefundStatus

    method: RefundMethod

    total_with_taxes: Optional[Money]

    total_without_taxes: Optional[Money]

    created_at: Optional[datetime]

    refunded_at: Optional[datetime]


@dataclass
class RpnGroupMember:
    id: int
    """
    Rpn group member ID.
    """

    status: RpnGroupMemberStatus
    """
    RPN group member status.
    """

    group_id: int
    """
    RPN group ID.
    """

    group_name: str
    """
    RPN group name.
    """

    group_owner: str
    """
    RPN group owner.
    """

    owner: str
    """
    RPN member owner.
    """

    san_server: Optional[RpnSanServer]
    """
    Authorized RPN SAN server.
    """

    server: Optional[Server]
    """
    Authorized rpn v1 capable server.
    """

    speed: Optional[int]
    """
    RPN speed.
    """


@dataclass
class RpnSanSummary:
    id: int
    """
    RPN SAN  ID.
    """

    datacenter_name: str
    """
    Datacenter location.
    """

    organization_id: str
    """
    Organization ID.
    """

    project_id: str
    """
    Project ID.
    """

    server_hostname: str
    """
    RPN SAN server hostname.
    """

    iqn_suffix: str
    """
    IQN suffix.
    """

    offer_id: int
    """
    Offer ID.
    """

    created_at: Optional[datetime]
    """
    Date of creation of the RPN SAN.
    """

    offer_name: str
    """
    Offer description.
    """

    status: RpnSanStatus
    """
    Status.
    """

    storage_size: int
    """
    RPN SAN storage size.
    """

    rpnv1_compatible: bool
    """
    True if the SAN is compatible with the RPNv1 technology.
    """

    rpnv1_implicit: bool
    """
    True if the offer supports the RPNv1 implicitly, false if it must to be added to a group to support RPNv1.
    """

    delivered_at: Optional[datetime]
    """
    RPN SAN delivery date.
    """

    terminated_at: Optional[datetime]
    """
    RPN SAN termination date.
    """

    expires_at: Optional[datetime]
    """
    RPN SAN expiration date.
    """


@dataclass
class RpnServerCapability:
    id: int
    """
    Server ID.
    """

    hostname: str
    """
    Server hostname.
    """

    datacenter_name: str
    """
    Server datacenter name.
    """

    zone: Zone
    """
    Server zone.
    """

    compatible_qinq: bool
    """
    True if server is compatible with QinQ protocol (rpn v2).
    """

    can_join_qinq_group: bool
    """
    True if server can join a QinQ group.
    """

    rpnv1_group_count: int
    """
    Times server is linked in a rpnv1 group.
    """

    rpnv2_group_count: int
    """
    Times server is linked in a rpnv2 group.
    """

    can_join_rpnv2_group: bool
    """
    True if server can join an rpnv2 group.
    """

    ip_address: Optional[str]
    """
    Private IP address (if rpn compatiblle).
    """

    rpn_version: Optional[int]
    """
    Supported rpn version.
    """


@dataclass
class Log:
    id: int
    """
    RPN V2 log ID.
    """

    action: LogAction
    """
    Which action was performed.
    """

    status: LogStatus
    """
    Action status.
    """

    group: Optional[RpnV2Group]
    """
    RPN V2 group.
    """

    member: Optional[RpnV2Member]
    """
    RPN V2 member (if appliable).
    """

    created_at: Optional[datetime]
    """
    Creation date.
    """

    finished_at: Optional[datetime]
    """
    Completion date.
    """


@dataclass
class ServerEvent:
    event_id: int
    """
    ID of the event.
    """

    description: str
    """
    Description of the event.
    """

    date: Optional[datetime]
    """
    Date of the event.
    """


@dataclass
class ServerSummary:
    id: int
    """
    ID of the server.
    """

    datacenter_name: str
    """
    Datacenter of the server.
    """

    organization_id: str
    """
    Organization ID the server is attached to.
    """

    project_id: str
    """
    Project ID the server is attached to.
    """

    hostname: str
    """
    Hostname of the server.
    """

    created_at: Optional[datetime]
    """
    Date of creation of the server.
    """

    updated_at: Optional[datetime]
    """
    Date of last modification of the server.
    """

    expired_at: Optional[datetime]
    """
    Date of release of the server.
    """

    offer_id: int
    """
    Offer ID of the server.
    """

    offer_name: str
    """
    Offer name of the server.
    """

    status: ServerStatus
    """
    Status of the server.
    """

    interfaces: List[NetworkInterface]
    """
    Network interfaces of the server.
    """

    zone: Zone
    """
    The zone in which is the server.
    """

    is_outsourced: bool
    """
    Whether the server is outsourced or not.
    """

    qinq: bool
    """
    Whether the server is compatible with QinQ.
    """

    os_id: Optional[int]
    """
    OS ID installed on server.
    """

    level: Optional[ServiceLevel]
    """
    Service level of the server.
    """

    rpn_version: Optional[int]
    """
    Supported RPN version.
    """


@dataclass
class CPU:
    name: str
    """
    Name of CPU.
    """

    core_count: int
    """
    Number of cores of the CPU.
    """

    thread_count: int
    """
    Number of threads of the CPU.
    """

    frequency: int
    """
    Frequency of the CPU.
    """


@dataclass
class Disk:
    capacity: int
    """
    Capacity of the disk.
    """

    type_: ServerDiskType
    """
    Type of the disk.
    """


@dataclass
class Memory:
    capacity: int
    """
    Capacity of the memory.
    """

    type_: MemoryType
    """
    Type of the memory.
    """

    frequency: int
    """
    Frequency of the memory.
    """

    is_ecc: bool
    """
    True if the memory is an error-correcting code memory.
    """


@dataclass
class PersistentMemory:
    capacity: int
    """
    Capacity of the persistent memory.
    """

    frequency: int
    """
    Frequency of the persistent memory.
    """

    model: str
    """
    Model of the persistent memory.
    """


@dataclass
class RaidController:
    model: str
    """
    Model of the RAID controller.
    """

    raid_level: List[str]
    """
    RAID level of the RAID controller.
    """


@dataclass
class RaidArray:
    raid_level: RaidArrayRaidLevel
    """
    The RAID level.
    """

    disks: List[ServerDisk]
    """
    Disks on the RAID controller.
    """


@dataclass
class Partition:
    type_: PartitionType
    """
    Type of the partition.
    """

    file_system: PartitionFileSystem
    """
    File system of the partition.
    """

    raid_level: RaidArrayRaidLevel
    """
    Raid level of the partition.
    """

    capacity: int
    """
    Capacity of the partition.
    """

    connectors: List[str]
    """
    Connectors of the partition.
    """

    mount_point: Optional[str]
    """
    Mount point of the partition.
    """


@dataclass
class UpdatableRaidArray:
    raid_level: RaidArrayRaidLevel
    """
    The RAID level.
    """

    disk_ids: List[int]
    """
    The list of Disk ID of the updatable RAID.
    """


@dataclass
class AttachFailoverIPToMacAddressRequest:
    ip_id: int
    """
    ID of the failover IP.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    type_: Optional[AttachFailoverIPToMacAddressRequestMacType]
    """
    A mac type.
    """

    mac: Optional[str]
    """
    A valid mac address (existing or not).
    """


@dataclass
class AttachFailoverIPsRequest:
    server_id: int
    """
    ID of the server.
    """

    fips_ids: List[int]
    """
    List of ID of failovers IP to attach.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
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

    status: BMCAccessStatus
    """
    Status of the connection.
    """

    expires_at: Optional[datetime]
    """
    The date after which the BMC (Baseboard Management Controller) access will be closed.
    """


@dataclass
class Backup:
    id: int
    """
    ID of the backup.
    """

    login: str
    """
    Login of the backup.
    """

    server: str
    """
    Server of the backup.
    """

    status: BackupStatus
    """
    Status of the backup.
    """

    acl_enabled: bool
    """
    ACL enable boolean of the backup.
    """

    autologin: bool
    """
    Autologin boolean of the backup.
    """

    quota_space: int
    """
    Total quota space of the backup.
    """

    quota_space_used: int
    """
    Quota space used of the backup.
    """

    quota_files: int
    """
    Total quota files of the backup.
    """

    quota_files_used: int
    """
    Quota files used of the backup.
    """


@dataclass
class BillingApiCanOrderRequest:
    project_id: Optional[str]


@dataclass
class BillingApiDownloadInvoiceRequest:
    invoice_id: int


@dataclass
class BillingApiDownloadRefundRequest:
    refund_id: int


@dataclass
class BillingApiGetInvoiceRequest:
    invoice_id: int


@dataclass
class BillingApiGetRefundRequest:
    refund_id: int


@dataclass
class BillingApiListInvoicesRequest:
    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListInvoicesRequestOrderBy]

    project_id: Optional[str]


@dataclass
class BillingApiListRefundsRequest:
    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListRefundsRequestOrderBy]

    project_id: Optional[str]


@dataclass
class CanOrderResponse:
    can_order: bool

    quota_ok: bool

    phone_confirmed: bool

    email_confirmed: bool

    user_confirmed: bool

    payment_mode: bool

    billing_ok: bool

    message: Optional[str]


@dataclass
class CancelServerInstallRequest:
    server_id: int
    """
    Server ID of the server to cancel install.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class CreateFailoverIPsRequest:
    offer_id: int
    """
    Failover IP offer ID.
    """

    quantity: int
    """
    Quantity.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str]
    """
    Project ID.
    """


@dataclass
class CreateFailoverIPsResponse:
    total_count: int

    services: List[Service]


@dataclass
class CreateServerRequest:
    offer_id: int
    """
    Offer ID of the new server.
    """

    server_option_ids: List[int]
    """
    Server option IDs of the new server.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str]
    """
    Project ID of the new server.
    """

    datacenter_name: Optional[str]
    """
    Datacenter name of the new server.
    """


@dataclass
class DeleteFailoverIPRequest:
    ip_id: int
    """
    ID of the failover IP to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteServerRequest:
    server_id: int
    """
    Server ID to delete.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DeleteServiceRequest:
    service_id: int
    """
    ID of the service.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DetachFailoverIPFromMacAddressRequest:
    ip_id: int
    """
    ID of the failover IP.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class DetachFailoverIPsRequest:
    fips_ids: List[int]
    """
    List of IDs of failovers IP to detach.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetBMCAccessRequest:
    server_id: int
    """
    ID of the server to get BMC access.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetFailoverIPRequest:
    ip_id: int
    """
    ID of the failover IP.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetIPv6BlockQuotasResponse:
    quotas: List[GetIPv6BlockQuotasResponseQuota]
    """
    Quota for each CIDR of IPv6 block.
    """

    total_count: int
    """
    Total count of quotas.
    """


@dataclass
class GetOSRequest:
    os_id: int
    """
    ID of the OS.
    """

    server_id: int
    """
    ID of the server.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str]
    """
    Project ID.
    """


@dataclass
class GetOfferRequest:
    offer_id: int
    """
    ID of offer.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str]
    """
    Project ID.
    """


@dataclass
class GetOrderedServiceRequest:
    ordered_service_id: int

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetRaidRequest:
    server_id: int
    """
    ID of the server.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetRemainingQuotaRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    project_id: Optional[str]
    """
    Project ID.
    """


@dataclass
class GetRemainingQuotaResponse:
    failover_ip_quota: int
    """
    Current failover IP quota.
    """

    failover_ip_remaining_quota: int
    """
    Remaining failover IP quota.
    """

    failover_block_quota: int
    """
    Current failover block quota.
    """

    failover_block_remaining_quota: int
    """
    Remaining failover block quota.
    """


@dataclass
class GetRescueRequest:
    server_id: int
    """
    ID of the server to get rescue.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetRpnStatusResponse:
    status: GetRpnStatusResponseStatus
    """
    If status = 'operational', you can perform rpn actions in write.
    """

    operations_left: Optional[int]
    """
    Number of operations left to perform before being operational.
    """


@dataclass
class GetServerBackupRequest:
    server_id: int
    """
    Server ID of the backup.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerDefaultPartitioningRequest:
    server_id: int
    """
    ID of the server.
    """

    os_id: int
    """
    OS ID of the default partitioning.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerInstallRequest:
    server_id: int
    """
    Server ID of the server to install.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServerRequest:
    server_id: int
    """
    ID of the server.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class GetServiceRequest:
    service_id: int
    """
    ID of the service.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class IPv6Block:
    id: int
    """
    ID of the IPv6.
    """

    address: str
    """
    Address of the IPv6.
    """

    duid: str
    """
    DUID of the IPv6.
    """

    nameservers: List[str]
    """
    DNS linked to the IPv6.
    """

    cidr: int
    """
    Classless InterDomain Routing notation of the IPv6.
    """

    subnets: List[IPv6Block]
    """
    All IPv6 subnets.
    """

    delegation_status: IPv6BlockDelegationStatus
    """
    The nameservers delegation status.
    """


@dataclass
class IPv6BlockApiCreateIPv6BlockRequest:
    project_id: Optional[str]
    """
    ID of the project.
    """


@dataclass
class IPv6BlockApiCreateIPv6BlockSubnetRequest:
    block_id: int
    """
    ID of the IPv6 block.
    """

    address: str
    """
    Address of the IPv6.
    """

    cidr: int
    """
    Classless InterDomain Routing notation of the IPv6.
    """


@dataclass
class IPv6BlockApiDeleteIPv6BlockRequest:
    block_id: int
    """
    ID of the IPv6 block to delete.
    """


@dataclass
class IPv6BlockApiGetIPv6BlockQuotasRequest:
    project_id: Optional[str]
    """
    ID of the project.
    """


@dataclass
class IPv6BlockApiGetIPv6BlockRequest:
    project_id: Optional[str]
    """
    ID of the project.
    """


@dataclass
class IPv6BlockApiListIPv6BlockSubnetsAvailableRequest:
    block_id: int
    """
    ID of the IPv6 block.
    """


@dataclass
class IPv6BlockApiUpdateIPv6BlockRequest:
    block_id: int
    """
    ID of the IPv6 block.
    """

    nameservers: Optional[List[str]]
    """
    DNS to link to the IPv6.
    """


@dataclass
class InstallServerRequest:
    server_id: int
    """
    Server ID to install.
    """

    os_id: int
    """
    OS ID to install on the server.
    """

    hostname: str
    """
    Hostname of the server.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    user_login: Optional[str]
    """
    User to install on the server.
    """

    user_password: Optional[str]
    """
    User password to install on the server.
    """

    panel_password: Optional[str]
    """
    Panel password to install on the server.
    """

    root_password: Optional[str]
    """
    Root password to install on the server.
    """

    partitions: Optional[List[InstallPartition]]
    """
    Partitions to install on the server.
    """

    ssh_key_ids: Optional[List[str]]
    """
    SSH key IDs authorized on the server.
    """

    license_offer_id: Optional[int]
    """
    Offer ID of license to install on server.
    """

    ip_id: Optional[int]
    """
    IP to link at the license to install on server.
    """


@dataclass
class Invoice:
    id: int

    status: InvoiceStatus

    payment_method: InvoicePaymentMethod

    content: str

    transaction_id: int

    total_with_taxes: Optional[Money]

    total_without_taxes: Optional[Money]

    created_at: Optional[datetime]

    paid_at: Optional[datetime]


@dataclass
class ListFailoverIPsRequest:
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
    Number of failovers IP per page.
    """

    order_by: Optional[ListFailoverIPsRequestOrderBy]
    """
    Order of the failovers IP.
    """

    project_id: Optional[str]
    """
    Filter failovers IP by project ID.
    """

    search: Optional[str]
    """
    Filter failovers IP which matching with this field.
    """

    only_available: Optional[bool]
    """
    True: return all failovers IP not attached on server
false: return all failovers IP attached on server.
    """


@dataclass
class ListFailoverIPsResponse:
    total_count: int
    """
    Total count of matching failovers IP.
    """

    failover_ips: List[FailoverIP]
    """
    List of failover IPs that match filters.
    """


@dataclass
class ListIPv6BlockSubnetsAvailableResponse:
    subnet_availables: List[ListIPv6BlockSubnetsAvailableResponseSubnet]
    """
    All available address and CIDR available in subnet.
    """

    total_count: int
    """
    Total count of available subnets.
    """


@dataclass
class ListInvoicesResponse:
    total_count: int

    invoices: List[InvoiceSummary]


@dataclass
class ListIpsResponse:
    total_count: int
    """
    Total count of authorized IPs.
    """

    ips: List[RpnSanIp]
    """
    List of authorized IPs.
    """


@dataclass
class ListOSRequest:
    server_id: int
    """
    Filter OS by compatible server ID.
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
    Number of OS per page.
    """

    order_by: Optional[ListOSRequestOrderBy]
    """
    Order of the OS.
    """

    type_: Optional[OSType]
    """
    Type of the OS.
    """

    project_id: Optional[str]
    """
    Project ID.
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
    Number of offer per page.
    """

    order_by: Optional[ListOffersRequestOrderBy]
    """
    Order of the offers.
    """

    commercial_range: Optional[str]
    """
    Filter on commercial range.
    """

    catalog: Optional[OfferCatalog]
    """
    Filter on catalog.
    """

    project_id: Optional[str]
    """
    Project ID.
    """

    is_failover_ip: Optional[bool]
    """
    Get the current failover IP offer.
    """

    is_failover_block: Optional[bool]
    """
    Get the current failover IP block offer.
    """

    sold_in: Optional[List[str]]
    """
    Filter offers depending on their datacenter.
    """

    available_only: Optional[bool]
    """
    Set this filter to true to only return available offers.
    """

    is_rpn_san: Optional[bool]
    """
    Get the RPN SAN offers.
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
class ListRefundsResponse:
    total_count: int

    refunds: List[RefundSummary]


@dataclass
class ListRpnCapableSanServersResponse:
    total_count: int
    """
    Total count of rpn capable san servers.
    """

    san_servers: List[RpnSanServer]
    """
    List of san servers.
    """


@dataclass
class ListRpnCapableServersResponse:
    total_count: int
    """
    Total count of rpn capable servers.
    """

    servers: List[Server]
    """
    List of servers.
    """


@dataclass
class ListRpnGroupMembersResponse:
    total_count: int
    """
    Total count of rpn v1 group members.
    """

    members: List[RpnGroupMember]
    """
    List of rpn v1 group members.
    """


@dataclass
class ListRpnGroupsResponse:
    total_count: int
    """
    Total count of rpn groups.
    """

    rpn_groups: List[RpnGroup]
    """
    List of rpn v1 groups.
    """


@dataclass
class ListRpnInvitesResponse:
    total_count: int
    """
    Total count of invites.
    """

    members: List[RpnGroupMember]
    """
    List of invites.
    """


@dataclass
class ListRpnSansResponse:
    total_count: int
    """
    Total count of matching RPN SANs.
    """

    rpn_sans: List[RpnSanSummary]
    """
    List of RPN SANs that match filters.
    """


@dataclass
class ListRpnServerCapabilitiesResponse:
    total_count: int
    """
    Total count of servers.
    """

    servers: List[RpnServerCapability]
    """
    List of servers and their RPN capabilities.
    """


@dataclass
class ListRpnV2CapableResourcesResponse:
    total_count: int
    """
    Total count of matching rpn v2 capable resources.
    """

    servers: List[Server]
    """
    List of rpn v2 capable resources that match filters.
    """


@dataclass
class ListRpnV2GroupLogsResponse:
    total_count: int
    """
    Total count of matching rpn v2 logs.
    """

    logs: List[Log]
    """
    List of rpn v2 logs that match filters.
    """


@dataclass
class ListRpnV2GroupsResponse:
    total_count: int
    """
    Total count of matching rpn v2 groups.
    """

    rpn_groups: List[RpnV2Group]
    """
    List of rpn v2 groups that match filters.
    """


@dataclass
class ListRpnV2MembersResponse:
    total_count: int
    """
    Total count of matching rpn v2 group members.
    """

    members: List[RpnV2Member]
    """
    List of rpn v2 group members that match filters.
    """


@dataclass
class ListServerDisksRequest:
    server_id: int
    """
    Server ID of the server disks.
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
    Number of server disk per page.
    """

    order_by: Optional[ListServerDisksRequestOrderBy]
    """
    Order of the server disks.
    """


@dataclass
class ListServerDisksResponse:
    total_count: int
    """
    Total count of matching server disks.
    """

    disks: List[ServerDisk]
    """
    Server disks that match filters.
    """


@dataclass
class ListServerEventsRequest:
    server_id: int
    """
    Server ID of the server events.
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
    Number of server event per page.
    """

    order_by: Optional[ListServerEventsRequestOrderBy]
    """
    Order of the server events.
    """


@dataclass
class ListServerEventsResponse:
    total_count: int
    """
    Total count of matching server events.
    """

    events: List[ServerEvent]
    """
    Server events that match filters.
    """


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
    Number of server per page.
    """

    order_by: Optional[ListServersRequestOrderBy]
    """
    Order of the servers.
    """

    project_id: Optional[str]
    """
    Filter servers by project ID.
    """

    search: Optional[str]
    """
    Filter servers by hostname.
    """


@dataclass
class ListServersResponse:
    total_count: int
    """
    Total count of matching servers.
    """

    servers: List[ServerSummary]
    """
    Servers that match filters.
    """


@dataclass
class ListServicesRequest:
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
    Number of service per page.
    """

    order_by: Optional[ListServicesRequestOrderBy]
    """
    Order of the services.
    """

    project_id: Optional[str]
    """
    Project ID.
    """


@dataclass
class ListServicesResponse:
    total_count: int
    """
    Total count of matching services.
    """

    services: List[Service]
    """
    Services that match filters.
    """


@dataclass
class ListSubscribableServerOptionsRequest:
    server_id: int
    """
    Server ID of the subscribable server options.
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
    Number of subscribable server option per page.
    """


@dataclass
class ListSubscribableServerOptionsResponse:
    total_count: int
    """
    Total count of matching subscribable server options.
    """

    server_options: List[Offer]
    """
    Server options that match filters.
    """


@dataclass
class OfferFailoverBlockInfo:
    onetime_fees: Optional[Offer]


@dataclass
class OfferFailoverIpInfo:
    onetime_fees: Optional[Offer]


@dataclass
class OfferServerInfo:
    bandwidth: int

    stock: OfferServerInfoStock

    commercial_range: str

    disks: List[Disk]

    cpus: List[CPU]

    memories: List[Memory]

    persistent_memories: List[PersistentMemory]

    raid_controllers: List[RaidController]

    available_options: List[Offer]

    connectivity: int

    stock_by_datacenter: Dict[str, OfferServerInfoStock]

    rpn_version: Optional[int]

    onetime_fees: Optional[Offer]


@dataclass
class OfferServiceLevelInfo:
    support_ticket: bool

    support_phone: bool

    sales_support: bool

    git: str

    sla: float

    priority_support: bool

    high_rpn_bandwidth: bool

    customization: bool

    antidos: bool

    extra_failover_quota: int

    available_options: List[Offer]


@dataclass
class Raid:
    raid_arrays: List[RaidArray]
    """
    Details about the RAID controller.
    """


@dataclass
class RebootServerRequest:
    server_id: int
    """
    Server ID to reboot.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class Refund:
    id: int

    status: RefundStatus

    method: RefundMethod

    content: str

    total_with_taxes: Optional[Money]

    total_without_taxes: Optional[Money]

    created_at: Optional[datetime]

    refunded_at: Optional[datetime]


@dataclass
class Rescue:
    os_id: int
    """
    OS ID of the rescue.
    """

    login: str
    """
    Login of the rescue.
    """

    password: str
    """
    Password of the rescue.
    """

    protocol: RescueProtocol
    """
    Protocol of the resuce.
    """


@dataclass
class RpnApiGetRpnStatusRequest:
    project_id: Optional[str]
    """
    A project ID.
    """

    rpnv1_group_id: Optional[int]
    """
    An RPN v1 group ID.
    """

    rpnv2_group_id: Optional[int]
    """
    An RPN v2 group ID.
    """


@dataclass
class RpnApiListRpnServerCapabilitiesRequest:
    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of servers per page.
    """

    order_by: Optional[ListRpnServerCapabilitiesRequestOrderBy]
    """
    Order of the servers.
    """

    project_id: Optional[str]
    """
    Filter servers by project ID.
    """


@dataclass
class RpnSanApiAddIpRequest:
    rpn_san_id: int
    """
    RPN SAN ID.
    """

    ip_ids: List[int]
    """
    An array of IP ID.
    """


@dataclass
class RpnSanApiCreateRpnSanRequest:
    offer_id: int
    """
    Offer ID.
    """

    project_id: Optional[str]
    """
    Your project ID.
    """


@dataclass
class RpnSanApiDeleteRpnSanRequest:
    rpn_san_id: int
    """
    RPN SAN ID.
    """


@dataclass
class RpnSanApiGetRpnSanRequest:
    rpn_san_id: int
    """
    RPN SAN ID.
    """


@dataclass
class RpnSanApiListAvailableIpsRequest:
    rpn_san_id: int
    """
    RPN SAN ID.
    """

    type_: Optional[RpnSanIpType]
    """
    Filter by IP type (server | rpnv2_subnet).
    """


@dataclass
class RpnSanApiListIpsRequest:
    rpn_san_id: int
    """
    RPN SAN ID.
    """

    type_: Optional[RpnSanIpType]
    """
    Filter by IP type (server | rpnv2_subnet).
    """


@dataclass
class RpnSanApiListRpnSansRequest:
    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of RPN SANs per page.
    """

    order_by: Optional[ListRpnSansRequestOrderBy]
    """
    Order of the RPN SANs.
    """

    project_id: Optional[str]
    """
    Filter RPN SANs by project ID.
    """


@dataclass
class RpnSanApiRemoveIpRequest:
    rpn_san_id: int
    """
    RPN SAN ID.
    """

    ip_ids: List[int]
    """
    An array of IP ID.
    """


@dataclass
class RpnV1ApiAcceptRpnInviteRequest:
    member_id: int
    """
    The member ID.
    """


@dataclass
class RpnV1ApiAddRpnGroupMembersRequest:
    group_id: int
    """
    The rpn v1 group ID.
    """

    server_ids: Optional[List[int]]
    """
    A collection of rpn v1 capable server IDs.
    """

    san_server_ids: Optional[List[int]]
    """
    A collection of rpn v1 capable RPN SAN server IDs.
    """


@dataclass
class RpnV1ApiCreateRpnGroupRequest:
    name: str
    """
    Rpn v1 group name.
    """

    server_ids: Optional[List[int]]
    """
    A collection of rpn v1 capable servers.
    """

    san_server_ids: Optional[List[int]]
    """
    A collection of rpn v1 capable rpn sans servers.
    """

    project_id: Optional[str]
    """
    A project ID.
    """


@dataclass
class RpnV1ApiDeleteRpnGroupMembersRequest:
    group_id: int
    """
    The rpn v1 group ID.
    """

    member_ids: List[int]
    """
    A collection of rpn v1 group members IDs.
    """


@dataclass
class RpnV1ApiDeleteRpnGroupRequest:
    group_id: int
    """
    Rpn v1 group ID.
    """


@dataclass
class RpnV1ApiGetRpnGroupRequest:
    group_id: int
    """
    Rpn v1 group ID.
    """


@dataclass
class RpnV1ApiLeaveRpnGroupRequest:
    group_id: int
    """
    The RPN V1 group ID.
    """

    member_ids: List[int]
    """
    A collection of rpn v1 group members IDs.
    """

    project_id: Optional[str]
    """
    A project ID.
    """


@dataclass
class RpnV1ApiListRpnCapableSanServersRequest:
    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of rpn capable resources per page.
    """

    order_by: Optional[ListRpnCapableSanServersRequestOrderBy]
    """
    Order of the rpn capable resources.
    """

    project_id: Optional[str]
    """
    Filter rpn capable resources by project ID.
    """


@dataclass
class RpnV1ApiListRpnCapableServersRequest:
    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of rpn capable resources per page.
    """

    order_by: Optional[ListRpnCapableServersRequestOrderBy]
    """
    Order of the rpn capable resources.
    """

    project_id: Optional[str]
    """
    Filter rpn capable resources by project ID.
    """


@dataclass
class RpnV1ApiListRpnGroupMembersRequest:
    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of rpn v1 group members per page.
    """

    order_by: Optional[ListRpnGroupMembersRequestOrderBy]
    """
    Order of the rpn v1 group members.
    """

    group_id: int
    """
    Filter rpn v1 group members by group ID.
    """

    project_id: Optional[str]
    """
    A project ID.
    """


@dataclass
class RpnV1ApiListRpnGroupsRequest:
    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of rpn v1 groups per page.
    """

    order_by: Optional[ListRpnGroupsRequestOrderBy]
    """
    Order of the rpn v1 groups.
    """

    project_id: Optional[str]
    """
    Filter rpn v1 groups by project ID.
    """


@dataclass
class RpnV1ApiListRpnInvitesRequest:
    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of rpn capable resources per page.
    """

    order_by: Optional[ListRpnInvitesRequestOrderBy]
    """
    Order of the rpn capable resources.
    """

    project_id: Optional[str]
    """
    Filter rpn capable resources by project ID.
    """


@dataclass
class RpnV1ApiRefuseRpnInviteRequest:
    member_id: int
    """
    The member ID.
    """


@dataclass
class RpnV1ApiRpnGroupInviteRequest:
    group_id: int
    """
    The RPN V1 group ID.
    """

    server_ids: List[int]
    """
    A collection of external server IDs.
    """

    project_id: Optional[str]
    """
    A project ID.
    """


@dataclass
class RpnV1ApiUpdateRpnGroupNameRequest:
    group_id: int
    """
    Rpn v1 group ID.
    """

    name: Optional[str]
    """
    New rpn v1 group name.
    """


@dataclass
class RpnV2ApiAddRpnV2MembersRequest:
    group_id: int
    """
    RPN V2 group ID.
    """

    servers: List[int]
    """
    A collection of server IDs.
    """


@dataclass
class RpnV2ApiCreateRpnV2GroupRequest:
    name: str
    """
    RPN V2 group name.
    """

    servers: List[int]
    """
    A collection of server IDs.
    """

    project_id: Optional[str]
    """
    Project ID of the RPN V2 group.
    """

    type_: Optional[RpnV2GroupType]
    """
    RPN V2 group type (qing / standard).
    """


@dataclass
class RpnV2ApiDeleteRpnV2GroupRequest:
    group_id: int
    """
    RPN V2 group ID.
    """


@dataclass
class RpnV2ApiDeleteRpnV2MembersRequest:
    group_id: int
    """
    RPN V2 group ID.
    """

    member_ids: List[int]
    """
    A collection of member IDs.
    """


@dataclass
class RpnV2ApiDisableRpnV2GroupCompatibilityRequest:
    group_id: int
    """
    RPN V2 group ID.
    """


@dataclass
class RpnV2ApiEnableRpnV2GroupCompatibilityRequest:
    group_id: int
    """
    RPN V2 group ID.
    """

    rpnv1_group_id: int
    """
    RPN V1 group ID.
    """


@dataclass
class RpnV2ApiGetRpnV2GroupRequest:
    group_id: int
    """
    RPN V2 group ID.
    """


@dataclass
class RpnV2ApiListRpnV2CapableResourcesRequest:
    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of rpn v2 capable resources per page.
    """

    order_by: Optional[ListRpnV2CapableResourcesRequestOrderBy]
    """
    Order of the rpn v2 capable resources.
    """

    project_id: Optional[str]
    """
    Filter rpn v2 capable resources by project ID.
    """


@dataclass
class RpnV2ApiListRpnV2GroupLogsRequest:
    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of rpn v2 group logs per page.
    """

    order_by: Optional[ListRpnV2GroupLogsRequestOrderBy]
    """
    Order of the rpn v2 group logs.
    """

    group_id: int
    """
    RPN V2 group ID.
    """


@dataclass
class RpnV2ApiListRpnV2GroupsRequest:
    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of rpn v2 groups per page.
    """

    order_by: Optional[ListRpnV2GroupsRequestOrderBy]
    """
    Order of the rpn v2 groups.
    """

    project_id: Optional[str]
    """
    Filter rpn v2 groups by project ID.
    """


@dataclass
class RpnV2ApiListRpnV2MembersRequest:
    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Number of rpn v2 group members per page.
    """

    order_by: Optional[ListRpnV2MembersRequestOrderBy]
    """
    Order of the rpn v2 group members.
    """

    group_id: int
    """
    RPN V2 group ID.
    """

    type_: Optional[ListRpnV2MembersRequestType]
    """
    Filter members by type.
    """


@dataclass
class RpnV2ApiUpdateRpnV2GroupNameRequest:
    group_id: int
    """
    RPN V2 group ID.
    """

    name: Optional[str]
    """
    RPN V2 group name.
    """


@dataclass
class RpnV2ApiUpdateRpnV2VlanForMembersRequest:
    group_id: int
    """
    RPN V2 group ID.
    """

    member_ids: List[int]
    """
    RPN V2 member IDs.
    """

    vlan: Optional[int]
    """
    Min: 0.
Max: 3967.
    """


@dataclass
class ServerDefaultPartitioning:
    partitions: List[Partition]
    """
    Default partitions.
    """


@dataclass
class ServerInstall:
    os_id: int

    hostname: str

    partitions: List[Partition]

    ssh_key_ids: List[str]

    status: ServerInstallStatus

    user_login: Optional[str]

    panel_url: Optional[str]


@dataclass
class StartBMCAccessRequest:
    server_id: int
    """
    ID of the server to start the BMC access.
    """

    ip: str
    """
    The IP authorized to connect to the given server.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class StartRescueRequest:
    server_id: int
    """
    ID of the server to start rescue.
    """

    os_id: int
    """
    OS ID to use to start rescue.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class StartServerRequest:
    server_id: int
    """
    Server ID to start.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class StopBMCAccessRequest:
    server_id: int
    """
    ID of the server to stop BMC access.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class StopRescueRequest:
    server_id: int
    """
    ID of the server to stop rescue.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class StopServerRequest:
    server_id: int
    """
    Server ID to stop.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SubscribeServerOptionRequest:
    server_id: int
    """
    Server ID to subscribe server option.
    """

    option_id: int
    """
    Option ID to subscribe.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SubscribeStorageOptionsRequest:
    server_id: int
    """
    Server ID of the storage options to subscribe.
    """

    options_ids: List[int]
    """
    Option IDs of the storage options to subscribe.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class SubscribeStorageOptionsResponse:
    services: List[Service]
    """
    Services subscribe storage options.
    """


@dataclass
class UpdateRaidRequest:
    server_id: int
    """
    ID of the server.
    """

    raid_arrays: List[UpdatableRaidArray]
    """
    RAIDs to update.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class UpdateReverseRequest:
    ip_id: int
    """
    ID of the IP.
    """

    reverse: str
    """
    Reverse to apply on the IP.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class UpdateServerBackupRequest:
    server_id: int
    """
    Server ID to update backup.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    password: Optional[str]
    """
    Password of the server backup.
    """

    autologin: Optional[bool]
    """
    Autologin of the server backup.
    """

    acl_enabled: Optional[bool]
    """
    Boolean to enable or disable ACL.
    """


@dataclass
class UpdateServerRequest:
    server_id: int
    """
    Server ID to update.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    hostname: Optional[str]
    """
    Hostname of the server to update.
    """

    enable_ipv6: Optional[bool]
    """
    Flag to enable or not the IPv6 of server.
    """


@dataclass
class UpdateServerTagsRequest:
    server_id: int
    """
    Server ID to update the tags.
    """

    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    tags: Optional[List[str]]
    """
    Tags of server to update.
    """
