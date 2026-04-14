# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

from scaleway_core.api import API
from scaleway_core.utils import (
    WaitForOptions,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
)
from .types import (
    DomainStatus,
    ListDomainsRequestOrderBy,
    ListMailboxesRequestOrderBy,
    MailboxStatus,
    MailboxSubscriptionPeriod,
    BatchCreateMailboxesRequest,
    BatchCreateMailboxesRequestMailboxParameters,
    BatchCreateMailboxesResponse,
    CreateDomainRequest,
    Domain,
    GetDomainRecordsResponse,
    ListDomainsResponse,
    ListMailboxesResponse,
    Mailbox,
    UpdateMailboxRequest,
)
from .content import (
    DOMAIN_TRANSIENT_STATUSES,
    MAILBOX_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Mailbox,
    unmarshal_Domain,
    unmarshal_BatchCreateMailboxesResponse,
    unmarshal_GetDomainRecordsResponse,
    unmarshal_ListDomainsResponse,
    unmarshal_ListMailboxesResponse,
    marshal_BatchCreateMailboxesRequest,
    marshal_CreateDomainRequest,
    marshal_UpdateMailboxRequest,
)


class MailboxV1Alpha1API(API):
    """
    This API allows you to manage your Mailbox services.
    """

    def create_domain(
        self,
        *,
        name: str,
        project_id: Optional[str] = None,
    ) -> Domain:
        """
        Register a domain in a project.
        You must specify a `project_id` and a `domain_name` to register a domain in a specific Project.
        :param name: Fully qualified domain name.
        :param project_id: ID of the project to which the domain belongs.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.create_domain(
                name="example",
            )
        """

        res = self._request(
            "POST",
            "/mailbox/v1alpha1/domains",
            body=marshal_CreateDomainRequest(
                CreateDomainRequest(
                    name=name,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def list_domains(
        self,
        *,
        order_by: Optional[ListDomainsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        statuses: Optional[list[DomainStatus]] = None,
        search: Optional[str] = None,
    ) -> ListDomainsResponse:
        """
        List domains in an organization.
        The return list can be filtered with request parameters.
        :param order_by:
        :param page:
        :param page_size:
        :param project_id:
        :param statuses:
        :param search:
        :return: :class:`ListDomainsResponse <ListDomainsResponse>`

        Usage:
        ::

            result = api.list_domains()
        """

        res = self._request(
            "GET",
            "/mailbox/v1alpha1/domains",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "search": search,
                "statuses": statuses,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDomainsResponse(res.json())

    def list_domains_all(
        self,
        *,
        order_by: Optional[ListDomainsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        statuses: Optional[list[DomainStatus]] = None,
        search: Optional[str] = None,
    ) -> list[Domain]:
        """
        List domains in an organization.
        The return list can be filtered with request parameters.
        :param order_by:
        :param page:
        :param page_size:
        :param project_id:
        :param statuses:
        :param search:
        :return: :class:`list[Domain] <list[Domain]>`

        Usage:
        ::

            result = api.list_domains_all()
        """

        return fetch_all_pages(
            type=ListDomainsResponse,
            key="domains",
            fetcher=self.list_domains,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "project_id": project_id or self.client.default_project_id,
                "statuses": statuses,
                "search": search,
            },
        )

    def get_domain(
        self,
        *,
        domain_id: str,
    ) -> Domain:
        """
        Get a domain by its ID.
        :param domain_id: ID of the domain to get.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.get_domain(
                domain_id="example",
            )
        """

        param_domain_id = validate_path_param("domain_id", domain_id)

        res = self._request(
            "GET",
            f"/mailbox/v1alpha1/domains/{param_domain_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def wait_for_domain(
        self,
        *,
        domain_id: str,
        options: Optional[WaitForOptions[Domain, bool]] = None,
    ) -> Domain:
        """
        Get a domain by its ID.
        :param domain_id: ID of the domain to get.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.get_domain(
                domain_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in DOMAIN_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_domain,
            options=options,
            args={
                "domain_id": domain_id,
            },
        )

    def delete_domain(
        self,
        *,
        domain_id: str,
    ) -> Domain:
        """
        Delete a domain by its ID.
        :param domain_id: ID of the domain to delete.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.delete_domain(
                domain_id="example",
            )
        """

        param_domain_id = validate_path_param("domain_id", domain_id)

        res = self._request(
            "DELETE",
            f"/mailbox/v1alpha1/domains/{param_domain_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    def get_domain_records(
        self,
        *,
        domain_id: str,
    ) -> GetDomainRecordsResponse:
        """
        Get domain records by its ID.
        :param domain_id: (Optional) ID of the domain in which to get the records.
        :return: :class:`GetDomainRecordsResponse <GetDomainRecordsResponse>`

        Usage:
        ::

            result = api.get_domain_records(
                domain_id="example",
            )
        """

        param_domain_id = validate_path_param("domain_id", domain_id)

        res = self._request(
            "GET",
            f"/mailbox/v1alpha1/domains/{param_domain_id}/records",
        )

        self._throw_on_error(res)
        return unmarshal_GetDomainRecordsResponse(res.json())

    def validate_domain_records(
        self,
        *,
        domain_id: str,
    ) -> None:
        """
        :param domain_id:

        Usage:
        ::

            result = api.validate_domain_records(
                domain_id="example",
            )
        """

        param_domain_id = validate_path_param("domain_id", domain_id)

        res = self._request(
            "POST",
            f"/mailbox/v1alpha1/domains/{param_domain_id}/validate-records",
            body={},
        )

        self._throw_on_error(res)

    def batch_create_mailboxes(
        self,
        *,
        domain_id: str,
        mailboxes: Optional[list[BatchCreateMailboxesRequestMailboxParameters]] = None,
        subscription_period: Optional[MailboxSubscriptionPeriod] = None,
    ) -> BatchCreateMailboxesResponse:
        """
        :param domain_id: ID of the domain in which to create the mailboxes.
        :param mailboxes: Parameters for the mailboxes to create.
        :param subscription_period: Subscription renewal period, it can be monthly or yearly.
        :return: :class:`BatchCreateMailboxesResponse <BatchCreateMailboxesResponse>`

        Usage:
        ::

            result = api.batch_create_mailboxes(
                domain_id="example",
            )
        """

        res = self._request(
            "POST",
            "/mailbox/v1alpha1/batch-create-mailboxes",
            body=marshal_BatchCreateMailboxesRequest(
                BatchCreateMailboxesRequest(
                    domain_id=domain_id,
                    mailboxes=mailboxes,
                    subscription_period=subscription_period,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_BatchCreateMailboxesResponse(res.json())

    def list_mailboxes(
        self,
        *,
        order_by: Optional[ListMailboxesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        domain_id: Optional[str] = None,
        statuses: Optional[list[MailboxStatus]] = None,
        search: Optional[str] = None,
    ) -> ListMailboxesResponse:
        """
        List mailboxes in an organization.
        The return list can be filtered with request parameters.
        :param order_by: Order matching mailbox by different criteria.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Requested page size. Value must be between 1 and 1000.
        :param domain_id: (Optional) ID of the domain in which to list the mailboxes.
        :param statuses: (Optional) Filter mailboxes by their statuses.
        :param search: (Optional) Search term to filter mailboxes on name and local_part.
        :return: :class:`ListMailboxesResponse <ListMailboxesResponse>`

        Usage:
        ::

            result = api.list_mailboxes()
        """

        res = self._request(
            "GET",
            "/mailbox/v1alpha1/mailboxes",
            params={
                "domain_id": domain_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "search": search,
                "statuses": statuses,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListMailboxesResponse(res.json())

    def list_mailboxes_all(
        self,
        *,
        order_by: Optional[ListMailboxesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        domain_id: Optional[str] = None,
        statuses: Optional[list[MailboxStatus]] = None,
        search: Optional[str] = None,
    ) -> list[Mailbox]:
        """
        List mailboxes in an organization.
        The return list can be filtered with request parameters.
        :param order_by: Order matching mailbox by different criteria.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Requested page size. Value must be between 1 and 1000.
        :param domain_id: (Optional) ID of the domain in which to list the mailboxes.
        :param statuses: (Optional) Filter mailboxes by their statuses.
        :param search: (Optional) Search term to filter mailboxes on name and local_part.
        :return: :class:`list[Mailbox] <list[Mailbox]>`

        Usage:
        ::

            result = api.list_mailboxes_all()
        """

        return fetch_all_pages(
            type=ListMailboxesResponse,
            key="mailboxes",
            fetcher=self.list_mailboxes,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "domain_id": domain_id,
                "statuses": statuses,
                "search": search,
            },
        )

    def get_mailbox(
        self,
        *,
        mailbox_id: str,
    ) -> Mailbox:
        """
        Get a mailbox by its ID.
        :param mailbox_id: ID of the mailbox to get.
        :return: :class:`Mailbox <Mailbox>`

        Usage:
        ::

            result = api.get_mailbox(
                mailbox_id="example",
            )
        """

        param_mailbox_id = validate_path_param("mailbox_id", mailbox_id)

        res = self._request(
            "GET",
            f"/mailbox/v1alpha1/mailboxes/{param_mailbox_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Mailbox(res.json())

    def wait_for_mailbox(
        self,
        *,
        mailbox_id: str,
        options: Optional[WaitForOptions[Mailbox, bool]] = None,
    ) -> Mailbox:
        """
        Get a mailbox by its ID.
        :param mailbox_id: ID of the mailbox to get.
        :return: :class:`Mailbox <Mailbox>`

        Usage:
        ::

            result = api.get_mailbox(
                mailbox_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in MAILBOX_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_mailbox,
            options=options,
            args={
                "mailbox_id": mailbox_id,
            },
        )

    def update_mailbox(
        self,
        *,
        mailbox_id: str,
        subscription_period: Optional[MailboxSubscriptionPeriod] = None,
        new_password: Optional[str] = None,
    ) -> Mailbox:
        """
        Update a mailbox subscription period or password with its ID.
        :param mailbox_id: ID of the mailbox to update.
        :param subscription_period: (Optional) New subscription period for the mailbox.
        :param new_password: (Optional) New password of the mailbox.
        :return: :class:`Mailbox <Mailbox>`

        Usage:
        ::

            result = api.update_mailbox(
                mailbox_id="example",
            )
        """

        param_mailbox_id = validate_path_param("mailbox_id", mailbox_id)

        res = self._request(
            "PATCH",
            f"/mailbox/v1alpha1/mailboxes/{param_mailbox_id}",
            body=marshal_UpdateMailboxRequest(
                UpdateMailboxRequest(
                    mailbox_id=mailbox_id,
                    subscription_period=subscription_period,
                    new_password=new_password,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Mailbox(res.json())

    def delete_mailbox(
        self,
        *,
        mailbox_id: str,
    ) -> Mailbox:
        """
        Delete a mailbox by its ID.
        :param mailbox_id: ID of the mailbox to delete.
        :return: :class:`Mailbox <Mailbox>`

        Usage:
        ::

            result = api.delete_mailbox(
                mailbox_id="example",
            )
        """

        param_mailbox_id = validate_path_param("mailbox_id", mailbox_id)

        res = self._request(
            "DELETE",
            f"/mailbox/v1alpha1/mailboxes/{param_mailbox_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Mailbox(res.json())

    def restore_mailbox(
        self,
        *,
        mailbox_id: str,
    ) -> Mailbox:
        """
        Restore a mailbox in deletion scheduled status by its ID.
        :param mailbox_id: ID of the mailbox to restore.
        :return: :class:`Mailbox <Mailbox>`

        Usage:
        ::

            result = api.restore_mailbox(
                mailbox_id="example",
            )
        """

        param_mailbox_id = validate_path_param("mailbox_id", mailbox_id)

        res = self._request(
            "POST",
            f"/mailbox/v1alpha1/mailboxes/{param_mailbox_id}/restore",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Mailbox(res.json())
