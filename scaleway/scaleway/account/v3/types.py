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


class ListProjectsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Project:
    id: str
    """
    ID of the Project.
    """

    name: str
    """
    Name of the Project.
    """

    organization_id: str
    """
    Organization ID of the Project.
    """

    description: str
    """
    Description of the Project.
    """

    created_at: Optional[datetime]
    """
    Creation date of the Project.
    """

    updated_at: Optional[datetime]
    """
    Update date of the Project.
    """


@dataclass
class ListProjectsResponse:
    total_count: int
    """
    Total number of Projects.
    """

    projects: List[Project]
    """
    Paginated returned Projects.
    """


@dataclass
class ProjectApiCreateProjectRequest:
    description: str
    """
    Description of the Project.
    """

    name: Optional[str]
    """
    Name of the Project.
    """

    organization_id: Optional[str]
    """
    Organization ID of the Project.
    """


@dataclass
class ProjectApiDeleteProjectRequest:
    project_id: Optional[str]
    """
    Project ID of the Project.
    """


@dataclass
class ProjectApiGetProjectRequest:
    project_id: Optional[str]
    """
    Project ID of the Project.
    """


@dataclass
class ProjectApiListProjectsRequest:
    organization_id: Optional[str]
    """
    Organization ID of the Project.
    """

    name: Optional[str]
    """
    Name of the Project.
    """

    page: Optional[int]
    """
    Page number for the returned Projects.
    """

    page_size: Optional[int]
    """
    Maximum number of Project per page.
    """

    order_by: Optional[ListProjectsRequestOrderBy]
    """
    Sort order of the returned Projects.
    """

    project_ids: Optional[List[str]]
    """
    Project IDs to filter for. The results will be limited to any Projects with an ID in this array.
    """


@dataclass
class ProjectApiUpdateProjectRequest:
    project_id: Optional[str]
    """
    Project ID of the Project.
    """

    name: Optional[str]
    """
    Name of the Project.
    """

    description: Optional[str]
    """
    Description of the Project.
    """
