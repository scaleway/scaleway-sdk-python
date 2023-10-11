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

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class RecordGeoIPConfigMatch:
    data: str

    continents: List[str]

    countries: List[str]


@dataclass
class RecordViewConfigView:
    data: str

    subnet: str


@dataclass
class RecordWeightedConfigWeightedIP:
    weight: int

    ip: str


@dataclass
class DSRecordPublicKey:
    key: str


@dataclass
class RecordGeoIPConfig:
    default: str

    matches: List[RecordGeoIPConfigMatch]


@dataclass
class RecordHTTPServiceConfig:
    strategy: RecordHTTPServiceConfigStrategy

    url: str

    ips: List[str]

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
    local_id: str

    duns_id: str


@dataclass
class ContactExtensionFRIndividualInfo:
    whois_opt_in: bool


@dataclass
class ContactExtensionFRTrademarkInfo:
    trademark_inpi: str


@dataclass
class DSRecordDigest:
    public_key: DSRecordPublicKey

    digest: str

    type_: DSRecordDigestType


@dataclass
class Record:
    id: str

    type_: RecordType

    ttl: int

    priority: int

    name: str

    data: str

    comment: Optional[str]

    geo_ip_config: Optional[RecordGeoIPConfig]

    http_service_config: Optional[RecordHTTPServiceConfig]

    weighted_config: Optional[RecordWeightedConfig]

    view_config: Optional[RecordViewConfig]


@dataclass
class RecordIdentifier:
    type_: RecordType

    name: str

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
    legal_form_registration_number: str

    legal_form: ContactExtensionNLLegalForm


@dataclass
class ContactQuestion:
    answer: str

    question: str


@dataclass
class TldOffer:
    operation_path: str

    action: str

    price: Optional[Money]


@dataclass
class DSRecord:
    algorithm: DSRecordAlgorithm

    key_id: int

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
    algorithm: str

    key: str

    name: str


@dataclass
class Contact:
    resale: bool

    legal_form: ContactLegalForm

    company_name: str

    country: str

    id: str

    extension_fr: ContactExtensionFR

    email_alt: str

    address_line_2: str

    firstname: str

    email: str

    company_identification_code: str

    zip: str

    extension_nl: ContactExtensionNL

    state: str

    fax_number: str

    phone_number: str

    address_line_1: str

    vat_identification_code: str

    lang: StdLanguageCode

    lastname: str

    email_status: ContactEmailStatus

    whois_opt_in: bool

    extension_eu: ContactExtensionEU

    city: str

    questions: Optional[List[ContactQuestion]]


@dataclass
class ContactRolesRoles:
    is_technical: bool

    is_administrative: bool

    is_owner: bool


@dataclass
class DomainRegistrationStatusExternalDomain:
    validation_token: str


@dataclass
class DomainRegistrationStatusTransfer:
    vote_new_owner: bool

    vote_current_owner: bool

    status: DomainRegistrationStatusTransferStatus


@dataclass
class Tld:
    specifications: Dict[str, str]

    offers: Dict[str, TldOffer]

    idn_support: bool

    duration_in_years_max: int

    duration_in_years_min: int

    dnssec_support: bool

    name: str


@dataclass
class NewContact:
    city: str

    legal_form: ContactLegalForm

    extension_fr: ContactExtensionFR

    address_line_1: str

    extension_eu: ContactExtensionEU

    resale: bool

    whois_opt_in: bool

    email: str

    extension_nl: ContactExtensionNL

    lastname: str

    firstname: str

    country: str

    lang: StdLanguageCode

    phone_number: str

    zip: str

    company_identification_code: Optional[str]

    vat_identification_code: Optional[str]

    questions: Optional[List[ContactQuestion]]

    address_line_2: Optional[str]

    fax_number: Optional[str]

    email_alt: Optional[str]

    state: Optional[str]

    company_name: Optional[str]


@dataclass
class CheckContactsCompatibilityResponseContactCheckResult:
    compatible: bool

    error_message: Optional[str]


@dataclass
class DNSZone:
    project_id: str

    status: DNSZoneStatus

    ns_master: List[str]

    ns_default: List[str]

    ns: List[str]

    subdomain: str

    domain: str

    message: Optional[str]

    updated_at: Optional[datetime]


@dataclass
class DomainDNSSEC:
    ds_records: List[DSRecord]

    status: DomainFeatureStatus


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
    tsig_key: ImportRawDNSZoneRequestTsigKey

    name_server: str


@dataclass
class ImportRawDNSZoneRequestBindSource:
    content: str


@dataclass
class ContactRoles:
    roles: Dict[str, ContactRolesRoles]

    contact: Contact


@dataclass
class Nameserver:
    ip: List[str]

    name: str


@dataclass
class DNSZoneVersion:
    id: str

    created_at: Optional[datetime]


@dataclass
class Host:
    status: HostStatus

    ips: List[str]

    name: str

    domain: str


@dataclass
class DomainSummary:
    organization_id: str

    status: DomainStatus

    is_external: bool

    registrar: str

    epp_code: List[str]

    dnssec_status: DomainFeatureStatus

    auto_renew_status: DomainFeatureStatus

    project_id: str

    domain: str

    expired_at: Optional[datetime]

    updated_at: Optional[datetime]

    external_domain_registration_status: Optional[
        DomainRegistrationStatusExternalDomain
    ]

    transfer_registration_status: Optional[DomainRegistrationStatusTransfer]


@dataclass
class RenewableDomain:
    tld: Tld

    status: RenewableDomainStatus

    organization_id: str

    project_id: str

    domain: str

    renewable_duration_in_years: Optional[int]

    expired_at: Optional[datetime]

    limit_renew_at: Optional[datetime]

    limit_redemption_at: Optional[datetime]

    estimated_delete_at: Optional[datetime]


@dataclass
class SSLCertificate:
    certificate_chain: str

    private_key: str

    status: SSLCertificateStatus

    alternative_dns_zones: List[str]

    dns_zone: str

    created_at: Optional[datetime]

    expired_at: Optional[datetime]


@dataclass
class Task:
    status: TaskStatus

    type_: TaskType

    organization_id: str

    project_id: str

    id: str

    domain: Optional[str]

    started_at: Optional[datetime]

    updated_at: Optional[datetime]

    message: Optional[str]


@dataclass
class TransferInDomainRequestTransferRequest:
    auth_code: str

    domain: str


@dataclass
class UpdateContactRequestQuestion:
    question: Optional[str]

    answer: Optional[str]


@dataclass
class AvailableDomain:
    tld: Tld

    available: bool

    domain: str


@dataclass
class CheckContactsCompatibilityResponse:
    technical_check_result: CheckContactsCompatibilityResponseContactCheckResult

    administrative_check_result: CheckContactsCompatibilityResponseContactCheckResult

    owner_check_result: CheckContactsCompatibilityResponseContactCheckResult

    compatible: bool


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
    overwrite: bool
    """
    Specifies whether or not the destination DNS zone will be overwritten.
    """

    dest_dns_zone: str
    """
    Destination DNS zone in which to clone the chosen DNS zone.
    """

    dns_zone: str
    """
    DNS zone to clone.
    """

    project_id: Optional[str]
    """
    Project ID of the destination DNS zone.
    """


@dataclass
class CreateDNSZoneRequest:
    subdomain: str
    """
    Subdomain of the DNS zone to create.
    """

    domain: str
    """
    Domain in which to crreate the DNS zone.
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
    dns_zones: List[DNSZone]

    status: DomainStatus

    is_external: bool

    domain: str

    administrative_contact: Contact

    technical_contact: Contact

    epp_code: List[str]

    dnssec: DomainDNSSEC

    auto_renew_status: DomainFeatureStatus

    project_id: str

    organization_id: str

    owner_contact: Contact

    tld: Tld

    registrar: str

    updated_at: Optional[datetime]

    expired_at: Optional[datetime]

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
    algorithm: str

    key: str

    name: str


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
    contacts: List[ContactRoles]

    total_count: int


@dataclass
class ListDNSZoneNameserversRequest:
    dns_zone: str
    """
    DNS zone on which to filter the returned DNS zone name servers.
    """

    project_id: Optional[str]
    """
    Project ID on which to filter the returned DNS zone name servers.
    """


@dataclass
class ListDNSZoneNameserversResponse:
    ns: List[Nameserver]
    """
    DNS zone name servers returned.
    """


@dataclass
class ListDNSZoneRecordsRequest:
    name: str
    """
    Name on which to filter the returned DNS zone records.
    """

    dns_zone: str
    """
    DNS zone on which to filter the returned DNS zone records.
    """

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
    records: List[Record]
    """
    Paginated returned DNS zone records.
    """

    total_count: int
    """
    Total number of DNS zone records.
    """


@dataclass
class ListDNSZoneVersionRecordsRequest:
    dns_zone_version_id: str

    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Maximum number of DNS zones versions records per page.
    """


@dataclass
class ListDNSZoneVersionRecordsResponse:
    records: List[Record]

    total_count: int
    """
    Total number of DNS zones versions records.
    """


@dataclass
class ListDNSZoneVersionsRequest:
    dns_zone: str

    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int]
    """
    Maximum number of DNS zones versions per page.
    """


@dataclass
class ListDNSZoneVersionsResponse:
    versions: List[DNSZoneVersion]

    total_count: int
    """
    Total number of DNS zones versions.
    """


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
    dns_zones: List[DNSZone]
    """
    Paginated returned DNS zones.
    """

    total_count: int
    """
    Total number of DNS zones matching the requested criteria.
    """


@dataclass
class ListDomainHostsResponse:
    hosts: List[Host]

    total_count: int


@dataclass
class ListDomainsResponse:
    domains: List[DomainSummary]

    total_count: int


@dataclass
class ListRenewableDomainsResponse:
    domains: List[RenewableDomain]

    total_count: int


@dataclass
class ListSSLCertificatesRequest:
    dns_zone: str

    page: Optional[int]

    page_size: Optional[int]

    project_id: Optional[str]


@dataclass
class ListSSLCertificatesResponse:
    certificates: List[SSLCertificate]

    total_count: int


@dataclass
class ListTasksResponse:
    tasks: List[Task]

    total_count: int


@dataclass
class ListTldsResponse:
    total_count: int
    """
    Total count of TLDs returned.
    """

    tlds: List[Tld]
    """
    Array of TLDs.
    """


@dataclass
class OrderResponse:
    task_id: str

    project_id: str

    organization_id: str

    domains: List[str]

    created_at: Optional[datetime]


@dataclass
class RefreshDNSZoneRequest:
    recreate_sub_dns_zone: bool
    """
    Specifies whether or not to recreate the sub DNS zone.
    """

    recreate_dns_zone: bool
    """
    Specifies whether or not to recreate the DNS zone.
    """

    dns_zone: str
    """
    DNS zone to refresh.
    """


@dataclass
class RefreshDNSZoneResponse:
    dns_zones: List[DNSZone]
    """
    DNS zones returned.
    """


@dataclass
class RegisterExternalDomainResponse:
    project_id: str

    validation_token: str

    organization_id: str

    domain: str

    created_at: Optional[datetime]


@dataclass
class RegistrarApiBuyDomainsRequest:
    duration_in_years: int

    domains: Optional[List[str]]

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
    name: str

    domain: str

    ips: Optional[List[str]]


@dataclass
class RegistrarApiDeleteDomainHostRequest:
    name: str

    domain: str


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
    ds_record: DSRecord

    domain: str


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
    domain: str

    page: Optional[int]

    page_size: Optional[int]


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
    duration_in_years: int

    domains: Optional[List[str]]

    force_late_renewal: Optional[bool]


@dataclass
class RegistrarApiSearchAvailableDomainsRequest:
    strict_search: bool
    """
    Search exact match.
    """

    domains: Optional[List[str]]
    """
    A list of domain to search, TLD is optional.
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
    domains: Optional[List[TransferInDomainRequestTransferRequest]]

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
    extension_fr: ContactExtensionFR

    extension_eu: ContactExtensionEU

    extension_nl: ContactExtensionNL

    contact_id: str

    address_line_1: Optional[str]

    company_identification_code: Optional[str]

    address_line_2: Optional[str]

    zip: Optional[str]

    city: Optional[str]

    country: Optional[str]

    vat_identification_code: Optional[str]

    fax_number: Optional[str]

    lang: Optional[StdLanguageCode]

    resale: Optional[bool]

    questions: Optional[List[UpdateContactRequestQuestion]]

    phone_number: Optional[str]

    email_alt: Optional[str]

    whois_opt_in: Optional[bool]

    state: Optional[str]

    email: Optional[str]


@dataclass
class RegistrarApiUpdateDomainHostRequest:
    name: str

    domain: str

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

    ns: Optional[List[Nameserver]]
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
    disallow_new_zone_creation: bool
    """
    Disable the creation of the target zone if it does not exist. Target zone creation is disabled by default.
    """

    dns_zone: str
    """
    DNS zone in which to update the DNS zone records.
    """

    changes: Optional[List[RecordChange]]
    """
    Changes made to the records.
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
