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
    INTERNAL_ERROR = "internal_error"

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
class CronSchedule:
    schedule: str
    """
    UNIX cron schedule to run job (e.g., '* * * * *').
    """

    timezone: str
    """
    Timezone for the cron schedule, in tz database format (e.g., 'Europe/Paris').
    """


@dataclass
class CreateJobDefinitionRequestCronScheduleConfig:
    schedule: str

    timezone: str


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

    local_storage_capacity: int

    region: Region
    """
    Region to target. If none is passed will use default region from the config.
    """

    job_timeout: Optional[str]

    cron_schedule: Optional[CronSchedule]


@dataclass
class JobRun:
    id: str

    job_definition_id: str

    state: JobRunState

    error_message: str

    cpu_limit: int

    memory_limit: int

    command: str

    created_at: Optional[datetime]

    updated_at: Optional[datetime]

    terminated_at: Optional[datetime]

    exit_code: Optional[int]

    run_duration: Optional[str]

    environment_variables: Dict[str, str]

    local_storage_capacity: int

    region: Region
    """
    Region to target. If none is passed will use default region from the config.
    """

    started_at: Optional[datetime]


@dataclass
class Resource:
    cpu_limit: int

    memory_limit: int


@dataclass
class UpdateJobDefinitionRequestCronScheduleConfig:
    schedule: Optional[str]

    timezone: Optional[str]


@dataclass
class CreateJobDefinitionRequest:
    cpu_limit: int
    """
    CPU limit of the job.
    """

    memory_limit: int
    """
    Memory limit of the job (in MiB).
    """

    image_uri: str
    """
    Image to use for the job.
    """

    command: str
    """
    Startup command. If empty or not defined, the image's default command is used.
    """

    description: str
    """
    Description of the job.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the job definition.
    """

    local_storage_capacity: Optional[int]
    """
    Local storage capacity of the job (in MiB).
    """

    project_id: Optional[str]
    """
    UUID of the Scaleway Project containing the job.
    """

    environment_variables: Optional[Dict[str, str]]
    """
    Environment variables of the job.
    """

    job_timeout: Optional[str]
    """
    Timeout of the job in seconds.
    """

    cron_schedule: Optional[CreateJobDefinitionRequestCronScheduleConfig]
    """
    Configure a cron for the job.
    """


@dataclass
class DeleteJobDefinitionRequest:
    job_definition_id: str
    """
    UUID of the job definition to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetJobDefinitionRequest:
    job_definition_id: str
    """
    UUID of the job definition to get.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetJobRunRequest:
    job_run_id: str
    """
    UUID of the job run to get.
    """

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

    organization_id: Optional[str]


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

    organization_id: Optional[str]


@dataclass
class ListJobRunsResponse:
    job_runs: List[JobRun]

    total_count: int


@dataclass
class ListJobsResourcesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListJobsResourcesResponse:
    resources: List[Resource]


@dataclass
class StartJobDefinitionRequest:
    job_definition_id: str
    """
    UUID of the job definition to start.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    command: Optional[str]
    """
    Contextual startup command for this specific job run.
    """

    environment_variables: Optional[Dict[str, str]]
    """
    Contextual environment variables for this specific job run.
    """

    replicas: Optional[int]
    """
    Number of jobs to run.
    """


@dataclass
class StartJobDefinitionResponse:
    job_runs: List[JobRun]


@dataclass
class StopJobRunRequest:
    job_run_id: str
    """
    UUID of the job run to stop.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class UpdateJobDefinitionRequest:
    job_definition_id: str
    """
    UUID of the job definition to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the job definition.
    """

    cpu_limit: Optional[int]
    """
    CPU limit of the job.
    """

    memory_limit: Optional[int]
    """
    Memory limit of the job (in MiB).
    """

    local_storage_capacity: Optional[int]
    """
    Local storage capacity of the job (in MiB).
    """

    image_uri: Optional[str]
    """
    Image to use for the job.
    """

    command: Optional[str]
    """
    Startup command.
    """

    environment_variables: Optional[Dict[str, str]]
    """
    Environment variables of the job.
    """

    description: Optional[str]
    """
    Description of the job.
    """

    job_timeout: Optional[str]
    """
    Timeout of the job in seconds.
    """

    cron_schedule: Optional[UpdateJobDefinitionRequestCronScheduleConfig]
