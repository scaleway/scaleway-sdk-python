# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

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


class BookingStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    WAITING = "waiting"
    VALIDATING = "validating"
    VALIDATED = "validated"
    CANCELLING = "cancelling"
    CANCELLED = "cancelled"
    ERROR = "error"

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


class ListBookingsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"
    STARTED_AT_DESC = "started_at_desc"
    STARTED_AT_ASC = "started_at_asc"

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


class ListModelsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"

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
    MAINTENANCE = "maintenance"

    def __str__(self) -> str:
        return str(self.value)


class PlatformTechnology(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TECHNOLOGY = "unknown_technology"
    PHOTONIC = "photonic"
    GENERAL_PURPOSE = "general_purpose"
    TRAPPED_ION = "trapped_ion"
    SUPERCONDUCTING = "superconducting"
    NEUTRAL_ATOM = "neutral_atom"

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
class PlatformBookingRequirement:
    max_booking_per_week: int
    """
    Maximum amount of booking allowed for one organization per week.
    """

    max_booking_per_day: int
    """
    Maximum amount of booking allowed for one organization per day.
    """

    min_duration: Optional[str] = None
    """
    Minimal duration of any booking based on this platform.
    """

    max_duration: Optional[str] = None
    """
    Maximal duration of any bookings based on this platform.
    """

    max_cancellation_duration: Optional[str] = None
    """
    Allowed time to cancel a booking attached to this platform before the beginning of the session.
    """

    max_planification_duration: Optional[str] = None
    """
    Allowed planification time from now where the platform can be booked in the future.
    """

    min_planification_duration: Optional[str] = None
    """
    Minimum planification time before a platform can be booked.
    """


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
    perceval_circuit: Optional[str] = None

    qiskit_circuit: Optional[str] = None


@dataclass
class CreateSessionRequestBookingDemand:
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    description: Optional[str] = None


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

    compatible_platform_ids: list[str]
    """
    List of compatible platform (by IDs) able to run this application.
    """

    input_template: str
    """
    JSON format describing the expected input.
    """


@dataclass
class Booking:
    id: str
    """
    Unique ID of the booking.
    """

    status: BookingStatus
    """
    Status of the booking.
    """

    description: str
    """
    Description of the booking slot.
    """

    progress_message: str
    """
    Any progress message of the booking.
    """

    created_at: Optional[datetime] = None
    """
    Time at which the booking was created.
    """

    started_at: Optional[datetime] = None
    """
    Time at which the booking starts.
    """

    updated_at: Optional[datetime] = None
    """
    Time at which the booking was updated.
    """

    finished_at: Optional[datetime] = None
    """
    Time at which the booking finishes.
    """


@dataclass
class JobResult:
    job_id: str
    """
    ID of the parent job.
    """

    result: Optional[str] = None
    """
    Result in JSON format.
    """

    url: Optional[str] = None
    """
    URL to download a large result (optional).
    """

    created_at: Optional[datetime] = None
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

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the job.
    """

    created_at: Optional[datetime] = None
    """
    Time at which the job was created.
    """

    started_at: Optional[datetime] = None
    """
    Time at which the job was started.
    """

    updated_at: Optional[datetime] = None
    """
    Time at which the job was updated.
    """

    progress_message: Optional[str] = None
    """
    Last progress message, if the job has started.
    """

    job_duration: Optional[str] = None
    """
    Duration of the job, if the job is finished.
    """

    result_distribution: Optional[str] = None
    """
    Result of the job, if the job is finished.
    """

    model_id: Optional[str] = None
    """
    Computation model ID executed by the job.
    """

    parameters: Optional[str] = None
    """
    Execution parameters for this job.
    """


@dataclass
class Model:
    id: str
    """
    Unique ID of the model.
    """

    project_id: str
    """
    Project ID in which the model has been created.
    """

    created_at: Optional[datetime] = None
    """
    Time at which the model was created.
    """

    url: Optional[str] = None
    """
    Storage URL of the model.
    """


@dataclass
class Platform:
    id: str
    """
    Unique ID of the platform.
    """

    version: str
    """
    Version of the platform.
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

    max_shot_count: int
    """
    Maximum number of shots during a circuit execution.
    """

    max_circuit_count: int
    """
    Maximum number of circuit that can be executed in one call.
    """

    availability: PlatformAvailability
    """
    Availability of the platform.
    """

    metadata: str
    """
    Metadata provided by the platform.
    """

    description: str
    """
    English description of the platform.
    """

    documentation_url: str
    """
    Documentation link to external documentation to learn more on this platform.
    """

    is_bookable: bool
    """
    Specify if the platform is bookable.
    """

    price_per_hour: Optional[Money] = None
    """
    Price to be paid per hour (excluding free tiers).
    """

    price_per_shot: Optional[Money] = None
    """
    Price to be paid per shot (excluding free tiers).
    """

    price_per_circuit: Optional[Money] = None
    """
    Price to be paid per circuit setup before its execution (excluding free tiers).
    """

    hardware: Optional[PlatformHardware] = None
    """
    Specifications of the underlying hardware.
    """

    booking_requirement: Optional[PlatformBookingRequirement] = None
    """
    Booking constraints to fit if the platform is bookable.
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

    created_at: Optional[datetime] = None
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

    attached_session_ids: list[str]
    """
    List of sessions generated by the process.
    """

    status: ProcessStatus
    """
    Status of the process.
    """

    project_id: str
    """
    Project ID in which the process has been created.
    """

    tags: list[str]
    """
    Tags of the process.
    """

    application_id: Optional[str] = None
    """
    Application ID for which the process has been created.
    """

    platform_id: Optional[str] = None
    """
    Platform ID for which the process has been created.
    """

    created_at: Optional[datetime] = None
    """
    Time at which the process was created.
    """

    started_at: Optional[datetime] = None
    """
    Time at which the process started.
    """

    updated_at: Optional[datetime] = None
    """
    Time at which the process was updated.
    """

    finished_at: Optional[datetime] = None
    """
    Time at which the process was finished.
    """

    progress: Optional[int] = 0
    """
    Progress of the process, from 0 to 1.
    """

    progress_message: Optional[str] = None
    """
    Any progress of the process.
    """

    input: Optional[str] = None
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

    created_at: Optional[datetime] = None
    """
    The time at which the session was created.
    """

    started_at: Optional[datetime] = None
    """
    The time at which the session started.
    """

    updated_at: Optional[datetime] = None
    """
    The time at which the session was updated.
    """

    terminated_at: Optional[datetime] = None
    """
    The time at which the session was terminated.
    """

    max_idle_duration: Optional[str] = None
    """
    Maximum idle time before the session ends.
    """

    max_duration: Optional[str] = None
    """
    Maximum duration before the session ends.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the session.
    """

    origin_id: Optional[str] = None
    """
    Unique ID of the session's origin resource (if exists).
    """

    progress_message: Optional[str] = None
    """
    Any progress of the session.
    """

    booking_id: Optional[str] = None
    """
    An optional booking unique ID of an attached booking.
    """

    model_id: Optional[str] = None
    """
    Default computation model ID to be executed by job assigned to this session.
    """

    parameters: Optional[str] = None
    """
    Platform configuration parameters applied to this session.
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

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the job.
    """

    max_duration: Optional[str] = None
    """
    Maximum duration of the job.
    """

    model_id: Optional[str] = None
    """
    Computation model ID to be executed by the job.
    """

    parameters: Optional[str] = None
    """
    Execution parameters for this job.
    """


@dataclass
class CreateModelRequest:
    project_id: Optional[str] = None
    """
    Project ID to attach this model.
    """

    payload: Optional[str] = None
    """
    The serialized model data.
    """


@dataclass
class CreateProcessRequest:
    name: str
    """
    Name of the process.
    """

    project_id: Optional[str] = None
    """
    ID of the project in which the process was created.
    """

    platform_id: Optional[str] = None
    """
    ID of the platform for which the process was created.
    """

    application_id: Optional[str] = None
    """
    ID of the application for which the process was created.
    """

    input: Optional[str] = None
    """
    Process parameters in JSON format.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the process.
    """


@dataclass
class CreateSessionRequest:
    platform_id: str
    """
    ID of the Platform for which the session was created.
    """

    project_id: Optional[str] = None
    """
    ID of the Project in which the session was created.
    """

    name: Optional[str] = None
    """
    Name of the session.
    """

    max_idle_duration: Optional[str] = None
    """
    Maximum idle duration before the session ends.
    """

    max_duration: Optional[str] = None
    """
    Maximum duration before the session ends.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the session.
    """

    deduplication_id: Optional[str] = None
    """
    Deduplication ID of the session.
    """

    booking_demand: Optional[CreateSessionRequestBookingDemand] = None
    """
    A booking demand to schedule the session, only applicable if the platform is bookable.
    """

    model_id: Optional[str] = None
    """
    Default computation model ID to be executed by job assigned to this session.
    """

    parameters: Optional[str] = None
    """
    Optional platform configuration parameters applied to this session.
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
class GetBookingRequest:
    booking_id: str
    """
    Unique ID of the booking.
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
class GetModelRequest:
    model_id: str
    """
    Unique ID of the model.
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
    name: Optional[str] = None
    """
    List applications with this name.
    """

    application_type: Optional[ApplicationType] = ApplicationType.UNKNOWN_TYPE
    """
    List applications with this type.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of applications a to return per page.
    """

    order_by: Optional[ListApplicationsRequestOrderBy] = (
        ListApplicationsRequestOrderBy.NAME_ASC
    )
    """
    Sort order of the returned applications.
    """


@dataclass
class ListApplicationsResponse:
    total_count: int
    """
    Total number of applications.
    """

    applications: list[Application]
    """
    List of applications.
    """


@dataclass
class ListBookingsRequest:
    project_id: Optional[str] = None
    """
    List bookings belonging to this project ID.
    """

    platform_id: Optional[str] = None
    """
    List bookings attached to this platform ID.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of results to return per page.
    """

    order_by: Optional[ListBookingsRequestOrderBy] = (
        ListBookingsRequestOrderBy.CREATED_AT_DESC
    )
    """
    Sort order of the returned results.
    """


@dataclass
class ListBookingsResponse:
    total_count: int
    """
    Total number of bookings.
    """

    bookings: list[Booking]
    """
    List of bookings.
    """


@dataclass
class ListJobResultsRequest:
    job_id: str
    """
    ID of the job.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of results to return per page.
    """

    order_by: Optional[ListJobResultsRequestOrderBy] = (
        ListJobResultsRequestOrderBy.CREATED_AT_DESC
    )
    """
    Sort order of the returned results.
    """


@dataclass
class ListJobResultsResponse:
    total_count: int
    """
    Total number of results.
    """

    job_results: list[JobResult]
    """
    List of results.
    """


@dataclass
class ListJobsRequest:
    tags: Optional[list[str]] = field(default_factory=list)
    """
    List jobs with these tags.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of jobs to return per page.
    """

    order_by: Optional[ListJobsRequestOrderBy] = ListJobsRequestOrderBy.CREATED_AT_DESC
    """
    Sort order of the returned jobs.
    """

    session_id: Optional[str] = None

    project_id: Optional[str] = None


@dataclass
class ListJobsResponse:
    total_count: int
    """
    Total number of jobs.
    """

    jobs: list[Job]
    """
    List of jobs.
    """


@dataclass
class ListModelsRequest:
    project_id: Optional[str] = None
    """
    List models belonging to this project ID.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of results to return per page.
    """

    order_by: Optional[ListModelsRequestOrderBy] = (
        ListModelsRequestOrderBy.CREATED_AT_DESC
    )
    """
    Sort order of the returned results.
    """


@dataclass
class ListModelsResponse:
    total_count: int
    """
    Total number of models.
    """

    models: list[Model]
    """
    List of models.
    """


@dataclass
class ListPlatformsRequest:
    provider_name: Optional[str] = None
    """
    List platforms with this provider name.
    """

    backend_name: Optional[str] = None
    """
    List platforms with this backend name.
    """

    name: Optional[str] = None
    """
    List platforms with this name.
    """

    platform_type: Optional[PlatformType] = PlatformType.UNKNOWN_TYPE
    """
    List platforms with this type.
    """

    platform_technology: Optional[PlatformTechnology] = (
        PlatformTechnology.UNKNOWN_TECHNOLOGY
    )
    """
    List platforms with this technology.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of platforms to return per page.
    """

    order_by: Optional[ListPlatformsRequestOrderBy] = (
        ListPlatformsRequestOrderBy.NAME_ASC
    )
    """
    Sort order of the returned platforms.
    """


@dataclass
class ListPlatformsResponse:
    total_count: int
    """
    Total number of platforms.
    """

    platforms: list[Platform]
    """
    List of platforms.
    """


@dataclass
class ListProcessResultsRequest:
    process_id: str
    """
    ID of the process.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of results to return per page.
    """

    order_by: Optional[ListProcessResultsRequestOrderBy] = (
        ListProcessResultsRequestOrderBy.CREATED_AT_DESC
    )
    """
    Sort order of the returned results.
    """


@dataclass
class ListProcessResultsResponse:
    total_count: int
    """
    Total number of results.
    """

    process_results: list[ProcessResult]
    """
    List of results.
    """


@dataclass
class ListProcessesRequest:
    application_id: Optional[str] = None
    """
    List processes that have been created for this application.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List processes with these tags.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of processes to return per page.
    """

    order_by: Optional[ListProcessesRequestOrderBy] = (
        ListProcessesRequestOrderBy.CREATED_AT_DESC
    )
    """
    Sort order of the returned processes.
    """

    project_id: Optional[str] = None
    """
    List processes belonging to this project ID.
    """


@dataclass
class ListProcessesResponse:
    total_count: int
    """
    Total number of processes.
    """

    processes: list[Process]
    """
    List of processes.
    """


@dataclass
class ListSessionACLsRequest:
    session_id: str
    page: Optional[int] = None
    page_size: Optional[int] = None
    order_by: Optional[ListSessionACLsRequestOrderBy] = None


@dataclass
class ListSessionACLsResponse:
    total_count: int
    acls: list[SessionAccess]


@dataclass
class ListSessionsRequest:
    platform_id: Optional[str] = None
    """
    List sessions that have been created for this platform.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List sessions with these tags.
    """

    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of sessions to return per page.
    """

    order_by: Optional[ListSessionsRequestOrderBy] = ListSessionsRequestOrderBy.NAME_ASC
    """
    Sort order of the returned sessions.
    """

    project_id: Optional[str] = None
    """
    List sessions belonging to this project ID.
    """


@dataclass
class ListSessionsResponse:
    total_count: int
    """
    Total number of sessions.
    """

    sessions: list[Session]
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
class UpdateBookingRequest:
    booking_id: str
    """
    Unique ID of the booking.
    """

    description: Optional[str] = None
    """
    Description of the booking slot.
    """


@dataclass
class UpdateJobRequest:
    job_id: str
    """
    Unique ID of the job.
    """

    name: Optional[str] = None
    """
    Name of the job.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the job.
    """


@dataclass
class UpdateProcessRequest:
    process_id: str
    """
    Unique ID of the process.
    """

    name: Optional[str] = None
    """
    Name of the process.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the process.
    """


@dataclass
class UpdateSessionRequest:
    session_id: str
    """
    Unique ID of the session.
    """

    name: Optional[str] = None
    """
    Name of the session.
    """

    max_idle_duration: Optional[str] = None
    """
    Maximum idle duration before the session ends.
    """

    max_duration: Optional[str] = None
    """
    Maximum time before the session ends.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags of the session.
    """
