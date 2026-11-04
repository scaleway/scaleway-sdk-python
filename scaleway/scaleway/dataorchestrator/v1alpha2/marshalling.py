# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    DefaultTaskDefaultRunReason,
    RunServerlessContainersTaskAction,
    RunServerlessContainersTaskReason,
    RunServerlessContainersTaskStatus,
    RunStatus,
    ServerlessJobsTaskServerlessJobRunReason,
    TriggerType,
    WorkflowRunReason,
    WorkflowVersion,
    CronSchedule,
    WorkflowRunInfo,
    WorkflowDefinition,
    DefaultTask,
    RunServerlessContainersTask,
    S3Task,
    ServerlessJobsTask,
    TaskRun,
    WorkflowRun,
    ListWorkflowDefinitionsResponse,
    ListWorkflowRunsResponse,
    CreateWorkflowDefinitionRequestCronScheduleConfig,
    CreateWorkflowDefinitionRequestWorkflowVersionConfig,
    CreateWorkflowDefinitionRequest,
    StartWorkflowDefinitionRequest,
    UpdateWorkflowDefinitionRequestCronScheduleConfig,
    UpdateWorkflowDefinitionRequest,
    UpdateWorkflowVersionRequest,
)


def unmarshal_WorkflowVersion(data: Any) -> WorkflowVersion:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'WorkflowVersion' failed as data isn't a dictionary."
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

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("workflow_dsl", None)
    if field is not None:
        args["workflow_dsl"] = field
    else:
        args["workflow_dsl"] = None

    field = data.get("is_current", None)
    if field is not None:
        args["is_current"] = field
    else:
        args["is_current"] = False

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

    field = data.get("deleted_at", None)
    if field is not None:
        args["deleted_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["deleted_at"] = None

    return WorkflowVersion(**args)


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

    field = data.get("timezone_identifier", None)
    if field is not None:
        args["timezone_identifier"] = field
    else:
        args["timezone_identifier"] = None

    field = data.get("overlap", None)
    if field is not None:
        args["overlap"] = field
    else:
        args["overlap"] = None

    return CronSchedule(**args)


def unmarshal_WorkflowRunInfo(data: Any) -> WorkflowRunInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'WorkflowRunInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("workflow_run_id", None)
    if field is not None:
        args["workflow_run_id"] = field
    else:
        args["workflow_run_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = RunStatus.UNKNOWN_RUN_STATUS

    field = data.get("reason", None)
    if field is not None:
        args["reason"] = field
    else:
        args["reason"] = WorkflowRunReason.UNKNOWN_WORKFLOW_RUN_REASON

    return WorkflowRunInfo(**args)


def unmarshal_WorkflowDefinition(data: Any) -> WorkflowDefinition:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'WorkflowDefinition' failed as data isn't a dictionary."
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

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

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

    field = data.get("versions", None)
    if field is not None:
        args["versions"] = (
            [unmarshal_WorkflowVersion(v) for v in field] if field is not None else None
        )
    else:
        args["versions"] = []

    field = data.get("environment_variables", None)
    if field is not None:
        args["environment_variables"] = field
    else:
        args["environment_variables"] = {}

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("srn", None)
    if field is not None:
        args["srn"] = field
    else:
        args["srn"] = None

    field = data.get("cron_schedule", None)
    if field is not None:
        args["cron_schedule"] = unmarshal_CronSchedule(field)
    else:
        args["cron_schedule"] = None

    field = data.get("workflow_timeout", None)
    if field is not None:
        args["workflow_timeout"] = field
    else:
        args["workflow_timeout"] = None

    field = data.get("last_run", None)
    if field is not None:
        args["last_run"] = unmarshal_WorkflowRunInfo(field)
    else:
        args["last_run"] = None

    return WorkflowDefinition(**args)


def unmarshal_DefaultTask(data: Any) -> DefaultTask:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DefaultTask' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("reason", None)
    if field is not None:
        args["reason"] = field
    else:
        args["reason"] = DefaultTaskDefaultRunReason.UNKNOWN_DEFAULT_RUN_REASON

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

    return DefaultTask(**args)


def unmarshal_RunServerlessContainersTask(data: Any) -> RunServerlessContainersTask:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RunServerlessContainersTask' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("container_id", None)
    if field is not None:
        args["container_id"] = field
    else:
        args["container_id"] = None

    field = data.get("image_url", None)
    if field is not None:
        args["image_url"] = field
    else:
        args["image_url"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = RunServerlessContainersTaskStatus.UNKNOWN_STATUS

    field = data.get("action", None)
    if field is not None:
        args["action"] = field
    else:
        args["action"] = RunServerlessContainersTaskAction.UNKNOWN_ACTION

    field = data.get("reason", None)
    if field is not None:
        args["reason"] = field
    else:
        args["reason"] = RunServerlessContainersTaskReason.UNKNOWN_REASON

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

    return RunServerlessContainersTask(**args)


def unmarshal_S3Task(data: Any) -> S3Task:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'S3Task' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("action", None)
    if field is not None:
        args["action"] = field
    else:
        args["action"] = None

    field = data.get("reason", None)
    if field is not None:
        args["reason"] = field
    else:
        args["reason"] = None

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

    return S3Task(**args)


def unmarshal_ServerlessJobsTask(data: Any) -> ServerlessJobsTask:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerlessJobsTask' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("job_definition_id", None)
    if field is not None:
        args["job_definition_id"] = field
    else:
        args["job_definition_id"] = None

    field = data.get("job_run_id", None)
    if field is not None:
        args["job_run_id"] = field
    else:
        args["job_run_id"] = None

    field = data.get("reason", None)
    if field is not None:
        args["reason"] = field
    else:
        args["reason"] = (
            ServerlessJobsTaskServerlessJobRunReason.UNKNOWN_SERVERLESS_JOB_RUN_REASON
        )

    field = data.get("exit_code", None)
    if field is not None:
        args["exit_code"] = field
    else:
        args["exit_code"] = 0

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

    return ServerlessJobsTask(**args)


def unmarshal_TaskRun(data: Any) -> TaskRun:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TaskRun' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("task_name", None)
    if field is not None:
        args["task_name"] = field
    else:
        args["task_name"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = RunStatus.UNKNOWN_RUN_STATUS

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

    field = data.get("duration", None)
    if field is not None:
        args["duration"] = field
    else:
        args["duration"] = None

    field = data.get("output", None)
    if field is not None:
        args["output"] = field
    else:
        args["output"] = None

    field = data.get("serverless_job_task_run_details", None)
    if field is not None:
        args["serverless_job_task_run_details"] = unmarshal_ServerlessJobsTask(field)
    else:
        args["serverless_job_task_run_details"] = None

    field = data.get("raise_task_run_details", None)
    if field is not None:
        args["raise_task_run_details"] = unmarshal_DefaultTask(field)
    else:
        args["raise_task_run_details"] = None

    field = data.get("set_task_run_details", None)
    if field is not None:
        args["set_task_run_details"] = unmarshal_DefaultTask(field)
    else:
        args["set_task_run_details"] = None

    field = data.get("call_http_task_run_details", None)
    if field is not None:
        args["call_http_task_run_details"] = unmarshal_DefaultTask(field)
    else:
        args["call_http_task_run_details"] = None

    field = data.get("wait_task_run_details", None)
    if field is not None:
        args["wait_task_run_details"] = unmarshal_DefaultTask(field)
    else:
        args["wait_task_run_details"] = None

    field = data.get("serverless_function_task_run_details", None)
    if field is not None:
        args["serverless_function_task_run_details"] = unmarshal_DefaultTask(field)
    else:
        args["serverless_function_task_run_details"] = None

    field = data.get("run_serverless_container_task_run_details", None)
    if field is not None:
        args["run_serverless_container_task_run_details"] = (
            unmarshal_RunServerlessContainersTask(field)
        )
    else:
        args["run_serverless_container_task_run_details"] = None

    field = data.get("call_serverless_container_task_run_details", None)
    if field is not None:
        args["call_serverless_container_task_run_details"] = unmarshal_DefaultTask(
            field
        )
    else:
        args["call_serverless_container_task_run_details"] = None

    field = data.get("s3_task_run_details", None)
    if field is not None:
        args["s3_task_run_details"] = unmarshal_S3Task(field)
    else:
        args["s3_task_run_details"] = None

    field = data.get("generative_api_task_run_details", None)
    if field is not None:
        args["generative_api_task_run_details"] = unmarshal_DefaultTask(field)
    else:
        args["generative_api_task_run_details"] = None

    field = data.get("run_iteration", None)
    if field is not None:
        args["run_iteration"] = field
    else:
        args["run_iteration"] = 0

    return TaskRun(**args)


def unmarshal_WorkflowRun(data: Any) -> WorkflowRun:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'WorkflowRun' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("workflow_definition_id", None)
    if field is not None:
        args["workflow_definition_id"] = field
    else:
        args["workflow_definition_id"] = None

    field = data.get("workflow_definition_name", None)
    if field is not None:
        args["workflow_definition_name"] = field
    else:
        args["workflow_definition_name"] = None

    field = data.get("workflow_version_id", None)
    if field is not None:
        args["workflow_version_id"] = field
    else:
        args["workflow_version_id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("trigger_type", None)
    if field is not None:
        args["trigger_type"] = field
    else:
        args["trigger_type"] = TriggerType.UNKNOWN_TRIGGER_TYPE

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = RunStatus.UNKNOWN_RUN_STATUS

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

    field = data.get("duration", None)
    if field is not None:
        args["duration"] = field
    else:
        args["duration"] = None

    field = data.get("reason", None)
    if field is not None:
        args["reason"] = field
    else:
        args["reason"] = WorkflowRunReason.UNKNOWN_WORKFLOW_RUN_REASON

    field = data.get("task_runs", None)
    if field is not None:
        args["task_runs"] = (
            [unmarshal_TaskRun(v) for v in field] if field is not None else None
        )
    else:
        args["task_runs"] = []

    field = data.get("environment_variables", None)
    if field is not None:
        args["environment_variables"] = field
    else:
        args["environment_variables"] = {}

    field = data.get("workflow_dsl", None)
    if field is not None:
        args["workflow_dsl"] = field
    else:
        args["workflow_dsl"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("srn", None)
    if field is not None:
        args["srn"] = field
    else:
        args["srn"] = None

    field = data.get("output", None)
    if field is not None:
        args["output"] = field
    else:
        args["output"] = None

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

    return WorkflowRun(**args)


def unmarshal_ListWorkflowDefinitionsResponse(
    data: Any,
) -> ListWorkflowDefinitionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListWorkflowDefinitionsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("workflow_definitions", None)
    if field is not None:
        args["workflow_definitions"] = (
            [unmarshal_WorkflowDefinition(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["workflow_definitions"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    return ListWorkflowDefinitionsResponse(**args)


def unmarshal_ListWorkflowRunsResponse(data: Any) -> ListWorkflowRunsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListWorkflowRunsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("workflow_runs", None)
    if field is not None:
        args["workflow_runs"] = (
            [unmarshal_WorkflowRun(v) for v in field] if field is not None else None
        )
    else:
        args["workflow_runs"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListWorkflowRunsResponse(**args)


def marshal_CreateWorkflowDefinitionRequestCronScheduleConfig(
    request: CreateWorkflowDefinitionRequestCronScheduleConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.schedule is not None:
        output["schedule"] = request.schedule

    if request.timezone_identifier is not None:
        output["timezone_identifier"] = request.timezone_identifier

    if request.overlap is not None:
        output["overlap"] = request.overlap

    return output


def marshal_CreateWorkflowDefinitionRequestWorkflowVersionConfig(
    request: CreateWorkflowDefinitionRequestWorkflowVersionConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.workflow_dsl is not None:
        output["workflow_dsl"] = request.workflow_dsl

    return output


def marshal_CreateWorkflowDefinitionRequest(
    request: CreateWorkflowDefinitionRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.workflow_version is not None:
        output["workflow_version"] = (
            marshal_CreateWorkflowDefinitionRequestWorkflowVersionConfig(
                request.workflow_version, defaults
            )
        )

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.environment_variables is not None:
        output["environment_variables"] = {
            key: value for key, value in request.environment_variables.items()
        }

    if request.workflow_timeout is not None:
        output["workflow_timeout"] = request.workflow_timeout

    if request.cron_schedule is not None:
        output["cron_schedule"] = (
            marshal_CreateWorkflowDefinitionRequestCronScheduleConfig(
                request.cron_schedule, defaults
            )
        )

    return output


def marshal_StartWorkflowDefinitionRequest(
    request: StartWorkflowDefinitionRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.environment_variables is not None:
        output["environment_variables"] = request.environment_variables

    return output


def marshal_UpdateWorkflowDefinitionRequestCronScheduleConfig(
    request: UpdateWorkflowDefinitionRequestCronScheduleConfig,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.schedule is not None:
        output["schedule"] = request.schedule

    if request.timezone_identifier is not None:
        output["timezone_identifier"] = request.timezone_identifier

    if request.overlap is not None:
        output["overlap"] = request.overlap

    return output


def marshal_UpdateWorkflowDefinitionRequest(
    request: UpdateWorkflowDefinitionRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.environment_variables is not None:
        output["environment_variables"] = request.environment_variables

    if request.workflow_timeout is not None:
        output["workflow_timeout"] = request.workflow_timeout

    if request.cron_schedule is not None:
        output["cron_schedule"] = (
            marshal_UpdateWorkflowDefinitionRequestCronScheduleConfig(
                request.cron_schedule, defaults
            )
        )

    return output


def marshal_UpdateWorkflowVersionRequest(
    request: UpdateWorkflowVersionRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.workflow_dsl is not None:
        output["workflow_dsl"] = request.workflow_dsl

    return output
