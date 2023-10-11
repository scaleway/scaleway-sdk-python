# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class ListPinsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListVolumesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class PinDetails(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_DETAILS = "unknown_details"
    PINNING_LOOKING_FOR_PROVIDER = "pinning_looking_for_provider"
    PINNING_IN_PROGRESS = "pinning_in_progress"
    PINNING_BLOCKS_FETCHED = "pinning_blocks_fetched"
    PINNING_FETCHING_URL_DATA = "pinning_fetching_url_data"
    PINNED_OK = "pinned_ok"
    UNPINNED_OK = "unpinned_ok"
    UNPINNING_IN_PROGRESS = "unpinning_in_progress"
    FAILED_CONTAINS_BANNED_CID = "failed_contains_banned_cid"
    FAILED_PINNING = "failed_pinning"
    FAILED_PINNING_NO_PROVIDER = "failed_pinning_no_provider"
    FAILED_PINNING_BAD_CID_FORMAT = "failed_pinning_bad_cid_format"
    FAILED_PINNING_TIMEOUT = "failed_pinning_timeout"
    FAILED_PINNING_TOO_BIG_CONTENT = "failed_pinning_too_big_content"
    FAILED_PINNING_UNREACHABLE_URL = "failed_pinning_unreachable_url"
    FAILED_PINNING_BAD_URL_FORMAT = "failed_pinning_bad_url_format"
    FAILED_PINNING_NO_URL_CONTENT_LENGTH = "failed_pinning_no_url_content_length"
    FAILED_PINNING_BAD_URL_STATUS_CODE = "failed_pinning_bad_url_status_code"
    FAILED_UNPINNING = "failed_unpinning"
    CHECKING_COHERENCE = "checking_coherence"
    RESCHEDULED = "rescheduled"

    def __str__(self) -> str:
        return str(self.value)


class PinStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    QUEUED = "queued"
    PINNING = "pinning"
    FAILED = "failed"
    PINNED = "pinned"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class PinCIDMeta:
    id: Optional[str]


@dataclass
class PinCID:
    meta: PinCIDMeta

    origins: List[str]

    cid: Optional[str]

    name: Optional[str]


@dataclass
class PinInfo:
    status_details: PinDetails

    id: Optional[str]

    url: Optional[str]

    size: Optional[int]

    progress: Optional[int]


@dataclass
class PinOptions:
    replication_count: int

    required_zones: List[str]


@dataclass
class Pin:
    info: PinInfo

    delegates: List[str]

    cid: PinCID

    status: PinStatus

    pin_id: str

    created_at: Optional[datetime]


@dataclass
class Volume:
    name: str

    tags: List[str]

    count_pin: int

    region: Region
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: str

    id: str

    created_at: Optional[datetime]

    updated_at: Optional[datetime]

    size: Optional[int]


@dataclass
class CreatePinByCIDRequest:
    pin_options: PinOptions
    """
    Pin options.
    """

    cid: str
    """
    CID containing the content you want to pin.
    """

    volume_id: str
    """
    Volume ID on which you want to pin your content.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    origins: Optional[List[str]]
    """
    Node containing the content you want to pin.
    """

    name: Optional[str]
    """
    Pin name.
    """


@dataclass
class CreatePinByURLRequest:
    pin_options: PinOptions
    """
    Pin options.
    """

    url: str
    """
    URL containing the content you want to pin.
    """

    volume_id: str
    """
    Volume ID on which you want to pin your content.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Pin name.
    """


@dataclass
class CreateVolumeRequest:
    name: str
    """
    Volume name.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project ID.
    """


@dataclass
class DeletePinRequest:
    volume_id: str
    """
    Volume ID.
    """

    pin_id: str
    """
    Pin ID you want to remove from the volume.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteVolumeRequest:
    volume_id: str
    """
    Volume ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetPinRequest:
    volume_id: str
    """
    Volume ID.
    """

    pin_id: str
    """
    Pin ID of which you want to obtain information.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetVolumeRequest:
    volume_id: str
    """
    Volume ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListPinsRequest:
    volume_id: str
    """
    Volume ID of which you want to list the pins.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project ID.
    """

    organization_id: Optional[str]
    """
    Organization ID.
    """

    order_by: Optional[ListPinsRequestOrderBy]
    """
    Sort order of the returned Volume.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Maximum number of volumes to return per page.
    """

    status: Optional[PinStatus]
    """
    List pins by status.
    """


@dataclass
class ListPinsResponse:
    pins: List[Pin]

    total_count: int


@dataclass
class ListVolumesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project ID, only volumes belonging to this project will be listed.
    """

    order_by: Optional[ListVolumesRequestOrderBy]
    """
    Sort the order of the returned volumes.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Maximum number of volumes to return per page.
    """


@dataclass
class ListVolumesResponse:
    total_count: int

    volumes: List[Volume]


@dataclass
class ReplacePinRequest:
    pin_options: PinOptions
    """
    Pin options.
    """

    cid: str
    """
    New CID you want to pin in place of the old one.
    """

    volume_id: str
    """
    Volume ID.
    """

    pin_id: str
    """
    Pin ID whose information you wish to replace.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    New name to replace.
    """

    origins: Optional[List[str]]
    """
    Node containing the content you want to pin.
    """


@dataclass
class ReplacePinResponse:
    pin: Pin


@dataclass
class UpdateVolumeRequest:
    volume_id: str
    """
    Volume ID.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Volume name.
    """

    tags: Optional[List[str]]
    """
    Tags of the volume.
    """
