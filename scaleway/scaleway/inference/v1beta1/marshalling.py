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

    args: Dict[str, Any] = {}

    field = data.get("private_network_id", str())
    args["private_network_id"] = field

    return EndpointPrivateNetworkDetails(**args)

def unmarshal_EndpointPublicAccessDetails(data: Any) -> EndpointPublicAccessDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EndpointPublicAccessDetails' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return EndpointPublicAccessDetails(**args)

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

    field = data.get("public_access", None)
    args["public_access"] = unmarshal_EndpointPublicAccessDetails(field) if field is not None else None

    field = data.get("private_network", None)
    args["private_network"] = unmarshal_EndpointPrivateNetworkDetails(field) if field is not None else None

    return Endpoint(**args)

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

    field = data.get("node_type", str())
    args["node_type"] = field

    field = data.get("endpoints", [])
    args["endpoints"] = [unmarshal_Endpoint(v) for v in field] if field is not None else None

    field = data.get("size", 0)
    args["size"] = field

    field = data.get("min_size", 0)
    args["min_size"] = field

    field = data.get("max_size", 0)
    args["max_size"] = field

    field = data.get("model_name", str())
    args["model_name"] = field

    field = data.get("model_id", str())
    args["model_id"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("error_message", None)
    args["error_message"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Deployment(**args)

def unmarshal_ModelS3Model(data: Any) -> ModelS3Model:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ModelS3Model' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("s3_url", str())
    args["s3_url"] = field

    field = data.get("python_dependencies", str())
    args["python_dependencies"] = field

    field = data.get("node_type", None)
    args["node_type"] = field

    field = data.get("triton_server_version", None)
    args["triton_server_version"] = field

    return ModelS3Model(**args)

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

    field = data.get("provider", str())
    args["provider"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("has_eula", False)
    args["has_eula"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("is_public", False)
    args["is_public"] = field

    field = data.get("compatible_node_types", [])
    args["compatible_node_types"] = field

    field = data.get("quantization_level", str())
    args["quantization_level"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("s3_model", None)
    args["s3_model"] = unmarshal_ModelS3Model(field) if field is not None else None

    return Model(**args)

def unmarshal_ACLRule(data: Any) -> ACLRule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ACLRule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("ip", str())
    args["ip"] = field

    field = data.get("description", str())
    args["description"] = field

    return ACLRule(**args)

def unmarshal_AddDeploymentACLRulesResponse(data: Any) -> AddDeploymentACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AddDeploymentACLRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", [])
    args["rules"] = [unmarshal_ACLRule(v) for v in field] if field is not None else None

    return AddDeploymentACLRulesResponse(**args)

def unmarshal_Eula(data: Any) -> Eula:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Eula' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("content", str())
    args["content"] = field

    return Eula(**args)

def unmarshal_ListDeploymentACLRulesResponse(data: Any) -> ListDeploymentACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDeploymentACLRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", [])
    args["rules"] = [unmarshal_ACLRule(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListDeploymentACLRulesResponse(**args)

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

def unmarshal_SetDeploymentACLRulesResponse(data: Any) -> SetDeploymentACLRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetDeploymentACLRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", [])
    args["rules"] = [unmarshal_ACLRule(v) for v in field] if field is not None else None

    return SetDeploymentACLRulesResponse(**args)

def marshal_ACLRuleRequest(
    request: ACLRuleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip is not None:
        output["ip"] = request.ip
    else:
        output["ip"] = str()

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()


    return output

def marshal_AddDeploymentACLRulesRequest(
    request: AddDeploymentACLRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.acls is not None:
        output["acls"] = [marshal_ACLRuleRequest(item, defaults) for item in request.acls]
    else:
        output["acls"] = None


    return output

def marshal_EndpointSpecPrivateNetwork(
    request: EndpointSpecPrivateNetwork,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id
    else:
        output["private_network_id"] = str()


    return output

def marshal_EndpointSpecPublic(
    request: EndpointSpecPublic,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}


    return output

def marshal_EndpointSpec(
    request: EndpointSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="public", value=request.public,marshal_func=marshal_EndpointSpecPublic
            ),
            OneOfPossibility(param="private_network", value=request.private_network,marshal_func=marshal_EndpointSpecPrivateNetwork
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

    if request.model_name is not None:
        output["model_name"] = request.model_name
    else:
        output["model_name"] = str()

    if request.node_type is not None:
        output["node_type"] = request.node_type
    else:
        output["node_type"] = str()

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

def marshal_SetDeploymentACLRulesRequest(
    request: SetDeploymentACLRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.acls is not None:
        output["acls"] = [marshal_ACLRuleRequest(item, defaults) for item in request.acls]
    else:
        output["acls"] = None


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
