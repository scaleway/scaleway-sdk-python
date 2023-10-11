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
class LocalImage:
    zone: Zone
    """
    Availability Zone where this local image is available.
    """

    arch: str
    """
    Supported architecture for this local image.
    """

    compatible_commercial_types: List[str]
    """
    List of all commercial types that are compatible with this local image.
    """

    id: str
    """
    Version you will typically use to define an image in an API call.
    """


@dataclass
class Organization:
    name: str

    id: str


@dataclass
class Version:
    local_images: List[LocalImage]
    """
    List of local images available in this version.
    """

    name: str
    """
    Name of this version.
    """

    id: str
    """
    UUID of this version.
    """

    creation_date: Optional[datetime]
    """
    Creation date of this image version.
    """

    modification_date: Optional[datetime]
    """
    Date of the last modification of this version.
    """


@dataclass
class Image:
    current_public_version: str

    organization: Organization
    """
    Organization this image belongs to.
    """

    versions: List[Version]
    """
    List of versions of this image.
    """

    label: str
    """
    Typically an identifier for a distribution (ex. "ubuntu_focal").
    """

    categories: List[str]
    """
    List of categories this image belongs to.
    """

    logo: str
    """
    URL of this image's logo.
    """

    description: str
    """
    Text description of this image.
    """

    name: str
    """
    Name of the image.
    """

    id: str
    """
    UUID of this image.
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


@dataclass
class GetImageRequest:
    image_id: str
    """
    Display the image name.
    """


@dataclass
class GetImageResponse:
    image: Image


@dataclass
class GetVersionRequest:
    version_id: str

    image_id: str


@dataclass
class GetVersionResponse:
    version: Version


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
class ListImagesResponse:
    total_count: int

    images: List[Image]


@dataclass
class ListVersionsRequest:
    image_id: str


@dataclass
class ListVersionsResponse:
    total_count: int

    versions: List[Version]
