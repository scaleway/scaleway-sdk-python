# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Dict, List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    random_name,
    validate_path_param,
    fetch_all_pages,
)
from .types import (
    ListJobDefinitionsRequestOrderBy,
    ListJobRunsRequestOrderBy,
    CreateJobDefinitionRequest,
    CreateJobDefinitionRequestCronScheduleConfig,
    JobDefinition,
    JobRun,
    ListJobDefinitionsResponse,
    ListJobRunsResponse,
    ListJobsResourcesResponse,
    StartJobDefinitionRequest,
    StartJobDefinitionResponse,
    UpdateJobDefinitionRequest,
    UpdateJobDefinitionRequestCronScheduleConfig,
)
from .marshalling import (
    unmarshal_JobDefinition,
    unmarshal_JobRun,
    unmarshal_ListJobDefinitionsResponse,
    unmarshal_ListJobRunsResponse,
    unmarshal_ListJobsResourcesResponse,
    unmarshal_StartJobDefinitionResponse,
    marshal_CreateJobDefinitionRequest,
    marshal_StartJobDefinitionRequest,
    marshal_UpdateJobDefinitionRequest,
)


class JobsV1Alpha1API(API):
    """
    This API allows you to manage your Serverless Jobs.
    """

    def create_job_definition(
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

            result = api.create_job_definition(
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

    def get_job_definition(
        self,
        *,
        job_definition_id: str,
        region: Optional[Region] = None,
    ) -> JobDefinition:
        """
        Get a job definition by its unique identifier.
        :param job_definition_id: UUID of the job definition to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`JobDefinition <JobDefinition>`

        Usage:
        ::

            result = api.get_job_definition(
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

    def list_job_definitions(
        self,
        *,
        region: Optional[Region] = None,
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

            result = api.list_job_definitions()
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

    def list_job_definitions_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListJobDefinitionsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
    ) -> List[JobDefinition]:
        """
        List all your job definitions with filters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param project_id:
        :param organization_id:
        :return: :class:`List[JobDefinition] <List[JobDefinition]>`

        Usage:
        ::

            result = api.list_job_definitions_all()
        """

        return fetch_all_pages(
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

    def update_job_definition(
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

            result = api.update_job_definition(
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

    def delete_job_definition(
        self,
        *,
        job_definition_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete an exsisting job definition by its unique identifier.
        :param job_definition_id: UUID of the job definition to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_job_definition(
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

    def start_job_definition(
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
        :param job_definition_id: UUID of the job definition to start.
        :param region: Region to target. If none is passed will use default region from the config.
        :param command: Contextual startup command for this specific job run.
        :param environment_variables: Contextual environment variables for this specific job run.
        :param replicas: Number of jobs to run.
        :return: :class:`StartJobDefinitionResponse <StartJobDefinitionResponse>`

        Usage:
        ::

            result = api.start_job_definition(
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

    def get_job_run(
        self,
        *,
        job_run_id: str,
        region: Optional[Region] = None,
    ) -> JobRun:
        """
        Get a job run by its unique identifier.
        :param job_run_id: UUID of the job run to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`JobRun <JobRun>`

        Usage:
        ::

            result = api.get_job_run(
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

    def stop_job_run(
        self,
        *,
        job_run_id: str,
        region: Optional[Region] = None,
    ) -> JobRun:
        """
        Stop a job run by its unique identifier.
        :param job_run_id: UUID of the job run to stop.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`JobRun <JobRun>`

        Usage:
        ::

            result = api.stop_job_run(
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

    def list_job_runs(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListJobRunsRequestOrderBy] = None,
        job_definition_id: Optional[str] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
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
        :return: :class:`ListJobRunsResponse <ListJobRunsResponse>`

        Usage:
        ::

            result = api.list_job_runs()
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
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListJobRunsResponse(res.json())

    def list_job_runs_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListJobRunsRequestOrderBy] = None,
        job_definition_id: Optional[str] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
    ) -> List[JobRun]:
        """
        List all job runs with filters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param job_definition_id:
        :param project_id:
        :param organization_id:
        :return: :class:`List[JobRun] <List[JobRun]>`

        Usage:
        ::

            result = api.list_job_runs_all()
        """

        return fetch_all_pages(
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
            },
        )

    def list_jobs_resources(
        self,
        *,
        region: Optional[Region] = None,
    ) -> ListJobsResourcesResponse:
        """
        List jobs resources for the console.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ListJobsResourcesResponse <ListJobsResourcesResponse>`

        Usage:
        ::

            result = api.list_jobs_resources()
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
