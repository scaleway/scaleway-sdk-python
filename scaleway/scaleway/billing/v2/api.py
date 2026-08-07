# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Optional

from scaleway_core.api import API
from scaleway_core.utils import (
    validate_path_param,
    fetch_all_pages,
)
from .types import (
    ListElectronicAddressesRequestOrderBy,
    Budget,
    BudgetAlert,
    BudgetAlertNotification,
    CreateBudgetAlertNotificationRequest,
    CreateBudgetAlertRequest,
    CreateBudgetRequest,
    ElectronicAddress,
    ElectronicBillingApiCreateElectronicAddressRequest,
    ElectronicBillingApiUpdateElectronicAddressRequest,
    ListBudgetsResponse,
    ListElectronicAddressesResponse,
    UpdateBudgetAlertNotificationRequest,
    UpdateBudgetAlertRequest,
    UpdateBudgetRequest,
)
from .marshalling import (
    unmarshal_BudgetAlertNotification,
    unmarshal_BudgetAlert,
    unmarshal_Budget,
    unmarshal_ElectronicAddress,
    unmarshal_ListBudgetsResponse,
    unmarshal_ListElectronicAddressesResponse,
    marshal_CreateBudgetAlertNotificationRequest,
    marshal_CreateBudgetAlertRequest,
    marshal_CreateBudgetRequest,
    marshal_ElectronicBillingApiCreateElectronicAddressRequest,
    marshal_ElectronicBillingApiUpdateElectronicAddressRequest,
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


class BillingV2ElectronicBillingAPI(API):
    """
    This API allows you to query electronic billing related objects.
    """

    def list_electronic_addresses(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListElectronicAddressesRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        starts_after: Optional[datetime] = None,
        stops_before: Optional[datetime] = None,
    ) -> ListElectronicAddressesResponse:
        """
        List electronic addresses.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of Electronic Address to return per page.
        :param order_by: Sort order of Electronic address in the response.
        :param organization_id: The Organization ID to set electronic address.
        :param starts_after: Filter services where electronic address start_date is greater or equal to starts_after.
        :param stops_before: Filter services where electronic address stop_date is before stops_before.
        :return: :class:`ListElectronicAddressesResponse <ListElectronicAddressesResponse>`

        Usage:
        ::

            result = api.list_electronic_addresses()
        """

        res = self._request(
            "GET",
            "/billing/v2/electronic-address",
            params={
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "starts_after": starts_after,
                "stops_before": stops_before,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListElectronicAddressesResponse(res.json())

    def list_electronic_addresses_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListElectronicAddressesRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        starts_after: Optional[datetime] = None,
        stops_before: Optional[datetime] = None,
    ) -> list[ElectronicAddress]:
        """
        List electronic addresses.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of Electronic Address to return per page.
        :param order_by: Sort order of Electronic address in the response.
        :param organization_id: The Organization ID to set electronic address.
        :param starts_after: Filter services where electronic address start_date is greater or equal to starts_after.
        :param stops_before: Filter services where electronic address stop_date is before stops_before.
        :return: :class:`list[ElectronicAddress] <list[ElectronicAddress]>`

        Usage:
        ::

            result = api.list_electronic_addresses_all()
        """

        return fetch_all_pages(
            type=ListElectronicAddressesResponse,
            key="electronic_addresses",
            fetcher=self.list_electronic_addresses,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "organization_id": organization_id,
                "starts_after": starts_after,
                "stops_before": stops_before,
            },
        )

    def get_electronic_address(
        self,
        *,
        electronic_address_id: str,
    ) -> ElectronicAddress:
        """
        Fetch an electronic address.
        :param electronic_address_id: The ID of the electronic address we want to retrieve.
        :return: :class:`ElectronicAddress <ElectronicAddress>`

        Usage:
        ::

            result = api.get_electronic_address(
                electronic_address_id="example",
            )
        """

        param_electronic_address_id = validate_path_param(
            "electronic_address_id", electronic_address_id
        )

        res = self._request(
            "GET",
            f"/billing/v2/electronic-address/{param_electronic_address_id}",
        )

        self._throw_on_error(res)
        return unmarshal_ElectronicAddress(res.json())

    def create_electronic_address(
        self,
        *,
        value: str,
        organization_id: Optional[str] = None,
        starts_at: Optional[datetime] = None,
        stops_at: Optional[datetime] = None,
    ) -> ElectronicAddress:
        """
        Create a new electronic address.
        :param value: Electronic address to set.
        :param organization_id: The Organization ID to set electronic address.
        :param starts_at: When electronic address should be active.
        :param stops_at: When electronic address should stop being active.
        :return: :class:`ElectronicAddress <ElectronicAddress>`

        Usage:
        ::

            result = api.create_electronic_address(
                value="example",
            )
        """

        res = self._request(
            "POST",
            "/billing/v2/electronic-address",
            body=marshal_ElectronicBillingApiCreateElectronicAddressRequest(
                ElectronicBillingApiCreateElectronicAddressRequest(
                    value=value,
                    organization_id=organization_id,
                    starts_at=starts_at,
                    stops_at=stops_at,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ElectronicAddress(res.json())

    def update_electronic_address(
        self,
        *,
        electronic_address_id: str,
        value: Optional[str] = None,
        stops_at: Optional[datetime] = None,
    ) -> ElectronicAddress:
        """
        Update an electronic address.
        :param electronic_address_id: The ID of the electronic address we want to update.
        :param value: Electronic address to set.
        :param stops_at: When electronic address should stop being active.
        :return: :class:`ElectronicAddress <ElectronicAddress>`

        Usage:
        ::

            result = api.update_electronic_address(
                electronic_address_id="example",
            )
        """

        param_electronic_address_id = validate_path_param(
            "electronic_address_id", electronic_address_id
        )

        res = self._request(
            "PATCH",
            f"/billing/v2/electronic-address/{param_electronic_address_id}",
            body=marshal_ElectronicBillingApiUpdateElectronicAddressRequest(
                ElectronicBillingApiUpdateElectronicAddressRequest(
                    electronic_address_id=electronic_address_id,
                    value=value,
                    stops_at=stops_at,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ElectronicAddress(res.json())

    def delete_electronic_address(
        self,
        *,
        electronic_address_id: str,
    ) -> None:
        """
        Delete an electronic address.
        :param electronic_address_id: The ID of the electronic address to delete.

        Usage:
        ::

            result = api.delete_electronic_address(
                electronic_address_id="example",
            )
        """

        param_electronic_address_id = validate_path_param(
            "electronic_address_id", electronic_address_id
        )

        res = self._request(
            "DELETE",
            f"/billing/v2/electronic-address/{param_electronic_address_id}",
        )

        self._throw_on_error(res)
