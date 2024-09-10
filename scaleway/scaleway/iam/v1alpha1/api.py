# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.utils import (
    OneOfPossibility,
    random_name,
    resolve_one_of,
    validate_path_param,
    fetch_all_pages,
)
from .types import (
    BearerType,
    ListAPIKeysRequestOrderBy,
    ListApplicationsRequestOrderBy,
    ListGroupsRequestOrderBy,
    ListJWTsRequestOrderBy,
    ListLogsRequestOrderBy,
    ListPermissionSetsRequestOrderBy,
    ListPoliciesRequestOrderBy,
    ListQuotaRequestOrderBy,
    ListSSHKeysRequestOrderBy,
    ListUsersRequestOrderBy,
    LogAction,
    LogResourceType,
    APIKey,
    AddGroupMemberRequest,
    AddGroupMembersRequest,
    Application,
    CreateAPIKeyRequest,
    CreateApplicationRequest,
    CreateGroupRequest,
    CreateJWTRequest,
    CreatePolicyRequest,
    CreateSSHKeyRequest,
    CreateUserRequest,
    CreateUserRequestMember,
    EncodedJWT,
    Group,
    JWT,
    ListAPIKeysResponse,
    ListApplicationsResponse,
    ListGroupsResponse,
    ListJWTsResponse,
    ListLogsResponse,
    ListPermissionSetsResponse,
    ListPoliciesResponse,
    ListQuotaResponse,
    ListRulesResponse,
    ListSSHKeysResponse,
    ListUsersResponse,
    Log,
    PermissionSet,
    Policy,
    Quotum,
    RemoveGroupMemberRequest,
    Rule,
    RuleSpecs,
    SSHKey,
    SetGroupMembersRequest,
    SetRulesRequest,
    SetRulesResponse,
    UpdateAPIKeyRequest,
    UpdateApplicationRequest,
    UpdateGroupRequest,
    UpdatePolicyRequest,
    UpdateSSHKeyRequest,
    UpdateUserRequest,
    User,
)
from .marshalling import (
    unmarshal_JWT,
    unmarshal_APIKey,
    unmarshal_Application,
    unmarshal_Group,
    unmarshal_Log,
    unmarshal_Policy,
    unmarshal_Quotum,
    unmarshal_SSHKey,
    unmarshal_User,
    unmarshal_EncodedJWT,
    unmarshal_ListAPIKeysResponse,
    unmarshal_ListApplicationsResponse,
    unmarshal_ListGroupsResponse,
    unmarshal_ListJWTsResponse,
    unmarshal_ListLogsResponse,
    unmarshal_ListPermissionSetsResponse,
    unmarshal_ListPoliciesResponse,
    unmarshal_ListQuotaResponse,
    unmarshal_ListRulesResponse,
    unmarshal_ListSSHKeysResponse,
    unmarshal_ListUsersResponse,
    unmarshal_SetRulesResponse,
    marshal_AddGroupMemberRequest,
    marshal_AddGroupMembersRequest,
    marshal_CreateAPIKeyRequest,
    marshal_CreateApplicationRequest,
    marshal_CreateGroupRequest,
    marshal_CreateJWTRequest,
    marshal_CreatePolicyRequest,
    marshal_CreateSSHKeyRequest,
    marshal_CreateUserRequest,
    marshal_RemoveGroupMemberRequest,
    marshal_SetGroupMembersRequest,
    marshal_SetRulesRequest,
    marshal_UpdateAPIKeyRequest,
    marshal_UpdateApplicationRequest,
    marshal_UpdateGroupRequest,
    marshal_UpdatePolicyRequest,
    marshal_UpdateSSHKeyRequest,
    marshal_UpdateUserRequest,
)


class IamV1Alpha1API(API):
    """
    This API allows you to manage Identity and Access Management (IAM) across your Scaleway Organizations, Projects and resources.
    """

    def list_ssh_keys(
        self,
        *,
        order_by: Optional[ListSSHKeysRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        disabled: Optional[bool] = None,
    ) -> ListSSHKeysResponse:
        """
        List SSH keys.
        List SSH keys. By default, the SSH keys listed are ordered by creation date in ascending order. This can be modified via the `order_by` field. You can define additional parameters for your query such as `organization_id`, `name`, `project_id` and `disabled`.
        :param order_by: Sort order of the SSH keys.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Number of items per page. Value must be between 1 and 100.
        :param organization_id: Filter by Organization ID.
        :param name: Name of group to find.
        :param project_id: Filter by Project ID.
        :param disabled: Defines whether to include disabled SSH keys or not.
        :return: :class:`ListSSHKeysResponse <ListSSHKeysResponse>`

        Usage:
        ::

            result = api.list_ssh_keys()
        """

        res = self._request(
            "GET",
            "/iam/v1alpha1/ssh-keys",
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

    def list_ssh_keys_all(
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
        List SSH keys.
        List SSH keys. By default, the SSH keys listed are ordered by creation date in ascending order. This can be modified via the `order_by` field. You can define additional parameters for your query such as `organization_id`, `name`, `project_id` and `disabled`.
        :param order_by: Sort order of the SSH keys.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Number of items per page. Value must be between 1 and 100.
        :param organization_id: Filter by Organization ID.
        :param name: Name of group to find.
        :param project_id: Filter by Project ID.
        :param disabled: Defines whether to include disabled SSH keys or not.
        :return: :class:`List[SSHKey] <List[SSHKey]>`

        Usage:
        ::

            result = api.list_ssh_keys_all()
        """

        return fetch_all_pages(
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

    def create_ssh_key(
        self,
        *,
        public_key: str,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> SSHKey:
        """
        Create an SSH key.
        Add a new SSH key to a Scaleway Project. You must specify the `name`, `public_key` and `project_id`.
        :param public_key: SSH public key. Currently only the ssh-rsa, ssh-dss (DSA), ssh-ed25519 and ecdsa keys with NIST curves are supported. Max length is 65000.
        :param name: Name of the SSH key. Max length is 1000.
        :param project_id: Project the resource is attributed to.
        :return: :class:`SSHKey <SSHKey>`

        Usage:
        ::

            result = api.create_ssh_key(
                public_key="example",
            )
        """

        res = self._request(
            "POST",
            "/iam/v1alpha1/ssh-keys",
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

    def get_ssh_key(
        self,
        *,
        ssh_key_id: str,
    ) -> SSHKey:
        """
        Get an SSH key.
        Retrieve information about a given SSH key, specified by the `ssh_key_id` parameter. The SSH key's full details, including `id`, `name`, `public_key`, and `project_id` are returned in the response.
        :param ssh_key_id: ID of the SSH key.
        :return: :class:`SSHKey <SSHKey>`

        Usage:
        ::

            result = api.get_ssh_key(
                ssh_key_id="example",
            )
        """

        param_ssh_key_id = validate_path_param("ssh_key_id", ssh_key_id)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/ssh-keys/{param_ssh_key_id}",
        )

        self._throw_on_error(res)
        return unmarshal_SSHKey(res.json())

    def update_ssh_key(
        self,
        *,
        ssh_key_id: str,
        name: Optional[str] = None,
        disabled: Optional[bool] = None,
    ) -> SSHKey:
        """
        Update an SSH key.
        Update the parameters of an SSH key, including `name` and `disable`.
        :param ssh_key_id:
        :param name: Name of the SSH key. Max length is 1000.
        :param disabled: Enable or disable the SSH key.
        :return: :class:`SSHKey <SSHKey>`

        Usage:
        ::

            result = api.update_ssh_key(
                ssh_key_id="example",
            )
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

    def delete_ssh_key(
        self,
        *,
        ssh_key_id: str,
    ) -> None:
        """
        Delete an SSH key.
        Delete a given SSH key, specified by the `ssh_key_id`. Deleting an SSH is permanent, and cannot be undone. Note that you might need to update any configurations that used the SSH key.
        :param ssh_key_id:

        Usage:
        ::

            result = api.delete_ssh_key(
                ssh_key_id="example",
            )
        """

        param_ssh_key_id = validate_path_param("ssh_key_id", ssh_key_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/ssh-keys/{param_ssh_key_id}",
        )

        self._throw_on_error(res)

    def list_users(
        self,
        *,
        order_by: Optional[ListUsersRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        user_ids: Optional[List[str]] = None,
        mfa: Optional[bool] = None,
        tag: Optional[str] = None,
    ) -> ListUsersResponse:
        """
        List users of an Organization.
        List the users of an Organization. By default, the users listed are ordered by creation date in ascending order. This can be modified via the `order_by` field. You must define the `organization_id` in the query path of your request. You can also define additional parameters for your query such as `user_ids`.
        :param order_by: Criteria for sorting results.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater or equal to 1.
        :param organization_id: ID of the Organization to filter.
        :param user_ids: Filter by list of IDs.
        :param mfa: Filter by MFA status.
        :param tag: Filter by tags containing a given string.
        :return: :class:`ListUsersResponse <ListUsersResponse>`

        Usage:
        ::

            result = api.list_users()
        """

        res = self._request(
            "GET",
            "/iam/v1alpha1/users",
            params={
                "mfa": mfa,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "tag": tag,
                "user_ids": user_ids,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListUsersResponse(res.json())

    def list_users_all(
        self,
        *,
        order_by: Optional[ListUsersRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        user_ids: Optional[List[str]] = None,
        mfa: Optional[bool] = None,
        tag: Optional[str] = None,
    ) -> List[User]:
        """
        List users of an Organization.
        List the users of an Organization. By default, the users listed are ordered by creation date in ascending order. This can be modified via the `order_by` field. You must define the `organization_id` in the query path of your request. You can also define additional parameters for your query such as `user_ids`.
        :param order_by: Criteria for sorting results.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater or equal to 1.
        :param organization_id: ID of the Organization to filter.
        :param user_ids: Filter by list of IDs.
        :param mfa: Filter by MFA status.
        :param tag: Filter by tags containing a given string.
        :return: :class:`List[User] <List[User]>`

        Usage:
        ::

            result = api.list_users_all()
        """

        return fetch_all_pages(
            type=ListUsersResponse,
            key="users",
            fetcher=self.list_users,
            args={
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
                "organization_id": organization_id,
                "user_ids": user_ids,
                "mfa": mfa,
                "tag": tag,
            },
        )

    def get_user(
        self,
        *,
        user_id: str,
    ) -> User:
        """
        Get a given user.
        Retrieve information about a user, specified by the `user_id` parameter. The user's full details, including `id`, `email`, `organization_id`, `status` and `mfa` are returned in the response.
        :param user_id: ID of the user to find.
        :return: :class:`User <User>`

        Usage:
        ::

            result = api.get_user(
                user_id="example",
            )
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/users/{param_user_id}",
        )

        self._throw_on_error(res)
        return unmarshal_User(res.json())

    def update_user(
        self,
        *,
        user_id: str,
        tags: Optional[List[str]] = None,
    ) -> User:
        """
        Update a user.
        Update the parameters of a user, including `tags`.
        :param user_id: ID of the user to update.
        :param tags: New tags for the user (maximum of 10 tags).
        :return: :class:`User <User>`

        Usage:
        ::

            result = api.update_user(
                user_id="example",
            )
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "PATCH",
            f"/iam/v1alpha1/users/{param_user_id}",
            body=marshal_UpdateUserRequest(
                UpdateUserRequest(
                    user_id=user_id,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_User(res.json())

    def delete_user(
        self,
        *,
        user_id: str,
    ) -> None:
        """
        Delete a guest user from an Organization.
        Remove a user from an Organization in which they are a guest. You must define the `user_id` in your request. Note that removing a user from an Organization automatically deletes their API keys, and any policies directly attached to them become orphaned.
        :param user_id: ID of the user to delete.

        Usage:
        ::

            result = api.delete_user(
                user_id="example",
            )
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/users/{param_user_id}",
        )

        self._throw_on_error(res)

    def create_user(
        self,
        *,
        organization_id: Optional[str] = None,
        email: Optional[str] = None,
        tags: Optional[List[str]] = None,
        member: Optional[CreateUserRequestMember] = None,
    ) -> User:
        """
        Create a new user.
        Create a new user. You must define the `organization_id` and the `email` in your request.
        :param organization_id: ID of the Organization.
        :param email: Email of the user.
        One-Of ('type'): at most one of 'email', 'member' could be set.
        :param tags: Tags associated with the user.
        :param member: A new IAM Member to create.
        One-Of ('type'): at most one of 'email', 'member' could be set.
        :return: :class:`User <User>`

        Usage:
        ::

            result = api.create_user()
        """

        res = self._request(
            "POST",
            "/iam/v1alpha1/users",
            body=marshal_CreateUserRequest(
                CreateUserRequest(
                    organization_id=organization_id,
                    tags=tags,
                    email=email,
                    member=member,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_User(res.json())

    def list_applications(
        self,
        *,
        order_by: Optional[ListApplicationsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        editable: Optional[bool] = None,
        application_ids: Optional[List[str]] = None,
        tag: Optional[str] = None,
    ) -> ListApplicationsResponse:
        """
        List applications of an Organization.
        List the applications of an Organization. By default, the applications listed are ordered by creation date in ascending order. This can be modified via the `order_by` field. You must define the `organization_id` in the query path of your request. You can also define additional parameters for your query such as `application_ids`.
        :param order_by: Criteria for sorting results.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater than 1.
        :param name: Name of the application to filter.
        :param organization_id: ID of the Organization to filter.
        :param editable: Defines whether to filter out editable applications or not.
        :param application_ids: Filter by list of IDs.
        :param tag: Filter by tags containing a given string.
        :return: :class:`ListApplicationsResponse <ListApplicationsResponse>`

        Usage:
        ::

            result = api.list_applications()
        """

        res = self._request(
            "GET",
            "/iam/v1alpha1/applications",
            params={
                "application_ids": application_ids,
                "editable": editable,
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "tag": tag,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListApplicationsResponse(res.json())

    def list_applications_all(
        self,
        *,
        order_by: Optional[ListApplicationsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        editable: Optional[bool] = None,
        application_ids: Optional[List[str]] = None,
        tag: Optional[str] = None,
    ) -> List[Application]:
        """
        List applications of an Organization.
        List the applications of an Organization. By default, the applications listed are ordered by creation date in ascending order. This can be modified via the `order_by` field. You must define the `organization_id` in the query path of your request. You can also define additional parameters for your query such as `application_ids`.
        :param order_by: Criteria for sorting results.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater than 1.
        :param name: Name of the application to filter.
        :param organization_id: ID of the Organization to filter.
        :param editable: Defines whether to filter out editable applications or not.
        :param application_ids: Filter by list of IDs.
        :param tag: Filter by tags containing a given string.
        :return: :class:`List[Application] <List[Application]>`

        Usage:
        ::

            result = api.list_applications_all()
        """

        return fetch_all_pages(
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
                "tag": tag,
            },
        )

    def create_application(
        self,
        *,
        description: str,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Application:
        """
        Create a new application.
        Create a new application. You must define the `name` parameter in the request.
        :param description: Description of the application (max length is 200 characters).
        :param name: Name of the application to create (max length is 64 characters).
        :param organization_id: ID of the Organization.
        :param tags: Tags associated with the application (maximum of 10 tags).
        :return: :class:`Application <Application>`

        Usage:
        ::

            result = api.create_application(
                description="example",
            )
        """

        res = self._request(
            "POST",
            "/iam/v1alpha1/applications",
            body=marshal_CreateApplicationRequest(
                CreateApplicationRequest(
                    description=description,
                    name=name or random_name(prefix="app"),
                    organization_id=organization_id,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Application(res.json())

    def get_application(
        self,
        *,
        application_id: str,
    ) -> Application:
        """
        Get a given application.
        Retrieve information about an application, specified by the `application_id` parameter. The application's full details, including `id`, `email`, `organization_id`, `status` and `two_factor_enabled` are returned in the response.
        :param application_id: ID of the application to find.
        :return: :class:`Application <Application>`

        Usage:
        ::

            result = api.get_application(
                application_id="example",
            )
        """

        param_application_id = validate_path_param("application_id", application_id)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/applications/{param_application_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Application(res.json())

    def update_application(
        self,
        *,
        application_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Application:
        """
        Update an application.
        Update the parameters of an application, including `name` and `description`.
        :param application_id: ID of the application to update.
        :param name: New name for the application (max length is 64 chars).
        :param description: New description for the application (max length is 200 chars).
        :param tags: New tags for the application (maximum of 10 tags).
        :return: :class:`Application <Application>`

        Usage:
        ::

            result = api.update_application(
                application_id="example",
            )
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
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Application(res.json())

    def delete_application(
        self,
        *,
        application_id: str,
    ) -> None:
        """
        Delete an application.
        Delete an application. Note that this action is irreversible and will automatically delete the application's API keys. Policies attached to users and applications via this group will no longer apply.
        :param application_id: ID of the application to delete.

        Usage:
        ::

            result = api.delete_application(
                application_id="example",
            )
        """

        param_application_id = validate_path_param("application_id", application_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/applications/{param_application_id}",
        )

        self._throw_on_error(res)

    def list_groups(
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
        tag: Optional[str] = None,
    ) -> ListGroupsResponse:
        """
        List groups.
        List groups. By default, the groups listed are ordered by creation date in ascending order. This can be modified via the `order_by` field. You can define additional parameters to filter your query. Use `user_ids` or `application_ids` to list all groups certain users or applications belong to.
        :param order_by: Sort order of groups.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Number of items per page. Value must be between 1 and 100.
        :param organization_id: Filter by Organization ID.
        :param name: Name of group to find.
        :param application_ids: Filter by a list of application IDs.
        :param user_ids: Filter by a list of user IDs.
        :param group_ids: Filter by a list of group IDs.
        :param tag: Filter by tags containing a given string.
        :return: :class:`ListGroupsResponse <ListGroupsResponse>`

        Usage:
        ::

            result = api.list_groups()
        """

        res = self._request(
            "GET",
            "/iam/v1alpha1/groups",
            params={
                "application_ids": application_ids,
                "group_ids": group_ids,
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "tag": tag,
                "user_ids": user_ids,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListGroupsResponse(res.json())

    def list_groups_all(
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
        tag: Optional[str] = None,
    ) -> List[Group]:
        """
        List groups.
        List groups. By default, the groups listed are ordered by creation date in ascending order. This can be modified via the `order_by` field. You can define additional parameters to filter your query. Use `user_ids` or `application_ids` to list all groups certain users or applications belong to.
        :param order_by: Sort order of groups.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Number of items per page. Value must be between 1 and 100.
        :param organization_id: Filter by Organization ID.
        :param name: Name of group to find.
        :param application_ids: Filter by a list of application IDs.
        :param user_ids: Filter by a list of user IDs.
        :param group_ids: Filter by a list of group IDs.
        :param tag: Filter by tags containing a given string.
        :return: :class:`List[Group] <List[Group]>`

        Usage:
        ::

            result = api.list_groups_all()
        """

        return fetch_all_pages(
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
                "tag": tag,
            },
        )

    def create_group(
        self,
        *,
        description: str,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Group:
        """
        Create a group.
        Create a new group. You must define the `name` and `organization_id` parameters in the request.
        :param description: Description of the group to create (max length is 200 chars).
        :param organization_id: ID of Organization linked to the group.
        :param name: Name of the group to create (max length is 64 chars). MUST be unique inside an Organization.
        :param tags: Tags associated with the group (maximum of 10 tags).
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = api.create_group(
                description="example",
            )
        """

        res = self._request(
            "POST",
            "/iam/v1alpha1/groups",
            body=marshal_CreateGroupRequest(
                CreateGroupRequest(
                    description=description,
                    organization_id=organization_id,
                    name=name or random_name(prefix="grp"),
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Group(res.json())

    def get_group(
        self,
        *,
        group_id: str,
    ) -> Group:
        """
        Get a group.
        Retrive information about a given group, specified by the `group_id` parameter. The group's full details, including `user_ids` and `application_ids` are returned in the response.
        :param group_id: ID of the group.
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = api.get_group(
                group_id="example",
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/groups/{param_group_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Group(res.json())

    def update_group(
        self,
        *,
        group_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Group:
        """
        Update a group.
        Update the parameters of group, including `name` and `description`.
        :param group_id: ID of the group to update.
        :param name: New name for the group (max length is 64 chars). MUST be unique inside an Organization.
        :param description: New description for the group (max length is 200 chars).
        :param tags: New tags for the group (maximum of 10 tags).
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = api.update_group(
                group_id="example",
            )
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
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Group(res.json())

    def set_group_members(
        self,
        *,
        group_id: str,
        user_ids: List[str],
        application_ids: List[str],
    ) -> Group:
        """
        Overwrite users and applications of a group.
        Overwrite users and applications configuration in a group. Any information that you add using this command will overwrite the previous configuration.
        :param group_id:
        :param user_ids:
        :param application_ids:
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = api.set_group_members(
                group_id="example",
                user_ids=[],
                application_ids=[],
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

    def add_group_member(
        self,
        *,
        group_id: str,
        user_id: Optional[str] = None,
        application_id: Optional[str] = None,
    ) -> Group:
        """
        Add a user or an application to a group.
        Add a user or an application to a group. You can specify a `user_id` and and `application_id` in the body of your request. Note that you can only add one of each per request.
        :param group_id: ID of the group.
        :param user_id: ID of the user to add.
        One-Of ('member'): at most one of 'user_id', 'application_id' could be set.
        :param application_id: ID of the application to add.
        One-Of ('member'): at most one of 'user_id', 'application_id' could be set.
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = api.add_group_member(
                group_id="example",
            )
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

    def add_group_members(
        self,
        *,
        group_id: str,
        user_ids: Optional[List[str]] = None,
        application_ids: Optional[List[str]] = None,
    ) -> Group:
        """
        Add multiple users and applications to a group.
        Add multiple users and applications to a group in a single call. You can specify an array of `user_id`s and `application_id`s. Note that any existing users and applications in the group will remain. To add new users/applications and delete pre-existing ones, use the [Overwrite users and applications of a group](#path-groups-overwrite-users-and-applications-of-a-group) method.
        :param group_id: ID of the group.
        :param user_ids: IDs of the users to add.
        :param application_ids: IDs of the applications to add.
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = api.add_group_members(
                group_id="example",
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "POST",
            f"/iam/v1alpha1/groups/{param_group_id}/add-members",
            body=marshal_AddGroupMembersRequest(
                AddGroupMembersRequest(
                    group_id=group_id,
                    user_ids=user_ids,
                    application_ids=application_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Group(res.json())

    def remove_group_member(
        self,
        *,
        group_id: str,
        user_id: Optional[str] = None,
        application_id: Optional[str] = None,
    ) -> Group:
        """
        Remove a user or an application from a group.
        Remove a user or an application from a group. You can specify a `user_id` and and `application_id` in the body of your request. Note that you can only remove one of each per request. Removing a user from a group means that any permissions given to them via the group (i.e. from an attached policy) will no longer apply. Be sure you want to remove these permissions from the user before proceeding.
        :param group_id: ID of the group.
        :param user_id: ID of the user to remove.
        One-Of ('member'): at most one of 'user_id', 'application_id' could be set.
        :param application_id: ID of the application to remove.
        One-Of ('member'): at most one of 'user_id', 'application_id' could be set.
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = api.remove_group_member(
                group_id="example",
            )
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

    def delete_group(
        self,
        *,
        group_id: str,
    ) -> None:
        """
        Delete a group.
        Delete a group. Note that this action is irreversible and could delete permissions for group members. Policies attached to users and applications via this group will no longer apply.
        :param group_id: ID of the group to delete.

        Usage:
        ::

            result = api.delete_group(
                group_id="example",
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/groups/{param_group_id}",
        )

        self._throw_on_error(res)

    def list_policies(
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
        tag: Optional[str] = None,
        policy_ids: Optional[List[str]] = None,
    ) -> ListPoliciesResponse:
        """
        List policies of an Organization.
        List the policies of an Organization. By default, the policies listed are ordered by creation date in ascending order. This can be modified via the `order_by` field. You must define the `organization_id` in the query path of your request. You can also define additional parameters to filter your query, such as `user_ids`, `groups_ids`, `application_ids`, and `policy_name`.
        :param order_by: Criteria for sorting results.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater than 1.
        :param organization_id: ID of the Organization to filter.
        :param editable: Defines whether or not filter out editable policies.
        :param user_ids: Defines whether or not to filter by list of user IDs.
        :param group_ids: Defines whether or not to filter by list of group IDs.
        :param application_ids: Filter by a list of application IDs.
        :param no_principal: Defines whether or not the policy is attributed to a principal.
        :param policy_name: Name of the policy to fetch.
        :param tag: Filter by tags containing a given string.
        :param policy_ids: Filter by a list of IDs.
        :return: :class:`ListPoliciesResponse <ListPoliciesResponse>`

        Usage:
        ::

            result = api.list_policies()
        """

        res = self._request(
            "GET",
            "/iam/v1alpha1/policies",
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
                "policy_ids": policy_ids,
                "policy_name": policy_name,
                "tag": tag,
                "user_ids": user_ids,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPoliciesResponse(res.json())

    def list_policies_all(
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
        tag: Optional[str] = None,
        policy_ids: Optional[List[str]] = None,
    ) -> List[Policy]:
        """
        List policies of an Organization.
        List the policies of an Organization. By default, the policies listed are ordered by creation date in ascending order. This can be modified via the `order_by` field. You must define the `organization_id` in the query path of your request. You can also define additional parameters to filter your query, such as `user_ids`, `groups_ids`, `application_ids`, and `policy_name`.
        :param order_by: Criteria for sorting results.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater than 1.
        :param organization_id: ID of the Organization to filter.
        :param editable: Defines whether or not filter out editable policies.
        :param user_ids: Defines whether or not to filter by list of user IDs.
        :param group_ids: Defines whether or not to filter by list of group IDs.
        :param application_ids: Filter by a list of application IDs.
        :param no_principal: Defines whether or not the policy is attributed to a principal.
        :param policy_name: Name of the policy to fetch.
        :param tag: Filter by tags containing a given string.
        :param policy_ids: Filter by a list of IDs.
        :return: :class:`List[Policy] <List[Policy]>`

        Usage:
        ::

            result = api.list_policies_all()
        """

        return fetch_all_pages(
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
                "tag": tag,
                "policy_ids": policy_ids,
            },
        )

    def create_policy(
        self,
        *,
        description: str,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        rules: Optional[List[RuleSpecs]] = None,
        tags: Optional[List[str]] = None,
        user_id: Optional[str] = None,
        group_id: Optional[str] = None,
        application_id: Optional[str] = None,
        no_principal: Optional[bool] = None,
    ) -> Policy:
        """
        Create a new policy.
        Create a new application. You must define the `name` parameter in the request. You can specify parameters such as `user_id`, `groups_id`, `application_id`, `no_principal`, `rules` and its child attributes.
        :param description: Description of the policy to create (max length is 200 characters).
        :param name: Name of the policy to create (max length is 64 characters).
        :param organization_id: ID of the Organization.
        :param rules: Rules of the policy to create.
        :param tags: Tags associated with the policy (maximum of 10 tags).
        :param user_id: ID of user attributed to the policy.
        One-Of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
        :param group_id: ID of group attributed to the policy.
        One-Of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
        :param application_id: ID of application attributed to the policy.
        One-Of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
        :param no_principal: Defines whether or not a policy is attributed to a principal.
        One-Of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
        :return: :class:`Policy <Policy>`

        Usage:
        ::

            result = api.create_policy(
                description="example",
            )
        """

        res = self._request(
            "POST",
            "/iam/v1alpha1/policies",
            body=marshal_CreatePolicyRequest(
                CreatePolicyRequest(
                    description=description,
                    name=name or random_name(prefix="pol"),
                    organization_id=organization_id,
                    rules=rules,
                    tags=tags,
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

    def get_policy(
        self,
        *,
        policy_id: str,
    ) -> Policy:
        """
        Get an existing policy.
        Retrieve information about a policy, speficified by the `policy_id` parameter. The policy's full details, including `id`, `name`, `organization_id`, `nb_rules` and `nb_scopes`, `nb_permission_sets` are returned in the response.
        :param policy_id: Id of policy to search.
        :return: :class:`Policy <Policy>`

        Usage:
        ::

            result = api.get_policy(
                policy_id="example",
            )
        """

        param_policy_id = validate_path_param("policy_id", policy_id)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/policies/{param_policy_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Policy(res.json())

    def update_policy(
        self,
        *,
        policy_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        user_id: Optional[str] = None,
        group_id: Optional[str] = None,
        application_id: Optional[str] = None,
        no_principal: Optional[bool] = None,
    ) -> Policy:
        """
        Update an existing policy.
        Update the parameters of a policy, including `name`, `description`, `user_id`, `group_id`, `application_id` and `no_principal`.
        :param policy_id: Id of policy to update.
        :param name: New name for the policy (max length is 64 characters).
        :param description: New description of policy (max length is 200 characters).
        :param tags: New tags for the policy (maximum of 10 tags).
        :param user_id: New ID of user attributed to the policy.
        One-Of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
        :param group_id: New ID of group attributed to the policy.
        One-Of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
        :param application_id: New ID of application attributed to the policy.
        One-Of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
        :param no_principal: Defines whether or not the policy is attributed to a principal.
        One-Of ('principal'): at most one of 'user_id', 'group_id', 'application_id', 'no_principal' could be set.
        :return: :class:`Policy <Policy>`

        Usage:
        ::

            result = api.update_policy(
                policy_id="example",
            )
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
                    tags=tags,
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

    def delete_policy(
        self,
        *,
        policy_id: str,
    ) -> None:
        """
        Delete a policy.
        Delete a policy. You must define specify the `policy_id` parameter in your request. Note that when deleting a policy, all permissions it gives to its principal (user, group or application) will be revoked.
        :param policy_id: Id of policy to delete.

        Usage:
        ::

            result = api.delete_policy(
                policy_id="example",
            )
        """

        param_policy_id = validate_path_param("policy_id", policy_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/policies/{param_policy_id}",
        )

        self._throw_on_error(res)

    def clone_policy(
        self,
        *,
        policy_id: str,
    ) -> Policy:
        """
        Clone a policy.
        Clone a policy. You must define specify the `policy_id` parameter in your request.
        :param policy_id:
        :return: :class:`Policy <Policy>`

        Usage:
        ::

            result = api.clone_policy(
                policy_id="example",
            )
        """

        param_policy_id = validate_path_param("policy_id", policy_id)

        res = self._request(
            "POST",
            f"/iam/v1alpha1/policies/{param_policy_id}/clone",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Policy(res.json())

    def set_rules(
        self,
        *,
        policy_id: str,
        rules: List[RuleSpecs],
    ) -> SetRulesResponse:
        """
        Set rules of a given policy.
        Overwrite the rules of a given policy. Any information that you add using this command will overwrite the previous configuration. If you include some of the rules you already had in your previous configuration in your new one, but you change their order, the new order of display will apply. While policy rules are ordered, they have no impact on the access logic of IAM because rules are allow-only.
        :param policy_id: Id of policy to update.
        :param rules: Rules of the policy to set.
        :return: :class:`SetRulesResponse <SetRulesResponse>`

        Usage:
        ::

            result = api.set_rules(
                policy_id="example",
                rules=[],
            )
        """

        res = self._request(
            "PUT",
            "/iam/v1alpha1/rules",
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

    def list_rules(
        self,
        *,
        policy_id: str,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListRulesResponse:
        """
        List rules of a given policy.
        List the rules of a given policy. By default, the rules listed are ordered by creation date in ascending order. This can be modified via the `order_by` field. You must define the `policy_id` in the query path of your request.
        :param policy_id: Id of policy to search.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater than 1.
        :return: :class:`ListRulesResponse <ListRulesResponse>`

        Usage:
        ::

            result = api.list_rules(
                policy_id="example",
            )
        """

        res = self._request(
            "GET",
            "/iam/v1alpha1/rules",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "policy_id": policy_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRulesResponse(res.json())

    def list_rules_all(
        self,
        *,
        policy_id: str,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[Rule]:
        """
        List rules of a given policy.
        List the rules of a given policy. By default, the rules listed are ordered by creation date in ascending order. This can be modified via the `order_by` field. You must define the `policy_id` in the query path of your request.
        :param policy_id: Id of policy to search.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater than 1.
        :return: :class:`List[Rule] <List[Rule]>`

        Usage:
        ::

            result = api.list_rules_all(
                policy_id="example",
            )
        """

        return fetch_all_pages(
            type=ListRulesResponse,
            key="rules",
            fetcher=self.list_rules,
            args={
                "policy_id": policy_id,
                "page_size": page_size,
                "page": page,
            },
        )

    def list_permission_sets(
        self,
        *,
        order_by: Optional[ListPermissionSetsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
    ) -> ListPermissionSetsResponse:
        """
        List permission sets.
        List permission sets available for given Organization. You must define the `organization_id` in the query path of your request.
        :param order_by: Criteria for sorting results.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater than 1.
        :param organization_id: Filter by Organization ID.
        :return: :class:`ListPermissionSetsResponse <ListPermissionSetsResponse>`

        Usage:
        ::

            result = api.list_permission_sets()
        """

        res = self._request(
            "GET",
            "/iam/v1alpha1/permission-sets",
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

    def list_permission_sets_all(
        self,
        *,
        order_by: Optional[ListPermissionSetsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
    ) -> List[PermissionSet]:
        """
        List permission sets.
        List permission sets available for given Organization. You must define the `organization_id` in the query path of your request.
        :param order_by: Criteria for sorting results.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater than 1.
        :param organization_id: Filter by Organization ID.
        :return: :class:`List[PermissionSet] <List[PermissionSet]>`

        Usage:
        ::

            result = api.list_permission_sets_all()
        """

        return fetch_all_pages(
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

    def list_api_keys(
        self,
        *,
        order_by: Optional[ListAPIKeysRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        application_id: Optional[str] = None,
        user_id: Optional[str] = None,
        editable: Optional[bool] = None,
        expired: Optional[bool] = None,
        access_key: Optional[str] = None,
        description: Optional[str] = None,
        bearer_id: Optional[str] = None,
        bearer_type: Optional[BearerType] = None,
        access_keys: Optional[List[str]] = None,
    ) -> ListAPIKeysResponse:
        """
        List API keys.
        List API keys. By default, the API keys listed are ordered by creation date in ascending order. This can be modified via the `order_by` field. You can define additional parameters for your query such as `editable`, `expired`, `access_key` and `bearer_id`.
        :param order_by: Criteria for sorting results.
        :param page: Page number. Value must be greater or equal to 1.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param organization_id: ID of Organization.
        :param application_id: ID of application that bears the API key.
        One-Of ('bearer'): at most one of 'application_id', 'user_id' could be set.
        :param user_id: ID of user that bears the API key.
        One-Of ('bearer'): at most one of 'application_id', 'user_id' could be set.
        :param editable: Defines whether to filter out editable API keys or not.
        :param expired: Defines whether to filter out expired API keys or not.
        :param access_key: Filter by access key (deprecated in favor of `access_keys`).
        :param description: Filter by description.
        :param bearer_id: Filter by bearer ID.
        :param bearer_type: Filter by type of bearer.
        :param access_keys: Filter by a list of access keys.
        :return: :class:`ListAPIKeysResponse <ListAPIKeysResponse>`

        Usage:
        ::

            result = api.list_api_keys()
        """

        res = self._request(
            "GET",
            "/iam/v1alpha1/api-keys",
            params={
                "access_key": access_key,
                "access_keys": access_keys,
                "bearer_id": bearer_id,
                "bearer_type": bearer_type,
                "description": description,
                "editable": editable,
                "expired": expired,
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

    def list_api_keys_all(
        self,
        *,
        order_by: Optional[ListAPIKeysRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        application_id: Optional[str] = None,
        user_id: Optional[str] = None,
        editable: Optional[bool] = None,
        expired: Optional[bool] = None,
        access_key: Optional[str] = None,
        description: Optional[str] = None,
        bearer_id: Optional[str] = None,
        bearer_type: Optional[BearerType] = None,
        access_keys: Optional[List[str]] = None,
    ) -> List[APIKey]:
        """
        List API keys.
        List API keys. By default, the API keys listed are ordered by creation date in ascending order. This can be modified via the `order_by` field. You can define additional parameters for your query such as `editable`, `expired`, `access_key` and `bearer_id`.
        :param order_by: Criteria for sorting results.
        :param page: Page number. Value must be greater or equal to 1.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param organization_id: ID of Organization.
        :param application_id: ID of application that bears the API key.
        One-Of ('bearer'): at most one of 'application_id', 'user_id' could be set.
        :param user_id: ID of user that bears the API key.
        One-Of ('bearer'): at most one of 'application_id', 'user_id' could be set.
        :param editable: Defines whether to filter out editable API keys or not.
        :param expired: Defines whether to filter out expired API keys or not.
        :param access_key: Filter by access key (deprecated in favor of `access_keys`).
        :param description: Filter by description.
        :param bearer_id: Filter by bearer ID.
        :param bearer_type: Filter by type of bearer.
        :param access_keys: Filter by a list of access keys.
        :return: :class:`List[APIKey] <List[APIKey]>`

        Usage:
        ::

            result = api.list_api_keys_all()
        """

        return fetch_all_pages(
            type=ListAPIKeysResponse,
            key="api_keys",
            fetcher=self.list_api_keys,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "organization_id": organization_id,
                "editable": editable,
                "expired": expired,
                "access_key": access_key,
                "description": description,
                "bearer_id": bearer_id,
                "bearer_type": bearer_type,
                "access_keys": access_keys,
                "application_id": application_id,
                "user_id": user_id,
            },
        )

    def create_api_key(
        self,
        *,
        description: str,
        application_id: Optional[str] = None,
        user_id: Optional[str] = None,
        expires_at: Optional[datetime] = None,
        default_project_id: Optional[str] = None,
    ) -> APIKey:
        """
        Create an API key.
        Create an API key. You must specify the `application_id` or the `user_id` and the description. You can also specify the `default_project_id` which is the Project ID of your preferred Project, to use with Object Storage. The `access_key` and `secret_key` values are returned in the response. Note that he secret key is only showed once. Make sure that you copy and store both keys somewhere safe.
        :param description: Description of the API key (max length is 200 characters).
        :param application_id: ID of the application.
        One-Of ('bearer'): at most one of 'application_id', 'user_id' could be set.
        :param user_id: ID of the user.
        One-Of ('bearer'): at most one of 'application_id', 'user_id' could be set.
        :param expires_at: Expiration date of the API key.
        :param default_project_id: Default Project ID to use with Object Storage.
        :return: :class:`APIKey <APIKey>`

        Usage:
        ::

            result = api.create_api_key(
                description="example",
            )
        """

        res = self._request(
            "POST",
            "/iam/v1alpha1/api-keys",
            body=marshal_CreateAPIKeyRequest(
                CreateAPIKeyRequest(
                    description=description,
                    expires_at=expires_at,
                    default_project_id=default_project_id,
                    application_id=application_id,
                    user_id=user_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_APIKey(res.json())

    def get_api_key(
        self,
        *,
        access_key: str,
    ) -> APIKey:
        """
        Get an API key.
        Retrive information about an API key, specified by the `access_key` parameter. The API key's details, including either the `user_id` or `application_id` of its bearer are returned in the response. Note that the string value for the `secret_key` is nullable, and therefore is not displayed in the response. The `secret_key` value is only displayed upon API key creation.
        :param access_key: Access key to search for.
        :return: :class:`APIKey <APIKey>`

        Usage:
        ::

            result = api.get_api_key(
                access_key="example",
            )
        """

        param_access_key = validate_path_param("access_key", access_key)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/api-keys/{param_access_key}",
        )

        self._throw_on_error(res)
        return unmarshal_APIKey(res.json())

    def update_api_key(
        self,
        *,
        access_key: str,
        default_project_id: Optional[str] = None,
        description: Optional[str] = None,
    ) -> APIKey:
        """
        Update an API key.
        Update the parameters of an API key, including `default_project_id` and `description`.
        :param access_key: Access key to update.
        :param default_project_id: New default Project ID to set.
        :param description: New description to update.
        :return: :class:`APIKey <APIKey>`

        Usage:
        ::

            result = api.update_api_key(
                access_key="example",
            )
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

    def delete_api_key(
        self,
        *,
        access_key: str,
    ) -> None:
        """
        Delete an API key.
        Delete an API key. Note that this action is irreversible and cannot be undone. Make sure you update any configurations using the API keys you delete.
        :param access_key: Access key to delete.

        Usage:
        ::

            result = api.delete_api_key(
                access_key="example",
            )
        """

        param_access_key = validate_path_param("access_key", access_key)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/api-keys/{param_access_key}",
        )

        self._throw_on_error(res)

    def list_quota(
        self,
        *,
        order_by: Optional[ListQuotaRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        quotum_names: Optional[List[str]] = None,
    ) -> ListQuotaResponse:
        """
        List all quotas in the Organization.
        List all product and features quota for an Organization, with their associated limits. By default, the quota listed are ordered by creation date in ascending order. This can be modified via the `order_by` field. You must define the `organization_id` in the query path of your request.
        :param order_by: Criteria for sorting results.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater than 1.
        :param organization_id: Filter by Organization ID.
        :param quotum_names: List of quotum names to filter from.
        :return: :class:`ListQuotaResponse <ListQuotaResponse>`

        Usage:
        ::

            result = api.list_quota()
        """

        res = self._request(
            "GET",
            "/iam/v1alpha1/quota",
            params={
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "quotum_names": quotum_names,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListQuotaResponse(res.json())

    def list_quota_all(
        self,
        *,
        order_by: Optional[ListQuotaRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        quotum_names: Optional[List[str]] = None,
    ) -> List[Quotum]:
        """
        List all quotas in the Organization.
        List all product and features quota for an Organization, with their associated limits. By default, the quota listed are ordered by creation date in ascending order. This can be modified via the `order_by` field. You must define the `organization_id` in the query path of your request.
        :param order_by: Criteria for sorting results.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater than 1.
        :param organization_id: Filter by Organization ID.
        :param quotum_names: List of quotum names to filter from.
        :return: :class:`List[Quotum] <List[Quotum]>`

        Usage:
        ::

            result = api.list_quota_all()
        """

        return fetch_all_pages(
            type=ListQuotaResponse,
            key="quota",
            fetcher=self.list_quota,
            args={
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
                "organization_id": organization_id,
                "quotum_names": quotum_names,
            },
        )

    def get_quotum(
        self,
        *,
        quotum_name: str,
        organization_id: Optional[str] = None,
    ) -> Quotum:
        """
        Get a quota in the Organization.
        Retrieve information about a resource quota, specified by the `quotum_name` parameter. The quota's `limit`, or whether it is unlimited, is returned in the response.
        :param quotum_name: Name of the quota to get.
        :param organization_id: ID of the Organization.
        :return: :class:`Quotum <Quotum>`

        Usage:
        ::

            result = api.get_quotum(
                quotum_name="example",
            )
        """

        param_quotum_name = validate_path_param("quotum_name", quotum_name)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/quota/{param_quotum_name}",
            params={
                "organization_id": organization_id
                or self.client.default_organization_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_Quotum(res.json())

    def list_jw_ts(
        self,
        *,
        order_by: Optional[ListJWTsRequestOrderBy] = None,
        audience_id: Optional[str] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        expired: Optional[bool] = None,
    ) -> ListJWTsResponse:
        """
        List JWTs.
        :param order_by: Criteria for sorting results.
        :param audience_id: ID of the user to search.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater to 1.
        :param expired: Filter out expired JWTs or not.
        :return: :class:`ListJWTsResponse <ListJWTsResponse>`

        Usage:
        ::

            result = api.list_jw_ts()
        """

        res = self._request(
            "GET",
            "/iam/v1alpha1/jwts",
            params={
                "audience_id": audience_id,
                "expired": expired,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListJWTsResponse(res.json())

    def list_jw_ts_all(
        self,
        *,
        order_by: Optional[ListJWTsRequestOrderBy] = None,
        audience_id: Optional[str] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        expired: Optional[bool] = None,
    ) -> List[JWT]:
        """
        List JWTs.
        :param order_by: Criteria for sorting results.
        :param audience_id: ID of the user to search.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater to 1.
        :param expired: Filter out expired JWTs or not.
        :return: :class:`List[JWT] <List[JWT]>`

        Usage:
        ::

            result = api.list_jw_ts_all()
        """

        return fetch_all_pages(
            type=ListJWTsResponse,
            key="jwts",
            fetcher=self.list_jw_ts,
            args={
                "order_by": order_by,
                "audience_id": audience_id,
                "page_size": page_size,
                "page": page,
                "expired": expired,
            },
        )

    def create_jwt(
        self,
        *,
        user_id: str,
        referrer: str,
    ) -> EncodedJWT:
        """
        Create a JWT.
        :param user_id: ID of the user the JWT will be created for.
        :param referrer: Referrer of the JWT.
        :return: :class:`EncodedJWT <EncodedJWT>`

        Usage:
        ::

            result = api.create_jwt(
                user_id="example",
                referrer="example",
            )
        """

        res = self._request(
            "POST",
            "/iam/v1alpha1/jwts",
            body=marshal_CreateJWTRequest(
                CreateJWTRequest(
                    user_id=user_id,
                    referrer=referrer,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_EncodedJWT(res.json())

    def get_jwt(
        self,
        *,
        jti: str,
    ) -> JWT:
        """
        Get a JWT.
        :param jti: JWT ID of the JWT to get.
        :return: :class:`JWT <JWT>`

        Usage:
        ::

            result = api.get_jwt(
                jti="example",
            )
        """

        param_jti = validate_path_param("jti", jti)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/jwts/{param_jti}",
        )

        self._throw_on_error(res)
        return unmarshal_JWT(res.json())

    def delete_jwt(
        self,
        *,
        jti: str,
    ) -> None:
        """
        Delete a JWT.
        :param jti: JWT ID of the JWT to delete.

        Usage:
        ::

            result = api.delete_jwt(
                jti="example",
            )
        """

        param_jti = validate_path_param("jti", jti)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/jwts/{param_jti}",
        )

        self._throw_on_error(res)

    def list_logs(
        self,
        *,
        order_by: Optional[ListLogsRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        created_after: Optional[datetime] = None,
        created_before: Optional[datetime] = None,
        action: Optional[LogAction] = None,
        resource_type: Optional[LogResourceType] = None,
        search: Optional[str] = None,
    ) -> ListLogsResponse:
        """
        List logs.
        List logs available for given Organization. You must define the `organization_id` in the query path of your request.
        :param order_by: Criteria for sorting results.
        :param organization_id: Filter by Organization ID.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater to 1.
        :param created_after: Defined whether or not to filter out logs created after this timestamp.
        :param created_before: Defined whether or not to filter out logs created before this timestamp.
        :param action: Defined whether or not to filter out by a specific action.
        :param resource_type: Defined whether or not to filter out by a specific type of resource.
        :param search: Defined whether or not to filter out log by bearer ID or resource ID.
        :return: :class:`ListLogsResponse <ListLogsResponse>`

        Usage:
        ::

            result = api.list_logs()
        """

        res = self._request(
            "GET",
            "/iam/v1alpha1/logs",
            params={
                "action": action,
                "created_after": created_after,
                "created_before": created_before,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "resource_type": resource_type,
                "search": search,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListLogsResponse(res.json())

    def list_logs_all(
        self,
        *,
        order_by: Optional[ListLogsRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        created_after: Optional[datetime] = None,
        created_before: Optional[datetime] = None,
        action: Optional[LogAction] = None,
        resource_type: Optional[LogResourceType] = None,
        search: Optional[str] = None,
    ) -> List[Log]:
        """
        List logs.
        List logs available for given Organization. You must define the `organization_id` in the query path of your request.
        :param order_by: Criteria for sorting results.
        :param organization_id: Filter by Organization ID.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater to 1.
        :param created_after: Defined whether or not to filter out logs created after this timestamp.
        :param created_before: Defined whether or not to filter out logs created before this timestamp.
        :param action: Defined whether or not to filter out by a specific action.
        :param resource_type: Defined whether or not to filter out by a specific type of resource.
        :param search: Defined whether or not to filter out log by bearer ID or resource ID.
        :return: :class:`List[Log] <List[Log]>`

        Usage:
        ::

            result = api.list_logs_all()
        """

        return fetch_all_pages(
            type=ListLogsResponse,
            key="logs",
            fetcher=self.list_logs,
            args={
                "order_by": order_by,
                "organization_id": organization_id,
                "page_size": page_size,
                "page": page,
                "created_after": created_after,
                "created_before": created_before,
                "action": action,
                "resource_type": resource_type,
                "search": search,
            },
        )

    def get_log(
        self,
        *,
        log_id: str,
    ) -> Log:
        """
        Get a log.
        Retrieve information about a log, specified by the `log_id` parameter. The log's full details, including `id`, `ip`, `user_agent`, `action`, `bearer_id`, `resource_type` and `resource_id` are returned in the response.
        :param log_id: ID of the log.
        :return: :class:`Log <Log>`

        Usage:
        ::

            result = api.get_log(
                log_id="example",
            )
        """

        param_log_id = validate_path_param("log_id", log_id)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/logs/{param_log_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Log(res.json())
