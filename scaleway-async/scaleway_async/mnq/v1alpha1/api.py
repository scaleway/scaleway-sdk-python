# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    fetch_all_pages_async,
    random_name,
    validate_path_param,
)
from .types import (
    ListCredentialsRequestOrderBy,
    ListNamespacesRequestOrderBy,
    NamespaceProtocol,
    Credential,
    CredentialSummary,
    ListCredentialsResponse,
    ListNamespacesResponse,
    Namespace,
    Permissions,
    CreateNamespaceRequest,
    UpdateNamespaceRequest,
    CreateCredentialRequest,
    UpdateCredentialRequest,
)
from .marshalling import (
    marshal_CreateCredentialRequest,
    marshal_CreateNamespaceRequest,
    marshal_UpdateCredentialRequest,
    marshal_UpdateNamespaceRequest,
    unmarshal_Namespace,
    unmarshal_Credential,
    unmarshal_ListCredentialsResponse,
    unmarshal_ListNamespacesResponse,
)


class MnqV1Alpha1API(API):
    """
    MnQ API (beta).

    This API allows you to manage Messaging or Queueing brokers.
    """

    async def list_namespaces(
        self,
        *,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListNamespacesRequestOrderBy = ListNamespacesRequestOrderBy.CREATED_AT_ASC,
    ) -> ListNamespacesResponse:
        """
        List namespaces
        :param region: Region to target. If none is passed will use default region from the config
        :param organization_id: Will list only the Namespaces owned by the specified organization
        :param project_id: Will list only the Namespaces contained into the specified project
        :param page: Indicate the page number of results to be returned
        :param page_size: Maximum number of results returned by page
        :param order_by: Field used for sorting results
        :return: :class:`ListNamespacesResponse <ListNamespacesResponse>`

        Usage:
        ::

            result = await api.list_namespaces()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/mnq/v1alpha1/regions/{param_region}/namespaces",
            params={
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListNamespacesResponse(res.json())

    async def list_namespaces_all(
        self,
        *,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNamespacesRequestOrderBy] = None,
    ) -> List[Namespace]:
        """
        List namespaces
        :param region: Region to target. If none is passed will use default region from the config
        :param organization_id: Will list only the Namespaces owned by the specified organization
        :param project_id: Will list only the Namespaces contained into the specified project
        :param page: Indicate the page number of results to be returned
        :param page_size: Maximum number of results returned by page
        :param order_by: Field used for sorting results
        :return: :class:`List[ListNamespacesResponse] <List[ListNamespacesResponse]>`

        Usage:
        ::

            result = await api.list_namespaces_all()
        """

        return await fetch_all_pages_async(
            type=ListNamespacesResponse,
            key="namespaces",
            fetcher=self.list_namespaces,
            args={
                "region": region,
                "organization_id": organization_id,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def create_namespace(
        self,
        *,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        protocol: NamespaceProtocol = NamespaceProtocol.UNKNOWN,
        project_id: Optional[str] = None,
    ) -> Namespace:
        """
        Create a namespace
        :param region: Region to target. If none is passed will use default region from the config
        :param name: Namespace name
        :param protocol: Namespace protocol
        :param project_id: Project containing the Namespace
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = await api.create_namespace()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/mnq/v1alpha1/regions/{param_region}/namespaces",
            body=marshal_CreateNamespaceRequest(
                CreateNamespaceRequest(
                    region=region,
                    name=name or random_name(prefix="mnq"),
                    protocol=protocol,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())

    async def update_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
    ) -> Namespace:
        """
        Update the name of a namespace
        :param region: Region to target. If none is passed will use default region from the config
        :param namespace_id: ID of the Namespace to update
        :param name: Namespace name
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = await api.update_namespace(namespace_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "PATCH",
            f"/mnq/v1alpha1/regions/{param_region}/namespaces",
            body=marshal_UpdateNamespaceRequest(
                UpdateNamespaceRequest(
                    namespace_id=namespace_id,
                    region=region,
                    name=name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())

    async def get_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
    ) -> Namespace:
        """
        Get a namespace
        :param region: Region to target. If none is passed will use default region from the config
        :param namespace_id: ID of the Namespace to get
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = await api.get_namespace(namespace_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_namespace_id = validate_path_param("namespace_id", namespace_id)

        res = self._request(
            "GET",
            f"/mnq/v1alpha1/regions/{param_region}/namespaces/{param_namespace_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())

    async def delete_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a namespace
        :param region: Region to target. If none is passed will use default region from the config
        :param namespace_id: ID of the Namespace to delete

        Usage:
        ::

            result = await api.delete_namespace(namespace_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_namespace_id = validate_path_param("namespace_id", namespace_id)

        res = self._request(
            "DELETE",
            f"/mnq/v1alpha1/regions/{param_region}/namespaces/{param_namespace_id}",
        )

        self._throw_on_error(res)
        return None

    async def create_credential(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        permissions: Optional[Permissions] = None,
    ) -> Credential:
        """
        Create a set of credentials for a specific namespace.
        :param region: Region to target. If none is passed will use default region from the config
        :param namespace_id: Namespace containing the Credential
        :param name: Credential name
        :param permissions: List of permissions associated to this Credential.

        One-of ('optional_permissions'): at most one of 'permissions' could be set.
        :return: :class:`Credential <Credential>`

        Usage:
        ::

            result = await api.create_credential(namespace_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/mnq/v1alpha1/regions/{param_region}/credentials",
            body=marshal_CreateCredentialRequest(
                CreateCredentialRequest(
                    namespace_id=namespace_id,
                    region=region,
                    name=name or random_name(prefix="mnq"),
                    permissions=permissions,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Credential(res.json())

    async def delete_credential(
        self,
        *,
        credential_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete credentials
        :param region: Region to target. If none is passed will use default region from the config
        :param credential_id: ID of the Credential to delete

        Usage:
        ::

            result = await api.delete_credential(credential_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_credential_id = validate_path_param("credential_id", credential_id)

        res = self._request(
            "DELETE",
            f"/mnq/v1alpha1/regions/{param_region}/credentials/{param_credential_id}",
        )

        self._throw_on_error(res)
        return None

    async def list_credentials(
        self,
        *,
        region: Optional[Region] = None,
        namespace_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListCredentialsRequestOrderBy = ListCredentialsRequestOrderBy.ID_ASC,
    ) -> ListCredentialsResponse:
        """
        List credentials
        :param region: Region to target. If none is passed will use default region from the config
        :param namespace_id: Namespace containing the Credential
        :param page: Indicate the page number of results to be returned
        :param page_size: Maximum number of results returned by page
        :param order_by: Field used for sorting results
        :return: :class:`ListCredentialsResponse <ListCredentialsResponse>`

        Usage:
        ::

            result = await api.list_credentials()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/mnq/v1alpha1/regions/{param_region}/credentials",
            params={
                "namespace_id": namespace_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListCredentialsResponse(res.json())

    async def list_credentials_all(
        self,
        *,
        region: Optional[Region] = None,
        namespace_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListCredentialsRequestOrderBy] = None,
    ) -> List[CredentialSummary]:
        """
        List credentials
        :param region: Region to target. If none is passed will use default region from the config
        :param namespace_id: Namespace containing the Credential
        :param page: Indicate the page number of results to be returned
        :param page_size: Maximum number of results returned by page
        :param order_by: Field used for sorting results
        :return: :class:`List[ListCredentialsResponse] <List[ListCredentialsResponse]>`

        Usage:
        ::

            result = await api.list_credentials_all()
        """

        return await fetch_all_pages_async(
            type=ListCredentialsResponse,
            key="credentials",
            fetcher=self.list_credentials,
            args={
                "region": region,
                "namespace_id": namespace_id,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def update_credential(
        self,
        *,
        credential_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        permissions: Optional[Permissions] = None,
    ) -> Credential:
        """
        Update a set of credentials.
        :param region: Region to target. If none is passed will use default region from the config
        :param credential_id: ID of the Credential to update
        :param name: Credential name
        :param permissions: List of permissions associated to this Credential.

        One-of ('optional_permissions'): at most one of 'permissions' could be set.
        :return: :class:`Credential <Credential>`

        Usage:
        ::

            result = await api.update_credential(credential_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_credential_id = validate_path_param("credential_id", credential_id)

        res = self._request(
            "PATCH",
            f"/mnq/v1alpha1/regions/{param_region}/credentials/{param_credential_id}",
            body=marshal_UpdateCredentialRequest(
                UpdateCredentialRequest(
                    credential_id=credential_id,
                    region=region,
                    name=name,
                    permissions=permissions,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Credential(res.json())

    async def get_credential(
        self,
        *,
        credential_id: str,
        region: Optional[Region] = None,
    ) -> Credential:
        """
        Get a set of credentials
        :param region: Region to target. If none is passed will use default region from the config
        :param credential_id: ID of the Credential to get
        :return: :class:`Credential <Credential>`

        Usage:
        ::

            result = await api.get_credential(credential_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_credential_id = validate_path_param("credential_id", credential_id)

        res = self._request(
            "GET",
            f"/mnq/v1alpha1/regions/{param_region}/credentials/{param_credential_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Credential(res.json())
