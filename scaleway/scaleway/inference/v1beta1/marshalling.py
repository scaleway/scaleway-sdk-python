# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    DeploymentStatus,
    NodeTypeStock,
    EndpointPrivateNetworkDetails,
    EndpointPublicAccessDetails,
    Endpoint,
    Deployment,
    ModelS3Model,
    Model,
    ACLRule,
    AddDeploymentACLRulesResponse,
    Eula,
    ListDeploymentACLRulesResponse,
    ListDeploymentsResponse,
    ListModelsResponse,
    NodeType,
    ListNodeTypesResponse,
    SetDeploymentACLRulesResponse,
    ACLRuleRequest,
    AddDeploymentACLRulesRequest,
    EndpointSpecPrivateNetwork,
    EndpointSpecPublic,
    EndpointSpec,
    CreateDeploymentRequest,
    CreateEndpointRequest,
    SetDeploymentACLRulesRequest,
    UpdateDeploymentRequest,
    UpdateEndpointRequest,
)


def unmarshal_EndpointPrivateNetworkDetails(data: Any) -> EndpointPrivateNetworkDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EndpointPrivateNetworkDetails' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("private_network_id", None)
    if field is not None:
        args["private_network_id"] = field
    else:
        args["private_network_id"] = None

    return EndpointPrivateNetworkDetails(**args)


def unmarshal_EndpointPublicAccessDetails(data: Any) -> EndpointPublicAccessDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EndpointPublicAccessDetails' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return EndpointPublicAccessDetails(**args)


def unmarshal_Endpoint(data: Any) -> Endpoint:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Endpoint' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("url", None)
    if field is not None:
        args["url"] = field
    else:
        args["url"] = None

    field = data.get("disable_auth", None)
    if field is not None:
        args["disable_auth"] = field
    else:
        args["disable_auth"] = False

    field = data.get("public_access", None)
    if field is not None:
        args["public_access"] = unmarshal_EndpointPublicAccessDetails(field)
    else:
        args["public_access"] = None

    field = data.get("private_network", None)
    if field is not None:
        args["private_network"] = unmarshal_EndpointPrivateNetworkDetails(field)
    else:
        args["private_network"] = None

    return Endpoint(**args)


def unmarshal_Deployment(data: Any) -> Deployment:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Deployment' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DeploymentStatus.UNKNOWN_STATUS

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("node_type", None)
    if field is not None:
        args["node_type"] = field
    else:
        args["node_type"] = None

    field = data.get("endpoints", None)
    if field is not None:
        args["endpoints"] = (
            [unmarshal_Endpoint(v) for v in field] if field is not None else None
        )
    else:
        args["endpoints"] = []

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = 0

    field = data.get("min_size", None)
    if field is not None:
        args["min_size"] = field
    else:
        args["min_size"] = 0

    field = data.get("max_size", None)
    if field is not None:
        args["max_size"] = field
    else:
        args["max_size"] = 0

    field = data.get("model_name", None)
    if field is not None:
        args["model_name"] = field
    else:
        args["model_name"] = None

    field = data.get("model_id", None)
    if field is not None:
        args["model_id"] = field
    else:
        args["model_id"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

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

    return Deployment(**args)


def unmarshal_ModelS3Model(data: Any) -> ModelS3Model:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ModelS3Model' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("s3_url", None)
    if field is not None:
        args["s3_url"] = field
    else:
        args["s3_url"] = None

    field = data.get("python_dependencies", None)
    if field is not None:
        args["python_dependencies"] = field
    else:
        args["python_dependencies"] = None

    field = data.get("node_type", None)
    if field is not None:
        args["node_type"] = field
    else:
        args["node_type"] = None

    field = data.get("triton_server_version", None)
    if field is not None:
        args["triton_server_version"] = field
    else:
        args["triton_server_version"] = None

    return ModelS3Model(**args)


def unmarshal_Model(data: Any) -> Model:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Model' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("provider", None)
    if field is not None:
        args["provider"] = field
    else:
        args["provider"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("has_eula", None)
    if field is not None:
        args["has_eula"] = field
    else:
        args["has_eula"] = False

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("is_public", None)
    if field is not None:
        args["is_public"] = field
    else:
        args["is_public"] = False

    field = data.get("compatible_node_types", None)
    if field is not None:
        args["compatible_node_types"] = field
    else:
        args["compatible_node_types"] = []

    field = data.get("quantization_level", None)
    if field is not None:
        args["quantization_level"] = field
    else:
        args["quantization_level"] = None

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

    field = data.get("s3_model", None)
    if field is not None:
        args["s3_model"] = unmarshal_ModelS3Model(field)
    else:
        args["s3_model"] = None

    return Model(**args)


def unmarshal_ACLRule(data: Any) -> ACLRule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ACLRule' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("ip", None)
    if field is not None:
        args["ip"] = field
    else:
        args["ip"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    return ACLRule(**args)


def unmarshal_AddDeploymentACLRulesResponse(data: Any) -> AddDeploymentACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddDeploymentACLRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("rules", None)
    if field is not None:
        args["rules"] = (
            [unmarshal_ACLRule(v) for v in field] if field is not None else None
        )
    else:
        args["rules"] = []

    return AddDeploymentACLRulesResponse(**args)


def unmarshal_Eula(data: Any) -> Eula:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Eula' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("content", None)
    if field is not None:
        args["content"] = field
    else:
        args["content"] = None

    return Eula(**args)


def unmarshal_ListDeploymentACLRulesResponse(
    data: Any,
) -> ListDeploymentACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDeploymentACLRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("rules", None)
    if field is not None:
        args["rules"] = (
            [unmarshal_ACLRule(v) for v in field] if field is not None else None
        )
    else:
        args["rules"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListDeploymentACLRulesResponse(**args)


def unmarshal_ListDeploymentsResponse(data: Any) -> ListDeploymentsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDeploymentsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("deployments", None)
    if field is not None:
        args["deployments"] = (
            [unmarshal_Deployment(v) for v in field] if field is not None else None
        )
    else:
        args["deployments"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListDeploymentsResponse(**args)


def unmarshal_ListModelsResponse(data: Any) -> ListModelsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListModelsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("models", None)
    if field is not None:
        args["models"] = (
            [unmarshal_Model(v) for v in field] if field is not None else None
        )
    else:
        args["models"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListModelsResponse(**args)


def unmarshal_NodeType(data: Any) -> NodeType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NodeType' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("stock_status", None)
    if field is not None:
        args["stock_status"] = field
    else:
        args["stock_status"] = NodeTypeStock.UNKNOWN_STOCK

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

    field = data.get("memory", None)
    if field is not None:
        args["memory"] = field
    else:
        args["memory"] = 0

    field = data.get("vram", None)
    if field is not None:
        args["vram"] = field
    else:
        args["vram"] = 0

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

    field = data.get("gpus", None)
    if field is not None:
        args["gpus"] = field
    else:
        args["gpus"] = 0

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

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


def unmarshal_SetDeploymentACLRulesResponse(data: Any) -> SetDeploymentACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetDeploymentACLRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("rules", None)
    if field is not None:
        args["rules"] = (
            [unmarshal_ACLRule(v) for v in field] if field is not None else None
        )
    else:
        args["rules"] = []

    return SetDeploymentACLRulesResponse(**args)


def marshal_ACLRuleRequest(
    request: ACLRuleRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ip is not None:
        output["ip"] = request.ip

    if request.description is not None:
        output["description"] = request.description

    return output


def marshal_AddDeploymentACLRulesRequest(
    request: AddDeploymentACLRulesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.acls is not None:
        output["acls"] = [
            marshal_ACLRuleRequest(item, defaults) for item in request.acls
        ]

    return output


def marshal_EndpointSpecPrivateNetwork(
    request: EndpointSpecPrivateNetwork,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id

    return output


def marshal_EndpointSpecPublic(
    request: EndpointSpecPublic,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    return output


def marshal_EndpointSpec(
    request: EndpointSpec,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="public",
                    value=request.public,
                    marshal_func=marshal_EndpointSpecPublic,
                ),
                OneOfPossibility(
                    param="private_network",
                    value=request.private_network,
                    marshal_func=marshal_EndpointSpecPrivateNetwork,
                ),
            ]
        ),
    )

    if request.disable_auth is not None:
        output["disable_auth"] = request.disable_auth

    return output


def marshal_CreateDeploymentRequest(
    request: CreateDeploymentRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.model_name is not None:
        output["model_name"] = request.model_name

    if request.node_type is not None:
        output["node_type"] = request.node_type

    if request.endpoints is not None:
        output["endpoints"] = [
            marshal_EndpointSpec(item, defaults) for item in request.endpoints
        ]

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.accept_eula is not None:
        output["accept_eula"] = request.accept_eula

    if request.tags is not None:
        output["tags"] = request.tags

    if request.min_size is not None:
        output["min_size"] = request.min_size

    if request.max_size is not None:
        output["max_size"] = request.max_size

    return output


def marshal_CreateEndpointRequest(
    request: CreateEndpointRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.deployment_id is not None:
        output["deployment_id"] = request.deployment_id

    if request.endpoint is not None:
        output["endpoint"] = marshal_EndpointSpec(request.endpoint, defaults)

    return output


def marshal_SetDeploymentACLRulesRequest(
    request: SetDeploymentACLRulesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.acls is not None:
        output["acls"] = [
            marshal_ACLRuleRequest(item, defaults) for item in request.acls
        ]

    return output


def marshal_UpdateDeploymentRequest(
    request: UpdateDeploymentRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

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
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.disable_auth is not None:
        output["disable_auth"] = request.disable_auth

    return output
