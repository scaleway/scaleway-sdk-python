# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.bridge import (
    unmarshal_Money,
)
from .types import (
    GetConsumptionResponseConsumption,
    GetConsumptionResponse,
    DiscountCoupon,
    DiscountFilter,
    Discount,
    ListDiscountsResponse,
    Invoice,
    ListInvoicesResponse,
)


def unmarshal_GetConsumptionResponseConsumption(
    data: Any,
) -> GetConsumptionResponseConsumption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetConsumptionResponseConsumption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description", None)
    if field is not None:
        args["description"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("category", None)
    if field is not None:
        args["category"] = field

    field = data.get("operation_path", None)
    if field is not None:
        args["operation_path"] = field

    field = data.get("value", None)
    if field is not None:
        args["value"] = unmarshal_Money(field)
    else:
        args["value"] = None

    return GetConsumptionResponseConsumption(**args)


def unmarshal_GetConsumptionResponse(data: Any) -> GetConsumptionResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetConsumptionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("consumptions", None)
    if field is not None:
        args["consumptions"] = (
            [unmarshal_GetConsumptionResponseConsumption(v) for v in field]
            if field is not None
            else None
        )

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return GetConsumptionResponse(**args)


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


def unmarshal_Invoice(data: Any) -> Invoice:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Invoice' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("invoice_type", None)
    if field is not None:
        args["invoice_type"] = field

    field = data.get("number", None)
    if field is not None:
        args["number"] = field

    field = data.get("start_date", None)
    if field is not None:
        args["start_date"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["start_date"] = None

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

    return Invoice(**args)


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
