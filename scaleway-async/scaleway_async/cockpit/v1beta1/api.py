# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages_async,
    validate_path_param,
    wait_for_resource_async,
)
from .types import (
    GrafanaUserRole,
    ListGrafanaUsersRequestOrderBy,
    ListTokensRequestOrderBy,
    Cockpit,
    ContactPoint,
    GrafanaUser,
    ListContactPointsResponse,
    ListGrafanaUsersResponse,
    ListTokensResponse,
    Token,
    TokenScopes,
    ActivateCockpitRequest,
    DeactivateCockpitRequest,
    ResetCockpitGrafanaRequest,
    CreateTokenRequest,
    CreateContactPointRequest,
    DeleteContactPointRequest,
    EnableManagedAlertsRequest,
    DisableManagedAlertsRequest,
    TriggerTestAlertRequest,
    CreateGrafanaUserRequest,
    DeleteGrafanaUserRequest,
    ResetGrafanaUserPasswordRequest,
)
from .content import (
    COCKPIT_TRANSIENT_STATUSES,
)
from .marshalling import (
    marshal_ActivateCockpitRequest,
    marshal_CreateContactPointRequest,
    marshal_CreateGrafanaUserRequest,
    marshal_CreateTokenRequest,
    marshal_DeactivateCockpitRequest,
    marshal_DeleteContactPointRequest,
    marshal_DeleteGrafanaUserRequest,
    marshal_DisableManagedAlertsRequest,
    marshal_EnableManagedAlertsRequest,
    marshal_ResetCockpitGrafanaRequest,
    marshal_ResetGrafanaUserPasswordRequest,
    marshal_TriggerTestAlertRequest,
    unmarshal_ContactPoint,
    unmarshal_GrafanaUser,
    unmarshal_Token,
    unmarshal_Cockpit,
    unmarshal_ListContactPointsResponse,
    unmarshal_ListGrafanaUsersResponse,
    unmarshal_ListTokensResponse,
)


class CockpitV1Beta1API(API):
    """
    Cockpit API.

    This API allows to manage Cockpits.
    """

    async def activate_cockpit(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Cockpit:
        """

        Usage:
        ::

            result = await api.activate_cockpit()
        """

        res = self._request(
            "POST",
            f"/cockpit/v1beta1/activate",
            body=marshal_ActivateCockpitRequest(
                ActivateCockpitRequest(
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Cockpit(res.json())

    async def get_cockpit(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Cockpit:
        """
        Get the cockpit associated with the given project ID.
        :param project_id:
        :return: :class:`Cockpit <Cockpit>`

        Usage:
        ::

            result = await api.get_cockpit()
        """

        res = self._request(
            "GET",
            f"/cockpit/v1beta1/cockpit",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_Cockpit(res.json())

    async def wait_for_cockpit(
        self,
        *,
        project_id: Optional[str] = None,
        options: Optional[WaitForOptions[Cockpit, Union[bool, Awaitable[bool]]]] = None,
    ) -> Cockpit:
        """
        Waits for :class:`Cockpit <Cockpit>` to be in a final state.
        :param project_id:
        :param options: The options for the waiter
        :return: :class:`Cockpit <Cockpit>`

        Usage:
        ::

            result = api.wait_for_cockpit()
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in COCKPIT_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_cockpit,
            options=options,
            args={
                "project_id": project_id,
            },
        )

    async def deactivate_cockpit(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Cockpit:
        """

        Usage:
        ::

            result = await api.deactivate_cockpit()
        """

        res = self._request(
            "POST",
            f"/cockpit/v1beta1/deactivate",
            body=marshal_DeactivateCockpitRequest(
                DeactivateCockpitRequest(
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Cockpit(res.json())

    async def reset_cockpit_grafana(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Cockpit:
        """
        Reset the Grafana your cockpit associated with the given project ID.
        :param project_id:
        :return: :class:`Cockpit <Cockpit>`

        Usage:
        ::

            result = await api.reset_cockpit_grafana()
        """

        res = self._request(
            "POST",
            f"/cockpit/v1beta1/reset-grafana",
            body=marshal_ResetCockpitGrafanaRequest(
                ResetCockpitGrafanaRequest(
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Cockpit(res.json())

    async def create_token(
        self,
        *,
        name: str,
        project_id: Optional[str] = None,
        scopes: Optional[TokenScopes] = None,
    ) -> Token:
        """
        Create token associated with the given project ID.
        :param project_id:
        :param name:
        :param scopes:
        :return: :class:`Token <Token>`

        Usage:
        ::

            result = await api.create_token(name="example")
        """

        res = self._request(
            "POST",
            f"/cockpit/v1beta1/tokens",
            body=marshal_CreateTokenRequest(
                CreateTokenRequest(
                    name=name,
                    project_id=project_id,
                    scopes=scopes,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Token(res.json())

    async def list_tokens(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListTokensRequestOrderBy = ListTokensRequestOrderBy.CREATED_AT_ASC,
        project_id: Optional[str] = None,
    ) -> ListTokensResponse:
        """
        List tokens associated with the given project ID.
        :param page:
        :param page_size:
        :param order_by:
        :param project_id:
        :return: :class:`ListTokensResponse <ListTokensResponse>`

        Usage:
        ::

            result = await api.list_tokens()
        """

        res = self._request(
            "GET",
            f"/cockpit/v1beta1/tokens",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListTokensResponse(res.json())

    async def list_tokens_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListTokensRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[Token]:
        """
        List tokens associated with the given project ID.
        :param page:
        :param page_size:
        :param order_by:
        :param project_id:
        :return: :class:`List[ListTokensResponse] <List[ListTokensResponse]>`

        Usage:
        ::

            result = await api.list_tokens_all()
        """

        return await fetch_all_pages_async(
            type=ListTokensResponse,
            key="tokens",
            fetcher=self.list_tokens,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
            },
        )

    async def get_token(
        self,
        *,
        token_id: str,
    ) -> Token:
        """
        Get the token associated with the given ID.
        :param token_id:
        :return: :class:`Token <Token>`

        Usage:
        ::

            result = await api.get_token(token_id="example")
        """

        param_token_id = validate_path_param("token_id", token_id)

        res = self._request(
            "GET",
            f"/cockpit/v1beta1/tokens/{param_token_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Token(res.json())

    async def delete_token(
        self,
        *,
        token_id: str,
    ) -> Optional[None]:
        """
        Delete the token associated with the given ID.
        :param token_id:

        Usage:
        ::

            result = await api.delete_token(token_id="example")
        """

        param_token_id = validate_path_param("token_id", token_id)

        res = self._request(
            "DELETE",
            f"/cockpit/v1beta1/tokens/{param_token_id}",
        )

        self._throw_on_error(res)
        return None

    async def create_contact_point(
        self,
        *,
        project_id: Optional[str] = None,
        contact_point: Optional[ContactPoint] = None,
    ) -> ContactPoint:
        """
        Create an alert contact point for the default receiver.
        :param project_id: Project ID
        :param contact_point: Contact point to create
        :return: :class:`ContactPoint <ContactPoint>`

        Usage:
        ::

            result = await api.create_contact_point()
        """

        res = self._request(
            "POST",
            f"/cockpit/v1beta1/contact-points",
            body=marshal_CreateContactPointRequest(
                CreateContactPointRequest(
                    project_id=project_id,
                    contact_point=contact_point,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ContactPoint(res.json())

    async def list_contact_points(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
    ) -> ListContactPointsResponse:
        """
        List alert contact points associated with the given cockpit ID.
        :param page: Page number
        :param page_size: Page size
        :param project_id: Project ID
        :return: :class:`ListContactPointsResponse <ListContactPointsResponse>`

        Usage:
        ::

            result = await api.list_contact_points()
        """

        res = self._request(
            "GET",
            f"/cockpit/v1beta1/contact-points",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListContactPointsResponse(res.json())

    async def list_contact_points_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
    ) -> List[ContactPoint]:
        """
        List alert contact points associated with the given cockpit ID.
        :param page: Page number
        :param page_size: Page size
        :param project_id: Project ID
        :return: :class:`List[ListContactPointsResponse] <List[ListContactPointsResponse]>`

        Usage:
        ::

            result = await api.list_contact_points_all()
        """

        return await fetch_all_pages_async(
            type=ListContactPointsResponse,
            key="contact_points",
            fetcher=self.list_contact_points,
            args={
                "page": page,
                "page_size": page_size,
                "project_id": project_id,
            },
        )

    async def delete_contact_point(
        self,
        *,
        project_id: Optional[str] = None,
        contact_point: Optional[ContactPoint] = None,
    ) -> Optional[None]:
        """
        Delete an alert contact point for the default receiver.
        :param project_id:
        :param contact_point: Contact point to delete

        Usage:
        ::

            result = await api.delete_contact_point()
        """

        res = self._request(
            "POST",
            f"/cockpit/v1beta1/delete-contact-point",
            body=marshal_DeleteContactPointRequest(
                DeleteContactPointRequest(
                    project_id=project_id,
                    contact_point=contact_point,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return None

    async def enable_managed_alerts(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Optional[None]:
        """
        Enable managed alerts.
        :param project_id:

        Usage:
        ::

            result = await api.enable_managed_alerts()
        """

        res = self._request(
            "POST",
            f"/cockpit/v1beta1/enable-managed-alerts",
            body=marshal_EnableManagedAlertsRequest(
                EnableManagedAlertsRequest(
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return None

    async def disable_managed_alerts(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Optional[None]:
        """
        Disable managed alerts.
        :param project_id:

        Usage:
        ::

            result = await api.disable_managed_alerts()
        """

        res = self._request(
            "POST",
            f"/cockpit/v1beta1/disable-managed-alerts",
            body=marshal_DisableManagedAlertsRequest(
                DisableManagedAlertsRequest(
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return None

    async def trigger_test_alert(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Optional[None]:
        """
        Trigger a test alert to all receivers.
        :param project_id:

        Usage:
        ::

            result = await api.trigger_test_alert()
        """

        res = self._request(
            "POST",
            f"/cockpit/v1beta1/trigger-test-alert",
            body=marshal_TriggerTestAlertRequest(
                TriggerTestAlertRequest(
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return None

    async def create_grafana_user(
        self,
        *,
        login: str,
        role: GrafanaUserRole,
        project_id: Optional[str] = None,
    ) -> GrafanaUser:
        """
        Create a grafana user for your grafana instance.
        :param project_id:
        :param login:
        :param role:
        :return: :class:`GrafanaUser <GrafanaUser>`

        Usage:
        ::

            result = await api.create_grafana_user(
                login="example",
                role=unknown_role,
            )
        """

        res = self._request(
            "POST",
            f"/cockpit/v1beta1/grafana-users",
            body=marshal_CreateGrafanaUserRequest(
                CreateGrafanaUserRequest(
                    login=login,
                    role=role,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_GrafanaUser(res.json())

    async def list_grafana_users(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListGrafanaUsersRequestOrderBy = ListGrafanaUsersRequestOrderBy.LOGIN_ASC,
        project_id: Optional[str] = None,
    ) -> ListGrafanaUsersResponse:
        """
        List grafana users who are able to connect to your grafana instance.
        :param page:
        :param page_size:
        :param order_by:
        :param project_id:
        :return: :class:`ListGrafanaUsersResponse <ListGrafanaUsersResponse>`

        Usage:
        ::

            result = await api.list_grafana_users()
        """

        res = self._request(
            "GET",
            f"/cockpit/v1beta1/grafana-users",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListGrafanaUsersResponse(res.json())

    async def list_grafana_users_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListGrafanaUsersRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[GrafanaUser]:
        """
        List grafana users who are able to connect to your grafana instance.
        :param page:
        :param page_size:
        :param order_by:
        :param project_id:
        :return: :class:`List[ListGrafanaUsersResponse] <List[ListGrafanaUsersResponse]>`

        Usage:
        ::

            result = await api.list_grafana_users_all()
        """

        return await fetch_all_pages_async(
            type=ListGrafanaUsersResponse,
            key="grafana_users",
            fetcher=self.list_grafana_users,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
            },
        )

    async def delete_grafana_user(
        self,
        *,
        grafana_user_id: int,
        project_id: Optional[str] = None,
    ) -> Optional[None]:
        """
        Delete a grafana user from your grafana instance.
        :param grafana_user_id:
        :param project_id:

        Usage:
        ::

            result = await api.delete_grafana_user(grafana_user_id=1)
        """

        param_grafana_user_id = validate_path_param("grafana_user_id", grafana_user_id)

        res = self._request(
            "POST",
            f"/cockpit/v1beta1/grafana-users/{param_grafana_user_id}/delete",
            body=marshal_DeleteGrafanaUserRequest(
                DeleteGrafanaUserRequest(
                    grafana_user_id=grafana_user_id,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return None

    async def reset_grafana_user_password(
        self,
        *,
        grafana_user_id: int,
        project_id: Optional[str] = None,
    ) -> GrafanaUser:
        """
        Reset the Grafana user password from your grafana instance.
        :param grafana_user_id:
        :param project_id:
        :return: :class:`GrafanaUser <GrafanaUser>`

        Usage:
        ::

            result = await api.reset_grafana_user_password(grafana_user_id=1)
        """

        param_grafana_user_id = validate_path_param("grafana_user_id", grafana_user_id)

        res = self._request(
            "POST",
            f"/cockpit/v1beta1/grafana-users/{param_grafana_user_id}/reset-password",
            body=marshal_ResetGrafanaUserPasswordRequest(
                ResetGrafanaUserPasswordRequest(
                    grafana_user_id=grafana_user_id,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_GrafanaUser(res.json())
