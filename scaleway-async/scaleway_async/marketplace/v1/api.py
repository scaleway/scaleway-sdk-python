# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.utils import (
    validate_path_param,
    fetch_all_pages_async,
)
from .types import (
    GetImageResponse,
    Image,
    ListImagesResponse,
)
from .marshalling import (
    unmarshal_GetImageResponse,
    unmarshal_ListImagesResponse,
)


class MarketplaceV1API(API):
    """
    Marketplace API.
    """

    async def list_images(
        self,
        *,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListImagesResponse:
        """
        List marketplace images.
        List marketplace images.
        :param per_page: A positive integer lower or equal to 100 to select the number of items to display.
        :param page: A positive integer to choose the page to display.
        :return: :class:`ListImagesResponse <ListImagesResponse>`

        Usage:
        ::

            result = await api.list_images()
        """

        res = self._request(
            "GET",
            "/marketplace/v1/images",
            params={
                "page": page,
                "per_page": per_page or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListImagesResponse(res.json())

    async def list_images_all(
        self,
        *,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[Image]:
        """
        List marketplace images.
        List marketplace images.
        :param per_page: A positive integer lower or equal to 100 to select the number of items to display.
        :param page: A positive integer to choose the page to display.
        :return: :class:`List[Image] <List[Image]>`

        Usage:
        ::

            result = await api.list_images_all()
        """

        return await fetch_all_pages_async(
            type=ListImagesResponse,
            key="images",
            fetcher=self.list_images,
            args={
                "per_page": per_page,
                "page": page,
            },
        )

    async def get_image(
        self,
        *,
        image_id: str,
    ) -> GetImageResponse:
        """
        Get a specific marketplace image.
        Get a specific marketplace image.
        :param image_id: Display the image name.
        :return: :class:`GetImageResponse <GetImageResponse>`

        Usage:
        ::

            result = await api.get_image(
                image_id="example",
            )
        """

        param_image_id = validate_path_param("image_id", image_id)

        res = self._request(
            "GET",
            f"/marketplace/v1/images/{param_image_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GetImageResponse(res.json())
