# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

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

    auto_config_domain_dns: Optional[AutoConfigDomainDns]
    """
    Indicates whether to auto-configure DNS for this domain.
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

    price: Optional[Money]
    """
    Price of the option for 1 value.
    """


@dataclass
class PlatformControlPanel:
    name: str
    """
    Name of the control panel.
    """

    urls: Optional[PlatformControlPanelUrls]
    """
    URL to connect to control panel dashboard and to Webmail interface.
    """


@dataclass
class HostingDomain:
    subdomain: str
    """
    Optional free subdomain linked to the Web Hosting plan.
    """

    custom_domain: Optional[HostingDomainCustomDomain]
    """
    Optional custom domain linked to the Web Hosting plan.
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

    priority: Optional[int]
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

    one_time_password: Optional[str]
    """
    One-time-password used for the first login to the control panel, cleared after first use (deprecated, use password_b64 instead).
    """

    one_time_password_b64: Optional[str]
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

    options: List[OfferOption]
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

    price: Optional[Money]
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

    control_panel: Optional[PlatformControlPanel]
    """
    Details of the platform control panel.
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

    available_languages: List[StdLanguageCode]
    """
    List of available languages for the control panel.
    """


@dataclass
class DatabaseUser:
    username: str
    """
    Name of the database user.
    """

    databases: List[str]
    """
    List of databases accessible by the user.
    """


@dataclass
class Database:
    database_name: str
    """
    Name of the database.
    """

    users: List[str]
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

    protected: bool
    """
    Whether the hosting is protected or not.
    """

    offer_name: str
    """
    Name of the active offer for the Web Hosting plan.
    """

    region: ScwRegion
    """
    Region where the Web Hosting plan is hosted.
    """

    created_at: Optional[datetime]
    """
    Date on which the Web Hosting plan was created.
    """

    updated_at: Optional[datetime]
    """
    Date on which the Web Hosting plan was last updated.
    """

    domain: Optional[str]
    """
    Main domain associated with the Web Hosting plan (deprecated, use domain_info).
    """

    dns_status: Optional[DnsRecordsStatus]
    """
    DNS status of the Web Hosting plan.
    """

    domain_status: Optional[DomainStatus]
    """
    Main domain status of the Web Hosting plan.
    """

    domain_info: Optional[HostingDomain]
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

    available_actions: List[DomainAvailabilityAction]
    """
    A list of actions that can be performed on the domain.
    """

    can_create_hosting: bool
    """
    Whether a hosting can be created for this domain.
    """

    price: Optional[Money]
    """
    Price for registering the domain.
    """


@dataclass
class CheckUserOwnsDomainResponse:
    owns_domain: bool
    """
    Indicates whether the specified project owns the domain.
    """


@dataclass
class ControlPanelApiListControlPanelsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number (must be a positive integer).
    """

    page_size: Optional[int]
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

    region: Optional[ScwRegion]
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

    region: Optional[ScwRegion]
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

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    new_user: Optional[CreateDatabaseRequestUser]

    existing_username: Optional[str]


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

    region: Optional[ScwRegion]
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

    region: Optional[ScwRegion]
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

    region: Optional[ScwRegion]
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

    region: Optional[ScwRegion]
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

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DatabaseApiListDatabaseUsersRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number (must be a positive integer).
    """

    page_size: Optional[int]
    """
    Number of database users to return (must be a positive integer lower or equal to 100).
    """

    order_by: Optional[ListDatabaseUsersRequestOrderBy]
    """
    Sort order of database users in the response.
    """


@dataclass
class DatabaseApiListDatabasesRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number (must be a positive integer).
    """

    page_size: Optional[int]
    """
    Number of databases to return (must be a positive integer lower or equal to 100).
    """

    order_by: Optional[ListDatabasesRequestOrderBy]
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

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DnsApiCheckUserOwnsDomainRequest:
    domain: str
    """
    Domain for which ownership is to be verified.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the project currently in use.
    """


@dataclass
class DnsApiGetDomainDnsRecordsRequest:
    domain: str
    """
    Domain associated with the DNS records.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DnsApiGetDomainRequest:
    domain_name: str
    """
    Domain name to get.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Scaleway Project in which to get the domain to create the Web Hosting plan.
    """


@dataclass
class DnsApiSearchDomainsRequest:
    domain_name: str
    """
    Domain name to search.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Scaleway Project in which to search the domain to create the Web Hosting plan.
    """


@dataclass
class DnsApiSyncDomainDnsRecordsRequest:
    domain: str
    """
    Domain for which the DNS records will be synchronized.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    update_web_records: Optional[bool]
    """
    Whether or not to synchronize the web records (deprecated, use auto_config_domain_dns).
    """

    update_mail_records: Optional[bool]
    """
    Whether or not to synchronize the mail records (deprecated, use auto_config_domain_dns).
    """

    update_all_records: Optional[bool]
    """
    Whether or not to synchronize all types of records. This one has priority (deprecated, use auto_config_domain_dns).
    """

    update_nameservers: Optional[bool]
    """
    Whether or not to synchronize domain nameservers (deprecated, use auto_config_domain_dns).
    """

    custom_records: Optional[List[SyncDomainDnsRecordsRequestRecord]]
    """
    Custom records to synchronize.
    """

    auto_config_domain_dns: Optional[AutoConfigDomainDns]
    """
    Whether or not to synchronize each types of records.
    """


@dataclass
class DnsRecords:
    records: List[DnsRecord]
    """
    List of DNS records.
    """

    name_servers: List[Nameserver]
    """
    List of nameservers.
    """

    status: DnsRecordsStatus
    """
    Status of the records.
    """

    dns_config: Optional[List[DomainDnsAction]]
    """
    Records dns auto configuration settings (deprecated, use auto_config_domain_dns).
    """

    auto_config_domain_dns: Optional[AutoConfigDomainDns]
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

    available_actions: List[DomainAction]
    """
    A list of actions that can be performed on the domain.
    """

    available_dns_actions: Optional[List[DomainDnsAction]]
    """
    A list of DNS-related actions that can be auto configured for the domain (deprecated, use auto_config_domain_dns instead).
    """

    auto_config_domain_dns: Optional[AutoConfigDomainDns]
    """
    Whether or not to synchronize each type of record.
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

    region: Optional[ScwRegion]
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

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class FtpAccountApiListFtpAccountsRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number (must be a positive integer).
    """

    page_size: Optional[int]
    """
    Number of FTP accounts to return (must be a positive integer lower or equal to 100).
    """

    order_by: Optional[ListFtpAccountsRequestOrderBy]
    """
    Sort order of FTP accounts in the response.
    """

    domain: Optional[str]
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

    region: Optional[ScwRegion]
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

    updated_at: Optional[datetime]
    """
    Date on which the Web Hosting plan was last updated.
    """

    created_at: Optional[datetime]
    """
    Date on which the Web Hosting plan was created.
    """

    domain: Optional[str]
    """
    Main domain associated with the Web Hosting plan (deprecated, use domain_info).
    """

    offer: Optional[Offer]
    """
    Details of the Web Hosting plan offer and options.
    """

    platform: Optional[Platform]
    """
    Details of the hosting platform.
    """

    tags: List[str]
    """
    List of tags associated with the Web Hosting plan.
    """

    ipv4: str
    """
    Current IPv4 address of the hosting.
    """

    protected: bool
    """
    Whether the hosting is protected or not.
    """

    region: ScwRegion
    """
    Region where the Web Hosting plan is hosted.
    """

    dns_status: Optional[DnsRecordsStatus]
    """
    DNS status of the Web Hosting plan (deprecated, use domain_info).
    """

    user: Optional[HostingUser]
    """
    Details of the hosting user.
    """

    domain_status: Optional[DomainStatus]
    """
    Main domain status of the Web Hosting plan (deprecated, use domain_info).
    """

    domain_info: Optional[HostingDomain]
    """
    Domain configuration block (subdomain, optional custom domain, and DNS settings).
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

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Scaleway Project in which to create the Web Hosting plan.
    """

    tags: Optional[List[str]]
    """
    List of tags for the Web Hosting plan.
    """

    subdomain: Optional[str]
    """
    The name prefix to use as a free subdomain (for example, `mysite`) assigned to the Web Hosting plan. The full domain will be automatically created by adding it to the fixed base domain (e.g. `mysite.scw.site`). You do not need to include the base domain yourself.
    """

    offer_options: Optional[List[OfferOptionRequest]]
    """
    List of the Web Hosting plan options IDs with their quantities.
    """

    language: Optional[StdLanguageCode]
    """
    Default language for the control panel interface.
    """

    domain_configuration: Optional[CreateHostingRequestDomainConfiguration]
    """
    Indicates whether to update hosting domain name servers and DNS records for domains managed by Scaleway Elements (deprecated, use auto_config_domain_dns instead).
    """

    skip_welcome_email: Optional[bool]
    """
    Indicates whether to skip a welcome email to the contact email containing hosting info.
    """

    auto_config_domain_dns: Optional[AutoConfigDomainDns]
    """
    Indicates whether to update hosting domain name servers and DNS records for domains managed by Scaleway Elements (deprecated, use auto_update_* fields instead).
    """


@dataclass
class HostingApiCreateSessionRequest:
    hosting_id: str
    """
    Hosting ID.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiDeleteHostingRequest:
    hosting_id: str
    """
    Hosting ID.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiGetHostingRequest:
    hosting_id: str
    """
    Hosting ID.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiGetResourceSummaryRequest:
    hosting_id: str
    """
    Hosting ID.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiListHostingsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number to return, from the paginated results (must be a positive integer).
    """

    page_size: Optional[int]
    """
    Number of Web Hosting plans to return (must be a positive integer lower or equal to 100).
    """

    order_by: Optional[ListHostingsRequestOrderBy]
    """
    Sort order for Web Hosting plans in the response.
    """

    tags: Optional[List[str]]
    """
    Tags to filter for, only Web Hosting plans with matching tags will be returned.
    """

    statuses: Optional[List[HostingStatus]]
    """
    Statuses to filter for, only Web Hosting plans with matching statuses will be returned.
    """

    domain: Optional[str]
    """
    Domain to filter for, only Web Hosting plans associated with this domain will be returned.
    """

    project_id: Optional[str]
    """
    Project ID to filter for, only Web Hosting plans from this Project will be returned.
    """

    organization_id: Optional[str]
    """
    Organization ID to filter for, only Web Hosting plans from this Organization will be returned.
    """

    control_panels: Optional[List[str]]
    """
    Name of the control panel to filter for, only Web Hosting plans from this control panel will be returned.
    """

    subdomain: Optional[str]
    """
    Optional free subdomain linked to the Web Hosting plan.
    """


@dataclass
class HostingApiResetHostingPasswordRequest:
    hosting_id: str
    """
    UUID of the hosting.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiUpdateHostingRequest:
    hosting_id: str
    """
    Hosting ID.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    email: Optional[str]
    """
    New contact email for the Web Hosting plan.
    """

    tags: Optional[List[str]]
    """
    New tags for the Web Hosting plan.
    """

    offer_options: Optional[List[OfferOptionRequest]]
    """
    List of the Web Hosting plan options IDs with their quantities.
    """

    offer_id: Optional[str]
    """
    ID of the new offer for the Web Hosting plan.
    """

    protected: Optional[bool]
    """
    Whether the hosting is protected or not.
    """


@dataclass
class ListControlPanelsResponse:
    total_count: int
    """
    Number of control panels returned.
    """

    control_panels: List[ControlPanel]
    """
    List of control panels.
    """


@dataclass
class ListDatabaseUsersResponse:
    total_count: int
    """
    Total number of database users.
    """

    users: List[DatabaseUser]
    """
    List of database users.
    """


@dataclass
class ListDatabasesResponse:
    total_count: int
    """
    Total number of databases.
    """

    databases: List[Database]
    """
    List of databases.
    """


@dataclass
class ListFtpAccountsResponse:
    total_count: int
    """
    Total number of FTP accounts.
    """

    ftp_accounts: List[FtpAccount]
    """
    List of FTP accounts.
    """


@dataclass
class ListHostingsResponse:
    total_count: int
    """
    Number of Web Hosting plans returned.
    """

    hostings: List[HostingSummary]
    """
    List of Web Hosting plans.
    """


@dataclass
class ListMailAccountsResponse:
    total_count: int
    """
    Total number of mail accounts.
    """

    mail_accounts: List[MailAccount]
    """
    List of mail accounts.
    """


@dataclass
class ListOffersResponse:
    total_count: int
    """
    Total number of offers.
    """

    offers: List[Offer]
    """
    List of offers.
    """


@dataclass
class ListWebsitesResponse:
    total_count: int
    """
    Total number of websites.
    """

    websites: List[Website]
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

    region: Optional[ScwRegion]
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

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class MailAccountApiListMailAccountsRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number (must be a positive integer).
    """

    page_size: Optional[int]
    """
    Number of mail accounts to return (must be a positive integer lower or equal to 100).
    """

    order_by: Optional[ListMailAccountsRequestOrderBy]
    """
    Sort order of mail accounts in the response.
    """

    domain: Optional[str]
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

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class OfferApiListOffersRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number (must be a positive integer).
    """

    page_size: Optional[int]
    """
    Number of websites to return (must be a positive integer lower or equal to 100).
    """

    order_by: Optional[ListOffersRequestOrderBy]
    """
    Sort order for Web Hosting offers in the response.
    """

    hosting_id: Optional[str]
    """
    UUID of the hosting plan.
    """

    control_panels: Optional[List[str]]
    """
    Name of the control panel(s) to filter for.
    """


@dataclass
class ResetHostingPasswordResponse:
    one_time_password_b64: str
    """
    New temporary password, encoded in base64.
    """

    one_time_password: Optional[str]
    """
    New temporary password (deprecated, use password_b64 instead).
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
class SearchDomainsResponse:
    domains_available: List[DomainAvailability]
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
class WebsiteApiListWebsitesRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number (must be a positive integer).
    """

    page_size: Optional[int]
    """
    Number of websites to return (must be a positive integer lower or equal to 100).
    """

    order_by: Optional[ListWebsitesRequestOrderBy]
    """
    Sort order for Web Hosting websites in the response.
    """
