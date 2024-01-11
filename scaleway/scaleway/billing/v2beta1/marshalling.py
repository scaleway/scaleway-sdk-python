# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.bridge import (
    unmarshal_Money,
)
from dateutil import parser
from .types import (
    Discount,
    DiscountCoupon,
    DiscountFilter,
    Invoice,
    ListConsumptionsResponse,
    ListConsumptionsResponseConsumption,
    ListDiscountsResponse,
    ListInvoicesResponse,
    ListTaxesResponse,
    ListTaxesResponseTax,
)


def unmarshal_DiscountCoupon(data: Any) -> DiscountCoupon:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DiscountCoupon' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description", None)
    args["description"] = field

    return DiscountCoupon(**args)


def unmarshal_DiscountFilter(data: Any) -> DiscountFilter:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DiscountFilter' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", None)
    args["type_"] = field

    field = data.get("value", None)
    args["value"] = field

    return DiscountFilter(**args)


def unmarshal_Discount(data: Any) -> Discount:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Discount' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("coupon", None)
    args["coupon"] = unmarshal_DiscountCoupon(field) if field is not None else None

    field = data.get("creation_date", None)
    args["creation_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("filters", None)
    args["filters"] = (
        [unmarshal_DiscountFilter(v) for v in field] if field is not None else None
    )

    field = data.get("id", None)
    args["id"] = field

    field = data.get("mode", None)
    args["mode"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("start_date", None)
    args["start_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("stop_date", None)
    args["stop_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("value", None)
    args["value"] = field

    field = data.get("value_remaining", None)
    args["value_remaining"] = field

    field = data.get("value_used", None)
    args["value_used"] = field

    return Discount(**args)


def unmarshal_Invoice(data: Any) -> Invoice:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Invoice' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("billing_period", None)
    args["billing_period"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("due_date", None)
    args["due_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("issued_date", None)
    args["issued_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("number", None)
    args["number"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("organization_name", None)
    args["organization_name"] = field

    field = data.get("seller_name", None)
    args["seller_name"] = field

    field = data.get("start_date", None)
    args["start_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("state", None)
    args["state"] = field

    field = data.get("stop_date", None)
    args["stop_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("total_discount", None)
    args["total_discount"] = unmarshal_Money(field) if field is not None else None

    field = data.get("total_tax", None)
    args["total_tax"] = unmarshal_Money(field) if field is not None else None

    field = data.get("total_taxed", None)
    args["total_taxed"] = unmarshal_Money(field) if field is not None else None

    field = data.get("total_undiscount", None)
    args["total_undiscount"] = unmarshal_Money(field) if field is not None else None

    field = data.get("total_untaxed", None)
    args["total_untaxed"] = unmarshal_Money(field) if field is not None else None

    field = data.get("type", None)
    args["type_"] = field

    return Invoice(**args)


def unmarshal_ListConsumptionsResponseConsumption(
    data: Any,
) -> ListConsumptionsResponseConsumption:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListConsumptionsResponseConsumption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("billed_quantity", None)
    args["billed_quantity"] = field

    field = data.get("category_name", None)
    args["category_name"] = field

    field = data.get("product_name", None)
    args["product_name"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("resource_name", None)
    args["resource_name"] = field

    field = data.get("sku", None)
    args["sku"] = field

    field = data.get("unit", None)
    args["unit"] = field

    field = data.get("value", None)
    args["value"] = unmarshal_Money(field) if field is not None else None

    return ListConsumptionsResponseConsumption(**args)


def unmarshal_ListTaxesResponseTax(data: Any) -> ListTaxesResponseTax:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListTaxesResponseTax' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("currency", None)
    args["currency"] = field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("rate", None)
    args["rate"] = field

    field = data.get("total_tax_value", None)
    args["total_tax_value"] = field

    return ListTaxesResponseTax(**args)


def unmarshal_ListConsumptionsResponse(data: Any) -> ListConsumptionsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListConsumptionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("consumptions", None)
    args["consumptions"] = (
        [unmarshal_ListConsumptionsResponseConsumption(v) for v in field]
        if field is not None
        else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    field = data.get("total_discount_untaxed_value", None)
    args["total_discount_untaxed_value"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return ListConsumptionsResponse(**args)


def unmarshal_ListDiscountsResponse(data: Any) -> ListDiscountsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDiscountsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("discounts", None)
    args["discounts"] = (
        [unmarshal_Discount(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListDiscountsResponse(**args)


def unmarshal_ListInvoicesResponse(data: Any) -> ListInvoicesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListInvoicesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("invoices", None)
    args["invoices"] = (
        [unmarshal_Invoice(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListInvoicesResponse(**args)


def unmarshal_ListTaxesResponse(data: Any) -> ListTaxesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListTaxesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("taxes", None)
    args["taxes"] = (
        [unmarshal_ListTaxesResponseTax(v) for v in field]
        if field is not None
        else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return ListTaxesResponse(**args)
