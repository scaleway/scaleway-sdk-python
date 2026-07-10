# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any

from scaleway_core.profile import ProfileDefaults
from .types import (
    BindingKey,
    BindingValue,
    Binding,
    Key,
    Value,
    DeleteAllBindingsMatchingSRNResponse,
    DeleteAllBindingsMatchingValueResponse,
    DeleteAllValuesMatchingKeyResponse,
    ListAllKeysAndValuesResponseValue,
    ListAllKeysAndValuesResponseKey,
    ListAllKeysAndValuesResponse,
    ListBindingsResponse,
    ListKeysResponse,
    ListValuesResponse,
    CreateBindingRequest,
    CreateKeyRequest,
    CreateValueRequest,
    UpdateKeyRequest,
    UpdateValueRequest,
)


def unmarshal_BindingKey(data: Any) -> BindingKey:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BindingKey' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return BindingKey(**args)


def unmarshal_BindingValue(data: Any) -> BindingValue:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BindingValue' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return BindingValue(**args)


def unmarshal_Binding(data: Any) -> Binding:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Binding' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("srn", None)
    if field is not None:
        args["srn"] = field
    else:
        args["srn"] = None

    field = data.get("key", None)
    if field is not None:
        args["key"] = unmarshal_BindingKey(field)
    else:
        args["key"] = None

    field = data.get("value", None)
    if field is not None:
        args["value"] = unmarshal_BindingValue(field)
    else:
        args["value"] = None

    return Binding(**args)


def unmarshal_Key(data: Any) -> Key:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Key' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    return Key(**args)


def unmarshal_Value(data: Any) -> Value:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Value' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("key_id", None)
    if field is not None:
        args["key_id"] = field
    else:
        args["key_id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    return Value(**args)


def unmarshal_DeleteAllBindingsMatchingSRNResponse(
    data: Any,
) -> DeleteAllBindingsMatchingSRNResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeleteAllBindingsMatchingSRNResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_deleted", None)
    if field is not None:
        args["total_deleted"] = field
    else:
        args["total_deleted"] = 0

    return DeleteAllBindingsMatchingSRNResponse(**args)


def unmarshal_DeleteAllBindingsMatchingValueResponse(
    data: Any,
) -> DeleteAllBindingsMatchingValueResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeleteAllBindingsMatchingValueResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_deleted", None)
    if field is not None:
        args["total_deleted"] = field
    else:
        args["total_deleted"] = 0

    return DeleteAllBindingsMatchingValueResponse(**args)


def unmarshal_DeleteAllValuesMatchingKeyResponse(
    data: Any,
) -> DeleteAllValuesMatchingKeyResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DeleteAllValuesMatchingKeyResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_deleted", None)
    if field is not None:
        args["total_deleted"] = field
    else:
        args["total_deleted"] = 0

    return DeleteAllValuesMatchingKeyResponse(**args)


def unmarshal_ListAllKeysAndValuesResponseValue(
    data: Any,
) -> ListAllKeysAndValuesResponseValue:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListAllKeysAndValuesResponseValue' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    return ListAllKeysAndValuesResponseValue(**args)


def unmarshal_ListAllKeysAndValuesResponseKey(
    data: Any,
) -> ListAllKeysAndValuesResponseKey:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListAllKeysAndValuesResponseKey' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("values", None)
    if field is not None:
        args["values"] = (
            [unmarshal_ListAllKeysAndValuesResponseValue(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["values"] = []

    return ListAllKeysAndValuesResponseKey(**args)


def unmarshal_ListAllKeysAndValuesResponse(data: Any) -> ListAllKeysAndValuesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListAllKeysAndValuesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("keys", None)
    if field is not None:
        args["keys"] = (
            [unmarshal_ListAllKeysAndValuesResponseKey(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["keys"] = []

    return ListAllKeysAndValuesResponse(**args)


def unmarshal_ListBindingsResponse(data: Any) -> ListBindingsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListBindingsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("bindings", None)
    if field is not None:
        args["bindings"] = (
            [unmarshal_Binding(v) for v in field] if field is not None else None
        )
    else:
        args["bindings"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListBindingsResponse(**args)


def unmarshal_ListKeysResponse(data: Any) -> ListKeysResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListKeysResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("keys", None)
    if field is not None:
        args["keys"] = [unmarshal_Key(v) for v in field] if field is not None else None
    else:
        args["keys"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListKeysResponse(**args)


def unmarshal_ListValuesResponse(data: Any) -> ListValuesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListValuesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("values", None)
    if field is not None:
        args["values"] = (
            [unmarshal_Value(v) for v in field] if field is not None else None
        )
    else:
        args["values"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListValuesResponse(**args)


def marshal_CreateBindingRequest(
    request: CreateBindingRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.srn is not None:
        output["srn"] = request.srn

    if request.value_id is not None:
        output["value_id"] = request.value_id

    return output


def marshal_CreateKeyRequest(
    request: CreateKeyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id
    else:
        output["organization_id"] = defaults.default_organization_id

    return output


def marshal_CreateValueRequest(
    request: CreateValueRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.key_id is not None:
        output["key_id"] = request.key_id

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    return output


def marshal_UpdateKeyRequest(
    request: UpdateKeyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    return output


def marshal_UpdateValueRequest(
    request: UpdateValueRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    return output
