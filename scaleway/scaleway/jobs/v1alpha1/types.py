# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class JobRunState(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATE = "unknown_state"
    QUEUED = "queued"
    SCHEDULED = "scheduled"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELED = "canceled"

    def __str__(self) -> str:
        return str(self.value)


class ListJobDefinitionsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListJobRunsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class JobDefinition:
    id: str

    name: str

    cpu_limit: int

    memory_limit: int

    image_uri: str

    command: str

    project_id: str

    created_at: Optional[datetime]

    updated_at: Optional[datetime]

    environment_variables: Dict[str, str]

    description: str

    region: Region
    """
    Region to target. If none is passed will use default region from the config.
    """

    job_timeout: Optional[str]


@dataclass
class JobRun:
    id: str

    job_definition_id: str

    state: JobRunState

    error_message: str

    region: Region
    """
    Region to target. If none is passed will use default region from the config.
    """

    created_at: Optional[datetime]

    updated_at: Optional[datetime]

    terminated_at: Optional[datetime]

    exit_code: Optional[int]

    run_duration: Optional[str]


@dataclass
class CreateJobDefinitionRequest:
    cpu_limit: int

    memory_limit: int

    image_uri: str

    command: str

    description: str

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]

    project_id: Optional[str]

    environment_variables: Optional[Dict[str, str]]

    job_timeout: Optional[str]


@dataclass
class DeleteJobDefinitionRequest:
    job_definition_id: str

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetJobDefinitionRequest:
    job_definition_id: str

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetJobRunRequest:
    job_run_id: str

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetServiceInfoRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListJobDefinitionsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListJobDefinitionsRequestOrderBy]

    project_id: Optional[str]


@dataclass
class ListJobDefinitionsResponse:
    job_definitions: List[JobDefinition]

    total_count: int


@dataclass
class ListJobRunsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListJobRunsRequestOrderBy]

    job_definition_id: Optional[str]

    project_id: Optional[str]


@dataclass
class ListJobRunsResponse:
    job_runs: List[JobRun]

    total_count: int


@dataclass
class StartJobDefinitionRequest:
    job_definition_id: str

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class StopJobRunRequest:
    job_run_id: str

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class UpdateJobDefinitionRequest:
    job_definition_id: str

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]

    cpu_limit: Optional[int]

    memory_limit: Optional[int]

    image_uri: Optional[str]

    command: Optional[str]

    environment_variables: Optional[Dict[str, str]]

    description: Optional[str]

    job_timeout: Optional[str]
