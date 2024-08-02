# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    WaitForOptions,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
)
from .types import (
    HostingStatus,
    ListHostingsRequestOrderBy,
    ListOffersRequestOrderBy,
    CheckUserOwnsDomainRequest,
    CheckUserOwnsDomainResponse,
    ClassicMailApiCreateMailboxRequest,
    ClassicMailApiUpdateMailboxRequest,
    ControlPanel,
    CreateHostingRequest,
    CreateHostingRequestDomainConfiguration,
    DnsRecords,
    EmailAddress,
    Hosting,
    ListControlPanelsResponse,
    ListHostingsResponse,
    ListMailboxesResponse,
    ListOffersResponse,
    Mailbox,
    ResetHostingPasswordResponse,
    Session,
    UpdateHostingRequest,
)
from .content import (
    HOSTING_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Hosting,
    unmarshal_Mailbox,
    unmarshal_CheckUserOwnsDomainResponse,
    unmarshal_DnsRecords,
    unmarshal_ListControlPanelsResponse,
    unmarshal_ListHostingsResponse,
    unmarshal_ListMailboxesResponse,
    unmarshal_ListOffersResponse,
    unmarshal_ResetHostingPasswordResponse,
    unmarshal_Session,
    marshal_CheckUserOwnsDomainRequest,
    marshal_ClassicMailApiCreateMailboxRequest,
    marshal_ClassicMailApiUpdateMailboxRequest,
    marshal_CreateHostingRequest,
    marshal_UpdateHostingRequest,
)
from ...std.types import (
    LanguageCode as StdLanguageCode,
)


class WebhostingV1Alpha1API(API):
    """
    This API allows you to manage your Web Hosting services.
    """

    def create_hosting(
        self,
        *,
        offer_id: str,
        domain: str,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        email: Optional[str] = None,
        tags: Optional[List[str]] = None,
        option_ids: Optional[List[str]] = None,
        language: Optional[StdLanguageCode] = None,
        domain_configuration: Optional[CreateHostingRequestDomainConfiguration] = None,
    ) -> Hosting:
        """
        Order a Web Hosting plan.
        Order a Web Hosting plan, specifying the offer type required via the `offer_id` parameter.
        :param offer_id: ID of the selected offer for the Web Hosting plan.
        :param domain: Domain name to link to the Web Hosting plan. You must already own this domain name, and have completed the DNS validation process beforehand.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Scaleway Project in which to create the Web Hosting plan.
        :param email: Contact email for the Web Hosting client.
        :param tags: List of tags for the Web Hosting plan.
        :param option_ids: IDs of any selected additional options for the Web Hosting plan.
        :param language: Default language for the control panel interface.
        :param domain_configuration: Indicates whether to update hosting domain name servers and DNS records for domains managed by Scaleway Elements.
        :return: :class:`Hosting <Hosting>`

        Usage:
        ::

            result = api.create_hosting(
                offer_id="example",
                domain="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/webhosting/v1alpha1/regions/{param_region}/hostings",
            body=marshal_CreateHostingRequest(
                CreateHostingRequest(
                    offer_id=offer_id,
                    domain=domain,
                    region=region,
                    project_id=project_id,
                    email=email,
                    tags=tags,
                    option_ids=option_ids,
                    language=language,
                    domain_configuration=domain_configuration,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Hosting(res.json())

    def list_hostings(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListHostingsRequestOrderBy] = None,
        tags: Optional[List[str]] = None,
        statuses: Optional[List[HostingStatus]] = None,
        domain: Optional[str] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        control_panels: Optional[List[str]] = None,
    ) -> ListHostingsResponse:
        """
        List all Web Hosting plans.
        List all of your existing Web Hosting plans. Various filters are available to limit the results, including filtering by domain, status, tag and Project ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return, from the paginated results (must be a positive integer).
        :param page_size: Number of Web Hosting plans to return (must be a positive integer lower or equal to 100).
        :param order_by: Sort order for Web Hosting plans in the response.
        :param tags: Tags to filter for, only Web Hosting plans with matching tags will be returned.
        :param statuses: Statuses to filter for, only Web Hosting plans with matching statuses will be returned.
        :param domain: Domain to filter for, only Web Hosting plans associated with this domain will be returned.
        :param project_id: Project ID to filter for, only Web Hosting plans from this Project will be returned.
        :param organization_id: Organization ID to filter for, only Web Hosting plans from this Organization will be returned.
        :param control_panels: Name of the control panel to filter for, only Web Hosting plans from this control panel will be returned.
        :return: :class:`ListHostingsResponse <ListHostingsResponse>`

        Usage:
        ::

            result = api.list_hostings()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/webhosting/v1alpha1/regions/{param_region}/hostings",
            params={
                "control_panels": control_panels,
                "domain": domain,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "statuses": statuses,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListHostingsResponse(res.json())

    def list_hostings_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListHostingsRequestOrderBy] = None,
        tags: Optional[List[str]] = None,
        statuses: Optional[List[HostingStatus]] = None,
        domain: Optional[str] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        control_panels: Optional[List[str]] = None,
    ) -> List[Hosting]:
        """
        List all Web Hosting plans.
        List all of your existing Web Hosting plans. Various filters are available to limit the results, including filtering by domain, status, tag and Project ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return, from the paginated results (must be a positive integer).
        :param page_size: Number of Web Hosting plans to return (must be a positive integer lower or equal to 100).
        :param order_by: Sort order for Web Hosting plans in the response.
        :param tags: Tags to filter for, only Web Hosting plans with matching tags will be returned.
        :param statuses: Statuses to filter for, only Web Hosting plans with matching statuses will be returned.
        :param domain: Domain to filter for, only Web Hosting plans associated with this domain will be returned.
        :param project_id: Project ID to filter for, only Web Hosting plans from this Project will be returned.
        :param organization_id: Organization ID to filter for, only Web Hosting plans from this Organization will be returned.
        :param control_panels: Name of the control panel to filter for, only Web Hosting plans from this control panel will be returned.
        :return: :class:`List[Hosting] <List[Hosting]>`

        Usage:
        ::

            result = api.list_hostings_all()
        """

        return fetch_all_pages(
            type=ListHostingsResponse,
            key="hostings",
            fetcher=self.list_hostings,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "tags": tags,
                "statuses": statuses,
                "domain": domain,
                "project_id": project_id,
                "organization_id": organization_id,
                "control_panels": control_panels,
            },
        )

    def get_hosting(
        self,
        *,
        hosting_id: str,
        region: Optional[Region] = None,
    ) -> Hosting:
        """
        Get a Web Hosting plan.
        Get the details of one of your existing Web Hosting plans, specified by its `hosting_id`.
        :param hosting_id: Hosting ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Hosting <Hosting>`

        Usage:
        ::

            result = api.get_hosting(
                hosting_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hosting_id = validate_path_param("hosting_id", hosting_id)

        res = self._request(
            "GET",
            f"/webhosting/v1alpha1/regions/{param_region}/hostings/{param_hosting_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Hosting(res.json())

    def wait_for_hosting(
        self,
        *,
        hosting_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Hosting, bool]] = None,
    ) -> Hosting:
        """
        Get a Web Hosting plan.
        Get the details of one of your existing Web Hosting plans, specified by its `hosting_id`.
        :param hosting_id: Hosting ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Hosting <Hosting>`

        Usage:
        ::

            result = api.get_hosting(
                hosting_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in HOSTING_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_hosting,
            options=options,
            args={
                "hosting_id": hosting_id,
                "region": region,
            },
        )

    def update_hosting(
        self,
        *,
        hosting_id: str,
        region: Optional[Region] = None,
        email: Optional[str] = None,
        tags: Optional[List[str]] = None,
        option_ids: Optional[List[str]] = None,
        offer_id: Optional[str] = None,
        protected: Optional[bool] = None,
    ) -> Hosting:
        """
        Update a Web Hosting plan.
        Update the details of one of your existing Web Hosting plans, specified by its `hosting_id`. You can update parameters including the contact email address, tags, options and offer.
        :param hosting_id: Hosting ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param email: New contact email for the Web Hosting plan.
        :param tags: New tags for the Web Hosting plan.
        :param option_ids: IDs of the new options for the Web Hosting plan.
        :param offer_id: ID of the new offer for the Web Hosting plan.
        :param protected: Whether the hosting is protected or not.
        :return: :class:`Hosting <Hosting>`

        Usage:
        ::

            result = api.update_hosting(
                hosting_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hosting_id = validate_path_param("hosting_id", hosting_id)

        res = self._request(
            "PATCH",
            f"/webhosting/v1alpha1/regions/{param_region}/hostings/{param_hosting_id}",
            body=marshal_UpdateHostingRequest(
                UpdateHostingRequest(
                    hosting_id=hosting_id,
                    region=region,
                    email=email,
                    tags=tags,
                    option_ids=option_ids,
                    offer_id=offer_id,
                    protected=protected,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Hosting(res.json())

    def delete_hosting(
        self,
        *,
        hosting_id: str,
        region: Optional[Region] = None,
    ) -> Hosting:
        """
        Delete a Web Hosting plan.
        Delete a Web Hosting plan, specified by its `hosting_id`. Note that deletion is not immediate: it will take place at the end of the calendar month, after which time your Web Hosting plan and all its data (files and emails) will be irreversibly lost.
        :param hosting_id: Hosting ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Hosting <Hosting>`

        Usage:
        ::

            result = api.delete_hosting(
                hosting_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hosting_id = validate_path_param("hosting_id", hosting_id)

        res = self._request(
            "DELETE",
            f"/webhosting/v1alpha1/regions/{param_region}/hostings/{param_hosting_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Hosting(res.json())

    def restore_hosting(
        self,
        *,
        hosting_id: str,
        region: Optional[Region] = None,
    ) -> Hosting:
        """
        Restore a Web Hosting plan.
        When you [delete a Web Hosting plan](#path-hostings-delete-a-hosting), definitive deletion does not take place until the end of the calendar month. In the time between initiating the deletion, and definitive deletion at the end of the month, you can choose to **restore** the Web Hosting plan, using this endpoint and specifying its `hosting_id`.
        :param hosting_id: Hosting ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Hosting <Hosting>`

        Usage:
        ::

            result = api.restore_hosting(
                hosting_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hosting_id = validate_path_param("hosting_id", hosting_id)

        res = self._request(
            "POST",
            f"/webhosting/v1alpha1/regions/{param_region}/hostings/{param_hosting_id}/restore",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Hosting(res.json())

    def get_domain_dns_records(
        self,
        *,
        domain: str,
        region: Optional[Region] = None,
    ) -> DnsRecords:
        """
        Get DNS records.
        Get the set of DNS records of a specified domain associated with a Web Hosting plan.
        :param domain: Domain associated with the DNS records.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DnsRecords <DnsRecords>`

        Usage:
        ::

            result = api.get_domain_dns_records(
                domain="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "GET",
            f"/webhosting/v1alpha1/regions/{param_region}/domains/{param_domain}/dns-records",
        )

        self._throw_on_error(res)
        return unmarshal_DnsRecords(res.json())

    def check_user_owns_domain(
        self,
        *,
        domain: str,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
    ) -> CheckUserOwnsDomainResponse:
        """
        "Check whether you own this domain or not.".
        :param domain: Domain for which ownership is to be verified.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the project currently in use.
        :return: :class:`CheckUserOwnsDomainResponse <CheckUserOwnsDomainResponse>`

        Usage:
        ::

            result = api.check_user_owns_domain(
                domain="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_domain = validate_path_param("domain", domain)

        res = self._request(
            "POST",
            f"/webhosting/v1/regions/{param_region}/domains/{param_domain}/check-ownership",
            body=marshal_CheckUserOwnsDomainRequest(
                CheckUserOwnsDomainRequest(
                    domain=domain,
                    region=region,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CheckUserOwnsDomainResponse(res.json())

    def list_offers(
        self,
        *,
        without_options: bool,
        only_options: bool,
        region: Optional[Region] = None,
        order_by: Optional[ListOffersRequestOrderBy] = None,
        hosting_id: Optional[str] = None,
        control_panels: Optional[List[str]] = None,
    ) -> ListOffersResponse:
        """
        List all offers.
        List the different Web Hosting offers, and their options, available to order from Scaleway.
        :param without_options: Defines whether the response should consist of offers only, without options.
        :param only_options: Defines whether the response should consist of options only, without offers.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of offers in the response.
        :param hosting_id: ID of a Web Hosting plan, to check compatibility with returned offers (in case of wanting to update the plan).
        :param control_panels: Name of the control panel to filter for.
        :return: :class:`ListOffersResponse <ListOffersResponse>`

        Usage:
        ::

            result = api.list_offers(
                without_options=False,
                only_options=False,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/webhosting/v1alpha1/regions/{param_region}/offers",
            params={
                "control_panels": control_panels,
                "hosting_id": hosting_id,
                "only_options": only_options,
                "order_by": order_by,
                "without_options": without_options,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListOffersResponse(res.json())

    def list_control_panels(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListControlPanelsResponse:
        """
        "List the control panels type: cpanel or plesk.".
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return, from the paginated results (must be a positive integer).
        :param page_size: Number of control panels to return (must be a positive integer lower or equal to 100).
        :return: :class:`ListControlPanelsResponse <ListControlPanelsResponse>`

        Usage:
        ::

            result = api.list_control_panels()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/webhosting/v1alpha1/regions/{param_region}/control-panels",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListControlPanelsResponse(res.json())

    def list_control_panels_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ControlPanel]:
        """
        "List the control panels type: cpanel or plesk.".
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return, from the paginated results (must be a positive integer).
        :param page_size: Number of control panels to return (must be a positive integer lower or equal to 100).
        :return: :class:`List[ControlPanel] <List[ControlPanel]>`

        Usage:
        ::

            result = api.list_control_panels_all()
        """

        return fetch_all_pages(
            type=ListControlPanelsResponse,
            key="control_panels",
            fetcher=self.list_control_panels,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
            },
        )

    def create_session(
        self,
        *,
        hosting_id: str,
        region: Optional[Region] = None,
    ) -> Session:
        """
        Create a user session.
        :param hosting_id: Hosting ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Session <Session>`

        Usage:
        ::

            result = api.create_session(
                hosting_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hosting_id = validate_path_param("hosting_id", hosting_id)

        res = self._request(
            "POST",
            f"/webhosting/v1alpha1/regions/{param_region}/hostings/{param_hosting_id}/sessions",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Session(res.json())

    def reset_hosting_password(
        self,
        *,
        hosting_id: str,
        region: Optional[Region] = None,
    ) -> ResetHostingPasswordResponse:
        """
        :param hosting_id: UUID of the hosting.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ResetHostingPasswordResponse <ResetHostingPasswordResponse>`

        Usage:
        ::

            result = api.reset_hosting_password(
                hosting_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hosting_id = validate_path_param("hosting_id", hosting_id)

        res = self._request(
            "POST",
            f"/webhosting/v1alpha1/regions/{param_region}/hostings/{param_hosting_id}/reset-password",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_ResetHostingPasswordResponse(res.json())


class WebhostingV1Alpha1ClassicMailAPI(API):
    """
    This API allows you to manage your mailboxes for your Web Hosting services.
    """

    def create_mailbox(
        self,
        *,
        online_id: int,
        password: str,
        region: Optional[Region] = None,
        email: Optional[EmailAddress] = None,
    ) -> Mailbox:
        """
        Create a new mailbox within your hosting plan.
        :param online_id: The Online hosting ID.
        :param password: Password for the new mailbox.
        :param region: Region to target. If none is passed will use default region from the config.
        :param email: The email address of the mailbox.
        :return: :class:`Mailbox <Mailbox>`

        Usage:
        ::

            result = api.create_mailbox(
                online_id=1,
                password="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_online_id = validate_path_param("online_id", online_id)

        res = self._request(
            "POST",
            f"/webhosting/v1alpha1/regions/{param_region}/classic-hostings/{param_online_id}/mailboxes",
            body=marshal_ClassicMailApiCreateMailboxRequest(
                ClassicMailApiCreateMailboxRequest(
                    online_id=online_id,
                    password=password,
                    region=region,
                    email=email,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Mailbox(res.json())

    def get_mailbox(
        self,
        *,
        online_id: int,
        mailbox_id: int,
        region: Optional[Region] = None,
    ) -> Mailbox:
        """
        Get a mailbox by id within your hosting plan.
        :param online_id: The Online hosting ID.
        :param mailbox_id: The ID of the mailbox to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Mailbox <Mailbox>`

        Usage:
        ::

            result = api.get_mailbox(
                online_id=1,
                mailbox_id=1,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_online_id = validate_path_param("online_id", online_id)
        param_mailbox_id = validate_path_param("mailbox_id", mailbox_id)

        res = self._request(
            "GET",
            f"/webhosting/v1alpha1/regions/{param_region}/classic-hostings/{param_online_id}/mailboxes/{param_mailbox_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Mailbox(res.json())

    def list_mailboxes(
        self,
        *,
        online_id: int,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        domain: Optional[str] = None,
    ) -> ListMailboxesResponse:
        """
        List all mailboxes within your hosting plan.
        :param online_id: The Online hosting ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number (must be a positive integer).
        :param page_size: Number of mailboxes to return (must be a positive integer lower or equal to 100).
        :param domain: Domain to filter the mailboxes.
        :return: :class:`ListMailboxesResponse <ListMailboxesResponse>`

        Usage:
        ::

            result = api.list_mailboxes(
                online_id=1,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_online_id = validate_path_param("online_id", online_id)

        res = self._request(
            "GET",
            f"/webhosting/v1alpha1/regions/{param_region}/classic-hostings/{param_online_id}/mailboxes",
            params={
                "domain": domain,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListMailboxesResponse(res.json())

    def list_mailboxes_all(
        self,
        *,
        online_id: int,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        domain: Optional[str] = None,
    ) -> List[Mailbox]:
        """
        List all mailboxes within your hosting plan.
        :param online_id: The Online hosting ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number (must be a positive integer).
        :param page_size: Number of mailboxes to return (must be a positive integer lower or equal to 100).
        :param domain: Domain to filter the mailboxes.
        :return: :class:`List[Mailbox] <List[Mailbox]>`

        Usage:
        ::

            result = api.list_mailboxes_all(
                online_id=1,
            )
        """

        return fetch_all_pages(
            type=ListMailboxesResponse,
            key="mailboxes",
            fetcher=self.list_mailboxes,
            args={
                "online_id": online_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "domain": domain,
            },
        )

    def delete_mailbox(
        self,
        *,
        online_id: int,
        mailbox_id: int,
        region: Optional[Region] = None,
    ) -> Mailbox:
        """
        :param online_id: The Online hosting ID.
        :param mailbox_id: The ID of the mailbox to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Mailbox <Mailbox>`

        Usage:
        ::

            result = api.delete_mailbox(
                online_id=1,
                mailbox_id=1,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_online_id = validate_path_param("online_id", online_id)
        param_mailbox_id = validate_path_param("mailbox_id", mailbox_id)

        res = self._request(
            "DELETE",
            f"/webhosting/v1alpha1/regions/{param_region}/classic-hostings/{param_online_id}/mailboxes/{param_mailbox_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Mailbox(res.json())

    def update_mailbox(
        self,
        *,
        online_id: int,
        mailbox_id: int,
        region: Optional[Region] = None,
        password: Optional[str] = None,
    ) -> Mailbox:
        """
        Update the mailbox within your hosting plan.
        :param online_id: The Online hosting ID.
        :param mailbox_id: The ID of the mailbox to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param password: New password for the mailbox.
        :return: :class:`Mailbox <Mailbox>`

        Usage:
        ::

            result = api.update_mailbox(
                online_id=1,
                mailbox_id=1,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_online_id = validate_path_param("online_id", online_id)
        param_mailbox_id = validate_path_param("mailbox_id", mailbox_id)

        res = self._request(
            "PATCH",
            f"/webhosting/v1alpha1/regions/{param_region}/classic-hostings/{param_online_id}/mailboxes/{param_mailbox_id}",
            body=marshal_ClassicMailApiUpdateMailboxRequest(
                ClassicMailApiUpdateMailboxRequest(
                    online_id=online_id,
                    mailbox_id=mailbox_id,
                    region=region,
                    password=password,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Mailbox(res.json())
