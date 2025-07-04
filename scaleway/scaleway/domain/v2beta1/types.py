# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from scaleway_core.bridge import (
    Money,
)
from scaleway_core.utils import (
    StrEnumMeta,
)

from ...std.types import (
    LanguageCode as StdLanguageCode,
)


class ContactEmailStatus(str, Enum, metaclass=StrEnumMeta):
    EMAIL_STATUS_UNKNOWN = "email_status_unknown"
    VALIDATED = "validated"
    NOT_VALIDATED = "not_validated"
    INVALID_EMAIL = "invalid_email"

    def __str__(self) -> str:
        return str(self.value)


class ContactExtensionFRMode(str, Enum, metaclass=StrEnumMeta):
    MODE_UNKNOWN = "mode_unknown"
    INDIVIDUAL = "individual"
    COMPANY_IDENTIFICATION_CODE = "company_identification_code"
    DUNS = "duns"
    LOCAL = "local"
    ASSOCIATION = "association"
    TRADEMARK = "trademark"
    CODE_AUTH_AFNIC = "code_auth_afnic"

    def __str__(self) -> str:
        return str(self.value)


class ContactExtensionNLLegalForm(str, Enum, metaclass=StrEnumMeta):
    LEGAL_FORM_UNKNOWN = "legal_form_unknown"
    OTHER = "other"
    NON_DUTCH_EU_COMPANY = "non_dutch_eu_company"
    NON_DUTCH_LEGAL_FORM_ENTERPRISE_SUBSIDIARY = (
        "non_dutch_legal_form_enterprise_subsidiary"
    )
    LIMITED_COMPANY = "limited_company"
    LIMITED_COMPANY_IN_FORMATION = "limited_company_in_formation"
    COOPERATIVE = "cooperative"
    LIMITED_PARTNERSHIP = "limited_partnership"
    SOLE_COMPANY = "sole_company"
    EUROPEAN_ECONOMIC_INTEREST_GROUP = "european_economic_interest_group"
    RELIGIOUS_ENTITY = "religious_entity"
    PARTNERSHIP = "partnership"
    PUBLIC_COMPANY = "public_company"
    MUTUAL_BENEFIT_COMPANY = "mutual_benefit_company"
    RESIDENTIAL = "residential"
    SHIPPING_COMPANY = "shipping_company"
    FOUNDATION = "foundation"
    ASSOCIATION = "association"
    TRADING_PARTNERSHIP = "trading_partnership"
    NATURAL_PERSON = "natural_person"

    def __str__(self) -> str:
        return str(self.value)


class ContactLegalForm(str, Enum, metaclass=StrEnumMeta):
    LEGAL_FORM_UNKNOWN = "legal_form_unknown"
    INDIVIDUAL = "individual"
    CORPORATE = "corporate"
    ASSOCIATION = "association"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)


class ContactStatus(str, Enum, metaclass=StrEnumMeta):
    STATUS_UNKNOWN = "status_unknown"
    ACTIVE = "active"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)


class DNSZoneStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    ACTIVE = "active"
    PENDING = "pending"
    ERROR = "error"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class DSRecordAlgorithm(str, Enum, metaclass=StrEnumMeta):
    RSAMD5 = "rsamd5"
    DH = "dh"
    DSA = "dsa"
    RSASHA1 = "rsasha1"
    DSA_NSEC3_SHA1 = "dsa_nsec3_sha1"
    RSASHA1_NSEC3_SHA1 = "rsasha1_nsec3_sha1"
    RSASHA256 = "rsasha256"
    RSASHA512 = "rsasha512"
    ECC_GOST = "ecc_gost"
    ECDSAP256SHA256 = "ecdsap256sha256"
    ECDSAP384SHA384 = "ecdsap384sha384"
    ED25519 = "ed25519"
    ED448 = "ed448"

    def __str__(self) -> str:
        return str(self.value)


class DSRecordDigestType(str, Enum, metaclass=StrEnumMeta):
    SHA_1 = "sha_1"
    SHA_256 = "sha_256"
    GOST_R_34_11_94 = "gost_r_34_11_94"
    SHA_384 = "sha_384"

    def __str__(self) -> str:
        return str(self.value)


class DomainFeatureStatus(str, Enum, metaclass=StrEnumMeta):
    FEATURE_STATUS_UNKNOWN = "feature_status_unknown"
    ENABLING = "enabling"
    ENABLED = "enabled"
    DISABLING = "disabling"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)


class DomainRegistrationStatusTransferStatus(str, Enum, metaclass=StrEnumMeta):
    STATUS_UNKNOWN = "status_unknown"
    PENDING = "pending"
    WAITING_VOTE = "waiting_vote"
    REJECTED = "rejected"
    PROCESSING = "processing"
    DONE = "done"

    def __str__(self) -> str:
        return str(self.value)


class DomainStatus(str, Enum, metaclass=StrEnumMeta):
    STATUS_UNKNOWN = "status_unknown"
    ACTIVE = "active"
    CREATING = "creating"
    CREATE_ERROR = "create_error"
    RENEWING = "renewing"
    RENEW_ERROR = "renew_error"
    XFERING = "xfering"
    XFER_ERROR = "xfer_error"
    EXPIRED = "expired"
    EXPIRING = "expiring"
    UPDATING = "updating"
    CHECKING = "checking"
    LOCKED = "locked"
    DELETING = "deleting"

    def __str__(self) -> str:
        return str(self.value)


class HostStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    ACTIVE = "active"
    UPDATING = "updating"
    DELETING = "deleting"

    def __str__(self) -> str:
        return str(self.value)


class LinkedProduct(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_PRODUCT = "unknown_product"
    VPC = "vpc"

    def __str__(self) -> str:
        return str(self.value)


class ListContactsRequestRole(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ROLE = "unknown_role"
    OWNER = "owner"
    ADMINISTRATIVE = "administrative"
    TECHNICAL = "technical"

    def __str__(self) -> str:
        return str(self.value)


class ListDNSZoneRecordsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListDNSZonesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    DOMAIN_ASC = "domain_asc"
    DOMAIN_DESC = "domain_desc"
    SUBDOMAIN_ASC = "subdomain_asc"
    SUBDOMAIN_DESC = "subdomain_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListDomainsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    DOMAIN_ASC = "domain_asc"
    DOMAIN_DESC = "domain_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListRenewableDomainsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    DOMAIN_ASC = "domain_asc"
    DOMAIN_DESC = "domain_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListTasksRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    DOMAIN_DESC = "domain_desc"
    DOMAIN_ASC = "domain_asc"
    TYPE_ASC = "type_asc"
    TYPE_DESC = "type_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListTldsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class RawFormat(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_RAW_FORMAT = "unknown_raw_format"
    BIND = "bind"

    def __str__(self) -> str:
        return str(self.value)


class RecordHTTPServiceConfigStrategy(str, Enum, metaclass=StrEnumMeta):
    RANDOM = "random"
    HASHED = "hashed"
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)


class RecordType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    A = "a"
    AAAA = "aaaa"
    CNAME = "cname"
    TXT = "txt"
    SRV = "srv"
    TLSA = "tlsa"
    MX = "mx"
    NS = "ns"
    PTR = "ptr"
    CAA = "caa"
    ALIAS = "alias"
    LOC = "loc"
    SSHFP = "sshfp"
    HINFO = "hinfo"
    RP = "rp"
    URI = "uri"
    DS = "ds"
    NAPTR = "naptr"
    DNAME = "dname"
    SVCB = "svcb"
    HTTPS = "https"

    def __str__(self) -> str:
        return str(self.value)


class RenewableDomainStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    RENEWABLE = "renewable"
    LATE_RENEWEABLE = "late_reneweable"
    NOT_RENEWABLE = "not_renewable"

    def __str__(self) -> str:
        return str(self.value)


class SSLCertificateStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    NEW = "new"
    PENDING = "pending"
    SUCCESS = "success"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class TaskStatus(str, Enum, metaclass=StrEnumMeta):
    UNAVAILABLE = "unavailable"
    NEW = "new"
    WAITING_PAYMENT = "waiting_payment"
    PENDING = "pending"
    SUCCESS = "success"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class TaskType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    CREATE_DOMAIN = "create_domain"
    CREATE_EXTERNAL_DOMAIN = "create_external_domain"
    RENEW_DOMAIN = "renew_domain"
    TRANSFER_DOMAIN = "transfer_domain"
    TRADE_DOMAIN = "trade_domain"
    LOCK_DOMAIN_TRANSFER = "lock_domain_transfer"
    UNLOCK_DOMAIN_TRANSFER = "unlock_domain_transfer"
    ENABLE_DNSSEC = "enable_dnssec"
    DISABLE_DNSSEC = "disable_dnssec"
    UPDATE_DOMAIN = "update_domain"
    UPDATE_CONTACT = "update_contact"
    DELETE_DOMAIN = "delete_domain"
    CANCEL_TASK = "cancel_task"
    GENERATE_SSL_CERTIFICATE = "generate_ssl_certificate"
    RENEW_SSL_CERTIFICATE = "renew_ssl_certificate"
    SEND_MESSAGE = "send_message"
    DELETE_DOMAIN_EXPIRED = "delete_domain_expired"
    DELETE_EXTERNAL_DOMAIN = "delete_external_domain"
    CREATE_HOST = "create_host"
    UPDATE_HOST = "update_host"
    DELETE_HOST = "delete_host"
    MOVE_PROJECT = "move_project"
    TRANSFER_ONLINE_DOMAIN = "transfer_online_domain"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class RecordGeoIPConfigMatch:
    countries: List[str]

    continents: List[str]

    data: str


@dataclass
class RecordViewConfigView:
    subnet: str

    data: str


@dataclass
class RecordWeightedConfigWeightedIP:
    ip: str

    weight: int


@dataclass
class DSRecordPublicKey:
    key: str


@dataclass
class RecordGeoIPConfig:
    matches: List[RecordGeoIPConfigMatch]

    default: str


@dataclass
class RecordHTTPServiceConfig:
    ips: List[str]

    url: str

    strategy: RecordHTTPServiceConfigStrategy

    must_contain: Optional[str]

    user_agent: Optional[str]


@dataclass
class RecordViewConfig:
    views: List[RecordViewConfigView]


@dataclass
class RecordWeightedConfig:
    weighted_ips: List[RecordWeightedConfigWeightedIP]


@dataclass
class ContactExtensionFRAssociationInfo:
    publication_jo_page: int

    publication_jo: Optional[datetime]


@dataclass
class ContactExtensionFRCodeAuthAfnicInfo:
    code_auth_afnic: str


@dataclass
class ContactExtensionFRDunsInfo:
    duns_id: str

    local_id: str


@dataclass
class ContactExtensionFRIndividualInfo:
    whois_opt_in: bool


@dataclass
class ContactExtensionFRTrademarkInfo:
    trademark_inpi: str


@dataclass
class DSRecordDigest:
    type_: DSRecordDigestType

    digest: str

    public_key: Optional[DSRecordPublicKey]


@dataclass
class Record:
    data: str

    name: str

    priority: int

    ttl: int

    type_: RecordType

    id: str

    comment: Optional[str]

    geo_ip_config: Optional[RecordGeoIPConfig]

    http_service_config: Optional[RecordHTTPServiceConfig]

    weighted_config: Optional[RecordWeightedConfig]

    view_config: Optional[RecordViewConfig]


@dataclass
class RecordIdentifier:
    name: str

    type_: RecordType

    data: Optional[str]

    ttl: Optional[int]


@dataclass
class ContactExtensionEU:
    european_citizenship: str


@dataclass
class ContactExtensionFR:
    mode: ContactExtensionFRMode

    individual_info: Optional[ContactExtensionFRIndividualInfo]

    duns_info: Optional[ContactExtensionFRDunsInfo]

    association_info: Optional[ContactExtensionFRAssociationInfo]

    trademark_info: Optional[ContactExtensionFRTrademarkInfo]

    code_auth_afnic_info: Optional[ContactExtensionFRCodeAuthAfnicInfo]


@dataclass
class ContactExtensionNL:
    legal_form: ContactExtensionNLLegalForm

    legal_form_registration_number: str


@dataclass
class ContactQuestion:
    question: str

    answer: str


@dataclass
class TldOffer:
    action: str

    operation_path: str

    price: Optional[Money]


@dataclass
class DSRecord:
    key_id: int

    algorithm: DSRecordAlgorithm

    digest: Optional[DSRecordDigest]

    public_key: Optional[DSRecordPublicKey]


@dataclass
class RecordChangeAdd:
    records: List[Record]


@dataclass
class RecordChangeClear:
    pass


@dataclass
class RecordChangeDelete:
    id: Optional[str]

    id_fields: Optional[RecordIdentifier]


@dataclass
class RecordChangeSet:
    records: List[Record]

    id: Optional[str]

    id_fields: Optional[RecordIdentifier]


@dataclass
class ImportRawDNSZoneRequestTsigKey:
    name: str

    key: str

    algorithm: str


@dataclass
class Contact:
    id: str

    legal_form: ContactLegalForm

    firstname: str

    lastname: str

    company_name: str

    email: str

    email_alt: str

    phone_number: str

    fax_number: str

    address_line_1: str

    address_line_2: str

    zip: str

    city: str

    country: str

    vat_identification_code: str

    company_identification_code: str

    lang: StdLanguageCode

    resale: bool

    whois_opt_in: bool

    questions: Optional[List[ContactQuestion]]

    extension_fr: Optional[ContactExtensionFR]

    extension_eu: Optional[ContactExtensionEU]

    email_status: ContactEmailStatus

    state: str

    status: ContactStatus

    extension_nl: Optional[ContactExtensionNL]


@dataclass
class ContactRolesRoles:
    is_owner: bool

    is_administrative: bool

    is_technical: bool


@dataclass
class DomainRegistrationStatusExternalDomain:
    validation_token: str


@dataclass
class DomainRegistrationStatusTransfer:
    status: DomainRegistrationStatusTransferStatus

    vote_current_owner: bool

    vote_new_owner: bool


@dataclass
class Tld:
    name: str

    dnssec_support: bool

    duration_in_years_min: int

    duration_in_years_max: int

    idn_support: bool

    offers: Dict[str, TldOffer]

    specifications: Dict[str, str]


@dataclass
class NewContact:
    legal_form: ContactLegalForm

    firstname: str

    lastname: str

    email: str

    company_name: Optional[str]

    email_alt: Optional[str]

    phone_number: str

    address_line_1: str

    zip: str

    city: str

    country: str

    fax_number: Optional[str]

    address_line_2: Optional[str]

    vat_identification_code: Optional[str]

    company_identification_code: Optional[str]

    lang: StdLanguageCode

    resale: bool

    whois_opt_in: bool

    questions: Optional[List[ContactQuestion]]

    extension_fr: Optional[ContactExtensionFR]

    extension_eu: Optional[ContactExtensionEU]

    state: Optional[str]

    extension_nl: Optional[ContactExtensionNL]


@dataclass
class CheckContactsCompatibilityResponseContactCheckResult:
    compatible: bool

    error_message: Optional[str]


@dataclass
class DNSZone:
    domain: str

    subdomain: str

    ns: List[str]

    ns_default: List[str]

    ns_master: List[str]

    status: DNSZoneStatus

    project_id: str

    linked_products: List[LinkedProduct]

    message: Optional[str]

    updated_at: Optional[datetime]


@dataclass
class DomainDNSSEC:
    status: DomainFeatureStatus

    ds_records: List[DSRecord]


@dataclass
class RecordChange:
    add: Optional[RecordChangeAdd]

    set_: Optional[RecordChangeSet]

    delete: Optional[RecordChangeDelete]

    clear: Optional[RecordChangeClear]


@dataclass
class ImportProviderDNSZoneRequestOnlineV1:
    token: str


@dataclass
class ImportRawDNSZoneRequestAXFRSource:
    name_server: str

    tsig_key: Optional[ImportRawDNSZoneRequestTsigKey]


@dataclass
class ImportRawDNSZoneRequestBindSource:
    content: str


@dataclass
class ContactRoles:
    roles: Dict[str, ContactRolesRoles]

    contact: Optional[Contact]


@dataclass
class Nameserver:
    name: str

    ip: List[str]


@dataclass
class DNSZoneVersion:
    id: str

    created_at: Optional[datetime]


@dataclass
class Host:
    domain: str

    name: str

    ips: List[str]

    status: HostStatus


@dataclass
class DomainSummary:
    domain: str

    project_id: str

    auto_renew_status: DomainFeatureStatus

    dnssec_status: DomainFeatureStatus

    epp_code: List[str]

    registrar: str

    is_external: bool

    expired_at: Optional[datetime]

    updated_at: Optional[datetime]

    status: DomainStatus

    organization_id: str

    pending_trade: bool

    created_at: Optional[datetime]

    external_domain_registration_status: Optional[
        DomainRegistrationStatusExternalDomain
    ]

    transfer_registration_status: Optional[DomainRegistrationStatusTransfer]


@dataclass
class RenewableDomain:
    domain: str

    project_id: str

    organization_id: str

    status: RenewableDomainStatus

    renewable_duration_in_years: Optional[int]

    expired_at: Optional[datetime]

    limit_renew_at: Optional[datetime]

    limit_redemption_at: Optional[datetime]

    estimated_delete_at: Optional[datetime]

    tld: Optional[Tld]


@dataclass
class SSLCertificate:
    dns_zone: str

    alternative_dns_zones: List[str]

    status: SSLCertificateStatus

    private_key: str

    certificate_chain: str

    created_at: Optional[datetime]

    expired_at: Optional[datetime]


@dataclass
class Task:
    id: str
    """
    The unique identifier of the task.
    """

    project_id: str
    """
    The project ID associated to the task.
    """

    organization_id: str
    """
    The organization ID associated to the task.
    """

    type_: TaskType
    """
    The type of the task.
    """

    status: TaskStatus
    """
    The status of the task.
    """

    domain: Optional[str]
    """
    The domain name associated to the task.
    """

    started_at: Optional[datetime]
    """
    Start date of the task.
    """

    updated_at: Optional[datetime]
    """
    Last update of the task.
    """

    message: Optional[str]
    """
    Error message associated to the task.
    """

    contact_identifier: Optional[str]
    """
    Human-friendly contact identifier used when the task concerns a contact.
    """


@dataclass
class TransferInDomainRequestTransferRequest:
    domain: str

    auth_code: str


@dataclass
class UpdateContactRequestQuestion:
    question: Optional[str]

    answer: Optional[str]


@dataclass
class AvailableDomain:
    domain: str

    available: bool

    tld: Optional[Tld]


@dataclass
class CheckContactsCompatibilityResponse:
    compatible: bool

    owner_check_result: Optional[CheckContactsCompatibilityResponseContactCheckResult]

    administrative_check_result: Optional[
        CheckContactsCompatibilityResponseContactCheckResult
    ]

    technical_check_result: Optional[
        CheckContactsCompatibilityResponseContactCheckResult
    ]


@dataclass
class ClearDNSZoneRecordsRequest:
    dns_zone: str
    """
    DNS zone to clear.
    """


@dataclass
class ClearDNSZoneRecordsResponse:
    pass


@dataclass
class CloneDNSZoneRequest:
    dns_zone: str
    """
    DNS zone to clone.
    """

    dest_dns_zone: str
    """
    Destination DNS zone in which to clone the chosen DNS zone.
    """

    overwrite: bool
    """
    Specifies whether or not the destination DNS zone will be overwritten.
    """

    project_id: Optional[str]
    """
    Project ID of the destination DNS zone.
    """


@dataclass
class CreateDNSZoneRequest:
    domain: str
    """
    Domain in which to crreate the DNS zone.
    """

    subdomain: str
    """
    Subdomain of the DNS zone to create.
    """

    project_id: Optional[str]
    """
    Project ID in which to create the DNS zone.
    """


@dataclass
class CreateSSLCertificateRequest:
    dns_zone: str

    alternative_dns_zones: Optional[List[str]]


@dataclass
class DeleteDNSZoneRequest:
    dns_zone: str
    """
    DNS zone to delete.
    """

    project_id: Optional[str]
    """
    Project ID of the DNS zone to delete.
    """


@dataclass
class DeleteDNSZoneResponse:
    pass


@dataclass
class DeleteDNSZoneTsigKeyRequest:
    dns_zone: str


@dataclass
class DeleteExternalDomainResponse:
    pass


@dataclass
class DeleteSSLCertificateRequest:
    dns_zone: str


@dataclass
class DeleteSSLCertificateResponse:
    pass


@dataclass
class Domain:
    domain: str

    organization_id: str

    project_id: str

    auto_renew_status: DomainFeatureStatus
    """
    Status of the automatic renewal of the domain.
    """

    epp_code: List[str]
    """
    List of the domain's EPP codes.
    """

    dnssec: Optional[DomainDNSSEC]
    """
    Status of the DNSSEC configuration of the domain.
    """

    expired_at: Optional[datetime]
    """
    Date of expiration of the domain.
    """

    updated_at: Optional[datetime]
    """
    Domain's last modification date.
    """

    registrar: str

    is_external: bool
    """
    Indicates whether Scaleway is the domain's registrar.
    """

    status: DomainStatus
    """
    Status of the domain.
    """

    dns_zones: List[DNSZone]
    """
    List of the domain's DNS zones.
    """

    linked_products: List[LinkedProduct]
    """
    List of Scaleway resources linked to the domain.
    """

    pending_trade: bool
    """
    Indicates if a trade is ongoing.
    """

    owner_contact: Optional[Contact]
    """
    Contact information of the domain's owner.
    """

    technical_contact: Optional[Contact]
    """
    Contact information of the domain's technical contact.
    """

    administrative_contact: Optional[Contact]
    """
    Contact information of the domain's administrative contact.
    """

    tld: Optional[Tld]
    """
    Domain's TLD information.
    """

    external_domain_registration_status: Optional[
        DomainRegistrationStatusExternalDomain
    ]

    transfer_registration_status: Optional[DomainRegistrationStatusTransfer]


@dataclass
class ExportRawDNSZoneRequest:
    dns_zone: str
    """
    DNS zone to export.
    """

    format: Optional[RawFormat]
    """
    DNS zone format.
    """


@dataclass
class GetDNSZoneTsigKeyRequest:
    dns_zone: str


@dataclass
class GetDNSZoneTsigKeyResponse:
    name: str

    key: str

    algorithm: str


@dataclass
class GetDNSZoneVersionDiffRequest:
    dns_zone_version_id: str


@dataclass
class GetDNSZoneVersionDiffResponse:
    changes: List[RecordChange]


@dataclass
class GetDomainAuthCodeResponse:
    auth_code: str


@dataclass
class GetSSLCertificateRequest:
    dns_zone: str


@dataclass
class ImportProviderDNSZoneRequest:
    dns_zone: str

    online_v1: Optional[ImportProviderDNSZoneRequestOnlineV1]


@dataclass
class ImportProviderDNSZoneResponse:
    records: List[Record]


@dataclass
class ImportRawDNSZoneRequest:
    dns_zone: str
    """
    DNS zone to import.
    """

    content: Optional[str]

    project_id: Optional[str]

    format: Optional[RawFormat]

    bind_source: Optional[ImportRawDNSZoneRequestBindSource]

    axfr_source: Optional[ImportRawDNSZoneRequestAXFRSource]


@dataclass
class ImportRawDNSZoneResponse:
    records: List[Record]


@dataclass
class ListContactsResponse:
    total_count: int

    contacts: List[ContactRoles]


@dataclass
class ListDNSZoneNameserversRequest:
    project_id: Optional[str]
    """
    Project ID on which to filter the returned DNS zone name servers.
    """

    dns_zone: str
    """
    DNS zone on which to filter the returned DNS zone name servers.
    """


@dataclass
class ListDNSZoneNameserversResponse:
    ns: List[Nameserver]
    """
    DNS zone name servers returned.
    """


@dataclass
class ListDNSZoneRecordsRequest:
    project_id: Optional[str]
    """
    Project ID on which to filter the returned DNS zone records.
    """

    order_by: Optional[ListDNSZoneRecordsRequestOrderBy]
    """
    Sort order of the returned DNS zone records.
    """

    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Maximum number of DNS zone records per page.
    """

    dns_zone: str
    """
    DNS zone on which to filter the returned DNS zone records.
    """

    name: str
    """
    Name on which to filter the returned DNS zone records.
    """

    type_: Optional[RecordType]
    """
    Record type on which to filter the returned DNS zone records.
    """

    id: Optional[str]
    """
    Record ID on which to filter the returned DNS zone records.
    """


@dataclass
class ListDNSZoneRecordsResponse:
    total_count: int
    """
    Total number of DNS zone records.
    """

    records: List[Record]
    """
    Paginated returned DNS zone records.
    """


@dataclass
class ListDNSZoneVersionRecordsRequest:
    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Maximum number of DNS zones versions records per page.
    """

    dns_zone_version_id: str


@dataclass
class ListDNSZoneVersionRecordsResponse:
    total_count: int
    """
    Total number of DNS zones versions records.
    """

    records: List[Record]


@dataclass
class ListDNSZoneVersionsRequest:
    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Maximum number of DNS zones versions per page.
    """

    dns_zone: str


@dataclass
class ListDNSZoneVersionsResponse:
    total_count: int
    """
    Total number of DNS zones versions.
    """

    versions: List[DNSZoneVersion]


@dataclass
class ListDNSZonesRequest:
    domain: str
    """
    Domain on which to filter the returned DNS zones.
    """

    organization_id: Optional[str]
    """
    Organization ID on which to filter the returned DNS zones.
    """

    project_id: Optional[str]
    """
    Project ID on which to filter the returned DNS zones.
    """

    order_by: Optional[ListDNSZonesRequestOrderBy]
    """
    Sort order of the returned DNS zones.
    """

    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Maximum number of DNS zones to return per page.
    """

    dns_zone: Optional[str]
    """
    DNS zone on which to filter the returned DNS zones.
    """

    dns_zones: Optional[List[str]]
    """
    DNS zones on which to filter the returned DNS zones.
    """

    created_after: Optional[datetime]
    """
    Only list DNS zones created after this date.
    """

    created_before: Optional[datetime]
    """
    Only list DNS zones created before this date.
    """

    updated_after: Optional[datetime]
    """
    Only list DNS zones updated after this date.
    """

    updated_before: Optional[datetime]
    """
    Only list DNS zones updated before this date.
    """


@dataclass
class ListDNSZonesResponse:
    total_count: int
    """
    Total number of DNS zones matching the requested criteria.
    """

    dns_zones: List[DNSZone]
    """
    Paginated returned DNS zones.
    """


@dataclass
class ListDomainHostsResponse:
    total_count: int

    hosts: List[Host]


@dataclass
class ListDomainsResponse:
    total_count: int

    domains: List[DomainSummary]


@dataclass
class ListRenewableDomainsResponse:
    total_count: int

    domains: List[RenewableDomain]


@dataclass
class ListSSLCertificatesRequest:
    dns_zone: str

    page: Optional[int]

    page_size: Optional[int]

    project_id: Optional[str]


@dataclass
class ListSSLCertificatesResponse:
    total_count: int

    certificates: List[SSLCertificate]


@dataclass
class ListTasksResponse:
    total_count: int

    tasks: List[Task]


@dataclass
class ListTldsResponse:
    tlds: List[Tld]
    """
    Array of TLDs.
    """

    total_count: int
    """
    Total count of TLDs returned.
    """


@dataclass
class OrderResponse:
    domains: List[str]

    organization_id: str

    project_id: str

    task_id: str

    created_at: Optional[datetime]


@dataclass
class RefreshDNSZoneRequest:
    dns_zone: str
    """
    DNS zone to refresh.
    """

    recreate_dns_zone: bool
    """
    Specifies whether or not to recreate the DNS zone.
    """

    recreate_sub_dns_zone: bool
    """
    Specifies whether or not to recreate the sub DNS zone.
    """


@dataclass
class RefreshDNSZoneResponse:
    dns_zones: List[DNSZone]
    """
    DNS zones returned.
    """


@dataclass
class RegisterExternalDomainResponse:
    domain: str

    organization_id: str

    validation_token: str

    project_id: str

    created_at: Optional[datetime]


@dataclass
class RegistrarApiBuyDomainsRequest:
    domains: List[str]

    duration_in_years: int

    project_id: Optional[str]

    owner_contact_id: Optional[str]

    owner_contact: Optional[NewContact]

    administrative_contact_id: Optional[str]

    administrative_contact: Optional[NewContact]

    technical_contact_id: Optional[str]

    technical_contact: Optional[NewContact]


@dataclass
class RegistrarApiCheckContactsCompatibilityRequest:
    domains: Optional[List[str]]

    tlds: Optional[List[str]]

    owner_contact_id: Optional[str]

    owner_contact: Optional[NewContact]

    administrative_contact_id: Optional[str]

    administrative_contact: Optional[NewContact]

    technical_contact_id: Optional[str]

    technical_contact: Optional[NewContact]


@dataclass
class RegistrarApiCreateDomainHostRequest:
    domain: str

    name: str

    ips: Optional[List[str]]


@dataclass
class RegistrarApiDeleteDomainHostRequest:
    domain: str

    name: str


@dataclass
class RegistrarApiDeleteExternalDomainRequest:
    domain: str


@dataclass
class RegistrarApiDisableDomainAutoRenewRequest:
    domain: str


@dataclass
class RegistrarApiDisableDomainDNSSECRequest:
    domain: str


@dataclass
class RegistrarApiEnableDomainAutoRenewRequest:
    domain: str


@dataclass
class RegistrarApiEnableDomainDNSSECRequest:
    domain: str

    ds_record: Optional[DSRecord]


@dataclass
class RegistrarApiGetContactRequest:
    contact_id: str


@dataclass
class RegistrarApiGetDomainAuthCodeRequest:
    domain: str


@dataclass
class RegistrarApiGetDomainRequest:
    domain: str


@dataclass
class RegistrarApiListContactsRequest:
    page: Optional[int]

    page_size: Optional[int]

    domain: Optional[str]

    project_id: Optional[str]

    organization_id: Optional[str]

    role: Optional[ListContactsRequestRole]

    email_status: Optional[ContactEmailStatus]


@dataclass
class RegistrarApiListDomainHostsRequest:
    page: Optional[int]

    page_size: Optional[int]

    domain: str


@dataclass
class RegistrarApiListDomainsRequest:
    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListDomainsRequestOrderBy]

    registrar: Optional[str]

    status: Optional[DomainStatus]

    project_id: Optional[str]

    organization_id: Optional[str]

    is_external: Optional[bool]

    domain: Optional[str]


@dataclass
class RegistrarApiListRenewableDomainsRequest:
    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListRenewableDomainsRequestOrderBy]

    project_id: Optional[str]

    organization_id: Optional[str]


@dataclass
class RegistrarApiListTasksRequest:
    page: Optional[int]

    page_size: Optional[int]

    project_id: Optional[str]

    organization_id: Optional[str]

    domain: Optional[str]

    types: Optional[List[TaskType]]

    statuses: Optional[List[TaskStatus]]

    order_by: Optional[ListTasksRequestOrderBy]


@dataclass
class RegistrarApiListTldsRequest:
    tlds: Optional[List[str]]
    """
    Array of TLDs to return.
    """

    page: Optional[int]
    """
    Page number for the returned Projects.
    """

    page_size: Optional[int]
    """
    Maximum number of Project per page.
    """

    order_by: Optional[ListTldsRequestOrderBy]
    """
    Sort order of the returned TLDs.
    """


@dataclass
class RegistrarApiLockDomainTransferRequest:
    domain: str


@dataclass
class RegistrarApiRegisterExternalDomainRequest:
    domain: str

    project_id: Optional[str]


@dataclass
class RegistrarApiRenewDomainsRequest:
    domains: List[str]

    duration_in_years: int

    force_late_renewal: Optional[bool]


@dataclass
class RegistrarApiSearchAvailableDomainsRequest:
    domains: List[str]
    """
    A list of domain to search, TLD is optional.
    """

    strict_search: bool
    """
    Search exact match.
    """

    tlds: Optional[List[str]]
    """
    Array of tlds to search on.
    """


@dataclass
class RegistrarApiTradeDomainRequest:
    domain: str

    project_id: Optional[str]

    new_owner_contact_id: Optional[str]

    new_owner_contact: Optional[NewContact]


@dataclass
class RegistrarApiTransferInDomainRequest:
    domains: List[TransferInDomainRequestTransferRequest]

    project_id: Optional[str]

    owner_contact_id: Optional[str]

    owner_contact: Optional[NewContact]

    administrative_contact_id: Optional[str]

    administrative_contact: Optional[NewContact]

    technical_contact_id: Optional[str]

    technical_contact: Optional[NewContact]


@dataclass
class RegistrarApiUnlockDomainTransferRequest:
    domain: str


@dataclass
class RegistrarApiUpdateContactRequest:
    contact_id: str

    email: Optional[str]

    email_alt: Optional[str]

    phone_number: Optional[str]

    fax_number: Optional[str]

    address_line_1: Optional[str]

    address_line_2: Optional[str]

    zip: Optional[str]

    city: Optional[str]

    country: Optional[str]

    vat_identification_code: Optional[str]

    company_identification_code: Optional[str]

    lang: Optional[StdLanguageCode]

    resale: Optional[bool]

    questions: Optional[List[UpdateContactRequestQuestion]]

    extension_fr: Optional[ContactExtensionFR]

    extension_eu: Optional[ContactExtensionEU]

    whois_opt_in: Optional[bool]

    state: Optional[str]

    extension_nl: Optional[ContactExtensionNL]


@dataclass
class RegistrarApiUpdateDomainHostRequest:
    domain: str

    name: str

    ips: Optional[List[str]]


@dataclass
class RegistrarApiUpdateDomainRequest:
    domain: str

    technical_contact_id: Optional[str]

    technical_contact: Optional[NewContact]

    owner_contact_id: Optional[str]

    owner_contact: Optional[NewContact]

    administrative_contact_id: Optional[str]

    administrative_contact: Optional[NewContact]


@dataclass
class RestoreDNSZoneVersionRequest:
    dns_zone_version_id: str


@dataclass
class RestoreDNSZoneVersionResponse:
    pass


@dataclass
class SearchAvailableDomainsResponse:
    available_domains: List[AvailableDomain]
    """
    Array of available domains.
    """


@dataclass
class UpdateDNSZoneNameserversRequest:
    dns_zone: str
    """
    DNS zone in which to update the DNS zone name servers.
    """

    ns: List[Nameserver]
    """
    New DNS zone name servers.
    """


@dataclass
class UpdateDNSZoneNameserversResponse:
    ns: List[Nameserver]
    """
    DNS zone name servers returned.
    """


@dataclass
class UpdateDNSZoneRecordsRequest:
    dns_zone: str
    """
    DNS zone in which to update the DNS zone records.
    """

    changes: List[RecordChange]
    """
    Changes made to the records.
    """

    disallow_new_zone_creation: bool
    """
    Disable the creation of the target zone if it does not exist. Target zone creation is disabled by default.
    """

    return_all_records: Optional[bool]
    """
    Specifies whether or not to return all the records.
    """

    serial: Optional[int]
    """
    Use the provided serial (0) instead of the auto-increment serial.
    """


@dataclass
class UpdateDNSZoneRecordsResponse:
    records: List[Record]
    """
    DNS zone records returned.
    """


@dataclass
class UpdateDNSZoneRequest:
    dns_zone: str
    """
    DNS zone to update.
    """

    new_dns_zone: Optional[str]
    """
    Name of the new DNS zone to create.
    """

    project_id: Optional[str]
    """
    Project ID in which to create the new DNS zone.
    """
