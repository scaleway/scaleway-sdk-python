# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Optional

from scaleway_core.api import API
from .types import (
    Locality,
    ResourceType,
    SearchResourcesRequestOrderBy,
    SearchResourcesResponse,
)
from .marshalling import (
    unmarshal_SearchResourcesResponse,
)


class SearchV1Alpha1API(API):
    """ """

    async def search_resources(
        self,
        *,
        query: str,
        organization_id: Optional[str] = None,
        project_ids: Optional[list[str]] = None,
        types: Optional[list[ResourceType]] = None,
        localities: Optional[list[Locality]] = None,
        created_after: Optional[datetime] = None,
        created_before: Optional[datetime] = None,
        modified_after: Optional[datetime] = None,
        modified_before: Optional[datetime] = None,
        page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        order_by: Optional[SearchResourcesRequestOrderBy] = None,
    ) -> SearchResourcesResponse:
        """
        Search API.
        :param query: Search query.
        :param organization_id: ID of the Organization to search in.
        :param project_ids: List of Project IDs to filter the resources by.
        :param types: List of resource types to filter the resources by.
        :param localities: List of scopes (zones, regions, or global) to filter the resources by.
        :param created_after: Filter resources created after this timestamp.
        :param created_before: Filter resources created before this timestamp.
        :param modified_after: Filter resources modified after this timestamp.
        :param modified_before: Filter resources modified before this timestamp.
        :param page_token: Leave empty or omit to fetch the first page.
        :param page_size: Number of resources to retrieve per page.
        :param order_by: Sort order in the response.
        :return: :class:`SearchResourcesResponse <SearchResourcesResponse>`

        Usage:
        ::

            result = await api.search_resources(
                query="example",
            )
        """

        res = self._request(
            "GET",
            "/search/v1alpha1/resources",
            params={
                "created_after": created_after,
                "created_before": created_before,
                "localities": localities,
                "modified_after": modified_after,
                "modified_before": modified_before,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
                "project_ids": project_ids,
                "query": query,
                "types": types,
            },
        )

        self._throw_on_error(res)
        return unmarshal_SearchResourcesResponse(res.json())
