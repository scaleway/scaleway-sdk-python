# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    JobDefinition,
    JobRun,
    ListJobDefinitionsResponse,
    ListJobRunsResponse,
    CreateJobDefinitionRequest,
    UpdateJobDefinitionRequest,
)


def unmarshal_JobDefinition(data: Any) -> JobDefinition:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'JobDefinition' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("cpu_limit", None)
    if field is not None:
        args["cpu_limit"] = field

    field = data.get("memory_limit", None)
    if field is not None:
        args["memory_limit"] = field

    field = data.get("image_uri", None)
    if field is not None:
        args["image_uri"] = field

    field = data.get("command", None)
    if field is not None:
        args["command"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("environment_variables", None)
    if field is not None:
        args["environment_variables"] = field

    field = data.get("description", None)
    if field is not None:
        args["description"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("job_timeout", None)
    if field is not None:
        args["job_timeout"] = field

    return JobDefinition(**args)


def unmarshal_JobRun(data: Any) -> JobRun:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'JobRun' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("job_definition_id", None)
    if field is not None:
        args["job_definition_id"] = field

    field = data.get("state", None)
    if field is not None:
        args["state"] = field

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("terminated_at", None)
    if field is not None:
        args["terminated_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )

    field = data.get("exit_code", None)
    if field is not None:
        args["exit_code"] = field

    field = data.get("run_duration", None)
    if field is not None:
        args["run_duration"] = field

    return JobRun(**args)


def unmarshal_ListJobDefinitionsResponse(data: Any) -> ListJobDefinitionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListJobDefinitionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("job_definitions", None)
    if field is not None:
        args["job_definitions"] = (
            [unmarshal_JobDefinition(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListJobDefinitionsResponse(**args)


def unmarshal_ListJobRunsResponse(data: Any) -> ListJobRunsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListJobRunsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("job_runs", None)
    if field is not None:
        args["job_runs"] = (
            [unmarshal_JobRun(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListJobRunsResponse(**args)


def marshal_CreateJobDefinitionRequest(
    request: CreateJobDefinitionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.cpu_limit is not None:
        output["cpu_limit"] = request.cpu_limit

    if request.memory_limit is not None:
        output["memory_limit"] = request.memory_limit

    if request.image_uri is not None:
        output["image_uri"] = request.image_uri

    if request.command is not None:
        output["command"] = request.command

    if request.description is not None:
        output["description"] = request.description

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.environment_variables is not None:
        output["environment_variables"] = {
            key: value for key, value in request.environment_variables.items()
        }

    if request.job_timeout is not None:
        output["job_timeout"] = request.job_timeout

    return output


def marshal_UpdateJobDefinitionRequest(
    request: UpdateJobDefinitionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.cpu_limit is not None:
        output["cpu_limit"] = request.cpu_limit

    if request.memory_limit is not None:
        output["memory_limit"] = request.memory_limit

    if request.image_uri is not None:
        output["image_uri"] = request.image_uri

    if request.command is not None:
        output["command"] = request.command

    if request.environment_variables is not None:
        output["environment_variables"] = request.environment_variables

    if request.description is not None:
        output["description"] = request.description

    if request.job_timeout is not None:
        output["job_timeout"] = request.job_timeout

    return output
