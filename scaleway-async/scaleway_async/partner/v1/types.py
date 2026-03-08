# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.utils import (
    StrEnumMeta,
)


class ListOrganizationsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class OrganizationLockedBy(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_LOCKED_BY = "unknown_locked_by"
    PARTNER = "partner"
    SCALEWAY = "scaleway"

    def __str__(self) -> str:
        return str(self.value)


class OrganizationStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    OPENED = "opened"
    LOCKED = "locked"
    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Organization:
    id: str
    """
    ID of the organization.
    """

    name: str
    """
    Name of the organization.
    """

    email: str
    """
    Organization owner's email.
    """

    status: OrganizationStatus
    """
    The current status of the organization.
    """

    owner_firstname: str
    """
    Organization owner's first name.
    """

    owner_lastname: str
    """
    Organization owner's last name.
    """

    customer_id: str
    """
    Customer ID associated with this organization.
    """

    lock_reason_message: str
    """
    If the organization is locked, this field will contain a human-readable reason.
    """

    locked_by: OrganizationLockedBy
    """
    Originator of the lock. Can be one of "partner" or "scaleway".
    """

    comment: str
    """
    A comment about the organization.
    """

    created_at: Optional[datetime] = None
    """
    Date of organization creation.
    """

    phone_number: Optional[str] = None
    """
    Organization owner's phone number.
    """

    siren_number: Optional[str] = None
    """
    Siren number of the organization.
    """

    locked_at: Optional[datetime] = None
    """
    Date of lock.
    """

    picture_link: Optional[str] = None
    """
    Link to the Organization's picture.
    """


@dataclass
class CreateOrganizationRequest:
    partner_id: str
    """
    Your personal `partner_id`. This is the same as your Organization ID.
    """

    email: str
    """
    The email of the new organization owner.
    """

    organization_name: str
    """
    The name of the organization you want to create. Usually the company name.
    """

    owner_firstname: str
    """
    The first name of the new organization owner.
    """

    owner_lastname: str
    """
    The last name of the new organization owner.
    """

    customer_id: str
    """
    A custom ID for the customer in your own infrastructure.
    """

    phone_number: Optional[str] = None
    """
    The phone number of the new organization owner.
    """

    siren_number: Optional[str] = None
    """
    A SIREN number for the customer.
    """


@dataclass
class GetOrganizationRequest:
    organization_id: Optional[str] = None
    """
    The ID of the organization you want to GET.
    """


@dataclass
class ListOrganizationsRequest:
    page_size: Optional[int] = 0
    page: Optional[int] = 0
    order_by: Optional[ListOrganizationsRequestOrderBy] = (
        ListOrganizationsRequestOrderBy.CREATED_AT_ASC
    )
    status: Optional[OrganizationStatus] = OrganizationStatus.UNKNOWN_STATUS
    """
    Only list organizations with this status.
    """

    email: Optional[str] = None
    """
    Only list organizations created with this email.
    """

    customer_id: Optional[str] = None
    """
    Only list organizations attached to this Customer ID.
If the customer ID was changed only the last one can be used.
    """

    locked_by: Optional[OrganizationLockedBy] = OrganizationLockedBy.UNKNOWN_LOCKED_BY
    """
    Only list organizations locked by a certain entity.
    """


@dataclass
class ListOrganizationsResponse:
    organizations: list[Organization]
    """
    List of organizations.
    """

    total_count: int
    """
    Total number of organizations.
    """


@dataclass
class LockOrganizationRequest:
    organization_id: Optional[str] = None
    """
    The ID of the organization you want to lock.
    """


@dataclass
class RequestAdminRoleRequest:
    username: str
    """
    The member username.
    """

    email: str
    """
    The member email.
    """

    password: str
    """
    The member password.
    """

    organization_id: Optional[str] = None
    """
    The ID of the organization you want to be invited to.
    """


@dataclass
class UnlockOrganizationRequest:
    organization_id: Optional[str] = None
    """
    The ID of the organization you want to unlock.
    """


@dataclass
class UpdateOrganizationRequest:
    organization_id: Optional[str] = None
    """
    The ID of the organization you want to update.
    """

    email: Optional[str] = None
    """
    The new email.
    """

    name: Optional[str] = None
    """
    The new name.
    """

    owner_firstname: Optional[str] = None
    """
    The first name of the new owner.
    """

    owner_lastname: Optional[str] = None
    """
    The last name of the new owner.
    """

    phone_number: Optional[str] = None
    """
    The phone number of the new owner.
    """

    customer_id: Optional[str] = None
    """
    Customer ID associated with this organization.
Warning: Changing this value will only affect future invoices.
If you try to change this value after the 25th of the month, we cannot guarantee that this will take effect on the invoice issued for the current month.
    """

    comment: Optional[str] = None
    """
    A comment about the organization.
    """
