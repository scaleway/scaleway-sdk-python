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
    ListAPIKeysResponse,
    ListApplicationsResponse,
    ListGroupsResponse,
    ListPermissionSetsResponse,
    ListPoliciesResponse,
    ListRulesResponse,
    ListSSHKeysResponse,
    ListUsersResponse,
    PermissionSet,
    Policy,
    Rule,
    RuleSpecs,
    SSHKey,
    SetRulesResponse,
    User,
    CreateSSHKeyRequest,
    UpdateSSHKeyRequest,
    CreateApplicationRequest,
    UpdateApplicationRequest,
    CreateGroupRequest,
    UpdateGroupRequest,
    SetGroupMembersRequest,
    AddGroupMemberRequest,
    RemoveGroupMemberRequest,
    CreatePolicyRequest,
    UpdatePolicyRequest,
    SetRulesRequest,
    CreateAPIKeyRequest,
    UpdateAPIKeyRequest,
)


def unmarshal_APIKey(data: Any) -> APIKey:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'APIKey' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("access_key")
    args["access_key"] = field

    field = data.get("application_id")
    args["application_id"] = field

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("creation_ip")
    args["creation_ip"] = field

    field = data.get("default_project_id")
    args["default_project_id"] = field

    field = data.get("description")
    args["description"] = field

    field = data.get("editable")
    args["editable"] = field

    field = data.get("expires_at")
    args["expires_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("secret_key")
    args["secret_key"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("user_id")
    args["user_id"] = field

    return APIKey(**args)


def unmarshal_Application(data: Any) -> Application:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Application' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description")
    args["description"] = field

    field = data.get("editable")
    args["editable"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("nb_api_keys")
    args["nb_api_keys"] = field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return Application(**args)


def unmarshal_Group(data: Any) -> Group:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Group' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("application_ids")
    args["application_ids"] = field

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description")
    args["description"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("user_ids")
    args["user_ids"] = field

    return Group(**args)


def unmarshal_PermissionSet(data: Any) -> PermissionSet:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'PermissionSet' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("categories")
    args["categories"] = field

    field = data.get("description")
    args["description"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("scope_type")
    args["scope_type"] = field

    return PermissionSet(**args)


def unmarshal_Policy(data: Any) -> Policy:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Policy' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("application_id")
    args["application_id"] = field

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description")
    args["description"] = field

    field = data.get("editable")
    args["editable"] = field

    field = data.get("group_id")
    args["group_id"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("nb_permission_sets")
    args["nb_permission_sets"] = field

    field = data.get("nb_rules")
    args["nb_rules"] = field

    field = data.get("nb_scopes")
    args["nb_scopes"] = field

    field = data.get("no_principal")
    args["no_principal"] = field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("user_id")
    args["user_id"] = field

    return Policy(**args)


def unmarshal_Rule(data: Any) -> Rule:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Rule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("account_root_user_id")
    args["account_root_user_id"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("permission_set_names")
    args["permission_set_names"] = field

    field = data.get("permission_sets_scope_type")
    args["permission_sets_scope_type"] = field

    field = data.get("project_ids")
    args["project_ids"] = field

    return Rule(**args)


def unmarshal_SSHKey(data: Any) -> SSHKey:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SSHKey' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("disabled")
    args["disabled"] = field

    field = data.get("fingerprint")
    args["fingerprint"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("public_key")
    args["public_key"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return SSHKey(**args)


def unmarshal_User(data: Any) -> User:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'User' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("deletable")
    args["deletable"] = field

    field = data.get("email")
    args["email"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("last_login_at")
    args["last_login_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("two_factor_enabled")
    args["two_factor_enabled"] = field

    field = data.get("type_")
    args["type_"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return User(**args)


def unmarshal_ListAPIKeysResponse(data: Any) -> ListAPIKeysResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListAPIKeysResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("api_keys")
    args["api_keys"] = [unmarshal_APIKey(v) for v in data["api_keys"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListAPIKeysResponse(**args)


def unmarshal_ListApplicationsResponse(data: Any) -> ListApplicationsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListApplicationsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("applications")
    args["applications"] = [unmarshal_Application(v) for v in data["applications"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListApplicationsResponse(**args)


def unmarshal_ListGroupsResponse(data: Any) -> ListGroupsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListGroupsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("groups")
    args["groups"] = [unmarshal_Group(v) for v in data["groups"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListGroupsResponse(**args)


def unmarshal_ListPermissionSetsResponse(data: Any) -> ListPermissionSetsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListPermissionSetsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("permission_sets")
    args["permission_sets"] = [
        unmarshal_PermissionSet(v) for v in data["permission_sets"]
    ]

    field = data.get("total_count")
    args["total_count"] = field

    return ListPermissionSetsResponse(**args)


def unmarshal_ListPoliciesResponse(data: Any) -> ListPoliciesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListPoliciesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("policies")
    args["policies"] = [unmarshal_Policy(v) for v in data["policies"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListPoliciesResponse(**args)


def unmarshal_ListRulesResponse(data: Any) -> ListRulesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules")
    args["rules"] = [unmarshal_Rule(v) for v in data["rules"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListRulesResponse(**args)


def unmarshal_ListSSHKeysResponse(data: Any) -> ListSSHKeysResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListSSHKeysResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ssh_keys")
    args["ssh_keys"] = [unmarshal_SSHKey(v) for v in data["ssh_keys"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListSSHKeysResponse(**args)


def unmarshal_ListUsersResponse(data: Any) -> ListUsersResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListUsersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count")
    args["total_count"] = field

    field = data.get("users")
    args["users"] = [unmarshal_User(v) for v in data["users"]]

    return ListUsersResponse(**args)


def unmarshal_SetRulesResponse(data: Any) -> SetRulesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SetRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules")
    args["rules"] = [unmarshal_Rule(v) for v in data["rules"]]

    return SetRulesResponse(**args)


def marshal_RuleSpecs(
    request: RuleSpecs,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("project_ids", request.project_ids),
                OneOfPossibility(
                    "organization_id",
                    request.organization_id,
                    defaults.default_organization_id,
                ),
            ]
        ),
        "permission_set_names": request.permission_set_names,
    }


def marshal_AddGroupMemberRequest(
    request: AddGroupMemberRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("user_id", request.user_id),
                OneOfPossibility("application_id", request.application_id),
            ]
        ),
    }


def marshal_CreateAPIKeyRequest(
    request: CreateAPIKeyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("application_id", request.application_id),
                OneOfPossibility("user_id", request.user_id),
            ]
        ),
        "default_project_id": request.default_project_id,
        "description": request.description,
        "expires_at": request.expires_at,
    }


def marshal_CreateApplicationRequest(
    request: CreateApplicationRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "name": request.name,
        "organization_id": request.organization_id or defaults.default_organization_id,
    }


def marshal_CreateGroupRequest(
    request: CreateGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "name": request.name,
        "organization_id": request.organization_id or defaults.default_organization_id,
    }


def marshal_CreatePolicyRequest(
    request: CreatePolicyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("user_id", request.user_id),
                OneOfPossibility("group_id", request.group_id),
                OneOfPossibility("application_id", request.application_id),
                OneOfPossibility("no_principal", request.no_principal),
            ]
        ),
        "description": request.description,
        "name": request.name,
        "organization_id": request.organization_id or defaults.default_organization_id,
        "rules": [marshal_RuleSpecs(v, defaults) for v in request.rules]
        if request.rules is not None
        else None,
    }


def marshal_CreateSSHKeyRequest(
    request: CreateSSHKeyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "name": request.name,
        "project_id": request.project_id or defaults.default_project_id,
        "public_key": request.public_key,
    }


def marshal_RemoveGroupMemberRequest(
    request: RemoveGroupMemberRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("user_id", request.user_id),
                OneOfPossibility("application_id", request.application_id),
            ]
        ),
    }


def marshal_SetGroupMembersRequest(
    request: SetGroupMembersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "application_ids": request.application_ids,
        "user_ids": request.user_ids,
    }


def marshal_SetRulesRequest(
    request: SetRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "policy_id": request.policy_id,
        "rules": [marshal_RuleSpecs(v, defaults) for v in request.rules],
    }


def marshal_UpdateAPIKeyRequest(
    request: UpdateAPIKeyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "default_project_id": request.default_project_id,
        "description": request.description,
    }


def marshal_UpdateApplicationRequest(
    request: UpdateApplicationRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "name": request.name,
    }


def marshal_UpdateGroupRequest(
    request: UpdateGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "name": request.name,
    }


def marshal_UpdatePolicyRequest(
    request: UpdatePolicyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility("user_id", request.user_id),
                OneOfPossibility("group_id", request.group_id),
                OneOfPossibility("application_id", request.application_id),
                OneOfPossibility("no_principal", request.no_principal),
            ]
        ),
        "description": request.description,
        "name": request.name,
    }


def marshal_UpdateSSHKeyRequest(
    request: UpdateSSHKeyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "disabled": request.disabled,
        "name": request.name,
    }
