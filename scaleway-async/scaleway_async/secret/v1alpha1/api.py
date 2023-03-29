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
    SecretVersionStatus,
    AccessSecretVersionResponse,
    ListSecretVersionsResponse,
    ListSecretsResponse,
    PasswordGenerationParams,
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
    Secret Manager API documentation.

    This API allows you to conveniently store, access and share sensitive data.
    Secret Manager API documentation.
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
        Create a secret.
        You must sepcify the `region` to create a secret.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project containing the secret.
        :param name: Name of the secret.
        :param tags: List of the secret's tags.
        :param description: Description of the secret.
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
        Get metadata using the secret's name.
        Retrieve the metadata of a secret specified by the `region` and the `secret_name` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
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

    async def get_secret_by_name(
        self,
        *,
        secret_name: str,
        region: Optional[Region] = None,
    ) -> Secret:
        """
        Get metadata using the secret's ID.
        Retrieve the metadata of a secret specified by the `region` and the `secret_id` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_name: Name of the secret.
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = await api.get_secret_by_name(secret_name="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_name = validate_path_param("secret_name", secret_name)

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets-by-name/{param_secret_name}",
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
        Update metadata of a secret.
        Edit a secret's metadata such as name, tag(s) and description. The secret to update is specified by the `secret_id` and `region` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param name: Secret's updated name (optional).
        :param tags: Secret's updated list of tags (optional).
        :param description: Description of the secret.
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
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        order_by: ListSecretsRequestOrderBy = ListSecretsRequestOrderBy.NAME_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListSecretsResponse:
        """
        List secrets.
        Retrieve the list of secrets created within an Organization and/or Project. You must specify either the `organization_id` or the `project_id` and the `region`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Filter by Organization ID (optional).
        :param project_id: Filter by Project ID (optional).
        :param name: Filter by secret name (optional).
        :param tags: List of tags to filter on (optional).
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
        return unmarshal_ListSecretsResponse(res.json())

    async def list_secrets_all(
        self,
        *,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        order_by: Optional[ListSecretsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[Secret]:
        """
        List secrets.
        Retrieve the list of secrets created within an Organization and/or Project. You must specify either the `organization_id` or the `project_id` and the `region`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Filter by Organization ID (optional).
        :param project_id: Filter by Project ID (optional).
        :param name: Filter by secret name (optional).
        :param tags: List of tags to filter on (optional).
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
                "name": name,
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
        Delete a secret.
        Delete a given secret specified by the `region` and `secret_id` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.

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
        disable_previous: bool,
        region: Optional[Region] = None,
        description: Optional[str] = None,
        password_generation: Optional[PasswordGenerationParams] = None,
    ) -> SecretVersion:
        """
        Create a version.
        Create a version of a given secret specified by the `region` and `secret_id` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param data: The base64-encoded secret payload of the version.
        :param description: Description of the version.
        :param disable_previous: Disable the previous secret version.
        If there is no previous version or if the previous version was already disabled, does nothing.
        :param password_generation: Options to generate a password.
        If specified, a random password will be generated. The data field must be empty.
        By default, the generator will use upper and lower case letters, and digits.
        This behavior can be tuned using the generation params.

        One-of ('_password_generation'): at most one of 'password_generation' could be set.
        :return: :class:`SecretVersion <SecretVersion>`

        Usage:
        ::

            result = await api.create_secret_version(
                secret_id="example",
                data="example",
                disable_previous=True,
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
                    disable_previous=disable_previous,
                    region=region,
                    description=description,
                    password_generation=password_generation,
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
        Get metadata of a secret's version using the secret's ID.
        Retrieve the metadata of a secret's given version specified by the `region`, `secret_id` and `revision` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param revision: Version number. The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be a number or "latest".
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

    async def get_secret_version_by_name(
        self,
        *,
        secret_name: str,
        revision: str,
        region: Optional[Region] = None,
    ) -> SecretVersion:
        """
        Get metadata of a secret's version using the secret's name.
        Retrieve the metadata of a secret's given version specified by the `region`, `secret_name` and `revision` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_name: Name of the secret.
        :param revision: Version number. The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be a number or "latest".
        :return: :class:`SecretVersion <SecretVersion>`

        Usage:
        ::

            result = await api.get_secret_version_by_name(
                secret_name="example",
                revision="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_name = validate_path_param("secret_name", secret_name)
        param_revision = validate_path_param("revision", revision)

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets-by-name/{param_secret_name}/versions/{param_revision}",
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
        Update metadata of a version.
        Edit the metadata of a secret's given version, specified by the `region`, `secret_id` and `revision` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param revision: Version number. The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be a number or "latest".
        :param description: Description of the version.
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
        status: Optional[List[SecretVersionStatus]] = None,
    ) -> ListSecretVersionsResponse:
        """
        List versions of a secret using the secret's ID.
        Retrieve the list of a given secret's versions specified by the `secret_id` and `region` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param page:
        :param page_size:
        :param status: Filter results by status.
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
                "status": status,
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
        status: Optional[List[SecretVersionStatus]] = None,
    ) -> List[SecretVersion]:
        """
        List versions of a secret using the secret's ID.
        Retrieve the list of a given secret's versions specified by the `secret_id` and `region` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param page:
        :param page_size:
        :param status: Filter results by status.
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
                "status": status,
            },
        )

    async def list_secret_versions_by_name(
        self,
        *,
        secret_name: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        status: Optional[List[SecretVersionStatus]] = None,
    ) -> ListSecretVersionsResponse:
        """
        List versions of a secret using the secret's name.
        Retrieve the list of a given secret's versions specified by the `secret_name` and `region` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_name: Name of the secret.
        :param page:
        :param page_size:
        :param status: Filter results by status.
        :return: :class:`ListSecretVersionsResponse <ListSecretVersionsResponse>`

        Usage:
        ::

            result = await api.list_secret_versions_by_name(secret_name="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_name = validate_path_param("secret_name", secret_name)

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets-by-name/{param_secret_name}/versions",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "status": status,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSecretVersionsResponse(res.json())

    async def list_secret_versions_by_name_all(
        self,
        *,
        secret_name: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        status: Optional[List[SecretVersionStatus]] = None,
    ) -> List[SecretVersion]:
        """
        List versions of a secret using the secret's name.
        Retrieve the list of a given secret's versions specified by the `secret_name` and `region` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_name: Name of the secret.
        :param page:
        :param page_size:
        :param status: Filter results by status.
        :return: :class:`List[ListSecretVersionsResponse] <List[ListSecretVersionsResponse]>`

        Usage:
        ::

            result = await api.list_secret_versions_by_name_all(secret_name="example")
        """

        return await fetch_all_pages_async(
            type=ListSecretVersionsResponse,
            key="versions",
            fetcher=self.list_secret_versions_by_name,
            args={
                "secret_name": secret_name,
                "region": region,
                "page": page,
                "page_size": page_size,
                "status": status,
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
        Delete a version.
        Delete a secret's version and the sensitive data contained in it. Deleting a version is permanent and cannot be undone.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param revision: Version number. The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be a number or "latest".
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
        Enable a version.
        Make a specific version accessible. You must specify the `region`, `secret_id` and `revision` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param revision: Version number. The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be a number or "latest".
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
        Disable a version.
        Make a specific version inaccessible. You must specify the `region`, `secret_id` and `revision` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param revision: Version number. The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be a number or "latest".
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
        Access a secret's version using the secret's ID.
        Access sensitive data in a secret's version specified by the `region`, `secret_id` and `revision` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param revision: Version number. The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be a number or "latest".
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

    async def access_secret_version_by_name(
        self,
        *,
        secret_name: str,
        revision: str,
        region: Optional[Region] = None,
    ) -> AccessSecretVersionResponse:
        """
        Access a secret's version using the secret's name.
        Access sensitive data in a secret's version specified by the `region`, `secret_name` and `revision` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_name: Name of the secret.
        :param revision: Version number. The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be a number or "latest".
        :return: :class:`AccessSecretVersionResponse <AccessSecretVersionResponse>`

        Usage:
        ::

            result = await api.access_secret_version_by_name(
                secret_name="example",
                revision="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_name = validate_path_param("secret_name", secret_name)
        param_revision = validate_path_param("revision", revision)

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets-by-name/{param_secret_name}/versions/{param_revision}/access",
        )

        self._throw_on_error(res)
        return unmarshal_AccessSecretVersionResponse(res.json())
