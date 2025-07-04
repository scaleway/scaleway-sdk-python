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
    DiscountDiscountMode,
    DiscountFilterType,
    DownloadInvoiceRequestFileType,
    ExportInvoicesRequestFileType,
    ExportInvoicesRequestOrderBy,
    InvoiceType,
    ListConsumptionsRequestOrderBy,
    ListDiscountsRequestOrderBy,
    ListInvoicesRequestOrderBy,
    ListTaxesRequestOrderBy,
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

    args: Dict[str, Any] = {}

    field = data.get("description", None)
    args["description"] = field

    return DiscountCoupon(**args)

def unmarshal_DiscountFilter(data: Any) -> DiscountFilter:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DiscountFilter' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", getattr(DiscountFilterType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("value", str())
    args["value"] = field

    field = data.get("exclude", False)
    args["exclude"] = field

    return DiscountFilter(**args)

def unmarshal_Discount(data: Any) -> Discount:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Discount' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("value", 0.0)
    args["value"] = field

    field = data.get("value_used", 0.0)
    args["value_used"] = field

    field = data.get("value_remaining", 0.0)
    args["value_remaining"] = field

    field = data.get("mode", getattr(DiscountDiscountMode, "UNKNOWN_DISCOUNT_MODE"))
    args["mode"] = field

    field = data.get("filters", [])
    args["filters"] = [unmarshal_DiscountFilter(v) for v in field] if field is not None else None

    field = data.get("creation_date", None)
    args["creation_date"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("start_date", None)
    args["start_date"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("stop_date", None)
    args["stop_date"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("coupon", None)
    args["coupon"] = unmarshal_DiscountCoupon(field) if field is not None else None

    return Discount(**args)

def unmarshal_Invoice(data: Any) -> Invoice:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Invoice' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("organization_name", str())
    args["organization_name"] = field

    field = data.get("start_date", None)
    args["start_date"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("stop_date", None)
    args["stop_date"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("billing_period", None)
    args["billing_period"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("issued_date", None)
    args["issued_date"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("due_date", None)
    args["due_date"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("type", getattr(InvoiceType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("state", str())
    args["state"] = field

    field = data.get("number", 0)
    args["number"] = field

    field = data.get("seller_name", str())
    args["seller_name"] = field

    field = data.get("total_untaxed", None)
    args["total_untaxed"] = unmarshal_Money(field) if field is not None else None

    field = data.get("total_taxed", None)
    args["total_taxed"] = unmarshal_Money(field) if field is not None else None

    field = data.get("total_tax", None)
    args["total_tax"] = unmarshal_Money(field) if field is not None else None

    field = data.get("total_discount", None)
    args["total_discount"] = unmarshal_Money(field) if field is not None else None

    field = data.get("total_undiscount", None)
    args["total_undiscount"] = unmarshal_Money(field) if field is not None else None

    return Invoice(**args)

def unmarshal_ListConsumptionsResponseConsumption(data: Any) -> ListConsumptionsResponseConsumption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListConsumptionsResponseConsumption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("product_name", str())
    args["product_name"] = field

    field = data.get("resource_name", str())
    args["resource_name"] = field

    field = data.get("sku", str())
    args["sku"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("category_name", str())
    args["category_name"] = field

    field = data.get("unit", str())
    args["unit"] = field

    field = data.get("billed_quantity", str())
    args["billed_quantity"] = field

    field = data.get("value", None)
    args["value"] = unmarshal_Money(field) if field is not None else None

    return ListConsumptionsResponseConsumption(**args)

def unmarshal_ListConsumptionsResponse(data: Any) -> ListConsumptionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListConsumptionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("consumptions", [])
    args["consumptions"] = [unmarshal_ListConsumptionsResponseConsumption(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("total_discount_untaxed_value", 0.0)
    args["total_discount_untaxed_value"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return ListConsumptionsResponse(**args)

def unmarshal_ListDiscountsResponse(data: Any) -> ListDiscountsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDiscountsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("discounts", [])
    args["discounts"] = [unmarshal_Discount(v) for v in field] if field is not None else None

    return ListDiscountsResponse(**args)

def unmarshal_ListInvoicesResponse(data: Any) -> ListInvoicesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInvoicesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("invoices", [])
    args["invoices"] = [unmarshal_Invoice(v) for v in field] if field is not None else None

    return ListInvoicesResponse(**args)

def unmarshal_ListTaxesResponseTax(data: Any) -> ListTaxesResponseTax:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTaxesResponseTax' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description", str())
    args["description"] = field

    field = data.get("currency", str())
    args["currency"] = field

    field = data.get("rate", None)
    args["rate"] = field

    field = data.get("total_tax_value", None)
    args["total_tax_value"] = field

    return ListTaxesResponseTax(**args)

def unmarshal_ListTaxesResponse(data: Any) -> ListTaxesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTaxesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("taxes", [])
    args["taxes"] = [unmarshal_ListTaxesResponseTax(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return ListTaxesResponse(**args)
