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
    webmail: str

    dashboard: str


@dataclass
class HostingOption:
    name: str
    """
    Option name.
    """

    id: str
    """
    Option ID.
    """


@dataclass
class OfferProduct:
    max_addon_domains: int
    """
    Limit number of add-on domains.
    """

    ram: int
    """
    Limit quantity of memory in gigabytes.
    """

    v_cpu: int
    """
    Limit number of virtual CPU.
    """

    support_included: bool
    """
    Whether or not support is included.
    """

    hosting_storage_quota: int
    """
    Limit quantity of hosting storage in gigabytes.
    """

    databases_quota: int
    """
    Limit number of databases.
    """

    email_storage_quota: int
    """
    Limit quantity of email storage in gigabytes.
    """

    email_accounts_quota: int
    """
    Limit number of email accounts.
    """

    option: bool
    """
    Product option.
    """

    name: str
    """
    Product name.
    """


@dataclass
class DnsRecord:
    status: DnsRecordStatus
    """
    Record status.
    """

    value: str
    """
    Record value.
    """

    ttl: int
    """
    Record time-to-live.
    """

    type_: DnsRecordType
    """
    Record type.
    """

    name: str
    """
    Record name.
    """

    priority: Optional[int]
    """
    Record priority level.
    """


@dataclass
class Nameserver:
    is_default: bool
    """
    Defines whether the nameserver is the default one.
    """

    status: NameserverStatus
    """
    Status of the nameserver.
    """

    hostname: str
    """
    Hostname of the nameserver.
    """


@dataclass
class Hosting:
    tags: List[str]
    """
    List of tags associated with the Web Hosting plan.
    """

    domain: str
    """
    Main domain associated with the Web Hosting plan.
    """

    offer_name: str
    """
    Name of the active offer for the Web Hosting plan.
    """

    id: str
    """
    ID of the Web Hosting plan.
    """

    username: str
    """
    Main Web Hosting cPanel username.
    """

    dns_status: HostingDnsStatus
    """
    DNS status of the Web Hosting plan.
    """

    status: HostingStatus
    """
    Status of the Web Hosting plan.
    """

    offer_end_of_life: bool
    """
    Indicates if the hosting offer has reached its end of life.
    """

    region: Region
    """
    Region where the Web Hosting plan is hosted.
    """

    project_id: str
    """
    ID of the Scaleway Project the Web Hosting plan belongs to.
    """

    organization_id: str
    """
    ID of the Scaleway Organization the Web Hosting plan belongs to.
    """

    options: List[HostingOption]
    """
    Array of any options activated for the Web Hosting plan.
    """

    cpanel_urls: HostingCpanelUrls
    """
    URL to connect to cPanel dashboard and to Webmail interface.
    """

    platform_hostname: str
    """
    Hostname of the host platform.
    """

    offer_id: str
    """
    ID of the active offer for the Web Hosting plan.
    """

    platform_number: Optional[int]
    """
    Number of the host platform.
    """

    created_at: Optional[datetime]
    """
    Date on which the Web Hosting plan was created.
    """

    updated_at: Optional[datetime]
    """
    Date on which the Web Hosting plan was last updated.
    """


@dataclass
class Offer:
    end_of_life: bool
    """
    Indicates if the offer has reached its end of life.
    """

    quota_warnings: List[OfferQuotaWarning]
    """
    Quota warnings, if the offer is not available for the specified hosting_id.
    """

    available: bool
    """
    If a hosting_id was specified in the call, defines whether this offer is available for that Web Hosting plan to migrate (update) to.
    """

    product: OfferProduct
    """
    Product constituting this offer.
    """

    billing_operation_path: str
    """
    Unique identifier used for billing.
    """

    id: str
    """
    Offer ID.
    """

    price: Optional[Money]
    """
    Price of this offer.
    """


@dataclass
class CreateHostingRequest:
    domain: str
    """
    Domain name to link to the Web Hosting plan. You must already own this domain name, and have completed the DNS validation process beforehand.
    """

    offer_id: str
    """
    ID of the selected offer for the Web Hosting plan.
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
    status: DnsRecordsStatus
    """
    Status of the records.
    """

    name_servers: List[Nameserver]
    """
    List of nameservers.
    """

    records: List[DnsRecord]
    """
    List of DNS records.
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


@dataclass
class ListHostingsResponse:
    hostings: List[Hosting]
    """
    List of Web Hosting plans.
    """

    total_count: int
    """
    Number of Web Hosting plans returned.
    """


@dataclass
class ListOffersRequest:
    only_options: bool
    """
    Defines whether the response should consist of options only, without offers.
    """

    without_options: bool
    """
    Defines whether the response should consist of offers only, without options.
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


@dataclass
class ListOffersResponse:
    offers: List[Offer]
    """
    List of offers.
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
