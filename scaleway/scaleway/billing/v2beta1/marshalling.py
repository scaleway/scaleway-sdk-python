# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.bridge import (
    unmarshal_Money,
)
from .types import (
    DiscountDiscountMode,
    DiscountFilterType,
    InvoiceType,
    DiscountCoupon,
    DiscountFilter,
    Discount,
    Invoice,
    ListConsumptionsResponseConsumption,
    ListConsumptionsResponse,
    ListDiscountsResponse,
    ListInvoicesResponse,
    ListTaxesResponseTax,
    ListTaxesResponse,
)


def unmarshal_DiscountCoupon(data: Any) -> DiscountCoupon:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DiscountCoupon' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    return DiscountCoupon(**args)


def unmarshal_DiscountFilter(data: Any) -> DiscountFilter:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DiscountFilter' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = DiscountFilterType.UNKNOWN_TYPE

    field = data.get("value", None)
    if field is not None:
        args["value"] = field
    else:
        args["value"] = None

    field = data.get("exclude", None)
    if field is not None:
        args["exclude"] = field
    else:
        args["exclude"] = False

    return DiscountFilter(**args)


def unmarshal_Discount(data: Any) -> Discount:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Discount' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("value", None)
    if field is not None:
        args["value"] = field
    else:
        args["value"] = 0.0

    field = data.get("value_used", None)
    if field is not None:
        args["value_used"] = field
    else:
        args["value_used"] = 0.0

    field = data.get("value_remaining", None)
    if field is not None:
        args["value_remaining"] = field
    else:
        args["value_remaining"] = 0.0

    field = data.get("mode", None)
    if field is not None:
        args["mode"] = field
    else:
        args["mode"] = DiscountDiscountMode.UNKNOWN_DISCOUNT_MODE

    field = data.get("filters", None)
    if field is not None:
        args["filters"] = (
            [unmarshal_DiscountFilter(v) for v in field] if field is not None else None
        )
    else:
        args["filters"] = []

    field = data.get("creation_date", None)
    if field is not None:
        args["creation_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["creation_date"] = None

    field = data.get("start_date", None)
    if field is not None:
        args["start_date"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["start_date"] = None

    field = data.get("stop_date", None)
    if field is not None:
        args["stop_date"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["stop_date"] = None

    field = data.get("coupon", None)
    if field is not None:
        args["coupon"] = unmarshal_DiscountCoupon(field)
    else:
        args["coupon"] = None

    return Discount(**args)


def unmarshal_Invoice(data: Any) -> Invoice:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Invoice' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("organization_name", None)
    if field is not None:
        args["organization_name"] = field
    else:
        args["organization_name"] = None

    field = data.get("start_date", None)
    if field is not None:
        args["start_date"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["start_date"] = None

    field = data.get("stop_date", None)
    if field is not None:
        args["stop_date"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["stop_date"] = None

    field = data.get("billing_period", None)
    if field is not None:
        args["billing_period"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["billing_period"] = None

    field = data.get("issued_date", None)
    if field is not None:
        args["issued_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["issued_date"] = None

    field = data.get("due_date", None)
    if field is not None:
        args["due_date"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["due_date"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = InvoiceType.UNKNOWN_TYPE

    field = data.get("state", None)
    if field is not None:
        args["state"] = field
    else:
        args["state"] = None

    field = data.get("number", None)
    if field is not None:
        args["number"] = field
    else:
        args["number"] = 0

    field = data.get("seller_name", None)
    if field is not None:
        args["seller_name"] = field
    else:
        args["seller_name"] = None

    field = data.get("total_untaxed", None)
    if field is not None:
        args["total_untaxed"] = unmarshal_Money(field)
    else:
        args["total_untaxed"] = None

    field = data.get("total_taxed", None)
    if field is not None:
        args["total_taxed"] = unmarshal_Money(field)
    else:
        args["total_taxed"] = None

    field = data.get("total_tax", None)
    if field is not None:
        args["total_tax"] = unmarshal_Money(field)
    else:
        args["total_tax"] = None

    field = data.get("total_discount", None)
    if field is not None:
        args["total_discount"] = unmarshal_Money(field)
    else:
        args["total_discount"] = None

    field = data.get("total_undiscount", None)
    if field is not None:
        args["total_undiscount"] = unmarshal_Money(field)
    else:
        args["total_undiscount"] = None

    return Invoice(**args)


def unmarshal_ListConsumptionsResponseConsumption(
    data: Any,
) -> ListConsumptionsResponseConsumption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListConsumptionsResponseConsumption' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("product_name", None)
    if field is not None:
        args["product_name"] = field
    else:
        args["product_name"] = None

    field = data.get("resource_name", None)
    if field is not None:
        args["resource_name"] = field
    else:
        args["resource_name"] = None

    field = data.get("sku", None)
    if field is not None:
        args["sku"] = field
    else:
        args["sku"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("category_name", None)
    if field is not None:
        args["category_name"] = field
    else:
        args["category_name"] = None

    field = data.get("unit", None)
    if field is not None:
        args["unit"] = field
    else:
        args["unit"] = None

    field = data.get("billed_quantity", None)
    if field is not None:
        args["billed_quantity"] = field
    else:
        args["billed_quantity"] = None

    field = data.get("value", None)
    if field is not None:
        args["value"] = unmarshal_Money(field)
    else:
        args["value"] = None

    return ListConsumptionsResponseConsumption(**args)


def unmarshal_ListConsumptionsResponse(data: Any) -> ListConsumptionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListConsumptionsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("consumptions", None)
    if field is not None:
        args["consumptions"] = (
            [unmarshal_ListConsumptionsResponseConsumption(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["consumptions"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("total_discount_untaxed_value", None)
    if field is not None:
        args["total_discount_untaxed_value"] = field
    else:
        args["total_discount_untaxed_value"] = 0.0

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return ListConsumptionsResponse(**args)


def unmarshal_ListDiscountsResponse(data: Any) -> ListDiscountsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDiscountsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("discounts", None)
    if field is not None:
        args["discounts"] = (
            [unmarshal_Discount(v) for v in field] if field is not None else None
        )
    else:
        args["discounts"] = []

    return ListDiscountsResponse(**args)


def unmarshal_ListInvoicesResponse(data: Any) -> ListInvoicesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInvoicesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("invoices", None)
    if field is not None:
        args["invoices"] = (
            [unmarshal_Invoice(v) for v in field] if field is not None else None
        )
    else:
        args["invoices"] = []

    return ListInvoicesResponse(**args)


def unmarshal_ListTaxesResponseTax(data: Any) -> ListTaxesResponseTax:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTaxesResponseTax' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("currency", None)
    if field is not None:
        args["currency"] = field
    else:
        args["currency"] = None

    field = data.get("rate", None)
    if field is not None:
        args["rate"] = field
    else:
        args["rate"] = 0.0

    field = data.get("total_tax_value", None)
    if field is not None:
        args["total_tax_value"] = field
    else:
        args["total_tax_value"] = 0.0

    return ListTaxesResponseTax(**args)


def unmarshal_ListTaxesResponse(data: Any) -> ListTaxesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTaxesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("taxes", None)
    if field is not None:
        args["taxes"] = (
            [unmarshal_ListTaxesResponseTax(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["taxes"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return ListTaxesResponse(**args)
