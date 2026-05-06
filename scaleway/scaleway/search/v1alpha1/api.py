# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

from scaleway_core.api import API
from .types import (
    SearchResourcesResponse,
)
from .marshalling import (
    unmarshal_SearchResourcesResponse,
)


class SearchV1Alpha1API(API):
    """ """

    def search_resources(
        self,
        *,
        query: str,
        organization_id: Optional[str] = None,
    ) -> SearchResourcesResponse:
        """
        Search API.
        :param query: Search query.
        :param organization_id: ID of the Organization to search in.
        :return: :class:`SearchResourcesResponse <SearchResourcesResponse>`

        Usage:
        ::

            result = api.search_resources(
                query="example",
            )
        """

        res = self._request(
            "GET",
            "/search/v1alpha1/resources",
            params={
                "organization_id": organization_id
                or self.client.default_organization_id,
                "query": query,
            },
        )

        self._throw_on_error(res)
        return unmarshal_SearchResourcesResponse(res.json())
