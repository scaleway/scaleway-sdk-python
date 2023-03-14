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

    field = data.get("dashboard")
    args["dashboard"] = field

    field = data.get("webmail")
    args["webmail"] = field

    return HostingCpanelUrls(**args)


def unmarshal_HostingOption(data: Any) -> HostingOption:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'HostingOption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    return HostingOption(**args)


def unmarshal_OfferProduct(data: Any) -> OfferProduct:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'OfferProduct' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("databases_quota")
    args["databases_quota"] = field

    field = data.get("email_accounts_quota")
    args["email_accounts_quota"] = field

    field = data.get("email_storage_quota")
    args["email_storage_quota"] = field

    field = data.get("hosting_storage_quota")
    args["hosting_storage_quota"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("option")
    args["option"] = field

    field = data.get("ram")
    args["ram"] = field

    field = data.get("support_included")
    args["support_included"] = field

    field = data.get("v_cpu")
    args["v_cpu"] = field

    return OfferProduct(**args)


def unmarshal_DnsRecord(data: Any) -> DnsRecord:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DnsRecord' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name")
    args["name"] = field

    field = data.get("priority")
    args["priority"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("ttl")
    args["ttl"] = field

    field = data.get("type_")
    args["type_"] = field

    field = data.get("value")
    args["value"] = field

    return DnsRecord(**args)


def unmarshal_Hosting(data: Any) -> Hosting:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Hosting' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("cpanel_urls")
    args["cpanel_urls"] = (
        unmarshal_HostingCpanelUrls(field) if field is not None else None
    )

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("dns_status")
    args["dns_status"] = field

    field = data.get("domain")
    args["domain"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("offer_id")
    args["offer_id"] = field

    field = data.get("offer_name")
    args["offer_name"] = field

    field = data.get("options")
    args["options"] = [unmarshal_HostingOption(v) for v in data["options"]]

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("platform_hostname")
    args["platform_hostname"] = field

    field = data.get("platform_number")
    args["platform_number"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("region")
    args["region"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("tags")
    args["tags"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("username")
    args["username"] = field

    return Hosting(**args)


def unmarshal_Nameserver(data: Any) -> Nameserver:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Nameserver' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("hostname")
    args["hostname"] = field

    field = data.get("is_default")
    args["is_default"] = field

    field = data.get("status")
    args["status"] = field

    return Nameserver(**args)


def unmarshal_Offer(data: Any) -> Offer:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Offer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("available")
    args["available"] = field

    field = data.get("billing_operation_path")
    args["billing_operation_path"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("price")
    args["price"] = unmarshal_Money(field) if field is not None else None

    field = data.get("product")
    args["product"] = unmarshal_OfferProduct(field) if field is not None else None

    field = data.get("quota_warnings")
    args["quota_warnings"] = field

    return Offer(**args)


def unmarshal_DnsRecords(data: Any) -> DnsRecords:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DnsRecords' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name_servers")
    args["name_servers"] = [unmarshal_Nameserver(v) for v in data["name_servers"]]

    field = data.get("records")
    args["records"] = [unmarshal_DnsRecord(v) for v in data["records"]]

    field = data.get("status")
    args["status"] = field

    return DnsRecords(**args)


def unmarshal_ListHostingsResponse(data: Any) -> ListHostingsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListHostingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("hostings")
    args["hostings"] = [unmarshal_Hosting(v) for v in data["hostings"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListHostingsResponse(**args)


def unmarshal_ListOffersResponse(data: Any) -> ListOffersResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListOffersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("offers")
    args["offers"] = [unmarshal_Offer(v) for v in data["offers"]]

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
