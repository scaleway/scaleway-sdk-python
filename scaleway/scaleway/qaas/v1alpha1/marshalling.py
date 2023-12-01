# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    JobCircuit,
    Job,
    Platform,
    Session,
    ListJobsResponse,
    ListPlatformsResponse,
    ListSessionsResponse,
    CreateJobRequest,
    CreateSessionRequest,
    UpdateJobRequest,
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

    return JobCircuit(**args)


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

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("started_at", None)
    if field is not None:
        args["started_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("progress_message", None)
    if field is not None:
        args["progress_message"] = field

    field = data.get("job_duration", None)
    if field is not None:
        args["job_duration"] = field

    field = data.get("result_distribution", None)
    if field is not None:
        args["result_distribution"] = field

    return Job(**args)


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

    field = data.get("type_", None)
    if field is not None:
        args["type_"] = field

    field = data.get("technology", None)
    if field is not None:
        args["technology"] = field

    field = data.get("max_qubit_count", None)
    if field is not None:
        args["max_qubit_count"] = field

    field = data.get("metadata", None)
    if field is not None:
        args["metadata"] = field

    return Platform(**args)


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

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("started_at", None)
    if field is not None:
        args["started_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("update_at", None)
    if field is not None:
        args["update_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("max_idle_duration", None)
    if field is not None:
        args["max_idle_duration"] = field

    field = data.get("max_duration", None)
    if field is not None:
        args["max_duration"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    return Session(**args)


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
        output["circuit"] = (marshal_JobCircuit(request.circuit, defaults),)

    if request.tags is not None:
        output["tags"] = request.tags

    if request.max_duration is not None:
        output["max_duration"] = request.max_duration

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
