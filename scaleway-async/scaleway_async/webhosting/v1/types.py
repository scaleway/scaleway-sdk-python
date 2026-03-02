# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
)
from scaleway_core.utils import (
    StrEnumMeta,
)

from ...std.types import (
    LanguageCode as StdLanguageCode,
)


class BackupItemType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_BACKUP_ITEM_TYPE = "unknown_backup_item_type"
    FULL = "full"
    WEB = "web"
    MAIL = "mail"
    DB = "db"
    DB_USER = "db_user"
    FTP_USER = "ftp_user"
    DNS_ZONE = "dns_zone"
    CRON_JOB = "cron_job"
    SSL_CERTIFICATE = "ssl_certificate"

    def __str__(self) -> str:
        return str(self.value)


class BackupStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_BACKUP_STATUS = "unknown_backup_status"
    ACTIVE = "active"
    LOCKED = "locked"
    DISABLED = "disabled"
    DAMAGED = "damaged"
    RESTORING = "restoring"

    def __str__(self) -> str:
        return str(self.value)


class CheckFreeDomainAvailabilityResponseUnavailableReason(
    str, Enum, metaclass=StrEnumMeta
):
    UNAVAILABLE_REASON_UNKNOWN = "unavailable_reason_unknown"
    UNAVAILABLE_REASON_ALREADY_USED = "unavailable_reason_already_used"
    UNAVAILABLE_REASON_TOO_SHORT = "unavailable_reason_too_short"
    UNAVAILABLE_REASON_TOO_LONG = "unavailable_reason_too_long"
    UNAVAILABLE_REASON_INVALID_CHARACTERS = "unavailable_reason_invalid_characters"
    UNAVAILABLE_REASON_STARTS_OR_ENDS_WITH_HYPHEN = (
        "unavailable_reason_starts_or_ends_with_hyphen"
    )
    UNAVAILABLE_REASON_CONTAINS_DOTS = "unavailable_reason_contains_dots"
    UNAVAILABLE_REASON_CONTAINS_RESERVED_KEYWORD = (
        "unavailable_reason_contains_reserved_keyword"
    )

    def __str__(self) -> str:
        return str(self.value)


class DnsRecordStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    VALID = "valid"
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)


class DnsRecordType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    A = "a"
    CNAME = "cname"
    MX = "mx"
    TXT = "txt"
    NS = "ns"
    AAAA = "aaaa"

    def __str__(self) -> str:
        return str(self.value)


class DnsRecordsStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    VALID = "valid"
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)


class DomainAction(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ACTION = "unknown_action"
    TRANSFER = "transfer"
    MANAGE_EXTERNAL = "manage_external"
    RENEW = "renew"

    def __str__(self) -> str:
        return str(self.value)


class DomainAvailabilityAction(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ACTION = "unknown_action"
    REGISTER = "register"
    TRANSFER = "transfer"
    MANAGE_EXTERNAL = "manage_external"

    def __str__(self) -> str:
        return str(self.value)


class DomainAvailabilityStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    AVAILABLE = "available"
    NOT_AVAILABLE = "not_available"
    OWNED = "owned"
    VALIDATING = "validating"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class DomainDnsAction(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_DNS_ACTION = "unknown_dns_action"
    AUTO_CONFIG_ALL_RECORDS = "auto_config_all_records"
    AUTO_CONFIG_WEB_RECORDS = "auto_config_web_records"
    AUTO_CONFIG_MAIL_RECORDS = "auto_config_mail_records"
    AUTO_CONFIG_NAMESERVERS = "auto_config_nameservers"
    AUTO_CONFIG_NONE = "auto_config_none"

    def __str__(self) -> str:
        return str(self.value)


class DomainStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    VALID = "valid"
    INVALID = "invalid"
    VALIDATING = "validating"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class DomainZoneOwner(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ZONE_OWNER = "unknown_zone_owner"
    EXTERNAL = "external"
    SCALEWAY = "scaleway"
    ONLINE = "online"
    WEBHOSTING = "webhosting"

    def __str__(self) -> str:
        return str(self.value)


class HostingStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    DELIVERING = "delivering"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"
    MIGRATING = "migrating"
    UPDATING = "updating"

    def __str__(self) -> str:
        return str(self.value)


class ListBackupsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListDatabaseUsersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    USERNAME_ASC = "username_asc"
    USERNAME_DESC = "username_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListDatabasesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    DATABASE_NAME_ASC = "database_name_asc"
    DATABASE_NAME_DESC = "database_name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListFtpAccountsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    USERNAME_ASC = "username_asc"
    USERNAME_DESC = "username_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListHostingsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListMailAccountsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    USERNAME_ASC = "username_asc"
    USERNAME_DESC = "username_desc"
    DOMAIN_ASC = "domain_asc"
    DOMAIN_DESC = "domain_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListOffersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    PRICE_ASC = "price_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListWebsitesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    DOMAIN_ASC = "domain_asc"
    DOMAIN_DESC = "domain_desc"

    def __str__(self) -> str:
        return str(self.value)


class NameserverStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    VALID = "valid"
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)


class OfferOptionName(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_NAME = "unknown_name"
    DOMAIN_COUNT = "domain_count"
    EMAIL_COUNT = "email_count"
    STORAGE_GB = "storage_gb"
    VCPU_COUNT = "vcpu_count"
    RAM_GB = "ram_gb"
    BACKUP = "backup"
    DEDICATED_IP = "dedicated_ip"
    EMAIL_STORAGE_GB = "email_storage_gb"
    DATABASE_COUNT = "database_count"
    SUPPORT = "support"
    ADDITIONAL_EMAIL = "additional_email"

    def __str__(self) -> str:
        return str(self.value)


class OfferOptionWarning(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_WARNING = "unknown_warning"
    QUOTA_EXCEEDED_WARNING = "quota_exceeded_warning"
    USAGE_LOW_WARNING = "usage_low_warning"

    def __str__(self) -> str:
        return str(self.value)


class PlatformPlatformGroup(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_GROUP = "unknown_group"
    DEFAULT = "default"
    PREMIUM = "premium"

    def __str__(self) -> str:
        return str(self.value)


class ProgressStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    PARTIALLY_COMPLETED = "partially_completed"
    FAILED = "failed"
    ABORTED = "aborted"
    NEVER_FINISHED = "never_finished"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class AutoConfigDomainDns:
    nameservers: bool
    """
    Whether or not to synchronize domain nameservers.
    """

    web_records: bool
    """
    Whether or not to synchronize web records.
    """

    mail_records: bool
    """
    Whether or not to synchronize mail records.
    """

    all_records: bool
    """
    Whether or not to synchronize all types of records. Takes priority over the other fields.
    """

    none: bool
    """
    No automatic domain configuration. Users must configure their domain for the Web Hosting to work.
    """


@dataclass
class PlatformControlPanelUrls:
    dashboard: str
    """
    URL to connect to the hosting control panel dashboard.
    """

    webmail: str
    """
    URL to connect to the hosting Webmail interface.
    """


@dataclass
class HostingDomainCustomDomain:
    domain: str
    """
    Custom domain linked to the hosting plan.
    """

    domain_status: DomainStatus
    """
    Status of the custom domain verification.
    """

    dns_status: DnsRecordsStatus
    """
    Status of the DNS configuration for the custom domain.
    """

    auto_config_domain_dns: Optional[AutoConfigDomainDns] = None
    """
    Indicates whether to auto-configure DNS for this domain.
    """


@dataclass
class ControlPanel:
    name: str
    """
    Control panel name.
    """

    available: bool
    """
    Define if the control panel type is available to order.
    """

    logo_url: str
    """
    URL of the control panel's logo.
    """

    available_languages: list[StdLanguageCode]
    """
    List of available languages for the control panel.
    """


@dataclass
class OfferOption:
    id: str
    """
    Option ID.
    """

    name: OfferOptionName
    """
    Name of the option.
    """

    billing_operation_path: str
    """
    Unique identifier used for billing.
    """

    min_value: int
    """
    Minimum value for the option in the offer.
    """

    current_value: int
    """
    If a hosting_id was specified in the call, defines the current value of the option in the hosting.
    """

    max_value: int
    """
    Maximum value for the option in the offer.
    """

    quota_warning: OfferOptionWarning
    """
    Defines a warning if the maximum value for the option has been reached.
    """

    price: Optional[Money] = None
    """
    Price of the option for 1 value.
    """


@dataclass
class PlatformControlPanel:
    name: str
    """
    Name of the control panel.
    """

    urls: Optional[PlatformControlPanelUrls] = None
    """
    URL to connect to control panel dashboard and to Webmail interface.
    """


@dataclass
class BackupItem:
    id: str
    """
    ID of the item.
    """

    name: str
    """
    Name of the item (e.g., `database name`, `email address`).
    """

    type_: BackupItemType
    """
    Type of the item (e.g., email, database, FTP).
    """

    size: int
    """
    Size of the item in bytes.
    """

    status: BackupStatus
    """
    Status of the item. Available values are `active`, `damaged`, and `restoring`.
    """

    created_at: Optional[datetime] = None
    """
    Date and time at which this item was backed up.
    """


@dataclass
class HostingDomain:
    subdomain: str
    """
    Optional free subdomain linked to the Web Hosting plan.
    """

    custom_domain: Optional[HostingDomainCustomDomain] = None
    """
    Optional custom domain linked to the Web Hosting plan.
    """


@dataclass
class FreeDomain:
    slug: str
    """
    Custom prefix used for the free domain.
    """

    root_domain: str
    """
    Free root domain provided by Web Hosting, selected from the list returned by `ListFreeRootDomains`.
    """


@dataclass
class CreateDatabaseRequestUser:
    username: str
    password: str


@dataclass
class CreateHostingRequestDomainConfiguration:
    update_nameservers: bool
    update_web_record: bool
    update_mail_record: bool
    update_all_records: bool


@dataclass
class OfferOptionRequest:
    id: str
    """
    Offer option ID.
    """

    quantity: int
    """
    The option requested quantity to set for the Web Hosting plan.
    """


@dataclass
class SyncDomainDnsRecordsRequestRecord:
    name: str
    type_: DnsRecordType


@dataclass
class DnsRecord:
    name: str
    """
    Record name.
    """

    type_: DnsRecordType
    """
    Record type.
    """

    ttl: int
    """
    Record time-to-live.
    """

    value: str
    """
    Record value.
    """

    status: DnsRecordStatus
    """
    Record status.
    """

    raw_data: str
    """
    Record representation as it appears in the zone file or DNS management system.
    """

    priority: Optional[int] = 0
    """
    Record priority level.
    """


@dataclass
class Nameserver:
    hostname: str
    """
    Hostname of the nameserver.
    """

    status: NameserverStatus
    """
    Status of the nameserver.
    """

    is_default: bool
    """
    Defines whether the nameserver is the default one.
    """


@dataclass
class HostingUser:
    username: str
    """
    Main Web Hosting control panel username.
    """

    contact_email: str
    """
    Contact email used for the hosting.
    """

    one_time_password: Optional[str] = None
    """
    One-time-password used for the first login to the control panel, cleared after first use (deprecated, use password_b64 instead).
    """

    one_time_password_b64: Optional[str] = None
    """
    One-time-password used for the first login to the control panel, cleared after first use, encoded in base64.
    """


@dataclass
class Offer:
    id: str
    """
    Offer ID.
    """

    name: str
    """
    Offer name.
    """

    billing_operation_path: str
    """
    Unique identifier used for billing.
    """

    options: list[OfferOption]
    """
    Options available for the offer.
    """

    available: bool
    """
    If a hosting_id was specified in the call, defines whether the offer is available for a specified hosting plan to migrate (update) to.
    """

    control_panel_name: str
    """
    Name of the control panel.
    """

    end_of_life: bool
    """
    Indicates if the offer has reached its end of life.
    """

    quota_warning: OfferOptionWarning
    """
    Defines a warning if the maximum value for an option in the offer is exceeded.
    """

    control_panels: list[ControlPanel]
    """
    Lists available control panels for the specified offer.
    """

    region: ScwRegion
    """
    Region where the offer is hosted.
    """

    price: Optional[Money] = None
    """
    Price of the offer.
    """


@dataclass
class Platform:
    hostname: str
    """
    Hostname of the host platform.
    """

    number: int
    """
    Number of the host platform.
    """

    group_name: PlatformPlatformGroup
    """
    Group name of the hosting's host platform.
    """

    ipv4: str
    """
    IPv4 address of the hosting's host platform.
    """

    ipv6: str
    """
    IPv6 address of the hosting's host platform.
    """

    control_panel: Optional[PlatformControlPanel] = None
    """
    Details of the platform control panel.
    """


@dataclass
class BackupItemGroup:
    type_: BackupItemType
    """
    Type of items (e.g., email, database, FTP).
    """

    items: list[BackupItem]
    """
    List of individual backup items of this type.
    """


@dataclass
class Backup:
    id: str
    """
    ID of the backup.
    """

    size: int
    """
    Total size of the backup in bytes.
    """

    status: BackupStatus
    """
    Status of the backup. Available values are `active`, `locked`, and `restoring`.
    """

    total_items: int
    """
    Total number of restorable items in the backup.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the backup.
    """


@dataclass
class DatabaseUser:
    username: str
    """
    Name of the database user.
    """

    databases: list[str]
    """
    List of databases accessible by the user.
    """


@dataclass
class Database:
    database_name: str
    """
    Name of the database.
    """

    users: list[str]
    """
    List of users who have access to the database.
    """


@dataclass
class FtpAccount:
    username: str
    """
    The username of the FTP account.
    """

    path: str
    """
    The path associated with the FTP account.
    """


@dataclass
class HostingSummary:
    id: str
    """
    ID of the Web Hosting plan.
    """

    project_id: str
    """
    ID of the Scaleway Project the Web Hosting plan belongs to.
    """

    status: HostingStatus
    """
    Status of the Web Hosting plan.
    """

    domain: str
    """
    Main domain associated with the Web Hosting plan (deprecated, use domain_info).
    """

    protected: bool
    """
    Whether the hosting is protected or not.
    """

    dns_status: DnsRecordsStatus
    """
    DNS status of the Web Hosting plan.
    """

    offer_name: str
    """
    Name of the active offer for the Web Hosting plan.
    """

    domain_status: DomainStatus
    """
    Main domain status of the Web Hosting plan.
    """

    region: ScwRegion
    """
    Region where the Web Hosting plan is hosted.
    """

    created_at: Optional[datetime] = None
    """
    Date on which the Web Hosting plan was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date on which the Web Hosting plan was last updated.
    """

    domain_info: Optional[HostingDomain] = None
    """
    Domain configuration block (subdomain, optional custom domain, and DNS settings).
    """


@dataclass
class MailAccount:
    domain: str
    """
    Domain part of the mail account address.
    """

    username: str
    """
    Username part address of the mail account address.
    """


@dataclass
class ProgressSummary:
    id: str
    """
    ID of the progress.
    """

    backup_items_count: int
    """
    Total number of backup items included in the progress.
    """

    percentage: int
    """
    Completion percentage of the progress.
    """

    status: ProgressStatus
    """
    Current status of the progress operation.
    """


@dataclass
class Website:
    domain: str
    """
    The domain of the website.
    """

    path: str
    """
    The directory path of the website.
    """

    ssl_status: bool
    """
    The SSL status of the website.
    """


@dataclass
class DomainAvailability:
    name: str
    """
    Fully qualified domain name (FQDN).
    """

    zone_name: str
    """
    DNS zone associated with the domain.
    """

    status: DomainAvailabilityStatus
    """
    Availability status of the domain.
    """

    available_actions: list[DomainAvailabilityAction]
    """
    A list of actions that can be performed on the domain.
    """

    can_create_hosting: bool
    """
    Whether a hosting can be created for this domain.
    """

    price: Optional[Money] = None
    """
    Price for registering the domain.
    """


@dataclass
class BackupApiGetBackupRequest:
    hosting_id: str
    """
    UUID of the hosting account.
    """

    backup_id: str
    """
    ID of the backup to retrieve.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class BackupApiGetProgressRequest:
    hosting_id: str
    """
    ID of the hosting associated with the progress.
    """

    progress_id: str
    """
    ID of the progress to retrieve.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class BackupApiListBackupItemsRequest:
    hosting_id: str
    """
    UUID of the hosting account.
    """

    backup_id: str
    """
    ID of the backup to list items from.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class BackupApiListBackupsRequest:
    hosting_id: str
    """
    UUID of the hosting account.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number to retrieve.
    """

    page_size: Optional[int] = 0
    """
    Number of backups to return per page.
    """

    order_by: Optional[ListBackupsRequestOrderBy] = (
        ListBackupsRequestOrderBy.CREATED_AT_DESC
    )
    """
    Order in which to return the list of backups.
    """


@dataclass
class BackupApiListRecentProgressesRequest:
    hosting_id: str
    """
    ID of the hosting linked to the progress.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class BackupApiRestoreBackupItemsRequest:
    hosting_id: str
    """
    UUID of the hosting account.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    item_ids: Optional[list[str]] = field(default_factory=list)
    """
    List of backup item IDs to restore individually.
    """


@dataclass
class BackupApiRestoreBackupRequest:
    hosting_id: str
    """
    UUID of the hosting account.
    """

    backup_id: str
    """
    ID of the backup to fully restore.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class CheckFreeDomainAvailabilityResponse:
    is_available: bool
    """
    Whether the free domain is available.
    """

    free_domain: Optional[FreeDomain] = None
    """
    The free domain that was checked.
    """

    reason: Optional[CheckFreeDomainAvailabilityResponseUnavailableReason] = (
        CheckFreeDomainAvailabilityResponseUnavailableReason.UNAVAILABLE_REASON_UNKNOWN
    )
    """
    Reason the domain is unavailable, if applicable.
    """


@dataclass
class CheckUserOwnsDomainResponse:
    owns_domain: bool
    """
    Indicates whether the specified project owns the domain.
    """


@dataclass
class ControlPanelApiListControlPanelsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number (must be a positive integer).
    """

    page_size: Optional[int] = 0
    """
    Number of control panels to return (must be a positive integer lower or equal to 100).
    """


@dataclass
class DatabaseApiAssignDatabaseUserRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    username: str
    """
    Name of the user to assign.
    """

    database_name: str
    """
    Name of the database to be assigned.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DatabaseApiChangeDatabaseUserPasswordRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    username: str
    """
    Name of the user to update.
    """

    password: str
    """
    New password.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DatabaseApiCreateDatabaseRequest:
    hosting_id: str
    """
    UUID of the hosting plan where the database will be created.
    """

    database_name: str
    """
    Name of the database to be created.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    new_user: Optional[CreateDatabaseRequestUser] = None

    existing_username: Optional[str] = None


@dataclass
class DatabaseApiCreateDatabaseUserRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    username: str
    """
    Name of the user to create.
    """

    password: str
    """
    Password of the user to create.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DatabaseApiDeleteDatabaseRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    database_name: str
    """
    Name of the database to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DatabaseApiDeleteDatabaseUserRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    username: str
    """
    Name of the database user to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DatabaseApiGetDatabaseRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    database_name: str
    """
    Name of the database.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DatabaseApiGetDatabaseUserRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    username: str
    """
    Name of the database user to retrieve details.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DatabaseApiListDatabaseUsersRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number (must be a positive integer).
    """

    page_size: Optional[int] = 0
    """
    Number of database users to return (must be a positive integer lower or equal to 100).
    """

    order_by: Optional[ListDatabaseUsersRequestOrderBy] = (
        ListDatabaseUsersRequestOrderBy.USERNAME_ASC
    )
    """
    Sort order of database users in the response.
    """


@dataclass
class DatabaseApiListDatabasesRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number (must be a positive integer).
    """

    page_size: Optional[int] = 0
    """
    Number of databases to return (must be a positive integer lower or equal to 100).
    """

    order_by: Optional[ListDatabasesRequestOrderBy] = (
        ListDatabasesRequestOrderBy.DATABASE_NAME_ASC
    )
    """
    Sort order of databases in the response.
    """


@dataclass
class DatabaseApiUnassignDatabaseUserRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    username: str
    """
    Name of the user to unassign.
    """

    database_name: str
    """
    Name of the database to be unassigned.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DnsApiCheckUserOwnsDomainRequest:
    domain: str
    """
    Domain for which ownership is to be verified.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the project currently in use.
    """


@dataclass
class DnsApiGetDomainDnsRecordsRequest:
    domain: str
    """
    Domain associated with the DNS records.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DnsApiGetDomainRequest:
    domain_name: str
    """
    Domain name to get.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Scaleway Project in which to get the domain to create the Web Hosting plan.
    """


@dataclass
class DnsApiSearchDomainsRequest:
    domain_name: str
    """
    Domain name to search.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Scaleway Project in which to search the domain to create the Web Hosting plan.
    """


@dataclass
class DnsApiSyncDomainDnsRecordsRequest:
    domain: str
    """
    Domain for which the DNS records will be synchronized.
    """

    update_web_records: bool
    """
    Whether or not to synchronize the web records (deprecated, use auto_config_domain_dns).
    """

    update_mail_records: bool
    """
    Whether or not to synchronize the mail records (deprecated, use auto_config_domain_dns).
    """

    update_all_records: bool
    """
    Whether or not to synchronize all types of records. This one has priority (deprecated, use auto_config_domain_dns).
    """

    update_nameservers: bool
    """
    Whether or not to synchronize domain nameservers (deprecated, use auto_config_domain_dns).
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    custom_records: Optional[list[SyncDomainDnsRecordsRequestRecord]] = field(
        default_factory=list
    )
    """
    Custom records to synchronize.
    """

    auto_config_domain_dns: Optional[AutoConfigDomainDns] = None
    """
    Whether or not to synchronize each types of records.
    """


@dataclass
class DnsRecords:
    records: list[DnsRecord]
    """
    List of DNS records.
    """

    name_servers: list[Nameserver]
    """
    List of nameservers.
    """

    status: DnsRecordsStatus
    """
    Status of the records.
    """

    dns_config: list[DomainDnsAction]
    """
    Records dns auto configuration settings (deprecated, use auto_config_domain_dns).
    """

    auto_config_domain_dns: Optional[AutoConfigDomainDns] = None
    """
    Whether or not to synchronize each types of records.
    """


@dataclass
class Domain:
    name: str
    """
    Name of the domain.
    """

    status: DomainStatus
    """
    Current status of the domain.
    """

    owner: DomainZoneOwner
    """
    Zone owner of the domain.
    """

    zone_domain_name: str
    """
    Main domain for this zone.
    """

    available_actions: list[DomainAction]
    """
    A list of actions that can be performed on the domain.
    """

    available_dns_actions: list[DomainDnsAction]
    """
    A list of DNS-related actions that can be auto configured for the domain (deprecated, use auto_config_domain_dns instead).
    """

    auto_config_domain_dns: Optional[AutoConfigDomainDns] = None
    """
    Whether or not to synchronize each type of record.
    """


@dataclass
class FreeDomainApiCheckFreeDomainAvailabilityRequest:
    slug: str
    """
    Custom prefix used for the free domain.
    """

    root_domain: str
    """
    Free root domain provided by Web Hosting, selected from the list returned by `ListFreeRootDomains`.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class FreeDomainApiListFreeRootDomainsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results (must be a positive integer).
    """

    page_size: Optional[int] = 0
    """
    Number of free root domains to return (must be a positive integer lower or equal to 100).
    """


@dataclass
class FtpAccountApiChangeFtpAccountPasswordRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    username: str
    """
    Username of the FTP account.
    """

    password: str
    """
    New password for the FTP account.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class FtpAccountApiCreateFtpAccountRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    username: str
    """
    Username for the new FTP account.
    """

    path: str
    """
    Path for the new FTP account.
    """

    password: str
    """
    Password for the new FTP account.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class FtpAccountApiListFtpAccountsRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number (must be a positive integer).
    """

    page_size: Optional[int] = 0
    """
    Number of FTP accounts to return (must be a positive integer lower or equal to 100).
    """

    order_by: Optional[ListFtpAccountsRequestOrderBy] = (
        ListFtpAccountsRequestOrderBy.USERNAME_ASC
    )
    """
    Sort order of FTP accounts in the response.
    """

    domain: Optional[str] = None
    """
    Domain to filter the FTP accounts.
    """


@dataclass
class FtpAccountApiRemoveFtpAccountRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    username: str
    """
    Username of the FTP account to be deleted.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class Hosting:
    id: str
    """
    ID of the Web Hosting plan.
    """

    project_id: str
    """
    ID of the Scaleway Project the Web Hosting plan belongs to.
    """

    status: HostingStatus
    """
    Status of the Web Hosting plan.
    """

    domain: str
    """
    Main domain associated with the Web Hosting plan (deprecated, use domain_info).
    """

    tags: list[str]
    """
    List of tags associated with the Web Hosting plan.
    """

    dns_status: DnsRecordsStatus
    """
    DNS status of the Web Hosting plan (deprecated, use domain_info).
    """

    ipv4: str
    """
    Current IPv4 address of the hosting.
    """

    protected: bool
    """
    Whether the hosting is protected or not.
    """

    domain_status: DomainStatus
    """
    Main domain status of the Web Hosting plan (deprecated, use domain_info).
    """

    region: ScwRegion
    """
    Region where the Web Hosting plan is hosted.
    """

    updated_at: Optional[datetime] = None
    """
    Date on which the Web Hosting plan was last updated.
    """

    created_at: Optional[datetime] = None
    """
    Date on which the Web Hosting plan was created.
    """

    offer: Optional[Offer] = None
    """
    Details of the Web Hosting plan offer and options.
    """

    platform: Optional[Platform] = None
    """
    Details of the hosting platform.
    """

    user: Optional[HostingUser] = None
    """
    Details of the hosting user.
    """

    domain_info: Optional[HostingDomain] = None
    """
    Domain configuration block (subdomain, optional custom domain, and DNS settings).
    """


@dataclass
class HostingApiAddCustomDomainRequest:
    hosting_id: str
    """
    Hosting ID to which the custom domain is attached to.
    """

    domain_name: str
    """
    The custom domain name to attach to the hosting.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiCreateHostingRequest:
    offer_id: str
    """
    ID of the selected offer for the Web Hosting plan.
    """

    email: str
    """
    Contact email for the Web Hosting client.
    """

    domain: str
    """
    Domain name to link to the Web Hosting plan. You must already own this domain name, and have completed the DNS validation process beforehand.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Scaleway Project in which to create the Web Hosting plan.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List of tags for the Web Hosting plan.
    """

    subdomain: Optional[str] = None
    """
    The name prefix to use as a free subdomain (for example, `mysite`) assigned to the Web Hosting plan. The full domain will be automatically created by adding it to the fixed base domain (e.g. `mysite.scw.site`). You do not need to include the base domain yourself.
    """

    offer_options: Optional[list[OfferOptionRequest]] = field(default_factory=list)
    """
    List of the Web Hosting plan options IDs with their quantities.
    """

    language: Optional[StdLanguageCode] = StdLanguageCode.UNKNOWN_LANGUAGE_CODE
    """
    Default language for the control panel interface.
    """

    domain_configuration: Optional[CreateHostingRequestDomainConfiguration] = None
    """
    Indicates whether to update hosting domain name servers and DNS records for domains managed by Scaleway Elements (deprecated, use auto_config_domain_dns instead).
    """

    skip_welcome_email: Optional[bool] = False
    """
    Indicates whether to skip a welcome email to the contact email containing hosting info.
    """

    auto_config_domain_dns: Optional[AutoConfigDomainDns] = None
    """
    Indicates whether to update hosting domain name servers and DNS records for domains managed by Scaleway Elements (deprecated, use auto_update_* fields instead).
    """


@dataclass
class HostingApiCreateSessionRequest:
    hosting_id: str
    """
    Hosting ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiDeleteHostingDomainsRequest:
    hosting_id: str
    """
    Hosting ID of the Web Hosting plan from which to delete domains.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    domains: Optional[list[str]] = field(default_factory=list)
    """
    List of domains to delete from the Web Hosting plan.
    """


@dataclass
class HostingApiDeleteHostingRequest:
    hosting_id: str
    """
    Hosting ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiGetHostingRequest:
    hosting_id: str
    """
    Hosting ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiGetResourceSummaryRequest:
    hosting_id: str
    """
    Hosting ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiListHostingsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results (must be a positive integer).
    """

    page_size: Optional[int] = 0
    """
    Number of Web Hosting plans to return (must be a positive integer lower or equal to 100).
    """

    order_by: Optional[ListHostingsRequestOrderBy] = (
        ListHostingsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order for Web Hosting plans in the response.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags to filter for, only Web Hosting plans with matching tags will be returned.
    """

    statuses: Optional[list[HostingStatus]] = field(default_factory=list)
    """
    Statuses to filter for, only Web Hosting plans with matching statuses will be returned.
    """

    domain: Optional[str] = None
    """
    Domain to filter for, only Web Hosting plans associated with this domain will be returned.
    """

    project_id: Optional[str] = None
    """
    Project ID to filter for, only Web Hosting plans from this Project will be returned.
    """

    organization_id: Optional[str] = None
    """
    Organization ID to filter for, only Web Hosting plans from this Organization will be returned.
    """

    control_panels: Optional[list[str]] = field(default_factory=list)
    """
    Name of the control panel to filter for, only Web Hosting plans from this control panel will be returned.
    """

    subdomain: Optional[str] = None
    """
    Optional free subdomain linked to the Web Hosting plan.
    """


@dataclass
class HostingApiMigrateControlPanelRequest:
    hosting_id: str
    """
    Hosting ID to migrate to a new control panel.
    """

    control_panel_name: str
    """
    Control panel will migrate the hosting to a new server.
    """

    offer_id: str
    """
    Migration.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiRemoveCustomDomainRequest:
    hosting_id: str
    """
    Hosting ID to which the custom domain is detached from.
    """

    domain_name: str
    """
    The custom domain name to detach from the hosting.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiResetHostingPasswordRequest:
    hosting_id: str
    """
    UUID of the hosting.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiResetHostingRequest:
    hosting_id: str
    """
    Hosting ID of the Web Hosting plan to reset.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiUpdateHostingFreeDomainRequest:
    hosting_id: str
    """
    Hosting ID of the Web Hosting plan to update.
    """

    free_domain: str
    """
    New free domain to associate with the Web Hosting plan.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiUpdateHostingRequest:
    hosting_id: str
    """
    Hosting ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    email: Optional[str] = None
    """
    New contact email for the Web Hosting plan.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    New tags for the Web Hosting plan.
    """

    offer_options: Optional[list[OfferOptionRequest]] = field(default_factory=list)
    """
    List of the Web Hosting plan options IDs with their quantities.
    """

    offer_id: Optional[str] = None
    """
    ID of the new offer for the Web Hosting plan.
    """

    protected: Optional[bool] = False
    """
    Whether the hosting is protected or not.
    """


@dataclass
class ListBackupItemsResponse:
    total_count: int
    """
    Total number of backup item groups.
    """

    groups: list[BackupItemGroup]
    """
    List of backup item groups categorized by type.
    """


@dataclass
class ListBackupsResponse:
    total_count: int
    """
    Total number of available backups.
    """

    backups: list[Backup]
    """
    List of available backups.
    """


@dataclass
class ListControlPanelsResponse:
    total_count: int
    """
    Number of control panels returned.
    """

    control_panels: list[ControlPanel]
    """
    List of control panels.
    """


@dataclass
class ListDatabaseUsersResponse:
    total_count: int
    """
    Total number of database users.
    """

    users: list[DatabaseUser]
    """
    List of database users.
    """


@dataclass
class ListDatabasesResponse:
    total_count: int
    """
    Total number of databases.
    """

    databases: list[Database]
    """
    List of databases.
    """


@dataclass
class ListFreeRootDomainsResponse:
    root_domains: list[str]
    """
    List of free root domains available for the Web Hosting.
    """

    total_count: int
    """
    Total number of free root domains available.
    """


@dataclass
class ListFtpAccountsResponse:
    total_count: int
    """
    Total number of FTP accounts.
    """

    ftp_accounts: list[FtpAccount]
    """
    List of FTP accounts.
    """


@dataclass
class ListHostingsResponse:
    total_count: int
    """
    Number of Web Hosting plans returned.
    """

    hostings: list[HostingSummary]
    """
    List of Web Hosting plans.
    """


@dataclass
class ListMailAccountsResponse:
    total_count: int
    """
    Total number of mail accounts.
    """

    mail_accounts: list[MailAccount]
    """
    List of mail accounts.
    """


@dataclass
class ListOffersResponse:
    total_count: int
    """
    Total number of offers.
    """

    offers: list[Offer]
    """
    List of offers.
    """


@dataclass
class ListRecentProgressesResponse:
    progresses: list[ProgressSummary]
    """
    List of summarized progress entries.
    """


@dataclass
class ListWebsitesResponse:
    total_count: int
    """
    Total number of websites.
    """

    websites: list[Website]
    """
    List of websites.
    """


@dataclass
class MailAccountApiChangeMailAccountPasswordRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    domain: str
    """
    Domain part of the mail account address.
    """

    username: str
    """
    Username part of the mail account address.
    """

    password: str
    """
    New password for the mail account.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class MailAccountApiCreateMailAccountRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    domain: str
    """
    Domain part of the mail account address.
    """

    username: str
    """
    Username part address of the mail account address.
    """

    password: str
    """
    Password for the new mail account.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class MailAccountApiListMailAccountsRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number (must be a positive integer).
    """

    page_size: Optional[int] = 0
    """
    Number of mail accounts to return (must be a positive integer lower or equal to 100).
    """

    order_by: Optional[ListMailAccountsRequestOrderBy] = (
        ListMailAccountsRequestOrderBy.USERNAME_ASC
    )
    """
    Sort order of mail accounts in the response.
    """

    domain: Optional[str] = None
    """
    Domain to filter the mail accounts.
    """


@dataclass
class MailAccountApiRemoveMailAccountRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    domain: str
    """
    Domain part of the mail account address.
    """

    username: str
    """
    Username part of the mail account address.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class OfferApiListOffersRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number (must be a positive integer).
    """

    page_size: Optional[int] = 0
    """
    Number of websites to return (must be a positive integer lower or equal to 100).
    """

    order_by: Optional[ListOffersRequestOrderBy] = ListOffersRequestOrderBy.PRICE_ASC
    """
    Sort order for Web Hosting offers in the response.
    """

    hosting_id: Optional[str] = None
    """
    UUID of the hosting plan.
    """

    control_panels: Optional[list[str]] = field(default_factory=list)
    """
    Name of the control panel(s) to filter for.
    """


@dataclass
class Progress:
    id: str
    """
    ID of the progress.
    """

    backup_item_groups: list[BackupItemGroup]
    """
    Groups of backup items included in this progress.
    """

    percentage: int
    """
    Completion percentage of the progress.
    """

    status: ProgressStatus
    """
    Current status of the progress operation.
    """


@dataclass
class ResetHostingPasswordResponse:
    one_time_password: str
    """
    New temporary password (deprecated, use password_b64 instead).
    """

    one_time_password_b64: str
    """
    New temporary password, encoded in base64.
    """


@dataclass
class ResourceSummary:
    databases_count: int
    """
    Total number of active databases in the Web Hosting plan.
    """

    mail_accounts_count: int
    """
    Total number of active email accounts in the Web Hosting plan.
    """

    ftp_accounts_count: int
    """
    Total number of active FTP accounts in the Web Hosting plan.
    """

    websites_count: int
    """
    Total number of active domains in the Web Hosting plan.
    """


@dataclass
class RestoreBackupItemsResponse:
    progress_id: str
    """
    Identifier used to track the item restoration progress.
    """


@dataclass
class RestoreBackupResponse:
    progress_id: str
    """
    Identifier used to track the backup restoration progress.
    """


@dataclass
class SearchDomainsResponse:
    domains_available: list[DomainAvailability]
    """
    List of domains availability.
    """


@dataclass
class Session:
    url: str
    """
    Logged user's session URL.
    """


@dataclass
class WebsiteApiCreateWebsiteRequest:
    hosting_id: str
    """
    Hosting ID to which the website is attached to.
    """

    domain_name: str
    """
    The new domain name or subdomain to use for the website.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class WebsiteApiDeleteWebsiteRequest:
    hosting_id: str
    """
    Hosting ID to which the website is detached from.
    """

    domain_name: str
    """
    The new domain name or subdomain attached to the website.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class WebsiteApiListWebsitesRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number (must be a positive integer).
    """

    page_size: Optional[int] = 0
    """
    Number of websites to return (must be a positive integer lower or equal to 100).
    """

    order_by: Optional[ListWebsitesRequestOrderBy] = (
        ListWebsitesRequestOrderBy.DOMAIN_ASC
    )
    """
    Sort order for Web Hosting websites in the response.
    """


@dataclass
class WebsiteApiResetWebsiteRequest:
    hosting_id: str
    """
    Hosting ID to which the website is attached to.
    """

    domain_name: str
    """
    The domain name with which the website is associated.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """
