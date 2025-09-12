# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    SecretEnvVar,
    SecretFile,
    Secret,
    CronSchedule,
    JobDefinition,
    JobRun,
    CreateJobDefinitionSecretsResponse,
    JobsLimits,
    ListJobDefinitionSecretsResponse,
    ListJobDefinitionsResponse,
    ListJobRunsResponse,
    Resource,
    ListJobsResourcesResponse,
    StartJobDefinitionResponse,
    CreateJobDefinitionRequestCronScheduleConfig,
    CreateJobDefinitionRequest,
    CreateJobDefinitionSecretsRequestSecretConfig,
    CreateJobDefinitionSecretsRequest,
    StartJobDefinitionRequest,
    UpdateJobDefinitionRequestCronScheduleConfig,
    UpdateJobDefinitionRequest,
    UpdateJobDefinitionSecretRequest,
)


def unmarshal_SecretEnvVar(data: Any) -> SecretEnvVar:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecretEnvVar' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return SecretEnvVar(**args)


def unmarshal_SecretFile(data: Any) -> SecretFile:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecretFile' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("path", None)
    if field is not None:
        args["path"] = field
    else:
        args["path"] = None

    return SecretFile(**args)


def unmarshal_Secret(data: Any) -> Secret:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Secret' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("secret_id", None)
    if field is not None:
        args["secret_id"] = field
    else:
        args["secret_id"] = None

    field = data.get("secret_manager_id", None)
    if field is not None:
        args["secret_manager_id"] = field
    else:
        args["secret_manager_id"] = None

    field = data.get("secret_manager_version", None)
    if field is not None:
        args["secret_manager_version"] = field
    else:
        args["secret_manager_version"] = None

    field = data.get("file", None)
    if field is not None:
        args["file"] = unmarshal_SecretFile(field)
    else:
        args["file"] = None

    field = data.get("env_var", None)
    if field is not None:
        args["env_var"] = unmarshal_SecretEnvVar(field)
    else:
        args["env_var"] = None

    return Secret(**args)


def unmarshal_CronSchedule(data: Any) -> CronSchedule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CronSchedule' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("schedule", None)
    if field is not None:
        args["schedule"] = field
    else:
        args["schedule"] = None

    field = data.get("timezone", None)
    if field is not None:
        args["timezone"] = field
    else:
        args["timezone"] = None

    return CronSchedule(**args)


def unmarshal_JobDefinition(data: Any) -> JobDefinition:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'JobDefinition' failed as data isn't a dictionary."
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

    field = data.get("cpu_limit", None)
    if field is not None:
        args["cpu_limit"] = field
    else:
        args["cpu_limit"] = None

    field = data.get("memory_limit", None)
    if field is not None:
        args["memory_limit"] = field
    else:
        args["memory_limit"] = None

    field = data.get("image_uri", None)
    if field is not None:
        args["image_uri"] = field
    else:
        args["image_uri"] = None

    field = data.get("command", None)
    if field is not None:
        args["command"] = field
    else:
        args["command"] = None

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

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("environment_variables", None)
    if field is not None:
        args["environment_variables"] = field
    else:
        args["environment_variables"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("local_storage_capacity", None)
    if field is not None:
        args["local_storage_capacity"] = field
    else:
        args["local_storage_capacity"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("job_timeout", None)
    if field is not None:
        args["job_timeout"] = field
    else:
        args["job_timeout"] = None

    field = data.get("cron_schedule", None)
    if field is not None:
        args["cron_schedule"] = unmarshal_CronSchedule(field)
    else:
        args["cron_schedule"] = None

    return JobDefinition(**args)


def unmarshal_JobRun(data: Any) -> JobRun:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'JobRun' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("job_definition_id", None)
    if field is not None:
        args["job_definition_id"] = field
    else:
        args["job_definition_id"] = None

    field = data.get("state", None)
    if field is not None:
        args["state"] = field
    else:
        args["state"] = None

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

    field = data.get("cpu_limit", None)
    if field is not None:
        args["cpu_limit"] = field
    else:
        args["cpu_limit"] = None

    field = data.get("memory_limit", None)
    if field is not None:
        args["memory_limit"] = field
    else:
        args["memory_limit"] = None

    field = data.get("command", None)
    if field is not None:
        args["command"] = field
    else:
        args["command"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

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

    field = data.get("exit_code", None)
    if field is not None:
        args["exit_code"] = field
    else:
        args["exit_code"] = None

    field = data.get("run_duration", None)
    if field is not None:
        args["run_duration"] = field
    else:
        args["run_duration"] = None

    field = data.get("environment_variables", None)
    if field is not None:
        args["environment_variables"] = field
    else:
        args["environment_variables"] = None

    field = data.get("local_storage_capacity", None)
    if field is not None:
        args["local_storage_capacity"] = field
    else:
        args["local_storage_capacity"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("started_at", None)
    if field is not None:
        args["started_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["started_at"] = None

    return JobRun(**args)


def unmarshal_CreateJobDefinitionSecretsResponse(
    data: Any,
) -> CreateJobDefinitionSecretsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateJobDefinitionSecretsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("secrets", None)
    if field is not None:
        args["secrets"] = (
            [unmarshal_Secret(v) for v in field] if field is not None else None
        )
    else:
        args["secrets"] = []

    return CreateJobDefinitionSecretsResponse(**args)


def unmarshal_JobsLimits(data: Any) -> JobsLimits:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'JobsLimits' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("secrets_per_job_definition", None)
    if field is not None:
        args["secrets_per_job_definition"] = field
    else:
        args["secrets_per_job_definition"] = None

    return JobsLimits(**args)


def unmarshal_ListJobDefinitionSecretsResponse(
    data: Any,
) -> ListJobDefinitionSecretsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListJobDefinitionSecretsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("secrets", None)
    if field is not None:
        args["secrets"] = (
            [unmarshal_Secret(v) for v in field] if field is not None else None
        )
    else:
        args["secrets"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListJobDefinitionSecretsResponse(**args)


def unmarshal_ListJobDefinitionsResponse(data: Any) -> ListJobDefinitionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListJobDefinitionsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("job_definitions", None)
    if field is not None:
        args["job_definitions"] = (
            [unmarshal_JobDefinition(v) for v in field] if field is not None else None
        )
    else:
        args["job_definitions"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    return ListJobDefinitionsResponse(**args)


def unmarshal_ListJobRunsResponse(data: Any) -> ListJobRunsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListJobRunsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("job_runs", None)
    if field is not None:
        args["job_runs"] = (
            [unmarshal_JobRun(v) for v in field] if field is not None else None
        )
    else:
        args["job_runs"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    return ListJobRunsResponse(**args)


def unmarshal_Resource(data: Any) -> Resource:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Resource' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("cpu_limit", None)
    if field is not None:
        args["cpu_limit"] = field
    else:
        args["cpu_limit"] = None

    field = data.get("memory_limit", None)
    if field is not None:
        args["memory_limit"] = field
    else:
        args["memory_limit"] = None

    return Resource(**args)


def unmarshal_ListJobsResourcesResponse(data: Any) -> ListJobsResourcesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListJobsResourcesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("resources", None)
    if field is not None:
        args["resources"] = (
            [unmarshal_Resource(v) for v in field] if field is not None else None
        )
    else:
        args["resources"] = None

    return ListJobsResourcesResponse(**args)


def unmarshal_StartJobDefinitionResponse(data: Any) -> StartJobDefinitionResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'StartJobDefinitionResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("job_runs", None)
    if field is not None:
        args["job_runs"] = (
            [unmarshal_JobRun(v) for v in field] if field is not None else None
        )
    else:
        args["job_runs"] = None

    return StartJobDefinitionResponse(**args)


def marshal_CreateJobDefinitionRequestCronScheduleConfig(
    request: CreateJobDefinitionRequestCronScheduleConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.schedule is not None:
        output["schedule"] = request.schedule

    if request.timezone is not None:
        output["timezone"] = request.timezone

    return output


def marshal_CreateJobDefinitionRequest(
    request: CreateJobDefinitionRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

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

    if request.local_storage_capacity is not None:
        output["local_storage_capacity"] = request.local_storage_capacity

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.environment_variables is not None:
        output["environment_variables"] = {
            key: value for key, value in request.environment_variables.items()
        }

    if request.job_timeout is not None:
        output["job_timeout"] = request.job_timeout

    if request.cron_schedule is not None:
        output["cron_schedule"] = marshal_CreateJobDefinitionRequestCronScheduleConfig(
            request.cron_schedule, defaults
        )

    return output


def marshal_CreateJobDefinitionSecretsRequestSecretConfig(
    request: CreateJobDefinitionSecretsRequestSecretConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(param="path", value=request.path, marshal_func=None),
                OneOfPossibility(
                    param="env_var_name", value=request.env_var_name, marshal_func=None
                ),
            ]
        ),
    )

    if request.secret_manager_id is not None:
        output["secret_manager_id"] = request.secret_manager_id

    if request.secret_manager_version is not None:
        output["secret_manager_version"] = request.secret_manager_version

    return output


def marshal_CreateJobDefinitionSecretsRequest(
    request: CreateJobDefinitionSecretsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.secrets is not None:
        output["secrets"] = [
            marshal_CreateJobDefinitionSecretsRequestSecretConfig(item, defaults)
            for item in request.secrets
        ]

    return output


def marshal_StartJobDefinitionRequest(
    request: StartJobDefinitionRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.command is not None:
        output["command"] = request.command

    if request.environment_variables is not None:
        output["environment_variables"] = request.environment_variables

    if request.replicas is not None:
        output["replicas"] = request.replicas

    return output


def marshal_UpdateJobDefinitionRequestCronScheduleConfig(
    request: UpdateJobDefinitionRequestCronScheduleConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.schedule is not None:
        output["schedule"] = request.schedule

    if request.timezone is not None:
        output["timezone"] = request.timezone

    return output


def marshal_UpdateJobDefinitionRequest(
    request: UpdateJobDefinitionRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.cpu_limit is not None:
        output["cpu_limit"] = request.cpu_limit

    if request.memory_limit is not None:
        output["memory_limit"] = request.memory_limit

    if request.local_storage_capacity is not None:
        output["local_storage_capacity"] = request.local_storage_capacity

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

    if request.cron_schedule is not None:
        output["cron_schedule"] = marshal_UpdateJobDefinitionRequestCronScheduleConfig(
            request.cron_schedule, defaults
        )

    return output


def marshal_UpdateJobDefinitionSecretRequest(
    request: UpdateJobDefinitionSecretRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(param="path", value=request.path, marshal_func=None),
                OneOfPossibility(
                    param="env_var_name", value=request.env_var_name, marshal_func=None
                ),
            ]
        ),
    )

    if request.secret_manager_version is not None:
        output["secret_manager_version"] = request.secret_manager_version

    return output
