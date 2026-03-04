# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    unmarshal_Money,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    ContactEmailStatus,
    ContactLegalForm,
    ContactStatus,
    DomainFeatureStatus,
    DomainStatus,
    InboundTransferStatus,
    LinkedProduct,
    TaskStatus,
    TaskType,
    ContactExtensionFRAssociationInfo,
    ContactExtensionFRCodeAuthAfnicInfo,
    ContactExtensionFRDunsInfo,
    ContactExtensionFRIndividualInfo,
    ContactExtensionFRTrademarkInfo,
    ContactExtensionEU,
    ContactExtensionFR,
    ContactExtensionIT,
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
    InboundTransfer,
    ListInboundTransfersResponse,
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
    RetryInboundTransferResponse,
    AvailableDomain,
    SearchAvailableDomainsConsoleResponse,
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
    RegistrarApiRetryInboundTransferRequest,
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


def unmarshal_ContactExtensionFRAssociationInfo(
    data: Any,
) -> ContactExtensionFRAssociationInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionFRAssociationInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("publication_jo_page", None)
    if field is not None:
        args["publication_jo_page"] = field
    else:
        args["publication_jo_page"] = None

    field = data.get("publication_jo", None)
    if field is not None:
        args["publication_jo"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["publication_jo"] = None

    return ContactExtensionFRAssociationInfo(**args)


def unmarshal_ContactExtensionFRCodeAuthAfnicInfo(
    data: Any,
) -> ContactExtensionFRCodeAuthAfnicInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionFRCodeAuthAfnicInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("code_auth_afnic", None)
    if field is not None:
        args["code_auth_afnic"] = field
    else:
        args["code_auth_afnic"] = None

    return ContactExtensionFRCodeAuthAfnicInfo(**args)


def unmarshal_ContactExtensionFRDunsInfo(data: Any) -> ContactExtensionFRDunsInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionFRDunsInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("duns_id", None)
    if field is not None:
        args["duns_id"] = field
    else:
        args["duns_id"] = None

    field = data.get("local_id", None)
    if field is not None:
        args["local_id"] = field
    else:
        args["local_id"] = None

    return ContactExtensionFRDunsInfo(**args)


def unmarshal_ContactExtensionFRIndividualInfo(
    data: Any,
) -> ContactExtensionFRIndividualInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionFRIndividualInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("whois_opt_in", None)
    if field is not None:
        args["whois_opt_in"] = field
    else:
        args["whois_opt_in"] = None

    return ContactExtensionFRIndividualInfo(**args)


def unmarshal_ContactExtensionFRTrademarkInfo(
    data: Any,
) -> ContactExtensionFRTrademarkInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionFRTrademarkInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("trademark_inpi", None)
    if field is not None:
        args["trademark_inpi"] = field
    else:
        args["trademark_inpi"] = None

    return ContactExtensionFRTrademarkInfo(**args)


def unmarshal_ContactExtensionEU(data: Any) -> ContactExtensionEU:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionEU' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("european_citizenship", None)
    if field is not None:
        args["european_citizenship"] = field
    else:
        args["european_citizenship"] = None

    return ContactExtensionEU(**args)


def unmarshal_ContactExtensionFR(data: Any) -> ContactExtensionFR:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionFR' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("mode", None)
    if field is not None:
        args["mode"] = field
    else:
        args["mode"] = None

    field = data.get("individual_info", None)
    if field is not None:
        args["individual_info"] = unmarshal_ContactExtensionFRIndividualInfo(field)
    else:
        args["individual_info"] = None

    field = data.get("duns_info", None)
    if field is not None:
        args["duns_info"] = unmarshal_ContactExtensionFRDunsInfo(field)
    else:
        args["duns_info"] = None

    field = data.get("association_info", None)
    if field is not None:
        args["association_info"] = unmarshal_ContactExtensionFRAssociationInfo(field)
    else:
        args["association_info"] = None

    field = data.get("trademark_info", None)
    if field is not None:
        args["trademark_info"] = unmarshal_ContactExtensionFRTrademarkInfo(field)
    else:
        args["trademark_info"] = None

    field = data.get("code_auth_afnic_info", None)
    if field is not None:
        args["code_auth_afnic_info"] = unmarshal_ContactExtensionFRCodeAuthAfnicInfo(
            field
        )
    else:
        args["code_auth_afnic_info"] = None

    return ContactExtensionFR(**args)


def unmarshal_ContactExtensionIT(data: Any) -> ContactExtensionIT:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionIT' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("european_citizenship", None)
    if field is not None:
        args["european_citizenship"] = field
    else:
        args["european_citizenship"] = None

    field = data.get("tax_code", None)
    if field is not None:
        args["tax_code"] = field
    else:
        args["tax_code"] = None

    field = data.get("pin", None)
    if field is not None:
        args["pin"] = field
    else:
        args["pin"] = None

    return ContactExtensionIT(**args)


def unmarshal_ContactExtensionNL(data: Any) -> ContactExtensionNL:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactExtensionNL' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("legal_form", None)
    if field is not None:
        args["legal_form"] = field
    else:
        args["legal_form"] = None

    field = data.get("legal_form_registration_number", None)
    if field is not None:
        args["legal_form_registration_number"] = field
    else:
        args["legal_form_registration_number"] = None

    return ContactExtensionNL(**args)


def unmarshal_ContactQuestion(data: Any) -> ContactQuestion:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactQuestion' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("question", None)
    if field is not None:
        args["question"] = field
    else:
        args["question"] = None

    field = data.get("answer", None)
    if field is not None:
        args["answer"] = field
    else:
        args["answer"] = None

    return ContactQuestion(**args)


def unmarshal_Contact(data: Any) -> Contact:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Contact' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("legal_form", None)
    if field is not None:
        args["legal_form"] = field
    else:
        args["legal_form"] = ContactLegalForm.LEGAL_FORM_UNKNOWN

    field = data.get("firstname", None)
    if field is not None:
        args["firstname"] = field
    else:
        args["firstname"] = None

    field = data.get("lastname", None)
    if field is not None:
        args["lastname"] = field
    else:
        args["lastname"] = None

    field = data.get("company_name", None)
    if field is not None:
        args["company_name"] = field
    else:
        args["company_name"] = None

    field = data.get("email", None)
    if field is not None:
        args["email"] = field
    else:
        args["email"] = None

    field = data.get("email_alt", None)
    if field is not None:
        args["email_alt"] = field
    else:
        args["email_alt"] = None

    field = data.get("phone_number", None)
    if field is not None:
        args["phone_number"] = field
    else:
        args["phone_number"] = None

    field = data.get("fax_number", None)
    if field is not None:
        args["fax_number"] = field
    else:
        args["fax_number"] = None

    field = data.get("address_line_1", None)
    if field is not None:
        args["address_line_1"] = field
    else:
        args["address_line_1"] = None

    field = data.get("address_line_2", None)
    if field is not None:
        args["address_line_2"] = field
    else:
        args["address_line_2"] = None

    field = data.get("zip", None)
    if field is not None:
        args["zip"] = field
    else:
        args["zip"] = None

    field = data.get("city", None)
    if field is not None:
        args["city"] = field
    else:
        args["city"] = None

    field = data.get("country", None)
    if field is not None:
        args["country"] = field
    else:
        args["country"] = None

    field = data.get("vat_identification_code", None)
    if field is not None:
        args["vat_identification_code"] = field
    else:
        args["vat_identification_code"] = None

    field = data.get("company_identification_code", None)
    if field is not None:
        args["company_identification_code"] = field
    else:
        args["company_identification_code"] = None

    field = data.get("lang", None)
    if field is not None:
        args["lang"] = field
    else:
        args["lang"] = StdLanguageCode.UNKNOWN_LANGUAGE_CODE

    field = data.get("resale", None)
    if field is not None:
        args["resale"] = field
    else:
        args["resale"] = False

    field = data.get("whois_opt_in", None)
    if field is not None:
        args["whois_opt_in"] = field
    else:
        args["whois_opt_in"] = False

    field = data.get("email_status", None)
    if field is not None:
        args["email_status"] = field
    else:
        args["email_status"] = ContactEmailStatus.EMAIL_STATUS_UNKNOWN

    field = data.get("extension_fr", None)
    if field is not None:
        args["extension_fr"] = unmarshal_ContactExtensionFR(field)
    else:
        args["extension_fr"] = None

    field = data.get("extension_eu", None)
    if field is not None:
        args["extension_eu"] = unmarshal_ContactExtensionEU(field)
    else:
        args["extension_eu"] = None

    field = data.get("state", None)
    if field is not None:
        args["state"] = field
    else:
        args["state"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = ContactStatus.STATUS_UNKNOWN

    field = data.get("questions", None)
    if field is not None:
        args["questions"] = (
            [unmarshal_ContactQuestion(v) for v in field] if field is not None else None
        )
    else:
        args["questions"] = []

    field = data.get("extension_nl", None)
    if field is not None:
        args["extension_nl"] = unmarshal_ContactExtensionNL(field)
    else:
        args["extension_nl"] = None

    field = data.get("extension_it", None)
    if field is not None:
        args["extension_it"] = unmarshal_ContactExtensionIT(field)
    else:
        args["extension_it"] = None

    return Contact(**args)


def unmarshal_DNSZone(data: Any) -> DNSZone:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DNSZone' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field
    else:
        args["domain"] = None

    field = data.get("subdomain", None)
    if field is not None:
        args["subdomain"] = field
    else:
        args["subdomain"] = None

    field = data.get("ns", None)
    if field is not None:
        args["ns"] = field
    else:
        args["ns"] = None

    field = data.get("ns_default", None)
    if field is not None:
        args["ns_default"] = field
    else:
        args["ns_default"] = None

    field = data.get("ns_master", None)
    if field is not None:
        args["ns_master"] = field
    else:
        args["ns_master"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("linked_products", None)
    if field is not None:
        args["linked_products"] = (
            [LinkedProduct(v) for v in field] if field is not None else None
        )
    else:
        args["linked_products"] = None

    field = data.get("message", None)
    if field is not None:
        args["message"] = field
    else:
        args["message"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return DNSZone(**args)


def unmarshal_Host(data: Any) -> Host:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Host' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field
    else:
        args["domain"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("ips", None)
    if field is not None:
        args["ips"] = field
    else:
        args["ips"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = None

    return Host(**args)


def unmarshal_SSLCertificate(data: Any) -> SSLCertificate:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SSLCertificate' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("dns_zone", None)
    if field is not None:
        args["dns_zone"] = field
    else:
        args["dns_zone"] = None

    field = data.get("alternative_dns_zones", None)
    if field is not None:
        args["alternative_dns_zones"] = field
    else:
        args["alternative_dns_zones"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = None

    field = data.get("private_key", None)
    if field is not None:
        args["private_key"] = field
    else:
        args["private_key"] = None

    field = data.get("certificate_chain", None)
    if field is not None:
        args["certificate_chain"] = field
    else:
        args["certificate_chain"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("expired_at", None)
    if field is not None:
        args["expired_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["expired_at"] = None

    return SSLCertificate(**args)


def unmarshal_CheckContactsCompatibilityResponseContactCheckResult(
    data: Any,
) -> CheckContactsCompatibilityResponseContactCheckResult:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckContactsCompatibilityResponseContactCheckResult' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("compatible", None)
    if field is not None:
        args["compatible"] = field
    else:
        args["compatible"] = None

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

    return CheckContactsCompatibilityResponseContactCheckResult(**args)


def unmarshal_CheckContactsCompatibilityResponse(
    data: Any,
) -> CheckContactsCompatibilityResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckContactsCompatibilityResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("compatible", None)
    if field is not None:
        args["compatible"] = field
    else:
        args["compatible"] = None

    field = data.get("owner_check_result", None)
    if field is not None:
        args["owner_check_result"] = (
            unmarshal_CheckContactsCompatibilityResponseContactCheckResult(field)
        )
    else:
        args["owner_check_result"] = None

    field = data.get("administrative_check_result", None)
    if field is not None:
        args["administrative_check_result"] = (
            unmarshal_CheckContactsCompatibilityResponseContactCheckResult(field)
        )
    else:
        args["administrative_check_result"] = None

    field = data.get("technical_check_result", None)
    if field is not None:
        args["technical_check_result"] = (
            unmarshal_CheckContactsCompatibilityResponseContactCheckResult(field)
        )
    else:
        args["technical_check_result"] = None

    return CheckContactsCompatibilityResponse(**args)


def unmarshal_ClearDNSZoneRecordsResponse(data: Any) -> ClearDNSZoneRecordsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClearDNSZoneRecordsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return ClearDNSZoneRecordsResponse(**args)


def unmarshal_DeleteDNSZoneResponse(data: Any) -> DeleteDNSZoneResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeleteDNSZoneResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return DeleteDNSZoneResponse(**args)


def unmarshal_DeleteExternalDomainResponse(data: Any) -> DeleteExternalDomainResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeleteExternalDomainResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return DeleteExternalDomainResponse(**args)


def unmarshal_DeleteSSLCertificateResponse(data: Any) -> DeleteSSLCertificateResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeleteSSLCertificateResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return DeleteSSLCertificateResponse(**args)


def unmarshal_DSRecordPublicKey(data: Any) -> DSRecordPublicKey:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DSRecordPublicKey' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("key", None)
    if field is not None:
        args["key"] = field
    else:
        args["key"] = None

    return DSRecordPublicKey(**args)


def unmarshal_DSRecordDigest(data: Any) -> DSRecordDigest:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DSRecordDigest' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    field = data.get("digest", None)
    if field is not None:
        args["digest"] = field
    else:
        args["digest"] = None

    field = data.get("public_key", None)
    if field is not None:
        args["public_key"] = unmarshal_DSRecordPublicKey(field)
    else:
        args["public_key"] = None

    return DSRecordDigest(**args)


def unmarshal_DSRecord(data: Any) -> DSRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DSRecord' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("key_id", None)
    if field is not None:
        args["key_id"] = field
    else:
        args["key_id"] = None

    field = data.get("algorithm", None)
    if field is not None:
        args["algorithm"] = field
    else:
        args["algorithm"] = None

    field = data.get("digest", None)
    if field is not None:
        args["digest"] = unmarshal_DSRecordDigest(field)
    else:
        args["digest"] = None

    field = data.get("public_key", None)
    if field is not None:
        args["public_key"] = unmarshal_DSRecordPublicKey(field)
    else:
        args["public_key"] = None

    return DSRecord(**args)


def unmarshal_TldOffer(data: Any) -> TldOffer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TldOffer' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("action", None)
    if field is not None:
        args["action"] = field
    else:
        args["action"] = None

    field = data.get("operation_path", None)
    if field is not None:
        args["operation_path"] = field
    else:
        args["operation_path"] = None

    field = data.get("price", None)
    if field is not None:
        args["price"] = unmarshal_Money(field)
    else:
        args["price"] = None

    return TldOffer(**args)


def unmarshal_DomainDNSSEC(data: Any) -> DomainDNSSEC:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainDNSSEC' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = None

    field = data.get("ds_records", None)
    if field is not None:
        args["ds_records"] = (
            [unmarshal_DSRecord(v) for v in field] if field is not None else None
        )
    else:
        args["ds_records"] = None

    return DomainDNSSEC(**args)


def unmarshal_DomainRegistrationStatusExternalDomain(
    data: Any,
) -> DomainRegistrationStatusExternalDomain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRegistrationStatusExternalDomain' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("validation_token", None)
    if field is not None:
        args["validation_token"] = field
    else:
        args["validation_token"] = None

    return DomainRegistrationStatusExternalDomain(**args)


def unmarshal_DomainRegistrationStatusTransfer(
    data: Any,
) -> DomainRegistrationStatusTransfer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRegistrationStatusTransfer' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = None

    field = data.get("vote_current_owner", None)
    if field is not None:
        args["vote_current_owner"] = field
    else:
        args["vote_current_owner"] = None

    field = data.get("vote_new_owner", None)
    if field is not None:
        args["vote_new_owner"] = field
    else:
        args["vote_new_owner"] = None

    return DomainRegistrationStatusTransfer(**args)


def unmarshal_Tld(data: Any) -> Tld:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Tld' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("dnssec_support", None)
    if field is not None:
        args["dnssec_support"] = field
    else:
        args["dnssec_support"] = None

    field = data.get("duration_in_years_min", None)
    if field is not None:
        args["duration_in_years_min"] = field
    else:
        args["duration_in_years_min"] = None

    field = data.get("duration_in_years_max", None)
    if field is not None:
        args["duration_in_years_max"] = field
    else:
        args["duration_in_years_max"] = None

    field = data.get("idn_support", None)
    if field is not None:
        args["idn_support"] = field
    else:
        args["idn_support"] = None

    field = data.get("offers", None)
    if field is not None:
        args["offers"] = (
            {key: unmarshal_TldOffer(value) for key, value in field.items()}
            if field is not None
            else None
        )
    else:
        args["offers"] = None

    field = data.get("specifications", None)
    if field is not None:
        args["specifications"] = field
    else:
        args["specifications"] = None

    return Tld(**args)


def unmarshal_Domain(data: Any) -> Domain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Domain' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field
    else:
        args["domain"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("auto_renew_status", None)
    if field is not None:
        args["auto_renew_status"] = field
    else:
        args["auto_renew_status"] = DomainFeatureStatus.FEATURE_STATUS_UNKNOWN

    field = data.get("epp_code", None)
    if field is not None:
        args["epp_code"] = field
    else:
        args["epp_code"] = []

    field = data.get("registrar", None)
    if field is not None:
        args["registrar"] = field
    else:
        args["registrar"] = None

    field = data.get("is_external", None)
    if field is not None:
        args["is_external"] = field
    else:
        args["is_external"] = False

    field = data.get("dnssec", None)
    if field is not None:
        args["dnssec"] = unmarshal_DomainDNSSEC(field)
    else:
        args["dnssec"] = None

    field = data.get("expired_at", None)
    if field is not None:
        args["expired_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["expired_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DomainStatus.STATUS_UNKNOWN

    field = data.get("dns_zones", None)
    if field is not None:
        args["dns_zones"] = (
            [unmarshal_DNSZone(v) for v in field] if field is not None else None
        )
    else:
        args["dns_zones"] = []

    field = data.get("linked_products", None)
    if field is not None:
        args["linked_products"] = (
            [LinkedProduct(v) for v in field] if field is not None else None
        )
    else:
        args["linked_products"] = []

    field = data.get("pending_trade", None)
    if field is not None:
        args["pending_trade"] = field
    else:
        args["pending_trade"] = False

    field = data.get("owner_contact", None)
    if field is not None:
        args["owner_contact"] = unmarshal_Contact(field)
    else:
        args["owner_contact"] = None

    field = data.get("technical_contact", None)
    if field is not None:
        args["technical_contact"] = unmarshal_Contact(field)
    else:
        args["technical_contact"] = None

    field = data.get("administrative_contact", None)
    if field is not None:
        args["administrative_contact"] = unmarshal_Contact(field)
    else:
        args["administrative_contact"] = None

    field = data.get("external_domain_registration_status", None)
    if field is not None:
        args["external_domain_registration_status"] = (
            unmarshal_DomainRegistrationStatusExternalDomain(field)
        )
    else:
        args["external_domain_registration_status"] = None

    field = data.get("transfer_registration_status", None)
    if field is not None:
        args["transfer_registration_status"] = (
            unmarshal_DomainRegistrationStatusTransfer(field)
        )
    else:
        args["transfer_registration_status"] = None

    field = data.get("tld", None)
    if field is not None:
        args["tld"] = unmarshal_Tld(field)
    else:
        args["tld"] = None

    return Domain(**args)


def unmarshal_GetDNSZoneTsigKeyResponse(data: Any) -> GetDNSZoneTsigKeyResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetDNSZoneTsigKeyResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("key", None)
    if field is not None:
        args["key"] = field
    else:
        args["key"] = None

    field = data.get("algorithm", None)
    if field is not None:
        args["algorithm"] = field
    else:
        args["algorithm"] = None

    return GetDNSZoneTsigKeyResponse(**args)


def unmarshal_RecordGeoIPConfigMatch(data: Any) -> RecordGeoIPConfigMatch:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordGeoIPConfigMatch' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("countries", None)
    if field is not None:
        args["countries"] = field
    else:
        args["countries"] = None

    field = data.get("continents", None)
    if field is not None:
        args["continents"] = field
    else:
        args["continents"] = None

    field = data.get("data", None)
    if field is not None:
        args["data"] = field
    else:
        args["data"] = None

    return RecordGeoIPConfigMatch(**args)


def unmarshal_RecordViewConfigView(data: Any) -> RecordViewConfigView:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordViewConfigView' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("subnet", None)
    if field is not None:
        args["subnet"] = field
    else:
        args["subnet"] = None

    field = data.get("data", None)
    if field is not None:
        args["data"] = field
    else:
        args["data"] = None

    return RecordViewConfigView(**args)


def unmarshal_RecordWeightedConfigWeightedIP(
    data: Any,
) -> RecordWeightedConfigWeightedIP:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordWeightedConfigWeightedIP' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("ip", None)
    if field is not None:
        args["ip"] = field
    else:
        args["ip"] = None

    field = data.get("weight", None)
    if field is not None:
        args["weight"] = field
    else:
        args["weight"] = None

    return RecordWeightedConfigWeightedIP(**args)


def unmarshal_RecordGeoIPConfig(data: Any) -> RecordGeoIPConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordGeoIPConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("matches", None)
    if field is not None:
        args["matches"] = (
            [unmarshal_RecordGeoIPConfigMatch(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["matches"] = None

    field = data.get("default", None)
    if field is not None:
        args["default"] = field
    else:
        args["default"] = None

    return RecordGeoIPConfig(**args)


def unmarshal_RecordHTTPServiceConfig(data: Any) -> RecordHTTPServiceConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordHTTPServiceConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("ips", None)
    if field is not None:
        args["ips"] = field
    else:
        args["ips"] = None

    field = data.get("url", None)
    if field is not None:
        args["url"] = field
    else:
        args["url"] = None

    field = data.get("strategy", None)
    if field is not None:
        args["strategy"] = field
    else:
        args["strategy"] = None

    field = data.get("must_contain", None)
    if field is not None:
        args["must_contain"] = field
    else:
        args["must_contain"] = None

    field = data.get("user_agent", None)
    if field is not None:
        args["user_agent"] = field
    else:
        args["user_agent"] = None

    return RecordHTTPServiceConfig(**args)


def unmarshal_RecordViewConfig(data: Any) -> RecordViewConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordViewConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("views", None)
    if field is not None:
        args["views"] = (
            [unmarshal_RecordViewConfigView(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["views"] = None

    return RecordViewConfig(**args)


def unmarshal_RecordWeightedConfig(data: Any) -> RecordWeightedConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordWeightedConfig' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("weighted_ips", None)
    if field is not None:
        args["weighted_ips"] = (
            [unmarshal_RecordWeightedConfigWeightedIP(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["weighted_ips"] = None

    return RecordWeightedConfig(**args)


def unmarshal_Record(data: Any) -> Record:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Record' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("data", None)
    if field is not None:
        args["data"] = field
    else:
        args["data"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("priority", None)
    if field is not None:
        args["priority"] = field
    else:
        args["priority"] = None

    field = data.get("ttl", None)
    if field is not None:
        args["ttl"] = field
    else:
        args["ttl"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("comment", None)
    if field is not None:
        args["comment"] = field
    else:
        args["comment"] = None

    field = data.get("geo_ip_config", None)
    if field is not None:
        args["geo_ip_config"] = unmarshal_RecordGeoIPConfig(field)
    else:
        args["geo_ip_config"] = None

    field = data.get("http_service_config", None)
    if field is not None:
        args["http_service_config"] = unmarshal_RecordHTTPServiceConfig(field)
    else:
        args["http_service_config"] = None

    field = data.get("weighted_config", None)
    if field is not None:
        args["weighted_config"] = unmarshal_RecordWeightedConfig(field)
    else:
        args["weighted_config"] = None

    field = data.get("view_config", None)
    if field is not None:
        args["view_config"] = unmarshal_RecordViewConfig(field)
    else:
        args["view_config"] = None

    return Record(**args)


def unmarshal_RecordIdentifier(data: Any) -> RecordIdentifier:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordIdentifier' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    field = data.get("data", None)
    if field is not None:
        args["data"] = field
    else:
        args["data"] = None

    field = data.get("ttl", None)
    if field is not None:
        args["ttl"] = field
    else:
        args["ttl"] = None

    return RecordIdentifier(**args)


def unmarshal_RecordChangeAdd(data: Any) -> RecordChangeAdd:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordChangeAdd' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("records", None)
    if field is not None:
        args["records"] = (
            [unmarshal_Record(v) for v in field] if field is not None else None
        )
    else:
        args["records"] = None

    return RecordChangeAdd(**args)


def unmarshal_RecordChangeClear(data: Any) -> RecordChangeClear:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordChangeClear' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return RecordChangeClear(**args)


def unmarshal_RecordChangeDelete(data: Any) -> RecordChangeDelete:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordChangeDelete' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("id_fields", None)
    if field is not None:
        args["id_fields"] = unmarshal_RecordIdentifier(field)
    else:
        args["id_fields"] = None

    return RecordChangeDelete(**args)


def unmarshal_RecordChangeSet(data: Any) -> RecordChangeSet:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordChangeSet' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("records", None)
    if field is not None:
        args["records"] = (
            [unmarshal_Record(v) for v in field] if field is not None else None
        )
    else:
        args["records"] = None

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("id_fields", None)
    if field is not None:
        args["id_fields"] = unmarshal_RecordIdentifier(field)
    else:
        args["id_fields"] = None

    return RecordChangeSet(**args)


def unmarshal_RecordChange(data: Any) -> RecordChange:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RecordChange' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("add", None)
    if field is not None:
        args["add"] = unmarshal_RecordChangeAdd(field)
    else:
        args["add"] = None

    field = data.get("set", None)
    if field is not None:
        args["set_"] = unmarshal_RecordChangeSet(field)
    else:
        args["set_"] = None

    field = data.get("delete", None)
    if field is not None:
        args["delete"] = unmarshal_RecordChangeDelete(field)
    else:
        args["delete"] = None

    field = data.get("clear", None)
    if field is not None:
        args["clear"] = unmarshal_RecordChangeClear(field)
    else:
        args["clear"] = None

    return RecordChange(**args)


def unmarshal_GetDNSZoneVersionDiffResponse(data: Any) -> GetDNSZoneVersionDiffResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetDNSZoneVersionDiffResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("changes", None)
    if field is not None:
        args["changes"] = (
            [unmarshal_RecordChange(v) for v in field] if field is not None else None
        )
    else:
        args["changes"] = None

    return GetDNSZoneVersionDiffResponse(**args)


def unmarshal_GetDomainAuthCodeResponse(data: Any) -> GetDomainAuthCodeResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetDomainAuthCodeResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("auth_code", None)
    if field is not None:
        args["auth_code"] = field
    else:
        args["auth_code"] = None

    return GetDomainAuthCodeResponse(**args)


def unmarshal_ImportProviderDNSZoneResponse(data: Any) -> ImportProviderDNSZoneResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ImportProviderDNSZoneResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("records", None)
    if field is not None:
        args["records"] = (
            [unmarshal_Record(v) for v in field] if field is not None else None
        )
    else:
        args["records"] = None

    return ImportProviderDNSZoneResponse(**args)


def unmarshal_ImportRawDNSZoneResponse(data: Any) -> ImportRawDNSZoneResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ImportRawDNSZoneResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("records", None)
    if field is not None:
        args["records"] = (
            [unmarshal_Record(v) for v in field] if field is not None else None
        )
    else:
        args["records"] = None

    return ImportRawDNSZoneResponse(**args)


def unmarshal_ContactRolesRoles(data: Any) -> ContactRolesRoles:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactRolesRoles' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("is_owner", None)
    if field is not None:
        args["is_owner"] = field
    else:
        args["is_owner"] = None

    field = data.get("is_administrative", None)
    if field is not None:
        args["is_administrative"] = field
    else:
        args["is_administrative"] = None

    field = data.get("is_technical", None)
    if field is not None:
        args["is_technical"] = field
    else:
        args["is_technical"] = None

    return ContactRolesRoles(**args)


def unmarshal_ContactRoles(data: Any) -> ContactRoles:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContactRoles' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("roles", None)
    if field is not None:
        args["roles"] = (
            {key: unmarshal_ContactRolesRoles(value) for key, value in field.items()}
            if field is not None
            else None
        )
    else:
        args["roles"] = None

    field = data.get("contact", None)
    if field is not None:
        args["contact"] = unmarshal_Contact(field)
    else:
        args["contact"] = None

    return ContactRoles(**args)


def unmarshal_ListContactsResponse(data: Any) -> ListContactsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListContactsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("contacts", None)
    if field is not None:
        args["contacts"] = (
            [unmarshal_ContactRoles(v) for v in field] if field is not None else None
        )
    else:
        args["contacts"] = None

    return ListContactsResponse(**args)


def unmarshal_Nameserver(data: Any) -> Nameserver:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Nameserver' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("ip", None)
    if field is not None:
        args["ip"] = field
    else:
        args["ip"] = None

    return Nameserver(**args)


def unmarshal_ListDNSZoneNameserversResponse(
    data: Any,
) -> ListDNSZoneNameserversResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDNSZoneNameserversResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("ns", None)
    if field is not None:
        args["ns"] = (
            [unmarshal_Nameserver(v) for v in field] if field is not None else None
        )
    else:
        args["ns"] = []

    return ListDNSZoneNameserversResponse(**args)


def unmarshal_ListDNSZoneRecordsResponse(data: Any) -> ListDNSZoneRecordsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDNSZoneRecordsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("records", None)
    if field is not None:
        args["records"] = (
            [unmarshal_Record(v) for v in field] if field is not None else None
        )
    else:
        args["records"] = []

    return ListDNSZoneRecordsResponse(**args)


def unmarshal_ListDNSZoneVersionRecordsResponse(
    data: Any,
) -> ListDNSZoneVersionRecordsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDNSZoneVersionRecordsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("records", None)
    if field is not None:
        args["records"] = (
            [unmarshal_Record(v) for v in field] if field is not None else None
        )
    else:
        args["records"] = []

    return ListDNSZoneVersionRecordsResponse(**args)


def unmarshal_DNSZoneVersion(data: Any) -> DNSZoneVersion:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DNSZoneVersion' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    return DNSZoneVersion(**args)


def unmarshal_ListDNSZoneVersionsResponse(data: Any) -> ListDNSZoneVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDNSZoneVersionsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("versions", None)
    if field is not None:
        args["versions"] = (
            [unmarshal_DNSZoneVersion(v) for v in field] if field is not None else None
        )
    else:
        args["versions"] = []

    return ListDNSZoneVersionsResponse(**args)


def unmarshal_ListDNSZonesResponse(data: Any) -> ListDNSZonesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDNSZonesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("dns_zones", None)
    if field is not None:
        args["dns_zones"] = (
            [unmarshal_DNSZone(v) for v in field] if field is not None else None
        )
    else:
        args["dns_zones"] = []

    return ListDNSZonesResponse(**args)


def unmarshal_ListDomainHostsResponse(data: Any) -> ListDomainHostsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDomainHostsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("hosts", None)
    if field is not None:
        args["hosts"] = (
            [unmarshal_Host(v) for v in field] if field is not None else None
        )
    else:
        args["hosts"] = None

    return ListDomainHostsResponse(**args)


def unmarshal_DomainSummary(data: Any) -> DomainSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainSummary' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field
    else:
        args["domain"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("auto_renew_status", None)
    if field is not None:
        args["auto_renew_status"] = field
    else:
        args["auto_renew_status"] = None

    field = data.get("dnssec_status", None)
    if field is not None:
        args["dnssec_status"] = field
    else:
        args["dnssec_status"] = None

    field = data.get("epp_code", None)
    if field is not None:
        args["epp_code"] = field
    else:
        args["epp_code"] = None

    field = data.get("registrar", None)
    if field is not None:
        args["registrar"] = field
    else:
        args["registrar"] = None

    field = data.get("is_external", None)
    if field is not None:
        args["is_external"] = field
    else:
        args["is_external"] = None

    field = data.get("expired_at", None)
    if field is not None:
        args["expired_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["expired_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("pending_trade", None)
    if field is not None:
        args["pending_trade"] = field
    else:
        args["pending_trade"] = None

    field = data.get("external_domain_registration_status", None)
    if field is not None:
        args["external_domain_registration_status"] = (
            unmarshal_DomainRegistrationStatusExternalDomain(field)
        )
    else:
        args["external_domain_registration_status"] = None

    field = data.get("transfer_registration_status", None)
    if field is not None:
        args["transfer_registration_status"] = (
            unmarshal_DomainRegistrationStatusTransfer(field)
        )
    else:
        args["transfer_registration_status"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    return DomainSummary(**args)


def unmarshal_ListDomainsResponse(data: Any) -> ListDomainsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDomainsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("domains", None)
    if field is not None:
        args["domains"] = (
            [unmarshal_DomainSummary(v) for v in field] if field is not None else None
        )
    else:
        args["domains"] = None

    return ListDomainsResponse(**args)


def unmarshal_InboundTransfer(data: Any) -> InboundTransfer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InboundTransfer' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field
    else:
        args["domain"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = InboundTransferStatus.UNKNOWN

    field = data.get("message", None)
    if field is not None:
        args["message"] = field
    else:
        args["message"] = None

    field = data.get("task_id", None)
    if field is not None:
        args["task_id"] = field
    else:
        args["task_id"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("last_updated_at", None)
    if field is not None:
        args["last_updated_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["last_updated_at"] = None

    return InboundTransfer(**args)


def unmarshal_ListInboundTransfersResponse(data: Any) -> ListInboundTransfersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInboundTransfersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("inbound_transfers", None)
    if field is not None:
        args["inbound_transfers"] = (
            [unmarshal_InboundTransfer(v) for v in field] if field is not None else None
        )
    else:
        args["inbound_transfers"] = None

    return ListInboundTransfersResponse(**args)


def unmarshal_RenewableDomain(data: Any) -> RenewableDomain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RenewableDomain' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field
    else:
        args["domain"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = None

    field = data.get("renewable_duration_in_years", None)
    if field is not None:
        args["renewable_duration_in_years"] = field
    else:
        args["renewable_duration_in_years"] = None

    field = data.get("expired_at", None)
    if field is not None:
        args["expired_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["expired_at"] = None

    field = data.get("limit_renew_at", None)
    if field is not None:
        args["limit_renew_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["limit_renew_at"] = None

    field = data.get("limit_redemption_at", None)
    if field is not None:
        args["limit_redemption_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["limit_redemption_at"] = None

    field = data.get("estimated_delete_at", None)
    if field is not None:
        args["estimated_delete_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["estimated_delete_at"] = None

    field = data.get("tld", None)
    if field is not None:
        args["tld"] = unmarshal_Tld(field)
    else:
        args["tld"] = None

    return RenewableDomain(**args)


def unmarshal_ListRenewableDomainsResponse(data: Any) -> ListRenewableDomainsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRenewableDomainsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("domains", None)
    if field is not None:
        args["domains"] = (
            [unmarshal_RenewableDomain(v) for v in field] if field is not None else None
        )
    else:
        args["domains"] = None

    return ListRenewableDomainsResponse(**args)


def unmarshal_ListSSLCertificatesResponse(data: Any) -> ListSSLCertificatesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSSLCertificatesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("certificates", None)
    if field is not None:
        args["certificates"] = (
            [unmarshal_SSLCertificate(v) for v in field] if field is not None else None
        )
    else:
        args["certificates"] = None

    return ListSSLCertificatesResponse(**args)


def unmarshal_Task(data: Any) -> Task:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Task' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = TaskType.UNKNOWN

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = TaskStatus.UNAVAILABLE

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field
    else:
        args["domain"] = None

    field = data.get("started_at", None)
    if field is not None:
        args["started_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["started_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("message", None)
    if field is not None:
        args["message"] = field
    else:
        args["message"] = None

    field = data.get("contact_identifier", None)
    if field is not None:
        args["contact_identifier"] = field
    else:
        args["contact_identifier"] = None

    return Task(**args)


def unmarshal_ListTasksResponse(data: Any) -> ListTasksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTasksResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("tasks", None)
    if field is not None:
        args["tasks"] = (
            [unmarshal_Task(v) for v in field] if field is not None else None
        )
    else:
        args["tasks"] = None

    return ListTasksResponse(**args)


def unmarshal_ListTldsResponse(data: Any) -> ListTldsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTldsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("tlds", None)
    if field is not None:
        args["tlds"] = [unmarshal_Tld(v) for v in field] if field is not None else None
    else:
        args["tlds"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListTldsResponse(**args)


def unmarshal_OrderResponse(data: Any) -> OrderResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OrderResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("domains", None)
    if field is not None:
        args["domains"] = field
    else:
        args["domains"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("task_id", None)
    if field is not None:
        args["task_id"] = field
    else:
        args["task_id"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    return OrderResponse(**args)


def unmarshal_RefreshDNSZoneResponse(data: Any) -> RefreshDNSZoneResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RefreshDNSZoneResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("dns_zones", None)
    if field is not None:
        args["dns_zones"] = (
            [unmarshal_DNSZone(v) for v in field] if field is not None else None
        )
    else:
        args["dns_zones"] = []

    return RefreshDNSZoneResponse(**args)


def unmarshal_RegisterExternalDomainResponse(
    data: Any,
) -> RegisterExternalDomainResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RegisterExternalDomainResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field
    else:
        args["domain"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("validation_token", None)
    if field is not None:
        args["validation_token"] = field
    else:
        args["validation_token"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    return RegisterExternalDomainResponse(**args)


def unmarshal_RestoreDNSZoneVersionResponse(data: Any) -> RestoreDNSZoneVersionResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RestoreDNSZoneVersionResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return RestoreDNSZoneVersionResponse(**args)


def unmarshal_RetryInboundTransferResponse(data: Any) -> RetryInboundTransferResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RetryInboundTransferResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return RetryInboundTransferResponse(**args)


def unmarshal_AvailableDomain(data: Any) -> AvailableDomain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AvailableDomain' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field
    else:
        args["domain"] = None

    field = data.get("available", None)
    if field is not None:
        args["available"] = field
    else:
        args["available"] = None

    field = data.get("tld", None)
    if field is not None:
        args["tld"] = unmarshal_Tld(field)
    else:
        args["tld"] = None

    return AvailableDomain(**args)


def unmarshal_SearchAvailableDomainsConsoleResponse(
    data: Any,
) -> SearchAvailableDomainsConsoleResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SearchAvailableDomainsConsoleResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("available_domains", None)
    if field is not None:
        args["available_domains"] = (
            [unmarshal_AvailableDomain(v) for v in field] if field is not None else None
        )
    else:
        args["available_domains"] = None

    field = data.get("exact_match_domain", None)
    if field is not None:
        args["exact_match_domain"] = unmarshal_AvailableDomain(field)
    else:
        args["exact_match_domain"] = None

    return SearchAvailableDomainsConsoleResponse(**args)


def unmarshal_SearchAvailableDomainsResponse(
    data: Any,
) -> SearchAvailableDomainsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SearchAvailableDomainsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("available_domains", None)
    if field is not None:
        args["available_domains"] = (
            [unmarshal_AvailableDomain(v) for v in field] if field is not None else None
        )
    else:
        args["available_domains"] = []

    return SearchAvailableDomainsResponse(**args)


def unmarshal_UpdateDNSZoneNameserversResponse(
    data: Any,
) -> UpdateDNSZoneNameserversResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateDNSZoneNameserversResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("ns", None)
    if field is not None:
        args["ns"] = (
            [unmarshal_Nameserver(v) for v in field] if field is not None else None
        )
    else:
        args["ns"] = []

    return UpdateDNSZoneNameserversResponse(**args)


def unmarshal_UpdateDNSZoneRecordsResponse(data: Any) -> UpdateDNSZoneRecordsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'UpdateDNSZoneRecordsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("records", None)
    if field is not None:
        args["records"] = (
            [unmarshal_Record(v) for v in field] if field is not None else None
        )
    else:
        args["records"] = []

    return UpdateDNSZoneRecordsResponse(**args)


def marshal_CloneDNSZoneRequest(
    request: CloneDNSZoneRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.dest_dns_zone is not None:
        output["dest_dns_zone"] = request.dest_dns_zone

    if request.overwrite is not None:
        output["overwrite"] = request.overwrite

    if request.project_id is not None:
        output["project_id"] = request.project_id

    return output


def marshal_CreateDNSZoneRequest(
    request: CreateDNSZoneRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.domain is not None:
        output["domain"] = request.domain

    if request.subdomain is not None:
        output["subdomain"] = request.subdomain

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_CreateSSLCertificateRequest(
    request: CreateSSLCertificateRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.dns_zone is not None:
        output["dns_zone"] = request.dns_zone

    if request.alternative_dns_zones is not None:
        output["alternative_dns_zones"] = request.alternative_dns_zones

    return output


def marshal_ImportProviderDNSZoneRequestOnlineV1(
    request: ImportProviderDNSZoneRequestOnlineV1,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.token is not None:
        output["token"] = request.token

    return output


def marshal_ImportProviderDNSZoneRequest(
    request: ImportProviderDNSZoneRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="online_v1",
                    value=request.online_v1,
                    marshal_func=marshal_ImportProviderDNSZoneRequestOnlineV1,
                ),
            ]
        ),
    )

    return output


def marshal_ImportRawDNSZoneRequestTsigKey(
    request: ImportRawDNSZoneRequestTsigKey,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.key is not None:
        output["key"] = request.key

    if request.algorithm is not None:
        output["algorithm"] = request.algorithm

    return output


def marshal_ImportRawDNSZoneRequestAXFRSource(
    request: ImportRawDNSZoneRequestAXFRSource,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

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
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.content is not None:
        output["content"] = request.content

    return output


def marshal_ImportRawDNSZoneRequest(
    request: ImportRawDNSZoneRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="bind_source",
                    value=request.bind_source,
                    marshal_func=marshal_ImportRawDNSZoneRequestBindSource,
                ),
                OneOfPossibility(
                    param="axfr_source",
                    value=request.axfr_source,
                    marshal_func=marshal_ImportRawDNSZoneRequestAXFRSource,
                ),
            ]
        ),
    )

    if request.content is not None:
        output["content"] = request.content

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.format is not None:
        output["format"] = request.format

    return output


def marshal_RefreshDNSZoneRequest(
    request: RefreshDNSZoneRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.recreate_dns_zone is not None:
        output["recreate_dns_zone"] = request.recreate_dns_zone

    if request.recreate_sub_dns_zone is not None:
        output["recreate_sub_dns_zone"] = request.recreate_sub_dns_zone

    return output


def marshal_ContactExtensionFRAssociationInfo(
    request: ContactExtensionFRAssociationInfo,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.publication_jo_page is not None:
        output["publication_jo_page"] = request.publication_jo_page

    if request.publication_jo is not None:
        output["publication_jo"] = request.publication_jo.isoformat()

    return output


def marshal_ContactExtensionFRCodeAuthAfnicInfo(
    request: ContactExtensionFRCodeAuthAfnicInfo,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.code_auth_afnic is not None:
        output["code_auth_afnic"] = request.code_auth_afnic

    return output


def marshal_ContactExtensionFRDunsInfo(
    request: ContactExtensionFRDunsInfo,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.duns_id is not None:
        output["duns_id"] = request.duns_id

    if request.local_id is not None:
        output["local_id"] = request.local_id

    return output


def marshal_ContactExtensionFRIndividualInfo(
    request: ContactExtensionFRIndividualInfo,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.whois_opt_in is not None:
        output["whois_opt_in"] = request.whois_opt_in

    return output


def marshal_ContactExtensionFRTrademarkInfo(
    request: ContactExtensionFRTrademarkInfo,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.trademark_inpi is not None:
        output["trademark_inpi"] = request.trademark_inpi

    return output


def marshal_ContactExtensionEU(
    request: ContactExtensionEU,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.european_citizenship is not None:
        output["european_citizenship"] = request.european_citizenship

    return output


def marshal_ContactExtensionFR(
    request: ContactExtensionFR,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="individual_info",
                    value=request.individual_info,
                    marshal_func=marshal_ContactExtensionFRIndividualInfo,
                ),
                OneOfPossibility(
                    param="duns_info",
                    value=request.duns_info,
                    marshal_func=marshal_ContactExtensionFRDunsInfo,
                ),
                OneOfPossibility(
                    param="association_info",
                    value=request.association_info,
                    marshal_func=marshal_ContactExtensionFRAssociationInfo,
                ),
                OneOfPossibility(
                    param="trademark_info",
                    value=request.trademark_info,
                    marshal_func=marshal_ContactExtensionFRTrademarkInfo,
                ),
                OneOfPossibility(
                    param="code_auth_afnic_info",
                    value=request.code_auth_afnic_info,
                    marshal_func=marshal_ContactExtensionFRCodeAuthAfnicInfo,
                ),
            ]
        ),
    )

    if request.mode is not None:
        output["mode"] = request.mode

    return output


def marshal_ContactExtensionIT(
    request: ContactExtensionIT,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.european_citizenship is not None:
        output["european_citizenship"] = request.european_citizenship

    if request.tax_code is not None:
        output["tax_code"] = request.tax_code

    if request.pin is not None:
        output["pin"] = request.pin

    return output


def marshal_ContactExtensionNL(
    request: ContactExtensionNL,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.legal_form is not None:
        output["legal_form"] = request.legal_form

    if request.legal_form_registration_number is not None:
        output["legal_form_registration_number"] = (
            request.legal_form_registration_number
        )

    return output


def marshal_ContactQuestion(
    request: ContactQuestion,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.question is not None:
        output["question"] = request.question

    if request.answer is not None:
        output["answer"] = request.answer

    return output


def marshal_NewContact(
    request: NewContact,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.legal_form is not None:
        output["legal_form"] = request.legal_form

    if request.firstname is not None:
        output["firstname"] = request.firstname

    if request.lastname is not None:
        output["lastname"] = request.lastname

    if request.email is not None:
        output["email"] = request.email

    if request.phone_number is not None:
        output["phone_number"] = request.phone_number

    if request.address_line_1 is not None:
        output["address_line_1"] = request.address_line_1

    if request.zip is not None:
        output["zip"] = request.zip

    if request.city is not None:
        output["city"] = request.city

    if request.company_name is not None:
        output["company_name"] = request.company_name

    if request.email_alt is not None:
        output["email_alt"] = request.email_alt

    if request.fax_number is not None:
        output["fax_number"] = request.fax_number

    if request.address_line_2 is not None:
        output["address_line_2"] = request.address_line_2

    if request.country is not None:
        output["country"] = request.country

    if request.lang is not None:
        output["lang"] = request.lang

    if request.resale is not None:
        output["resale"] = request.resale

    if request.whois_opt_in is not None:
        output["whois_opt_in"] = request.whois_opt_in

    if request.questions is not None:
        output["questions"] = [
            marshal_ContactQuestion(item, defaults) for item in request.questions
        ]

    if request.vat_identification_code is not None:
        output["vat_identification_code"] = request.vat_identification_code

    if request.company_identification_code is not None:
        output["company_identification_code"] = request.company_identification_code

    if request.extension_fr is not None:
        output["extension_fr"] = marshal_ContactExtensionFR(
            request.extension_fr, defaults
        )

    if request.extension_eu is not None:
        output["extension_eu"] = marshal_ContactExtensionEU(
            request.extension_eu, defaults
        )

    if request.state is not None:
        output["state"] = request.state

    if request.extension_nl is not None:
        output["extension_nl"] = marshal_ContactExtensionNL(
            request.extension_nl, defaults
        )

    if request.extension_it is not None:
        output["extension_it"] = marshal_ContactExtensionIT(
            request.extension_it, defaults
        )

    return output


def marshal_RegistrarApiBuyDomainsRequest(
    request: RegistrarApiBuyDomainsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="owner_contact_id",
                    value=request.owner_contact_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="owner_contact",
                    value=request.owner_contact,
                    marshal_func=marshal_NewContact,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="administrative_contact_id",
                    value=request.administrative_contact_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="administrative_contact",
                    value=request.administrative_contact,
                    marshal_func=marshal_NewContact,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="technical_contact_id",
                    value=request.technical_contact_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="technical_contact",
                    value=request.technical_contact,
                    marshal_func=marshal_NewContact,
                ),
            ]
        ),
    )

    if request.domains is not None:
        output["domains"] = request.domains

    if request.duration_in_years is not None:
        output["duration_in_years"] = request.duration_in_years

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_RegistrarApiCheckContactsCompatibilityRequest(
    request: RegistrarApiCheckContactsCompatibilityRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="owner_contact_id",
                    value=request.owner_contact_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="owner_contact",
                    value=request.owner_contact,
                    marshal_func=marshal_NewContact,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="administrative_contact_id",
                    value=request.administrative_contact_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="administrative_contact",
                    value=request.administrative_contact,
                    marshal_func=marshal_NewContact,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="technical_contact_id",
                    value=request.technical_contact_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="technical_contact",
                    value=request.technical_contact,
                    marshal_func=marshal_NewContact,
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
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.ips is not None:
        output["ips"] = request.ips

    return output


def marshal_DSRecordPublicKey(
    request: DSRecordPublicKey,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.key is not None:
        output["key"] = request.key

    return output


def marshal_DSRecordDigest(
    request: DSRecordDigest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    if request.digest is not None:
        output["digest"] = request.digest

    if request.public_key is not None:
        output["public_key"] = marshal_DSRecordPublicKey(request.public_key, defaults)

    return output


def marshal_DSRecord(
    request: DSRecord,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="digest",
                    value=request.digest,
                    marshal_func=marshal_DSRecordDigest,
                ),
                OneOfPossibility(
                    param="public_key",
                    value=request.public_key,
                    marshal_func=marshal_DSRecordPublicKey,
                ),
            ]
        ),
    )

    if request.key_id is not None:
        output["key_id"] = request.key_id

    if request.algorithm is not None:
        output["algorithm"] = request.algorithm

    return output


def marshal_RegistrarApiEnableDomainDNSSECRequest(
    request: RegistrarApiEnableDomainDNSSECRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ds_record is not None:
        output["ds_record"] = marshal_DSRecord(request.ds_record, defaults)

    return output


def marshal_RegistrarApiRegisterExternalDomainRequest(
    request: RegistrarApiRegisterExternalDomainRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.domain is not None:
        output["domain"] = request.domain

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_RegistrarApiRenewDomainsRequest(
    request: RegistrarApiRenewDomainsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.domains is not None:
        output["domains"] = request.domains

    if request.duration_in_years is not None:
        output["duration_in_years"] = request.duration_in_years

    if request.force_late_renewal is not None:
        output["force_late_renewal"] = request.force_late_renewal

    return output


def marshal_RegistrarApiRetryInboundTransferRequest(
    request: RegistrarApiRetryInboundTransferRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.domain is not None:
        output["domain"] = request.domain

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.auth_code is not None:
        output["auth_code"] = request.auth_code

    return output


def marshal_RegistrarApiTradeDomainRequest(
    request: RegistrarApiTradeDomainRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="new_owner_contact_id",
                    value=request.new_owner_contact_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="new_owner_contact",
                    value=request.new_owner_contact,
                    marshal_func=marshal_NewContact,
                ),
            ]
        ),
    )

    if request.project_id is not None:
        output["project_id"] = request.project_id

    return output


def marshal_TransferInDomainRequestTransferRequest(
    request: TransferInDomainRequestTransferRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.domain is not None:
        output["domain"] = request.domain

    if request.auth_code is not None:
        output["auth_code"] = request.auth_code

    return output


def marshal_RegistrarApiTransferInDomainRequest(
    request: RegistrarApiTransferInDomainRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="owner_contact_id",
                    value=request.owner_contact_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="owner_contact",
                    value=request.owner_contact,
                    marshal_func=marshal_NewContact,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="administrative_contact_id",
                    value=request.administrative_contact_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="administrative_contact",
                    value=request.administrative_contact,
                    marshal_func=marshal_NewContact,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="technical_contact_id",
                    value=request.technical_contact_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="technical_contact",
                    value=request.technical_contact,
                    marshal_func=marshal_NewContact,
                ),
            ]
        ),
    )

    if request.domains is not None:
        output["domains"] = [
            marshal_TransferInDomainRequestTransferRequest(item, defaults)
            for item in request.domains
        ]

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_UpdateContactRequestQuestion(
    request: UpdateContactRequestQuestion,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.question is not None:
        output["question"] = request.question

    if request.answer is not None:
        output["answer"] = request.answer

    return output


def marshal_RegistrarApiUpdateContactRequest(
    request: RegistrarApiUpdateContactRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.email is not None:
        output["email"] = request.email

    if request.email_alt is not None:
        output["email_alt"] = request.email_alt

    if request.phone_number is not None:
        output["phone_number"] = request.phone_number

    if request.fax_number is not None:
        output["fax_number"] = request.fax_number

    if request.address_line_1 is not None:
        output["address_line_1"] = request.address_line_1

    if request.address_line_2 is not None:
        output["address_line_2"] = request.address_line_2

    if request.zip is not None:
        output["zip"] = request.zip

    if request.city is not None:
        output["city"] = request.city

    if request.country is not None:
        output["country"] = request.country

    if request.vat_identification_code is not None:
        output["vat_identification_code"] = request.vat_identification_code

    if request.company_identification_code is not None:
        output["company_identification_code"] = request.company_identification_code

    if request.lang is not None:
        output["lang"] = request.lang

    if request.resale is not None:
        output["resale"] = request.resale

    if request.extension_fr is not None:
        output["extension_fr"] = marshal_ContactExtensionFR(
            request.extension_fr, defaults
        )

    if request.extension_eu is not None:
        output["extension_eu"] = marshal_ContactExtensionEU(
            request.extension_eu, defaults
        )

    if request.extension_nl is not None:
        output["extension_nl"] = marshal_ContactExtensionNL(
            request.extension_nl, defaults
        )

    if request.extension_it is not None:
        output["extension_it"] = marshal_ContactExtensionIT(
            request.extension_it, defaults
        )

    if request.whois_opt_in is not None:
        output["whois_opt_in"] = request.whois_opt_in

    if request.state is not None:
        output["state"] = request.state

    if request.questions is not None:
        output["questions"] = [
            marshal_UpdateContactRequestQuestion(item, defaults)
            for item in request.questions
        ]

    return output


def marshal_RegistrarApiUpdateDomainHostRequest(
    request: RegistrarApiUpdateDomainHostRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ips is not None:
        output["ips"] = request.ips

    return output


def marshal_RegistrarApiUpdateDomainRequest(
    request: RegistrarApiUpdateDomainRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="technical_contact_id",
                    value=request.technical_contact_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="technical_contact",
                    value=request.technical_contact,
                    marshal_func=marshal_NewContact,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="owner_contact_id",
                    value=request.owner_contact_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="owner_contact",
                    value=request.owner_contact,
                    marshal_func=marshal_NewContact,
                ),
            ]
        ),
    )
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="administrative_contact_id",
                    value=request.administrative_contact_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="administrative_contact",
                    value=request.administrative_contact,
                    marshal_func=marshal_NewContact,
                ),
            ]
        ),
    )

    return output


def marshal_Nameserver(
    request: Nameserver,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.ip is not None:
        output["ip"] = request.ip

    return output


def marshal_UpdateDNSZoneNameserversRequest(
    request: UpdateDNSZoneNameserversRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ns is not None:
        output["ns"] = [marshal_Nameserver(item, defaults) for item in request.ns]

    return output


def marshal_RecordGeoIPConfigMatch(
    request: RecordGeoIPConfigMatch,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.countries is not None:
        output["countries"] = request.countries

    if request.continents is not None:
        output["continents"] = request.continents

    if request.data is not None:
        output["data"] = request.data

    return output


def marshal_RecordViewConfigView(
    request: RecordViewConfigView,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.subnet is not None:
        output["subnet"] = request.subnet

    if request.data is not None:
        output["data"] = request.data

    return output


def marshal_RecordWeightedConfigWeightedIP(
    request: RecordWeightedConfigWeightedIP,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ip is not None:
        output["ip"] = request.ip

    if request.weight is not None:
        output["weight"] = request.weight

    return output


def marshal_RecordGeoIPConfig(
    request: RecordGeoIPConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.matches is not None:
        output["matches"] = [
            marshal_RecordGeoIPConfigMatch(item, defaults) for item in request.matches
        ]

    if request.default is not None:
        output["default"] = request.default

    return output


def marshal_RecordHTTPServiceConfig(
    request: RecordHTTPServiceConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ips is not None:
        output["ips"] = request.ips

    if request.url is not None:
        output["url"] = request.url

    if request.strategy is not None:
        output["strategy"] = request.strategy

    if request.must_contain is not None:
        output["must_contain"] = request.must_contain

    if request.user_agent is not None:
        output["user_agent"] = request.user_agent

    return output


def marshal_RecordViewConfig(
    request: RecordViewConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.views is not None:
        output["views"] = [
            marshal_RecordViewConfigView(item, defaults) for item in request.views
        ]

    return output


def marshal_RecordWeightedConfig(
    request: RecordWeightedConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.weighted_ips is not None:
        output["weighted_ips"] = [
            marshal_RecordWeightedConfigWeightedIP(item, defaults)
            for item in request.weighted_ips
        ]

    return output


def marshal_Record(
    request: Record,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="geo_ip_config",
                    value=request.geo_ip_config,
                    marshal_func=marshal_RecordGeoIPConfig,
                ),
                OneOfPossibility(
                    param="http_service_config",
                    value=request.http_service_config,
                    marshal_func=marshal_RecordHTTPServiceConfig,
                ),
                OneOfPossibility(
                    param="weighted_config",
                    value=request.weighted_config,
                    marshal_func=marshal_RecordWeightedConfig,
                ),
                OneOfPossibility(
                    param="view_config",
                    value=request.view_config,
                    marshal_func=marshal_RecordViewConfig,
                ),
            ]
        ),
    )

    if request.data is not None:
        output["data"] = request.data

    if request.name is not None:
        output["name"] = request.name

    if request.priority is not None:
        output["priority"] = request.priority

    if request.ttl is not None:
        output["ttl"] = request.ttl

    if request.type_ is not None:
        output["type"] = request.type_

    if request.id is not None:
        output["id"] = request.id

    if request.comment is not None:
        output["comment"] = request.comment

    return output


def marshal_RecordIdentifier(
    request: RecordIdentifier,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.type_ is not None:
        output["type"] = request.type_

    if request.data is not None:
        output["data"] = request.data

    if request.ttl is not None:
        output["ttl"] = request.ttl

    return output


def marshal_RecordChangeAdd(
    request: RecordChangeAdd,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.records is not None:
        output["records"] = [marshal_Record(item, defaults) for item in request.records]

    return output


def marshal_RecordChangeClear(
    request: RecordChangeClear,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    return output


def marshal_RecordChangeDelete(
    request: RecordChangeDelete,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(param="id", value=request.id, marshal_func=None),
                OneOfPossibility(
                    param="id_fields",
                    value=request.id_fields,
                    marshal_func=marshal_RecordIdentifier,
                ),
            ]
        ),
    )

    return output


def marshal_RecordChangeSet(
    request: RecordChangeSet,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(param="id", value=request.id, marshal_func=None),
                OneOfPossibility(
                    param="id_fields",
                    value=request.id_fields,
                    marshal_func=marshal_RecordIdentifier,
                ),
            ]
        ),
    )

    if request.records is not None:
        output["records"] = [marshal_Record(item, defaults) for item in request.records]

    return output


def marshal_RecordChange(
    request: RecordChange,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="add", value=request.add, marshal_func=marshal_RecordChangeAdd
                ),
                OneOfPossibility(
                    param="set",
                    value=request.set_,
                    marshal_func=marshal_RecordChangeSet,
                ),
                OneOfPossibility(
                    param="delete",
                    value=request.delete,
                    marshal_func=marshal_RecordChangeDelete,
                ),
                OneOfPossibility(
                    param="clear",
                    value=request.clear,
                    marshal_func=marshal_RecordChangeClear,
                ),
            ]
        ),
    )

    return output


def marshal_UpdateDNSZoneRecordsRequest(
    request: UpdateDNSZoneRecordsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.changes is not None:
        output["changes"] = [
            marshal_RecordChange(item, defaults) for item in request.changes
        ]

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
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.new_dns_zone is not None:
        output["new_dns_zone"] = request.new_dns_zone

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output
