# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.utils import (
    fetch_all_pages_async,
)
from .types import (
    ListPublicCatalogProductsResponse,
    PublicCatalogProduct,
)
from .marshalling import (
    unmarshal_ListPublicCatalogProductsResponse,
)


class ProductCatalogV2Alpha1PublicCatalogAPI(API):
    """ """

    async def list_public_catalog_products(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListPublicCatalogProductsResponse:
        """
        List all available products.
        List all available products in the Scaleway catalog. Returns a complete list of products with their corresponding description, locations, prices and properties. You can define the `page` number and `page_size` for your query in the request.
        :param page: Number of the page. Value must be greater or equal to 1.
        :param page_size: The number of products per page. Value must be greater or equal to 1.
        :return: :class:`ListPublicCatalogProductsResponse <ListPublicCatalogProductsResponse>`

        Usage:
        ::

            result = await api.list_public_catalog_products()
        """

        res = self._request(
            "GET",
            "/product-catalog/v2alpha1/public-catalog/products",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPublicCatalogProductsResponse(res.json())

    async def list_public_catalog_products_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[PublicCatalogProduct]:
        """
        List all available products.
        List all available products in the Scaleway catalog. Returns a complete list of products with their corresponding description, locations, prices and properties. You can define the `page` number and `page_size` for your query in the request.
        :param page: Number of the page. Value must be greater or equal to 1.
        :param page_size: The number of products per page. Value must be greater or equal to 1.
        :return: :class:`List[PublicCatalogProduct] <List[PublicCatalogProduct]>`

        Usage:
        ::

            result = await api.list_public_catalog_products_all()
        """

        return await fetch_all_pages_async(
            type=ListPublicCatalogProductsResponse,
            key="products",
            fetcher=self.list_public_catalog_products,
            args={
                "page": page,
                "page_size": page_size,
            },
        )
