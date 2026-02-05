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


class DatalabStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    CREATING = "creating"
    UPDATING = "updating"
    READY = "ready"
    ERROR = "error"
    DELETING = "deleting"
    LOCKED = "locked"
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)


class ListClusterVersionsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListDatalabsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListNodeTypesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    VCPUS_ASC = "vcpus_asc"
    VCPUS_DESC = "vcpus_desc"
    MEMORY_GIGABYTES_ASC = "memory_gigabytes_asc"
    MEMORY_GIGABYTES_DESC = "memory_gigabytes_desc"
    VRAM_BYTES_ASC = "vram_bytes_asc"
    VRAM_BYTES_DESC = "vram_bytes_desc"
    GPUS_ASC = "gpus_asc"
    GPUS_DESC = "gpus_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListNodeTypesRequestResourceType(str, Enum, metaclass=StrEnumMeta):
    ALL = "all"
    GPU = "gpu"
    CPU = "cpu"

    def __str__(self) -> str:
        return str(self.value)


class ListNotebookVersionsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class NodeTypeStock(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STOCK = "unknown_stock"
    LOW_STOCK = "low_stock"
    OUT_OF_STOCK = "out_of_stock"
    AVAILABLE = "available"

    def __str__(self) -> str:
        return str(self.value)


class NodeTypeTarget(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TARGET = "unknown_target"
    NOTEBOOK = "notebook"
    WORKER = "worker"

    def __str__(self) -> str:
        return str(self.value)


class VolumeType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    SBS_5K = "sbs_5k"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Volume:
    type_: VolumeType
    size: int


@dataclass
class ClusterVersion:
    """
    A cluster version.
    """

    version: str
    """
    The version of the cluster.
    """

    disabled: bool
    """
    Whether the cluster version is disabled.
    """

    beta: bool
    """
    Whether the cluster version is in beta.
    """

    end_of_life: Optional[datetime] = None
    """
    The end of life date of the cluster version.
    """

    created_at: Optional[datetime] = None
    """
    The creation date of the cluster version.
    """

    updated_at: Optional[datetime] = None
    """
    The last update date of the cluster version.
    """


@dataclass
class DatalabSparkMain:
    node_type: str
    spark_ui_url: str
    spark_master_url: str
    root_volume: Optional[Volume] = None


@dataclass
class DatalabSparkWorker:
    node_type: str
    node_count: int
    root_volume: Optional[Volume] = None


@dataclass
class NotebookVersion:
    """
    A notebook version.
    """

    version: str
    """
    The version of the notebook.
    """

    disabled: bool
    """
    Whether the notebook version is disabled.
    """

    beta: bool
    """
    Whether the notebook version is in beta.
    """

    end_of_life: Optional[datetime] = None
    """
    The end of life date of the notebook version.
    """

    created_at: Optional[datetime] = None
    """
    The creation date of the notebook version.
    """

    updated_at: Optional[datetime] = None
    """
    The last update date of the notebook version.
    """


@dataclass
class CreateDatalabRequestSparkMain:
    node_type: str


@dataclass
class CreateDatalabRequestSparkWorker:
    node_type: str
    node_count: int


@dataclass
class Cluster:
    """
    A cluster.
    """

    name: str
    """
    The name of the cluster.
    """

    description: str
    """
    The description of the cluster.
    """

    versions: list[ClusterVersion]
    """
    The versions of the cluster.
    """


@dataclass
class Datalab:
    """
    A Data Lab resource.
    """

    id: str
    """
    The unique identifier of the Data Lab.
    """

    project_id: str
    """
    The unique identifier of the project where the Data Lab has been created.
    """

    name: str
    """
    The name of the Data Lab.
    """

    description: str
    """
    The description of the Data Lab.
    """

    tags: list[str]
    """
    The tags of the Data Lab.
    """

    status: DatalabStatus
    """
    The status of the Data Lab. For a working Data Lab the status is marked as `ready`.
    """

    region: ScwRegion
    """
    The region of the Data Lab.
    """

    has_notebook: bool
    """
    Whether a JupyterLab notebook is associated with the Data Lab or not.
    """

    spark_version: str
    """
    The version of Spark running inside the Data Lab.
    """

    private_network_id: str
    """
    The unique identifier of the private network to which the Data Lab is attached to.
    """

    main: Optional[DatalabSparkMain] = None
    """
    The Spark Main node specification of Data lab. It holds the parameters `node_type`, `spark_ui_url` (available to reach Spark UI), `spark_master_url` (used to reach the cluster within a VPC), `root_volume` (size of the volume assigned to the cluster).
    """

    worker: Optional[DatalabSparkWorker] = None
    """
    The cluster worker nodes specification. It holds the parameters `node_type`, `node_count`, `root_volume` (size of the volume assigned to the cluster).
    """

    created_at: Optional[datetime] = None
    """
    The creation timestamp of the Data Lab.
    """

    updated_at: Optional[datetime] = None
    """
    The last update date of the Data Lab.
    """

    notebook_url: Optional[str] = None
    """
    The URL of the notebook if available.
    """

    total_storage: Optional[Volume] = None
    """
    The total persistent volume storage selected to run Spark.
    """

    notebook_master_url: Optional[str] = None
    """
    The URL that is used to reach the cluster from the notebook when available. This URL cannot be used to reach the cluster from a server.
    """


@dataclass
class NodeType:
    """
    A node type.
    """

    stock_status: NodeTypeStock
    """
    The stock status of the node type.
    """

    name: str
    """
    The name of the node type.
    """

    description: str
    """
    The description of the node type.
    """

    vcpus: int
    """
    The number of vCPUs.
    """

    memory_gigabytes: int
    """
    The amount of memory.
    """

    vram_gigabytes: int
    """
    The amount of VRAM.
    """

    gpus: int
    """
    The number of GPUs.
    """

    disabled: bool
    """
    Whether the node type is disabled.
    """

    beta: bool
    """
    Whether the node type is in beta.
    """

    targets: list[NodeTypeTarget]
    """
    The targets of the node type.
    """

    created_at: Optional[datetime] = None
    """
    The creation date of the node type.
    """

    updated_at: Optional[datetime] = None
    """
    The last update date of the node type.
    """


@dataclass
class Notebook:
    """
    A notebook.
    """

    name: str
    """
    The name of the notebook.
    """

    description: str
    """
    The description of the notebook.
    """

    versions: list[NotebookVersion]
    """
    The versions of the notebook.
    """


@dataclass
class CreateDatalabRequest:
    """
    A request to create a Data Lab.
    """

    name: str
    """
    The name of the Data Lab.
    """

    description: str
    """
    The description of the Data Lab.
    """

    has_notebook: bool
    """
    Select this option to include a notebook as part of the Data Lab.
    """

    spark_version: str
    """
    The version of Spark running inside the Data Lab, available options can be viewed at ListClusterVersions.
    """

    private_network_id: str
    """
    The unique identifier of the private network the Data Lab will be attached to.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    The unique identifier of the project where the Data Lab will be created.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    The tags of the Data Lab.
    """

    main: Optional[CreateDatalabRequestSparkMain] = None
    """
    The cluster main node specification. It holds the parameters `node_type` which specifies the node type of the main node. See ListNodeTypes for available options. See ListNodeTypes for available options.
    """

    worker: Optional[CreateDatalabRequestSparkWorker] = None
    """
    The cluster worker node specification. It holds the parameters `node_type` which specifies the node type of the worker node and `node_count` for specifying the amount of nodes.
    """

    total_storage: Optional[Volume] = None
    """
    The maximum persistent volume storage that will be available during workload.
    """


@dataclass
class DeleteDatalabRequest:
    """
    A request to delete a Data Lab.
    """

    datalab_id: str
    """
    The unique identifier of the Data Lab.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetDatalabRequest:
    """
    A request to get information about a Data Lab.
    """

    datalab_id: str
    """
    The unique identifier of the Data Lab.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListClusterVersionsRequest:
    """
    A request to list cluster versions.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    The page number.
    """

    page_size: Optional[int] = 0
    """
    The page size.
    """

    order_by: Optional[ListClusterVersionsRequestOrderBy] = (
        ListClusterVersionsRequestOrderBy.NAME_ASC
    )
    """
    The order by field.
    """


@dataclass
class ListClusterVersionsResponse:
    """
    A response to list cluster versions.
    """

    clusters: list[Cluster]
    """
    The list of cluster versions.
    """

    total_count: int
    """
    The total count of cluster versions.
    """


@dataclass
class ListDatalabsRequest:
    """
    A request to list Data Labs.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str] = None
    """
    The unique identifier of the organization whose Data Labs you want to list.
    """

    project_id: Optional[str] = None
    """
    The unique identifier of the project whose Data Labs you want to list.
    """

    name: Optional[str] = None
    """
    The name of the Data Lab you want to list.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    The tags associated with the Data Lab you want to list.
    """

    page: Optional[int] = 0
    """
    The page number for pagination.
    """

    page_size: Optional[int] = 0
    """
    The page size for pagination.
    """

    order_by: Optional[ListDatalabsRequestOrderBy] = ListDatalabsRequestOrderBy.NAME_ASC
    """
    The order by field, available options are `name_asc`, `name_desc`, `created_at_asc`, `created_at_desc`, `updated_at_asc`, `updated_at_desc`.
    """


@dataclass
class ListDatalabsResponse:
    """
    A response to list Data Labs.
    """

    datalabs: list[Datalab]
    """
    The list of Data Labs. This is a list composed of messages of type `DataLab`.
    """

    total_count: int
    """
    The total count of Data Labs.
    """


@dataclass
class ListNodeTypesRequest:
    """
    A request to list node types.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    The page number.
    """

    page_size: Optional[int] = 0
    """
    The page size.
    """

    order_by: Optional[ListNodeTypesRequestOrderBy] = (
        ListNodeTypesRequestOrderBy.NAME_ASC
    )
    """
    The order by field. Available fields are `name_asc`, `name_desc`, `vcpus_asc`, `vcpus_desc`, `memory_gigabytes_asc`, `memory_gigabytes_desc`, `vram_bytes_asc`, `vram_bytes_desc`, `gpus_asc`, `gpus_desc`.
    """

    targets: Optional[list[NodeTypeTarget]] = field(default_factory=list)
    """
    Filter based on the target of the nodes. Allows to filter the nodes based on their purpose which can be main or worker node.
    """

    resource_type: Optional[ListNodeTypesRequestResourceType] = (
        ListNodeTypesRequestResourceType.ALL
    )
    """
    Filter based on node type ( `cpu`/`gpu`/`all` ).
    """


@dataclass
class ListNodeTypesResponse:
    """
    A response to list node types.
    """

    node_types: list[NodeType]
    """
    The list of node types.
    """

    total_count: int
    """
    The total count of node types.
    """


@dataclass
class ListNotebookVersionsRequest:
    """
    A request to list notebook versions.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    The page number.
    """

    page_size: Optional[int] = 0
    """
    The page size.
    """

    order_by: Optional[ListNotebookVersionsRequestOrderBy] = (
        ListNotebookVersionsRequestOrderBy.NAME_ASC
    )
    """
    The order by field. Available options are `name_asc` and `name_desc`.
    """


@dataclass
class ListNotebookVersionsResponse:
    """
    A response to list notebook versions.
    """

    notebooks: list[Notebook]
    """
    The list of notebook versions.
    """

    total_count: int
    """
    The total count of notebook versions.
    """


@dataclass
class UpdateDatalabRequest:
    """
    A request to update a Data Lab.
    """

    datalab_id: str
    """
    The unique identifier of the Data Lab.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    The updated name of the Data Lab.
    """

    description: Optional[str] = None
    """
    The updated description of the Data Lab.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    The updated tags of the Data Lab.
    """

    node_count: Optional[int] = 0
    """
    The updated node count of the Data Lab. Scale up or down the number of worker nodes.
    """
