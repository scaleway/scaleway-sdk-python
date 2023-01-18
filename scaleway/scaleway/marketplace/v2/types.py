# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Zone,
)


class ListImagesRequestOrderBy(str, Enum):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListLocalImagesRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListVersionsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Category:
    id: str

    name: str

    description: str


@dataclass
class Image:
    """
    Image
    """

    id: str
    """
    UUID of this image
    """

    name: str
    """
    Name of the image
    """

    description: str
    """
    Text description of this image
    """

    logo: str
    """
    URL of this image's logo
    """

    categories: List[str]
    """
    List of categories this image belongs to
    """

    created_at: Optional[datetime]
    """
    Creation date of this image
    """

    updated_at: Optional[datetime]
    """
    Date of the last modification of this image
    """

    valid_until: Optional[datetime]
    """
    Expiration date of this image
    """

    label: str
    """
    Typically an identifier for a distribution (ex. "ubuntu_focal").
    
    """


@dataclass
class ListCategoriesResponse:
    categories: List[Category]

    total_count: int


@dataclass
class ListImagesResponse:
    images: List[Image]

    total_count: int


@dataclass
class ListLocalImagesResponse:
    local_images: List[LocalImage]

    total_count: int


@dataclass
class ListVersionsResponse:
    versions: List[Version]

    total_count: int


@dataclass
class LocalImage:
    """
    Local image
    """

    id: str
    """
    Version you will typically use to define an image in an API call.
    
    """

    compatible_commercial_types: List[str]
    """
    List of all commercial types that are compatible with this local image
    """

    arch: str
    """
    Supported architecture for this local image
    """

    zone: Zone
    """
    Availability Zone where this local image is available
    """

    label: str
    """
    Image label this image belongs to
    """


@dataclass
class Version:
    """
    Version
    """

    id: str
    """
    UUID of this version
    """

    name: str
    """
    Name of this version
    """

    created_at: Optional[datetime]
    """
    Creation date of this image version
    """

    updated_at: Optional[datetime]
    """
    Date of the last modification of this version
    """

    published_at: Optional[datetime]
    """
    Date this version was officially published
    """


@dataclass
class ListImagesRequest:
    page_size: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to display
    """

    page: Optional[int]
    """
    A positive integer to choose the page to display
    """

    order_by: Optional[ListImagesRequestOrderBy]
    """
    Ordering to use
    """

    arch: Optional[str]
    """
    Choose for which machine architecture to return images
    """

    category: Optional[str]
    """
    Choose the category of images to get
    """

    include_eol: bool
    """
    Choose to include end-of-life images
    """


@dataclass
class GetImageRequest:
    image_id: str
    """
    Display the image name
    """


@dataclass
class ListVersionsRequest:
    image_id: str

    page_size: Optional[int]

    page: Optional[int]

    order_by: Optional[ListVersionsRequestOrderBy]


@dataclass
class GetVersionRequest:
    version_id: str


@dataclass
class ListLocalImagesRequest:
    image_id: Optional[str]
    """
    One-of ('scope'): at most one of 'image_id', 'version_id', 'image_label' could be set.
    """

    version_id: Optional[str]
    """
    One-of ('scope'): at most one of 'image_id', 'version_id', 'image_label' could be set.
    """

    page_size: Optional[int]

    page: Optional[int]

    order_by: Optional[ListLocalImagesRequestOrderBy]

    image_label: Optional[str]
    """
    One-of ('scope'): at most one of 'image_id', 'version_id', 'image_label' could be set.
    """

    zone: Optional[Zone]


@dataclass
class GetLocalImageRequest:
    local_image_id: str


@dataclass
class ListCategoriesRequest:
    page_size: Optional[int]

    page: Optional[int]


@dataclass
class GetCategoryRequest:
    category_id: str
