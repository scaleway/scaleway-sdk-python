# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    ScwFile,
)
from scaleway_core.utils import (
    OneOfPossibility,
    random_name,
    resolve_one_of,
    validate_path_param,
    fetch_all_pages_async,
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
    ListScimTokensRequestOrderBy,
    ListUserWebAuthnAuthenticatorsRequestOrderBy,
    ListUsersRequestOrderBy,
    LogAction,
    LogResourceType,
    SamlCertificateType,
    UserType,
    APIKey,
    AddGroupMemberRequest,
    AddGroupMembersRequest,
    AddSamlCertificateRequest,
    Application,
    CreateAPIKeyRequest,
    CreateApplicationRequest,
    CreateGroupRequest,
    CreateJWTRequest,
    CreatePolicyRequest,
    CreateSSHKeyRequest,
    CreateScimTokenResponse,
    CreateUserRequest,
    CreateUserRequestMember,
    EncodedJWT,
    FinishUserWebAuthnRegistrationRequest,
    FinishUserWebAuthnRegistrationResponse,
    GetUserConnectionsResponse,
    Group,
    InitiateUserConnectionResponse,
    JWT,
    JoinUserConnectionRequest,
    ListAPIKeysResponse,
    ListApplicationsResponse,
    ListGracePeriodsResponse,
    ListGroupsResponse,
    ListJWTsResponse,
    ListLogsResponse,
    ListPermissionSetsResponse,
    ListPoliciesResponse,
    ListQuotaResponse,
    ListRulesResponse,
    ListSSHKeysResponse,
    ListSamlCertificatesResponse,
    ListScimTokensResponse,
    ListUserWebAuthnAuthenticatorsResponse,
    ListUsersResponse,
    Log,
    MFAOTP,
    Organization,
    OrganizationSecuritySettings,
    ParseSamlMetadataRequest,
    ParseSamlMetadataResponse,
    PermissionSet,
    Policy,
    Quotum,
    RemoveGroupMemberRequest,
    RemoveUserConnectionRequest,
    Rule,
    RuleSpecs,
    SSHKey,
    Saml,
    SamlCertificate,
    Scim,
    ScimToken,
    SetGroupMembersRequest,
    SetOrganizationAliasRequest,
    SetRulesRequest,
    SetRulesResponse,
    StartUserWebAuthnRegistrationResponse,
    UpdateAPIKeyRequest,
    UpdateApplicationRequest,
    UpdateGroupRequest,
    UpdateOrganizationLoginMethodsRequest,
    UpdateOrganizationSecuritySettingsRequest,
    UpdatePolicyRequest,
    UpdateSSHKeyRequest,
    UpdateSamlRequest,
    UpdateUserPasswordRequest,
    UpdateUserRequest,
    UpdateUserUsernameRequest,
    UpdateWebAuthnAuthenticatorRequest,
    User,
    ValidateUserMFAOTPRequest,
    ValidateUserMFAOTPResponse,
    WebAuthnAuthenticator,
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
    unmarshal_SamlCertificate,
    unmarshal_WebAuthnAuthenticator,
    unmarshal_User,
    unmarshal_CreateScimTokenResponse,
    unmarshal_EncodedJWT,
    unmarshal_FinishUserWebAuthnRegistrationResponse,
    unmarshal_GetUserConnectionsResponse,
    unmarshal_InitiateUserConnectionResponse,
    unmarshal_ListAPIKeysResponse,
    unmarshal_ListApplicationsResponse,
    unmarshal_ListGracePeriodsResponse,
    unmarshal_ListGroupsResponse,
    unmarshal_ListJWTsResponse,
    unmarshal_ListLogsResponse,
    unmarshal_ListPermissionSetsResponse,
    unmarshal_ListPoliciesResponse,
    unmarshal_ListQuotaResponse,
    unmarshal_ListRulesResponse,
    unmarshal_ListSSHKeysResponse,
    unmarshal_ListSamlCertificatesResponse,
    unmarshal_ListScimTokensResponse,
    unmarshal_ListUserWebAuthnAuthenticatorsResponse,
    unmarshal_ListUsersResponse,
    unmarshal_MFAOTP,
    unmarshal_Organization,
    unmarshal_OrganizationSecuritySettings,
    unmarshal_ParseSamlMetadataResponse,
    unmarshal_Saml,
    unmarshal_Scim,
    unmarshal_SetRulesResponse,
    unmarshal_StartUserWebAuthnRegistrationResponse,
    unmarshal_ValidateUserMFAOTPResponse,
    marshal_AddGroupMemberRequest,
    marshal_AddGroupMembersRequest,
    marshal_AddSamlCertificateRequest,
    marshal_CreateAPIKeyRequest,
    marshal_CreateApplicationRequest,
    marshal_CreateGroupRequest,
    marshal_CreateJWTRequest,
    marshal_CreatePolicyRequest,
    marshal_CreateSSHKeyRequest,
    marshal_CreateUserRequest,
    marshal_FinishUserWebAuthnRegistrationRequest,
    marshal_JoinUserConnectionRequest,
    marshal_ParseSamlMetadataRequest,
    marshal_RemoveGroupMemberRequest,
    marshal_RemoveUserConnectionRequest,
    marshal_SetGroupMembersRequest,
    marshal_SetOrganizationAliasRequest,
    marshal_SetRulesRequest,
    marshal_UpdateAPIKeyRequest,
    marshal_UpdateApplicationRequest,
    marshal_UpdateGroupRequest,
    marshal_UpdateOrganizationLoginMethodsRequest,
    marshal_UpdateOrganizationSecuritySettingsRequest,
    marshal_UpdatePolicyRequest,
    marshal_UpdateSSHKeyRequest,
    marshal_UpdateSamlRequest,
    marshal_UpdateUserPasswordRequest,
    marshal_UpdateUserRequest,
    marshal_UpdateUserUsernameRequest,
    marshal_UpdateWebAuthnAuthenticatorRequest,
    marshal_ValidateUserMFAOTPRequest,
)


class IamV1Alpha1API(API):
    """
    This API allows you to manage Identity and Access Management (IAM) across your Scaleway Organizations, Projects and resources.
    """

    async def list_ssh_keys(
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

            result = await api.list_ssh_keys()
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
    ) -> list[SSHKey]:
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
        :return: :class:`list[SSHKey] <list[SSHKey]>`

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
        Create an SSH key.
        Add a new SSH key to a Scaleway Project. You must specify the `name`, `public_key` and `project_id`.
        :param public_key: SSH public key. Currently only the ssh-rsa, ssh-dss (DSA), ssh-ed25519 and ecdsa keys with NIST curves are supported. Max length is 65000.
        :param name: Name of the SSH key. Max length is 1000.
        :param project_id: Project the resource is attributed to.
        :return: :class:`SSHKey <SSHKey>`

        Usage:
        ::

            result = await api.create_ssh_key(
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

    async def get_ssh_key(
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

            result = await api.get_ssh_key(
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

    async def update_ssh_key(
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

            result = await api.update_ssh_key(
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

    async def delete_ssh_key(
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

            result = await api.delete_ssh_key(
                ssh_key_id="example",
            )
        """

        param_ssh_key_id = validate_path_param("ssh_key_id", ssh_key_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/ssh-keys/{param_ssh_key_id}",
        )

        self._throw_on_error(res)

    async def list_users(
        self,
        *,
        order_by: Optional[ListUsersRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        user_ids: Optional[list[str]] = None,
        mfa: Optional[bool] = None,
        tag: Optional[str] = None,
        type_: Optional[UserType] = None,
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
        :param type_: Filter by user type.
        :return: :class:`ListUsersResponse <ListUsersResponse>`

        Usage:
        ::

            result = await api.list_users()
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
                "type": type_,
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
        user_ids: Optional[list[str]] = None,
        mfa: Optional[bool] = None,
        tag: Optional[str] = None,
        type_: Optional[UserType] = None,
    ) -> list[User]:
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
        :param type_: Filter by user type.
        :return: :class:`list[User] <list[User]>`

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
                "mfa": mfa,
                "tag": tag,
                "type_": type_,
            },
        )

    async def get_user(
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

            result = await api.get_user(
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

    async def update_user(
        self,
        *,
        user_id: str,
        tags: Optional[list[str]] = None,
        email: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone_number: Optional[str] = None,
        locale: Optional[str] = None,
    ) -> User:
        """
        Update a user.
        Update the parameters of a user, including `tags`.
        :param user_id: ID of the user to update.
        :param tags: New tags for the user (maximum of 10 tags).
        :param email: IAM member email.
        :param first_name: IAM member first name.
        :param last_name: IAM member last name.
        :param phone_number: IAM member phone number.
        :param locale: IAM member locale.
        :return: :class:`User <User>`

        Usage:
        ::

            result = await api.update_user(
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
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    phone_number=phone_number,
                    locale=locale,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_User(res.json())

    async def delete_user(
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

            result = await api.delete_user(
                user_id="example",
            )
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/users/{param_user_id}",
        )

        self._throw_on_error(res)

    async def create_user(
        self,
        *,
        organization_id: Optional[str] = None,
        email: Optional[str] = None,
        tags: Optional[list[str]] = None,
        member: Optional[CreateUserRequestMember] = None,
    ) -> User:
        """
        Create a new user.
        Create a new user. You must define the `organization_id` in your request. If you are adding a member, enter the member's details. If you are adding a guest, you must define the `email` and not add the member attribute.
        :param organization_id: ID of the Organization.
        :param email: Email of the user.
        One-Of ('type'): at most one of 'email', 'member' could be set.
        :param tags: Tags associated with the user.
        :param member: Details of IAM member.
        One-Of ('type'): at most one of 'email', 'member' could be set.
        :return: :class:`User <User>`

        Usage:
        ::

            result = await api.create_user()
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

    async def update_user_username(
        self,
        *,
        user_id: str,
        username: str,
    ) -> User:
        """
        Update an user's username.
        :param user_id: ID of the user to update.
        :param username: The new username.
        :return: :class:`User <User>`

        Usage:
        ::

            result = await api.update_user_username(
                user_id="example",
                username="example",
            )
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "POST",
            f"/iam/v1alpha1/users/{param_user_id}/update-username",
            body=marshal_UpdateUserUsernameRequest(
                UpdateUserUsernameRequest(
                    user_id=user_id,
                    username=username,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_User(res.json())

    async def update_user_password(
        self,
        *,
        user_id: str,
        password: str,
    ) -> User:
        """
        Update an user's password.
        :param user_id: ID of the user to update.
        :param password: The new password.
        :return: :class:`User <User>`

        Usage:
        ::

            result = await api.update_user_password(
                user_id="example",
                password="example",
            )
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "POST",
            f"/iam/v1alpha1/users/{param_user_id}/update-password",
            body=marshal_UpdateUserPasswordRequest(
                UpdateUserPasswordRequest(
                    user_id=user_id,
                    password=password,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_User(res.json())

    async def create_user_mfaotp(
        self,
        *,
        user_id: str,
    ) -> MFAOTP:
        """
        Create a MFA OTP.
        :param user_id: User ID of the MFA OTP.
        :return: :class:`MFAOTP <MFAOTP>`

        Usage:
        ::

            result = await api.create_user_mfaotp(
                user_id="example",
            )
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "POST",
            f"/iam/v1alpha1/users/{param_user_id}/mfa-otp",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_MFAOTP(res.json())

    async def validate_user_mfaotp(
        self,
        *,
        user_id: str,
        one_time_password: str,
    ) -> ValidateUserMFAOTPResponse:
        """
        Validate a MFA OTP.
        :param user_id: User ID of the MFA OTP.
        :param one_time_password: A password generated using the OTP.
        :return: :class:`ValidateUserMFAOTPResponse <ValidateUserMFAOTPResponse>`

        Usage:
        ::

            result = await api.validate_user_mfaotp(
                user_id="example",
                one_time_password="example",
            )
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "POST",
            f"/iam/v1alpha1/users/{param_user_id}/validate-mfa-otp",
            body=marshal_ValidateUserMFAOTPRequest(
                ValidateUserMFAOTPRequest(
                    user_id=user_id,
                    one_time_password=one_time_password,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ValidateUserMFAOTPResponse(res.json())

    async def delete_user_mfaotp(
        self,
        *,
        user_id: str,
    ) -> None:
        """
        Delete a MFA OTP.
        :param user_id: User ID of the MFA OTP.

        Usage:
        ::

            result = await api.delete_user_mfaotp(
                user_id="example",
            )
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/users/{param_user_id}/mfa-otp",
            body={},
        )

        self._throw_on_error(res)

    async def lock_user(
        self,
        *,
        user_id: str,
    ) -> User:
        """
        Lock a member.
        Lock a member. A locked member cannot log in or use API keys until the locked status is removed.
        :param user_id: ID of the user to lock.
        :return: :class:`User <User>`

        Usage:
        ::

            result = await api.lock_user(
                user_id="example",
            )
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "POST",
            f"/iam/v1alpha1/users/{param_user_id}/lock",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_User(res.json())

    async def unlock_user(
        self,
        *,
        user_id: str,
    ) -> User:
        """
        Unlock a member.
        :param user_id: ID of the user to unlock.
        :return: :class:`User <User>`

        Usage:
        ::

            result = await api.unlock_user(
                user_id="example",
            )
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "POST",
            f"/iam/v1alpha1/users/{param_user_id}/unlock",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_User(res.json())

    async def list_grace_periods(
        self,
        *,
        user_id: Optional[str] = None,
    ) -> ListGracePeriodsResponse:
        """
        List grace periods of a member.
        List the grace periods of a member.
        :param user_id: ID of the user to list grace periods for.
        :return: :class:`ListGracePeriodsResponse <ListGracePeriodsResponse>`

        Usage:
        ::

            result = await api.list_grace_periods()
        """

        res = self._request(
            "GET",
            "/iam/v1alpha1/grace-periods",
            params={
                "user_id": user_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListGracePeriodsResponse(res.json())

    async def get_user_connections(
        self,
        *,
        user_id: str,
    ) -> GetUserConnectionsResponse:
        """
        :param user_id: ID of the user to list connections for.
        :return: :class:`GetUserConnectionsResponse <GetUserConnectionsResponse>`

        Usage:
        ::

            result = await api.get_user_connections(
                user_id="example",
            )
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/users/{param_user_id}/connections",
        )

        self._throw_on_error(res)
        return unmarshal_GetUserConnectionsResponse(res.json())

    async def initiate_user_connection(
        self,
        *,
        user_id: str,
    ) -> InitiateUserConnectionResponse:
        """
        :param user_id: ID of the user that will be added to your connection.
        :return: :class:`InitiateUserConnectionResponse <InitiateUserConnectionResponse>`

        Usage:
        ::

            result = await api.initiate_user_connection(
                user_id="example",
            )
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "POST",
            f"/iam/v1alpha1/users/{param_user_id}/initiate-connection",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_InitiateUserConnectionResponse(res.json())

    async def join_user_connection(
        self,
        *,
        user_id: str,
        token: str,
    ) -> None:
        """
        :param user_id: User ID.
        :param token: A token returned by InitiateUserConnection.

        Usage:
        ::

            result = await api.join_user_connection(
                user_id="example",
                token="example",
            )
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "POST",
            f"/iam/v1alpha1/users/{param_user_id}/join-connection",
            body=marshal_JoinUserConnectionRequest(
                JoinUserConnectionRequest(
                    user_id=user_id,
                    token=token,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def remove_user_connection(
        self,
        *,
        user_id: str,
        target_user_id: str,
    ) -> None:
        """
        :param user_id: ID of the user you want to manage the connection for.
        :param target_user_id: ID of the user you want to remove from your connection.

        Usage:
        ::

            result = await api.remove_user_connection(
                user_id="example",
                target_user_id="example",
            )
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "POST",
            f"/iam/v1alpha1/users/{param_user_id}/remove-connection",
            body=marshal_RemoveUserConnectionRequest(
                RemoveUserConnectionRequest(
                    user_id=user_id,
                    target_user_id=target_user_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def list_applications(
        self,
        *,
        order_by: Optional[ListApplicationsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        editable: Optional[bool] = None,
        application_ids: Optional[list[str]] = None,
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

            result = await api.list_applications()
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

    async def list_applications_all(
        self,
        *,
        order_by: Optional[ListApplicationsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        editable: Optional[bool] = None,
        application_ids: Optional[list[str]] = None,
        tag: Optional[str] = None,
    ) -> list[Application]:
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
        :return: :class:`list[Application] <list[Application]>`

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
                "tag": tag,
            },
        )

    async def create_application(
        self,
        *,
        description: str,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
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

            result = await api.create_application(
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

    async def get_application(
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

            result = await api.get_application(
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

    async def update_application(
        self,
        *,
        application_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[list[str]] = None,
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

            result = await api.update_application(
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

    async def delete_application(
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

            result = await api.delete_application(
                application_id="example",
            )
        """

        param_application_id = validate_path_param("application_id", application_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/applications/{param_application_id}",
        )

        self._throw_on_error(res)

    async def list_groups(
        self,
        *,
        order_by: Optional[ListGroupsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        application_ids: Optional[list[str]] = None,
        user_ids: Optional[list[str]] = None,
        group_ids: Optional[list[str]] = None,
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

            result = await api.list_groups()
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

    async def list_groups_all(
        self,
        *,
        order_by: Optional[ListGroupsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        application_ids: Optional[list[str]] = None,
        user_ids: Optional[list[str]] = None,
        group_ids: Optional[list[str]] = None,
        tag: Optional[str] = None,
    ) -> list[Group]:
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
        :return: :class:`list[Group] <list[Group]>`

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
                "tag": tag,
            },
        )

    async def create_group(
        self,
        *,
        description: str,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
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

            result = await api.create_group(
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

    async def get_group(
        self,
        *,
        group_id: str,
    ) -> Group:
        """
        Get a group.
        Retrieve information about a given group, specified by the `group_id` parameter. The group's full details, including `user_ids` and `application_ids` are returned in the response.
        :param group_id: ID of the group.
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = await api.get_group(
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

    async def update_group(
        self,
        *,
        group_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[list[str]] = None,
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

            result = await api.update_group(
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

    async def set_group_members(
        self,
        *,
        group_id: str,
        user_ids: list[str],
        application_ids: list[str],
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

            result = await api.set_group_members(
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

    async def add_group_member(
        self,
        *,
        group_id: str,
        user_id: Optional[str] = None,
        application_id: Optional[str] = None,
    ) -> Group:
        """
        Add a user or an application to a group.
        Add a user or an application to a group. You can specify a `user_id` and `application_id` in the body of your request. Note that you can only add one of each per request.
        :param group_id: ID of the group.
        :param user_id: ID of the user to add.
        One-Of ('member'): at most one of 'user_id', 'application_id' could be set.
        :param application_id: ID of the application to add.
        One-Of ('member'): at most one of 'user_id', 'application_id' could be set.
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = await api.add_group_member(
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

    async def add_group_members(
        self,
        *,
        group_id: str,
        user_ids: Optional[list[str]] = None,
        application_ids: Optional[list[str]] = None,
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

            result = await api.add_group_members(
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

    async def remove_group_member(
        self,
        *,
        group_id: str,
        user_id: Optional[str] = None,
        application_id: Optional[str] = None,
    ) -> Group:
        """
        Remove a user or an application from a group.
        Remove a user or an application from a group. You can specify a `user_id` and `application_id` in the body of your request. Note that you can only remove one of each per request. Removing a user from a group means that any permissions given to them via the group (i.e. from an attached policy) will no longer apply. Be sure you want to remove these permissions from the user before proceeding.
        :param group_id: ID of the group.
        :param user_id: ID of the user to remove.
        One-Of ('member'): at most one of 'user_id', 'application_id' could be set.
        :param application_id: ID of the application to remove.
        One-Of ('member'): at most one of 'user_id', 'application_id' could be set.
        :return: :class:`Group <Group>`

        Usage:
        ::

            result = await api.remove_group_member(
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

    async def delete_group(
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

            result = await api.delete_group(
                group_id="example",
            )
        """

        param_group_id = validate_path_param("group_id", group_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/groups/{param_group_id}",
        )

        self._throw_on_error(res)

    async def list_policies(
        self,
        *,
        order_by: Optional[ListPoliciesRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        editable: Optional[bool] = None,
        user_ids: Optional[list[str]] = None,
        group_ids: Optional[list[str]] = None,
        application_ids: Optional[list[str]] = None,
        no_principal: Optional[bool] = None,
        policy_name: Optional[str] = None,
        tag: Optional[str] = None,
        policy_ids: Optional[list[str]] = None,
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

            result = await api.list_policies()
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

    async def list_policies_all(
        self,
        *,
        order_by: Optional[ListPoliciesRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        editable: Optional[bool] = None,
        user_ids: Optional[list[str]] = None,
        group_ids: Optional[list[str]] = None,
        application_ids: Optional[list[str]] = None,
        no_principal: Optional[bool] = None,
        policy_name: Optional[str] = None,
        tag: Optional[str] = None,
        policy_ids: Optional[list[str]] = None,
    ) -> list[Policy]:
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
        :return: :class:`list[Policy] <list[Policy]>`

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
                "tag": tag,
                "policy_ids": policy_ids,
            },
        )

    async def create_policy(
        self,
        *,
        description: str,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        rules: Optional[list[RuleSpecs]] = None,
        tags: Optional[list[str]] = None,
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

            result = await api.create_policy(
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

    async def get_policy(
        self,
        *,
        policy_id: str,
    ) -> Policy:
        """
        Get an existing policy.
        Retrieve information about a policy, specified by the `policy_id` parameter. The policy's full details, including `id`, `name`, `organization_id`, `nb_rules` and `nb_scopes`, `nb_permission_sets` are returned in the response.
        :param policy_id: Id of policy to search.
        :return: :class:`Policy <Policy>`

        Usage:
        ::

            result = await api.get_policy(
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

    async def update_policy(
        self,
        *,
        policy_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[list[str]] = None,
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

            result = await api.update_policy(
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

    async def delete_policy(
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

            result = await api.delete_policy(
                policy_id="example",
            )
        """

        param_policy_id = validate_path_param("policy_id", policy_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/policies/{param_policy_id}",
        )

        self._throw_on_error(res)

    async def clone_policy(
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

            result = await api.clone_policy(
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

    async def set_rules(
        self,
        *,
        policy_id: str,
        rules: list[RuleSpecs],
    ) -> SetRulesResponse:
        """
        Set rules of a given policy.
        Overwrite the rules of a given policy. Any information that you add using this command will overwrite the previous configuration. If you include some of the rules you already had in your previous configuration in your new one, but you change their order, the new order of display will apply. While policy rules are ordered, they have no impact on the access logic of IAM because rules are allow-only.
        :param policy_id: Id of policy to update.
        :param rules: Rules of the policy to set.
        :return: :class:`SetRulesResponse <SetRulesResponse>`

        Usage:
        ::

            result = await api.set_rules(
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

    async def list_rules(
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

            result = await api.list_rules(
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

    async def list_rules_all(
        self,
        *,
        policy_id: str,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> list[Rule]:
        """
        List rules of a given policy.
        List the rules of a given policy. By default, the rules listed are ordered by creation date in ascending order. This can be modified via the `order_by` field. You must define the `policy_id` in the query path of your request.
        :param policy_id: Id of policy to search.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater than 1.
        :return: :class:`list[Rule] <list[Rule]>`

        Usage:
        ::

            result = await api.list_rules_all(
                policy_id="example",
            )
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

            result = await api.list_permission_sets()
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

    async def list_permission_sets_all(
        self,
        *,
        order_by: Optional[ListPermissionSetsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
    ) -> list[PermissionSet]:
        """
        List permission sets.
        List permission sets available for given Organization. You must define the `organization_id` in the query path of your request.
        :param order_by: Criteria for sorting results.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater than 1.
        :param organization_id: Filter by Organization ID.
        :return: :class:`list[PermissionSet] <list[PermissionSet]>`

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
        access_keys: Optional[list[str]] = None,
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

            result = await api.list_api_keys()
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
        expired: Optional[bool] = None,
        access_key: Optional[str] = None,
        description: Optional[str] = None,
        bearer_id: Optional[str] = None,
        bearer_type: Optional[BearerType] = None,
        access_keys: Optional[list[str]] = None,
    ) -> list[APIKey]:
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
        :return: :class:`list[APIKey] <list[APIKey]>`

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
        Create an API key.
        Create an API key. You must specify the `application_id` or the `user_id` and the description. You can also specify the `default_project_id`, which is the Project ID of your preferred Project, to use with Object Storage. The `access_key` and `secret_key` values are returned in the response. Note that the secret key is only shown once. Make sure that you copy and store both keys somewhere safe.
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

            result = await api.create_api_key(
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

    async def get_api_key(
        self,
        *,
        access_key: str,
    ) -> APIKey:
        """
        Get an API key.
        Retrieve information about an API key, specified by the `access_key` parameter. The API key's details, including either the `user_id` or `application_id` of its bearer are returned in the response. Note that the string value for the `secret_key` is nullable, and therefore is not displayed in the response. The `secret_key` value is only displayed upon API key creation.
        :param access_key: Access key to search for.
        :return: :class:`APIKey <APIKey>`

        Usage:
        ::

            result = await api.get_api_key(
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

    async def update_api_key(
        self,
        *,
        access_key: str,
        default_project_id: Optional[str] = None,
        description: Optional[str] = None,
        expires_at: Optional[datetime] = None,
    ) -> APIKey:
        """
        Update an API key.
        Update the parameters of an API key, including `default_project_id` and `description`.
        :param access_key: Access key to update.
        :param default_project_id: New default Project ID to set.
        :param description: New description to update.
        :param expires_at: New expiration date of the API key.
        :return: :class:`APIKey <APIKey>`

        Usage:
        ::

            result = await api.update_api_key(
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
                    expires_at=expires_at,
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
    ) -> None:
        """
        Delete an API key.
        Delete an API key. Note that this action is irreversible and cannot be undone. Make sure you update any configurations using the API keys you delete.
        :param access_key: Access key to delete.

        Usage:
        ::

            result = await api.delete_api_key(
                access_key="example",
            )
        """

        param_access_key = validate_path_param("access_key", access_key)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/api-keys/{param_access_key}",
        )

        self._throw_on_error(res)

    async def list_quota(
        self,
        *,
        order_by: Optional[ListQuotaRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        quotum_names: Optional[list[str]] = None,
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

            result = await api.list_quota()
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

    async def list_quota_all(
        self,
        *,
        order_by: Optional[ListQuotaRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        quotum_names: Optional[list[str]] = None,
    ) -> list[Quotum]:
        """
        List all quotas in the Organization.
        List all product and features quota for an Organization, with their associated limits. By default, the quota listed are ordered by creation date in ascending order. This can be modified via the `order_by` field. You must define the `organization_id` in the query path of your request.
        :param order_by: Criteria for sorting results.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater than 1.
        :param organization_id: Filter by Organization ID.
        :param quotum_names: List of quotum names to filter from.
        :return: :class:`list[Quotum] <list[Quotum]>`

        Usage:
        ::

            result = await api.list_quota_all()
        """

        return await fetch_all_pages_async(
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

    async def get_quotum(
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

            result = await api.get_quotum(
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

    async def list_jw_ts(
        self,
        *,
        audience_id: str,
        order_by: Optional[ListJWTsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        expired: Optional[bool] = None,
    ) -> ListJWTsResponse:
        """
        List JWTs.
        :param audience_id: ID of the user to search.
        :param order_by: Criteria for sorting results.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater to 1.
        :param expired: Filter out expired JWTs or not.
        :return: :class:`ListJWTsResponse <ListJWTsResponse>`

        Usage:
        ::

            result = await api.list_jw_ts(
                audience_id="example",
            )
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

    async def list_jw_ts_all(
        self,
        *,
        audience_id: str,
        order_by: Optional[ListJWTsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        expired: Optional[bool] = None,
    ) -> list[JWT]:
        """
        List JWTs.
        :param audience_id: ID of the user to search.
        :param order_by: Criteria for sorting results.
        :param page_size: Number of results per page. Value must be between 1 and 100.
        :param page: Page number. Value must be greater to 1.
        :param expired: Filter out expired JWTs or not.
        :return: :class:`list[JWT] <list[JWT]>`

        Usage:
        ::

            result = await api.list_jw_ts_all(
                audience_id="example",
            )
        """

        return await fetch_all_pages_async(
            type=ListJWTsResponse,
            key="jwts",
            fetcher=self.list_jw_ts,
            args={
                "audience_id": audience_id,
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
                "expired": expired,
            },
        )

    async def create_jwt(
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

            result = await api.create_jwt(
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

    async def get_jwt(
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

            result = await api.get_jwt(
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

    async def delete_jwt(
        self,
        *,
        jti: str,
    ) -> None:
        """
        Delete a JWT.
        :param jti: JWT ID of the JWT to delete.

        Usage:
        ::

            result = await api.delete_jwt(
                jti="example",
            )
        """

        param_jti = validate_path_param("jti", jti)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/jwts/{param_jti}",
        )

        self._throw_on_error(res)

    async def list_logs(
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

            result = await api.list_logs()
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

    async def list_logs_all(
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
    ) -> list[Log]:
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
        :return: :class:`list[Log] <list[Log]>`

        Usage:
        ::

            result = await api.list_logs_all()
        """

        return await fetch_all_pages_async(
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

    async def get_log(
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

            result = await api.get_log(
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

    async def get_organization_security_settings(
        self,
        *,
        organization_id: Optional[str] = None,
    ) -> OrganizationSecuritySettings:
        """
        Get security settings of an Organization.
        Retrieve information about the security settings of an Organization, specified by the `organization_id` parameter.
        :param organization_id: ID of the Organization.
        :return: :class:`OrganizationSecuritySettings <OrganizationSecuritySettings>`

        Usage:
        ::

            result = await api.get_organization_security_settings()
        """

        param_organization_id = validate_path_param(
            "organization_id", organization_id or self.client.default_organization_id
        )

        res = self._request(
            "GET",
            f"/iam/v1alpha1/organizations/{param_organization_id}/security-settings",
        )

        self._throw_on_error(res)
        return unmarshal_OrganizationSecuritySettings(res.json())

    async def update_organization_security_settings(
        self,
        *,
        organization_id: Optional[str] = None,
        enforce_password_renewal: Optional[bool] = None,
        grace_period_duration: Optional[str] = None,
        login_attempts_before_locked: Optional[int] = None,
        max_login_session_duration: Optional[str] = None,
        max_api_key_expiration_duration: Optional[str] = None,
    ) -> OrganizationSecuritySettings:
        """
        Update the security settings of an Organization.
        :param organization_id: ID of the Organization.
        :param enforce_password_renewal: Defines whether password renewal is enforced during first login.
        :param grace_period_duration: Duration of the grace period to renew password or enable MFA.
        :param login_attempts_before_locked: Number of login attempts before the account is locked.
        :param max_login_session_duration: Maximum duration a login session will stay active before needing to relogin.
        :param max_api_key_expiration_duration: Maximum duration the `expires_at` field of an API key can represent. A value of 0 means there is no maximum duration.
        :return: :class:`OrganizationSecuritySettings <OrganizationSecuritySettings>`

        Usage:
        ::

            result = await api.update_organization_security_settings()
        """

        param_organization_id = validate_path_param(
            "organization_id", organization_id or self.client.default_organization_id
        )

        res = self._request(
            "PATCH",
            f"/iam/v1alpha1/organizations/{param_organization_id}/security-settings",
            body=marshal_UpdateOrganizationSecuritySettingsRequest(
                UpdateOrganizationSecuritySettingsRequest(
                    organization_id=organization_id,
                    enforce_password_renewal=enforce_password_renewal,
                    grace_period_duration=grace_period_duration,
                    login_attempts_before_locked=login_attempts_before_locked,
                    max_login_session_duration=max_login_session_duration,
                    max_api_key_expiration_duration=max_api_key_expiration_duration,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_OrganizationSecuritySettings(res.json())

    async def set_organization_alias(
        self,
        *,
        alias: str,
        organization_id: Optional[str] = None,
    ) -> Organization:
        """
        Set your Organization's alias.
        This will fail if an alias has already been defined. Please contact support if you need to change your Organization's alias.
        :param alias: Alias of the Organization.
        :param organization_id: ID of the Organization.
        :return: :class:`Organization <Organization>`

        Usage:
        ::

            result = await api.set_organization_alias(
                alias="example",
            )
        """

        param_organization_id = validate_path_param(
            "organization_id", organization_id or self.client.default_organization_id
        )

        res = self._request(
            "PUT",
            f"/iam/v1alpha1/organizations/{param_organization_id}/alias",
            body=marshal_SetOrganizationAliasRequest(
                SetOrganizationAliasRequest(
                    alias=alias,
                    organization_id=organization_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Organization(res.json())

    async def get_organization(
        self,
        *,
        organization_id: Optional[str] = None,
    ) -> Organization:
        """
        Get your Organization's IAM information.
        :param organization_id: ID of the Organization.
        :return: :class:`Organization <Organization>`

        Usage:
        ::

            result = await api.get_organization()
        """

        param_organization_id = validate_path_param(
            "organization_id", organization_id or self.client.default_organization_id
        )

        res = self._request(
            "GET",
            f"/iam/v1alpha1/organizations/{param_organization_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Organization(res.json())

    async def update_organization_login_methods(
        self,
        *,
        organization_id: Optional[str] = None,
        login_password_enabled: Optional[bool] = None,
        login_oauth2_enabled: Optional[bool] = None,
        login_magic_code_enabled: Optional[bool] = None,
        login_saml_enabled: Optional[bool] = None,
    ) -> Organization:
        """
        Set your Organization's allowed login methods.
        :param organization_id: ID of the Organization.
        :param login_password_enabled: Defines whether login with a password is enabled for the Organization.
        :param login_oauth2_enabled: Defines whether login through OAuth2 is enabled for the Organization.
        :param login_magic_code_enabled: Defines whether login with an authentication code is enabled for the Organization.
        :param login_saml_enabled: Defines whether login through SAML is enabled for the Organization.
        :return: :class:`Organization <Organization>`

        Usage:
        ::

            result = await api.update_organization_login_methods()
        """

        param_organization_id = validate_path_param(
            "organization_id", organization_id or self.client.default_organization_id
        )

        res = self._request(
            "PATCH",
            f"/iam/v1alpha1/organizations/{param_organization_id}/login-methods",
            body=marshal_UpdateOrganizationLoginMethodsRequest(
                UpdateOrganizationLoginMethodsRequest(
                    organization_id=organization_id,
                    login_password_enabled=login_password_enabled,
                    login_oauth2_enabled=login_oauth2_enabled,
                    login_magic_code_enabled=login_magic_code_enabled,
                    login_saml_enabled=login_saml_enabled,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Organization(res.json())

    async def get_organization_saml(
        self,
        *,
        organization_id: Optional[str] = None,
    ) -> Saml:
        """
        Get SAML Identity Provider configuration of an Organization.
        :param organization_id: ID of the Organization.
        :return: :class:`Saml <Saml>`

        Usage:
        ::

            result = await api.get_organization_saml()
        """

        param_organization_id = validate_path_param(
            "organization_id", organization_id or self.client.default_organization_id
        )

        res = self._request(
            "GET",
            f"/iam/v1alpha1/organizations/{param_organization_id}/saml",
        )

        self._throw_on_error(res)
        return unmarshal_Saml(res.json())

    async def enable_organization_saml(
        self,
        *,
        organization_id: Optional[str] = None,
    ) -> Saml:
        """
        Enable SAML Identity Provider for an Organization.
        :param organization_id: ID of the Organization.
        :return: :class:`Saml <Saml>`

        Usage:
        ::

            result = await api.enable_organization_saml()
        """

        param_organization_id = validate_path_param(
            "organization_id", organization_id or self.client.default_organization_id
        )

        res = self._request(
            "POST",
            f"/iam/v1alpha1/organizations/{param_organization_id}/saml",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Saml(res.json())

    async def update_saml(
        self,
        *,
        saml_id: str,
        entity_id: Optional[str] = None,
        single_sign_on_url: Optional[str] = None,
    ) -> Saml:
        """
        Update SAML Identity Provider configuration.
        :param saml_id: ID of the SAML configuration.
        :param entity_id: Entity ID of the SAML Identity Provider.
        :param single_sign_on_url: Single Sign-On URL of the SAML Identity Provider.
        :return: :class:`Saml <Saml>`

        Usage:
        ::

            result = await api.update_saml(
                saml_id="example",
            )
        """

        param_saml_id = validate_path_param("saml_id", saml_id)

        res = self._request(
            "PATCH",
            f"/iam/v1alpha1/saml/{param_saml_id}",
            body=marshal_UpdateSamlRequest(
                UpdateSamlRequest(
                    saml_id=saml_id,
                    entity_id=entity_id,
                    single_sign_on_url=single_sign_on_url,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Saml(res.json())

    async def delete_saml(
        self,
        *,
        saml_id: str,
    ) -> None:
        """
        Disable SAML Identity Provider for an Organization.
        :param saml_id: ID of the SAML configuration.

        Usage:
        ::

            result = await api.delete_saml(
                saml_id="example",
            )
        """

        param_saml_id = validate_path_param("saml_id", saml_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/saml/{param_saml_id}",
        )

        self._throw_on_error(res)

    async def parse_saml_metadata(
        self,
        *,
        file: ScwFile,
    ) -> ParseSamlMetadataResponse:
        """
        Parse SAML xml metadata file.
        :param file:
        :return: :class:`ParseSamlMetadataResponse <ParseSamlMetadataResponse>`

        Usage:
        ::

            result = await api.parse_saml_metadata(
                file=,
            )
        """

        res = self._request(
            "POST",
            "/iam/v1alpha1/parse-saml-metadata",
            body=marshal_ParseSamlMetadataRequest(
                ParseSamlMetadataRequest(
                    file=file,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ParseSamlMetadataResponse(res.json())

    async def list_saml_certificates(
        self,
        *,
        saml_id: str,
    ) -> ListSamlCertificatesResponse:
        """
        List SAML certificates.
        :param saml_id: ID of the SAML configuration.
        :return: :class:`ListSamlCertificatesResponse <ListSamlCertificatesResponse>`

        Usage:
        ::

            result = await api.list_saml_certificates(
                saml_id="example",
            )
        """

        param_saml_id = validate_path_param("saml_id", saml_id)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/saml/{param_saml_id}/certificates",
        )

        self._throw_on_error(res)
        return unmarshal_ListSamlCertificatesResponse(res.json())

    async def add_saml_certificate(
        self,
        *,
        saml_id: str,
        type_: SamlCertificateType,
        content: str,
    ) -> SamlCertificate:
        """
        Add a SAML certificate.
        :param saml_id: ID of the SAML configuration.
        :param type_: Type of the SAML certificate.
        :param content: Content of the SAML certificate.
        :return: :class:`SamlCertificate <SamlCertificate>`

        Usage:
        ::

            result = await api.add_saml_certificate(
                saml_id="example",
                type=SamlCertificateType.unknown_certificate_type,
                content="example",
            )
        """

        param_saml_id = validate_path_param("saml_id", saml_id)

        res = self._request(
            "POST",
            f"/iam/v1alpha1/saml/{param_saml_id}/certificates",
            body=marshal_AddSamlCertificateRequest(
                AddSamlCertificateRequest(
                    saml_id=saml_id,
                    type_=type_,
                    content=content,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SamlCertificate(res.json())

    async def delete_saml_certificate(
        self,
        *,
        certificate_id: str,
    ) -> None:
        """
        Delete a SAML certificate.
        :param certificate_id: ID of the certificate to delete.

        Usage:
        ::

            result = await api.delete_saml_certificate(
                certificate_id="example",
            )
        """

        param_certificate_id = validate_path_param("certificate_id", certificate_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/saml-certificates/{param_certificate_id}",
        )

        self._throw_on_error(res)

    async def get_organization_scim(
        self,
        *,
        organization_id: Optional[str] = None,
    ) -> Scim:
        """
        Get SCIM configuration of an Organization.
        :param organization_id:
        :return: :class:`Scim <Scim>`

        Usage:
        ::

            result = await api.get_organization_scim()
        """

        param_organization_id = validate_path_param(
            "organization_id", organization_id or self.client.default_organization_id
        )

        res = self._request(
            "GET",
            f"/iam/v1alpha1/organizations/{param_organization_id}/scim",
        )

        self._throw_on_error(res)
        return unmarshal_Scim(res.json())

    async def enable_organization_scim(
        self,
        *,
        organization_id: Optional[str] = None,
    ) -> Scim:
        """
        Enable SCIM for an Organization.
        :param organization_id: ID of the Organization.
        :return: :class:`Scim <Scim>`

        Usage:
        ::

            result = await api.enable_organization_scim()
        """

        param_organization_id = validate_path_param(
            "organization_id", organization_id or self.client.default_organization_id
        )

        res = self._request(
            "POST",
            f"/iam/v1alpha1/organizations/{param_organization_id}/scim",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Scim(res.json())

    async def delete_scim(
        self,
        *,
        scim_id: str,
    ) -> None:
        """
        Disable SCIM for an Organization.
        :param scim_id: ID of the SCIM configuration.

        Usage:
        ::

            result = await api.delete_scim(
                scim_id="example",
            )
        """

        param_scim_id = validate_path_param("scim_id", scim_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/scim/{param_scim_id}",
        )

        self._throw_on_error(res)

    async def list_scim_tokens(
        self,
        *,
        scim_id: str,
        order_by: Optional[ListScimTokensRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListScimTokensResponse:
        """
        List SCIM tokens.
        :param scim_id: ID of the SCIM configuration.
        :param order_by: Sort order of SCIM tokens.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Number of items per page. Value must be between 1 and 100.
        :return: :class:`ListScimTokensResponse <ListScimTokensResponse>`

        Usage:
        ::

            result = await api.list_scim_tokens(
                scim_id="example",
            )
        """

        param_scim_id = validate_path_param("scim_id", scim_id)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/scim/{param_scim_id}/tokens",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListScimTokensResponse(res.json())

    async def list_scim_tokens_all(
        self,
        *,
        scim_id: str,
        order_by: Optional[ListScimTokensRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[ScimToken]:
        """
        List SCIM tokens.
        :param scim_id: ID of the SCIM configuration.
        :param order_by: Sort order of SCIM tokens.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Number of items per page. Value must be between 1 and 100.
        :return: :class:`list[ScimToken] <list[ScimToken]>`

        Usage:
        ::

            result = await api.list_scim_tokens_all(
                scim_id="example",
            )
        """

        return await fetch_all_pages_async(
            type=ListScimTokensResponse,
            key="scim_tokens",
            fetcher=self.list_scim_tokens,
            args={
                "scim_id": scim_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    async def create_scim_token(
        self,
        *,
        scim_id: str,
    ) -> CreateScimTokenResponse:
        """
        Create a SCIM token.
        :param scim_id: ID of the SCIM configuration.
        :return: :class:`CreateScimTokenResponse <CreateScimTokenResponse>`

        Usage:
        ::

            result = await api.create_scim_token(
                scim_id="example",
            )
        """

        param_scim_id = validate_path_param("scim_id", scim_id)

        res = self._request(
            "POST",
            f"/iam/v1alpha1/scim/{param_scim_id}/tokens",
        )

        self._throw_on_error(res)
        return unmarshal_CreateScimTokenResponse(res.json())

    async def delete_scim_token(
        self,
        *,
        token_id: str,
    ) -> None:
        """
        Delete a SCIM token.
        :param token_id: The SCIM token ID.

        Usage:
        ::

            result = await api.delete_scim_token(
                token_id="example",
            )
        """

        param_token_id = validate_path_param("token_id", token_id)

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/scim-tokens/{param_token_id}",
        )

        self._throw_on_error(res)

    async def start_user_web_authn_registration(
        self,
        *,
        user_id: str,
        origin: str,
    ) -> StartUserWebAuthnRegistrationResponse:
        """
        Start registering a WebAuthn authenticator.
        :param user_id: The ID of the user on which to start registering a WebAuthn authenticator.
        :param origin: The URL from which the registration request originated.
        :return: :class:`StartUserWebAuthnRegistrationResponse <StartUserWebAuthnRegistrationResponse>`

        Usage:
        ::

            result = await api.start_user_web_authn_registration(
                user_id="example",
                origin="example",
            )
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "POST",
            f"/iam/v1alpha1/users/{param_user_id}/start-webauthn-registration",
            params={
                "origin": origin,
            },
        )

        self._throw_on_error(res)
        return unmarshal_StartUserWebAuthnRegistrationResponse(res.json())

    async def finish_user_web_authn_registration(
        self,
        *,
        user_id: str,
        ceremony_id: str,
        authenticator_name: str,
        origin: str,
        raw_id: str,
        client_data_json: str,
        authenticator_data: str,
        attestation_object: str,
        public_key: str,
        public_key_algorithm: int,
    ) -> FinishUserWebAuthnRegistrationResponse:
        """
        Complete a WebAuthen authenticator registration.
        :param user_id: The ID of the user on which to finish a webauthn registration.
        :param ceremony_id: The ceremony ID returned by StartUserWebAuthnRegistration.
        :param authenticator_name: Name of the WebAuthn Authenticator to create.
        :param origin: The domain on which the registration is occurring.
        :param raw_id: Unique identifier of the key used by the authenticator.
        :param client_data_json: JSON representation of the client data.
        :param authenticator_data: Data about the authenticator that performed the authentication.
        :param attestation_object: Attestation Object.
        :param public_key: Public key that allows to verify signature.
        :param public_key_algorithm: Algorithm used for the signature (see https://www.iana.org/assignments/cose/cose.xhtml#algorithms).
        :return: :class:`FinishUserWebAuthnRegistrationResponse <FinishUserWebAuthnRegistrationResponse>`

        Usage:
        ::

            result = await api.finish_user_web_authn_registration(
                user_id="example",
                ceremony_id="example",
                authenticator_name="example",
                origin="example",
                raw_id="example",
                client_data_json="example",
                authenticator_data="example",
                attestation_object="example",
                public_key="example",
                public_key_algorithm=1,
            )
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "POST",
            f"/iam/v1alpha1/users/{param_user_id}/finish-webauthn-registration",
            body=marshal_FinishUserWebAuthnRegistrationRequest(
                FinishUserWebAuthnRegistrationRequest(
                    user_id=user_id,
                    ceremony_id=ceremony_id,
                    authenticator_name=authenticator_name,
                    origin=origin,
                    raw_id=raw_id,
                    client_data_json=client_data_json,
                    authenticator_data=authenticator_data,
                    attestation_object=attestation_object,
                    public_key=public_key,
                    public_key_algorithm=public_key_algorithm,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_FinishUserWebAuthnRegistrationResponse(res.json())

    async def list_user_web_authn_authenticators(
        self,
        *,
        order_by: Optional[ListUserWebAuthnAuthenticatorsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        user_id: str,
    ) -> ListUserWebAuthnAuthenticatorsResponse:
        """
        List all of a user's WebAuthn Authenticators.
        :param order_by: Sort order of the Authenticators.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Number of items per page. Value must be between 1 and 100.
        :param user_id: A user ID to filter the authenticators for.
        :return: :class:`ListUserWebAuthnAuthenticatorsResponse <ListUserWebAuthnAuthenticatorsResponse>`

        Usage:
        ::

            result = await api.list_user_web_authn_authenticators(
                user_id="example",
            )
        """

        param_user_id = validate_path_param("user_id", user_id)

        res = self._request(
            "GET",
            f"/iam/v1alpha1/users/{param_user_id}/webauthn-authenticators",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListUserWebAuthnAuthenticatorsResponse(res.json())

    async def list_user_web_authn_authenticators_all(
        self,
        *,
        order_by: Optional[ListUserWebAuthnAuthenticatorsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        user_id: str,
    ) -> list[WebAuthnAuthenticator]:
        """
        List all of a user's WebAuthn Authenticators.
        :param order_by: Sort order of the Authenticators.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Number of items per page. Value must be between 1 and 100.
        :param user_id: A user ID to filter the authenticators for.
        :return: :class:`list[WebAuthnAuthenticator] <list[WebAuthnAuthenticator]>`

        Usage:
        ::

            result = await api.list_user_web_authn_authenticators_all(
                user_id="example",
            )
        """

        return await fetch_all_pages_async(
            type=ListUserWebAuthnAuthenticatorsResponse,
            key="authenticators",
            fetcher=self.list_user_web_authn_authenticators,
            args={
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "user_id": user_id,
            },
        )

    async def update_web_authn_authenticator(
        self,
        *,
        authenticator_id: str,
        authenticator_name: Optional[str] = None,
    ) -> WebAuthnAuthenticator:
        """
        Update a WebAuthn authenticator.
        :param authenticator_id: The ID of the authenticator to update.
        :param authenticator_name: A new name for this authenticator.
        :return: :class:`WebAuthnAuthenticator <WebAuthnAuthenticator>`

        Usage:
        ::

            result = await api.update_web_authn_authenticator(
                authenticator_id="example",
            )
        """

        param_authenticator_id = validate_path_param(
            "authenticator_id", authenticator_id
        )

        res = self._request(
            "PATCH",
            f"/iam/v1alpha1/webauthn-authenticator/{param_authenticator_id}",
            body=marshal_UpdateWebAuthnAuthenticatorRequest(
                UpdateWebAuthnAuthenticatorRequest(
                    authenticator_id=authenticator_id,
                    authenticator_name=authenticator_name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_WebAuthnAuthenticator(res.json())

    async def delete_web_authn_authenticator(
        self,
        *,
        authenticator_id: str,
    ) -> None:
        """
        Delete a WebAuthn authenticator.
        :param authenticator_id:

        Usage:
        ::

            result = await api.delete_web_authn_authenticator(
                authenticator_id="example",
            )
        """

        param_authenticator_id = validate_path_param(
            "authenticator_id", authenticator_id
        )

        res = self._request(
            "DELETE",
            f"/iam/v1alpha1/webauthn-authenticator/{param_authenticator_id}",
            body={},
        )

        self._throw_on_error(res)
