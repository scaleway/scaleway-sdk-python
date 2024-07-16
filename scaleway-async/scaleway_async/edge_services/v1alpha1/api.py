# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.utils import (
    WaitForOptions,
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    ListBackendStagesRequestOrderBy,
    ListCacheStagesRequestOrderBy,
    ListDNSStagesRequestOrderBy,
    ListPipelinesRequestOrderBy,
    ListPurgeRequestsRequestOrderBy,
    ListTLSStagesRequestOrderBy,
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
    CreateTLSStageRequest,
    DNSStage,
    ListBackendStagesResponse,
    ListCacheStagesResponse,
    ListDNSStagesResponse,
    ListPipelinesResponse,
    ListPurgeRequestsResponse,
    ListTLSStagesResponse,
    Pipeline,
    PurgeRequest,
    ScalewayLb,
    ScalewayLbBackendConfig,
    ScalewayS3BackendConfig,
    TLSSecret,
    TLSSecretsConfig,
    TLSStage,
    UpdateBackendStageRequest,
    UpdateCacheStageRequest,
    UpdateDNSStageRequest,
    UpdatePipelineRequest,
    UpdateTLSStageRequest,
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
    unmarshal_PurgeRequest,
    unmarshal_TLSStage,
    unmarshal_CheckDomainResponse,
    unmarshal_CheckLbOriginResponse,
    unmarshal_CheckPEMChainResponse,
    unmarshal_ListBackendStagesResponse,
    unmarshal_ListCacheStagesResponse,
    unmarshal_ListDNSStagesResponse,
    unmarshal_ListPipelinesResponse,
    unmarshal_ListPurgeRequestsResponse,
    unmarshal_ListTLSStagesResponse,
    marshal_CheckDomainRequest,
    marshal_CheckLbOriginRequest,
    marshal_CheckPEMChainRequest,
    marshal_CreateBackendStageRequest,
    marshal_CreateCacheStageRequest,
    marshal_CreateDNSStageRequest,
    marshal_CreatePipelineRequest,
    marshal_CreatePurgeRequestRequest,
    marshal_CreateTLSStageRequest,
    marshal_UpdateBackendStageRequest,
    marshal_UpdateCacheStageRequest,
    marshal_UpdateDNSStageRequest,
    marshal_UpdatePipelineRequest,
    marshal_UpdateTLSStageRequest,
)


class EdgeServicesV1Alpha1API(API):
    """ """

    async def list_pipelines(
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
        :param name: Pipeline name to filter for, only pipelines with this string within their name will be returned.
        :param organization_id: Organization ID to filter for, only pipelines from this Organization will be returned.
        :param project_id: Project ID to filter for, only pipelines from this Project will be returned.
        :param has_backend_stage_lb: Filter on backend stage, only pipelines with a Load Balancer origin will be returned.
        :return: :class:`ListPipelinesResponse <ListPipelinesResponse>`

        Usage:
        ::

            result = await api.list_pipelines()
        """

        res = self._request(
            "GET",
            "/edge-services/v1alpha1/pipelines",
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

    async def list_pipelines_all(
        self,
        *,
        order_by: Optional[ListPipelinesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        has_backend_stage_lb: Optional[bool] = None,
    ) -> List[Pipeline]:
        """
        List pipelines.
        List all pipelines, for a Scaleway Organization or Scaleway Project. By default, the pipelines returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of pipelines in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of pipelines to return per page.
        :param name: Pipeline name to filter for, only pipelines with this string within their name will be returned.
        :param organization_id: Organization ID to filter for, only pipelines from this Organization will be returned.
        :param project_id: Project ID to filter for, only pipelines from this Project will be returned.
        :param has_backend_stage_lb: Filter on backend stage, only pipelines with a Load Balancer origin will be returned.
        :return: :class:`List[Pipeline] <List[Pipeline]>`

        Usage:
        ::

            result = await api.list_pipelines_all()
        """

        return await fetch_all_pages_async(
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

    async def create_pipeline(
        self,
        *,
        name: str,
        description: str,
        project_id: Optional[str] = None,
        dns_stage_id: Optional[str] = None,
    ) -> Pipeline:
        """
        Create pipeline.
        Create a new pipeline. You must specify a `dns_stage_id` to form a stage-chain that goes all the way to the backend stage (origin), so the HTTP request will be processed according to the stages you created.
        :param name: Name of the pipeline.
        :param description: Description of the pipeline.
        :param project_id: Project ID in which the pipeline will be created.
        :param dns_stage_id: DNS stage ID the pipeline will be attached to.
        One-Of ('head'): at most one of 'dns_stage_id' could be set.
        :return: :class:`Pipeline <Pipeline>`

        Usage:
        ::

            result = await api.create_pipeline(
                name="example",
                description="example",
            )
        """

        res = self._request(
            "POST",
            "/edge-services/v1alpha1/pipelines",
            body=marshal_CreatePipelineRequest(
                CreatePipelineRequest(
                    name=name,
                    description=description,
                    project_id=project_id,
                    dns_stage_id=dns_stage_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Pipeline(res.json())

    async def get_pipeline(
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

            result = await api.get_pipeline(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "GET",
            f"/edge-services/v1alpha1/pipelines/{param_pipeline_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Pipeline(res.json())

    async def wait_for_pipeline(
        self,
        *,
        pipeline_id: str,
        options: Optional[
            WaitForOptions[Pipeline, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> Pipeline:
        """
        Get pipeline.
        Retrieve information about an existing pipeline, specified by its `pipeline_id`. Its full details, including errors, are returned in the response object.
        :param pipeline_id: ID of the requested pipeline.
        :return: :class:`Pipeline <Pipeline>`

        Usage:
        ::

            result = await api.get_pipeline(
                pipeline_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in PIPELINE_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_pipeline,
            options=options,
            args={
                "pipeline_id": pipeline_id,
            },
        )

    async def update_pipeline(
        self,
        *,
        pipeline_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        dns_stage_id: Optional[str] = None,
    ) -> Pipeline:
        """
        Update pipeline.
        Update the parameters of an existing pipeline, specified by its `pipeline_id`. Parameters which can be updated include the `name`, `description` and `dns_stage_id`.
        :param pipeline_id: ID of the pipeline to update.
        :param name: Name of the pipeline.
        :param description: Description of the pipeline.
        :param dns_stage_id: DNS stage ID the pipeline will be attached to.
        One-Of ('head'): at most one of 'dns_stage_id' could be set.
        :return: :class:`Pipeline <Pipeline>`

        Usage:
        ::

            result = await api.update_pipeline(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "PATCH",
            f"/edge-services/v1alpha1/pipelines/{param_pipeline_id}",
            body=marshal_UpdatePipelineRequest(
                UpdatePipelineRequest(
                    pipeline_id=pipeline_id,
                    name=name,
                    description=description,
                    dns_stage_id=dns_stage_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Pipeline(res.json())

    async def delete_pipeline(
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

            result = await api.delete_pipeline(
                pipeline_id="example",
            )
        """

        param_pipeline_id = validate_path_param("pipeline_id", pipeline_id)

        res = self._request(
            "DELETE",
            f"/edge-services/v1alpha1/pipelines/{param_pipeline_id}",
        )

        self._throw_on_error(res)

    async def list_dns_stages(
        self,
        *,
        order_by: Optional[ListDNSStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: Optional[str] = None,
        project_id: Optional[str] = None,
        fqdn: Optional[str] = None,
    ) -> ListDNSStagesResponse:
        """
        List DNS stages.
        List all DNS stages, for a Scaleway Organization or Scaleway Project. By default, the DNS stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of DNS stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of DNS stages to return per page.
        :param pipeline_id: Pipeline ID to filter for, only DNS stages from this pipeline will be returned.
        :param project_id: Project ID to filter for, only DNS stages from this Project will be returned.
        :param fqdn: Fully Qualified Domain Name to filter for (in the format subdomain.example.com), only DNS stages with this FQDN will be returned.
        :return: :class:`ListDNSStagesResponse <ListDNSStagesResponse>`

        Usage:
        ::

            result = await api.list_dns_stages()
        """

        res = self._request(
            "GET",
            "/edge-services/v1alpha1/dns-stages",
            params={
                "fqdn": fqdn,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "pipeline_id": pipeline_id,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDNSStagesResponse(res.json())

    async def list_dns_stages_all(
        self,
        *,
        order_by: Optional[ListDNSStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: Optional[str] = None,
        project_id: Optional[str] = None,
        fqdn: Optional[str] = None,
    ) -> List[DNSStage]:
        """
        List DNS stages.
        List all DNS stages, for a Scaleway Organization or Scaleway Project. By default, the DNS stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of DNS stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of DNS stages to return per page.
        :param pipeline_id: Pipeline ID to filter for, only DNS stages from this pipeline will be returned.
        :param project_id: Project ID to filter for, only DNS stages from this Project will be returned.
        :param fqdn: Fully Qualified Domain Name to filter for (in the format subdomain.example.com), only DNS stages with this FQDN will be returned.
        :return: :class:`List[DNSStage] <List[DNSStage]>`

        Usage:
        ::

            result = await api.list_dns_stages_all()
        """

        return await fetch_all_pages_async(
            type=ListDNSStagesResponse,
            key="stages",
            fetcher=self.list_dns_stages,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "pipeline_id": pipeline_id,
                "project_id": project_id,
                "fqdn": fqdn,
            },
        )

    async def create_dns_stage(
        self,
        *,
        project_id: Optional[str] = None,
        fqdns: Optional[List[str]] = None,
        tls_stage_id: Optional[str] = None,
        cache_stage_id: Optional[str] = None,
        backend_stage_id: Optional[str] = None,
    ) -> DNSStage:
        """
        Create DNS stage.
        Create a new DNS stage. You must specify the `fqdns` field to customize the domain endpoint, using a domain you already own.
        :param project_id: Project ID in which the DNS stage will be created.
        :param fqdns: Fully Qualified Domain Name (in the format subdomain.example.com) to attach to the stage.
        :param tls_stage_id: TLS stage ID the DNS stage will be linked to.
        One-Of ('next'): at most one of 'tls_stage_id', 'cache_stage_id', 'backend_stage_id' could be set.
        :param cache_stage_id: Cache stage ID the DNS stage will be linked to.
        One-Of ('next'): at most one of 'tls_stage_id', 'cache_stage_id', 'backend_stage_id' could be set.
        :param backend_stage_id: Backend stage ID the DNS stage will be linked to.
        One-Of ('next'): at most one of 'tls_stage_id', 'cache_stage_id', 'backend_stage_id' could be set.
        :return: :class:`DNSStage <DNSStage>`

        Usage:
        ::

            result = await api.create_dns_stage()
        """

        res = self._request(
            "POST",
            "/edge-services/v1alpha1/dns-stages",
            body=marshal_CreateDNSStageRequest(
                CreateDNSStageRequest(
                    project_id=project_id,
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

    async def get_dns_stage(
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

            result = await api.get_dns_stage(
                dns_stage_id="example",
            )
        """

        param_dns_stage_id = validate_path_param("dns_stage_id", dns_stage_id)

        res = self._request(
            "GET",
            f"/edge-services/v1alpha1/dns-stages/{param_dns_stage_id}",
        )

        self._throw_on_error(res)
        return unmarshal_DNSStage(res.json())

    async def update_dns_stage(
        self,
        *,
        dns_stage_id: str,
        fqdns: Optional[List[str]] = None,
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

            result = await api.update_dns_stage(
                dns_stage_id="example",
            )
        """

        param_dns_stage_id = validate_path_param("dns_stage_id", dns_stage_id)

        res = self._request(
            "PATCH",
            f"/edge-services/v1alpha1/dns-stages/{param_dns_stage_id}",
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

    async def delete_dns_stage(
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

            result = await api.delete_dns_stage(
                dns_stage_id="example",
            )
        """

        param_dns_stage_id = validate_path_param("dns_stage_id", dns_stage_id)

        res = self._request(
            "DELETE",
            f"/edge-services/v1alpha1/dns-stages/{param_dns_stage_id}",
        )

        self._throw_on_error(res)

    async def list_tls_stages(
        self,
        *,
        order_by: Optional[ListTLSStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: Optional[str] = None,
        project_id: Optional[str] = None,
        secret_id: Optional[str] = None,
        secret_region: Optional[str] = None,
    ) -> ListTLSStagesResponse:
        """
        List TLS stages.
        List all TLS stages, for a Scaleway Organization or Scaleway Project. By default, the TLS stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of TLS stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of TLS stages to return per page.
        :param pipeline_id: Pipeline ID to filter for, only TLS stages from this pipeline will be returned.
        :param project_id: Project ID to filter for, only TLS stages from this Project will be returned.
        :param secret_id: Secret ID to filter for, only TLS stages with this Secret ID will be returned.
        :param secret_region: Secret region to filter for, only TLS stages with a Secret in this region will be returned.
        :return: :class:`ListTLSStagesResponse <ListTLSStagesResponse>`

        Usage:
        ::

            result = await api.list_tls_stages()
        """

        res = self._request(
            "GET",
            "/edge-services/v1alpha1/tls-stages",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "pipeline_id": pipeline_id,
                "project_id": project_id or self.client.default_project_id,
                "secret_id": secret_id,
                "secret_region": secret_region,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListTLSStagesResponse(res.json())

    async def list_tls_stages_all(
        self,
        *,
        order_by: Optional[ListTLSStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: Optional[str] = None,
        project_id: Optional[str] = None,
        secret_id: Optional[str] = None,
        secret_region: Optional[str] = None,
    ) -> List[TLSStage]:
        """
        List TLS stages.
        List all TLS stages, for a Scaleway Organization or Scaleway Project. By default, the TLS stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of TLS stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of TLS stages to return per page.
        :param pipeline_id: Pipeline ID to filter for, only TLS stages from this pipeline will be returned.
        :param project_id: Project ID to filter for, only TLS stages from this Project will be returned.
        :param secret_id: Secret ID to filter for, only TLS stages with this Secret ID will be returned.
        :param secret_region: Secret region to filter for, only TLS stages with a Secret in this region will be returned.
        :return: :class:`List[TLSStage] <List[TLSStage]>`

        Usage:
        ::

            result = await api.list_tls_stages_all()
        """

        return await fetch_all_pages_async(
            type=ListTLSStagesResponse,
            key="stages",
            fetcher=self.list_tls_stages,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "pipeline_id": pipeline_id,
                "project_id": project_id,
                "secret_id": secret_id,
                "secret_region": secret_region,
            },
        )

    async def create_tls_stage(
        self,
        *,
        project_id: Optional[str] = None,
        secrets: Optional[List[TLSSecret]] = None,
        managed_certificate: Optional[bool] = None,
        cache_stage_id: Optional[str] = None,
        backend_stage_id: Optional[str] = None,
    ) -> TLSStage:
        """
        Create TLS stage.
        Create a new TLS stage. You must specify either the `secrets` or `managed_certificate` fields to customize the SSL/TLS certificate of your endpoint. Choose `secrets` if you are using a pre-existing certificate held in Scaleway Secret Manager, or `managed_certificate` to let Scaleway generate and manage a Let's Encrypt certificate for your customized endpoint.
        :param project_id: Project ID in which the TLS stage will be created.
        :param secrets: Secret (from Scaleway Secret Manager) containing your custom certificate.
        :param managed_certificate: True when Scaleway generates and manages a Let's Encrypt certificate for the TLS stage/custom endpoint.
        :param cache_stage_id: Cache stage ID the TLS stage will be linked to.
        One-Of ('next'): at most one of 'cache_stage_id', 'backend_stage_id' could be set.
        :param backend_stage_id: Backend stage ID the TLS stage will be linked to.
        One-Of ('next'): at most one of 'cache_stage_id', 'backend_stage_id' could be set.
        :return: :class:`TLSStage <TLSStage>`

        Usage:
        ::

            result = await api.create_tls_stage()
        """

        res = self._request(
            "POST",
            "/edge-services/v1alpha1/tls-stages",
            body=marshal_CreateTLSStageRequest(
                CreateTLSStageRequest(
                    project_id=project_id,
                    secrets=secrets,
                    managed_certificate=managed_certificate,
                    cache_stage_id=cache_stage_id,
                    backend_stage_id=backend_stage_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_TLSStage(res.json())

    async def get_tls_stage(
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

            result = await api.get_tls_stage(
                tls_stage_id="example",
            )
        """

        param_tls_stage_id = validate_path_param("tls_stage_id", tls_stage_id)

        res = self._request(
            "GET",
            f"/edge-services/v1alpha1/tls-stages/{param_tls_stage_id}",
        )

        self._throw_on_error(res)
        return unmarshal_TLSStage(res.json())

    async def update_tls_stage(
        self,
        *,
        tls_stage_id: str,
        tls_secrets_config: Optional[TLSSecretsConfig] = None,
        managed_certificate: Optional[bool] = None,
        cache_stage_id: Optional[str] = None,
        backend_stage_id: Optional[str] = None,
    ) -> TLSStage:
        """
        Update TLS stage.
        Update the parameters of an existing TLS stage, specified by its `tls_stage_id`. Both `tls_secrets_config` and `managed_certificate` parameters can be updated.
        :param tls_stage_id: ID of the TLS stage to update.
        :param tls_secrets_config: Secret (from Scaleway Secret-Manager) containing your custom certificate.
        :param managed_certificate: True when Scaleway generates and manages a Let's Encrypt certificate for the TLS stage/custom endpoint.
        :param cache_stage_id: Cache stage ID the TLS stage will be linked to.
        One-Of ('next'): at most one of 'cache_stage_id', 'backend_stage_id' could be set.
        :param backend_stage_id: Backend stage ID the TLS stage will be linked to.
        One-Of ('next'): at most one of 'cache_stage_id', 'backend_stage_id' could be set.
        :return: :class:`TLSStage <TLSStage>`

        Usage:
        ::

            result = await api.update_tls_stage(
                tls_stage_id="example",
            )
        """

        param_tls_stage_id = validate_path_param("tls_stage_id", tls_stage_id)

        res = self._request(
            "PATCH",
            f"/edge-services/v1alpha1/tls-stages/{param_tls_stage_id}",
            body=marshal_UpdateTLSStageRequest(
                UpdateTLSStageRequest(
                    tls_stage_id=tls_stage_id,
                    tls_secrets_config=tls_secrets_config,
                    managed_certificate=managed_certificate,
                    cache_stage_id=cache_stage_id,
                    backend_stage_id=backend_stage_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_TLSStage(res.json())

    async def delete_tls_stage(
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

            result = await api.delete_tls_stage(
                tls_stage_id="example",
            )
        """

        param_tls_stage_id = validate_path_param("tls_stage_id", tls_stage_id)

        res = self._request(
            "DELETE",
            f"/edge-services/v1alpha1/tls-stages/{param_tls_stage_id}",
        )

        self._throw_on_error(res)

    async def list_cache_stages(
        self,
        *,
        order_by: Optional[ListCacheStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListCacheStagesResponse:
        """
        List cache stages.
        List all cache stages, for a Scaleway Organization or Scaleway Project. By default, the cache stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of cache stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of cache stages to return per page.
        :param pipeline_id: Pipeline ID to filter for, only cache stages from this pipeline will be returned.
        :param project_id: Project ID to filter for, only cache stages from this Project will be returned.
        :return: :class:`ListCacheStagesResponse <ListCacheStagesResponse>`

        Usage:
        ::

            result = await api.list_cache_stages()
        """

        res = self._request(
            "GET",
            "/edge-services/v1alpha1/cache-stages",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "pipeline_id": pipeline_id,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListCacheStagesResponse(res.json())

    async def list_cache_stages_all(
        self,
        *,
        order_by: Optional[ListCacheStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[CacheStage]:
        """
        List cache stages.
        List all cache stages, for a Scaleway Organization or Scaleway Project. By default, the cache stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of cache stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of cache stages to return per page.
        :param pipeline_id: Pipeline ID to filter for, only cache stages from this pipeline will be returned.
        :param project_id: Project ID to filter for, only cache stages from this Project will be returned.
        :return: :class:`List[CacheStage] <List[CacheStage]>`

        Usage:
        ::

            result = await api.list_cache_stages_all()
        """

        return await fetch_all_pages_async(
            type=ListCacheStagesResponse,
            key="stages",
            fetcher=self.list_cache_stages,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "pipeline_id": pipeline_id,
                "project_id": project_id,
            },
        )

    async def create_cache_stage(
        self,
        *,
        project_id: Optional[str] = None,
        fallback_ttl: Optional[str] = None,
        backend_stage_id: Optional[str] = None,
    ) -> CacheStage:
        """
        Create cache stage.
        Create a new cache stage. You must specify the `fallback_ttl` field to customize the TTL of the cache.
        :param project_id: Project ID in which the cache stage will be created.
        :param fallback_ttl: Time To Live (TTL) in seconds. Defines how long content is cached.
        :param backend_stage_id: Backend stage ID the cache stage will be linked to.
        One-Of ('next'): at most one of 'backend_stage_id' could be set.
        :return: :class:`CacheStage <CacheStage>`

        Usage:
        ::

            result = await api.create_cache_stage()
        """

        res = self._request(
            "POST",
            "/edge-services/v1alpha1/cache-stages",
            body=marshal_CreateCacheStageRequest(
                CreateCacheStageRequest(
                    project_id=project_id,
                    fallback_ttl=fallback_ttl,
                    backend_stage_id=backend_stage_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CacheStage(res.json())

    async def get_cache_stage(
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

            result = await api.get_cache_stage(
                cache_stage_id="example",
            )
        """

        param_cache_stage_id = validate_path_param("cache_stage_id", cache_stage_id)

        res = self._request(
            "GET",
            f"/edge-services/v1alpha1/cache-stages/{param_cache_stage_id}",
        )

        self._throw_on_error(res)
        return unmarshal_CacheStage(res.json())

    async def update_cache_stage(
        self,
        *,
        cache_stage_id: str,
        fallback_ttl: Optional[str] = None,
        backend_stage_id: Optional[str] = None,
    ) -> CacheStage:
        """
        Update cache stage.
        Update the parameters of an existing cache stage, specified by its `cache_stage_id`. Parameters which can be updated include the `fallback_ttl` and `backend_stage_id`.
        :param cache_stage_id: ID of the cache stage to update.
        :param fallback_ttl: Time To Live (TTL) in seconds. Defines how long content is cached.
        :param backend_stage_id: Backend stage ID the cache stage will be linked to.
        One-Of ('next'): at most one of 'backend_stage_id' could be set.
        :return: :class:`CacheStage <CacheStage>`

        Usage:
        ::

            result = await api.update_cache_stage(
                cache_stage_id="example",
            )
        """

        param_cache_stage_id = validate_path_param("cache_stage_id", cache_stage_id)

        res = self._request(
            "PATCH",
            f"/edge-services/v1alpha1/cache-stages/{param_cache_stage_id}",
            body=marshal_UpdateCacheStageRequest(
                UpdateCacheStageRequest(
                    cache_stage_id=cache_stage_id,
                    fallback_ttl=fallback_ttl,
                    backend_stage_id=backend_stage_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CacheStage(res.json())

    async def delete_cache_stage(
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

            result = await api.delete_cache_stage(
                cache_stage_id="example",
            )
        """

        param_cache_stage_id = validate_path_param("cache_stage_id", cache_stage_id)

        res = self._request(
            "DELETE",
            f"/edge-services/v1alpha1/cache-stages/{param_cache_stage_id}",
        )

        self._throw_on_error(res)

    async def list_backend_stages(
        self,
        *,
        order_by: Optional[ListBackendStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: Optional[str] = None,
        project_id: Optional[str] = None,
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
        :param pipeline_id: Pipeline ID to filter for, only backend stages from this pipeline will be returned.
        :param project_id: Project ID to filter for, only backend stages from this Project will be returned.
        :param bucket_name: Bucket name to filter for, only backend stages from this Bucket will be returned.
        :param bucket_region: Bucket region to filter for, only backend stages with buckets in this region will be returned.
        :param lb_id: Load Balancer ID to filter for, only backend stages with this Load Balancer will be returned.
        :return: :class:`ListBackendStagesResponse <ListBackendStagesResponse>`

        Usage:
        ::

            result = await api.list_backend_stages()
        """

        res = self._request(
            "GET",
            "/edge-services/v1alpha1/backend-stages",
            params={
                "bucket_name": bucket_name,
                "bucket_region": bucket_region,
                "lb_id": lb_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "pipeline_id": pipeline_id,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListBackendStagesResponse(res.json())

    async def list_backend_stages_all(
        self,
        *,
        order_by: Optional[ListBackendStagesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pipeline_id: Optional[str] = None,
        project_id: Optional[str] = None,
        bucket_name: Optional[str] = None,
        bucket_region: Optional[str] = None,
        lb_id: Optional[str] = None,
    ) -> List[BackendStage]:
        """
        List backend stages.
        List all backend stages, for a Scaleway Organization or Scaleway Project. By default, the backend stages returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of backend stages in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of backend stages to return per page.
        :param pipeline_id: Pipeline ID to filter for, only backend stages from this pipeline will be returned.
        :param project_id: Project ID to filter for, only backend stages from this Project will be returned.
        :param bucket_name: Bucket name to filter for, only backend stages from this Bucket will be returned.
        :param bucket_region: Bucket region to filter for, only backend stages with buckets in this region will be returned.
        :param lb_id: Load Balancer ID to filter for, only backend stages with this Load Balancer will be returned.
        :return: :class:`List[BackendStage] <List[BackendStage]>`

        Usage:
        ::

            result = await api.list_backend_stages_all()
        """

        return await fetch_all_pages_async(
            type=ListBackendStagesResponse,
            key="stages",
            fetcher=self.list_backend_stages,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "pipeline_id": pipeline_id,
                "project_id": project_id,
                "bucket_name": bucket_name,
                "bucket_region": bucket_region,
                "lb_id": lb_id,
            },
        )

    async def create_backend_stage(
        self,
        *,
        project_id: Optional[str] = None,
        scaleway_s3: Optional[ScalewayS3BackendConfig] = None,
        scaleway_lb: Optional[ScalewayLbBackendConfig] = None,
    ) -> BackendStage:
        """
        Create backend stage.
        Create a new backend stage. You must specify either a `scaleway_s3` (for a Scaleway Object Storage bucket) or `scaleway_lb` (for a Scaleway Load Balancer) field to configure the origin.
        :param project_id: Project ID in which the backend stage will be created.
        :param scaleway_s3: Scaleway Object Storage origin bucket (S3) linked to the backend stage.
        One-Of ('backend_config'): at most one of 'scaleway_s3', 'scaleway_lb' could be set.
        :param scaleway_lb: Scaleway Load Balancer origin linked to the backend stage.
        One-Of ('backend_config'): at most one of 'scaleway_s3', 'scaleway_lb' could be set.
        :return: :class:`BackendStage <BackendStage>`

        Usage:
        ::

            result = await api.create_backend_stage()
        """

        res = self._request(
            "POST",
            "/edge-services/v1alpha1/backend-stages",
            body=marshal_CreateBackendStageRequest(
                CreateBackendStageRequest(
                    project_id=project_id,
                    scaleway_s3=scaleway_s3,
                    scaleway_lb=scaleway_lb,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_BackendStage(res.json())

    async def get_backend_stage(
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

            result = await api.get_backend_stage(
                backend_stage_id="example",
            )
        """

        param_backend_stage_id = validate_path_param(
            "backend_stage_id", backend_stage_id
        )

        res = self._request(
            "GET",
            f"/edge-services/v1alpha1/backend-stages/{param_backend_stage_id}",
        )

        self._throw_on_error(res)
        return unmarshal_BackendStage(res.json())

    async def update_backend_stage(
        self,
        *,
        backend_stage_id: str,
        scaleway_s3: Optional[ScalewayS3BackendConfig] = None,
        scaleway_lb: Optional[ScalewayLbBackendConfig] = None,
    ) -> BackendStage:
        """
        Update backend stage.
        Update the parameters of an existing backend stage, specified by its `backend_stage_id`.
        :param backend_stage_id: ID of the backend stage to update.
        :param scaleway_s3: Scaleway Object Storage origin bucket (S3) linked to the backend stage.
        One-Of ('backend_config'): at most one of 'scaleway_s3', 'scaleway_lb' could be set.
        :param scaleway_lb: Scaleway Load Balancer origin linked to the backend stage.
        One-Of ('backend_config'): at most one of 'scaleway_s3', 'scaleway_lb' could be set.
        :return: :class:`BackendStage <BackendStage>`

        Usage:
        ::

            result = await api.update_backend_stage(
                backend_stage_id="example",
            )
        """

        param_backend_stage_id = validate_path_param(
            "backend_stage_id", backend_stage_id
        )

        res = self._request(
            "PATCH",
            f"/edge-services/v1alpha1/backend-stages/{param_backend_stage_id}",
            body=marshal_UpdateBackendStageRequest(
                UpdateBackendStageRequest(
                    backend_stage_id=backend_stage_id,
                    scaleway_s3=scaleway_s3,
                    scaleway_lb=scaleway_lb,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_BackendStage(res.json())

    async def delete_backend_stage(
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

            result = await api.delete_backend_stage(
                backend_stage_id="example",
            )
        """

        param_backend_stage_id = validate_path_param(
            "backend_stage_id", backend_stage_id
        )

        res = self._request(
            "DELETE",
            f"/edge-services/v1alpha1/backend-stages/{param_backend_stage_id}",
        )

        self._throw_on_error(res)

    async def check_domain(
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

            result = await api.check_domain(
                fqdn="example",
                cname="example",
            )
        """

        res = self._request(
            "POST",
            "/edge-services/v1alpha1/check-domain",
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

    async def check_pem_chain(
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

            result = await api.check_pem_chain(
                fqdn="example",
            )
        """

        res = self._request(
            "POST",
            "/edge-services/v1alpha1/check-pem-chain",
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

    async def list_purge_requests(
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
        :param organization_id: Organization ID to filter for, only purge requests from this Project will be returned.
        :param project_id: Project ID to filter for, only purge requests from this Project will be returned.
        :param pipeline_id: Pipeline ID to filter for, only purge requests from this pipeline will be returned.
        :return: :class:`ListPurgeRequestsResponse <ListPurgeRequestsResponse>`

        Usage:
        ::

            result = await api.list_purge_requests()
        """

        res = self._request(
            "GET",
            "/edge-services/v1alpha1/purge-requests",
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

    async def list_purge_requests_all(
        self,
        *,
        order_by: Optional[ListPurgeRequestsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        pipeline_id: Optional[str] = None,
    ) -> List[PurgeRequest]:
        """
        List purge requests.
        List all purge requests, for a Scaleway Organization or Scaleway Project. This enables you to retrieve a history of all previously-made purge requests. By default, the purge requests returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param order_by: Sort order of purge requests in the response.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of purge requests to return per page.
        :param organization_id: Organization ID to filter for, only purge requests from this Project will be returned.
        :param project_id: Project ID to filter for, only purge requests from this Project will be returned.
        :param pipeline_id: Pipeline ID to filter for, only purge requests from this pipeline will be returned.
        :return: :class:`List[PurgeRequest] <List[PurgeRequest]>`

        Usage:
        ::

            result = await api.list_purge_requests_all()
        """

        return await fetch_all_pages_async(
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

    async def create_purge_request(
        self,
        *,
        pipeline_id: str,
        assets: Optional[List[str]] = None,
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

            result = await api.create_purge_request(
                pipeline_id="example",
            )
        """

        res = self._request(
            "POST",
            "/edge-services/v1alpha1/purge-requests",
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

    async def get_purge_request(
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

            result = await api.get_purge_request(
                purge_request_id="example",
            )
        """

        param_purge_request_id = validate_path_param(
            "purge_request_id", purge_request_id
        )

        res = self._request(
            "GET",
            f"/edge-services/v1alpha1/purge-requests/{param_purge_request_id}",
        )

        self._throw_on_error(res)
        return unmarshal_PurgeRequest(res.json())

    async def wait_for_purge_request(
        self,
        *,
        purge_request_id: str,
        options: Optional[
            WaitForOptions[PurgeRequest, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> PurgeRequest:
        """
        Get purge request.
        Retrieve information about a purge request, specified by its `purge_request_id`. Its full details, including `status` and `target`, are returned in the response object.
        :param purge_request_id: ID of the requested purge request.
        :return: :class:`PurgeRequest <PurgeRequest>`

        Usage:
        ::

            result = await api.get_purge_request(
                purge_request_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = (
                lambda res: res.status not in PURGE_REQUEST_TRANSIENT_STATUSES
            )

        return await wait_for_resource_async(
            fetcher=self.get_purge_request,
            options=options,
            args={
                "purge_request_id": purge_request_id,
            },
        )

    async def check_lb_origin(
        self,
        *,
        lb: Optional[ScalewayLb] = None,
    ) -> CheckLbOriginResponse:
        """
        :param lb:
        :return: :class:`CheckLbOriginResponse <CheckLbOriginResponse>`

        Usage:
        ::

            result = await api.check_lb_origin()
        """

        res = self._request(
            "POST",
            "/edge-services/v1alpha1/check-lb-origin",
            body=marshal_CheckLbOriginRequest(
                CheckLbOriginRequest(
                    lb=lb,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CheckLbOriginResponse(res.json())
