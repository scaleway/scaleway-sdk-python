# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region as ScwRegion,
    ScwFile,
    unmarshal_ScwFile,
)
from scaleway_core.utils import (
    WaitForOptions,
    random_name,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
)
from .types import (
    ListDeploymentsRequestOrderBy,
    ListModelsRequestOrderBy,
    CreateDeploymentRequest,
    CreateEndpointRequest,
    CreateModelRequest,
    Deployment,
    DeploymentQuantization,
    Endpoint,
    EndpointSpec,
    ListDeploymentsResponse,
    ListModelsResponse,
    ListNodeTypesResponse,
    Model,
    ModelSource,
    NodeType,
    UpdateDeploymentRequest,
    UpdateEndpointRequest,
)
from .content import (
    DEPLOYMENT_TRANSIENT_STATUSES,
    MODEL_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Endpoint,
    unmarshal_Deployment,
    unmarshal_Model,
    unmarshal_ListDeploymentsResponse,
    unmarshal_ListModelsResponse,
    unmarshal_ListNodeTypesResponse,
    marshal_CreateDeploymentRequest,
    marshal_CreateEndpointRequest,
    marshal_CreateModelRequest,
    marshal_UpdateDeploymentRequest,
    marshal_UpdateEndpointRequest,
)


class InferenceV1API(API):
    """
    This API allows you to handle your Managed Inference services.
    """

    def list_deployments(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDeploymentsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> ListDeploymentsResponse:
        """
        List inference deployments.
        List all your inference deployments.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of deployments to return per page.
        :param order_by: Order in which to return results.
        :param project_id: Filter by Project ID.
        :param organization_id: Filter by Organization ID.
        :param name: Filter by deployment name.
        :param tags: Filter by tags.
        :return: :class:`ListDeploymentsResponse <ListDeploymentsResponse>`

        Usage:
        ::

            result = api.list_deployments()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/inference/v1/regions/{param_region}/deployments",
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
        return unmarshal_ListDeploymentsResponse(res.json())

    def list_deployments_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDeploymentsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> list[Deployment]:
        """
        List inference deployments.
        List all your inference deployments.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of deployments to return per page.
        :param order_by: Order in which to return results.
        :param project_id: Filter by Project ID.
        :param organization_id: Filter by Organization ID.
        :param name: Filter by deployment name.
        :param tags: Filter by tags.
        :return: :class:`list[Deployment] <list[Deployment]>`

        Usage:
        ::

            result = api.list_deployments_all()
        """

        return fetch_all_pages(
            type=ListDeploymentsResponse,
            key="deployments",
            fetcher=self.list_deployments,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
                "organization_id": organization_id,
                "name": name,
                "tags": tags,
            },
        )

    def get_deployment(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Deployment:
        """
        Get a deployment.
        Get the deployment for the given ID.
        :param deployment_id: ID of the deployment to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Deployment <Deployment>`

        Usage:
        ::

            result = api.get_deployment(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "GET",
            f"/inference/v1/regions/{param_region}/deployments/{param_deployment_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Deployment(res.json())

    def wait_for_deployment(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[WaitForOptions[Deployment, bool]] = None,
    ) -> Deployment:
        """
        Get a deployment.
        Get the deployment for the given ID.
        :param deployment_id: ID of the deployment to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Deployment <Deployment>`

        Usage:
        ::

            result = api.get_deployment(
                deployment_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in DEPLOYMENT_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_deployment,
            options=options,
            args={
                "deployment_id": deployment_id,
                "region": region,
            },
        )

    def create_deployment(
        self,
        *,
        model_id: str,
        node_type_name: str,
        endpoints: list[EndpointSpec],
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        accept_eula: Optional[bool] = None,
        tags: Optional[list[str]] = None,
        min_size: Optional[int] = None,
        max_size: Optional[int] = None,
        quantization: Optional[DeploymentQuantization] = None,
    ) -> Deployment:
        """
        Create a deployment.
        Create a new inference deployment related to a specific model.
        :param model_id: ID of the model to use.
        :param node_type_name: Name of the node type to use.
        :param endpoints: List of endpoints to create.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the deployment.
        :param project_id: ID of the Project to create the deployment in.
        :param accept_eula: If the model has an EULA, you must accept it before proceeding.
        The terms of the EULA can be retrieved using the `GetModelEula` API call.
        :param tags: List of tags to apply to the deployment.
        :param min_size: Defines the minimum size of the pool.
        :param max_size: Defines the maximum size of the pool.
        :param quantization: Quantization settings to apply to this deployment.
        :return: :class:`Deployment <Deployment>`

        Usage:
        ::

            result = api.create_deployment(
                model_id="example",
                node_type_name="example",
                endpoints=[],
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/inference/v1/regions/{param_region}/deployments",
            body=marshal_CreateDeploymentRequest(
                CreateDeploymentRequest(
                    model_id=model_id,
                    node_type_name=node_type_name,
                    endpoints=endpoints,
                    region=region,
                    name=name or random_name(prefix="inference"),
                    project_id=project_id,
                    accept_eula=accept_eula,
                    tags=tags,
                    min_size=min_size,
                    max_size=max_size,
                    quantization=quantization,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Deployment(res.json())

    def update_deployment(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
        min_size: Optional[int] = None,
        max_size: Optional[int] = None,
        model_id: Optional[str] = None,
        quantization: Optional[DeploymentQuantization] = None,
    ) -> Deployment:
        """
        Update a deployment.
        Update an existing inference deployment.
        :param deployment_id: ID of the deployment to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the deployment.
        :param tags: List of tags to apply to the deployment.
        :param min_size: Defines the new minimum size of the pool.
        :param max_size: Defines the new maximum size of the pool.
        :param model_id: Id of the model to set to the deployment.
        :param quantization: Quantization to use to the deployment.
        :return: :class:`Deployment <Deployment>`

        Usage:
        ::

            result = api.update_deployment(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "PATCH",
            f"/inference/v1/regions/{param_region}/deployments/{param_deployment_id}",
            body=marshal_UpdateDeploymentRequest(
                UpdateDeploymentRequest(
                    deployment_id=deployment_id,
                    region=region,
                    name=name,
                    tags=tags,
                    min_size=min_size,
                    max_size=max_size,
                    model_id=model_id,
                    quantization=quantization,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Deployment(res.json())

    def delete_deployment(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Deployment:
        """
        Delete a deployment.
        Delete an existing inference deployment.
        :param deployment_id: ID of the deployment to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Deployment <Deployment>`

        Usage:
        ::

            result = api.delete_deployment(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "DELETE",
            f"/inference/v1/regions/{param_region}/deployments/{param_deployment_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Deployment(res.json())

    def get_deployment_certificate(
        self,
        *,
        deployment_id: str,
        region: Optional[ScwRegion] = None,
    ) -> ScwFile:
        """
        Get the CA certificate.
        Get the CA certificate used for the deployment of private endpoints.
        The CA certificate will be returned as a PEM file.
        :param deployment_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ScwFile <ScwFile>`

        Usage:
        ::

            result = api.get_deployment_certificate(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "GET",
            f"/inference/v1/regions/{param_region}/deployments/{param_deployment_id}/certificate",
        )

        self._throw_on_error(res)
        return unmarshal_ScwFile(res.json())

    def create_endpoint(
        self,
        *,
        deployment_id: str,
        endpoint: EndpointSpec,
        region: Optional[ScwRegion] = None,
    ) -> Endpoint:
        """
        Create an endpoint.
        Create a new Endpoint related to a specific deployment.
        :param deployment_id: ID of the deployment to create the endpoint for.
        :param endpoint: Specification of the endpoint.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Endpoint <Endpoint>`

        Usage:
        ::

            result = api.create_endpoint(
                deployment_id="example",
                endpoint=EndpointSpec(),
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/inference/v1/regions/{param_region}/endpoints",
            body=marshal_CreateEndpointRequest(
                CreateEndpointRequest(
                    deployment_id=deployment_id,
                    endpoint=endpoint,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Endpoint(res.json())

    def update_endpoint(
        self,
        *,
        endpoint_id: str,
        region: Optional[ScwRegion] = None,
        disable_auth: Optional[bool] = None,
    ) -> Endpoint:
        """
        Update an endpoint.
        Update an existing Endpoint.
        :param endpoint_id: ID of the endpoint to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param disable_auth: By default, deployments are protected by IAM authentication.
        When setting this field to true, the authentication will be disabled.
        :return: :class:`Endpoint <Endpoint>`

        Usage:
        ::

            result = api.update_endpoint(
                endpoint_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_endpoint_id = validate_path_param("endpoint_id", endpoint_id)

        res = self._request(
            "PATCH",
            f"/inference/v1/regions/{param_region}/endpoints/{param_endpoint_id}",
            body=marshal_UpdateEndpointRequest(
                UpdateEndpointRequest(
                    endpoint_id=endpoint_id,
                    region=region,
                    disable_auth=disable_auth,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Endpoint(res.json())

    def delete_endpoint(
        self,
        *,
        endpoint_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete an endpoint.
        Delete an existing Endpoint.
        :param endpoint_id: ID of the endpoint to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_endpoint(
                endpoint_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_endpoint_id = validate_path_param("endpoint_id", endpoint_id)

        res = self._request(
            "DELETE",
            f"/inference/v1/regions/{param_region}/endpoints/{param_endpoint_id}",
        )

        self._throw_on_error(res)

    def list_models(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListModelsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> ListModelsResponse:
        """
        List models.
        List all available models.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Order in which to return results.
        :param page: Page number to return.
        :param page_size: Maximum number of models to return per page.
        :param project_id: Filter by Project ID.
        :param name: Filter by model name.
        :param tags: Filter by tags.
        :return: :class:`ListModelsResponse <ListModelsResponse>`

        Usage:
        ::

            result = api.list_models()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/inference/v1/regions/{param_region}/models",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListModelsResponse(res.json())

    def list_models_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListModelsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> list[Model]:
        """
        List models.
        List all available models.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Order in which to return results.
        :param page: Page number to return.
        :param page_size: Maximum number of models to return per page.
        :param project_id: Filter by Project ID.
        :param name: Filter by model name.
        :param tags: Filter by tags.
        :return: :class:`list[Model] <list[Model]>`

        Usage:
        ::

            result = api.list_models_all()
        """

        return fetch_all_pages(
            type=ListModelsResponse,
            key="models",
            fetcher=self.list_models,
            args={
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "project_id": project_id,
                "name": name,
                "tags": tags,
            },
        )

    def get_model(
        self,
        *,
        model_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Model:
        """
        Get a model.
        Get the model for the given ID.
        :param model_id: ID of the model to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Model <Model>`

        Usage:
        ::

            result = api.get_model(
                model_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_model_id = validate_path_param("model_id", model_id)

        res = self._request(
            "GET",
            f"/inference/v1/regions/{param_region}/models/{param_model_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Model(res.json())

    def wait_for_model(
        self,
        *,
        model_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[WaitForOptions[Model, bool]] = None,
    ) -> Model:
        """
        Get a model.
        Get the model for the given ID.
        :param model_id: ID of the model to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Model <Model>`

        Usage:
        ::

            result = api.get_model(
                model_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in MODEL_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_model,
            options=options,
            args={
                "model_id": model_id,
                "region": region,
            },
        )

    def create_model(
        self,
        *,
        source: ModelSource,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> Model:
        """
        Import a model.
        Import a new model to your model library.
        :param source: Where to import the model from.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the model.
        :param project_id: ID of the Project to import the model in.
        :return: :class:`Model <Model>`

        Usage:
        ::

            result = api.create_model(
                source=ModelSource(),
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/inference/v1/regions/{param_region}/models",
            body=marshal_CreateModelRequest(
                CreateModelRequest(
                    source=source,
                    region=region,
                    name=name or random_name(prefix="model"),
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Model(res.json())

    def delete_model(
        self,
        *,
        model_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a model.
        Delete an existing model from your model library.
        :param model_id: ID of the model to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_model(
                model_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_model_id = validate_path_param("model_id", model_id)

        res = self._request(
            "DELETE",
            f"/inference/v1/regions/{param_region}/models/{param_model_id}",
        )

        self._throw_on_error(res)

    def list_node_types(
        self,
        *,
        include_disabled_types: bool,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListNodeTypesResponse:
        """
        List available node types.
        List all available node types. By default, the node types returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param include_disabled_types: Include disabled node types in the response.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of node types to return per page.
        :return: :class:`ListNodeTypesResponse <ListNodeTypesResponse>`

        Usage:
        ::

            result = api.list_node_types(
                include_disabled_types=False,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/inference/v1/regions/{param_region}/node-types",
            params={
                "include_disabled_types": include_disabled_types,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListNodeTypesResponse(res.json())

    def list_node_types_all(
        self,
        *,
        include_disabled_types: bool,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[NodeType]:
        """
        List available node types.
        List all available node types. By default, the node types returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param include_disabled_types: Include disabled node types in the response.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of node types to return per page.
        :return: :class:`list[NodeType] <list[NodeType]>`

        Usage:
        ::

            result = api.list_node_types_all(
                include_disabled_types=False,
            )
        """

        return fetch_all_pages(
            type=ListNodeTypesResponse,
            key="node_types",
            fetcher=self.list_node_types,
            args={
                "include_disabled_types": include_disabled_types,
                "region": region,
                "page": page,
                "page_size": page_size,
            },
        )
