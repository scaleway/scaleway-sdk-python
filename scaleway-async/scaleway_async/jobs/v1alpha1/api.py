# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    random_name,
    validate_path_param,
    fetch_all_pages_async,
)
from .types import (
    JobRunState,
    ListJobDefinitionsRequestOrderBy,
    ListJobRunsRequestOrderBy,
    CreateJobDefinitionRequest,
    CreateJobDefinitionRequestCronScheduleConfig,
    CreateJobDefinitionSecretsRequest,
    CreateJobDefinitionSecretsRequestSecretConfig,
    CreateJobDefinitionSecretsResponse,
    JobDefinition,
    JobRun,
    JobsLimits,
    ListJobDefinitionSecretsResponse,
    ListJobDefinitionsResponse,
    ListJobRunsResponse,
    ListJobsResourcesResponse,
    Secret,
    StartJobDefinitionRequest,
    StartJobDefinitionResponse,
    UpdateJobDefinitionRequest,
    UpdateJobDefinitionRequestCronScheduleConfig,
    UpdateJobDefinitionSecretRequest,
)
from .marshalling import (
    unmarshal_Secret,
    unmarshal_JobDefinition,
    unmarshal_JobRun,
    unmarshal_CreateJobDefinitionSecretsResponse,
    unmarshal_JobsLimits,
    unmarshal_ListJobDefinitionSecretsResponse,
    unmarshal_ListJobDefinitionsResponse,
    unmarshal_ListJobRunsResponse,
    unmarshal_ListJobsResourcesResponse,
    unmarshal_StartJobDefinitionResponse,
    marshal_CreateJobDefinitionRequest,
    marshal_CreateJobDefinitionSecretsRequest,
    marshal_StartJobDefinitionRequest,
    marshal_UpdateJobDefinitionRequest,
    marshal_UpdateJobDefinitionSecretRequest,
)


class JobsV1Alpha1API(API):
    """
    This API allows you to manage your Serverless Jobs.
    """

    async def create_job_definition(
        self,
        *,
        cpu_limit: int,
        memory_limit: int,
        image_uri: str,
        command: str,
        description: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        local_storage_capacity: Optional[int] = None,
        project_id: Optional[str] = None,
        environment_variables: Optional[dict[str, str]] = None,
        job_timeout: Optional[str] = None,
        cron_schedule: Optional[CreateJobDefinitionRequestCronScheduleConfig] = None,
    ) -> JobDefinition:
        """
        Create a new job definition in a specified Project.
        :param cpu_limit: CPU limit of the job.
        :param memory_limit: Memory limit of the job (in MiB).
        :param image_uri: Image to use for the job.
        :param command: Startup command. If empty or not defined, the image's default command is used.
        :param description: Description of the job.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the job definition.
        :param local_storage_capacity: Local storage capacity of the job (in MiB).
        :param project_id: UUID of the Scaleway Project containing the job.
        :param environment_variables: Environment variables of the job.
        :param job_timeout: Timeout of the job in seconds.
        :param cron_schedule: Configure a cron for the job.
        :return: :class:`JobDefinition <JobDefinition>`

        Usage:
        ::

            result = await api.create_job_definition(
                cpu_limit=1,
                memory_limit=1,
                image_uri="example",
                command="example",
                description="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-definitions",
            body=marshal_CreateJobDefinitionRequest(
                CreateJobDefinitionRequest(
                    cpu_limit=cpu_limit,
                    memory_limit=memory_limit,
                    image_uri=image_uri,
                    command=command,
                    description=description,
                    region=region,
                    name=name or random_name(prefix="job"),
                    local_storage_capacity=local_storage_capacity,
                    project_id=project_id,
                    environment_variables=environment_variables,
                    job_timeout=job_timeout,
                    cron_schedule=cron_schedule,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_JobDefinition(res.json())

    async def get_job_definition(
        self,
        *,
        job_definition_id: str,
        region: Optional[ScwRegion] = None,
    ) -> JobDefinition:
        """
        Get a job definition by its unique identifier.
        :param job_definition_id: UUID of the job definition to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`JobDefinition <JobDefinition>`

        Usage:
        ::

            result = await api.get_job_definition(
                job_definition_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_job_definition_id = validate_path_param(
            "job_definition_id", job_definition_id
        )

        res = self._request(
            "GET",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-definitions/{param_job_definition_id}",
        )

        self._throw_on_error(res)
        return unmarshal_JobDefinition(res.json())

    async def list_job_definitions(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListJobDefinitionsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
    ) -> ListJobDefinitionsResponse:
        """
        List all your job definitions with filters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param project_id:
        :param organization_id:
        :return: :class:`ListJobDefinitionsResponse <ListJobDefinitionsResponse>`

        Usage:
        ::

            result = await api.list_job_definitions()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-definitions",
            params={
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListJobDefinitionsResponse(res.json())

    async def list_job_definitions_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListJobDefinitionsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
    ) -> list[JobDefinition]:
        """
        List all your job definitions with filters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param project_id:
        :param organization_id:
        :return: :class:`list[JobDefinition] <list[JobDefinition]>`

        Usage:
        ::

            result = await api.list_job_definitions_all()
        """

        return await fetch_all_pages_async(
            type=ListJobDefinitionsResponse,
            key="job_definitions",
            fetcher=self.list_job_definitions,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
                "organization_id": organization_id,
            },
        )

    async def update_job_definition(
        self,
        *,
        job_definition_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        cpu_limit: Optional[int] = None,
        memory_limit: Optional[int] = None,
        local_storage_capacity: Optional[int] = None,
        image_uri: Optional[str] = None,
        command: Optional[str] = None,
        environment_variables: Optional[dict[str, str]] = None,
        description: Optional[str] = None,
        job_timeout: Optional[str] = None,
        cron_schedule: Optional[UpdateJobDefinitionRequestCronScheduleConfig] = None,
    ) -> JobDefinition:
        """
        Update an existing job definition associated with the specified unique identifier.
        :param job_definition_id: UUID of the job definition to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the job definition.
        :param cpu_limit: CPU limit of the job.
        :param memory_limit: Memory limit of the job (in MiB).
        :param local_storage_capacity: Local storage capacity of the job (in MiB).
        :param image_uri: Image to use for the job.
        :param command: Startup command.
        :param environment_variables: Environment variables of the job.
        :param description: Description of the job.
        :param job_timeout: Timeout of the job in seconds.
        :param cron_schedule:
        :return: :class:`JobDefinition <JobDefinition>`

        Usage:
        ::

            result = await api.update_job_definition(
                job_definition_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_job_definition_id = validate_path_param(
            "job_definition_id", job_definition_id
        )

        res = self._request(
            "PATCH",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-definitions/{param_job_definition_id}",
            body=marshal_UpdateJobDefinitionRequest(
                UpdateJobDefinitionRequest(
                    job_definition_id=job_definition_id,
                    region=region,
                    name=name,
                    cpu_limit=cpu_limit,
                    memory_limit=memory_limit,
                    local_storage_capacity=local_storage_capacity,
                    image_uri=image_uri,
                    command=command,
                    environment_variables=environment_variables,
                    description=description,
                    job_timeout=job_timeout,
                    cron_schedule=cron_schedule,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_JobDefinition(res.json())

    async def delete_job_definition(
        self,
        *,
        job_definition_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete an exsisting job definition by its unique identifier.
        :param job_definition_id: UUID of the job definition to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_job_definition(
                job_definition_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_job_definition_id = validate_path_param(
            "job_definition_id", job_definition_id
        )

        res = self._request(
            "DELETE",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-definitions/{param_job_definition_id}",
        )

        self._throw_on_error(res)

    async def start_job_definition(
        self,
        *,
        job_definition_id: str,
        region: Optional[ScwRegion] = None,
        command: Optional[str] = None,
        environment_variables: Optional[dict[str, str]] = None,
        replicas: Optional[int] = None,
    ) -> StartJobDefinitionResponse:
        """
        Run an existing job definition by its unique identifier. This will create a new job run.
        :param job_definition_id: UUID of the job definition to start.
        :param region: Region to target. If none is passed will use default region from the config.
        :param command: Contextual startup command for this specific job run.
        :param environment_variables: Contextual environment variables for this specific job run.
        :param replicas: Number of jobs to run.
        :return: :class:`StartJobDefinitionResponse <StartJobDefinitionResponse>`

        Usage:
        ::

            result = await api.start_job_definition(
                job_definition_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_job_definition_id = validate_path_param(
            "job_definition_id", job_definition_id
        )

        res = self._request(
            "POST",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-definitions/{param_job_definition_id}/start",
            body=marshal_StartJobDefinitionRequest(
                StartJobDefinitionRequest(
                    job_definition_id=job_definition_id,
                    region=region,
                    command=command,
                    environment_variables=environment_variables,
                    replicas=replicas,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_StartJobDefinitionResponse(res.json())

    async def create_job_definition_secrets(
        self,
        *,
        job_definition_id: str,
        secrets: list[CreateJobDefinitionSecretsRequestSecretConfig],
        region: Optional[ScwRegion] = None,
    ) -> CreateJobDefinitionSecretsResponse:
        """
        Create a secret reference within a job definition.
        :param job_definition_id: UUID of the job definition.
        :param secrets: List of secrets to inject into the job.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`CreateJobDefinitionSecretsResponse <CreateJobDefinitionSecretsResponse>`

        Usage:
        ::

            result = await api.create_job_definition_secrets(
                job_definition_id="example",
                secrets=[],
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_job_definition_id = validate_path_param(
            "job_definition_id", job_definition_id
        )

        res = self._request(
            "POST",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-definitions/{param_job_definition_id}/secrets",
            body=marshal_CreateJobDefinitionSecretsRequest(
                CreateJobDefinitionSecretsRequest(
                    job_definition_id=job_definition_id,
                    secrets=secrets,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateJobDefinitionSecretsResponse(res.json())

    async def get_job_definition_secret(
        self,
        *,
        job_definition_id: str,
        secret_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Secret:
        """
        Get a secret references within a job definition.
        :param job_definition_id: UUID of the job definition.
        :param secret_id: UUID of the secret reference within the job.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = await api.get_job_definition_secret(
                job_definition_id="example",
                secret_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_job_definition_id = validate_path_param(
            "job_definition_id", job_definition_id
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "GET",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-definitions/{param_job_definition_id}/secrets/{param_secret_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())

    async def list_job_definition_secrets(
        self,
        *,
        job_definition_id: str,
        region: Optional[ScwRegion] = None,
    ) -> ListJobDefinitionSecretsResponse:
        """
        List secrets references within a job definition.
        :param job_definition_id: UUID of the job definition.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ListJobDefinitionSecretsResponse <ListJobDefinitionSecretsResponse>`

        Usage:
        ::

            result = await api.list_job_definition_secrets(
                job_definition_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_job_definition_id = validate_path_param(
            "job_definition_id", job_definition_id
        )

        res = self._request(
            "GET",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-definitions/{param_job_definition_id}/secrets",
        )

        self._throw_on_error(res)
        return unmarshal_ListJobDefinitionSecretsResponse(res.json())

    async def update_job_definition_secret(
        self,
        *,
        job_definition_id: str,
        secret_id: str,
        region: Optional[ScwRegion] = None,
        secret_manager_version: Optional[str] = None,
        path: Optional[str] = None,
        env_var_name: Optional[str] = None,
    ) -> Secret:
        """
        Update a secret reference within a job definition.
        :param job_definition_id: UUID of the job definition.
        :param secret_id: UUID of the secret reference within the job.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_manager_version: Version of the secret in Secret Manager.
        :param path: Path of the secret to mount inside the job (either `path` or `env_var_name` must be set).
        One-Of ('secret_config'): at most one of 'path', 'env_var_name' could be set.
        :param env_var_name: Environment variable name used to expose the secret inside the job (either `path` or `env_var_name` must be set).
        One-Of ('secret_config'): at most one of 'path', 'env_var_name' could be set.
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = await api.update_job_definition_secret(
                job_definition_id="example",
                secret_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_job_definition_id = validate_path_param(
            "job_definition_id", job_definition_id
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "PATCH",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-definitions/{param_job_definition_id}/secrets/{param_secret_id}",
            body=marshal_UpdateJobDefinitionSecretRequest(
                UpdateJobDefinitionSecretRequest(
                    job_definition_id=job_definition_id,
                    secret_id=secret_id,
                    region=region,
                    secret_manager_version=secret_manager_version,
                    path=path,
                    env_var_name=env_var_name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())

    async def delete_job_definition_secret(
        self,
        *,
        job_definition_id: str,
        secret_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a secret reference within a job definition.
        :param job_definition_id: UUID of the job definition.
        :param secret_id: UUID of the secret reference within the job.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_job_definition_secret(
                job_definition_id="example",
                secret_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_job_definition_id = validate_path_param(
            "job_definition_id", job_definition_id
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "DELETE",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-definitions/{param_job_definition_id}/secrets/{param_secret_id}",
        )

        self._throw_on_error(res)

    async def get_job_run(
        self,
        *,
        job_run_id: str,
        region: Optional[ScwRegion] = None,
    ) -> JobRun:
        """
        Get a job run by its unique identifier.
        :param job_run_id: UUID of the job run to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`JobRun <JobRun>`

        Usage:
        ::

            result = await api.get_job_run(
                job_run_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_job_run_id = validate_path_param("job_run_id", job_run_id)

        res = self._request(
            "GET",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-runs/{param_job_run_id}",
        )

        self._throw_on_error(res)
        return unmarshal_JobRun(res.json())

    async def stop_job_run(
        self,
        *,
        job_run_id: str,
        region: Optional[ScwRegion] = None,
    ) -> JobRun:
        """
        Stop a job run by its unique identifier.
        :param job_run_id: UUID of the job run to stop.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`JobRun <JobRun>`

        Usage:
        ::

            result = await api.stop_job_run(
                job_run_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_job_run_id = validate_path_param("job_run_id", job_run_id)

        res = self._request(
            "POST",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-runs/{param_job_run_id}/stop",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_JobRun(res.json())

    async def list_job_runs(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListJobRunsRequestOrderBy] = None,
        job_definition_id: Optional[str] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        state: Optional[JobRunState] = None,
        states: Optional[list[JobRunState]] = None,
    ) -> ListJobRunsResponse:
        """
        List all job runs with filters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param job_definition_id:
        :param project_id:
        :param organization_id:
        :param state:
        :param states:
        :return: :class:`ListJobRunsResponse <ListJobRunsResponse>`

        Usage:
        ::

            result = await api.list_job_runs()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-runs",
            params={
                "job_definition_id": job_definition_id,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "state": state,
                "states": states,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListJobRunsResponse(res.json())

    async def list_job_runs_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListJobRunsRequestOrderBy] = None,
        job_definition_id: Optional[str] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        state: Optional[JobRunState] = None,
        states: Optional[list[JobRunState]] = None,
    ) -> list[JobRun]:
        """
        List all job runs with filters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param job_definition_id:
        :param project_id:
        :param organization_id:
        :param state:
        :param states:
        :return: :class:`list[JobRun] <list[JobRun]>`

        Usage:
        ::

            result = await api.list_job_runs_all()
        """

        return await fetch_all_pages_async(
            type=ListJobRunsResponse,
            key="job_runs",
            fetcher=self.list_job_runs,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "job_definition_id": job_definition_id,
                "project_id": project_id,
                "organization_id": organization_id,
                "state": state,
                "states": states,
            },
        )

    async def list_jobs_resources(
        self,
        *,
        region: Optional[ScwRegion] = None,
    ) -> ListJobsResourcesResponse:
        """
        List jobs resources for the console.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ListJobsResourcesResponse <ListJobsResourcesResponse>`

        Usage:
        ::

            result = await api.list_jobs_resources()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/jobs-resources",
        )

        self._throw_on_error(res)
        return unmarshal_ListJobsResourcesResponse(res.json())

    async def get_jobs_limits(
        self,
        *,
        region: Optional[ScwRegion] = None,
    ) -> JobsLimits:
        """
        Get jobs limits for the console.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`JobsLimits <JobsLimits>`

        Usage:
        ::

            result = await api.get_jobs_limits()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/jobs-limits",
        )

        self._throw_on_error(res)
        return unmarshal_JobsLimits(res.json())
