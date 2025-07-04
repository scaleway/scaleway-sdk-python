# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from decimal import Decimal
from datetime import datetime
from typing import Any, Dict, List, Optional
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
    unmarshal_Money,
    marshal_Money,
    marshal_ScwFile,
    marshal_ServiceInfo,
    marshal_TimeSeries,
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    ApplicationType,
    BookingStatus,
    JobStatus,
    ListApplicationsRequestOrderBy,
    ListBookingsRequestOrderBy,
    ListJobResultsRequestOrderBy,
    ListJobsRequestOrderBy,
    ListPlatformsRequestOrderBy,
    ListProcessResultsRequestOrderBy,
    ListProcessesRequestOrderBy,
    ListSessionACLsRequestOrderBy,
    ListSessionsRequestOrderBy,
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
    ListPlatformsResponse,
    ProcessResult,
    ListProcessResultsResponse,
    ListProcessesResponse,
    ListSessionACLsResponse,
    ListSessionsResponse,
    CreateJobRequest,
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

    args: Dict[str, Any] = {}

    field = data.get("perceval_circuit", None)
    args["perceval_circuit"] = field

    field = data.get("qiskit_circuit", None)
    args["qiskit_circuit"] = field

    return JobCircuit(**args)

def unmarshal_Application(data: Any) -> Application:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Application' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("type", getattr(ApplicationType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("compatible_platform_ids", [])
    args["compatible_platform_ids"] = field

    field = data.get("input_template", str())
    args["input_template"] = field

    return Application(**args)

def unmarshal_Booking(data: Any) -> Booking:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Booking' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("status", getattr(BookingStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("progress_message", str())
    args["progress_message"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("started_at", None)
    args["started_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("finished_at", None)
    args["finished_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Booking(**args)

def unmarshal_Job(data: Any) -> Job:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Job' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("session_id", str())
    args["session_id"] = field

    field = data.get("status", getattr(JobStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("started_at", None)
    args["started_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("progress_message", None)
    args["progress_message"] = field

    field = data.get("job_duration", None)
    args["job_duration"] = field

    field = data.get("result_distribution", None)
    args["result_distribution"] = field

    return Job(**args)

def unmarshal_PlatformBookingRequirement(data: Any) -> PlatformBookingRequirement:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlatformBookingRequirement' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("min_duration", None)
    args["min_duration"] = field

    field = data.get("max_duration", None)
    args["max_duration"] = field

    field = data.get("max_cancellation_duration", None)
    args["max_cancellation_duration"] = field

    field = data.get("max_planification_duration", None)
    args["max_planification_duration"] = field

    return PlatformBookingRequirement(**args)

def unmarshal_PlatformHardware(data: Any) -> PlatformHardware:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlatformHardware' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("vcpus", 0)
    args["vcpus"] = field

    field = data.get("gpus", 0)
    args["gpus"] = field

    field = data.get("gpus_network", str())
    args["gpus_network"] = field

    field = data.get("ram", 0)
    args["ram"] = field

    field = data.get("vram", 0)
    args["vram"] = field

    return PlatformHardware(**args)

def unmarshal_Platform(data: Any) -> Platform:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Platform' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("version", str())
    args["version"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("provider_name", str())
    args["provider_name"] = field

    field = data.get("backend_name", str())
    args["backend_name"] = field

    field = data.get("type", getattr(PlatformType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("technology", getattr(PlatformTechnology, "UNKNOWN_TECHNOLOGY"))
    args["technology"] = field

    field = data.get("max_qubit_count", 0)
    args["max_qubit_count"] = field

    field = data.get("max_shot_count", 0)
    args["max_shot_count"] = field

    field = data.get("max_circuit_count", 0)
    args["max_circuit_count"] = field

    field = data.get("availability", getattr(PlatformAvailability, "UNKNOWN_AVAILABILITY"))
    args["availability"] = field

    field = data.get("metadata", str())
    args["metadata"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("documentation_url", str())
    args["documentation_url"] = field

    field = data.get("is_bookable", False)
    args["is_bookable"] = field

    field = data.get("price_per_hour", None)
    args["price_per_hour"] = unmarshal_Money(field) if field is not None else None

    field = data.get("price_per_shot", None)
    args["price_per_shot"] = unmarshal_Money(field) if field is not None else None

    field = data.get("price_per_circuit", None)
    args["price_per_circuit"] = unmarshal_Money(field) if field is not None else None

    field = data.get("hardware", None)
    args["hardware"] = unmarshal_PlatformHardware(field) if field is not None else None

    field = data.get("booking_requirement", None)
    args["booking_requirement"] = unmarshal_PlatformBookingRequirement(field) if field is not None else None

    return Platform(**args)

def unmarshal_Process(data: Any) -> Process:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Process' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("attached_session_ids", [])
    args["attached_session_ids"] = field

    field = data.get("application_id", None)
    args["application_id"] = field

    field = data.get("status", getattr(ProcessStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("platform_id", None)
    args["platform_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("started_at", None)
    args["started_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("finished_at", None)
    args["finished_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("progress", None)
    args["progress"] = field

    field = data.get("progress_message", None)
    args["progress_message"] = field

    field = data.get("input", None)
    args["input"] = field

    return Process(**args)

def unmarshal_Session(data: Any) -> Session:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Session' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("platform_id", str())
    args["platform_id"] = field

    field = data.get("waiting_job_count", 0)
    args["waiting_job_count"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("finished_job_count", 0)
    args["finished_job_count"] = field

    field = data.get("status", getattr(SessionStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("deduplication_id", str())
    args["deduplication_id"] = field

    field = data.get("origin_type", getattr(SessionOriginType, "UNKNOWN_ORIGIN_TYPE"))
    args["origin_type"] = field

    field = data.get("started_at", None)
    args["started_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("terminated_at", None)
    args["terminated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("max_idle_duration", None)
    args["max_idle_duration"] = field

    field = data.get("max_duration", None)
    args["max_duration"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("origin_id", None)
    args["origin_id"] = field

    field = data.get("progress_message", None)
    args["progress_message"] = field

    field = data.get("booking_id", None)
    args["booking_id"] = field

    return Session(**args)

def unmarshal_ListApplicationsResponse(data: Any) -> ListApplicationsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListApplicationsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("applications", [])
    args["applications"] = [unmarshal_Application(v) for v in field] if field is not None else None

    return ListApplicationsResponse(**args)

def unmarshal_ListBookingsResponse(data: Any) -> ListBookingsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListBookingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("bookings", [])
    args["bookings"] = [unmarshal_Booking(v) for v in field] if field is not None else None

    return ListBookingsResponse(**args)

def unmarshal_JobResult(data: Any) -> JobResult:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'JobResult' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("job_id", str())
    args["job_id"] = field

    field = data.get("result", None)
    args["result"] = field

    field = data.get("url", None)
    args["url"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return JobResult(**args)

def unmarshal_ListJobResultsResponse(data: Any) -> ListJobResultsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListJobResultsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("job_results", [])
    args["job_results"] = [unmarshal_JobResult(v) for v in field] if field is not None else None

    return ListJobResultsResponse(**args)

def unmarshal_ListJobsResponse(data: Any) -> ListJobsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListJobsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("jobs", [])
    args["jobs"] = [unmarshal_Job(v) for v in field] if field is not None else None

    return ListJobsResponse(**args)

def unmarshal_ListPlatformsResponse(data: Any) -> ListPlatformsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPlatformsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("platforms", [])
    args["platforms"] = [unmarshal_Platform(v) for v in field] if field is not None else None

    return ListPlatformsResponse(**args)

def unmarshal_ProcessResult(data: Any) -> ProcessResult:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ProcessResult' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("process_id", str())
    args["process_id"] = field

    field = data.get("result", str())
    args["result"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return ProcessResult(**args)

def unmarshal_ListProcessResultsResponse(data: Any) -> ListProcessResultsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListProcessResultsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("process_results", [])
    args["process_results"] = [unmarshal_ProcessResult(v) for v in field] if field is not None else None

    return ListProcessResultsResponse(**args)

def unmarshal_ListProcessesResponse(data: Any) -> ListProcessesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListProcessesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("processes", [])
    args["processes"] = [unmarshal_Process(v) for v in field] if field is not None else None

    return ListProcessesResponse(**args)

def unmarshal_ListSessionACLsResponse(data: Any) -> ListSessionACLsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSessionACLsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", str())
    args["total_count"] = field

    field = data.get("acls", str())
    args["acls"] = [SessionAccess(v) for v in field] if field is not None else None

    return ListSessionACLsResponse(**args)

def unmarshal_ListSessionsResponse(data: Any) -> ListSessionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSessionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("sessions", [])
    args["sessions"] = [unmarshal_Session(v) for v in field] if field is not None else None

    return ListSessionsResponse(**args)

def marshal_JobCircuit(
    request: JobCircuit,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="perceval_circuit", value=request.perceval_circuit,marshal_func=None
            ),
            OneOfPossibility(param="qiskit_circuit", value=request.qiskit_circuit,marshal_func=None
            ),
        ]),
    )


    return output

def marshal_CreateJobRequest(
    request: CreateJobRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.session_id is not None:
        output["session_id"] = request.session_id
    else:
        output["session_id"] = str()

    if request.circuit is not None:
        output["circuit"] = marshal_JobCircuit(request.circuit, defaults)
    else:
        output["circuit"] = str()

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.max_duration is not None:
        output["max_duration"] = request.max_duration
    else:
        output["max_duration"] = None


    return output

def marshal_CreateProcessRequest(
    request: CreateProcessRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.platform_id is not None:
        output["platform_id"] = request.platform_id
    else:
        output["platform_id"] = None

    if request.application_id is not None:
        output["application_id"] = request.application_id
    else:
        output["application_id"] = None

    if request.input is not None:
        output["input"] = request.input
    else:
        output["input"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_CreateSessionRequestBookingDemand(
    request: CreateSessionRequestBookingDemand,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.started_at is not None:
        output["started_at"] = request.started_at.isoformat()
    else:
        output["started_at"] = None

    if request.finished_at is not None:
        output["finished_at"] = request.finished_at.isoformat()
    else:
        output["finished_at"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None


    return output

def marshal_CreateSessionRequest(
    request: CreateSessionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.platform_id is not None:
        output["platform_id"] = request.platform_id
    else:
        output["platform_id"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.max_idle_duration is not None:
        output["max_idle_duration"] = request.max_idle_duration
    else:
        output["max_idle_duration"] = None

    if request.max_duration is not None:
        output["max_duration"] = request.max_duration
    else:
        output["max_duration"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.deduplication_id is not None:
        output["deduplication_id"] = request.deduplication_id
    else:
        output["deduplication_id"] = None

    if request.booking_demand is not None:
        output["booking_demand"] = marshal_CreateSessionRequestBookingDemand(request.booking_demand, defaults)
    else:
        output["booking_demand"] = None


    return output

def marshal_UpdateBookingRequest(
    request: UpdateBookingRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None


    return output

def marshal_UpdateJobRequest(
    request: UpdateJobRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_UpdateProcessRequest(
    request: UpdateProcessRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_UpdateSessionRequest(
    request: UpdateSessionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.max_idle_duration is not None:
        output["max_idle_duration"] = request.max_idle_duration
    else:
        output["max_idle_duration"] = None

    if request.max_duration is not None:
        output["max_duration"] = request.max_duration
    else:
        output["max_duration"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output
