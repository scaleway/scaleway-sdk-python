# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    ScwFile,
    unmarshal_ScwFile,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
    validate_path_param,
    fetch_all_pages,
)
from .types import (
    DownloadInvoiceRequestFileType,
    ExportInvoicesRequestFileType,
    ExportInvoicesRequestOrderBy,
    InvoiceType,
    ListConsumptionsRequestOrderBy,
    ListDiscountsRequestOrderBy,
    ListInvoicesRequestOrderBy,
    ListTaxesRequestOrderBy,
    Discount,
    Invoice,
    ListConsumptionsResponse,
    ListConsumptionsResponseConsumption,
    ListDiscountsResponse,
    ListInvoicesResponse,
    ListTaxesResponse,
    ListTaxesResponseTax,
)
from .marshalling import (
    unmarshal_Invoice,
    unmarshal_ListConsumptionsResponse,
    unmarshal_ListDiscountsResponse,
    unmarshal_ListInvoicesResponse,
    unmarshal_ListTaxesResponse,
)


class BillingV2Beta1API(API):
    """
    This API allows you to manage and query your Scaleway billing and consumption.
    """

    def list_consumptions(
        self,
        *,
        order_by: Optional[ListConsumptionsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        category_name: Optional[str] = None,
        billing_period: Optional[str] = None,
    ) -> ListConsumptionsResponse:
        """
        Get monthly consumption.
        Consumption allows you to retrieve your past or current consumption cost, by project or category.
        :param order_by: Order consumptions list in the response by their update date.
        :param page: Positive integer to choose the page to return.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :param organization_id: Filter by Organization ID.
        One-Of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Filter by Project ID.
        One-Of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param category_name: Filter by name of a Category as they are shown in the invoice (Compute, Network, Observability).
        :param billing_period: Filter by the billing period in the YYYY-MM format. If it is empty the current billing period will be used as default.
        :return: :class:`ListConsumptionsResponse <ListConsumptionsResponse>`

        Usage:
        ::

            result = api.list_consumptions()
        """

        res = self._request(
            "GET",
            "/billing/v2beta1/consumptions",
            params={
                "billing_period": billing_period,
                "category_name": category_name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                **resolve_one_of(
                    [
                        OneOfPossibility("organization_id", organization_id),
                        OneOfPossibility("project_id", project_id),
                    ]
                ),
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListConsumptionsResponse(res.json())

    def list_consumptions_all(
        self,
        *,
        order_by: Optional[ListConsumptionsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        category_name: Optional[str] = None,
        billing_period: Optional[str] = None,
    ) -> List[ListConsumptionsResponseConsumption]:
        """
        Get monthly consumption.
        Consumption allows you to retrieve your past or current consumption cost, by project or category.
        :param order_by: Order consumptions list in the response by their update date.
        :param page: Positive integer to choose the page to return.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :param organization_id: Filter by Organization ID.
        One-Of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Filter by Project ID.
        One-Of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param category_name: Filter by name of a Category as they are shown in the invoice (Compute, Network, Observability).
        :param billing_period: Filter by the billing period in the YYYY-MM format. If it is empty the current billing period will be used as default.
        :return: :class:`List[ListConsumptionsResponseConsumption] <List[ListConsumptionsResponseConsumption]>`

        Usage:
        ::

            result = api.list_consumptions_all()
        """

        return fetch_all_pages(
            type=ListConsumptionsResponse,
            key="consumptions",
            fetcher=self.list_consumptions,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "category_name": category_name,
                "billing_period": billing_period,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    def list_taxes(
        self,
        *,
        order_by: Optional[ListTaxesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        billing_period: Optional[str] = None,
    ) -> ListTaxesResponse:
        """
        Get monthly consumption taxes.
        Consumption Tax allows you to retrieve your past or current tax charges, by project or category.
        :param order_by: Order consumed taxes list in the response by their update date.
        :param page: Page number.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :param organization_id: Filter by Organization ID.
        :param billing_period: Filter by the billing period in the YYYY-MM format. If it is empty the current billing period will be used as default.
        :return: :class:`ListTaxesResponse <ListTaxesResponse>`

        Usage:
        ::

            result = api.list_taxes()
        """

        res = self._request(
            "GET",
            "/billing/v2beta1/taxes",
            params={
                "billing_period": billing_period,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListTaxesResponse(res.json())

    def list_taxes_all(
        self,
        *,
        order_by: Optional[ListTaxesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        billing_period: Optional[str] = None,
    ) -> List[ListTaxesResponseTax]:
        """
        Get monthly consumption taxes.
        Consumption Tax allows you to retrieve your past or current tax charges, by project or category.
        :param order_by: Order consumed taxes list in the response by their update date.
        :param page: Page number.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :param organization_id: Filter by Organization ID.
        :param billing_period: Filter by the billing period in the YYYY-MM format. If it is empty the current billing period will be used as default.
        :return: :class:`List[ListTaxesResponseTax] <List[ListTaxesResponseTax]>`

        Usage:
        ::

            result = api.list_taxes_all()
        """

        return fetch_all_pages(
            type=ListTaxesResponse,
            key="taxes",
            fetcher=self.list_taxes,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "organization_id": organization_id,
                "billing_period": billing_period,
            },
        )

    def list_invoices(
        self,
        *,
        organization_id: Optional[str] = None,
        billing_period_start_after: Optional[datetime] = None,
        billing_period_start_before: Optional[datetime] = None,
        invoice_type: Optional[InvoiceType] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListInvoicesRequestOrderBy] = None,
    ) -> ListInvoicesResponse:
        """
        List invoices.
        List all your invoices, filtering by `start_date` and `invoice_type`. Each invoice has its own ID.
        :param organization_id: Organization ID. If specified, only invoices from this Organization will be returned.
        :param billing_period_start_after: Return only invoice with start date greater than billing_period_start.
        :param billing_period_start_before: Return only invoice with start date less than billing_period_start.
        :param invoice_type: Invoice type. It can either be `periodic` or `purchase`.
        :param page: Page number.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :param order_by: How invoices are ordered in the response.
        :return: :class:`ListInvoicesResponse <ListInvoicesResponse>`

        Usage:
        ::

            result = api.list_invoices()
        """

        res = self._request(
            "GET",
            "/billing/v2beta1/invoices",
            params={
                "billing_period_start_after": billing_period_start_after,
                "billing_period_start_before": billing_period_start_before,
                "invoice_type": invoice_type,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListInvoicesResponse(res.json())

    def list_invoices_all(
        self,
        *,
        organization_id: Optional[str] = None,
        billing_period_start_after: Optional[datetime] = None,
        billing_period_start_before: Optional[datetime] = None,
        invoice_type: Optional[InvoiceType] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListInvoicesRequestOrderBy] = None,
    ) -> List[Invoice]:
        """
        List invoices.
        List all your invoices, filtering by `start_date` and `invoice_type`. Each invoice has its own ID.
        :param organization_id: Organization ID. If specified, only invoices from this Organization will be returned.
        :param billing_period_start_after: Return only invoice with start date greater than billing_period_start.
        :param billing_period_start_before: Return only invoice with start date less than billing_period_start.
        :param invoice_type: Invoice type. It can either be `periodic` or `purchase`.
        :param page: Page number.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :param order_by: How invoices are ordered in the response.
        :return: :class:`List[Invoice] <List[Invoice]>`

        Usage:
        ::

            result = api.list_invoices_all()
        """

        return fetch_all_pages(
            type=ListInvoicesResponse,
            key="invoices",
            fetcher=self.list_invoices,
            args={
                "organization_id": organization_id,
                "billing_period_start_after": billing_period_start_after,
                "billing_period_start_before": billing_period_start_before,
                "invoice_type": invoice_type,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    def export_invoices(
        self,
        *,
        organization_id: Optional[str] = None,
        billing_period_start_after: Optional[datetime] = None,
        billing_period_start_before: Optional[datetime] = None,
        invoice_type: Optional[InvoiceType] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ExportInvoicesRequestOrderBy] = None,
        file_type: Optional[ExportInvoicesRequestFileType] = None,
    ) -> ScwFile:
        """
        Export invoices.
        Export invoices in a CSV file.
        :param organization_id: Organization ID. If specified, only invoices from this Organization will be returned.
        :param billing_period_start_after: Return only invoice with start date greater than billing_period_start.
        :param billing_period_start_before: Return only invoice with start date less than billing_period_start.
        :param invoice_type: Invoice type. It can either be `periodic` or `purchase`.
        :param page: Page number.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :param order_by: How invoices are ordered in the response.
        :param file_type: File format for exporting the invoice list.
        :return: :class:`ScwFile <ScwFile>`

        Usage:
        ::

            result = api.export_invoices()
        """

        res = self._request(
            "GET",
            "/billing/v2beta1/export-invoices",
            params={
                "billing_period_start_after": billing_period_start_after,
                "billing_period_start_before": billing_period_start_before,
                "file_type": file_type,
                "invoice_type": invoice_type,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ScwFile(res.json())

    def get_invoice(
        self,
        *,
        invoice_id: str,
    ) -> Invoice:
        """
        Get an invoice.
        Get a specific invoice, specified by its ID.
        :param invoice_id: Invoice ID.
        :return: :class:`Invoice <Invoice>`

        Usage:
        ::

            result = api.get_invoice(
                invoice_id="example",
            )
        """

        param_invoice_id = validate_path_param("invoice_id", invoice_id)

        res = self._request(
            "GET",
            f"/billing/v2beta1/invoices/{param_invoice_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Invoice(res.json())

    def download_invoice(
        self,
        *,
        invoice_id: str,
        file_type: Optional[DownloadInvoiceRequestFileType] = None,
    ) -> ScwFile:
        """
        Download an invoice.
        Download a specific invoice, specified by its ID.
        :param invoice_id: Invoice ID.
        :param file_type: File type. PDF by default.
        :return: :class:`ScwFile <ScwFile>`

        Usage:
        ::

            result = api.download_invoice(
                invoice_id="example",
            )
        """

        param_invoice_id = validate_path_param("invoice_id", invoice_id)

        res = self._request(
            "GET",
            f"/billing/v2beta1/invoices/{param_invoice_id}/download",
            params={
                "file_type": file_type,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ScwFile(res.json())

    def list_discounts(
        self,
        *,
        order_by: Optional[ListDiscountsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
    ) -> ListDiscountsResponse:
        """
        List discounts.
        List all discounts for your organization and usable categories, products, offers, references, regions and zones where the discount can be applied.
        :param order_by: Order discounts in the response by their description.
        :param page: Positive integer to choose the page to return.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :param organization_id: ID of the organization.
        :return: :class:`ListDiscountsResponse <ListDiscountsResponse>`

        Usage:
        ::

            result = api.list_discounts()
        """

        res = self._request(
            "GET",
            "/billing/v2beta1/discounts",
            params={
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDiscountsResponse(res.json())

    def list_discounts_all(
        self,
        *,
        order_by: Optional[ListDiscountsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
    ) -> List[Discount]:
        """
        List discounts.
        List all discounts for your organization and usable categories, products, offers, references, regions and zones where the discount can be applied.
        :param order_by: Order discounts in the response by their description.
        :param page: Positive integer to choose the page to return.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :param organization_id: ID of the organization.
        :return: :class:`List[Discount] <List[Discount]>`

        Usage:
        ::

            result = api.list_discounts_all()
        """

        return fetch_all_pages(
            type=ListDiscountsResponse,
            key="discounts",
            fetcher=self.list_discounts,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "organization_id": organization_id,
            },
        )
