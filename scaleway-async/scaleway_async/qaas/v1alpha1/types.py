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


class JobStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    WAITING = "waiting"
    ERROR = "error"
    RUNNING = "running"
    COMPLETED = "completed"
    CANCELLING = "cancelling"
    CANCELLED = "cancelled"

    def __str__(self) -> str:
        return str(self.value)


class ListJobsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"
    PLATFORM_NAME_ASC = "platform_name_asc"
    PLATFORM_NAME_DESC = "platform_name_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    SESSION_NAME_ASC = "session_name_asc"
    SESSION_NAME_DESC = "session_name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPlatformsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    PROVIDER_NAME_ASC = "provider_name_asc"
    PROVIDER_NAME_DESC = "provider_name_desc"
    TYPE_ASC = "type_asc"
    TYPE_DESC = "type_desc"
    TECHNOLOGY_ASC = "technology_asc"
    TECHNOLOGY_DESC = "technology_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListSessionsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    STARTED_AT_ASC = "started_at_asc"
    STARTED_AT_DESC = "started_at_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"

    def __str__(self) -> str:
        return str(self.value)


class PlatformTechnology(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TECHNOLOGY = "unknown_technology"
    PHOTONIC = "photonic"

    def __str__(self) -> str:
        return str(self.value)


class PlatformType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    SIMULATOR = "simulator"
    QPU = "qpu"

    def __str__(self) -> str:
        return str(self.value)


class SessionStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    RUNNING = "running"
    STOPPED = "stopped"
    STARTING = "starting"
    STOPPING = "stopping"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class JobCircuit:
    perceval_circuit: Optional[str]


@dataclass
class Job:
    id: str
    """
    Unique ID of the job.
    """

    name: str
    """
    Job name.
    """

    session_id: str
    """
    Session ID in which the job is executed.
    """

    status: JobStatus
    """
    Job status.
    """

    tags: Optional[List[str]]
    """
    Tags of the job.
    """

    created_at: Optional[datetime]
    """
    Time at which the job was created.
    """

    started_at: Optional[datetime]
    """
    Time at which the job was started.
    """

    updated_at: Optional[datetime]
    """
    Time at which the job was updated.
    """

    progress_message: Optional[str]
    """
    Last progress message, if the job has started.
    """

    job_duration: Optional[str]
    """
    Duration of the job, if the job is finished.
    """

    result_distribution: Optional[str]
    """
    Result of the job, if the job is finished.
    """


@dataclass
class Platform:
    id: str
    """
    Unique ID of the platform.
    """

    version: str
    """
    Verison of the platform.
    """

    name: str
    """
    Name of the platform.
    """

    provider_name: str
    """
    Provider name of the platform.
    """

    type_: PlatformType
    """
    Type of the platform.
    """

    technology: PlatformTechnology
    """
    Technology used by the platform.
    """

    max_qubit_count: int
    """
    Maximum number of qubits supported by the platform.
    """

    metadata: str
    """
    Metadata provided by the platform.
    """


@dataclass
class Session:
    id: str
    """
    Unique ID of the session.
    """

    name: str
    """
    Name of the session.
    """

    platform_id: str
    """
    Platform ID for which the session has been created.
    """

    waiting_job_count: int
    """
    Number of waiting jobs linked to the session.
    """

    finished_job_count: int
    """
    Number of finished jobs linked to the session.
    """

    status: SessionStatus
    """
    Status of the session.
    """

    project_id: str
    """
    Project ID in which the session has been created.
    """

    deduplication_id: str
    """
    Deduplication ID of the session.
    """

    created_at: Optional[datetime]
    """
    Time at which the session has been created.
    """

    started_at: Optional[datetime]
    """
    Time at which the session has been started.
    """

    update_at: Optional[datetime]
    """
    Time at which the session has been updated.
    """

    max_idle_duration: Optional[str]
    """
    Maximum idle duration before the session ends.
    """

    max_duration: Optional[str]
    """
    Maximum duration before the session ends.
    """

    tags: Optional[List[str]]
    """
    Tags of the session.
    """


@dataclass
class CancelJobRequest:
    job_id: str
    """
    Unique ID of the job.
    """


@dataclass
class CreateJobRequest:
    name: str
    """
    Name of the job.
    """

    session_id: str
    """
    Session in which the job is executed.
    """

    circuit: JobCircuit
    """
    Quantum circuit that should be executed.
    """

    tags: Optional[List[str]]
    """
    Tags of the job.
    """

    max_duration: Optional[str]
    """
    Maximum duration of the job.
    """


@dataclass
class CreateSessionRequest:
    platform_id: str
    """
    ID of the Platform for which the session was created.
    """

    project_id: Optional[str]
    """
    ID of the Project in which the session was created.
    """

    name: Optional[str]
    """
    Name of the session.
    """

    max_idle_duration: Optional[str]
    """
    Maximum idle duration before the session ends.
    """

    max_duration: Optional[str]
    """
    Maximum duration before the session ends.
    """

    tags: Optional[List[str]]
    """
    Tags of the session.
    """

    deduplication_id: Optional[str]
    """
    Deduplication ID of the session.
    """


@dataclass
class DeleteSessionRequest:
    session_id: str
    """
    Unique ID of the session.
    """


@dataclass
class GetJobCircuitRequest:
    job_id: str
    """
    Unique ID of the job.
    """


@dataclass
class GetJobRequest:
    job_id: str
    """
    Unique ID of the job you want to get.
    """


@dataclass
class GetPlatformRequest:
    platform_id: str
    """
    Unique ID of the platform.
    """


@dataclass
class GetSessionRequest:
    session_id: str
    """
    Unique ID of the session.
    """


@dataclass
class ListJobsRequest:
    tags: Optional[List[str]]
    """
    List jobs with these tags.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Maximum number of jobs to return per page.
    """

    order_by: Optional[ListJobsRequestOrderBy]
    """
    Sort order of the returned jobs.
    """

    session_id: Optional[str]

    project_id: Optional[str]


@dataclass
class ListJobsResponse:
    total_count: int
    """
    Total number of jobs.
    """

    jobs: List[Job]
    """
    List of jobs.
    """


@dataclass
class ListPlatformsRequest:
    provider_name: Optional[str]
    """
    List platforms with this provider name.
    """

    name: Optional[str]
    """
    List platforms with this name.
    """

    platform_type: Optional[PlatformType]
    """
    List platforms with this type.
    """

    platform_technology: Optional[PlatformTechnology]
    """
    List platforms with this technology.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Maximum number of platforms to return per page.
    """

    order_by: Optional[ListPlatformsRequestOrderBy]
    """
    Sort order of the returned platforms.
    """


@dataclass
class ListPlatformsResponse:
    total_count: int
    """
    Total number of platforms.
    """

    platforms: List[Platform]
    """
    List of platforms.
    """


@dataclass
class ListSessionsRequest:
    platform_id: Optional[str]
    """
    List sessions that have been created for this platform.
    """

    tags: Optional[List[str]]
    """
    List sessions with these tags.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Maximum number of sessions to return per page.
    """

    order_by: Optional[ListSessionsRequestOrderBy]
    """
    Sort order of the returned sessions.
    """

    project_id: Optional[str]
    """
    List sessions belonging to this project ID.
    """


@dataclass
class ListSessionsResponse:
    total_count: int
    """
    Total number of sessions.
    """

    sessions: List[Session]
    """
    List of sessions.
    """


@dataclass
class UpdateJobRequest:
    job_id: str
    """
    Unique ID of the job.
    """

    name: Optional[str]
    """
    Name of the job.
    """

    tags: Optional[List[str]]
    """
    Tags of the job.
    """


@dataclass
class UpdateSessionRequest:
    session_id: str
    """
    Unique ID of the session.
    """

    name: Optional[str]
    """
    Name of the session.
    """

    max_idle_duration: Optional[str]
    """
    Maximum idle duration before the session ends.
    """

    max_duration: Optional[str]
    """
    Maximum duration before the session ends.
    """

    tags: Optional[List[str]]
    """
    Tags of the session.
    """
