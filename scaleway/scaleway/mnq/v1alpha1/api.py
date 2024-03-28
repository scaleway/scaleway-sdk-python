# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    random_name,
    validate_path_param,
    fetch_all_pages,
)
from .types import (
    ListCredentialsRequestOrderBy,
    ListNamespacesRequestOrderBy,
    NamespaceProtocol,
    CreateCredentialRequest,
    CreateNamespaceRequest,
    Credential,
    CredentialSummary,
    ListCredentialsResponse,
    ListNamespacesResponse,
    Namespace,
    Permissions,
    UpdateCredentialRequest,
    UpdateNamespaceRequest,
)
from .marshalling import (
    unmarshal_Namespace,
    unmarshal_Credential,
    unmarshal_ListCredentialsResponse,
    unmarshal_ListNamespacesResponse,
    marshal_CreateCredentialRequest,
    marshal_CreateNamespaceRequest,
    marshal_UpdateCredentialRequest,
    marshal_UpdateNamespaceRequest,
)


class MnqV1Alpha1API(API):
    """
    This API allows you to manage Scaleway Messaging and Queueing brokers.
    """

    def list_namespaces(
        self,
        *,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNamespacesRequestOrderBy] = None,
    ) -> ListNamespacesResponse:
        """
        List namespaces.
        List all Messaging and Queuing namespaces in the specified region, for a Scaleway Organization or Project. By default, the namespaces returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Include only namespaces in this Organization.
        :param project_id: Include only namespaces in this Project.
        :param page: Page number to return.
        :param page_size: Maximum number of namespaces to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`ListNamespacesResponse <ListNamespacesResponse>`

        Usage:
        ::

            result = api.list_namespaces()
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

    def list_namespaces_all(
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
        List namespaces.
        List all Messaging and Queuing namespaces in the specified region, for a Scaleway Organization or Project. By default, the namespaces returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Include only namespaces in this Organization.
        :param project_id: Include only namespaces in this Project.
        :param page: Page number to return.
        :param page_size: Maximum number of namespaces to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`List[Namespace] <List[Namespace]>`

        Usage:
        ::

            result = api.list_namespaces_all()
        """

        return fetch_all_pages(
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

    def create_namespace(
        self,
        *,
        protocol: NamespaceProtocol,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> Namespace:
        """
        Create a namespace.
        Create a Messaging and Queuing namespace, set to the desired protocol.
        :param protocol: Namespace protocol. You must specify a valid protocol (and not `unknown`) to avoid an error.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Namespace name.
        :param project_id: Project containing the Namespace.
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = api.create_namespace(
                protocol=NamespaceProtocol.unknown,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/mnq/v1alpha1/regions/{param_region}/namespaces",
            body=marshal_CreateNamespaceRequest(
                CreateNamespaceRequest(
                    protocol=protocol,
                    region=region,
                    name=name or random_name(prefix="mnq"),
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())

    def update_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
    ) -> Namespace:
        """
        Update the name of a namespace.
        Update the name of a Messaging and Queuing namespace, specified by its namespace ID.
        :param namespace_id: ID of the Namespace to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Namespace name.
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = api.update_namespace(
                namespace_id="example",
            )
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

    def get_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
    ) -> Namespace:
        """
        Get a namespace.
        Retrieve information about an existing Messaging and Queuing namespace, identified by its namespace ID. Its full details, including name, endpoint and protocol, are returned in the response.
        :param namespace_id: ID of the Namespace to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = api.get_namespace(
                namespace_id="example",
            )
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

    def delete_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete a namespace.
        Delete a Messaging and Queuing namespace, specified by its namespace ID. Note that deleting a namespace is irreversible, and any URLs, credentials and queued messages belonging to this namespace will also be deleted.
        :param namespace_id: ID of the namespace to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_namespace(
                namespace_id="example",
            )
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

    def create_credential(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        permissions: Optional[Permissions] = None,
    ) -> Credential:
        """
        Create credentials.
        Create a set of credentials for a Messaging and Queuing namespace, specified by its namespace ID. If creating credentials for a NATS namespace, the `permissions` object must not be included in the request. If creating credentials for an SQS/SNS namespace, the `permissions` object is required, with all three of its child attributes.
        :param namespace_id: Namespace containing the credentials.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the credentials.
        :param permissions: Permissions associated with these credentials.
        :return: :class:`Credential <Credential>`

        Usage:
        ::

            result = api.create_credential(
                namespace_id="example",
            )
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

    def delete_credential(
        self,
        *,
        credential_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete credentials.
        Delete a set of credentials, specified by their credential ID. Deleting credentials is irreversible and cannot be undone. The credentials can no longer be used to access the namespace.
        :param credential_id: ID of the credentials to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_credential(
                credential_id="example",
            )
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

    def list_credentials(
        self,
        *,
        region: Optional[Region] = None,
        namespace_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListCredentialsRequestOrderBy] = None,
    ) -> ListCredentialsResponse:
        """
        List credentials.
        List existing credentials in the specified region. The response contains only the metadata for the credentials, not the credentials themselves (for this, use **Get Credentials**).
        :param region: Region to target. If none is passed will use default region from the config.
        :param namespace_id: Namespace containing the credentials.
        :param page: Page number to return.
        :param page_size: Maximum number of credentials to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`ListCredentialsResponse <ListCredentialsResponse>`

        Usage:
        ::

            result = api.list_credentials()
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

    def list_credentials_all(
        self,
        *,
        region: Optional[Region] = None,
        namespace_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListCredentialsRequestOrderBy] = None,
    ) -> List[CredentialSummary]:
        """
        List credentials.
        List existing credentials in the specified region. The response contains only the metadata for the credentials, not the credentials themselves (for this, use **Get Credentials**).
        :param region: Region to target. If none is passed will use default region from the config.
        :param namespace_id: Namespace containing the credentials.
        :param page: Page number to return.
        :param page_size: Maximum number of credentials to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`List[CredentialSummary] <List[CredentialSummary]>`

        Usage:
        ::

            result = api.list_credentials_all()
        """

        return fetch_all_pages(
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

    def update_credential(
        self,
        *,
        credential_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        permissions: Optional[Permissions] = None,
    ) -> Credential:
        """
        Update credentials.
        Update a set of credentials. You can update the credentials' name, or (in the case of SQS/SNS credentials only) their permissions. To update the name of NATS credentials, do not include the `permissions` object in your request.
        :param credential_id: ID of the credentials to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the credentials.
        :param permissions: Permissions associated with these credentials.
        :return: :class:`Credential <Credential>`

        Usage:
        ::

            result = api.update_credential(
                credential_id="example",
            )
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

    def get_credential(
        self,
        *,
        credential_id: str,
        region: Optional[Region] = None,
    ) -> Credential:
        """
        Get credentials.
        Retrieve an existing set of credentials, identified by the `credential_id`. The credentials themselves, as well as their metadata (protocol, namespace ID etc), are returned in the response.
        :param credential_id: ID of the credentials to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Credential <Credential>`

        Usage:
        ::

            result = api.get_credential(
                credential_id="example",
            )
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
