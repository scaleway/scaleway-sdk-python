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
    CATEGORY_NAME = "category_name"
    PRODUCT_NAME = "product_name"
    PRODUCT_RANGE = "product_range"
    RESOURCE_NAME = "resource_name"
    REGION = "region"
    ZONE = "zone"

    def __str__(self) -> str:
        return str(self.value)


class DownloadInvoiceRequestFileType(str, Enum, metaclass=StrEnumMeta):
    PDF = "pdf"

    def __str__(self) -> str:
        return str(self.value)


class ExportInvoicesRequestFileType(str, Enum, metaclass=StrEnumMeta):
    CSV = "csv"

    def __str__(self) -> str:
        return str(self.value)


class ExportInvoicesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
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


class InvoiceType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    PERIODIC = "periodic"
    PURCHASE = "purchase"

    def __str__(self) -> str:
        return str(self.value)


class ListConsumptionsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    UPDATED_AT_DESC = "updated_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    CATEGORY_NAME_DESC = "category_name_desc"
    CATEGORY_NAME_ASC = "category_name_asc"

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


class ListTaxesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    UPDATED_AT_DESC = "updated_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    CATEGORY_NAME_DESC = "category_name_desc"
    CATEGORY_NAME_ASC = "category_name_asc"

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
    Type of the filter (category name, product name, product range, resource name, region or zone).
    """

    value: str
    """
    Value of filter.
    """


@dataclass
class ListConsumptionsResponseConsumption:
    product_name: str
    """
    The product name. For example, "VPC Public Gateway S", "VPC Public Gateway M" for the VPC product.
    """

    resource_name: str
    """
    Identifies the reference based on the category.
    """

    sku: str
    """
    Unique identifier of the product.
    """

    project_id: str
    """
    Project ID of the consumption.
    """

    category_name: str
    """
    Name of consumption category.
    """

    unit: str
    """
    Unit of consumed quantity.
    """

    billed_quantity: str
    """
    Consumed quantity.
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
    List of the discount scopes.
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

    organization_id: str

    organization_name: str

    start_date: Optional[datetime]
    """
    Start date of the billing period.
    """

    stop_date: Optional[datetime]

    billing_period: Optional[datetime]
    """
    The billing period of the invoice in the YYYY-MM format.
    """

    issued_date: Optional[datetime]
    """
    Date when the invoice was sent to the customer.
    """

    due_date: Optional[datetime]
    """
    Payment time limit, set according to the Organization's payment conditions.
    """

    type_: InvoiceType
    """
    Type of invoice, either periodic or purchase.
    """

    state: str
    """
    The state of the Invoice.
    """

    number: int
    """
    Invoice number.
    """

    seller_name: str
    """
    The name of the seller (Scaleway).
    """

    total_untaxed: Optional[Money]
    """
    Total amount, untaxed.
    """

    total_taxed: Optional[Money]
    """
    Total amount, taxed.
    """

    total_tax: Optional[Money]
    """
    The total tax amount of the invoice.
    """

    total_discount: Optional[Money]
    """
    The total discount amount of the invoice.
    """

    total_undiscount: Optional[Money]
    """
    The total amount of the invoice before applying the discount.
    """


@dataclass
class ListTaxesResponseTax:
    description: str
    """
    Description of the tax applied.
    """

    currency: str
    """
    The three-letter currency code.
    """

    rate: Optional[float]
    """
    Applied tax rate (0.2 means a VAT of 20%).
    """

    total_tax_value: Optional[float]
    """
    The total tax value of the consumption.
    """


@dataclass
class DownloadInvoiceRequest:
    invoice_id: str
    """
    Invoice ID.
    """

    file_type: Optional[DownloadInvoiceRequestFileType]
    """
    File type. PDF by default.
    """


@dataclass
class ExportInvoicesRequest:
    organization_id: Optional[str]
    """
    Organization ID. If specified, only invoices from this Organization will be returned.
    """

    billing_period_start_after: Optional[datetime]
    """
    Return only invoice with start date greater than billing_period_start.
    """

    billing_period_start_before: Optional[datetime]
    """
    Return only invoice with start date less than billing_period_start.
    """

    invoice_type: Optional[InvoiceType]
    """
    Invoice type. It can either be `periodic` or `purchase`.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Positive integer lower or equal to 100 to select the number of items to return.
    """

    order_by: Optional[ExportInvoicesRequestOrderBy]
    """
    How invoices are ordered in the response.
    """

    file_type: Optional[ExportInvoicesRequestFileType]
    """
    File format for exporting the invoice list.
    """


@dataclass
class GetInvoiceRequest:
    invoice_id: str
    """
    Invoice ID.
    """


@dataclass
class ListConsumptionsRequest:
    order_by: Optional[ListConsumptionsRequestOrderBy]
    """
    Order consumptions list in the response by their update date.
    """

    page: Optional[int]
    """
    Positive integer to choose the page to return.
    """

    page_size: Optional[int]
    """
    Positive integer lower or equal to 100 to select the number of items to return.
    """

    category_name: Optional[str]
    """
    Filter by name of a Category as they are shown in the invoice (Compute, Network, Observability).
    """

    billing_period: Optional[str]
    """
    Filter by the billing period in the YYYY-MM format. If it is empty the current billing period will be used as default.
    """

    organization_id: Optional[str]

    project_id: Optional[str]


@dataclass
class ListConsumptionsResponse:
    consumptions: List[ListConsumptionsResponseConsumption]
    """
    Detailed consumption list.
    """

    total_count: int
    """
    Total number of returned items.
    """

    total_discount_untaxed_value: float
    """
    Sum of all discounts, displayed only when no category or project ID filter is applied.
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
    Organization ID. If specified, only invoices from this Organization will be returned.
    """

    billing_period_start_after: Optional[datetime]
    """
    Return only invoice with start date greater than billing_period_start.
    """

    billing_period_start_before: Optional[datetime]
    """
    Return only invoice with start date less than billing_period_start.
    """

    invoice_type: Optional[InvoiceType]
    """
    Invoice type. It can either be `periodic` or `purchase`.
    """

    page: Optional[int]
    """
    Page number.
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


@dataclass
class ListTaxesRequest:
    order_by: Optional[ListTaxesRequestOrderBy]
    """
    Order consumed taxes list in the response by their update date.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Positive integer lower or equal to 100 to select the number of items to return.
    """

    organization_id: Optional[str]
    """
    Filter by Organization ID.
    """

    billing_period: Optional[str]
    """
    Filter by the billing period in the YYYY-MM format. If it is empty the current billing period will be used as default.
    """


@dataclass
class ListTaxesResponse:
    taxes: List[ListTaxesResponseTax]
    """
    Detailed consumption tax.
    """

    total_count: int
    """
    Total number of returned items.
    """

    updated_at: Optional[datetime]
    """
    Last consumption update date.
    """
