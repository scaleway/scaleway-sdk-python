# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

from scaleway_core.api import API
from scaleway_core.utils import (
    validate_path_param,
    fetch_all_pages,
)
from .types import (
    ListOrganizationsRequestOrderBy,
    OrganizationLockedBy,
    OrganizationStatus,
    CreateOrganizationRequest,
    ListOrganizationsResponse,
    Organization,
    RequestAdminRoleRequest,
    UpdateOrganizationRequest,
)
from .marshalling import (
    unmarshal_Organization,
    unmarshal_ListOrganizationsResponse,
    marshal_CreateOrganizationRequest,
    marshal_RequestAdminRoleRequest,
    marshal_UpdateOrganizationRequest,
)


class PartnerV1API(API):
    """
    Scaleway Partner API ( for partner only ).
    """

    def request_admin_role(
        self,
        *,
        username: str,
        email: str,
        password: str,
        organization_id: Optional[str] = None,
    ) -> None:
        """
        Invite a partner user in the customer organization.
        :param username: The member username.
        :param email: The member email.
        :param password: The member password.
        :param organization_id: The ID of the organization you want to be invited to.

        Usage:
        ::

            result = api.request_admin_role(
                username="example",
                email="example",
                password="example",
            )
        """

        param_organization_id = validate_path_param(
            "organization_id", organization_id or self.client.default_organization_id
        )

        res = self._request(
            "POST",
            f"/partner/v1/organizations/{param_organization_id}/request-admin-role",
            body=marshal_RequestAdminRoleRequest(
                RequestAdminRoleRequest(
                    username=username,
                    email=email,
                    password=password,
                    organization_id=organization_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    def create_organization(
        self,
        *,
        partner_id: str,
        email: str,
        organization_name: str,
        owner_firstname: str,
        owner_lastname: str,
        customer_id: str,
        phone_number: Optional[str] = None,
        siren_number: Optional[str] = None,
    ) -> Organization:
        """
        Create a new organization.
        :param partner_id: Your personal `partner_id`. This is the same as your Organization ID.
        :param email: The email of the new organization owner.
        :param organization_name: The name of the organization you want to create. Usually the company name.
        :param owner_firstname: The first name of the new organization owner.
        :param owner_lastname: The last name of the new organization owner.
        :param customer_id: A custom ID for the customer in your own infrastructure.
        :param phone_number: The phone number of the new organization owner.
        :param siren_number: A SIREN number for the customer.
        :return: :class:`Organization <Organization>`

        Usage:
        ::

            result = api.create_organization(
                partner_id="example",
                email="example",
                organization_name="example",
                owner_firstname="example",
                owner_lastname="example",
                customer_id="example",
            )
        """

        res = self._request(
            "POST",
            "/partner/v1/organizations",
            body=marshal_CreateOrganizationRequest(
                CreateOrganizationRequest(
                    partner_id=partner_id,
                    email=email,
                    organization_name=organization_name,
                    owner_firstname=owner_firstname,
                    owner_lastname=owner_lastname,
                    customer_id=customer_id,
                    phone_number=phone_number,
                    siren_number=siren_number,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Organization(res.json())

    def get_organization(
        self,
        *,
        organization_id: Optional[str] = None,
    ) -> Organization:
        """
        Get an organization.
        :param organization_id: The ID of the organization you want to GET.
        :return: :class:`Organization <Organization>`

        Usage:
        ::

            result = api.get_organization()
        """

        param_organization_id = validate_path_param(
            "organization_id", organization_id or self.client.default_organization_id
        )

        res = self._request(
            "GET",
            f"/partner/v1/organizations/{param_organization_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Organization(res.json())

    def list_organizations(
        self,
        *,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        order_by: Optional[ListOrganizationsRequestOrderBy] = None,
        status: Optional[OrganizationStatus] = None,
        email: Optional[str] = None,
        customer_id: Optional[str] = None,
        locked_by: Optional[OrganizationLockedBy] = None,
    ) -> ListOrganizationsResponse:
        """
        List Organizations.
        :param page_size:
        :param page:
        :param order_by:
        :param status: Only list organizations with this status.
        :param email: Only list organizations created with this email.
        :param customer_id: Only list organizations attached to this Customer ID.
        If the customer ID was changed only the last one can be used.
        :param locked_by: Only list organizations locked by a certain entity.
        :return: :class:`ListOrganizationsResponse <ListOrganizationsResponse>`

        Usage:
        ::

            result = api.list_organizations()
        """

        res = self._request(
            "GET",
            "/partner/v1/organizations",
            params={
                "customer_id": customer_id,
                "email": email,
                "locked_by": locked_by,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "status": status,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListOrganizationsResponse(res.json())

    def list_organizations_all(
        self,
        *,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        order_by: Optional[ListOrganizationsRequestOrderBy] = None,
        status: Optional[OrganizationStatus] = None,
        email: Optional[str] = None,
        customer_id: Optional[str] = None,
        locked_by: Optional[OrganizationLockedBy] = None,
    ) -> list[Organization]:
        """
        List Organizations.
        :param page_size:
        :param page:
        :param order_by:
        :param status: Only list organizations with this status.
        :param email: Only list organizations created with this email.
        :param customer_id: Only list organizations attached to this Customer ID.
        If the customer ID was changed only the last one can be used.
        :param locked_by: Only list organizations locked by a certain entity.
        :return: :class:`list[Organization] <list[Organization]>`

        Usage:
        ::

            result = api.list_organizations_all()
        """

        return fetch_all_pages(
            type=ListOrganizationsResponse,
            key="organizations",
            fetcher=self.list_organizations,
            args={
                "page_size": page_size,
                "page": page,
                "order_by": order_by,
                "status": status,
                "email": email,
                "customer_id": customer_id,
                "locked_by": locked_by,
            },
        )

    def lock_organization(
        self,
        *,
        organization_id: Optional[str] = None,
    ) -> Organization:
        """
        Lock an organization.
        :param organization_id: The ID of the organization you want to lock.
        :return: :class:`Organization <Organization>`

        Usage:
        ::

            result = api.lock_organization()
        """

        param_organization_id = validate_path_param(
            "organization_id", organization_id or self.client.default_organization_id
        )

        res = self._request(
            "POST",
            f"/partner/v1/organizations/{param_organization_id}/lock",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Organization(res.json())

    def unlock_organization(
        self,
        *,
        organization_id: Optional[str] = None,
    ) -> Organization:
        """
        Unlock an organization.
        :param organization_id: The ID of the organization you want to unlock.
        :return: :class:`Organization <Organization>`

        Usage:
        ::

            result = api.unlock_organization()
        """

        param_organization_id = validate_path_param(
            "organization_id", organization_id or self.client.default_organization_id
        )

        res = self._request(
            "POST",
            f"/partner/v1/organizations/{param_organization_id}/unlock",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Organization(res.json())

    def update_organization(
        self,
        *,
        organization_id: Optional[str] = None,
        email: Optional[str] = None,
        name: Optional[str] = None,
        owner_firstname: Optional[str] = None,
        owner_lastname: Optional[str] = None,
        phone_number: Optional[str] = None,
        customer_id: Optional[str] = None,
        comment: Optional[str] = None,
    ) -> Organization:
        """
        Update an organization.
        :param organization_id: The ID of the organization you want to update.
        :param email: The new email.
        :param name: The new name.
        :param owner_firstname: The first name of the new owner.
        :param owner_lastname: The last name of the new owner.
        :param phone_number: The phone number of the new owner.
        :param customer_id: Customer ID associated with this organization.
        Warning: Changing this value will only affect future invoices.
        If you try to change this value after the 25th of the month, we cannot guarantee that this will take effect on the invoice issued for the current month.
        :param comment: A comment about the organization.
        :return: :class:`Organization <Organization>`

        Usage:
        ::

            result = api.update_organization()
        """

        param_organization_id = validate_path_param(
            "organization_id", organization_id or self.client.default_organization_id
        )

        res = self._request(
            "PATCH",
            f"/partner/v1/organizations/{param_organization_id}",
            body=marshal_UpdateOrganizationRequest(
                UpdateOrganizationRequest(
                    organization_id=organization_id,
                    email=email,
                    name=name,
                    owner_firstname=owner_firstname,
                    owner_lastname=owner_lastname,
                    phone_number=phone_number,
                    customer_id=customer_id,
                    comment=comment,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Organization(res.json())
