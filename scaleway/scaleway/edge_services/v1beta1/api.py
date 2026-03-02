# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

from scaleway_core.api import API
from scaleway_core.utils import (
    WaitForOptions,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
)
from .types import (
    ListBackendStagesRequestOrderBy,
    ListCacheStagesRequestOrderBy,
    ListDNSStagesRequestOrderBy,
    ListPipelinesRequestOrderBy,
    ListPipelinesWithStagesRequestOrderBy,
    ListPurgeRequestsRequestOrderBy,
    ListRouteStagesRequestOrderBy,
    ListTLSStagesRequestOrderBy,
    ListWafStagesRequestOrderBy,
    PlanName,
    SearchBackendStagesRequestOrderBy,
    SearchRouteRulesRequestOrderBy,
    SearchWafStagesRequestOrderBy,
    WafStageMode,
    AddRouteRulesRequest,
    AddRouteRulesResponse,
    BackendStage,
    CacheStage,
    CheckDomainRequest,
    CheckDomainResponse,
    CheckLbOriginRequest,
    CheckLbOriginResponse,
    CheckPEMChainRequest,
    CheckPEMChainRequestSecretChain,
    CheckPEMChainResponse,
    CreateBackendStageRequest,
    CreateCacheStageRequest,
    CreateDNSStageRequest,
    CreatePipelineRequest,
    CreatePurgeRequestRequest,
    CreateRouteStageRequest,
    CreateTLSStageRequest,
    CreateWafStageRequest,
    DNSStage,
    GetBillingResponse,
    HeadStageResponse,
    ListBackendStagesResponse,
    ListCacheStagesResponse,
    ListDNSStagesResponse,
    ListHeadStagesResponse,
    ListHeadStagesResponseHeadStage,
    ListPipelinesResponse,
    ListPipelinesWithStagesResponse,
    ListPlansResponse,
    ListPurgeRequestsResponse,
    ListRouteRulesResponse,
    ListRouteStagesResponse,
    ListTLSStagesResponse,
    ListWafStagesResponse,
    Pipeline,
    PipelineStages,
    Plan,
    PurgeRequest,
    RouteStage,
    ScalewayLb,
    ScalewayLbBackendConfig,
    ScalewayS3BackendConfig,
    ScalewayServerlessContainerBackendConfig,
    ScalewayServerlessFunctionBackendConfig,
    SelectPlanRequest,
    SetHeadStageRequest,
    SetHeadStageRequestAddNewHeadStage,
    SetHeadStageRequestRemoveHeadStage,
    SetHeadStageRequestSwapHeadStage,
    SetRouteRulesRequest,
    SetRouteRulesRequestRouteRule,
    SetRouteRulesResponse,
    TLSSecret,
    TLSSecretsConfig,
    TLSStage,
    UpdateBackendStageRequest,
    UpdateCacheStageRequest,
    UpdateDNSStageRequest,
    UpdatePipelineRequest,
    UpdateRouteStageRequest,
    UpdateTLSStageRequest,
    UpdateWafStageRequest,
    WafStage,
)
from .content import (
    PIPELINE_TRANSIENT_STATUSES,
    PURGE_REQUEST_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_BackendStage,
    unmarshal_CacheStage,
    unmarshal_DNSStage,
    unmarshal_Pipeline,
    unmarshal_RouteStage,
    unmarshal_TLSStage,
    unmarshal_WafStage,
    unmarshal_PurgeRequest,
    unmarshal_AddRouteRulesResponse,
    unmarshal_CheckDomainResponse,
    unmarshal_CheckLbOriginResponse,
    unmarshal_CheckPEMChainResponse,
    unmarshal_GetBillingResponse,
    unmarshal_HeadStageResponse,
    unmarshal_ListBackendStagesResponse,
    unmarshal_ListCacheStagesResponse,
    unmarshal_ListDNSStagesResponse,
    unmarshal_ListHeadStagesResponse,
    unmarshal_ListPipelinesResponse,
    unmarshal_ListPipelinesWithStagesResponse,
    unmarshal_ListPlansResponse,
    unmarshal_ListPurgeRequestsResponse,
    unmarshal_ListRouteRulesResponse,
    unmarshal_ListRouteStagesResponse,
    unmarshal_ListTLSStagesResponse,
    unmarshal_ListWafStagesResponse,
    unmarshal_Plan,
    unmarshal_SetRouteRulesResponse,
    marshal_AddRouteRulesRequest,
    marshal_CheckDomainRequest,
    marshal_CheckLbOriginRequest,
    marshal_CheckPEMChainRequest,
    marshal_CreateBackendStageRequest,
    marshal_CreateCacheStageRequest,
    marshal_CreateDNSStageRequest,
    marshal_CreatePipelineRequest,
    marshal_CreatePurgeRequestRequest,
    marshal_CreateRouteStageRequest,
    marshal_CreateTLSStageRequest,
    marshal_CreateWafStageRequest,
    marshal_SelectPlanRequest,
    marshal_SetHeadStageRequest,
    marshal_SetRouteRulesRequest,
    marshal_UpdateBackendStageRequest,
    marshal_UpdateCacheStageRequest,
    marshal_UpdateDNSStageRequest,
    marshal_UpdatePipelineRequest,
    marshal_UpdateRouteStageRequest,
    marshal_UpdateTLSStageRequest,
    marshal_UpdateWafStageRequest,
)


class EdgeServicesV1Beta1API(API):
    """ """

    def list_pipelines(
        self,
        *,
        order_by: Optional[ListPipelinesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        has_backend_stage_lb: Optional[bool] = None,
    ) -> ListPipelinesResponse:
        """
        List pipelines.
        List all pipelines, for a Scaleway Organization or Scaleway Project. By default, the pipelines returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of pipelines in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of pipelines to return per page.
        :param name: Pipeline name to filter for. Only pipelines with this string within their name will be returned.
        :param organization_id: Organization ID to filter for. Only pipelines from this Organization will be returned.
        :param project_id: Project ID to filter for. Only pipelines from this Project will be returned.
        :param has_backend_stage_lb: Filter on backend stage. Only pipelines with a Load Balancer origin will be returned.
        :return: :class:`ListPipelinesResponse <ListPipelinesResponse>`

        Usage:
        ::

            result = api.list_pipelines()
        """

        res = self._request(
            "GET",
            "/edge-services/v1beta1/pipelines",
            params={
                "has_backend_stage_lb": has_backend_stage_lb,
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPipelinesResponse(res.json())

    def list_pipelines_all(
        self,
        *,
        order_by: Optional[ListPipelinesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        has_backend_stage_lb: Optional[bool] = None,
    ) -> list[Pipeline]:
        """
        List pipelines.
        List all pipelines, for a Scaleway Organization or Scaleway Project. By default, the pipelines returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of pipelines in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of pipelines to return per page.
        :param name: Pipeline name to filter for. Only pipelines with this string within their name will be returned.
        :param organization_id: Organization ID to filter for. Only pipelines from this Organization will be returned.
        :param project_id: Project ID to filter for. Only pipelines from this Project will be returned.
        :param has_backend_stage_lb: Filter on backend stage. Only pipelines with a Load Balancer origin will be returned.
        :return: :class:`list[Pipeline] <list[Pipeline]>`

        Usage:
        ::

            result = api.list_pipelines_all()
        """

        return fetch_all_pages(
            type=ListPipelinesResponse,
            key="pipelines",
            fetcher=self.list_pipelines,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
                "organization_id": organization_id,
                "project_id": project_id,
                "has_backend_stage_lb": has_backend_stage_lb,
            },
        )

    def create_pipeline(
        self,
        *,
        name: str,
        description: str,
        project_id: Optional[str] = None,
    ) -> Pipeline:
        """
        Create pipeline.
        Create a new pipeline. You must specify a `dns_stage_id` to form a stage-chain that goes all the way to the backend stage (origin), so the HTTP request will be processed according to the stages you created.
        :param name: Name of the pipeline.
        :param description: Description of the pipeline.
        :param project_id: Project ID in which the pipeline will be created.
        :return: :class:`Pipeline <Pipeline>`

        Usage:
        ::

            result = api.create_pipeline(
                name="example",
                description="example",
            )
        """

        res = self._request(
            "POST",
            "/edge-services/v1beta1/pipelines",
            body=marshal_CreatePipelineRequest(
                CreatePipelineRequest(
                    name=name,
                    description=description,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Pipeline(res.json())

    def get_pipeline(
        self,
        *,
        pipeline_id: str,
    ) -> Pipeline:
        """
        Get pipeline.
        Retrieve information about an existing pipeline, specified by its `pipeline_id`. Its full details, including errors, are returned in the response object.
        :param pipeline_id: ID of the requested pipeline.
        :return: :class:`Pipeline <Pipeline>`

        Usage:
        ::

            result = api.get_pipeline(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "GET",
            f"/edge-services/v1beta1/pipelines/{param_pipeline_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Pipeline(res.json())

    def wait_for_pipeline(
        self,
        *,
        pipeline_id: str,
        options: Optional[WaitForOptions[Pipeline, bool]] = None,
    ) -> Pipeline:
        """
        Get pipeline.
        Retrieve information about an existing pipeline, specified by its `pipeline_id`. Its full details, including errors, are returned in the response object.
        :param pipeline_id: ID of the requested pipeline.
        :return: :class:`Pipeline <Pipeline>`

        Usage:
        ::

            result = api.get_pipeline(
                pipeline_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in PIPELINE_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_pipeline,
            options=options,
            args={
                "pipeline_id": pipeline_id,
            },
        )

    def list_pipelines_with_stages(
        self,
        *,
        order_by: Optional[ListPipelinesWithStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListPipelinesWithStagesResponse:
        """
        :param order_by:
        :param page:
        :param page_size:
        :param name:
        :param organization_id:
        :param project_id:
        :return: :class:`ListPipelinesWithStagesResponse <ListPipelinesWithStagesResponse>`

        Usage:
        ::

            result = api.list_pipelines_with_stages()
        """

        res = self._request(
            "GET",
            "/edge-services/v1beta1/pipelines-stages",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPipelinesWithStagesResponse(res.json())

    def list_pipelines_with_stages_all(
        self,
        *,
        order_by: Optional[ListPipelinesWithStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> list[PipelineStages]:
        """
        :param order_by:
        :param page:
        :param page_size:
        :param name:
        :param organization_id:
        :param project_id:
        :return: :class:`list[PipelineStages] <list[PipelineStages]>`

        Usage:
        ::

            result = api.list_pipelines_with_stages_all()
        """

        return fetch_all_pages(
            type=ListPipelinesWithStagesResponse,
            key="pipelines",
            fetcher=self.list_pipelines_with_stages,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    def update_pipeline(
        self,
        *,
        pipeline_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Pipeline:
        """
        Update pipeline.
        Update the parameters of an existing pipeline, specified by its `pipeline_id`. Parameters which can be updated include the `name`, `description` and `dns_stage_id`.
        :param pipeline_id: ID of the pipeline to update.
        :param name: Name of the pipeline.
        :param description: Description of the pipeline.
        :return: :class:`Pipeline <Pipeline>`

        Usage:
        ::

            result = api.update_pipeline(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "PATCH",
            f"/edge-services/v1beta1/pipelines/{param_pipeline_id}",
            body=marshal_UpdatePipelineRequest(
                UpdatePipelineRequest(
                    pipeline_id=pipeline_id,
                    name=name,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Pipeline(res.json())

    def delete_pipeline(
        self,
        *,
        pipeline_id: str,
    ) -> None:
        """
        Delete pipeline.
        Delete an existing pipeline, specified by its `pipeline_id`. Deleting a pipeline is permanent, and cannot be undone. Note that all stages linked to the pipeline are also deleted.
        :param pipeline_id: ID of the pipeline to delete.

        Usage:
        ::

            result = api.delete_pipeline(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "DELETE",
            f"/edge-services/v1beta1/pipelines/{param_pipeline_id}",
        )

        self._throw_on_error(res)

    def list_head_stages(
        self,
        *,
        pipeline_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListHeadStagesResponse:
        """
        List Head stage for your pipeline.
        :param pipeline_id: ID of the pipeline to update.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of head stages to return per page.
        :return: :class:`ListHeadStagesResponse <ListHeadStagesResponse>`

        Usage:
        ::

            result = api.list_head_stages(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "GET",
            f"/edge-services/v1beta1/pipelines/{param_pipeline_id}/head-stages",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListHeadStagesResponse(res.json())

    def list_head_stages_all(
        self,
        *,
        pipeline_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[ListHeadStagesResponseHeadStage]:
        """
        List Head stage for your pipeline.
        :param pipeline_id: ID of the pipeline to update.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of head stages to return per page.
        :return: :class:`list[ListHeadStagesResponseHeadStage] <list[ListHeadStagesResponseHeadStage]>`

        Usage:
        ::

            result = api.list_head_stages_all(
                pipeline_id="example",
            )
        """

        return fetch_all_pages(
            type=ListHeadStagesResponse,
            key="head_stages",
            fetcher=self.list_head_stages,
            args={
                "pipeline_id": pipeline_id,
                "page": page,
                "page_size": page_size,
            },
        )

    def set_head_stage(
        self,
        *,
        pipeline_id: str,
        add_new_head_stage: Optional[SetHeadStageRequestAddNewHeadStage] = None,
        remove_head_stage: Optional[SetHeadStageRequestRemoveHeadStage] = None,
        swap_head_stage: Optional[SetHeadStageRequestSwapHeadStage] = None,
    ) -> HeadStageResponse:
        """
        Configure a entry point to your pipeline. You must specify a `head stage` to form a stage-chain that goes all the way to the backend stage (origin), so the HTTP request will be processed according to the stages you created.
        You must specify either a `add_new_head_stage` (to add a new head stage), `remove_head_stage` (to remove a head stage) or `swap_head_stage` (to replace a head stage).
        :param pipeline_id: ID of the pipeline to update.
        :param add_new_head_stage: Add a new head stage.
        One-Of ('action'): at most one of 'add_new_head_stage', 'remove_head_stage', 'swap_head_stage' could be set.
        :param remove_head_stage: Remove a head stage.
        One-Of ('action'): at most one of 'add_new_head_stage', 'remove_head_stage', 'swap_head_stage' could be set.
        :param swap_head_stage: Replace a head stage with a new one.
        One-Of ('action'): at most one of 'add_new_head_stage', 'remove_head_stage', 'swap_head_stage' could be set.
        :return: :class:`HeadStageResponse <HeadStageResponse>`

        Usage:
        ::

            result = api.set_head_stage(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "POST",
            f"/edge-services/v1beta1/pipelines/{param_pipeline_id}/set-head-stage",
            body=marshal_SetHeadStageRequest(
                SetHeadStageRequest(
                    pipeline_id=pipeline_id,
                    add_new_head_stage=add_new_head_stage,
                    remove_head_stage=remove_head_stage,
                    swap_head_stage=swap_head_stage,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_HeadStageResponse(res.json())

    def list_dns_stages(
        self,
        *,
        order_by: Optional[ListDNSStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: str,
        fqdn: Optional[str] = None,
    ) -> ListDNSStagesResponse:
        """
        List DNS stages.
        List all DNS stages, for a Scaleway Organization or Scaleway Project. By default, the DNS stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of DNS stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of DNS stages to return per page.
        :param pipeline_id: Pipeline ID to filter for. Only DNS stages from this pipeline will be returned.
        :param fqdn: Fully Qualified Domain Name to filter for (in the format subdomain.example.com). Only DNS stages with this FQDN will be returned.
        :return: :class:`ListDNSStagesResponse <ListDNSStagesResponse>`

        Usage:
        ::

            result = api.list_dns_stages(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "GET",
            f"/edge-services/v1beta1/pipelines/{param_pipeline_id}/dns-stages",
            params={
                "fqdn": fqdn,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDNSStagesResponse(res.json())

    def list_dns_stages_all(
        self,
        *,
        order_by: Optional[ListDNSStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: str,
        fqdn: Optional[str] = None,
    ) -> list[DNSStage]:
        """
        List DNS stages.
        List all DNS stages, for a Scaleway Organization or Scaleway Project. By default, the DNS stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of DNS stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of DNS stages to return per page.
        :param pipeline_id: Pipeline ID to filter for. Only DNS stages from this pipeline will be returned.
        :param fqdn: Fully Qualified Domain Name to filter for (in the format subdomain.example.com). Only DNS stages with this FQDN will be returned.
        :return: :class:`list[DNSStage] <list[DNSStage]>`

        Usage:
        ::

            result = api.list_dns_stages_all(
                pipeline_id="example",
            )
        """

        return fetch_all_pages(
            type=ListDNSStagesResponse,
            key="stages",
            fetcher=self.list_dns_stages,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "pipeline_id": pipeline_id,
                "fqdn": fqdn,
            },
        )

    def create_dns_stage(
        self,
        *,
        fqdns: Optional[list[str]] = None,
        tls_stage_id: Optional[str] = None,
        cache_stage_id: Optional[str] = None,
        backend_stage_id: Optional[str] = None,
        pipeline_id: str,
    ) -> DNSStage:
        """
        Create DNS stage.
        Create a new DNS stage. You must specify the `fqdns` field to customize the domain endpoint, using a domain you already own.
        :param fqdns: Fully Qualified Domain Name (in the format subdomain.example.com) to attach to the stage.
        :param tls_stage_id: TLS stage ID the DNS stage will be linked to.
        One-Of ('next'): at most one of 'tls_stage_id', 'cache_stage_id', 'backend_stage_id' could be set.
        :param cache_stage_id: Cache stage ID the DNS stage will be linked to.
        One-Of ('next'): at most one of 'tls_stage_id', 'cache_stage_id', 'backend_stage_id' could be set.
        :param backend_stage_id: Backend stage ID the DNS stage will be linked to.
        One-Of ('next'): at most one of 'tls_stage_id', 'cache_stage_id', 'backend_stage_id' could be set.
        :param pipeline_id: Pipeline ID the DNS stage belongs to.
        :return: :class:`DNSStage <DNSStage>`

        Usage:
        ::

            result = api.create_dns_stage(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "POST",
            f"/edge-services/v1beta1/pipelines/{param_pipeline_id}/dns-stages",
            body=marshal_CreateDNSStageRequest(
                CreateDNSStageRequest(
                    fqdns=fqdns,
                    pipeline_id=pipeline_id,
                    tls_stage_id=tls_stage_id,
                    cache_stage_id=cache_stage_id,
                    backend_stage_id=backend_stage_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DNSStage(res.json())

    def get_dns_stage(
        self,
        *,
        dns_stage_id: str,
    ) -> DNSStage:
        """
        Get DNS stage.
        Retrieve information about an existing DNS stage, specified by its `dns_stage_id`. Its full details, including FQDNs, are returned in the response object.
        :param dns_stage_id: ID of the requested DNS stage.
        :return: :class:`DNSStage <DNSStage>`

        Usage:
        ::

            result = api.get_dns_stage(
                dns_stage_id="example",
            )
        """

        param_dns_stage_id = validate_path_param("dns_stage_id", dns_stage_id)

        res = self._request(
            "GET",
            f"/edge-services/v1beta1/dns-stages/{param_dns_stage_id}",
        )

        self._throw_on_error(res)
        return unmarshal_DNSStage(res.json())

    def update_dns_stage(
        self,
        *,
        dns_stage_id: str,
        fqdns: Optional[list[str]] = None,
        tls_stage_id: Optional[str] = None,
        cache_stage_id: Optional[str] = None,
        backend_stage_id: Optional[str] = None,
    ) -> DNSStage:
        """
        Update DNS stage.
        Update the parameters of an existing DNS stage, specified by its `dns_stage_id`.
        :param dns_stage_id: ID of the DNS stage to update.
        :param fqdns: Fully Qualified Domain Name (in the format subdomain.example.com) attached to the stage.
        :param tls_stage_id: TLS stage ID the DNS stage will be linked to.
        One-Of ('next'): at most one of 'tls_stage_id', 'cache_stage_id', 'backend_stage_id' could be set.
        :param cache_stage_id: Cache stage ID the DNS stage will be linked to.
        One-Of ('next'): at most one of 'tls_stage_id', 'cache_stage_id', 'backend_stage_id' could be set.
        :param backend_stage_id: Backend stage ID the DNS stage will be linked to.
        One-Of ('next'): at most one of 'tls_stage_id', 'cache_stage_id', 'backend_stage_id' could be set.
        :return: :class:`DNSStage <DNSStage>`

        Usage:
        ::

            result = api.update_dns_stage(
                dns_stage_id="example",
            )
        """

        param_dns_stage_id = validate_path_param("dns_stage_id", dns_stage_id)

        res = self._request(
            "PATCH",
            f"/edge-services/v1beta1/dns-stages/{param_dns_stage_id}",
            body=marshal_UpdateDNSStageRequest(
                UpdateDNSStageRequest(
                    dns_stage_id=dns_stage_id,
                    fqdns=fqdns,
                    tls_stage_id=tls_stage_id,
                    cache_stage_id=cache_stage_id,
                    backend_stage_id=backend_stage_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DNSStage(res.json())

    def delete_dns_stage(
        self,
        *,
        dns_stage_id: str,
    ) -> None:
        """
        Delete DNS stage.
        Delete an existing DNS stage, specified by its `dns_stage_id`. Deleting a DNS stage is permanent, and cannot be undone.
        :param dns_stage_id: ID of the DNS stage to delete.

        Usage:
        ::

            result = api.delete_dns_stage(
                dns_stage_id="example",
            )
        """

        param_dns_stage_id = validate_path_param("dns_stage_id", dns_stage_id)

        res = self._request(
            "DELETE",
            f"/edge-services/v1beta1/dns-stages/{param_dns_stage_id}",
        )

        self._throw_on_error(res)

    def list_tls_stages(
        self,
        *,
        order_by: Optional[ListTLSStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: str,
        secret_id: Optional[str] = None,
        secret_region: Optional[str] = None,
    ) -> ListTLSStagesResponse:
        """
        List TLS stages.
        List all TLS stages, for a Scaleway Organization or Scaleway Project. By default, the TLS stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of TLS stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of TLS stages to return per page.
        :param pipeline_id: Pipeline ID to filter for. Only TLS stages from this pipeline will be returned.
        :param secret_id: Secret ID to filter for. Only TLS stages with this Secret ID will be returned.
        :param secret_region: Secret region to filter for. Only TLS stages with a Secret in this region will be returned.
        :return: :class:`ListTLSStagesResponse <ListTLSStagesResponse>`

        Usage:
        ::

            result = api.list_tls_stages(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "GET",
            f"/edge-services/v1beta1/pipelines/{param_pipeline_id}/tls-stages",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "secret_id": secret_id,
                "secret_region": secret_region,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListTLSStagesResponse(res.json())

    def list_tls_stages_all(
        self,
        *,
        order_by: Optional[ListTLSStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: str,
        secret_id: Optional[str] = None,
        secret_region: Optional[str] = None,
    ) -> list[TLSStage]:
        """
        List TLS stages.
        List all TLS stages, for a Scaleway Organization or Scaleway Project. By default, the TLS stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of TLS stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of TLS stages to return per page.
        :param pipeline_id: Pipeline ID to filter for. Only TLS stages from this pipeline will be returned.
        :param secret_id: Secret ID to filter for. Only TLS stages with this Secret ID will be returned.
        :param secret_region: Secret region to filter for. Only TLS stages with a Secret in this region will be returned.
        :return: :class:`list[TLSStage] <list[TLSStage]>`

        Usage:
        ::

            result = api.list_tls_stages_all(
                pipeline_id="example",
            )
        """

        return fetch_all_pages(
            type=ListTLSStagesResponse,
            key="stages",
            fetcher=self.list_tls_stages,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "pipeline_id": pipeline_id,
                "secret_id": secret_id,
                "secret_region": secret_region,
            },
        )

    def create_tls_stage(
        self,
        *,
        secrets: Optional[list[TLSSecret]] = None,
        managed_certificate: Optional[bool] = None,
        cache_stage_id: Optional[str] = None,
        backend_stage_id: Optional[str] = None,
        pipeline_id: str,
        route_stage_id: Optional[str] = None,
        waf_stage_id: Optional[str] = None,
    ) -> TLSStage:
        """
        Create TLS stage.
        Create a new TLS stage. You must specify either the `secrets` or `managed_certificate` fields to customize the SSL/TLS certificate of your endpoint. Choose `secrets` if you are using a pre-existing certificate held in Scaleway Secret Manager, or `managed_certificate` to let Scaleway generate and manage a Let's Encrypt certificate for your customized endpoint.
        :param secrets: Secret (from Scaleway Secret Manager) containing your custom certificate.
        :param managed_certificate: True when Scaleway generates and manages a Let's Encrypt certificate for the TLS stage/custom endpoint.
        :param cache_stage_id: Cache stage ID the TLS stage will be linked to.
        One-Of ('next'): at most one of 'cache_stage_id', 'backend_stage_id', 'route_stage_id', 'waf_stage_id' could be set.
        :param backend_stage_id: Backend stage ID the TLS stage will be linked to.
        One-Of ('next'): at most one of 'cache_stage_id', 'backend_stage_id', 'route_stage_id', 'waf_stage_id' could be set.
        :param pipeline_id: Pipeline ID the TLS stage belongs to.
        :param route_stage_id:
        One-Of ('next'): at most one of 'cache_stage_id', 'backend_stage_id', 'route_stage_id', 'waf_stage_id' could be set.
        :param waf_stage_id:
        One-Of ('next'): at most one of 'cache_stage_id', 'backend_stage_id', 'route_stage_id', 'waf_stage_id' could be set.
        :return: :class:`TLSStage <TLSStage>`

        Usage:
        ::

            result = api.create_tls_stage(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "POST",
            f"/edge-services/v1beta1/pipelines/{param_pipeline_id}/tls-stages",
            body=marshal_CreateTLSStageRequest(
                CreateTLSStageRequest(
                    secrets=secrets,
                    managed_certificate=managed_certificate,
                    pipeline_id=pipeline_id,
                    cache_stage_id=cache_stage_id,
                    backend_stage_id=backend_stage_id,
                    route_stage_id=route_stage_id,
                    waf_stage_id=waf_stage_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_TLSStage(res.json())

    def get_tls_stage(
        self,
        *,
        tls_stage_id: str,
    ) -> TLSStage:
        """
        Get TLS stage.
        Retrieve information about an existing TLS stage, specified by its `tls_stage_id`. Its full details, including secrets and certificate expiration date are returned in the response object.
        :param tls_stage_id: ID of the requested TLS stage.
        :return: :class:`TLSStage <TLSStage>`

        Usage:
        ::

            result = api.get_tls_stage(
                tls_stage_id="example",
            )
        """

        param_tls_stage_id = validate_path_param("tls_stage_id", tls_stage_id)

        res = self._request(
            "GET",
            f"/edge-services/v1beta1/tls-stages/{param_tls_stage_id}",
        )

        self._throw_on_error(res)
        return unmarshal_TLSStage(res.json())

    def update_tls_stage(
        self,
        *,
        tls_stage_id: str,
        tls_secrets_config: Optional[TLSSecretsConfig] = None,
        managed_certificate: Optional[bool] = None,
        cache_stage_id: Optional[str] = None,
        backend_stage_id: Optional[str] = None,
        route_stage_id: Optional[str] = None,
        waf_stage_id: Optional[str] = None,
    ) -> TLSStage:
        """
        Update TLS stage.
        Update the parameters of an existing TLS stage, specified by its `tls_stage_id`. Both `tls_secrets_config` and `managed_certificate` parameters can be updated.
        :param tls_stage_id: ID of the TLS stage to update.
        :param tls_secrets_config: Secret (from Scaleway Secret-Manager) containing your custom certificate.
        :param managed_certificate: True when Scaleway generates and manages a Let's Encrypt certificate for the TLS stage/custom endpoint.
        :param cache_stage_id: Cache stage ID the TLS stage will be linked to.
        One-Of ('next'): at most one of 'cache_stage_id', 'backend_stage_id', 'route_stage_id', 'waf_stage_id' could be set.
        :param backend_stage_id: Backend stage ID the TLS stage will be linked to.
        One-Of ('next'): at most one of 'cache_stage_id', 'backend_stage_id', 'route_stage_id', 'waf_stage_id' could be set.
        :param route_stage_id:
        One-Of ('next'): at most one of 'cache_stage_id', 'backend_stage_id', 'route_stage_id', 'waf_stage_id' could be set.
        :param waf_stage_id:
        One-Of ('next'): at most one of 'cache_stage_id', 'backend_stage_id', 'route_stage_id', 'waf_stage_id' could be set.
        :return: :class:`TLSStage <TLSStage>`

        Usage:
        ::

            result = api.update_tls_stage(
                tls_stage_id="example",
            )
        """

        param_tls_stage_id = validate_path_param("tls_stage_id", tls_stage_id)

        res = self._request(
            "PATCH",
            f"/edge-services/v1beta1/tls-stages/{param_tls_stage_id}",
            body=marshal_UpdateTLSStageRequest(
                UpdateTLSStageRequest(
                    tls_stage_id=tls_stage_id,
                    tls_secrets_config=tls_secrets_config,
                    managed_certificate=managed_certificate,
                    cache_stage_id=cache_stage_id,
                    backend_stage_id=backend_stage_id,
                    route_stage_id=route_stage_id,
                    waf_stage_id=waf_stage_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_TLSStage(res.json())

    def delete_tls_stage(
        self,
        *,
        tls_stage_id: str,
    ) -> None:
        """
        Delete TLS stage.
        Delete an existing TLS stage, specified by its `tls_stage_id`. Deleting a TLS stage is permanent, and cannot be undone.
        :param tls_stage_id: ID of the TLS stage to delete.

        Usage:
        ::

            result = api.delete_tls_stage(
                tls_stage_id="example",
            )
        """

        param_tls_stage_id = validate_path_param("tls_stage_id", tls_stage_id)

        res = self._request(
            "DELETE",
            f"/edge-services/v1beta1/tls-stages/{param_tls_stage_id}",
        )

        self._throw_on_error(res)

    def list_cache_stages(
        self,
        *,
        order_by: Optional[ListCacheStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: str,
    ) -> ListCacheStagesResponse:
        """
        List cache stages.
        List all cache stages, for a Scaleway Organization or Scaleway Project. By default, the cache stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of cache stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of cache stages to return per page.
        :param pipeline_id: Pipeline ID to filter for. Only cache stages from this pipeline will be returned.
        :return: :class:`ListCacheStagesResponse <ListCacheStagesResponse>`

        Usage:
        ::

            result = api.list_cache_stages(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "GET",
            f"/edge-services/v1beta1/pipelines/{param_pipeline_id}/cache-stages",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListCacheStagesResponse(res.json())

    def list_cache_stages_all(
        self,
        *,
        order_by: Optional[ListCacheStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: str,
    ) -> list[CacheStage]:
        """
        List cache stages.
        List all cache stages, for a Scaleway Organization or Scaleway Project. By default, the cache stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of cache stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of cache stages to return per page.
        :param pipeline_id: Pipeline ID to filter for. Only cache stages from this pipeline will be returned.
        :return: :class:`list[CacheStage] <list[CacheStage]>`

        Usage:
        ::

            result = api.list_cache_stages_all(
                pipeline_id="example",
            )
        """

        return fetch_all_pages(
            type=ListCacheStagesResponse,
            key="stages",
            fetcher=self.list_cache_stages,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "pipeline_id": pipeline_id,
            },
        )

    def create_cache_stage(
        self,
        *,
        fallback_ttl: Optional[str] = None,
        include_cookies: Optional[bool] = None,
        backend_stage_id: Optional[str] = None,
        pipeline_id: str,
        waf_stage_id: Optional[str] = None,
        route_stage_id: Optional[str] = None,
    ) -> CacheStage:
        """
        Create cache stage.
        Create a new cache stage. You must specify the `fallback_ttl` field to customize the TTL of the cache.
        :param fallback_ttl: Time To Live (TTL) in seconds. Defines how long content is cached.
        :param include_cookies: Defines whether responses to requests with cookies must be stored in the cache.
        :param backend_stage_id: Backend stage ID the cache stage will be linked to.
        One-Of ('next'): at most one of 'backend_stage_id', 'waf_stage_id', 'route_stage_id' could be set.
        :param pipeline_id: Pipeline ID the Cache stage belongs to.
        :param waf_stage_id:
        One-Of ('next'): at most one of 'backend_stage_id', 'waf_stage_id', 'route_stage_id' could be set.
        :param route_stage_id:
        One-Of ('next'): at most one of 'backend_stage_id', 'waf_stage_id', 'route_stage_id' could be set.
        :return: :class:`CacheStage <CacheStage>`

        Usage:
        ::

            result = api.create_cache_stage(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "POST",
            f"/edge-services/v1beta1/pipelines/{param_pipeline_id}/cache-stages",
            body=marshal_CreateCacheStageRequest(
                CreateCacheStageRequest(
                    fallback_ttl=fallback_ttl,
                    include_cookies=include_cookies,
                    pipeline_id=pipeline_id,
                    backend_stage_id=backend_stage_id,
                    waf_stage_id=waf_stage_id,
                    route_stage_id=route_stage_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CacheStage(res.json())

    def get_cache_stage(
        self,
        *,
        cache_stage_id: str,
    ) -> CacheStage:
        """
        Get cache stage.
        Retrieve information about an existing cache stage, specified by its `cache_stage_id`. Its full details, including Time To Live (TTL), are returned in the response object.
        :param cache_stage_id: ID of the requested cache stage.
        :return: :class:`CacheStage <CacheStage>`

        Usage:
        ::

            result = api.get_cache_stage(
                cache_stage_id="example",
            )
        """

        param_cache_stage_id = validate_path_param("cache_stage_id", cache_stage_id)

        res = self._request(
            "GET",
            f"/edge-services/v1beta1/cache-stages/{param_cache_stage_id}",
        )

        self._throw_on_error(res)
        return unmarshal_CacheStage(res.json())

    def update_cache_stage(
        self,
        *,
        cache_stage_id: str,
        fallback_ttl: Optional[str] = None,
        include_cookies: Optional[bool] = None,
        backend_stage_id: Optional[str] = None,
        waf_stage_id: Optional[str] = None,
        route_stage_id: Optional[str] = None,
    ) -> CacheStage:
        """
        Update cache stage.
        Update the parameters of an existing cache stage, specified by its `cache_stage_id`. Parameters which can be updated include the `fallback_ttl`, `include_cookies` and `backend_stage_id`.
        :param cache_stage_id: ID of the cache stage to update.
        :param fallback_ttl: Time To Live (TTL) in seconds. Defines how long content is cached.
        :param include_cookies: Defines whether responses to requests with cookies must be stored in the cache.
        :param backend_stage_id: Backend stage ID the cache stage will be linked to.
        One-Of ('next'): at most one of 'backend_stage_id', 'waf_stage_id', 'route_stage_id' could be set.
        :param waf_stage_id:
        One-Of ('next'): at most one of 'backend_stage_id', 'waf_stage_id', 'route_stage_id' could be set.
        :param route_stage_id:
        One-Of ('next'): at most one of 'backend_stage_id', 'waf_stage_id', 'route_stage_id' could be set.
        :return: :class:`CacheStage <CacheStage>`

        Usage:
        ::

            result = api.update_cache_stage(
                cache_stage_id="example",
            )
        """

        param_cache_stage_id = validate_path_param("cache_stage_id", cache_stage_id)

        res = self._request(
            "PATCH",
            f"/edge-services/v1beta1/cache-stages/{param_cache_stage_id}",
            body=marshal_UpdateCacheStageRequest(
                UpdateCacheStageRequest(
                    cache_stage_id=cache_stage_id,
                    fallback_ttl=fallback_ttl,
                    include_cookies=include_cookies,
                    backend_stage_id=backend_stage_id,
                    waf_stage_id=waf_stage_id,
                    route_stage_id=route_stage_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CacheStage(res.json())

    def delete_cache_stage(
        self,
        *,
        cache_stage_id: str,
    ) -> None:
        """
        Delete cache stage.
        Delete an existing cache stage, specified by its `cache_stage_id`. Deleting a cache stage is permanent, and cannot be undone.
        :param cache_stage_id: ID of the cache stage to delete.

        Usage:
        ::

            result = api.delete_cache_stage(
                cache_stage_id="example",
            )
        """

        param_cache_stage_id = validate_path_param("cache_stage_id", cache_stage_id)

        res = self._request(
            "DELETE",
            f"/edge-services/v1beta1/cache-stages/{param_cache_stage_id}",
        )

        self._throw_on_error(res)

    def list_backend_stages(
        self,
        *,
        order_by: Optional[ListBackendStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: str,
        bucket_name: Optional[str] = None,
        bucket_region: Optional[str] = None,
        lb_id: Optional[str] = None,
    ) -> ListBackendStagesResponse:
        """
        List backend stages.
        List all backend stages, for a Scaleway Organization or Scaleway Project. By default, the backend stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of backend stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of backend stages to return per page.
        :param pipeline_id: Pipeline ID to filter for. Only backend stages from this pipeline will be returned.
        :param bucket_name: Bucket name to filter for. Only backend stages from this Bucket will be returned.
        :param bucket_region: Bucket region to filter for. Only backend stages with buckets in this region will be returned.
        :param lb_id: Load Balancer ID to filter for. Only backend stages with this Load Balancer will be returned.
        :return: :class:`ListBackendStagesResponse <ListBackendStagesResponse>`

        Usage:
        ::

            result = api.list_backend_stages(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "GET",
            f"/edge-services/v1beta1/pipelines/{param_pipeline_id}/backend-stages",
            params={
                "bucket_name": bucket_name,
                "bucket_region": bucket_region,
                "lb_id": lb_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListBackendStagesResponse(res.json())

    def list_backend_stages_all(
        self,
        *,
        order_by: Optional[ListBackendStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: str,
        bucket_name: Optional[str] = None,
        bucket_region: Optional[str] = None,
        lb_id: Optional[str] = None,
    ) -> list[BackendStage]:
        """
        List backend stages.
        List all backend stages, for a Scaleway Organization or Scaleway Project. By default, the backend stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of backend stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of backend stages to return per page.
        :param pipeline_id: Pipeline ID to filter for. Only backend stages from this pipeline will be returned.
        :param bucket_name: Bucket name to filter for. Only backend stages from this Bucket will be returned.
        :param bucket_region: Bucket region to filter for. Only backend stages with buckets in this region will be returned.
        :param lb_id: Load Balancer ID to filter for. Only backend stages with this Load Balancer will be returned.
        :return: :class:`list[BackendStage] <list[BackendStage]>`

        Usage:
        ::

            result = api.list_backend_stages_all(
                pipeline_id="example",
            )
        """

        return fetch_all_pages(
            type=ListBackendStagesResponse,
            key="stages",
            fetcher=self.list_backend_stages,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "pipeline_id": pipeline_id,
                "bucket_name": bucket_name,
                "bucket_region": bucket_region,
                "lb_id": lb_id,
            },
        )

    def create_backend_stage(
        self,
        *,
        scaleway_s3: Optional[ScalewayS3BackendConfig] = None,
        scaleway_lb: Optional[ScalewayLbBackendConfig] = None,
        pipeline_id: str,
        scaleway_serverless_container: Optional[
            ScalewayServerlessContainerBackendConfig
        ] = None,
        scaleway_serverless_function: Optional[
            ScalewayServerlessFunctionBackendConfig
        ] = None,
    ) -> BackendStage:
        """
        Create backend stage.
        Create a new backend stage. You must specify either a `scaleway_s3` (for a Scaleway Object Storage bucket) or `scaleway_lb` (for a Scaleway Load Balancer) field to configure the origin.
        :param scaleway_s3: Scaleway Object Storage origin bucket (S3) linked to the backend stage.
        One-Of ('backend_config'): at most one of 'scaleway_s3', 'scaleway_lb', 'scaleway_serverless_container', 'scaleway_serverless_function' could be set.
        :param scaleway_lb: Scaleway Load Balancer origin linked to the backend stage.
        One-Of ('backend_config'): at most one of 'scaleway_s3', 'scaleway_lb', 'scaleway_serverless_container', 'scaleway_serverless_function' could be set.
        :param pipeline_id: Pipeline ID the Backend stage belongs to.
        :param scaleway_serverless_container:
        One-Of ('backend_config'): at most one of 'scaleway_s3', 'scaleway_lb', 'scaleway_serverless_container', 'scaleway_serverless_function' could be set.
        :param scaleway_serverless_function:
        One-Of ('backend_config'): at most one of 'scaleway_s3', 'scaleway_lb', 'scaleway_serverless_container', 'scaleway_serverless_function' could be set.
        :return: :class:`BackendStage <BackendStage>`

        Usage:
        ::

            result = api.create_backend_stage(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "POST",
            f"/edge-services/v1beta1/pipelines/{param_pipeline_id}/backend-stages",
            body=marshal_CreateBackendStageRequest(
                CreateBackendStageRequest(
                    pipeline_id=pipeline_id,
                    scaleway_s3=scaleway_s3,
                    scaleway_lb=scaleway_lb,
                    scaleway_serverless_container=scaleway_serverless_container,
                    scaleway_serverless_function=scaleway_serverless_function,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_BackendStage(res.json())

    def get_backend_stage(
        self,
        *,
        backend_stage_id: str,
    ) -> BackendStage:
        """
        Get backend stage.
        Retrieve information about an existing backend stage, specified by its `backend_stage_id`. Its full details, including `scaleway_s3` or `scaleway_lb`, are returned in the response object.
        :param backend_stage_id: ID of the requested backend stage.
        :return: :class:`BackendStage <BackendStage>`

        Usage:
        ::

            result = api.get_backend_stage(
                backend_stage_id="example",
            )
        """

        param_backend_stage_id = validate_path_param(
            "backend_stage_id", backend_stage_id
        )

        res = self._request(
            "GET",
            f"/edge-services/v1beta1/backend-stages/{param_backend_stage_id}",
        )

        self._throw_on_error(res)
        return unmarshal_BackendStage(res.json())

    def update_backend_stage(
        self,
        *,
        backend_stage_id: str,
        pipeline_id: str,
        scaleway_s3: Optional[ScalewayS3BackendConfig] = None,
        scaleway_lb: Optional[ScalewayLbBackendConfig] = None,
        scaleway_serverless_container: Optional[
            ScalewayServerlessContainerBackendConfig
        ] = None,
        scaleway_serverless_function: Optional[
            ScalewayServerlessFunctionBackendConfig
        ] = None,
    ) -> BackendStage:
        """
        Update backend stage.
        Update the parameters of an existing backend stage, specified by its `backend_stage_id`.
        :param backend_stage_id: ID of the backend stage to update.
        :param pipeline_id: Pipeline ID the Backend stage belongs to.
        :param scaleway_s3: Scaleway Object Storage origin bucket (S3) linked to the backend stage.
        One-Of ('backend_config'): at most one of 'scaleway_s3', 'scaleway_lb', 'scaleway_serverless_container', 'scaleway_serverless_function' could be set.
        :param scaleway_lb: Scaleway Load Balancer origin linked to the backend stage.
        One-Of ('backend_config'): at most one of 'scaleway_s3', 'scaleway_lb', 'scaleway_serverless_container', 'scaleway_serverless_function' could be set.
        :param scaleway_serverless_container:
        One-Of ('backend_config'): at most one of 'scaleway_s3', 'scaleway_lb', 'scaleway_serverless_container', 'scaleway_serverless_function' could be set.
        :param scaleway_serverless_function:
        One-Of ('backend_config'): at most one of 'scaleway_s3', 'scaleway_lb', 'scaleway_serverless_container', 'scaleway_serverless_function' could be set.
        :return: :class:`BackendStage <BackendStage>`

        Usage:
        ::

            result = api.update_backend_stage(
                backend_stage_id="example",
                pipeline_id="example",
            )
        """

        param_backend_stage_id = validate_path_param(
            "backend_stage_id", backend_stage_id
        )

        res = self._request(
            "PATCH",
            f"/edge-services/v1beta1/backend-stages/{param_backend_stage_id}",
            body=marshal_UpdateBackendStageRequest(
                UpdateBackendStageRequest(
                    backend_stage_id=backend_stage_id,
                    pipeline_id=pipeline_id,
                    scaleway_s3=scaleway_s3,
                    scaleway_lb=scaleway_lb,
                    scaleway_serverless_container=scaleway_serverless_container,
                    scaleway_serverless_function=scaleway_serverless_function,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_BackendStage(res.json())

    def delete_backend_stage(
        self,
        *,
        backend_stage_id: str,
    ) -> None:
        """
        Delete backend stage.
        Delete an existing backend stage, specified by its `backend_stage_id`. Deleting a backend stage is permanent, and cannot be undone.
        :param backend_stage_id: ID of the backend stage to delete.

        Usage:
        ::

            result = api.delete_backend_stage(
                backend_stage_id="example",
            )
        """

        param_backend_stage_id = validate_path_param(
            "backend_stage_id", backend_stage_id
        )

        res = self._request(
            "DELETE",
            f"/edge-services/v1beta1/backend-stages/{param_backend_stage_id}",
        )

        self._throw_on_error(res)

    def search_backend_stages(
        self,
        *,
        order_by: Optional[SearchBackendStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        bucket_name: Optional[str] = None,
        bucket_region: Optional[str] = None,
        lb_id: Optional[str] = None,
    ) -> ListBackendStagesResponse:
        """
        :param order_by:
        :param page:
        :param page_size:
        :param project_id:
        :param bucket_name:
        :param bucket_region:
        :param lb_id:
        :return: :class:`ListBackendStagesResponse <ListBackendStagesResponse>`

        Usage:
        ::

            result = api.search_backend_stages()
        """

        res = self._request(
            "GET",
            "/edge-services/v1beta1/search-backend-stages",
            params={
                "bucket_name": bucket_name,
                "bucket_region": bucket_region,
                "lb_id": lb_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListBackendStagesResponse(res.json())

    def list_waf_stages(
        self,
        *,
        order_by: Optional[ListWafStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: str,
    ) -> ListWafStagesResponse:
        """
        List WAF stages.
        List all WAF stages, for a Scaleway Organization or Scaleway Project. By default, the WAF stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of WAF stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of WAF stages to return per page.
        :param pipeline_id: Pipeline ID to filter for. Only WAF stages from this pipeline will be returned.
        :return: :class:`ListWafStagesResponse <ListWafStagesResponse>`

        Usage:
        ::

            result = api.list_waf_stages(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "GET",
            f"/edge-services/v1beta1/pipelines/{param_pipeline_id}/waf-stages",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListWafStagesResponse(res.json())

    def list_waf_stages_all(
        self,
        *,
        order_by: Optional[ListWafStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: str,
    ) -> list[WafStage]:
        """
        List WAF stages.
        List all WAF stages, for a Scaleway Organization or Scaleway Project. By default, the WAF stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of WAF stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of WAF stages to return per page.
        :param pipeline_id: Pipeline ID to filter for. Only WAF stages from this pipeline will be returned.
        :return: :class:`list[WafStage] <list[WafStage]>`

        Usage:
        ::

            result = api.list_waf_stages_all(
                pipeline_id="example",
            )
        """

        return fetch_all_pages(
            type=ListWafStagesResponse,
            key="stages",
            fetcher=self.list_waf_stages,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "pipeline_id": pipeline_id,
            },
        )

    def create_waf_stage(
        self,
        *,
        pipeline_id: str,
        paranoia_level: int,
        mode: Optional[WafStageMode] = None,
        backend_stage_id: Optional[str] = None,
    ) -> WafStage:
        """
        Create WAF stage.
        Create a new WAF stage. You must specify the `mode` and `paranoia_level` fields to customize the WAF.
        :param pipeline_id: Pipeline ID the WAF stage belongs to.
        :param paranoia_level: Sensitivity level (`1`,`2`,`3`,`4`) to use when classifying requests as malicious. With a high level, requests are more likely to be classed as malicious, and false positives are expected. With a lower level, requests are more likely to be classed as benign.
        :param mode: Mode defining WAF behavior (`disable`/`log_only`/`enable`).
        :param backend_stage_id: ID of the backend stage to forward requests to after the WAF stage.
        One-Of ('next'): at most one of 'backend_stage_id' could be set.
        :return: :class:`WafStage <WafStage>`

        Usage:
        ::

            result = api.create_waf_stage(
                pipeline_id="example",
                paranoia_level=1,
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "POST",
            f"/edge-services/v1beta1/pipelines/{param_pipeline_id}/waf-stages",
            body=marshal_CreateWafStageRequest(
                CreateWafStageRequest(
                    pipeline_id=pipeline_id,
                    paranoia_level=paranoia_level,
                    mode=mode,
                    backend_stage_id=backend_stage_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_WafStage(res.json())

    def get_waf_stage(
        self,
        *,
        waf_stage_id: str,
    ) -> WafStage:
        """
        Get WAF stage.
        Retrieve information about an existing WAF stage, specified by its `waf_stage_id`. Its full details are returned in the response object.
        :param waf_stage_id: ID of the requested WAF stage.
        :return: :class:`WafStage <WafStage>`

        Usage:
        ::

            result = api.get_waf_stage(
                waf_stage_id="example",
            )
        """

        param_waf_stage_id = validate_path_param("waf_stage_id", waf_stage_id)

        res = self._request(
            "GET",
            f"/edge-services/v1beta1/waf-stages/{param_waf_stage_id}",
        )

        self._throw_on_error(res)
        return unmarshal_WafStage(res.json())

    def update_waf_stage(
        self,
        *,
        waf_stage_id: str,
        mode: Optional[WafStageMode] = None,
        paranoia_level: Optional[int] = None,
        backend_stage_id: Optional[str] = None,
    ) -> WafStage:
        """
        Update WAF stage.
        Update the parameters of an existing WAF stage, specified by its `waf_stage_id`. Both `mode` and `paranoia_level` parameters can be updated.
        :param waf_stage_id: ID of the WAF stage to update.
        :param mode: Mode defining WAF behavior (`disable`/`log_only`/`enable`).
        :param paranoia_level: Sensitivity level (`1`,`2`,`3`,`4`) to use when classifying requests as malicious. With a high level, requests are more likely to be classed as malicious, and false positives are expected. With a lower level, requests are more likely to be classed as benign.
        :param backend_stage_id: ID of the backend stage to forward requests to after the WAF stage.
        One-Of ('next'): at most one of 'backend_stage_id' could be set.
        :return: :class:`WafStage <WafStage>`

        Usage:
        ::

            result = api.update_waf_stage(
                waf_stage_id="example",
            )
        """

        param_waf_stage_id = validate_path_param("waf_stage_id", waf_stage_id)

        res = self._request(
            "PATCH",
            f"/edge-services/v1beta1/waf-stages/{param_waf_stage_id}",
            body=marshal_UpdateWafStageRequest(
                UpdateWafStageRequest(
                    waf_stage_id=waf_stage_id,
                    mode=mode,
                    paranoia_level=paranoia_level,
                    backend_stage_id=backend_stage_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_WafStage(res.json())

    def delete_waf_stage(
        self,
        *,
        waf_stage_id: str,
    ) -> None:
        """
        Delete WAF stage.
        Delete an existing WAF stage, specified by its `waf_stage_id`. Deleting a WAF stage is permanent, and cannot be undone.
        :param waf_stage_id: ID of the WAF stage to delete.

        Usage:
        ::

            result = api.delete_waf_stage(
                waf_stage_id="example",
            )
        """

        param_waf_stage_id = validate_path_param("waf_stage_id", waf_stage_id)

        res = self._request(
            "DELETE",
            f"/edge-services/v1beta1/waf-stages/{param_waf_stage_id}",
        )

        self._throw_on_error(res)

    def search_waf_stages(
        self,
        *,
        order_by: Optional[SearchWafStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
    ) -> ListWafStagesResponse:
        """
        :param order_by:
        :param page:
        :param page_size:
        :param project_id:
        :return: :class:`ListWafStagesResponse <ListWafStagesResponse>`

        Usage:
        ::

            result = api.search_waf_stages()
        """

        res = self._request(
            "GET",
            "/edge-services/v1beta1/search-waf-stages",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListWafStagesResponse(res.json())

    def list_route_stages(
        self,
        *,
        order_by: Optional[ListRouteStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: str,
    ) -> ListRouteStagesResponse:
        """
        List route stages.
        List all route stages, for a given pipeline. By default, the route stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of route stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of route stages to return per page.
        :param pipeline_id: Pipeline ID to filter for. Only route stages from this pipeline will be returned.
        :return: :class:`ListRouteStagesResponse <ListRouteStagesResponse>`

        Usage:
        ::

            result = api.list_route_stages(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "GET",
            f"/edge-services/v1beta1/pipelines/{param_pipeline_id}/route-stages",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRouteStagesResponse(res.json())

    def list_route_stages_all(
        self,
        *,
        order_by: Optional[ListRouteStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: str,
    ) -> list[RouteStage]:
        """
        List route stages.
        List all route stages, for a given pipeline. By default, the route stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of route stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of route stages to return per page.
        :param pipeline_id: Pipeline ID to filter for. Only route stages from this pipeline will be returned.
        :return: :class:`list[RouteStage] <list[RouteStage]>`

        Usage:
        ::

            result = api.list_route_stages_all(
                pipeline_id="example",
            )
        """

        return fetch_all_pages(
            type=ListRouteStagesResponse,
            key="stages",
            fetcher=self.list_route_stages,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "pipeline_id": pipeline_id,
            },
        )

    def create_route_stage(
        self,
        *,
        pipeline_id: str,
        waf_stage_id: Optional[str] = None,
    ) -> RouteStage:
        """
        Create route stage.
        Create a new route stage. You must specify the `waf_stage_id` field to customize the route.
        :param pipeline_id: Pipeline ID the route stage belongs to.
        :param waf_stage_id: ID of the WAF stage HTTP requests should be forwarded to when no rules are matched.
        One-Of ('next'): at most one of 'waf_stage_id' could be set.
        :return: :class:`RouteStage <RouteStage>`

        Usage:
        ::

            result = api.create_route_stage(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "POST",
            f"/edge-services/v1beta1/pipelines/{param_pipeline_id}/route-stages",
            body=marshal_CreateRouteStageRequest(
                CreateRouteStageRequest(
                    pipeline_id=pipeline_id,
                    waf_stage_id=waf_stage_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_RouteStage(res.json())

    def get_route_stage(
        self,
        *,
        route_stage_id: str,
    ) -> RouteStage:
        """
        Get route stage.
        Retrieve information about an existing route stage, specified by its `route_stage_id`. The summary of the route stage (without route rules) is returned in the response object.
        :param route_stage_id: ID of the requested route stage.
        :return: :class:`RouteStage <RouteStage>`

        Usage:
        ::

            result = api.get_route_stage(
                route_stage_id="example",
            )
        """

        param_route_stage_id = validate_path_param("route_stage_id", route_stage_id)

        res = self._request(
            "GET",
            f"/edge-services/v1beta1/route-stages/{param_route_stage_id}",
        )

        self._throw_on_error(res)
        return unmarshal_RouteStage(res.json())

    def update_route_stage(
        self,
        *,
        route_stage_id: str,
        waf_stage_id: Optional[str] = None,
    ) -> RouteStage:
        """
        Update route stage.
        Update the parameters of an existing route stage, specified by its `route_stage_id`.
        :param route_stage_id: ID of the route stage to update.
        :param waf_stage_id: ID of the WAF stage HTTP requests should be forwarded to when no rules are matched.
        One-Of ('next'): at most one of 'waf_stage_id' could be set.
        :return: :class:`RouteStage <RouteStage>`

        Usage:
        ::

            result = api.update_route_stage(
                route_stage_id="example",
            )
        """

        param_route_stage_id = validate_path_param("route_stage_id", route_stage_id)

        res = self._request(
            "PATCH",
            f"/edge-services/v1beta1/route-stages/{param_route_stage_id}",
            body=marshal_UpdateRouteStageRequest(
                UpdateRouteStageRequest(
                    route_stage_id=route_stage_id,
                    waf_stage_id=waf_stage_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_RouteStage(res.json())

    def delete_route_stage(
        self,
        *,
        route_stage_id: str,
    ) -> None:
        """
        Delete route stage.
        Delete an existing route stage, specified by its `route_stage_id`. Deleting a route stage is permanent, and cannot be undone.
        :param route_stage_id: ID of the route stage to delete.

        Usage:
        ::

            result = api.delete_route_stage(
                route_stage_id="example",
            )
        """

        param_route_stage_id = validate_path_param("route_stage_id", route_stage_id)

        res = self._request(
            "DELETE",
            f"/edge-services/v1beta1/route-stages/{param_route_stage_id}",
        )

        self._throw_on_error(res)

    def list_route_rules(
        self,
        *,
        route_stage_id: str,
    ) -> ListRouteRulesResponse:
        """
        List route rules.
        List all route rules of an existing route stage, specified by its `route_stage_id`.
        :param route_stage_id: Route stage ID to filter for. Only route rules from this route stage will be returned.
        :return: :class:`ListRouteRulesResponse <ListRouteRulesResponse>`

        Usage:
        ::

            result = api.list_route_rules(
                route_stage_id="example",
            )
        """

        param_route_stage_id = validate_path_param("route_stage_id", route_stage_id)

        res = self._request(
            "GET",
            f"/edge-services/v1beta1/route-stages/{param_route_stage_id}/route-rules",
        )

        self._throw_on_error(res)
        return unmarshal_ListRouteRulesResponse(res.json())

    def set_route_rules(
        self,
        *,
        route_stage_id: str,
        route_rules: Optional[list[SetRouteRulesRequestRouteRule]] = None,
    ) -> SetRouteRulesResponse:
        """
        Set route rules.
        Set the rules of an existing route stage, specified by its `route_stage_id`.
        :param route_stage_id: ID of the route stage to update.
        :param route_rules: List of rules to be checked against every HTTP request. The first matching rule will forward the request to its specified backend stage. If no rules are matched, the request is forwarded to the WAF stage defined by `waf_stage_id`.
        :return: :class:`SetRouteRulesResponse <SetRouteRulesResponse>`

        Usage:
        ::

            result = api.set_route_rules(
                route_stage_id="example",
            )
        """

        param_route_stage_id = validate_path_param("route_stage_id", route_stage_id)

        res = self._request(
            "PUT",
            f"/edge-services/v1beta1/route-stages/{param_route_stage_id}/route-rules",
            body=marshal_SetRouteRulesRequest(
                SetRouteRulesRequest(
                    route_stage_id=route_stage_id,
                    route_rules=route_rules,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetRouteRulesResponse(res.json())

    def add_route_rules(
        self,
        *,
        route_stage_id: str,
        route_rules: Optional[list[SetRouteRulesRequestRouteRule]] = None,
        after_position: Optional[int] = None,
        before_position: Optional[int] = None,
    ) -> AddRouteRulesResponse:
        """
        Add route rules.
        Add route rules to an existing route stage, specified by its `route_stage_id`.
        :param route_stage_id: ID of the route stage to update.
        :param route_rules: List of rules to be checked against every HTTP request. The first matching rule will forward the request to its specified backend stage. If no rules are matched, the request is forwarded to the WAF stage defined by `waf_stage_id`.
        :param after_position: Add rules after the given position.
        One-Of ('position'): at most one of 'after_position', 'before_position' could be set.
        :param before_position: Add rules before the given position.
        One-Of ('position'): at most one of 'after_position', 'before_position' could be set.
        :return: :class:`AddRouteRulesResponse <AddRouteRulesResponse>`

        Usage:
        ::

            result = api.add_route_rules(
                route_stage_id="example",
            )
        """

        param_route_stage_id = validate_path_param("route_stage_id", route_stage_id)

        res = self._request(
            "POST",
            f"/edge-services/v1beta1/route-stages/{param_route_stage_id}/route-rules",
            body=marshal_AddRouteRulesRequest(
                AddRouteRulesRequest(
                    route_stage_id=route_stage_id,
                    route_rules=route_rules,
                    after_position=after_position,
                    before_position=before_position,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_AddRouteRulesResponse(res.json())

    def search_route_rules(
        self,
        *,
        order_by: Optional[SearchRouteRulesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListRouteRulesResponse:
        """
        List route rules.
        List all route rules of an organization or project.
        :param order_by:
        :param page:
        :param page_size:
        :param organization_id:
        :param project_id:
        :return: :class:`ListRouteRulesResponse <ListRouteRulesResponse>`

        Usage:
        ::

            result = api.search_route_rules()
        """

        res = self._request(
            "GET",
            "/edge-services/v1beta1/search-route-rules",
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
        return unmarshal_ListRouteRulesResponse(res.json())

    def check_domain(
        self,
        *,
        fqdn: str,
        cname: str,
        project_id: Optional[str] = None,
    ) -> CheckDomainResponse:
        """
        :param fqdn:
        :param cname:
        :param project_id:
        :return: :class:`CheckDomainResponse <CheckDomainResponse>`

        Usage:
        ::

            result = api.check_domain(
                fqdn="example",
                cname="example",
            )
        """

        res = self._request(
            "POST",
            "/edge-services/v1beta1/check-domain",
            body=marshal_CheckDomainRequest(
                CheckDomainRequest(
                    fqdn=fqdn,
                    cname=cname,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CheckDomainResponse(res.json())

    def check_pem_chain(
        self,
        *,
        fqdn: str,
        project_id: Optional[str] = None,
        secret: Optional[CheckPEMChainRequestSecretChain] = None,
        raw: Optional[str] = None,
    ) -> CheckPEMChainResponse:
        """
        :param fqdn:
        :param project_id:
        :param secret:
        One-Of ('chain'): at most one of 'secret', 'raw' could be set.
        :param raw:
        One-Of ('chain'): at most one of 'secret', 'raw' could be set.
        :return: :class:`CheckPEMChainResponse <CheckPEMChainResponse>`

        Usage:
        ::

            result = api.check_pem_chain(
                fqdn="example",
            )
        """

        res = self._request(
            "POST",
            "/edge-services/v1beta1/check-pem-chain",
            body=marshal_CheckPEMChainRequest(
                CheckPEMChainRequest(
                    fqdn=fqdn,
                    project_id=project_id,
                    secret=secret,
                    raw=raw,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CheckPEMChainResponse(res.json())

    def list_purge_requests(
        self,
        *,
        order_by: Optional[ListPurgeRequestsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        pipeline_id: Optional[str] = None,
    ) -> ListPurgeRequestsResponse:
        """
        List purge requests.
        List all purge requests, for a Scaleway Organization or Scaleway Project. This enables you to retrieve a history of all previously-made purge requests. By default, the purge requests returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of purge requests in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of purge requests to return per page.
        :param organization_id: Organization ID to filter for. Only purge requests from this Project will be returned.
        :param project_id: Project ID to filter for. Only purge requests from this Project will be returned.
        :param pipeline_id: Pipeline ID to filter for. Only purge requests from this pipeline will be returned.
        :return: :class:`ListPurgeRequestsResponse <ListPurgeRequestsResponse>`

        Usage:
        ::

            result = api.list_purge_requests()
        """

        res = self._request(
            "GET",
            "/edge-services/v1beta1/purge-requests",
            params={
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "pipeline_id": pipeline_id,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPurgeRequestsResponse(res.json())

    def list_purge_requests_all(
        self,
        *,
        order_by: Optional[ListPurgeRequestsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        pipeline_id: Optional[str] = None,
    ) -> list[PurgeRequest]:
        """
        List purge requests.
        List all purge requests, for a Scaleway Organization or Scaleway Project. This enables you to retrieve a history of all previously-made purge requests. By default, the purge requests returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of purge requests in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of purge requests to return per page.
        :param organization_id: Organization ID to filter for. Only purge requests from this Project will be returned.
        :param project_id: Project ID to filter for. Only purge requests from this Project will be returned.
        :param pipeline_id: Pipeline ID to filter for. Only purge requests from this pipeline will be returned.
        :return: :class:`list[PurgeRequest] <list[PurgeRequest]>`

        Usage:
        ::

            result = api.list_purge_requests_all()
        """

        return fetch_all_pages(
            type=ListPurgeRequestsResponse,
            key="purge_requests",
            fetcher=self.list_purge_requests,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "organization_id": organization_id,
                "project_id": project_id,
                "pipeline_id": pipeline_id,
            },
        )

    def create_purge_request(
        self,
        *,
        pipeline_id: str,
        assets: Optional[list[str]] = None,
        all: Optional[bool] = None,
    ) -> PurgeRequest:
        """
        Create purge request.
        Create a new purge request. You must specify either the `all` field (to purge all content) or a list of `assets` (to define the precise assets to purge).
        :param pipeline_id: Pipeline ID in which the purge request will be created.
        :param assets: List of asserts to purge.
        One-Of ('target'): at most one of 'assets', 'all' could be set.
        :param all: Defines whether to purge all content.
        One-Of ('target'): at most one of 'assets', 'all' could be set.
        :return: :class:`PurgeRequest <PurgeRequest>`

        Usage:
        ::

            result = api.create_purge_request(
                pipeline_id="example",
            )
        """

        res = self._request(
            "POST",
            "/edge-services/v1beta1/purge-requests",
            body=marshal_CreatePurgeRequestRequest(
                CreatePurgeRequestRequest(
                    pipeline_id=pipeline_id,
                    assets=assets,
                    all=all,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PurgeRequest(res.json())

    def get_purge_request(
        self,
        *,
        purge_request_id: str,
    ) -> PurgeRequest:
        """
        Get purge request.
        Retrieve information about a purge request, specified by its `purge_request_id`. Its full details, including `status` and `target`, are returned in the response object.
        :param purge_request_id: ID of the requested purge request.
        :return: :class:`PurgeRequest <PurgeRequest>`

        Usage:
        ::

            result = api.get_purge_request(
                purge_request_id="example",
            )
        """

        param_purge_request_id = validate_path_param(
            "purge_request_id", purge_request_id
        )

        res = self._request(
            "GET",
            f"/edge-services/v1beta1/purge-requests/{param_purge_request_id}",
        )

        self._throw_on_error(res)
        return unmarshal_PurgeRequest(res.json())

    def wait_for_purge_request(
        self,
        *,
        purge_request_id: str,
        options: Optional[WaitForOptions[PurgeRequest, bool]] = None,
    ) -> PurgeRequest:
        """
        Get purge request.
        Retrieve information about a purge request, specified by its `purge_request_id`. Its full details, including `status` and `target`, are returned in the response object.
        :param purge_request_id: ID of the requested purge request.
        :return: :class:`PurgeRequest <PurgeRequest>`

        Usage:
        ::

            result = api.get_purge_request(
                purge_request_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: (
                res.status not in PURGE_REQUEST_TRANSIENT_STATUSES
            )

        return wait_for_resource(
            fetcher=self.get_purge_request,
            options=options,
            args={
                "purge_request_id": purge_request_id,
            },
        )

    def check_lb_origin(
        self,
        *,
        lb: Optional[ScalewayLb] = None,
    ) -> CheckLbOriginResponse:
        """
        :param lb:
        :return: :class:`CheckLbOriginResponse <CheckLbOriginResponse>`

        Usage:
        ::

            result = api.check_lb_origin()
        """

        res = self._request(
            "POST",
            "/edge-services/v1beta1/check-lb-origin",
            body=marshal_CheckLbOriginRequest(
                CheckLbOriginRequest(
                    lb=lb,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CheckLbOriginResponse(res.json())

    def list_plans(
        self,
    ) -> ListPlansResponse:
        """

        :return: :class:`ListPlansResponse <ListPlansResponse>`

        Usage:
        ::

            result = api.list_plans()
        """

        res = self._request(
            "GET",
            "/edge-services/v1beta1/plans",
        )

        self._throw_on_error(res)
        return unmarshal_ListPlansResponse(res.json())

    def select_plan(
        self,
        *,
        project_id: Optional[str] = None,
        plan_name: Optional[PlanName] = None,
    ) -> Plan:
        """
        :param project_id:
        :param plan_name:
        :return: :class:`Plan <Plan>`

        Usage:
        ::

            result = api.select_plan()
        """

        res = self._request(
            "PATCH",
            "/edge-services/v1beta1/current-plan",
            body=marshal_SelectPlanRequest(
                SelectPlanRequest(
                    project_id=project_id,
                    plan_name=plan_name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Plan(res.json())

    def get_current_plan(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Plan:
        """
        :param project_id:
        :return: :class:`Plan <Plan>`

        Usage:
        ::

            result = api.get_current_plan()
        """

        param_project_id = validate_path_param(
            "project_id", project_id or self.client.default_project_id
        )

        res = self._request(
            "GET",
            f"/edge-services/v1beta1/current-plan/{param_project_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Plan(res.json())

    def delete_current_plan(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> None:
        """
        :param project_id:

        Usage:
        ::

            result = api.delete_current_plan()
        """

        param_project_id = validate_path_param(
            "project_id", project_id or self.client.default_project_id
        )

        res = self._request(
            "DELETE",
            f"/edge-services/v1beta1/current-plan/{param_project_id}",
        )

        self._throw_on_error(res)

    def get_billing(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> GetBillingResponse:
        """
        Gives information on the currently selected Edge Services subscription plan, resource usage and associated billing information for this calendar month (including whether consumption falls within or exceeds the currently selected subscription plan.).
        :param project_id:
        :return: :class:`GetBillingResponse <GetBillingResponse>`

        Usage:
        ::

            result = api.get_billing()
        """

        param_project_id = validate_path_param(
            "project_id", project_id or self.client.default_project_id
        )

        res = self._request(
            "GET",
            f"/edge-services/v1beta1/billing/{param_project_id}",
        )

        self._throw_on_error(res)
        return unmarshal_GetBillingResponse(res.json())
