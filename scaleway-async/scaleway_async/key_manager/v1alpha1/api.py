# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    validate_path_param,
    fetch_all_pages_async,
)
from .types import (
    DataKeyAlgorithmSymmetricEncryption,
    KeyOrigin,
    ListAlgorithmsRequestUsage,
    ListKeysRequestOrderBy,
    ListKeysRequestUsage,
    CreateKeyRequest,
    DataKey,
    DecryptRequest,
    DecryptResponse,
    EncryptRequest,
    EncryptResponse,
    GenerateDataKeyRequest,
    ImportKeyMaterialRequest,
    Key,
    KeyRotationPolicy,
    KeyUsage,
    ListAlgorithmsResponse,
    ListKeysResponse,
    PublicKey,
    SignRequest,
    SignResponse,
    UpdateKeyRequest,
    VerifyRequest,
    VerifyResponse,
)
from .marshalling import (
    unmarshal_Key,
    unmarshal_DataKey,
    unmarshal_DecryptResponse,
    unmarshal_EncryptResponse,
    unmarshal_ListAlgorithmsResponse,
    unmarshal_ListKeysResponse,
    unmarshal_PublicKey,
    unmarshal_SignResponse,
    unmarshal_VerifyResponse,
    marshal_CreateKeyRequest,
    marshal_DecryptRequest,
    marshal_EncryptRequest,
    marshal_GenerateDataKeyRequest,
    marshal_ImportKeyMaterialRequest,
    marshal_SignRequest,
    marshal_UpdateKeyRequest,
    marshal_VerifyRequest,
)


class KeyManagerV1Alpha1API(API):
    """
    This API allows you to create, manage and use cryptographic keys in a centralized and secure service.
    """

    async def create_key(
        self,
        *,
        unprotected: bool,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        usage: Optional[KeyUsage] = None,
        description: Optional[str] = None,
        tags: Optional[list[str]] = None,
        rotation_policy: Optional[KeyRotationPolicy] = None,
        origin: Optional[KeyOrigin] = None,
    ) -> Key:
        """
        Create a key.
        Create a key in a given region specified by the `region` parameter. You can use keys to encrypt or decrypt arbitrary payloads, to sign and verify messages or to generate data encryption keys. **Data encryption keys are not stored in Key Manager**.
        :param unprotected: Default value is `false`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project containing the key.
        :param name: (Optional) Name of the key.
        :param usage: See the `Key.Usage` enum for a description of possible values.
        :param description: (Optional) Description of the key.
        :param tags: (Optional) List of the key's tags.
        :param rotation_policy: If not specified, no rotation policy will be applied to the key.
        :param origin: Refer to the `Key.Origin` enum for a description of values.
        :return: :class:`Key <Key>`

        Usage:
        ::

            result = await api.create_key(
                unprotected=False,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/key-manager/v1alpha1/regions/{param_region}/keys",
            body=marshal_CreateKeyRequest(
                CreateKeyRequest(
                    unprotected=unprotected,
                    region=region,
                    project_id=project_id,
                    name=name,
                    usage=usage,
                    description=description,
                    tags=tags,
                    rotation_policy=rotation_policy,
                    origin=origin,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Key(res.json())

    async def get_key(
        self,
        *,
        key_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Key:
        """
        Get key metadata.
        Retrieve metadata for a specified key using the `region` and `key_id` parameters.
        :param key_id: ID of the key to target.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Key <Key>`

        Usage:
        ::

            result = await api.get_key(
                key_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "GET",
            f"/key-manager/v1alpha1/regions/{param_region}/keys/{param_key_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Key(res.json())

    async def get_public_key(
        self,
        *,
        key_id: str,
        region: Optional[ScwRegion] = None,
    ) -> PublicKey:
        """
        Get the public key in PEM format.
        Retrieves the public portion of an asymmetric cryptographic key in PEM format.
        :param key_id: ID of the key.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`PublicKey <PublicKey>`

        Usage:
        ::

            result = await api.get_public_key(
                key_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "GET",
            f"/key-manager/v1alpha1/regions/{param_region}/keys/{param_key_id}/public-key",
        )

        self._throw_on_error(res)
        return unmarshal_PublicKey(res.json())

    async def update_key(
        self,
        *,
        key_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[list[str]] = None,
        rotation_policy: Optional[KeyRotationPolicy] = None,
    ) -> Key:
        """
        Update a key.
        Modify a key's metadata including name, description and tags, specified by the `key_id` and `region` parameters.
        :param key_id: ID of the key to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: (Optional) Updated name of the key.
        :param description: (Optional) Updated description of the key.
        :param tags: (Optional) Updated list of the key's tags.
        :param rotation_policy: If not specified, the key's existing rotation policy applies.
        :return: :class:`Key <Key>`

        Usage:
        ::

            result = await api.update_key(
                key_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "PATCH",
            f"/key-manager/v1alpha1/regions/{param_region}/keys/{param_key_id}",
            body=marshal_UpdateKeyRequest(
                UpdateKeyRequest(
                    key_id=key_id,
                    region=region,
                    name=name,
                    description=description,
                    tags=tags,
                    rotation_policy=rotation_policy,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Key(res.json())

    async def delete_key(
        self,
        *,
        key_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a key.
        Permanently delete a key specified by the `region` and `key_id` parameters. This action is irreversible. Any data encrypted with this key, including data encryption keys, will no longer be decipherable.
        :param key_id: ID of the key to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_key(
                key_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "DELETE",
            f"/key-manager/v1alpha1/regions/{param_region}/keys/{param_key_id}",
        )

        self._throw_on_error(res)

    async def rotate_key(
        self,
        *,
        key_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Key:
        """
        Rotate a key.
        Generate a new version of an existing key with new key material. Previous key versions remain usable to decrypt previously encrypted data, but the key's new version will be used for subsequent encryption operations and data key generation.
        :param key_id: ID of the key to rotate.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Key <Key>`

        Usage:
        ::

            result = await api.rotate_key(
                key_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "POST",
            f"/key-manager/v1alpha1/regions/{param_region}/keys/{param_key_id}/rotate",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Key(res.json())

    async def protect_key(
        self,
        *,
        key_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Key:
        """
        Apply key protection.
        Apply protection to a given key specified by the `key_id` parameter. Applying key protection means that your key can be used and modified, but it cannot be deleted.
        :param key_id: ID of the key to apply key protection to.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Key <Key>`

        Usage:
        ::

            result = await api.protect_key(
                key_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "POST",
            f"/key-manager/v1alpha1/regions/{param_region}/keys/{param_key_id}/protect",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Key(res.json())

    async def unprotect_key(
        self,
        *,
        key_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Key:
        """
        Remove key protection.
        Remove key protection from a given key specified by the `key_id` parameter. Removing key protection means that your key can be deleted anytime.
        :param key_id: ID of the key to remove key protection from.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Key <Key>`

        Usage:
        ::

            result = await api.unprotect_key(
                key_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "POST",
            f"/key-manager/v1alpha1/regions/{param_region}/keys/{param_key_id}/unprotect",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Key(res.json())

    async def enable_key(
        self,
        *,
        key_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Key:
        """
        Enable key.
        Enable a given key to be used for cryptographic operations. Enabling a key allows you to make a disabled key usable again. You must specify the `region` and `key_id` parameters.
        :param key_id: ID of the key to enable.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Key <Key>`

        Usage:
        ::

            result = await api.enable_key(
                key_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "POST",
            f"/key-manager/v1alpha1/regions/{param_region}/keys/{param_key_id}/enable",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Key(res.json())

    async def disable_key(
        self,
        *,
        key_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Key:
        """
        Disable key.
        Disable a given key, preventing it to be used for cryptographic operations. Disabling a key renders it unusable. You must specify the `region` and `key_id` parameters.
        :param key_id: ID of the key to disable.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Key <Key>`

        Usage:
        ::

            result = await api.disable_key(
                key_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "POST",
            f"/key-manager/v1alpha1/regions/{param_region}/keys/{param_key_id}/disable",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Key(res.json())

    async def list_keys(
        self,
        *,
        scheduled_for_deletion: bool,
        region: Optional[ScwRegion] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        order_by: Optional[ListKeysRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        tags: Optional[list[str]] = None,
        name: Optional[str] = None,
        usage: Optional[ListKeysRequestUsage] = None,
    ) -> ListKeysResponse:
        """
        List keys.
        Retrieve a list of keys across all Projects in an Organization or within a specific Project. You must specify the `region`, and either the `organization_id` or the `project_id`.
        :param scheduled_for_deletion: Filter keys based on their deletion status. By default, only keys not scheduled for deletion are returned in the output.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: (Optional) Filter by Organization ID.
        :param project_id: (Optional) Filter by Project ID.
        :param order_by:
        :param page:
        :param page_size:
        :param tags: (Optional) List of tags to filter on.
        :param name: (Optional) Filter by key name.
        :param usage: Select from symmetric encryption, asymmetric encryption, or asymmetric signing.
        :return: :class:`ListKeysResponse <ListKeysResponse>`

        Usage:
        ::

            result = await api.list_keys(
                scheduled_for_deletion=False,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/key-manager/v1alpha1/regions/{param_region}/keys",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "scheduled_for_deletion": scheduled_for_deletion,
                "tags": tags,
                "usage": usage,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListKeysResponse(res.json())

    async def list_keys_all(
        self,
        *,
        scheduled_for_deletion: bool,
        region: Optional[ScwRegion] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        order_by: Optional[ListKeysRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        tags: Optional[list[str]] = None,
        name: Optional[str] = None,
        usage: Optional[ListKeysRequestUsage] = None,
    ) -> list[Key]:
        """
        List keys.
        Retrieve a list of keys across all Projects in an Organization or within a specific Project. You must specify the `region`, and either the `organization_id` or the `project_id`.
        :param scheduled_for_deletion: Filter keys based on their deletion status. By default, only keys not scheduled for deletion are returned in the output.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: (Optional) Filter by Organization ID.
        :param project_id: (Optional) Filter by Project ID.
        :param order_by:
        :param page:
        :param page_size:
        :param tags: (Optional) List of tags to filter on.
        :param name: (Optional) Filter by key name.
        :param usage: Select from symmetric encryption, asymmetric encryption, or asymmetric signing.
        :return: :class:`list[Key] <list[Key]>`

        Usage:
        ::

            result = await api.list_keys_all(
                scheduled_for_deletion=False,
            )
        """

        return await fetch_all_pages_async(
            type=ListKeysResponse,
            key="keys",
            fetcher=self.list_keys,
            args={
                "scheduled_for_deletion": scheduled_for_deletion,
                "region": region,
                "organization_id": organization_id,
                "project_id": project_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "tags": tags,
                "name": name,
                "usage": usage,
            },
        )

    async def generate_data_key(
        self,
        *,
        key_id: str,
        without_plaintext: bool,
        region: Optional[ScwRegion] = None,
        algorithm: Optional[DataKeyAlgorithmSymmetricEncryption] = None,
    ) -> DataKey:
        """
        Create a data encryption key.
        Create a new data encryption key for cryptographic operations outside of Key Manager. The data encryption key is encrypted and must be decrypted using the key you have created in Key Manager.

        The data encryption key is returned in plaintext and ciphertext but it should only be stored in its encrypted form (ciphertext). Key Manager does not store your data encryption key. To retrieve your key's plaintext, use the `Decrypt` method with your key's ID and ciphertext.
        :param key_id: ID of the key.
        :param without_plaintext: Default value is `false`, meaning that the plaintext is returned.
        Set it to `true` if you do not wish the plaintext to be returned in the response object.
        :param region: Region to target. If none is passed will use default region from the config.
        :param algorithm: See the `DataKey.Algorithm.SymmetricEncryption` enum for a description of values.
        :return: :class:`DataKey <DataKey>`

        Usage:
        ::

            result = await api.generate_data_key(
                key_id="example",
                without_plaintext=False,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "POST",
            f"/key-manager/v1alpha1/regions/{param_region}/keys/{param_key_id}/generate-data-key",
            body=marshal_GenerateDataKeyRequest(
                GenerateDataKeyRequest(
                    key_id=key_id,
                    without_plaintext=without_plaintext,
                    region=region,
                    algorithm=algorithm,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DataKey(res.json())

    async def encrypt(
        self,
        *,
        key_id: str,
        plaintext: str,
        region: Optional[ScwRegion] = None,
        associated_data: Optional[str] = None,
    ) -> EncryptResponse:
        """
        Encrypt a payload.
        Encrypt a payload using an existing key, specified by the `key_id` parameter. The maximum payload size that can be encrypted is 64 KB of plaintext.
        :param key_id: The key must have an usage set to `symmetric_encryption` or `asymmetric_encryption`.
        :param plaintext: Data size must be between 1 and 65535 bytes.
        :param region: Region to target. If none is passed will use default region from the config.
        :param associated_data: Additional data which will not be encrypted, but authenticated and appended to the encrypted payload. Only supported by keys with a usage set to `symmetric_encryption`.
        :return: :class:`EncryptResponse <EncryptResponse>`

        Usage:
        ::

            result = await api.encrypt(
                key_id="example",
                plaintext="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "POST",
            f"/key-manager/v1alpha1/regions/{param_region}/keys/{param_key_id}/encrypt",
            body=marshal_EncryptRequest(
                EncryptRequest(
                    key_id=key_id,
                    plaintext=plaintext,
                    region=region,
                    associated_data=associated_data,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_EncryptResponse(res.json())

    async def decrypt(
        self,
        *,
        key_id: str,
        ciphertext: str,
        region: Optional[ScwRegion] = None,
        associated_data: Optional[str] = None,
    ) -> DecryptResponse:
        """
        Decrypt an encrypted payload.
        Decrypt an encrypted payload using an existing key, specified by the `key_id` parameter. The maximum payload size that can be decrypted is equivalent to the encrypted output of 64 KB of data (around 131 KB).
        :param key_id: The key must have an usage set to `symmetric_encryption` or `asymmetric_encryption`.
        :param ciphertext: Data size must be between 1 and 131071 bytes.
        :param region: Region to target. If none is passed will use default region from the config.
        :param associated_data: The additional data must match the value passed in the encryption request. Only supported by keys with a usage set to `symmetric_encryption`.
        :return: :class:`DecryptResponse <DecryptResponse>`

        Usage:
        ::

            result = await api.decrypt(
                key_id="example",
                ciphertext="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "POST",
            f"/key-manager/v1alpha1/regions/{param_region}/keys/{param_key_id}/decrypt",
            body=marshal_DecryptRequest(
                DecryptRequest(
                    key_id=key_id,
                    ciphertext=ciphertext,
                    region=region,
                    associated_data=associated_data,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DecryptResponse(res.json())

    async def sign(
        self,
        *,
        key_id: str,
        digest: str,
        region: Optional[ScwRegion] = None,
    ) -> SignResponse:
        """
        Sign a message digest.
        Use a given key to sign a message digest. The key must have its usage set to `asymmetric_signing`. The digest must be created using the same digest algorithm that is defined in the key's algorithm configuration.
        :param key_id: ID of the key to use for signing.
        :param digest: The digest must be generated using the same algorithm defined in the key’s algorithm settings.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`SignResponse <SignResponse>`

        Usage:
        ::

            result = await api.sign(
                key_id="example",
                digest="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "POST",
            f"/key-manager/v1alpha1/regions/{param_region}/keys/{param_key_id}/sign",
            body=marshal_SignRequest(
                SignRequest(
                    key_id=key_id,
                    digest=digest,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SignResponse(res.json())

    async def verify(
        self,
        *,
        key_id: str,
        digest: str,
        signature: str,
        region: Optional[ScwRegion] = None,
    ) -> VerifyResponse:
        """
        Verify a message signature.
        Use a given key to verify a message signature against a message digest. The key must have its usage set to `asymmetric_signing`. The message digest must be generated using the same digest algorithm that is defined in the key's algorithm configuration.
        :param key_id: ID of the key to use for signature verification.
        :param digest: Must be generated using the same algorithm specified in the key’s configuration.
        :param signature: The message signature to verify.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`VerifyResponse <VerifyResponse>`

        Usage:
        ::

            result = await api.verify(
                key_id="example",
                digest="example",
                signature="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "POST",
            f"/key-manager/v1alpha1/regions/{param_region}/keys/{param_key_id}/verify",
            body=marshal_VerifyRequest(
                VerifyRequest(
                    key_id=key_id,
                    digest=digest,
                    signature=signature,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_VerifyResponse(res.json())

    async def import_key_material(
        self,
        *,
        key_id: str,
        key_material: str,
        region: Optional[ScwRegion] = None,
        salt: Optional[str] = None,
    ) -> Key:
        """
        Import key material.
        Import externally generated key material into Key Manager to derive a new cryptographic key. The key's origin must be `external`.
        :param key_id: The key's origin must be `external`.
        :param key_material: The key material The key material is a random sequence of bytes used to derive a cryptographic key.
        :param region: Region to target. If none is passed will use default region from the config.
        :param salt: A salt is random data added to key material to ensure unique derived keys, even if the input is similar. It helps strengthen security when the key material has low randomness (low entropy).
        :return: :class:`Key <Key>`

        Usage:
        ::

            result = await api.import_key_material(
                key_id="example",
                key_material="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "POST",
            f"/key-manager/v1alpha1/regions/{param_region}/keys/{param_key_id}/import-key-material",
            body=marshal_ImportKeyMaterialRequest(
                ImportKeyMaterialRequest(
                    key_id=key_id,
                    key_material=key_material,
                    region=region,
                    salt=salt,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Key(res.json())

    async def delete_key_material(
        self,
        *,
        key_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete key material.
        Delete previously imported key material. This renders the associated cryptographic key unusable for any operation. The key's origin must be `external`.
        :param key_id: ID of the key of which to delete the key material.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_key_material(
                key_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "POST",
            f"/key-manager/v1alpha1/regions/{param_region}/keys/{param_key_id}/delete-key-material",
            body={},
        )

        self._throw_on_error(res)

    async def restore_key(
        self,
        *,
        key_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Key:
        """
        Restore a key.
        Restore a key and all its rotations scheduled for deletion specified by the `region` and `key_id` parameters.
        :param key_id:
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Key <Key>`

        Usage:
        ::

            result = await api.restore_key(
                key_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "POST",
            f"/key-manager/v1alpha1/regions/{param_region}/keys/{param_key_id}/restore",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Key(res.json())

    async def list_algorithms(
        self,
        *,
        region: Optional[ScwRegion] = None,
        usages: Optional[list[ListAlgorithmsRequestUsage]] = None,
    ) -> ListAlgorithmsResponse:
        """
        List all available algorithms.
        Lists all cryptographic algorithms supported by the Key Manager service.
        :param region: Region to target. If none is passed will use default region from the config.
        :param usages: Filter by key usage.
        :return: :class:`ListAlgorithmsResponse <ListAlgorithmsResponse>`

        Usage:
        ::

            result = await api.list_algorithms()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/key-manager/v1alpha1/regions/{param_region}/algorithms",
            params={
                "usages": usages,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListAlgorithmsResponse(res.json())
