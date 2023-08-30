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
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRecordGeoIPConfigMatch' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("continents", None)
    args["continents"] = field

    field = data.get("countries", None)
    args["countries"] = field

    field = data.get("data", None)
    args["data"] = field

    return DomainRecordGeoIPConfigMatch(**args)


def unmarshal_DomainRecordViewConfigView(data: Any) -> DomainRecordViewConfigView:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRecordViewConfigView' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("data", None)
    args["data"] = field

    field = data.get("subnet", None)
    args["subnet"] = field

    return DomainRecordViewConfigView(**args)


def unmarshal_DomainRecordWeightedConfigWeightedIP(
    data: Any,
) -> DomainRecordWeightedConfigWeightedIP:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRecordWeightedConfigWeightedIP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip", None)
    args["ip"] = field

    field = data.get("weight", None)
    args["weight"] = field

    return DomainRecordWeightedConfigWeightedIP(**args)


def unmarshal_ContactExtensionFRAssociationInfo(
    data: Any,
) -> ContactExtensionFRAssociationInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionFRAssociationInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("publication_jo", None)
    args["publication_jo"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("publication_jo_page", None)
    args["publication_jo_page"] = field

    return ContactExtensionFRAssociationInfo(**args)


def unmarshal_ContactExtensionFRCodeAuthAfnicInfo(
    data: Any,
) -> ContactExtensionFRCodeAuthAfnicInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionFRCodeAuthAfnicInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("code_auth_afnic", None)
    args["code_auth_afnic"] = field

    return ContactExtensionFRCodeAuthAfnicInfo(**args)


def unmarshal_ContactExtensionFRDunsInfo(data: Any) -> ContactExtensionFRDunsInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionFRDunsInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("duns_id", None)
    args["duns_id"] = field

    field = data.get("local_id", None)
    args["local_id"] = field

    return ContactExtensionFRDunsInfo(**args)


def unmarshal_ContactExtensionFRIndividualInfo(
    data: Any,
) -> ContactExtensionFRIndividualInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionFRIndividualInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("whois_opt_in", None)
    args["whois_opt_in"] = field

    return ContactExtensionFRIndividualInfo(**args)


def unmarshal_ContactExtensionFRTrademarkInfo(
    data: Any,
) -> ContactExtensionFRTrademarkInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionFRTrademarkInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("trademark_inpi", None)
    args["trademark_inpi"] = field

    return ContactExtensionFRTrademarkInfo(**args)


def unmarshal_DSRecordPublicKey(data: Any) -> DSRecordPublicKey:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DSRecordPublicKey' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("key", None)
    args["key"] = field

    return DSRecordPublicKey(**args)


def unmarshal_DomainRecordGeoIPConfig(data: Any) -> DomainRecordGeoIPConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRecordGeoIPConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("default", None)
    args["default"] = field

    field = data.get("matches", None)
    args["matches"] = (
        [unmarshal_DomainRecordGeoIPConfigMatch(v) for v in field]
        if field is not None
        else None
    )

    return DomainRecordGeoIPConfig(**args)


def unmarshal_DomainRecordHTTPServiceConfig(data: Any) -> DomainRecordHTTPServiceConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRecordHTTPServiceConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ips", None)
    args["ips"] = field

    field = data.get("must_contain", None)
    args["must_contain"] = field

    field = data.get("strategy", None)
    args["strategy"] = field

    field = data.get("url", None)
    args["url"] = field

    field = data.get("user_agent", None)
    args["user_agent"] = field

    return DomainRecordHTTPServiceConfig(**args)


def unmarshal_DomainRecordViewConfig(data: Any) -> DomainRecordViewConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRecordViewConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("views", None)
    args["views"] = (
        [unmarshal_DomainRecordViewConfigView(v) for v in field]
        if field is not None
        else None
    )

    return DomainRecordViewConfig(**args)


def unmarshal_DomainRecordWeightedConfig(data: Any) -> DomainRecordWeightedConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRecordWeightedConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("weighted_ips", None)
    args["weighted_ips"] = (
        [unmarshal_DomainRecordWeightedConfigWeightedIP(v) for v in field]
        if field is not None
        else None
    )

    return DomainRecordWeightedConfig(**args)


def unmarshal_ContactExtensionEU(data: Any) -> ContactExtensionEU:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionEU' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("european_citizenship", None)
    args["european_citizenship"] = field

    return ContactExtensionEU(**args)


def unmarshal_ContactExtensionFR(data: Any) -> ContactExtensionFR:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionFR' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("association_info", None)
    args["association_info"] = (
        unmarshal_ContactExtensionFRAssociationInfo(field)
        if field is not None
        else None
    )

    field = data.get("code_auth_afnic_info", None)
    args["code_auth_afnic_info"] = (
        unmarshal_ContactExtensionFRCodeAuthAfnicInfo(field)
        if field is not None
        else None
    )

    field = data.get("duns_info", None)
    args["duns_info"] = (
        unmarshal_ContactExtensionFRDunsInfo(field) if field is not None else None
    )

    field = data.get("individual_info", None)
    args["individual_info"] = (
        unmarshal_ContactExtensionFRIndividualInfo(field) if field is not None else None
    )

    field = data.get("mode", None)
    args["mode"] = field

    field = data.get("trademark_info", None)
    args["trademark_info"] = (
        unmarshal_ContactExtensionFRTrademarkInfo(field) if field is not None else None
    )

    return ContactExtensionFR(**args)


def unmarshal_ContactExtensionNL(data: Any) -> ContactExtensionNL:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionNL' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("legal_form", None)
    args["legal_form"] = field

    field = data.get("legal_form_registration_number", None)
    args["legal_form_registration_number"] = field

    return ContactExtensionNL(**args)


def unmarshal_ContactQuestion(data: Any) -> ContactQuestion:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactQuestion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("answer", None)
    args["answer"] = field

    field = data.get("question", None)
    args["question"] = field

    return ContactQuestion(**args)


def unmarshal_DSRecordDigest(data: Any) -> DSRecordDigest:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DSRecordDigest' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("digest", None)
    args["digest"] = field

    field = data.get("public_key", None)
    args["public_key"] = (
        unmarshal_DSRecordPublicKey(field) if field is not None else None
    )

    field = data.get("type", None)
    args["type_"] = field

    return DSRecordDigest(**args)


def unmarshal_DomainRecord(data: Any) -> DomainRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRecord' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("comment", None)
    args["comment"] = field

    field = data.get("data", None)
    args["data"] = field

    field = data.get("geo_ip_config", None)
    args["geo_ip_config"] = (
        unmarshal_DomainRecordGeoIPConfig(field) if field is not None else None
    )

    field = data.get("http_service_config", None)
    args["http_service_config"] = (
        unmarshal_DomainRecordHTTPServiceConfig(field) if field is not None else None
    )

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("priority", None)
    args["priority"] = field

    field = data.get("ttl", None)
    args["ttl"] = field

    field = data.get("type", None)
    args["type_"] = field

    field = data.get("view_config", None)
    args["view_config"] = (
        unmarshal_DomainRecordViewConfig(field) if field is not None else None
    )

    field = data.get("weighted_config", None)
    args["weighted_config"] = (
        unmarshal_DomainRecordWeightedConfig(field) if field is not None else None
    )

    return DomainRecord(**args)


def unmarshal_RecordIdentifier(data: Any) -> RecordIdentifier:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordIdentifier' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("data", None)
    args["data"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("ttl", None)
    args["ttl"] = field

    field = data.get("type", None)
    args["type_"] = field

    return RecordIdentifier(**args)


def unmarshal_TldOffer(data: Any) -> TldOffer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TldOffer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("action", None)
    args["action"] = field

    field = data.get("operation_path", None)
    args["operation_path"] = field

    field = data.get("price", None)
    args["price"] = unmarshal_Money(field) if field is not None else None

    return TldOffer(**args)


def unmarshal_Contact(data: Any) -> Contact:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Contact' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("address_line_1", None)
    args["address_line_1"] = field

    field = data.get("address_line_2", None)
    args["address_line_2"] = field

    field = data.get("city", None)
    args["city"] = field

    field = data.get("company_identification_code", None)
    args["company_identification_code"] = field

    field = data.get("company_name", None)
    args["company_name"] = field

    field = data.get("country", None)
    args["country"] = field

    field = data.get("email", None)
    args["email"] = field

    field = data.get("email_alt", None)
    args["email_alt"] = field

    field = data.get("email_status", None)
    args["email_status"] = field

    field = data.get("extension_eu", None)
    args["extension_eu"] = (
        unmarshal_ContactExtensionEU(field) if field is not None else None
    )

    field = data.get("extension_fr", None)
    args["extension_fr"] = (
        unmarshal_ContactExtensionFR(field) if field is not None else None
    )

    field = data.get("extension_nl", None)
    args["extension_nl"] = (
        unmarshal_ContactExtensionNL(field) if field is not None else None
    )

    field = data.get("fax_number", None)
    args["fax_number"] = field

    field = data.get("firstname", None)
    args["firstname"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("lang", None)
    args["lang"] = field

    field = data.get("lastname", None)
    args["lastname"] = field

    field = data.get("legal_form", None)
    args["legal_form"] = field

    field = data.get("phone_number", None)
    args["phone_number"] = field

    field = data.get("questions", None)
    args["questions"] = (
        [unmarshal_ContactQuestion(v) for v in field] if field is not None else None
    )

    field = data.get("resale", None)
    args["resale"] = field

    field = data.get("state", None)
    args["state"] = field

    field = data.get("vat_identification_code", None)
    args["vat_identification_code"] = field

    field = data.get("whois_opt_in", None)
    args["whois_opt_in"] = field

    field = data.get("zip", None)
    args["zip"] = field

    return Contact(**args)


def unmarshal_ContactRolesRoles(data: Any) -> ContactRolesRoles:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactRolesRoles' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("is_administrative", None)
    args["is_administrative"] = field

    field = data.get("is_owner", None)
    args["is_owner"] = field

    field = data.get("is_technical", None)
    args["is_technical"] = field

    return ContactRolesRoles(**args)


def unmarshal_DSRecord(data: Any) -> DSRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DSRecord' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("algorithm", None)
    args["algorithm"] = field

    field = data.get("digest", None)
    args["digest"] = unmarshal_DSRecordDigest(field) if field is not None else None

    field = data.get("key_id", None)
    args["key_id"] = field

    field = data.get("public_key", None)
    args["public_key"] = (
        unmarshal_DSRecordPublicKey(field) if field is not None else None
    )

    return DSRecord(**args)


def unmarshal_DomainRegistrationStatusExternalDomain(
    data: Any,
) -> DomainRegistrationStatusExternalDomain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRegistrationStatusExternalDomain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("validation_token", None)
    args["validation_token"] = field

    return DomainRegistrationStatusExternalDomain(**args)


def unmarshal_DomainRegistrationStatusTransfer(
    data: Any,
) -> DomainRegistrationStatusTransfer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRegistrationStatusTransfer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("status", None)
    args["status"] = field

    field = data.get("vote_current_owner", None)
    args["vote_current_owner"] = field

    field = data.get("vote_new_owner", None)
    args["vote_new_owner"] = field

    return DomainRegistrationStatusTransfer(**args)


def unmarshal_RecordChangeAdd(data: Any) -> RecordChangeAdd:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordChangeAdd' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records", None)
    args["records"] = (
        [unmarshal_DomainRecord(v) for v in field] if field is not None else None
    )

    return RecordChangeAdd(**args)


def unmarshal_RecordChangeClear(data: Any) -> RecordChangeClear:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordChangeClear' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return RecordChangeClear(**args)


def unmarshal_RecordChangeDelete(data: Any) -> RecordChangeDelete:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordChangeDelete' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("id_fields", None)
    args["id_fields"] = unmarshal_RecordIdentifier(field) if field is not None else None

    return RecordChangeDelete(**args)


def unmarshal_RecordChangeSet(data: Any) -> RecordChangeSet:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordChangeSet' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("id_fields", None)
    args["id_fields"] = unmarshal_RecordIdentifier(field) if field is not None else None

    field = data.get("records", None)
    args["records"] = (
        [unmarshal_DomainRecord(v) for v in field] if field is not None else None
    )

    return RecordChangeSet(**args)


def unmarshal_Tld(data: Any) -> Tld:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Tld' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dnssec_support", None)
    args["dnssec_support"] = field

    field = data.get("duration_in_years_max", None)
    args["duration_in_years_max"] = field

    field = data.get("duration_in_years_min", None)
    args["duration_in_years_min"] = field

    field = data.get("idn_support", None)
    args["idn_support"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("offers", None)
    args["offers"] = (
        {k: unmarshal_TldOffer(v) for k, v in field.items()}
        if field is not None
        else None
    )

    field = data.get("specifications", None)
    args["specifications"] = field

    return Tld(**args)


def unmarshal_AvailableDomain(data: Any) -> AvailableDomain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AvailableDomain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("available", None)
    args["available"] = field

    field = data.get("domain", None)
    args["domain"] = field

    field = data.get("tld", None)
    args["tld"] = unmarshal_Tld(field) if field is not None else None

    return AvailableDomain(**args)


def unmarshal_CheckContactsCompatibilityResponseContactCheckResult(
    data: Any,
) -> CheckContactsCompatibilityResponseContactCheckResult:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckContactsCompatibilityResponseContactCheckResult' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("compatible", None)
    args["compatible"] = field

    field = data.get("error_message", None)
    args["error_message"] = field

    return CheckContactsCompatibilityResponseContactCheckResult(**args)


def unmarshal_ContactRoles(data: Any) -> ContactRoles:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactRoles' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("contact", None)
    args["contact"] = unmarshal_Contact(field) if field is not None else None

    field = data.get("roles", None)
    args["roles"] = (
        {k: unmarshal_ContactRolesRoles(v) for k, v in field.items()}
        if field is not None
        else None
    )

    return ContactRoles(**args)


def unmarshal_DNSZone(data: Any) -> DNSZone:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DNSZone' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain", None)
    args["domain"] = field

    field = data.get("message", None)
    args["message"] = field

    field = data.get("ns", None)
    args["ns"] = field

    field = data.get("ns_default", None)
    args["ns_default"] = field

    field = data.get("ns_master", None)
    args["ns_master"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("subdomain", None)
    args["subdomain"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return DNSZone(**args)


def unmarshal_DNSZoneVersion(data: Any) -> DNSZoneVersion:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DNSZoneVersion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("id", None)
    args["id"] = field

    return DNSZoneVersion(**args)


def unmarshal_DomainDNSSEC(data: Any) -> DomainDNSSEC:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainDNSSEC' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ds_records", None)
    args["ds_records"] = (
        [unmarshal_DSRecord(v) for v in field] if field is not None else None
    )

    field = data.get("status", None)
    args["status"] = field

    return DomainDNSSEC(**args)


def unmarshal_DomainSummary(data: Any) -> DomainSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("auto_renew_status", None)
    args["auto_renew_status"] = field

    field = data.get("dnssec_status", None)
    args["dnssec_status"] = field

    field = data.get("domain", None)
    args["domain"] = field

    field = data.get("epp_code", None)
    args["epp_code"] = field

    field = data.get("expired_at", None)
    args["expired_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("external_domain_registration_status", None)
    args["external_domain_registration_status"] = (
        unmarshal_DomainRegistrationStatusExternalDomain(field)
        if field is not None
        else None
    )

    field = data.get("is_external", None)
    args["is_external"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("registrar", None)
    args["registrar"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("transfer_registration_status", None)
    args["transfer_registration_status"] = (
        unmarshal_DomainRegistrationStatusTransfer(field) if field is not None else None
    )

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return DomainSummary(**args)


def unmarshal_Host(data: Any) -> Host:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Host' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain", None)
    args["domain"] = field

    field = data.get("ips", None)
    args["ips"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("status", None)
    args["status"] = field

    return Host(**args)


def unmarshal_Nameserver(data: Any) -> Nameserver:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Nameserver' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip", None)
    args["ip"] = field

    field = data.get("name", None)
    args["name"] = field

    return Nameserver(**args)


def unmarshal_RecordChange(data: Any) -> RecordChange:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordChange' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("add", None)
    args["add"] = unmarshal_RecordChangeAdd(field) if field is not None else None

    field = data.get("clear", None)
    args["clear"] = unmarshal_RecordChangeClear(field) if field is not None else None

    field = data.get("delete", None)
    args["delete"] = unmarshal_RecordChangeDelete(field) if field is not None else None

    field = data.get("set", None)
    args["set_"] = unmarshal_RecordChangeSet(field) if field is not None else None

    return RecordChange(**args)


def unmarshal_RenewableDomain(data: Any) -> RenewableDomain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RenewableDomain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain", None)
    args["domain"] = field

    field = data.get("estimated_delete_at", None)
    args["estimated_delete_at"] = (
        parser.isoparse(field) if isinstance(field, str) else field
    )

    field = data.get("expired_at", None)
    args["expired_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("limit_redemption_at", None)
    args["limit_redemption_at"] = (
        parser.isoparse(field) if isinstance(field, str) else field
    )

    field = data.get("limit_renew_at", None)
    args["limit_renew_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("renewable_duration_in_years", None)
    args["renewable_duration_in_years"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("tld", None)
    args["tld"] = unmarshal_Tld(field) if field is not None else None

    return RenewableDomain(**args)


def unmarshal_SSLCertificate(data: Any) -> SSLCertificate:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SSLCertificate' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("alternative_dns_zones", None)
    args["alternative_dns_zones"] = field

    field = data.get("certificate_chain", None)
    args["certificate_chain"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("dns_zone", None)
    args["dns_zone"] = field

    field = data.get("expired_at", None)
    args["expired_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("private_key", None)
    args["private_key"] = field

    field = data.get("status", None)
    args["status"] = field

    return SSLCertificate(**args)


def unmarshal_Task(data: Any) -> Task:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Task' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain", None)
    args["domain"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("message", None)
    args["message"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("started_at", None)
    args["started_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("type", None)
    args["type_"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Task(**args)


def unmarshal_CheckContactsCompatibilityResponse(
    data: Any,
) -> CheckContactsCompatibilityResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckContactsCompatibilityResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("administrative_check_result", None)
    args["administrative_check_result"] = (
        unmarshal_CheckContactsCompatibilityResponseContactCheckResult(field)
        if field is not None
        else None
    )

    field = data.get("compatible", None)
    args["compatible"] = field

    field = data.get("owner_check_result", None)
    args["owner_check_result"] = (
        unmarshal_CheckContactsCompatibilityResponseContactCheckResult(field)
        if field is not None
        else None
    )

    field = data.get("technical_check_result", None)
    args["technical_check_result"] = (
        unmarshal_CheckContactsCompatibilityResponseContactCheckResult(field)
        if field is not None
        else None
    )

    return CheckContactsCompatibilityResponse(**args)


def unmarshal_ClearDNSZoneRecordsResponse(data: Any) -> ClearDNSZoneRecordsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClearDNSZoneRecordsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return ClearDNSZoneRecordsResponse(**args)


def unmarshal_DeleteDNSZoneResponse(data: Any) -> DeleteDNSZoneResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeleteDNSZoneResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return DeleteDNSZoneResponse(**args)


def unmarshal_DeleteExternalDomainResponse(data: Any) -> DeleteExternalDomainResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeleteExternalDomainResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return DeleteExternalDomainResponse(**args)


def unmarshal_DeleteSSLCertificateResponse(data: Any) -> DeleteSSLCertificateResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeleteSSLCertificateResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return DeleteSSLCertificateResponse(**args)


def unmarshal_Domain(data: Any) -> Domain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Domain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("administrative_contact", None)
    args["administrative_contact"] = (
        unmarshal_Contact(field) if field is not None else None
    )

    field = data.get("auto_renew_status", None)
    args["auto_renew_status"] = field

    field = data.get("dns_zones", None)
    args["dns_zones"] = (
        [unmarshal_DNSZone(v) for v in field] if field is not None else None
    )

    field = data.get("dnssec", None)
    args["dnssec"] = unmarshal_DomainDNSSEC(field) if field is not None else None

    field = data.get("domain", None)
    args["domain"] = field

    field = data.get("epp_code", None)
    args["epp_code"] = field

    field = data.get("expired_at", None)
    args["expired_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("external_domain_registration_status", None)
    args["external_domain_registration_status"] = (
        unmarshal_DomainRegistrationStatusExternalDomain(field)
        if field is not None
        else None
    )

    field = data.get("is_external", None)
    args["is_external"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("owner_contact", None)
    args["owner_contact"] = unmarshal_Contact(field) if field is not None else None

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("registrar", None)
    args["registrar"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("technical_contact", None)
    args["technical_contact"] = unmarshal_Contact(field) if field is not None else None

    field = data.get("tld", None)
    args["tld"] = unmarshal_Tld(field) if field is not None else None

    field = data.get("transfer_registration_status", None)
    args["transfer_registration_status"] = (
        unmarshal_DomainRegistrationStatusTransfer(field) if field is not None else None
    )

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Domain(**args)


def unmarshal_GetDNSZoneTsigKeyResponse(data: Any) -> GetDNSZoneTsigKeyResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetDNSZoneTsigKeyResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("algorithm", None)
    args["algorithm"] = field

    field = data.get("key", None)
    args["key"] = field

    field = data.get("name", None)
    args["name"] = field

    return GetDNSZoneTsigKeyResponse(**args)


def unmarshal_GetDNSZoneVersionDiffResponse(data: Any) -> GetDNSZoneVersionDiffResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetDNSZoneVersionDiffResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("changes", None)
    args["changes"] = (
        [unmarshal_RecordChange(v) for v in field] if field is not None else None
    )

    return GetDNSZoneVersionDiffResponse(**args)


def unmarshal_GetDomainAuthCodeResponse(data: Any) -> GetDomainAuthCodeResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetDomainAuthCodeResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("auth_code", None)
    args["auth_code"] = field

    return GetDomainAuthCodeResponse(**args)


def unmarshal_ImportProviderDNSZoneResponse(data: Any) -> ImportProviderDNSZoneResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ImportProviderDNSZoneResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records", None)
    args["records"] = (
        [unmarshal_DomainRecord(v) for v in field] if field is not None else None
    )

    return ImportProviderDNSZoneResponse(**args)


def unmarshal_ImportRawDNSZoneResponse(data: Any) -> ImportRawDNSZoneResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ImportRawDNSZoneResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records", None)
    args["records"] = (
        [unmarshal_DomainRecord(v) for v in field] if field is not None else None
    )

    return ImportRawDNSZoneResponse(**args)


def unmarshal_ListContactsResponse(data: Any) -> ListContactsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListContactsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("contacts", None)
    args["contacts"] = (
        [unmarshal_ContactRoles(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListContactsResponse(**args)


def unmarshal_ListDNSZoneNameserversResponse(
    data: Any,
) -> ListDNSZoneNameserversResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDNSZoneNameserversResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ns", None)
    args["ns"] = [unmarshal_Nameserver(v) for v in field] if field is not None else None

    return ListDNSZoneNameserversResponse(**args)


def unmarshal_ListDNSZoneRecordsResponse(data: Any) -> ListDNSZoneRecordsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDNSZoneRecordsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records", None)
    args["records"] = (
        [unmarshal_DomainRecord(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListDNSZoneRecordsResponse(**args)


def unmarshal_ListDNSZoneVersionRecordsResponse(
    data: Any,
) -> ListDNSZoneVersionRecordsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDNSZoneVersionRecordsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records", None)
    args["records"] = (
        [unmarshal_DomainRecord(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListDNSZoneVersionRecordsResponse(**args)


def unmarshal_ListDNSZoneVersionsResponse(data: Any) -> ListDNSZoneVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDNSZoneVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    args["total_count"] = field

    field = data.get("versions", None)
    args["versions"] = (
        [unmarshal_DNSZoneVersion(v) for v in field] if field is not None else None
    )

    return ListDNSZoneVersionsResponse(**args)


def unmarshal_ListDNSZonesResponse(data: Any) -> ListDNSZonesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDNSZonesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dns_zones", None)
    args["dns_zones"] = (
        [unmarshal_DNSZone(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListDNSZonesResponse(**args)


def unmarshal_ListDomainHostsResponse(data: Any) -> ListDomainHostsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDomainHostsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("hosts", None)
    args["hosts"] = [unmarshal_Host(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListDomainHostsResponse(**args)


def unmarshal_ListDomainsResponse(data: Any) -> ListDomainsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDomainsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domains", None)
    args["domains"] = (
        [unmarshal_DomainSummary(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListDomainsResponse(**args)


def unmarshal_ListRenewableDomainsResponse(data: Any) -> ListRenewableDomainsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRenewableDomainsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domains", None)
    args["domains"] = (
        [unmarshal_RenewableDomain(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListRenewableDomainsResponse(**args)


def unmarshal_ListSSLCertificatesResponse(data: Any) -> ListSSLCertificatesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSSLCertificatesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("certificates", None)
    args["certificates"] = (
        [unmarshal_SSLCertificate(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListSSLCertificatesResponse(**args)


def unmarshal_ListTasksResponse(data: Any) -> ListTasksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTasksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("tasks", None)
    args["tasks"] = [unmarshal_Task(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListTasksResponse(**args)


def unmarshal_OrderResponse(data: Any) -> OrderResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OrderResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("domains", None)
    args["domains"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("task_id", None)
    args["task_id"] = field

    return OrderResponse(**args)


def unmarshal_RefreshDNSZoneResponse(data: Any) -> RefreshDNSZoneResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RefreshDNSZoneResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dns_zones", None)
    args["dns_zones"] = (
        [unmarshal_DNSZone(v) for v in field] if field is not None else None
    )

    return RefreshDNSZoneResponse(**args)


def unmarshal_RegisterExternalDomainResponse(
    data: Any,
) -> RegisterExternalDomainResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RegisterExternalDomainResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("domain", None)
    args["domain"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("validation_token", None)
    args["validation_token"] = field

    return RegisterExternalDomainResponse(**args)


def unmarshal_RestoreDNSZoneVersionResponse(data: Any) -> RestoreDNSZoneVersionResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RestoreDNSZoneVersionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return RestoreDNSZoneVersionResponse(**args)


def unmarshal_SearchAvailableDomainsResponse(
    data: Any,
) -> SearchAvailableDomainsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SearchAvailableDomainsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("available_domains", None)
    args["available_domains"] = (
        [unmarshal_AvailableDomain(v) for v in field] if field is not None else None
    )

    return SearchAvailableDomainsResponse(**args)


def unmarshal_UpdateDNSZoneNameserversResponse(
    data: Any,
) -> UpdateDNSZoneNameserversResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateDNSZoneNameserversResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ns", None)
    args["ns"] = [unmarshal_Nameserver(v) for v in field] if field is not None else None

    return UpdateDNSZoneNameserversResponse(**args)


def unmarshal_UpdateDNSZoneRecordsResponse(data: Any) -> UpdateDNSZoneRecordsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateDNSZoneRecordsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records", None)
    args["records"] = (
        [unmarshal_DomainRecord(v) for v in field] if field is not None else None
    )

    return UpdateDNSZoneRecordsResponse(**args)


def marshal_DomainRecordGeoIPConfigMatch(
    request: DomainRecordGeoIPConfigMatch,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.continents is not None:
        output["continents"] = request.continents

    if request.countries is not None:
        output["countries"] = request.countries

    if request.data is not None:
        output["data"] = request.data

    return output


def marshal_DomainRecordViewConfigView(
    request: DomainRecordViewConfigView,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.data is not None:
        output["data"] = request.data

    if request.subnet is not None:
        output["subnet"] = request.subnet

    return output


def marshal_DomainRecordWeightedConfigWeightedIP(
    request: DomainRecordWeightedConfigWeightedIP,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip is not None:
        output["ip"] = request.ip

    if request.weight is not None:
        output["weight"] = request.weight

    return output


def marshal_DomainRecordGeoIPConfig(
    request: DomainRecordGeoIPConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.default is not None:
        output["default"] = request.default

    if request.matches is not None:
        output["matches"] = [
            marshal_DomainRecordGeoIPConfigMatch(v, defaults) for v in request.matches
        ]

    return output


def marshal_DomainRecordHTTPServiceConfig(
    request: DomainRecordHTTPServiceConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ips is not None:
        output["ips"] = request.ips

    if request.must_contain is not None:
        output["must_contain"] = request.must_contain

    if request.strategy is not None:
        output["strategy"] = DomainRecordHTTPServiceConfigStrategy(request.strategy)

    if request.url is not None:
        output["url"] = request.url

    if request.user_agent is not None:
        output["user_agent"] = request.user_agent

    return output


def marshal_DomainRecordViewConfig(
    request: DomainRecordViewConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.views is not None:
        output["views"] = [
            marshal_DomainRecordViewConfigView(v, defaults) for v in request.views
        ]

    return output


def marshal_DomainRecordWeightedConfig(
    request: DomainRecordWeightedConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.weighted_ips is not None:
        output["weighted_ips"] = [
            marshal_DomainRecordWeightedConfigWeightedIP(v, defaults)
            for v in request.weighted_ips
        ]

    return output


def marshal_ContactExtensionFRAssociationInfo(
    request: ContactExtensionFRAssociationInfo,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.publication_jo is not None:
        output["publication_jo"] = request.publication_jo

    if request.publication_jo_page is not None:
        output["publication_jo_page"] = request.publication_jo_page

    return output


def marshal_ContactExtensionFRCodeAuthAfnicInfo(
    request: ContactExtensionFRCodeAuthAfnicInfo,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.code_auth_afnic is not None:
        output["code_auth_afnic"] = request.code_auth_afnic

    return output


def marshal_ContactExtensionFRDunsInfo(
    request: ContactExtensionFRDunsInfo,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.duns_id is not None:
        output["duns_id"] = request.duns_id

    if request.local_id is not None:
        output["local_id"] = request.local_id

    return output


def marshal_ContactExtensionFRIndividualInfo(
    request: ContactExtensionFRIndividualInfo,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.whois_opt_in is not None:
        output["whois_opt_in"] = request.whois_opt_in

    return output


def marshal_ContactExtensionFRTrademarkInfo(
    request: ContactExtensionFRTrademarkInfo,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.trademark_inpi is not None:
        output["trademark_inpi"] = request.trademark_inpi

    return output


def marshal_DSRecordPublicKey(
    request: DSRecordPublicKey,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.key is not None:
        output["key"] = request.key

    return output


def marshal_DomainRecord(
    request: DomainRecord,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "geo_ip_config",
                    marshal_DomainRecordGeoIPConfig(request.geo_ip_config, defaults)
                    if request.geo_ip_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "http_service_config",
                    marshal_DomainRecordHTTPServiceConfig(
                        request.http_service_config, defaults
                    )
                    if request.http_service_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "weighted_config",
                    marshal_DomainRecordWeightedConfig(
                        request.weighted_config, defaults
                    )
                    if request.weighted_config is not None
                    else None,
                ),
                OneOfPossibility(
                    "view_config",
                    marshal_DomainRecordViewConfig(request.view_config, defaults)
                    if request.view_config is not None
                    else None,
                ),
            ]
        ),
    )

    if request.comment is not None:
        output["comment"] = request.comment

    if request.data is not None:
        output["data"] = request.data

    if request.id is not None:
        output["id"] = request.id

    if request.name is not None:
        output["name"] = request.name

    if request.priority is not None:
        output["priority"] = request.priority

    if request.ttl is not None:
        output["ttl"] = request.ttl

    if request.type_ is not None:
        output["type"] = DomainRecordType(request.type_)

    return output


def marshal_RecordIdentifier(
    request: RecordIdentifier,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.data is not None:
        output["data"] = request.data

    if request.name is not None:
        output["name"] = request.name

    if request.ttl is not None:
        output["ttl"] = request.ttl

    if request.type_ is not None:
        output["type"] = DomainRecordType(request.type_)

    return output


def marshal_ContactExtensionEU(
    request: ContactExtensionEU,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.european_citizenship is not None:
        output["european_citizenship"] = request.european_citizenship

    return output


def marshal_ContactExtensionFR(
    request: ContactExtensionFR,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "individual_info",
                    marshal_ContactExtensionFRIndividualInfo(
                        request.individual_info, defaults
                    )
                    if request.individual_info is not None
                    else None,
                ),
                OneOfPossibility(
                    "duns_info",
                    marshal_ContactExtensionFRDunsInfo(request.duns_info, defaults)
                    if request.duns_info is not None
                    else None,
                ),
                OneOfPossibility(
                    "association_info",
                    marshal_ContactExtensionFRAssociationInfo(
                        request.association_info, defaults
                    )
                    if request.association_info is not None
                    else None,
                ),
                OneOfPossibility(
                    "trademark_info",
                    marshal_ContactExtensionFRTrademarkInfo(
                        request.trademark_info, defaults
                    )
                    if request.trademark_info is not None
                    else None,
                ),
                OneOfPossibility(
                    "code_auth_afnic_info",
                    marshal_ContactExtensionFRCodeAuthAfnicInfo(
                        request.code_auth_afnic_info, defaults
                    )
                    if request.code_auth_afnic_info is not None
                    else None,
                ),
            ]
        ),
    )

    if request.mode is not None:
        output["mode"] = ContactExtensionFRMode(request.mode)

    return output


def marshal_ContactExtensionNL(
    request: ContactExtensionNL,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.legal_form is not None:
        output["legal_form"] = ContactExtensionNLLegalForm(request.legal_form)

    if request.legal_form_registration_number is not None:
        output[
            "legal_form_registration_number"
        ] = request.legal_form_registration_number

    return output


def marshal_ContactQuestion(
    request: ContactQuestion,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.answer is not None:
        output["answer"] = request.answer

    if request.question is not None:
        output["question"] = request.question

    return output


def marshal_DSRecordDigest(
    request: DSRecordDigest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.digest is not None:
        output["digest"] = request.digest

    if request.public_key is not None:
        output["public_key"] = marshal_DSRecordPublicKey(request.public_key, defaults)

    if request.type_ is not None:
        output["type"] = DSRecordDigestType(request.type_)

    return output


def marshal_ImportRawDNSZoneRequestTsigKey(
    request: ImportRawDNSZoneRequestTsigKey,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.algorithm is not None:
        output["algorithm"] = request.algorithm

    if request.key is not None:
        output["key"] = request.key

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_RecordChangeAdd(
    request: RecordChangeAdd,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.records is not None:
        output["records"] = [marshal_DomainRecord(v, defaults) for v in request.records]

    return output


def marshal_RecordChangeClear(
    request: RecordChangeClear,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    return output


def marshal_RecordChangeDelete(
    request: RecordChangeDelete,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("id", request.id if request.id is not None else None),
                OneOfPossibility(
                    "id_fields",
                    marshal_RecordIdentifier(request.id_fields, defaults)
                    if request.id_fields is not None
                    else None,
                ),
            ]
        ),
    )

    return output


def marshal_RecordChangeSet(
    request: RecordChangeSet,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("id", request.id if request.id is not None else None),
                OneOfPossibility(
                    "id_fields",
                    marshal_RecordIdentifier(request.id_fields, defaults)
                    if request.id_fields is not None
                    else None,
                ),
            ]
        ),
    )

    if request.records is not None:
        output["records"] = [marshal_DomainRecord(v, defaults) for v in request.records]

    return output


def marshal_DSRecord(
    request: DSRecord,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "digest",
                    marshal_DSRecordDigest(request.digest, defaults)
                    if request.digest is not None
                    else None,
                ),
                OneOfPossibility(
                    "public_key",
                    marshal_DSRecordPublicKey(request.public_key, defaults)
                    if request.public_key is not None
                    else None,
                ),
            ]
        ),
    )

    if request.algorithm is not None:
        output["algorithm"] = DSRecordAlgorithm(request.algorithm)

    if request.key_id is not None:
        output["key_id"] = request.key_id

    return output


def marshal_ImportProviderDNSZoneRequestOnlineV1(
    request: ImportProviderDNSZoneRequestOnlineV1,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.token is not None:
        output["token"] = request.token

    return output


def marshal_ImportRawDNSZoneRequestAXFRSource(
    request: ImportRawDNSZoneRequestAXFRSource,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name_server is not None:
        output["name_server"] = request.name_server

    if request.tsig_key is not None:
        output["tsig_key"] = marshal_ImportRawDNSZoneRequestTsigKey(
            request.tsig_key, defaults
        )

    return output


def marshal_ImportRawDNSZoneRequestBindSource(
    request: ImportRawDNSZoneRequestBindSource,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.content is not None:
        output["content"] = request.content

    return output


def marshal_Nameserver(
    request: Nameserver,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip is not None:
        output["ip"] = request.ip

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_NewContact(
    request: NewContact,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.address_line_1 is not None:
        output["address_line_1"] = request.address_line_1

    if request.address_line_2 is not None:
        output["address_line_2"] = request.address_line_2

    if request.city is not None:
        output["city"] = request.city

    if request.company_identification_code is not None:
        output["company_identification_code"] = request.company_identification_code

    if request.company_name is not None:
        output["company_name"] = request.company_name

    if request.country is not None:
        output["country"] = request.country

    if request.email is not None:
        output["email"] = request.email

    if request.email_alt is not None:
        output["email_alt"] = request.email_alt

    if request.extension_eu is not None:
        output["extension_eu"] = marshal_ContactExtensionEU(
            request.extension_eu, defaults
        )

    if request.extension_fr is not None:
        output["extension_fr"] = marshal_ContactExtensionFR(
            request.extension_fr, defaults
        )

    if request.extension_nl is not None:
        output["extension_nl"] = marshal_ContactExtensionNL(
            request.extension_nl, defaults
        )

    if request.fax_number is not None:
        output["fax_number"] = request.fax_number

    if request.firstname is not None:
        output["firstname"] = request.firstname

    if request.lang is not None:
        output["lang"] = LanguageCode(request.lang)

    if request.lastname is not None:
        output["lastname"] = request.lastname

    if request.legal_form is not None:
        output["legal_form"] = ContactLegalForm(request.legal_form)

    if request.phone_number is not None:
        output["phone_number"] = request.phone_number

    if request.questions is not None:
        output["questions"] = [
            marshal_ContactQuestion(v, defaults) for v in request.questions
        ]

    if request.resale is not None:
        output["resale"] = request.resale

    if request.state is not None:
        output["state"] = request.state

    if request.vat_identification_code is not None:
        output["vat_identification_code"] = request.vat_identification_code

    if request.whois_opt_in is not None:
        output["whois_opt_in"] = request.whois_opt_in

    if request.zip is not None:
        output["zip"] = request.zip

    return output


def marshal_RecordChange(
    request: RecordChange,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "add",
                    marshal_RecordChangeAdd(request.add, defaults)
                    if request.add is not None
                    else None,
                ),
                OneOfPossibility(
                    "set",
                    marshal_RecordChangeSet(request.set_, defaults)
                    if request.set_ is not None
                    else None,
                ),
                OneOfPossibility(
                    "delete",
                    marshal_RecordChangeDelete(request.delete, defaults)
                    if request.delete is not None
                    else None,
                ),
                OneOfPossibility(
                    "clear",
                    marshal_RecordChangeClear(request.clear, defaults)
                    if request.clear is not None
                    else None,
                ),
            ]
        ),
    )

    return output


def marshal_TransferInDomainRequestTransferRequest(
    request: TransferInDomainRequestTransferRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.auth_code is not None:
        output["auth_code"] = request.auth_code

    if request.domain is not None:
        output["domain"] = request.domain

    return output


def marshal_UpdateContactRequestQuestion(
    request: UpdateContactRequestQuestion,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.answer is not None:
        output["answer"] = request.answer

    if request.question is not None:
        output["question"] = request.question

    return output


def marshal_CloneDNSZoneRequest(
    request: CloneDNSZoneRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.dest_dns_zone is not None:
        output["dest_dns_zone"] = request.dest_dns_zone

    if request.overwrite is not None:
        output["overwrite"] = request.overwrite

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_CreateDNSZoneRequest(
    request: CreateDNSZoneRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domain is not None:
        output["domain"] = request.domain

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.subdomain is not None:
        output["subdomain"] = request.subdomain

    return output


def marshal_CreateSSLCertificateRequest(
    request: CreateSSLCertificateRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.alternative_dns_zones is not None:
        output["alternative_dns_zones"] = request.alternative_dns_zones

    if request.dns_zone is not None:
        output["dns_zone"] = request.dns_zone

    return output


def marshal_ImportProviderDNSZoneRequest(
    request: ImportProviderDNSZoneRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "online_v1",
                    marshal_ImportProviderDNSZoneRequestOnlineV1(
                        request.online_v1, defaults
                    )
                    if request.online_v1 is not None
                    else None,
                ),
            ]
        ),
    )

    return output


def marshal_ImportRawDNSZoneRequest(
    request: ImportRawDNSZoneRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "bind_source",
                    marshal_ImportRawDNSZoneRequestBindSource(
                        request.bind_source, defaults
                    )
                    if request.bind_source is not None
                    else None,
                ),
                OneOfPossibility(
                    "axfr_source",
                    marshal_ImportRawDNSZoneRequestAXFRSource(
                        request.axfr_source, defaults
                    )
                    if request.axfr_source is not None
                    else None,
                ),
            ]
        ),
    )

    if request.content is not None:
        output["content"] = request.content

    if request.format is not None:
        output["format"] = RawFormat(request.format)

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_RefreshDNSZoneRequest(
    request: RefreshDNSZoneRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.recreate_dns_zone is not None:
        output["recreate_dns_zone"] = request.recreate_dns_zone

    if request.recreate_sub_dns_zone is not None:
        output["recreate_sub_dns_zone"] = request.recreate_sub_dns_zone

    return output


def marshal_RegistrarApiBuyDomainsRequest(
    request: RegistrarApiBuyDomainsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "administrative_contact_id",
                    request.administrative_contact_id
                    if request.administrative_contact_id is not None
                    else None,
                ),
                OneOfPossibility(
                    "administrative_contact",
                    marshal_NewContact(request.administrative_contact, defaults)
                    if request.administrative_contact is not None
                    else None,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "owner_contact_id",
                    request.owner_contact_id
                    if request.owner_contact_id is not None
                    else None,
                ),
                OneOfPossibility(
                    "owner_contact",
                    marshal_NewContact(request.owner_contact, defaults)
                    if request.owner_contact is not None
                    else None,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "technical_contact_id",
                    request.technical_contact_id
                    if request.technical_contact_id is not None
                    else None,
                ),
                OneOfPossibility(
                    "technical_contact",
                    marshal_NewContact(request.technical_contact, defaults)
                    if request.technical_contact is not None
                    else None,
                ),
            ]
        ),
    )

    if request.domains is not None:
        output["domains"] = request.domains

    if request.duration_in_years is not None:
        output["duration_in_years"] = request.duration_in_years

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_RegistrarApiCheckContactsCompatibilityRequest(
    request: RegistrarApiCheckContactsCompatibilityRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "administrative_contact_id",
                    request.administrative_contact_id
                    if request.administrative_contact_id is not None
                    else None,
                ),
                OneOfPossibility(
                    "administrative_contact",
                    marshal_NewContact(request.administrative_contact, defaults)
                    if request.administrative_contact is not None
                    else None,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "owner_contact_id",
                    request.owner_contact_id
                    if request.owner_contact_id is not None
                    else None,
                ),
                OneOfPossibility(
                    "owner_contact",
                    marshal_NewContact(request.owner_contact, defaults)
                    if request.owner_contact is not None
                    else None,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "technical_contact_id",
                    request.technical_contact_id
                    if request.technical_contact_id is not None
                    else None,
                ),
                OneOfPossibility(
                    "technical_contact",
                    marshal_NewContact(request.technical_contact, defaults)
                    if request.technical_contact is not None
                    else None,
                ),
            ]
        ),
    )

    if request.domains is not None:
        output["domains"] = request.domains

    if request.tlds is not None:
        output["tlds"] = request.tlds

    return output


def marshal_RegistrarApiCreateDomainHostRequest(
    request: RegistrarApiCreateDomainHostRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ips is not None:
        output["ips"] = request.ips

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_RegistrarApiEnableDomainDNSSECRequest(
    request: RegistrarApiEnableDomainDNSSECRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ds_record is not None:
        output["ds_record"] = marshal_DSRecord(request.ds_record, defaults)

    return output


def marshal_RegistrarApiRegisterExternalDomainRequest(
    request: RegistrarApiRegisterExternalDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domain is not None:
        output["domain"] = request.domain

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_RegistrarApiRenewDomainsRequest(
    request: RegistrarApiRenewDomainsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domains is not None:
        output["domains"] = request.domains

    if request.duration_in_years is not None:
        output["duration_in_years"] = request.duration_in_years

    if request.force_late_renewal is not None:
        output["force_late_renewal"] = request.force_late_renewal

    return output


def marshal_RegistrarApiTradeDomainRequest(
    request: RegistrarApiTradeDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "new_owner_contact_id",
                    request.new_owner_contact_id
                    if request.new_owner_contact_id is not None
                    else None,
                ),
                OneOfPossibility(
                    "new_owner_contact",
                    marshal_NewContact(request.new_owner_contact, defaults)
                    if request.new_owner_contact is not None
                    else None,
                ),
            ]
        ),
    )

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_RegistrarApiTransferInDomainRequest(
    request: RegistrarApiTransferInDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "administrative_contact_id",
                    request.administrative_contact_id
                    if request.administrative_contact_id is not None
                    else None,
                ),
                OneOfPossibility(
                    "administrative_contact",
                    marshal_NewContact(request.administrative_contact, defaults)
                    if request.administrative_contact is not None
                    else None,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "owner_contact_id",
                    request.owner_contact_id
                    if request.owner_contact_id is not None
                    else None,
                ),
                OneOfPossibility(
                    "owner_contact",
                    marshal_NewContact(request.owner_contact, defaults)
                    if request.owner_contact is not None
                    else None,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "technical_contact_id",
                    request.technical_contact_id
                    if request.technical_contact_id is not None
                    else None,
                ),
                OneOfPossibility(
                    "technical_contact",
                    marshal_NewContact(request.technical_contact, defaults)
                    if request.technical_contact is not None
                    else None,
                ),
            ]
        ),
    )

    if request.domains is not None:
        output["domains"] = [
            marshal_TransferInDomainRequestTransferRequest(v, defaults)
            for v in request.domains
        ]

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_RegistrarApiUpdateContactRequest(
    request: RegistrarApiUpdateContactRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.address_line_1 is not None:
        output["address_line_1"] = request.address_line_1

    if request.address_line_2 is not None:
        output["address_line_2"] = request.address_line_2

    if request.city is not None:
        output["city"] = request.city

    if request.company_identification_code is not None:
        output["company_identification_code"] = request.company_identification_code

    if request.country is not None:
        output["country"] = request.country

    if request.email is not None:
        output["email"] = request.email

    if request.email_alt is not None:
        output["email_alt"] = request.email_alt

    if request.extension_eu is not None:
        output["extension_eu"] = marshal_ContactExtensionEU(
            request.extension_eu, defaults
        )

    if request.extension_fr is not None:
        output["extension_fr"] = marshal_ContactExtensionFR(
            request.extension_fr, defaults
        )

    if request.extension_nl is not None:
        output["extension_nl"] = marshal_ContactExtensionNL(
            request.extension_nl, defaults
        )

    if request.fax_number is not None:
        output["fax_number"] = request.fax_number

    if request.lang is not None:
        output["lang"] = LanguageCode(request.lang)

    if request.phone_number is not None:
        output["phone_number"] = request.phone_number

    if request.questions is not None:
        output["questions"] = [
            marshal_UpdateContactRequestQuestion(v, defaults) for v in request.questions
        ]

    if request.resale is not None:
        output["resale"] = request.resale

    if request.state is not None:
        output["state"] = request.state

    if request.vat_identification_code is not None:
        output["vat_identification_code"] = request.vat_identification_code

    if request.whois_opt_in is not None:
        output["whois_opt_in"] = request.whois_opt_in

    if request.zip is not None:
        output["zip"] = request.zip

    return output


def marshal_RegistrarApiUpdateDomainHostRequest(
    request: RegistrarApiUpdateDomainHostRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ips is not None:
        output["ips"] = request.ips

    return output


def marshal_RegistrarApiUpdateDomainRequest(
    request: RegistrarApiUpdateDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "administrative_contact_id",
                    request.administrative_contact_id
                    if request.administrative_contact_id is not None
                    else None,
                ),
                OneOfPossibility(
                    "administrative_contact",
                    marshal_NewContact(request.administrative_contact, defaults)
                    if request.administrative_contact is not None
                    else None,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "owner_contact_id",
                    request.owner_contact_id
                    if request.owner_contact_id is not None
                    else None,
                ),
                OneOfPossibility(
                    "owner_contact",
                    marshal_NewContact(request.owner_contact, defaults)
                    if request.owner_contact is not None
                    else None,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "technical_contact_id",
                    request.technical_contact_id
                    if request.technical_contact_id is not None
                    else None,
                ),
                OneOfPossibility(
                    "technical_contact",
                    marshal_NewContact(request.technical_contact, defaults)
                    if request.technical_contact is not None
                    else None,
                ),
            ]
        ),
    )

    return output


def marshal_UpdateDNSZoneNameserversRequest(
    request: UpdateDNSZoneNameserversRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ns is not None:
        output["ns"] = [marshal_Nameserver(v, defaults) for v in request.ns]

    return output


def marshal_UpdateDNSZoneRecordsRequest(
    request: UpdateDNSZoneRecordsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.changes is not None:
        output["changes"] = [marshal_RecordChange(v, defaults) for v in request.changes]

    if request.disallow_new_zone_creation is not None:
        output["disallow_new_zone_creation"] = request.disallow_new_zone_creation

    if request.return_all_records is not None:
        output["return_all_records"] = request.return_all_records

    if request.serial is not None:
        output["serial"] = request.serial

    return output


def marshal_UpdateDNSZoneRequest(
    request: UpdateDNSZoneRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.new_dns_zone is not None:
        output["new_dns_zone"] = request.new_dns_zone

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output
