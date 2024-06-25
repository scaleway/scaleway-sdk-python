# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
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
    ACLRule,
    ACLRuleRequest,
    AddDeploymentACLRulesRequest,
    AddDeploymentACLRulesResponse,
    CreateDeploymentRequest,
    CreateEndpointRequest,
    Deployment,
    Endpoint,
    EndpointSpec,
    Eula,
    ListDeploymentACLRulesResponse,
    ListDeploymentsResponse,
    ListModelsResponse,
    ListNodeTypesResponse,
    Model,
    NodeType,
    SetDeploymentACLRulesRequest,
    SetDeploymentACLRulesResponse,
    UpdateDeploymentRequest,
    UpdateEndpointRequest,
)
from .content import (
    DEPLOYMENT_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Endpoint,
    unmarshal_Deployment,
    unmarshal_Model,
    unmarshal_AddDeploymentACLRulesResponse,
    unmarshal_Eula,
    unmarshal_ListDeploymentACLRulesResponse,
    unmarshal_ListDeploymentsResponse,
    unmarshal_ListModelsResponse,
    unmarshal_ListNodeTypesResponse,
    unmarshal_SetDeploymentACLRulesResponse,
    marshal_AddDeploymentACLRulesRequest,
    marshal_CreateDeploymentRequest,
    marshal_CreateEndpointRequest,
    marshal_SetDeploymentACLRulesRequest,
    marshal_UpdateDeploymentRequest,
    marshal_UpdateEndpointRequest,
)


class InferenceV1Beta1API(API):
    """
    This API allows you to manage your Inference services.
    """

    def list_deployments(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDeploymentsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
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
            f"/inference/v1beta1/regions/{param_region}/deployments",
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
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDeploymentsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> List[Deployment]:
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
        :return: :class:`List[Deployment] <List[Deployment]>`

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
        region: Optional[Region] = None,
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
            f"/inference/v1beta1/regions/{param_region}/deployments/{param_deployment_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Deployment(res.json())

    def wait_for_deployment(
        self,
        *,
        deployment_id: str,
        region: Optional[Region] = None,
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
        model_name: str,
        node_type: str,
        endpoints: List[EndpointSpec],
        region: Optional[Region] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        accept_eula: Optional[bool] = None,
        tags: Optional[List[str]] = None,
        min_size: Optional[int] = None,
        max_size: Optional[int] = None,
    ) -> Deployment:
        """
        Create a deployment.
        Create a new inference deployment related to a specific model.
        :param model_name: Name of the model to use.
        :param node_type: Name of the node type to use.
        :param endpoints: List of endpoints to create.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the deployment.
        :param project_id: ID of the Project to create the deployment in.
        :param accept_eula: If the model has an EULA, you must accept it before proceeding.
        The terms of the EULA can be retrieved using the `GetModelEula` API call.
        :param tags: List of tags to apply to the deployment.
        :param min_size: Defines the minimum size of the pool.
        :param max_size: Defines the maximum size of the pool.
        :return: :class:`Deployment <Deployment>`

        Usage:
        ::

            result = api.create_deployment(
                model_name="example",
                node_type="example",
                endpoints=[],
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/inference/v1beta1/regions/{param_region}/deployments",
            body=marshal_CreateDeploymentRequest(
                CreateDeploymentRequest(
                    model_name=model_name,
                    node_type=node_type,
                    endpoints=endpoints,
                    region=region,
                    name=name or random_name(prefix="inference"),
                    project_id=project_id,
                    accept_eula=accept_eula,
                    tags=tags,
                    min_size=min_size,
                    max_size=max_size,
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
        region: Optional[Region] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        min_size: Optional[int] = None,
        max_size: Optional[int] = None,
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
            f"/inference/v1beta1/regions/{param_region}/deployments/{param_deployment_id}",
            body=marshal_UpdateDeploymentRequest(
                UpdateDeploymentRequest(
                    deployment_id=deployment_id,
                    region=region,
                    name=name,
                    tags=tags,
                    min_size=min_size,
                    max_size=max_size,
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
        region: Optional[Region] = None,
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
            f"/inference/v1beta1/regions/{param_region}/deployments/{param_deployment_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Deployment(res.json())

    def get_deployment_certificate(
        self,
        *,
        deployment_id: str,
        region: Optional[Region] = None,
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
            f"/inference/v1beta1/regions/{param_region}/deployments/{param_deployment_id}/certificate",
        )

        self._throw_on_error(res)
        return unmarshal_ScwFile(res.json())

    def create_endpoint(
        self,
        *,
        deployment_id: str,
        endpoint: EndpointSpec,
        region: Optional[Region] = None,
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
            f"/inference/v1beta1/regions/{param_region}/endpoints",
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
        region: Optional[Region] = None,
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
            f"/inference/v1beta1/regions/{param_region}/endpoints/{param_endpoint_id}",
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
        region: Optional[Region] = None,
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
            f"/inference/v1beta1/regions/{param_region}/endpoints/{param_endpoint_id}",
        )

        self._throw_on_error(res)

    def list_deployment_acl_rules(
        self,
        *,
        deployment_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListDeploymentACLRulesResponse:
        """
        List your ACLs.
        List ACLs for a specific deployment.
        :param deployment_id: ID of the deployment to list ACL rules for.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of ACL rules to return per page.
        :return: :class:`ListDeploymentACLRulesResponse <ListDeploymentACLRulesResponse>`

        Usage:
        ::

            result = api.list_deployment_acl_rules(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "GET",
            f"/inference/v1beta1/regions/{param_region}/deployments/{param_deployment_id}/acls",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDeploymentACLRulesResponse(res.json())

    def list_deployment_acl_rules_all(
        self,
        *,
        deployment_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ACLRule]:
        """
        List your ACLs.
        List ACLs for a specific deployment.
        :param deployment_id: ID of the deployment to list ACL rules for.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of ACL rules to return per page.
        :return: :class:`List[ACLRule] <List[ACLRule]>`

        Usage:
        ::

            result = api.list_deployment_acl_rules_all(
                deployment_id="example",
            )
        """

        return fetch_all_pages(
            type=ListDeploymentACLRulesResponse,
            key="rules",
            fetcher=self.list_deployment_acl_rules,
            args={
                "deployment_id": deployment_id,
                "region": region,
                "page": page,
                "page_size": page_size,
            },
        )

    def add_deployment_acl_rules(
        self,
        *,
        deployment_id: str,
        region: Optional[Region] = None,
        acls: Optional[List[ACLRuleRequest]] = None,
    ) -> AddDeploymentACLRulesResponse:
        """
        Add new ACLs.
        Add new ACL rules for a specific deployment.
        :param deployment_id: ID of the deployment to add ACL rules to.
        :param region: Region to target. If none is passed will use default region from the config.
        :param acls: List of ACL rules to add.
        :return: :class:`AddDeploymentACLRulesResponse <AddDeploymentACLRulesResponse>`

        Usage:
        ::

            result = api.add_deployment_acl_rules(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "POST",
            f"/inference/v1beta1/regions/{param_region}/deployments/{param_deployment_id}/acls",
            body=marshal_AddDeploymentACLRulesRequest(
                AddDeploymentACLRulesRequest(
                    deployment_id=deployment_id,
                    region=region,
                    acls=acls,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_AddDeploymentACLRulesResponse(res.json())

    def set_deployment_acl_rules(
        self,
        *,
        deployment_id: str,
        region: Optional[Region] = None,
        acls: Optional[List[ACLRuleRequest]] = None,
    ) -> SetDeploymentACLRulesResponse:
        """
        Set new ACL.
        Set new ACL rules for a specific deployment.
        :param deployment_id: ID of the deployment to set ACL rules for.
        :param region: Region to target. If none is passed will use default region from the config.
        :param acls: All existing ACL rules will be replaced by the new ones.
        :return: :class:`SetDeploymentACLRulesResponse <SetDeploymentACLRulesResponse>`

        Usage:
        ::

            result = api.set_deployment_acl_rules(
                deployment_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_deployment_id = validate_path_param("deployment_id", deployment_id)

        res = self._request(
            "PUT",
            f"/inference/v1beta1/regions/{param_region}/deployments/{param_deployment_id}/acls",
            body=marshal_SetDeploymentACLRulesRequest(
                SetDeploymentACLRulesRequest(
                    deployment_id=deployment_id,
                    region=region,
                    acls=acls,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetDeploymentACLRulesResponse(res.json())

    def delete_deployment_acl_rule(
        self,
        *,
        acl_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete an exising ACL.
        :param acl_id: ID of the ACL rule to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_deployment_acl_rule(
                acl_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_acl_id = validate_path_param("acl_id", acl_id)

        res = self._request(
            "DELETE",
            f"/inference/v1beta1/regions/{param_region}/acls/{param_acl_id}",
        )

        self._throw_on_error(res)

    def list_models(
        self,
        *,
        region: Optional[Region] = None,
        order_by: Optional[ListModelsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
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
            f"/inference/v1beta1/regions/{param_region}/models",
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
        region: Optional[Region] = None,
        order_by: Optional[ListModelsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> List[Model]:
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
        :return: :class:`List[Model] <List[Model]>`

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
        region: Optional[Region] = None,
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
            f"/inference/v1beta1/regions/{param_region}/models/{param_model_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Model(res.json())

    def get_model_eula(
        self,
        *,
        model_id: str,
        region: Optional[Region] = None,
    ) -> Eula:
        """
        :param model_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Eula <Eula>`

        Usage:
        ::

            result = api.get_model_eula(
                model_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_model_id = validate_path_param("model_id", model_id)

        res = self._request(
            "GET",
            f"/inference/v1beta1/regions/{param_region}/models/{param_model_id}/eula",
        )

        self._throw_on_error(res)
        return unmarshal_Eula(res.json())

    def list_node_types(
        self,
        *,
        include_disabled_types: bool,
        region: Optional[Region] = None,
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
            f"/inference/v1beta1/regions/{param_region}/node-types",
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
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[NodeType]:
        """
        List available node types.
        List all available node types. By default, the node types returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param include_disabled_types: Include disabled node types in the response.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return.
        :param page_size: Maximum number of node types to return per page.
        :return: :class:`List[NodeType] <List[NodeType]>`

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
