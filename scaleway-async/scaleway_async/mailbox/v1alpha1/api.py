# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, Optional, Union

from scaleway_core.api import API
from scaleway_core.utils import (
    OneOfPossibility,
    WaitForOptions,
    resolve_one_of,
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    AliasStatus,
    DomainStatus,
    ForwardingStatus,
    ListAliasesRequestOrderBy,
    ListDomainsRequestOrderBy,
    ListForwardingsRequestOrderBy,
    ListMailboxesRequestOrderBy,
    MailboxStatus,
    MailboxSubscriptionPeriod,
    Alias,
    BatchCreateMailboxesRequest,
    BatchCreateMailboxesRequestMailboxParameters,
    BatchCreateMailboxesResponse,
    CreateAliasRequest,
    CreateDomainRequest,
    CreateForwardingRequest,
    Domain,
    Forwarding,
    GetDomainRecordsResponse,
    ListAliasesResponse,
    ListDomainsResponse,
    ListForwardingsResponse,
    ListMailboxesResponse,
    Mailbox,
    MailboxForwarding,
    UpdateAliasRequest,
    UpdateForwardingRequest,
    UpdateMailboxForwardingRequest,
    UpdateMailboxRequest,
)
from .content import (
    ALIAS_TRANSIENT_STATUSES,
    DOMAIN_TRANSIENT_STATUSES,
    FORWARDING_TRANSIENT_STATUSES,
    MAILBOX_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Mailbox,
    unmarshal_Alias,
    unmarshal_Domain,
    unmarshal_Forwarding,
    unmarshal_BatchCreateMailboxesResponse,
    unmarshal_GetDomainRecordsResponse,
    unmarshal_ListAliasesResponse,
    unmarshal_ListDomainsResponse,
    unmarshal_ListForwardingsResponse,
    unmarshal_ListMailboxesResponse,
    unmarshal_MailboxForwarding,
    marshal_BatchCreateMailboxesRequest,
    marshal_CreateAliasRequest,
    marshal_CreateDomainRequest,
    marshal_CreateForwardingRequest,
    marshal_UpdateAliasRequest,
    marshal_UpdateForwardingRequest,
    marshal_UpdateMailboxForwardingRequest,
    marshal_UpdateMailboxRequest,
)


class MailboxV1Alpha1API(API):
    """
    This API allows you to manage your Mailbox services.
    """

    async def create_domain(
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

            result = await api.create_domain(
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

    async def list_domains(
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

            result = await api.list_domains()
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

    async def list_domains_all(
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

            result = await api.list_domains_all()
        """

        return await fetch_all_pages_async(
            type=ListDomainsResponse,
            key="domains",
            fetcher=self.list_domains,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "project_id": project_id,
                "statuses": statuses,
                "search": search,
            },
        )

    async def get_domain(
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

            result = await api.get_domain(
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

    async def wait_for_domain(
        self,
        *,
        domain_id: str,
        options: Optional[WaitForOptions[Domain, Union[bool, Awaitable[bool]]]] = None,
    ) -> Domain:
        """
        Get a domain by its ID.
        :param domain_id: ID of the domain to get.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = await api.get_domain(
                domain_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in DOMAIN_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_domain,
            options=options,
            args={
                "domain_id": domain_id,
            },
        )

    async def delete_domain(
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

            result = await api.delete_domain(
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

    async def get_domain_records(
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

            result = await api.get_domain_records(
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

    async def validate_domain_records(
        self,
        *,
        domain_id: str,
    ) -> None:
        """
        Validate domain records by its ID.
        :param domain_id: ID of the domain with which to validate the records.

        Usage:
        ::

            result = await api.validate_domain_records(
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

    async def batch_create_mailboxes(
        self,
        *,
        domain_id: str,
        mailboxes: Optional[list[BatchCreateMailboxesRequestMailboxParameters]] = None,
        subscription_period: Optional[MailboxSubscriptionPeriod] = None,
    ) -> BatchCreateMailboxesResponse:
        """
        Create one or more mailboxes.
        :param domain_id: ID of the domain in which to create the mailboxes.
        :param mailboxes: Parameters for the mailboxes to create.
        :param subscription_period: Subscription renewal period, it can be monthly or yearly.
        :return: :class:`BatchCreateMailboxesResponse <BatchCreateMailboxesResponse>`

        Usage:
        ::

            result = await api.batch_create_mailboxes(
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

    async def list_mailboxes(
        self,
        *,
        order_by: Optional[ListMailboxesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        domain_id: Optional[str] = None,
        statuses: Optional[list[MailboxStatus]] = None,
        search: Optional[str] = None,
        project_id: Optional[str] = None,
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
        :param project_id: (Optional) Project ID to filter mailboxes on.
        :return: :class:`ListMailboxesResponse <ListMailboxesResponse>`

        Usage:
        ::

            result = await api.list_mailboxes()
        """

        res = self._request(
            "GET",
            "/mailbox/v1alpha1/mailboxes",
            params={
                "domain_id": domain_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "search": search,
                "statuses": statuses,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListMailboxesResponse(res.json())

    async def list_mailboxes_all(
        self,
        *,
        order_by: Optional[ListMailboxesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        domain_id: Optional[str] = None,
        statuses: Optional[list[MailboxStatus]] = None,
        search: Optional[str] = None,
        project_id: Optional[str] = None,
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
        :param project_id: (Optional) Project ID to filter mailboxes on.
        :return: :class:`list[Mailbox] <list[Mailbox]>`

        Usage:
        ::

            result = await api.list_mailboxes_all()
        """

        return await fetch_all_pages_async(
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
                "project_id": project_id,
            },
        )

    async def get_mailbox(
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

            result = await api.get_mailbox(
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

    async def wait_for_mailbox(
        self,
        *,
        mailbox_id: str,
        options: Optional[WaitForOptions[Mailbox, Union[bool, Awaitable[bool]]]] = None,
    ) -> Mailbox:
        """
        Get a mailbox by its ID.
        :param mailbox_id: ID of the mailbox to get.
        :return: :class:`Mailbox <Mailbox>`

        Usage:
        ::

            result = await api.get_mailbox(
                mailbox_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in MAILBOX_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_mailbox,
            options=options,
            args={
                "mailbox_id": mailbox_id,
            },
        )

    async def update_mailbox(
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

            result = await api.update_mailbox(
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

    async def delete_mailbox(
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

            result = await api.delete_mailbox(
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

    async def restore_mailbox(
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

            result = await api.restore_mailbox(
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

    async def create_alias(
        self,
        *,
        local_part: str,
        mailbox_id: str,
        description: Optional[str] = None,
    ) -> Alias:
        """
        Create an alias for a mailbox.
        :param local_part: Local part of the email address (e.g. local_part@domain.com).
        :param mailbox_id: ID of the mailbox to associate with the alias.
        :param description: (Optional) Description of the alias.
        :return: :class:`Alias <Alias>`

        Usage:
        ::

            result = await api.create_alias(
                local_part="example",
                mailbox_id="example",
            )
        """

        res = self._request(
            "POST",
            "/mailbox/v1alpha1/aliases",
            body=marshal_CreateAliasRequest(
                CreateAliasRequest(
                    local_part=local_part,
                    mailbox_id=mailbox_id,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Alias(res.json())

    async def list_aliases(
        self,
        *,
        order_by: Optional[ListAliasesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        mailbox_id: Optional[str] = None,
        status: Optional[AliasStatus] = None,
        project_id: Optional[str] = None,
    ) -> ListAliasesResponse:
        """
        List aliases for a mailbox.
        :param order_by: Order aliases by specific criteria.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Requested page size. Value must be between 1 and 100.
        :param mailbox_id: ID of the mailbox for which to list aliases.
        :param status: (Optional) Filter aliases by their status.
        :param project_id: Project ID to filter on.
        :return: :class:`ListAliasesResponse <ListAliasesResponse>`

        Usage:
        ::

            result = await api.list_aliases()
        """

        res = self._request(
            "GET",
            "/mailbox/v1alpha1/aliases",
            params={
                "mailbox_id": mailbox_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "status": status,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListAliasesResponse(res.json())

    async def list_aliases_all(
        self,
        *,
        order_by: Optional[ListAliasesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        mailbox_id: Optional[str] = None,
        status: Optional[AliasStatus] = None,
        project_id: Optional[str] = None,
    ) -> list[Alias]:
        """
        List aliases for a mailbox.
        :param order_by: Order aliases by specific criteria.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Requested page size. Value must be between 1 and 100.
        :param mailbox_id: ID of the mailbox for which to list aliases.
        :param status: (Optional) Filter aliases by their status.
        :param project_id: Project ID to filter on.
        :return: :class:`list[Alias] <list[Alias]>`

        Usage:
        ::

            result = await api.list_aliases_all()
        """

        return await fetch_all_pages_async(
            type=ListAliasesResponse,
            key="aliases",
            fetcher=self.list_aliases,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "mailbox_id": mailbox_id,
                "status": status,
                "project_id": project_id,
            },
        )

    async def get_alias(
        self,
        *,
        alias_id: str,
    ) -> Alias:
        """
        Get an alias by its ID.
        :param alias_id: ID of the alias to get.
        :return: :class:`Alias <Alias>`

        Usage:
        ::

            result = await api.get_alias(
                alias_id="example",
            )
        """

        param_alias_id = validate_path_param("alias_id", alias_id)

        res = self._request(
            "GET",
            f"/mailbox/v1alpha1/aliases/{param_alias_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Alias(res.json())

    async def wait_for_alias(
        self,
        *,
        alias_id: str,
        options: Optional[WaitForOptions[Alias, Union[bool, Awaitable[bool]]]] = None,
    ) -> Alias:
        """
        Get an alias by its ID.
        :param alias_id: ID of the alias to get.
        :return: :class:`Alias <Alias>`

        Usage:
        ::

            result = await api.get_alias(
                alias_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in ALIAS_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_alias,
            options=options,
            args={
                "alias_id": alias_id,
            },
        )

    async def update_alias(
        self,
        *,
        alias_id: str,
        description: Optional[str] = None,
    ) -> Alias:
        """
        Update an alias by its ID.
        :param alias_id: ID of the alias to update.
        :param description: (Optional) Description of the alias.
        :return: :class:`Alias <Alias>`

        Usage:
        ::

            result = await api.update_alias(
                alias_id="example",
            )
        """

        param_alias_id = validate_path_param("alias_id", alias_id)

        res = self._request(
            "PATCH",
            f"/mailbox/v1alpha1/aliases/{param_alias_id}",
            body=marshal_UpdateAliasRequest(
                UpdateAliasRequest(
                    alias_id=alias_id,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Alias(res.json())

    async def delete_alias(
        self,
        *,
        alias_id: str,
    ) -> Alias:
        """
        Delete an alias by its ID.
        :param alias_id: ID of the alias to delete.
        :return: :class:`Alias <Alias>`

        Usage:
        ::

            result = await api.delete_alias(
                alias_id="example",
            )
        """

        param_alias_id = validate_path_param("alias_id", alias_id)

        res = self._request(
            "DELETE",
            f"/mailbox/v1alpha1/aliases/{param_alias_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Alias(res.json())

    async def create_forwarding(
        self,
        *,
        mailbox_id: str,
        email: str,
    ) -> Forwarding:
        """
        Create a forwarding rule for a mailbox.
        All incoming emails to the mailbox will be redirected to the specified destination email address.
        A mailbox can have up to 5 forwarding rules. Forwarding to the mailbox's own email address is not allowed.
        :param mailbox_id: ID of the mailbox for which to create the forwarding rule.
        :param email: Destination email address to which incoming emails will be forwarded. Must not be the same as the mailbox's own email address.
        :return: :class:`Forwarding <Forwarding>`

        Usage:
        ::

            result = await api.create_forwarding(
                mailbox_id="example",
                email="example",
            )
        """

        res = self._request(
            "POST",
            "/mailbox/v1alpha1/forwardings",
            body=marshal_CreateForwardingRequest(
                CreateForwardingRequest(
                    mailbox_id=mailbox_id,
                    email=email,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Forwarding(res.json())

    async def list_forwardings(
        self,
        *,
        order_by: Optional[ListForwardingsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        mailbox_id: Optional[str] = None,
        status: Optional[ForwardingStatus] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
    ) -> ListForwardingsResponse:
        """
        List forwarding rules in an organization.
        The return list can be filtered with request parameters.
        :param order_by: Order forwardings by specific criteria.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Requested page size. Value must be between 1 and 100.
        :param mailbox_id: (Optional) ID of the mailbox for which to list forwarding rules.
        :param status: (Optional) Filter forwarding rules by their status.
        :param project_id: ID of the Project to filter on.
        One-Of ('scope'): at most one of 'project_id', 'organization_id' could be set.
        :param organization_id: ID of the Organization to filter on.
        One-Of ('scope'): at most one of 'project_id', 'organization_id' could be set.
        :return: :class:`ListForwardingsResponse <ListForwardingsResponse>`

        Usage:
        ::

            result = await api.list_forwardings()
        """

        res = self._request(
            "GET",
            "/mailbox/v1alpha1/forwardings",
            params={
                "mailbox_id": mailbox_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "status": status,
                **resolve_one_of(
                    [
                        OneOfPossibility("organization_id", organization_id),
                        OneOfPossibility("project_id", project_id),
                    ]
                ),
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListForwardingsResponse(res.json())

    async def list_forwardings_all(
        self,
        *,
        order_by: Optional[ListForwardingsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        mailbox_id: Optional[str] = None,
        status: Optional[ForwardingStatus] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
    ) -> list[Forwarding]:
        """
        List forwarding rules in an organization.
        The return list can be filtered with request parameters.
        :param order_by: Order forwardings by specific criteria.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Requested page size. Value must be between 1 and 100.
        :param mailbox_id: (Optional) ID of the mailbox for which to list forwarding rules.
        :param status: (Optional) Filter forwarding rules by their status.
        :param project_id: ID of the Project to filter on.
        One-Of ('scope'): at most one of 'project_id', 'organization_id' could be set.
        :param organization_id: ID of the Organization to filter on.
        One-Of ('scope'): at most one of 'project_id', 'organization_id' could be set.
        :return: :class:`list[Forwarding] <list[Forwarding]>`

        Usage:
        ::

            result = await api.list_forwardings_all()
        """

        return await fetch_all_pages_async(
            type=ListForwardingsResponse,
            key="forwardings",
            fetcher=self.list_forwardings,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "mailbox_id": mailbox_id,
                "status": status,
                "project_id": project_id,
                "organization_id": organization_id,
            },
        )

    async def get_forwarding(
        self,
        *,
        forwarding_id: str,
    ) -> Forwarding:
        """
        Get a forwarding rule by its ID.
        :param forwarding_id: ID of the forwarding rule to get.
        :return: :class:`Forwarding <Forwarding>`

        Usage:
        ::

            result = await api.get_forwarding(
                forwarding_id="example",
            )
        """

        param_forwarding_id = validate_path_param("forwarding_id", forwarding_id)

        res = self._request(
            "GET",
            f"/mailbox/v1alpha1/forwardings/{param_forwarding_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Forwarding(res.json())

    async def wait_for_forwarding(
        self,
        *,
        forwarding_id: str,
        options: Optional[
            WaitForOptions[Forwarding, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> Forwarding:
        """
        Get a forwarding rule by its ID.
        :param forwarding_id: ID of the forwarding rule to get.
        :return: :class:`Forwarding <Forwarding>`

        Usage:
        ::

            result = await api.get_forwarding(
                forwarding_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in FORWARDING_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_forwarding,
            options=options,
            args={
                "forwarding_id": forwarding_id,
            },
        )

    async def update_forwarding(
        self,
        *,
        forwarding_id: str,
        email: Optional[str] = None,
    ) -> Forwarding:
        """
        Update a forwarding rule's destination email address by its ID.
        :param forwarding_id: ID of the forwarding rule to update.
        :param email: (Optional) New destination email address for the forwarding rule. Must not be the same as the mailbox's own email address.
        :return: :class:`Forwarding <Forwarding>`

        Usage:
        ::

            result = await api.update_forwarding(
                forwarding_id="example",
            )
        """

        param_forwarding_id = validate_path_param("forwarding_id", forwarding_id)

        res = self._request(
            "PATCH",
            f"/mailbox/v1alpha1/forwardings/{param_forwarding_id}",
            body=marshal_UpdateForwardingRequest(
                UpdateForwardingRequest(
                    forwarding_id=forwarding_id,
                    email=email,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Forwarding(res.json())

    async def delete_forwarding(
        self,
        *,
        forwarding_id: str,
    ) -> Forwarding:
        """
        Delete a forwarding rule by its ID.
        :param forwarding_id: ID of the forwarding rule to delete.
        :return: :class:`Forwarding <Forwarding>`

        Usage:
        ::

            result = await api.delete_forwarding(
                forwarding_id="example",
            )
        """

        param_forwarding_id = validate_path_param("forwarding_id", forwarding_id)

        res = self._request(
            "DELETE",
            f"/mailbox/v1alpha1/forwardings/{param_forwarding_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Forwarding(res.json())

    async def get_mailbox_forwarding(
        self,
        *,
        mailbox_id: str,
    ) -> MailboxForwarding:
        """
        :param mailbox_id: ID of the mailbox to get the forwarding settings for.
        :return: :class:`MailboxForwarding <MailboxForwarding>`

        Usage:
        ::

            result = await api.get_mailbox_forwarding(
                mailbox_id="example",
            )
        """

        param_mailbox_id = validate_path_param("mailbox_id", mailbox_id)

        res = self._request(
            "GET",
            f"/mailbox/v1alpha1/mailboxes/{param_mailbox_id}/forwarding",
        )

        self._throw_on_error(res)
        return unmarshal_MailboxForwarding(res.json())

    async def update_mailbox_forwarding(
        self,
        *,
        mailbox_id: str,
        keep_copy: Optional[bool] = None,
        enabled: Optional[bool] = None,
    ) -> MailboxForwarding:
        """
        :param mailbox_id: ID of the mailbox to update the forwarding settings for.
        :param keep_copy: (Optional) Whether to keep a copy of forwarded emails in the local mailbox.
        :param enabled: (Optional) Enable or disable forwarding for the mailbox.
        :return: :class:`MailboxForwarding <MailboxForwarding>`

        Usage:
        ::

            result = await api.update_mailbox_forwarding(
                mailbox_id="example",
            )
        """

        param_mailbox_id = validate_path_param("mailbox_id", mailbox_id)

        res = self._request(
            "PATCH",
            f"/mailbox/v1alpha1/mailboxes/{param_mailbox_id}/forwarding",
            body=marshal_UpdateMailboxForwardingRequest(
                UpdateMailboxForwardingRequest(
                    mailbox_id=mailbox_id,
                    keep_copy=keep_copy,
                    enabled=enabled,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_MailboxForwarding(res.json())
