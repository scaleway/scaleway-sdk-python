# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListAllKeysAndValuesResponseValue:
    id: str
    """
    ID of the value.
    """

    name: str
    """
    Name of the value.
    """

    description: str
    """
    Description of the value.
    """


@dataclass
class BindingKey:
    id: str
    """
    ID of the key.
    """

    name: str
    """
    Name of the key.
    """


@dataclass
class BindingValue:
    id: str
    """
    ID of the value.
    """

    name: str
    """
    Name of the value.
    """


@dataclass
class ListAllKeysAndValuesResponseKey:
    id: str
    """
    ID of the key.
    """

    name: str
    """
    Name of the key.
    """

    description: str
    """
    Description of the key.
    """

    values: list[ListAllKeysAndValuesResponseValue]
    """
    List of values associated with the key, sorted alphabetically by name.
    """


@dataclass
class Binding:
    id: str
    """
    ID of the binding.
    """

    srn: str
    """
    Scaleway Resource Number associated to the binding.
    """

    key: Optional[BindingKey] = None
    """
    Key associated to the binding.
    """

    value: Optional[BindingValue] = None
    """
    Value associated to the binding.
    """


@dataclass
class Key:
    id: str
    """
    ID of the annotation key.
    """

    name: str
    """
    Name of the annotation key.
    """

    description: str
    """
    Description of the annotation key.
    """


@dataclass
class Value:
    id: str
    """
    ID of the value.
    """

    key_id: str
    """
    ID of the key the value is associated to.
    """

    name: str
    """
    Name of the value (e.g. "production" for a key "environment").
    """

    description: str
    """
    Description of the value.
    """


@dataclass
class CreateBindingRequest:
    srn: str
    """
    Scaleway Resource Number to associate.
    """

    value_id: str
    """
    ID of the value to associate.
    """


@dataclass
class CreateKeyRequest:
    name: str
    """
    Name of the annotation key.
    """

    description: str
    """
    Description of the annotation key.
    """

    organization_id: Optional[str] = None
    """
    ID of the organization.
    """


@dataclass
class CreateValueRequest:
    key_id: str
    """
    ID of the key the value will be bound to.
    """

    name: str
    """
    Name of the value.
    """

    description: str
    """
    Description of the value.
    """


@dataclass
class DeleteAllBindingsMatchingSRNRequest:
    srn: str
    """
    Scaleway Resource Number for which all bindings should be deleted.
    """

    organization_id: Optional[str] = None
    """
    ID of the organization.
    """


@dataclass
class DeleteAllBindingsMatchingSRNResponse:
    total_deleted: int
    """
    Total number of bindings deleted.
    """


@dataclass
class DeleteAllBindingsMatchingValueRequest:
    value_id: str
    """
    ID of the value for which all bindings should be deleted.
    """


@dataclass
class DeleteAllBindingsMatchingValueResponse:
    total_deleted: int
    """
    Total number of bindings deleted.
    """


@dataclass
class DeleteAllValuesMatchingKeyRequest:
    key_id: str
    """
    ID of the key for which to delete all values.
    """


@dataclass
class DeleteAllValuesMatchingKeyResponse:
    total_deleted: int
    """
    Total number of bindings deleted.
    """


@dataclass
class DeleteBindingRequest:
    binding_id: str
    """
    ID of the binding to delete.
    """


@dataclass
class DeleteKeyRequest:
    key_id: str
    """
    ID of the key to delete.
    """


@dataclass
class DeleteValueRequest:
    value_id: str
    """
    ID of the value to delete.
    """


@dataclass
class GetKeyRequest:
    key_id: str
    """
    ID of the key to retrieve.
    """


@dataclass
class GetValueRequest:
    value_id: str
    """
    ID of the value to retrieve.
    """


@dataclass
class ListAllKeysAndValuesRequest:
    organization_id: Optional[str] = None
    """
    ID of the organization.
    """


@dataclass
class ListAllKeysAndValuesResponse:
    keys: list[ListAllKeysAndValuesResponseKey]
    """
    List of keys with values for an organization, sorted alphabetically by name.
    """


@dataclass
class ListBindingsRequest:
    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of bindings on the page.
    """

    organization_id: Optional[str] = None
    """
    ID of the organization.
    """

    srn: Optional[str] = None
    """
    Scaleway Resource Number for which to list all bindings.
    """

    value_id: Optional[str] = None
    """
    Value ID for which to list all bindings.
    """


@dataclass
class ListBindingsResponse:
    bindings: list[Binding]
    """
    List of bindings for the organization. Response order by ID.
    """

    total_count: int
    """
    Total number of bindings returned.
    """


@dataclass
class ListKeysRequest:
    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of keys on the page.
    """

    organization_id: Optional[str] = None
    """
    ID of the organization.
    """


@dataclass
class ListKeysResponse:
    keys: list[Key]
    """
    List of keys for an organization, sorted alphabetically by name.
    """

    total_count: int
    """
    Total number of keys returned.
    """


@dataclass
class ListValuesRequest:
    page: Optional[int] = 0
    """
    Page number.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of values on the page.
    """

    organization_id: Optional[str] = None
    """
    ID of the organization.
    """

    key_id: Optional[str] = None
    """
    ID of the key to list the values for.
    """


@dataclass
class ListValuesResponse:
    values: list[Value]
    """
    List of values for a key, sorted alphabetically by name.
    """

    total_count: int
    """
    Total number of values returned.
    """


@dataclass
class UpdateKeyRequest:
    key_id: str
    """
    ID of the key to update.
    """

    name: Optional[str] = None
    """
    New name of the key.
    """

    description: Optional[str] = None
    """
    New description of the key.
    """


@dataclass
class UpdateValueRequest:
    value_id: str
    """
    ID of the value to update.
    """

    name: Optional[str] = None
    """
    New name of the value.
    """

    description: Optional[str] = None
    """
    New description of the value.
    """
