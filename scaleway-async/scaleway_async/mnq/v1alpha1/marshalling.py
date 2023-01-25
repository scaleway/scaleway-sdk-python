# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
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

    field = data.get("can_manage")
    args["can_manage"] = field

    field = data.get("can_publish")
    args["can_publish"] = field

    field = data.get("can_receive")
    args["can_receive"] = field

    return Permissions(**args)


def unmarshal_CredentialSummarySQSSNSCreds(data: Any) -> CredentialSummarySQSSNSCreds:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CredentialSummarySQSSNSCreds' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("access_key")
    args["access_key"] = field

    field = data.get("permissions")
    args["permissions"] = unmarshal_Permissions(field) if field is not None else None

    return CredentialSummarySQSSNSCreds(**args)


def unmarshal_CredentialNATSCredsFile(data: Any) -> CredentialNATSCredsFile:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CredentialNATSCredsFile' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("content")
    args["content"] = field

    return CredentialNATSCredsFile(**args)


def unmarshal_CredentialSQSSNSCreds(data: Any) -> CredentialSQSSNSCreds:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CredentialSQSSNSCreds' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("access_key")
    args["access_key"] = field

    field = data.get("permissions")
    args["permissions"] = unmarshal_Permissions(field) if field is not None else None

    field = data.get("secret_key")
    args["secret_key"] = field

    return CredentialSQSSNSCreds(**args)


def unmarshal_CredentialSummary(data: Any) -> CredentialSummary:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CredentialSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("namespace_id")
    args["namespace_id"] = field

    field = data.get("protocol")
    args["protocol"] = field

    field = data.get("sqs_sns_credentials")
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

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("endpoint")
    args["endpoint"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("protocol")
    args["protocol"] = field

    field = data.get("region")
    args["region"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return Namespace(**args)


def unmarshal_Credential(data: Any) -> Credential:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Credential' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("namespace_id")
    args["namespace_id"] = field

    field = data.get("nats_credentials")
    args["nats_credentials"] = (
        unmarshal_CredentialNATSCredsFile(field) if field is not None else None
    )

    field = data.get("protocol")
    args["protocol"] = field

    field = data.get("sqs_sns_credentials")
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

    field = data.get("credentials")
    args["credentials"] = [unmarshal_CredentialSummary(v) for v in data["credentials"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListCredentialsResponse(**args)


def unmarshal_ListNamespacesResponse(data: Any) -> ListNamespacesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListNamespacesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("namespaces")
    args["namespaces"] = [unmarshal_Namespace(v) for v in data["namespaces"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListNamespacesResponse(**args)


def marshal_Permissions(
    request: Permissions,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "can_manage": request.can_manage,
        "can_publish": request.can_publish,
        "can_receive": request.can_receive,
    }


def marshal_CreateCredentialRequest(
    request: CreateCredentialRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("permissions", request.permissions),
            ]
        ),
        "name": request.name,
        "namespace_id": request.namespace_id,
    }


def marshal_CreateNamespaceRequest(
    request: CreateNamespaceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name": request.name,
        "project_id": request.project_id or defaults.default_project_id,
        "protocol": NamespaceProtocol(request.protocol)
        if request.protocol is not None
        else None,
    }


def marshal_UpdateCredentialRequest(
    request: UpdateCredentialRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("permissions", request.permissions),
            ]
        ),
        "name": request.name,
    }


def marshal_UpdateNamespaceRequest(
    request: UpdateNamespaceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name": request.name,
        "namespace_id": request.namespace_id,
    }
