# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from dateutil import parser
from .types import (
    JobDefinition,
    JobRun,
    ListJobDefinitionsResponse,
    ListJobRunsResponse,
    CreateJobDefinitionRequest,
    UpdateJobDefinitionRequest,
)


def unmarshal_JobDefinition(data: Any) -> JobDefinition:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'JobDefinition' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("command", None)
    args["command"] = field

    field = data.get("cpu_limit", None)
    args["cpu_limit"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("environment_variables", None)
    args["environment_variables"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("image_uri", None)
    args["image_uri"] = field

    field = data.get("job_timeout", None)
    args["job_timeout"] = field

    field = data.get("memory_limit", None)
    args["memory_limit"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return JobDefinition(**args)


def unmarshal_JobRun(data: Any) -> JobRun:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'JobRun' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("error_message", None)
    args["error_message"] = field

    field = data.get("exit_code", None)
    args["exit_code"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("job_definition_id", None)
    args["job_definition_id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("run_duration", None)
    args["run_duration"] = field

    field = data.get("state", None)
    args["state"] = field

    field = data.get("terminated_at", None)
    args["terminated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return JobRun(**args)


def unmarshal_ListJobDefinitionsResponse(data: Any) -> ListJobDefinitionsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListJobDefinitionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("job_definitions", None)
    args["job_definitions"] = (
        [unmarshal_JobDefinition(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListJobDefinitionsResponse(**args)


def unmarshal_ListJobRunsResponse(data: Any) -> ListJobRunsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListJobRunsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("job_runs", None)
    args["job_runs"] = (
        [unmarshal_JobRun(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListJobRunsResponse(**args)


def marshal_CreateJobDefinitionRequest(
    request: CreateJobDefinitionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.command is not None:
        output["command"] = request.command

    if request.cpu_limit is not None:
        output["cpu_limit"] = request.cpu_limit

    if request.description is not None:
        output["description"] = request.description

    if request.environment_variables is not None:
        output["environment_variables"] = request.environment_variables

    if request.image_uri is not None:
        output["image_uri"] = request.image_uri

    if request.job_timeout is not None:
        output["job_timeout"] = request.job_timeout

    if request.memory_limit is not None:
        output["memory_limit"] = request.memory_limit

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_UpdateJobDefinitionRequest(
    request: UpdateJobDefinitionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.command is not None:
        output["command"] = request.command

    if request.cpu_limit is not None:
        output["cpu_limit"] = request.cpu_limit

    if request.description is not None:
        output["description"] = request.description

    if request.environment_variables is not None:
        output["environment_variables"] = request.environment_variables

    if request.image_uri is not None:
        output["image_uri"] = request.image_uri

    if request.job_timeout is not None:
        output["job_timeout"] = request.job_timeout

    if request.memory_limit is not None:
        output["memory_limit"] = request.memory_limit

    if request.name is not None:
        output["name"] = request.name

    return output
