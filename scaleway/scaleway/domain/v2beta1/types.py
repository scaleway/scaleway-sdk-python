# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

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


class InboundTransferStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    ERR_INTERNAL = "err_internal"
    ERR_DOMAIN_PENDING = "err_domain_pending"
    ERR_ALREADY_TRANSFERRING = "err_already_transferring"
    ERR_TRANSFER_PROHIBITED = "err_transfer_prohibited"
    ERR_TRANSFER_IMPOSSIBLE = "err_transfer_impossible"
    ERR_INVALID_AUTHCODE = "err_invalid_authcode"
    ERR_DOMAIN_TOO_YOUNG = "err_domain_too_young"
    ERR_TOO_MANY_REQUESTS = "err_too_many_requests"

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
    countries: list[str]
    continents: list[str]
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
    matches: list[RecordGeoIPConfigMatch]
    default: str


@dataclass
class RecordHTTPServiceConfig:
    ips: list[str]
    url: str
    strategy: RecordHTTPServiceConfigStrategy
    must_contain: Optional[str] = None
    user_agent: Optional[str] = None


@dataclass
class RecordViewConfig:
    views: list[RecordViewConfigView]


@dataclass
class RecordWeightedConfig:
    weighted_ips: list[RecordWeightedConfigWeightedIP]


@dataclass
class ContactExtensionFRAssociationInfo:
    publication_jo_page: int
    publication_jo: Optional[datetime] = None


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
    public_key: Optional[DSRecordPublicKey] = None


@dataclass
class Record:
    data: str
    name: str
    priority: int
    ttl: int
    type_: RecordType
    id: str
    comment: Optional[str] = None
    geo_ip_config: Optional[RecordGeoIPConfig] = None

    http_service_config: Optional[RecordHTTPServiceConfig] = None

    weighted_config: Optional[RecordWeightedConfig] = None

    view_config: Optional[RecordViewConfig] = None


@dataclass
class RecordIdentifier:
    name: str
    type_: RecordType
    data: Optional[str] = None
    ttl: Optional[int] = None


@dataclass
class ContactExtensionEU:
    european_citizenship: str


@dataclass
class ContactExtensionFR:
    mode: ContactExtensionFRMode
    individual_info: Optional[ContactExtensionFRIndividualInfo] = None

    duns_info: Optional[ContactExtensionFRDunsInfo] = None

    association_info: Optional[ContactExtensionFRAssociationInfo] = None

    trademark_info: Optional[ContactExtensionFRTrademarkInfo] = None

    code_auth_afnic_info: Optional[ContactExtensionFRCodeAuthAfnicInfo] = None


@dataclass
class ContactExtensionIT:
    european_citizenship: str
    """
    This option is useless anymore.
    """

    tax_code: str
    """
    Tax_code is renamed to pin.
    """

    pin: str
    """
    Domain name registrant's Taxcode (mandatory / only optional when the trustee is used)

If the requester:
* is an Italian natural person it contains his/her Codice Fiscale (16 characters format).
* For others than residents of IT it can contain a document number. (ID Card).
* In all other cases it must be equal to VAT number (in the 16 characters format if nationality is IT) or the numeric Codice Fiscale.
    """


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
    price: Optional[Money] = None


@dataclass
class DSRecord:
    key_id: int
    algorithm: DSRecordAlgorithm
    digest: Optional[DSRecordDigest] = None

    public_key: Optional[DSRecordPublicKey] = None


@dataclass
class RecordChangeAdd:
    records: list[Record]


@dataclass
class RecordChangeClear:
    pass


@dataclass
class RecordChangeDelete:
    id: Optional[str] = None

    id_fields: Optional[RecordIdentifier] = None


@dataclass
class RecordChangeSet:
    records: list[Record]
    id: Optional[str] = None

    id_fields: Optional[RecordIdentifier] = None


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
    email_status: ContactEmailStatus
    state: str
    status: ContactStatus
    questions: list[ContactQuestion]
    extension_fr: Optional[ContactExtensionFR] = None
    extension_eu: Optional[ContactExtensionEU] = None
    extension_nl: Optional[ContactExtensionNL] = None
    extension_it: Optional[ContactExtensionIT] = None


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
    offers: dict[str, TldOffer]
    specifications: dict[str, str]


@dataclass
class NewContact:
    legal_form: ContactLegalForm
    firstname: str
    lastname: str
    email: str
    phone_number: str
    address_line_1: str
    zip: str
    city: str
    country: str
    lang: StdLanguageCode
    resale: bool
    whois_opt_in: bool
    questions: list[ContactQuestion]
    company_name: Optional[str] = None
    email_alt: Optional[str] = None
    fax_number: Optional[str] = None
    address_line_2: Optional[str] = None
    vat_identification_code: Optional[str] = None
    company_identification_code: Optional[str] = None
    extension_fr: Optional[ContactExtensionFR] = None
    extension_eu: Optional[ContactExtensionEU] = None
    state: Optional[str] = None
    extension_nl: Optional[ContactExtensionNL] = None
    extension_it: Optional[ContactExtensionIT] = None


@dataclass
class CheckContactsCompatibilityResponseContactCheckResult:
    compatible: bool
    error_message: Optional[str] = None


@dataclass
class DNSZone:
    domain: str
    subdomain: str
    ns: list[str]
    ns_default: list[str]
    ns_master: list[str]
    status: DNSZoneStatus
    project_id: str
    linked_products: list[LinkedProduct]
    message: Optional[str] = None
    updated_at: Optional[datetime] = None


@dataclass
class DomainDNSSEC:
    status: DomainFeatureStatus
    ds_records: list[DSRecord]


@dataclass
class RecordChange:
    add: Optional[RecordChangeAdd] = None

    set_: Optional[RecordChangeSet] = None

    delete: Optional[RecordChangeDelete] = None

    clear: Optional[RecordChangeClear] = None


@dataclass
class ImportProviderDNSZoneRequestOnlineV1:
    token: str


@dataclass
class ImportRawDNSZoneRequestAXFRSource:
    name_server: str
    tsig_key: Optional[ImportRawDNSZoneRequestTsigKey] = None


@dataclass
class ImportRawDNSZoneRequestBindSource:
    content: str


@dataclass
class ContactRoles:
    roles: dict[str, ContactRolesRoles]
    contact: Optional[Contact] = None


@dataclass
class Nameserver:
    name: str
    ip: list[str]


@dataclass
class DNSZoneVersion:
    id: str
    created_at: Optional[datetime] = None


@dataclass
class Host:
    domain: str
    name: str
    ips: list[str]
    status: HostStatus


@dataclass
class DomainSummary:
    domain: str
    project_id: str
    auto_renew_status: DomainFeatureStatus
    dnssec_status: DomainFeatureStatus
    epp_code: list[str]
    registrar: str
    is_external: bool
    status: DomainStatus
    organization_id: str
    pending_trade: bool
    expired_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    external_domain_registration_status: Optional[
        DomainRegistrationStatusExternalDomain
    ] = None

    transfer_registration_status: Optional[DomainRegistrationStatusTransfer] = None


@dataclass
class InboundTransfer:
    id: str
    """
    The unique identifier of the inbound transfer.
    """

    project_id: str
    """
    The project ID associated with the inbound transfer.
    """

    domain: str
    """
    The domain associated with the inbound transfer.
    """

    status: InboundTransferStatus
    """
    Inbound transfer status.
    """

    message: str
    """
    Human-friendly message to describe the current inbound transfer status.
    """

    task_id: str
    """
    The unique identifier of the associated task.
    """

    created_at: Optional[datetime] = None
    """
    The creation date of the inbound transfer.
    """

    last_updated_at: Optional[datetime] = None
    """
    The last modification date of the inbound transfer.
    """


@dataclass
class RenewableDomain:
    domain: str
    project_id: str
    organization_id: str
    status: RenewableDomainStatus
    renewable_duration_in_years: Optional[int] = None
    expired_at: Optional[datetime] = None
    limit_renew_at: Optional[datetime] = None
    limit_redemption_at: Optional[datetime] = None
    estimated_delete_at: Optional[datetime] = None
    tld: Optional[Tld] = None


@dataclass
class SSLCertificate:
    dns_zone: str
    alternative_dns_zones: list[str]
    status: SSLCertificateStatus
    private_key: str
    certificate_chain: str
    created_at: Optional[datetime] = None
    expired_at: Optional[datetime] = None


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

    domain: Optional[str] = None
    """
    The domain name associated to the task.
    """

    started_at: Optional[datetime] = None
    """
    Start date of the task.
    """

    updated_at: Optional[datetime] = None
    """
    Last update of the task.
    """

    message: Optional[str] = None
    """
    Error message associated to the task.
    """

    contact_identifier: Optional[str] = None
    """
    Human-friendly contact identifier used when the task concerns a contact.
    """


@dataclass
class TransferInDomainRequestTransferRequest:
    domain: str
    auth_code: str


@dataclass
class UpdateContactRequestQuestion:
    question: Optional[str] = None
    answer: Optional[str] = None


@dataclass
class AvailableDomain:
    domain: str
    available: bool
    tld: Optional[Tld] = None


@dataclass
class CheckContactsCompatibilityResponse:
    compatible: bool
    owner_check_result: Optional[
        CheckContactsCompatibilityResponseContactCheckResult
    ] = None
    administrative_check_result: Optional[
        CheckContactsCompatibilityResponseContactCheckResult
    ] = None
    technical_check_result: Optional[
        CheckContactsCompatibilityResponseContactCheckResult
    ] = None


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

    project_id: Optional[str] = None
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

    project_id: Optional[str] = None
    """
    Project ID in which to create the DNS zone.
    """


@dataclass
class CreateSSLCertificateRequest:
    dns_zone: str
    alternative_dns_zones: Optional[list[str]] = field(default_factory=list)


@dataclass
class DeleteDNSZoneRequest:
    dns_zone: str
    """
    DNS zone to delete.
    """

    project_id: Optional[str] = None
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

    epp_code: list[str]
    """
    List of the domain's EPP codes.
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

    dns_zones: list[DNSZone]
    """
    List of the domain's DNS zones.
    """

    linked_products: list[LinkedProduct]
    """
    List of Scaleway resources linked to the domain.
    """

    pending_trade: bool
    """
    Indicates if a trade is ongoing.
    """

    dnssec: Optional[DomainDNSSEC] = None
    """
    Status of the DNSSEC configuration of the domain.
    """

    expired_at: Optional[datetime] = None
    """
    Date of expiration of the domain.
    """

    updated_at: Optional[datetime] = None
    """
    Domain's last modification date.
    """

    owner_contact: Optional[Contact] = None
    """
    Contact information of the domain's owner.
    """

    technical_contact: Optional[Contact] = None
    """
    Contact information of the domain's technical contact.
    """

    administrative_contact: Optional[Contact] = None
    """
    Contact information of the domain's administrative contact.
    """

    tld: Optional[Tld] = None
    """
    Domain's TLD information.
    """

    external_domain_registration_status: Optional[
        DomainRegistrationStatusExternalDomain
    ] = None

    transfer_registration_status: Optional[DomainRegistrationStatusTransfer] = None


@dataclass
class ExportRawDNSZoneRequest:
    dns_zone: str
    """
    DNS zone to export.
    """

    format: Optional[RawFormat] = RawFormat.UNKNOWN_RAW_FORMAT
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
    changes: list[RecordChange]


@dataclass
class GetDomainAuthCodeResponse:
    auth_code: str


@dataclass
class GetSSLCertificateRequest:
    dns_zone: str


@dataclass
class ImportProviderDNSZoneRequest:
    dns_zone: str
    online_v1: Optional[ImportProviderDNSZoneRequestOnlineV1] = None


@dataclass
class ImportProviderDNSZoneResponse:
    records: list[Record]


@dataclass
class ImportRawDNSZoneRequest:
    dns_zone: str
    """
    DNS zone to import.
    """

    content: str
    project_id: Optional[str] = None
    format: Optional[RawFormat] = RawFormat.UNKNOWN_RAW_FORMAT
    bind_source: Optional[ImportRawDNSZoneRequestBindSource] = None

    axfr_source: Optional[ImportRawDNSZoneRequestAXFRSource] = None


@dataclass
class ImportRawDNSZoneResponse:
    records: list[Record]


@dataclass
class ListContactsResponse:
    total_count: int
    contacts: list[ContactRoles]


@dataclass
class ListDNSZoneNameserversRequest:
    dns_zone: str
    """
    DNS zone on which to filter the returned DNS zone name servers.
    """

    project_id: Optional[str] = None
    """
    Project ID on which to filter the returned DNS zone name servers.
    """


@dataclass
class ListDNSZoneNameserversResponse:
    ns: list[Nameserver]
    """
    DNS zone name servers returned.
    """


@dataclass
class ListDNSZoneRecordsRequest:
    dns_zone: str
    """
    DNS zone on which to filter the returned DNS zone records.
    """

    name: str
    """
    Name on which to filter the returned DNS zone records.
    """

    project_id: Optional[str] = None
    """
    Project ID on which to filter the returned DNS zone records.
    """

    order_by: Optional[ListDNSZoneRecordsRequestOrderBy] = (
        ListDNSZoneRecordsRequestOrderBy.NAME_ASC
    )
    """
    Sort order of the returned DNS zone records.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of DNS zone records per page.
    """

    type_: Optional[RecordType] = RecordType.UNKNOWN
    """
    Record type on which to filter the returned DNS zone records.
    """

    id: Optional[str] = None
    """
    Record ID on which to filter the returned DNS zone records.
    """


@dataclass
class ListDNSZoneRecordsResponse:
    total_count: int
    """
    Total number of DNS zone records.
    """

    records: list[Record]
    """
    Paginated returned DNS zone records.
    """


@dataclass
class ListDNSZoneVersionRecordsRequest:
    dns_zone_version_id: str
    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of DNS zones versions records per page.
    """


@dataclass
class ListDNSZoneVersionRecordsResponse:
    total_count: int
    """
    Total number of DNS zones versions records.
    """

    records: list[Record]


@dataclass
class ListDNSZoneVersionsRequest:
    dns_zone: str
    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of DNS zones versions per page.
    """


@dataclass
class ListDNSZoneVersionsResponse:
    total_count: int
    """
    Total number of DNS zones versions.
    """

    versions: list[DNSZoneVersion]


@dataclass
class ListDNSZonesRequest:
    domain: str
    """
    Domain on which to filter the returned DNS zones.
    """

    dns_zone: str
    """
    DNS zone on which to filter the returned DNS zones.
    """

    organization_id: Optional[str] = None
    """
    Organization ID on which to filter the returned DNS zones.
    """

    project_id: Optional[str] = None
    """
    Project ID on which to filter the returned DNS zones.
    """

    order_by: Optional[ListDNSZonesRequestOrderBy] = (
        ListDNSZonesRequestOrderBy.DOMAIN_ASC
    )
    """
    Sort order of the returned DNS zones.
    """

    page: Optional[int] = 0
    """
    Page number to return, from the paginated results.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of DNS zones to return per page.
    """

    dns_zones: Optional[list[str]] = field(default_factory=list)
    """
    DNS zones on which to filter the returned DNS zones.
    """

    created_after: Optional[datetime] = None
    """
    Only list DNS zones created after this date.
    """

    created_before: Optional[datetime] = None
    """
    Only list DNS zones created before this date.
    """

    updated_after: Optional[datetime] = None
    """
    Only list DNS zones updated after this date.
    """

    updated_before: Optional[datetime] = None
    """
    Only list DNS zones updated before this date.
    """


@dataclass
class ListDNSZonesResponse:
    total_count: int
    """
    Total number of DNS zones matching the requested criteria.
    """

    dns_zones: list[DNSZone]
    """
    Paginated returned DNS zones.
    """


@dataclass
class ListDomainHostsResponse:
    total_count: int
    hosts: list[Host]


@dataclass
class ListDomainsResponse:
    total_count: int
    domains: list[DomainSummary]


@dataclass
class ListInboundTransfersResponse:
    total_count: int
    inbound_transfers: list[InboundTransfer]


@dataclass
class ListRenewableDomainsResponse:
    total_count: int
    domains: list[RenewableDomain]


@dataclass
class ListSSLCertificatesRequest:
    dns_zone: str
    page: Optional[int] = 0
    page_size: Optional[int] = 0
    project_id: Optional[str] = None


@dataclass
class ListSSLCertificatesResponse:
    total_count: int
    certificates: list[SSLCertificate]


@dataclass
class ListTasksResponse:
    total_count: int
    tasks: list[Task]


@dataclass
class ListTldsResponse:
    tlds: list[Tld]
    """
    Array of TLDs.
    """

    total_count: int
    """
    Total count of TLDs returned.
    """


@dataclass
class OrderResponse:
    domains: list[str]
    organization_id: str
    project_id: str
    task_id: str
    created_at: Optional[datetime] = None


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
    dns_zones: list[DNSZone]
    """
    DNS zones returned.
    """


@dataclass
class RegisterExternalDomainResponse:
    domain: str
    organization_id: str
    validation_token: str
    project_id: str
    created_at: Optional[datetime] = None


@dataclass
class RegistrarApiBuyDomainsRequest:
    domains: list[str]
    duration_in_years: int
    project_id: Optional[str] = None
    owner_contact_id: Optional[str] = None

    owner_contact: Optional[NewContact] = None

    administrative_contact_id: Optional[str] = None

    administrative_contact: Optional[NewContact] = None

    technical_contact_id: Optional[str] = None

    technical_contact: Optional[NewContact] = None


@dataclass
class RegistrarApiCheckContactsCompatibilityRequest:
    domains: Optional[list[str]] = field(default_factory=list)
    tlds: Optional[list[str]] = field(default_factory=list)
    owner_contact_id: Optional[str] = None

    owner_contact: Optional[NewContact] = None

    administrative_contact_id: Optional[str] = None

    administrative_contact: Optional[NewContact] = None

    technical_contact_id: Optional[str] = None

    technical_contact: Optional[NewContact] = None


@dataclass
class RegistrarApiCreateDomainHostRequest:
    domain: str
    name: str
    ips: Optional[list[str]] = field(default_factory=list)


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
    ds_record: Optional[DSRecord] = None


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
    page: Optional[int] = None
    page_size: Optional[int] = None
    domain: Optional[str] = None
    project_id: Optional[str] = None
    organization_id: Optional[str] = None
    role: Optional[ListContactsRequestRole] = None
    email_status: Optional[ContactEmailStatus] = None


@dataclass
class RegistrarApiListDomainHostsRequest:
    domain: str
    page: Optional[int] = None
    page_size: Optional[int] = None


@dataclass
class RegistrarApiListDomainsRequest:
    page: Optional[int] = None
    page_size: Optional[int] = None
    order_by: Optional[ListDomainsRequestOrderBy] = None
    registrar: Optional[str] = None
    status: Optional[DomainStatus] = None
    project_id: Optional[str] = None
    organization_id: Optional[str] = None
    is_external: Optional[bool] = None
    domain: Optional[str] = None


@dataclass
class RegistrarApiListInboundTransfersRequest:
    page: int
    domain: str
    page_size: Optional[int] = None
    project_id: Optional[str] = None
    organization_id: Optional[str] = None


@dataclass
class RegistrarApiListRenewableDomainsRequest:
    page: Optional[int] = None
    page_size: Optional[int] = None
    order_by: Optional[ListRenewableDomainsRequestOrderBy] = None
    project_id: Optional[str] = None
    organization_id: Optional[str] = None


@dataclass
class RegistrarApiListTasksRequest:
    page: Optional[int] = None
    page_size: Optional[int] = None
    project_id: Optional[str] = None
    organization_id: Optional[str] = None
    domain: Optional[str] = None
    types: Optional[list[TaskType]] = field(default_factory=list)
    statuses: Optional[list[TaskStatus]] = field(default_factory=list)
    order_by: Optional[ListTasksRequestOrderBy] = None


@dataclass
class RegistrarApiListTldsRequest:
    tlds: Optional[list[str]] = field(default_factory=list)
    """
    Array of TLDs to return.
    """

    page: Optional[int] = 0
    """
    Page number for the returned Projects.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of Project per page.
    """

    order_by: Optional[ListTldsRequestOrderBy] = ListTldsRequestOrderBy.NAME_ASC
    """
    Sort order of the returned TLDs.
    """


@dataclass
class RegistrarApiLockDomainTransferRequest:
    domain: str


@dataclass
class RegistrarApiRegisterExternalDomainRequest:
    domain: str
    project_id: Optional[str] = None


@dataclass
class RegistrarApiRenewDomainsRequest:
    domains: list[str]
    duration_in_years: int
    force_late_renewal: Optional[bool] = False


@dataclass
class RegistrarApiRetryInboundTransferRequest:
    domain: str
    """
    The domain being transferred.
    """

    project_id: Optional[str] = None
    """
    The project ID to associated with the inbound transfer.
    """

    auth_code: Optional[str] = None
    """
    An optional new auth code to replace the previous one for the retry.
    """


@dataclass
class RegistrarApiSearchAvailableDomainsRequest:
    domains: list[str]
    """
    A list of domain to search, TLD is optional.
    """

    strict_search: bool
    """
    Search exact match.
    """

    tlds: Optional[list[str]] = field(default_factory=list)
    """
    Array of tlds to search on.
    """


@dataclass
class RegistrarApiTradeDomainRequest:
    domain: str
    project_id: Optional[str] = None
    new_owner_contact_id: Optional[str] = None

    new_owner_contact: Optional[NewContact] = None


@dataclass
class RegistrarApiTransferInDomainRequest:
    domains: list[TransferInDomainRequestTransferRequest]
    project_id: Optional[str] = None
    owner_contact_id: Optional[str] = None

    owner_contact: Optional[NewContact] = None

    administrative_contact_id: Optional[str] = None

    administrative_contact: Optional[NewContact] = None

    technical_contact_id: Optional[str] = None

    technical_contact: Optional[NewContact] = None


@dataclass
class RegistrarApiUnlockDomainTransferRequest:
    domain: str


@dataclass
class RegistrarApiUpdateContactRequest:
    contact_id: str
    email: Optional[str] = None
    email_alt: Optional[str] = None
    phone_number: Optional[str] = None
    fax_number: Optional[str] = None
    address_line_1: Optional[str] = None
    address_line_2: Optional[str] = None
    zip: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    vat_identification_code: Optional[str] = None
    company_identification_code: Optional[str] = None
    lang: Optional[StdLanguageCode] = StdLanguageCode.UNKNOWN_LANGUAGE_CODE
    resale: Optional[bool] = False
    extension_fr: Optional[ContactExtensionFR] = None
    extension_eu: Optional[ContactExtensionEU] = None
    extension_nl: Optional[ContactExtensionNL] = None
    extension_it: Optional[ContactExtensionIT] = None
    whois_opt_in: Optional[bool] = False
    state: Optional[str] = None
    questions: Optional[list[UpdateContactRequestQuestion]] = field(
        default_factory=list
    )


@dataclass
class RegistrarApiUpdateDomainHostRequest:
    domain: str
    name: str
    ips: Optional[list[str]] = field(default_factory=list)


@dataclass
class RegistrarApiUpdateDomainRequest:
    domain: str
    technical_contact_id: Optional[str] = None

    technical_contact: Optional[NewContact] = None

    owner_contact_id: Optional[str] = None

    owner_contact: Optional[NewContact] = None

    administrative_contact_id: Optional[str] = None

    administrative_contact: Optional[NewContact] = None


@dataclass
class RestoreDNSZoneVersionRequest:
    dns_zone_version_id: str


@dataclass
class RestoreDNSZoneVersionResponse:
    pass


@dataclass
class RetryInboundTransferResponse:
    pass


@dataclass
class SearchAvailableDomainsConsoleResponse:
    available_domains: list[AvailableDomain]
    exact_match_domain: Optional[AvailableDomain] = None


@dataclass
class SearchAvailableDomainsResponse:
    available_domains: list[AvailableDomain]
    """
    Array of available domains.
    """


@dataclass
class UnauthenticatedRegistrarApiSearchAvailableDomainsConsoleRequest:
    domain: str
    strict_search: bool
    tlds: Optional[list[str]] = field(default_factory=list)


@dataclass
class UpdateDNSZoneNameserversRequest:
    dns_zone: str
    """
    DNS zone in which to update the DNS zone name servers.
    """

    ns: list[Nameserver]
    """
    New DNS zone name servers.
    """


@dataclass
class UpdateDNSZoneNameserversResponse:
    ns: list[Nameserver]
    """
    DNS zone name servers returned.
    """


@dataclass
class UpdateDNSZoneRecordsRequest:
    dns_zone: str
    """
    DNS zone in which to update the DNS zone records.
    """

    changes: list[RecordChange]
    """
    Changes made to the records.
    """

    disallow_new_zone_creation: bool
    """
    Disable the creation of the target zone if it does not exist. Target zone creation is disabled by default.
    """

    return_all_records: Optional[bool] = False
    """
    Specifies whether or not to return all the records.
    """

    serial: Optional[int] = 0
    """
    Use the provided serial (0) instead of the auto-increment serial.
    """


@dataclass
class UpdateDNSZoneRecordsResponse:
    records: list[Record]
    """
    DNS zone records returned.
    """


@dataclass
class UpdateDNSZoneRequest:
    dns_zone: str
    """
    DNS zone to update.
    """

    new_dns_zone: Optional[str] = None
    """
    Name of the new DNS zone to create.
    """

    project_id: Optional[str] = None
    """
    Project ID in which to create the new DNS zone.
    """
