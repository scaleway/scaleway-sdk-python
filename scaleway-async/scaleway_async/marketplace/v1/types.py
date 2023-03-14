# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from scaleway_core.bridge import (
    Zone,
)


@dataclass
class GetImageResponse:
    image: Optional[Image]


@dataclass
class GetVersionResponse:
    version: Optional[Version]


@dataclass
class Image:
    """
    Image.
    """

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

    categories: List[str]
    """
    List of categories this image belongs to.
    """

    creation_date: Optional[datetime]
    """
    Creation date of this image.
    """

    modification_date: Optional[datetime]
    """
    Date of the last modification of this image.
    """

    valid_until: Optional[datetime]
    """
    Expiration date of this image.
    """

    label: str
    """
    Label of this image.
    Typically an identifier for a distribution (ex. "ubuntu_focal").
    """

    versions: List[Version]
    """
    List of versions of this image.
    """

    organization: Optional[Organization]
    """
    Organization this image belongs to.
    """

    current_public_version: str


@dataclass
class ListImagesResponse:
    images: List[Image]

    total_count: int


@dataclass
class ListVersionsResponse:
    versions: List[Version]

    total_count: int


@dataclass
class LocalImage:
    """
    Local image.
    """

    id: str
    """
    UUID of this local image.
    Version you will typically use to define an image in an API call.
    """

    compatible_commercial_types: List[str]
    """
    List of all commercial types that are compatible with this local image.
    """

    arch: str
    """
    Supported architecture for this local image.
    """

    zone: Zone
    """
    Availability Zone where this local image is available.
    """


@dataclass
class Organization:
    id: str

    name: str


@dataclass
class Version:
    """
    Version.
    """

    id: str
    """
    UUID of this version.
    """

    name: str
    """
    Name of this version.
    """

    creation_date: Optional[datetime]
    """
    Creation date of this image version.
    """

    modification_date: Optional[datetime]
    """
    Date of the last modification of this version.
    """

    local_images: List[LocalImage]
    """
    List of local images available in this version.
    """


@dataclass
class ListImagesRequest:
    per_page: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to display.
    """

    page: Optional[int]
    """
    A positive integer to choose the page to display.
    """


@dataclass
class GetImageRequest:
    image_id: str
    """
    Display the image name.
    """


@dataclass
class ListVersionsRequest:
    image_id: str


@dataclass
class GetVersionRequest:
    image_id: str

    version_id: str
