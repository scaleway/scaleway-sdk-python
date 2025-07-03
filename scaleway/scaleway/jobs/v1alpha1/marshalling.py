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
    JobRunState,
    ListJobDefinitionsRequestOrderBy,
    ListJobRunsRequestOrderBy,
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

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    return SecretEnvVar(**args)

def unmarshal_SecretFile(data: Any) -> SecretFile:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecretFile' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("path", str())
    args["path"] = field

    return SecretFile(**args)

def unmarshal_Secret(data: Any) -> Secret:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Secret' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("secret_id", str())
    args["secret_id"] = field

    field = data.get("secret_manager_id", str())
    args["secret_manager_id"] = field

    field = data.get("secret_manager_version", str())
    args["secret_manager_version"] = field

    field = data.get("file", None)
    args["file"] = unmarshal_SecretFile(field) if field is not None else None

    field = data.get("env_var", None)
    args["env_var"] = unmarshal_SecretEnvVar(field) if field is not None else None

    return Secret(**args)

def unmarshal_CronSchedule(data: Any) -> CronSchedule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CronSchedule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("schedule", str())
    args["schedule"] = field

    field = data.get("timezone", str())
    args["timezone"] = field

    return CronSchedule(**args)

def unmarshal_JobDefinition(data: Any) -> JobDefinition:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'JobDefinition' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("cpu_limit", str())
    args["cpu_limit"] = field

    field = data.get("memory_limit", str())
    args["memory_limit"] = field

    field = data.get("image_uri", str())
    args["image_uri"] = field

    field = data.get("command", str())
    args["command"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("environment_variables", str())
    args["environment_variables"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("local_storage_capacity", str())
    args["local_storage_capacity"] = field

    field = data.get("region", str())
    args["region"] = field

    field = data.get("job_timeout", None)
    args["job_timeout"] = field

    field = data.get("cron_schedule", None)
    args["cron_schedule"] = unmarshal_CronSchedule(field) if field is not None else None

    return JobDefinition(**args)

def unmarshal_JobRun(data: Any) -> JobRun:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'JobRun' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("job_definition_id", str())
    args["job_definition_id"] = field

    field = data.get("state", str())
    args["state"] = field

    field = data.get("error_message", str())
    args["error_message"] = field

    field = data.get("cpu_limit", str())
    args["cpu_limit"] = field

    field = data.get("memory_limit", str())
    args["memory_limit"] = field

    field = data.get("command", str())
    args["command"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("terminated_at", None)
    args["terminated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("exit_code", None)
    args["exit_code"] = field

    field = data.get("run_duration", None)
    args["run_duration"] = field

    field = data.get("environment_variables", str())
    args["environment_variables"] = field

    field = data.get("local_storage_capacity", str())
    args["local_storage_capacity"] = field

    field = data.get("region", str())
    args["region"] = field

    field = data.get("started_at", None)
    args["started_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return JobRun(**args)

def unmarshal_CreateJobDefinitionSecretsResponse(data: Any) -> CreateJobDefinitionSecretsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateJobDefinitionSecretsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("secrets", [])
    args["secrets"] = [unmarshal_Secret(v) for v in field] if field is not None else None

    return CreateJobDefinitionSecretsResponse(**args)

def unmarshal_JobsLimits(data: Any) -> JobsLimits:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'JobsLimits' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("secrets_per_job_definition", str())
    args["secrets_per_job_definition"] = field

    return JobsLimits(**args)

def unmarshal_ListJobDefinitionSecretsResponse(data: Any) -> ListJobDefinitionSecretsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListJobDefinitionSecretsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("secrets", [])
    args["secrets"] = [unmarshal_Secret(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListJobDefinitionSecretsResponse(**args)

def unmarshal_ListJobDefinitionsResponse(data: Any) -> ListJobDefinitionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListJobDefinitionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("job_definitions", str())
    args["job_definitions"] = [unmarshal_JobDefinition(v) for v in field] if field is not None else None

    field = data.get("total_count", str())
    args["total_count"] = field

    return ListJobDefinitionsResponse(**args)

def unmarshal_ListJobRunsResponse(data: Any) -> ListJobRunsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListJobRunsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("job_runs", str())
    args["job_runs"] = [unmarshal_JobRun(v) for v in field] if field is not None else None

    field = data.get("total_count", str())
    args["total_count"] = field

    return ListJobRunsResponse(**args)

def unmarshal_Resource(data: Any) -> Resource:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Resource' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("cpu_limit", str())
    args["cpu_limit"] = field

    field = data.get("memory_limit", str())
    args["memory_limit"] = field

    return Resource(**args)

def unmarshal_ListJobsResourcesResponse(data: Any) -> ListJobsResourcesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListJobsResourcesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("resources", str())
    args["resources"] = [unmarshal_Resource(v) for v in field] if field is not None else None

    return ListJobsResourcesResponse(**args)

def unmarshal_StartJobDefinitionResponse(data: Any) -> StartJobDefinitionResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'StartJobDefinitionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("job_runs", str())
    args["job_runs"] = [unmarshal_JobRun(v) for v in field] if field is not None else None

    return StartJobDefinitionResponse(**args)

def marshal_CreateJobDefinitionRequestCronScheduleConfig(
    request: CreateJobDefinitionRequestCronScheduleConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.schedule is not None:
        output["schedule"] = request.schedule
    else:
        output["schedule"] = str()

    if request.timezone is not None:
        output["timezone"] = request.timezone
    else:
        output["timezone"] = str()


    return output

def marshal_CreateJobDefinitionRequest(
    request: CreateJobDefinitionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.cpu_limit is not None:
        output["cpu_limit"] = request.cpu_limit
    else:
        output["cpu_limit"] = str()

    if request.memory_limit is not None:
        output["memory_limit"] = request.memory_limit
    else:
        output["memory_limit"] = str()

    if request.image_uri is not None:
        output["image_uri"] = request.image_uri
    else:
        output["image_uri"] = str()

    if request.command is not None:
        output["command"] = request.command
    else:
        output["command"] = str()

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.local_storage_capacity is not None:
        output["local_storage_capacity"] = request.local_storage_capacity
    else:
        output["local_storage_capacity"] = None

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.environment_variables is not None:
        output["environment_variables"] = {
            key: value
            for key, value in request.environment_variables.items()
        }
    else:
        output["environment_variables"] = None

    if request.job_timeout is not None:
        output["job_timeout"] = request.job_timeout
    else:
        output["job_timeout"] = None

    if request.cron_schedule is not None:
        output["cron_schedule"] = marshal_CreateJobDefinitionRequestCronScheduleConfig(request.cron_schedule, defaults)
    else:
        output["cron_schedule"] = None


    return output

def marshal_CreateJobDefinitionSecretsRequestSecretConfig(
    request: CreateJobDefinitionSecretsRequestSecretConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="path", value=request.path,marshal_func=None
            ),
            OneOfPossibility(param="env_var_name", value=request.env_var_name,marshal_func=None
            ),
        ]),
    )

    if request.secret_manager_id is not None:
        output["secret_manager_id"] = request.secret_manager_id
    else:
        output["secret_manager_id"] = str()

    if request.secret_manager_version is not None:
        output["secret_manager_version"] = request.secret_manager_version
    else:
        output["secret_manager_version"] = str()


    return output

def marshal_CreateJobDefinitionSecretsRequest(
    request: CreateJobDefinitionSecretsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.secrets is not None:
        output["secrets"] = [marshal_CreateJobDefinitionSecretsRequestSecretConfig(item, defaults) for item in request.secrets]
    else:
        output["secrets"] = str()


    return output

def marshal_StartJobDefinitionRequest(
    request: StartJobDefinitionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.command is not None:
        output["command"] = request.command
    else:
        output["command"] = None

    if request.environment_variables is not None:
        output["environment_variables"] = request.environment_variables
    else:
        output["environment_variables"] = None

    if request.replicas is not None:
        output["replicas"] = request.replicas
    else:
        output["replicas"] = None


    return output

def marshal_UpdateJobDefinitionRequestCronScheduleConfig(
    request: UpdateJobDefinitionRequestCronScheduleConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.schedule is not None:
        output["schedule"] = request.schedule
    else:
        output["schedule"] = None

    if request.timezone is not None:
        output["timezone"] = request.timezone
    else:
        output["timezone"] = None


    return output

def marshal_UpdateJobDefinitionRequest(
    request: UpdateJobDefinitionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.cpu_limit is not None:
        output["cpu_limit"] = request.cpu_limit
    else:
        output["cpu_limit"] = None

    if request.memory_limit is not None:
        output["memory_limit"] = request.memory_limit
    else:
        output["memory_limit"] = None

    if request.local_storage_capacity is not None:
        output["local_storage_capacity"] = request.local_storage_capacity
    else:
        output["local_storage_capacity"] = None

    if request.image_uri is not None:
        output["image_uri"] = request.image_uri
    else:
        output["image_uri"] = None

    if request.command is not None:
        output["command"] = request.command
    else:
        output["command"] = None

    if request.environment_variables is not None:
        output["environment_variables"] = request.environment_variables
    else:
        output["environment_variables"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.job_timeout is not None:
        output["job_timeout"] = request.job_timeout
    else:
        output["job_timeout"] = None

    if request.cron_schedule is not None:
        output["cron_schedule"] = marshal_UpdateJobDefinitionRequestCronScheduleConfig(request.cron_schedule, defaults)
    else:
        output["cron_schedule"] = None


    return output

def marshal_UpdateJobDefinitionSecretRequest(
    request: UpdateJobDefinitionSecretRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="path", value=request.path,marshal_func=None
            ),
            OneOfPossibility(param="env_var_name", value=request.env_var_name,marshal_func=None
            ),
        ]),
    )

    if request.secret_manager_version is not None:
        output["secret_manager_version"] = request.secret_manager_version
    else:
        output["secret_manager_version"] = None


    return output
