# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Zone,
)
from scaleway_core.utils import (
    OneOfPossibility,
    fetch_all_pages_async,
    resolve_one_of,
    validate_path_param,
)
from .types import (
    ListImagesRequestOrderBy,
    ListLocalImagesRequestOrderBy,
    ListVersionsRequestOrderBy,
    Category,
    Image,
    ListCategoriesResponse,
    ListImagesResponse,
    ListLocalImagesResponse,
    ListVersionsResponse,
    LocalImage,
    Version,
)
from .marshalling import (
    unmarshal_Category,
    unmarshal_Image,
    unmarshal_LocalImage,
    unmarshal_Version,
    unmarshal_ListCategoriesResponse,
    unmarshal_ListImagesResponse,
    unmarshal_ListLocalImagesResponse,
    unmarshal_ListVersionsResponse,
)


class MarketplaceV2API(API):
    """
    Marketplace API.
    """

    async def list_images(
        self,
        *,
        include_eol: bool,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        order_by: ListImagesRequestOrderBy = ListImagesRequestOrderBy.NAME_ASC,
        arch: Optional[str] = None,
        category: Optional[str] = None,
    ) -> ListImagesResponse:
        """
        List marketplace images
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display
        :param page: A positive integer to choose the page to display
        :param order_by: Ordering to use
        :param arch: Choose for which machine architecture to return images
        :param category: Choose the category of images to get
        :param include_eol: Choose to include end-of-life images
        :return: :class:`ListImagesResponse <ListImagesResponse>`

        Usage:
        ::

            result = await api.list_images(include_eol=True)
        """

        res = self._request(
            "GET",
            f"/marketplace/v2/images",
            params={
                "arch": arch,
                "category": category,
                "include_eol": include_eol,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListImagesResponse(res.json())

    async def list_images_all(
        self,
        *,
        include_eol: bool,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        order_by: Optional[ListImagesRequestOrderBy] = None,
        arch: Optional[str] = None,
        category: Optional[str] = None,
    ) -> List[Image]:
        """
        List marketplace images
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display
        :param page: A positive integer to choose the page to display
        :param order_by: Ordering to use
        :param arch: Choose for which machine architecture to return images
        :param category: Choose the category of images to get
        :param include_eol: Choose to include end-of-life images
        :return: :class:`List[ListImagesResponse] <List[ListImagesResponse]>`

        Usage:
        ::

            result = await api.list_images_all(include_eol=True)
        """

        return await fetch_all_pages_async(
            type=ListImagesResponse,
            key="images",
            fetcher=self.list_images,
            args={
                "include_eol": include_eol,
                "page_size": page_size,
                "page": page,
                "order_by": order_by,
                "arch": arch,
                "category": category,
            },
        )

    async def get_image(
        self,
        *,
        image_id: str,
    ) -> Image:
        """
        Get a specific marketplace image
        :param image_id: Display the image name
        :return: :class:`Image <Image>`

        Usage:
        ::

            result = await api.get_image(image_id="example")
        """

        param_image_id = validate_path_param("image_id", image_id)

        res = self._request(
            "GET",
            f"/marketplace/v2/images/{param_image_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Image(res.json())

    async def list_versions(
        self,
        *,
        image_id: str,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        order_by: ListVersionsRequestOrderBy = ListVersionsRequestOrderBy.CREATED_AT_ASC,
    ) -> ListVersionsResponse:
        """

        Usage:
        ::

            result = await api.list_versions(image_id="example")
        """

        res = self._request(
            "GET",
            f"/marketplace/v2/versions",
            params={
                "image_id": image_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListVersionsResponse(res.json())

    async def list_versions_all(
        self,
        *,
        image_id: str,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        order_by: Optional[ListVersionsRequestOrderBy] = None,
    ) -> List[Version]:
        """
        :return: :class:`List[ListVersionsResponse] <List[ListVersionsResponse]>`

        Usage:
        ::

            result = await api.list_versions_all(image_id="example")
        """

        return await fetch_all_pages_async(
            type=ListVersionsResponse,
            key="versions",
            fetcher=self.list_versions,
            args={
                "image_id": image_id,
                "page_size": page_size,
                "page": page,
                "order_by": order_by,
            },
        )

    async def get_version(
        self,
        *,
        version_id: str,
    ) -> Version:
        """

        Usage:
        ::

            result = await api.get_version(version_id="example")
        """

        param_version_id = validate_path_param("version_id", version_id)

        res = self._request(
            "GET",
            f"/marketplace/v2/versions/{param_version_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Version(res.json())

    async def list_local_images(
        self,
        *,
        image_id: Optional[str] = None,
        version_id: Optional[str] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        order_by: ListLocalImagesRequestOrderBy = ListLocalImagesRequestOrderBy.CREATED_AT_ASC,
        image_label: Optional[str] = None,
        zone: Optional[Zone] = None,
    ) -> ListLocalImagesResponse:
        """
        List local images from a specific image or version
        :param image_id: One-of ('scope'): at most one of 'image_id', 'version_id', 'image_label' could be set.
        :param version_id: One-of ('scope'): at most one of 'image_id', 'version_id', 'image_label' could be set.
        :param page_size:
        :param page:
        :param order_by:
        :param image_label: One-of ('scope'): at most one of 'image_id', 'version_id', 'image_label' could be set.
        :param zone:
        :return: :class:`ListLocalImagesResponse <ListLocalImagesResponse>`

        Usage:
        ::

            result = await api.list_local_images()
        """

        res = self._request(
            "GET",
            f"/marketplace/v2/local-images",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "zone": zone or self.client.default_zone,
                **resolve_one_of(
                    [
                        OneOfPossibility("image_id", image_id),
                        OneOfPossibility("version_id", version_id),
                        OneOfPossibility("image_label", image_label),
                    ]
                ),
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListLocalImagesResponse(res.json())

    async def list_local_images_all(
        self,
        *,
        image_id: Optional[str] = None,
        version_id: Optional[str] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        order_by: Optional[ListLocalImagesRequestOrderBy] = None,
        image_label: Optional[str] = None,
        zone: Optional[Zone] = None,
    ) -> List[LocalImage]:
        """
        List local images from a specific image or version
        :param image_id: One-of ('scope'): at most one of 'image_id', 'version_id', 'image_label' could be set.
        :param version_id: One-of ('scope'): at most one of 'image_id', 'version_id', 'image_label' could be set.
        :param page_size:
        :param page:
        :param order_by:
        :param image_label: One-of ('scope'): at most one of 'image_id', 'version_id', 'image_label' could be set.
        :param zone:
        :return: :class:`List[ListLocalImagesResponse] <List[ListLocalImagesResponse]>`

        Usage:
        ::

            result = await api.list_local_images_all()
        """

        return await fetch_all_pages_async(
            type=ListLocalImagesResponse,
            key="local_images",
            fetcher=self.list_local_images,
            args={
                "image_id": image_id,
                "version_id": version_id,
                "page_size": page_size,
                "page": page,
                "order_by": order_by,
                "image_label": image_label,
                "zone": zone,
            },
        )

    async def get_local_image(
        self,
        *,
        local_image_id: str,
    ) -> LocalImage:
        """

        Usage:
        ::

            result = await api.get_local_image(local_image_id="example")
        """

        param_local_image_id = validate_path_param("local_image_id", local_image_id)

        res = self._request(
            "GET",
            f"/marketplace/v2/local-images/{param_local_image_id}",
        )

        self._throw_on_error(res)
        return unmarshal_LocalImage(res.json())

    async def list_categories(
        self,
        *,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListCategoriesResponse:
        """

        Usage:
        ::

            result = await api.list_categories()
        """

        res = self._request(
            "GET",
            f"/marketplace/v2/categories",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListCategoriesResponse(res.json())

    async def list_categories_all(
        self,
        *,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[Category]:
        """
        :return: :class:`List[ListCategoriesResponse] <List[ListCategoriesResponse]>`

        Usage:
        ::

            result = await api.list_categories_all()
        """

        return await fetch_all_pages_async(
            type=ListCategoriesResponse,
            key="categories",
            fetcher=self.list_categories,
            args={
                "page_size": page_size,
                "page": page,
            },
        )

    async def get_category(
        self,
        *,
        category_id: str,
    ) -> Category:
        """

        Usage:
        ::

            result = await api.get_category(category_id="example")
        """

        param_category_id = validate_path_param("category_id", category_id)

        res = self._request(
            "GET",
            f"/marketplace/v2/categories/{param_category_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Category(res.json())
