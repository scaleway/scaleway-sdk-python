# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    unmarshal_Money,
)
from .types import (
    OfferQuotaWarning,
    HostingCpanelUrls,
    HostingOption,
    Hosting,
    EmailAddress,
    Mailbox,
    CheckUserOwnsDomainResponse,
    DnsRecord,
    Nameserver,
    DnsRecords,
    ControlPanel,
    ListControlPanelsResponse,
    ListHostingsResponse,
    ListMailboxesResponse,
    OfferProduct,
    Offer,
    ListOffersResponse,
    ResetHostingPasswordResponse,
    Session,
    CheckUserOwnsDomainRequest,
    ClassicMailApiCreateMailboxRequest,
    ClassicMailApiUpdateMailboxRequest,
    CreateHostingRequestDomainConfiguration,
    CreateHostingRequest,
    UpdateHostingRequest,
)
from ...std.types import (
    LanguageCode as StdLanguageCode,
)


def unmarshal_HostingCpanelUrls(data: Any) -> HostingCpanelUrls:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HostingCpanelUrls' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dashboard", None)
    if field is not None:
        args["dashboard"] = field

    field = data.get("webmail", None)
    if field is not None:
        args["webmail"] = field

    return HostingCpanelUrls(**args)


def unmarshal_HostingOption(data: Any) -> HostingOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HostingOption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    return HostingOption(**args)


def unmarshal_Hosting(data: Any) -> Hosting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Hosting' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("platform_hostname", None)
    if field is not None:
        args["platform_hostname"] = field

    field = data.get("offer_id", None)
    if field is not None:
        args["offer_id"] = field

    field = data.get("offer_name", None)
    if field is not None:
        args["offer_name"] = field

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("platform_number", None)
    if field is not None:
        args["platform_number"] = field
    else:
        args["platform_number"] = None

    field = data.get("options", None)
    if field is not None:
        args["options"] = (
            [unmarshal_HostingOption(v) for v in field] if field is not None else None
        )

    field = data.get("dns_status", None)
    if field is not None:
        args["dns_status"] = field

    field = data.get("username", None)
    if field is not None:
        args["username"] = field

    field = data.get("offer_end_of_life", None)
    if field is not None:
        args["offer_end_of_life"] = field

    field = data.get("control_panel_name", None)
    if field is not None:
        args["control_panel_name"] = field

    field = data.get("platform_group", None)
    if field is not None:
        args["platform_group"] = field

    field = data.get("ipv4", None)
    if field is not None:
        args["ipv4"] = field

    field = data.get("ipv6", None)
    if field is not None:
        args["ipv6"] = field

    field = data.get("protected", None)
    if field is not None:
        args["protected"] = field

    field = data.get("one_time_password", None)
    if field is not None:
        args["one_time_password"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("cpanel_urls", None)
    if field is not None:
        args["cpanel_urls"] = unmarshal_HostingCpanelUrls(field)
    else:
        args["cpanel_urls"] = None

    return Hosting(**args)


def unmarshal_EmailAddress(data: Any) -> EmailAddress:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EmailAddress' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field

    field = data.get("login", None)
    if field is not None:
        args["login"] = field

    return EmailAddress(**args)


def unmarshal_Mailbox(data: Any) -> Mailbox:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Mailbox' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("mailbox_id", None)
    if field is not None:
        args["mailbox_id"] = field

    field = data.get("email", None)
    if field is not None:
        args["email"] = unmarshal_EmailAddress(field)
    else:
        args["email"] = None

    return Mailbox(**args)


def unmarshal_CheckUserOwnsDomainResponse(data: Any) -> CheckUserOwnsDomainResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckUserOwnsDomainResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("owns_domain", None)
    if field is not None:
        args["owns_domain"] = field

    return CheckUserOwnsDomainResponse(**args)


def unmarshal_DnsRecord(data: Any) -> DnsRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DnsRecord' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("ttl", None)
    if field is not None:
        args["ttl"] = field

    field = data.get("value", None)
    if field is not None:
        args["value"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("priority", None)
    if field is not None:
        args["priority"] = field
    else:
        args["priority"] = None

    return DnsRecord(**args)


def unmarshal_Nameserver(data: Any) -> Nameserver:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Nameserver' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("hostname", None)
    if field is not None:
        args["hostname"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("is_default", None)
    if field is not None:
        args["is_default"] = field

    return Nameserver(**args)


def unmarshal_DnsRecords(data: Any) -> DnsRecords:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DnsRecords' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records", None)
    if field is not None:
        args["records"] = (
            [unmarshal_DnsRecord(v) for v in field] if field is not None else None
        )

    field = data.get("name_servers", None)
    if field is not None:
        args["name_servers"] = (
            [unmarshal_Nameserver(v) for v in field] if field is not None else None
        )

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    return DnsRecords(**args)


def unmarshal_ControlPanel(data: Any) -> ControlPanel:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ControlPanel' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("available", None)
    if field is not None:
        args["available"] = field

    field = data.get("logo_url", None)
    if field is not None:
        args["logo_url"] = field

    field = data.get("available_languages", None)
    if field is not None:
        args["available_languages"] = (
            [StdLanguageCode(v) for v in field] if field is not None else None
        )

    return ControlPanel(**args)


def unmarshal_ListControlPanelsResponse(data: Any) -> ListControlPanelsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListControlPanelsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("control_panels", None)
    if field is not None:
        args["control_panels"] = (
            [unmarshal_ControlPanel(v) for v in field] if field is not None else None
        )

    return ListControlPanelsResponse(**args)


def unmarshal_ListHostingsResponse(data: Any) -> ListHostingsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListHostingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("hostings", None)
    if field is not None:
        args["hostings"] = (
            [unmarshal_Hosting(v) for v in field] if field is not None else None
        )

    return ListHostingsResponse(**args)


def unmarshal_ListMailboxesResponse(data: Any) -> ListMailboxesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListMailboxesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("mailboxes", None)
    if field is not None:
        args["mailboxes"] = (
            [unmarshal_Mailbox(v) for v in field] if field is not None else None
        )

    return ListMailboxesResponse(**args)


def unmarshal_OfferProduct(data: Any) -> OfferProduct:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferProduct' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("option", None)
    if field is not None:
        args["option"] = field

    field = data.get("email_accounts_quota", None)
    if field is not None:
        args["email_accounts_quota"] = field

    field = data.get("email_storage_quota", None)
    if field is not None:
        args["email_storage_quota"] = field

    field = data.get("databases_quota", None)
    if field is not None:
        args["databases_quota"] = field

    field = data.get("hosting_storage_quota", None)
    if field is not None:
        args["hosting_storage_quota"] = field

    field = data.get("support_included", None)
    if field is not None:
        args["support_included"] = field

    field = data.get("v_cpu", None)
    if field is not None:
        args["v_cpu"] = field

    field = data.get("ram", None)
    if field is not None:
        args["ram"] = field

    field = data.get("max_addon_domains", None)
    if field is not None:
        args["max_addon_domains"] = field

    return OfferProduct(**args)


def unmarshal_Offer(data: Any) -> Offer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Offer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("billing_operation_path", None)
    if field is not None:
        args["billing_operation_path"] = field

    field = data.get("available", None)
    if field is not None:
        args["available"] = field

    field = data.get("quota_warnings", None)
    if field is not None:
        args["quota_warnings"] = (
            [OfferQuotaWarning(v) for v in field] if field is not None else None
        )

    field = data.get("end_of_life", None)
    if field is not None:
        args["end_of_life"] = field

    field = data.get("control_panel_name", None)
    if field is not None:
        args["control_panel_name"] = field

    field = data.get("product", None)
    if field is not None:
        args["product"] = unmarshal_OfferProduct(field)
    else:
        args["product"] = None

    field = data.get("price", None)
    if field is not None:
        args["price"] = unmarshal_Money(field)
    else:
        args["price"] = None

    return Offer(**args)


def unmarshal_ListOffersResponse(data: Any) -> ListOffersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOffersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("offers", None)
    if field is not None:
        args["offers"] = (
            [unmarshal_Offer(v) for v in field] if field is not None else None
        )

    return ListOffersResponse(**args)


def unmarshal_ResetHostingPasswordResponse(data: Any) -> ResetHostingPasswordResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ResetHostingPasswordResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("password", None)
    if field is not None:
        args["password"] = field

    return ResetHostingPasswordResponse(**args)


def unmarshal_Session(data: Any) -> Session:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Session' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("url", None)
    if field is not None:
        args["url"] = field

    return Session(**args)


def marshal_CheckUserOwnsDomainRequest(
    request: CheckUserOwnsDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_EmailAddress(
    request: EmailAddress,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domain is not None:
        output["domain"] = request.domain

    if request.login is not None:
        output["login"] = request.login

    return output


def marshal_ClassicMailApiCreateMailboxRequest(
    request: ClassicMailApiCreateMailboxRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.password is not None:
        output["password"] = request.password

    if request.email is not None:
        output["email"] = marshal_EmailAddress(request.email, defaults)

    return output


def marshal_ClassicMailApiUpdateMailboxRequest(
    request: ClassicMailApiUpdateMailboxRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_CreateHostingRequestDomainConfiguration(
    request: CreateHostingRequestDomainConfiguration,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.update_nameservers is not None:
        output["update_nameservers"] = request.update_nameservers

    if request.update_web_record is not None:
        output["update_web_record"] = request.update_web_record

    if request.update_mail_record is not None:
        output["update_mail_record"] = request.update_mail_record

    if request.update_all_records is not None:
        output["update_all_records"] = request.update_all_records

    return output


def marshal_CreateHostingRequest(
    request: CreateHostingRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.offer_id is not None:
        output["offer_id"] = request.offer_id

    if request.domain is not None:
        output["domain"] = request.domain

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.email is not None:
        output["email"] = request.email

    if request.tags is not None:
        output["tags"] = request.tags

    if request.option_ids is not None:
        output["option_ids"] = request.option_ids

    if request.language is not None:
        output["language"] = str(request.language)

    if request.domain_configuration is not None:
        output["domain_configuration"] = (
            marshal_CreateHostingRequestDomainConfiguration(
                request.domain_configuration, defaults
            )
        )

    return output


def marshal_UpdateHostingRequest(
    request: UpdateHostingRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.email is not None:
        output["email"] = request.email

    if request.tags is not None:
        output["tags"] = request.tags

    if request.option_ids is not None:
        output["option_ids"] = request.option_ids

    if request.offer_id is not None:
        output["offer_id"] = request.offer_id

    if request.protected is not None:
        output["protected"] = request.protected

    return output
