# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.bridge import (
    unmarshal_Money,
)
from dateutil import parser
from .types import (
    GetConsumptionResponse,
    GetConsumptionResponseConsumption,
    Invoice,
    ListInvoicesResponse,
)


def unmarshal_GetConsumptionResponseConsumption(
    data: Any,
) -> GetConsumptionResponseConsumption:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetConsumptionResponseConsumption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("category", None)
    args["category"] = field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("operation_path", None)
    args["operation_path"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("value", None)
    args["value"] = unmarshal_Money(field) if field is not None else None

    return GetConsumptionResponseConsumption(**args)


def unmarshal_Invoice(data: Any) -> Invoice:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Invoice' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("due_date", None)
    args["due_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("invoice_type", None)
    args["invoice_type"] = field

    field = data.get("issued_date", None)
    args["issued_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("number", None)
    args["number"] = field

    field = data.get("start_date", None)
    args["start_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("total_taxed", None)
    args["total_taxed"] = unmarshal_Money(field) if field is not None else None

    field = data.get("total_untaxed", None)
    args["total_untaxed"] = unmarshal_Money(field) if field is not None else None

    return Invoice(**args)


def unmarshal_GetConsumptionResponse(data: Any) -> GetConsumptionResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetConsumptionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("consumptions", None)
    args["consumptions"] = (
        [unmarshal_GetConsumptionResponseConsumption(v) for v in field]
        if field is not None
        else None
    )

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return GetConsumptionResponse(**args)


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
