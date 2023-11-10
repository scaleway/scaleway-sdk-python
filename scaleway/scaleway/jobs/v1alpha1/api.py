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
    fetch_all_pages,
    random_name,
    validate_path_param,
)
from .types import (
    ListJobDefinitionsRequestOrderBy,
    ListJobRunsRequestOrderBy,
    JobDefinition,
    JobRun,
    ListJobDefinitionsResponse,
    ListJobRunsResponse,
    CreateJobDefinitionRequest,
    UpdateJobDefinitionRequest,
)
from .marshalling import (
    marshal_CreateJobDefinitionRequest,
    marshal_UpdateJobDefinitionRequest,
    unmarshal_JobDefinition,
    unmarshal_JobRun,
    unmarshal_ListJobDefinitionsResponse,
    unmarshal_ListJobRunsResponse,
)


class JobsV1Alpha1API(API):
    """
    Serverless Jobs API.

    Serverless Jobs API.
    """

    def get_service_info(
        self,
        *,
        region: Optional[Region] = None,
    ) -> Optional[ServiceInfo]:
        """

        Usage:
        ::

            result = api.get_service_info()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/serverless-jobs/v1alpha1/regions/{param_region}",
        )

        self._throw_on_error(res)
        json = res.json()
        return unmarshal_ServiceInfo(json) if json is not None else None

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
        project_id: Optional[str] = None,
        environment_variables: Optional[Dict[str, str]] = None,
        job_timeout: Optional[str] = None,
    ) -> JobDefinition:
        """

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
                    project_id=project_id,
                    environment_variables=environment_variables,
                    job_timeout=job_timeout,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_JobDefinition(res.json())

    def get_job_definition(
        self,
        *,
        id: str,
        region: Optional[Region] = None,
    ) -> JobDefinition:
        """

        Usage:
        ::

            result = api.get_job_definition(id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_id = validate_path_param("id", id)

        res = self._request(
            "GET",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-definitions/{param_id}",
        )

        self._throw_on_error(res)
        return unmarshal_JobDefinition(res.json())

    def list_job_definitions(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListJobDefinitionsRequestOrderBy = ListJobDefinitionsRequestOrderBy.CREATED_AT_ASC,
        project_id: Optional[str] = None,
    ) -> ListJobDefinitionsResponse:
        """

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
    ) -> List[JobDefinition]:
        """
        :return: :class:`List[ListJobDefinitionsResponse] <List[ListJobDefinitionsResponse]>`

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
            },
        )

    def update_job_definition(
        self,
        *,
        id: str,
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

        Usage:
        ::

            result = api.update_job_definition(id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_id = validate_path_param("id", id)

        res = self._request(
            "PATCH",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-definitions/{param_id}",
            body=marshal_UpdateJobDefinitionRequest(
                UpdateJobDefinitionRequest(
                    id=id,
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

    def delete_job_definition(
        self,
        *,
        id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """

        Usage:
        ::

            result = api.delete_job_definition(id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_id = validate_path_param("id", id)

        res = self._request(
            "DELETE",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-definitions/{param_id}",
        )

        self._throw_on_error(res)
        return None

    def start_job_definition(
        self,
        *,
        id: str,
        region: Optional[Region] = None,
    ) -> JobRun:
        """

        Usage:
        ::

            result = api.start_job_definition(id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_id = validate_path_param("id", id)

        res = self._request(
            "POST",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-definitions/{param_id}/start",
        )

        self._throw_on_error(res)
        return unmarshal_JobRun(res.json())

    def get_job_run(
        self,
        *,
        id: str,
        region: Optional[Region] = None,
    ) -> JobRun:
        """

        Usage:
        ::

            result = api.get_job_run(id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_id = validate_path_param("id", id)

        res = self._request(
            "GET",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-runs/{param_id}",
        )

        self._throw_on_error(res)
        return unmarshal_JobRun(res.json())

    def stop_job_run(
        self,
        *,
        id: str,
        region: Optional[Region] = None,
    ) -> JobRun:
        """

        Usage:
        ::

            result = api.stop_job_run(id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_id = validate_path_param("id", id)

        res = self._request(
            "POST",
            f"/serverless-jobs/v1alpha1/regions/{param_region}/job-runs/{param_id}/stop",
        )

        self._throw_on_error(res)
        return unmarshal_JobRun(res.json())

    def list_job_runs(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListJobRunsRequestOrderBy = ListJobRunsRequestOrderBy.CREATED_AT_ASC,
        id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListJobRunsResponse:
        """

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
                "id": id,
                "order_by": order_by,
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
        id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[JobRun]:
        """
        :return: :class:`List[ListJobRunsResponse] <List[ListJobRunsResponse]>`

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
                "id": id,
                "project_id": project_id,
            },
        )