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


class DnsRecordStatus(str, Enum):
    UNKNOWN_STATUS = "unknown_status"
    VALID = "valid"
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)


class DnsRecordType(str, Enum):
    UNKNOWN_TYPE = "unknown_type"
    A = "a"
    CNAME = "cname"
    MX = "mx"
    TXT = "txt"
    NS = "ns"
    AAAA = "aaaa"

    def __str__(self) -> str:
        return str(self.value)


class DnsRecordsStatus(str, Enum):
    UNKNOWN = "unknown"
    VALID = "valid"
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)


class HostingDnsStatus(str, Enum):
    UNKNOWN_DNS_STATUS = "unknown_dns_status"
    VALID = "valid"
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)


class HostingStatus(str, Enum):
    UNKNOWN_STATUS = "unknown_status"
    DELIVERING = "delivering"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class ListHostingsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListOffersRequestOrderBy(str, Enum):
    PRICE_ASC = "price_asc"

    def __str__(self) -> str:
        return str(self.value)


class NameserverStatus(str, Enum):
    UNKNOWN_STATUS = "unknown_status"
    VALID = "valid"
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)


class OfferQuotaWarning(str, Enum):
    UNKNOWN_QUOTA_WARNING = "unknown_quota_warning"
    EMAIL_COUNT_EXCEEDED = "email_count_exceeded"
    DATABASE_COUNT_EXCEEDED = "database_count_exceeded"
    DISK_USAGE_EXCEEDED = "disk_usage_exceeded"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class DnsRecord:
    """
    Dns record.
    """

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

    priority: Optional[int]
    """
    Record priority level.
    """

    status: DnsRecordStatus
    """
    Record status.
    """


@dataclass
class DnsRecords:
    """
    Dns records.
    """

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
class Hosting:
    """
    Hosting.
    """

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

    updated_at: Optional[datetime]
    """
    Date on which the Web Hosting plan was last updated.
    """

    created_at: Optional[datetime]
    """
    Date on which the Web Hosting plan was created.
    """

    status: HostingStatus
    """
    Status of the Web Hosting plan.
    """

    platform_hostname: str
    """
    Hostname of the host platform.
    """

    platform_number: Optional[int]
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
    Array of any options activated for the Web Hosting plan.
    """

    dns_status: HostingDnsStatus
    """
    DNS status of the Web Hosting plan.
    """

    cpanel_urls: Optional[HostingCpanelUrls]
    """
    URL to connect to cPanel dashboard and to Webmail interface.
    """

    username: str
    """
    Main Web Hosting cPanel username.
    """

    region: Region
    """
    Region where the Web Hosting plan is hosted.
    """


@dataclass
class HostingCpanelUrls:
    dashboard: str

    webmail: str


@dataclass
class HostingOption:
    """
    Hosting. option.
    """

    id: str
    """
    Option ID.
    """

    name: str
    """
    Option name.
    """


@dataclass
class ListHostingsResponse:
    """
    List hostings response.
    """

    total_count: int
    """
    Number of Web Hosting plans returned.
    """

    hostings: List[Hosting]
    """
    List of Web Hosting plans.
    """


@dataclass
class ListOffersResponse:
    """
    List offers response.
    """

    offers: List[Offer]
    """
    List of offers.
    """


@dataclass
class Nameserver:
    """
    Nameserver.
    """

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
class Offer:
    """
    Offer.
    """

    id: str
    """
    Offer ID.
    """

    billing_operation_path: str
    """
    Unique identifier used for billing.
    """

    product: Optional[OfferProduct]
    """
    Product constituting this offer.
    """

    price: Optional[Money]
    """
    Price of this offer.
    """

    available: bool
    """
    If a hosting_id was specified in the call, defines whether this offer is available for that Web Hosting plan to migrate (update) to.
    """

    quota_warnings: List[OfferQuotaWarning]
    """
    Quota warnings, if the offer is not available for the specified hosting_id.
    """


@dataclass
class OfferProduct:
    """
    Offer. product.
    """

    name: str
    """
    Product name.
    """

    option: bool
    """
    Product option.
    """

    email_accounts_quota: int

    email_storage_quota: int

    databases_quota: int

    hosting_storage_quota: int

    support_included: bool

    v_cpu: int

    ram: int


@dataclass
class CreateHostingRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    offer_id: str
    """
    ID of the selected offer for the Web Hosting plan.
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

    domain: str
    """
    Domain name to link to the Web Hosting plan. You must already own this domain name, and have completed the DNS validation process beforehand.
    """

    option_ids: Optional[List[str]]
    """
    IDs of any selected additional options for the Web Hosting plan.
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
class GetHostingRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    hosting_id: str
    """
    Hosting ID.
    """


@dataclass
class UpdateHostingRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    hosting_id: str
    """
    Hosting ID.
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


@dataclass
class DeleteHostingRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    hosting_id: str
    """
    Hosting ID.
    """


@dataclass
class RestoreHostingRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    hosting_id: str
    """
    Hosting ID.
    """


@dataclass
class GetDomainDnsRecordsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    domain: str
    """
    Domain associated with the DNS records.
    """


@dataclass
class ListOffersRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: ListOffersRequestOrderBy
    """
    Sort order of offers in the response.
    """

    without_options: bool
    """
    Defines whether the response should consist of offers only, without options.
    """

    only_options: bool
    """
    Defines whether the response should consist of options only, without offers.
    """

    hosting_id: Optional[str]
    """
    ID of a Web Hosting plan, to check compatibility with returned offers (in case of wanting to update the plan).
    """
