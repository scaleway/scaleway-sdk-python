# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    Namespace,
    Permissions,
    CredentialNATSCredsFile,
    CredentialSQSSNSCreds,
    Credential,
    CredentialSummarySQSSNSCreds,
    CredentialSummary,
    ListCredentialsResponse,
    ListNamespacesResponse,
    CreateCredentialRequest,
    CreateNamespaceRequest,
    UpdateCredentialRequest,
    UpdateNamespaceRequest,
)


def unmarshal_Namespace(data: Any) -> Namespace:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Namespace' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("endpoint", None)
    if field is not None:
        args["endpoint"] = field

    field = data.get("protocol", None)
    if field is not None:
        args["protocol"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Namespace(**args)


def unmarshal_Permissions(data: Any) -> Permissions:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Permissions' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("can_publish", None)
    if field is not None:
        args["can_publish"] = field

    field = data.get("can_receive", None)
    if field is not None:
        args["can_receive"] = field

    field = data.get("can_manage", None)
    if field is not None:
        args["can_manage"] = field

    return Permissions(**args)


def unmarshal_CredentialNATSCredsFile(data: Any) -> CredentialNATSCredsFile:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CredentialNATSCredsFile' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("content", None)
    if field is not None:
        args["content"] = field

    return CredentialNATSCredsFile(**args)


def unmarshal_CredentialSQSSNSCreds(data: Any) -> CredentialSQSSNSCreds:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CredentialSQSSNSCreds' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("access_key", None)
    if field is not None:
        args["access_key"] = field

    field = data.get("secret_key", None)
    if field is not None:
        args["secret_key"] = field

    field = data.get("permissions", None)
    if field is not None:
        args["permissions"] = unmarshal_Permissions(field)

    return CredentialSQSSNSCreds(**args)


def unmarshal_Credential(data: Any) -> Credential:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Credential' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("namespace_id", None)
    if field is not None:
        args["namespace_id"] = field

    field = data.get("protocol", None)
    if field is not None:
        args["protocol"] = field

    field = data.get("nats_credentials", None)
    if field is not None:
        args["nats_credentials"] = unmarshal_CredentialNATSCredsFile(field)

    field = data.get("sqs_sns_credentials", None)
    if field is not None:
        args["sqs_sns_credentials"] = unmarshal_CredentialSQSSNSCreds(field)

    return Credential(**args)


def unmarshal_CredentialSummarySQSSNSCreds(data: Any) -> CredentialSummarySQSSNSCreds:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CredentialSummarySQSSNSCreds' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("access_key", None)
    if field is not None:
        args["access_key"] = field

    field = data.get("permissions", None)
    if field is not None:
        args["permissions"] = unmarshal_Permissions(field)

    return CredentialSummarySQSSNSCreds(**args)


def unmarshal_CredentialSummary(data: Any) -> CredentialSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CredentialSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("namespace_id", None)
    if field is not None:
        args["namespace_id"] = field

    field = data.get("protocol", None)
    if field is not None:
        args["protocol"] = field

    field = data.get("sqs_sns_credentials", None)
    if field is not None:
        args["sqs_sns_credentials"] = unmarshal_CredentialSummarySQSSNSCreds(field)

    return CredentialSummary(**args)


def unmarshal_ListCredentialsResponse(data: Any) -> ListCredentialsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListCredentialsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("credentials", None)
    if field is not None:
        args["credentials"] = (
            [unmarshal_CredentialSummary(v) for v in field]
            if field is not None
            else None
        )

    return ListCredentialsResponse(**args)


def unmarshal_ListNamespacesResponse(data: Any) -> ListNamespacesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNamespacesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("namespaces", None)
    if field is not None:
        args["namespaces"] = (
            [unmarshal_Namespace(v) for v in field] if field is not None else None
        )

    return ListNamespacesResponse(**args)


def marshal_Permissions(
    request: Permissions,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.can_publish is not None:
        output["can_publish"] = request.can_publish

    if request.can_receive is not None:
        output["can_receive"] = request.can_receive

    if request.can_manage is not None:
        output["can_manage"] = request.can_manage

    return output


def marshal_CreateCredentialRequest(
    request: CreateCredentialRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.namespace_id is not None:
        output["namespace_id"] = request.namespace_id

    if request.name is not None:
        output["name"] = request.name

    if request.permissions is not None:
        output["permissions"] = (marshal_Permissions(request.permissions, defaults),)

    return output


def marshal_CreateNamespaceRequest(
    request: CreateNamespaceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.protocol is not None:
        output["protocol"] = str(request.protocol)

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_UpdateCredentialRequest(
    request: UpdateCredentialRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.permissions is not None:
        output["permissions"] = (marshal_Permissions(request.permissions, defaults),)

    return output


def marshal_UpdateNamespaceRequest(
    request: UpdateNamespaceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.namespace_id is not None:
        output["namespace_id"] = request.namespace_id

    if request.name is not None:
        output["name"] = request.name

    return output
