# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

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
    eyes_color: EyeColors

    is_happy: bool

    hair_count: int

    fingers_count: int

    altitude_in_millimeter: int

    id: str

    shoe_size: float

    height: float

    name: str

    project_id: str

    organization_id: str

    status: HumanStatus

    altitude_in_meter: int

    updated_at: Optional[datetime]

    created_at: Optional[datetime]


@dataclass
class CreateHumanRequest:
    name: str

    is_happy: bool

    hair_count: int

    fingers_count: int

    altitude_in_millimeter: int

    altitude_in_meter: int

    shoe_size: float

    height: float

    eyes_color: Optional[EyeColors]

    organization_id: Optional[str]

    project_id: Optional[str]


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
    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListHumansRequestOrderBy]

    organization_id: Optional[str]

    project_id: Optional[str]


@dataclass
class ListHumansResponse:
    humans: List[Human]

    total_count: int


@dataclass
class RegisterRequest:
    username: str


@dataclass
class RegisterResponse:
    access_key: str

    secret_key: str


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

    height: Optional[float]

    shoe_size: Optional[float]

    altitude_in_meter: Optional[int]

    altitude_in_millimeter: Optional[int]

    fingers_count: Optional[int]

    hair_count: Optional[int]

    is_happy: Optional[bool]

    eyes_color: Optional[EyeColors]

    name: Optional[str]
