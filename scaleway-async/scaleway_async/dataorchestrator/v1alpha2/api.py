# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Awaitable, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    OneOfPossibility,
    WaitForOptions,
    random_name,
    resolve_one_of,
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    ListWorkflowDefinitionsRequestOrderBy,
    ListWorkflowRunsRequestOrderBy,
    RunStatus,
    TriggerType,
    CreateWorkflowDefinitionRequest,
    CreateWorkflowDefinitionRequestCronScheduleConfig,
    CreateWorkflowDefinitionRequestWorkflowVersionConfig,
    ListWorkflowDefinitionsResponse,
    ListWorkflowRunsResponse,
    StartWorkflowDefinitionRequest,
    UpdateWorkflowDefinitionRequest,
    UpdateWorkflowDefinitionRequestCronScheduleConfig,
    UpdateWorkflowVersionRequest,
    WorkflowDefinition,
    WorkflowRun,
    WorkflowVersion,
)
from .content import (
    RUN_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_WorkflowVersion,
    unmarshal_WorkflowDefinition,
    unmarshal_WorkflowRun,
    unmarshal_ListWorkflowDefinitionsResponse,
    unmarshal_ListWorkflowRunsResponse,
    marshal_CreateWorkflowDefinitionRequest,
    marshal_StartWorkflowDefinitionRequest,
    marshal_UpdateWorkflowDefinitionRequest,
    marshal_UpdateWorkflowVersionRequest,
)


class DataorchestratorV1Alpha2API(API):
    """
    This API is a boilerplate for products.
    """

    async def create_workflow_definition(
        self,
        *,
        description: str,
        workflow_version: CreateWorkflowDefinitionRequestWorkflowVersionConfig,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        environment_variables: Optional[dict[str, str]] = None,
        workflow_timeout: Optional[str] = None,
        cron_schedule: Optional[
            CreateWorkflowDefinitionRequestCronScheduleConfig
        ] = None,
    ) -> WorkflowDefinition:
        """
        Create a new workflow definition in a specified Project.
        :param description: Description of the workflow.
        :param workflow_version: Version of the workflow definition.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the workflow definition.
        :param project_id: UUID of the Scaleway Project containing the workflow.
        :param environment_variables: Environment variables of the workflow.
        :param workflow_timeout: Timeout of the workflow in seconds.
        :param cron_schedule: Configure a cron for the workflow.
        :return: :class:`WorkflowDefinition <WorkflowDefinition>`

        Usage:
        ::

            result = await api.create_workflow_definition(
                description="example",
                workflow_version=CreateWorkflowDefinitionRequestWorkflowVersionConfig(),
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/data-orchestrator/v1alpha2/regions/{param_region}/workflow-definitions",
            body=marshal_CreateWorkflowDefinitionRequest(
                CreateWorkflowDefinitionRequest(
                    description=description,
                    workflow_version=workflow_version,
                    region=region,
                    name=name or random_name(prefix="workflow"),
                    project_id=project_id,
                    environment_variables=environment_variables,
                    workflow_timeout=workflow_timeout,
                    cron_schedule=cron_schedule,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_WorkflowDefinition(res.json())

    async def get_workflow_definition(
        self,
        *,
        workflow_definition_id: str,
        region: Optional[ScwRegion] = None,
    ) -> WorkflowDefinition:
        """
        Get a workflow definition by its unique identifier.
        :param workflow_definition_id: UUID of the workflow definition to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`WorkflowDefinition <WorkflowDefinition>`

        Usage:
        ::

            result = await api.get_workflow_definition(
                workflow_definition_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_workflow_definition_id = validate_path_param(
            "workflow_definition_id", workflow_definition_id
        )

        res = self._request(
            "GET",
            f"/data-orchestrator/v1alpha2/regions/{param_region}/workflow-definitions/{param_workflow_definition_id}",
        )

        self._throw_on_error(res)
        return unmarshal_WorkflowDefinition(res.json())

    async def list_workflow_definitions(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListWorkflowDefinitionsRequestOrderBy] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        statuses: Optional[list[RunStatus]] = None,
        created_after: Optional[datetime] = None,
        created_before: Optional[datetime] = None,
        trigger_types: Optional[list[TriggerType]] = None,
    ) -> ListWorkflowDefinitionsResponse:
        """
        List all your workflow definitions with filters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param name:
        :param project_id:
        One-Of ('scope'): at most one of 'project_id', 'organization_id' could be set.
        :param organization_id:
        One-Of ('scope'): at most one of 'project_id', 'organization_id' could be set.
        :param statuses:
        :param created_after:
        :param created_before:
        :param trigger_types:
        :return: :class:`ListWorkflowDefinitionsResponse <ListWorkflowDefinitionsResponse>`

        Usage:
        ::

            result = await api.list_workflow_definitions()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/data-orchestrator/v1alpha2/regions/{param_region}/workflow-definitions",
            params={
                "created_after": created_after,
                "created_before": created_before,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "statuses": statuses,
                "trigger_types": trigger_types,
                **resolve_one_of(
                    [
                        OneOfPossibility("organization_id", organization_id),
                        OneOfPossibility("project_id", project_id),
                    ]
                ),
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListWorkflowDefinitionsResponse(res.json())

    async def list_workflow_definitions_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListWorkflowDefinitionsRequestOrderBy] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        statuses: Optional[list[RunStatus]] = None,
        created_after: Optional[datetime] = None,
        created_before: Optional[datetime] = None,
        trigger_types: Optional[list[TriggerType]] = None,
    ) -> list[WorkflowDefinition]:
        """
        List all your workflow definitions with filters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param name:
        :param project_id:
        One-Of ('scope'): at most one of 'project_id', 'organization_id' could be set.
        :param organization_id:
        One-Of ('scope'): at most one of 'project_id', 'organization_id' could be set.
        :param statuses:
        :param created_after:
        :param created_before:
        :param trigger_types:
        :return: :class:`list[WorkflowDefinition] <list[WorkflowDefinition]>`

        Usage:
        ::

            result = await api.list_workflow_definitions_all()
        """

        return await fetch_all_pages_async(
            type=ListWorkflowDefinitionsResponse,
            key="workflow_definitions",
            fetcher=self.list_workflow_definitions,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "name": name,
                "statuses": statuses,
                "created_after": created_after,
                "created_before": created_before,
                "trigger_types": trigger_types,
                "project_id": project_id,
                "organization_id": organization_id,
            },
        )

    async def update_workflow_definition(
        self,
        *,
        workflow_definition_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        environment_variables: Optional[dict[str, str]] = None,
        workflow_timeout: Optional[str] = None,
        cron_schedule: Optional[
            UpdateWorkflowDefinitionRequestCronScheduleConfig
        ] = None,
    ) -> WorkflowDefinition:
        """
        Update an existing workflow definition by its unique identifier.
        :param workflow_definition_id: UUID of the workflow definition to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the workflow definition.
        :param description: Description of the workflow.
        :param environment_variables: Environment variables of the workflow.
        :param workflow_timeout: Timeout of the workflow in seconds.
        :param cron_schedule: Configure a cron for the workflow.
        :return: :class:`WorkflowDefinition <WorkflowDefinition>`

        Usage:
        ::

            result = await api.update_workflow_definition(
                workflow_definition_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_workflow_definition_id = validate_path_param(
            "workflow_definition_id", workflow_definition_id
        )

        res = self._request(
            "PATCH",
            f"/data-orchestrator/v1alpha2/regions/{param_region}/workflow-definitions/{param_workflow_definition_id}",
            body=marshal_UpdateWorkflowDefinitionRequest(
                UpdateWorkflowDefinitionRequest(
                    workflow_definition_id=workflow_definition_id,
                    region=region,
                    name=name,
                    description=description,
                    environment_variables=environment_variables,
                    workflow_timeout=workflow_timeout,
                    cron_schedule=cron_schedule,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_WorkflowDefinition(res.json())

    async def delete_workflow_definition(
        self,
        *,
        workflow_definition_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete an existing workflow definition by its unique identifier.
        :param workflow_definition_id: UUID of the workflow definition to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_workflow_definition(
                workflow_definition_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_workflow_definition_id = validate_path_param(
            "workflow_definition_id", workflow_definition_id
        )

        res = self._request(
            "DELETE",
            f"/data-orchestrator/v1alpha2/regions/{param_region}/workflow-definitions/{param_workflow_definition_id}",
        )

        self._throw_on_error(res)

    async def update_workflow_version(
        self,
        *,
        workflow_version_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        workflow_dsl: Optional[str] = None,
    ) -> WorkflowVersion:
        """
        Update an existing workflow version by its unique identifier.
        :param workflow_version_id: UUID of the workflow version to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the workflow version.
        :param description: Description of the workflow version.
        :param workflow_dsl: DSL of workflow in YAML format based from https://open-workflow-specification.org/schemas/1.0.3/workflow.yaml.
        :return: :class:`WorkflowVersion <WorkflowVersion>`

        Usage:
        ::

            result = await api.update_workflow_version(
                workflow_version_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_workflow_version_id = validate_path_param(
            "workflow_version_id", workflow_version_id
        )

        res = self._request(
            "PATCH",
            f"/data-orchestrator/v1alpha2/regions/{param_region}/workflow-versions/{param_workflow_version_id}",
            body=marshal_UpdateWorkflowVersionRequest(
                UpdateWorkflowVersionRequest(
                    workflow_version_id=workflow_version_id,
                    region=region,
                    name=name,
                    description=description,
                    workflow_dsl=workflow_dsl,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_WorkflowVersion(res.json())

    async def start_workflow_definition(
        self,
        *,
        workflow_definition_id: str,
        region: Optional[ScwRegion] = None,
        environment_variables: Optional[dict[str, str]] = None,
    ) -> WorkflowRun:
        """
        Run an existing workflow definition using its unique identifier and create a new workflow run.
        :param workflow_definition_id: UUID of the workflow definition to start.
        :param region: Region to target. If none is passed will use default region from the config.
        :param environment_variables: Contextual environment variables for this specific workflow run.
        :return: :class:`WorkflowRun <WorkflowRun>`

        Usage:
        ::

            result = await api.start_workflow_definition(
                workflow_definition_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_workflow_definition_id = validate_path_param(
            "workflow_definition_id", workflow_definition_id
        )

        res = self._request(
            "POST",
            f"/data-orchestrator/v1alpha2/regions/{param_region}/workflow-definitions/{param_workflow_definition_id}/start",
            body=marshal_StartWorkflowDefinitionRequest(
                StartWorkflowDefinitionRequest(
                    workflow_definition_id=workflow_definition_id,
                    region=region,
                    environment_variables=environment_variables,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_WorkflowRun(res.json())

    async def get_workflow_run(
        self,
        *,
        workflow_run_id: str,
        region: Optional[ScwRegion] = None,
    ) -> WorkflowRun:
        """
        Get a workflow run by its unique identifier.
        :param workflow_run_id: UUID of the workflow run to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`WorkflowRun <WorkflowRun>`

        Usage:
        ::

            result = await api.get_workflow_run(
                workflow_run_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_workflow_run_id = validate_path_param("workflow_run_id", workflow_run_id)

        res = self._request(
            "GET",
            f"/data-orchestrator/v1alpha2/regions/{param_region}/workflow-runs/{param_workflow_run_id}",
        )

        self._throw_on_error(res)
        return unmarshal_WorkflowRun(res.json())

    async def wait_for_workflow_run(
        self,
        *,
        workflow_run_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[
            WaitForOptions[WorkflowRun, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> WorkflowRun:
        """
        Get a workflow run by its unique identifier.
        :param workflow_run_id: UUID of the workflow run to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`WorkflowRun <WorkflowRun>`

        Usage:
        ::

            result = await api.get_workflow_run(
                workflow_run_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in RUN_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_workflow_run,
            options=options,
            args={
                "workflow_run_id": workflow_run_id,
                "region": region,
            },
        )

    async def list_workflow_runs(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListWorkflowRunsRequestOrderBy] = None,
        workflow_definition_id: Optional[str] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        statuses: Optional[list[RunStatus]] = None,
        created_after: Optional[datetime] = None,
        created_before: Optional[datetime] = None,
        trigger_types: Optional[list[TriggerType]] = None,
        workflow_definition_name: Optional[str] = None,
    ) -> ListWorkflowRunsResponse:
        """
        List all your workflow runs with filters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param workflow_definition_id:
        :param project_id:
        One-Of ('scope'): at most one of 'project_id', 'organization_id' could be set.
        :param organization_id:
        One-Of ('scope'): at most one of 'project_id', 'organization_id' could be set.
        :param statuses:
        :param created_after:
        :param created_before:
        :param trigger_types:
        :param workflow_definition_name:
        :return: :class:`ListWorkflowRunsResponse <ListWorkflowRunsResponse>`

        Usage:
        ::

            result = await api.list_workflow_runs()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/data-orchestrator/v1alpha2/regions/{param_region}/workflow-runs",
            params={
                "created_after": created_after,
                "created_before": created_before,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "statuses": statuses,
                "trigger_types": trigger_types,
                "workflow_definition_id": workflow_definition_id,
                "workflow_definition_name": workflow_definition_name,
                **resolve_one_of(
                    [
                        OneOfPossibility("organization_id", organization_id),
                        OneOfPossibility("project_id", project_id),
                    ]
                ),
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListWorkflowRunsResponse(res.json())

    async def list_workflow_runs_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListWorkflowRunsRequestOrderBy] = None,
        workflow_definition_id: Optional[str] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        statuses: Optional[list[RunStatus]] = None,
        created_after: Optional[datetime] = None,
        created_before: Optional[datetime] = None,
        trigger_types: Optional[list[TriggerType]] = None,
        workflow_definition_name: Optional[str] = None,
    ) -> list[WorkflowRun]:
        """
        List all your workflow runs with filters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param order_by:
        :param workflow_definition_id:
        :param project_id:
        One-Of ('scope'): at most one of 'project_id', 'organization_id' could be set.
        :param organization_id:
        One-Of ('scope'): at most one of 'project_id', 'organization_id' could be set.
        :param statuses:
        :param created_after:
        :param created_before:
        :param trigger_types:
        :param workflow_definition_name:
        :return: :class:`list[WorkflowRun] <list[WorkflowRun]>`

        Usage:
        ::

            result = await api.list_workflow_runs_all()
        """

        return await fetch_all_pages_async(
            type=ListWorkflowRunsResponse,
            key="workflow_runs",
            fetcher=self.list_workflow_runs,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "workflow_definition_id": workflow_definition_id,
                "statuses": statuses,
                "created_after": created_after,
                "created_before": created_before,
                "trigger_types": trigger_types,
                "workflow_definition_name": workflow_definition_name,
                "project_id": project_id,
                "organization_id": organization_id,
            },
        )

    async def terminate_workflow_run(
        self,
        *,
        workflow_run_id: str,
        region: Optional[ScwRegion] = None,
    ) -> WorkflowRun:
        """
        Terminate a workflow run using its unique identifier.
        :param workflow_run_id: UUID of the workflow run to terminate.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`WorkflowRun <WorkflowRun>`

        Usage:
        ::

            result = await api.terminate_workflow_run(
                workflow_run_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_workflow_run_id = validate_path_param("workflow_run_id", workflow_run_id)

        res = self._request(
            "POST",
            f"/data-orchestrator/v1alpha2/regions/{param_region}/workflow-runs/{param_workflow_run_id}/terminate",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_WorkflowRun(res.json())

    async def pause_workflow_run(
        self,
        *,
        workflow_run_id: str,
        region: Optional[ScwRegion] = None,
    ) -> WorkflowRun:
        """
        Pause a workflow run using its unique identifier.
        :param workflow_run_id: UUID of the workflow run to pause.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`WorkflowRun <WorkflowRun>`

        Usage:
        ::

            result = await api.pause_workflow_run(
                workflow_run_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_workflow_run_id = validate_path_param("workflow_run_id", workflow_run_id)

        res = self._request(
            "POST",
            f"/data-orchestrator/v1alpha2/regions/{param_region}/workflow-runs/{param_workflow_run_id}/pause",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_WorkflowRun(res.json())

    async def resume_workflow_run(
        self,
        *,
        workflow_run_id: str,
        region: Optional[ScwRegion] = None,
    ) -> WorkflowRun:
        """
        Resume a workflow run using its unique identifier.
        :param workflow_run_id: UUID of the workflow run to resume.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`WorkflowRun <WorkflowRun>`

        Usage:
        ::

            result = await api.resume_workflow_run(
                workflow_run_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_workflow_run_id = validate_path_param("workflow_run_id", workflow_run_id)

        res = self._request(
            "POST",
            f"/data-orchestrator/v1alpha2/regions/{param_region}/workflow-runs/{param_workflow_run_id}/resume",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_WorkflowRun(res.json())

    async def delete_workflow_run(
        self,
        *,
        workflow_run_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete an existing workflow run by its unique identifier.
        :param workflow_run_id: UUID of the workflow run to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_workflow_run(
                workflow_run_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_workflow_run_id = validate_path_param("workflow_run_id", workflow_run_id)

        res = self._request(
            "DELETE",
            f"/data-orchestrator/v1alpha2/regions/{param_region}/workflow-runs/{param_workflow_run_id}",
        )

        self._throw_on_error(res)
