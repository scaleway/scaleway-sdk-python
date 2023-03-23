# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages_async,
    validate_path_param,
    wait_for_resource_async,
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
    Webhosting API.

    Webhosting API.
    """

    async def create_hosting(
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
        Create a hosting.
        :param region: Region to target. If none is passed will use default region from the config.
        :param offer_id: ID of the selected offer for the hosting.
        :param project_id: Project ID of the hosting.
        :param email: Contact email of the client for the hosting.
        :param tags: The tags of the hosting.
        :param domain: The domain name of the hosting.
        :param option_ids: IDs of the selected options for the hosting.
        :return: :class:`Hosting <Hosting>`

        Usage:
        ::

            result = await api.create_hosting(
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

    async def list_hostings(
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
        List all hostings.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: A positive integer to choose the page to return.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to return.
        :param order_by: Define the order of the returned hostings.
        :param tags: Return hostings with these tags.
        :param statuses: Return hostings with these statuses.
        :param domain: Return hostings with this domain.
        :param project_id: Return hostings from this project ID.
        :param organization_id: Return hostings from this organization ID.
        :return: :class:`ListHostingsResponse <ListHostingsResponse>`

        Usage:
        ::

            result = await api.list_hostings()
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

    async def list_hostings_all(
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
        List all hostings.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: A positive integer to choose the page to return.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to return.
        :param order_by: Define the order of the returned hostings.
        :param tags: Return hostings with these tags.
        :param statuses: Return hostings with these statuses.
        :param domain: Return hostings with this domain.
        :param project_id: Return hostings from this project ID.
        :param organization_id: Return hostings from this organization ID.
        :return: :class:`List[ListHostingsResponse] <List[ListHostingsResponse]>`

        Usage:
        ::

            result = await api.list_hostings_all()
        """

        return await fetch_all_pages_async(
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

    async def get_hosting(
        self,
        *,
        hosting_id: str,
        region: Optional[Region] = None,
    ) -> Hosting:
        """
        Get a hosting.
        Get the details of a Hosting with the given ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param hosting_id: Hosting ID.
        :return: :class:`Hosting <Hosting>`

        Usage:
        ::

            result = await api.get_hosting(hosting_id="example")
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

    async def wait_for_hosting(
        self,
        *,
        hosting_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Hosting, Union[bool, Awaitable[bool]]]] = None,
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

        return await wait_for_resource_async(
            fetcher=self.get_hosting,
            options=options,
            args={
                "hosting_id": hosting_id,
                "region": region,
            },
        )

    async def update_hosting(
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
        Update a hosting.
        :param region: Region to target. If none is passed will use default region from the config.
        :param hosting_id: Hosting ID.
        :param email: New contact email for the hosting.
        :param tags: New tags for the hosting.
        :param option_ids: New options IDs for the hosting.
        :param offer_id: New offer ID for the hosting.
        :return: :class:`Hosting <Hosting>`

        Usage:
        ::

            result = await api.update_hosting(hosting_id="example")
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

    async def delete_hosting(
        self,
        *,
        hosting_id: str,
        region: Optional[Region] = None,
    ) -> Hosting:
        """
        Delete a hosting.
        Delete a hosting with the given ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param hosting_id: Hosting ID.
        :return: :class:`Hosting <Hosting>`

        Usage:
        ::

            result = await api.delete_hosting(hosting_id="example")
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

    async def restore_hosting(
        self,
        *,
        hosting_id: str,
        region: Optional[Region] = None,
    ) -> Hosting:
        """
        Restore a hosting.
        Restore a hosting with the given ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param hosting_id: Hosting ID.
        :return: :class:`Hosting <Hosting>`

        Usage:
        ::

            result = await api.restore_hosting(hosting_id="example")
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

    async def get_domain_dns_records(
        self,
        *,
        domain: str,
        region: Optional[Region] = None,
    ) -> DnsRecords:
        """
        Get the DNS records.
        The set of DNS record of a specific domain associated to a hosting.
        :param region: Region to target. If none is passed will use default region from the config.
        :param domain: Domain associated to the DNS records.
        :return: :class:`DnsRecords <DnsRecords>`

        Usage:
        ::

            result = await api.get_domain_dns_records(domain="example")
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

    async def list_offers(
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
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Define the order of the returned hostings.
        :param without_options: Select only offers, no options.
        :param only_options: Select only options.
        :param hosting_id: Define a specific hosting id (optional).
        :return: :class:`ListOffersResponse <ListOffersResponse>`

        Usage:
        ::

            result = await api.list_offers(
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
