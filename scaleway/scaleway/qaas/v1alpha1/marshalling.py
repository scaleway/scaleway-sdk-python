# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
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
    SessionAccess,
    JobCircuit,
    Application,
    Job,
    PlatformHardware,
    Platform,
    Process,
    Session,
    ListApplicationsResponse,
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
    CreateSessionRequest,
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

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("compatible_platform_ids", None)
    if field is not None:
        args["compatible_platform_ids"] = field

    field = data.get("input_template", None)
    if field is not None:
        args["input_template"] = field

    return Application(**args)


def unmarshal_Job(data: Any) -> Job:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Job' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("session_id", None)
    if field is not None:
        args["session_id"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = None

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

    return Job(**args)


def unmarshal_PlatformHardware(data: Any) -> PlatformHardware:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlatformHardware' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("vcpus", None)
    if field is not None:
        args["vcpus"] = field

    field = data.get("gpus", None)
    if field is not None:
        args["gpus"] = field

    field = data.get("gpus_network", None)
    if field is not None:
        args["gpus_network"] = field

    field = data.get("ram", None)
    if field is not None:
        args["ram"] = field

    field = data.get("vram", None)
    if field is not None:
        args["vram"] = field

    return PlatformHardware(**args)


def unmarshal_Platform(data: Any) -> Platform:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Platform' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("version", None)
    if field is not None:
        args["version"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("provider_name", None)
    if field is not None:
        args["provider_name"] = field

    field = data.get("backend_name", None)
    if field is not None:
        args["backend_name"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("technology", None)
    if field is not None:
        args["technology"] = field

    field = data.get("max_qubit_count", None)
    if field is not None:
        args["max_qubit_count"] = field

    field = data.get("availability", None)
    if field is not None:
        args["availability"] = field

    field = data.get("metadata", None)
    if field is not None:
        args["metadata"] = field

    field = data.get("price_per_hour", None)
    if field is not None:
        args["price_per_hour"] = unmarshal_Money(field)
    else:
        args["price_per_hour"] = None

    field = data.get("hardware", None)
    if field is not None:
        args["hardware"] = unmarshal_PlatformHardware(field)
    else:
        args["hardware"] = None

    return Platform(**args)


def unmarshal_Process(data: Any) -> Process:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Process' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("attached_session_ids", None)
    if field is not None:
        args["attached_session_ids"] = field

    field = data.get("application_id", None)
    if field is not None:
        args["application_id"] = field
    else:
        args["application_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

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
        args["progress"] = None

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

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("platform_id", None)
    if field is not None:
        args["platform_id"] = field

    field = data.get("waiting_job_count", None)
    if field is not None:
        args["waiting_job_count"] = field

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("finished_job_count", None)
    if field is not None:
        args["finished_job_count"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("deduplication_id", None)
    if field is not None:
        args["deduplication_id"] = field

    field = data.get("origin_type", None)
    if field is not None:
        args["origin_type"] = field

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
        args["tags"] = None

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

    return Session(**args)


def unmarshal_ListApplicationsResponse(data: Any) -> ListApplicationsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListApplicationsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("applications", None)
    if field is not None:
        args["applications"] = (
            [unmarshal_Application(v) for v in field] if field is not None else None
        )

    return ListApplicationsResponse(**args)


def unmarshal_JobResult(data: Any) -> JobResult:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'JobResult' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("job_id", None)
    if field is not None:
        args["job_id"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("job_results", None)
    if field is not None:
        args["job_results"] = (
            [unmarshal_JobResult(v) for v in field] if field is not None else None
        )

    return ListJobResultsResponse(**args)


def unmarshal_ListJobsResponse(data: Any) -> ListJobsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListJobsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("jobs", None)
    if field is not None:
        args["jobs"] = [unmarshal_Job(v) for v in field] if field is not None else None

    return ListJobsResponse(**args)


def unmarshal_ListPlatformsResponse(data: Any) -> ListPlatformsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPlatformsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("platforms", None)
    if field is not None:
        args["platforms"] = (
            [unmarshal_Platform(v) for v in field] if field is not None else None
        )

    return ListPlatformsResponse(**args)


def unmarshal_ProcessResult(data: Any) -> ProcessResult:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ProcessResult' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("process_id", None)
    if field is not None:
        args["process_id"] = field

    field = data.get("result", None)
    if field is not None:
        args["result"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("process_results", None)
    if field is not None:
        args["process_results"] = (
            [unmarshal_ProcessResult(v) for v in field] if field is not None else None
        )

    return ListProcessResultsResponse(**args)


def unmarshal_ListProcessesResponse(data: Any) -> ListProcessesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListProcessesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("processes", None)
    if field is not None:
        args["processes"] = (
            [unmarshal_Process(v) for v in field] if field is not None else None
        )

    return ListProcessesResponse(**args)


def unmarshal_ListSessionACLsResponse(data: Any) -> ListSessionACLsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSessionACLsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("acls", None)
    if field is not None:
        args["acls"] = [SessionAccess(v) for v in field] if field is not None else None

    return ListSessionACLsResponse(**args)


def unmarshal_ListSessionsResponse(data: Any) -> ListSessionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSessionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("sessions", None)
    if field is not None:
        args["sessions"] = (
            [unmarshal_Session(v) for v in field] if field is not None else None
        )

    return ListSessionsResponse(**args)


def marshal_JobCircuit(
    request: JobCircuit,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("perceval_circuit", request.perceval_circuit),
                OneOfPossibility("qiskit_circuit", request.qiskit_circuit),
            ]
        ),
    )

    return output


def marshal_CreateJobRequest(
    request: CreateJobRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

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

    return output


def marshal_CreateProcessRequest(
    request: CreateProcessRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.platform_id is not None:
        output["platform_id"] = request.platform_id

    if request.application_id is not None:
        output["application_id"] = request.application_id

    if request.input is not None:
        output["input"] = request.input

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreateSessionRequest(
    request: CreateSessionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.platform_id is not None:
        output["platform_id"] = request.platform_id

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

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

    return output


def marshal_UpdateJobRequest(
    request: UpdateJobRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateProcessRequest(
    request: UpdateProcessRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateSessionRequest(
    request: UpdateSessionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.max_idle_duration is not None:
        output["max_idle_duration"] = request.max_idle_duration

    if request.max_duration is not None:
        output["max_duration"] = request.max_duration

    if request.tags is not None:
        output["tags"] = request.tags

    return output
