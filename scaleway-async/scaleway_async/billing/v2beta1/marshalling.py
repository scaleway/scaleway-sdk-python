# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.bridge import (
    unmarshal_Money,
)
from .types import (
    Invoice,
    ListConsumptionsResponseConsumption,
    ListConsumptionsResponse,
    DiscountCoupon,
    DiscountFilter,
    Discount,
    ListDiscountsResponse,
    ListInvoicesResponse,
    ListTaxesResponseTax,
    ListTaxesResponse,
)


def unmarshal_Invoice(data: Any) -> Invoice:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Invoice' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("organization_name", None)
    if field is not None:
        args["organization_name"] = field

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

    field = data.get("state", None)
    if field is not None:
        args["state"] = field

    field = data.get("number", None)
    if field is not None:
        args["number"] = field

    field = data.get("seller_name", None)
    if field is not None:
        args["seller_name"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("product_name", None)
    if field is not None:
        args["product_name"] = field

    field = data.get("resource_name", None)
    if field is not None:
        args["resource_name"] = field

    field = data.get("sku", None)
    if field is not None:
        args["sku"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("category_name", None)
    if field is not None:
        args["category_name"] = field

    field = data.get("unit", None)
    if field is not None:
        args["unit"] = field

    field = data.get("billed_quantity", None)
    if field is not None:
        args["billed_quantity"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("consumptions", None)
    if field is not None:
        args["consumptions"] = (
            [unmarshal_ListConsumptionsResponseConsumption(v) for v in field]
            if field is not None
            else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("total_discount_untaxed_value", None)
    if field is not None:
        args["total_discount_untaxed_value"] = field

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return ListConsumptionsResponse(**args)


def unmarshal_DiscountCoupon(data: Any) -> DiscountCoupon:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DiscountCoupon' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

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

    args: Dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("value", None)
    if field is not None:
        args["value"] = field

    return DiscountFilter(**args)


def unmarshal_Discount(data: Any) -> Discount:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Discount' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("description", None)
    if field is not None:
        args["description"] = field

    field = data.get("value", None)
    if field is not None:
        args["value"] = field

    field = data.get("value_used", None)
    if field is not None:
        args["value_used"] = field

    field = data.get("value_remaining", None)
    if field is not None:
        args["value_remaining"] = field

    field = data.get("mode", None)
    if field is not None:
        args["mode"] = field

    field = data.get("filters", None)
    if field is not None:
        args["filters"] = (
            [unmarshal_DiscountFilter(v) for v in field] if field is not None else None
        )

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


def unmarshal_ListDiscountsResponse(data: Any) -> ListDiscountsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDiscountsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("discounts", None)
    if field is not None:
        args["discounts"] = (
            [unmarshal_Discount(v) for v in field] if field is not None else None
        )

    return ListDiscountsResponse(**args)


def unmarshal_ListInvoicesResponse(data: Any) -> ListInvoicesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInvoicesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("invoices", None)
    if field is not None:
        args["invoices"] = (
            [unmarshal_Invoice(v) for v in field] if field is not None else None
        )

    return ListInvoicesResponse(**args)


def unmarshal_ListTaxesResponseTax(data: Any) -> ListTaxesResponseTax:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTaxesResponseTax' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description", None)
    if field is not None:
        args["description"] = field

    field = data.get("currency", None)
    if field is not None:
        args["currency"] = field

    field = data.get("rate", None)
    if field is not None:
        args["rate"] = field
    else:
        args["rate"] = None

    field = data.get("total_tax_value", None)
    if field is not None:
        args["total_tax_value"] = field
    else:
        args["total_tax_value"] = None

    return ListTaxesResponseTax(**args)


def unmarshal_ListTaxesResponse(data: Any) -> ListTaxesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTaxesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("taxes", None)
    if field is not None:
        args["taxes"] = (
            [unmarshal_ListTaxesResponseTax(v) for v in field]
            if field is not None
            else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return ListTaxesResponse(**args)
