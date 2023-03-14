# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional


class EyeColors(str, Enum):
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


class HumanStatus(str, Enum):
    UNKNOWN = "unknown"
    STOPPED = "stopped"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)


class ListHumansRequestOrderBy(str, Enum):
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

    created_at: Optional[datetime]

    updated_at: Optional[datetime]

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


@dataclass
class ListHumansResponse:
    total_count: int

    humans: List[Human]


@dataclass
class RegisterResponse:
    secret_key: str

    access_key: str


@dataclass
class RegisterRequest:
    username: str


@dataclass
class ListHumansRequest:
    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListHumansRequestOrderBy]

    organization_id: Optional[str]

    project_id: Optional[str]


@dataclass
class GetHumanRequest:
    human_id: str
    """
    UUID of the human you want to get.
    """


@dataclass
class CreateHumanRequest:
    height: float

    shoe_size: float

    altitude_in_meter: int

    altitude_in_millimeter: int

    fingers_count: int

    hair_count: int

    is_happy: bool

    eyes_color: EyeColors

    organization_id: Optional[str]
    """
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
    :deprecated
    """

    name: str

    project_id: Optional[str]
    """
    One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
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

    eyes_color: EyeColors

    name: Optional[str]


@dataclass
class DeleteHumanRequest:
    human_id: str
    """
    UUID of the human you want to delete.
    """


@dataclass
class RunHumanRequest:
    human_id: str
    """
    UUID of the human you want to make run.
    """


@dataclass
class SmokeHumanRequest:
    human_id: Optional[str]
    """
    UUID of the human you want to make smoking.
    :deprecated
    """
