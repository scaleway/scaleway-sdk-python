# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    unmarshal_Money,
)
from dateutil import parser
from .types import (
    DnsRecord,
    DnsRecords,
    Hosting,
    HostingCpanelUrls,
    HostingOption,
    ListHostingsResponse,
    ListOffersResponse,
    Nameserver,
    Offer,
    OfferProduct,
    CreateHostingRequest,
    UpdateHostingRequest,
)


def unmarshal_HostingCpanelUrls(data: Any) -> HostingCpanelUrls:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'HostingCpanelUrls' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dashboard", None)
    args["dashboard"] = field

    field = data.get("webmail", None)
    args["webmail"] = field

    return HostingCpanelUrls(**args)


def unmarshal_HostingOption(data: Any) -> HostingOption:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'HostingOption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    return HostingOption(**args)


def unmarshal_OfferProduct(data: Any) -> OfferProduct:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'OfferProduct' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("databases_quota", None)
    args["databases_quota"] = field

    field = data.get("email_accounts_quota", None)
    args["email_accounts_quota"] = field

    field = data.get("email_storage_quota", None)
    args["email_storage_quota"] = field

    field = data.get("hosting_storage_quota", None)
    args["hosting_storage_quota"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("option", None)
    args["option"] = field

    field = data.get("ram", None)
    args["ram"] = field

    field = data.get("support_included", None)
    args["support_included"] = field

    field = data.get("v_cpu", None)
    args["v_cpu"] = field

    return OfferProduct(**args)


def unmarshal_DnsRecord(data: Any) -> DnsRecord:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DnsRecord' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    args["name"] = field

    field = data.get("priority", None)
    args["priority"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("ttl", None)
    args["ttl"] = field

    field = data.get("type", None)
    args["type_"] = field

    field = data.get("value", None)
    args["value"] = field

    return DnsRecord(**args)


def unmarshal_Hosting(data: Any) -> Hosting:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Hosting' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("cpanel_urls", None)
    args["cpanel_urls"] = (
        unmarshal_HostingCpanelUrls(field) if field is not None else None
    )

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("dns_status", None)
    args["dns_status"] = field

    field = data.get("domain", None)
    args["domain"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("offer_id", None)
    args["offer_id"] = field

    field = data.get("offer_name", None)
    args["offer_name"] = field

    field = data.get("options", None)
    args["options"] = (
        [unmarshal_HostingOption(v) for v in field] if field is not None else None
    )

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("platform_hostname", None)
    args["platform_hostname"] = field

    field = data.get("platform_number", None)
    args["platform_number"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("username", None)
    args["username"] = field

    return Hosting(**args)


def unmarshal_Nameserver(data: Any) -> Nameserver:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Nameserver' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("hostname", None)
    args["hostname"] = field

    field = data.get("is_default", None)
    args["is_default"] = field

    field = data.get("status", None)
    args["status"] = field

    return Nameserver(**args)


def unmarshal_Offer(data: Any) -> Offer:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Offer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("available", None)
    args["available"] = field

    field = data.get("billing_operation_path", None)
    args["billing_operation_path"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("price", None)
    args["price"] = unmarshal_Money(field) if field is not None else None

    field = data.get("product", None)
    args["product"] = unmarshal_OfferProduct(field) if field is not None else None

    field = data.get("quota_warnings", None)
    args["quota_warnings"] = field

    return Offer(**args)


def unmarshal_DnsRecords(data: Any) -> DnsRecords:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DnsRecords' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name_servers", None)
    args["name_servers"] = (
        [unmarshal_Nameserver(v) for v in field] if field is not None else None
    )

    field = data.get("records", None)
    args["records"] = (
        [unmarshal_DnsRecord(v) for v in field] if field is not None else None
    )

    field = data.get("status", None)
    args["status"] = field

    return DnsRecords(**args)


def unmarshal_ListHostingsResponse(data: Any) -> ListHostingsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListHostingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("hostings", None)
    args["hostings"] = (
        [unmarshal_Hosting(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListHostingsResponse(**args)


def unmarshal_ListOffersResponse(data: Any) -> ListOffersResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListOffersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("offers", None)
    args["offers"] = [unmarshal_Offer(v) for v in field] if field is not None else None

    return ListOffersResponse(**args)


def marshal_CreateHostingRequest(
    request: CreateHostingRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "domain": request.domain,
        "email": request.email,
        "offer_id": request.offer_id,
        "option_ids": request.option_ids,
        "project_id": request.project_id or defaults.default_project_id,
        "tags": request.tags,
    }


def marshal_UpdateHostingRequest(
    request: UpdateHostingRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "email": request.email,
        "offer_id": request.offer_id,
        "option_ids": request.option_ids,
        "tags": request.tags,
    }
