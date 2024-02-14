# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Dict, List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    fetch_all_pages_async,
    random_name,
    validate_path_param,
)
from .types import (
    ListJobDefinitionsRequestOrderBy,
    ListJobRunsRequestOrderBy,
    CreateJobDefinitionRequestCronScheduleConfig,
    JobDefinition,
    JobRun,
    ListJobDefinitionsResponse,
    ListJobRunsResponse,
    StartJobDefinitionResponse,
    UpdateJobDefinitionRequestCronScheduleConfig,
    CreateJobDefinitionRequest,
    UpdateJobDefinitionRequest,
    StartJobDefinitionRequest,
)
from .marshalling import (
    marshal_CreateJobDefinitionRequest,
    marshal_StartJobDefinitionRequest,
    marshal_UpdateJobDefinitionRequest,
    unmarshal_JobDefinition,
    unmarshal_JobRun,
    unmarshal_ListJobDefinitionsResponse,
    unmarshal_ListJobRunsResponse,
    unmarshal_StartJobDefinitionResponse,
)


class JobsV1Alpha1API(API):
    """
    Serverless Jobs API.

    Serverless Jobs API.
    """

    async def create_job_definition(
        self,
        *,
        cpu_limit: int,
        memory_limit: int,
        image_uri: str,
        command: str,
        description: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        local_storage_capacity: Optional[int] = None,
        project_id: Optional[str] = None,
        environment_variables: Optional[Dict[str, str]] = None,
        job_timeout: Optional[str] = None,
        cron_schedule: Optional[CreateJobDefinitionRequestCronScheduleConfig] = None,
    ) -> JobDefinition:
        """
        Create a new job definition in a specified Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the job definition.
        :param cpu_limit: CPU limit of the job.
        :param memory_limit: Memory limit of the job (in MiB).
        :param local_storage_capacity: Local storage capacity of the job (in MiB).
        :param image_uri: Image to use for the job.
        :param command: Startup command.
        :param project_id: UUID of the Scaleway Project containing the job.
        :param environment_variables: Environment variables of the job.
        :param description: Description of the job.
        :param job_timeout: Timeout of the job in seconds.
        :param cron_schedule:
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
        region: Optional[Region] = None,
    ) -> JobDefinition:
        """
        Get a job definition by its unique identifier.
        :param region: Region to target. If none is passed will use default region from the config.
        :param job_definition_id: UUID of the job definition to get.
        :return: :class:`JobDefinition <JobDefinition>`

        Usage:
        ::

            result = await api.get_job_definition(job_definition_id="example")
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
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListJobDefinitionsRequestOrderBy = ListJobDefinitionsRequestOrderBy.CREATED_AT_ASC,
        project_id: Optional[str] = None,
    ) -> ListJobDefinitionsResponse:
        """
        List all your job definitions with filters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param project_id:
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
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListJobDefinitionsRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[JobDefinition]:
        """
        List all your job definitions with filters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param project_id:
        :return: :class:`List[ListJobDefinitionsResponse] <List[ListJobDefinitionsResponse]>`

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
            },
        )

    async def update_job_definition(
        self,
        *,
        job_definition_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        cpu_limit: Optional[int] = None,
        memory_limit: Optional[int] = None,
        local_storage_capacity: Optional[int] = None,
        image_uri: Optional[str] = None,
        command: Optional[str] = None,
        environment_variables: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        job_timeout: Optional[str] = None,
        cron_schedule: Optional[UpdateJobDefinitionRequestCronScheduleConfig] = None,
    ) -> JobDefinition:
        """
        Update an existing job definition associated with the specified unique identifier.
        :param region: Region to target. If none is passed will use default region from the config.
        :param job_definition_id: UUID of the job definition to update.
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

            result = await api.update_job_definition(job_definition_id="example")
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
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete an exsisting job definition by its unique identifier.
        :param region: Region to target. If none is passed will use default region from the config.
        :param job_definition_id: UUID of the job definition to delete.

        Usage:
        ::

            result = await api.delete_job_definition(job_definition_id="example")
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
        return None

    async def start_job_definition(
        self,
        *,
        job_definition_id: str,
        region: Optional[Region] = None,
        command: Optional[str] = None,
        environment_variables: Optional[Dict[str, str]] = None,
        replicas: Optional[int] = None,
    ) -> StartJobDefinitionResponse:
        """
        Run an existing job definition by its unique identifier. This will create a new job run.
        :param region: Region to target. If none is passed will use default region from the config.
        :param job_definition_id: UUID of the job definition to start.
        :param command: Contextual startup command for this specific job run.

        One-of ('_command'): at most one of 'command' could be set.
        :param environment_variables: Contextual environment variables for this specific job run.
        :param replicas: Number of jobs to run.

        One-of ('_replicas'): at most one of 'replicas' could be set.
        :return: :class:`StartJobDefinitionResponse <StartJobDefinitionResponse>`

        Usage:
        ::

            result = await api.start_job_definition(job_definition_id="example")
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

    async def get_job_run(
        self,
        *,
        job_run_id: str,
        region: Optional[Region] = None,
    ) -> JobRun:
        """
        Get a job run by its unique identifier.
        :param region: Region to target. If none is passed will use default region from the config.
        :param job_run_id: UUID of the job run to get.
        :return: :class:`JobRun <JobRun>`

        Usage:
        ::

            result = await api.get_job_run(job_run_id="example")
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
        region: Optional[Region] = None,
    ) -> JobRun:
        """
        Stop a job run by its unique identifier.
        :param region: Region to target. If none is passed will use default region from the config.
        :param job_run_id: UUID of the job run to stop.
        :return: :class:`JobRun <JobRun>`

        Usage:
        ::

            result = await api.stop_job_run(job_run_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_job_run_id = validate_path_param("job_run_id", job_run_id)

        res = self._request(
            "POST",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-runs/{param_job_run_id}/stop",
        )

        self._throw_on_error(res)
        return unmarshal_JobRun(res.json())

    async def list_job_runs(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListJobRunsRequestOrderBy = ListJobRunsRequestOrderBy.CREATED_AT_ASC,
        job_definition_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListJobRunsResponse:
        """
        List all job runs with filters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param job_definition_id:
        :param project_id:
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
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListJobRunsResponse(res.json())

    async def list_job_runs_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListJobRunsRequestOrderBy] = None,
        job_definition_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[JobRun]:
        """
        List all job runs with filters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param job_definition_id:
        :param project_id:
        :return: :class:`List[ListJobRunsResponse] <List[ListJobRunsResponse]>`

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
            },
        )
