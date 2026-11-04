# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class DefaultTaskDefaultRunReason(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_DEFAULT_RUN_REASON = "unknown_default_run_reason"
    TIMEOUT = "timeout"
    CANCELLATION = "cancellation"
    TECHNICAL_ERROR = "technical_error"
    FUNCTIONAL_ERROR = "functional_error"

    def __str__(self) -> str:
        return str(self.value)


class ListWorkflowDefinitionsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListWorkflowRunsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    TERMINATED_AT_ASC = "terminated_at_asc"
    TERMINATED_AT_DESC = "terminated_at_desc"
    DURATION_ASC = "duration_asc"
    DURATION_DESC = "duration_desc"
    WORKFLOW_DEFINITION_NAME_ASC = "workflow_definition_name_asc"
    WORKFLOW_DEFINITION_NAME_DESC = "workflow_definition_name_desc"

    def __str__(self) -> str:
        return str(self.value)


class RunServerlessContainersTaskAction(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ACTION = "unknown_action"
    DEPLOY = "deploy"
    DELETE = "delete"
    GET = "get"

    def __str__(self) -> str:
        return str(self.value)


class RunServerlessContainersTaskReason(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_REASON = "unknown_reason"
    TIMEOUT = "timeout"
    CANCELLATION = "cancellation"
    TECHNICAL_ERROR = "technical_error"
    FUNCTIONAL_ERROR = "functional_error"

    def __str__(self) -> str:
        return str(self.value)


class RunServerlessContainersTaskStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    UPDATING = "updating"
    CREATING = "creating"
    LOCKED = "locked"
    UPGRADING = "upgrading"
    REBALANCING = "rebalancing"
    TRIGGERING = "triggering"

    def __str__(self) -> str:
        return str(self.value)


class RunStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_RUN_STATUS = "unknown_run_status"
    INITIALIZED = "initialized"
    VALIDATED = "validated"
    QUEUED = "queued"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    INTERRUPTING = "interrupting"
    INTERRUPTED = "interrupted"
    PAUSING = "pausing"
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)


class S3TaskReason(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_DEFAULT_RUN_REASON = "unknown_default_run_reason"
    TIMEOUT = "timeout"
    CANCELLATION = "cancellation"
    TECHNICAL_ERROR = "technical_error"
    FUNCTIONAL_ERROR = "functional_error"

    def __str__(self) -> str:
        return str(self.value)


class ScheduleOverlapPolicy(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SCHEDULE_OVERLAP_POLICY = "unknown_schedule_overlap_policy"
    FORBID = "forbid"
    BUFFER_ONE = "buffer_one"
    BUFFER_ALL = "buffer_all"
    ALLOW_ALL = "allow_all"

    def __str__(self) -> str:
        return str(self.value)


class ServerlessJobsTaskServerlessJobRunReason(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SERVERLESS_JOB_RUN_REASON = "unknown_serverless_job_run_reason"
    INVALID_REQUEST = "invalid_request"
    TIMEOUT = "timeout"
    CANCELLATION = "cancellation"
    TECHNICAL_ERROR = "technical_error"
    IMAGE_NOT_FOUND = "image_not_found"
    INVALID_IMAGE = "invalid_image"
    MEMORY_USAGE_EXCEEDED = "memory_usage_exceeded"
    STORAGE_USAGE_EXCEEDED = "storage_usage_exceeded"
    EXITED_WITH_ERROR = "exited_with_error"
    SECRET_DISABLED = "secret_disabled"
    SECRET_NOT_FOUND = "secret_not_found"
    QUOTA_EXCEEDED = "quota_exceeded"

    def __str__(self) -> str:
        return str(self.value)


class TriggerType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TRIGGER_TYPE = "unknown_trigger_type"
    MANUAL = "manual"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)


class WorkflowRunReason(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_WORKFLOW_RUN_REASON = "unknown_workflow_run_reason"
    TIMEOUT = "timeout"
    CANCELLATION = "cancellation"
    TECHNICAL_ERROR = "technical_error"
    FUNCTIONAL_ERROR = "functional_error"
    NOT_FOUND = "not_found"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class DefaultTask:
    reason: Optional[DefaultTaskDefaultRunReason] = (
        DefaultTaskDefaultRunReason.UNKNOWN_DEFAULT_RUN_REASON
    )
    """
    Current reason of the task run.
    """

    error_message: Optional[str] = None
    """
    Error message of the task run.
    """


@dataclass
class RunServerlessContainersTask:
    container_id: str
    """
    Unique identifier of the serverless-container deployment.
    """

    image_url: str
    """
    Image deployed with the serverless-container.
    """

    status: RunServerlessContainersTaskStatus
    """
    Status of the serverless-container deployment.
    """

    action: RunServerlessContainersTaskAction
    """
    Action used on the serverless-container deployment.
    """

    reason: Optional[RunServerlessContainersTaskReason] = (
        RunServerlessContainersTaskReason.UNKNOWN_REASON
    )
    """
    Current reason of the task run.
    """

    error_message: Optional[str] = None
    """
    Error message of the task run.
    """


@dataclass
class S3Task:
    action: str
    reason: Optional[S3TaskReason] = None
    error_message: Optional[str] = None


@dataclass
class ServerlessJobsTask:
    job_definition_id: str
    """
    Unique identifier of the serverless-job definition.
    """

    job_run_id: str
    """
    Unique identifier of the serverless-job run.
    """

    reason: Optional[ServerlessJobsTaskServerlessJobRunReason] = (
        ServerlessJobsTaskServerlessJobRunReason.UNKNOWN_SERVERLESS_JOB_RUN_REASON
    )
    """
    Terminated reason of the serverless-job run.
    """

    exit_code: Optional[int] = 0
    """
    Exit code of the serverless-job run.
    """

    error_message: Optional[str] = None
    """
    Error message of the serverless-job run.
    """


@dataclass
class CronSchedule:
    schedule: str
    """
    UNIX cron schedule to run workflow (e.g., '* * * * *').
    """

    timezone_identifier: str
    """
    Timezone identifier for the cron schedule, in tz database format (e.g., 'Europe/Paris').
    """

    overlap: ScheduleOverlapPolicy
    """
    Controls what happens when an WorkflowDefinition would be started by a Schedule.
    """


@dataclass
class WorkflowRunInfo:
    workflow_run_id: str
    """
    Workflow run ID.
    """

    status: RunStatus
    """
    Workflow run status.
    """

    reason: Optional[WorkflowRunReason] = WorkflowRunReason.UNKNOWN_WORKFLOW_RUN_REASON
    """
    Workflow run reason.
    """


@dataclass
class WorkflowVersion:
    id: str
    """
    Unique identifier.
    """

    name: str
    """
    Name of the workflow version.
    """

    description: str
    """
    Description of the workflow version.
    """

    workflow_dsl: str
    """
    DSL of workflow in YAML format based from https://open-workflow-specification.org/schemas/1.0.3/workflow.yaml.
    """

    is_current: bool
    """
    Indicate if the version is the current selected by the workflow to run.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the workflow version.
    """

    updated_at: Optional[datetime] = None
    """
    Last modification date of the workflow version.
    """

    deleted_at: Optional[datetime] = None
    """
    Deleted date of the workflow version.
    """


@dataclass
class TaskRun:
    id: str
    """
    Unique identifier.
    """

    task_name: str
    """
    Unique identifier of the task.
    """

    status: RunStatus
    """
    Status of the task run.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the task run.
    """

    updated_at: Optional[datetime] = None
    """
    Last modification date of the task run.
    """

    terminated_at: Optional[datetime] = None
    """
    Terminated date of the task run.
    """

    duration: Optional[str] = None
    """
    Run duration of the task run.
    """

    output: Optional[str] = None
    """
    Output of the task run.
    """

    run_iteration: Optional[int] = 0
    """
    Run iteration of the task (in loop or retry).
    """

    serverless_job_task_run_details: Optional[ServerlessJobsTask] = None

    raise_task_run_details: Optional[DefaultTask] = None

    set_task_run_details: Optional[DefaultTask] = None

    call_http_task_run_details: Optional[DefaultTask] = None

    wait_task_run_details: Optional[DefaultTask] = None

    serverless_function_task_run_details: Optional[DefaultTask] = None

    run_serverless_container_task_run_details: Optional[RunServerlessContainersTask] = (
        None
    )

    call_serverless_container_task_run_details: Optional[DefaultTask] = None

    s3_task_run_details: Optional[S3Task] = None

    generative_api_task_run_details: Optional[DefaultTask] = None


@dataclass
class CreateWorkflowDefinitionRequestCronScheduleConfig:
    schedule: str
    timezone_identifier: str
    overlap: Optional[ScheduleOverlapPolicy] = None


@dataclass
class CreateWorkflowDefinitionRequestWorkflowVersionConfig:
    name: str
    description: str
    workflow_dsl: Optional[str] = None


@dataclass
class WorkflowDefinition:
    id: str
    """
    Unique identifier.
    """

    name: str
    """
    Name of the workflow definition.
    """

    description: str
    """
    Description of the workflow definition.
    """

    project_id: str
    """
    Project ID.
    """

    versions: list[WorkflowVersion]
    """
    Versions of workflow.
    """

    environment_variables: dict[str, str]
    """
    Environment variables of the workflow.
    """

    region: ScwRegion
    """
    Region of the workflow.
    """

    srn: str
    """
    The SRN of the workflow definition.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the workflow definition.
    """

    updated_at: Optional[datetime] = None
    """
    Last modification date of the workflow definition.
    """

    cron_schedule: Optional[CronSchedule] = None
    """
    Configure a cron for the workflow.
    """

    workflow_timeout: Optional[str] = None
    """
    Timeout of the workflow in seconds.
    """

    last_run: Optional[WorkflowRunInfo] = None
    """
    Last workflow run information.
    """


@dataclass
class WorkflowRun:
    id: str
    """
    Unique identifier.
    """

    workflow_definition_id: str
    """
    Unique identifier of the workflow definition.
    """

    workflow_definition_name: str
    """
    Name of the workflow definition.
    """

    workflow_version_id: str
    """
    Unique identifier of the workflow version.
    """

    project_id: str
    """
    Unique identifier of the project.
    """

    trigger_type: TriggerType
    """
    Type of trigger that started the workflow run.
    """

    status: RunStatus
    """
    Current status of the workflow run.
    """

    task_runs: list[TaskRun]
    """
    Task runs of the workflow run.
    """

    environment_variables: dict[str, str]
    """
    Environment variables of the workflow run.
    """

    workflow_dsl: str
    """
    DSL of workflow in YAML format based from https://open-workflow-specification.org/schemas/1.0.3/workflow.yaml.
    """

    region: ScwRegion
    """
    Region of the workflow run.
    """

    srn: str
    """
    The SRN of the workflow run.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the workflow run.
    """

    updated_at: Optional[datetime] = None
    """
    Last modification date of the workflow run.
    """

    terminated_at: Optional[datetime] = None
    """
    Terminated date of the workflow run.
    """

    duration: Optional[str] = None
    """
    Run duration of the workflow run.
    """

    reason: Optional[WorkflowRunReason] = WorkflowRunReason.UNKNOWN_WORKFLOW_RUN_REASON
    """
    Current reason of the workflow run.
    """

    output: Optional[str] = None
    """
    Output of the workflow run.
    """

    error_message: Optional[str] = None
    """
    Error message of the workflow run.
    """


@dataclass
class UpdateWorkflowDefinitionRequestCronScheduleConfig:
    schedule: Optional[str] = None
    timezone_identifier: Optional[str] = None
    overlap: Optional[ScheduleOverlapPolicy] = None


@dataclass
class CreateWorkflowDefinitionRequest:
    description: str
    """
    Description of the workflow.
    """

    workflow_version: CreateWorkflowDefinitionRequestWorkflowVersionConfig
    """
    Version of the workflow definition.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the workflow definition.
    """

    project_id: Optional[str] = None
    """
    UUID of the Scaleway Project containing the workflow.
    """

    environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Environment variables of the workflow.
    """

    workflow_timeout: Optional[str] = None
    """
    Timeout of the workflow in seconds.
    """

    cron_schedule: Optional[CreateWorkflowDefinitionRequestCronScheduleConfig] = None
    """
    Configure a cron for the workflow.
    """


@dataclass
class DeleteWorkflowDefinitionRequest:
    workflow_definition_id: str
    """
    UUID of the workflow definition to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteWorkflowRunRequest:
    workflow_run_id: str
    """
    UUID of the workflow run to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetWorkflowDefinitionRequest:
    workflow_definition_id: str
    """
    UUID of the workflow definition to get.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetWorkflowRunRequest:
    workflow_run_id: str
    """
    UUID of the workflow run to get.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListWorkflowDefinitionsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    page_size: Optional[int] = 0
    order_by: Optional[ListWorkflowDefinitionsRequestOrderBy] = (
        ListWorkflowDefinitionsRequestOrderBy.CREATED_AT_ASC
    )
    name: Optional[str] = None
    statuses: Optional[list[RunStatus]] = field(default_factory=list)
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None
    trigger_types: Optional[list[TriggerType]] = field(default_factory=list)
    project_id: Optional[str] = None

    organization_id: Optional[str] = None


@dataclass
class ListWorkflowDefinitionsResponse:
    workflow_definitions: list[WorkflowDefinition]
    total_count: int


@dataclass
class ListWorkflowRunsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    page_size: Optional[int] = 0
    order_by: Optional[ListWorkflowRunsRequestOrderBy] = (
        ListWorkflowRunsRequestOrderBy.CREATED_AT_ASC
    )
    workflow_definition_id: Optional[str] = None
    statuses: Optional[list[RunStatus]] = field(default_factory=list)
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None
    trigger_types: Optional[list[TriggerType]] = field(default_factory=list)
    workflow_definition_name: Optional[str] = None
    project_id: Optional[str] = None

    organization_id: Optional[str] = None


@dataclass
class ListWorkflowRunsResponse:
    workflow_runs: list[WorkflowRun]
    """
    List workflow runs.
    """

    total_count: int
    """
    Total count of workflow runs.
    """


@dataclass
class PauseWorkflowRunRequest:
    workflow_run_id: str
    """
    UUID of the workflow run to pause.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ResumeWorkflowRunRequest:
    workflow_run_id: str
    """
    UUID of the workflow run to resume.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class StartWorkflowDefinitionRequest:
    workflow_definition_id: str
    """
    UUID of the workflow definition to start.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Contextual environment variables for this specific workflow run.
    """


@dataclass
class TerminateWorkflowRunRequest:
    workflow_run_id: str
    """
    UUID of the workflow run to terminate.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class UpdateWorkflowDefinitionRequest:
    workflow_definition_id: str
    """
    UUID of the workflow definition to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the workflow definition.
    """

    description: Optional[str] = None
    """
    Description of the workflow.
    """

    environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Environment variables of the workflow.
    """

    workflow_timeout: Optional[str] = None
    """
    Timeout of the workflow in seconds.
    """

    cron_schedule: Optional[UpdateWorkflowDefinitionRequestCronScheduleConfig] = None
    """
    Configure a cron for the workflow.
    """


@dataclass
class UpdateWorkflowVersionRequest:
    workflow_version_id: str
    """
    UUID of the workflow version to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the workflow version.
    """

    description: Optional[str] = None
    """
    Description of the workflow version.
    """

    workflow_dsl: Optional[str] = None
    """
    DSL of workflow in YAML format based from https://open-workflow-specification.org/schemas/1.0.3/workflow.yaml.
    """
