# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Awaitable, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.utils import (
    WaitForOptions,
    random_name,
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    DatasourceType,
    GrafanaUserRole,
    ListDatasourcesRequestOrderBy,
    ListGrafanaUsersRequestOrderBy,
    ListPlansRequestOrderBy,
    ListTokensRequestOrderBy,
    ActivateCockpitRequest,
    Cockpit,
    CockpitMetrics,
    ContactPoint,
    CreateContactPointRequest,
    CreateDatasourceRequest,
    CreateGrafanaUserRequest,
    CreateTokenRequest,
    Datasource,
    DeactivateCockpitRequest,
    DeleteContactPointRequest,
    DeleteGrafanaUserRequest,
    DisableManagedAlertsRequest,
    EnableManagedAlertsRequest,
    GrafanaProductDashboard,
    GrafanaUser,
    ListContactPointsResponse,
    ListDatasourcesResponse,
    ListGrafanaProductDashboardsResponse,
    ListGrafanaUsersResponse,
    ListPlansResponse,
    ListTokensResponse,
    Plan,
    ResetGrafanaUserPasswordRequest,
    SelectPlanRequest,
    SelectPlanResponse,
    Token,
    TokenScopes,
    TriggerTestAlertRequest,
)
from .content import (
    COCKPIT_TRANSIENT_STATUSES,
)
from .marshalling import (
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
    marshal_ResetGrafanaUserPasswordRequest,
    marshal_SelectPlanRequest,
    marshal_TriggerTestAlertRequest,
)


class CockpitV1Beta1API(API):
    """
    This API allows you to manage your Scaleway Cockpit, for storing and visualizing metrics and logs.
    """

    async def activate_cockpit(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Cockpit:
        """
        Activate the Cockpit of a given Project specified by the Project ID.
        :param project_id: ID of the Project the Cockpit belongs to.
        :return: :class:`Cockpit <Cockpit>`

        Usage:
        ::

            result = await api.activate_cockpit()
        """

        res = self._request(
            "POST",
            "/cockpit/v1beta1/activate",
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
        Retrieve the Cockpit of a given Project specified by the Project ID.
        :param project_id: ID of the Project the Cockpit belongs to.
        :return: :class:`Cockpit <Cockpit>`

        Usage:
        ::

            result = await api.get_cockpit()
        """

        res = self._request(
            "GET",
            "/cockpit/v1beta1/cockpit",
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
        Retrieve the Cockpit of a given Project specified by the Project ID.
        :param project_id: ID of the Project the Cockpit belongs to.
        :return: :class:`Cockpit <Cockpit>`

        Usage:
        ::

            result = await api.get_cockpit()
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

    async def get_cockpit_metrics(
        self,
        *,
        project_id: Optional[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        metric_name: Optional[str] = None,
    ) -> CockpitMetrics:
        """
        Retrieve metrics from your Cockpit specified by the ID of the Project the Cockpit belongs to.
        :param project_id: ID of the Project the Cockpit belongs to.
        :param start_date: Desired time range's start date for the metrics.
        :param end_date: Desired time range's end date for the metrics.
        :param metric_name: Name of the metric requested.
        :return: :class:`CockpitMetrics <CockpitMetrics>`

        Usage:
        ::

            result = await api.get_cockpit_metrics()
        """

        res = self._request(
            "GET",
            "/cockpit/v1beta1/cockpit/metrics",
            params={
                "end_date": end_date,
                "metric_name": metric_name,
                "project_id": project_id or self.client.default_project_id,
                "start_date": start_date,
            },
        )

        self._throw_on_error(res)
        return unmarshal_CockpitMetrics(res.json())

    async def deactivate_cockpit(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Cockpit:
        """
        Deactivate the Cockpit of a given Project specified by the Project ID.
        :param project_id: ID of the Project the Cockpit belongs to.
        :return: :class:`Cockpit <Cockpit>`

        Usage:
        ::

            result = await api.deactivate_cockpit()
        """

        res = self._request(
            "POST",
            "/cockpit/v1beta1/deactivate",
            body=marshal_DeactivateCockpitRequest(
                DeactivateCockpitRequest(
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Cockpit(res.json())

    async def create_datasource(
        self,
        *,
        name: str,
        is_default: bool,
        project_id: Optional[str] = None,
        type_: Optional[DatasourceType] = None,
    ) -> Datasource:
        """
        Create a data source for a given Project specified by the Project ID and the data source type.
        :param name: Data source name.
        :param is_default: Specifies that the returned output is the default data source per type.
        :param project_id: ID of the Project the Cockpit belongs to.
        :param type_: Data source type.
        :return: :class:`Datasource <Datasource>`

        Usage:
        ::

            result = await api.create_datasource(
                name="example",
                is_default=False,
            )
        """

        res = self._request(
            "POST",
            "/cockpit/v1beta1/datasources",
            body=marshal_CreateDatasourceRequest(
                CreateDatasourceRequest(
                    name=name,
                    is_default=is_default,
                    project_id=project_id,
                    type_=type_,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Datasource(res.json())

    async def delete_datasource(
        self,
        *,
        datasource_id: str,
    ) -> None:
        """
        Delete a given data source specified by the data source ID.
        :param datasource_id: ID of the data source.

        Usage:
        ::

            result = await api.delete_datasource(
                datasource_id="example",
            )
        """

        param_datasource_id = validate_path_param("datasource_id", datasource_id)

        res = self._request(
            "DELETE",
            f"/cockpit/v1beta1/datasources/{param_datasource_id}",
        )

        self._throw_on_error(res)

    async def list_datasources(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDatasourcesRequestOrderBy] = None,
        project_id: Optional[str] = None,
        types: Optional[List[DatasourceType]] = None,
        is_managed_by_scaleway: Optional[bool] = None,
    ) -> ListDatasourcesResponse:
        """
        Get a list of data sources for the specified Project ID.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by: How the response is ordered.
        :param project_id: ID of the Project.
        :param types: Filter by datasource types.
        :param is_managed_by_scaleway: Filter by managed datasources.
        :return: :class:`ListDatasourcesResponse <ListDatasourcesResponse>`

        Usage:
        ::

            result = await api.list_datasources()
        """

        res = self._request(
            "GET",
            "/cockpit/v1beta1/datasources",
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

    async def list_datasources_all(
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
        Get a list of data sources for the specified Project ID.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by: How the response is ordered.
        :param project_id: ID of the Project.
        :param types: Filter by datasource types.
        :param is_managed_by_scaleway: Filter by managed datasources.
        :return: :class:`List[Datasource] <List[Datasource]>`

        Usage:
        ::

            result = await api.list_datasources_all()
        """

        return await fetch_all_pages_async(
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

    async def create_token(
        self,
        *,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        scopes: Optional[TokenScopes] = None,
    ) -> Token:
        """
        Create a token in a given Project specified by the Project ID.
        :param project_id: ID of the Project.
        :param name: Name of the token.
        :param scopes: Token's permissions.
        :return: :class:`Token <Token>`

        Usage:
        ::

            result = await api.create_token()
        """

        res = self._request(
            "POST",
            "/cockpit/v1beta1/tokens",
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

    async def list_tokens(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListTokensRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> ListTokensResponse:
        """
        Get a list of tokens in a given Project specified by the Project ID.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by: How the response is ordered.
        :param project_id: ID of the Project.
        :return: :class:`ListTokensResponse <ListTokensResponse>`

        Usage:
        ::

            result = await api.list_tokens()
        """

        res = self._request(
            "GET",
            "/cockpit/v1beta1/tokens",
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
        Get a list of tokens in a given Project specified by the Project ID.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by: How the response is ordered.
        :param project_id: ID of the Project.
        :return: :class:`List[Token] <List[Token]>`

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
        Retrieve a given token specified by the token ID.
        :param token_id: ID of the token.
        :return: :class:`Token <Token>`

        Usage:
        ::

            result = await api.get_token(
                token_id="example",
            )
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
    ) -> None:
        """
        Delete a given token specified by the token ID.
        :param token_id: ID of the token.

        Usage:
        ::

            result = await api.delete_token(
                token_id="example",
            )
        """

        param_token_id = validate_path_param("token_id", token_id)

        res = self._request(
            "DELETE",
            f"/cockpit/v1beta1/tokens/{param_token_id}",
        )

        self._throw_on_error(res)

    async def create_contact_point(
        self,
        *,
        project_id: Optional[str] = None,
        contact_point: Optional[ContactPoint] = None,
    ) -> ContactPoint:
        """
        Create a contact point associated with the default receiver, to receive alerts.
        :param project_id: ID of the Project in which to create the contact point.
        :param contact_point: Contact point to create.
        :return: :class:`ContactPoint <ContactPoint>`

        Usage:
        ::

            result = await api.create_contact_point()
        """

        res = self._request(
            "POST",
            "/cockpit/v1beta1/contact-points",
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
        Get a list of contact points created for a given Cockpit, specified by the ID of the Project the Cockpit belongs to.
        :param page: Page number.
        :param page_size: Page size.
        :param project_id: ID of the Project from which to list the contact points.
        :return: :class:`ListContactPointsResponse <ListContactPointsResponse>`

        Usage:
        ::

            result = await api.list_contact_points()
        """

        res = self._request(
            "GET",
            "/cockpit/v1beta1/contact-points",
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
        Get a list of contact points created for a given Cockpit, specified by the ID of the Project the Cockpit belongs to.
        :param page: Page number.
        :param page_size: Page size.
        :param project_id: ID of the Project from which to list the contact points.
        :return: :class:`List[ContactPoint] <List[ContactPoint]>`

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
    ) -> None:
        """
        Delete a contact point associated with the default receiver.
        :param project_id: ID of the Project.
        :param contact_point: Contact point to delete.

        Usage:
        ::

            result = await api.delete_contact_point()
        """

        res = self._request(
            "POST",
            "/cockpit/v1beta1/delete-contact-point",
            body=marshal_DeleteContactPointRequest(
                DeleteContactPointRequest(
                    project_id=project_id,
                    contact_point=contact_point,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def enable_managed_alerts(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> None:
        """
        Enable the sending of managed alerts for a given Cockpit, specified by the ID of the Project the Cockpit belongs to.
        :param project_id: ID of the Project.

        Usage:
        ::

            result = await api.enable_managed_alerts()
        """

        res = self._request(
            "POST",
            "/cockpit/v1beta1/enable-managed-alerts",
            body=marshal_EnableManagedAlertsRequest(
                EnableManagedAlertsRequest(
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def disable_managed_alerts(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> None:
        """
        Disable the sending of managed alerts for a given Cockpit, specified by the ID of the Project the Cockpit belongs to.
        :param project_id: ID of the Project.

        Usage:
        ::

            result = await api.disable_managed_alerts()
        """

        res = self._request(
            "POST",
            "/cockpit/v1beta1/disable-managed-alerts",
            body=marshal_DisableManagedAlertsRequest(
                DisableManagedAlertsRequest(
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def trigger_test_alert(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> None:
        """
        Send a test alert to make sure your contact points get notified when an actual alert is triggered.
        :param project_id:

        Usage:
        ::

            result = await api.trigger_test_alert()
        """

        res = self._request(
            "POST",
            "/cockpit/v1beta1/trigger-test-alert",
            body=marshal_TriggerTestAlertRequest(
                TriggerTestAlertRequest(
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def create_grafana_user(
        self,
        *,
        login: str,
        project_id: Optional[str] = None,
        role: Optional[GrafanaUserRole] = None,
    ) -> GrafanaUser:
        """
        Create a Grafana user for your Cockpit's Grafana. Make sure you save the automatically-generated password and the Grafana user ID.
        :param login: Username of the Grafana user.
        :param project_id: ID of the Project.
        :param role: Role assigned to the Grafana user.
        :return: :class:`GrafanaUser <GrafanaUser>`

        Usage:
        ::

            result = await api.create_grafana_user(
                login="example",
            )
        """

        res = self._request(
            "POST",
            "/cockpit/v1beta1/grafana-users",
            body=marshal_CreateGrafanaUserRequest(
                CreateGrafanaUserRequest(
                    login=login,
                    project_id=project_id,
                    role=role,
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
        order_by: Optional[ListGrafanaUsersRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> ListGrafanaUsersResponse:
        """
        Get a list of all Grafana users created in your Cockpit's Grafana.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by:
        :param project_id: ID of the Project.
        :return: :class:`ListGrafanaUsersResponse <ListGrafanaUsersResponse>`

        Usage:
        ::

            result = await api.list_grafana_users()
        """

        res = self._request(
            "GET",
            "/cockpit/v1beta1/grafana-users",
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
        Get a list of all Grafana users created in your Cockpit's Grafana.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by:
        :param project_id: ID of the Project.
        :return: :class:`List[GrafanaUser] <List[GrafanaUser]>`

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
        project_id: Optional[str] = None,
        grafana_user_id: int,
    ) -> None:
        """
        Delete a Grafana user from your Cockpit's Grafana, specified by the ID of the Project the Cockpit belongs to, and the ID of the Grafana user.
        :param project_id: ID of the Project.
        :param grafana_user_id: ID of the Grafana user.

        Usage:
        ::

            result = await api.delete_grafana_user(
                grafana_user_id=1,
            )
        """

        param_grafana_user_id = validate_path_param("grafana_user_id", grafana_user_id)

        res = self._request(
            "POST",
            f"/cockpit/v1beta1/grafana-users/{param_grafana_user_id}/delete",
            body=marshal_DeleteGrafanaUserRequest(
                DeleteGrafanaUserRequest(
                    project_id=project_id,
                    grafana_user_id=grafana_user_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def reset_grafana_user_password(
        self,
        *,
        project_id: Optional[str] = None,
        grafana_user_id: int,
    ) -> GrafanaUser:
        """
        Reset the password of a Grafana user, specified by the ID of the Project the Cockpit belongs to, and the ID of the Grafana user.
        :param project_id: ID of the Project.
        :param grafana_user_id: ID of the Grafana user.
        :return: :class:`GrafanaUser <GrafanaUser>`

        Usage:
        ::

            result = await api.reset_grafana_user_password(
                grafana_user_id=1,
            )
        """

        param_grafana_user_id = validate_path_param("grafana_user_id", grafana_user_id)

        res = self._request(
            "POST",
            f"/cockpit/v1beta1/grafana-users/{param_grafana_user_id}/reset-password",
            body=marshal_ResetGrafanaUserPasswordRequest(
                ResetGrafanaUserPasswordRequest(
                    project_id=project_id,
                    grafana_user_id=grafana_user_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_GrafanaUser(res.json())

    async def list_plans(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListPlansRequestOrderBy] = None,
    ) -> ListPlansResponse:
        """
        Get a list of all pricing plans available.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by:
        :return: :class:`ListPlansResponse <ListPlansResponse>`

        Usage:
        ::

            result = await api.list_plans()
        """

        res = self._request(
            "GET",
            "/cockpit/v1beta1/plans",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPlansResponse(res.json())

    async def list_plans_all(
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
        :return: :class:`List[Plan] <List[Plan]>`

        Usage:
        ::

            result = await api.list_plans_all()
        """

        return await fetch_all_pages_async(
            type=ListPlansResponse,
            key="plans",
            fetcher=self.list_plans,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def select_plan(
        self,
        *,
        plan_id: str,
        project_id: Optional[str] = None,
    ) -> SelectPlanResponse:
        """
        Select your chosen pricing plan for your Cockpit, specifying the Cockpit's Project ID and the pricing plan's ID in the request.
        :param plan_id: ID of the pricing plan.
        :param project_id: ID of the Project.
        :return: :class:`SelectPlanResponse <SelectPlanResponse>`

        Usage:
        ::

            result = await api.select_plan(
                plan_id="example",
            )
        """

        res = self._request(
            "POST",
            "/cockpit/v1beta1/select-plan",
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

    async def list_grafana_product_dashboards(
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

            result = await api.list_grafana_product_dashboards()
        """

        res = self._request(
            "GET",
            "/cockpit/v1beta1/grafana-product-dashboards",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListGrafanaProductDashboardsResponse(res.json())

    async def list_grafana_product_dashboards_all(
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
        :return: :class:`List[GrafanaProductDashboard] <List[GrafanaProductDashboard]>`

        Usage:
        ::

            result = await api.list_grafana_product_dashboards_all()
        """

        return await fetch_all_pages_async(
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

    async def get_grafana_product_dashboard(
        self,
        *,
        project_id: Optional[str] = None,
        dashboard_name: str,
    ) -> GrafanaProductDashboard:
        """
        Get a product dashboard.
        Get a product dashboard specified by the dashboard ID.
        :param project_id: ID of the Project.
        :param dashboard_name: Name of the dashboard.
        :return: :class:`GrafanaProductDashboard <GrafanaProductDashboard>`

        Usage:
        ::

            result = await api.get_grafana_product_dashboard(
                dashboard_name="example",
            )
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
