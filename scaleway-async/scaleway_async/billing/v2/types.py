# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    Money,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class BudgetAlertNotificationType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    SMS = "sms"
    EMAIL = "email"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class BudgetAlertNotification:
    id: str
    """
    Alert notification's ID.
    """

    type_: BudgetAlertNotificationType
    """
    Kind of notification.
    """

    recipients: list[str]
    """
    List of recipients for this alert.
    """

    created_at: Optional[datetime] = None
    """
    The creation date of the alert notification.
    """

    updated_at: Optional[datetime] = None
    """
    The last modification date of the alert notification.
    """


@dataclass
class BudgetAlert:
    id: str
    """
    Alert's ID.
    """

    threshold: int
    """
    Percentage threshold of the budget's limit for which the alert is triggered.
    """

    notifications: list[BudgetAlertNotification]
    """
    Notifications to send when the alert is triggered.
    """

    created_at: Optional[datetime] = None
    """
    The creation date of the alert.
    """

    updated_at: Optional[datetime] = None
    """
    The last modification date of the alert.
    """


@dataclass
class Budget:
    id: str
    """
    Budget's ID.
    """

    organization_id: str
    """
    The organization ID of the budget.
    """

    enabled: bool
    """
    Whether the budget is enabled or not.
    """

    alerts: list[BudgetAlert]
    """
    Alerts defined for this budget.
    """

    created_at: Optional[datetime] = None
    """
    The creation date of the budget.
    """

    updated_at: Optional[datetime] = None
    """
    The last modification date of the budget.
    """

    consumption_limit: Optional[Money] = None
    """
    Cost limit for this budget.
    """


@dataclass
class CreateBudgetAlertNotificationRequest:
    budget_alert_id: str
    """
    The ID of the budget alert to create notification for.
    """

    sms_phone_numbers: Optional[list[str]] = field(default_factory=list)

    email_addresses: Optional[list[str]] = field(default_factory=list)

    webhook_urls: Optional[list[str]] = field(default_factory=list)


@dataclass
class CreateBudgetAlertRequest:
    budget_id: str
    """
    The ID of the budget to create alert for.
    """

    threshold: int
    """
    Threshold above which the alert is sent.
    """


@dataclass
class CreateBudgetRequest:
    consumption_limit: int
    """
    Cost limit for the budget.
    """

    enabled: bool
    """
    Whether the budget is enabled or not.
    """

    organization_id: Optional[str] = None
    """
    The Organization ID of the budget.
    """


@dataclass
class DeleteBudgetAlertNotificationRequest:
    budget_alert_notification_id: str
    """
    The ID of the budget alert notification to delete.
    """


@dataclass
class DeleteBudgetAlertRequest:
    budget_alert_id: str
    """
    The ID of the budget alert to delete.
    """


@dataclass
class DeleteBudgetRequest:
    budget_id: str
    """
    The ID of the budget to delete.
    """


@dataclass
class GetBudgetRequest:
    budget_id: str
    """
    The ID of the budget.
    """


@dataclass
class ListBudgetsRequest:
    organization_id: Optional[str] = None
    """
    Filter by organization ID.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Positive integer to select the number of items to return.
    """


@dataclass
class ListBudgetsResponse:
    budgets: list[Budget]
    """
    Detailed budget list.
    """

    total_count: int
    """
    Total number of items.
    """


@dataclass
class UpdateBudgetAlertNotificationRequest:
    budget_alert_notification_id: str
    """
    The ID of the budget alert notification to update.
    """

    sms_phone_numbers: Optional[list[str]] = field(default_factory=list)

    email_addresses: Optional[list[str]] = field(default_factory=list)

    webhook_urls: Optional[list[str]] = field(default_factory=list)


@dataclass
class UpdateBudgetAlertRequest:
    budget_alert_id: str
    """
    The ID of the budget alert to update.
    """

    threshold: int
    """
    Threshold above which the alert is sent.
    """


@dataclass
class UpdateBudgetRequest:
    budget_id: str
    """
    The ID of the budget to update.
    """

    consumption_limit: Optional[int] = 0
    """
    Cost limit for the budget.
    """

    enabled: Optional[bool] = False
    """
    Whether the budget will be enabled or not.
    """
