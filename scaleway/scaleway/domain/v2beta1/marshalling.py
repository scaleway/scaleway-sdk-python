# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    unmarshal_Money,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from dateutil import parser
from .types import (
    ContactExtensionFRMode,
    ContactExtensionNLLegalForm,
    ContactLegalForm,
    DSRecordAlgorithm,
    DSRecordDigestType,
    DomainRecordHTTPServiceConfigStrategy,
    DomainRecordType,
    LanguageCode,
    RawFormat,
    AvailableDomain,
    CheckContactsCompatibilityResponse,
    CheckContactsCompatibilityResponseContactCheckResult,
    ClearDNSZoneRecordsResponse,
    Contact,
    ContactExtensionEU,
    ContactExtensionFR,
    ContactExtensionFRAssociationInfo,
    ContactExtensionFRCodeAuthAfnicInfo,
    ContactExtensionFRDunsInfo,
    ContactExtensionFRIndividualInfo,
    ContactExtensionFRTrademarkInfo,
    ContactExtensionNL,
    ContactQuestion,
    ContactRoles,
    ContactRolesRoles,
    DNSZone,
    DNSZoneVersion,
    DSRecord,
    DSRecordDigest,
    DSRecordPublicKey,
    DeleteDNSZoneResponse,
    DeleteExternalDomainResponse,
    DeleteSSLCertificateResponse,
    Domain,
    DomainDNSSEC,
    DomainRecord,
    DomainRecordGeoIPConfig,
    DomainRecordGeoIPConfigMatch,
    DomainRecordHTTPServiceConfig,
    DomainRecordViewConfig,
    DomainRecordViewConfigView,
    DomainRecordWeightedConfig,
    DomainRecordWeightedConfigWeightedIP,
    DomainRegistrationStatusExternalDomain,
    DomainRegistrationStatusTransfer,
    DomainSummary,
    GetDNSZoneTsigKeyResponse,
    GetDNSZoneVersionDiffResponse,
    GetDomainAuthCodeResponse,
    Host,
    ImportProviderDNSZoneRequestOnlineV1,
    ImportProviderDNSZoneResponse,
    ImportRawDNSZoneRequestAXFRSource,
    ImportRawDNSZoneRequestBindSource,
    ImportRawDNSZoneRequestTsigKey,
    ImportRawDNSZoneResponse,
    ListContactsResponse,
    ListDNSZoneNameserversResponse,
    ListDNSZoneRecordsResponse,
    ListDNSZoneVersionRecordsResponse,
    ListDNSZoneVersionsResponse,
    ListDNSZonesResponse,
    ListDomainHostsResponse,
    ListDomainsResponse,
    ListRenewableDomainsResponse,
    ListSSLCertificatesResponse,
    ListTasksResponse,
    Nameserver,
    NewContact,
    OrderResponse,
    RecordChange,
    RecordChangeAdd,
    RecordChangeClear,
    RecordChangeDelete,
    RecordChangeSet,
    RecordIdentifier,
    RefreshDNSZoneResponse,
    RegisterExternalDomainResponse,
    RenewableDomain,
    RestoreDNSZoneVersionResponse,
    SSLCertificate,
    SearchAvailableDomainsResponse,
    Task,
    Tld,
    TldOffer,
    TransferInDomainRequestTransferRequest,
    UpdateContactRequestQuestion,
    UpdateDNSZoneNameserversResponse,
    UpdateDNSZoneRecordsResponse,
    CreateDNSZoneRequest,
    UpdateDNSZoneRequest,
    CloneDNSZoneRequest,
    UpdateDNSZoneRecordsRequest,
    UpdateDNSZoneNameserversRequest,
    ImportRawDNSZoneRequest,
    ImportProviderDNSZoneRequest,
    RefreshDNSZoneRequest,
    CreateSSLCertificateRequest,
    RegistrarApiBuyDomainsRequest,
    RegistrarApiRenewDomainsRequest,
    RegistrarApiTransferInDomainRequest,
    RegistrarApiTradeDomainRequest,
    RegistrarApiRegisterExternalDomainRequest,
    RegistrarApiCheckContactsCompatibilityRequest,
    RegistrarApiUpdateContactRequest,
    RegistrarApiUpdateDomainRequest,
    RegistrarApiEnableDomainDNSSECRequest,
    RegistrarApiCreateDomainHostRequest,
    RegistrarApiUpdateDomainHostRequest,
)


def unmarshal_DomainRecordGeoIPConfigMatch(data: Any) -> DomainRecordGeoIPConfigMatch:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DomainRecordGeoIPConfigMatch' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("continents")
    args["continents"] = field

    field = data.get("countries")
    args["countries"] = field

    field = data.get("data")
    args["data"] = field

    return DomainRecordGeoIPConfigMatch(**args)


def unmarshal_DomainRecordViewConfigView(data: Any) -> DomainRecordViewConfigView:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DomainRecordViewConfigView' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("data")
    args["data"] = field

    field = data.get("subnet")
    args["subnet"] = field

    return DomainRecordViewConfigView(**args)


def unmarshal_DomainRecordWeightedConfigWeightedIP(
    data: Any,
) -> DomainRecordWeightedConfigWeightedIP:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DomainRecordWeightedConfigWeightedIP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip")
    args["ip"] = field

    field = data.get("weight")
    args["weight"] = field

    return DomainRecordWeightedConfigWeightedIP(**args)


def unmarshal_ContactExtensionFRAssociationInfo(
    data: Any,
) -> ContactExtensionFRAssociationInfo:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ContactExtensionFRAssociationInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("publication_jo")
    args["publication_jo"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("publication_jo_page")
    args["publication_jo_page"] = field

    return ContactExtensionFRAssociationInfo(**args)


def unmarshal_ContactExtensionFRCodeAuthAfnicInfo(
    data: Any,
) -> ContactExtensionFRCodeAuthAfnicInfo:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ContactExtensionFRCodeAuthAfnicInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("code_auth_afnic")
    args["code_auth_afnic"] = field

    return ContactExtensionFRCodeAuthAfnicInfo(**args)


def unmarshal_ContactExtensionFRDunsInfo(data: Any) -> ContactExtensionFRDunsInfo:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ContactExtensionFRDunsInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("duns_id")
    args["duns_id"] = field

    field = data.get("local_id")
    args["local_id"] = field

    return ContactExtensionFRDunsInfo(**args)


def unmarshal_ContactExtensionFRIndividualInfo(
    data: Any,
) -> ContactExtensionFRIndividualInfo:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ContactExtensionFRIndividualInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("whois_opt_in")
    args["whois_opt_in"] = field

    return ContactExtensionFRIndividualInfo(**args)


def unmarshal_ContactExtensionFRTrademarkInfo(
    data: Any,
) -> ContactExtensionFRTrademarkInfo:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ContactExtensionFRTrademarkInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("trademark_inpi")
    args["trademark_inpi"] = field

    return ContactExtensionFRTrademarkInfo(**args)


def unmarshal_DSRecordPublicKey(data: Any) -> DSRecordPublicKey:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DSRecordPublicKey' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("key")
    args["key"] = field

    return DSRecordPublicKey(**args)


def unmarshal_DomainRecordGeoIPConfig(data: Any) -> DomainRecordGeoIPConfig:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DomainRecordGeoIPConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("default")
    args["default"] = field

    field = data.get("matches")
    args["matches"] = [
        unmarshal_DomainRecordGeoIPConfigMatch(v) for v in data["matches"]
    ]

    return DomainRecordGeoIPConfig(**args)


def unmarshal_DomainRecordHTTPServiceConfig(data: Any) -> DomainRecordHTTPServiceConfig:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DomainRecordHTTPServiceConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ips")
    args["ips"] = field

    field = data.get("must_contain")
    args["must_contain"] = field

    field = data.get("strategy")
    args["strategy"] = field

    field = data.get("url")
    args["url"] = field

    field = data.get("user_agent")
    args["user_agent"] = field

    return DomainRecordHTTPServiceConfig(**args)


def unmarshal_DomainRecordViewConfig(data: Any) -> DomainRecordViewConfig:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DomainRecordViewConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("views")
    args["views"] = [unmarshal_DomainRecordViewConfigView(v) for v in data["views"]]

    return DomainRecordViewConfig(**args)


def unmarshal_DomainRecordWeightedConfig(data: Any) -> DomainRecordWeightedConfig:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DomainRecordWeightedConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("weighted_ips")
    args["weighted_ips"] = [
        unmarshal_DomainRecordWeightedConfigWeightedIP(v) for v in data["weighted_ips"]
    ]

    return DomainRecordWeightedConfig(**args)


def unmarshal_ContactExtensionEU(data: Any) -> ContactExtensionEU:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ContactExtensionEU' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("european_citizenship")
    args["european_citizenship"] = field

    return ContactExtensionEU(**args)


def unmarshal_ContactExtensionFR(data: Any) -> ContactExtensionFR:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ContactExtensionFR' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("association_info")
    args["association_info"] = (
        unmarshal_ContactExtensionFRAssociationInfo(field)
        if field is not None
        else None
    )

    field = data.get("code_auth_afnic_info")
    args["code_auth_afnic_info"] = (
        unmarshal_ContactExtensionFRCodeAuthAfnicInfo(field)
        if field is not None
        else None
    )

    field = data.get("duns_info")
    args["duns_info"] = (
        unmarshal_ContactExtensionFRDunsInfo(field) if field is not None else None
    )

    field = data.get("individual_info")
    args["individual_info"] = (
        unmarshal_ContactExtensionFRIndividualInfo(field) if field is not None else None
    )

    field = data.get("mode")
    args["mode"] = field

    field = data.get("trademark_info")
    args["trademark_info"] = (
        unmarshal_ContactExtensionFRTrademarkInfo(field) if field is not None else None
    )

    return ContactExtensionFR(**args)


def unmarshal_ContactExtensionNL(data: Any) -> ContactExtensionNL:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ContactExtensionNL' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("legal_form")
    args["legal_form"] = field

    field = data.get("legal_form_registration_number")
    args["legal_form_registration_number"] = field

    return ContactExtensionNL(**args)


def unmarshal_ContactQuestion(data: Any) -> ContactQuestion:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ContactQuestion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("answer")
    args["answer"] = field

    field = data.get("question")
    args["question"] = field

    return ContactQuestion(**args)


def unmarshal_DSRecordDigest(data: Any) -> DSRecordDigest:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DSRecordDigest' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("digest")
    args["digest"] = field

    field = data.get("public_key")
    args["public_key"] = (
        unmarshal_DSRecordPublicKey(field) if field is not None else None
    )

    field = data.get("type_")
    args["type_"] = field

    return DSRecordDigest(**args)


def unmarshal_DomainRecord(data: Any) -> DomainRecord:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DomainRecord' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("comment")
    args["comment"] = field

    field = data.get("data")
    args["data"] = field

    field = data.get("geo_ip_config")
    args["geo_ip_config"] = (
        unmarshal_DomainRecordGeoIPConfig(field) if field is not None else None
    )

    field = data.get("http_service_config")
    args["http_service_config"] = (
        unmarshal_DomainRecordHTTPServiceConfig(field) if field is not None else None
    )

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("priority")
    args["priority"] = field

    field = data.get("ttl")
    args["ttl"] = field

    field = data.get("type_")
    args["type_"] = field

    field = data.get("view_config")
    args["view_config"] = (
        unmarshal_DomainRecordViewConfig(field) if field is not None else None
    )

    field = data.get("weighted_config")
    args["weighted_config"] = (
        unmarshal_DomainRecordWeightedConfig(field) if field is not None else None
    )

    return DomainRecord(**args)


def unmarshal_RecordIdentifier(data: Any) -> RecordIdentifier:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'RecordIdentifier' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("data")
    args["data"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("ttl")
    args["ttl"] = field

    field = data.get("type_")
    args["type_"] = field

    return RecordIdentifier(**args)


def unmarshal_TldOffer(data: Any) -> TldOffer:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'TldOffer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("action")
    args["action"] = field

    field = data.get("operation_path")
    args["operation_path"] = field

    field = data.get("price")
    args["price"] = unmarshal_Money(field) if field is not None else None

    return TldOffer(**args)


def unmarshal_Contact(data: Any) -> Contact:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Contact' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("address_line_1")
    args["address_line_1"] = field

    field = data.get("address_line_2")
    args["address_line_2"] = field

    field = data.get("city")
    args["city"] = field

    field = data.get("company_identification_code")
    args["company_identification_code"] = field

    field = data.get("company_name")
    args["company_name"] = field

    field = data.get("country")
    args["country"] = field

    field = data.get("email")
    args["email"] = field

    field = data.get("email_alt")
    args["email_alt"] = field

    field = data.get("email_status")
    args["email_status"] = field

    field = data.get("extension_eu")
    args["extension_eu"] = (
        unmarshal_ContactExtensionEU(field) if field is not None else None
    )

    field = data.get("extension_fr")
    args["extension_fr"] = (
        unmarshal_ContactExtensionFR(field) if field is not None else None
    )

    field = data.get("extension_nl")
    args["extension_nl"] = (
        unmarshal_ContactExtensionNL(field) if field is not None else None
    )

    field = data.get("fax_number")
    args["fax_number"] = field

    field = data.get("firstname")
    args["firstname"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("lang")
    args["lang"] = field

    field = data.get("lastname")
    args["lastname"] = field

    field = data.get("legal_form")
    args["legal_form"] = field

    field = data.get("phone_number")
    args["phone_number"] = field

    field = data.get("questions")
    args["questions"] = (
        [unmarshal_ContactQuestion(v) for v in data["questions"]]
        if field is not None
        else None
    )

    field = data.get("resale")
    args["resale"] = field

    field = data.get("state")
    args["state"] = field

    field = data.get("vat_identification_code")
    args["vat_identification_code"] = field

    field = data.get("whois_opt_in")
    args["whois_opt_in"] = field

    field = data.get("zip")
    args["zip"] = field

    return Contact(**args)


def unmarshal_ContactRolesRoles(data: Any) -> ContactRolesRoles:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ContactRolesRoles' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("is_administrative")
    args["is_administrative"] = field

    field = data.get("is_owner")
    args["is_owner"] = field

    field = data.get("is_technical")
    args["is_technical"] = field

    return ContactRolesRoles(**args)


def unmarshal_DSRecord(data: Any) -> DSRecord:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DSRecord' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("algorithm")
    args["algorithm"] = field

    field = data.get("digest")
    args["digest"] = unmarshal_DSRecordDigest(field) if field is not None else None

    field = data.get("key_id")
    args["key_id"] = field

    field = data.get("public_key")
    args["public_key"] = (
        unmarshal_DSRecordPublicKey(field) if field is not None else None
    )

    return DSRecord(**args)


def unmarshal_DomainRegistrationStatusExternalDomain(
    data: Any,
) -> DomainRegistrationStatusExternalDomain:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DomainRegistrationStatusExternalDomain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("validation_token")
    args["validation_token"] = field

    return DomainRegistrationStatusExternalDomain(**args)


def unmarshal_DomainRegistrationStatusTransfer(
    data: Any,
) -> DomainRegistrationStatusTransfer:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DomainRegistrationStatusTransfer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("status")
    args["status"] = field

    field = data.get("vote_current_owner")
    args["vote_current_owner"] = field

    field = data.get("vote_new_owner")
    args["vote_new_owner"] = field

    return DomainRegistrationStatusTransfer(**args)


def unmarshal_RecordChangeAdd(data: Any) -> RecordChangeAdd:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'RecordChangeAdd' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records")
    args["records"] = [unmarshal_DomainRecord(v) for v in data["records"]]

    return RecordChangeAdd(**args)


def unmarshal_RecordChangeClear(data: Any) -> RecordChangeClear:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'RecordChangeClear' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return RecordChangeClear(**args)


def unmarshal_RecordChangeDelete(data: Any) -> RecordChangeDelete:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'RecordChangeDelete' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id")
    args["id"] = field

    field = data.get("id_fields")
    args["id_fields"] = unmarshal_RecordIdentifier(field) if field is not None else None

    return RecordChangeDelete(**args)


def unmarshal_RecordChangeSet(data: Any) -> RecordChangeSet:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'RecordChangeSet' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id")
    args["id"] = field

    field = data.get("id_fields")
    args["id_fields"] = unmarshal_RecordIdentifier(field) if field is not None else None

    field = data.get("records")
    args["records"] = [unmarshal_DomainRecord(v) for v in data["records"]]

    return RecordChangeSet(**args)


def unmarshal_Tld(data: Any) -> Tld:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Tld' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dnssec_support")
    args["dnssec_support"] = field

    field = data.get("duration_in_years_max")
    args["duration_in_years_max"] = field

    field = data.get("duration_in_years_min")
    args["duration_in_years_min"] = field

    field = data.get("idn_support")
    args["idn_support"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("offers")
    args["offers"] = {k: unmarshal_TldOffer(v) for k, v in data["offers"].items()}

    field = data.get("specifications")
    args["specifications"] = field

    return Tld(**args)


def unmarshal_AvailableDomain(data: Any) -> AvailableDomain:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'AvailableDomain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("available")
    args["available"] = field

    field = data.get("domain")
    args["domain"] = field

    field = data.get("tld")
    args["tld"] = unmarshal_Tld(field) if field is not None else None

    return AvailableDomain(**args)


def unmarshal_CheckContactsCompatibilityResponseContactCheckResult(
    data: Any,
) -> CheckContactsCompatibilityResponseContactCheckResult:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CheckContactsCompatibilityResponseContactCheckResult' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("compatible")
    args["compatible"] = field

    field = data.get("error_message")
    args["error_message"] = field

    return CheckContactsCompatibilityResponseContactCheckResult(**args)


def unmarshal_ContactRoles(data: Any) -> ContactRoles:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ContactRoles' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("contact")
    args["contact"] = unmarshal_Contact(field) if field is not None else None

    field = data.get("roles")
    args["roles"] = {
        k: unmarshal_ContactRolesRoles(v) for k, v in data["roles"].items()
    }

    return ContactRoles(**args)


def unmarshal_DNSZone(data: Any) -> DNSZone:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DNSZone' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain")
    args["domain"] = field

    field = data.get("message")
    args["message"] = field

    field = data.get("ns")
    args["ns"] = field

    field = data.get("ns_default")
    args["ns_default"] = field

    field = data.get("ns_master")
    args["ns_master"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("subdomain")
    args["subdomain"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return DNSZone(**args)


def unmarshal_DNSZoneVersion(data: Any) -> DNSZoneVersion:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DNSZoneVersion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id")
    args["id"] = field

    return DNSZoneVersion(**args)


def unmarshal_DomainDNSSEC(data: Any) -> DomainDNSSEC:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DomainDNSSEC' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ds_records")
    args["ds_records"] = [unmarshal_DSRecord(v) for v in data["ds_records"]]

    field = data.get("status")
    args["status"] = field

    return DomainDNSSEC(**args)


def unmarshal_DomainSummary(data: Any) -> DomainSummary:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DomainSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("auto_renew_status")
    args["auto_renew_status"] = field

    field = data.get("dnssec_status")
    args["dnssec_status"] = field

    field = data.get("domain")
    args["domain"] = field

    field = data.get("epp_code")
    args["epp_code"] = field

    field = data.get("expired_at")
    args["expired_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("external_domain_registration_status")
    args["external_domain_registration_status"] = (
        unmarshal_DomainRegistrationStatusExternalDomain(field)
        if field is not None
        else None
    )

    field = data.get("is_external")
    args["is_external"] = field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("registrar")
    args["registrar"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("transfer_registration_status")
    args["transfer_registration_status"] = (
        unmarshal_DomainRegistrationStatusTransfer(field) if field is not None else None
    )

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return DomainSummary(**args)


def unmarshal_Host(data: Any) -> Host:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Host' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain")
    args["domain"] = field

    field = data.get("ips")
    args["ips"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("status")
    args["status"] = field

    return Host(**args)


def unmarshal_Nameserver(data: Any) -> Nameserver:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Nameserver' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip")
    args["ip"] = field

    field = data.get("name")
    args["name"] = field

    return Nameserver(**args)


def unmarshal_RecordChange(data: Any) -> RecordChange:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'RecordChange' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("add")
    args["add"] = unmarshal_RecordChangeAdd(field) if field is not None else None

    field = data.get("clear")
    args["clear"] = unmarshal_RecordChangeClear(field) if field is not None else None

    field = data.get("delete")
    args["delete"] = unmarshal_RecordChangeDelete(field) if field is not None else None

    field = data.get("set_")
    args["set_"] = unmarshal_RecordChangeSet(field) if field is not None else None

    return RecordChange(**args)


def unmarshal_RenewableDomain(data: Any) -> RenewableDomain:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'RenewableDomain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain")
    args["domain"] = field

    field = data.get("estimated_delete_at")
    args["estimated_delete_at"] = (
        parser.isoparse(field) if type(field) is str else field
    )

    field = data.get("expired_at")
    args["expired_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("limit_redemption_at")
    args["limit_redemption_at"] = (
        parser.isoparse(field) if type(field) is str else field
    )

    field = data.get("limit_renew_at")
    args["limit_renew_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("renewable_duration_in_years")
    args["renewable_duration_in_years"] = field

    field = data.get("status")
    args["status"] = field

    return RenewableDomain(**args)


def unmarshal_SSLCertificate(data: Any) -> SSLCertificate:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SSLCertificate' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("alternative_dns_zones")
    args["alternative_dns_zones"] = field

    field = data.get("certificate_chain")
    args["certificate_chain"] = field

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("dns_zone")
    args["dns_zone"] = field

    field = data.get("expired_at")
    args["expired_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("private_key")
    args["private_key"] = field

    field = data.get("status")
    args["status"] = field

    return SSLCertificate(**args)


def unmarshal_Task(data: Any) -> Task:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Task' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain")
    args["domain"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("message")
    args["message"] = field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("started_at")
    args["started_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("status")
    args["status"] = field

    field = data.get("type_")
    args["type_"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return Task(**args)


def unmarshal_CheckContactsCompatibilityResponse(
    data: Any,
) -> CheckContactsCompatibilityResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CheckContactsCompatibilityResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("administrative_check_result")
    args["administrative_check_result"] = (
        unmarshal_CheckContactsCompatibilityResponseContactCheckResult(field)
        if field is not None
        else None
    )

    field = data.get("compatible")
    args["compatible"] = field

    field = data.get("owner_check_result")
    args["owner_check_result"] = (
        unmarshal_CheckContactsCompatibilityResponseContactCheckResult(field)
        if field is not None
        else None
    )

    field = data.get("technical_check_result")
    args["technical_check_result"] = (
        unmarshal_CheckContactsCompatibilityResponseContactCheckResult(field)
        if field is not None
        else None
    )

    return CheckContactsCompatibilityResponse(**args)


def unmarshal_ClearDNSZoneRecordsResponse(data: Any) -> ClearDNSZoneRecordsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ClearDNSZoneRecordsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return ClearDNSZoneRecordsResponse(**args)


def unmarshal_DeleteDNSZoneResponse(data: Any) -> DeleteDNSZoneResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DeleteDNSZoneResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return DeleteDNSZoneResponse(**args)


def unmarshal_DeleteExternalDomainResponse(data: Any) -> DeleteExternalDomainResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DeleteExternalDomainResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return DeleteExternalDomainResponse(**args)


def unmarshal_DeleteSSLCertificateResponse(data: Any) -> DeleteSSLCertificateResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DeleteSSLCertificateResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return DeleteSSLCertificateResponse(**args)


def unmarshal_Domain(data: Any) -> Domain:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Domain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("administrative_contact")
    args["administrative_contact"] = (
        unmarshal_Contact(field) if field is not None else None
    )

    field = data.get("auto_renew_status")
    args["auto_renew_status"] = field

    field = data.get("dns_zones")
    args["dns_zones"] = [unmarshal_DNSZone(v) for v in data["dns_zones"]]

    field = data.get("dnssec")
    args["dnssec"] = unmarshal_DomainDNSSEC(field) if field is not None else None

    field = data.get("domain")
    args["domain"] = field

    field = data.get("epp_code")
    args["epp_code"] = field

    field = data.get("expired_at")
    args["expired_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("external_domain_registration_status")
    args["external_domain_registration_status"] = (
        unmarshal_DomainRegistrationStatusExternalDomain(field)
        if field is not None
        else None
    )

    field = data.get("is_external")
    args["is_external"] = field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("owner_contact")
    args["owner_contact"] = unmarshal_Contact(field) if field is not None else None

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("registrar")
    args["registrar"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("technical_contact")
    args["technical_contact"] = unmarshal_Contact(field) if field is not None else None

    field = data.get("transfer_registration_status")
    args["transfer_registration_status"] = (
        unmarshal_DomainRegistrationStatusTransfer(field) if field is not None else None
    )

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return Domain(**args)


def unmarshal_GetDNSZoneTsigKeyResponse(data: Any) -> GetDNSZoneTsigKeyResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetDNSZoneTsigKeyResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("algorithm")
    args["algorithm"] = field

    field = data.get("key")
    args["key"] = field

    field = data.get("name")
    args["name"] = field

    return GetDNSZoneTsigKeyResponse(**args)


def unmarshal_GetDNSZoneVersionDiffResponse(data: Any) -> GetDNSZoneVersionDiffResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetDNSZoneVersionDiffResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("changes")
    args["changes"] = [unmarshal_RecordChange(v) for v in data["changes"]]

    return GetDNSZoneVersionDiffResponse(**args)


def unmarshal_GetDomainAuthCodeResponse(data: Any) -> GetDomainAuthCodeResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetDomainAuthCodeResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("auth_code")
    args["auth_code"] = field

    return GetDomainAuthCodeResponse(**args)


def unmarshal_ImportProviderDNSZoneResponse(data: Any) -> ImportProviderDNSZoneResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ImportProviderDNSZoneResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records")
    args["records"] = [unmarshal_DomainRecord(v) for v in data["records"]]

    return ImportProviderDNSZoneResponse(**args)


def unmarshal_ImportRawDNSZoneResponse(data: Any) -> ImportRawDNSZoneResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ImportRawDNSZoneResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records")
    args["records"] = [unmarshal_DomainRecord(v) for v in data["records"]]

    return ImportRawDNSZoneResponse(**args)


def unmarshal_ListContactsResponse(data: Any) -> ListContactsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListContactsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("contacts")
    args["contacts"] = [unmarshal_ContactRoles(v) for v in data["contacts"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListContactsResponse(**args)


def unmarshal_ListDNSZoneNameserversResponse(
    data: Any,
) -> ListDNSZoneNameserversResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDNSZoneNameserversResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ns")
    args["ns"] = [unmarshal_Nameserver(v) for v in data["ns"]]

    return ListDNSZoneNameserversResponse(**args)


def unmarshal_ListDNSZoneRecordsResponse(data: Any) -> ListDNSZoneRecordsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDNSZoneRecordsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records")
    args["records"] = [unmarshal_DomainRecord(v) for v in data["records"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListDNSZoneRecordsResponse(**args)


def unmarshal_ListDNSZoneVersionRecordsResponse(
    data: Any,
) -> ListDNSZoneVersionRecordsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDNSZoneVersionRecordsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records")
    args["records"] = [unmarshal_DomainRecord(v) for v in data["records"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListDNSZoneVersionRecordsResponse(**args)


def unmarshal_ListDNSZoneVersionsResponse(data: Any) -> ListDNSZoneVersionsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDNSZoneVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count")
    args["total_count"] = field

    field = data.get("versions")
    args["versions"] = [unmarshal_DNSZoneVersion(v) for v in data["versions"]]

    return ListDNSZoneVersionsResponse(**args)


def unmarshal_ListDNSZonesResponse(data: Any) -> ListDNSZonesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDNSZonesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dns_zones")
    args["dns_zones"] = [unmarshal_DNSZone(v) for v in data["dns_zones"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListDNSZonesResponse(**args)


def unmarshal_ListDomainHostsResponse(data: Any) -> ListDomainHostsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDomainHostsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("hosts")
    args["hosts"] = [unmarshal_Host(v) for v in data["hosts"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListDomainHostsResponse(**args)


def unmarshal_ListDomainsResponse(data: Any) -> ListDomainsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDomainsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domains")
    args["domains"] = [unmarshal_DomainSummary(v) for v in data["domains"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListDomainsResponse(**args)


def unmarshal_ListRenewableDomainsResponse(data: Any) -> ListRenewableDomainsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListRenewableDomainsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domains")
    args["domains"] = [unmarshal_RenewableDomain(v) for v in data["domains"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListRenewableDomainsResponse(**args)


def unmarshal_ListSSLCertificatesResponse(data: Any) -> ListSSLCertificatesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListSSLCertificatesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("certificates")
    args["certificates"] = [unmarshal_SSLCertificate(v) for v in data["certificates"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListSSLCertificatesResponse(**args)


def unmarshal_ListTasksResponse(data: Any) -> ListTasksResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListTasksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("tasks")
    args["tasks"] = [unmarshal_Task(v) for v in data["tasks"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListTasksResponse(**args)


def unmarshal_OrderResponse(data: Any) -> OrderResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'OrderResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("domains")
    args["domains"] = field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("task_id")
    args["task_id"] = field

    return OrderResponse(**args)


def unmarshal_RefreshDNSZoneResponse(data: Any) -> RefreshDNSZoneResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'RefreshDNSZoneResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dns_zones")
    args["dns_zones"] = [unmarshal_DNSZone(v) for v in data["dns_zones"]]

    return RefreshDNSZoneResponse(**args)


def unmarshal_RegisterExternalDomainResponse(
    data: Any,
) -> RegisterExternalDomainResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'RegisterExternalDomainResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("domain")
    args["domain"] = field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("validation_token")
    args["validation_token"] = field

    return RegisterExternalDomainResponse(**args)


def unmarshal_RestoreDNSZoneVersionResponse(data: Any) -> RestoreDNSZoneVersionResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'RestoreDNSZoneVersionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return RestoreDNSZoneVersionResponse(**args)


def unmarshal_SearchAvailableDomainsResponse(
    data: Any,
) -> SearchAvailableDomainsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SearchAvailableDomainsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("available_domains")
    args["available_domains"] = [
        unmarshal_AvailableDomain(v) for v in data["available_domains"]
    ]

    return SearchAvailableDomainsResponse(**args)


def unmarshal_UpdateDNSZoneNameserversResponse(
    data: Any,
) -> UpdateDNSZoneNameserversResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'UpdateDNSZoneNameserversResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ns")
    args["ns"] = [unmarshal_Nameserver(v) for v in data["ns"]]

    return UpdateDNSZoneNameserversResponse(**args)


def unmarshal_UpdateDNSZoneRecordsResponse(data: Any) -> UpdateDNSZoneRecordsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'UpdateDNSZoneRecordsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records")
    args["records"] = [unmarshal_DomainRecord(v) for v in data["records"]]

    return UpdateDNSZoneRecordsResponse(**args)


def marshal_DomainRecordGeoIPConfigMatch(
    request: DomainRecordGeoIPConfigMatch,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "continents": request.continents,
        "countries": request.countries,
        "data": request.data,
    }


def marshal_DomainRecordViewConfigView(
    request: DomainRecordViewConfigView,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "data": request.data,
        "subnet": request.subnet,
    }


def marshal_DomainRecordWeightedConfigWeightedIP(
    request: DomainRecordWeightedConfigWeightedIP,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "ip": request.ip,
        "weight": request.weight,
    }


def marshal_DomainRecordGeoIPConfig(
    request: DomainRecordGeoIPConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "default": request.default,
        "matches": [
            marshal_DomainRecordGeoIPConfigMatch(v, defaults) for v in request.matches
        ],
    }


def marshal_DomainRecordHTTPServiceConfig(
    request: DomainRecordHTTPServiceConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "ips": request.ips,
        "must_contain": request.must_contain,
        "strategy": DomainRecordHTTPServiceConfigStrategy(request.strategy),
        "url": request.url,
        "user_agent": request.user_agent,
    }


def marshal_DomainRecordViewConfig(
    request: DomainRecordViewConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "views": [
            marshal_DomainRecordViewConfigView(v, defaults) for v in request.views
        ],
    }


def marshal_DomainRecordWeightedConfig(
    request: DomainRecordWeightedConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "weighted_ips": [
            marshal_DomainRecordWeightedConfigWeightedIP(v, defaults)
            for v in request.weighted_ips
        ],
    }


def marshal_ContactExtensionFRAssociationInfo(
    request: ContactExtensionFRAssociationInfo,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "publication_jo": request.publication_jo,
        "publication_jo_page": request.publication_jo_page,
    }


def marshal_ContactExtensionFRCodeAuthAfnicInfo(
    request: ContactExtensionFRCodeAuthAfnicInfo,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "code_auth_afnic": request.code_auth_afnic,
    }


def marshal_ContactExtensionFRDunsInfo(
    request: ContactExtensionFRDunsInfo,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "duns_id": request.duns_id,
        "local_id": request.local_id,
    }


def marshal_ContactExtensionFRIndividualInfo(
    request: ContactExtensionFRIndividualInfo,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "whois_opt_in": request.whois_opt_in,
    }


def marshal_ContactExtensionFRTrademarkInfo(
    request: ContactExtensionFRTrademarkInfo,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "trademark_inpi": request.trademark_inpi,
    }


def marshal_DSRecordPublicKey(
    request: DSRecordPublicKey,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "key": request.key,
    }


def marshal_DomainRecord(
    request: DomainRecord,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("geo_ip_config", request.geo_ip_config),
                OneOfPossibility("http_service_config", request.http_service_config),
                OneOfPossibility("weighted_config", request.weighted_config),
                OneOfPossibility("view_config", request.view_config),
            ]
        ),
        "comment": request.comment,
        "data": request.data,
        "id": request.id,
        "name": request.name,
        "priority": request.priority,
        "ttl": request.ttl,
        "type": DomainRecordType(request.type_),
    }


def marshal_RecordIdentifier(
    request: RecordIdentifier,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "data": request.data,
        "name": request.name,
        "ttl": request.ttl,
        "type": DomainRecordType(request.type_),
    }


def marshal_ContactExtensionEU(
    request: ContactExtensionEU,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "european_citizenship": request.european_citizenship,
    }


def marshal_ContactExtensionFR(
    request: ContactExtensionFR,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("individual_info", request.individual_info),
                OneOfPossibility("duns_info", request.duns_info),
                OneOfPossibility("association_info", request.association_info),
                OneOfPossibility("trademark_info", request.trademark_info),
                OneOfPossibility("code_auth_afnic_info", request.code_auth_afnic_info),
            ]
        ),
        "mode": ContactExtensionFRMode(request.mode),
    }


def marshal_ContactExtensionNL(
    request: ContactExtensionNL,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "legal_form": ContactExtensionNLLegalForm(request.legal_form),
        "legal_form_registration_number": request.legal_form_registration_number,
    }


def marshal_ContactQuestion(
    request: ContactQuestion,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "answer": request.answer,
        "question": request.question,
    }


def marshal_DSRecordDigest(
    request: DSRecordDigest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "digest": request.digest,
        "public_key": marshal_DSRecordPublicKey(request.public_key, defaults)
        if request.public_key is not None
        else None,
        "type": DSRecordDigestType(request.type_),
    }


def marshal_ImportRawDNSZoneRequestTsigKey(
    request: ImportRawDNSZoneRequestTsigKey,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "algorithm": request.algorithm,
        "key": request.key,
        "name": request.name,
    }


def marshal_RecordChangeAdd(
    request: RecordChangeAdd,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "records": [marshal_DomainRecord(v, defaults) for v in request.records],
    }


def marshal_RecordChangeClear(
    request: RecordChangeClear,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {}


def marshal_RecordChangeDelete(
    request: RecordChangeDelete,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("id", request.id),
                OneOfPossibility("id_fields", request.id_fields),
            ]
        ),
    }


def marshal_RecordChangeSet(
    request: RecordChangeSet,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("id", request.id),
                OneOfPossibility("id_fields", request.id_fields),
            ]
        ),
        "records": [marshal_DomainRecord(v, defaults) for v in request.records],
    }


def marshal_DSRecord(
    request: DSRecord,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("digest", request.digest),
                OneOfPossibility("public_key", request.public_key),
            ]
        ),
        "algorithm": DSRecordAlgorithm(request.algorithm),
        "key_id": request.key_id,
    }


def marshal_ImportProviderDNSZoneRequestOnlineV1(
    request: ImportProviderDNSZoneRequestOnlineV1,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "token": request.token,
    }


def marshal_ImportRawDNSZoneRequestAXFRSource(
    request: ImportRawDNSZoneRequestAXFRSource,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name_server": request.name_server,
        "tsig_key": marshal_ImportRawDNSZoneRequestTsigKey(request.tsig_key, defaults)
        if request.tsig_key is not None
        else None,
    }


def marshal_ImportRawDNSZoneRequestBindSource(
    request: ImportRawDNSZoneRequestBindSource,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "content": request.content,
    }


def marshal_Nameserver(
    request: Nameserver,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "ip": request.ip,
        "name": request.name,
    }


def marshal_NewContact(
    request: NewContact,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "address_line_1": request.address_line_1,
        "address_line_2": request.address_line_2,
        "city": request.city,
        "company_identification_code": request.company_identification_code,
        "company_name": request.company_name,
        "country": request.country,
        "email": request.email,
        "email_alt": request.email_alt,
        "extension_eu": marshal_ContactExtensionEU(request.extension_eu, defaults)
        if request.extension_eu is not None
        else None,
        "extension_fr": marshal_ContactExtensionFR(request.extension_fr, defaults)
        if request.extension_fr is not None
        else None,
        "extension_nl": marshal_ContactExtensionNL(request.extension_nl, defaults)
        if request.extension_nl is not None
        else None,
        "fax_number": request.fax_number,
        "firstname": request.firstname,
        "lang": LanguageCode(request.lang),
        "lastname": request.lastname,
        "legal_form": ContactLegalForm(request.legal_form),
        "phone_number": request.phone_number,
        "questions": [marshal_ContactQuestion(v, defaults) for v in request.questions]
        if request.questions is not None
        else None,
        "resale": request.resale,
        "state": request.state,
        "vat_identification_code": request.vat_identification_code,
        "whois_opt_in": request.whois_opt_in,
        "zip": request.zip,
    }


def marshal_RecordChange(
    request: RecordChange,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("add", request.add),
                OneOfPossibility("set", request.set_),
                OneOfPossibility("delete", request.delete),
                OneOfPossibility("clear", request.clear),
            ]
        ),
    }


def marshal_TransferInDomainRequestTransferRequest(
    request: TransferInDomainRequestTransferRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "auth_code": request.auth_code,
        "domain": request.domain,
    }


def marshal_UpdateContactRequestQuestion(
    request: UpdateContactRequestQuestion,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "answer": request.answer,
        "question": request.question,
    }


def marshal_CloneDNSZoneRequest(
    request: CloneDNSZoneRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "dest_dns_zone": request.dest_dns_zone,
        "overwrite": request.overwrite,
        "project_id": request.project_id or defaults.default_project_id,
    }


def marshal_CreateDNSZoneRequest(
    request: CreateDNSZoneRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "domain": request.domain,
        "project_id": request.project_id or defaults.default_project_id,
        "subdomain": request.subdomain,
    }


def marshal_CreateSSLCertificateRequest(
    request: CreateSSLCertificateRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "alternative_dns_zones": request.alternative_dns_zones,
        "dns_zone": request.dns_zone,
    }


def marshal_ImportProviderDNSZoneRequest(
    request: ImportProviderDNSZoneRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("online_v1", request.online_v1),
            ]
        ),
    }


def marshal_ImportRawDNSZoneRequest(
    request: ImportRawDNSZoneRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("bind_source", request.bind_source),
                OneOfPossibility("axfr_source", request.axfr_source),
            ]
        ),
        "content": request.content,
        "format": RawFormat(request.format) if request.format is not None else None,
        "project_id": request.project_id or defaults.default_project_id,
    }


def marshal_RefreshDNSZoneRequest(
    request: RefreshDNSZoneRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "recreate_dns_zone": request.recreate_dns_zone,
        "recreate_sub_dns_zone": request.recreate_sub_dns_zone,
    }


def marshal_RegistrarApiBuyDomainsRequest(
    request: RegistrarApiBuyDomainsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "administrative_contact_id", request.administrative_contact_id
                ),
                OneOfPossibility(
                    "administrative_contact", request.administrative_contact
                ),
            ]
        ),
        **resolve_one_of(
            [
                OneOfPossibility("owner_contact_id", request.owner_contact_id),
                OneOfPossibility("owner_contact", request.owner_contact),
            ]
        ),
        **resolve_one_of(
            [
                OneOfPossibility("technical_contact_id", request.technical_contact_id),
                OneOfPossibility("technical_contact", request.technical_contact),
            ]
        ),
        "domains": request.domains,
        "duration_in_years": request.duration_in_years,
        "project_id": request.project_id or defaults.default_project_id,
    }


def marshal_RegistrarApiCheckContactsCompatibilityRequest(
    request: RegistrarApiCheckContactsCompatibilityRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "administrative_contact_id", request.administrative_contact_id
                ),
                OneOfPossibility(
                    "administrative_contact", request.administrative_contact
                ),
            ]
        ),
        **resolve_one_of(
            [
                OneOfPossibility("owner_contact_id", request.owner_contact_id),
                OneOfPossibility("owner_contact", request.owner_contact),
            ]
        ),
        **resolve_one_of(
            [
                OneOfPossibility("domain", request.domain),
                OneOfPossibility("tld", request.tld),
            ]
        ),
        **resolve_one_of(
            [
                OneOfPossibility("technical_contact_id", request.technical_contact_id),
                OneOfPossibility("technical_contact", request.technical_contact),
            ]
        ),
    }


def marshal_RegistrarApiCreateDomainHostRequest(
    request: RegistrarApiCreateDomainHostRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "ips": request.ips,
        "name": request.name,
    }


def marshal_RegistrarApiEnableDomainDNSSECRequest(
    request: RegistrarApiEnableDomainDNSSECRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "ds_record": marshal_DSRecord(request.ds_record, defaults)
        if request.ds_record is not None
        else None,
    }


def marshal_RegistrarApiRegisterExternalDomainRequest(
    request: RegistrarApiRegisterExternalDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "domain": request.domain,
        "project_id": request.project_id or defaults.default_project_id,
    }


def marshal_RegistrarApiRenewDomainsRequest(
    request: RegistrarApiRenewDomainsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "domains": request.domains,
        "duration_in_years": request.duration_in_years,
        "force_late_renewal": request.force_late_renewal,
    }


def marshal_RegistrarApiTradeDomainRequest(
    request: RegistrarApiTradeDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("new_owner_contact_id", request.new_owner_contact_id),
                OneOfPossibility("new_owner_contact", request.new_owner_contact),
            ]
        ),
        "project_id": request.project_id or defaults.default_project_id,
    }


def marshal_RegistrarApiTransferInDomainRequest(
    request: RegistrarApiTransferInDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "administrative_contact_id", request.administrative_contact_id
                ),
                OneOfPossibility(
                    "administrative_contact", request.administrative_contact
                ),
            ]
        ),
        **resolve_one_of(
            [
                OneOfPossibility("owner_contact_id", request.owner_contact_id),
                OneOfPossibility("owner_contact", request.owner_contact),
            ]
        ),
        **resolve_one_of(
            [
                OneOfPossibility("technical_contact_id", request.technical_contact_id),
                OneOfPossibility("technical_contact", request.technical_contact),
            ]
        ),
        "domains": [
            marshal_TransferInDomainRequestTransferRequest(v, defaults)
            for v in request.domains
        ],
        "project_id": request.project_id or defaults.default_project_id,
    }


def marshal_RegistrarApiUpdateContactRequest(
    request: RegistrarApiUpdateContactRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "address_line_1": request.address_line_1,
        "address_line_2": request.address_line_2,
        "city": request.city,
        "company_identification_code": request.company_identification_code,
        "country": request.country,
        "email": request.email,
        "email_alt": request.email_alt,
        "extension_eu": marshal_ContactExtensionEU(request.extension_eu, defaults)
        if request.extension_eu is not None
        else None,
        "extension_fr": marshal_ContactExtensionFR(request.extension_fr, defaults)
        if request.extension_fr is not None
        else None,
        "extension_nl": marshal_ContactExtensionNL(request.extension_nl, defaults)
        if request.extension_nl is not None
        else None,
        "fax_number": request.fax_number,
        "lang": LanguageCode(request.lang),
        "phone_number": request.phone_number,
        "questions": [
            marshal_UpdateContactRequestQuestion(v, defaults) for v in request.questions
        ]
        if request.questions is not None
        else None,
        "resale": request.resale,
        "state": request.state,
        "vat_identification_code": request.vat_identification_code,
        "whois_opt_in": request.whois_opt_in,
        "zip": request.zip,
    }


def marshal_RegistrarApiUpdateDomainHostRequest(
    request: RegistrarApiUpdateDomainHostRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "ips": request.ips,
    }


def marshal_RegistrarApiUpdateDomainRequest(
    request: RegistrarApiUpdateDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "administrative_contact_id", request.administrative_contact_id
                ),
                OneOfPossibility(
                    "administrative_contact", request.administrative_contact
                ),
            ]
        ),
        **resolve_one_of(
            [
                OneOfPossibility("owner_contact_id", request.owner_contact_id),
                OneOfPossibility("owner_contact", request.owner_contact),
            ]
        ),
        **resolve_one_of(
            [
                OneOfPossibility("technical_contact_id", request.technical_contact_id),
                OneOfPossibility("technical_contact", request.technical_contact),
            ]
        ),
    }


def marshal_UpdateDNSZoneNameserversRequest(
    request: UpdateDNSZoneNameserversRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "ns": [marshal_Nameserver(v, defaults) for v in request.ns],
    }


def marshal_UpdateDNSZoneRecordsRequest(
    request: UpdateDNSZoneRecordsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "changes": [marshal_RecordChange(v, defaults) for v in request.changes],
        "disallow_new_zone_creation": request.disallow_new_zone_creation,
        "return_all_records": request.return_all_records,
        "serial": request.serial,
    }


def marshal_UpdateDNSZoneRequest(
    request: UpdateDNSZoneRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "new_dns_zone": request.new_dns_zone,
        "project_id": request.project_id or defaults.default_project_id,
    }
