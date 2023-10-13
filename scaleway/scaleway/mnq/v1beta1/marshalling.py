# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from dateutil import parser
from .types import (
    File,
    ListNatsAccountsResponse,
    ListNatsCredentialsResponse,
    ListSnsCredentialsResponse,
    ListSqsCredentialsResponse,
    NatsAccount,
    NatsCredentials,
    SnsCredentials,
    SnsInfo,
    SnsPermissions,
    SqsCredentials,
    SqsInfo,
    SqsPermissions,
    NatsApiCreateNatsAccountRequest,
    NatsApiUpdateNatsAccountRequest,
    NatsApiCreateNatsCredentialsRequest,
    SnsApiActivateSnsRequest,
    SnsApiDeactivateSnsRequest,
    SnsApiCreateSnsCredentialsRequest,
    SnsApiUpdateSnsCredentialsRequest,
    SqsApiActivateSqsRequest,
    SqsApiDeactivateSqsRequest,
    SqsApiCreateSqsCredentialsRequest,
    SqsApiUpdateSqsCredentialsRequest,
)


def unmarshal_File(data: Any) -> File:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'File' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("content", None)
    args["content"] = field

    field = data.get("name", None)
    args["name"] = field

    return File(**args)


def unmarshal_SnsPermissions(data: Any) -> SnsPermissions:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SnsPermissions' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("can_manage", None)
    args["can_manage"] = field

    field = data.get("can_publish", None)
    args["can_publish"] = field

    field = data.get("can_receive", None)
    args["can_receive"] = field

    return SnsPermissions(**args)


def unmarshal_SqsPermissions(data: Any) -> SqsPermissions:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SqsPermissions' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("can_manage", None)
    args["can_manage"] = field

    field = data.get("can_publish", None)
    args["can_publish"] = field

    field = data.get("can_receive", None)
    args["can_receive"] = field

    return SqsPermissions(**args)


def unmarshal_NatsAccount(data: Any) -> NatsAccount:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'NatsAccount' failed as data isn't a dictionary."
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

    field = data.get("region", None)
    args["region"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return NatsAccount(**args)


def unmarshal_NatsCredentials(data: Any) -> NatsCredentials:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'NatsCredentials' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("checksum", None)
    args["checksum"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("credentials", None)
    args["credentials"] = unmarshal_File(field) if field is not None else None

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("nats_account_id", None)
    args["nats_account_id"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return NatsCredentials(**args)


def unmarshal_SnsCredentials(data: Any) -> SnsCredentials:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SnsCredentials' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("access_key", None)
    args["access_key"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("permissions", None)
    args["permissions"] = unmarshal_SnsPermissions(field) if field is not None else None

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("secret_checksum", None)
    args["secret_checksum"] = field

    field = data.get("secret_key", None)
    args["secret_key"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return SnsCredentials(**args)


def unmarshal_SqsCredentials(data: Any) -> SqsCredentials:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SqsCredentials' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("access_key", None)
    args["access_key"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("permissions", None)
    args["permissions"] = unmarshal_SqsPermissions(field) if field is not None else None

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("secret_checksum", None)
    args["secret_checksum"] = field

    field = data.get("secret_key", None)
    args["secret_key"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return SqsCredentials(**args)


def unmarshal_ListNatsAccountsResponse(data: Any) -> ListNatsAccountsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListNatsAccountsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("nats_accounts", None)
    args["nats_accounts"] = (
        [unmarshal_NatsAccount(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListNatsAccountsResponse(**args)


def unmarshal_ListNatsCredentialsResponse(data: Any) -> ListNatsCredentialsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListNatsCredentialsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("nats_credentials", None)
    args["nats_credentials"] = (
        [unmarshal_NatsCredentials(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListNatsCredentialsResponse(**args)


def unmarshal_ListSnsCredentialsResponse(data: Any) -> ListSnsCredentialsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListSnsCredentialsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("sns_credentials", None)
    args["sns_credentials"] = (
        [unmarshal_SnsCredentials(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListSnsCredentialsResponse(**args)


def unmarshal_ListSqsCredentialsResponse(data: Any) -> ListSqsCredentialsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListSqsCredentialsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("sqs_credentials", None)
    args["sqs_credentials"] = (
        [unmarshal_SqsCredentials(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListSqsCredentialsResponse(**args)


def unmarshal_SnsInfo(data: Any) -> SnsInfo:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SnsInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("sns_endpoint_url", None)
    args["sns_endpoint_url"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return SnsInfo(**args)


def unmarshal_SqsInfo(data: Any) -> SqsInfo:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SqsInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("sqs_endpoint_url", None)
    args["sqs_endpoint_url"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return SqsInfo(**args)


def marshal_SnsPermissions(
    request: SnsPermissions,
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


def marshal_SqsPermissions(
    request: SqsPermissions,
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


def marshal_NatsApiCreateNatsAccountRequest(
    request: NatsApiCreateNatsAccountRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_NatsApiCreateNatsCredentialsRequest(
    request: NatsApiCreateNatsCredentialsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.nats_account_id is not None:
        output["nats_account_id"] = request.nats_account_id

    return output


def marshal_NatsApiUpdateNatsAccountRequest(
    request: NatsApiUpdateNatsAccountRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_SnsApiActivateSnsRequest(
    request: SnsApiActivateSnsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_SnsApiCreateSnsCredentialsRequest(
    request: SnsApiCreateSnsCredentialsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.permissions is not None:
        output["permissions"] = marshal_SnsPermissions(request.permissions, defaults)

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_SnsApiDeactivateSnsRequest(
    request: SnsApiDeactivateSnsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_SnsApiUpdateSnsCredentialsRequest(
    request: SnsApiUpdateSnsCredentialsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.permissions is not None:
        output["permissions"] = marshal_SnsPermissions(request.permissions, defaults)

    return output


def marshal_SqsApiActivateSqsRequest(
    request: SqsApiActivateSqsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_SqsApiCreateSqsCredentialsRequest(
    request: SqsApiCreateSqsCredentialsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.permissions is not None:
        output["permissions"] = marshal_SqsPermissions(request.permissions, defaults)

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_SqsApiDeactivateSqsRequest(
    request: SqsApiDeactivateSqsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_SqsApiUpdateSqsCredentialsRequest(
    request: SqsApiUpdateSqsCredentialsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.permissions is not None:
        output["permissions"] = marshal_SqsPermissions(request.permissions, defaults)

    return output
