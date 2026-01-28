# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    WaitForOptions,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
)
from .types import (
    AlertState,
    AlertStatus,
    DataSourceOrigin,
    DataSourceType,
    GrafanaUserRole,
    ListDataSourcesRequestOrderBy,
    ListExportersRequestOrderBy,
    ListGrafanaUsersRequestOrderBy,
    ListPlansRequestOrderBy,
    ListProductsRequestOrderBy,
    ListTokensRequestOrderBy,
    PlanName,
    TokenScope,
    AlertManager,
    ContactPoint,
    ContactPointEmail,
    DataSource,
    DisableAlertRulesResponse,
    EnableAlertRulesResponse,
    Exporter,
    ExporterDatadogDestination,
    ExporterOTLPDestination,
    GetConfigResponse,
    GetRulesCountResponse,
    GlobalApiCreateGrafanaUserRequest,
    GlobalApiResetGrafanaUserPasswordRequest,
    GlobalApiSelectPlanRequest,
    GlobalApiSyncGrafanaDataSourcesRequest,
    Grafana,
    GrafanaProductDashboard,
    GrafanaUser,
    ListAlertsResponse,
    ListContactPointsResponse,
    ListDataSourcesResponse,
    ListExportersResponse,
    ListGrafanaProductDashboardsResponse,
    ListGrafanaUsersResponse,
    ListPlansResponse,
    ListProductsResponse,
    ListTokensResponse,
    Plan,
    Product,
    RegionalApiCreateContactPointRequest,
    RegionalApiCreateDataSourceRequest,
    RegionalApiCreateExporterRequest,
    RegionalApiCreateTokenRequest,
    RegionalApiDeleteContactPointRequest,
    RegionalApiDisableAlertManagerRequest,
    RegionalApiDisableAlertRulesRequest,
    RegionalApiDisableManagedAlertsRequest,
    RegionalApiEnableAlertManagerRequest,
    RegionalApiEnableAlertRulesRequest,
    RegionalApiEnableManagedAlertsRequest,
    RegionalApiTriggerTestAlertRequest,
    RegionalApiUpdateContactPointRequest,
    RegionalApiUpdateDataSourceRequest,
    RegionalApiUpdateExporterRequest,
    Token,
    UsageOverview,
)
from .content import (
    EXPORTER_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_ContactPoint,
    unmarshal_DataSource,
    unmarshal_Exporter,
    unmarshal_GrafanaProductDashboard,
    unmarshal_GrafanaUser,
    unmarshal_Plan,
    unmarshal_Token,
    unmarshal_AlertManager,
    unmarshal_DisableAlertRulesResponse,
    unmarshal_EnableAlertRulesResponse,
    unmarshal_GetConfigResponse,
    unmarshal_GetRulesCountResponse,
    unmarshal_Grafana,
    unmarshal_ListAlertsResponse,
    unmarshal_ListContactPointsResponse,
    unmarshal_ListDataSourcesResponse,
    unmarshal_ListExportersResponse,
    unmarshal_ListGrafanaProductDashboardsResponse,
    unmarshal_ListGrafanaUsersResponse,
    unmarshal_ListPlansResponse,
    unmarshal_ListProductsResponse,
    unmarshal_ListTokensResponse,
    unmarshal_UsageOverview,
    marshal_GlobalApiCreateGrafanaUserRequest,
    marshal_GlobalApiResetGrafanaUserPasswordRequest,
    marshal_GlobalApiSelectPlanRequest,
    marshal_GlobalApiSyncGrafanaDataSourcesRequest,
    marshal_RegionalApiCreateContactPointRequest,
    marshal_RegionalApiCreateDataSourceRequest,
    marshal_RegionalApiCreateExporterRequest,
    marshal_RegionalApiCreateTokenRequest,
    marshal_RegionalApiDeleteContactPointRequest,
    marshal_RegionalApiDisableAlertManagerRequest,
    marshal_RegionalApiDisableAlertRulesRequest,
    marshal_RegionalApiDisableManagedAlertsRequest,
    marshal_RegionalApiEnableAlertManagerRequest,
    marshal_RegionalApiEnableAlertRulesRequest,
    marshal_RegionalApiEnableManagedAlertsRequest,
    marshal_RegionalApiTriggerTestAlertRequest,
    marshal_RegionalApiUpdateContactPointRequest,
    marshal_RegionalApiUpdateDataSourceRequest,
    marshal_RegionalApiUpdateExporterRequest,
)


class CockpitV1GlobalAPI(API):
    """
    The Cockpit Global API allows you to manage your Cockpit's Grafana.
    """

    def get_grafana(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Grafana:
        """
        Get your Cockpit's Grafana.
        Retrieve information on your Cockpit's Grafana, specified by the ID of the Project the Cockpit belongs to.
        The output returned displays the URL to access your Cockpit's Grafana.
        :param project_id: ID of the Project.
        :return: :class:`Grafana <Grafana>`

        Usage:
        ::

            result = api.get_grafana()
        """

        res = self._request(
            "GET",
            "/cockpit/v1/grafana",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_Grafana(res.json())

    def sync_grafana_data_sources(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> None:
        """
        Synchronize Grafana data sources.
        Trigger the synchronization of all your data sources and the alert manager in the relevant regions. The alert manager will only be synchronized if you have enabled it.
        :param project_id: ID of the Project to target.

        Usage:
        ::

            result = api.sync_grafana_data_sources()
        """

        res = self._request(
            "POST",
            "/cockpit/v1/grafana/sync-data-sources",
            body=marshal_GlobalApiSyncGrafanaDataSourcesRequest(
                GlobalApiSyncGrafanaDataSourcesRequest(
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    def create_grafana_user(
        self,
        *,
        login: str,
        project_id: Optional[str] = None,
        role: Optional[GrafanaUserRole] = None,
    ) -> GrafanaUser:
        """
        (Deprecated) EOL 2026-01-20.
        Create a Grafana user
        Create a Grafana user to connect to your Cockpit's Grafana. Upon creation, your user password displays only once, so make sure that you save it.
        Each Grafana user is associated with a role: viewer or editor. A viewer can only view dashboards, whereas an editor can create and edit dashboards. Note that the `admin` username is not available for creation.
        :param login: Username of the Grafana user. Note that the `admin` username is not available for creation.
        :param project_id: ID of the Project in which to create the Grafana user.
        :param role: Role assigned to the Grafana user.
        :return: :class:`GrafanaUser <GrafanaUser>`
        :deprecated

        Usage:
        ::

            result = api.create_grafana_user(
                login="example",
            )
        """

        res = self._request(
            "POST",
            "/cockpit/v1/grafana/users",
            body=marshal_GlobalApiCreateGrafanaUserRequest(
                GlobalApiCreateGrafanaUserRequest(
                    login=login,
                    project_id=project_id,
                    role=role,
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
        order_by: Optional[ListGrafanaUsersRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> ListGrafanaUsersResponse:
        """
        (Deprecated) EOL 2026-01-20.
        List Grafana users
        List all Grafana users created in your Cockpit's Grafana. By default, the Grafana users returned in the list are ordered in ascending order.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by: Order of the Grafana users.
        :param project_id: ID of the Project to target.
        :return: :class:`ListGrafanaUsersResponse <ListGrafanaUsersResponse>`
        :deprecated

        Usage:
        ::

            result = api.list_grafana_users()
        """

        res = self._request(
            "GET",
            "/cockpit/v1/grafana/users",
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
    ) -> list[GrafanaUser]:
        """
        (Deprecated) EOL 2026-01-20.
        List Grafana users
        List all Grafana users created in your Cockpit's Grafana. By default, the Grafana users returned in the list are ordered in ascending order.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by: Order of the Grafana users.
        :param project_id: ID of the Project to target.
        :return: :class:`list[GrafanaUser] <list[GrafanaUser]>`
        :deprecated

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
        project_id: Optional[str] = None,
        grafana_user_id: int,
    ) -> None:
        """
        (Deprecated) EOL 2026-01-20.
        Delete a Grafana user
        Delete a Grafana user from your Cockpit's Grafana, specified by the ID of the Project the Cockpit belongs to, and the ID of the Grafana user.
        :param project_id: ID of the Project to target.
        :param grafana_user_id: ID of the Grafana user.
        :deprecated

        Usage:
        ::

            result = api.delete_grafana_user(
                grafana_user_id=1,
            )
        """

        param_grafana_user_id = validate_path_param("grafana_user_id", grafana_user_id)

        res = self._request(
            "DELETE",
            f"/cockpit/v1/grafana/users/{param_grafana_user_id}",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)

    def reset_grafana_user_password(
        self,
        *,
        project_id: Optional[str] = None,
        grafana_user_id: int,
    ) -> GrafanaUser:
        """
        (Deprecated) EOL 2026-01-20.
        Reset a Grafana user password
        Reset the password of a Grafana user, specified by the ID of the Project the Cockpit belongs to, and the ID of the Grafana user.
        A new password regenerates and only displays once. Make sure that you save it.
        :param project_id: ID of the Project to target.
        :param grafana_user_id: ID of the Grafana user.
        :return: :class:`GrafanaUser <GrafanaUser>`
        :deprecated

        Usage:
        ::

            result = api.reset_grafana_user_password(
                grafana_user_id=1,
            )
        """

        param_grafana_user_id = validate_path_param("grafana_user_id", grafana_user_id)

        res = self._request(
            "POST",
            f"/cockpit/v1/grafana/users/{param_grafana_user_id}/reset-password",
            body=marshal_GlobalApiResetGrafanaUserPasswordRequest(
                GlobalApiResetGrafanaUserPasswordRequest(
                    project_id=project_id,
                    grafana_user_id=grafana_user_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_GrafanaUser(res.json())

    def list_grafana_product_dashboards(
        self,
        *,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        tags: Optional[list[str]] = None,
    ) -> ListGrafanaProductDashboardsResponse:
        """
        List Scaleway resources dashboards.
        Retrieve a list of available dashboards in Grafana, for all Scaleway resources which are integrated with Cockpit.
        :param project_id: ID of the Project to target.
        :param page: Page number.
        :param page_size: Page size.
        :param tags: Tags to filter for.
        :return: :class:`ListGrafanaProductDashboardsResponse <ListGrafanaProductDashboardsResponse>`

        Usage:
        ::

            result = api.list_grafana_product_dashboards()
        """

        res = self._request(
            "GET",
            "/cockpit/v1/grafana/product-dashboards",
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
        tags: Optional[list[str]] = None,
    ) -> list[GrafanaProductDashboard]:
        """
        List Scaleway resources dashboards.
        Retrieve a list of available dashboards in Grafana, for all Scaleway resources which are integrated with Cockpit.
        :param project_id: ID of the Project to target.
        :param page: Page number.
        :param page_size: Page size.
        :param tags: Tags to filter for.
        :return: :class:`list[GrafanaProductDashboard] <list[GrafanaProductDashboard]>`

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
        project_id: Optional[str] = None,
        dashboard_name: str,
    ) -> GrafanaProductDashboard:
        """
        Get Scaleway resource dashboard.
        Retrieve information about the dashboard of a Scaleway resource in Grafana, specified by the ID of the Project the Cockpit belongs to, and the name of the dashboard.
        :param project_id: ID of the Project the dashboard belongs to.
        :param dashboard_name: Name of the dashboard.
        :return: :class:`GrafanaProductDashboard <GrafanaProductDashboard>`

        Usage:
        ::

            result = api.get_grafana_product_dashboard(
                dashboard_name="example",
            )
        """

        param_dashboard_name = validate_path_param("dashboard_name", dashboard_name)

        res = self._request(
            "GET",
            f"/cockpit/v1/grafana/product-dashboards/{param_dashboard_name}",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_GrafanaProductDashboard(res.json())

    def list_plans(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListPlansRequestOrderBy] = None,
    ) -> ListPlansResponse:
        """
        List plan types.
        Retrieve a list of available pricing plan types.
        Deprecated due to retention now being managed at the data source level.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by:
        :return: :class:`ListPlansResponse <ListPlansResponse>`
        :deprecated

        Usage:
        ::

            result = api.list_plans()
        """

        res = self._request(
            "GET",
            "/cockpit/v1/plans",
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
    ) -> list[Plan]:
        """
        List plan types.
        Retrieve a list of available pricing plan types.
        Deprecated due to retention now being managed at the data source level.
        :param page: Page number.
        :param page_size: Page size.
        :param order_by:
        :return: :class:`list[Plan] <list[Plan]>`
        :deprecated

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
        project_id: Optional[str] = None,
        plan_name: Optional[PlanName] = None,
    ) -> Plan:
        """
        Apply a pricing plan.
        Apply a pricing plan on a given Project. You must specify the ID of the pricing plan type. Note that you will be billed for the plan you apply.
        Deprecated due to retention now being managed at the data source level.
        :param project_id: ID of the Project.
        :param plan_name: Name of the pricing plan.
        :return: :class:`Plan <Plan>`
        :deprecated

        Usage:
        ::

            result = api.select_plan()
        """

        res = self._request(
            "PATCH",
            "/cockpit/v1/plans",
            body=marshal_GlobalApiSelectPlanRequest(
                GlobalApiSelectPlanRequest(
                    project_id=project_id,
                    plan_name=plan_name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Plan(res.json())

    def get_current_plan(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Plan:
        """
        Get current plan.
        Retrieve a pricing plan for the given Project, specified by the ID of the Project.
        Deprecated due to retention now being managed at the data source level.
        :param project_id: ID of the Project.
        :return: :class:`Plan <Plan>`
        :deprecated

        Usage:
        ::

            result = api.get_current_plan()
        """

        res = self._request(
            "GET",
            "/cockpit/v1/current-plan",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_Plan(res.json())


class CockpitV1RegionalAPI(API):
    """
    The Cockpit API allows you to create data sources and Cockpit tokens to store and query data types such as metrics, logs, and traces. You can also push your data into Cockpit, and send alerts to your contact points when your resources may require your attention, using the regional Alert manager.
    """

    def get_config(
        self,
        *,
        region: Optional[ScwRegion] = None,
    ) -> GetConfigResponse:
        """
        Get the Cockpit configuration.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`GetConfigResponse <GetConfigResponse>`

        Usage:
        ::

            result = api.get_config()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/cockpit/v1/regions/{param_region}/config",
        )

        self._throw_on_error(res)
        return unmarshal_GetConfigResponse(res.json())

    def create_exporter(
        self,
        *,
        datasource_id: str,
        exported_products: list[str],
        name: str,
        region: Optional[ScwRegion] = None,
        datadog_destination: Optional[ExporterDatadogDestination] = None,
        otlp_destination: Optional[ExporterOTLPDestination] = None,
        description: Optional[str] = None,
    ) -> Exporter:
        """
        Create a data export.
        Create an export to send your metrics/logs from a Scaleway data source to an external destination.
        Current supported destination for data exports are Datadog and OTLP endpoints.
        This feature is in Beta phase. During Beta phase, exporter can take up to 30 min to be effectively active.
        :param datasource_id: ID of the data source linked to the data export.
        :param exported_products: To include all products in your data export, you can use an array containing "all"
        You can retrieve the complete list of product names using the `ListProducts` endpoint.
        :param name: Name of the data export.
        :param region: Region to target. If none is passed will use default region from the config.
        :param datadog_destination: Datadog destination configuration for the data export.
        One-Of ('destination'): at most one of 'datadog_destination', 'otlp_destination' could be set.
        :param otlp_destination: OTLP destination configuration for the data export.
        One-Of ('destination'): at most one of 'datadog_destination', 'otlp_destination' could be set.
        :param description: Description of the data export.
        :return: :class:`Exporter <Exporter>`

        Usage:
        ::

            result = api.create_exporter(
                datasource_id="example",
                exported_products=[],
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/cockpit/v1/regions/{param_region}/exporters",
            body=marshal_RegionalApiCreateExporterRequest(
                RegionalApiCreateExporterRequest(
                    datasource_id=datasource_id,
                    exported_products=exported_products,
                    name=name,
                    region=region,
                    description=description,
                    datadog_destination=datadog_destination,
                    otlp_destination=otlp_destination,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Exporter(res.json())

    def list_exporters(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        datasource_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListExportersRequestOrderBy] = None,
    ) -> ListExportersResponse:
        """
        List data exports.
        List all data exports within a given Scaleway Project, specified by its ID.
        Optionally, specify a Scaleway data source ID to retrieve only data exports associated with that data source.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project ID to filter for. Only data exports from this Project will be returned.
        :param datasource_id: Data source ID to filter for. Only data exports linked to this data source will be returned.
        :param page: Page number to return from the paginated results.
        :param page_size: Number of data exports to return per page.
        :param order_by: Sort order for data exports in the response.
        :return: :class:`ListExportersResponse <ListExportersResponse>`

        Usage:
        ::

            result = api.list_exporters()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/cockpit/v1/regions/{param_region}/exporters",
            params={
                "datasource_id": datasource_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListExportersResponse(res.json())

    def list_exporters_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        datasource_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListExportersRequestOrderBy] = None,
    ) -> list[Exporter]:
        """
        List data exports.
        List all data exports within a given Scaleway Project, specified by its ID.
        Optionally, specify a Scaleway data source ID to retrieve only data exports associated with that data source.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project ID to filter for. Only data exports from this Project will be returned.
        :param datasource_id: Data source ID to filter for. Only data exports linked to this data source will be returned.
        :param page: Page number to return from the paginated results.
        :param page_size: Number of data exports to return per page.
        :param order_by: Sort order for data exports in the response.
        :return: :class:`list[Exporter] <list[Exporter]>`

        Usage:
        ::

            result = api.list_exporters_all()
        """

        return fetch_all_pages(
            type=ListExportersResponse,
            key="exporters",
            fetcher=self.list_exporters,
            args={
                "region": region,
                "project_id": project_id,
                "datasource_id": datasource_id,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    def get_exporter(
        self,
        *,
        exporter_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Exporter:
        """
        Get a data export.
        Retrieve information about a given data export, specified by its ID.
        :param exporter_id: ID of the data export to retrieve.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Exporter <Exporter>`

        Usage:
        ::

            result = api.get_exporter(
                exporter_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_exporter_id = validate_path_param("exporter_id", exporter_id)

        res = self._request(
            "GET",
            f"/cockpit/v1/regions/{param_region}/exporters/{param_exporter_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Exporter(res.json())

    def wait_for_exporter(
        self,
        *,
        exporter_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[WaitForOptions[Exporter, bool]] = None,
    ) -> Exporter:
        """
        Get a data export.
        Retrieve information about a given data export, specified by its ID.
        :param exporter_id: ID of the data export to retrieve.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Exporter <Exporter>`

        Usage:
        ::

            result = api.get_exporter(
                exporter_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in EXPORTER_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_exporter,
            options=options,
            args={
                "exporter_id": exporter_id,
                "region": region,
            },
        )

    def delete_exporter(
        self,
        *,
        exporter_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a data export.
        Delete a given data export, specified by its ID.
        Note that this action will immediatly and permanently delete this data exports.
        :param exporter_id: ID of the data export to update.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_exporter(
                exporter_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_exporter_id = validate_path_param("exporter_id", exporter_id)

        res = self._request(
            "DELETE",
            f"/cockpit/v1/regions/{param_region}/exporters/{param_exporter_id}",
        )

        self._throw_on_error(res)

    def update_exporter(
        self,
        *,
        exporter_id: str,
        region: Optional[ScwRegion] = None,
        datadog_destination: Optional[ExporterDatadogDestination] = None,
        otlp_destination: Optional[ExporterOTLPDestination] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        exported_products: Optional[list[str]] = None,
    ) -> Exporter:
        """
        Update a data export.
        Update a data export attributes. Changes are effective immediatly even during Beta phase.
        Note that you can not change the data source linked to the export. If you need to do so, you will need to re-create the export.
        :param exporter_id: ID of the data export to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param datadog_destination: Updated Datadog destination configuration for the data export.
        One-Of ('destination'): at most one of 'datadog_destination', 'otlp_destination' could be set.
        :param otlp_destination: Updated OTLP destination configuration for the data export.
        One-Of ('destination'): at most one of 'datadog_destination', 'otlp_destination' could be set.
        :param name: Updated name of the data export.
        :param description: Updated description of the data export.
        :param exported_products: To include all products in your data export, you can use an array containing "all"
        You can retrieve the complete list of product names using the `ListProducts` endpoint.
        :return: :class:`Exporter <Exporter>`

        Usage:
        ::

            result = api.update_exporter(
                exporter_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_exporter_id = validate_path_param("exporter_id", exporter_id)

        res = self._request(
            "PATCH",
            f"/cockpit/v1/regions/{param_region}/exporters/{param_exporter_id}",
            body=marshal_RegionalApiUpdateExporterRequest(
                RegionalApiUpdateExporterRequest(
                    exporter_id=exporter_id,
                    region=region,
                    name=name,
                    description=description,
                    exported_products=exported_products,
                    datadog_destination=datadog_destination,
                    otlp_destination=otlp_destination,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Exporter(res.json())

    def create_data_source(
        self,
        *,
        name: str,
        type_: DataSourceType,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        retention_days: Optional[int] = None,
    ) -> DataSource:
        """
        Create a data source.
        You must specify the data source name and type (metrics, logs, traces) upon creation.
        The name of the data source will then be used as reference to name the associated Grafana data source.
        :param name: Data source name.
        :param type_: Data source type.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project the data source belongs to.
        :param retention_days: Default values are 31 days for metrics, 7 days for logs and traces.
        :return: :class:`DataSource <DataSource>`

        Usage:
        ::

            result = api.create_data_source(
                name="example",
                type=DataSourceType.unknown_type,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/cockpit/v1/regions/{param_region}/data-sources",
            body=marshal_RegionalApiCreateDataSourceRequest(
                RegionalApiCreateDataSourceRequest(
                    name=name,
                    type_=type_,
                    region=region,
                    project_id=project_id,
                    retention_days=retention_days,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DataSource(res.json())

    def get_data_source(
        self,
        *,
        data_source_id: str,
        region: Optional[ScwRegion] = None,
    ) -> DataSource:
        """
        Get a data source.
        Retrieve information about a given data source, specified by the data source ID. The data source's information such as its name, type, URL, origin, and retention period, is returned.
        :param data_source_id: ID of the relevant data source.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DataSource <DataSource>`

        Usage:
        ::

            result = api.get_data_source(
                data_source_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_data_source_id = validate_path_param("data_source_id", data_source_id)

        res = self._request(
            "GET",
            f"/cockpit/v1/regions/{param_region}/data-sources/{param_data_source_id}",
        )

        self._throw_on_error(res)
        return unmarshal_DataSource(res.json())

    def delete_data_source(
        self,
        *,
        data_source_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a data source.
        Delete a given data source. Note that this action will permanently delete this data source and any data associated with it.
        :param data_source_id: ID of the data source to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_data_source(
                data_source_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_data_source_id = validate_path_param("data_source_id", data_source_id)

        res = self._request(
            "DELETE",
            f"/cockpit/v1/regions/{param_region}/data-sources/{param_data_source_id}",
        )

        self._throw_on_error(res)

    def list_data_sources(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        origin: Optional[DataSourceOrigin] = None,
        types: Optional[list[DataSourceType]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDataSourcesRequestOrderBy] = None,
    ) -> ListDataSourcesResponse:
        """
        List data sources.
        Retrieve the list of data sources available in the specified region. By default, the data sources returned in the list are ordered by creation date, in ascending order.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project ID to filter for, only data sources from this Project will be returned.
        :param origin: Origin to filter for, only data sources with matching origin will be returned. If omitted, all types will be returned.
        :param types: Types to filter for (metrics, logs, traces), only data sources with matching types will be returned. If omitted, all types will be returned.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of data sources to return per page.
        :param order_by: Sort order for data sources in the response.
        :return: :class:`ListDataSourcesResponse <ListDataSourcesResponse>`

        Usage:
        ::

            result = api.list_data_sources()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/cockpit/v1/regions/{param_region}/data-sources",
            params={
                "order_by": order_by,
                "origin": origin,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "types": types,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDataSourcesResponse(res.json())

    def list_data_sources_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        origin: Optional[DataSourceOrigin] = None,
        types: Optional[list[DataSourceType]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDataSourcesRequestOrderBy] = None,
    ) -> list[DataSource]:
        """
        List data sources.
        Retrieve the list of data sources available in the specified region. By default, the data sources returned in the list are ordered by creation date, in ascending order.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project ID to filter for, only data sources from this Project will be returned.
        :param origin: Origin to filter for, only data sources with matching origin will be returned. If omitted, all types will be returned.
        :param types: Types to filter for (metrics, logs, traces), only data sources with matching types will be returned. If omitted, all types will be returned.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of data sources to return per page.
        :param order_by: Sort order for data sources in the response.
        :return: :class:`list[DataSource] <list[DataSource]>`

        Usage:
        ::

            result = api.list_data_sources_all()
        """

        return fetch_all_pages(
            type=ListDataSourcesResponse,
            key="data_sources",
            fetcher=self.list_data_sources,
            args={
                "region": region,
                "project_id": project_id,
                "origin": origin,
                "types": types,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    def update_data_source(
        self,
        *,
        data_source_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        retention_days: Optional[int] = None,
    ) -> DataSource:
        """
        Update a data source.
        Update a given data source attributes (name and/or retention_days).
        :param data_source_id: ID of the data source to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Updated name of the data source.
        :param retention_days: Duration for which the data will be retained in the data source.
        :return: :class:`DataSource <DataSource>`

        Usage:
        ::

            result = api.update_data_source(
                data_source_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_data_source_id = validate_path_param("data_source_id", data_source_id)

        res = self._request(
            "PATCH",
            f"/cockpit/v1/regions/{param_region}/data-sources/{param_data_source_id}",
            body=marshal_RegionalApiUpdateDataSourceRequest(
                RegionalApiUpdateDataSourceRequest(
                    data_source_id=data_source_id,
                    region=region,
                    name=name,
                    retention_days=retention_days,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DataSource(res.json())

    def get_usage_overview(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        interval: Optional[str] = None,
    ) -> UsageOverview:
        """
        Get data source usage overview.
        Retrieve the volume of data ingested for each of your data sources in the specified project and region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id:
        :param interval:
        :return: :class:`UsageOverview <UsageOverview>`

        Usage:
        ::

            result = api.get_usage_overview()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/cockpit/v1/regions/{param_region}/usage-overview",
            params={
                "interval": interval,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_UsageOverview(res.json())

    def create_token(
        self,
        *,
        name: str,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        token_scopes: Optional[list[TokenScope]] = None,
    ) -> Token:
        """
        Create a token.
        Give your token the relevant scopes to ensure it has the right permissions to interact with your data sources and the Alert manager. Make sure that you create your token in the same regions as the data sources you want to use it for.
        Upon creation, your token's secret key display only once. Make sure that you save it.
        :param name: Name of the token.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project the token belongs to.
        :param token_scopes: Token permission scopes.
        :return: :class:`Token <Token>`

        Usage:
        ::

            result = api.create_token(
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/cockpit/v1/regions/{param_region}/tokens",
            body=marshal_RegionalApiCreateTokenRequest(
                RegionalApiCreateTokenRequest(
                    name=name,
                    region=region,
                    project_id=project_id,
                    token_scopes=token_scopes,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Token(res.json())

    def list_tokens(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        token_scopes: Optional[list[TokenScope]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListTokensRequestOrderBy] = None,
    ) -> ListTokensResponse:
        """
        List tokens.
        Retrieve a list of all tokens in the specified region. By default, tokens returned in the list are ordered by creation date, in ascending order.
        You can filter tokens by Project ID and token scopes.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project the tokens belong to.
        :param token_scopes: Token scopes to filter for.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of tokens to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`ListTokensResponse <ListTokensResponse>`

        Usage:
        ::

            result = api.list_tokens()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/cockpit/v1/regions/{param_region}/tokens",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "token_scopes": token_scopes,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListTokensResponse(res.json())

    def list_tokens_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        token_scopes: Optional[list[TokenScope]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListTokensRequestOrderBy] = None,
    ) -> list[Token]:
        """
        List tokens.
        Retrieve a list of all tokens in the specified region. By default, tokens returned in the list are ordered by creation date, in ascending order.
        You can filter tokens by Project ID and token scopes.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project the tokens belong to.
        :param token_scopes: Token scopes to filter for.
        :param page: Page number to return, from the paginated results.
        :param page_size: Number of tokens to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`list[Token] <list[Token]>`

        Usage:
        ::

            result = api.list_tokens_all()
        """

        return fetch_all_pages(
            type=ListTokensResponse,
            key="tokens",
            fetcher=self.list_tokens,
            args={
                "region": region,
                "project_id": project_id,
                "token_scopes": token_scopes,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    def get_token(
        self,
        *,
        token_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Token:
        """
        Get a token.
        Retrieve information about a given token, specified by the token ID. The token's information such as its scopes, is returned.
        :param token_id: Token ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Token <Token>`

        Usage:
        ::

            result = api.get_token(
                token_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_token_id = validate_path_param("token_id", token_id)

        res = self._request(
            "GET",
            f"/cockpit/v1/regions/{param_region}/tokens/{param_token_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Token(res.json())

    def delete_token(
        self,
        *,
        token_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a token.
        Delete a given token, specified by the token ID. Deleting a token is irreversible and cannot be undone.
        :param token_id: ID of the token to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_token(
                token_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_token_id = validate_path_param("token_id", token_id)

        res = self._request(
            "DELETE",
            f"/cockpit/v1/regions/{param_region}/tokens/{param_token_id}",
        )

        self._throw_on_error(res)

    def list_products(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListProductsRequestOrderBy] = None,
    ) -> ListProductsResponse:
        """
        List Scaleway products.
        List all Scaleway products that send metrics and/or logs to Cockpit.
        Note that all of those products send at least metrics, but only a subset send logs to Cockpit.
        For more information, see https://www.scaleway.com/en/docs/cockpit/reference-content/cockpit-product-integration/.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return from the paginated results.
        :param page_size: Number of products to return per page.
        :param order_by: Sort order for products in the response.
        :return: :class:`ListProductsResponse <ListProductsResponse>`

        Usage:
        ::

            result = api.list_products()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/cockpit/v1/regions/{param_region}/products",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListProductsResponse(res.json())

    def list_products_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListProductsRequestOrderBy] = None,
    ) -> list[Product]:
        """
        List Scaleway products.
        List all Scaleway products that send metrics and/or logs to Cockpit.
        Note that all of those products send at least metrics, but only a subset send logs to Cockpit.
        For more information, see https://www.scaleway.com/en/docs/cockpit/reference-content/cockpit-product-integration/.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return from the paginated results.
        :param page_size: Number of products to return per page.
        :param order_by: Sort order for products in the response.
        :return: :class:`list[Product] <list[Product]>`

        Usage:
        ::

            result = api.list_products_all()
        """

        return fetch_all_pages(
            type=ListProductsResponse,
            key="products_list",
            fetcher=self.list_products,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    def get_alert_manager(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> AlertManager:
        """
        Get the Alert manager.
        Retrieve information about the Alert manager which is unique per Project and region. By default the Alert manager is disabled.
        The output returned displays a URL to access the Alert manager, and whether the Alert manager and managed alerts are enabled.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project ID of the requested Alert manager.
        :return: :class:`AlertManager <AlertManager>`

        Usage:
        ::

            result = api.get_alert_manager()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/cockpit/v1/regions/{param_region}/alert-manager",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_AlertManager(res.json())

    def enable_alert_manager(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> AlertManager:
        """
        Enable the Alert manager.
        Enabling the Alert manager allows you to enable managed alerts and create contact points in the specified Project and region, to be notified when your Scaleway resources may require your attention.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project to enable the Alert manager in.
        :return: :class:`AlertManager <AlertManager>`

        Usage:
        ::

            result = api.enable_alert_manager()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/cockpit/v1/regions/{param_region}/alert-manager/enable",
            body=marshal_RegionalApiEnableAlertManagerRequest(
                RegionalApiEnableAlertManagerRequest(
                    region=region,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_AlertManager(res.json())

    def disable_alert_manager(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> AlertManager:
        """
        Disable the Alert manager.
        Disabling the Alert manager deletes the contact points you have created and disables managed alerts in the specified Project and region.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project to disable the Alert manager in.
        :return: :class:`AlertManager <AlertManager>`

        Usage:
        ::

            result = api.disable_alert_manager()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/cockpit/v1/regions/{param_region}/alert-manager/disable",
            body=marshal_RegionalApiDisableAlertManagerRequest(
                RegionalApiDisableAlertManagerRequest(
                    region=region,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_AlertManager(res.json())

    def get_rules_count(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> GetRulesCountResponse:
        """
        Get the number of enabled rules.
        Get a detailed count of enabled rules in the specified Project. Includes preconfigured and custom alerting and recording rules.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project to retrieve the rule count for.
        :return: :class:`GetRulesCountResponse <GetRulesCountResponse>`

        Usage:
        ::

            result = api.get_rules_count()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/cockpit/v1/regions/{param_region}/rules/count",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_GetRulesCountResponse(res.json())

    def create_contact_point(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        email: Optional[ContactPointEmail] = None,
        send_resolved_notifications: Optional[bool] = None,
    ) -> ContactPoint:
        """
        Create a contact point.
        Contact points are email addresses associated with the default receiver, that the Alert manager sends alerts to.
        The source of the alerts are data sources within the same Project and region as the Alert manager.
        If you need to receive alerts for other receivers, you can create additional contact points and receivers in Grafana. Make sure that you select the Scaleway Alert manager.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project to create the contact point in.
        :param email: Email address of the contact point to create.
        One-Of ('configuration'): at most one of 'email' could be set.
        :param send_resolved_notifications: Send an email notification when an alert is marked as resolved.
        :return: :class:`ContactPoint <ContactPoint>`

        Usage:
        ::

            result = api.create_contact_point()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/cockpit/v1/regions/{param_region}/alert-manager/contact-points",
            body=marshal_RegionalApiCreateContactPointRequest(
                RegionalApiCreateContactPointRequest(
                    region=region,
                    project_id=project_id,
                    send_resolved_notifications=send_resolved_notifications,
                    email=email,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ContactPoint(res.json())

    def list_contact_points(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListContactPointsResponse:
        """
        List contact points.
        Retrieve a list of contact points for the specified Project. The response lists all contact points and receivers created in Grafana or via the API.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project containing the contact points to list.
        :param page: Page number to return, from the paginated results.
        :param page_size: Total count of contact points to return per page.
        :return: :class:`ListContactPointsResponse <ListContactPointsResponse>`

        Usage:
        ::

            result = api.list_contact_points()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/cockpit/v1/regions/{param_region}/alert-manager/contact-points",
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
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> list[ContactPoint]:
        """
        List contact points.
        Retrieve a list of contact points for the specified Project. The response lists all contact points and receivers created in Grafana or via the API.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project containing the contact points to list.
        :param page: Page number to return, from the paginated results.
        :param page_size: Total count of contact points to return per page.
        :return: :class:`list[ContactPoint] <list[ContactPoint]>`

        Usage:
        ::

            result = api.list_contact_points_all()
        """

        return fetch_all_pages(
            type=ListContactPointsResponse,
            key="contact_points",
            fetcher=self.list_contact_points,
            args={
                "region": region,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
            },
        )

    def update_contact_point(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        email: Optional[ContactPointEmail] = None,
        send_resolved_notifications: Optional[bool] = None,
    ) -> ContactPoint:
        """
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project containing the contact point to update.
        :param email: Email address of the contact point to update.
        One-Of ('configuration'): at most one of 'email' could be set.
        :param send_resolved_notifications: Enable or disable notifications when alert is resolved.
        :return: :class:`ContactPoint <ContactPoint>`

        Usage:
        ::

            result = api.update_contact_point()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "PATCH",
            f"/cockpit/v1/regions/{param_region}/alert-manager/contact-points",
            body=marshal_RegionalApiUpdateContactPointRequest(
                RegionalApiUpdateContactPointRequest(
                    region=region,
                    project_id=project_id,
                    send_resolved_notifications=send_resolved_notifications,
                    email=email,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ContactPoint(res.json())

    def delete_contact_point(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        email: Optional[ContactPointEmail] = None,
    ) -> None:
        """
        Delete a contact point.
        Delete a contact point associated with the default receiver.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project containing the contact point to delete.
        :param email: Email address of the contact point to delete.
        One-Of ('configuration'): at most one of 'email' could be set.

        Usage:
        ::

            result = api.delete_contact_point()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/cockpit/v1/regions/{param_region}/alert-manager/contact-points/delete",
            body=marshal_RegionalApiDeleteContactPointRequest(
                RegionalApiDeleteContactPointRequest(
                    region=region,
                    project_id=project_id,
                    email=email,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    def list_alerts(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        rule_status: Optional[AlertStatus] = None,
        is_preconfigured: Optional[bool] = None,
        state: Optional[AlertState] = None,
        data_source_id: Optional[str] = None,
    ) -> ListAlertsResponse:
        """
        List alerts.
        List preconfigured and/or custom alerts for the specified Project and data source.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project ID to filter for, only alerts from this Project will be returned.
        :param rule_status: Returns only alerts with the given activation status. If omitted, no alert filtering is applied. Other filters may still apply.
        :param is_preconfigured: True returns only preconfigured alerts. False returns only custom alerts. If omitted, no filtering is applied on alert types. Other filters may still apply.
        :param state: Valid values to filter on are `inactive`, `pending` and `firing`. If omitted, no filtering is applied on alert states. Other filters may still apply.
        :param data_source_id: If omitted, only alerts from the default Scaleway metrics data source will be listed.
        :return: :class:`ListAlertsResponse <ListAlertsResponse>`

        Usage:
        ::

            result = api.list_alerts()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/cockpit/v1/regions/{param_region}/alerts",
            params={
                "data_source_id": data_source_id,
                "is_preconfigured": is_preconfigured,
                "project_id": project_id or self.client.default_project_id,
                "rule_status": rule_status,
                "state": state,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListAlertsResponse(res.json())

    def enable_managed_alerts(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> AlertManager:
        """
        Enable managed alerts.
        Enable the sending of managed alerts for the specified Project. Managed alerts are predefined alerts that apply to Scaleway resources integrated with Cockpit by default.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project.
        :return: :class:`AlertManager <AlertManager>`
        :deprecated

        Usage:
        ::

            result = api.enable_managed_alerts()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/cockpit/v1/regions/{param_region}/alert-manager/managed-alerts/enable",
            body=marshal_RegionalApiEnableManagedAlertsRequest(
                RegionalApiEnableManagedAlertsRequest(
                    region=region,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_AlertManager(res.json())

    def disable_managed_alerts(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> AlertManager:
        """
        Disable managed alerts.
        Disable the sending of managed alerts for the specified Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project.
        :return: :class:`AlertManager <AlertManager>`
        :deprecated

        Usage:
        ::

            result = api.disable_managed_alerts()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/cockpit/v1/regions/{param_region}/alert-manager/managed-alerts/disable",
            body=marshal_RegionalApiDisableManagedAlertsRequest(
                RegionalApiDisableManagedAlertsRequest(
                    region=region,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_AlertManager(res.json())

    def enable_alert_rules(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        rule_ids: Optional[list[str]] = None,
    ) -> EnableAlertRulesResponse:
        """
        Enable preconfigured alert rules.
        Enable alert rules from the list of available preconfigured rules.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project.
        :param rule_ids: List of IDs of the rules to enable. If empty, enables all preconfigured rules.
        :return: :class:`EnableAlertRulesResponse <EnableAlertRulesResponse>`

        Usage:
        ::

            result = api.enable_alert_rules()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/cockpit/v1/regions/{param_region}/alert-manager/enable-alert-rules",
            body=marshal_RegionalApiEnableAlertRulesRequest(
                RegionalApiEnableAlertRulesRequest(
                    region=region,
                    project_id=project_id,
                    rule_ids=rule_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_EnableAlertRulesResponse(res.json())

    def disable_alert_rules(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        rule_ids: Optional[list[str]] = None,
    ) -> DisableAlertRulesResponse:
        """
        Disable preconfigured alert rules.
        Disable alert rules from the list of available preconfigured rules.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project.
        :param rule_ids: List of IDs of the rules to enable. If empty, disables all preconfigured rules.
        :return: :class:`DisableAlertRulesResponse <DisableAlertRulesResponse>`

        Usage:
        ::

            result = api.disable_alert_rules()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/cockpit/v1/regions/{param_region}/alert-manager/disable-alert-rules",
            body=marshal_RegionalApiDisableAlertRulesRequest(
                RegionalApiDisableAlertRulesRequest(
                    region=region,
                    project_id=project_id,
                    rule_ids=rule_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DisableAlertRulesResponse(res.json())

    def trigger_test_alert(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> None:
        """
        Trigger a test alert.
        Send a test alert to the Alert manager to make sure your contact points get notified.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project.

        Usage:
        ::

            result = api.trigger_test_alert()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/cockpit/v1/regions/{param_region}/alert-manager/trigger-test-alert",
            body=marshal_RegionalApiTriggerTestAlertRequest(
                RegionalApiTriggerTestAlertRequest(
                    region=region,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
