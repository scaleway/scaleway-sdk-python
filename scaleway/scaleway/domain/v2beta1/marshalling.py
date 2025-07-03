# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from decimal import Decimal
from datetime import datetime
from typing import Any, Dict, List, Optional
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
    unmarshal_Money,
    marshal_Money,
    marshal_ScwFile,
    marshal_ServiceInfo,
    marshal_TimeSeries,
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    ContactEmailStatus,
    ContactExtensionFRMode,
    ContactExtensionNLLegalForm,
    ContactLegalForm,
    ContactStatus,
    DNSZoneStatus,
    DSRecordAlgorithm,
    DSRecordDigestType,
    DomainFeatureStatus,
    DomainRegistrationStatusTransferStatus,
    DomainStatus,
    HostStatus,
    LinkedProduct,
    ListContactsRequestRole,
    ListDNSZoneRecordsRequestOrderBy,
    ListDNSZonesRequestOrderBy,
    ListDomainsRequestOrderBy,
    ListRenewableDomainsRequestOrderBy,
    ListTasksRequestOrderBy,
    ListTldsRequestOrderBy,
    RawFormat,
    RecordHTTPServiceConfigStrategy,
    RecordType,
    RenewableDomainStatus,
    SSLCertificateStatus,
    TaskStatus,
    TaskType,
    ContactExtensionFRAssociationInfo,
    ContactExtensionFRCodeAuthAfnicInfo,
    ContactExtensionFRDunsInfo,
    ContactExtensionFRIndividualInfo,
    ContactExtensionFRTrademarkInfo,
    ContactExtensionEU,
    ContactExtensionFR,
    ContactExtensionNL,
    ContactQuestion,
    Contact,
    DNSZone,
    Host,
    SSLCertificate,
    CheckContactsCompatibilityResponseContactCheckResult,
    CheckContactsCompatibilityResponse,
    ClearDNSZoneRecordsResponse,
    DeleteDNSZoneResponse,
    DeleteExternalDomainResponse,
    DeleteSSLCertificateResponse,
    DSRecordPublicKey,
    DSRecordDigest,
    DSRecord,
    TldOffer,
    DomainDNSSEC,
    DomainRegistrationStatusExternalDomain,
    DomainRegistrationStatusTransfer,
    Tld,
    Domain,
    GetDNSZoneTsigKeyResponse,
    RecordGeoIPConfigMatch,
    RecordViewConfigView,
    RecordWeightedConfigWeightedIP,
    RecordGeoIPConfig,
    RecordHTTPServiceConfig,
    RecordViewConfig,
    RecordWeightedConfig,
    Record,
    RecordIdentifier,
    RecordChangeAdd,
    RecordChangeClear,
    RecordChangeDelete,
    RecordChangeSet,
    RecordChange,
    GetDNSZoneVersionDiffResponse,
    GetDomainAuthCodeResponse,
    ImportProviderDNSZoneResponse,
    ImportRawDNSZoneResponse,
    ContactRolesRoles,
    ContactRoles,
    ListContactsResponse,
    Nameserver,
    ListDNSZoneNameserversResponse,
    ListDNSZoneRecordsResponse,
    ListDNSZoneVersionRecordsResponse,
    DNSZoneVersion,
    ListDNSZoneVersionsResponse,
    ListDNSZonesResponse,
    ListDomainHostsResponse,
    DomainSummary,
    ListDomainsResponse,
    RenewableDomain,
    ListRenewableDomainsResponse,
    ListSSLCertificatesResponse,
    Task,
    ListTasksResponse,
    ListTldsResponse,
    OrderResponse,
    RefreshDNSZoneResponse,
    RegisterExternalDomainResponse,
    RestoreDNSZoneVersionResponse,
    AvailableDomain,
    SearchAvailableDomainsResponse,
    UpdateDNSZoneNameserversResponse,
    UpdateDNSZoneRecordsResponse,
    CloneDNSZoneRequest,
    CreateDNSZoneRequest,
    CreateSSLCertificateRequest,
    ImportProviderDNSZoneRequestOnlineV1,
    ImportProviderDNSZoneRequest,
    ImportRawDNSZoneRequestTsigKey,
    ImportRawDNSZoneRequestAXFRSource,
    ImportRawDNSZoneRequestBindSource,
    ImportRawDNSZoneRequest,
    RefreshDNSZoneRequest,
    NewContact,
    RegistrarApiBuyDomainsRequest,
    RegistrarApiCheckContactsCompatibilityRequest,
    RegistrarApiCreateDomainHostRequest,
    RegistrarApiEnableDomainDNSSECRequest,
    RegistrarApiRegisterExternalDomainRequest,
    RegistrarApiRenewDomainsRequest,
    RegistrarApiTradeDomainRequest,
    TransferInDomainRequestTransferRequest,
    RegistrarApiTransferInDomainRequest,
    UpdateContactRequestQuestion,
    RegistrarApiUpdateContactRequest,
    RegistrarApiUpdateDomainHostRequest,
    RegistrarApiUpdateDomainRequest,
    UpdateDNSZoneNameserversRequest,
    UpdateDNSZoneRecordsRequest,
    UpdateDNSZoneRequest,
)
from ...std.types import (
LanguageCode as StdLanguageCode,
)

def unmarshal_ContactExtensionFRAssociationInfo(data: Any) -> ContactExtensionFRAssociationInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionFRAssociationInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("publication_jo_page", str())
    args["publication_jo_page"] = field

    field = data.get("publication_jo", None)
    args["publication_jo"] = parser.isoparse(field) if isinstance(field, str) else field

    return ContactExtensionFRAssociationInfo(**args)

def unmarshal_ContactExtensionFRCodeAuthAfnicInfo(data: Any) -> ContactExtensionFRCodeAuthAfnicInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionFRCodeAuthAfnicInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("code_auth_afnic", str())
    args["code_auth_afnic"] = field

    return ContactExtensionFRCodeAuthAfnicInfo(**args)

def unmarshal_ContactExtensionFRDunsInfo(data: Any) -> ContactExtensionFRDunsInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionFRDunsInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("duns_id", str())
    args["duns_id"] = field

    field = data.get("local_id", str())
    args["local_id"] = field

    return ContactExtensionFRDunsInfo(**args)

def unmarshal_ContactExtensionFRIndividualInfo(data: Any) -> ContactExtensionFRIndividualInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionFRIndividualInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("whois_opt_in", str())
    args["whois_opt_in"] = field

    return ContactExtensionFRIndividualInfo(**args)

def unmarshal_ContactExtensionFRTrademarkInfo(data: Any) -> ContactExtensionFRTrademarkInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionFRTrademarkInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("trademark_inpi", str())
    args["trademark_inpi"] = field

    return ContactExtensionFRTrademarkInfo(**args)

def unmarshal_ContactExtensionEU(data: Any) -> ContactExtensionEU:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionEU' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("european_citizenship", str())
    args["european_citizenship"] = field

    return ContactExtensionEU(**args)

def unmarshal_ContactExtensionFR(data: Any) -> ContactExtensionFR:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionFR' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("mode", str())
    args["mode"] = field

    field = data.get("individual_info", None)
    args["individual_info"] = unmarshal_ContactExtensionFRIndividualInfo(field) if field is not None else None

    field = data.get("duns_info", None)
    args["duns_info"] = unmarshal_ContactExtensionFRDunsInfo(field) if field is not None else None

    field = data.get("association_info", None)
    args["association_info"] = unmarshal_ContactExtensionFRAssociationInfo(field) if field is not None else None

    field = data.get("trademark_info", None)
    args["trademark_info"] = unmarshal_ContactExtensionFRTrademarkInfo(field) if field is not None else None

    field = data.get("code_auth_afnic_info", None)
    args["code_auth_afnic_info"] = unmarshal_ContactExtensionFRCodeAuthAfnicInfo(field) if field is not None else None

    return ContactExtensionFR(**args)

def unmarshal_ContactExtensionNL(data: Any) -> ContactExtensionNL:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionNL' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("legal_form", str())
    args["legal_form"] = field

    field = data.get("legal_form_registration_number", str())
    args["legal_form_registration_number"] = field

    return ContactExtensionNL(**args)

def unmarshal_ContactQuestion(data: Any) -> ContactQuestion:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactQuestion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("question", str())
    args["question"] = field

    field = data.get("answer", str())
    args["answer"] = field

    return ContactQuestion(**args)

def unmarshal_Contact(data: Any) -> Contact:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Contact' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("legal_form", str())
    args["legal_form"] = field

    field = data.get("firstname", str())
    args["firstname"] = field

    field = data.get("lastname", str())
    args["lastname"] = field

    field = data.get("company_name", str())
    args["company_name"] = field

    field = data.get("email", str())
    args["email"] = field

    field = data.get("email_alt", str())
    args["email_alt"] = field

    field = data.get("phone_number", str())
    args["phone_number"] = field

    field = data.get("fax_number", str())
    args["fax_number"] = field

    field = data.get("address_line_1", str())
    args["address_line_1"] = field

    field = data.get("address_line_2", str())
    args["address_line_2"] = field

    field = data.get("zip", str())
    args["zip"] = field

    field = data.get("city", str())
    args["city"] = field

    field = data.get("country", str())
    args["country"] = field

    field = data.get("vat_identification_code", str())
    args["vat_identification_code"] = field

    field = data.get("company_identification_code", str())
    args["company_identification_code"] = field

    field = data.get("lang", str())
    args["lang"] = field

    field = data.get("resale", str())
    args["resale"] = field

    field = data.get("whois_opt_in", str())
    args["whois_opt_in"] = field

    field = data.get("questions", None)
    args["questions"] = [unmarshal_ContactQuestion(v) for v in field] if field is not None else None

    field = data.get("extension_fr", None)
    args["extension_fr"] = unmarshal_ContactExtensionFR(field) if field is not None else None

    field = data.get("extension_eu", None)
    args["extension_eu"] = unmarshal_ContactExtensionEU(field) if field is not None else None

    field = data.get("email_status", str())
    args["email_status"] = field

    field = data.get("state", str())
    args["state"] = field

    field = data.get("status", str())
    args["status"] = field

    field = data.get("extension_nl", None)
    args["extension_nl"] = unmarshal_ContactExtensionNL(field) if field is not None else None

    return Contact(**args)

def unmarshal_DNSZone(data: Any) -> DNSZone:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DNSZone' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain", str())
    args["domain"] = field

    field = data.get("subdomain", str())
    args["subdomain"] = field

    field = data.get("ns", str())
    args["ns"] = field

    field = data.get("ns_default", str())
    args["ns_default"] = field

    field = data.get("ns_master", str())
    args["ns_master"] = field

    field = data.get("status", str())
    args["status"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("linked_products", str())
    args["linked_products"] = [LinkedProduct(v) for v in field] if field is not None else None

    field = data.get("message", None)
    args["message"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return DNSZone(**args)

def unmarshal_Host(data: Any) -> Host:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Host' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain", str())
    args["domain"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("ips", str())
    args["ips"] = field

    field = data.get("status", str())
    args["status"] = field

    return Host(**args)

def unmarshal_SSLCertificate(data: Any) -> SSLCertificate:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SSLCertificate' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dns_zone", str())
    args["dns_zone"] = field

    field = data.get("alternative_dns_zones", str())
    args["alternative_dns_zones"] = field

    field = data.get("status", str())
    args["status"] = field

    field = data.get("private_key", str())
    args["private_key"] = field

    field = data.get("certificate_chain", str())
    args["certificate_chain"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("expired_at", None)
    args["expired_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return SSLCertificate(**args)

def unmarshal_CheckContactsCompatibilityResponseContactCheckResult(data: Any) -> CheckContactsCompatibilityResponseContactCheckResult:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckContactsCompatibilityResponseContactCheckResult' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("compatible", str())
    args["compatible"] = field

    field = data.get("error_message", None)
    args["error_message"] = field

    return CheckContactsCompatibilityResponseContactCheckResult(**args)

def unmarshal_CheckContactsCompatibilityResponse(data: Any) -> CheckContactsCompatibilityResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckContactsCompatibilityResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("compatible", str())
    args["compatible"] = field

    field = data.get("owner_check_result", None)
    args["owner_check_result"] = unmarshal_CheckContactsCompatibilityResponseContactCheckResult(field) if field is not None else None

    field = data.get("administrative_check_result", None)
    args["administrative_check_result"] = unmarshal_CheckContactsCompatibilityResponseContactCheckResult(field) if field is not None else None

    field = data.get("technical_check_result", None)
    args["technical_check_result"] = unmarshal_CheckContactsCompatibilityResponseContactCheckResult(field) if field is not None else None

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

def unmarshal_DSRecordPublicKey(data: Any) -> DSRecordPublicKey:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DSRecordPublicKey' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("key", str())
    args["key"] = field

    return DSRecordPublicKey(**args)

def unmarshal_DSRecordDigest(data: Any) -> DSRecordDigest:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DSRecordDigest' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("digest", str())
    args["digest"] = field

    field = data.get("public_key", None)
    args["public_key"] = unmarshal_DSRecordPublicKey(field) if field is not None else None

    return DSRecordDigest(**args)

def unmarshal_DSRecord(data: Any) -> DSRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DSRecord' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("key_id", str())
    args["key_id"] = field

    field = data.get("algorithm", str())
    args["algorithm"] = field

    field = data.get("digest", None)
    args["digest"] = unmarshal_DSRecordDigest(field) if field is not None else None

    field = data.get("public_key", None)
    args["public_key"] = unmarshal_DSRecordPublicKey(field) if field is not None else None

    return DSRecord(**args)

def unmarshal_TldOffer(data: Any) -> TldOffer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TldOffer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("action", str())
    args["action"] = field

    field = data.get("operation_path", str())
    args["operation_path"] = field

    field = data.get("price", None)
    args["price"] = unmarshal_Money(field) if field is not None else None

    return TldOffer(**args)

def unmarshal_DomainDNSSEC(data: Any) -> DomainDNSSEC:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainDNSSEC' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("status", str())
    args["status"] = field

    field = data.get("ds_records", str())
    args["ds_records"] = [unmarshal_DSRecord(v) for v in field] if field is not None else None

    return DomainDNSSEC(**args)

def unmarshal_DomainRegistrationStatusExternalDomain(data: Any) -> DomainRegistrationStatusExternalDomain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRegistrationStatusExternalDomain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("validation_token", str())
    args["validation_token"] = field

    return DomainRegistrationStatusExternalDomain(**args)

def unmarshal_DomainRegistrationStatusTransfer(data: Any) -> DomainRegistrationStatusTransfer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRegistrationStatusTransfer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("status", str())
    args["status"] = field

    field = data.get("vote_current_owner", str())
    args["vote_current_owner"] = field

    field = data.get("vote_new_owner", str())
    args["vote_new_owner"] = field

    return DomainRegistrationStatusTransfer(**args)

def unmarshal_Tld(data: Any) -> Tld:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Tld' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("dnssec_support", str())
    args["dnssec_support"] = field

    field = data.get("duration_in_years_min", str())
    args["duration_in_years_min"] = field

    field = data.get("duration_in_years_max", str())
    args["duration_in_years_max"] = field

    field = data.get("idn_support", str())
    args["idn_support"] = field

    field = data.get("offers", str())
    args["offers"] = {key: unmarshal_TldOffer(value)for key, value in field.items()
    } if field is not None else None

    field = data.get("specifications", str())
    args["specifications"] = field

    return Tld(**args)

def unmarshal_Domain(data: Any) -> Domain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Domain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain", str())
    args["domain"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("auto_renew_status", getattr(DomainFeatureStatus, "FEATURE_STATUS_UNKNOWN"))
    args["auto_renew_status"] = field

    field = data.get("epp_code", [])
    args["epp_code"] = field

    field = data.get("registrar", str())
    args["registrar"] = field

    field = data.get("is_external", False)
    args["is_external"] = field

    field = data.get("dnssec", None)
    args["dnssec"] = unmarshal_DomainDNSSEC(field) if field is not None else None

    field = data.get("expired_at", None)
    args["expired_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("status", getattr(DomainStatus, "STATUS_UNKNOWN"))
    args["status"] = field

    field = data.get("dns_zones", [])
    args["dns_zones"] = [unmarshal_DNSZone(v) for v in field] if field is not None else None

    field = data.get("linked_products", [])
    args["linked_products"] = [LinkedProduct(v) for v in field] if field is not None else None

    field = data.get("pending_trade", False)
    args["pending_trade"] = field

    field = data.get("owner_contact", None)
    args["owner_contact"] = unmarshal_Contact(field) if field is not None else None

    field = data.get("technical_contact", None)
    args["technical_contact"] = unmarshal_Contact(field) if field is not None else None

    field = data.get("administrative_contact", None)
    args["administrative_contact"] = unmarshal_Contact(field) if field is not None else None

    field = data.get("external_domain_registration_status", None)
    args["external_domain_registration_status"] = unmarshal_DomainRegistrationStatusExternalDomain(field) if field is not None else None

    field = data.get("transfer_registration_status", None)
    args["transfer_registration_status"] = unmarshal_DomainRegistrationStatusTransfer(field) if field is not None else None

    field = data.get("tld", None)
    args["tld"] = unmarshal_Tld(field) if field is not None else None

    return Domain(**args)

def unmarshal_GetDNSZoneTsigKeyResponse(data: Any) -> GetDNSZoneTsigKeyResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetDNSZoneTsigKeyResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("key", str())
    args["key"] = field

    field = data.get("algorithm", str())
    args["algorithm"] = field

    return GetDNSZoneTsigKeyResponse(**args)

def unmarshal_RecordGeoIPConfigMatch(data: Any) -> RecordGeoIPConfigMatch:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordGeoIPConfigMatch' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("countries", str())
    args["countries"] = field

    field = data.get("continents", str())
    args["continents"] = field

    field = data.get("data", str())
    args["data"] = field

    return RecordGeoIPConfigMatch(**args)

def unmarshal_RecordViewConfigView(data: Any) -> RecordViewConfigView:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordViewConfigView' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("subnet", str())
    args["subnet"] = field

    field = data.get("data", str())
    args["data"] = field

    return RecordViewConfigView(**args)

def unmarshal_RecordWeightedConfigWeightedIP(data: Any) -> RecordWeightedConfigWeightedIP:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordWeightedConfigWeightedIP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip", str())
    args["ip"] = field

    field = data.get("weight", str())
    args["weight"] = field

    return RecordWeightedConfigWeightedIP(**args)

def unmarshal_RecordGeoIPConfig(data: Any) -> RecordGeoIPConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordGeoIPConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("matches", str())
    args["matches"] = [unmarshal_RecordGeoIPConfigMatch(v) for v in field] if field is not None else None

    field = data.get("default", str())
    args["default"] = field

    return RecordGeoIPConfig(**args)

def unmarshal_RecordHTTPServiceConfig(data: Any) -> RecordHTTPServiceConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordHTTPServiceConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ips", str())
    args["ips"] = field

    field = data.get("url", str())
    args["url"] = field

    field = data.get("strategy", str())
    args["strategy"] = field

    field = data.get("must_contain", None)
    args["must_contain"] = field

    field = data.get("user_agent", None)
    args["user_agent"] = field

    return RecordHTTPServiceConfig(**args)

def unmarshal_RecordViewConfig(data: Any) -> RecordViewConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordViewConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("views", str())
    args["views"] = [unmarshal_RecordViewConfigView(v) for v in field] if field is not None else None

    return RecordViewConfig(**args)

def unmarshal_RecordWeightedConfig(data: Any) -> RecordWeightedConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordWeightedConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("weighted_ips", str())
    args["weighted_ips"] = [unmarshal_RecordWeightedConfigWeightedIP(v) for v in field] if field is not None else None

    return RecordWeightedConfig(**args)

def unmarshal_Record(data: Any) -> Record:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Record' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("data", str())
    args["data"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("priority", str())
    args["priority"] = field

    field = data.get("ttl", str())
    args["ttl"] = field

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("id", str())
    args["id"] = field

    field = data.get("comment", None)
    args["comment"] = field

    field = data.get("geo_ip_config", None)
    args["geo_ip_config"] = unmarshal_RecordGeoIPConfig(field) if field is not None else None

    field = data.get("http_service_config", None)
    args["http_service_config"] = unmarshal_RecordHTTPServiceConfig(field) if field is not None else None

    field = data.get("weighted_config", None)
    args["weighted_config"] = unmarshal_RecordWeightedConfig(field) if field is not None else None

    field = data.get("view_config", None)
    args["view_config"] = unmarshal_RecordViewConfig(field) if field is not None else None

    return Record(**args)

def unmarshal_RecordIdentifier(data: Any) -> RecordIdentifier:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordIdentifier' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("data", None)
    args["data"] = field

    field = data.get("ttl", None)
    args["ttl"] = field

    return RecordIdentifier(**args)

def unmarshal_RecordChangeAdd(data: Any) -> RecordChangeAdd:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordChangeAdd' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records", str())
    args["records"] = [unmarshal_Record(v) for v in field] if field is not None else None

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

    field = data.get("records", str())
    args["records"] = [unmarshal_Record(v) for v in field] if field is not None else None

    field = data.get("id", None)
    args["id"] = field

    field = data.get("id_fields", None)
    args["id_fields"] = unmarshal_RecordIdentifier(field) if field is not None else None

    return RecordChangeSet(**args)

def unmarshal_RecordChange(data: Any) -> RecordChange:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordChange' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("add", None)
    args["add"] = unmarshal_RecordChangeAdd(field) if field is not None else None

    field = data.get("set", None)
    args["set_"] = unmarshal_RecordChangeSet(field) if field is not None else None

    field = data.get("delete", None)
    args["delete"] = unmarshal_RecordChangeDelete(field) if field is not None else None

    field = data.get("clear", None)
    args["clear"] = unmarshal_RecordChangeClear(field) if field is not None else None

    return RecordChange(**args)

def unmarshal_GetDNSZoneVersionDiffResponse(data: Any) -> GetDNSZoneVersionDiffResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetDNSZoneVersionDiffResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("changes", str())
    args["changes"] = [unmarshal_RecordChange(v) for v in field] if field is not None else None

    return GetDNSZoneVersionDiffResponse(**args)

def unmarshal_GetDomainAuthCodeResponse(data: Any) -> GetDomainAuthCodeResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetDomainAuthCodeResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("auth_code", str())
    args["auth_code"] = field

    return GetDomainAuthCodeResponse(**args)

def unmarshal_ImportProviderDNSZoneResponse(data: Any) -> ImportProviderDNSZoneResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ImportProviderDNSZoneResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records", str())
    args["records"] = [unmarshal_Record(v) for v in field] if field is not None else None

    return ImportProviderDNSZoneResponse(**args)

def unmarshal_ImportRawDNSZoneResponse(data: Any) -> ImportRawDNSZoneResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ImportRawDNSZoneResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records", str())
    args["records"] = [unmarshal_Record(v) for v in field] if field is not None else None

    return ImportRawDNSZoneResponse(**args)

def unmarshal_ContactRolesRoles(data: Any) -> ContactRolesRoles:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactRolesRoles' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("is_owner", str())
    args["is_owner"] = field

    field = data.get("is_administrative", str())
    args["is_administrative"] = field

    field = data.get("is_technical", str())
    args["is_technical"] = field

    return ContactRolesRoles(**args)

def unmarshal_ContactRoles(data: Any) -> ContactRoles:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactRoles' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("roles", str())
    args["roles"] = {key: unmarshal_ContactRolesRoles(value)for key, value in field.items()
    } if field is not None else None

    field = data.get("contact", None)
    args["contact"] = unmarshal_Contact(field) if field is not None else None

    return ContactRoles(**args)

def unmarshal_ListContactsResponse(data: Any) -> ListContactsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListContactsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", str())
    args["total_count"] = field

    field = data.get("contacts", str())
    args["contacts"] = [unmarshal_ContactRoles(v) for v in field] if field is not None else None

    return ListContactsResponse(**args)

def unmarshal_Nameserver(data: Any) -> Nameserver:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Nameserver' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("ip", str())
    args["ip"] = field

    return Nameserver(**args)

def unmarshal_ListDNSZoneNameserversResponse(data: Any) -> ListDNSZoneNameserversResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDNSZoneNameserversResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ns", [])
    args["ns"] = [unmarshal_Nameserver(v) for v in field] if field is not None else None

    return ListDNSZoneNameserversResponse(**args)

def unmarshal_ListDNSZoneRecordsResponse(data: Any) -> ListDNSZoneRecordsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDNSZoneRecordsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("records", [])
    args["records"] = [unmarshal_Record(v) for v in field] if field is not None else None

    return ListDNSZoneRecordsResponse(**args)

def unmarshal_ListDNSZoneVersionRecordsResponse(data: Any) -> ListDNSZoneVersionRecordsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDNSZoneVersionRecordsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("records", [])
    args["records"] = [unmarshal_Record(v) for v in field] if field is not None else None

    return ListDNSZoneVersionRecordsResponse(**args)

def unmarshal_DNSZoneVersion(data: Any) -> DNSZoneVersion:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DNSZoneVersion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return DNSZoneVersion(**args)

def unmarshal_ListDNSZoneVersionsResponse(data: Any) -> ListDNSZoneVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDNSZoneVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("versions", [])
    args["versions"] = [unmarshal_DNSZoneVersion(v) for v in field] if field is not None else None

    return ListDNSZoneVersionsResponse(**args)

def unmarshal_ListDNSZonesResponse(data: Any) -> ListDNSZonesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDNSZonesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("dns_zones", [])
    args["dns_zones"] = [unmarshal_DNSZone(v) for v in field] if field is not None else None

    return ListDNSZonesResponse(**args)

def unmarshal_ListDomainHostsResponse(data: Any) -> ListDomainHostsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDomainHostsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", str())
    args["total_count"] = field

    field = data.get("hosts", str())
    args["hosts"] = [unmarshal_Host(v) for v in field] if field is not None else None

    return ListDomainHostsResponse(**args)

def unmarshal_DomainSummary(data: Any) -> DomainSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain", str())
    args["domain"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("auto_renew_status", str())
    args["auto_renew_status"] = field

    field = data.get("dnssec_status", str())
    args["dnssec_status"] = field

    field = data.get("epp_code", str())
    args["epp_code"] = field

    field = data.get("registrar", str())
    args["registrar"] = field

    field = data.get("is_external", str())
    args["is_external"] = field

    field = data.get("expired_at", None)
    args["expired_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("status", str())
    args["status"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("pending_trade", str())
    args["pending_trade"] = field

    field = data.get("external_domain_registration_status", None)
    args["external_domain_registration_status"] = unmarshal_DomainRegistrationStatusExternalDomain(field) if field is not None else None

    field = data.get("transfer_registration_status", None)
    args["transfer_registration_status"] = unmarshal_DomainRegistrationStatusTransfer(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return DomainSummary(**args)

def unmarshal_ListDomainsResponse(data: Any) -> ListDomainsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDomainsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", str())
    args["total_count"] = field

    field = data.get("domains", str())
    args["domains"] = [unmarshal_DomainSummary(v) for v in field] if field is not None else None

    return ListDomainsResponse(**args)

def unmarshal_RenewableDomain(data: Any) -> RenewableDomain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RenewableDomain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain", str())
    args["domain"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("status", str())
    args["status"] = field

    field = data.get("renewable_duration_in_years", None)
    args["renewable_duration_in_years"] = field

    field = data.get("expired_at", None)
    args["expired_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("limit_renew_at", None)
    args["limit_renew_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("limit_redemption_at", None)
    args["limit_redemption_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("estimated_delete_at", None)
    args["estimated_delete_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("tld", None)
    args["tld"] = unmarshal_Tld(field) if field is not None else None

    return RenewableDomain(**args)

def unmarshal_ListRenewableDomainsResponse(data: Any) -> ListRenewableDomainsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRenewableDomainsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", str())
    args["total_count"] = field

    field = data.get("domains", str())
    args["domains"] = [unmarshal_RenewableDomain(v) for v in field] if field is not None else None

    return ListRenewableDomainsResponse(**args)

def unmarshal_ListSSLCertificatesResponse(data: Any) -> ListSSLCertificatesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSSLCertificatesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", str())
    args["total_count"] = field

    field = data.get("certificates", str())
    args["certificates"] = [unmarshal_SSLCertificate(v) for v in field] if field is not None else None

    return ListSSLCertificatesResponse(**args)

def unmarshal_Task(data: Any) -> Task:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Task' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("type", getattr(TaskType, "UNKNOWN"))
    args["type_"] = field

    field = data.get("status", getattr(TaskStatus, "UNAVAILABLE"))
    args["status"] = field

    field = data.get("domain", None)
    args["domain"] = field

    field = data.get("started_at", None)
    args["started_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("message", None)
    args["message"] = field

    field = data.get("contact_identifier", None)
    args["contact_identifier"] = field

    return Task(**args)

def unmarshal_ListTasksResponse(data: Any) -> ListTasksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTasksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", str())
    args["total_count"] = field

    field = data.get("tasks", str())
    args["tasks"] = [unmarshal_Task(v) for v in field] if field is not None else None

    return ListTasksResponse(**args)

def unmarshal_ListTldsResponse(data: Any) -> ListTldsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTldsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("tlds", [])
    args["tlds"] = [unmarshal_Tld(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListTldsResponse(**args)

def unmarshal_OrderResponse(data: Any) -> OrderResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OrderResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domains", str())
    args["domains"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("task_id", str())
    args["task_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return OrderResponse(**args)

def unmarshal_RefreshDNSZoneResponse(data: Any) -> RefreshDNSZoneResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RefreshDNSZoneResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dns_zones", [])
    args["dns_zones"] = [unmarshal_DNSZone(v) for v in field] if field is not None else None

    return RefreshDNSZoneResponse(**args)

def unmarshal_RegisterExternalDomainResponse(data: Any) -> RegisterExternalDomainResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RegisterExternalDomainResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain", str())
    args["domain"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("validation_token", str())
    args["validation_token"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return RegisterExternalDomainResponse(**args)

def unmarshal_RestoreDNSZoneVersionResponse(data: Any) -> RestoreDNSZoneVersionResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RestoreDNSZoneVersionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return RestoreDNSZoneVersionResponse(**args)

def unmarshal_AvailableDomain(data: Any) -> AvailableDomain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AvailableDomain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain", str())
    args["domain"] = field

    field = data.get("available", str())
    args["available"] = field

    field = data.get("tld", None)
    args["tld"] = unmarshal_Tld(field) if field is not None else None

    return AvailableDomain(**args)

def unmarshal_SearchAvailableDomainsResponse(data: Any) -> SearchAvailableDomainsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SearchAvailableDomainsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("available_domains", [])
    args["available_domains"] = [unmarshal_AvailableDomain(v) for v in field] if field is not None else None

    return SearchAvailableDomainsResponse(**args)

def unmarshal_UpdateDNSZoneNameserversResponse(data: Any) -> UpdateDNSZoneNameserversResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateDNSZoneNameserversResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ns", [])
    args["ns"] = [unmarshal_Nameserver(v) for v in field] if field is not None else None

    return UpdateDNSZoneNameserversResponse(**args)

def unmarshal_UpdateDNSZoneRecordsResponse(data: Any) -> UpdateDNSZoneRecordsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateDNSZoneRecordsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records", [])
    args["records"] = [unmarshal_Record(v) for v in field] if field is not None else None

    return UpdateDNSZoneRecordsResponse(**args)

def marshal_CloneDNSZoneRequest(
    request: CloneDNSZoneRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.dest_dns_zone is not None:
        output["dest_dns_zone"] = request.dest_dns_zone
    else:
        output["dest_dns_zone"] = str()

    if request.overwrite is not None:
        output["overwrite"] = request.overwrite
    else:
        output["overwrite"] = False

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = None


    return output

def marshal_CreateDNSZoneRequest(
    request: CreateDNSZoneRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domain is not None:
        output["domain"] = request.domain
    else:
        output["domain"] = str()

    if request.subdomain is not None:
        output["subdomain"] = request.subdomain
    else:
        output["subdomain"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_CreateSSLCertificateRequest(
    request: CreateSSLCertificateRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.dns_zone is not None:
        output["dns_zone"] = request.dns_zone
    else:
        output["dns_zone"] = str()

    if request.alternative_dns_zones is not None:
        output["alternative_dns_zones"] = request.alternative_dns_zones
    else:
        output["alternative_dns_zones"] = None


    return output

def marshal_ImportProviderDNSZoneRequestOnlineV1(
    request: ImportProviderDNSZoneRequestOnlineV1,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.token is not None:
        output["token"] = request.token
    else:
        output["token"] = str()


    return output

def marshal_ImportProviderDNSZoneRequest(
    request: ImportProviderDNSZoneRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="online_v1", value=request.online_v1,marshal_func=marshal_ImportProviderDNSZoneRequestOnlineV1
            ),
        ]),
    )


    return output

def marshal_ImportRawDNSZoneRequestTsigKey(
    request: ImportRawDNSZoneRequestTsigKey,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.key is not None:
        output["key"] = request.key
    else:
        output["key"] = str()

    if request.algorithm is not None:
        output["algorithm"] = request.algorithm
    else:
        output["algorithm"] = str()


    return output

def marshal_ImportRawDNSZoneRequestAXFRSource(
    request: ImportRawDNSZoneRequestAXFRSource,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name_server is not None:
        output["name_server"] = request.name_server
    else:
        output["name_server"] = str()

    if request.tsig_key is not None:
        output["tsig_key"] = marshal_ImportRawDNSZoneRequestTsigKey(request.tsig_key, defaults)
    else:
        output["tsig_key"] = None


    return output

def marshal_ImportRawDNSZoneRequestBindSource(
    request: ImportRawDNSZoneRequestBindSource,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.content is not None:
        output["content"] = request.content
    else:
        output["content"] = str()


    return output

def marshal_ImportRawDNSZoneRequest(
    request: ImportRawDNSZoneRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="bind_source", value=request.bind_source,marshal_func=marshal_ImportRawDNSZoneRequestBindSource
            ),
            OneOfPossibility(param="axfr_source", value=request.axfr_source,marshal_func=marshal_ImportRawDNSZoneRequestAXFRSource
            ),
        ]),
    )

    if request.content is not None:
        output["content"] = request.content
    else:
        output["content"] = None

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.format is not None:
        output["format"] = str(request.format)
    else:
        output["format"] = None


    return output

def marshal_RefreshDNSZoneRequest(
    request: RefreshDNSZoneRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.recreate_dns_zone is not None:
        output["recreate_dns_zone"] = request.recreate_dns_zone
    else:
        output["recreate_dns_zone"] = False

    if request.recreate_sub_dns_zone is not None:
        output["recreate_sub_dns_zone"] = request.recreate_sub_dns_zone
    else:
        output["recreate_sub_dns_zone"] = False


    return output

def marshal_ContactExtensionFRAssociationInfo(
    request: ContactExtensionFRAssociationInfo,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.publication_jo_page is not None:
        output["publication_jo_page"] = request.publication_jo_page
    else:
        output["publication_jo_page"] = str()

    if request.publication_jo is not None:
        output["publication_jo"] = request.publication_jo.isoformat()
    else:
        output["publication_jo"] = None


    return output

def marshal_ContactExtensionFRCodeAuthAfnicInfo(
    request: ContactExtensionFRCodeAuthAfnicInfo,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.code_auth_afnic is not None:
        output["code_auth_afnic"] = request.code_auth_afnic
    else:
        output["code_auth_afnic"] = str()


    return output

def marshal_ContactExtensionFRDunsInfo(
    request: ContactExtensionFRDunsInfo,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.duns_id is not None:
        output["duns_id"] = request.duns_id
    else:
        output["duns_id"] = str()

    if request.local_id is not None:
        output["local_id"] = request.local_id
    else:
        output["local_id"] = str()


    return output

def marshal_ContactExtensionFRIndividualInfo(
    request: ContactExtensionFRIndividualInfo,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.whois_opt_in is not None:
        output["whois_opt_in"] = request.whois_opt_in
    else:
        output["whois_opt_in"] = str()


    return output

def marshal_ContactExtensionFRTrademarkInfo(
    request: ContactExtensionFRTrademarkInfo,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.trademark_inpi is not None:
        output["trademark_inpi"] = request.trademark_inpi
    else:
        output["trademark_inpi"] = str()


    return output

def marshal_ContactExtensionEU(
    request: ContactExtensionEU,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.european_citizenship is not None:
        output["european_citizenship"] = request.european_citizenship
    else:
        output["european_citizenship"] = str()


    return output

def marshal_ContactExtensionFR(
    request: ContactExtensionFR,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="individual_info", value=request.individual_info,marshal_func=marshal_ContactExtensionFRIndividualInfo
            ),
            OneOfPossibility(param="duns_info", value=request.duns_info,marshal_func=marshal_ContactExtensionFRDunsInfo
            ),
            OneOfPossibility(param="association_info", value=request.association_info,marshal_func=marshal_ContactExtensionFRAssociationInfo
            ),
            OneOfPossibility(param="trademark_info", value=request.trademark_info,marshal_func=marshal_ContactExtensionFRTrademarkInfo
            ),
            OneOfPossibility(param="code_auth_afnic_info", value=request.code_auth_afnic_info,marshal_func=marshal_ContactExtensionFRCodeAuthAfnicInfo
            ),
        ]),
    )

    if request.mode is not None:
        output["mode"] = str(request.mode)
    else:
        output["mode"] = str()


    return output

def marshal_ContactExtensionNL(
    request: ContactExtensionNL,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.legal_form is not None:
        output["legal_form"] = str(request.legal_form)
    else:
        output["legal_form"] = str()

    if request.legal_form_registration_number is not None:
        output["legal_form_registration_number"] = request.legal_form_registration_number
    else:
        output["legal_form_registration_number"] = str()


    return output

def marshal_ContactQuestion(
    request: ContactQuestion,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.question is not None:
        output["question"] = request.question
    else:
        output["question"] = str()

    if request.answer is not None:
        output["answer"] = request.answer
    else:
        output["answer"] = str()


    return output

def marshal_NewContact(
    request: NewContact,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.legal_form is not None:
        output["legal_form"] = str(request.legal_form)
    else:
        output["legal_form"] = str()

    if request.firstname is not None:
        output["firstname"] = request.firstname
    else:
        output["firstname"] = str()

    if request.lastname is not None:
        output["lastname"] = request.lastname
    else:
        output["lastname"] = str()

    if request.email is not None:
        output["email"] = request.email
    else:
        output["email"] = str()

    if request.company_name is not None:
        output["company_name"] = request.company_name
    else:
        output["company_name"] = None

    if request.email_alt is not None:
        output["email_alt"] = request.email_alt
    else:
        output["email_alt"] = None

    if request.phone_number is not None:
        output["phone_number"] = request.phone_number
    else:
        output["phone_number"] = str()

    if request.address_line_1 is not None:
        output["address_line_1"] = request.address_line_1
    else:
        output["address_line_1"] = str()

    if request.zip is not None:
        output["zip"] = request.zip
    else:
        output["zip"] = str()

    if request.city is not None:
        output["city"] = request.city
    else:
        output["city"] = str()

    if request.country is not None:
        output["country"] = request.country
    else:
        output["country"] = str()

    if request.fax_number is not None:
        output["fax_number"] = request.fax_number
    else:
        output["fax_number"] = None

    if request.address_line_2 is not None:
        output["address_line_2"] = request.address_line_2
    else:
        output["address_line_2"] = None

    if request.vat_identification_code is not None:
        output["vat_identification_code"] = request.vat_identification_code
    else:
        output["vat_identification_code"] = None

    if request.company_identification_code is not None:
        output["company_identification_code"] = request.company_identification_code
    else:
        output["company_identification_code"] = None

    if request.lang is not None:
        output["lang"] = str(request.lang)
    else:
        output["lang"] = str()

    if request.resale is not None:
        output["resale"] = request.resale
    else:
        output["resale"] = str()

    if request.whois_opt_in is not None:
        output["whois_opt_in"] = request.whois_opt_in
    else:
        output["whois_opt_in"] = str()

    if request.questions is not None:
        output["questions"] = [marshal_ContactQuestion(item, defaults) for item in request.questions]
    else:
        output["questions"] = None

    if request.extension_fr is not None:
        output["extension_fr"] = marshal_ContactExtensionFR(request.extension_fr, defaults)
    else:
        output["extension_fr"] = None

    if request.extension_eu is not None:
        output["extension_eu"] = marshal_ContactExtensionEU(request.extension_eu, defaults)
    else:
        output["extension_eu"] = None

    if request.state is not None:
        output["state"] = request.state
    else:
        output["state"] = None

    if request.extension_nl is not None:
        output["extension_nl"] = marshal_ContactExtensionNL(request.extension_nl, defaults)
    else:
        output["extension_nl"] = None


    return output

def marshal_RegistrarApiBuyDomainsRequest(
    request: RegistrarApiBuyDomainsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="owner_contact_id", value=request.owner_contact_id,marshal_func=None
            ),
            OneOfPossibility(param="owner_contact", value=request.owner_contact,marshal_func=marshal_NewContact
            ),
        ]),
    )
    output.update(
        resolve_one_of([
            OneOfPossibility(param="administrative_contact_id", value=request.administrative_contact_id,marshal_func=None
            ),
            OneOfPossibility(param="administrative_contact", value=request.administrative_contact,marshal_func=marshal_NewContact
            ),
        ]),
    )
    output.update(
        resolve_one_of([
            OneOfPossibility(param="technical_contact_id", value=request.technical_contact_id,marshal_func=None
            ),
            OneOfPossibility(param="technical_contact", value=request.technical_contact,marshal_func=marshal_NewContact
            ),
        ]),
    )

    if request.domains is not None:
        output["domains"] = request.domains
    else:
        output["domains"] = str()

    if request.duration_in_years is not None:
        output["duration_in_years"] = request.duration_in_years
    else:
        output["duration_in_years"] = 0

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_RegistrarApiCheckContactsCompatibilityRequest(
    request: RegistrarApiCheckContactsCompatibilityRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="owner_contact_id", value=request.owner_contact_id,marshal_func=None
            ),
            OneOfPossibility(param="owner_contact", value=request.owner_contact,marshal_func=marshal_NewContact
            ),
        ]),
    )
    output.update(
        resolve_one_of([
            OneOfPossibility(param="administrative_contact_id", value=request.administrative_contact_id,marshal_func=None
            ),
            OneOfPossibility(param="administrative_contact", value=request.administrative_contact,marshal_func=marshal_NewContact
            ),
        ]),
    )
    output.update(
        resolve_one_of([
            OneOfPossibility(param="technical_contact_id", value=request.technical_contact_id,marshal_func=None
            ),
            OneOfPossibility(param="technical_contact", value=request.technical_contact,marshal_func=marshal_NewContact
            ),
        ]),
    )

    if request.domains is not None:
        output["domains"] = request.domains
    else:
        output["domains"] = None

    if request.tlds is not None:
        output["tlds"] = request.tlds
    else:
        output["tlds"] = None


    return output

def marshal_RegistrarApiCreateDomainHostRequest(
    request: RegistrarApiCreateDomainHostRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.ips is not None:
        output["ips"] = request.ips
    else:
        output["ips"] = None


    return output

def marshal_DSRecordPublicKey(
    request: DSRecordPublicKey,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.key is not None:
        output["key"] = request.key
    else:
        output["key"] = str()


    return output

def marshal_DSRecordDigest(
    request: DSRecordDigest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = str()

    if request.digest is not None:
        output["digest"] = request.digest
    else:
        output["digest"] = str()

    if request.public_key is not None:
        output["public_key"] = marshal_DSRecordPublicKey(request.public_key, defaults)
    else:
        output["public_key"] = None


    return output

def marshal_DSRecord(
    request: DSRecord,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="digest", value=request.digest,marshal_func=marshal_DSRecordDigest
            ),
            OneOfPossibility(param="public_key", value=request.public_key,marshal_func=marshal_DSRecordPublicKey
            ),
        ]),
    )

    if request.key_id is not None:
        output["key_id"] = request.key_id
    else:
        output["key_id"] = str()

    if request.algorithm is not None:
        output["algorithm"] = str(request.algorithm)
    else:
        output["algorithm"] = str()


    return output

def marshal_RegistrarApiEnableDomainDNSSECRequest(
    request: RegistrarApiEnableDomainDNSSECRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ds_record is not None:
        output["ds_record"] = marshal_DSRecord(request.ds_record, defaults)
    else:
        output["ds_record"] = None


    return output

def marshal_RegistrarApiRegisterExternalDomainRequest(
    request: RegistrarApiRegisterExternalDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domain is not None:
        output["domain"] = request.domain
    else:
        output["domain"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_RegistrarApiRenewDomainsRequest(
    request: RegistrarApiRenewDomainsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domains is not None:
        output["domains"] = request.domains
    else:
        output["domains"] = str()

    if request.duration_in_years is not None:
        output["duration_in_years"] = request.duration_in_years
    else:
        output["duration_in_years"] = 0

    if request.force_late_renewal is not None:
        output["force_late_renewal"] = request.force_late_renewal
    else:
        output["force_late_renewal"] = None


    return output

def marshal_RegistrarApiTradeDomainRequest(
    request: RegistrarApiTradeDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="new_owner_contact_id", value=request.new_owner_contact_id,marshal_func=None
            ),
            OneOfPossibility(param="new_owner_contact", value=request.new_owner_contact,marshal_func=marshal_NewContact
            ),
        ]),
    )

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = None


    return output

def marshal_TransferInDomainRequestTransferRequest(
    request: TransferInDomainRequestTransferRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domain is not None:
        output["domain"] = request.domain
    else:
        output["domain"] = str()

    if request.auth_code is not None:
        output["auth_code"] = request.auth_code
    else:
        output["auth_code"] = str()


    return output

def marshal_RegistrarApiTransferInDomainRequest(
    request: RegistrarApiTransferInDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="owner_contact_id", value=request.owner_contact_id,marshal_func=None
            ),
            OneOfPossibility(param="owner_contact", value=request.owner_contact,marshal_func=marshal_NewContact
            ),
        ]),
    )
    output.update(
        resolve_one_of([
            OneOfPossibility(param="administrative_contact_id", value=request.administrative_contact_id,marshal_func=None
            ),
            OneOfPossibility(param="administrative_contact", value=request.administrative_contact,marshal_func=marshal_NewContact
            ),
        ]),
    )
    output.update(
        resolve_one_of([
            OneOfPossibility(param="technical_contact_id", value=request.technical_contact_id,marshal_func=None
            ),
            OneOfPossibility(param="technical_contact", value=request.technical_contact,marshal_func=marshal_NewContact
            ),
        ]),
    )

    if request.domains is not None:
        output["domains"] = [marshal_TransferInDomainRequestTransferRequest(item, defaults) for item in request.domains]
    else:
        output["domains"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_UpdateContactRequestQuestion(
    request: UpdateContactRequestQuestion,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.question is not None:
        output["question"] = request.question
    else:
        output["question"] = None

    if request.answer is not None:
        output["answer"] = request.answer
    else:
        output["answer"] = None


    return output

def marshal_RegistrarApiUpdateContactRequest(
    request: RegistrarApiUpdateContactRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.email is not None:
        output["email"] = request.email
    else:
        output["email"] = None

    if request.email_alt is not None:
        output["email_alt"] = request.email_alt
    else:
        output["email_alt"] = None

    if request.phone_number is not None:
        output["phone_number"] = request.phone_number
    else:
        output["phone_number"] = None

    if request.fax_number is not None:
        output["fax_number"] = request.fax_number
    else:
        output["fax_number"] = None

    if request.address_line_1 is not None:
        output["address_line_1"] = request.address_line_1
    else:
        output["address_line_1"] = None

    if request.address_line_2 is not None:
        output["address_line_2"] = request.address_line_2
    else:
        output["address_line_2"] = None

    if request.zip is not None:
        output["zip"] = request.zip
    else:
        output["zip"] = None

    if request.city is not None:
        output["city"] = request.city
    else:
        output["city"] = None

    if request.country is not None:
        output["country"] = request.country
    else:
        output["country"] = None

    if request.vat_identification_code is not None:
        output["vat_identification_code"] = request.vat_identification_code
    else:
        output["vat_identification_code"] = None

    if request.company_identification_code is not None:
        output["company_identification_code"] = request.company_identification_code
    else:
        output["company_identification_code"] = None

    if request.lang is not None:
        output["lang"] = str(request.lang)
    else:
        output["lang"] = None

    if request.resale is not None:
        output["resale"] = request.resale
    else:
        output["resale"] = None

    if request.questions is not None:
        output["questions"] = [marshal_UpdateContactRequestQuestion(item, defaults) for item in request.questions]
    else:
        output["questions"] = None

    if request.extension_fr is not None:
        output["extension_fr"] = marshal_ContactExtensionFR(request.extension_fr, defaults)
    else:
        output["extension_fr"] = None

    if request.extension_eu is not None:
        output["extension_eu"] = marshal_ContactExtensionEU(request.extension_eu, defaults)
    else:
        output["extension_eu"] = None

    if request.whois_opt_in is not None:
        output["whois_opt_in"] = request.whois_opt_in
    else:
        output["whois_opt_in"] = None

    if request.state is not None:
        output["state"] = request.state
    else:
        output["state"] = None

    if request.extension_nl is not None:
        output["extension_nl"] = marshal_ContactExtensionNL(request.extension_nl, defaults)
    else:
        output["extension_nl"] = None


    return output

def marshal_RegistrarApiUpdateDomainHostRequest(
    request: RegistrarApiUpdateDomainHostRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ips is not None:
        output["ips"] = request.ips
    else:
        output["ips"] = None


    return output

def marshal_RegistrarApiUpdateDomainRequest(
    request: RegistrarApiUpdateDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="technical_contact_id", value=request.technical_contact_id,marshal_func=None
            ),
            OneOfPossibility(param="technical_contact", value=request.technical_contact,marshal_func=marshal_NewContact
            ),
        ]),
    )
    output.update(
        resolve_one_of([
            OneOfPossibility(param="owner_contact_id", value=request.owner_contact_id,marshal_func=None
            ),
            OneOfPossibility(param="owner_contact", value=request.owner_contact,marshal_func=marshal_NewContact
            ),
        ]),
    )
    output.update(
        resolve_one_of([
            OneOfPossibility(param="administrative_contact_id", value=request.administrative_contact_id,marshal_func=None
            ),
            OneOfPossibility(param="administrative_contact", value=request.administrative_contact,marshal_func=marshal_NewContact
            ),
        ]),
    )


    return output

def marshal_Nameserver(
    request: Nameserver,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.ip is not None:
        output["ip"] = request.ip
    else:
        output["ip"] = str()


    return output

def marshal_UpdateDNSZoneNameserversRequest(
    request: UpdateDNSZoneNameserversRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ns is not None:
        output["ns"] = [marshal_Nameserver(item, defaults) for item in request.ns]
    else:
        output["ns"] = str()


    return output

def marshal_RecordGeoIPConfigMatch(
    request: RecordGeoIPConfigMatch,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.countries is not None:
        output["countries"] = request.countries
    else:
        output["countries"] = str()

    if request.continents is not None:
        output["continents"] = request.continents
    else:
        output["continents"] = str()

    if request.data is not None:
        output["data"] = request.data
    else:
        output["data"] = str()


    return output

def marshal_RecordViewConfigView(
    request: RecordViewConfigView,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.subnet is not None:
        output["subnet"] = request.subnet
    else:
        output["subnet"] = str()

    if request.data is not None:
        output["data"] = request.data
    else:
        output["data"] = str()


    return output

def marshal_RecordWeightedConfigWeightedIP(
    request: RecordWeightedConfigWeightedIP,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip is not None:
        output["ip"] = request.ip
    else:
        output["ip"] = str()

    if request.weight is not None:
        output["weight"] = request.weight
    else:
        output["weight"] = str()


    return output

def marshal_RecordGeoIPConfig(
    request: RecordGeoIPConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.matches is not None:
        output["matches"] = [marshal_RecordGeoIPConfigMatch(item, defaults) for item in request.matches]
    else:
        output["matches"] = str()

    if request.default is not None:
        output["default"] = request.default
    else:
        output["default"] = str()


    return output

def marshal_RecordHTTPServiceConfig(
    request: RecordHTTPServiceConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ips is not None:
        output["ips"] = request.ips
    else:
        output["ips"] = str()

    if request.url is not None:
        output["url"] = request.url
    else:
        output["url"] = str()

    if request.strategy is not None:
        output["strategy"] = str(request.strategy)
    else:
        output["strategy"] = str()

    if request.must_contain is not None:
        output["must_contain"] = request.must_contain
    else:
        output["must_contain"] = None

    if request.user_agent is not None:
        output["user_agent"] = request.user_agent
    else:
        output["user_agent"] = None


    return output

def marshal_RecordViewConfig(
    request: RecordViewConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.views is not None:
        output["views"] = [marshal_RecordViewConfigView(item, defaults) for item in request.views]
    else:
        output["views"] = str()


    return output

def marshal_RecordWeightedConfig(
    request: RecordWeightedConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.weighted_ips is not None:
        output["weighted_ips"] = [marshal_RecordWeightedConfigWeightedIP(item, defaults) for item in request.weighted_ips]
    else:
        output["weighted_ips"] = str()


    return output

def marshal_Record(
    request: Record,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="geo_ip_config", value=request.geo_ip_config,marshal_func=marshal_RecordGeoIPConfig
            ),
            OneOfPossibility(param="http_service_config", value=request.http_service_config,marshal_func=marshal_RecordHTTPServiceConfig
            ),
            OneOfPossibility(param="weighted_config", value=request.weighted_config,marshal_func=marshal_RecordWeightedConfig
            ),
            OneOfPossibility(param="view_config", value=request.view_config,marshal_func=marshal_RecordViewConfig
            ),
        ]),
    )

    if request.data is not None:
        output["data"] = request.data
    else:
        output["data"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.priority is not None:
        output["priority"] = request.priority
    else:
        output["priority"] = str()

    if request.ttl is not None:
        output["ttl"] = request.ttl
    else:
        output["ttl"] = str()

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = str()

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.comment is not None:
        output["comment"] = request.comment
    else:
        output["comment"] = None


    return output

def marshal_RecordIdentifier(
    request: RecordIdentifier,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = str()

    if request.data is not None:
        output["data"] = request.data
    else:
        output["data"] = None

    if request.ttl is not None:
        output["ttl"] = request.ttl
    else:
        output["ttl"] = None


    return output

def marshal_RecordChangeAdd(
    request: RecordChangeAdd,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.records is not None:
        output["records"] = [marshal_Record(item, defaults) for item in request.records]
    else:
        output["records"] = str()


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
        resolve_one_of([
            OneOfPossibility(param="id", value=request.id,marshal_func=None
            ),
            OneOfPossibility(param="id_fields", value=request.id_fields,marshal_func=marshal_RecordIdentifier
            ),
        ]),
    )


    return output

def marshal_RecordChangeSet(
    request: RecordChangeSet,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="id", value=request.id,marshal_func=None
            ),
            OneOfPossibility(param="id_fields", value=request.id_fields,marshal_func=marshal_RecordIdentifier
            ),
        ]),
    )

    if request.records is not None:
        output["records"] = [marshal_Record(item, defaults) for item in request.records]
    else:
        output["records"] = str()


    return output

def marshal_RecordChange(
    request: RecordChange,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="add", value=request.add,marshal_func=marshal_RecordChangeAdd
            ),
            OneOfPossibility(param="set", value=request.set_,marshal_func=marshal_RecordChangeSet
            ),
            OneOfPossibility(param="delete", value=request.delete,marshal_func=marshal_RecordChangeDelete
            ),
            OneOfPossibility(param="clear", value=request.clear,marshal_func=marshal_RecordChangeClear
            ),
        ]),
    )


    return output

def marshal_UpdateDNSZoneRecordsRequest(
    request: UpdateDNSZoneRecordsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.changes is not None:
        output["changes"] = [marshal_RecordChange(item, defaults) for item in request.changes]
    else:
        output["changes"] = str()

    if request.disallow_new_zone_creation is not None:
        output["disallow_new_zone_creation"] = request.disallow_new_zone_creation
    else:
        output["disallow_new_zone_creation"] = False

    if request.return_all_records is not None:
        output["return_all_records"] = request.return_all_records
    else:
        output["return_all_records"] = None

    if request.serial is not None:
        output["serial"] = request.serial
    else:
        output["serial"] = None


    return output

def marshal_UpdateDNSZoneRequest(
    request: UpdateDNSZoneRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.new_dns_zone is not None:
        output["new_dns_zone"] = request.new_dns_zone
    else:
        output["new_dns_zone"] = None

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output
