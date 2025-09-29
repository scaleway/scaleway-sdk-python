# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    unmarshal_Money,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    ApplicationType,
    BookingStatus,
    JobStatus,
    PlatformAvailability,
    PlatformTechnology,
    PlatformType,
    ProcessStatus,
    SessionAccess,
    SessionOriginType,
    SessionStatus,
    JobCircuit,
    Application,
    Booking,
    Job,
    Model,
    PlatformBookingRequirement,
    PlatformHardware,
    Platform,
    Process,
    Session,
    ListApplicationsResponse,
    ListBookingsResponse,
    JobResult,
    ListJobResultsResponse,
    ListJobsResponse,
    ListModelsResponse,
    ListPlatformsResponse,
    ProcessResult,
    ListProcessResultsResponse,
    ListProcessesResponse,
    ListSessionACLsResponse,
    ListSessionsResponse,
    CreateJobRequest,
    CreateModelRequest,
    CreateProcessRequest,
    CreateSessionRequestBookingDemand,
    CreateSessionRequest,
    UpdateBookingRequest,
    UpdateJobRequest,
    UpdateProcessRequest,
    UpdateSessionRequest,
)


def unmarshal_JobCircuit(data: Any) -> JobCircuit:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'JobCircuit' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("perceval_circuit", None)
    if field is not None:
        args["perceval_circuit"] = field
    else:
        args["perceval_circuit"] = None

    field = data.get("qiskit_circuit", None)
    if field is not None:
        args["qiskit_circuit"] = field
    else:
        args["qiskit_circuit"] = None

    return JobCircuit(**args)


def unmarshal_Application(data: Any) -> Application:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Application' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = ApplicationType.UNKNOWN_TYPE

    field = data.get("compatible_platform_ids", None)
    if field is not None:
        args["compatible_platform_ids"] = field
    else:
        args["compatible_platform_ids"] = []

    field = data.get("input_template", None)
    if field is not None:
        args["input_template"] = field
    else:
        args["input_template"] = None

    return Application(**args)


def unmarshal_Booking(data: Any) -> Booking:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Booking' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = BookingStatus.UNKNOWN_STATUS

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("progress_message", None)
    if field is not None:
        args["progress_message"] = field
    else:
        args["progress_message"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("started_at", None)
    if field is not None:
        args["started_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["started_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("finished_at", None)
    if field is not None:
        args["finished_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["finished_at"] = None

    return Booking(**args)


def unmarshal_Job(data: Any) -> Job:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Job' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("session_id", None)
    if field is not None:
        args["session_id"] = field
    else:
        args["session_id"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("started_at", None)
    if field is not None:
        args["started_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["started_at"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = JobStatus.UNKNOWN_STATUS

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("progress_message", None)
    if field is not None:
        args["progress_message"] = field
    else:
        args["progress_message"] = None

    field = data.get("job_duration", None)
    if field is not None:
        args["job_duration"] = field
    else:
        args["job_duration"] = None

    field = data.get("result_distribution", None)
    if field is not None:
        args["result_distribution"] = field
    else:
        args["result_distribution"] = None

    field = data.get("model_id", None)
    if field is not None:
        args["model_id"] = field
    else:
        args["model_id"] = None

    field = data.get("parameters", None)
    if field is not None:
        args["parameters"] = field
    else:
        args["parameters"] = None

    return Job(**args)


def unmarshal_Model(data: Any) -> Model:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Model' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("url", None)
    if field is not None:
        args["url"] = field
    else:
        args["url"] = None

    return Model(**args)


def unmarshal_PlatformBookingRequirement(data: Any) -> PlatformBookingRequirement:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlatformBookingRequirement' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("max_booking_per_week", None)
    if field is not None:
        args["max_booking_per_week"] = field
    else:
        args["max_booking_per_week"] = 0

    field = data.get("max_booking_per_day", None)
    if field is not None:
        args["max_booking_per_day"] = field
    else:
        args["max_booking_per_day"] = 0

    field = data.get("min_duration", None)
    if field is not None:
        args["min_duration"] = field
    else:
        args["min_duration"] = None

    field = data.get("max_duration", None)
    if field is not None:
        args["max_duration"] = field
    else:
        args["max_duration"] = None

    field = data.get("max_cancellation_duration", None)
    if field is not None:
        args["max_cancellation_duration"] = field
    else:
        args["max_cancellation_duration"] = None

    field = data.get("max_planification_duration", None)
    if field is not None:
        args["max_planification_duration"] = field
    else:
        args["max_planification_duration"] = None

    field = data.get("min_planification_duration", None)
    if field is not None:
        args["min_planification_duration"] = field
    else:
        args["min_planification_duration"] = None

    return PlatformBookingRequirement(**args)


def unmarshal_PlatformHardware(data: Any) -> PlatformHardware:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlatformHardware' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("vcpus", None)
    if field is not None:
        args["vcpus"] = field
    else:
        args["vcpus"] = 0

    field = data.get("gpus", None)
    if field is not None:
        args["gpus"] = field
    else:
        args["gpus"] = 0

    field = data.get("gpus_network", None)
    if field is not None:
        args["gpus_network"] = field
    else:
        args["gpus_network"] = None

    field = data.get("ram", None)
    if field is not None:
        args["ram"] = field
    else:
        args["ram"] = 0

    field = data.get("vram", None)
    if field is not None:
        args["vram"] = field
    else:
        args["vram"] = 0

    return PlatformHardware(**args)


def unmarshal_Platform(data: Any) -> Platform:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Platform' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("version", None)
    if field is not None:
        args["version"] = field
    else:
        args["version"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("provider_name", None)
    if field is not None:
        args["provider_name"] = field
    else:
        args["provider_name"] = None

    field = data.get("backend_name", None)
    if field is not None:
        args["backend_name"] = field
    else:
        args["backend_name"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = PlatformType.UNKNOWN_TYPE

    field = data.get("technology", None)
    if field is not None:
        args["technology"] = field
    else:
        args["technology"] = PlatformTechnology.UNKNOWN_TECHNOLOGY

    field = data.get("max_qubit_count", None)
    if field is not None:
        args["max_qubit_count"] = field
    else:
        args["max_qubit_count"] = 0

    field = data.get("max_shot_count", None)
    if field is not None:
        args["max_shot_count"] = field
    else:
        args["max_shot_count"] = 0

    field = data.get("max_circuit_count", None)
    if field is not None:
        args["max_circuit_count"] = field
    else:
        args["max_circuit_count"] = 0

    field = data.get("availability", None)
    if field is not None:
        args["availability"] = field
    else:
        args["availability"] = PlatformAvailability.UNKNOWN_AVAILABILITY

    field = data.get("metadata", None)
    if field is not None:
        args["metadata"] = field
    else:
        args["metadata"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("documentation_url", None)
    if field is not None:
        args["documentation_url"] = field
    else:
        args["documentation_url"] = None

    field = data.get("is_bookable", None)
    if field is not None:
        args["is_bookable"] = field
    else:
        args["is_bookable"] = False

    field = data.get("price_per_hour", None)
    if field is not None:
        args["price_per_hour"] = unmarshal_Money(field)
    else:
        args["price_per_hour"] = None

    field = data.get("price_per_shot", None)
    if field is not None:
        args["price_per_shot"] = unmarshal_Money(field)
    else:
        args["price_per_shot"] = None

    field = data.get("price_per_circuit", None)
    if field is not None:
        args["price_per_circuit"] = unmarshal_Money(field)
    else:
        args["price_per_circuit"] = None

    field = data.get("hardware", None)
    if field is not None:
        args["hardware"] = unmarshal_PlatformHardware(field)
    else:
        args["hardware"] = None

    field = data.get("booking_requirement", None)
    if field is not None:
        args["booking_requirement"] = unmarshal_PlatformBookingRequirement(field)
    else:
        args["booking_requirement"] = None

    return Platform(**args)


def unmarshal_Process(data: Any) -> Process:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Process' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("attached_session_ids", None)
    if field is not None:
        args["attached_session_ids"] = field
    else:
        args["attached_session_ids"] = []

    field = data.get("application_id", None)
    if field is not None:
        args["application_id"] = field
    else:
        args["application_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = ProcessStatus.UNKNOWN_STATUS

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("platform_id", None)
    if field is not None:
        args["platform_id"] = field
    else:
        args["platform_id"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("started_at", None)
    if field is not None:
        args["started_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["started_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("finished_at", None)
    if field is not None:
        args["finished_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["finished_at"] = None

    field = data.get("progress", None)
    if field is not None:
        args["progress"] = field
    else:
        args["progress"] = 0

    field = data.get("progress_message", None)
    if field is not None:
        args["progress_message"] = field
    else:
        args["progress_message"] = None

    field = data.get("input", None)
    if field is not None:
        args["input"] = field
    else:
        args["input"] = None

    return Process(**args)


def unmarshal_Session(data: Any) -> Session:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Session' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("platform_id", None)
    if field is not None:
        args["platform_id"] = field
    else:
        args["platform_id"] = None

    field = data.get("waiting_job_count", None)
    if field is not None:
        args["waiting_job_count"] = field
    else:
        args["waiting_job_count"] = 0

    field = data.get("finished_job_count", None)
    if field is not None:
        args["finished_job_count"] = field
    else:
        args["finished_job_count"] = 0

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = SessionStatus.UNKNOWN_STATUS

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("deduplication_id", None)
    if field is not None:
        args["deduplication_id"] = field
    else:
        args["deduplication_id"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("started_at", None)
    if field is not None:
        args["started_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["started_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("terminated_at", None)
    if field is not None:
        args["terminated_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["terminated_at"] = None

    field = data.get("max_idle_duration", None)
    if field is not None:
        args["max_idle_duration"] = field
    else:
        args["max_idle_duration"] = None

    field = data.get("max_duration", None)
    if field is not None:
        args["max_duration"] = field
    else:
        args["max_duration"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("origin_type", None)
    if field is not None:
        args["origin_type"] = field
    else:
        args["origin_type"] = SessionOriginType.UNKNOWN_ORIGIN_TYPE

    field = data.get("origin_id", None)
    if field is not None:
        args["origin_id"] = field
    else:
        args["origin_id"] = None

    field = data.get("progress_message", None)
    if field is not None:
        args["progress_message"] = field
    else:
        args["progress_message"] = None

    field = data.get("booking_id", None)
    if field is not None:
        args["booking_id"] = field
    else:
        args["booking_id"] = None

    field = data.get("model_id", None)
    if field is not None:
        args["model_id"] = field
    else:
        args["model_id"] = None

    field = data.get("parameters", None)
    if field is not None:
        args["parameters"] = field
    else:
        args["parameters"] = None

    return Session(**args)


def unmarshal_ListApplicationsResponse(data: Any) -> ListApplicationsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListApplicationsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("applications", None)
    if field is not None:
        args["applications"] = (
            [unmarshal_Application(v) for v in field] if field is not None else None
        )
    else:
        args["applications"] = []

    return ListApplicationsResponse(**args)


def unmarshal_ListBookingsResponse(data: Any) -> ListBookingsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListBookingsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("bookings", None)
    if field is not None:
        args["bookings"] = (
            [unmarshal_Booking(v) for v in field] if field is not None else None
        )
    else:
        args["bookings"] = []

    return ListBookingsResponse(**args)


def unmarshal_JobResult(data: Any) -> JobResult:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'JobResult' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("job_id", None)
    if field is not None:
        args["job_id"] = field
    else:
        args["job_id"] = None

    field = data.get("result", None)
    if field is not None:
        args["result"] = field
    else:
        args["result"] = None

    field = data.get("url", None)
    if field is not None:
        args["url"] = field
    else:
        args["url"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    return JobResult(**args)


def unmarshal_ListJobResultsResponse(data: Any) -> ListJobResultsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListJobResultsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("job_results", None)
    if field is not None:
        args["job_results"] = (
            [unmarshal_JobResult(v) for v in field] if field is not None else None
        )
    else:
        args["job_results"] = []

    return ListJobResultsResponse(**args)


def unmarshal_ListJobsResponse(data: Any) -> ListJobsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListJobsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("jobs", None)
    if field is not None:
        args["jobs"] = [unmarshal_Job(v) for v in field] if field is not None else None
    else:
        args["jobs"] = []

    return ListJobsResponse(**args)


def unmarshal_ListModelsResponse(data: Any) -> ListModelsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListModelsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("models", None)
    if field is not None:
        args["models"] = (
            [unmarshal_Model(v) for v in field] if field is not None else None
        )
    else:
        args["models"] = []

    return ListModelsResponse(**args)


def unmarshal_ListPlatformsResponse(data: Any) -> ListPlatformsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPlatformsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("platforms", None)
    if field is not None:
        args["platforms"] = (
            [unmarshal_Platform(v) for v in field] if field is not None else None
        )
    else:
        args["platforms"] = []

    return ListPlatformsResponse(**args)


def unmarshal_ProcessResult(data: Any) -> ProcessResult:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ProcessResult' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("process_id", None)
    if field is not None:
        args["process_id"] = field
    else:
        args["process_id"] = None

    field = data.get("result", None)
    if field is not None:
        args["result"] = field
    else:
        args["result"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    return ProcessResult(**args)


def unmarshal_ListProcessResultsResponse(data: Any) -> ListProcessResultsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListProcessResultsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("process_results", None)
    if field is not None:
        args["process_results"] = (
            [unmarshal_ProcessResult(v) for v in field] if field is not None else None
        )
    else:
        args["process_results"] = []

    return ListProcessResultsResponse(**args)


def unmarshal_ListProcessesResponse(data: Any) -> ListProcessesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListProcessesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("processes", None)
    if field is not None:
        args["processes"] = (
            [unmarshal_Process(v) for v in field] if field is not None else None
        )
    else:
        args["processes"] = []

    return ListProcessesResponse(**args)


def unmarshal_ListSessionACLsResponse(data: Any) -> ListSessionACLsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSessionACLsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("acls", None)
    if field is not None:
        args["acls"] = [SessionAccess(v) for v in field] if field is not None else None
    else:
        args["acls"] = None

    return ListSessionACLsResponse(**args)


def unmarshal_ListSessionsResponse(data: Any) -> ListSessionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSessionsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("sessions", None)
    if field is not None:
        args["sessions"] = (
            [unmarshal_Session(v) for v in field] if field is not None else None
        )
    else:
        args["sessions"] = []

    return ListSessionsResponse(**args)


def marshal_JobCircuit(
    request: JobCircuit,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="perceval_circuit",
                    value=request.perceval_circuit,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="qiskit_circuit",
                    value=request.qiskit_circuit,
                    marshal_func=None,
                ),
            ]
        ),
    )

    return output


def marshal_CreateJobRequest(
    request: CreateJobRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.session_id is not None:
        output["session_id"] = request.session_id

    if request.circuit is not None:
        output["circuit"] = marshal_JobCircuit(request.circuit, defaults)

    if request.tags is not None:
        output["tags"] = request.tags

    if request.max_duration is not None:
        output["max_duration"] = request.max_duration

    if request.model_id is not None:
        output["model_id"] = request.model_id

    if request.parameters is not None:
        output["parameters"] = request.parameters

    return output


def marshal_CreateModelRequest(
    request: CreateModelRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.payload is not None:
        output["payload"] = request.payload

    return output


def marshal_CreateProcessRequest(
    request: CreateProcessRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.platform_id is not None:
        output["platform_id"] = request.platform_id

    if request.application_id is not None:
        output["application_id"] = request.application_id

    if request.input is not None:
        output["input"] = request.input

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreateSessionRequestBookingDemand(
    request: CreateSessionRequestBookingDemand,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.started_at is not None:
        output["started_at"] = request.started_at.isoformat()

    if request.finished_at is not None:
        output["finished_at"] = request.finished_at.isoformat()

    if request.description is not None:
        output["description"] = request.description

    return output


def marshal_CreateSessionRequest(
    request: CreateSessionRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.platform_id is not None:
        output["platform_id"] = request.platform_id

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.name is not None:
        output["name"] = request.name

    if request.max_idle_duration is not None:
        output["max_idle_duration"] = request.max_idle_duration

    if request.max_duration is not None:
        output["max_duration"] = request.max_duration

    if request.tags is not None:
        output["tags"] = request.tags

    if request.deduplication_id is not None:
        output["deduplication_id"] = request.deduplication_id

    if request.booking_demand is not None:
        output["booking_demand"] = marshal_CreateSessionRequestBookingDemand(
            request.booking_demand, defaults
        )

    if request.model_id is not None:
        output["model_id"] = request.model_id

    if request.parameters is not None:
        output["parameters"] = request.parameters

    return output


def marshal_UpdateBookingRequest(
    request: UpdateBookingRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    return output


def marshal_UpdateJobRequest(
    request: UpdateJobRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateProcessRequest(
    request: UpdateProcessRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateSessionRequest(
    request: UpdateSessionRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.max_idle_duration is not None:
        output["max_idle_duration"] = request.max_idle_duration

    if request.max_duration is not None:
        output["max_duration"] = request.max_duration

    if request.tags is not None:
        output["tags"] = request.tags

    return output
