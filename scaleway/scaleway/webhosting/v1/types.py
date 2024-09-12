# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Money,
    Region,
)
from scaleway_core.utils import (
    StrEnumMeta,
)

from ...std.types import (
    LanguageCode as StdLanguageCode,
)


class HostingDnsStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_DNS_STATUS = "unknown_dns_status"
    VALID = "valid"
    INVALID = "invalid"

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

    def __str__(self) -> str:
        return str(self.value)


class HostingSummaryStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    DELIVERING = "delivering"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"
    MIGRATING = "migrating"

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


class OfferOptionName(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_NAME = "unknown_name"
    DOMAIN_COUNT = "domain_count"
    EMAIL_COUNT = "email_count"
    STORAGE_GB = "storage_gb"
    VCPU_COUNT = "vcpu_count"
    RAM_GB = "ram_gb"
    BACKUP = "backup"
    DEDICATED_IP = "dedicated_ip"

    def __str__(self) -> str:
        return str(self.value)


class OfferOptionWarning(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_WARNING = "unknown_warning"
    QUOTA_EXCEEDED_WARNING = "quota_exceeded_warning"

    def __str__(self) -> str:
        return str(self.value)


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
class HostingCpanelUrls:
    dashboard: str

    webmail: str


@dataclass
class HostingOption:
    id: str
    """
    Option ID.
    """

    name: OfferOptionName
    """
    Option name.
    """

    quantity: int
    """
    Option quantity.
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

    status: HostingSummaryStatus
    """
    Status of the Web Hosting plan.
    """

    domain: str
    """
    Main domain associated with the Web Hosting plan.
    """

    protected: bool
    """
    Whether the hosting is protected or not.
    """

    region: Region
    """
    Region where the Web Hosting plan is hosted.
    """

    updated_at: Optional[datetime]
    """
    Date on which the Web Hosting plan was last updated.
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
class Offer:
    id: str
    """
    Offer ID.
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

    price: Optional[Money]
    """
    Price of the offer.
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
class ControlPanelApiListControlPanelsRequest:
    region: Optional[Region]
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

    region: Optional[Region]
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

    region: Optional[Region]
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

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


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

    region: Optional[Region]
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

    region: Optional[Region]
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

    region: Optional[Region]
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

    region: Optional[Region]
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

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DatabaseApiListDatabaseUsersRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    region: Optional[Region]
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

    region: Optional[Region]
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

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
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

    region: Optional[Region]
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

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class FtpAccountApiListFtpAccountsRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    region: Optional[Region]
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

    region: Optional[Region]
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

    platform_hostname: str
    """
    Hostname of the host platform.
    """

    platform_number: int
    """
    Number of the host platform.
    """

    offer_id: str
    """
    ID of the active offer for the Web Hosting plan.
    """

    offer_name: str
    """
    Name of the active offer for the Web Hosting plan.
    """

    domain: str
    """
    Main domain associated with the Web Hosting plan.
    """

    tags: List[str]
    """
    List of tags associated with the Web Hosting plan.
    """

    options: List[HostingOption]
    """
    List of the Web Hosting plan options.
    """

    updated_at: Optional[datetime]
    """
    Date on which the Web Hosting plan was last updated.
    """

    created_at: Optional[datetime]
    """
    Date on which the Web Hosting plan was created.
    """

    dns_status: HostingDnsStatus
    """
    DNS status of the Web Hosting plan.
    """

    username: str
    """
    Main Web Hosting cPanel username.
    """

    offer_end_of_life: bool
    """
    Indicates if the hosting offer has reached its end of life.
    """

    control_panel_name: str
    """
    Name of the control panel.
    """

    platform_group: str
    """
    Group of the hosting's host server/platform.
    """

    ipv4: str
    """
    IPv4 address of the hosting's host server.
    """

    ipv6: str
    """
    IPv6 address of the hosting's host server.
    """

    protected: bool
    """
    Whether the hosting is protected or not.
    """

    one_time_password: str
    """
    One-time-password used for the first login or reset password, empty after first use.
    """

    contact_email: str
    """
    Contact email used for the hosting.
    """

    region: Region
    """
    Region where the Web Hosting plan is hosted.
    """

    cpanel_urls: Optional[HostingCpanelUrls]
    """
    URL to connect to cPanel dashboard and to Webmail interface.
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

    region: Optional[Region]
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
    Indicates whether to update hosting domain name servers and DNS records for domains managed by Scaleway Elements.
    """


@dataclass
class HostingApiCreateSessionRequest:
    hosting_id: str
    """
    Hosting ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiDeleteHostingRequest:
    hosting_id: str
    """
    Hosting ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiGetHostingRequest:
    hosting_id: str
    """
    Hosting ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiListHostingsRequest:
    region: Optional[Region]
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


@dataclass
class HostingApiResetHostingPasswordRequest:
    hosting_id: str
    """
    UUID of the hosting.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class HostingApiUpdateHostingRequest:
    hosting_id: str
    """
    Hosting ID.
    """

    region: Optional[Region]
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

    region: Optional[Region]
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

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class MailAccountApiListMailAccountsRequest:
    hosting_id: str
    """
    UUID of the hosting plan.
    """

    region: Optional[Region]
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

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class OfferApiListOffersRequest:
    region: Optional[Region]
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
    one_time_password: str
    """
    New temporary password.
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

    region: Optional[Region]
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
