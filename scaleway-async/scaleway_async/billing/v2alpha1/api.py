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
    fetch_all_pages_async,
    validate_path_param,
)
from .types import (
    DownloadInvoiceRequestFileType,
    InvoiceType,
    ListInvoicesRequestOrderBy,
    GetConsumptionResponse,
    Invoice,
    ListInvoicesResponse,
)
from .marshalling import (
    unmarshal_GetConsumptionResponse,
    unmarshal_ListInvoicesResponse,
)


class BillingV2Alpha1API(API):
    """
    Billing API.

    This API allows you to query your consumption.
    Billing API.
    """

    async def get_consumption(
        self,
        *,
        organization_id: Optional[str] = None,
    ) -> GetConsumptionResponse:
        """

        Usage:
        ::

            result = await api.get_consumption()
        """

        res = self._request(
            "GET",
            f"/billing/v2alpha1/consumption",
            params={
                "organization_id": organization_id
                or self.client.default_organization_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_GetConsumptionResponse(res.json())

    async def list_invoices(
        self,
        *,
        organization_id: Optional[str] = None,
        started_after: Optional[datetime] = None,
        started_before: Optional[datetime] = None,
        invoice_type: InvoiceType = InvoiceType.UNKNOWN_TYPE,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListInvoicesRequestOrderBy = ListInvoicesRequestOrderBy.INVOICE_NUMBER_DESC,
    ) -> ListInvoicesResponse:
        """

        Usage:
        ::

            result = await api.list_invoices()
        """

        res = self._request(
            "GET",
            f"/billing/v2alpha1/invoices",
            params={
                "invoice_type": invoice_type,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "started_after": started_after,
                "started_before": started_before,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListInvoicesResponse(res.json())

    async def list_invoices_all(
        self,
        *,
        organization_id: Optional[str] = None,
        started_after: Optional[datetime] = None,
        started_before: Optional[datetime] = None,
        invoice_type: Optional[InvoiceType] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListInvoicesRequestOrderBy] = None,
    ) -> List[Invoice]:
        """
        :return: :class:`List[ListInvoicesResponse] <List[ListInvoicesResponse]>`

        Usage:
        ::

            result = await api.list_invoices_all()
        """

        return await fetch_all_pages_async(
            type=ListInvoicesResponse,
            key="invoices",
            fetcher=self.list_invoices,
            args={
                "organization_id": organization_id,
                "started_after": started_after,
                "started_before": started_before,
                "invoice_type": invoice_type,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def download_invoice(
        self,
        *,
        invoice_id: str,
        file_type: DownloadInvoiceRequestFileType,
    ) -> Optional[ScwFile]:
        """

        Usage:
        ::

            result = await api.download_invoice(
                invoice_id="example",
                file_type=pdf,
            )
        """

        param_invoice_id = validate_path_param("invoice_id", invoice_id)

        res = self._request(
            "GET",
            f"/billing/v2alpha1/invoices/{param_invoice_id}/download",
            params={
                "file_type": file_type,
            },
        )

        self._throw_on_error(res)
        json = res.json()
        return unmarshal_ScwFile(json) if json is not None else None
