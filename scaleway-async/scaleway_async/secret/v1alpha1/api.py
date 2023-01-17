# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    fetch_all_pages_async,
    validate_path_param,
)
from .types import (
    ListSecretsRequestOrderBy,
    AccessSecretVersionResponse,
    ListSecretVersionsResponse,
    ListSecretsResponse,
    Secret,
    SecretVersion,
    CreateSecretRequest,
    UpdateSecretRequest,
    CreateSecretVersionRequest,
    UpdateSecretVersionRequest,
)
from .marshalling import (
    marshal_CreateSecretRequest,
    marshal_CreateSecretVersionRequest,
    marshal_UpdateSecretRequest,
    marshal_UpdateSecretVersionRequest,
    unmarshal_Secret,
    unmarshal_SecretVersion,
    unmarshal_AccessSecretVersionResponse,
    unmarshal_ListSecretVersionsResponse,
    unmarshal_ListSecretsResponse,
)


class SecretV1Alpha1API(API):
    """
    Secret API (beta).

    This API allows you to conveniently store, access and share sensitive data.
    """

    async def create_secret(
        self,
        *,
        name: str,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        description: Optional[str] = None,
    ) -> Secret:
        """
        Create a Secret containing no versions
        :param region: Region to target. If none is passed will use default region from the config
        :param project_id: ID of the project containing the Secret
        :param name: Name of the Secret
        :param tags: List of tags associated to this Secret
        :param description: Description of the Secret
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = await api.create_secret(name="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets",
            body=marshal_CreateSecretRequest(
                CreateSecretRequest(
                    name=name,
                    region=region,
                    project_id=project_id,
                    tags=tags,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())

    async def get_secret(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
    ) -> Secret:
        """
        Get metadata of a Secret
        :param region: Region to target. If none is passed will use default region from the config
        :param secret_id: ID of the Secret
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = await api.get_secret(secret_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())

    async def update_secret(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        description: Optional[str] = None,
    ) -> Secret:
        """
        Update metadata of a Secret
        :param region: Region to target. If none is passed will use default region from the config
        :param secret_id: ID of the Secret
        :param name: New name of the Secret (optional)
        :param tags: New list of tags associated to this Secret (optional)
        :param description: Description of the Secret
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = await api.update_secret(secret_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "PATCH",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}",
            body=marshal_UpdateSecretRequest(
                UpdateSecretRequest(
                    secret_id=secret_id,
                    region=region,
                    name=name,
                    tags=tags,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())

    async def list_secrets(
        self,
        *,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        order_by: ListSecretsRequestOrderBy = ListSecretsRequestOrderBy.NAME_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListSecretsResponse:
        """
        List Secrets
        :param region: Region to target. If none is passed will use default region from the config
        :param organization_id: ID of an organization to filter on (optional)
        :param project_id: ID of a project to filter on (optional)
        :param tags: List of tags to filter on (optional)
        :param order_by:
        :param page:
        :param page_size:
        :return: :class:`ListSecretsResponse <ListSecretsResponse>`

        Usage:
        ::

            result = await api.list_secrets()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets",
            params={
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
        return unmarshal_ListSecretsResponse(res.json())

    async def list_secrets_all(
        self,
        *,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        order_by: Optional[ListSecretsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[Secret]:
        """
        List Secrets
        :param region: Region to target. If none is passed will use default region from the config
        :param organization_id: ID of an organization to filter on (optional)
        :param project_id: ID of a project to filter on (optional)
        :param tags: List of tags to filter on (optional)
        :param order_by:
        :param page:
        :param page_size:
        :return: :class:`List[ListSecretsResponse] <List[ListSecretsResponse]>`

        Usage:
        ::

            result = await api.list_secrets_all()
        """

        return await fetch_all_pages_async(
            type=ListSecretsResponse,
            key="secrets",
            fetcher=self.list_secrets,
            args={
                "region": region,
                "organization_id": organization_id,
                "project_id": project_id,
                "tags": tags,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    async def delete_secret(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a secret
        :param region: Region to target. If none is passed will use default region from the config
        :param secret_id: ID of the Secret

        Usage:
        ::

            result = await api.delete_secret(secret_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "DELETE",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}",
        )

        self._throw_on_error(res)
        return None

    async def create_secret_version(
        self,
        *,
        secret_id: str,
        data: str,
        region: Optional[Region] = None,
        description: Optional[str] = None,
    ) -> SecretVersion:
        """
        Create a SecretVersion
        :param region: Region to target. If none is passed will use default region from the config
        :param secret_id: ID of the Secret
        :param data: The base64-encoded secret payload of the SecretVersion
        :param description: Description of the SecretVersion
        :return: :class:`SecretVersion <SecretVersion>`

        Usage:
        ::

            result = await api.create_secret_version(
                secret_id="example",
                data="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "POST",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/versions",
            body=marshal_CreateSecretVersionRequest(
                CreateSecretVersionRequest(
                    secret_id=secret_id,
                    data=data,
                    region=region,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())

    async def get_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[Region] = None,
    ) -> SecretVersion:
        """
        Get metadata of a SecretVersion
        :param region: Region to target. If none is passed will use default region from the config
        :param secret_id: ID of the Secret
        :param revision: Revision of the SecretVersion (may be a number or "latest")
        :return: :class:`SecretVersion <SecretVersion>`

        Usage:
        ::

            result = await api.get_secret_version(
                secret_id="example",
                revision="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)
        param_revision = validate_path_param("revision", revision)

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}",
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())

    async def update_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[Region] = None,
        description: Optional[str] = None,
    ) -> SecretVersion:
        """
        Update metadata of a SecretVersion
        :param region: Region to target. If none is passed will use default region from the config
        :param secret_id: ID of the Secret
        :param revision: Revision of the SecretVersion (may be a number or "latest")
        :param description: Description of the SecretVersion
        :return: :class:`SecretVersion <SecretVersion>`

        Usage:
        ::

            result = await api.update_secret_version(
                secret_id="example",
                revision="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)
        param_revision = validate_path_param("revision", revision)

        res = self._request(
            "PATCH",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}",
            body=marshal_UpdateSecretVersionRequest(
                UpdateSecretVersionRequest(
                    secret_id=secret_id,
                    revision=revision,
                    region=region,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())

    async def list_secret_versions(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListSecretVersionsResponse:
        """
        List versions of a secret, not returning any sensitive data
        :param region: Region to target. If none is passed will use default region from the config
        :param secret_id: ID of the Secret
        :param page:
        :param page_size:
        :return: :class:`ListSecretVersionsResponse <ListSecretVersionsResponse>`

        Usage:
        ::

            result = await api.list_secret_versions(secret_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/versions",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSecretVersionsResponse(res.json())

    async def list_secret_versions_all(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SecretVersion]:
        """
        List versions of a secret, not returning any sensitive data
        :param region: Region to target. If none is passed will use default region from the config
        :param secret_id: ID of the Secret
        :param page:
        :param page_size:
        :return: :class:`List[ListSecretVersionsResponse] <List[ListSecretVersionsResponse]>`

        Usage:
        ::

            result = await api.list_secret_versions_all(secret_id="example")
        """

        return await fetch_all_pages_async(
            type=ListSecretVersionsResponse,
            key="versions",
            fetcher=self.list_secret_versions,
            args={
                "secret_id": secret_id,
                "region": region,
                "page": page,
                "page_size": page_size,
            },
        )

    async def destroy_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[Region] = None,
    ) -> SecretVersion:
        """
        Destroy a SecretVersion, permanently destroying the sensitive data
        :param region: Region to target. If none is passed will use default region from the config
        :param secret_id: ID of the Secret
        :param revision: Revision of the SecretVersion (may be a number or "latest")
        :return: :class:`SecretVersion <SecretVersion>`

        Usage:
        ::

            result = await api.destroy_secret_version(
                secret_id="example",
                revision="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)
        param_revision = validate_path_param("revision", revision)

        res = self._request(
            "POST",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}/destroy",
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())

    async def enable_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[Region] = None,
    ) -> SecretVersion:
        """
        Enable a SecretVersion
        :param region: Region to target. If none is passed will use default region from the config
        :param secret_id: ID of the Secret
        :param revision: Revision of the SecretVersion (may be a number or "latest")
        :return: :class:`SecretVersion <SecretVersion>`

        Usage:
        ::

            result = await api.enable_secret_version(
                secret_id="example",
                revision="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)
        param_revision = validate_path_param("revision", revision)

        res = self._request(
            "POST",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}/enable",
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())

    async def disable_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[Region] = None,
    ) -> SecretVersion:
        """
        Disable a SecretVersion
        :param region: Region to target. If none is passed will use default region from the config
        :param secret_id: ID of the Secret
        :param revision: Revision of the SecretVersion (may be a number or "latest")
        :return: :class:`SecretVersion <SecretVersion>`

        Usage:
        ::

            result = await api.disable_secret_version(
                secret_id="example",
                revision="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)
        param_revision = validate_path_param("revision", revision)

        res = self._request(
            "POST",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}/disable",
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())

    async def access_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[Region] = None,
    ) -> AccessSecretVersionResponse:
        """
        Access a SecretVersion, returning the sensitive data
        :param region: Region to target. If none is passed will use default region from the config
        :param secret_id: ID of the Secret
        :param revision: Revision of the SecretVersion (may be a number or "latest")
        :return: :class:`AccessSecretVersionResponse <AccessSecretVersionResponse>`

        Usage:
        ::

            result = await api.access_secret_version(
                secret_id="example",
                revision="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)
        param_revision = validate_path_param("revision", revision)

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}/access",
        )

        self._throw_on_error(res)
        return unmarshal_AccessSecretVersionResponse(res.json())
