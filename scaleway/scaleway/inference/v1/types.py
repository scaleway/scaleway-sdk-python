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


class DeploymentStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    CREATING = "creating"
    DEPLOYING = "deploying"
    READY = "ready"
    ERROR = "error"
    DELETING = "deleting"
    LOCKED = "locked"
    SCALING = "scaling"

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


class ModelStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    PREPARING = "preparing"
    DOWNLOADING = "downloading"
    READY = "ready"
    ERROR = "error"

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
class ModelSupportedQuantization:
    quantization_bits: int
    """
    Number of bits for this supported quantization.
    """

    allowed: bool
    """
    Tells whether this quantization is allowed for this node type.
    """

    max_context_size: int
    """
    Maximum inference context size available for this node type and quantization.
    """


@dataclass
class EndpointPrivateNetworkDetails:
    private_network_id: str


@dataclass
class EndpointPublicNetworkDetails:
    pass


@dataclass
class ModelSupportedNode:
    node_type_name: str
    """
    Supported node type.
    """

    quantizations: list[ModelSupportedQuantization]
    """
    Supported quantizations.
    """


@dataclass
class DeploymentQuantization:
    bits: int
    """
    The number of bits each model parameter should be quantized to. The quantization method is chosen based on this value.
    """


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

    public_network: Optional[EndpointPublicNetworkDetails] = None

    private_network: Optional[EndpointPrivateNetworkDetails] = None


@dataclass
class ModelSupportInfo:
    nodes: list[ModelSupportedNode]
    """
    List of supported node types.
    """


@dataclass
class EndpointSpec:
    disable_auth: bool
    """
    By default, deployments are protected by IAM authentication.
When setting this field to true, the authentication will be disabled.
    """

    public_network: Optional[EndpointPublicNetworkDetails] = None

    private_network: Optional[EndpointPrivateNetworkDetails] = None


@dataclass
class ModelSource:
    url: str
    secret: Optional[str] = None


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

    tags: list[str]
    """
    List of tags applied to the deployment.
    """

    node_type_name: str
    """
    Node type of the deployment.
    """

    endpoints: list[Endpoint]
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

    model_id: str
    """
    ID of the model used for the deployment.
    """

    model_name: str
    """
    Name of the deployed model.
    """

    region: ScwRegion
    """
    Region of the deployment.
    """

    error_message: Optional[str] = None
    """
    Displays information if your deployment is in error state.
    """

    quantization: Optional[DeploymentQuantization] = None
    """
    Quantization parameters for this deployment.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the deployment.
    """

    updated_at: Optional[datetime] = None
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

    tags: list[str]
    """
    List of tags applied to the model.
    """

    status: ModelStatus
    """
    Status of the model.
    """

    description: str
    """
    Purpose of the model.
    """

    has_eula: bool
    """
    Defines whether the model has an end user license agreement.
    """

    region: ScwRegion
    """
    Region of the model.
    """

    nodes_support: list[ModelSupportInfo]
    """
    Supported nodes types with quantization options and context lengths.
    """

    parameter_size_bits: int
    """
    Size, in bits, of the model parameters.
    """

    size_bytes: int
    """
    Total size, in bytes, of the model files.
    """

    error_message: Optional[str] = None
    """
    Displays information if your model is in error state.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the model.
    """

    updated_at: Optional[datetime] = None
    """
    Last modification date of the model.
    """


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

    region: ScwRegion
    """
    Region of the node type.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the node type.
    """

    updated_at: Optional[datetime] = None
    """
    Last modification date of the node type.
    """


@dataclass
class CreateDeploymentRequest:
    model_id: str
    """
    ID of the model to use.
    """

    node_type_name: str
    """
    Name of the node type to use.
    """

    endpoints: list[EndpointSpec]
    """
    List of endpoints to create.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the deployment.
    """

    project_id: Optional[str] = None
    """
    ID of the Project to create the deployment in.
    """

    accept_eula: Optional[bool] = False
    """
    If the model has an EULA, you must accept it before proceeding.
The terms of the EULA can be retrieved using the `GetModelEula` API call.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List of tags to apply to the deployment.
    """

    min_size: Optional[int] = 0
    """
    Defines the minimum size of the pool.
    """

    max_size: Optional[int] = 0
    """
    Defines the maximum size of the pool.
    """

    quantization: Optional[DeploymentQuantization] = None
    """
    Quantization settings to apply to this deployment.
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

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class CreateModelRequest:
    source: ModelSource
    """
    Where to import the model from.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the model.
    """

    project_id: Optional[str] = None
    """
    ID of the Project to import the model in.
    """


@dataclass
class DeleteDeploymentRequest:
    deployment_id: str
    """
    ID of the deployment to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteEndpointRequest:
    endpoint_id: str
    """
    ID of the endpoint to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteModelRequest:
    model_id: str
    """
    ID of the model to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetDeploymentCertificateRequest:
    deployment_id: str
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetDeploymentRequest:
    deployment_id: str
    """
    ID of the deployment to get.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetModelRequest:
    model_id: str
    """
    ID of the model to get.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListDeploymentsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number to return.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of deployments to return per page.
    """

    order_by: Optional[ListDeploymentsRequestOrderBy] = (
        ListDeploymentsRequestOrderBy.CREATED_AT_DESC
    )
    """
    Order in which to return results.
    """

    project_id: Optional[str] = None
    """
    Filter by Project ID.
    """

    organization_id: Optional[str] = None
    """
    Filter by Organization ID.
    """

    name: Optional[str] = None
    """
    Filter by deployment name.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Filter by tags.
    """


@dataclass
class ListDeploymentsResponse:
    deployments: list[Deployment]
    """
    List of deployments on the current page.
    """

    total_count: int
    """
    Total number of deployments.
    """


@dataclass
class ListModelsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListModelsRequestOrderBy] = (
        ListModelsRequestOrderBy.DISPLAY_RANK_ASC
    )
    """
    Order in which to return results.
    """

    page: Optional[int] = 0
    """
    Page number to return.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of models to return per page.
    """

    project_id: Optional[str] = None
    """
    Filter by Project ID.
    """

    name: Optional[str] = None
    """
    Filter by model name.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Filter by tags.
    """


@dataclass
class ListModelsResponse:
    models: list[Model]
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

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Page number to return.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of node types to return per page.
    """


@dataclass
class ListNodeTypesResponse:
    node_types: list[NodeType]
    """
    List of node types.
    """

    total_count: int
    """
    Total number of node types.
    """


@dataclass
class UpdateDeploymentRequest:
    deployment_id: str
    """
    ID of the deployment to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the deployment.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    List of tags to apply to the deployment.
    """

    min_size: Optional[int] = 0
    """
    Defines the new minimum size of the pool.
    """

    max_size: Optional[int] = 0
    """
    Defines the new maximum size of the pool.
    """

    model_id: Optional[str] = None
    """
    Id of the model to set to the deployment.
    """

    quantization: Optional[DeploymentQuantization] = None
    """
    Quantization to use to the deployment.
    """


@dataclass
class UpdateEndpointRequest:
    endpoint_id: str
    """
    ID of the endpoint to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    disable_auth: Optional[bool] = False
    """
    By default, deployments are protected by IAM authentication.
When setting this field to true, the authentication will be disabled.
    """
