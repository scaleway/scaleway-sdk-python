# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional


class ListAPIKeysRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    EXPIRES_AT_ASC = "expires_at_asc"
    EXPIRES_AT_DESC = "expires_at_desc"
    ACCESS_KEY_ASC = "access_key_asc"
    ACCESS_KEY_DESC = "access_key_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListApplicationsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListGroupsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPermissionSetsRequestOrderBy(str, Enum):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPoliciesRequestOrderBy(str, Enum):
    POLICY_NAME_ASC = "policy_name_asc"
    POLICY_NAME_DESC = "policy_name_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListSSHKeysRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListUsersRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    EMAIL_ASC = "email_asc"
    EMAIL_DESC = "email_desc"
    LAST_LOGIN_ASC = "last_login_asc"
    LAST_LOGIN_DESC = "last_login_desc"

    def __str__(self) -> str:
        return str(self.value)


class PermissionSetScopeType(str, Enum):
    UNKNOWN_SCOPE_TYPE = "unknown_scope_type"
    PROJECTS = "projects"
    ORGANIZATION = "organization"
    ACCOUNT_ROOT_USER = "account_root_user"

    def __str__(self) -> str:
        return str(self.value)


class UserStatus(str, Enum):
    UNKNOWN_STATUS = "unknown_status"
    INVITATION_PENDING = "invitation_pending"
    ACTIVATED = "activated"

    def __str__(self) -> str:
        return str(self.value)


class UserType(str, Enum):
    UNKNOWN_TYPE = "unknown_type"
    GUEST = "guest"
    OWNER = "owner"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class APIKey:
    """
    Api key
    """

    access_key: str
    """
    Access key of API key
    """

    secret_key: Optional[str]
    """
    Secret key of API Key
    """

    application_id: Optional[str]
    """
    ID of application bearer.
    
    One-of ('bearer'): at most one of 'application_id', 'user_id' could be set.
    """

    user_id: Optional[str]
    """
    ID of user bearer.
    
    One-of ('bearer'): at most one of 'application_id', 'user_id' could be set.
    """

    description: str
    """
    Description of API key
    """

    created_at: Optional[datetime]
    """
    Creation date and time of API key
    """

    updated_at: Optional[datetime]
    """
    Last update date and time of API key
    """

    expires_at: Optional[datetime]
    """
    Expiration date and time of API key
    """

    default_project_id: str
    """
    The default project ID specified for this API key
    """

    editable: bool
    """
    Whether or not the API key is editable
    """

    creation_ip: str
    """
    IP Address of the device which created the API key
    """


@dataclass
class Application:
    """
    Application
    """

    id: str
    """
    ID of application
    """

    name: str
    """
    Name of application
    """

    description: str
    """
    Description of the application
    """

    created_at: Optional[datetime]
    """
    Creation date of application
    """

    updated_at: Optional[datetime]
    """
    Last update date of application
    """

    organization_id: str
    """
    ID of organization
    """

    editable: bool
    """
    Whether or not the application is editable
    """

    nb_api_keys: int
    """
    Number of API keys owned by the application
    """


@dataclass
class Group:
    """
    Group
    """

    id: str
    """
    ID of group
    """

    created_at: Optional[datetime]
    """
    Creation date and time of group
    """

    updated_at: Optional[datetime]
    """
    Last update date and time of group
    """

    organization_id: str
    """
    ID of organization linked to the group
    """

    name: str
    """
    Name of group
    """

    description: str
    """
    Description of the group
    """

    user_ids: List[str]
    """
    IDs of users attached to this group
    """

    application_ids: List[str]
    """
    IDs of applications attached to this group
    """


@dataclass
class ListAPIKeysResponse:
    """
    List api keys response
    """

    api_keys: List[APIKey]
    """
    List of API keys
    """

    total_count: int
    """
    Total count of API Keys
    """


@dataclass
class ListApplicationsResponse:
    """
    List applications response
    """

    applications: List[Application]
    """
    List of applications
    """

    total_count: int
    """
    Total count of applications
    """


@dataclass
class ListGroupsResponse:
    """
    List groups response
    """

    groups: List[Group]
    """
    List of groups
    """

    total_count: int
    """
    Total count of groups
    """


@dataclass
class ListPermissionSetsResponse:
    """
    List permission sets response
    """

    permission_sets: List[PermissionSet]
    """
    List of permission sets
    """

    total_count: int
    """
    Total count of permission sets
    """


@dataclass
class ListPoliciesResponse:
    """
    List policies response
    """

    policies: List[Policy]
    """
    List of policies
    """

    total_count: int
    """
    Total count of policies
    """


@dataclass
class ListRulesResponse:
    """
    List rules response
    """

    rules: List[Rule]
    """
    Rules of the policy
    """

    total_count: int
    """
    Total count of rules
    """


@dataclass
class ListSSHKeysResponse:
    """
    List ssh keys response
    """

    ssh_keys: List[SSHKey]
    """
    List of SSH keys
    """

    total_count: int
    """
    Total count of SSH keys
    """


@dataclass
class ListUsersResponse:
    """
    List users response
    """

    users: List[User]
    """
    List of users
    """

    total_count: int
    """
    Total count of users
    """


@dataclass
class PermissionSet:
    """
    Permission set
    """

    id: str
    """
    Id of permission set
    """

    name: str
    """
    Name of permission set
    """

    scope_type: PermissionSetScopeType
    """
    Scope of permission set
    """

    description: str
    """
    Description of permission set
    """

    categories: Optional[List[str]]
    """
    Categories of permission set
    """


@dataclass
class Policy:
    """
    Policy
    """

    id: str
    """
    Id of policy
    """

    name: str
    """
    Name of policy
    """

    description: str
    """
    Description of policy
    """

    organization_id: str
    """
    Organization ID of policy
    """

    created_at: Optional[datetime]
    """
    Creation date and time of policy
    """

    updated_at: Optional[datetime]
    """
    Last update date and time of policy
    """

    editable: bool
    """
    Editable status of policy
    """

    nb_rules: int
    """
    Number of rules of policy
    """

    nb_scopes: int
    """
    Number of scopes of policy
    """

    nb_permission_sets: int
    """
    Number of permission sets of policy
    """

    user_id: Optional[str]
    """
    ID of user, owner of the policy.
    
    One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
    """

    group_id: Optional[str]
    """
    ID of group, owner of the policy.
    
    One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
    """

    application_id: Optional[str]
    """
    ID of application, owner of the policy.
    
    One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
    """

    no_principal: Optional[bool]
    """
    True when the policy do not belong to any principal.
    
    One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
    """


@dataclass
class Rule:
    """
    Rule
    """

    id: str
    """
    Id of rule
    """

    permission_set_names: Optional[List[str]]
    """
    Names of permission sets bound to the rule
    """

    permission_sets_scope_type: PermissionSetScopeType
    """
    Permission_set_names have the same scope_type
    """

    project_ids: Optional[List[str]]
    """
    List of project IDs scoped to the rule.
    
    One-of ('scope'): at most one of 'project_ids', 'organization_id', 'account_root_user_id' could be set.
    """

    organization_id: Optional[str]
    """
    ID of organization scoped to the rule.
    
    One-of ('scope'): at most one of 'project_ids', 'organization_id', 'account_root_user_id' could be set.
    """

    account_root_user_id: Optional[str]
    """
    ID of account root user scoped to the rule.
    
    One-of ('scope'): at most one of 'project_ids', 'organization_id', 'account_root_user_id' could be set.
    """


@dataclass
class RuleSpecs:
    """
    Rule specs
    """

    permission_set_names: Optional[List[str]]
    """
    Names of permission sets bound to the rule
    """

    project_ids: Optional[List[str]]
    """
    List of project IDs scoped to the rule.
    
    One-of ('scope'): at most one of 'project_ids', 'organization_id' could be set.
    """

    organization_id: Optional[str]
    """
    ID of organization scoped to the rule.
    
    One-of ('scope'): at most one of 'project_ids', 'organization_id' could be set.
    """


@dataclass
class SSHKey:
    """
    Ssh key
    """

    id: str
    """
    ID of SSH key
    """

    name: str
    """
    Name of SSH key
    """

    public_key: str
    """
    Public key of SSH key
    """

    fingerprint: str
    """
    Fingerprint of SSH key
    """

    created_at: Optional[datetime]
    """
    Creation date of SSH key
    """

    updated_at: Optional[datetime]
    """
    Last update date of SSH key
    """

    organization_id: str
    """
    ID of organization linked to the SSH key
    """

    project_id: str
    """
    ID of project linked to the SSH key
    """

    disabled: bool
    """
    SSH key status
    """


@dataclass
class SetRulesResponse:
    """
    Set rules response
    """

    rules: List[Rule]
    """
    Rules of policy
    """


@dataclass
class User:
    """
    User
    """

    id: str
    """
    ID of user
    """

    email: str
    """
    Email of user
    """

    created_at: Optional[datetime]
    """
    Creation date of user
    """

    updated_at: Optional[datetime]
    """
    Last update date of user
    """

    organization_id: str
    """
    ID of organization
    """

    deletable: bool
    """
    Deletion status of user. Owner user cannot be deleted
    """

    last_login_at: Optional[datetime]
    """
    Last login date
    """

    type_: UserType
    """
    Type of the user
    """

    two_factor_enabled: bool
    """
    2FA enabled
    """

    status: UserStatus
    """
    Status of invitation for the user
    """


@dataclass
class ListSSHKeysRequest:
    order_by: Optional[ListSSHKeysRequestOrderBy]
    """
    Sort order of SSH keys
    """

    page: Optional[int]
    """
    Requested page number. Value must be greater or equals to 1
    """

    page_size: Optional[int]
    """
    Number of items per page. Value must be between 1 and 100
    """

    organization_id: Optional[str]
    """
    Filter by organization ID
    """

    name: Optional[str]
    """
    Name of group to find
    """

    project_id: Optional[str]
    """
    Filter by project ID
    """

    disabled: Optional[bool]
    """
    Filter out disabled SSH keys or not
    """


@dataclass
class CreateSSHKeyRequest:
    name: Optional[str]
    """
    The name of the SSH key. Max length is 1000
    """

    public_key: str
    """
    SSH public key. Currently ssh-rsa, ssh-dss (DSA), ssh-ed25519 and ecdsa keys with NIST curves are supported. Max length is 65000
    """

    project_id: Optional[str]
    """
    Project owning the resource
    """


@dataclass
class GetSSHKeyRequest:
    ssh_key_id: str
    """
    The ID of the SSH key
    """


@dataclass
class UpdateSSHKeyRequest:
    ssh_key_id: str

    name: Optional[str]
    """
    Name of the SSH key. Max length is 1000
    """

    disabled: Optional[bool]
    """
    Enable or disable the SSH key
    """


@dataclass
class DeleteSSHKeyRequest:
    ssh_key_id: str


@dataclass
class ListUsersRequest:
    order_by: Optional[ListUsersRequestOrderBy]
    """
    Criteria for sorting results
    """

    page_size: Optional[int]
    """
    Number of results per page. Value must be between 1 and 100
    """

    page: Optional[int]
    """
    Number of page. Value must be greater or equals to 1
    """

    organization_id: Optional[str]
    """
    ID of organization to filter
    """

    user_ids: Optional[List[str]]
    """
    Filter out by a list of ID
    """


@dataclass
class GetUserRequest:
    user_id: str
    """
    ID of user to find
    """


@dataclass
class DeleteUserRequest:
    user_id: str
    """
    ID of user to delete
    """


@dataclass
class ListApplicationsRequest:
    order_by: Optional[ListApplicationsRequestOrderBy]
    """
    Criteria for sorting results
    """

    page_size: Optional[int]
    """
    Number of results per page. Value must be between 1 and 100
    """

    page: Optional[int]
    """
    Number of page. Value must be greater to 1
    """

    name: Optional[str]
    """
    Name of application to filter
    """

    organization_id: Optional[str]
    """
    ID of organization to filter
    """

    editable: Optional[bool]
    """
    Filter out editable applications or not
    """

    application_ids: Optional[List[str]]
    """
    Filter out by a list of ID
    """


@dataclass
class CreateApplicationRequest:
    name: Optional[str]
    """
    Name of application to create (max length is 64 chars)
    """

    organization_id: Optional[str]
    """
    ID of organization
    """

    description: str
    """
    Description of application (max length is 200 chars)
    """


@dataclass
class GetApplicationRequest:
    application_id: str
    """
    ID of application to find
    """


@dataclass
class UpdateApplicationRequest:
    application_id: str
    """
    ID of application to update
    """

    name: Optional[str]
    """
    New name of application (max length is 64 chars)
    """

    description: Optional[str]
    """
    New description of application (max length is 200 chars)
    """


@dataclass
class DeleteApplicationRequest:
    application_id: str
    """
    ID of application to delete
    """


@dataclass
class ListGroupsRequest:
    order_by: Optional[ListGroupsRequestOrderBy]
    """
    Sort order of groups
    """

    page: Optional[int]
    """
    Requested page number. Value must be greater or equals to 1
    """

    page_size: Optional[int]
    """
    Number of items per page. Value must be between 1 and 100
    """

    organization_id: Optional[str]
    """
    Filter by organization ID
    """

    name: Optional[str]
    """
    Name of group to find
    """

    application_ids: Optional[List[str]]
    """
    Filter out by a list of application ID
    """

    user_ids: Optional[List[str]]
    """
    Filter out by a list of user ID
    """

    group_ids: Optional[List[str]]
    """
    Filter out by a list of group ID
    """


@dataclass
class CreateGroupRequest:
    organization_id: Optional[str]
    """
    ID of organization linked to the group
    """

    name: Optional[str]
    """
    Name of the group to create (max length is 64 chars). MUST be unique inside an organization
    """

    description: str
    """
    Description of the group to create (max length is 200 chars)
    """


@dataclass
class GetGroupRequest:
    group_id: str
    """
    ID of group
    """


@dataclass
class UpdateGroupRequest:
    group_id: str
    """
    ID of group to update
    """

    name: Optional[str]
    """
    New name for the group (max length is 64 chars). MUST be unique inside an organization
    """

    description: Optional[str]
    """
    New description for the group (max length is 200 chars)
    """


@dataclass
class SetGroupMembersRequest:
    group_id: str

    user_ids: List[str]

    application_ids: List[str]


@dataclass
class AddGroupMemberRequest:
    group_id: str
    """
    ID of group
    """

    user_id: Optional[str]
    """
    ID of the user to add.
    
    One-of ('member'): at most one of 'user_id', 'application_id' could be set.
    """

    application_id: Optional[str]
    """
    ID of the application to add.
    
    One-of ('member'): at most one of 'user_id', 'application_id' could be set.
    """


@dataclass
class RemoveGroupMemberRequest:
    group_id: str
    """
    ID of group
    """

    user_id: Optional[str]
    """
    ID of the user to remove.
    
    One-of ('member'): at most one of 'user_id', 'application_id' could be set.
    """

    application_id: Optional[str]
    """
    ID of the application to remove.
    
    One-of ('member'): at most one of 'user_id', 'application_id' could be set.
    """


@dataclass
class DeleteGroupRequest:
    group_id: str
    """
    ID of group to delete
    """


@dataclass
class ListPoliciesRequest:
    order_by: Optional[ListPoliciesRequestOrderBy]
    """
    Criteria for sorting results
    """

    page_size: Optional[int]
    """
    Number of results per page. Value must be between 1 and 100
    """

    page: Optional[int]
    """
    Number of page. Value must be greater to 1
    """

    organization_id: Optional[str]
    """
    ID of organization to filter
    """

    editable: Optional[bool]
    """
    Filter out editable policies or not
    """

    user_ids: Optional[List[str]]
    """
    Filter out by a list of user ID
    """

    group_ids: Optional[List[str]]
    """
    Filter out by a list of group ID
    """

    application_ids: Optional[List[str]]
    """
    Filter out by a list of application ID
    """

    no_principal: Optional[bool]
    """
    True when the policy do not belong to any principal
    """

    policy_name: Optional[str]
    """
    Name of policy to fetch
    """


@dataclass
class CreatePolicyRequest:
    name: Optional[str]
    """
    Name of policy to create (max length is 64 chars)
    """

    description: str
    """
    Description of policy to create (max length is 200 chars)
    """

    organization_id: Optional[str]
    """
    ID of organization
    """

    rules: Optional[List[RuleSpecs]]
    """
    Rules of the policy to create
    """

    user_id: Optional[str]
    """
    ID of user, owner of the policy.
    
    One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
    """

    group_id: Optional[str]
    """
    ID of group, owner of the policy.
    
    One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
    """

    application_id: Optional[str]
    """
    ID of application, owner of the policy.
    
    One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
    """

    no_principal: Optional[bool]
    """
    True when the policy do not belong to any principal.
    
    One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
    """


@dataclass
class GetPolicyRequest:
    policy_id: str
    """
    Id of policy to search
    """


@dataclass
class UpdatePolicyRequest:
    policy_id: str
    """
    Id of policy to update
    """

    name: Optional[str]
    """
    New name of policy (max length is 64 chars)
    """

    description: Optional[str]
    """
    New description of policy (max length is 200 chars)
    """

    user_id: Optional[str]
    """
    New ID of user, owner of the policy.
    
    One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
    """

    group_id: Optional[str]
    """
    New ID of group, owner of the policy.
    
    One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
    """

    application_id: Optional[str]
    """
    New ID of application, owner of the policy.
    
    One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
    """

    no_principal: Optional[bool]
    """
    True when the policy do not belong to any principal.
    
    One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
    """


@dataclass
class DeletePolicyRequest:
    policy_id: str
    """
    Id of policy to delete
    """


@dataclass
class ClonePolicyRequest:
    policy_id: str


@dataclass
class SetRulesRequest:
    policy_id: str
    """
    Id of policy to update
    """

    rules: List[RuleSpecs]
    """
    Rules of the policy to set
    """


@dataclass
class ListRulesRequest:
    policy_id: str
    """
    Id of policy to search
    """

    page_size: Optional[int]
    """
    Number of results per page. Value must be between 1 and 100
    """

    page: Optional[int]
    """
    Number of page. Value must be greater to 1
    """


@dataclass
class ListPermissionSetsRequest:
    order_by: Optional[ListPermissionSetsRequestOrderBy]
    """
    Criteria for sorting results
    """

    page_size: Optional[int]
    """
    Number of results per page. Value must be between 1 and 100
    """

    page: Optional[int]
    """
    Number of page. Value must be greater to 1
    """

    organization_id: Optional[str]
    """
    Filter by organization ID
    """


@dataclass
class ListAPIKeysRequest:
    order_by: Optional[ListAPIKeysRequestOrderBy]
    """
    Criteria for sorting results
    """

    page: Optional[int]
    """
    Number of page. Value must be greater or equals to 1
    """

    page_size: Optional[int]
    """
    Number of results per page. Value must be between 1 and 100
    """

    organization_id: Optional[str]
    """
    ID of organization
    """

    application_id: Optional[str]
    """
    ID of an application bearer.
    
    One-of ('bearer'): at most one of 'application_id', 'user_id' could be set.
    """

    user_id: Optional[str]
    """
    ID of a user bearer.
    
    One-of ('bearer'): at most one of 'application_id', 'user_id' could be set.
    """

    editable: Optional[bool]
    """
    Filter out editable API keys or not
    """


@dataclass
class CreateAPIKeyRequest:
    application_id: Optional[str]
    """
    ID of application principal.
    
    One-of ('bearer'): at most one of 'application_id', 'user_id' could be set.
    """

    user_id: Optional[str]
    """
    ID of user principal.
    
    One-of ('bearer'): at most one of 'application_id', 'user_id' could be set.
    """

    expires_at: Optional[datetime]
    """
    Expiration date of the API key
    """

    default_project_id: Optional[str]
    """
    The default project ID to use with object storage
    """

    description: str
    """
    The description of the API key (max length is 200 chars)
    """


@dataclass
class GetAPIKeyRequest:
    access_key: str
    """
    Access key to search for
    """


@dataclass
class UpdateAPIKeyRequest:
    access_key: str
    """
    Access key to update
    """

    default_project_id: Optional[str]
    """
    The new default project ID to set
    """

    description: Optional[str]
    """
    The new description to update
    """


@dataclass
class DeleteAPIKeyRequest:
    access_key: str
    """
    Access key to delete
    """
