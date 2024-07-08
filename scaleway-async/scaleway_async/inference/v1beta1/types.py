# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class DeploymentStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    CREATING = "creating"
    DEPLOYING = "deploying"
    READY = "ready"
    ERROR = "error"
    DELETING = "deleting"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class ListDeploymentsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListModelsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    DISPLAY_RANK_ASC = "display_rank_asc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
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


@dataclass
class EndpointPrivateNetworkDetails:
    private_network_id: str
    """
    ID of the Private Network.
    """


@dataclass
class EndpointPublicAccessDetails:
    pass


@dataclass
class EndpointSpecPrivateNetwork:
    private_network_id: str
    """
    ID of the Private Network.
    """


@dataclass
class EndpointSpecPublic:
    pass


@dataclass
class Endpoint:
    id: str
    """
    Unique identifier.
    """

    url: str
    """
    For private endpoints, the URL will be accessible only from the Private Network.
In addition, private endpoints will expose a CA certificate that can be used to verify the server's identity.
This CA certificate can be retrieved using the `GetDeploymentCertificate` API call.
    """

    disable_auth: bool
    """
    Defines whether the authentication is disabled.
    """

    public_access: Optional[EndpointPublicAccessDetails]

    private_network: Optional[EndpointPrivateNetworkDetails]


@dataclass
class ModelS3Model:
    s3_url: str

    python_dependencies: Dict[str, str]

    node_type: Optional[str]

    triton_server_version: Optional[str]


@dataclass
class ACLRuleRequest:
    ip: str
    """
    It can be specified as a single IP address or a range of IP addresses in CIDR notation.
    """

    description: str
    """
    Description of the ACL rule.
    """


@dataclass
class ACLRule:
    id: str
    """
    Unique identifier.
    """

    ip: str
    """
    Allowed IP address or CIDR range.
    """

    description: str
    """
    Description of the ACL rule.
    """


@dataclass
class EndpointSpec:
    disable_auth: bool
    """
    By default, deployments are protected by IAM authentication.
When setting this field to true, the authentication will be disabled.
    """

    public: Optional[EndpointSpecPublic]

    private_network: Optional[EndpointSpecPrivateNetwork]


@dataclass
class Deployment:
    id: str
    """
    Unique identifier.
    """

    name: str
    """
    Name of the deployment.
    """

    project_id: str
    """
    Project ID.
    """

    status: DeploymentStatus
    """
    Status of the deployment.
    """

    tags: List[str]
    """
    List of tags applied to the deployment.
    """

    node_type: str
    """
    Node type of the deployment.
    """

    endpoints: List[Endpoint]
    """
    List of endpoints.
    """

    size: int
    """
    Current size of the pool.
    """

    min_size: int
    """
    Defines the minimum size of the pool.
    """

    max_size: int
    """
    Defines the maximum size of the pool.
    """

    model_name: str
    """
    The inference model used for the deployment.
    """

    model_id: str
    """
    ID of the model used for the deployment.
    """

    region: Region
    """
    Region of the deployment.
    """

    error_message: Optional[str]
    """
    Displays information if your deployment is in error state.
    """

    created_at: Optional[datetime]
    """
    Creation date of the deployment.
    """

    updated_at: Optional[datetime]
    """
    Last modification date of the deployment.
    """


@dataclass
class Model:
    id: str
    """
    Unique identifier.
    """

    name: str
    """
    Unique Name identifier.
    """

    project_id: str
    """
    Project ID.
    """

    provider: str
    """
    Name of the model provider.
    """

    tags: List[str]
    """
    List of tags applied to the model.
    """

    description: str
    """
    Purpose of the model.
    """

    has_eula: bool
    """
    Defines whether the model has an end user licence agreement.
    """

    region: Region
    """
    Region of the model.
    """

    is_public: bool
    """
    Defines whether the model is public or not.
    """

    compatible_node_types: List[str]
    """
    Names of the node types compatible with the model.
    """

    quantization_level: str
    """
    Quantization level of the model.
    """

    created_at: Optional[datetime]
    """
    Creation date of the model.
    """

    updated_at: Optional[datetime]
    """
    Last modification date of the model.
    """

    s3_model: Optional[ModelS3Model]


@dataclass
class NodeType:
    name: str
    """
    Name of the node type.
    """

    stock_status: NodeTypeStock
    """
    Current stock status for the node type.
    """

    description: str
    """
    Current specs of the offer.
    """

    vcpus: int
    """
    Number of virtual CPUs.
    """

    memory: int
    """
    Quantity of RAM.
    """

    vram: int
    """
    Quantity of GPU RAM.
    """

    disabled: bool
    """
    The node type is currently disabled.
    """

    beta: bool
    """
    The node type is currently in beta.
    """

    gpus: int
    """
    Number of GPUs.
    """

    region: Region
    """
    Region of the node type.
    """

    created_at: Optional[datetime]
    """
    Creation date of the node type.
    """

    updated_at: Optional[datetime]
    """
    Last modification date of the node type.
    """


@dataclass
class AddDeploymentACLRulesRequest:
    deployment_id: str
    """
    ID of the deployment to add ACL rules to.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    acls: Optional[List[ACLRuleRequest]]
    """
    List of ACL rules to add.
    """


@dataclass
class AddDeploymentACLRulesResponse:
    rules: List[ACLRule]
    """
    List of ACL rules added.
    """


@dataclass
class CreateDeploymentRequest:
    model_name: str
    """
    Name of the model to use.
    """

    node_type: str
    """
    Name of the node type to use.
    """

    endpoints: List[EndpointSpec]
    """
    List of endpoints to create.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the deployment.
    """

    project_id: Optional[str]
    """
    ID of the Project to create the deployment in.
    """

    accept_eula: Optional[bool]
    """
    If the model has an EULA, you must accept it before proceeding.
The terms of the EULA can be retrieved using the `GetModelEula` API call.
    """

    tags: Optional[List[str]]
    """
    List of tags to apply to the deployment.
    """

    min_size: Optional[int]
    """
    Defines the minimum size of the pool.
    """

    max_size: Optional[int]
    """
    Defines the maximum size of the pool.
    """


@dataclass
class CreateEndpointRequest:
    deployment_id: str
    """
    ID of the deployment to create the endpoint for.
    """

    endpoint: EndpointSpec
    """
    Specification of the endpoint.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteDeploymentACLRuleRequest:
    acl_id: str
    """
    ID of the ACL rule to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteDeploymentRequest:
    deployment_id: str
    """
    ID of the deployment to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteEndpointRequest:
    endpoint_id: str
    """
    ID of the endpoint to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class Eula:
    content: str
    """
    Content of the end user licence agreement.
    """


@dataclass
class GetDeploymentCertificateRequest:
    deployment_id: str

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetDeploymentRequest:
    deployment_id: str
    """
    ID of the deployment to get.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetModelEulaRequest:
    model_id: str

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetModelRequest:
    model_id: str
    """
    ID of the model to get.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListDeploymentACLRulesRequest:
    deployment_id: str
    """
    ID of the deployment to list ACL rules for.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number to return.
    """

    page_size: Optional[int]
    """
    Maximum number of ACL rules to return per page.
    """


@dataclass
class ListDeploymentACLRulesResponse:
    rules: List[ACLRule]
    """
    List of ACL rules on the current page.
    """

    total_count: int
    """
    Total number of ACL rules.
    """


@dataclass
class ListDeploymentsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number to return.
    """

    page_size: Optional[int]
    """
    Maximum number of deployments to return per page.
    """

    order_by: Optional[ListDeploymentsRequestOrderBy]
    """
    Order in which to return results.
    """

    project_id: Optional[str]
    """
    Filter by Project ID.
    """

    organization_id: Optional[str]
    """
    Filter by Organization ID.
    """

    name: Optional[str]
    """
    Filter by deployment name.
    """

    tags: Optional[List[str]]
    """
    Filter by tags.
    """


@dataclass
class ListDeploymentsResponse:
    deployments: List[Deployment]
    """
    List of deployments on the current page.
    """

    total_count: int
    """
    Total number of deployments.
    """


@dataclass
class ListModelsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListModelsRequestOrderBy]
    """
    Order in which to return results.
    """

    page: Optional[int]
    """
    Page number to return.
    """

    page_size: Optional[int]
    """
    Maximum number of models to return per page.
    """

    project_id: Optional[str]
    """
    Filter by Project ID.
    """

    name: Optional[str]
    """
    Filter by model name.
    """

    tags: Optional[List[str]]
    """
    Filter by tags.
    """


@dataclass
class ListModelsResponse:
    models: List[Model]
    """
    List of models on the current page.
    """

    total_count: int
    """
    Total number of models.
    """


@dataclass
class ListNodeTypesRequest:
    include_disabled_types: bool
    """
    Include disabled node types in the response.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Page number to return.
    """

    page_size: Optional[int]
    """
    Maximum number of node types to return per page.
    """


@dataclass
class ListNodeTypesResponse:
    node_types: List[NodeType]
    """
    List of node types.
    """

    total_count: int
    """
    Total number of node types.
    """


@dataclass
class SetDeploymentACLRulesRequest:
    deployment_id: str
    """
    ID of the deployment to set ACL rules for.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    acls: Optional[List[ACLRuleRequest]]
    """
    All existing ACL rules will be replaced by the new ones.
    """


@dataclass
class SetDeploymentACLRulesResponse:
    rules: List[ACLRule]
    """
    List of ACL rules that were set.
    """


@dataclass
class UpdateDeploymentRequest:
    deployment_id: str
    """
    ID of the deployment to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the deployment.
    """

    tags: Optional[List[str]]
    """
    List of tags to apply to the deployment.
    """

    min_size: Optional[int]
    """
    Defines the new minimum size of the pool.
    """

    max_size: Optional[int]
    """
    Defines the new maximum size of the pool.
    """


@dataclass
class UpdateEndpointRequest:
    endpoint_id: str
    """
    ID of the endpoint to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    disable_auth: Optional[bool]
    """
    By default, deployments are protected by IAM authentication.
When setting this field to true, the authentication will be disabled.
    """
