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
    APIKey,
    Application,
    Group,
    JWT,
    ListAPIKeysResponse,
    ListApplicationsResponse,
    ListGroupsResponse,
    ListJWTsResponse,
    ListPermissionSetsResponse,
    ListPoliciesResponse,
    ListQuotaResponse,
    ListRulesResponse,
    ListSSHKeysResponse,
    ListUsersResponse,
    PermissionSet,
    Policy,
    Quotum,
    Rule,
    RuleSpecs,
    SSHKey,
    SetRulesResponse,
    User,
    CreateSSHKeyRequest,
    UpdateSSHKeyRequest,
    CreateUserRequest,
    CreateApplicationRequest,
    UpdateApplicationRequest,
    CreateGroupRequest,
    UpdateGroupRequest,
    SetGroupMembersRequest,
    AddGroupMemberRequest,
    AddGroupMembersRequest,
    RemoveGroupMemberRequest,
    CreatePolicyRequest,
    UpdatePolicyRequest,
    SetRulesRequest,
    CreateAPIKeyRequest,
    UpdateAPIKeyRequest,
)


def unmarshal_APIKey(data: Any) -> APIKey:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'APIKey' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("access_key", None)
    args["access_key"] = field

    field = data.get("application_id", None)
    args["application_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("creation_ip", None)
    args["creation_ip"] = field

    field = data.get("default_project_id", None)
    args["default_project_id"] = field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("editable", None)
    args["editable"] = field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("secret_key", None)
    args["secret_key"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("user_id", None)
    args["user_id"] = field

    return APIKey(**args)


def unmarshal_Application(data: Any) -> Application:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Application' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("editable", None)
    args["editable"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("nb_api_keys", None)
    args["nb_api_keys"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Application(**args)


def unmarshal_Group(data: Any) -> Group:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Group' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("application_ids", None)
    args["application_ids"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("user_ids", None)
    args["user_ids"] = field

    return Group(**args)


def unmarshal_JWT(data: Any) -> JWT:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'JWT' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("audience_id", None)
    args["audience_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("ip", None)
    args["ip"] = field

    field = data.get("issuer_id", None)
    args["issuer_id"] = field

    field = data.get("jti", None)
    args["jti"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("user_agent", None)
    args["user_agent"] = field

    return JWT(**args)


def unmarshal_PermissionSet(data: Any) -> PermissionSet:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PermissionSet' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("categories", None)
    args["categories"] = field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("scope_type", None)
    args["scope_type"] = field

    return PermissionSet(**args)


def unmarshal_Policy(data: Any) -> Policy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Policy' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("application_id", None)
    args["application_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("editable", None)
    args["editable"] = field

    field = data.get("group_id", None)
    args["group_id"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("nb_permission_sets", None)
    args["nb_permission_sets"] = field

    field = data.get("nb_rules", None)
    args["nb_rules"] = field

    field = data.get("nb_scopes", None)
    args["nb_scopes"] = field

    field = data.get("no_principal", None)
    args["no_principal"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("user_id", None)
    args["user_id"] = field

    return Policy(**args)


def unmarshal_Quotum(data: Any) -> Quotum:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Quotum' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("limit", None)
    args["limit"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("unlimited", None)
    args["unlimited"] = field

    return Quotum(**args)


def unmarshal_Rule(data: Any) -> Rule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Rule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("account_root_user_id", None)
    args["account_root_user_id"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("permission_set_names", None)
    args["permission_set_names"] = field

    field = data.get("permission_sets_scope_type", None)
    args["permission_sets_scope_type"] = field

    field = data.get("project_ids", None)
    args["project_ids"] = field

    return Rule(**args)


def unmarshal_SSHKey(data: Any) -> SSHKey:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SSHKey' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("disabled", None)
    args["disabled"] = field

    field = data.get("fingerprint", None)
    args["fingerprint"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("public_key", None)
    args["public_key"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return SSHKey(**args)


def unmarshal_User(data: Any) -> User:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'User' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("account_root_user_id", None)
    args["account_root_user_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("deletable", None)
    args["deletable"] = field

    field = data.get("email", None)
    args["email"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("last_login_at", None)
    args["last_login_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("mfa", None)
    args["mfa"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("two_factor_enabled", None)
    args["two_factor_enabled"] = field

    field = data.get("type", None)
    args["type_"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return User(**args)


def unmarshal_ListAPIKeysResponse(data: Any) -> ListAPIKeysResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListAPIKeysResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("api_keys", None)
    args["api_keys"] = (
        [unmarshal_APIKey(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListAPIKeysResponse(**args)


def unmarshal_ListApplicationsResponse(data: Any) -> ListApplicationsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListApplicationsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("applications", None)
    args["applications"] = (
        [unmarshal_Application(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListApplicationsResponse(**args)


def unmarshal_ListGroupsResponse(data: Any) -> ListGroupsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListGroupsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("groups", None)
    args["groups"] = [unmarshal_Group(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListGroupsResponse(**args)


def unmarshal_ListJWTsResponse(data: Any) -> ListJWTsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListJWTsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("jwts", None)
    args["jwts"] = [unmarshal_JWT(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListJWTsResponse(**args)


def unmarshal_ListPermissionSetsResponse(data: Any) -> ListPermissionSetsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPermissionSetsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("permission_sets", None)
    args["permission_sets"] = (
        [unmarshal_PermissionSet(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListPermissionSetsResponse(**args)


def unmarshal_ListPoliciesResponse(data: Any) -> ListPoliciesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPoliciesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("policies", None)
    args["policies"] = (
        [unmarshal_Policy(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListPoliciesResponse(**args)


def unmarshal_ListQuotaResponse(data: Any) -> ListQuotaResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListQuotaResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("quota", None)
    args["quota"] = [unmarshal_Quotum(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListQuotaResponse(**args)


def unmarshal_ListRulesResponse(data: Any) -> ListRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", None)
    args["rules"] = [unmarshal_Rule(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListRulesResponse(**args)


def unmarshal_ListSSHKeysResponse(data: Any) -> ListSSHKeysResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSSHKeysResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ssh_keys", None)
    args["ssh_keys"] = (
        [unmarshal_SSHKey(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListSSHKeysResponse(**args)


def unmarshal_ListUsersResponse(data: Any) -> ListUsersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListUsersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    args["total_count"] = field

    field = data.get("users", None)
    args["users"] = [unmarshal_User(v) for v in field] if field is not None else None

    return ListUsersResponse(**args)


def unmarshal_SetRulesResponse(data: Any) -> SetRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", None)
    args["rules"] = [unmarshal_Rule(v) for v in field] if field is not None else None

    return SetRulesResponse(**args)


def marshal_RuleSpecs(
    request: RuleSpecs,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "project_ids",
                    request.project_ids if request.project_ids is not None else None,
                ),
                OneOfPossibility(
                    "organization_id",
                    request.organization_id
                    if request.organization_id is not None
                    else None,
                    defaults.default_organization_id,
                ),
            ]
        ),
    )

    if request.permission_set_names is not None:
        output["permission_set_names"] = request.permission_set_names

    return output


def marshal_AddGroupMemberRequest(
    request: AddGroupMemberRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "user_id", request.user_id if request.user_id is not None else None
                ),
                OneOfPossibility(
                    "application_id",
                    request.application_id
                    if request.application_id is not None
                    else None,
                ),
            ]
        ),
    )

    return output


def marshal_AddGroupMembersRequest(
    request: AddGroupMembersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.application_ids is not None:
        output["application_ids"] = request.application_ids

    if request.user_ids is not None:
        output["user_ids"] = request.user_ids

    return output


def marshal_CreateAPIKeyRequest(
    request: CreateAPIKeyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "application_id",
                    request.application_id
                    if request.application_id is not None
                    else None,
                ),
                OneOfPossibility(
                    "user_id", request.user_id if request.user_id is not None else None
                ),
            ]
        ),
    )

    if request.default_project_id is not None:
        output["default_project_id"] = request.default_project_id

    if request.description is not None:
        output["description"] = request.description

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at

    return output


def marshal_CreateApplicationRequest(
    request: CreateApplicationRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.name is not None:
        output["name"] = request.name

    if request.organization_id is not None:
        output["organization_id"] = (
            request.organization_id or defaults.default_organization_id
        )

    return output


def marshal_CreateGroupRequest(
    request: CreateGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.name is not None:
        output["name"] = request.name

    if request.organization_id is not None:
        output["organization_id"] = (
            request.organization_id or defaults.default_organization_id
        )

    return output


def marshal_CreatePolicyRequest(
    request: CreatePolicyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "user_id", request.user_id if request.user_id is not None else None
                ),
                OneOfPossibility(
                    "group_id",
                    request.group_id if request.group_id is not None else None,
                ),
                OneOfPossibility(
                    "application_id",
                    request.application_id
                    if request.application_id is not None
                    else None,
                ),
                OneOfPossibility(
                    "no_principal",
                    request.no_principal if request.no_principal is not None else None,
                ),
            ]
        ),
    )

    if request.description is not None:
        output["description"] = request.description

    if request.name is not None:
        output["name"] = request.name

    if request.organization_id is not None:
        output["organization_id"] = (
            request.organization_id or defaults.default_organization_id
        )

    if request.rules is not None:
        output["rules"] = [marshal_RuleSpecs(v, defaults) for v in request.rules]

    return output


def marshal_CreateSSHKeyRequest(
    request: CreateSSHKeyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.public_key is not None:
        output["public_key"] = request.public_key

    return output


def marshal_CreateUserRequest(
    request: CreateUserRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.email is not None:
        output["email"] = request.email

    if request.organization_id is not None:
        output["organization_id"] = (
            request.organization_id or defaults.default_organization_id
        )

    return output


def marshal_RemoveGroupMemberRequest(
    request: RemoveGroupMemberRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "user_id", request.user_id if request.user_id is not None else None
                ),
                OneOfPossibility(
                    "application_id",
                    request.application_id
                    if request.application_id is not None
                    else None,
                ),
            ]
        ),
    )

    return output


def marshal_SetGroupMembersRequest(
    request: SetGroupMembersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.application_ids is not None:
        output["application_ids"] = request.application_ids

    if request.user_ids is not None:
        output["user_ids"] = request.user_ids

    return output


def marshal_SetRulesRequest(
    request: SetRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.policy_id is not None:
        output["policy_id"] = request.policy_id

    if request.rules is not None:
        output["rules"] = [marshal_RuleSpecs(v, defaults) for v in request.rules]

    return output


def marshal_UpdateAPIKeyRequest(
    request: UpdateAPIKeyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.default_project_id is not None:
        output["default_project_id"] = request.default_project_id

    if request.description is not None:
        output["description"] = request.description

    return output


def marshal_UpdateApplicationRequest(
    request: UpdateApplicationRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_UpdateGroupRequest(
    request: UpdateGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_UpdatePolicyRequest(
    request: UpdatePolicyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    "user_id", request.user_id if request.user_id is not None else None
                ),
                OneOfPossibility(
                    "group_id",
                    request.group_id if request.group_id is not None else None,
                ),
                OneOfPossibility(
                    "application_id",
                    request.application_id
                    if request.application_id is not None
                    else None,
                ),
                OneOfPossibility(
                    "no_principal",
                    request.no_principal if request.no_principal is not None else None,
                ),
            ]
        ),
    )

    if request.description is not None:
        output["description"] = request.description

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_UpdateSSHKeyRequest(
    request: UpdateSSHKeyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.disabled is not None:
        output["disabled"] = request.disabled

    if request.name is not None:
        output["name"] = request.name

    return output
