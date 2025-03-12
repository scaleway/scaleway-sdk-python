# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
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

    field = data.get("private_network_id", None)
    if field is not None:
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

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("url", None)
    if field is not None:
        args["url"] = field

    field = data.get("disable_auth", None)
    if field is not None:
        args["disable_auth"] = field

    field = data.get("public_network", None)
    if field is not None:
        args["public_network"] = unmarshal_EndpointPublicNetworkDetails(field)
    else:
        args["public_network"] = None

    field = data.get("private_network", None)
    if field is not None:
        args["private_network"] = unmarshal_EndpointPrivateNetworkDetails(field)
    else:
        args["private_network"] = None

    return Endpoint(**args)


def unmarshal_ModelSupportedQuantization(data: Any) -> ModelSupportedQuantization:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ModelSupportedQuantization' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("quantization_bits", None)
    if field is not None:
        args["quantization_bits"] = field

    field = data.get("allowed", None)
    if field is not None:
        args["allowed"] = field

    field = data.get("max_context_size", None)
    if field is not None:
        args["max_context_size"] = field

    return ModelSupportedQuantization(**args)


def unmarshal_ModelSupportedNode(data: Any) -> ModelSupportedNode:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ModelSupportedNode' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("node_type_name", None)
    if field is not None:
        args["node_type_name"] = field

    field = data.get("quantizations", None)
    if field is not None:
        args["quantizations"] = (
            [unmarshal_ModelSupportedQuantization(v) for v in field]
            if field is not None
            else None
        )

    return ModelSupportedNode(**args)


def unmarshal_ModelSupportInfo(data: Any) -> ModelSupportInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ModelSupportInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("nodes", None)
    if field is not None:
        args["nodes"] = (
            [unmarshal_ModelSupportedNode(v) for v in field]
            if field is not None
            else None
        )

    return ModelSupportInfo(**args)


def unmarshal_DeploymentQuantization(data: Any) -> DeploymentQuantization:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeploymentQuantization' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("enabled", None)
    if field is not None:
        args["enabled"] = field

    field = data.get("bits", None)
    if field is not None:
        args["bits"] = field

    return DeploymentQuantization(**args)


def unmarshal_Deployment(data: Any) -> Deployment:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Deployment' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("node_type_name", None)
    if field is not None:
        args["node_type_name"] = field

    field = data.get("endpoints", None)
    if field is not None:
        args["endpoints"] = (
            [unmarshal_Endpoint(v) for v in field] if field is not None else None
        )

    field = data.get("size", None)
    if field is not None:
        args["size"] = field

    field = data.get("min_size", None)
    if field is not None:
        args["min_size"] = field

    field = data.get("max_size", None)
    if field is not None:
        args["max_size"] = field

    field = data.get("model_id", None)
    if field is not None:
        args["model_id"] = field

    field = data.get("model_name", None)
    if field is not None:
        args["model_name"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

    field = data.get("quantization", None)
    if field is not None:
        args["quantization"] = unmarshal_DeploymentQuantization(field)
    else:
        args["quantization"] = None

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

    return Deployment(**args)


def unmarshal_Model(data: Any) -> Model:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Model' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("description", None)
    if field is not None:
        args["description"] = field

    field = data.get("has_eula", None)
    if field is not None:
        args["has_eula"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("nodes_support", None)
    if field is not None:
        args["nodes_support"] = (
            [unmarshal_ModelSupportInfo(v) for v in field]
            if field is not None
            else None
        )

    field = data.get("parameter_size_bits", None)
    if field is not None:
        args["parameter_size_bits"] = field

    field = data.get("size_bytes", None)
    if field is not None:
        args["size_bytes"] = field

    field = data.get("error_message", None)
    if field is not None:
        args["error_message"] = field
    else:
        args["error_message"] = None

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

    return Model(**args)


def unmarshal_ListDeploymentsResponse(data: Any) -> ListDeploymentsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDeploymentsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("deployments", None)
    if field is not None:
        args["deployments"] = (
            [unmarshal_Deployment(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListDeploymentsResponse(**args)


def unmarshal_ListModelsResponse(data: Any) -> ListModelsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListModelsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("models", None)
    if field is not None:
        args["models"] = (
            [unmarshal_Model(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListModelsResponse(**args)


def unmarshal_NodeType(data: Any) -> NodeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("stock_status", None)
    if field is not None:
        args["stock_status"] = field

    field = data.get("description", None)
    if field is not None:
        args["description"] = field

    field = data.get("vcpus", None)
    if field is not None:
        args["vcpus"] = field

    field = data.get("memory", None)
    if field is not None:
        args["memory"] = field

    field = data.get("vram", None)
    if field is not None:
        args["vram"] = field

    field = data.get("disabled", None)
    if field is not None:
        args["disabled"] = field

    field = data.get("beta", None)
    if field is not None:
        args["beta"] = field

    field = data.get("gpus", None)
    if field is not None:
        args["gpus"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("node_types", None)
    if field is not None:
        args["node_types"] = (
            [unmarshal_NodeType(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListNodeTypesResponse(**args)


def marshal_EndpointPrivateNetworkDetails(
    request: EndpointPrivateNetworkDetails,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

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

    if request.enabled is not None:
        output["enabled"] = request.enabled

    if request.bits is not None:
        output["bits"] = request.bits

    return output


def marshal_EndpointSpec(
    request: EndpointSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("public_network", request.public_network),
                OneOfPossibility("private_network", request.private_network),
            ]
        ),
    )

    if request.disable_auth is not None:
        output["disable_auth"] = request.disable_auth

    return output


def marshal_CreateDeploymentRequest(
    request: CreateDeploymentRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.model_id is not None:
        output["model_id"] = request.model_id

    if request.node_type_name is not None:
        output["node_type_name"] = request.node_type_name

    if request.endpoints is not None:
        output["endpoints"] = [
            marshal_EndpointSpec(item, defaults) for item in request.endpoints
        ]

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.accept_eula is not None:
        output["accept_eula"] = request.accept_eula

    if request.tags is not None:
        output["tags"] = request.tags

    if request.min_size is not None:
        output["min_size"] = request.min_size

    if request.max_size is not None:
        output["max_size"] = request.max_size

    if request.quantization is not None:
        output["quantization"] = marshal_DeploymentQuantization(
            request.quantization, defaults
        )

    return output


def marshal_CreateEndpointRequest(
    request: CreateEndpointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.deployment_id is not None:
        output["deployment_id"] = request.deployment_id

    if request.endpoint is not None:
        output["endpoint"] = marshal_EndpointSpec(request.endpoint, defaults)

    return output


def marshal_ModelSource(
    request: ModelSource,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("secret", request.secret),
            ]
        ),
    )

    if request.url is not None:
        output["url"] = request.url

    return output


def marshal_CreateModelRequest(
    request: CreateModelRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.source is not None:
        output["source"] = marshal_ModelSource(request.source, defaults)

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_UpdateDeploymentRequest(
    request: UpdateDeploymentRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.min_size is not None:
        output["min_size"] = request.min_size

    if request.max_size is not None:
        output["max_size"] = request.max_size

    return output


def marshal_UpdateEndpointRequest(
    request: UpdateEndpointRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.disable_auth is not None:
        output["disable_auth"] = request.disable_auth

    return output
