# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages,
    random_name,
    validate_path_param,
    wait_for_resource,
)
from .types import (
    DatasourceType,
    GrafanaUserRole,
    ListDatasourcesRequestOrderBy,
    ListGrafanaUsersRequestOrderBy,
    ListPlansRequestOrderBy,
    ListTokensRequestOrderBy,
    Cockpit,
    CockpitMetrics,
    ContactPoint,
    Datasource,
    GrafanaProductDashboard,
    GrafanaUser,
    ListContactPointsResponse,
    ListDatasourcesResponse,
    ListGrafanaProductDashboardsResponse,
    ListGrafanaUsersResponse,
    ListPlansResponse,
    ListTokensResponse,
    Plan,
    SelectPlanResponse,
    Token,
    TokenScopes,
    ActivateCockpitRequest,
    DeactivateCockpitRequest,
    ResetCockpitGrafanaRequest,
    CreateDatasourceRequest,
    CreateTokenRequest,
    CreateContactPointRequest,
    DeleteContactPointRequest,
    EnableManagedAlertsRequest,
    DisableManagedAlertsRequest,
    TriggerTestAlertRequest,
    CreateGrafanaUserRequest,
    DeleteGrafanaUserRequest,
    ResetGrafanaUserPasswordRequest,
    SelectPlanRequest,
)
from .content import (
    COCKPIT_TRANSIENT_STATUSES,
)
from .marshalling import (
    marshal_ActivateCockpitRequest,
    marshal_CreateContactPointRequest,
    marshal_CreateDatasourceRequest,
    marshal_CreateGrafanaUserRequest,
    marshal_CreateTokenRequest,
    marshal_DeactivateCockpitRequest,
    marshal_DeleteContactPointRequest,
    marshal_DeleteGrafanaUserRequest,
    marshal_DisableManagedAlertsRequest,
    marshal_EnableManagedAlertsRequest,
    marshal_ResetCockpitGrafanaRequest,
    marshal_ResetGrafanaUserPasswordRequest,
    marshal_SelectPlanRequest,
    marshal_TriggerTestAlertRequest,
    unmarshal_ContactPoint,
    unmarshal_Datasource,
    unmarshal_GrafanaProductDashboard,
    unmarshal_GrafanaUser,
    unmarshal_Token,
    unmarshal_Cockpit,
    unmarshal_CockpitMetrics,
    unmarshal_ListContactPointsResponse,
    unmarshal_ListDatasourcesResponse,
    unmarshal_ListGrafanaProductDashboardsResponse,
    unmarshal_ListGrafanaUsersResponse,
    unmarshal_ListPlansResponse,
    unmarshal_ListTokensResponse,
    unmarshal_SelectPlanResponse,
)


class CockpitV1Beta1API(API):
    """
    Cockpit API.

    Cockpit's API allows you to activate your Cockpit on your Projects. Scaleway's Cockpit stores metrics and logs and provides a dedicated Grafana for dashboarding to visualize them.
    Cockpit API.
    """

    def activate_cockpit(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Cockpit:
        """
        Activate the Cockpit of the specified Project ID.
        :param project_id: ID of the Project the Cockpit belongs to.
        :return: :class:`Cockpit <Cockpit>`

        Usage:
        ::

            result = api.activate_cockpit()
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

    def get_cockpit(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Cockpit:
        """
        Retrieve the Cockpit of the specified Project ID.
        :param project_id: ID of the Project the Cockpit belongs to.
        :return: :class:`Cockpit <Cockpit>`

        Usage:
        ::

            result = api.get_cockpit()
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

    def wait_for_cockpit(
        self,
        *,
        project_id: Optional[str] = None,
        options: Optional[WaitForOptions[Cockpit, bool]] = None,
    ) -> Cockpit:
        """
        Waits for :class:`Cockpit <Cockpit>` to be in a final state.
        :param project_id: ID of the Project the Cockpit belongs to.
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

        return wait_for_resource(
            fetcher=self.get_cockpit,
            options=options,
            args={
                "project_id": project_id,
            },
        )

    def get_cockpit_metrics(
        self,
        *,
        project_id: Optional[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        metric_name: Optional[str] = None,
    ) -> CockpitMetrics:
        """
        Get metrics from your Cockpit with the specified Project ID.
        :param project_id: ID of the Project the Cockpit belongs to.
        :param start_date: Desired time range's start date for the metrics.
        :param end_date: Desired time range's end date for the metrics.
        :param metric_name: Name of the metric requested.
        :return: :class:`CockpitMetrics <CockpitMetrics>`

        Usage:
        ::

            result = api.get_cockpit_metrics()
        """

        res = self._request(
            "GET",
            f"/cockpit/v1beta1/cockpit/metrics",
            params={
                "end_date": end_date,
                "metric_name": metric_name,
                "project_id": project_id or self.client.default_project_id,
                "start_date": start_date,
            },
        )

        self._throw_on_error(res)
        return unmarshal_CockpitMetrics(res.json())

    def deactivate_cockpit(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Cockpit:
        """
        Deactivate the Cockpit of the specified Project ID.
        :param project_id: ID of the Project the Cockpit belongs to.
        :return: :class:`Cockpit <Cockpit>`

        Usage:
        ::

            result = api.deactivate_cockpit()
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

    def reset_cockpit_grafana(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Cockpit:
        """
        Reset your Cockpit's Grafana associated with the specified Project ID.
        :param project_id: ID of the Project the Cockpit belongs to.
        :return: :class:`Cockpit <Cockpit>`

        Usage:
        ::

            result = api.reset_cockpit_grafana()
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

    def create_datasource(
        self,
        *,
        name: str,
        type_: DatasourceType,
        is_default: bool,
        project_id: Optional[str] = None,
    ) -> Datasource:
        """
        Create a datasource for the specified Project ID and the given type.
        :param project_id: ID of the Project the Cockpit belongs to.
        :param name: Datasource name.
        :param type_: Datasource type.
        :param is_default: Specifies that the returned output is the default datasource per type.
        :return: :class:`Datasource <Datasource>`

        Usage:
        ::

            result = api.create_datasource(
                name="example",
                type_=unknown_datasource_type,
                is_default=True,
            )
        """

        res = self._request(
            "POST",
            f"/cockpit/v1beta1/datasources",
            body=marshal_CreateDatasourceRequest(
                CreateDatasourceRequest(
                    name=name,
                    type_=type_,
                    is_default=is_default,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Datasource(res.json())

    def list_datasources(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListDatasourcesRequestOrderBy = ListDatasourcesRequestOrderBy.CREATED_AT_ASC,
        project_id: Optional[str] = None,
        types: Optional[List[DatasourceType]] = None,
        is_managed_by_scaleway: Optional[bool] = None,
    ) -> ListDatasourcesResponse:
        """
        Get a list of datasources for the specified Project ID.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by: How the response is ordered.
        :param project_id: ID of the Project.
        :param types: Filter by datasource types.
        :param is_managed_by_scaleway: Filter by managed datasources.
        :return: :class:`ListDatasourcesResponse <ListDatasourcesResponse>`

        Usage:
        ::

            result = api.list_datasources()
        """

        res = self._request(
            "GET",
            f"/cockpit/v1beta1/datasources",
            params={
                "is_managed_by_scaleway": is_managed_by_scaleway,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "types": types,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDatasourcesResponse(res.json())

    def list_datasources_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDatasourcesRequestOrderBy] = None,
        project_id: Optional[str] = None,
        types: Optional[List[DatasourceType]] = None,
        is_managed_by_scaleway: Optional[bool] = None,
    ) -> List[Datasource]:
        """
        Get a list of datasources for the specified Project ID.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by: How the response is ordered.
        :param project_id: ID of the Project.
        :param types: Filter by datasource types.
        :param is_managed_by_scaleway: Filter by managed datasources.
        :return: :class:`List[ListDatasourcesResponse] <List[ListDatasourcesResponse]>`

        Usage:
        ::

            result = api.list_datasources_all()
        """

        return fetch_all_pages(
            type=ListDatasourcesResponse,
            key="datasources",
            fetcher=self.list_datasources,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
                "types": types,
                "is_managed_by_scaleway": is_managed_by_scaleway,
            },
        )

    def create_token(
        self,
        *,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        scopes: Optional[TokenScopes] = None,
    ) -> Token:
        """
        Create a token associated with the specified Project ID.
        :param project_id: ID of the Project.
        :param name: Name of the token.
        :param scopes: Token's permissions.
        :return: :class:`Token <Token>`

        Usage:
        ::

            result = api.create_token()
        """

        res = self._request(
            "POST",
            f"/cockpit/v1beta1/tokens",
            body=marshal_CreateTokenRequest(
                CreateTokenRequest(
                    project_id=project_id,
                    name=name or random_name(prefix="token"),
                    scopes=scopes,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Token(res.json())

    def list_tokens(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListTokensRequestOrderBy = ListTokensRequestOrderBy.CREATED_AT_ASC,
        project_id: Optional[str] = None,
    ) -> ListTokensResponse:
        """
        Get a list of tokens associated with the specified Project ID.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by: How the response is ordered.
        :param project_id: ID of the Project.
        :return: :class:`ListTokensResponse <ListTokensResponse>`

        Usage:
        ::

            result = api.list_tokens()
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

    def list_tokens_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListTokensRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[Token]:
        """
        Get a list of tokens associated with the specified Project ID.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by: How the response is ordered.
        :param project_id: ID of the Project.
        :return: :class:`List[ListTokensResponse] <List[ListTokensResponse]>`

        Usage:
        ::

            result = api.list_tokens_all()
        """

        return fetch_all_pages(
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

    def get_token(
        self,
        *,
        token_id: str,
    ) -> Token:
        """
        Retrieve the token associated with the specified token ID.
        :param token_id: ID of the token.
        :return: :class:`Token <Token>`

        Usage:
        ::

            result = api.get_token(token_id="example")
        """

        param_token_id = validate_path_param("token_id", token_id)

        res = self._request(
            "GET",
            f"/cockpit/v1beta1/tokens/{param_token_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Token(res.json())

    def delete_token(
        self,
        *,
        token_id: str,
    ) -> Optional[None]:
        """
        Delete the token associated with the specified token ID.
        :param token_id: ID of the token.

        Usage:
        ::

            result = api.delete_token(token_id="example")
        """

        param_token_id = validate_path_param("token_id", token_id)

        res = self._request(
            "DELETE",
            f"/cockpit/v1beta1/tokens/{param_token_id}",
        )

        self._throw_on_error(res)
        return None

    def create_contact_point(
        self,
        *,
        project_id: Optional[str] = None,
        contact_point: Optional[ContactPoint] = None,
    ) -> ContactPoint:
        """
        Create a contact point to receive alerts for the default receiver.
        :param project_id: ID of the Project in which to create the contact point.
        :param contact_point: Contact point to create.
        :return: :class:`ContactPoint <ContactPoint>`

        Usage:
        ::

            result = api.create_contact_point()
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

    def list_contact_points(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
    ) -> ListContactPointsResponse:
        """
        Get a list of contact points for the Cockpit associated with the specified Project ID.
        :param page: Page number.
        :param page_size: Page size.
        :param project_id: ID of the Project from which to list the contact points.
        :return: :class:`ListContactPointsResponse <ListContactPointsResponse>`

        Usage:
        ::

            result = api.list_contact_points()
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

    def list_contact_points_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
    ) -> List[ContactPoint]:
        """
        Get a list of contact points for the Cockpit associated with the specified Project ID.
        :param page: Page number.
        :param page_size: Page size.
        :param project_id: ID of the Project from which to list the contact points.
        :return: :class:`List[ListContactPointsResponse] <List[ListContactPointsResponse]>`

        Usage:
        ::

            result = api.list_contact_points_all()
        """

        return fetch_all_pages(
            type=ListContactPointsResponse,
            key="contact_points",
            fetcher=self.list_contact_points,
            args={
                "page": page,
                "page_size": page_size,
                "project_id": project_id,
            },
        )

    def delete_contact_point(
        self,
        *,
        project_id: Optional[str] = None,
        contact_point: Optional[ContactPoint] = None,
    ) -> Optional[None]:
        """
        Delete a contact point for the default receiver.
        :param project_id: ID of the Project.
        :param contact_point: Contact point to delete.

        Usage:
        ::

            result = api.delete_contact_point()
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

    def enable_managed_alerts(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Optional[None]:
        """
        Enable the sending of managed alerts for the specified Project's Cockpit.
        :param project_id: ID of the Project.

        Usage:
        ::

            result = api.enable_managed_alerts()
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

    def disable_managed_alerts(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Optional[None]:
        """
        Disable the sending of managed alerts for the specified Project's Cockpit.
        :param project_id: ID of the Project.

        Usage:
        ::

            result = api.disable_managed_alerts()
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

    def trigger_test_alert(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Optional[None]:
        """
        Trigger a test alert to all of the Cockpit's receivers.
        :param project_id:

        Usage:
        ::

            result = api.trigger_test_alert()
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

    def create_grafana_user(
        self,
        *,
        login: str,
        role: GrafanaUserRole,
        project_id: Optional[str] = None,
    ) -> GrafanaUser:
        """
        Create a Grafana user for your Cockpit's Grafana instance. Make sure you save the automatically-generated password and the Grafana user ID.
        :param project_id: ID of the Project.
        :param login: Username of the Grafana user.
        :param role: Role assigned to the Grafana user.
        :return: :class:`GrafanaUser <GrafanaUser>`

        Usage:
        ::

            result = api.create_grafana_user(
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

    def list_grafana_users(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListGrafanaUsersRequestOrderBy = ListGrafanaUsersRequestOrderBy.LOGIN_ASC,
        project_id: Optional[str] = None,
    ) -> ListGrafanaUsersResponse:
        """
        Get a list of Grafana users who are able to connect to the Cockpit's Grafana instance.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by:
        :param project_id: ID of the Project.
        :return: :class:`ListGrafanaUsersResponse <ListGrafanaUsersResponse>`

        Usage:
        ::

            result = api.list_grafana_users()
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

    def list_grafana_users_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListGrafanaUsersRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[GrafanaUser]:
        """
        Get a list of Grafana users who are able to connect to the Cockpit's Grafana instance.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by:
        :param project_id: ID of the Project.
        :return: :class:`List[ListGrafanaUsersResponse] <List[ListGrafanaUsersResponse]>`

        Usage:
        ::

            result = api.list_grafana_users_all()
        """

        return fetch_all_pages(
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

    def delete_grafana_user(
        self,
        *,
        grafana_user_id: int,
        project_id: Optional[str] = None,
    ) -> Optional[None]:
        """
        Delete a Grafana user from a Grafana instance, specified by the Cockpit's Project ID and the Grafana user ID.
        :param grafana_user_id: ID of the Grafana user.
        :param project_id: ID of the Project.

        Usage:
        ::

            result = api.delete_grafana_user(grafana_user_id=1)
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

    def reset_grafana_user_password(
        self,
        *,
        grafana_user_id: int,
        project_id: Optional[str] = None,
    ) -> GrafanaUser:
        """
        Reset a Grafana user's password specified by the Cockpit's Project ID and the Grafana user ID.
        :param grafana_user_id: ID of the Grafana user.
        :param project_id: ID of the Project.
        :return: :class:`GrafanaUser <GrafanaUser>`

        Usage:
        ::

            result = api.reset_grafana_user_password(grafana_user_id=1)
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

    def list_plans(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListPlansRequestOrderBy = ListPlansRequestOrderBy.NAME_ASC,
    ) -> ListPlansResponse:
        """
        Get a list of all pricing plans available.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by:
        :return: :class:`ListPlansResponse <ListPlansResponse>`

        Usage:
        ::

            result = api.list_plans()
        """

        res = self._request(
            "GET",
            f"/cockpit/v1beta1/plans",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPlansResponse(res.json())

    def list_plans_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListPlansRequestOrderBy] = None,
    ) -> List[Plan]:
        """
        Get a list of all pricing plans available.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by:
        :return: :class:`List[ListPlansResponse] <List[ListPlansResponse]>`

        Usage:
        ::

            result = api.list_plans_all()
        """

        return fetch_all_pages(
            type=ListPlansResponse,
            key="plans",
            fetcher=self.list_plans,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    def select_plan(
        self,
        *,
        plan_id: str,
        project_id: Optional[str] = None,
    ) -> SelectPlanResponse:
        """
        Select your chosen pricing plan for your Cockpit, specifying the Cockpit's Project ID and the pricing plan's ID in the request.
        :param project_id: ID of the Project.
        :param plan_id: ID of the pricing plan.
        :return: :class:`SelectPlanResponse <SelectPlanResponse>`

        Usage:
        ::

            result = api.select_plan(plan_id="example")
        """

        res = self._request(
            "POST",
            f"/cockpit/v1beta1/select-plan",
            body=marshal_SelectPlanRequest(
                SelectPlanRequest(
                    plan_id=plan_id,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SelectPlanResponse(res.json())

    def list_grafana_product_dashboards(
        self,
        *,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        tags: Optional[List[str]] = None,
    ) -> ListGrafanaProductDashboardsResponse:
        """
        List product dashboards.
        Get a list of available product dashboards.
        :param project_id: ID of the Project.
        :param page: Page number.
        :param page_size: Page size.
        :param tags: Tags to filter the dashboards.
        :return: :class:`ListGrafanaProductDashboardsResponse <ListGrafanaProductDashboardsResponse>`

        Usage:
        ::

            result = api.list_grafana_product_dashboards()
        """

        res = self._request(
            "GET",
            f"/cockpit/v1beta1/grafana-product-dashboards",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListGrafanaProductDashboardsResponse(res.json())

    def list_grafana_product_dashboards_all(
        self,
        *,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        tags: Optional[List[str]] = None,
    ) -> List[GrafanaProductDashboard]:
        """
        List product dashboards.
        Get a list of available product dashboards.
        :param project_id: ID of the Project.
        :param page: Page number.
        :param page_size: Page size.
        :param tags: Tags to filter the dashboards.
        :return: :class:`List[ListGrafanaProductDashboardsResponse] <List[ListGrafanaProductDashboardsResponse]>`

        Usage:
        ::

            result = api.list_grafana_product_dashboards_all()
        """

        return fetch_all_pages(
            type=ListGrafanaProductDashboardsResponse,
            key="dashboards",
            fetcher=self.list_grafana_product_dashboards,
            args={
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
                "tags": tags,
            },
        )

    def get_grafana_product_dashboard(
        self,
        *,
        dashboard_name: str,
        project_id: Optional[str] = None,
    ) -> GrafanaProductDashboard:
        """
        Get a product dashboard.
        Get a product dashboard specified by the dashboard ID.
        :param dashboard_name: Name of the dashboard.
        :param project_id: ID of the Project.
        :return: :class:`GrafanaProductDashboard <GrafanaProductDashboard>`

        Usage:
        ::

            result = api.get_grafana_product_dashboard(dashboard_name="example")
        """

        param_dashboard_name = validate_path_param("dashboard_name", dashboard_name)

        res = self._request(
            "GET",
            f"/cockpit/v1beta1/grafana-product-dashboards/{param_dashboard_name}",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_GrafanaProductDashboard(res.json())
