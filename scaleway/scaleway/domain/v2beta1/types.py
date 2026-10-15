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


class ListContactsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    EMAIL_ASC = "email_asc"
    EMAIL_DESC = "email_desc"

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
    """
    The public key string.
    """


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
    """
    The digest type of the DS record.
    """

    digest: str
    """
    The digest string of the DS record.
    """

    public_key: Optional[DSRecordPublicKey] = None
    """
    The public key associated with the digest.
    """


@dataclass
class Record:
    data: str
    name: str
    priority: int
    ttl: int
    type_: RecordType
    id: str
    comment: Optional[str] = None
    updated_at: Optional[datetime] = None
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
    pin: str
    """
    Domain name registrant's Taxcode (mandatory / only optional when the trustee is used)

If the requester:
* is an Italian natural person it contains his/her Codice Fiscale (16 characters format).
* For others than residents of IT it can contain a document number. (ID Card).
* In all other cases it must be equal to VAT number (in the 16 characters format if nationality is IT) or the numeric Codice Fiscale.
    """

    european_citizenship: Optional[str] = None
    """
    This option is useless anymore.
    """

    tax_code: Optional[str] = None
    """
    Tax_code is renamed to pin.
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
    """
    The action of the offer (create, renew, transfer, etc.).
    """

    operation_path: str
    """
    The operation path of the offer.
    """

    price: Optional[Money] = None
    """
    The price of the offer.
    """


@dataclass
class DSRecord:
    key_id: int
    """
    The key tag of the DS record.
    """

    algorithm: DSRecordAlgorithm
    """
    The cryptographic algorithm used for the DS record.
    """

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
    """
    The unique identifier of the contact.
    """

    legal_form: ContactLegalForm
    """
    Legal form of the contact (individual, corporate, association, other).
    """

    firstname: str
    """
    First name of the contact.
    """

    lastname: str
    """
    Last name of the contact.
    """

    company_name: str
    """
    Company name of the contact (required for corporate legal forms).
    """

    email: str
    """
    Email address of the contact.
    """

    email_alt: str
    """
    Alternative email address of the contact.
    """

    phone_number: str
    """
    Phone number of the contact.
    """

    fax_number: str
    """
    Fax number of the contact.
    """

    address_line_1: str
    """
    First line of the contact's address.
    """

    address_line_2: str
    """
    Second line of the contact's address.
    """

    zip: str
    """
    Postal code of the contact.
    """

    city: str
    """
    City of the contact.
    """

    country: str
    """
    Country code of the contact (ISO 3166-1 alpha-2 format).
    """

    vat_identification_code: str
    """
    VAT identification code of the contact.
    """

    company_identification_code: str
    """
    Company identification code (e.g. SIRET/SIREN) of the contact.
    """

    lang: StdLanguageCode
    """
    Preferred language of the contact.
    """

    resale: bool
    """
    Indicates whether the contact's information can be resold.
    """

    whois_opt_in: bool
    """
    Indicates whether the contact's information is published in the WHOIS database.
    """

    email_status: ContactEmailStatus
    """
    Email validation status of the contact.
    """

    state: str
    """
    State or region of the contact.
    """

    status: ContactStatus
    """
    Status of the contact.
    """

    extension_fr: Optional[ContactExtensionFR] = None
    """
    Additional information required for .fr domains.
    """

    extension_eu: Optional[ContactExtensionEU] = None
    """
    Additional information required for .eu domains.
    """

    extension_nl: Optional[ContactExtensionNL] = None
    """
    Additional information required for .nl domains.
    """

    extension_it: Optional[ContactExtensionIT] = None
    """
    Additional information required for .it domains.
    """

    questions: Optional[list[ContactQuestion]] = field(default_factory=list)


@dataclass
class ContactRolesRoles:
    is_owner: bool
    """
    Indicates whether the contact is the owner of the domain.
    """

    is_administrative: bool
    """
    Indicates whether the contact is the administrative contact of the domain.
    """

    is_technical: bool
    """
    Indicates whether the contact is the technical contact of the domain.
    """


@dataclass
class DomainRegistrationStatusExternalDomain:
    validation_token: str
    """
    Validation token for the external domain registration.
    """


@dataclass
class DomainRegistrationStatusTransfer:
    status: DomainRegistrationStatusTransferStatus
    """
    Status of the domain transfer.
    """

    vote_current_owner: bool
    """
    Indicates whether the current owner has voted for the transfer.
    """

    vote_new_owner: bool
    """
    Indicates whether the new owner has voted for the transfer.
    """


@dataclass
class Tld:
    name: str
    """
    The TLD name.
    """

    dnssec_support: bool
    """
    Indicates whether the TLD supports DNSSEC.
    """

    duration_in_years_min: int
    """
    Minimum registration duration in years for the TLD.
    """

    duration_in_years_max: int
    """
    Maximum registration duration in years for the TLD.
    """

    idn_support: bool
    """
    Indicates whether the TLD supports internationalized domain names (IDN).
    """

    offers: dict[str, TldOffer]
    """
    Available offers (create, renew, transfer, etc.) for the TLD.
    """

    specifications: dict[str, str]
    """
    Additional specifications of the TLD.
    """


@dataclass
class NewContact:
    legal_form: ContactLegalForm
    """
    Legal form of the contact (individual, corporate, association, other).
    """

    firstname: str
    """
    First name of the contact.
    """

    lastname: str
    """
    Last name of the contact.
    """

    email: str
    """
    Email address of the contact.
    """

    phone_number: str
    """
    Phone number of the contact.
    """

    address_line_1: str
    """
    First line of the contact's address.
    """

    zip: str
    """
    Postal code of the contact.
    """

    city: str
    """
    City of the contact.
    """

    country: str
    """
    Country code of the contact (ISO 3166-1 alpha-2 format).
    """

    lang: StdLanguageCode
    """
    Preferred language of the contact.
    """

    resale: bool
    """
    Indicates whether the contact's information can be resold.
    """

    whois_opt_in: bool
    """
    Indicates whether the contact's information is published in the WHOIS database.
    """

    company_name: Optional[str] = None
    """
    Company name of the contact (required for corporate legal forms).
    """

    email_alt: Optional[str] = None
    """
    Alternative email address of the contact.
    """

    fax_number: Optional[str] = None
    """
    Fax number of the contact.
    """

    address_line_2: Optional[str] = None
    """
    Second line of the contact's address.
    """

    vat_identification_code: Optional[str] = None
    """
    VAT identification code of the contact.
    """

    company_identification_code: Optional[str] = None
    """
    Company identification code (e.g. SIRET/SIREN) of the contact.
    """

    extension_fr: Optional[ContactExtensionFR] = None
    """
    Additional information required for .fr domains.
    """

    extension_eu: Optional[ContactExtensionEU] = None
    """
    Additional information required for .eu domains.
    """

    state: Optional[str] = None
    """
    State or region of the contact.
    """

    extension_nl: Optional[ContactExtensionNL] = None
    """
    Additional information required for .nl domains.
    """

    extension_it: Optional[ContactExtensionIT] = None
    """
    Additional information required for .it domains.
    """

    questions: Optional[list[ContactQuestion]] = field(default_factory=list)


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
    """
    Status of the DNSSEC configuration of the domain.
    """

    ds_records: list[DSRecord]
    """
    List of the domain's DS records.
    """


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
    """
    Map of domain names to the contact's roles on each domain.
    """

    contact: Optional[Contact] = None
    """
    The contact information.
    """


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
    """
    The domain name associated with the hostname.
    """

    name: str
    """
    The hostname.
    """

    ips: list[str]
    """
    List of glue IP addresses associated with the hostname.
    """

    status: HostStatus
    """
    Status of the hostname.
    """


@dataclass
class DomainSummary:
    domain: str
    """
    The domain name.
    """

    project_id: str
    """
    The project ID associated with the domain.
    """

    organization_id: str
    """
    The organization ID associated with the domain.
    """

    auto_renew_status: DomainFeatureStatus
    """
    Status of the automatic renewal of the domain.
    """

    dnssec_status: DomainFeatureStatus
    """
    Status of the DNSSEC configuration of the domain.
    """

    epp_code: list[str]
    """
    List of the domain's EPP codes.
    """

    registrar: str
    """
    The registrar managing the domain.
    """

    is_external: bool
    """
    Indicates whether Scaleway is the domain's registrar.
    """

    status: DomainStatus
    """
    Status of the domain.
    """

    pending_trade: bool
    """
    Indicates if a trade is ongoing.
    """

    expired_at: Optional[datetime] = None
    """
    Date of expiration of the domain.
    """

    updated_at: Optional[datetime] = None
    """
    Domain's last modification date.
    """

    created_at: Optional[datetime] = None
    """
    Domain's creation date.
    """

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
    """
    The domain name.
    """

    project_id: str
    """
    The project ID associated with the domain.
    """

    organization_id: str
    """
    The organization ID associated with the domain.
    """

    status: RenewableDomainStatus
    """
    The renewal status of the domain.
    """

    renewable_duration_in_years: Optional[int] = 0
    """
    Duration in years for which the domain can be renewed.
    """

    expired_at: Optional[datetime] = None
    """
    Date of expiration of the domain.
    """

    limit_renew_at: Optional[datetime] = None
    """
    Deadline to renew the domain before it enters the late renewal period.
    """

    limit_redemption_at: Optional[datetime] = None
    """
    Deadline to renew the domain before it enters the redemption period.
    """

    estimated_delete_at: Optional[datetime] = None
    """
    Estimated date at which the domain will be deleted.
    """

    tld: Optional[Tld] = None
    """
    TLD information of the domain.
    """


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
    """
    The domain name.
    """

    available: bool
    """
    Indicates whether the domain is available for registration.
    """

    tld: Optional[Tld] = None
    """
    TLD information of the domain.
    """


@dataclass
class CheckContactsCompatibilityResponse:
    compatible: bool
    """
    Indicates whether all contacts are compatible with the domains or TLDs.
    """

    owner_check_result: Optional[
        CheckContactsCompatibilityResponseContactCheckResult
    ] = None
    """
    Compatibility check result for the owner contact.
    """

    administrative_check_result: Optional[
        CheckContactsCompatibilityResponseContactCheckResult
    ] = None
    """
    Compatibility check result for the administrative contact.
    """

    technical_check_result: Optional[
        CheckContactsCompatibilityResponseContactCheckResult
    ] = None
    """
    Compatibility check result for the technical contact.
    """


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
    Domain in which to create the DNS zone.
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
    """
    The domain name.
    """

    organization_id: str
    """
    The organization ID associated with the domain.
    """

    project_id: str
    """
    The project ID associated with the domain.
    """

    auto_renew_status: DomainFeatureStatus
    """
    Status of the automatic renewal of the domain.
    """

    epp_code: list[str]
    """
    List of the domain's EPP codes.
    """

    registrar: str
    """
    The registrar managing the domain.
    """

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
    """
    The authorization code to transfer the domain.
    """


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

    content: Optional[str] = None
    project_id: Optional[str] = None
    format: Optional[RawFormat] = None
    bind_source: Optional[ImportRawDNSZoneRequestBindSource] = None

    axfr_source: Optional[ImportRawDNSZoneRequestAXFRSource] = None


@dataclass
class ImportRawDNSZoneResponse:
    records: list[Record]


@dataclass
class ListContactsResponse:
    total_count: int
    """
    Total count of contacts matching the request.
    """

    contacts: list[ContactRoles]
    """
    List of contacts with their associated roles.
    """


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

    dns_zone: Optional[str] = None
    """
    DNS zone on which to filter the returned DNS zones.
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
    """
    Total count of hostnames matching the request.
    """

    hosts: list[Host]
    """
    List of hostnames matching the request.
    """


@dataclass
class ListDomainsResponse:
    total_count: int
    """
    Total count of domains matching the request.
    """

    domains: list[DomainSummary]
    """
    List of domains matching the request.
    """


@dataclass
class ListInboundTransfersResponse:
    total_count: int
    """
    Total count of inbound transfers matching the request.
    """

    inbound_transfers: list[InboundTransfer]
    """
    List of inbound transfers matching the request.
    """


@dataclass
class ListRenewableDomainsResponse:
    total_count: int
    """
    Total count of renewable domains matching the request.
    """

    domains: list[RenewableDomain]
    """
    List of renewable domains matching the request.
    """


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
    """
    Total count of tasks matching the request.
    """

    tasks: list[Task]
    """
    List of tasks matching the request.
    """


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
    """
    List of domains in the order.
    """

    organization_id: str
    """
    The organization ID associated with the order.
    """

    project_id: str
    """
    The project ID associated with the order.
    """

    task_id: str
    """
    The unique identifier of the task associated with the order.
    """

    created_at: Optional[datetime] = None
    """
    The creation date of the order.
    """


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
    """
    The external domain name registered.
    """

    organization_id: str
    """
    The organization ID associated with the external domain.
    """

    project_id: str
    """
    The project ID associated with the external domain.
    """

    validation_token: str
    """
    The validation token to use to validate the external domain.
    """

    created_at: Optional[datetime] = None
    """
    The creation date of the external domain registration.
    """


@dataclass
class RegistrarApiBuyDomainsRequest:
    domains: list[str]
    """
    List of domains to purchase.
    """

    duration_in_years: int
    """
    Duration in years for the domain registration.
    """

    auto_renew: bool
    """
    Enable the `auto renew` feature for all the requested domains. This means the domain will be automatically renewed before its expiry date.
    """

    project_id: Optional[str] = None
    """
    Project ID to create the domains in.
    """

    owner_contact_id: Optional[str] = None

    owner_contact: Optional[NewContact] = None

    administrative_contact_id: Optional[str] = None

    administrative_contact: Optional[NewContact] = None

    technical_contact_id: Optional[str] = None

    technical_contact: Optional[NewContact] = None


@dataclass
class RegistrarApiCheckContactsCompatibilityRequest:
    domains: Optional[list[str]] = field(default_factory=list)
    """
    List of domains to check contacts compatibility against.
    """

    tlds: Optional[list[str]] = field(default_factory=list)
    """
    List of TLDs to check contacts compatibility against.
    """

    owner_contact_id: Optional[str] = None

    owner_contact: Optional[NewContact] = None

    administrative_contact_id: Optional[str] = None

    administrative_contact: Optional[NewContact] = None

    technical_contact_id: Optional[str] = None

    technical_contact: Optional[NewContact] = None


@dataclass
class RegistrarApiCreateDomainHostRequest:
    domain: str
    """
    The domain name to create the hostname for.
    """

    name: str
    """
    The hostname to create.
    """

    ips: Optional[list[str]] = field(default_factory=list)
    """
    List of glue IP addresses associated with the hostname.
    """


@dataclass
class RegistrarApiDeleteDomainHostRequest:
    domain: str
    """
    The domain name of the hostname to delete.
    """

    name: str
    """
    The hostname to delete.
    """


@dataclass
class RegistrarApiDeleteExternalDomainRequest:
    domain: str
    """
    The external domain name to delete.
    """


@dataclass
class RegistrarApiDisableDomainAutoRenewRequest:
    domain: str
    """
    The domain name to disable auto renew for.
    """


@dataclass
class RegistrarApiDisableDomainDNSSECRequest:
    domain: str
    """
    The domain name to disable DNSSEC for.
    """


@dataclass
class RegistrarApiEnableDomainAutoRenewRequest:
    domain: str
    """
    The domain name to enable auto renew for.
    """


@dataclass
class RegistrarApiEnableDomainDNSSECRequest:
    domain: str
    """
    The domain name to enable DNSSEC for.
    """

    ds_record: Optional[DSRecord] = None
    """
    The DS record to configure for DNSSEC. If omitted, the DS record will be automatically generated.
    """


@dataclass
class RegistrarApiGetContactRequest:
    contact_id: str
    """
    ID of the contact to retrieve.
    """


@dataclass
class RegistrarApiGetDomainAuthCodeRequest:
    domain: str
    """
    The domain name to retrieve the authorization code for.
    """


@dataclass
class RegistrarApiGetDomainRequest:
    domain: str
    """
    The domain name to retrieve.
    """


@dataclass
class RegistrarApiListContactsRequest:
    page: Optional[int] = 0
    """
    Page number for the returned contacts.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of contacts per page.
    """

    domain: Optional[str] = None
    """
    Filter contacts by domain name.
    """

    project_id: Optional[str] = None
    """
    Filter contacts by project ID.
    """

    organization_id: Optional[str] = None
    """
    Filter contacts by organization ID.
    """

    role: Optional[ListContactsRequestRole] = ListContactsRequestRole.UNKNOWN_ROLE
    """
    Filter contacts by role (owner, administrative, technical).
    """

    email_status: Optional[ContactEmailStatus] = ContactEmailStatus.EMAIL_STATUS_UNKNOWN
    """
    Filter contacts by email validation status.
    """

    order_by: Optional[ListContactsRequestOrderBy] = (
        ListContactsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order of the returned contacts.
    """

    status: Optional[ContactStatus] = ContactStatus.STATUS_UNKNOWN
    """
    Filter by contact status.
    """

    legal_form: Optional[ContactLegalForm] = ContactLegalForm.LEGAL_FORM_UNKNOWN
    """
    Filter by legal form.
    """

    email: Optional[str] = None
    """
    Filter by email address.
    """

    search: Optional[str] = None
    """
    Fuzzy search in firstname, lastname, email, and company_name.
    """


@dataclass
class RegistrarApiListDomainHostsRequest:
    domain: str
    """
    The domain name to list hostnames for.
    """

    page: Optional[int] = 0
    """
    Page number for the returned hostnames.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of hostnames per page.
    """


@dataclass
class RegistrarApiListDomainsRequest:
    page: Optional[int] = 0
    """
    Page number for the returned domains.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of domains per page.
    """

    order_by: Optional[ListDomainsRequestOrderBy] = ListDomainsRequestOrderBy.DOMAIN_ASC
    """
    Sort order of the returned domains.
    """

    registrar: Optional[str] = None
    """
    Filter domains by registrar.
    """

    status: Optional[DomainStatus] = DomainStatus.STATUS_UNKNOWN
    """
    Filter domains by status.
    """

    project_id: Optional[str] = None
    """
    Filter domains by project ID.
    """

    organization_id: Optional[str] = None
    """
    Filter domains by organization ID.
    """

    is_external: Optional[bool] = False
    """
    Filter domains by external status.
    """

    domain: Optional[str] = None
    """
    Filter domains by domain name.
    """


@dataclass
class RegistrarApiListInboundTransfersRequest:
    page: int
    """
    Page number for the returned inbound transfers.
    """

    domain: str
    """
    Filter inbound transfers by domain name.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of inbound transfers per page.
    """

    project_id: Optional[str] = None
    """
    Filter inbound transfers by project ID.
    """

    organization_id: Optional[str] = None
    """
    Filter inbound transfers by organization ID.
    """


@dataclass
class RegistrarApiListRenewableDomainsRequest:
    page: Optional[int] = 0
    """
    Page number for the returned renewable domains.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of renewable domains per page.
    """

    order_by: Optional[ListRenewableDomainsRequestOrderBy] = (
        ListRenewableDomainsRequestOrderBy.DOMAIN_ASC
    )
    """
    Sort order of the returned renewable domains.
    """

    project_id: Optional[str] = None
    """
    Filter renewable domains by project ID.
    """

    organization_id: Optional[str] = None
    """
    Filter renewable domains by organization ID.
    """


@dataclass
class RegistrarApiListTasksRequest:
    page: Optional[int] = 0
    """
    Page number for the returned tasks.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of tasks per page.
    """

    project_id: Optional[str] = None
    """
    Filter tasks by project ID.
    """

    organization_id: Optional[str] = None
    """
    Filter tasks by organization ID.
    """

    domain: Optional[str] = None
    """
    Filter tasks by domain name.
    """

    types: Optional[list[TaskType]] = field(default_factory=list)
    """
    Filter tasks by type.
    """

    statuses: Optional[list[TaskStatus]] = field(default_factory=list)
    """
    Filter tasks by status.
    """

    order_by: Optional[ListTasksRequestOrderBy] = ListTasksRequestOrderBy.DOMAIN_DESC
    """
    Sort order of the returned tasks.
    """


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
    """
    The domain name to lock for transfer.
    """


@dataclass
class RegistrarApiRegisterExternalDomainRequest:
    domain: str
    """
    The external domain name to register.
    """

    project_id: Optional[str] = None
    """
    Project ID to register the external domain in.
    """


@dataclass
class RegistrarApiRenewDomainsRequest:
    domains: list[str]
    """
    List of domains to renew.
    """

    duration_in_years: int
    """
    Duration in years for the domain renewal.
    """

    force_late_renewal: Optional[bool] = False
    """
    Force the renewal to be a late renewal.
    """


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

    include_exact_match: bool
    """
    If an exact match is found, include it in response as a separate element.
    """

    tlds: Optional[list[str]] = field(default_factory=list)
    """
    Array of tlds to search on.
    """


@dataclass
class RegistrarApiTradeDomainRequest:
    domain: str
    """
    The domain name to trade.
    """

    project_id: Optional[str] = None
    """
    Project ID to associate with the domain after the trade.
    """

    new_owner_contact_id: Optional[str] = None

    new_owner_contact: Optional[NewContact] = None


@dataclass
class RegistrarApiTransferInDomainRequest:
    domains: list[TransferInDomainRequestTransferRequest]
    """
    List of domains to transfer in, each with its auth code.
    """

    project_id: Optional[str] = None
    """
    Project ID to transfer the domains into.
    """

    owner_contact_id: Optional[str] = None

    owner_contact: Optional[NewContact] = None

    administrative_contact_id: Optional[str] = None

    administrative_contact: Optional[NewContact] = None

    technical_contact_id: Optional[str] = None

    technical_contact: Optional[NewContact] = None


@dataclass
class RegistrarApiUnlockDomainTransferRequest:
    domain: str
    """
    The domain name to unlock for transfer.
    """


@dataclass
class RegistrarApiUpdateContactRequest:
    contact_id: str
    """
    ID of the contact to update.
    """

    email: Optional[str] = None
    """
    Email address of the contact.
    """

    email_alt: Optional[str] = None
    """
    Alternative email address of the contact.
    """

    phone_number: Optional[str] = None
    """
    Phone number of the contact.
    """

    fax_number: Optional[str] = None
    """
    Fax number of the contact.
    """

    address_line_1: Optional[str] = None
    """
    First line of the contact's address.
    """

    address_line_2: Optional[str] = None
    """
    Second line of the contact's address.
    """

    zip: Optional[str] = None
    """
    Postal code of the contact.
    """

    city: Optional[str] = None
    """
    City of the contact.
    """

    country: Optional[str] = None
    """
    Country code of the contact (ISO 3166-1 alpha-2 format).
    """

    vat_identification_code: Optional[str] = None
    """
    VAT identification code of the contact.
    """

    company_identification_code: Optional[str] = None
    """
    Company identification code (e.g. SIRET/SIREN) of the contact.
    """

    lang: Optional[StdLanguageCode] = StdLanguageCode.UNKNOWN_LANGUAGE_CODE
    """
    Preferred language of the contact.
    """

    resale: Optional[bool] = False
    """
    Indicates whether the contact's information can be resold.
    """

    extension_fr: Optional[ContactExtensionFR] = None
    """
    Additional information required for .fr domains.
    """

    extension_eu: Optional[ContactExtensionEU] = None
    """
    Additional information required for .eu domains.
    """

    extension_nl: Optional[ContactExtensionNL] = None
    """
    Additional information required for .nl domains.
    """

    extension_it: Optional[ContactExtensionIT] = None
    """
    Additional information required for .it domains.
    """

    whois_opt_in: Optional[bool] = False
    """
    Indicates whether the contact's information is published in the WHOIS database.
    """

    state: Optional[str] = None
    """
    State or region of the contact.
    """

    questions: Optional[list[UpdateContactRequestQuestion]] = field(
        default_factory=list
    )


@dataclass
class RegistrarApiUpdateDomainHostRequest:
    domain: str
    """
    The domain name of the hostname to update.
    """

    name: str
    """
    The hostname to update.
    """

    ips: Optional[list[str]] = field(default_factory=list)
    """
    New list of glue IP addresses associated with the hostname.
    """


@dataclass
class RegistrarApiUpdateDomainRequest:
    domain: str
    """
    The domain name to update.
    """

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

    exact_match_domain: Optional[AvailableDomain] = None
    """
    If an exact match was asked and found, the result is in this field.
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
    The full name of the DNS zone to modify. For a root zone (e.g., example.com), enter `example.com`. For a specific sub-zone (e.g., prod.example.com), enter `prod.example.com`.
    """

    new_dns_zone: Optional[str] = None
    """
    Name of the new DNS zone to create.
    """

    project_id: Optional[str] = None
    """
    Project ID in which to create the new DNS zone.
    """
