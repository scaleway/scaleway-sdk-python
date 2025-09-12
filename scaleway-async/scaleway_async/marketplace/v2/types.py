# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    Zone as ScwZone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class ListImagesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListLocalImagesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    TYPE_ASC = "type_asc"
    TYPE_DESC = "type_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListVersionsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class LocalImageType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    INSTANCE_LOCAL = "instance_local"
    INSTANCE_SBS = "instance_sbs"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Category:
    id: str
    name: str
    description: str


@dataclass
class Image:
    id: str
    """
    UUID of this image.
    """

    name: str
    """
    Name of the image.
    """

    description: str
    """
    Text description of this image.
    """

    logo: str
    """
    URL of this image's logo.
    """

    categories: list[str]
    """
    List of categories this image belongs to.
    """

    label: str
    """
    Typically an identifier for a distribution (ex. "ubuntu_focal").
This label can be used in the image field of the server creation request.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of this image.
    """

    updated_at: Optional[datetime] = None
    """
    Date of the last modification of this image.
    """

    valid_until: Optional[datetime] = None
    """
    Expiration date of this image.
    """


@dataclass
class LocalImage:
    id: str
    """
    Version you will typically use to define an image in an API call.
    """

    compatible_commercial_types: list[str]
    """
    List of all commercial types that are compatible with this local image.
    """

    arch: str
    """
    Supported architecture for this local image.
    """

    zone: ScwZone
    """
    Availability Zone where this local image is available.
    """

    label: str
    """
    This label can be used in the image field of the server creation request.
    """

    type_: LocalImageType
    """
    Type of this local image.
    """


@dataclass
class Version:
    id: str
    """
    UUID of this version.
    """

    name: str
    """
    Name of this version.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of this image version.
    """

    updated_at: Optional[datetime] = None
    """
    Date of the last modification of this version.
    """

    published_at: Optional[datetime] = None
    """
    Date this version was officially published.
    """


@dataclass
class GetCategoryRequest:
    category_id: str


@dataclass
class GetImageRequest:
    image_id: str
    """
    Display the image name.
    """


@dataclass
class GetLocalImageRequest:
    local_image_id: str


@dataclass
class GetVersionRequest:
    version_id: str


@dataclass
class ListCategoriesRequest:
    page_size: Optional[int] = None
    page: Optional[int] = None


@dataclass
class ListCategoriesResponse:
    categories: list[Category]
    total_count: int


@dataclass
class ListImagesRequest:
    include_eol: bool
    """
    Choose to include end-of-life images.
    """

    page_size: Optional[int] = 0
    """
    A positive integer lower or equal to 100 to select the number of items to display.
    """

    page: Optional[int] = 0
    """
    A positive integer to choose the page to display.
    """

    order_by: Optional[ListImagesRequestOrderBy] = ListImagesRequestOrderBy.NAME_ASC
    """
    Ordering to use.
    """

    arch: Optional[str] = None
    """
    Choose for which machine architecture to return images.
    """

    category: Optional[str] = None
    """
    Choose the category of images to get.
    """


@dataclass
class ListImagesResponse:
    images: list[Image]
    total_count: int


@dataclass
class ListLocalImagesRequest:
    page_size: Optional[int] = 0
    """
    A positive integer lower or equal to 100 to select the number of items to display.
    """

    page: Optional[int] = 0
    """
    A positive integer to choose the page to display.
    """

    order_by: Optional[ListLocalImagesRequestOrderBy] = (
        ListLocalImagesRequestOrderBy.TYPE_ASC
    )
    """
    Ordering to use.
    """

    zone: Optional[ScwZone] = None
    """
    Filter local images available on this Availability Zone.
    """

    arch: Optional[str] = None
    """
    Filter local images available for this machine architecture.
    """

    type_: Optional[LocalImageType] = LocalImageType.UNKNOWN_TYPE
    """
    Filter by type.
    """

    image_id: Optional[str] = None

    version_id: Optional[str] = None

    image_label: Optional[str] = None


@dataclass
class ListLocalImagesResponse:
    local_images: list[LocalImage]
    total_count: int


@dataclass
class ListVersionsRequest:
    image_id: str
    page_size: Optional[int] = None
    page: Optional[int] = None
    order_by: Optional[ListVersionsRequestOrderBy] = None


@dataclass
class ListVersionsResponse:
    versions: list[Version]
    total_count: int
