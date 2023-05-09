# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages,
    validate_path_param,
    wait_for_resource,
)
from .types import (
    HostingStatus,
    ListHostingsRequestOrderBy,
    ListOffersRequestOrderBy,
    DnsRecords,
    Hosting,
    ListHostingsResponse,
    ListOffersResponse,
    CreateHostingRequest,
    UpdateHostingRequest,
)
from .content import (
    HOSTING_TRANSIENT_STATUSES,
)
from .marshalling import (
    marshal_CreateHostingRequest,
    marshal_UpdateHostingRequest,
    unmarshal_Hosting,
    unmarshal_DnsRecords,
    unmarshal_ListHostingsResponse,
    unmarshal_ListOffersResponse,
)


class WebhostingV1Alpha1API(API):
    """
    Web Hosting API.

    Web Hosting API.
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
    ) -> Hosting:
        """
        Order a Web Hosting plan.
        Order a Web Hosting plan, specifying the offer type required via the `offer_id` parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param offer_id: ID of the selected offer for the Web Hosting plan.
        :param project_id: ID of the Scaleway Project in which to create the Web Hosting plan.
        :param email: Contact email for the Web Hosting client.
        :param tags: List of tags for the Web Hosting plan.
        :param domain: Domain name to link to the Web Hosting plan. You must already own this domain name, and have completed the DNS validation process beforehand.
        :param option_ids: IDs of any selected additional options for the Web Hosting plan.
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
        order_by: ListHostingsRequestOrderBy = ListHostingsRequestOrderBy.CREATED_AT_ASC,
        tags: Optional[List[str]] = None,
        statuses: Optional[List[HostingStatus]] = None,
        domain: Optional[str] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
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
        :return: :class:`List[ListHostingsResponse] <List[ListHostingsResponse]>`

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
        :param region: Region to target. If none is passed will use default region from the config.
        :param hosting_id: Hosting ID.
        :return: :class:`Hosting <Hosting>`

        Usage:
        ::

            result = api.get_hosting(hosting_id="example")
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
        Waits for :class:`Hosting <Hosting>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config.
        :param hosting_id: Hosting ID.
        :param options: The options for the waiter
        :return: :class:`Hosting <Hosting>`

        Usage:
        ::

            result = api.wait_for_hosting(hosting_id="example")
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
    ) -> Hosting:
        """
        Update a Web Hosting plan.
        Update the details of one of your existing Web Hosting plans, specified by its `hosting_id`. You can update parameters including the contact email address, tags, options and offer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param hosting_id: Hosting ID.
        :param email: New contact email for the Web Hosting plan.
        :param tags: New tags for the Web Hosting plan.
        :param option_ids: IDs of the new options for the Web Hosting plan.
        :param offer_id: ID of the new offer for the Web Hosting plan.
        :return: :class:`Hosting <Hosting>`

        Usage:
        ::

            result = api.update_hosting(hosting_id="example")
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
        :param region: Region to target. If none is passed will use default region from the config.
        :param hosting_id: Hosting ID.
        :return: :class:`Hosting <Hosting>`

        Usage:
        ::

            result = api.delete_hosting(hosting_id="example")
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
        :param region: Region to target. If none is passed will use default region from the config.
        :param hosting_id: Hosting ID.
        :return: :class:`Hosting <Hosting>`

        Usage:
        ::

            result = api.restore_hosting(hosting_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hosting_id = validate_path_param("hosting_id", hosting_id)

        res = self._request(
            "POST",
            f"/webhosting/v1alpha1/regions/{param_region}/hostings/{param_hosting_id}/restore",
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
        :param region: Region to target. If none is passed will use default region from the config.
        :param domain: Domain associated with the DNS records.
        :return: :class:`DnsRecords <DnsRecords>`

        Usage:
        ::

            result = api.get_domain_dns_records(domain="example")
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

    def list_offers(
        self,
        *,
        order_by: ListOffersRequestOrderBy,
        without_options: bool,
        only_options: bool,
        region: Optional[Region] = None,
        hosting_id: Optional[str] = None,
    ) -> ListOffersResponse:
        """
        List all offers.
        List the different Web Hosting offers, and their options, available to order from Scaleway.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of offers in the response.
        :param without_options: Defines whether the response should consist of offers only, without options.
        :param only_options: Defines whether the response should consist of options only, without offers.
        :param hosting_id: ID of a Web Hosting plan, to check compatibility with returned offers (in case of wanting to update the plan).
        :return: :class:`ListOffersResponse <ListOffersResponse>`

        Usage:
        ::

            result = api.list_offers(
                order_by=price_asc,
                without_options=True,
                only_options=True,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/webhosting/v1alpha1/regions/{param_region}/offers",
            params={
                "hosting_id": hosting_id,
                "only_options": only_options,
                "order_by": order_by,
                "without_options": without_options,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListOffersResponse(res.json())
