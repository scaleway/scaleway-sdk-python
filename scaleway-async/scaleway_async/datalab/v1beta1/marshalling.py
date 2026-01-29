# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    DatalabStatus,
    NodeTypeStock,
    NodeTypeTarget,
    Volume,
    DatalabSparkMain,
    DatalabSparkWorker,
    Datalab,
    ClusterVersion,
    Cluster,
    ListClusterVersionsResponse,
    ListDatalabsResponse,
    NodeType,
    ListNodeTypesResponse,
    NotebookVersion,
    Notebook,
    ListNotebookVersionsResponse,
    CreateDatalabRequestSparkMain,
    CreateDatalabRequestSparkWorker,
    CreateDatalabRequest,
    UpdateDatalabRequest,
)


def unmarshal_Volume(data: Any) -> Volume:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Volume' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = None

    return Volume(**args)


def unmarshal_DatalabSparkMain(data: Any) -> DatalabSparkMain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DatalabSparkMain' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("node_type", None)
    if field is not None:
        args["node_type"] = field
    else:
        args["node_type"] = None

    field = data.get("spark_ui_url", None)
    if field is not None:
        args["spark_ui_url"] = field
    else:
        args["spark_ui_url"] = None

    field = data.get("spark_master_url", None)
    if field is not None:
        args["spark_master_url"] = field
    else:
        args["spark_master_url"] = None

    field = data.get("root_volume", None)
    if field is not None:
        args["root_volume"] = unmarshal_Volume(field)
    else:
        args["root_volume"] = None

    return DatalabSparkMain(**args)


def unmarshal_DatalabSparkWorker(data: Any) -> DatalabSparkWorker:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DatalabSparkWorker' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("node_type", None)
    if field is not None:
        args["node_type"] = field
    else:
        args["node_type"] = None

    field = data.get("node_count", None)
    if field is not None:
        args["node_count"] = field
    else:
        args["node_count"] = None

    field = data.get("root_volume", None)
    if field is not None:
        args["root_volume"] = unmarshal_Volume(field)
    else:
        args["root_volume"] = None

    return DatalabSparkWorker(**args)


def unmarshal_Datalab(data: Any) -> Datalab:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Datalab' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DatalabStatus.UNKNOWN_STATUS

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("has_notebook", None)
    if field is not None:
        args["has_notebook"] = field
    else:
        args["has_notebook"] = False

    field = data.get("main", None)
    if field is not None:
        args["main"] = unmarshal_DatalabSparkMain(field)
    else:
        args["main"] = None

    field = data.get("worker", None)
    if field is not None:
        args["worker"] = unmarshal_DatalabSparkWorker(field)
    else:
        args["worker"] = None

    field = data.get("spark_version", None)
    if field is not None:
        args["spark_version"] = field
    else:
        args["spark_version"] = None

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field
    else:
        args["private_network_id"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("notebook_url", None)
    if field is not None:
        args["notebook_url"] = field
    else:
        args["notebook_url"] = None

    field = data.get("total_storage", None)
    if field is not None:
        args["total_storage"] = unmarshal_Volume(field)
    else:
        args["total_storage"] = None

    field = data.get("notebook_master_url", None)
    if field is not None:
        args["notebook_master_url"] = field
    else:
        args["notebook_master_url"] = None

    return Datalab(**args)


def unmarshal_ClusterVersion(data: Any) -> ClusterVersion:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ClusterVersion' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("version", None)
    if field is not None:
        args["version"] = field
    else:
        args["version"] = None

    field = data.get("disabled", None)
    if field is not None:
        args["disabled"] = field
    else:
        args["disabled"] = False

    field = data.get("beta", None)
    if field is not None:
        args["beta"] = field
    else:
        args["beta"] = False

    field = data.get("end_of_life", None)
    if field is not None:
        args["end_of_life"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["end_of_life"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return ClusterVersion(**args)


def unmarshal_Cluster(data: Any) -> Cluster:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Cluster' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("versions", None)
    if field is not None:
        args["versions"] = (
            [unmarshal_ClusterVersion(v) for v in field] if field is not None else None
        )
    else:
        args["versions"] = []

    return Cluster(**args)


def unmarshal_ListClusterVersionsResponse(data: Any) -> ListClusterVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListClusterVersionsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("clusters", None)
    if field is not None:
        args["clusters"] = (
            [unmarshal_Cluster(v) for v in field] if field is not None else None
        )
    else:
        args["clusters"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListClusterVersionsResponse(**args)


def unmarshal_ListDatalabsResponse(data: Any) -> ListDatalabsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatalabsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("datalabs", None)
    if field is not None:
        args["datalabs"] = (
            [unmarshal_Datalab(v) for v in field] if field is not None else None
        )
    else:
        args["datalabs"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListDatalabsResponse(**args)


def unmarshal_NodeType(data: Any) -> NodeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeType' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("stock_status", None)
    if field is not None:
        args["stock_status"] = field
    else:
        args["stock_status"] = NodeTypeStock.UNKNOWN_STOCK

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("vcpus", None)
    if field is not None:
        args["vcpus"] = field
    else:
        args["vcpus"] = 0

    field = data.get("memory_gigabytes", None)
    if field is not None:
        args["memory_gigabytes"] = field
    else:
        args["memory_gigabytes"] = 0

    field = data.get("vram_gigabytes", None)
    if field is not None:
        args["vram_gigabytes"] = field
    else:
        args["vram_gigabytes"] = 0

    field = data.get("gpus", None)
    if field is not None:
        args["gpus"] = field
    else:
        args["gpus"] = 0

    field = data.get("disabled", None)
    if field is not None:
        args["disabled"] = field
    else:
        args["disabled"] = False

    field = data.get("beta", None)
    if field is not None:
        args["beta"] = field
    else:
        args["beta"] = False

    field = data.get("targets", None)
    if field is not None:
        args["targets"] = (
            [NodeTypeTarget(v) for v in field] if field is not None else None
        )
    else:
        args["targets"] = []

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return NodeType(**args)


def unmarshal_ListNodeTypesResponse(data: Any) -> ListNodeTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNodeTypesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("node_types", None)
    if field is not None:
        args["node_types"] = (
            [unmarshal_NodeType(v) for v in field] if field is not None else None
        )
    else:
        args["node_types"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListNodeTypesResponse(**args)


def unmarshal_NotebookVersion(data: Any) -> NotebookVersion:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NotebookVersion' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("version", None)
    if field is not None:
        args["version"] = field
    else:
        args["version"] = None

    field = data.get("disabled", None)
    if field is not None:
        args["disabled"] = field
    else:
        args["disabled"] = False

    field = data.get("beta", None)
    if field is not None:
        args["beta"] = field
    else:
        args["beta"] = False

    field = data.get("end_of_life", None)
    if field is not None:
        args["end_of_life"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["end_of_life"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return NotebookVersion(**args)


def unmarshal_Notebook(data: Any) -> Notebook:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Notebook' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("versions", None)
    if field is not None:
        args["versions"] = (
            [unmarshal_NotebookVersion(v) for v in field] if field is not None else None
        )
    else:
        args["versions"] = []

    return Notebook(**args)


def unmarshal_ListNotebookVersionsResponse(data: Any) -> ListNotebookVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNotebookVersionsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("notebooks", None)
    if field is not None:
        args["notebooks"] = (
            [unmarshal_Notebook(v) for v in field] if field is not None else None
        )
    else:
        args["notebooks"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListNotebookVersionsResponse(**args)


def marshal_CreateDatalabRequestSparkMain(
    request: CreateDatalabRequestSparkMain,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.node_type is not None:
        output["node_type"] = request.node_type

    return output


def marshal_CreateDatalabRequestSparkWorker(
    request: CreateDatalabRequestSparkWorker,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.node_type is not None:
        output["node_type"] = request.node_type

    if request.node_count is not None:
        output["node_count"] = request.node_count

    return output


def marshal_Volume(
    request: Volume,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    if request.size is not None:
        output["size"] = request.size

    return output


def marshal_CreateDatalabRequest(
    request: CreateDatalabRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.has_notebook is not None:
        output["has_notebook"] = request.has_notebook

    if request.spark_version is not None:
        output["spark_version"] = request.spark_version

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.main is not None:
        output["main"] = marshal_CreateDatalabRequestSparkMain(request.main, defaults)

    if request.worker is not None:
        output["worker"] = marshal_CreateDatalabRequestSparkWorker(
            request.worker, defaults
        )

    if request.total_storage is not None:
        output["total_storage"] = marshal_Volume(request.total_storage, defaults)

    return output


def marshal_UpdateDatalabRequest(
    request: UpdateDatalabRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.tags is not None:
        output["tags"] = request.tags

    if request.node_count is not None:
        output["node_count"] = request.node_count

    return output
