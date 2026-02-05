# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    WaitForOptions,
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    ListClusterVersionsRequestOrderBy,
    ListDatalabsRequestOrderBy,
    ListNodeTypesRequestOrderBy,
    ListNodeTypesRequestResourceType,
    ListNotebookVersionsRequestOrderBy,
    NodeTypeTarget,
    Cluster,
    CreateDatalabRequest,
    CreateDatalabRequestSparkMain,
    CreateDatalabRequestSparkWorker,
    Datalab,
    ListClusterVersionsResponse,
    ListDatalabsResponse,
    ListNodeTypesResponse,
    ListNotebookVersionsResponse,
    NodeType,
    Notebook,
    UpdateDatalabRequest,
    Volume,
)
from .content import (
    DATALAB_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Datalab,
    unmarshal_ListClusterVersionsResponse,
    unmarshal_ListDatalabsResponse,
    unmarshal_ListNodeTypesResponse,
    unmarshal_ListNotebookVersionsResponse,
    marshal_CreateDatalabRequest,
    marshal_UpdateDatalabRequest,
)


class DatalabV1Beta1API(API):
    """
    This API allows you to manage your Data Lab resources.
    """

    async def create_datalab(
        self,
        *,
        name: str,
        description: str,
        has_notebook: bool,
        spark_version: str,
        private_network_id: str,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
        main: Optional[CreateDatalabRequestSparkMain] = None,
        worker: Optional[CreateDatalabRequestSparkWorker] = None,
        total_storage: Optional[Volume] = None,
    ) -> Datalab:
        """
        Create a new Data Lab. In this call, one can personalize the node counts, add a notebook, choose the private network, define the persistent volume storage capacity.
        :param name: The name of the Data Lab.
        :param description: The description of the Data Lab.
        :param has_notebook: Select this option to include a notebook as part of the Data Lab.
        :param spark_version: The version of Spark running inside the Data Lab, available options can be viewed at ListClusterVersions.
        :param private_network_id: The unique identifier of the private network the Data Lab will be attached to.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: The unique identifier of the project where the Data Lab will be created.
        :param tags: The tags of the Data Lab.
        :param main: The cluster main node specification. It holds the parameters `node_type` which specifies the node type of the main node. See ListNodeTypes for available options. See ListNodeTypes for available options.
        :param worker: The cluster worker node specification. It holds the parameters `node_type` which specifies the node type of the worker node and `node_count` for specifying the amount of nodes.
        :param total_storage: The maximum persistent volume storage that will be available during workload.
        :return: :class:`Datalab <Datalab>`

        Usage:
        ::

            result = await api.create_datalab(
                name="example",
                description="example",
                has_notebook=False,
                spark_version="example",
                private_network_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/datalab/v1beta1/regions/{param_region}/datalabs",
            body=marshal_CreateDatalabRequest(
                CreateDatalabRequest(
                    name=name,
                    description=description,
                    has_notebook=has_notebook,
                    spark_version=spark_version,
                    private_network_id=private_network_id,
                    region=region,
                    project_id=project_id,
                    tags=tags,
                    main=main,
                    worker=worker,
                    total_storage=total_storage,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Datalab(res.json())

    async def get_datalab(
        self,
        *,
        datalab_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Datalab:
        """
        Retrieve information about a given Data Lab cluster, specified by the `region` and `datalab_id` parameters. Its full details, including name, status, node counts, are returned in the response object.
        :param datalab_id: The unique identifier of the Data Lab.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Datalab <Datalab>`

        Usage:
        ::

            result = await api.get_datalab(
                datalab_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_datalab_id = validate_path_param("datalab_id", datalab_id)

        res = self._request(
            "GET",
            f"/datalab/v1beta1/regions/{param_region}/datalabs/{param_datalab_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Datalab(res.json())

    async def wait_for_datalab(
        self,
        *,
        datalab_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[WaitForOptions[Datalab, Union[bool, Awaitable[bool]]]] = None,
    ) -> Datalab:
        """
        Retrieve information about a given Data Lab cluster, specified by the `region` and `datalab_id` parameters. Its full details, including name, status, node counts, are returned in the response object.
        :param datalab_id: The unique identifier of the Data Lab.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Datalab <Datalab>`

        Usage:
        ::

            result = await api.get_datalab(
                datalab_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in DATALAB_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_datalab,
            options=options,
            args={
                "datalab_id": datalab_id,
                "region": region,
            },
        )

    async def list_datalabs(
        self,
        *,
        region: Optional[ScwRegion] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDatalabsRequestOrderBy] = None,
    ) -> ListDatalabsResponse:
        """
        List information about Data Lab cluster within a project or an organization.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: The unique identifier of the organization whose Data Labs you want to list.
        :param project_id: The unique identifier of the project whose Data Labs you want to list.
        :param name: The name of the Data Lab you want to list.
        :param tags: The tags associated with the Data Lab you want to list.
        :param page: The page number for pagination.
        :param page_size: The page size for pagination.
        :param order_by: The order by field, available options are `name_asc`, `name_desc`, `created_at_asc`, `created_at_desc`, `updated_at_asc`, `updated_at_desc`.
        :return: :class:`ListDatalabsResponse <ListDatalabsResponse>`

        Usage:
        ::

            result = await api.list_datalabs()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/datalab/v1beta1/regions/{param_region}/datalabs",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDatalabsResponse(res.json())

    async def list_datalabs_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDatalabsRequestOrderBy] = None,
    ) -> list[Datalab]:
        """
        List information about Data Lab cluster within a project or an organization.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: The unique identifier of the organization whose Data Labs you want to list.
        :param project_id: The unique identifier of the project whose Data Labs you want to list.
        :param name: The name of the Data Lab you want to list.
        :param tags: The tags associated with the Data Lab you want to list.
        :param page: The page number for pagination.
        :param page_size: The page size for pagination.
        :param order_by: The order by field, available options are `name_asc`, `name_desc`, `created_at_asc`, `created_at_desc`, `updated_at_asc`, `updated_at_desc`.
        :return: :class:`list[Datalab] <list[Datalab]>`

        Usage:
        ::

            result = await api.list_datalabs_all()
        """

        return await fetch_all_pages_async(
            type=ListDatalabsResponse,
            key="datalabs",
            fetcher=self.list_datalabs,
            args={
                "region": region,
                "organization_id": organization_id,
                "project_id": project_id,
                "name": name,
                "tags": tags,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def update_datalab(
        self,
        *,
        datalab_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[list[str]] = None,
        node_count: Optional[int] = None,
    ) -> Datalab:
        """
        Update a Data Labs node counts. Allows for up- and downscaling on demand, depending on the expected workload.
        :param datalab_id: The unique identifier of the Data Lab.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: The updated name of the Data Lab.
        :param description: The updated description of the Data Lab.
        :param tags: The updated tags of the Data Lab.
        :param node_count: The updated node count of the Data Lab. Scale up or down the number of worker nodes.
        :return: :class:`Datalab <Datalab>`

        Usage:
        ::

            result = await api.update_datalab(
                datalab_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_datalab_id = validate_path_param("datalab_id", datalab_id)

        res = self._request(
            "PATCH",
            f"/datalab/v1beta1/regions/{param_region}/datalabs/{param_datalab_id}",
            body=marshal_UpdateDatalabRequest(
                UpdateDatalabRequest(
                    datalab_id=datalab_id,
                    region=region,
                    name=name,
                    description=description,
                    tags=tags,
                    node_count=node_count,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Datalab(res.json())

    async def delete_datalab(
        self,
        *,
        datalab_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Datalab:
        """
        Delete a Data Lab based on its region and id.
        :param datalab_id: The unique identifier of the Data Lab.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Datalab <Datalab>`

        Usage:
        ::

            result = await api.delete_datalab(
                datalab_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_datalab_id = validate_path_param("datalab_id", datalab_id)

        res = self._request(
            "DELETE",
            f"/datalab/v1beta1/regions/{param_region}/datalabs/{param_datalab_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Datalab(res.json())

    async def list_node_types(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNodeTypesRequestOrderBy] = None,
        targets: Optional[list[NodeTypeTarget]] = None,
        resource_type: Optional[ListNodeTypesRequestResourceType] = None,
    ) -> ListNodeTypesResponse:
        """
        List the available compute node types for creating a Data Lab.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: The page number.
        :param page_size: The page size.
        :param order_by: The order by field. Available fields are `name_asc`, `name_desc`, `vcpus_asc`, `vcpus_desc`, `memory_gigabytes_asc`, `memory_gigabytes_desc`, `vram_bytes_asc`, `vram_bytes_desc`, `gpus_asc`, `gpus_desc`.
        :param targets: Filter based on the target of the nodes. Allows to filter the nodes based on their purpose which can be main or worker node.
        :param resource_type: Filter based on node type ( `cpu`/`gpu`/`all` ).
        :return: :class:`ListNodeTypesResponse <ListNodeTypesResponse>`

        Usage:
        ::

            result = await api.list_node_types()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/datalab/v1beta1/regions/{param_region}/node-types",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "resource_type": resource_type,
                "targets": targets,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListNodeTypesResponse(res.json())

    async def list_node_types_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNodeTypesRequestOrderBy] = None,
        targets: Optional[list[NodeTypeTarget]] = None,
        resource_type: Optional[ListNodeTypesRequestResourceType] = None,
    ) -> list[NodeType]:
        """
        List the available compute node types for creating a Data Lab.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: The page number.
        :param page_size: The page size.
        :param order_by: The order by field. Available fields are `name_asc`, `name_desc`, `vcpus_asc`, `vcpus_desc`, `memory_gigabytes_asc`, `memory_gigabytes_desc`, `vram_bytes_asc`, `vram_bytes_desc`, `gpus_asc`, `gpus_desc`.
        :param targets: Filter based on the target of the nodes. Allows to filter the nodes based on their purpose which can be main or worker node.
        :param resource_type: Filter based on node type ( `cpu`/`gpu`/`all` ).
        :return: :class:`list[NodeType] <list[NodeType]>`

        Usage:
        ::

            result = await api.list_node_types_all()
        """

        return await fetch_all_pages_async(
            type=ListNodeTypesResponse,
            key="node_types",
            fetcher=self.list_node_types,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "targets": targets,
                "resource_type": resource_type,
            },
        )

    async def list_notebook_versions(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNotebookVersionsRequestOrderBy] = None,
    ) -> ListNotebookVersionsResponse:
        """
        Lists available notebook versions.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: The page number.
        :param page_size: The page size.
        :param order_by: The order by field. Available options are `name_asc` and `name_desc`.
        :return: :class:`ListNotebookVersionsResponse <ListNotebookVersionsResponse>`

        Usage:
        ::

            result = await api.list_notebook_versions()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/datalab/v1beta1/regions/{param_region}/notebook-versions",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListNotebookVersionsResponse(res.json())

    async def list_notebook_versions_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNotebookVersionsRequestOrderBy] = None,
    ) -> list[Notebook]:
        """
        Lists available notebook versions.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: The page number.
        :param page_size: The page size.
        :param order_by: The order by field. Available options are `name_asc` and `name_desc`.
        :return: :class:`list[Notebook] <list[Notebook]>`

        Usage:
        ::

            result = await api.list_notebook_versions_all()
        """

        return await fetch_all_pages_async(
            type=ListNotebookVersionsResponse,
            key="notebooks",
            fetcher=self.list_notebook_versions,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def list_cluster_versions(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListClusterVersionsRequestOrderBy] = None,
    ) -> ListClusterVersionsResponse:
        """
        List the Spark versions the product is compatible with.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: The page number.
        :param page_size: The page size.
        :param order_by: The order by field.
        :return: :class:`ListClusterVersionsResponse <ListClusterVersionsResponse>`

        Usage:
        ::

            result = await api.list_cluster_versions()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/datalab/v1beta1/regions/{param_region}/cluster-versions",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListClusterVersionsResponse(res.json())

    async def list_cluster_versions_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListClusterVersionsRequestOrderBy] = None,
    ) -> list[Cluster]:
        """
        List the Spark versions the product is compatible with.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: The page number.
        :param page_size: The page size.
        :param order_by: The order by field.
        :return: :class:`list[Cluster] <list[Cluster]>`

        Usage:
        ::

            result = await api.list_cluster_versions_all()
        """

        return await fetch_all_pages_async(
            type=ListClusterVersionsResponse,
            key="clusters",
            fetcher=self.list_cluster_versions,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )
