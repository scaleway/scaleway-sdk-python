# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Zone,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
    validate_path_param,
    fetch_all_pages_async,
)
from .types import (
    ListImagesRequestOrderBy,
    ListLocalImagesRequestOrderBy,
    ListVersionsRequestOrderBy,
    LocalImageType,
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
    This API allows you to find available images for use when launching a Scaleway Instance.
    """

    async def list_images(
        self,
        *,
        include_eol: bool,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        order_by: Optional[ListImagesRequestOrderBy] = None,
        arch: Optional[str] = None,
        category: Optional[str] = None,
    ) -> ListImagesResponse:
        """
        List marketplace images.
        List all available images on the marketplace, their UUID, CPU architecture and description.
        :param include_eol: Choose to include end-of-life images.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display.
        :param page: A positive integer to choose the page to display.
        :param order_by: Ordering to use.
        :param arch: Choose for which machine architecture to return images.
        :param category: Choose the category of images to get.
        :return: :class:`ListImagesResponse <ListImagesResponse>`

        Usage:
        ::

            result = await api.list_images(
                include_eol=False,
            )
        """

        res = self._request(
            "GET",
            "/marketplace/v2/images",
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
        List marketplace images.
        List all available images on the marketplace, their UUID, CPU architecture and description.
        :param include_eol: Choose to include end-of-life images.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display.
        :param page: A positive integer to choose the page to display.
        :param order_by: Ordering to use.
        :param arch: Choose for which machine architecture to return images.
        :param category: Choose the category of images to get.
        :return: :class:`List[Image] <List[Image]>`

        Usage:
        ::

            result = await api.list_images_all(
                include_eol=False,
            )
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
        Get a specific marketplace image.
        Get detailed information about a marketplace image, specified by its `image_id` (UUID format).
        :param image_id: Display the image name.
        :return: :class:`Image <Image>`

        Usage:
        ::

            result = await api.get_image(
                image_id="example",
            )
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
        order_by: Optional[ListVersionsRequestOrderBy] = None,
    ) -> ListVersionsResponse:
        """
        List versions of an Image.
        Get a list of all available version of an image, specified by its `image_id` (UUID format).
        :param image_id:
        :param page_size:
        :param page:
        :param order_by:
        :return: :class:`ListVersionsResponse <ListVersionsResponse>`

        Usage:
        ::

            result = await api.list_versions(
                image_id="example",
            )
        """

        res = self._request(
            "GET",
            "/marketplace/v2/versions",
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
        List versions of an Image.
        Get a list of all available version of an image, specified by its `image_id` (UUID format).
        :param image_id:
        :param page_size:
        :param page:
        :param order_by:
        :return: :class:`List[Version] <List[Version]>`

        Usage:
        ::

            result = await api.list_versions_all(
                image_id="example",
            )
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
        Get a specific image version.
        Get information such as the name, creation date, last update and published date for an image version specified by its `version_id` (UUID format).
        :param version_id:
        :return: :class:`Version <Version>`

        Usage:
        ::

            result = await api.get_version(
                version_id="example",
            )
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
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        order_by: Optional[ListLocalImagesRequestOrderBy] = None,
        zone: Optional[Zone] = None,
        image_id: Optional[str] = None,
        version_id: Optional[str] = None,
        image_label: Optional[str] = None,
        type_: Optional[LocalImageType] = None,
    ) -> ListLocalImagesResponse:
        """
        List local images from a specific image or version.
        List information about local images in a specific Availability Zone, specified by its `image_id` (UUID format), `version_id` (UUID format) or `image_label`. Only one of these three parameters may be set.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display.
        :param page: A positive integer to choose the page to display.
        :param order_by: Ordering to use.
        :param zone: Filter local images available on this Availability Zone.
        :param image_id: Filter by image id.
        One-Of ('scope'): at most one of 'image_id', 'version_id', 'image_label' could be set.
        :param version_id: Filter by version id.
        One-Of ('scope'): at most one of 'image_id', 'version_id', 'image_label' could be set.
        :param image_label: Filter by image label.
        One-Of ('scope'): at most one of 'image_id', 'version_id', 'image_label' could be set.
        :param type_: Filter by type.
        :return: :class:`ListLocalImagesResponse <ListLocalImagesResponse>`

        Usage:
        ::

            result = await api.list_local_images()
        """

        res = self._request(
            "GET",
            "/marketplace/v2/local-images",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "type": type_,
                "zone": zone or self.client.default_zone,
                **resolve_one_of(
                    [
                        OneOfPossibility("image_id", image_id),
                        OneOfPossibility("image_label", image_label),
                        OneOfPossibility("version_id", version_id),
                    ]
                ),
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListLocalImagesResponse(res.json())

    async def list_local_images_all(
        self,
        *,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        order_by: Optional[ListLocalImagesRequestOrderBy] = None,
        zone: Optional[Zone] = None,
        image_id: Optional[str] = None,
        version_id: Optional[str] = None,
        image_label: Optional[str] = None,
        type_: Optional[LocalImageType] = None,
    ) -> List[LocalImage]:
        """
        List local images from a specific image or version.
        List information about local images in a specific Availability Zone, specified by its `image_id` (UUID format), `version_id` (UUID format) or `image_label`. Only one of these three parameters may be set.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display.
        :param page: A positive integer to choose the page to display.
        :param order_by: Ordering to use.
        :param zone: Filter local images available on this Availability Zone.
        :param image_id: Filter by image id.
        One-Of ('scope'): at most one of 'image_id', 'version_id', 'image_label' could be set.
        :param version_id: Filter by version id.
        One-Of ('scope'): at most one of 'image_id', 'version_id', 'image_label' could be set.
        :param image_label: Filter by image label.
        One-Of ('scope'): at most one of 'image_id', 'version_id', 'image_label' could be set.
        :param type_: Filter by type.
        :return: :class:`List[LocalImage] <List[LocalImage]>`

        Usage:
        ::

            result = await api.list_local_images_all()
        """

        return await fetch_all_pages_async(
            type=ListLocalImagesResponse,
            key="local_images",
            fetcher=self.list_local_images,
            args={
                "page_size": page_size,
                "page": page,
                "order_by": order_by,
                "zone": zone,
                "type_": type_,
                "image_id": image_id,
                "version_id": version_id,
                "image_label": image_label,
            },
        )

    async def get_local_image(
        self,
        *,
        local_image_id: str,
    ) -> LocalImage:
        """
        Get a specific local image by ID.
        Get detailed information about a local image, including compatible commercial types, supported architecture, labels and the Availability Zone of the image, specified by its `local_image_id` (UUID format).
        :param local_image_id:
        :return: :class:`LocalImage <LocalImage>`

        Usage:
        ::

            result = await api.get_local_image(
                local_image_id="example",
            )
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
        List existing image categories.
        Get a list of all existing categories. The output can be paginated.
        :param page_size:
        :param page:
        :return: :class:`ListCategoriesResponse <ListCategoriesResponse>`

        Usage:
        ::

            result = await api.list_categories()
        """

        res = self._request(
            "GET",
            "/marketplace/v2/categories",
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
        List existing image categories.
        Get a list of all existing categories. The output can be paginated.
        :param page_size:
        :param page:
        :return: :class:`List[Category] <List[Category]>`

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
        Get a specific category.
        Get information about a specific category of the marketplace catalog, specified by its `category_id` (UUID format).
        :param category_id:
        :return: :class:`Category <Category>`

        Usage:
        ::

            result = await api.get_category(
                category_id="example",
            )
        """

        param_category_id = validate_path_param("category_id", category_id)

        res = self._request(
            "GET",
            f"/marketplace/v2/categories/{param_category_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Category(res.json())
