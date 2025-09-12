# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.utils import (
    StrEnumMeta,
)


class EyeColors(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    AMBER = "amber"
    BLUE = "blue"
    BROWN = "brown"
    GRAY = "gray"
    GREEN = "green"
    HAZEL = "hazel"
    RED = "red"
    VIOLET = "violet"

    def __str__(self) -> str:
        return str(self.value)


class HumanStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    STOPPED = "stopped"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)


class ListHumansRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    HEIGHT_ASC = "height_asc"
    HEIGHT_DESC = "height_desc"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Human:
    id: str
    organization_id: str
    height: float
    shoe_size: float
    altitude_in_meter: int
    altitude_in_millimeter: int
    fingers_count: int
    hair_count: int
    is_happy: bool
    eyes_color: EyeColors
    status: HumanStatus
    name: str
    project_id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class CreateHumanRequest:
    height: float
    shoe_size: float
    altitude_in_meter: int
    altitude_in_millimeter: int
    fingers_count: int
    hair_count: int
    is_happy: bool
    name: str
    eyes_color: Optional[EyeColors] = None
    project_id: Optional[str] = None

    organization_id: Optional[str] = None


@dataclass
class DeleteHumanRequest:
    human_id: str
    """
    UUID of the human you want to delete.
    """


@dataclass
class GetHumanRequest:
    human_id: str
    """
    UUID of the human you want to get.
    """


@dataclass
class ListHumansRequest:
    page: Optional[int] = None
    page_size: Optional[int] = None
    order_by: Optional[ListHumansRequestOrderBy] = None
    organization_id: Optional[str] = None
    project_id: Optional[str] = None


@dataclass
class ListHumansResponse:
    total_count: int
    humans: list[Human]


@dataclass
class RegisterRequest:
    username: str


@dataclass
class RegisterResponse:
    secret_key: str
    access_key: str


@dataclass
class RunHumanRequest:
    human_id: str
    """
    UUID of the human you want to make run.
    """


@dataclass
class SmokeHumanRequest:
    human_id: str
    """
    UUID of the human you want to make smoking.
    """


@dataclass
class UpdateHumanRequest:
    human_id: str
    """
    UUID of the human you want to update.
    """

    height: Optional[float] = 0.0
    """
    Height of the human in meters.
    """

    shoe_size: Optional[float] = 0.0
    altitude_in_meter: Optional[int] = 0
    altitude_in_millimeter: Optional[int] = 0
    fingers_count: Optional[int] = 0
    hair_count: Optional[int] = 0
    is_happy: Optional[bool] = False
    eyes_color: Optional[EyeColors] = EyeColors.UNKNOWN
    name: Optional[str] = None
