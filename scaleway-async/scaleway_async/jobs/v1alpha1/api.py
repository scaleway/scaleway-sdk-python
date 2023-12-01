# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Dict, List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
    ServiceInfo,
    unmarshal_ServiceInfo,
)
from scaleway_core.utils import (
    random_name,
    validate_path_param,
    fetch_all_pages_async,
)
from .types import (
    ListJobDefinitionsRequestOrderBy,
    ListJobRunsRequestOrderBy,
    CreateJobDefinitionRequest,
    JobDefinition,
    JobRun,
    ListJobDefinitionsResponse,
    ListJobRunsResponse,
    UpdateJobDefinitionRequest,
)
from .marshalling import (
    unmarshal_JobDefinition,
    unmarshal_JobRun,
    unmarshal_ListJobDefinitionsResponse,
    unmarshal_ListJobRunsResponse,
    marshal_CreateJobDefinitionRequest,
    marshal_UpdateJobDefinitionRequest,
)


class JobsV1Alpha1API(API):
    """
    Serverless Jobs API.
    """

    async def get_service_info(
        self,
        *,
        region: Optional[Region] = None,
    ) -> ServiceInfo:
        """
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ServiceInfo <ServiceInfo>`

        Usage:
        ::

            result = await api.get_service_info()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/serverless-jobs/v1alpha1/regions/{param_region}",
        )

        self._throw_on_error(res)
        return unmarshal_ServiceInfo(res.json())

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
        project_id: Optional[str] = None,
        environment_variables: Optional[Dict[str, str]] = None,
        job_timeout: Optional[str] = None,
    ) -> JobDefinition:
        """
        :param cpu_limit:
        :param memory_limit:
        :param image_uri:
        :param command:
        :param description:
        :param region: Region to target. If none is passed will use default region from the config.
        :param name:
        :param project_id:
        :param environment_variables:
        :param job_timeout:
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
                    project_id=project_id,
                    environment_variables=environment_variables,
                    job_timeout=job_timeout,
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
        :param job_definition_id:
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
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListJobDefinitionsRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> ListJobDefinitionsResponse:
        """
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
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param project_id:
        :return: :class:`List[JobDefinition] <List[JobDefinition]>`

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
        image_uri: Optional[str] = None,
        command: Optional[str] = None,
        environment_variables: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        job_timeout: Optional[str] = None,
    ) -> JobDefinition:
        """
        :param job_definition_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :param name:
        :param cpu_limit:
        :param memory_limit:
        :param image_uri:
        :param command:
        :param environment_variables:
        :param description:
        :param job_timeout:
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
                    image_uri=image_uri,
                    command=command,
                    environment_variables=environment_variables,
                    description=description,
                    job_timeout=job_timeout,
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
    ) -> None:
        """
        :param job_definition_id:
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
        region: Optional[Region] = None,
    ) -> JobRun:
        """
        :param job_definition_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`JobRun <JobRun>`

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
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_JobRun(res.json())

    async def get_job_run(
        self,
        *,
        job_run_id: str,
        region: Optional[Region] = None,
    ) -> JobRun:
        """
        :param job_run_id:
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
        region: Optional[Region] = None,
    ) -> JobRun:
        """
        :param job_run_id:
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
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListJobRunsRequestOrderBy] = None,
        job_definition_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListJobRunsResponse:
        """
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
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param job_definition_id:
        :param project_id:
        :return: :class:`List[JobRun] <List[JobRun]>`

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
