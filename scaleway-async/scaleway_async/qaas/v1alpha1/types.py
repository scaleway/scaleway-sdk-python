# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Money,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class ApplicationType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    VQE = "vqe"

    def __str__(self) -> str:
        return str(self.value)


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


class ListApplicationsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    TYPE_ASC = "type_asc"
    TYPE_DESC = "type_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListJobResultsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"

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
    BACKEND_NAME_ASC = "backend_name_asc"
    BACKEND_NAME_DESC = "backend_name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListProcessResultsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListProcessesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    STARTED_AT_ASC = "started_at_asc"
    STARTED_AT_DESC = "started_at_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListSessionACLsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    ACCESS_ASC = "access_asc"
    ACCESS_DESC = "access_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListSessionsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    STARTED_AT_ASC = "started_at_asc"
    STARTED_AT_DESC = "started_at_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class PlatformAvailability(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_AVAILABILITY = "unknown_availability"
    AVAILABLE = "available"
    SHORTAGE = "shortage"
    SCARCE = "scarce"

    def __str__(self) -> str:
        return str(self.value)


class PlatformTechnology(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TECHNOLOGY = "unknown_technology"
    PHOTONIC = "photonic"
    GENERAL_PURPOSE = "general_purpose"

    def __str__(self) -> str:
        return str(self.value)


class PlatformType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    SIMULATOR = "simulator"
    QPU = "qpu"

    def __str__(self) -> str:
        return str(self.value)


class ProcessStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    ERROR = "error"
    STARTING = "starting"
    RUNNING = "running"
    COMPLETED = "completed"
    CANCELLING = "cancelling"
    CANCELLED = "cancelled"

    def __str__(self) -> str:
        return str(self.value)


class SessionAccess(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ACCESS = "unknown_access"
    FULL = "full"
    READ_SESSION = "read_session"
    READ_WRITE_SESSION = "read_write_session"
    READ_JOB_RESULT = "read_job_result"
    READ_JOB_CIRCUIT = "read_job_circuit"
    READ_JOB = "read_job"
    READ_WRITE_JOB = "read_write_job"

    def __str__(self) -> str:
        return str(self.value)


class SessionOriginType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ORIGIN_TYPE = "unknown_origin_type"
    CUSTOMER = "customer"
    PROCESS = "process"

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
class PlatformHardware:
    name: str
    """
    Product name of the hardware.
    """

    vcpus: int
    """
    Number of vCPUs available.
    """

    gpus: int
    """
    Number of GPUs available (0 if no GPU).
    """

    gpus_network: str
    """
    Network topology of GPUs (PCIe, NVLink...).
    """

    ram: int
    """
    Amount of RAM available in byte.
    """

    vram: int
    """
    Amount of VRAM available in byte (0 if no GPU).
    """


@dataclass
class JobCircuit:
    perceval_circuit: Optional[str]

    qiskit_circuit: Optional[str]


@dataclass
class Application:
    id: str
    """
    Unique ID of the application.
    """

    name: str
    """
    Name of the application.
    """

    type_: ApplicationType
    """
    Type of the application.
    """

    compatible_platform_ids: List[str]
    """
    List of compatible platform (by IDs) able to run this application.
    """

    input_template: str
    """
    JSON format describing the expected input.
    """


@dataclass
class JobResult:
    job_id: str
    """
    ID of the parent job.
    """

    result: Optional[str]
    """
    Result in JSON format.
    """

    url: Optional[str]
    """
    URL to download a large result (optional).
    """

    created_at: Optional[datetime]
    """
    Creation time of the result.
    """


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

    backend_name: str
    """
    Name of the running backend over the platform (ascella, qsim, aer...).
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
    Estimated maximum number of qubits supported by the platform.
    """

    availability: PlatformAvailability
    """
    Availability of the platform.
    """

    metadata: str
    """
    Metadata provided by the platform.
    """

    price_per_hour: Optional[Money]
    """
    Price to be payed per hour (excluding free tiers).
    """

    hardware: Optional[PlatformHardware]
    """
    Specifications of the underlying hardware.
    """


@dataclass
class ProcessResult:
    process_id: str
    """
    ID of the parent process.
    """

    result: str
    """
    Result in JSON format.
    """

    created_at: Optional[datetime]
    """
    Creation time of the result.
    """


@dataclass
class Process:
    id: str
    """
    Unique ID of the process.
    """

    name: str
    """
    Name of the process.
    """

    attached_session_ids: List[str]
    """
    List of sessions generated by the process.
    """

    application_id: Optional[str]
    """
    Application ID for which the process has been created.
    """

    status: ProcessStatus
    """
    Status of the process.
    """

    project_id: str
    """
    Project ID in which the process has been created.
    """

    tags: List[str]
    """
    Tags of the process.
    """

    platform_id: Optional[str]
    """
    Platform ID for which the process has been created.
    """

    created_at: Optional[datetime]
    """
    Tme at which the process was created.
    """

    started_at: Optional[datetime]
    """
    Time at which the process started.
    """

    updated_at: Optional[datetime]
    """
    Time at which the process was updated.
    """

    finished_at: Optional[datetime]
    """
    Time at which the process was finished.
    """

    progress: Optional[int]
    """
    Progress of the process, from 0 to 1.
    """

    progress_message: Optional[str]
    """
    Any progress of the process.
    """

    input: Optional[str]
    """
    Input payload of the process as JSON string.
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

    created_at: Optional[datetime]
    """
    The time at which the session was created.
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

    origin_type: SessionOriginType
    """
    Resource type that creates the session.
    """

    started_at: Optional[datetime]
    """
    The time at which the session started.
    """

    updated_at: Optional[datetime]
    """
    The time at which the session was updated.
    """

    terminated_at: Optional[datetime]
    """
    The time at which the session was terminated.
    """

    max_idle_duration: Optional[str]
    """
    Maximum idle time before the session ends.
    """

    max_duration: Optional[str]
    """
    Maximum duration before the session ends.
    """

    tags: Optional[List[str]]
    """
    Tags of the session.
    """

    origin_id: Optional[str]
    """
    Unique ID of the session's origin resource (if exists).
    """

    progress_message: Optional[str]
    """
    Any progress of the session.
    """


@dataclass
class CancelJobRequest:
    job_id: str
    """
    Unique ID of the job.
    """


@dataclass
class CancelProcessRequest:
    process_id: str
    """
    Unique ID of the process.
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
class CreateProcessRequest:
    name: str
    """
    Name of the process.
    """

    project_id: Optional[str]
    """
    ID of the project in which the process was created.
    """

    platform_id: Optional[str]
    """
    ID of the platform for which the process was created.
    """

    application_id: Optional[str]
    """
    ID of the application for which the process was created.
    """

    input: Optional[str]
    """
    Process parameters in JSON format.
    """

    tags: Optional[List[str]]
    """
    Tags of the process.
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
class DeleteJobRequest:
    job_id: str
    """
    Unique ID of the job.
    """


@dataclass
class DeleteProcessRequest:
    process_id: str
    """
    Unique ID of the process.
    """


@dataclass
class DeleteSessionRequest:
    session_id: str
    """
    Unique ID of the session.
    """


@dataclass
class GetApplicationRequest:
    application_id: str
    """
    Unique ID of the application.
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
class GetProcessRequest:
    process_id: str
    """
    Unique ID of the process.
    """


@dataclass
class GetSessionRequest:
    session_id: str
    """
    Unique ID of the session.
    """


@dataclass
class ListApplicationsRequest:
    name: Optional[str]
    """
    List applications with this name.
    """

    application_type: Optional[ApplicationType]
    """
    List applications with this type.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Maximum number of applications a to return per page.
    """

    order_by: Optional[ListApplicationsRequestOrderBy]
    """
    Sort order of the returned applications.
    """


@dataclass
class ListApplicationsResponse:
    total_count: int
    """
    Total number of applications.
    """

    applications: List[Application]
    """
    List of applications.
    """


@dataclass
class ListJobResultsRequest:
    job_id: str
    """
    ID of the job.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Maximum number of results to return per page.
    """

    order_by: Optional[ListJobResultsRequestOrderBy]
    """
    Sort order of the returned results.
    """


@dataclass
class ListJobResultsResponse:
    total_count: int
    """
    Total number of results.
    """

    job_results: List[JobResult]
    """
    List of results.
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

    backend_name: Optional[str]
    """
    List platforms with this backend name.
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
class ListProcessResultsRequest:
    process_id: str
    """
    ID of the process.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Maximum number of results to return per page.
    """

    order_by: Optional[ListProcessResultsRequestOrderBy]
    """
    Sort order of the returned results.
    """


@dataclass
class ListProcessResultsResponse:
    total_count: int
    """
    Total number of results.
    """

    process_results: List[ProcessResult]
    """
    List of results.
    """


@dataclass
class ListProcessesRequest:
    application_id: Optional[str]
    """
    List processes that have been created for this application.
    """

    tags: Optional[List[str]]
    """
    List processes with these tags.
    """

    page: Optional[int]
    """
    Page number.
    """

    page_size: Optional[int]
    """
    Maximum number of processes to return per page.
    """

    order_by: Optional[ListProcessesRequestOrderBy]
    """
    Sort order of the returned processes.
    """

    project_id: Optional[str]
    """
    List processes belonging to this project ID.
    """


@dataclass
class ListProcessesResponse:
    total_count: int
    """
    Total number of processes.
    """

    processes: List[Process]
    """
    List of processes.
    """


@dataclass
class ListSessionACLsRequest:
    session_id: str

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListSessionACLsRequestOrderBy]


@dataclass
class ListSessionACLsResponse:
    total_count: int

    acls: List[SessionAccess]


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
class TerminateSessionRequest:
    session_id: str
    """
    Unique ID of the session.
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
class UpdateProcessRequest:
    process_id: str
    """
    Unique ID of the process.
    """

    name: Optional[str]
    """
    Name of the process.
    """

    tags: Optional[List[str]]
    """
    Tags of the process.
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
    Maximum time before the session ends.
    """

    tags: Optional[List[str]]
    """
    Tags of the session.
    """
