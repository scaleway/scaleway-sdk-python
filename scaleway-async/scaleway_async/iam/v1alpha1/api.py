# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.utils import (
    OneOfPossibility,
    fetch_all_pages_async,
    random_name,
    resolve_one_of,
    validate_path_param,
)
from .types import (
    ListAPIKeysRequestOrderBy,
    ListApplicationsRequestOrderBy,
    ListGroupsRequestOrderBy,
    ListPermissionSetsRequestOrderBy,
    ListPoliciesRequestOrderBy,
    ListSSHKeysRequestOrderBy,
    ListUsersRequestOrderBy,
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
from .marshalling import (
    marshal_AddGroupMemberRequest,
    marshal_CreateAPIKeyRequest,
    marshal_CreateApplicationRequest,
    marshal_CreateGroupRequest,
    marshal_CreatePolicyRequest,
    marshal_CreateSSHKeyRequest,
    marshal_RemoveGroupMemberRequest,
    marshal_SetGroupMembersRequest,
    marshal_SetRulesRequest,
    marshal_UpdateAPIKeyRequest,
    marshal_UpdateApplicationRequest,
    marshal_UpdateGroupRequest,
    marshal_UpdatePolicyRequest,
    marshal_UpdateSSHKeyRequest,
    unmarshal_APIKey,
    unmarshal_Application,
    unmarshal_Group,
    unmarshal_Policy,
    unmarshal_SSHKey,
    unmarshal_User,
    unmarshal_ListAPIKeysResponse,
    unmarshal_ListApplicationsResponse,
    unmarshal_ListGroupsResponse,
    unmarshal_ListPermissionSetsResponse,
    unmarshal_ListPoliciesResponse,
    unmarshal_ListRulesResponse,
    unmarshal_ListSSHKeysResponse,
    unmarshal_ListUsersResponse,
    unmarshal_SetRulesResponse,
)


class IamV1Alpha1API(API):
    """
    IAM API.
    """

    async def list_ssh_keys(
        self,
        *,
        order_by: ListSSHKeysRequestOrderBy = ListSSHKeysRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        disabled: Optional[bool] = None,
    ) -> ListSSHKeysResponse:
        """
        List SSH keys
        :param order_by: Sort order of SSH keys
        :param page: Requested page number. Value must be greater or equals to 1
        :param page_size: Number of items per page. Value must be between 1 and 100
        :param organization_id: Filter by organization ID
        :param name: Name of group to find
        :param project_id: Filter by project ID
        :param disabled: Filter out disabled SSH keys or not
        :return: :class:`ListSSHKeysResponse <ListSSHKeysResponse>`

        Usage:
        ::

            result = await api.list_ssh_keys()
        """

        res = self._request(
            "GET",
            f"/iam/v1alpha1/ssh-keys",
            params={
                "disabled": disabled,
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSSHKeysResponse(res.json())

    async def list_ssh_keys_all(
        self,
        *,
        order_by: Optional[ListSSHKeysRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        disabled: Optional[bool] = None,
    ) -> List[SSHKey]:
        """
        List SSH keys
        :param order_by: Sort order of SSH keys
        :param page: Requested page number. Value must be greater or equals to 1
        :param page_size: Number of items per page. Value must be between 1 and 100
        :param organization_id: Filter by organization ID
        :param name: Name of group to find
        :param project_id: Filter by project ID
        :param disabled: Filter out disabled SSH keys or not
        :return: :class:`List[ListSSHKeysResponse] <List[ListSSHKeysResponse]>`

        Usage:
        ::

            result = await api.list_ssh_keys_all()
        """

        return await fetch_all_pages_async(
            type=ListSSHKeysResponse,
            key="ssh_keys",
            fetcher=self.list_ssh_keys,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "organization_id": organization_id,
                "name": name,
                "project_id": project_id,
                "disabled": disabled,
            },
        )

    async def create_ssh_key(
        self,
        *,
        public_key: str,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> SSHKey:
        """
        Create an SSH key
        :param name: The name of the SSH key. Max length is 1000
        :param public_key: SSH public key. Currently ssh-rsa, ssh-dss (DSA), ssh-ed25519 and ecdsa keys with NIST curves are supported. Max length is 65000
        :param project_id: Project owning the resource
        :return: :class:`SSHKey <SSHKey>`

        Usage:
        ::

            result = await api.create_ssh_key(public_key="example")
        """

        res = self._request(
            "POST",
            f"/iam/v1alpha1/ssh-keys",
            body=marshal_CreateSSHKeyRequest(
                CreateSSHKeyRequest(
                    public_key=public_key,
                    name=name or random_name(prefix="key"),
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SSHKey(res.json())

    async def get_ssh_key(
        self,
        *,
        ssh_key_id: str,
    ) -> SSHKey:
        """
        Get an SSH key
        :param ssh_key_id: The ID of the SSH key
        :return: :class:`SSHKey <SSHKey>`

        Usage:
        ::

            result = await api.get_ssh_key(ssh_key_id="example")
        """

        param_ssh_key_id = validate_path_param("ssh_key_id", ssh_key_id)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/ssh-keys/{param_ssh_key_id}",
        )

        self._throw_on_error(res)
        return unmarshal_SSHKey(res.json())

    async def update_ssh_key(
        self,
        *,
        ssh_key_id: str,
        name: Optional[str] = None,
        disabled: Optional[bool] = None,
    ) -> SSHKey:
        """
        Update an SSH key
        :param ssh_key_id:
        :param name: Name of the SSH key. Max length is 1000
        :param disabled: Enable or disable the SSH key
        :return: :class:`SSHKey <SSHKey>`

        Usage:
        ::

            result = await api.update_ssh_key(ssh_key_id="example")
        """

        param_ssh_key_id = validate_path_param("ssh_key_id", ssh_key_id)

        res = self._request(
            "PATCH",
            f"/iam/v1alpha1/ssh-keys/{param_ssh_key_id}",
            body=marshal_UpdateSSHKeyRequest(
                UpdateSSHKeyRequest(
                    ssh_key_id=ssh_key_id,
                    name=name,
                    disabled=disabled,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SSHKey(res.json())

    async def delete_ssh_key(
        self,
        *,
        ssh_key_id: str,
    ) -> Optional[None]:
        """
        Delete an SSH key
        :param ssh_key_id:

        Usage:
        ::

            result = await api.delete_ssh_key(ssh_key_id="example")
        """

        param_ssh_key_id = validate_path_param("ssh_key_id", ssh_key_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/ssh-keys/{param_ssh_key_id}",
        )

        self._throw_on_error(res)
        return None

    async def list_users(
        self,
        *,
        order_by: ListUsersRequestOrderBy = ListUsersRequestOrderBy.CREATED_AT_ASC,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        user_ids: Optional[List[str]] = None,
    ) -> ListUsersResponse:
        """
        List users of an organization
        :param order_by: Criteria for sorting results
        :param page_size: Number of results per page. Value must be between 1 and 100
        :param page: Number of page. Value must be greater or equals to 1
        :param organization_id: ID of organization to filter
        :param user_ids: Filter out by a list of ID
        :return: :class:`ListUsersResponse <ListUsersResponse>`

        Usage:
        ::

            result = await api.list_users()
        """

        res = self._request(
            "GET",
            f"/iam/v1alpha1/users",
            params={
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "user_ids": user_ids,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListUsersResponse(res.json())

    async def list_users_all(
        self,
        *,
        order_by: Optional[ListUsersRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        user_ids: Optional[List[str]] = None,
    ) -> List[User]:
        """
        List users of an organization
        :param order_by: Criteria for sorting results
        :param page_size: Number of results per page. Value must be between 1 and 100
        :param page: Number of page. Value must be greater or equals to 1
        :param organization_id: ID of organization to filter
        :param user_ids: Filter out by a list of ID
        :return: :class:`List[ListUsersResponse] <List[ListUsersResponse]>`

        Usage:
        ::

            result = await api.list_users_all()
        """

        return await fetch_all_pages_async(
            type=ListUsersResponse,
            key="users",
            fetcher=self.list_users,
            args={
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
                "organization_id": organization_id,
                "user_ids": user_ids,
            },
        )

    async def get_user(
        self,
        *,
        user_id: str,
    ) -> User:
        """
        Retrieve a user from its ID
        :param user_id: ID of user to find
        :return: :class:`User <User>`

        Usage:
        ::

            result = await api.get_user(user_id="example")
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/users/{param_user_id}",
        )

        self._throw_on_error(res)
        return unmarshal_User(res.json())

    async def delete_user(
        self,
        *,
        user_id: str,
    ) -> Optional[None]:
        """
        Delete a guest user from an organization
        :param user_id: ID of user to delete

        Usage:
        ::

            result = await api.delete_user(user_id="example")
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/users/{param_user_id}",
        )

        self._throw_on_error(res)
        return None

    async def list_applications(
        self,
        *,
        order_by: ListApplicationsRequestOrderBy = ListApplicationsRequestOrderBy.CREATED_AT_ASC,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        editable: Optional[bool] = None,
        application_ids: Optional[List[str]] = None,
    ) -> ListApplicationsResponse:
        """
        List applications of an organization
        :param order_by: Criteria for sorting results
        :param page_size: Number of results per page. Value must be between 1 and 100
        :param page: Number of page. Value must be greater to 1
        :param name: Name of application to filter
        :param organization_id: ID of organization to filter
        :param editable: Filter out editable applications or not
        :param application_ids: Filter out by a list of ID
        :return: :class:`ListApplicationsResponse <ListApplicationsResponse>`

        Usage:
        ::

            result = await api.list_applications()
        """

        res = self._request(
            "GET",
            f"/iam/v1alpha1/applications",
            params={
                "application_ids": application_ids,
                "editable": editable,
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListApplicationsResponse(res.json())

    async def list_applications_all(
        self,
        *,
        order_by: Optional[ListApplicationsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        editable: Optional[bool] = None,
        application_ids: Optional[List[str]] = None,
    ) -> List[Application]:
        """
        List applications of an organization
        :param order_by: Criteria for sorting results
        :param page_size: Number of results per page. Value must be between 1 and 100
        :param page: Number of page. Value must be greater to 1
        :param name: Name of application to filter
        :param organization_id: ID of organization to filter
        :param editable: Filter out editable applications or not
        :param application_ids: Filter out by a list of ID
        :return: :class:`List[ListApplicationsResponse] <List[ListApplicationsResponse]>`

        Usage:
        ::

            result = await api.list_applications_all()
        """

        return await fetch_all_pages_async(
            type=ListApplicationsResponse,
            key="applications",
            fetcher=self.list_applications,
            args={
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
                "name": name,
                "organization_id": organization_id,
                "editable": editable,
                "application_ids": application_ids,
            },
        )

    async def create_application(
        self,
        *,
        description: str,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
    ) -> Application:
        """
        Create a new application
        :param name: Name of application to create (max length is 64 chars)
        :param organization_id: ID of organization
        :param description: Description of application (max length is 200 chars)
        :return: :class:`Application <Application>`

        Usage:
        ::

            result = await api.create_application(description="example")
        """

        res = self._request(
            "POST",
            f"/iam/v1alpha1/applications",
            body=marshal_CreateApplicationRequest(
                CreateApplicationRequest(
                    description=description,
                    name=name or random_name(prefix="app"),
                    organization_id=organization_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Application(res.json())

    async def get_application(
        self,
        *,
        application_id: str,
    ) -> Application:
        """
        Get an existing application
        :param application_id: ID of application to find
        :return: :class:`Application <Application>`

        Usage:
        ::

            result = await api.get_application(application_id="example")
        """

        param_application_id = validate_path_param("application_id", application_id)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/applications/{param_application_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Application(res.json())

    async def update_application(
        self,
        *,
        application_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Application:
        """
        Update an existing application
        :param application_id: ID of application to update
        :param name: New name of application (max length is 64 chars)
        :param description: New description of application (max length is 200 chars)
        :return: :class:`Application <Application>`

        Usage:
        ::

            result = await api.update_application(application_id="example")
        """

        param_application_id = validate_path_param("application_id", application_id)

        res = self._request(
            "PATCH",
            f"/iam/v1alpha1/applications/{param_application_id}",
            body=marshal_UpdateApplicationRequest(
                UpdateApplicationRequest(
                    application_id=application_id,
                    name=name,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Application(res.json())

    async def delete_application(
        self,
        *,
        application_id: str,
    ) -> Optional[None]:
        """
        Delete an application
        :param application_id: ID of application to delete

        Usage:
        ::

            result = await api.delete_application(application_id="example")
        """

        param_application_id = validate_path_param("application_id", application_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/applications/{param_application_id}",
        )

        self._throw_on_error(res)
        return None

    async def list_groups(
        self,
        *,
        order_by: ListGroupsRequestOrderBy = ListGroupsRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        application_ids: Optional[List[str]] = None,
        user_ids: Optional[List[str]] = None,
        group_ids: Optional[List[str]] = None,
    ) -> ListGroupsResponse:
        """
        List groups
        :param order_by: Sort order of groups
        :param page: Requested page number. Value must be greater or equals to 1
        :param page_size: Number of items per page. Value must be between 1 and 100
        :param organization_id: Filter by organization ID
        :param name: Name of group to find
        :param application_ids: Filter out by a list of application ID
        :param user_ids: Filter out by a list of user ID
        :param group_ids: Filter out by a list of group ID
        :return: :class:`ListGroupsResponse <ListGroupsResponse>`

        Usage:
        ::

            result = await api.list_groups()
        """

        res = self._request(
            "GET",
            f"/iam/v1alpha1/groups",
            params={
                "application_ids": application_ids,
                "group_ids": group_ids,
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "user_ids": user_ids,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListGroupsResponse(res.json())

    async def list_groups_all(
        self,
        *,
        order_by: Optional[ListGroupsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        application_ids: Optional[List[str]] = None,
        user_ids: Optional[List[str]] = None,
        group_ids: Optional[List[str]] = None,
    ) -> List[Group]:
        """
        List groups
        :param order_by: Sort order of groups
        :param page: Requested page number. Value must be greater or equals to 1
        :param page_size: Number of items per page. Value must be between 1 and 100
        :param organization_id: Filter by organization ID
        :param name: Name of group to find
        :param application_ids: Filter out by a list of application ID
        :param user_ids: Filter out by a list of user ID
        :param group_ids: Filter out by a list of group ID
        :return: :class:`List[ListGroupsResponse] <List[ListGroupsResponse]>`

        Usage:
        ::

            result = await api.list_groups_all()
        """

        return await fetch_all_pages_async(
            type=ListGroupsResponse,
            key="groups",
            fetcher=self.list_groups,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "organization_id": organization_id,
                "name": name,
                "application_ids": application_ids,
                "user_ids": user_ids,
                "group_ids": group_ids,
            },
        )

    async def create_group(
        self,
        *,
        description: str,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> Group:
        """
        Create a new group
        :param organization_id: ID of organization linked to the group
        :param name: Name of the group to create (max length is 64 chars). MUST be unique inside an organization
        :param description: Description of the group to create (max length is 200 chars)
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = await api.create_group(description="example")
        """

        res = self._request(
            "POST",
            f"/iam/v1alpha1/groups",
            body=marshal_CreateGroupRequest(
                CreateGroupRequest(
                    description=description,
                    organization_id=organization_id,
                    name=name or random_name(prefix="grp"),
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Group(res.json())

    async def get_group(
        self,
        *,
        group_id: str,
    ) -> Group:
        """
        Get a group
        :param group_id: ID of group
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = await api.get_group(group_id="example")
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/groups/{param_group_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Group(res.json())

    async def update_group(
        self,
        *,
        group_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Group:
        """
        Update a group
        :param group_id: ID of group to update
        :param name: New name for the group (max length is 64 chars). MUST be unique inside an organization
        :param description: New description for the group (max length is 200 chars)
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = await api.update_group(group_id="example")
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "PATCH",
            f"/iam/v1alpha1/groups/{param_group_id}",
            body=marshal_UpdateGroupRequest(
                UpdateGroupRequest(
                    group_id=group_id,
                    name=name,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Group(res.json())

    async def set_group_members(
        self,
        *,
        group_id: str,
        user_ids: List[str],
        application_ids: List[str],
    ) -> Group:
        """
        Overwrite users and applications of a group
        :param group_id:
        :param user_ids:
        :param application_ids:
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = await api.set_group_members(
                group_id="example",
                user_ids=["example"],
                application_ids=["example"],
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "PUT",
            f"/iam/v1alpha1/groups/{param_group_id}/members",
            body=marshal_SetGroupMembersRequest(
                SetGroupMembersRequest(
                    group_id=group_id,
                    user_ids=user_ids,
                    application_ids=application_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Group(res.json())

    async def add_group_member(
        self,
        *,
        group_id: str,
        user_id: Optional[str] = None,
        application_id: Optional[str] = None,
    ) -> Group:
        """
        Add a user of an application to a group
        :param group_id: ID of group
        :param user_id: ID of the user to add.

        One-of ('member'): at most one of 'user_id', 'application_id' could be set.
        :param application_id: ID of the application to add.

        One-of ('member'): at most one of 'user_id', 'application_id' could be set.
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = await api.add_group_member(group_id="example")
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "POST",
            f"/iam/v1alpha1/groups/{param_group_id}/add-member",
            body=marshal_AddGroupMemberRequest(
                AddGroupMemberRequest(
                    group_id=group_id,
                    user_id=user_id,
                    application_id=application_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Group(res.json())

    async def remove_group_member(
        self,
        *,
        group_id: str,
        user_id: Optional[str] = None,
        application_id: Optional[str] = None,
    ) -> Group:
        """
        Remove a user or an application from a group
        :param group_id: ID of group
        :param user_id: ID of the user to remove.

        One-of ('member'): at most one of 'user_id', 'application_id' could be set.
        :param application_id: ID of the application to remove.

        One-of ('member'): at most one of 'user_id', 'application_id' could be set.
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = await api.remove_group_member(group_id="example")
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "POST",
            f"/iam/v1alpha1/groups/{param_group_id}/remove-member",
            body=marshal_RemoveGroupMemberRequest(
                RemoveGroupMemberRequest(
                    group_id=group_id,
                    user_id=user_id,
                    application_id=application_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Group(res.json())

    async def delete_group(
        self,
        *,
        group_id: str,
    ) -> Optional[None]:
        """
        Delete a group
        :param group_id: ID of group to delete

        Usage:
        ::

            result = await api.delete_group(group_id="example")
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/groups/{param_group_id}",
        )

        self._throw_on_error(res)
        return None

    async def list_policies(
        self,
        *,
        order_by: ListPoliciesRequestOrderBy = ListPoliciesRequestOrderBy.POLICY_NAME_ASC,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        editable: Optional[bool] = None,
        user_ids: Optional[List[str]] = None,
        group_ids: Optional[List[str]] = None,
        application_ids: Optional[List[str]] = None,
        no_principal: Optional[bool] = None,
        policy_name: Optional[str] = None,
    ) -> ListPoliciesResponse:
        """
        List policies of an organization
        :param order_by: Criteria for sorting results
        :param page_size: Number of results per page. Value must be between 1 and 100
        :param page: Number of page. Value must be greater to 1
        :param organization_id: ID of organization to filter
        :param editable: Filter out editable policies or not
        :param user_ids: Filter out by a list of user ID
        :param group_ids: Filter out by a list of group ID
        :param application_ids: Filter out by a list of application ID
        :param no_principal: True when the policy do not belong to any principal
        :param policy_name: Name of policy to fetch
        :return: :class:`ListPoliciesResponse <ListPoliciesResponse>`

        Usage:
        ::

            result = await api.list_policies()
        """

        res = self._request(
            "GET",
            f"/iam/v1alpha1/policies",
            params={
                "application_ids": application_ids,
                "editable": editable,
                "group_ids": group_ids,
                "no_principal": no_principal,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "policy_name": policy_name,
                "user_ids": user_ids,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPoliciesResponse(res.json())

    async def list_policies_all(
        self,
        *,
        order_by: Optional[ListPoliciesRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        editable: Optional[bool] = None,
        user_ids: Optional[List[str]] = None,
        group_ids: Optional[List[str]] = None,
        application_ids: Optional[List[str]] = None,
        no_principal: Optional[bool] = None,
        policy_name: Optional[str] = None,
    ) -> List[Policy]:
        """
        List policies of an organization
        :param order_by: Criteria for sorting results
        :param page_size: Number of results per page. Value must be between 1 and 100
        :param page: Number of page. Value must be greater to 1
        :param organization_id: ID of organization to filter
        :param editable: Filter out editable policies or not
        :param user_ids: Filter out by a list of user ID
        :param group_ids: Filter out by a list of group ID
        :param application_ids: Filter out by a list of application ID
        :param no_principal: True when the policy do not belong to any principal
        :param policy_name: Name of policy to fetch
        :return: :class:`List[ListPoliciesResponse] <List[ListPoliciesResponse]>`

        Usage:
        ::

            result = await api.list_policies_all()
        """

        return await fetch_all_pages_async(
            type=ListPoliciesResponse,
            key="policies",
            fetcher=self.list_policies,
            args={
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
                "organization_id": organization_id,
                "editable": editable,
                "user_ids": user_ids,
                "group_ids": group_ids,
                "application_ids": application_ids,
                "no_principal": no_principal,
                "policy_name": policy_name,
            },
        )

    async def create_policy(
        self,
        *,
        description: str,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        rules: Optional[List[RuleSpecs]] = None,
        user_id: Optional[str] = None,
        group_id: Optional[str] = None,
        application_id: Optional[str] = None,
        no_principal: Optional[bool] = None,
    ) -> Policy:
        """
        Create a new policy
        :param name: Name of policy to create (max length is 64 chars)
        :param description: Description of policy to create (max length is 200 chars)
        :param organization_id: ID of organization
        :param rules: Rules of the policy to create
        :param user_id: ID of user, owner of the policy.

        One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
        :param group_id: ID of group, owner of the policy.

        One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
        :param application_id: ID of application, owner of the policy.

        One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
        :param no_principal: True when the policy do not belong to any principal.

        One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
        :return: :class:`Policy <Policy>`

        Usage:
        ::

            result = await api.create_policy(description="example")
        """

        res = self._request(
            "POST",
            f"/iam/v1alpha1/policies",
            body=marshal_CreatePolicyRequest(
                CreatePolicyRequest(
                    description=description,
                    name=name or random_name(prefix="pol"),
                    organization_id=organization_id,
                    rules=rules,
                    user_id=user_id,
                    group_id=group_id,
                    application_id=application_id,
                    no_principal=no_principal,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Policy(res.json())

    async def get_policy(
        self,
        *,
        policy_id: str,
    ) -> Policy:
        """
        Get an existing policy
        :param policy_id: Id of policy to search
        :return: :class:`Policy <Policy>`

        Usage:
        ::

            result = await api.get_policy(policy_id="example")
        """

        param_policy_id = validate_path_param("policy_id", policy_id)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/policies/{param_policy_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Policy(res.json())

    async def update_policy(
        self,
        *,
        policy_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        user_id: Optional[str] = None,
        group_id: Optional[str] = None,
        application_id: Optional[str] = None,
        no_principal: Optional[bool] = None,
    ) -> Policy:
        """
        Update an existing policy
        :param policy_id: Id of policy to update
        :param name: New name of policy (max length is 64 chars)
        :param description: New description of policy (max length is 200 chars)
        :param user_id: New ID of user, owner of the policy.

        One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
        :param group_id: New ID of group, owner of the policy.

        One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
        :param application_id: New ID of application, owner of the policy.

        One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
        :param no_principal: True when the policy do not belong to any principal.

        One-of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
        :return: :class:`Policy <Policy>`

        Usage:
        ::

            result = await api.update_policy(policy_id="example")
        """

        param_policy_id = validate_path_param("policy_id", policy_id)

        res = self._request(
            "PATCH",
            f"/iam/v1alpha1/policies/{param_policy_id}",
            body=marshal_UpdatePolicyRequest(
                UpdatePolicyRequest(
                    policy_id=policy_id,
                    name=name,
                    description=description,
                    user_id=user_id,
                    group_id=group_id,
                    application_id=application_id,
                    no_principal=no_principal,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Policy(res.json())

    async def delete_policy(
        self,
        *,
        policy_id: str,
    ) -> Optional[None]:
        """
        Delete a policy
        :param policy_id: Id of policy to delete

        Usage:
        ::

            result = await api.delete_policy(policy_id="example")
        """

        param_policy_id = validate_path_param("policy_id", policy_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/policies/{param_policy_id}",
        )

        self._throw_on_error(res)
        return None

    async def clone_policy(
        self,
        *,
        policy_id: str,
    ) -> Policy:
        """

        Usage:
        ::

            result = await api.clone_policy(policy_id="example")
        """

        param_policy_id = validate_path_param("policy_id", policy_id)

        res = self._request(
            "POST",
            f"/iam/v1alpha1/policies/{param_policy_id}/clone",
        )

        self._throw_on_error(res)
        return unmarshal_Policy(res.json())

    async def set_rules(
        self,
        *,
        policy_id: str,
        rules: List[RuleSpecs],
    ) -> SetRulesResponse:
        """
        Set rules of an existing policy
        :param policy_id: Id of policy to update
        :param rules: Rules of the policy to set
        :return: :class:`SetRulesResponse <SetRulesResponse>`

        Usage:
        ::

            result = await api.set_rules(
                policy_id="example",
                rules=[RuleSpecs(...)],
            )
        """

        res = self._request(
            "PUT",
            f"/iam/v1alpha1/rules",
            body=marshal_SetRulesRequest(
                SetRulesRequest(
                    policy_id=policy_id,
                    rules=rules,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetRulesResponse(res.json())

    async def list_rules(
        self,
        *,
        policy_id: str,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListRulesResponse:
        """
        List rules of an existing policy
        :param policy_id: Id of policy to search
        :param page_size: Number of results per page. Value must be between 1 and 100
        :param page: Number of page. Value must be greater to 1
        :return: :class:`ListRulesResponse <ListRulesResponse>`

        Usage:
        ::

            result = await api.list_rules(policy_id="example")
        """

        res = self._request(
            "GET",
            f"/iam/v1alpha1/rules",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "policy_id": policy_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRulesResponse(res.json())

    async def list_rules_all(
        self,
        *,
        policy_id: str,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[Rule]:
        """
        List rules of an existing policy
        :param policy_id: Id of policy to search
        :param page_size: Number of results per page. Value must be between 1 and 100
        :param page: Number of page. Value must be greater to 1
        :return: :class:`List[ListRulesResponse] <List[ListRulesResponse]>`

        Usage:
        ::

            result = await api.list_rules_all(policy_id="example")
        """

        return await fetch_all_pages_async(
            type=ListRulesResponse,
            key="rules",
            fetcher=self.list_rules,
            args={
                "policy_id": policy_id,
                "page_size": page_size,
                "page": page,
            },
        )

    async def list_permission_sets(
        self,
        *,
        order_by: ListPermissionSetsRequestOrderBy = ListPermissionSetsRequestOrderBy.NAME_ASC,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
    ) -> ListPermissionSetsResponse:
        """
        List permission sets
        :param order_by: Criteria for sorting results
        :param page_size: Number of results per page. Value must be between 1 and 100
        :param page: Number of page. Value must be greater to 1
        :param organization_id: Filter by organization ID
        :return: :class:`ListPermissionSetsResponse <ListPermissionSetsResponse>`

        Usage:
        ::

            result = await api.list_permission_sets()
        """

        res = self._request(
            "GET",
            f"/iam/v1alpha1/permission-sets",
            params={
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPermissionSetsResponse(res.json())

    async def list_permission_sets_all(
        self,
        *,
        order_by: Optional[ListPermissionSetsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
    ) -> List[PermissionSet]:
        """
        List permission sets
        :param order_by: Criteria for sorting results
        :param page_size: Number of results per page. Value must be between 1 and 100
        :param page: Number of page. Value must be greater to 1
        :param organization_id: Filter by organization ID
        :return: :class:`List[ListPermissionSetsResponse] <List[ListPermissionSetsResponse]>`

        Usage:
        ::

            result = await api.list_permission_sets_all()
        """

        return await fetch_all_pages_async(
            type=ListPermissionSetsResponse,
            key="permission_sets",
            fetcher=self.list_permission_sets,
            args={
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
                "organization_id": organization_id,
            },
        )

    async def list_api_keys(
        self,
        *,
        order_by: ListAPIKeysRequestOrderBy = ListAPIKeysRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        application_id: Optional[str] = None,
        user_id: Optional[str] = None,
        editable: Optional[bool] = None,
    ) -> ListAPIKeysResponse:
        """
        List API keys
        :param order_by: Criteria for sorting results
        :param page: Number of page. Value must be greater or equals to 1
        :param page_size: Number of results per page. Value must be between 1 and 100
        :param organization_id: ID of organization
        :param application_id: ID of an application bearer.

        One-of ('bearer'): at most one of 'application_id', 'user_id' could be set.
        :param user_id: ID of a user bearer.

        One-of ('bearer'): at most one of 'application_id', 'user_id' could be set.
        :param editable: Filter out editable API keys or not
        :return: :class:`ListAPIKeysResponse <ListAPIKeysResponse>`

        Usage:
        ::

            result = await api.list_api_keys()
        """

        res = self._request(
            "GET",
            f"/iam/v1alpha1/api-keys",
            params={
                "editable": editable,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                **resolve_one_of(
                    [
                        OneOfPossibility("application_id", application_id),
                        OneOfPossibility("user_id", user_id),
                    ]
                ),
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListAPIKeysResponse(res.json())

    async def list_api_keys_all(
        self,
        *,
        order_by: Optional[ListAPIKeysRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        application_id: Optional[str] = None,
        user_id: Optional[str] = None,
        editable: Optional[bool] = None,
    ) -> List[APIKey]:
        """
        List API keys
        :param order_by: Criteria for sorting results
        :param page: Number of page. Value must be greater or equals to 1
        :param page_size: Number of results per page. Value must be between 1 and 100
        :param organization_id: ID of organization
        :param application_id: ID of an application bearer.

        One-of ('bearer'): at most one of 'application_id', 'user_id' could be set.
        :param user_id: ID of a user bearer.

        One-of ('bearer'): at most one of 'application_id', 'user_id' could be set.
        :param editable: Filter out editable API keys or not
        :return: :class:`List[ListAPIKeysResponse] <List[ListAPIKeysResponse]>`

        Usage:
        ::

            result = await api.list_api_keys_all()
        """

        return await fetch_all_pages_async(
            type=ListAPIKeysResponse,
            key="api_keys",
            fetcher=self.list_api_keys,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "organization_id": organization_id,
                "application_id": application_id,
                "user_id": user_id,
                "editable": editable,
            },
        )

    async def create_api_key(
        self,
        *,
        description: str,
        application_id: Optional[str] = None,
        user_id: Optional[str] = None,
        expires_at: Optional[datetime] = None,
        default_project_id: Optional[str] = None,
    ) -> APIKey:
        """
        Create an API key
        :param application_id: ID of application principal.

        One-of ('bearer'): at most one of 'application_id', 'user_id' could be set.
        :param user_id: ID of user principal.

        One-of ('bearer'): at most one of 'application_id', 'user_id' could be set.
        :param expires_at: Expiration date of the API key
        :param default_project_id: The default project ID to use with object storage
        :param description: The description of the API key (max length is 200 chars)
        :return: :class:`APIKey <APIKey>`

        Usage:
        ::

            result = await api.create_api_key(description="example")
        """

        res = self._request(
            "POST",
            f"/iam/v1alpha1/api-keys",
            body=marshal_CreateAPIKeyRequest(
                CreateAPIKeyRequest(
                    description=description,
                    application_id=application_id,
                    user_id=user_id,
                    expires_at=expires_at,
                    default_project_id=default_project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_APIKey(res.json())

    async def get_api_key(
        self,
        *,
        access_key: str,
    ) -> APIKey:
        """
        Get an API key
        :param access_key: Access key to search for
        :return: :class:`APIKey <APIKey>`

        Usage:
        ::

            result = await api.get_api_key(access_key="example")
        """

        param_access_key = validate_path_param("access_key", access_key)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/api-keys/{param_access_key}",
        )

        self._throw_on_error(res)
        return unmarshal_APIKey(res.json())

    async def update_api_key(
        self,
        *,
        access_key: str,
        default_project_id: Optional[str] = None,
        description: Optional[str] = None,
    ) -> APIKey:
        """
        Update an API key
        :param access_key: Access key to update
        :param default_project_id: The new default project ID to set
        :param description: The new description to update
        :return: :class:`APIKey <APIKey>`

        Usage:
        ::

            result = await api.update_api_key(access_key="example")
        """

        param_access_key = validate_path_param("access_key", access_key)

        res = self._request(
            "PATCH",
            f"/iam/v1alpha1/api-keys/{param_access_key}",
            body=marshal_UpdateAPIKeyRequest(
                UpdateAPIKeyRequest(
                    access_key=access_key,
                    default_project_id=default_project_id,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_APIKey(res.json())

    async def delete_api_key(
        self,
        *,
        access_key: str,
    ) -> Optional[None]:
        """
        Delete an API key
        :param access_key: Access key to delete

        Usage:
        ::

            result = await api.delete_api_key(access_key="example")
        """

        param_access_key = validate_path_param("access_key", access_key)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/api-keys/{param_access_key}",
        )

        self._throw_on_error(res)
        return None
