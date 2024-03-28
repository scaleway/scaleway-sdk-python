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
from scaleway_core.utils import (
    StrEnumMeta,
)


class DiscountDiscountMode(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_DISCOUNT_MODE = "unknown_discount_mode"
    DISCOUNT_MODE_RATE = "discount_mode_rate"
    DISCOUNT_MODE_VALUE = "discount_mode_value"
    DISCOUNT_MODE_SPLITTABLE = "discount_mode_splittable"

    def __str__(self) -> str:
        return str(self.value)


class DiscountFilterType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    PRODUCT_CATEGORY = "product_category"
    PRODUCT = "product"
    PRODUCT_OFFER = "product_offer"
    PRODUCT_REFERENCE = "product_reference"
    REGION = "region"
    ZONE = "zone"

    def __str__(self) -> str:
        return str(self.value)


class DownloadInvoiceRequestFileType(str, Enum, metaclass=StrEnumMeta):
    PDF = "pdf"

    def __str__(self) -> str:
        return str(self.value)


class InvoiceType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    PERIODIC = "periodic"
    PURCHASE = "purchase"

    def __str__(self) -> str:
        return str(self.value)


class ListDiscountsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATION_DATE_DESC = "creation_date_desc"
    CREATION_DATE_ASC = "creation_date_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListInvoicesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
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
class DiscountCoupon:
    description: Optional[str]
    """
    The description of the coupon.
    """


@dataclass
class DiscountFilter:
    type_: DiscountFilterType
    """
    Type of the filter.
    """

    value: str
    """
    Value of filter, it can be a product/range/region/zone value.
    """


@dataclass
class GetConsumptionResponseConsumption:
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

    value: Optional[Money]
    """
    Monetary value of the consumption.
    """


@dataclass
class Discount:
    id: str
    """
    The ID of the discount.
    """

    organization_id: str
    """
    The organization ID of the discount.
    """

    description: str
    """
    The description of the discount.
    """

    value: float
    """
    The initial value of the discount.
    """

    value_used: float
    """
    The value indicating how much of the discount has been used.
    """

    value_remaining: float
    """
    The remaining value of the discount.
    """

    mode: DiscountDiscountMode
    """
    The mode of the discount.
    """

    filters: List[DiscountFilter]
    """
    List of products/ranges/regions/zones to limit the usability of discounts.
    """

    creation_date: Optional[datetime]
    """
    The creation date of the discount.
    """

    start_date: Optional[datetime]
    """
    The start date of the discount.
    """

    stop_date: Optional[datetime]
    """
    The stop date of the discount.
    """

    coupon: Optional[DiscountCoupon]
    """
    The description of the coupon.
    """


@dataclass
class Invoice:
    id: str
    """
    Invoice ID.
    """

    invoice_type: InvoiceType
    """
    Type of invoice.
    """

    number: int
    """
    Invoice number.
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


@dataclass
class DownloadInvoiceRequest:
    invoice_id: str
    """
    Invoice ID.
    """

    file_type: Optional[DownloadInvoiceRequestFileType]
    """
    Wanted file type.
    """


@dataclass
class GetConsumptionRequest:
    organization_id: Optional[str]
    """
    Filter by organization ID.
    """


@dataclass
class GetConsumptionResponse:
    consumptions: List[GetConsumptionResponseConsumption]
    """
    Detailed consumption list.
    """

    updated_at: Optional[datetime]
    """
    Last consumption update date.
    """


@dataclass
class ListDiscountsRequest:
    order_by: Optional[ListDiscountsRequestOrderBy]
    """
    Order discounts in the response by their description.
    """

    page: Optional[int]
    """
    Positive integer to choose the page to return.
    """

    page_size: Optional[int]
    """
    Positive integer lower or equal to 100 to select the number of items to return.
    """

    organization_id: Optional[str]
    """
    ID of the organization.
    """


@dataclass
class ListDiscountsResponse:
    total_count: int
    """
    Total number of discounts.
    """

    discounts: List[Discount]
    """
    Paginated returned discounts.
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
class ListInvoicesResponse:
    total_count: int
    """
    Total number of invoices.
    """

    invoices: List[Invoice]
    """
    Paginated returned invoices.
    """
