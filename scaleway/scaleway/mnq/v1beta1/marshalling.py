# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from decimal import Decimal
from datetime import datetime
from typing import Any, Dict, List, Optional
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
    unmarshal_Money,
    marshal_Money,
    marshal_ScwFile,
    marshal_ServiceInfo,
    marshal_TimeSeries,
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    ListNatsAccountsRequestOrderBy,
    ListNatsCredentialsRequestOrderBy,
    ListSnsCredentialsRequestOrderBy,
    ListSqsCredentialsRequestOrderBy,
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

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("endpoint", str())
    args["endpoint"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return NatsAccount(**args)

def unmarshal_File(data: Any) -> File:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'File' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("content", str())
    args["content"] = field

    return File(**args)

def unmarshal_NatsCredentials(data: Any) -> NatsCredentials:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NatsCredentials' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("nats_account_id", str())
    args["nats_account_id"] = field

    field = data.get("checksum", str())
    args["checksum"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("credentials", None)
    args["credentials"] = unmarshal_File(field) if field is not None else None

    return NatsCredentials(**args)

def unmarshal_SnsPermissions(data: Any) -> SnsPermissions:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SnsPermissions' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("can_publish", None)
    args["can_publish"] = field

    field = data.get("can_receive", None)
    args["can_receive"] = field

    field = data.get("can_manage", None)
    args["can_manage"] = field

    return SnsPermissions(**args)

def unmarshal_SnsCredentials(data: Any) -> SnsCredentials:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SnsCredentials' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("access_key", str())
    args["access_key"] = field

    field = data.get("secret_key", str())
    args["secret_key"] = field

    field = data.get("secret_checksum", str())
    args["secret_checksum"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("permissions", None)
    args["permissions"] = unmarshal_SnsPermissions(field) if field is not None else None

    return SnsCredentials(**args)

def unmarshal_SqsPermissions(data: Any) -> SqsPermissions:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SqsPermissions' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("can_publish", None)
    args["can_publish"] = field

    field = data.get("can_receive", None)
    args["can_receive"] = field

    field = data.get("can_manage", None)
    args["can_manage"] = field

    return SqsPermissions(**args)

def unmarshal_SqsCredentials(data: Any) -> SqsCredentials:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SqsCredentials' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("access_key", str())
    args["access_key"] = field

    field = data.get("secret_key", str())
    args["secret_key"] = field

    field = data.get("secret_checksum", str())
    args["secret_checksum"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("permissions", None)
    args["permissions"] = unmarshal_SqsPermissions(field) if field is not None else None

    return SqsCredentials(**args)

def unmarshal_ListNatsAccountsResponse(data: Any) -> ListNatsAccountsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNatsAccountsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("nats_accounts", [])
    args["nats_accounts"] = [unmarshal_NatsAccount(v) for v in field] if field is not None else None

    return ListNatsAccountsResponse(**args)

def unmarshal_ListNatsCredentialsResponse(data: Any) -> ListNatsCredentialsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNatsCredentialsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("nats_credentials", [])
    args["nats_credentials"] = [unmarshal_NatsCredentials(v) for v in field] if field is not None else None

    return ListNatsCredentialsResponse(**args)

def unmarshal_ListSnsCredentialsResponse(data: Any) -> ListSnsCredentialsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSnsCredentialsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("sns_credentials", [])
    args["sns_credentials"] = [unmarshal_SnsCredentials(v) for v in field] if field is not None else None

    return ListSnsCredentialsResponse(**args)

def unmarshal_ListSqsCredentialsResponse(data: Any) -> ListSqsCredentialsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSqsCredentialsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("sqs_credentials", [])
    args["sqs_credentials"] = [unmarshal_SqsCredentials(v) for v in field] if field is not None else None

    return ListSqsCredentialsResponse(**args)

def unmarshal_SnsInfo(data: Any) -> SnsInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SnsInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("status", getattr(SnsInfoStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("sns_endpoint_url", str())
    args["sns_endpoint_url"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return SnsInfo(**args)

def unmarshal_SqsInfo(data: Any) -> SqsInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SqsInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("status", getattr(SqsInfoStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("sqs_endpoint_url", str())
    args["sqs_endpoint_url"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return SqsInfo(**args)

def marshal_NatsApiCreateNatsAccountRequest(
    request: NatsApiCreateNatsAccountRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_NatsApiCreateNatsCredentialsRequest(
    request: NatsApiCreateNatsCredentialsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.nats_account_id is not None:
        output["nats_account_id"] = request.nats_account_id
    else:
        output["nats_account_id"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None


    return output

def marshal_NatsApiUpdateNatsAccountRequest(
    request: NatsApiUpdateNatsAccountRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None


    return output

def marshal_SnsApiActivateSnsRequest(
    request: SnsApiActivateSnsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_SnsPermissions(
    request: SnsPermissions,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.can_publish is not None:
        output["can_publish"] = request.can_publish
    else:
        output["can_publish"] = None

    if request.can_receive is not None:
        output["can_receive"] = request.can_receive
    else:
        output["can_receive"] = None

    if request.can_manage is not None:
        output["can_manage"] = request.can_manage
    else:
        output["can_manage"] = None


    return output

def marshal_SnsApiCreateSnsCredentialsRequest(
    request: SnsApiCreateSnsCredentialsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.permissions is not None:
        output["permissions"] = marshal_SnsPermissions(request.permissions, defaults)
    else:
        output["permissions"] = None


    return output

def marshal_SnsApiDeactivateSnsRequest(
    request: SnsApiDeactivateSnsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_SnsApiUpdateSnsCredentialsRequest(
    request: SnsApiUpdateSnsCredentialsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.permissions is not None:
        output["permissions"] = marshal_SnsPermissions(request.permissions, defaults)
    else:
        output["permissions"] = None


    return output

def marshal_SqsApiActivateSqsRequest(
    request: SqsApiActivateSqsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_SqsPermissions(
    request: SqsPermissions,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.can_publish is not None:
        output["can_publish"] = request.can_publish
    else:
        output["can_publish"] = None

    if request.can_receive is not None:
        output["can_receive"] = request.can_receive
    else:
        output["can_receive"] = None

    if request.can_manage is not None:
        output["can_manage"] = request.can_manage
    else:
        output["can_manage"] = None


    return output

def marshal_SqsApiCreateSqsCredentialsRequest(
    request: SqsApiCreateSqsCredentialsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.permissions is not None:
        output["permissions"] = marshal_SqsPermissions(request.permissions, defaults)
    else:
        output["permissions"] = None


    return output

def marshal_SqsApiDeactivateSqsRequest(
    request: SqsApiDeactivateSqsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_SqsApiUpdateSqsCredentialsRequest(
    request: SqsApiUpdateSqsCredentialsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.permissions is not None:
        output["permissions"] = marshal_SqsPermissions(request.permissions, defaults)
    else:
        output["permissions"] = None


    return output
