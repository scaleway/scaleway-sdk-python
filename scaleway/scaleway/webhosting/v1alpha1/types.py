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
    Record time to live.
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
    ID of the hosting.
    """

    organization_id: str
    """
    Organization ID of the hosting.
    """

    project_id: str
    """
    Project ID of the hosting.
    """

    updated_at: Optional[datetime]
    """
    Last update date.
    """

    created_at: Optional[datetime]
    """
    Creation date.
    """

    status: HostingStatus
    """
    The hosting status.
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
    ID of the active offer.
    """

    offer_name: str
    """
    Name of the active offer.
    """

    domain: str
    """
    Main domain of the hosting.
    """

    tags: List[str]
    """
    Tags of the hosting.
    """

    options: List[HostingOption]
    """
    Active options of the hosting.
    """

    dns_status: HostingDnsStatus
    """
    DNS status of the hosting.
    """

    cpanel_urls: Optional[HostingCpanelUrls]
    """
    URL to connect to cPanel Dashboard and to Webmail interface.
    """

    username: str
    """
    Main hosting cPanel username.
    """

    region: Region
    """
    Region of the hosting.
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
    Number of returned hostings.
    """

    hostings: List[Hosting]
    """
    List of hostings.
    """


@dataclass
class ListOffersResponse:
    """
    List offers response.
    """

    offers: List[Offer]
    """
    List of returned offers.
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
    If the nameserver is the default.
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
    Offer product.
    """

    price: Optional[Money]
    """
    Offer price.
    """

    available: bool
    """
    If offer is available for a specific hosting.
    """

    quota_warnings: List[OfferQuotaWarning]
    """
    If not available, return quota warnings.
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
    ID of the selected offer for the hosting.
    """

    project_id: Optional[str]
    """
    Project ID of the hosting.
    """

    email: Optional[str]
    """
    Contact email of the client for the hosting.
    """

    tags: Optional[List[str]]
    """
    The tags of the hosting.
    """

    domain: str
    """
    The domain name of the hosting.
    """

    option_ids: Optional[List[str]]
    """
    IDs of the selected options for the hosting.
    """


@dataclass
class ListHostingsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    A positive integer to choose the page to return.
    """

    page_size: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to return.
    """

    order_by: Optional[ListHostingsRequestOrderBy]
    """
    Define the order of the returned hostings.
    """

    tags: Optional[List[str]]
    """
    Return hostings with these tags.
    """

    statuses: Optional[List[HostingStatus]]
    """
    Return hostings with these statuses.
    """

    domain: Optional[str]
    """
    Return hostings with this domain.
    """

    project_id: Optional[str]
    """
    Return hostings from this project ID.
    """

    organization_id: Optional[str]
    """
    Return hostings from this organization ID.
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
    New contact email for the hosting.
    """

    tags: Optional[List[str]]
    """
    New tags for the hosting.
    """

    option_ids: Optional[List[str]]
    """
    New options IDs for the hosting.
    """

    offer_id: Optional[str]
    """
    New offer ID for the hosting.
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
    Domain associated to the DNS records.
    """


@dataclass
class ListOffersRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: ListOffersRequestOrderBy
    """
    Define the order of the returned hostings.
    """

    without_options: bool
    """
    Select only offers, no options.
    """

    only_options: bool
    """
    Select only options.
    """

    hosting_id: Optional[str]
    """
    Define a specific hosting id (optional).
    """
