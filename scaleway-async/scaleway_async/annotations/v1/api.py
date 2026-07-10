# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

from scaleway_core.api import API
from scaleway_core.utils import (
    validate_path_param,
    fetch_all_pages_async,
)
from .types import (
    Binding,
    CreateBindingRequest,
    CreateKeyRequest,
    CreateValueRequest,
    DeleteAllBindingsMatchingSRNResponse,
    DeleteAllBindingsMatchingValueResponse,
    DeleteAllValuesMatchingKeyResponse,
    Key,
    ListAllKeysAndValuesResponse,
    ListBindingsResponse,
    ListKeysResponse,
    ListValuesResponse,
    UpdateKeyRequest,
    UpdateValueRequest,
    Value,
)
from .marshalling import (
    unmarshal_Binding,
    unmarshal_Key,
    unmarshal_Value,
    unmarshal_DeleteAllBindingsMatchingSRNResponse,
    unmarshal_DeleteAllBindingsMatchingValueResponse,
    unmarshal_DeleteAllValuesMatchingKeyResponse,
    unmarshal_ListAllKeysAndValuesResponse,
    unmarshal_ListBindingsResponse,
    unmarshal_ListKeysResponse,
    unmarshal_ListValuesResponse,
    marshal_CreateBindingRequest,
    marshal_CreateKeyRequest,
    marshal_CreateValueRequest,
    marshal_UpdateKeyRequest,
    marshal_UpdateValueRequest,
)


class AnnotationsV1API(API):
    """ """

    async def create_key(
        self,
        *,
        name: str,
        description: str,
        organization_id: Optional[str] = None,
    ) -> Key:
        """
        Create an annotation key.
        :param name: Name of the annotation key.
        :param description: Description of the annotation key.
        :param organization_id: ID of the organization.
        :return: :class:`Key <Key>`

        Usage:
        ::

            result = await api.create_key(
                name="example",
                description="example",
            )
        """

        res = self._request(
            "POST",
            "/annotations/v1/keys",
            body=marshal_CreateKeyRequest(
                CreateKeyRequest(
                    name=name,
                    description=description,
                    organization_id=organization_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Key(res.json())

    async def list_keys(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
    ) -> ListKeysResponse:
        """
        List of keys.
        :param page: Page number.
        :param page_size: Maximum number of keys on the page.
        :param organization_id: ID of the organization.
        :return: :class:`ListKeysResponse <ListKeysResponse>`

        Usage:
        ::

            result = await api.list_keys()
        """

        res = self._request(
            "GET",
            "/annotations/v1/keys",
            params={
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListKeysResponse(res.json())

    async def list_keys_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
    ) -> list[Key]:
        """
        List of keys.
        :param page: Page number.
        :param page_size: Maximum number of keys on the page.
        :param organization_id: ID of the organization.
        :return: :class:`list[Key] <list[Key]>`

        Usage:
        ::

            result = await api.list_keys_all()
        """

        return await fetch_all_pages_async(
            type=ListKeysResponse,
            key="keys",
            fetcher=self.list_keys,
            args={
                "page": page,
                "page_size": page_size,
                "organization_id": organization_id,
            },
        )

    async def get_key(
        self,
        *,
        key_id: str,
    ) -> Key:
        """
        Retrieve a specific key.
        :param key_id: ID of the key to retrieve.
        :return: :class:`Key <Key>`

        Usage:
        ::

            result = await api.get_key(
                key_id="example",
            )
        """

        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "GET",
            f"/annotations/v1/keys/{param_key_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Key(res.json())

    async def update_key(
        self,
        *,
        key_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Key:
        """
        Update name or description. All associated resources will immediately display the new name.
        :param key_id: ID of the key to update.
        :param name: New name of the key.
        :param description: New description of the key.
        :return: :class:`Key <Key>`

        Usage:
        ::

            result = await api.update_key(
                key_id="example",
            )
        """

        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "PATCH",
            f"/annotations/v1/keys/{param_key_id}",
            body=marshal_UpdateKeyRequest(
                UpdateKeyRequest(
                    key_id=key_id,
                    name=name,
                    description=description,
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
    ) -> None:
        """
        Delete a key definition. Fails if the key has any associated values.
        :param key_id: ID of the key to delete.

        Usage:
        ::

            result = await api.delete_key(
                key_id="example",
            )
        """

        param_key_id = validate_path_param("key_id", key_id)

        res = self._request(
            "DELETE",
            f"/annotations/v1/keys/{param_key_id}",
        )

        self._throw_on_error(res)

    async def create_value(
        self,
        *,
        key_id: str,
        name: str,
        description: str,
    ) -> Value:
        """
        Add a value definition to a key.
        :param key_id: ID of the key the value will be bound to.
        :param name: Name of the value.
        :param description: Description of the value.
        :return: :class:`Value <Value>`

        Usage:
        ::

            result = await api.create_value(
                key_id="example",
                name="example",
                description="example",
            )
        """

        res = self._request(
            "POST",
            "/annotations/v1/values",
            body=marshal_CreateValueRequest(
                CreateValueRequest(
                    key_id=key_id,
                    name=name,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Value(res.json())

    async def list_values(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        key_id: Optional[str] = None,
    ) -> ListValuesResponse:
        """
        List all values for a key, sorted alphabetically by name.
        :param page: Page number.
        :param page_size: Maximum number of values on the page.
        :param organization_id: ID of the organization.
        :param key_id: ID of the key to list the values for.
        :return: :class:`ListValuesResponse <ListValuesResponse>`

        Usage:
        ::

            result = await api.list_values()
        """

        res = self._request(
            "GET",
            "/annotations/v1/values",
            params={
                "key_id": key_id,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListValuesResponse(res.json())

    async def list_values_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        key_id: Optional[str] = None,
    ) -> list[Value]:
        """
        List all values for a key, sorted alphabetically by name.
        :param page: Page number.
        :param page_size: Maximum number of values on the page.
        :param organization_id: ID of the organization.
        :param key_id: ID of the key to list the values for.
        :return: :class:`list[Value] <list[Value]>`

        Usage:
        ::

            result = await api.list_values_all()
        """

        return await fetch_all_pages_async(
            type=ListValuesResponse,
            key="values",
            fetcher=self.list_values,
            args={
                "page": page,
                "page_size": page_size,
                "organization_id": organization_id,
                "key_id": key_id,
            },
        )

    async def get_value(
        self,
        *,
        value_id: str,
    ) -> Value:
        """
        Retrieve a specific value.
        :param value_id: ID of the value to retrieve.
        :return: :class:`Value <Value>`

        Usage:
        ::

            result = await api.get_value(
                value_id="example",
            )
        """

        param_value_id = validate_path_param("value_id", value_id)

        res = self._request(
            "GET",
            f"/annotations/v1/values/{param_value_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Value(res.json())

    async def update_value(
        self,
        *,
        value_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Value:
        """
        Update name or description. Global update.
        :param value_id: ID of the value to update.
        :param name: New name of the value.
        :param description: New description of the value.
        :return: :class:`Value <Value>`

        Usage:
        ::

            result = await api.update_value(
                value_id="example",
            )
        """

        param_value_id = validate_path_param("value_id", value_id)

        res = self._request(
            "PATCH",
            f"/annotations/v1/values/{param_value_id}",
            body=marshal_UpdateValueRequest(
                UpdateValueRequest(
                    value_id=value_id,
                    name=name,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Value(res.json())

    async def delete_value(
        self,
        *,
        value_id: str,
    ) -> None:
        """
        Delete a value definition. Fails if the value is currently bound to any resource.
        :param value_id: ID of the value to delete.

        Usage:
        ::

            result = await api.delete_value(
                value_id="example",
            )
        """

        param_value_id = validate_path_param("value_id", value_id)

        res = self._request(
            "DELETE",
            f"/annotations/v1/values/{param_value_id}",
        )

        self._throw_on_error(res)

    async def delete_all_values_matching_key(
        self,
        *,
        key_id: str,
    ) -> DeleteAllValuesMatchingKeyResponse:
        """
        Delete ALL values associated with a key. Fails if any of these values are currently bound to any resource.
        :param key_id: ID of the key for which to delete all values.
        :return: :class:`DeleteAllValuesMatchingKeyResponse <DeleteAllValuesMatchingKeyResponse>`

        Usage:
        ::

            result = await api.delete_all_values_matching_key(
                key_id="example",
            )
        """

        res = self._request(
            "DELETE",
            "/annotations/v1/values/delete-all-matching-key",
            params={
                "key_id": key_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_DeleteAllValuesMatchingKeyResponse(res.json())

    async def list_all_keys_and_values(
        self,
        *,
        organization_id: Optional[str] = None,
    ) -> ListAllKeysAndValuesResponse:
        """
        List all keys and values for an organization, sorted alphabetically by key name and value name.
        :param organization_id: ID of the organization.
        :return: :class:`ListAllKeysAndValuesResponse <ListAllKeysAndValuesResponse>`

        Usage:
        ::

            result = await api.list_all_keys_and_values()
        """

        res = self._request(
            "GET",
            "/annotations/v1/all-keys-and-values",
            params={
                "organization_id": organization_id
                or self.client.default_organization_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListAllKeysAndValuesResponse(res.json())

    async def create_binding(
        self,
        *,
        srn: str,
        value_id: str,
    ) -> Binding:
        """
        Attach a value to a resource. Fails if the resource already has a value for this key.
        :param srn: Scaleway Resource Number to associate.
        :param value_id: ID of the value to associate.
        :return: :class:`Binding <Binding>`

        Usage:
        ::

            result = await api.create_binding(
                srn="example",
                value_id="example",
            )
        """

        res = self._request(
            "POST",
            "/annotations/v1/bindings",
            body=marshal_CreateBindingRequest(
                CreateBindingRequest(
                    srn=srn,
                    value_id=value_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Binding(res.json())

    async def list_bindings(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        srn: Optional[str] = None,
        value_id: Optional[str] = None,
    ) -> ListBindingsResponse:
        """
        List all bindings, or filter by Scaleway Resource Number or value ID. Response order by ID.
        :param page: Page number.
        :param page_size: Maximum number of bindings on the page.
        :param organization_id: ID of the organization.
        :param srn: Scaleway Resource Number for which to list all bindings.
        :param value_id: Value ID for which to list all bindings.
        :return: :class:`ListBindingsResponse <ListBindingsResponse>`

        Usage:
        ::

            result = await api.list_bindings()
        """

        res = self._request(
            "GET",
            "/annotations/v1/bindings",
            params={
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "srn": srn,
                "value_id": value_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListBindingsResponse(res.json())

    async def list_bindings_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        srn: Optional[str] = None,
        value_id: Optional[str] = None,
    ) -> list[Binding]:
        """
        List all bindings, or filter by Scaleway Resource Number or value ID. Response order by ID.
        :param page: Page number.
        :param page_size: Maximum number of bindings on the page.
        :param organization_id: ID of the organization.
        :param srn: Scaleway Resource Number for which to list all bindings.
        :param value_id: Value ID for which to list all bindings.
        :return: :class:`list[Binding] <list[Binding]>`

        Usage:
        ::

            result = await api.list_bindings_all()
        """

        return await fetch_all_pages_async(
            type=ListBindingsResponse,
            key="bindings",
            fetcher=self.list_bindings,
            args={
                "page": page,
                "page_size": page_size,
                "organization_id": organization_id,
                "srn": srn,
                "value_id": value_id,
            },
        )

    async def delete_binding(
        self,
        *,
        binding_id: str,
    ) -> None:
        """
        Detach an annotation from a resource.
        :param binding_id: ID of the binding to delete.

        Usage:
        ::

            result = await api.delete_binding(
                binding_id="example",
            )
        """

        param_binding_id = validate_path_param("binding_id", binding_id)

        res = self._request(
            "DELETE",
            f"/annotations/v1/bindings/{param_binding_id}",
        )

        self._throw_on_error(res)

    async def delete_all_bindings_matching_value(
        self,
        *,
        value_id: str,
    ) -> DeleteAllBindingsMatchingValueResponse:
        """
        Delete ALL bindings associated with a value.
        :param value_id: ID of the value for which all bindings should be deleted.
        :return: :class:`DeleteAllBindingsMatchingValueResponse <DeleteAllBindingsMatchingValueResponse>`

        Usage:
        ::

            result = await api.delete_all_bindings_matching_value(
                value_id="example",
            )
        """

        res = self._request(
            "DELETE",
            "/annotations/v1/bindings/delete-all-matching-value",
            params={
                "value_id": value_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_DeleteAllBindingsMatchingValueResponse(res.json())

    async def delete_all_bindings_matching_srn(
        self,
        *,
        srn: str,
        organization_id: Optional[str] = None,
    ) -> DeleteAllBindingsMatchingSRNResponse:
        """
        Delete ALL bindings associated with a Scaleway Resource Number.
        :param srn: Scaleway Resource Number for which all bindings should be deleted.
        :param organization_id: ID of the organization.
        :return: :class:`DeleteAllBindingsMatchingSRNResponse <DeleteAllBindingsMatchingSRNResponse>`

        Usage:
        ::

            result = await api.delete_all_bindings_matching_srn(
                srn="example",
            )
        """

        res = self._request(
            "DELETE",
            "/annotations/v1/bindings/delete-all-matching-srn",
            params={
                "organization_id": organization_id
                or self.client.default_organization_id,
                "srn": srn,
            },
        )

        self._throw_on_error(res)
        return unmarshal_DeleteAllBindingsMatchingSRNResponse(res.json())
