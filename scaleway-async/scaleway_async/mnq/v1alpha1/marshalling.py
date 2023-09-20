# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from dateutil import parser
from .types import (
    NamespaceProtocol,
    Credential,
    CredentialNATSCredsFile,
    CredentialSQSSNSCreds,
    CredentialSummary,
    CredentialSummarySQSSNSCreds,
    ListCredentialsResponse,
    ListNamespacesResponse,
    Namespace,
    Permissions,
    CreateNamespaceRequest,
    UpdateNamespaceRequest,
    CreateCredentialRequest,
    UpdateCredentialRequest,
)


def unmarshal_Permissions(data: Any) -> Permissions:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Permissions' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("can_manage", None)
    args["can_manage"] = field

    field = data.get("can_publish", None)
    args["can_publish"] = field

    field = data.get("can_receive", None)
    args["can_receive"] = field

    return Permissions(**args)


def unmarshal_CredentialSummarySQSSNSCreds(data: Any) -> CredentialSummarySQSSNSCreds:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CredentialSummarySQSSNSCreds' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("access_key", None)
    args["access_key"] = field

    field = data.get("permissions", None)
    args["permissions"] = unmarshal_Permissions(field) if field is not None else None

    return CredentialSummarySQSSNSCreds(**args)


def unmarshal_CredentialNATSCredsFile(data: Any) -> CredentialNATSCredsFile:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CredentialNATSCredsFile' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("content", None)
    args["content"] = field

    return CredentialNATSCredsFile(**args)


def unmarshal_CredentialSQSSNSCreds(data: Any) -> CredentialSQSSNSCreds:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CredentialSQSSNSCreds' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("access_key", None)
    args["access_key"] = field

    field = data.get("permissions", None)
    args["permissions"] = unmarshal_Permissions(field) if field is not None else None

    field = data.get("secret_key", None)
    args["secret_key"] = field

    return CredentialSQSSNSCreds(**args)


def unmarshal_CredentialSummary(data: Any) -> CredentialSummary:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CredentialSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("namespace_id", None)
    args["namespace_id"] = field

    field = data.get("protocol", None)
    args["protocol"] = field

    field = data.get("sqs_sns_credentials", None)
    args["sqs_sns_credentials"] = (
        unmarshal_CredentialSummarySQSSNSCreds(field) if field is not None else None
    )

    return CredentialSummary(**args)


def unmarshal_Namespace(data: Any) -> Namespace:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Namespace' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("endpoint", None)
    args["endpoint"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("protocol", None)
    args["protocol"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return Namespace(**args)


def unmarshal_Credential(data: Any) -> Credential:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Credential' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("namespace_id", None)
    args["namespace_id"] = field

    field = data.get("nats_credentials", None)
    args["nats_credentials"] = (
        unmarshal_CredentialNATSCredsFile(field) if field is not None else None
    )

    field = data.get("protocol", None)
    args["protocol"] = field

    field = data.get("sqs_sns_credentials", None)
    args["sqs_sns_credentials"] = (
        unmarshal_CredentialSQSSNSCreds(field) if field is not None else None
    )

    return Credential(**args)


def unmarshal_ListCredentialsResponse(data: Any) -> ListCredentialsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListCredentialsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("credentials", None)
    args["credentials"] = (
        [unmarshal_CredentialSummary(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListCredentialsResponse(**args)


def unmarshal_ListNamespacesResponse(data: Any) -> ListNamespacesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListNamespacesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("namespaces", None)
    args["namespaces"] = (
        [unmarshal_Namespace(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListNamespacesResponse(**args)


def marshal_Permissions(
    request: Permissions,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.can_manage is not None:
        output["can_manage"] = request.can_manage

    if request.can_publish is not None:
        output["can_publish"] = request.can_publish

    if request.can_receive is not None:
        output["can_receive"] = request.can_receive

    return output


def marshal_CreateCredentialRequest(
    request: CreateCredentialRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.namespace_id is not None:
        output["namespace_id"] = request.namespace_id

    if request.permissions is not None:
        output["permissions"] = marshal_Permissions(request.permissions, defaults)

    return output


def marshal_CreateNamespaceRequest(
    request: CreateNamespaceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.protocol is not None:
        output["protocol"] = NamespaceProtocol(request.protocol)

    return output


def marshal_UpdateCredentialRequest(
    request: UpdateCredentialRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.permissions is not None:
        output["permissions"] = marshal_Permissions(request.permissions, defaults)

    return output


def marshal_UpdateNamespaceRequest(
    request: UpdateNamespaceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.namespace_id is not None:
        output["namespace_id"] = request.namespace_id

    return output
