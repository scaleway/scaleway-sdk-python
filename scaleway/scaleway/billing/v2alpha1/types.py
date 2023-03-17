# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Money,
)


class DownloadInvoiceRequestFileType(str, Enum):
    PDF = "pdf"

    def __str__(self) -> str:
        return str(self.value)


class InvoiceType(str, Enum):
    UNKNOWN_TYPE = "unknown_type"
    PERIODIC = "periodic"
    PURCHASE = "purchase"

    def __str__(self) -> str:
        return str(self.value)


class ListInvoicesRequestOrderBy(str, Enum):
    INVOICE_NUMBER_DESC = "invoice_number_desc"
    INVOICE_NUMBER_ASC = "invoice_number_asc"
    START_DATE_DESC = "start_date_desc"
    START_DATE_ASC = "start_date_asc"
    ISSUED_DATE_DESC = "issued_date_desc"
    ISSUED_DATE_ASC = "issued_date_asc"
    DUE_DATE_DESC = "due_date_desc"
    DUE_DATE_ASC = "due_date_asc"
    TOTAL_UNTAXED_DESC = "total_untaxed_desc"
    TOTAL_UNTAXED_ASC = "total_untaxed_asc"
    TOTAL_TAXED_DESC = "total_taxed_desc"
    TOTAL_TAXED_ASC = "total_taxed_asc"
    INVOICE_TYPE_DESC = "invoice_type_desc"
    INVOICE_TYPE_ASC = "invoice_type_asc"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class GetConsumptionResponse:
    """
    Get consumption response.
    """

    consumptions: List[GetConsumptionResponseConsumption]
    """
    Detailed consumption list.
    """

    updated_at: Optional[datetime]
    """
    Last consumption update date.
    """


@dataclass
class GetConsumptionResponseConsumption:
    """
    Get consumption response. consumption.
    """

    value: Optional[Money]
    """
    Monetary value of the consumption.
    """

    description: str
    """
    Description of the consumption.
    """

    project_id: str
    """
    Project ID of the consumption.
    """

    category: str
    """
    Category of the consumption.
    """

    operation_path: str
    """
    Unique identifier of the product.
    """


@dataclass
class Invoice:
    """
    Invoice.
    """

    id: str
    """
    Invoice ID.
    """

    start_date: Optional[datetime]
    """
    Start date of the billing period.
    """

    issued_date: Optional[datetime]
    """
    Date when the invoice was sent to the customer.
    """

    due_date: Optional[datetime]
    """
    Payment time limit, set according to the Organization's payment conditions.
    """

    total_untaxed: Optional[Money]
    """
    Total amount, untaxed.
    """

    total_taxed: Optional[Money]
    """
    Total amount, taxed.
    """

    invoice_type: InvoiceType
    """
    Type of invoice.
    """

    number: int
    """
    Invoice number.
    """


@dataclass
class ListInvoicesResponse:
    """
    List invoices response.
    """

    total_count: int
    """
    Total number of invoices.
    """

    invoices: List[Invoice]
    """
    Paginated returned invoices.
    """


@dataclass
class GetConsumptionRequest:
    organization_id: Optional[str]
    """
    Filter by organization ID.
    """


@dataclass
class ListInvoicesRequest:
    organization_id: Optional[str]
    """
    Organization ID to filter for, only invoices from this Organization will be returned.
    """

    started_after: Optional[datetime]
    """
    Invoice's `start_date` is greater or equal to `started_after`.
    """

    started_before: Optional[datetime]
    """
    Invoice's `start_date` precedes `started_before`.
    """

    invoice_type: Optional[InvoiceType]
    """
    Invoice type. It can either be `periodic` or `purchase`.
    """

    page: Optional[int]
    """
    Positive integer to choose the page to return.
    """

    page_size: Optional[int]
    """
    Positive integer lower or equal to 100 to select the number of items to return.
    """

    order_by: Optional[ListInvoicesRequestOrderBy]
    """
    How invoices are ordered in the response.
    """


@dataclass
class DownloadInvoiceRequest:
    invoice_id: str
    """
    Invoice ID.
    """

    file_type: DownloadInvoiceRequestFileType
    """
    Wanted file type.
    """
