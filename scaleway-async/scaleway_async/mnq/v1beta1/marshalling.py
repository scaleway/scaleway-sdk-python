# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    SnsInfoStatus,
    SqsInfoStatus,
    NatsAccount,
    File,
    NatsCredentials,
    SnsPermissions,
    SnsCredentials,
    SqsPermissions,
    SqsCredentials,
    ListNatsAccountsResponse,
    ListNatsCredentialsResponse,
    ListSnsCredentialsResponse,
    ListSqsCredentialsResponse,
    SnsInfo,
    SqsInfo,
    NatsApiCreateNatsAccountRequest,
    NatsApiCreateNatsCredentialsRequest,
    NatsApiUpdateNatsAccountRequest,
    SnsApiActivateSnsRequest,
    SnsApiCreateSnsCredentialsRequest,
    SnsApiDeactivateSnsRequest,
    SnsApiUpdateSnsCredentialsRequest,
    SqsApiActivateSqsRequest,
    SqsApiCreateSqsCredentialsRequest,
    SqsApiDeactivateSqsRequest,
    SqsApiUpdateSqsCredentialsRequest,
)


def unmarshal_NatsAccount(data: Any) -> NatsAccount:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NatsAccount' failed as data isn't a dictionary."
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

    field = data.get("endpoint", None)
    if field is not None:
        args["endpoint"] = field
    else:
        args["endpoint"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return NatsAccount(**args)


def unmarshal_File(data: Any) -> File:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'File' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("content", None)
    if field is not None:
        args["content"] = field
    else:
        args["content"] = None

    return File(**args)


def unmarshal_NatsCredentials(data: Any) -> NatsCredentials:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NatsCredentials' failed as data isn't a dictionary."
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

    field = data.get("nats_account_id", None)
    if field is not None:
        args["nats_account_id"] = field
    else:
        args["nats_account_id"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("checksum", None)
    if field is not None:
        args["checksum"] = field
    else:
        args["checksum"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("credentials", None)
    if field is not None:
        args["credentials"] = unmarshal_File(field)
    else:
        args["credentials"] = None

    return NatsCredentials(**args)


def unmarshal_SnsPermissions(data: Any) -> SnsPermissions:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SnsPermissions' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("can_publish", None)
    if field is not None:
        args["can_publish"] = field
    else:
        args["can_publish"] = False

    field = data.get("can_receive", None)
    if field is not None:
        args["can_receive"] = field
    else:
        args["can_receive"] = False

    field = data.get("can_manage", None)
    if field is not None:
        args["can_manage"] = field
    else:
        args["can_manage"] = False

    return SnsPermissions(**args)


def unmarshal_SnsCredentials(data: Any) -> SnsCredentials:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SnsCredentials' failed as data isn't a dictionary."
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

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("access_key", None)
    if field is not None:
        args["access_key"] = field
    else:
        args["access_key"] = None

    field = data.get("secret_key", None)
    if field is not None:
        args["secret_key"] = field
    else:
        args["secret_key"] = None

    field = data.get("secret_checksum", None)
    if field is not None:
        args["secret_checksum"] = field
    else:
        args["secret_checksum"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("permissions", None)
    if field is not None:
        args["permissions"] = unmarshal_SnsPermissions(field)
    else:
        args["permissions"] = None

    return SnsCredentials(**args)


def unmarshal_SqsPermissions(data: Any) -> SqsPermissions:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SqsPermissions' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("can_publish", None)
    if field is not None:
        args["can_publish"] = field
    else:
        args["can_publish"] = False

    field = data.get("can_receive", None)
    if field is not None:
        args["can_receive"] = field
    else:
        args["can_receive"] = False

    field = data.get("can_manage", None)
    if field is not None:
        args["can_manage"] = field
    else:
        args["can_manage"] = False

    return SqsPermissions(**args)


def unmarshal_SqsCredentials(data: Any) -> SqsCredentials:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SqsCredentials' failed as data isn't a dictionary."
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

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("access_key", None)
    if field is not None:
        args["access_key"] = field
    else:
        args["access_key"] = None

    field = data.get("secret_key", None)
    if field is not None:
        args["secret_key"] = field
    else:
        args["secret_key"] = None

    field = data.get("secret_checksum", None)
    if field is not None:
        args["secret_checksum"] = field
    else:
        args["secret_checksum"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("permissions", None)
    if field is not None:
        args["permissions"] = unmarshal_SqsPermissions(field)
    else:
        args["permissions"] = None

    return SqsCredentials(**args)


def unmarshal_ListNatsAccountsResponse(data: Any) -> ListNatsAccountsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNatsAccountsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("nats_accounts", None)
    if field is not None:
        args["nats_accounts"] = (
            [unmarshal_NatsAccount(v) for v in field] if field is not None else None
        )
    else:
        args["nats_accounts"] = []

    return ListNatsAccountsResponse(**args)


def unmarshal_ListNatsCredentialsResponse(data: Any) -> ListNatsCredentialsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNatsCredentialsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("nats_credentials", None)
    if field is not None:
        args["nats_credentials"] = (
            [unmarshal_NatsCredentials(v) for v in field] if field is not None else None
        )
    else:
        args["nats_credentials"] = []

    return ListNatsCredentialsResponse(**args)


def unmarshal_ListSnsCredentialsResponse(data: Any) -> ListSnsCredentialsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSnsCredentialsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("sns_credentials", None)
    if field is not None:
        args["sns_credentials"] = (
            [unmarshal_SnsCredentials(v) for v in field] if field is not None else None
        )
    else:
        args["sns_credentials"] = []

    return ListSnsCredentialsResponse(**args)


def unmarshal_ListSqsCredentialsResponse(data: Any) -> ListSqsCredentialsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSqsCredentialsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("sqs_credentials", None)
    if field is not None:
        args["sqs_credentials"] = (
            [unmarshal_SqsCredentials(v) for v in field] if field is not None else None
        )
    else:
        args["sqs_credentials"] = []

    return ListSqsCredentialsResponse(**args)


def unmarshal_SnsInfo(data: Any) -> SnsInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SnsInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = SnsInfoStatus.UNKNOWN_STATUS

    field = data.get("sns_endpoint_url", None)
    if field is not None:
        args["sns_endpoint_url"] = field
    else:
        args["sns_endpoint_url"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return SnsInfo(**args)


def unmarshal_SqsInfo(data: Any) -> SqsInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SqsInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = SqsInfoStatus.UNKNOWN_STATUS

    field = data.get("sqs_endpoint_url", None)
    if field is not None:
        args["sqs_endpoint_url"] = field
    else:
        args["sqs_endpoint_url"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return SqsInfo(**args)


def marshal_NatsApiCreateNatsAccountRequest(
    request: NatsApiCreateNatsAccountRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_NatsApiCreateNatsCredentialsRequest(
    request: NatsApiCreateNatsCredentialsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.nats_account_id is not None:
        output["nats_account_id"] = request.nats_account_id

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_NatsApiUpdateNatsAccountRequest(
    request: NatsApiUpdateNatsAccountRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_SnsApiActivateSnsRequest(
    request: SnsApiActivateSnsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_SnsPermissions(
    request: SnsPermissions,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.can_publish is not None:
        output["can_publish"] = request.can_publish

    if request.can_receive is not None:
        output["can_receive"] = request.can_receive

    if request.can_manage is not None:
        output["can_manage"] = request.can_manage

    return output


def marshal_SnsApiCreateSnsCredentialsRequest(
    request: SnsApiCreateSnsCredentialsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.name is not None:
        output["name"] = request.name

    if request.permissions is not None:
        output["permissions"] = marshal_SnsPermissions(request.permissions, defaults)

    return output


def marshal_SnsApiDeactivateSnsRequest(
    request: SnsApiDeactivateSnsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_SnsApiUpdateSnsCredentialsRequest(
    request: SnsApiUpdateSnsCredentialsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.permissions is not None:
        output["permissions"] = marshal_SnsPermissions(request.permissions, defaults)

    return output


def marshal_SqsApiActivateSqsRequest(
    request: SqsApiActivateSqsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_SqsPermissions(
    request: SqsPermissions,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.can_publish is not None:
        output["can_publish"] = request.can_publish

    if request.can_receive is not None:
        output["can_receive"] = request.can_receive

    if request.can_manage is not None:
        output["can_manage"] = request.can_manage

    return output


def marshal_SqsApiCreateSqsCredentialsRequest(
    request: SqsApiCreateSqsCredentialsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.name is not None:
        output["name"] = request.name

    if request.permissions is not None:
        output["permissions"] = marshal_SqsPermissions(request.permissions, defaults)

    return output


def marshal_SqsApiDeactivateSqsRequest(
    request: SqsApiDeactivateSqsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_SqsApiUpdateSqsCredentialsRequest(
    request: SqsApiUpdateSqsCredentialsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.permissions is not None:
        output["permissions"] = marshal_SqsPermissions(request.permissions, defaults)

    return output
