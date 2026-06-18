# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

from scaleway_core.api import API
from scaleway_core.utils import (
    validate_path_param,
    fetch_all_pages,
)
from .types import (
    Budget,
    BudgetAlert,
    BudgetAlertNotification,
    CreateBudgetAlertNotificationRequest,
    CreateBudgetAlertRequest,
    CreateBudgetRequest,
    ListBudgetsResponse,
    UpdateBudgetAlertNotificationRequest,
    UpdateBudgetAlertRequest,
    UpdateBudgetRequest,
)
from .marshalling import (
    unmarshal_BudgetAlertNotification,
    unmarshal_BudgetAlert,
    unmarshal_Budget,
    unmarshal_ListBudgetsResponse,
    marshal_CreateBudgetAlertNotificationRequest,
    marshal_CreateBudgetAlertRequest,
    marshal_CreateBudgetRequest,
    marshal_UpdateBudgetAlertNotificationRequest,
    marshal_UpdateBudgetAlertRequest,
    marshal_UpdateBudgetRequest,
)


class BillingV2API(API):
    """
    This API allows you to query billing related objects.
    """

    def list_budgets(
        self,
        *,
        organization_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListBudgetsResponse:
        """
        List your budgets, filtering by `organization_id`.
        :param organization_id: Filter by organization ID.
        :param page: Page number.
        :param page_size: Positive integer to select the number of items to return.
        :return: :class:`ListBudgetsResponse <ListBudgetsResponse>`

        Usage:
        ::

            result = api.list_budgets()
        """

        res = self._request(
            "GET",
            "/billing/v2/budgets",
            params={
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListBudgetsResponse(res.json())

    def list_budgets_all(
        self,
        *,
        organization_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[Budget]:
        """
        List your budgets, filtering by `organization_id`.
        :param organization_id: Filter by organization ID.
        :param page: Page number.
        :param page_size: Positive integer to select the number of items to return.
        :return: :class:`list[Budget] <list[Budget]>`

        Usage:
        ::

            result = api.list_budgets_all()
        """

        return fetch_all_pages(
            type=ListBudgetsResponse,
            key="budgets",
            fetcher=self.list_budgets,
            args={
                "organization_id": organization_id,
                "page": page,
                "page_size": page_size,
            },
        )

    def get_budget(
        self,
        *,
        budget_id: str,
    ) -> Budget:
        """
        Fetch a budget.
        :param budget_id: The ID of the budget.
        :return: :class:`Budget <Budget>`

        Usage:
        ::

            result = api.get_budget(
                budget_id="example",
            )
        """

        param_budget_id = validate_path_param("budget_id", budget_id)

        res = self._request(
            "GET",
            f"/billing/v2/budgets/{param_budget_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Budget(res.json())

    def create_budget(
        self,
        *,
        consumption_limit: int,
        enabled: bool,
        organization_id: Optional[str] = None,
    ) -> Budget:
        """
        Create a new budget.
        :param consumption_limit: Cost limit for the budget.
        :param enabled: Whether the budget is enabled or not.
        :param organization_id: The Organization ID of the budget.
        :return: :class:`Budget <Budget>`

        Usage:
        ::

            result = api.create_budget(
                consumption_limit=1,
                enabled=False,
            )
        """

        res = self._request(
            "POST",
            "/billing/v2/budgets",
            body=marshal_CreateBudgetRequest(
                CreateBudgetRequest(
                    consumption_limit=consumption_limit,
                    enabled=enabled,
                    organization_id=organization_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Budget(res.json())

    def update_budget(
        self,
        *,
        budget_id: str,
        consumption_limit: Optional[int] = None,
        enabled: Optional[bool] = None,
    ) -> Budget:
        """
        Update a budget.
        :param budget_id: The ID of the budget to update.
        :param consumption_limit: Cost limit for the budget.
        :param enabled: Whether the budget will be enabled or not.
        :return: :class:`Budget <Budget>`

        Usage:
        ::

            result = api.update_budget(
                budget_id="example",
            )
        """

        param_budget_id = validate_path_param("budget_id", budget_id)

        res = self._request(
            "PATCH",
            f"/billing/v2/budgets/{param_budget_id}",
            body=marshal_UpdateBudgetRequest(
                UpdateBudgetRequest(
                    budget_id=budget_id,
                    consumption_limit=consumption_limit,
                    enabled=enabled,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Budget(res.json())

    def delete_budget(
        self,
        *,
        budget_id: str,
    ) -> None:
        """
        Delete a budget.
        :param budget_id: The ID of the budget to delete.

        Usage:
        ::

            result = api.delete_budget(
                budget_id="example",
            )
        """

        param_budget_id = validate_path_param("budget_id", budget_id)

        res = self._request(
            "DELETE",
            f"/billing/v2/budgets/{param_budget_id}",
        )

        self._throw_on_error(res)

    def create_budget_alert(
        self,
        *,
        budget_id: str,
        threshold: int,
    ) -> BudgetAlert:
        """
        Create a new budget alert.
        :param budget_id: The ID of the budget to create alert for.
        :param threshold: Threshold above which the alert is sent.
        :return: :class:`BudgetAlert <BudgetAlert>`

        Usage:
        ::

            result = api.create_budget_alert(
                budget_id="example",
                threshold=1,
            )
        """

        res = self._request(
            "POST",
            "/billing/v2/budget-alerts",
            body=marshal_CreateBudgetAlertRequest(
                CreateBudgetAlertRequest(
                    budget_id=budget_id,
                    threshold=threshold,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_BudgetAlert(res.json())

    def update_budget_alert(
        self,
        *,
        budget_alert_id: str,
        threshold: int,
    ) -> BudgetAlert:
        """
        Update a budget alert.
        :param budget_alert_id: The ID of the budget alert to update.
        :param threshold: Threshold above which the alert is sent.
        :return: :class:`BudgetAlert <BudgetAlert>`

        Usage:
        ::

            result = api.update_budget_alert(
                budget_alert_id="example",
                threshold=1,
            )
        """

        param_budget_alert_id = validate_path_param("budget_alert_id", budget_alert_id)

        res = self._request(
            "PATCH",
            f"/billing/v2/budget-alerts/{param_budget_alert_id}",
            body=marshal_UpdateBudgetAlertRequest(
                UpdateBudgetAlertRequest(
                    budget_alert_id=budget_alert_id,
                    threshold=threshold,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_BudgetAlert(res.json())

    def delete_budget_alert(
        self,
        *,
        budget_alert_id: str,
    ) -> None:
        """
        Delete a budget alert.
        :param budget_alert_id: The ID of the budget alert to delete.

        Usage:
        ::

            result = api.delete_budget_alert(
                budget_alert_id="example",
            )
        """

        param_budget_alert_id = validate_path_param("budget_alert_id", budget_alert_id)

        res = self._request(
            "DELETE",
            f"/billing/v2/budget-alerts/{param_budget_alert_id}",
        )

        self._throw_on_error(res)

    def create_budget_alert_notification(
        self,
        *,
        budget_alert_id: str,
        sms_phone_numbers: Optional[list[str]] = None,
        email_addresses: Optional[list[str]] = None,
        webhook_urls: Optional[list[str]] = None,
    ) -> BudgetAlertNotification:
        """
        Create a new budget alert notification.
        :param budget_alert_id: The ID of the budget alert to create notification for.
        :param sms_phone_numbers: List of phone numbers to receive sms notifications.
        One-Of ('recipient_type'): at most one of 'sms_phone_numbers', 'email_addresses', 'webhook_urls' could be set.
        :param email_addresses: List of email addresses to receive email notifications.
        One-Of ('recipient_type'): at most one of 'sms_phone_numbers', 'email_addresses', 'webhook_urls' could be set.
        :param webhook_urls: List of webhook url to receive webhook notifications.
        One-Of ('recipient_type'): at most one of 'sms_phone_numbers', 'email_addresses', 'webhook_urls' could be set.
        :return: :class:`BudgetAlertNotification <BudgetAlertNotification>`

        Usage:
        ::

            result = api.create_budget_alert_notification(
                budget_alert_id="example",
            )
        """

        res = self._request(
            "POST",
            "/billing/v2/budget-alert-notifications",
            body=marshal_CreateBudgetAlertNotificationRequest(
                CreateBudgetAlertNotificationRequest(
                    budget_alert_id=budget_alert_id,
                    sms_phone_numbers=sms_phone_numbers,
                    email_addresses=email_addresses,
                    webhook_urls=webhook_urls,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_BudgetAlertNotification(res.json())

    def update_budget_alert_notification(
        self,
        *,
        budget_alert_notification_id: str,
        sms_phone_numbers: Optional[list[str]] = None,
        email_addresses: Optional[list[str]] = None,
        webhook_urls: Optional[list[str]] = None,
    ) -> BudgetAlertNotification:
        """
        Update a budget alert notification.
        :param budget_alert_notification_id: The ID of the budget alert notification to update.
        :param sms_phone_numbers: List of phone numbers to receive sms notifications.
        One-Of ('recipient_type'): at most one of 'sms_phone_numbers', 'email_addresses', 'webhook_urls' could be set.
        :param email_addresses: List of email addresses to receive email notifications.
        One-Of ('recipient_type'): at most one of 'sms_phone_numbers', 'email_addresses', 'webhook_urls' could be set.
        :param webhook_urls: List of webhook url to receive webhook notifications.
        One-Of ('recipient_type'): at most one of 'sms_phone_numbers', 'email_addresses', 'webhook_urls' could be set.
        :return: :class:`BudgetAlertNotification <BudgetAlertNotification>`

        Usage:
        ::

            result = api.update_budget_alert_notification(
                budget_alert_notification_id="example",
            )
        """

        param_budget_alert_notification_id = validate_path_param(
            "budget_alert_notification_id", budget_alert_notification_id
        )

        res = self._request(
            "PATCH",
            f"/billing/v2/budget-alert-notifications/{param_budget_alert_notification_id}",
            body=marshal_UpdateBudgetAlertNotificationRequest(
                UpdateBudgetAlertNotificationRequest(
                    budget_alert_notification_id=budget_alert_notification_id,
                    sms_phone_numbers=sms_phone_numbers,
                    email_addresses=email_addresses,
                    webhook_urls=webhook_urls,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_BudgetAlertNotification(res.json())

    def delete_budget_alert_notification(
        self,
        *,
        budget_alert_notification_id: str,
    ) -> None:
        """
        Delete a budget alert notification.
        :param budget_alert_notification_id: The ID of the budget alert notification to delete.

        Usage:
        ::

            result = api.delete_budget_alert_notification(
                budget_alert_notification_id="example",
            )
        """

        param_budget_alert_notification_id = validate_path_param(
            "budget_alert_notification_id", budget_alert_notification_id
        )

        res = self._request(
            "DELETE",
            f"/billing/v2/budget-alert-notifications/{param_budget_alert_notification_id}",
        )

        self._throw_on_error(res)
