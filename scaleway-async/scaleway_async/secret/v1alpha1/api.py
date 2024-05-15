# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    validate_path_param,
    fetch_all_pages_async,
)
from .types import (
    ListFoldersRequestOrderBy,
    ListSecretsRequestOrderBy,
    Product,
    SecretType,
    SecretVersionStatus,
    AccessSecretVersionResponse,
    AddSecretOwnerRequest,
    CreateFolderRequest,
    CreateSecretRequest,
    CreateSecretVersionRequest,
    EphemeralPolicy,
    EphemeralProperties,
    Folder,
    GeneratePasswordRequest,
    ListFoldersResponse,
    ListSecretVersionsResponse,
    ListSecretsResponse,
    ListTagsResponse,
    PasswordGenerationParams,
    Secret,
    SecretVersion,
    UpdateSecretRequest,
    UpdateSecretVersionRequest,
)
from .marshalling import (
    unmarshal_Folder,
    unmarshal_SecretVersion,
    unmarshal_Secret,
    unmarshal_AccessSecretVersionResponse,
    unmarshal_ListFoldersResponse,
    unmarshal_ListSecretVersionsResponse,
    unmarshal_ListSecretsResponse,
    unmarshal_ListTagsResponse,
    marshal_AddSecretOwnerRequest,
    marshal_CreateFolderRequest,
    marshal_CreateSecretRequest,
    marshal_CreateSecretVersionRequest,
    marshal_GeneratePasswordRequest,
    marshal_UpdateSecretRequest,
    marshal_UpdateSecretVersionRequest,
)


class SecretV1Alpha1API(API):
    """
    This API allows you to manage your Secret Manager services, for storing, accessing and sharing sensitive data such as passwords, API keys and certificates.
    """

    async def create_secret(
        self,
        *,
        name: str,
        is_protected: bool,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        description: Optional[str] = None,
        type_: Optional[SecretType] = None,
        path: Optional[str] = None,
        ephemeral_policy: Optional[EphemeralPolicy] = None,
    ) -> Secret:
        """
        Create a secret.
        You must specify the `region` to create a secret.
        :param name: Name of the secret.
        :param is_protected: A protected secret cannot be deleted.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project containing the secret.
        :param tags: List of the secret's tags.
        :param description: Description of the secret.
        :param type_: (Optional.) See `Secret.Type` enum for description of values. If not specified, the type is `Opaque`.
        :param path: (Optional.) Location of the secret in the directory structure. If not specified, the path is `/`.
        :param ephemeral_policy: (Optional.) Policy that defines whether/when a secret's versions expire. By default, the policy is applied to all the secret's versions.
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = await api.create_secret(
                name="example",
                is_protected=False,
            )
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
                    is_protected=is_protected,
                    region=region,
                    project_id=project_id,
                    tags=tags,
                    description=description,
                    type_=type_,
                    path=path,
                    ephemeral_policy=ephemeral_policy,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())

    async def create_folder(
        self,
        *,
        name: str,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        path: Optional[str] = None,
    ) -> Folder:
        """
        Create folder.
        :param name: Name of the folder.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project containing the folder.
        :param path: (Optional.) Location of the folder in the directory structure. If not specified, the path is `/`.
        :return: :class:`Folder <Folder>`

        Usage:
        ::

            result = await api.create_folder(
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/secret-manager/v1alpha1/regions/{param_region}/folders",
            body=marshal_CreateFolderRequest(
                CreateFolderRequest(
                    name=name,
                    region=region,
                    project_id=project_id,
                    path=path,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Folder(res.json())

    async def get_secret(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
    ) -> Secret:
        """
        Get metadata using the secret's ID.
        Retrieve the metadata of a secret specified by the `region` and `secret_id` parameters.
        :param secret_id: ID of the secret.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = await api.get_secret(
                secret_id="example",
            )
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
        project_id: Optional[str] = None,
    ) -> Secret:
        """
        Get metadata using the secret's name.
        Retrieve the metadata of a secret specified by the `region` and `secret_name` parameters.

        GetSecretByName usage is now deprecated.

        Scaleway recommends that you use the `ListSecrets` request with the `name` filter.
        :param secret_name: Name of the secret.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: (Optional.) If not specified, Secret Manager will look for the secret in all Projects.
        :return: :class:`Secret <Secret>`
        :deprecated

        Usage:
        ::

            result = await api.get_secret_by_name(
                secret_name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_name = validate_path_param("secret_name", secret_name)

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets-by-name/{param_secret_name}",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
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
        path: Optional[str] = None,
        ephemeral_policy: Optional[EphemeralPolicy] = None,
    ) -> Secret:
        """
        Update metadata of a secret.
        Edit a secret's metadata such as name, tag(s), description and ephemeral policy. The secret to update is specified by the `secret_id` and `region` parameters.
        :param secret_id: ID of the secret.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Secret's updated name (optional).
        :param tags: Secret's updated list of tags (optional).
        :param description: Description of the secret.
        :param path: (Optional.) Location of the folder in the directory structure. If not specified, the path is `/`.
        :param ephemeral_policy: (Optional.) Policy that defines whether/when a secret's versions expire.
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = await api.update_secret(
                secret_id="example",
            )
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
                    path=path,
                    ephemeral_policy=ephemeral_policy,
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
        order_by: Optional[ListSecretsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
        is_managed: Optional[bool] = None,
        path: Optional[str] = None,
        is_ephemeral: Optional[bool] = None,
    ) -> ListSecretsResponse:
        """
        List secrets.
        Retrieve the list of secrets created within an Organization and/or Project. You must specify either the `organization_id` or the `project_id` and the `region`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Filter by Organization ID (optional).
        :param project_id: Filter by Project ID (optional).
        :param order_by:
        :param page:
        :param page_size:
        :param tags: List of tags to filter on (optional).
        :param name: Filter by secret name (optional).
        :param is_managed: Filter by managed / not managed (optional).
        :param path: Filter by path (optional).
        :param is_ephemeral: Filter by ephemeral / not ephemeral (optional).
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
                "is_ephemeral": is_ephemeral,
                "is_managed": is_managed,
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "path": path,
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
        order_by: Optional[ListSecretsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
        is_managed: Optional[bool] = None,
        path: Optional[str] = None,
        is_ephemeral: Optional[bool] = None,
    ) -> List[Secret]:
        """
        List secrets.
        Retrieve the list of secrets created within an Organization and/or Project. You must specify either the `organization_id` or the `project_id` and the `region`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Filter by Organization ID (optional).
        :param project_id: Filter by Project ID (optional).
        :param order_by:
        :param page:
        :param page_size:
        :param tags: List of tags to filter on (optional).
        :param name: Filter by secret name (optional).
        :param is_managed: Filter by managed / not managed (optional).
        :param path: Filter by path (optional).
        :param is_ephemeral: Filter by ephemeral / not ephemeral (optional).
        :return: :class:`List[Secret] <List[Secret]>`

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
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "tags": tags,
                "name": name,
                "is_managed": is_managed,
                "path": path,
                "is_ephemeral": is_ephemeral,
            },
        )

    async def list_folders(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        path: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListFoldersRequestOrderBy] = None,
    ) -> ListFoldersResponse:
        """
        List folders.
        Retrieve the list of folders created within a Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Filter by Project ID (optional).
        :param path: Filter by path (optional).
        :param page:
        :param page_size:
        :param order_by:
        :return: :class:`ListFoldersResponse <ListFoldersResponse>`

        Usage:
        ::

            result = await api.list_folders()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/folders",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "path": path,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListFoldersResponse(res.json())

    async def list_folders_all(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        path: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListFoldersRequestOrderBy] = None,
    ) -> List[Folder]:
        """
        List folders.
        Retrieve the list of folders created within a Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Filter by Project ID (optional).
        :param path: Filter by path (optional).
        :param page:
        :param page_size:
        :param order_by:
        :return: :class:`List[Folder] <List[Folder]>`

        Usage:
        ::

            result = await api.list_folders_all()
        """

        return await fetch_all_pages_async(
            type=ListFoldersResponse,
            key="folders",
            fetcher=self.list_folders,
            args={
                "region": region,
                "project_id": project_id,
                "path": path,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def delete_secret(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete a secret.
        Delete a given secret specified by the `region` and `secret_id` parameters.
        :param secret_id: ID of the secret.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_secret(
                secret_id="example",
            )
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

    async def delete_folder(
        self,
        *,
        folder_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete a given folder specified by the `region` and `folder_id` parameters.
        :param folder_id: ID of the folder.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_folder(
                folder_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_folder_id = validate_path_param("folder_id", folder_id)

        res = self._request(
            "DELETE",
            f"/secret-manager/v1alpha1/regions/{param_region}/folders/{param_folder_id}",
        )

        self._throw_on_error(res)

    async def protect_secret(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
    ) -> Secret:
        """
        Protect a secret.
        Protect a given secret specified by the `secret_id` parameter. A protected secret can be read and modified but cannot be deleted.
        :param secret_id: ID of the secret to protect.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = await api.protect_secret(
                secret_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "POST",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/protect",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())

    async def unprotect_secret(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
    ) -> Secret:
        """
        Unprotect a secret.
        Unprotect a given secret specified by the `secret_id` parameter. An unprotected secret can be read, modified and deleted.
        :param secret_id: ID of the secret to unprotect.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = await api.unprotect_secret(
                secret_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "POST",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/unprotect",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())

    async def add_secret_owner(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
        product_name: Optional[str] = None,
        product: Optional[Product] = None,
    ) -> None:
        """
        Allow a product to use the secret.
        :param secret_id: ID of the secret.
        :param region: Region to target. If none is passed will use default region from the config.
        :param product_name: (Deprecated: use `product` field) Name of the product to add.
        :param product: See `Product` enum for description of values.

        Usage:
        ::

            result = await api.add_secret_owner(
                secret_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "POST",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/add-owner",
            body=marshal_AddSecretOwnerRequest(
                AddSecretOwnerRequest(
                    secret_id=secret_id,
                    region=region,
                    product_name=product_name,
                    product=product,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def create_secret_version(
        self,
        *,
        secret_id: str,
        data: str,
        region: Optional[Region] = None,
        description: Optional[str] = None,
        disable_previous: Optional[bool] = None,
        password_generation: Optional[PasswordGenerationParams] = None,
        data_crc32: Optional[int] = None,
    ) -> SecretVersion:
        """
        Create a version.
        Create a version of a given secret specified by the `region` and `secret_id` parameters.
        :param secret_id: ID of the secret.
        :param data: The base64-encoded secret payload of the version.
        :param region: Region to target. If none is passed will use default region from the config.
        :param description: Description of the version.
        :param disable_previous: (Optional.) If there is no previous version or if the previous version was already disabled, does nothing.
        :param password_generation: (Optional.) If specified, a random password will be generated. The `data` and `data_crc32` fields must be empty. By default, the generator will use upper and lower case letters, and digits. This behavior can be tuned using the generation parameters.
        :param data_crc32: If specified, Secret Manager will verify the integrity of the data received against the given CRC32 checksum. An error is returned if the CRC32 does not match. If, however, the CRC32 matches, it will be stored and returned along with the SecretVersion on future access requests.
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
                    disable_previous=disable_previous,
                    password_generation=password_generation,
                    data_crc32=data_crc32,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())

    async def generate_password(
        self,
        *,
        secret_id: str,
        length: int,
        region: Optional[Region] = None,
        description: Optional[str] = None,
        disable_previous: Optional[bool] = None,
        no_lowercase_letters: Optional[bool] = None,
        no_uppercase_letters: Optional[bool] = None,
        no_digits: Optional[bool] = None,
        additional_chars: Optional[str] = None,
    ) -> SecretVersion:
        """
        Generate a password in a new version.
        Generate a password for the given secret specified by the `region` and `secret_id` parameters. This will also create a new version of the secret that will store the password.
        :param secret_id: ID of the secret.
        :param length: Length of the password to generate (between 1 and 1024 characters).
        :param region: Region to target. If none is passed will use default region from the config.
        :param description: Description of the version.
        :param disable_previous: This has no effect if there is no previous version or if the previous version was already disabled.
        :param no_lowercase_letters: (Optional.) Exclude lower case letters by default in the password character set.
        :param no_uppercase_letters: (Optional.) Exclude upper case letters by default in the password character set.
        :param no_digits: (Optional.) Exclude digits by default in the password character set.
        :param additional_chars: (Optional.) Additional ASCII characters to be included in the password character set.
        :return: :class:`SecretVersion <SecretVersion>`

        Usage:
        ::

            result = await api.generate_password(
                secret_id="example",
                length=1,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "POST",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/generate-password",
            body=marshal_GeneratePasswordRequest(
                GeneratePasswordRequest(
                    secret_id=secret_id,
                    length=length,
                    region=region,
                    description=description,
                    disable_previous=disable_previous,
                    no_lowercase_letters=no_lowercase_letters,
                    no_uppercase_letters=no_uppercase_letters,
                    no_digits=no_digits,
                    additional_chars=additional_chars,
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
        :param secret_id: ID of the secret.
        :param revision: The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :param region: Region to target. If none is passed will use default region from the config.
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
        project_id: Optional[str] = None,
    ) -> SecretVersion:
        """
        Get metadata of a secret's version using the secret's name.
        Retrieve the metadata of a secret's given version specified by the `region`, `secret_name`, `revision` and `project_id` parameters.

        This method is deprecated.

        Scaleway recommends that you use the `ListSecrets` request with the `name` filter to specify the secret version desired, then use the `GetSecretVersion` request.
        :param secret_name: Name of the secret.
        :param revision: The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: (Optional.) If not specified, Secret Manager will look for the secret version in all Projects.
        :return: :class:`SecretVersion <SecretVersion>`
        :deprecated

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
            params={
                "project_id": project_id or self.client.default_project_id,
            },
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
        ephemeral_properties: Optional[EphemeralProperties] = None,
    ) -> SecretVersion:
        """
        Update metadata of a version.
        Edit the metadata of a secret's given version, specified by the `region`, `secret_id` and `revision` parameters.
        :param secret_id: ID of the secret.
        :param revision: The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :param region: Region to target. If none is passed will use default region from the config.
        :param description: Description of the version.
        :param ephemeral_properties: (Optional.) Properties that defines the version's expiration date, whether it expires after being accessed once, and the action to perform (disable or delete) once the version expires.
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
                    ephemeral_properties=ephemeral_properties,
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
        :param secret_id: ID of the secret.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param status: Filter results by status.
        :return: :class:`ListSecretVersionsResponse <ListSecretVersionsResponse>`

        Usage:
        ::

            result = await api.list_secret_versions(
                secret_id="example",
            )
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
        :param secret_id: ID of the secret.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param status: Filter results by status.
        :return: :class:`List[SecretVersion] <List[SecretVersion]>`

        Usage:
        ::

            result = await api.list_secret_versions_all(
                secret_id="example",
            )
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
        project_id: Optional[str] = None,
    ) -> ListSecretVersionsResponse:
        """
        List versions of a secret using the secret's name.
        Retrieve the list of a given secret's versions specified by the `secret_name`,`region` and `project_id` parameters.

        This method is deprecated.

        Scaleway recommends that you use the `ListSecrets` request with the `name` filter to specify the secret version desired, then use the `ListSecretVersions` request.
        :param secret_name: Name of the secret.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param status: Filter results by status.
        :param project_id: (Optional.) If not specified, Secret Manager will look for the secret in all Projects.
        :return: :class:`ListSecretVersionsResponse <ListSecretVersionsResponse>`
        :deprecated

        Usage:
        ::

            result = await api.list_secret_versions_by_name(
                secret_name="example",
            )
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
                "project_id": project_id or self.client.default_project_id,
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
        project_id: Optional[str] = None,
    ) -> List[SecretVersion]:
        """
        List versions of a secret using the secret's name.
        Retrieve the list of a given secret's versions specified by the `secret_name`,`region` and `project_id` parameters.

        This method is deprecated.

        Scaleway recommends that you use the `ListSecrets` request with the `name` filter to specify the secret version desired, then use the `ListSecretVersions` request.
        :param secret_name: Name of the secret.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param status: Filter results by status.
        :param project_id: (Optional.) If not specified, Secret Manager will look for the secret in all Projects.
        :return: :class:`List[SecretVersion] <List[SecretVersion]>`
        :deprecated

        Usage:
        ::

            result = await api.list_secret_versions_by_name_all(
                secret_name="example",
            )
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
                "project_id": project_id,
            },
        )

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
        :param secret_id: ID of the secret.
        :param revision: The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :param region: Region to target. If none is passed will use default region from the config.
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
            body={},
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
        :param secret_id: ID of the secret.
        :param revision: The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :param region: Region to target. If none is passed will use default region from the config.
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
            body={},
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
        :param secret_id: ID of the secret.
        :param revision: The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :param region: Region to target. If none is passed will use default region from the config.
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
        project_id: Optional[str] = None,
    ) -> AccessSecretVersionResponse:
        """
        Access a secret's version using the secret's name.
        Access sensitive data in a secret's version specified by the `region`, `secret_name`, `revision` and `project_id` parameters.

        This method is deprecated.

        Scaleway recommends that you use the `ListSecrets` request with the `name` filter to specify the secret version desired, then use the `AccessSecretVersion` request.
        :param secret_name: Name of the secret.
        :param revision: The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: (Optional.) If not specified, Secret Manager will look for the secret version in all Projects.
        :return: :class:`AccessSecretVersionResponse <AccessSecretVersionResponse>`
        :deprecated

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
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_AccessSecretVersionResponse(res.json())

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
        :param secret_id: ID of the secret.
        :param revision: The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :param region: Region to target. If none is passed will use default region from the config.
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
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())

    async def list_tags(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListTagsResponse:
        """
        List tags.
        List all tags associated with secrets within a given Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: (Optional.) If not specified, Secret Manager will look for tags in all Projects.
        :param page:
        :param page_size:
        :return: :class:`ListTagsResponse <ListTagsResponse>`

        Usage:
        ::

            result = await api.list_tags()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/tags",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListTagsResponse(res.json())

    async def list_tags_all(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[str]:
        """
        List tags.
        List all tags associated with secrets within a given Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: (Optional.) If not specified, Secret Manager will look for tags in all Projects.
        :param page:
        :param page_size:
        :return: :class:`List[str] <List[str]>`

        Usage:
        ::

            result = await api.list_tags_all()
        """

        return await fetch_all_pages_async(
            type=ListTagsResponse,
            key="tags",
            fetcher=self.list_tags,
            args={
                "region": region,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
            },
        )
