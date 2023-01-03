# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional


class ListProjectsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class ListProjectsResponse:
    """
    List projects response
    """

    total_count: int
    """
    The total number of projects
    """

    projects: List[Project]
    """
    The paginated returned projects
    """


@dataclass
class Project:
    """
    Project
    """

    id: str
    """
    The ID of the project
    """

    name: str
    """
    The name of the project
    """

    organization_id: str
    """
    The organization ID of the project
    """

    created_at: Optional[datetime]
    """
    The creation date of the project
    """

    updated_at: Optional[datetime]
    """
    The update date of the project
    """

    description: str
    """
    The description of the project
    """


@dataclass
class CreateProjectRequest:
    name: str
    """
    The name of the project
    """

    organization_id: Optional[str]
    """
    The organization ID of the project
    """

    description: Optional[str]
    """
    The description of the project
    """


@dataclass
class ListProjectsRequest:
    organization_id: Optional[str]
    """
    The organization ID of the project
    """

    name: Optional[str]
    """
    The name of the project
    """

    page: Optional[int]
    """
    The page number for the returned projects
    """

    page_size: Optional[int]
    """
    The maximum number of project per page
    """

    order_by: Optional[ListProjectsRequestOrderBy]
    """
    The sort order of the returned projects
    """

    project_ids: Optional[List[str]]
    """
    Filter out by a list of project ID
    """


@dataclass
class GetProjectRequest:
    project_id: Optional[str]
    """
    The project ID of the project
    """


@dataclass
class DeleteProjectRequest:
    project_id: Optional[str]
    """
    The project ID of the project
    """


@dataclass
class UpdateProjectRequest:
    project_id: Optional[str]
    """
    The project ID of the project
    """

    name: Optional[str]
    """
    The name of the project
    """

    description: Optional[str]
    """
    The description of the project
    """
