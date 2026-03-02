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


class JobRunReason(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_REASON = "unknown_reason"
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


class JobRunState(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATE = "unknown_state"
    INITIALIZED = "initialized"
    VALIDATED = "validated"
    QUEUED = "queued"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    INTERRUPTING = "interrupting"
    INTERRUPTED = "interrupted"
    RETRYING = "retrying"

    def __str__(self) -> str:
        return str(self.value)


class ListJobDefinitionsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListJobRunsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class SecretEnvVar:
    name: str


@dataclass
class SecretFile:
    path: str


@dataclass
class CronSchedule:
    schedule: str
    """
    UNIX cron schedule to run job (e.g., '* * * * *').
    """

    timezone: str
    """
    Timezone for the cron schedule, in tz database format (e.g., 'Europe/Paris').
    """


@dataclass
class RetryPolicy:
    max_retries: int
    """
    Maximum number of retries upon a job failure.
    """


@dataclass
class CreateJobDefinitionRequestCronScheduleConfig:
    schedule: str
    timezone: str


@dataclass
class CreateSecretsRequestSecretConfig:
    secret_manager_id: str
    secret_manager_version: str
    path: Optional[str] = None

    env_var_name: Optional[str] = None


@dataclass
class Secret:
    secret_id: str
    """
    UUID of the secret reference within the job.
    """

    secret_manager_id: str
    """
    UUID of the secret in Secret Manager.
    """

    secret_manager_version: str
    """
    Version of the secret in Secret Manager.
    """

    job_definition_id: str
    """
    UUID of the job definition.
    """

    file: Optional[SecretFile] = None

    env_var: Optional[SecretEnvVar] = None


@dataclass
class JobDefinition:
    id: str
    """
    UUID of the job definition.
    """

    name: str
    """
    Name of the job definition.
    """

    project_id: str
    """
    UUID of the Scaleway Project containing the job.
    """

    cpu_limit: int
    """
    CPU limit of the job (in mvCPU).
    """

    memory_limit: int
    """
    Memory limit of the job (in MiB).
    """

    local_storage_capacity: int
    """
    Local storage capacity of the job (in MiB).
    """

    image_uri: str
    """
    Image to use for the job.
    """

    command: str
    """
    Deprecated, please use startup_command instead.
    """

    environment_variables: dict[str, str]
    """
    Environment variables of the job.
    """

    description: str
    """
    Description of the job.
    """

    startup_command: list[str]
    """
    Job startup command.
    """

    args: list[str]
    """
    Job arguments passed to the startup command at runtime.
    """

    region: ScwRegion
    """
    Region to target. If none is passed will use default region from the config.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the job definition.
    """

    updated_at: Optional[datetime] = None
    """
    Last update date of the job definition.
    """

    job_timeout: Optional[str] = None
    """
    Timeout of the job in seconds.
    """

    cron_schedule: Optional[CronSchedule] = None
    """
    Configure a cron for the job.
    """

    retry_policy: Optional[RetryPolicy] = None
    """
    Retry behaviour in case of job failure.
    """


@dataclass
class Resource:
    compute_limit_mvcpu: int
    memory_limit_bytes: int


@dataclass
class JobRun:
    id: str
    """
    UUID of the job run.
    """

    job_definition_id: str
    """
    UUID of the job definition.
    """

    state: JobRunState
    """
    State of the job run.
    """

    cpu_limit: int
    """
    CPU limit of the job (in mvCPU).
    """

    memory_limit: int
    """
    Memory limit of the job (in MiB).
    """

    local_storage_capacity: int
    """
    Local storage capacity of the job (in MiB).
    """

    command: str
    """
    Deprecated, please use startup_command instead.
    """

    environment_variables: dict[str, str]
    """
    Environment variables of the job run.
    """

    startup_command: list[str]
    """
    Job startup command.
    """

    args: list[str]
    """
    Job arguments passed to the startup command at runtime.
    """

    region: ScwRegion
    """
    Region to target. If none is passed will use default region from the config.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the job run.
    """

    updated_at: Optional[datetime] = None
    """
    Last update date of the job run.
    """

    started_at: Optional[datetime] = None
    """
    Start date of the job run.
    """

    terminated_at: Optional[datetime] = None
    """
    Termination date of the job run.
    """

    run_duration: Optional[str] = None
    """
    Duration of the job run.
    """

    reason: Optional[JobRunReason] = JobRunReason.UNKNOWN_REASON
    """
    Reason for failure if the job failed.
    """

    exit_code: Optional[int] = 0
    """
    Exit code of the job.
    """

    error_message: Optional[str] = None
    """
    Error message if the job failed.
    """

    attempts: Optional[int] = 0
    """
    Number of retry attempts.
    """


@dataclass
class UpdateJobDefinitionRequestCronScheduleConfig:
    schedule: Optional[str] = None
    timezone: Optional[str] = None


@dataclass
class CreateJobDefinitionRequest:
    cpu_limit: int
    """
    CPU limit of the job (in mvCPU).
    """

    memory_limit: int
    """
    Memory limit of the job (in MiB).
    """

    local_storage_capacity: int
    """
    Local storage capacity of the job (in MiB).
    """

    image_uri: str
    """
    Image to use for the job.
    """

    command: str
    """
    Deprecated: please use startup_command instead.
    """

    description: str
    """
    Description of the job.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the job definition.
    """

    startup_command: Optional[list[str]] = field(default_factory=list)
    """
    The main executable or entrypoint script to run.
If both command and startup_command are provided, only startup_command will be used.
    """

    args: Optional[list[str]] = field(default_factory=list)
    """
    Passed to the startup command at runtime.
Environment variables and secrets can be included, and will be expanded before the arguments are used.
    """

    project_id: Optional[str] = None
    """
    UUID of the Scaleway Project containing the job.
    """

    environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Environment variables of the job.
    """

    job_timeout: Optional[str] = None
    """
    Timeout of the job in seconds.
    """

    cron_schedule: Optional[CreateJobDefinitionRequestCronScheduleConfig] = None
    """
    Configure a cron for the job.
    """

    retry_policy: Optional[RetryPolicy] = None
    """
    Retry behaviour in case of job failure.
    """


@dataclass
class CreateSecretsRequest:
    job_definition_id: str
    """
    UUID of the job definition.
    """

    secrets: list[CreateSecretsRequestSecretConfig]
    """
    List of secrets to inject into the job.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class CreateSecretsResponse:
    secrets: list[Secret]
    """
    List of secrets created.
    """


@dataclass
class DeleteJobDefinitionRequest:
    job_definition_id: str
    """
    UUID of the job definition to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteSecretRequest:
    secret_id: str
    """
    UUID of the secret reference within the job.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetJobDefinitionRequest:
    job_definition_id: str
    """
    UUID of the job definition to get.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetJobLimitsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetJobRunRequest:
    job_run_id: str
    """
    UUID of the job run to get.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetSecretRequest:
    secret_id: str
    """
    UUID of the secret reference within the job.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class JobLimits:
    secrets_per_job_definition: int


@dataclass
class ListJobDefinitionsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = None
    page_size: Optional[int] = None
    order_by: Optional[ListJobDefinitionsRequestOrderBy] = None
    project_id: Optional[str] = None
    organization_id: Optional[str] = None


@dataclass
class ListJobDefinitionsResponse:
    job_definitions: list[JobDefinition]
    total_count: int


@dataclass
class ListJobResourcesRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListJobResourcesResponse:
    resources: list[Resource]


@dataclass
class ListJobRunsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = None
    page_size: Optional[int] = None
    order_by: Optional[ListJobRunsRequestOrderBy] = None
    job_definition_id: Optional[str] = None
    project_id: Optional[str] = None
    organization_id: Optional[str] = None
    state: Optional[JobRunState] = None
    states: Optional[list[JobRunState]] = field(default_factory=list)
    reasons: Optional[list[JobRunReason]] = field(default_factory=list)


@dataclass
class ListJobRunsResponse:
    job_runs: list[JobRun]
    total_count: int


@dataclass
class ListSecretsRequest:
    job_definition_id: str
    """
    UUID of the job definition.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListSecretsResponse:
    secrets: list[Secret]
    """
    List of secret references within a job definition.
    """

    total_count: int
    """
    Total count of secret references within a job definition.
    """


@dataclass
class StartJobDefinitionRequest:
    job_definition_id: str
    """
    UUID of the job definition to start.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    command: Optional[str] = None
    """
    If empty or not defined, the image's default command is used.
Deprecated: please use startup_command instead.
    """

    startup_command: Optional[list[str]] = field(default_factory=list)
    """
    Overrides the default defined in the job image.
The main executable or entrypoint script to run.
If both command and startup_command are provided, only startup_command will be used.
    """

    args: Optional[list[str]] = field(default_factory=list)
    """
    Overrides the default arguments defined in the job image.
Passed to the contextual startup command at runtime.
Environment variables and secrets can be included, and will be expanded before the arguments are used.
    """

    environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Contextual environment variables for this specific job run.
    """

    replicas: Optional[int] = 0
    """
    Number of jobs to run.
    """


@dataclass
class StartJobDefinitionResponse:
    job_runs: list[JobRun]
    """
    List of started job runs.
    """


@dataclass
class StopJobRunRequest:
    job_run_id: str
    """
    UUID of the job run to stop.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class UpdateJobDefinitionRequest:
    job_definition_id: str
    """
    UUID of the job definition to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the job definition.
    """

    cpu_limit: Optional[int] = 0
    """
    CPU limit of the job (in mvCPU).
    """

    memory_limit: Optional[int] = 0
    """
    Memory limit of the job (in MiB).
    """

    local_storage_capacity: Optional[int] = 0
    """
    Local storage capacity of the job (in MiB).
    """

    image_uri: Optional[str] = None
    """
    Image to use for the job.
    """

    command: Optional[str] = None
    """
    Deprecated: please use startup_command instead.
    """

    startup_command: Optional[list[str]] = field(default_factory=list)
    """
    The main executable or entrypoint script to run.
If both command and startup_command are provided, only startup_command will be used.
    """

    args: Optional[list[str]] = field(default_factory=list)
    """
    Passed to the startup command at runtime.
Environment variables and secrets can be included, and will be expanded before the arguments are used.
    """

    environment_variables: Optional[dict[str, str]] = field(default_factory=dict)
    """
    Environment variables of the job.
    """

    description: Optional[str] = None
    """
    Description of the job.
    """

    job_timeout: Optional[str] = None
    """
    Timeout of the job in seconds.
    """

    cron_schedule: Optional[UpdateJobDefinitionRequestCronScheduleConfig] = None
    """
    Configure a cron for the job.
    """

    retry_policy: Optional[RetryPolicy] = None
    """
    Retry behaviour in case of job failure.
    """


@dataclass
class UpdateSecretRequest:
    secret_id: str
    """
    UUID of the secret reference within the job.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_manager_version: Optional[str] = None
    """
    Version of the secret in Secret Manager.
    """

    path: Optional[str] = None

    env_var_name: Optional[str] = None
