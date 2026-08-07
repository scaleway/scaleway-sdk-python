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
    BudgetAlertNotificationType,
    BudgetAlertNotification,
    BudgetAlert,
    Budget,
    ElectronicAddress,
    ListBudgetsResponse,
    ListElectronicAddressesResponse,
    CreateBudgetAlertNotificationRequest,
    CreateBudgetAlertRequest,
    CreateBudgetRequest,
    ElectronicBillingApiCreateElectronicAddressRequest,
    ElectronicBillingApiUpdateElectronicAddressRequest,
    UpdateBudgetAlertNotificationRequest,
    UpdateBudgetAlertRequest,
    UpdateBudgetRequest,
)


def unmarshal_BudgetAlertNotification(data: Any) -> BudgetAlertNotification:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BudgetAlertNotification' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = BudgetAlertNotificationType.UNKNOWN_TYPE

    field = data.get("recipients", None)
    if field is not None:
        args["recipients"] = field
    else:
        args["recipients"] = []

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return BudgetAlertNotification(**args)


def unmarshal_BudgetAlert(data: Any) -> BudgetAlert:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BudgetAlert' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("threshold", None)
    if field is not None:
        args["threshold"] = field
    else:
        args["threshold"] = 0

    field = data.get("notifications", None)
    if field is not None:
        args["notifications"] = (
            [unmarshal_BudgetAlertNotification(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["notifications"] = []

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return BudgetAlert(**args)


def unmarshal_Budget(data: Any) -> Budget:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Budget' failed as data isn't a dictionary."
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

    field = data.get("enabled", None)
    if field is not None:
        args["enabled"] = field
    else:
        args["enabled"] = False

    field = data.get("alerts", None)
    if field is not None:
        args["alerts"] = (
            [unmarshal_BudgetAlert(v) for v in field] if field is not None else None
        )
    else:
        args["alerts"] = []

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("consumption_limit", None)
    if field is not None:
        args["consumption_limit"] = unmarshal_Money(field)
    else:
        args["consumption_limit"] = None

    return Budget(**args)


def unmarshal_ElectronicAddress(data: Any) -> ElectronicAddress:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ElectronicAddress' failed as data isn't a dictionary."
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

    field = data.get("value", None)
    if field is not None:
        args["value"] = field
    else:
        args["value"] = None

    field = data.get("starts_at", None)
    if field is not None:
        args["starts_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["starts_at"] = None

    field = data.get("stops_at", None)
    if field is not None:
        args["stops_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["stops_at"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return ElectronicAddress(**args)


def unmarshal_ListBudgetsResponse(data: Any) -> ListBudgetsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListBudgetsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("budgets", None)
    if field is not None:
        args["budgets"] = (
            [unmarshal_Budget(v) for v in field] if field is not None else None
        )
    else:
        args["budgets"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListBudgetsResponse(**args)


def unmarshal_ListElectronicAddressesResponse(
    data: Any,
) -> ListElectronicAddressesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListElectronicAddressesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("electronic_addresses", None)
    if field is not None:
        args["electronic_addresses"] = (
            [unmarshal_ElectronicAddress(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["electronic_addresses"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListElectronicAddressesResponse(**args)


def marshal_CreateBudgetAlertNotificationRequest(
    request: CreateBudgetAlertNotificationRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="sms_phone_numbers",
                    value=request.sms_phone_numbers,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="email_addresses",
                    value=request.email_addresses,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="webhook_urls", value=request.webhook_urls, marshal_func=None
                ),
            ]
        ),
    )

    if request.budget_alert_id is not None:
        output["budget_alert_id"] = request.budget_alert_id

    return output


def marshal_CreateBudgetAlertRequest(
    request: CreateBudgetAlertRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.budget_id is not None:
        output["budget_id"] = request.budget_id

    if request.threshold is not None:
        output["threshold"] = request.threshold

    return output


def marshal_CreateBudgetRequest(
    request: CreateBudgetRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.consumption_limit is not None:
        output["consumption_limit"] = request.consumption_limit

    if request.enabled is not None:
        output["enabled"] = request.enabled

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id
    else:
        output["organization_id"] = defaults.default_organization_id

    return output


def marshal_ElectronicBillingApiCreateElectronicAddressRequest(
    request: ElectronicBillingApiCreateElectronicAddressRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.value is not None:
        output["value"] = request.value

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id
    else:
        output["organization_id"] = defaults.default_organization_id

    if request.starts_at is not None:
        output["starts_at"] = request.starts_at.isoformat()

    if request.stops_at is not None:
        output["stops_at"] = request.stops_at.isoformat()

    return output


def marshal_ElectronicBillingApiUpdateElectronicAddressRequest(
    request: ElectronicBillingApiUpdateElectronicAddressRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.value is not None:
        output["value"] = request.value

    if request.stops_at is not None:
        output["stops_at"] = request.stops_at.isoformat()

    return output


def marshal_UpdateBudgetAlertNotificationRequest(
    request: UpdateBudgetAlertNotificationRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="sms_phone_numbers",
                    value=request.sms_phone_numbers,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="email_addresses",
                    value=request.email_addresses,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="webhook_urls", value=request.webhook_urls, marshal_func=None
                ),
            ]
        ),
    )

    return output


def marshal_UpdateBudgetAlertRequest(
    request: UpdateBudgetAlertRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.threshold is not None:
        output["threshold"] = request.threshold

    return output


def marshal_UpdateBudgetRequest(
    request: UpdateBudgetRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.consumption_limit is not None:
        output["consumption_limit"] = request.consumption_limit

    if request.enabled is not None:
        output["enabled"] = request.enabled

    return output
