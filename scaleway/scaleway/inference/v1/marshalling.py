# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from decimal import Decimal
from datetime import datetime
from typing import Any, Dict, List, Optional
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
    unmarshal_Money,
    marshal_Money,
    marshal_ScwFile,
    marshal_ServiceInfo,
    marshal_TimeSeries,
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    DeploymentStatus,
    ListDeploymentsRequestOrderBy,
    ListModelsRequestOrderBy,
    ModelStatus,
    NodeTypeStock,
    EndpointPrivateNetworkDetails,
    EndpointPublicNetworkDetails,
    Endpoint,
    ModelSupportedQuantization,
    ModelSupportedNode,
    ModelSupportInfo,
    DeploymentQuantization,
    Deployment,
    Model,
    ListDeploymentsResponse,
    ListModelsResponse,
    NodeType,
    ListNodeTypesResponse,
    EndpointSpec,
    CreateDeploymentRequest,
    CreateEndpointRequest,
    ModelSource,
    CreateModelRequest,
    UpdateDeploymentRequest,
    UpdateEndpointRequest,
)

def unmarshal_EndpointPrivateNetworkDetails(data: Any) -> EndpointPrivateNetworkDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EndpointPrivateNetworkDetails' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_network_id", str())
    args["private_network_id"] = field

    return EndpointPrivateNetworkDetails(**args)

def unmarshal_EndpointPublicNetworkDetails(data: Any) -> EndpointPublicNetworkDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EndpointPublicNetworkDetails' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return EndpointPublicNetworkDetails(**args)

def unmarshal_Endpoint(data: Any) -> Endpoint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Endpoint' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("url", str())
    args["url"] = field

    field = data.get("disable_auth", False)
    args["disable_auth"] = field

    field = data.get("public_network", None)
    args["public_network"] = unmarshal_EndpointPublicNetworkDetails(field) if field is not None else None

    field = data.get("private_network", None)
    args["private_network"] = unmarshal_EndpointPrivateNetworkDetails(field) if field is not None else None

    return Endpoint(**args)

def unmarshal_ModelSupportedQuantization(data: Any) -> ModelSupportedQuantization:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ModelSupportedQuantization' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("quantization_bits", 0)
    args["quantization_bits"] = field

    field = data.get("allowed", False)
    args["allowed"] = field

    field = data.get("max_context_size", 0)
    args["max_context_size"] = field

    return ModelSupportedQuantization(**args)

def unmarshal_ModelSupportedNode(data: Any) -> ModelSupportedNode:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ModelSupportedNode' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("node_type_name", str())
    args["node_type_name"] = field

    field = data.get("quantizations", [])
    args["quantizations"] = [unmarshal_ModelSupportedQuantization(v) for v in field] if field is not None else None

    return ModelSupportedNode(**args)

def unmarshal_ModelSupportInfo(data: Any) -> ModelSupportInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ModelSupportInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("nodes", [])
    args["nodes"] = [unmarshal_ModelSupportedNode(v) for v in field] if field is not None else None

    return ModelSupportInfo(**args)

def unmarshal_DeploymentQuantization(data: Any) -> DeploymentQuantization:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeploymentQuantization' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("bits", str())
    args["bits"] = field

    return DeploymentQuantization(**args)

def unmarshal_Deployment(data: Any) -> Deployment:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Deployment' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("status", getattr(DeploymentStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("node_type_name", str())
    args["node_type_name"] = field

    field = data.get("endpoints", [])
    args["endpoints"] = [unmarshal_Endpoint(v) for v in field] if field is not None else None

    field = data.get("size", 0)
    args["size"] = field

    field = data.get("min_size", 0)
    args["min_size"] = field

    field = data.get("max_size", 0)
    args["max_size"] = field

    field = data.get("model_id", str())
    args["model_id"] = field

    field = data.get("model_name", str())
    args["model_name"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("error_message", None)
    args["error_message"] = field

    field = data.get("quantization", None)
    args["quantization"] = unmarshal_DeploymentQuantization(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Deployment(**args)

def unmarshal_Model(data: Any) -> Model:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Model' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("status", getattr(ModelStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("has_eula", False)
    args["has_eula"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("nodes_support", [])
    args["nodes_support"] = [unmarshal_ModelSupportInfo(v) for v in field] if field is not None else None

    field = data.get("parameter_size_bits", 0)
    args["parameter_size_bits"] = field

    field = data.get("size_bytes", 0)
    args["size_bytes"] = field

    field = data.get("error_message", None)
    args["error_message"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Model(**args)

def unmarshal_ListDeploymentsResponse(data: Any) -> ListDeploymentsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDeploymentsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("deployments", [])
    args["deployments"] = [unmarshal_Deployment(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListDeploymentsResponse(**args)

def unmarshal_ListModelsResponse(data: Any) -> ListModelsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListModelsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("models", [])
    args["models"] = [unmarshal_Model(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListModelsResponse(**args)

def unmarshal_NodeType(data: Any) -> NodeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("stock_status", getattr(NodeTypeStock, "UNKNOWN_STOCK"))
    args["stock_status"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("vcpus", 0)
    args["vcpus"] = field

    field = data.get("memory", 0)
    args["memory"] = field

    field = data.get("vram", 0)
    args["vram"] = field

    field = data.get("disabled", False)
    args["disabled"] = field

    field = data.get("beta", False)
    args["beta"] = field

    field = data.get("gpus", 0)
    args["gpus"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return NodeType(**args)

def unmarshal_ListNodeTypesResponse(data: Any) -> ListNodeTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNodeTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("node_types", [])
    args["node_types"] = [unmarshal_NodeType(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListNodeTypesResponse(**args)

def marshal_EndpointPrivateNetworkDetails(
    request: EndpointPrivateNetworkDetails,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id
    else:
        output["private_network_id"] = str()


    return output

def marshal_EndpointPublicNetworkDetails(
    request: EndpointPublicNetworkDetails,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}


    return output

def marshal_DeploymentQuantization(
    request: DeploymentQuantization,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.bits is not None:
        output["bits"] = request.bits
    else:
        output["bits"] = str()


    return output

def marshal_EndpointSpec(
    request: EndpointSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="public_network", value=request.public_network,marshal_func=marshal_EndpointPublicNetworkDetails
            ),
            OneOfPossibility(param="private_network", value=request.private_network,marshal_func=marshal_EndpointPrivateNetworkDetails
            ),
        ]),
    )

    if request.disable_auth is not None:
        output["disable_auth"] = request.disable_auth
    else:
        output["disable_auth"] = False


    return output

def marshal_CreateDeploymentRequest(
    request: CreateDeploymentRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.model_id is not None:
        output["model_id"] = request.model_id
    else:
        output["model_id"] = str()

    if request.node_type_name is not None:
        output["node_type_name"] = request.node_type_name
    else:
        output["node_type_name"] = str()

    if request.endpoints is not None:
        output["endpoints"] = [marshal_EndpointSpec(item, defaults) for item in request.endpoints]
    else:
        output["endpoints"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.accept_eula is not None:
        output["accept_eula"] = request.accept_eula
    else:
        output["accept_eula"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.min_size is not None:
        output["min_size"] = request.min_size
    else:
        output["min_size"] = None

    if request.max_size is not None:
        output["max_size"] = request.max_size
    else:
        output["max_size"] = None

    if request.quantization is not None:
        output["quantization"] = marshal_DeploymentQuantization(request.quantization, defaults)
    else:
        output["quantization"] = None


    return output

def marshal_CreateEndpointRequest(
    request: CreateEndpointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.deployment_id is not None:
        output["deployment_id"] = request.deployment_id
    else:
        output["deployment_id"] = str()

    if request.endpoint is not None:
        output["endpoint"] = marshal_EndpointSpec(request.endpoint, defaults)
    else:
        output["endpoint"] = str()


    return output

def marshal_ModelSource(
    request: ModelSource,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="secret", value=request.secret,marshal_func=None
            ),
        ]),
    )

    if request.url is not None:
        output["url"] = request.url
    else:
        output["url"] = str()


    return output

def marshal_CreateModelRequest(
    request: CreateModelRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.source is not None:
        output["source"] = marshal_ModelSource(request.source, defaults)
    else:
        output["source"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_UpdateDeploymentRequest(
    request: UpdateDeploymentRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.min_size is not None:
        output["min_size"] = request.min_size
    else:
        output["min_size"] = None

    if request.max_size is not None:
        output["max_size"] = request.max_size
    else:
        output["max_size"] = None

    if request.model_id is not None:
        output["model_id"] = request.model_id
    else:
        output["model_id"] = None

    if request.quantization is not None:
        output["quantization"] = marshal_DeploymentQuantization(request.quantization, defaults)
    else:
        output["quantization"] = None


    return output

def marshal_UpdateEndpointRequest(
    request: UpdateEndpointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.disable_auth is not None:
        output["disable_auth"] = request.disable_auth
    else:
        output["disable_auth"] = None


    return output
