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
    BrowseSecretsRequestOrderBy,
    EphemeralPolicyAction,
    ListSecretsRequestOrderBy,
    Product,
    SecretStatus,
    SecretType,
    SecretVersionStatus,
    EphemeralProperties,
    SecretVersion,
    EphemeralPolicy,
    Secret,
    AccessSecretVersionResponse,
    BrowseSecretsResponseItemFolderDetails,
    BrowseSecretsResponseItemSecretDetails,
    BrowseSecretsResponseItem,
    BrowseSecretsResponse,
    ListSecretTypesResponse,
    ListSecretVersionsResponse,
    ListSecretsResponse,
    ListTagsResponse,
    AddSecretOwnerRequest,
    CreateSecretRequest,
    CreateSecretVersionRequest,
    UpdateSecretRequest,
    UpdateSecretVersionRequest,
)

def unmarshal_EphemeralProperties(data: Any) -> EphemeralProperties:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EphemeralProperties' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("action", getattr(EphemeralPolicyAction, "UNKNOWN_ACTION"))
    args["action"] = field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("expires_once_accessed", None)
    args["expires_once_accessed"] = field

    return EphemeralProperties(**args)

def unmarshal_SecretVersion(data: Any) -> SecretVersion:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecretVersion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("revision", 0)
    args["revision"] = field

    field = data.get("secret_id", str())
    args["secret_id"] = field

    field = data.get("status", getattr(SecretVersionStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("latest", False)
    args["latest"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("deleted_at", None)
    args["deleted_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("ephemeral_properties", None)
    args["ephemeral_properties"] = unmarshal_EphemeralProperties(field) if field is not None else None

    field = data.get("deletion_requested_at", None)
    args["deletion_requested_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return SecretVersion(**args)

def unmarshal_EphemeralPolicy(data: Any) -> EphemeralPolicy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EphemeralPolicy' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("action", getattr(EphemeralPolicyAction, "UNKNOWN_ACTION"))
    args["action"] = field

    field = data.get("time_to_live", None)
    args["time_to_live"] = field

    field = data.get("expires_once_accessed", None)
    args["expires_once_accessed"] = field

    return EphemeralPolicy(**args)

def unmarshal_Secret(data: Any) -> Secret:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Secret' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("status", getattr(SecretStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("version_count", 0)
    args["version_count"] = field

    field = data.get("managed", False)
    args["managed"] = field

    field = data.get("protected", False)
    args["protected"] = field

    field = data.get("type", getattr(SecretType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("path", str())
    args["path"] = field

    field = data.get("used_by", [])
    args["used_by"] = [Product(v) for v in field] if field is not None else None

    field = data.get("region", )
    args["region"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("ephemeral_policy", None)
    args["ephemeral_policy"] = unmarshal_EphemeralPolicy(field) if field is not None else None

    field = data.get("deletion_requested_at", None)
    args["deletion_requested_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("key_id", None)
    args["key_id"] = field

    return Secret(**args)

def unmarshal_AccessSecretVersionResponse(data: Any) -> AccessSecretVersionResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AccessSecretVersionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("secret_id", str())
    args["secret_id"] = field

    field = data.get("revision", 0)
    args["revision"] = field

    field = data.get("data", str())
    args["data"] = field

    field = data.get("type", getattr(SecretType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("data_crc32", None)
    args["data_crc32"] = field

    return AccessSecretVersionResponse(**args)

def unmarshal_BrowseSecretsResponseItemFolderDetails(data: Any) -> BrowseSecretsResponseItemFolderDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BrowseSecretsResponseItemFolderDetails' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return BrowseSecretsResponseItemFolderDetails(**args)

def unmarshal_BrowseSecretsResponseItemSecretDetails(data: Any) -> BrowseSecretsResponseItemSecretDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BrowseSecretsResponseItemSecretDetails' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("tags", str())
    args["tags"] = field

    field = data.get("version_count", str())
    args["version_count"] = field

    field = data.get("protected", str())
    args["protected"] = field

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("ephemeral_policy", None)
    args["ephemeral_policy"] = unmarshal_EphemeralPolicy(field) if field is not None else None

    return BrowseSecretsResponseItemSecretDetails(**args)

def unmarshal_BrowseSecretsResponseItem(data: Any) -> BrowseSecretsResponseItem:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BrowseSecretsResponseItem' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("secret", None)
    args["secret"] = unmarshal_BrowseSecretsResponseItemSecretDetails(field) if field is not None else None

    field = data.get("folder", None)
    args["folder"] = unmarshal_BrowseSecretsResponseItemFolderDetails(field) if field is not None else None

    return BrowseSecretsResponseItem(**args)

def unmarshal_BrowseSecretsResponse(data: Any) -> BrowseSecretsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BrowseSecretsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("items", [])
    args["items"] = [unmarshal_BrowseSecretsResponseItem(v) for v in field] if field is not None else None

    field = data.get("current_path", str())
    args["current_path"] = field

    field = data.get("total_count", 0)
    args["total_count"] = field

    return BrowseSecretsResponse(**args)

def unmarshal_ListSecretTypesResponse(data: Any) -> ListSecretTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSecretTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("types", [])
    args["types"] = [SecretType(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListSecretTypesResponse(**args)

def unmarshal_ListSecretVersionsResponse(data: Any) -> ListSecretVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSecretVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("versions", [])
    args["versions"] = [unmarshal_SecretVersion(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListSecretVersionsResponse(**args)

def unmarshal_ListSecretsResponse(data: Any) -> ListSecretsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSecretsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("secrets", [])
    args["secrets"] = [unmarshal_Secret(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListSecretsResponse(**args)

def unmarshal_ListTagsResponse(data: Any) -> ListTagsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTagsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListTagsResponse(**args)

def marshal_AddSecretOwnerRequest(
    request: AddSecretOwnerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.product is not None:
        output["product"] = str(request.product)
    else:
        output["product"] = None


    return output

def marshal_EphemeralPolicy(
    request: EphemeralPolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = str(request.action)
    else:
        output["action"] = getattr(EphemeralPolicyAction, "UNKNOWN_ACTION")

    if request.time_to_live is not None:
        output["time_to_live"] = request.time_to_live
    else:
        output["time_to_live"] = None

    if request.expires_once_accessed is not None:
        output["expires_once_accessed"] = request.expires_once_accessed
    else:
        output["expires_once_accessed"] = None


    return output

def marshal_CreateSecretRequest(
    request: CreateSecretRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.protected is not None:
        output["protected"] = request.protected
    else:
        output["protected"] = False

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = None

    if request.path is not None:
        output["path"] = request.path
    else:
        output["path"] = None

    if request.ephemeral_policy is not None:
        output["ephemeral_policy"] = marshal_EphemeralPolicy(request.ephemeral_policy, defaults)
    else:
        output["ephemeral_policy"] = None

    if request.key_id is not None:
        output["key_id"] = request.key_id
    else:
        output["key_id"] = None


    return output

def marshal_CreateSecretVersionRequest(
    request: CreateSecretVersionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.data is not None:
        output["data"] = request.data
    else:
        output["data"] = str()

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.disable_previous is not None:
        output["disable_previous"] = request.disable_previous
    else:
        output["disable_previous"] = None

    if request.data_crc32 is not None:
        output["data_crc32"] = request.data_crc32
    else:
        output["data_crc32"] = None


    return output

def marshal_UpdateSecretRequest(
    request: UpdateSecretRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.path is not None:
        output["path"] = request.path
    else:
        output["path"] = None

    if request.ephemeral_policy is not None:
        output["ephemeral_policy"] = marshal_EphemeralPolicy(request.ephemeral_policy, defaults)
    else:
        output["ephemeral_policy"] = None


    return output

def marshal_EphemeralProperties(
    request: EphemeralProperties,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = str(request.action)
    else:
        output["action"] = getattr(EphemeralPolicyAction, "UNKNOWN_ACTION")

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()
    else:
        output["expires_at"] = None

    if request.expires_once_accessed is not None:
        output["expires_once_accessed"] = request.expires_once_accessed
    else:
        output["expires_once_accessed"] = None


    return output

def marshal_UpdateSecretVersionRequest(
    request: UpdateSecretVersionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.ephemeral_properties is not None:
        output["ephemeral_properties"] = marshal_EphemeralProperties(request.ephemeral_properties, defaults)
    else:
        output["ephemeral_properties"] = None


    return output
