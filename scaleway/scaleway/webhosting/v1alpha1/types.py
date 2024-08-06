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
    UNKNOWN = "unknown"
    VALID = "valid"
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)


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


class ListHostingsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListOffersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    PRICE_ASC = "price_asc"

    def __str__(self) -> str:
        return str(self.value)


class NameserverStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    VALID = "valid"
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)


class OfferQuotaWarning(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_QUOTA_WARNING = "unknown_quota_warning"
    EMAIL_COUNT_EXCEEDED = "email_count_exceeded"
    DATABASE_COUNT_EXCEEDED = "database_count_exceeded"
    DISK_USAGE_EXCEEDED = "disk_usage_exceeded"

    def __str__(self) -> str:
        return str(self.value)


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

    name: str
    """
    Option name.
    """


@dataclass
class EmailAddress:
    domain: str
    """
    Domain part of the mailbox address.
    """

    login: str
    """
    Username part address of the mailbox address.
    """


@dataclass
class OfferProduct:
    name: str
    """
    Product name.
    """

    option: bool
    """
    Product option.
    """

    email_accounts_quota: int
    """
    Limit number of email accounts.
    """

    email_storage_quota: int
    """
    Limit quantity of email storage in gigabytes.
    """

    databases_quota: int
    """
    Limit number of databases.
    """

    hosting_storage_quota: int
    """
    Limit quantity of hosting storage in gigabytes.
    """

    support_included: bool
    """
    Whether or not support is included.
    """

    v_cpu: int
    """
    Limit number of virtual CPU.
    """

    ram: int
    """
    Limit quantity of memory in gigabytes.
    """

    max_addon_domains: int
    """
    Limit number of add-on domains.
    """


@dataclass
class CreateHostingRequestDomainConfiguration:
    update_nameservers: bool

    update_web_record: bool

    update_mail_record: bool

    update_all_records: bool


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
    URL of this control panel's logo.
    """

    available_languages: List[StdLanguageCode]
    """
    List of available languages for the control panel.
    """


@dataclass
class Hosting:
    id: str
    """
    ID of the Web Hosting plan.
    """

    organization_id: str
    """
    ID of the Scaleway Organization the Web Hosting plan belongs to.
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

    updated_at: Optional[datetime]
    """
    Date on which the Web Hosting plan was last updated.
    """

    created_at: Optional[datetime]
    """
    Date on which the Web Hosting plan was created.
    """

    platform_number: Optional[int]
    """
    Number of the host platform.
    """

    options: List[HostingOption]
    """
    Array of any options activated for the Web Hosting plan.
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

    region: Region
    """
    Region where the Web Hosting plan is hosted.
    """

    cpanel_urls: Optional[HostingCpanelUrls]
    """
    URL to connect to cPanel dashboard and to Webmail interface.
    """


@dataclass
class Mailbox:
    mailbox_id: int
    """
    The ID of the mailbox.
    """

    email: Optional[EmailAddress]
    """
    The email address of the mailbox.
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

    available: bool
    """
    If a hosting_id was specified in the call, defines whether this offer is available for that Web Hosting plan to migrate (update) to.
    """

    quota_warnings: List[OfferQuotaWarning]
    """
    Quota warnings, if the offer is not available for the specified hosting_id.
    """

    end_of_life: bool
    """
    Indicates if the offer has reached its end of life.
    """

    control_panel_name: str
    """
    Name of the control panel.
    """

    product: Optional[OfferProduct]
    """
    Product constituting this offer.
    """

    price: Optional[Money]
    """
    Price of this offer.
    """


@dataclass
class CheckUserOwnsDomainRequest:
    domain: str
    """
    Domain for which ownership is to be verified.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the project currently in use.
    """


@dataclass
class CheckUserOwnsDomainResponse:
    owns_domain: bool
    """
    Indicates whether the specified project owns the domain.
    """


@dataclass
class ClassicMailApiCreateMailboxRequest:
    online_id: int
    """
    The Online hosting ID.
    """

    password: str
    """
    Password for the new mailbox.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    email: Optional[EmailAddress]
    """
    The email address of the mailbox.
    """


@dataclass
class ClassicMailApiDeleteMailboxRequest:
    online_id: int
    """
    The Online hosting ID.
    """

    mailbox_id: int
    """
    The ID of the mailbox to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ClassicMailApiGetMailboxRequest:
    online_id: int
    """
    The Online hosting ID.
    """

    mailbox_id: int
    """
    The ID of the mailbox to get.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ClassicMailApiListMailboxesRequest:
    online_id: int
    """
    The Online hosting ID.
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
    Number of mailboxes to return (must be a positive integer lower or equal to 100).
    """

    domain: Optional[str]
    """
    Domain to filter the mailboxes.
    """


@dataclass
class ClassicMailApiUpdateMailboxRequest:
    online_id: int
    """
    The Online hosting ID.
    """

    mailbox_id: int
    """
    The ID of the mailbox to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    password: Optional[str]
    """
    New password for the mailbox.
    """


@dataclass
class CreateHostingRequest:
    offer_id: str
    """
    ID of the selected offer for the Web Hosting plan.
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

    email: Optional[str]
    """
    Contact email for the Web Hosting client.
    """

    tags: Optional[List[str]]
    """
    List of tags for the Web Hosting plan.
    """

    option_ids: Optional[List[str]]
    """
    IDs of any selected additional options for the Web Hosting plan.
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
class CreateSessionRequest:
    hosting_id: str
    """
    Hosting ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteHostingRequest:
    hosting_id: str
    """
    Hosting ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
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


@dataclass
class GetDomainDnsRecordsRequest:
    domain: str
    """
    Domain associated with the DNS records.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetHostingRequest:
    hosting_id: str
    """
    Hosting ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListControlPanelsRequest:
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
    Number of control panels to return (must be a positive integer lower or equal to 100).
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
class ListHostingsRequest:
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
class ListHostingsResponse:
    total_count: int
    """
    Number of Web Hosting plans returned.
    """

    hostings: List[Hosting]
    """
    List of Web Hosting plans.
    """


@dataclass
class ListMailboxesResponse:
    total_count: int
    """
    Total number of mailboxes.
    """

    mailboxes: List[Mailbox]
    """
    List of mailboxes.
    """


@dataclass
class ListOffersRequest:
    without_options: bool
    """
    Defines whether the response should consist of offers only, without options.
    """

    only_options: bool
    """
    Defines whether the response should consist of options only, without offers.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListOffersRequestOrderBy]
    """
    Sort order of offers in the response.
    """

    hosting_id: Optional[str]
    """
    ID of a Web Hosting plan, to check compatibility with returned offers (in case of wanting to update the plan).
    """

    control_panels: Optional[List[str]]
    """
    Name of the control panel to filter for.
    """


@dataclass
class ListOffersResponse:
    offers: List[Offer]
    """
    List of offers.
    """


@dataclass
class ResetHostingPasswordRequest:
    hosting_id: str
    """
    UUID of the hosting.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ResetHostingPasswordResponse:
    password: str
    """
    New password.
    """


@dataclass
class RestoreHostingRequest:
    hosting_id: str
    """
    Hosting ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class Session:
    url: str
    """
    Logged user's session URL.
    """


@dataclass
class UpdateHostingRequest:
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

    option_ids: Optional[List[str]]
    """
    IDs of the new options for the Web Hosting plan.
    """

    offer_id: Optional[str]
    """
    ID of the new offer for the Web Hosting plan.
    """

    protected: Optional[bool]
    """
    Whether the hosting is protected or not.
    """
