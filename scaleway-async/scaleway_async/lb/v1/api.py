# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
    Zone,
)
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages_async,
    random_name,
    validate_path_param,
    wait_for_resource_async,
)
from .types import (
    ForwardPortAlgorithm,
    ListAclRequestOrderBy,
    ListBackendsRequestOrderBy,
    ListCertificatesRequestOrderBy,
    ListFrontendsRequestOrderBy,
    ListLbsRequestOrderBy,
    ListPrivateNetworksRequestOrderBy,
    ListRoutesRequestOrderBy,
    ListSubscriberRequestOrderBy,
    OnMarkedDownAction,
    Protocol,
    ProxyProtocol,
    SSLCompatibilityLevel,
    StickySessionsType,
    Acl,
    AclAction,
    AclMatch,
    AclSpec,
    Backend,
    BackendServerStats,
    Certificate,
    CreateCertificateRequestCustomCertificate,
    CreateCertificateRequestLetsencryptConfig,
    Frontend,
    HealthCheck,
    HealthCheckHttpConfig,
    HealthCheckHttpsConfig,
    HealthCheckLdapConfig,
    HealthCheckMysqlConfig,
    HealthCheckPgsqlConfig,
    HealthCheckRedisConfig,
    HealthCheckTcpConfig,
    Ip,
    Lb,
    LbStats,
    LbType,
    ListAclResponse,
    ListBackendStatsResponse,
    ListBackendsResponse,
    ListCertificatesResponse,
    ListFrontendsResponse,
    ListIpsResponse,
    ListLbPrivateNetworksResponse,
    ListLbTypesResponse,
    ListLbsResponse,
    ListRoutesResponse,
    ListSubscriberResponse,
    PrivateNetwork,
    PrivateNetworkDHCPConfig,
    PrivateNetworkIpamConfig,
    PrivateNetworkStaticConfig,
    Route,
    RouteMatch,
    SetAclsResponse,
    Subscriber,
    SubscriberEmailConfig,
    SubscriberWebhookConfig,
    CreateLbRequest,
    UpdateLbRequest,
    MigrateLbRequest,
    CreateIpRequest,
    UpdateIpRequest,
    CreateBackendRequest,
    UpdateBackendRequest,
    AddBackendServersRequest,
    RemoveBackendServersRequest,
    SetBackendServersRequest,
    UpdateHealthCheckRequest,
    CreateFrontendRequest,
    UpdateFrontendRequest,
    CreateRouteRequest,
    UpdateRouteRequest,
    CreateAclRequest,
    UpdateAclRequest,
    CreateCertificateRequest,
    UpdateCertificateRequest,
    CreateSubscriberRequest,
    UpdateSubscriberRequest,
    SubscribeToLbRequest,
    AttachPrivateNetworkRequest,
    ZonedApiCreateLbRequest,
    ZonedApiUpdateLbRequest,
    ZonedApiMigrateLbRequest,
    ZonedApiCreateIpRequest,
    ZonedApiUpdateIpRequest,
    ZonedApiCreateBackendRequest,
    ZonedApiUpdateBackendRequest,
    ZonedApiAddBackendServersRequest,
    ZonedApiRemoveBackendServersRequest,
    ZonedApiSetBackendServersRequest,
    ZonedApiUpdateHealthCheckRequest,
    ZonedApiCreateFrontendRequest,
    ZonedApiUpdateFrontendRequest,
    ZonedApiCreateRouteRequest,
    ZonedApiUpdateRouteRequest,
    ZonedApiCreateAclRequest,
    ZonedApiUpdateAclRequest,
    ZonedApiSetAclsRequest,
    ZonedApiCreateCertificateRequest,
    ZonedApiUpdateCertificateRequest,
    ZonedApiCreateSubscriberRequest,
    ZonedApiUpdateSubscriberRequest,
    ZonedApiSubscribeToLbRequest,
    ZonedApiAttachPrivateNetworkRequest,
)
from .content import (
    CERTIFICATE_TRANSIENT_STATUSES,
    LB_TRANSIENT_STATUSES,
)
from .marshalling import (
    marshal_AddBackendServersRequest,
    marshal_AttachPrivateNetworkRequest,
    marshal_CreateAclRequest,
    marshal_CreateBackendRequest,
    marshal_CreateCertificateRequest,
    marshal_CreateFrontendRequest,
    marshal_CreateIpRequest,
    marshal_CreateLbRequest,
    marshal_CreateRouteRequest,
    marshal_CreateSubscriberRequest,
    marshal_MigrateLbRequest,
    marshal_RemoveBackendServersRequest,
    marshal_SetBackendServersRequest,
    marshal_SubscribeToLbRequest,
    marshal_UpdateAclRequest,
    marshal_UpdateBackendRequest,
    marshal_UpdateCertificateRequest,
    marshal_UpdateFrontendRequest,
    marshal_UpdateHealthCheckRequest,
    marshal_UpdateIpRequest,
    marshal_UpdateLbRequest,
    marshal_UpdateRouteRequest,
    marshal_UpdateSubscriberRequest,
    marshal_ZonedApiAddBackendServersRequest,
    marshal_ZonedApiAttachPrivateNetworkRequest,
    marshal_ZonedApiCreateAclRequest,
    marshal_ZonedApiCreateBackendRequest,
    marshal_ZonedApiCreateCertificateRequest,
    marshal_ZonedApiCreateFrontendRequest,
    marshal_ZonedApiCreateIpRequest,
    marshal_ZonedApiCreateLbRequest,
    marshal_ZonedApiCreateRouteRequest,
    marshal_ZonedApiCreateSubscriberRequest,
    marshal_ZonedApiMigrateLbRequest,
    marshal_ZonedApiRemoveBackendServersRequest,
    marshal_ZonedApiSetAclsRequest,
    marshal_ZonedApiSetBackendServersRequest,
    marshal_ZonedApiSubscribeToLbRequest,
    marshal_ZonedApiUpdateAclRequest,
    marshal_ZonedApiUpdateBackendRequest,
    marshal_ZonedApiUpdateCertificateRequest,
    marshal_ZonedApiUpdateFrontendRequest,
    marshal_ZonedApiUpdateHealthCheckRequest,
    marshal_ZonedApiUpdateIpRequest,
    marshal_ZonedApiUpdateLbRequest,
    marshal_ZonedApiUpdateRouteRequest,
    marshal_ZonedApiUpdateSubscriberRequest,
    unmarshal_Ip,
    unmarshal_Subscriber,
    unmarshal_HealthCheck,
    unmarshal_Lb,
    unmarshal_Backend,
    unmarshal_Certificate,
    unmarshal_Frontend,
    unmarshal_Acl,
    unmarshal_PrivateNetwork,
    unmarshal_Route,
    unmarshal_LbStats,
    unmarshal_ListAclResponse,
    unmarshal_ListBackendStatsResponse,
    unmarshal_ListBackendsResponse,
    unmarshal_ListCertificatesResponse,
    unmarshal_ListFrontendsResponse,
    unmarshal_ListIpsResponse,
    unmarshal_ListLbPrivateNetworksResponse,
    unmarshal_ListLbTypesResponse,
    unmarshal_ListLbsResponse,
    unmarshal_ListRoutesResponse,
    unmarshal_ListSubscriberResponse,
    unmarshal_SetAclsResponse,
)


class LbV1API(API):
    """
    Load balancer API.

    This API allows you to manage your load balancer service.
    Load balancer API.
    """

    async def list_lbs(
        self,
        *,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: ListLbsRequestOrderBy = ListLbsRequestOrderBy.CREATED_AT_ASC,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListLbsResponse:
        """
        List load balancers.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Load Balancer name to filter for.
        :param order_by: Sort order of Load Balancers in the response.
        :param page_size: Number of Load Balancers to return.
        :param page: Page number to return, from the paginated results.
        :param organization_id: Organization ID to filter for, only Load Balancers from this Organization will be returned.
        :param project_id: Project ID to filter for, only Load Balancers from this Project will be returned.
        :return: :class:`ListLbsResponse <ListLbsResponse>`

        Usage:
        ::

            result = await api.list_lbs()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lbs",
            params={
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
        return unmarshal_ListLbsResponse(res.json())

    async def list_lbs_all(
        self,
        *,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: Optional[ListLbsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Lb]:
        """
        List load balancers.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Load Balancer name to filter for.
        :param order_by: Sort order of Load Balancers in the response.
        :param page_size: Number of Load Balancers to return.
        :param page: Page number to return, from the paginated results.
        :param organization_id: Organization ID to filter for, only Load Balancers from this Organization will be returned.
        :param project_id: Project ID to filter for, only Load Balancers from this Project will be returned.
        :return: :class:`List[ListLbsResponse] <List[ListLbsResponse]>`

        Usage:
        ::

            result = await api.list_lbs_all()
        """

        return await fetch_all_pages_async(
            type=ListLbsResponse,
            key="lbs",
            fetcher=self.list_lbs,
            args={
                "region": region,
                "name": name,
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    async def create_lb(
        self,
        *,
        description: str,
        type_: str,
        ssl_compatibility_level: SSLCompatibilityLevel,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        ip_id: Optional[str] = None,
        assign_flexible_ip: Optional[bool] = None,
        tags: Optional[List[str]] = None,
    ) -> Lb:
        """
        Create a load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Scaleway Organization to create the Load Balancer in.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Scaleway Project to create the Load Balancer in.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param name: Name for the Load Balancer.
        :param description: Description for the Load Balancer.
        :param ip_id: ID of an existing flexible IP address to attach to the Load Balancer.
        :param assign_flexible_ip: Defines whether to automatically assign a flexible public IP to lb. Default value is `false` (do not assign).
        :param tags: List of tags for the Load Balancer.
        :param type_: Load Balancer commercial offer type. Use the Load Balancer types endpoint to retrieve a list of available offer types.
        :param ssl_compatibility_level: Determines the minimal SSL version which needs to be supported on the client side, in an SSL/TLS offloading context. Intermediate is suitable for general-purpose servers with a variety of clients, recommended for almost all systems. Modern is suitable for services with clients that support TLS 1.3 and do not need backward compatibility. Old is compatible with a small number of very old clients and should be used only as a last resort.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = await api.create_lb(
                description="example",
                type_="example",
                ssl_compatibility_level=ssl_compatibility_level_unknown,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/lbs",
            body=marshal_CreateLbRequest(
                CreateLbRequest(
                    description=description,
                    type_=type_,
                    ssl_compatibility_level=ssl_compatibility_level,
                    region=region,
                    organization_id=organization_id,
                    project_id=project_id,
                    name=name or random_name(prefix="lb"),
                    ip_id=ip_id,
                    assign_flexible_ip=assign_flexible_ip,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    async def get_lb(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
    ) -> Lb:
        """
        Get a load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = await api.get_lb(lb_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    async def wait_for_lb(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Lb, Union[bool, Awaitable[bool]]]] = None,
    ) -> Lb:
        """
        Waits for :class:`Lb <Lb>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID.
        :param options: The options for the waiter
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.wait_for_lb(lb_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in LB_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_lb,
            options=options,
            args={
                "lb_id": lb_id,
                "region": region,
            },
        )

    async def update_lb(
        self,
        *,
        lb_id: str,
        name: str,
        description: str,
        ssl_compatibility_level: SSLCompatibilityLevel,
        region: Optional[Region] = None,
        tags: Optional[List[str]] = None,
    ) -> Lb:
        """
        Update a load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID.
        :param name: Load Balancer name.
        :param description: Load Balancer description.
        :param tags: List of tags for the Load Balancer.
        :param ssl_compatibility_level: Determines the minimal SSL version which needs to be supported on the client side, in an SSL/TLS offloading context. Intermediate is suitable for general-purpose servers with a variety of clients, recommended for almost all systems. Modern is suitable for services with clients that support TLS 1.3 and don't need backward compatibility. Old is compatible with a small number of very old clients and should be used only as a last resort.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = await api.update_lb(
                lb_id="example",
                name="example",
                description="example",
                ssl_compatibility_level=ssl_compatibility_level_unknown,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "PUT",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}",
            body=marshal_UpdateLbRequest(
                UpdateLbRequest(
                    lb_id=lb_id,
                    name=name,
                    description=description,
                    ssl_compatibility_level=ssl_compatibility_level,
                    region=region,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    async def delete_lb(
        self,
        *,
        lb_id: str,
        release_ip: bool,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: ID of the Load Balancer to delete.
        :param release_ip: Defines whether the Load Balancer's flexible IP should be deleted. Set to true to release the flexible IP, or false to keep it available in your account for future Load Balancers.

        Usage:
        ::

            result = await api.delete_lb(
                lb_id="example",
                release_ip=True,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}",
            params={
                "release_ip": release_ip,
            },
        )

        self._throw_on_error(res)
        return None

    async def migrate_lb(
        self,
        *,
        lb_id: str,
        type_: str,
        region: Optional[Region] = None,
    ) -> Lb:
        """
        Migrate a load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID.
        :param type_: Load Balancer type to migrate to (use the List all Load Balancer offer types endpoint to get a list of available offer types).
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = await api.migrate_lb(
                lb_id="example",
                type_="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/migrate",
            body=marshal_MigrateLbRequest(
                MigrateLbRequest(
                    lb_id=lb_id,
                    type_=type_,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    async def list_i_ps(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        ip_address: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListIpsResponse:
        """
        List IPs.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of IP addresses to return.
        :param ip_address: IP address to filter for.
        :param organization_id: Organization ID to filter for, only Load Balancer IP addresses from this Organization will be returned.
        :param project_id: Project ID to filter for, only Load Balancer IP addresses from this Project will be returned.
        :return: :class:`ListIpsResponse <ListIpsResponse>`

        Usage:
        ::

            result = await api.list_i_ps()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/ips",
            params={
                "ip_address": ip_address,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListIpsResponse(res.json())

    async def list_i_ps_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        ip_address: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Ip]:
        """
        List IPs.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of IP addresses to return.
        :param ip_address: IP address to filter for.
        :param organization_id: Organization ID to filter for, only Load Balancer IP addresses from this Organization will be returned.
        :param project_id: Project ID to filter for, only Load Balancer IP addresses from this Project will be returned.
        :return: :class:`List[ListIpsResponse] <List[ListIpsResponse]>`

        Usage:
        ::

            result = await api.list_i_ps_all()
        """

        return await fetch_all_pages_async(
            type=ListIpsResponse,
            key="ips",
            fetcher=self.list_i_ps,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "ip_address": ip_address,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    async def create_ip(
        self,
        *,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        reverse: Optional[str] = None,
    ) -> Ip:
        """
        Create an IP.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Organization ID of the Organization where the IP address should be created.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Project ID of the Project where the IP address should be created.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param reverse: Reverse DNS (domain name) for the IP address.
        :return: :class:`Ip <Ip>`

        Usage:
        ::

            result = await api.create_ip()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/ips",
            body=marshal_CreateIpRequest(
                CreateIpRequest(
                    region=region,
                    organization_id=organization_id,
                    project_id=project_id,
                    reverse=reverse,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Ip(res.json())

    async def get_ip(
        self,
        *,
        ip_id: str,
        region: Optional[Region] = None,
    ) -> Ip:
        """
        Get an IP.
        :param region: Region to target. If none is passed will use default region from the config.
        :param ip_id: IP address ID.
        :return: :class:`Ip <Ip>`

        Usage:
        ::

            result = await api.get_ip(ip_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/ips/{param_ip_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Ip(res.json())

    async def release_ip(
        self,
        *,
        ip_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete an IP.
        :param region: Region to target. If none is passed will use default region from the config.
        :param ip_id: IP address ID.

        Usage:
        ::

            result = await api.release_ip(ip_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/ips/{param_ip_id}",
        )

        self._throw_on_error(res)
        return None

    async def update_ip(
        self,
        *,
        ip_id: str,
        region: Optional[Region] = None,
        reverse: Optional[str] = None,
    ) -> Ip:
        """
        Update an IP.
        :param region: Region to target. If none is passed will use default region from the config.
        :param ip_id: IP address ID.
        :param reverse: Reverse DNS (domain name) for the IP address.
        :return: :class:`Ip <Ip>`

        Usage:
        ::

            result = await api.update_ip(ip_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "PATCH",
            f"/lb/v1/regions/{param_region}/ips/{param_ip_id}",
            body=marshal_UpdateIpRequest(
                UpdateIpRequest(
                    ip_id=ip_id,
                    region=region,
                    reverse=reverse,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Ip(res.json())

    async def list_backends(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: ListBackendsRequestOrderBy = ListBackendsRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListBackendsResponse:
        """
        List backends in a given load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID.
        :param name: Name of the backend to filter for.
        :param order_by: Sort order of backends in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of backends to return.
        :return: :class:`ListBackendsResponse <ListBackendsResponse>`

        Usage:
        ::

            result = await api.list_backends(lb_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/backends",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListBackendsResponse(res.json())

    async def list_backends_all(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: Optional[ListBackendsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[Backend]:
        """
        List backends in a given load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID.
        :param name: Name of the backend to filter for.
        :param order_by: Sort order of backends in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of backends to return.
        :return: :class:`List[ListBackendsResponse] <List[ListBackendsResponse]>`

        Usage:
        ::

            result = await api.list_backends_all(lb_id="example")
        """

        return await fetch_all_pages_async(
            type=ListBackendsResponse,
            key="backends",
            fetcher=self.list_backends,
            args={
                "lb_id": lb_id,
                "region": region,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    async def create_backend(
        self,
        *,
        lb_id: str,
        forward_port: int,
        sticky_sessions_cookie_name: str,
        health_check: HealthCheck,
        server_ip: List[str],
        on_marked_down_action: OnMarkedDownAction,
        proxy_protocol: ProxyProtocol,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        forward_protocol: Protocol = Protocol.TCP,
        forward_port_algorithm: ForwardPortAlgorithm = ForwardPortAlgorithm.ROUNDROBIN,
        sticky_sessions: StickySessionsType = StickySessionsType.NONE,
        send_proxy_v2: Optional[bool] = None,
        timeout_server: Optional[str] = None,
        timeout_connect: Optional[str] = None,
        timeout_tunnel: Optional[str] = None,
        failover_host: Optional[str] = None,
        ssl_bridging: Optional[bool] = None,
        ignore_ssl_server_verify: Optional[bool] = None,
        redispatch_attempt_count: Optional[int] = None,
        max_retries: Optional[int] = None,
        max_connections: Optional[int] = None,
        timeout_queue: Optional[str] = None,
    ) -> Backend:
        """
        Create a backend in a given load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID.
        :param name: Name for the backend.
        :param forward_protocol: Protocol to be used by the backend when forwarding traffic to backend servers.
        :param forward_port: Port to be used by the backend when forwarding traffic to backend servers.
        :param forward_port_algorithm: Load balancing algorithm to be used when determining which backend server to forward new traffic to.
        :param sticky_sessions: Defines whether to activate sticky sessions (binding a particular session to a particular backend server) and the method to use if so. None disables sticky sessions. Cookie-based uses an HTTP cookie TO stick a session to a backend server. Table-based uses the source (client) IP address to stick a session to a backend server.
        :param sticky_sessions_cookie_name: Cookie name for cookie-based sticky sessions.
        :param health_check: Object defining the health check to be carried out by the backend when checking the status and health of backend servers.
        :param server_ip: List of backend server IP addresses (IPv4 or IPv6) the backend should forward traffic to.
        :param send_proxy_v2: Deprecated in favor of proxy_protocol field.
        :param timeout_server: Maximum allowed time for a backend server to process a request.
        :param timeout_connect: Maximum allowed time for establishing a connection to a backend server.
        :param timeout_tunnel: Maximum allowed tunnel inactivity time after Websocket is established (takes precedence over client and server timeout).
        :param on_marked_down_action: Action to take when a backend server is marked as down.
        :param proxy_protocol: Protocol to use between the Load Balancer and backend servers. Allows the backend servers to be informed of the client's real IP address. The PROXY protocol must be supported by the backend servers' software.
        :param failover_host: Scaleway S3 bucket website to be served as failover if all backend servers are down, e.g. failover-website.s3-website.fr-par.scw.cloud.
        :param ssl_bridging: Defines whether to enable SSL bridging between the Load Balancer and backend servers.
        :param ignore_ssl_server_verify: Defines whether the server certificate verification should be ignored.
        :param redispatch_attempt_count: Whether to use another backend server on each attempt.
        :param max_retries: Number of retries when a backend server connection failed.
        :param max_connections: Maximum number of connections allowed per backend server.
        :param timeout_queue: Maximum time for a request to be left pending in queue when `max_connections` is reached.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = await api.create_backend(
                lb_id="example",
                forward_port=1,
                sticky_sessions_cookie_name="example",
                health_check=HealthCheck(...),
                server_ip=["example"],
                on_marked_down_action=on_marked_down_action_none,
                proxy_protocol=proxy_protocol_unknown,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/backends",
            body=marshal_CreateBackendRequest(
                CreateBackendRequest(
                    lb_id=lb_id,
                    forward_port=forward_port,
                    sticky_sessions_cookie_name=sticky_sessions_cookie_name,
                    health_check=health_check,
                    server_ip=server_ip,
                    on_marked_down_action=on_marked_down_action,
                    proxy_protocol=proxy_protocol,
                    region=region,
                    name=name or random_name(prefix="lbb"),
                    forward_protocol=forward_protocol,
                    forward_port_algorithm=forward_port_algorithm,
                    sticky_sessions=sticky_sessions,
                    send_proxy_v2=send_proxy_v2,
                    timeout_server=timeout_server,
                    timeout_connect=timeout_connect,
                    timeout_tunnel=timeout_tunnel,
                    failover_host=failover_host,
                    ssl_bridging=ssl_bridging,
                    ignore_ssl_server_verify=ignore_ssl_server_verify,
                    redispatch_attempt_count=redispatch_attempt_count,
                    max_retries=max_retries,
                    max_connections=max_connections,
                    timeout_queue=timeout_queue,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    async def get_backend(
        self,
        *,
        backend_id: str,
        region: Optional[Region] = None,
    ) -> Backend:
        """
        Get a backend in a given load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param backend_id: Backend ID.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = await api.get_backend(backend_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/backends/{param_backend_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    async def update_backend(
        self,
        *,
        backend_id: str,
        name: str,
        forward_port: int,
        sticky_sessions_cookie_name: str,
        on_marked_down_action: OnMarkedDownAction,
        proxy_protocol: ProxyProtocol,
        region: Optional[Region] = None,
        forward_protocol: Protocol = Protocol.TCP,
        forward_port_algorithm: ForwardPortAlgorithm = ForwardPortAlgorithm.ROUNDROBIN,
        sticky_sessions: StickySessionsType = StickySessionsType.NONE,
        send_proxy_v2: Optional[bool] = None,
        timeout_server: Optional[str] = None,
        timeout_connect: Optional[str] = None,
        timeout_tunnel: Optional[str] = None,
        failover_host: Optional[str] = None,
        ssl_bridging: Optional[bool] = None,
        ignore_ssl_server_verify: Optional[bool] = None,
        redispatch_attempt_count: Optional[int] = None,
        max_retries: Optional[int] = None,
        max_connections: Optional[int] = None,
        timeout_queue: Optional[str] = None,
    ) -> Backend:
        """
        Update a backend in a given load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param backend_id: Backend ID.
        :param name: Backend name.
        :param forward_protocol: Protocol to be used by the backend when forwarding traffic to backend servers.
        :param forward_port: Port to be used by the backend when forwarding traffic to backend servers.
        :param forward_port_algorithm: Load balancing algorithm to be used when determining which backend server to forward new traffic to.
        :param sticky_sessions: Defines whether to activate sticky sessions (binding a particular session to a particular backend server) and the method to use if so. None disables sticky sessions. Cookie-based uses an HTTP cookie to stick a session to a backend server. Table-based uses the source (client) IP address to stick a session to a backend server.
        :param sticky_sessions_cookie_name: Cookie name for cookie-based sticky sessions.
        :param send_proxy_v2: Deprecated in favor of proxy_protocol field.
        :param timeout_server: Maximum allowed time for a backend server to process a request.
        :param timeout_connect: Maximum allowed time for establishing a connection to a backend server.
        :param timeout_tunnel: Maximum allowed tunnel inactivity time after Websocket is established (takes precedence over client and server timeout).
        :param on_marked_down_action: Action to take when a backend server is marked as down.
        :param proxy_protocol: Protocol to use between the Load Balancer and backend servers. Allows the backend servers to be informed of the client's real IP address. The PROXY protocol must be supported by the backend servers' software.
        :param failover_host: Scaleway S3 bucket website to be served as failover if all backend servers are down, e.g. failover-website.s3-website.fr-par.scw.cloud.
        :param ssl_bridging: Defines whether to enable SSL bridging between the Load Balancer and backend servers.
        :param ignore_ssl_server_verify: Defines whether the server certificate verification should be ignored.
        :param redispatch_attempt_count: Whether to use another backend server on each attempt.
        :param max_retries: Number of retries when a backend server connection failed.
        :param max_connections: Maximum number of connections allowed per backend server.
        :param timeout_queue: Maximum time for a request to be left pending in queue when `max_connections` is reached.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = await api.update_backend(
                backend_id="example",
                name="example",
                forward_port=1,
                sticky_sessions_cookie_name="example",
                on_marked_down_action=on_marked_down_action_none,
                proxy_protocol=proxy_protocol_unknown,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "PUT",
            f"/lb/v1/regions/{param_region}/backends/{param_backend_id}",
            body=marshal_UpdateBackendRequest(
                UpdateBackendRequest(
                    backend_id=backend_id,
                    name=name,
                    forward_port=forward_port,
                    sticky_sessions_cookie_name=sticky_sessions_cookie_name,
                    on_marked_down_action=on_marked_down_action,
                    proxy_protocol=proxy_protocol,
                    region=region,
                    forward_protocol=forward_protocol,
                    forward_port_algorithm=forward_port_algorithm,
                    sticky_sessions=sticky_sessions,
                    send_proxy_v2=send_proxy_v2,
                    timeout_server=timeout_server,
                    timeout_connect=timeout_connect,
                    timeout_tunnel=timeout_tunnel,
                    failover_host=failover_host,
                    ssl_bridging=ssl_bridging,
                    ignore_ssl_server_verify=ignore_ssl_server_verify,
                    redispatch_attempt_count=redispatch_attempt_count,
                    max_retries=max_retries,
                    max_connections=max_connections,
                    timeout_queue=timeout_queue,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    async def delete_backend(
        self,
        *,
        backend_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a backend in a given load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param backend_id: ID of the backend to delete.

        Usage:
        ::

            result = await api.delete_backend(backend_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/backends/{param_backend_id}",
        )

        self._throw_on_error(res)
        return None

    async def add_backend_servers(
        self,
        *,
        backend_id: str,
        server_ip: List[str],
        region: Optional[Region] = None,
    ) -> Backend:
        """
        Add a set of servers in a given backend.
        :param region: Region to target. If none is passed will use default region from the config.
        :param backend_id: Backend ID.
        :param server_ip: List of IP addresses to add to backend servers.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = await api.add_backend_servers(
                backend_id="example",
                server_ip=["example"],
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/backends/{param_backend_id}/servers",
            body=marshal_AddBackendServersRequest(
                AddBackendServersRequest(
                    backend_id=backend_id,
                    server_ip=server_ip,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    async def remove_backend_servers(
        self,
        *,
        backend_id: str,
        server_ip: List[str],
        region: Optional[Region] = None,
    ) -> Backend:
        """
        Remove a set of servers for a given backend.
        :param region: Region to target. If none is passed will use default region from the config.
        :param backend_id: Backend ID.
        :param server_ip: List of IP addresses to remove from backend servers.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = await api.remove_backend_servers(
                backend_id="example",
                server_ip=["example"],
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/backends/{param_backend_id}/servers",
            body=marshal_RemoveBackendServersRequest(
                RemoveBackendServersRequest(
                    backend_id=backend_id,
                    server_ip=server_ip,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    async def set_backend_servers(
        self,
        *,
        backend_id: str,
        server_ip: List[str],
        region: Optional[Region] = None,
    ) -> Backend:
        """
        Define all servers in a given backend.
        :param region: Region to target. If none is passed will use default region from the config.
        :param backend_id: Backend ID.
        :param server_ip: List of IP addresses for backend servers. Any other existing backend servers will be removed.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = await api.set_backend_servers(
                backend_id="example",
                server_ip=["example"],
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "PUT",
            f"/lb/v1/regions/{param_region}/backends/{param_backend_id}/servers",
            body=marshal_SetBackendServersRequest(
                SetBackendServersRequest(
                    backend_id=backend_id,
                    server_ip=server_ip,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    async def update_health_check(
        self,
        *,
        backend_id: str,
        port: int,
        check_delay: str,
        check_timeout: str,
        check_max_retries: int,
        check_send_proxy: bool,
        region: Optional[Region] = None,
        tcp_config: Optional[HealthCheckTcpConfig] = None,
        mysql_config: Optional[HealthCheckMysqlConfig] = None,
        pgsql_config: Optional[HealthCheckPgsqlConfig] = None,
        ldap_config: Optional[HealthCheckLdapConfig] = None,
        redis_config: Optional[HealthCheckRedisConfig] = None,
        http_config: Optional[HealthCheckHttpConfig] = None,
        https_config: Optional[HealthCheckHttpsConfig] = None,
        transient_check_delay: Optional[str] = None,
    ) -> HealthCheck:
        """
        Update an health check for a given backend.
        :param region: Region to target. If none is passed will use default region from the config.
        :param backend_id: Backend ID.
        :param port: Port to use for the backend server health check.
        :param check_delay: Time to wait between two consecutive health checks.
        :param check_timeout: Maximum time a backend server has to reply to the health check.
        :param check_max_retries: Number of consecutive unsuccessful health checks after which the server will be considered dead.
        :param check_send_proxy: Defines whether proxy protocol should be activated for the health check.
        :param tcp_config: Object to configure a basic TCP health check.

        One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
        :param mysql_config: Object to configure a MySQL health check. The check requires MySQL >=3.22, for older versions, use a TCP health check.

        One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
        :param pgsql_config: Object to configure a PostgreSQL health check.

        One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
        :param ldap_config: Object to configure an LDAP health check. The response is analyzed to find the LDAPv3 response message.

        One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
        :param redis_config: Object to configure a Redis health check. The response is analyzed to find the +PONG response message.

        One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
        :param http_config: Object to configure an HTTP health check.

        One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
        :param https_config: Object to configure an HTTPS health check.

        One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
        :param transient_check_delay: Time to wait between two consecutive health checks when a backend server is in a transient state (going UP or DOWN).
        :return: :class:`HealthCheck <HealthCheck>`

        Usage:
        ::

            result = await api.update_health_check(
                backend_id="example",
                port=1,
                check_delay="example",
                check_timeout="example",
                check_max_retries=1,
                check_send_proxy=True,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "PUT",
            f"/lb/v1/regions/{param_region}/backends/{param_backend_id}/healthcheck",
            body=marshal_UpdateHealthCheckRequest(
                UpdateHealthCheckRequest(
                    backend_id=backend_id,
                    port=port,
                    check_delay=check_delay,
                    check_timeout=check_timeout,
                    check_max_retries=check_max_retries,
                    check_send_proxy=check_send_proxy,
                    region=region,
                    tcp_config=tcp_config,
                    mysql_config=mysql_config,
                    pgsql_config=pgsql_config,
                    ldap_config=ldap_config,
                    redis_config=redis_config,
                    http_config=http_config,
                    https_config=https_config,
                    transient_check_delay=transient_check_delay,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_HealthCheck(res.json())

    async def list_frontends(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: ListFrontendsRequestOrderBy = ListFrontendsRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListFrontendsResponse:
        """
        List frontends in a given load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID.
        :param name: Name of the frontend to filter for.
        :param order_by: Sort order of frontends in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of frontends to return.
        :return: :class:`ListFrontendsResponse <ListFrontendsResponse>`

        Usage:
        ::

            result = await api.list_frontends(lb_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/frontends",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListFrontendsResponse(res.json())

    async def list_frontends_all(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        order_by: Optional[ListFrontendsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[Frontend]:
        """
        List frontends in a given load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID.
        :param name: Name of the frontend to filter for.
        :param order_by: Sort order of frontends in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of frontends to return.
        :return: :class:`List[ListFrontendsResponse] <List[ListFrontendsResponse]>`

        Usage:
        ::

            result = await api.list_frontends_all(lb_id="example")
        """

        return await fetch_all_pages_async(
            type=ListFrontendsResponse,
            key="frontends",
            fetcher=self.list_frontends,
            args={
                "lb_id": lb_id,
                "region": region,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    async def create_frontend(
        self,
        *,
        lb_id: str,
        inbound_port: int,
        backend_id: str,
        enable_http3: bool,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        timeout_client: Optional[str] = None,
        certificate_id: Optional[str] = None,
        certificate_ids: Optional[List[str]] = None,
    ) -> Frontend:
        """
        Create a frontend in a given load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID (ID of the Load Balancer to attach the frontend to).
        :param name: Name for the frontend.
        :param inbound_port: Port the frontend should listen on.
        :param backend_id: Backend ID (ID of the backend the frontend should pass traffic to).
        :param timeout_client: Maximum allowed inactivity time on the client side.
        :param certificate_id: Certificate ID, deprecated in favor of certificate_ids array.
        :param certificate_ids: List of SSL/TLS certificate IDs to bind to the frontend.
        :param enable_http3: Defines whether to enable HTTP/3 protocol on the frontend.
        :return: :class:`Frontend <Frontend>`

        Usage:
        ::

            result = await api.create_frontend(
                lb_id="example",
                inbound_port=1,
                backend_id="example",
                enable_http3=True,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/frontends",
            body=marshal_CreateFrontendRequest(
                CreateFrontendRequest(
                    lb_id=lb_id,
                    inbound_port=inbound_port,
                    backend_id=backend_id,
                    enable_http3=enable_http3,
                    region=region,
                    name=name or random_name(prefix="lbf"),
                    timeout_client=timeout_client,
                    certificate_id=certificate_id,
                    certificate_ids=certificate_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Frontend(res.json())

    async def get_frontend(
        self,
        *,
        frontend_id: str,
        region: Optional[Region] = None,
    ) -> Frontend:
        """
        Get a frontend.
        :param region: Region to target. If none is passed will use default region from the config.
        :param frontend_id: Frontend ID.
        :return: :class:`Frontend <Frontend>`

        Usage:
        ::

            result = await api.get_frontend(frontend_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/frontends/{param_frontend_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Frontend(res.json())

    async def update_frontend(
        self,
        *,
        frontend_id: str,
        name: str,
        inbound_port: int,
        backend_id: str,
        enable_http3: bool,
        region: Optional[Region] = None,
        timeout_client: Optional[str] = None,
        certificate_id: Optional[str] = None,
        certificate_ids: Optional[List[str]] = None,
    ) -> Frontend:
        """
        Update a frontend.
        :param region: Region to target. If none is passed will use default region from the config.
        :param frontend_id: Frontend ID.
        :param name: Frontend name.
        :param inbound_port: Port the frontend should listen on.
        :param backend_id: Backend ID (ID of the backend the frontend should pass traffic to).
        :param timeout_client: Maximum allowed inactivity time on the client side.
        :param certificate_id: Certificate ID, deprecated in favor of certificate_ids array.
        :param certificate_ids: List of SSL/TLS certificate IDs to bind to the frontend.
        :param enable_http3: Defines whether to enable HTTP/3 protocol on the frontend.
        :return: :class:`Frontend <Frontend>`

        Usage:
        ::

            result = await api.update_frontend(
                frontend_id="example",
                name="example",
                inbound_port=1,
                backend_id="example",
                enable_http3=True,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "PUT",
            f"/lb/v1/regions/{param_region}/frontends/{param_frontend_id}",
            body=marshal_UpdateFrontendRequest(
                UpdateFrontendRequest(
                    frontend_id=frontend_id,
                    name=name,
                    inbound_port=inbound_port,
                    backend_id=backend_id,
                    enable_http3=enable_http3,
                    region=region,
                    timeout_client=timeout_client,
                    certificate_id=certificate_id,
                    certificate_ids=certificate_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Frontend(res.json())

    async def delete_frontend(
        self,
        *,
        frontend_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a frontend.
        :param region: Region to target. If none is passed will use default region from the config.
        :param frontend_id: ID of the frontend to delete.

        Usage:
        ::

            result = await api.delete_frontend(frontend_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/frontends/{param_frontend_id}",
        )

        self._throw_on_error(res)
        return None

    async def list_routes(
        self,
        *,
        region: Optional[Region] = None,
        order_by: ListRoutesRequestOrderBy = ListRoutesRequestOrderBy.CREATED_AT_ASC,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        frontend_id: Optional[str] = None,
    ) -> ListRoutesResponse:
        """
        List all backend redirections.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of routes in the response.
        :param page_size: The number of route objects to return.
        :param page: The page number to return, from the paginated results.
        :param frontend_id: Frontend ID to filter for, only Routes from this Frontend will be returned.
        :return: :class:`ListRoutesResponse <ListRoutesResponse>`

        Usage:
        ::

            result = await api.list_routes()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/routes",
            params={
                "frontend_id": frontend_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRoutesResponse(res.json())

    async def list_routes_all(
        self,
        *,
        region: Optional[Region] = None,
        order_by: Optional[ListRoutesRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        frontend_id: Optional[str] = None,
    ) -> List[Route]:
        """
        List all backend redirections.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of routes in the response.
        :param page_size: The number of route objects to return.
        :param page: The page number to return, from the paginated results.
        :param frontend_id: Frontend ID to filter for, only Routes from this Frontend will be returned.
        :return: :class:`List[ListRoutesResponse] <List[ListRoutesResponse]>`

        Usage:
        ::

            result = await api.list_routes_all()
        """

        return await fetch_all_pages_async(
            type=ListRoutesResponse,
            key="routes",
            fetcher=self.list_routes,
            args={
                "region": region,
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
                "frontend_id": frontend_id,
            },
        )

    async def create_route(
        self,
        *,
        frontend_id: str,
        backend_id: str,
        region: Optional[Region] = None,
        match: Optional[RouteMatch] = None,
    ) -> Route:
        """
        Create a backend redirection.
        :param region: Region to target. If none is passed will use default region from the config.
        :param frontend_id: ID of the source frontend to create the route on.
        :param backend_id: ID of the target backend for the route.
        :param match: Object defining the match condition for a route to be applied. If an incoming client session matches the specified condition (i.e. it has a matching SNI value or HTTP Host header value), it will be passed to the target backend.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = await api.create_route(
                frontend_id="example",
                backend_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/routes",
            body=marshal_CreateRouteRequest(
                CreateRouteRequest(
                    frontend_id=frontend_id,
                    backend_id=backend_id,
                    region=region,
                    match=match,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    async def get_route(
        self,
        *,
        route_id: str,
        region: Optional[Region] = None,
    ) -> Route:
        """
        Get single backend redirection.
        :param region: Region to target. If none is passed will use default region from the config.
        :param route_id: Route ID.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = await api.get_route(route_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/routes/{param_route_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    async def update_route(
        self,
        *,
        route_id: str,
        backend_id: str,
        region: Optional[Region] = None,
        match: Optional[RouteMatch] = None,
    ) -> Route:
        """
        Edit a backend redirection.
        :param region: Region to target. If none is passed will use default region from the config.
        :param route_id: Route ID.
        :param backend_id: ID of the target backend for the route.
        :param match: Object defining the match condition for a route to be applied. If an incoming client session matches the specified condition (i.e. it has a matching SNI value or HTTP Host header value), it will be passed to the target backend.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = await api.update_route(
                route_id="example",
                backend_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "PUT",
            f"/lb/v1/regions/{param_region}/routes/{param_route_id}",
            body=marshal_UpdateRouteRequest(
                UpdateRouteRequest(
                    route_id=route_id,
                    backend_id=backend_id,
                    region=region,
                    match=match,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    async def delete_route(
        self,
        *,
        route_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a backend redirection.
        :param region: Region to target. If none is passed will use default region from the config.
        :param route_id: Route ID.

        Usage:
        ::

            result = await api.delete_route(route_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/routes/{param_route_id}",
        )

        self._throw_on_error(res)
        return None

    async def get_lb_stats(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        backend_id: Optional[str] = None,
    ) -> LbStats:
        """
        Get usage statistics of a given load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID.
        :param backend_id: ID of the backend.
        :return: :class:`LbStats <LbStats>`
        :deprecated

        Usage:
        ::

            result = await api.get_lb_stats(lb_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/stats",
            params={
                "backend_id": backend_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_LbStats(res.json())

    async def list_backend_stats(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        backend_id: Optional[str] = None,
    ) -> ListBackendStatsResponse:
        """

        Usage:
        ::

            result = await api.list_backend_stats(lb_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/backend-stats",
            params={
                "backend_id": backend_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListBackendStatsResponse(res.json())

    async def list_backend_stats_all(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        backend_id: Optional[str] = None,
    ) -> List[BackendServerStats]:
        """
        :return: :class:`List[ListBackendStatsResponse] <List[ListBackendStatsResponse]>`

        Usage:
        ::

            result = await api.list_backend_stats_all(lb_id="example")
        """

        return await fetch_all_pages_async(
            type=ListBackendStatsResponse,
            key="backend_servers_stats",
            fetcher=self.list_backend_stats,
            args={
                "lb_id": lb_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "backend_id": backend_id,
            },
        )

    async def list_acls(
        self,
        *,
        frontend_id: str,
        region: Optional[Region] = None,
        order_by: ListAclRequestOrderBy = ListAclRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
    ) -> ListAclResponse:
        """
        List ACL for a given frontend.
        :param region: Region to target. If none is passed will use default region from the config.
        :param frontend_id: Frontend ID (ACLs attached to this frontend will be returned in the response).
        :param order_by: Sort order of ACLs in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of ACLs to return.
        :param name: ACL name to filter for.
        :return: :class:`ListAclResponse <ListAclResponse>`

        Usage:
        ::

            result = await api.list_acls(frontend_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/frontends/{param_frontend_id}/acls",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListAclResponse(res.json())

    async def list_acls_all(
        self,
        *,
        frontend_id: str,
        region: Optional[Region] = None,
        order_by: Optional[ListAclRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
    ) -> List[Acl]:
        """
        List ACL for a given frontend.
        :param region: Region to target. If none is passed will use default region from the config.
        :param frontend_id: Frontend ID (ACLs attached to this frontend will be returned in the response).
        :param order_by: Sort order of ACLs in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of ACLs to return.
        :param name: ACL name to filter for.
        :return: :class:`List[ListAclResponse] <List[ListAclResponse]>`

        Usage:
        ::

            result = await api.list_acls_all(frontend_id="example")
        """

        return await fetch_all_pages_async(
            type=ListAclResponse,
            key="acls",
            fetcher=self.list_acls,
            args={
                "frontend_id": frontend_id,
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
            },
        )

    async def create_acl(
        self,
        *,
        frontend_id: str,
        action: AclAction,
        index: int,
        description: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        match: Optional[AclMatch] = None,
    ) -> Acl:
        """
        Create an ACL for a given frontend.
        :param region: Region to target. If none is passed will use default region from the config.
        :param frontend_id: Frontend ID to attach the ACL to.
        :param name: ACL name.
        :param action: Action to take when incoming traffic matches an ACL filter.
        :param match: ACL match filter object. One of `ip_subnet` or `http_filter` & `http_filter_value` are required.
        :param index: Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
        :param description: ACL description.
        :return: :class:`Acl <Acl>`

        Usage:
        ::

            result = await api.create_acl(
                frontend_id="example",
                action=AclAction(...),
                index=1,
                description="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/frontends/{param_frontend_id}/acls",
            body=marshal_CreateAclRequest(
                CreateAclRequest(
                    frontend_id=frontend_id,
                    action=action,
                    index=index,
                    description=description,
                    region=region,
                    name=name or random_name(prefix="acl"),
                    match=match,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Acl(res.json())

    async def get_acl(
        self,
        *,
        acl_id: str,
        region: Optional[Region] = None,
    ) -> Acl:
        """
        Get an ACL.
        :param region: Region to target. If none is passed will use default region from the config.
        :param acl_id: ACL ID.
        :return: :class:`Acl <Acl>`

        Usage:
        ::

            result = await api.get_acl(acl_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_acl_id = validate_path_param("acl_id", acl_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/acls/{param_acl_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Acl(res.json())

    async def update_acl(
        self,
        *,
        acl_id: str,
        name: str,
        action: AclAction,
        index: int,
        region: Optional[Region] = None,
        match: Optional[AclMatch] = None,
        description: Optional[str] = None,
    ) -> Acl:
        """
        Update an ACL.
        :param region: Region to target. If none is passed will use default region from the config.
        :param acl_id: ACL ID.
        :param name: ACL name.
        :param action: Action to take when incoming traffic matches an ACL filter.
        :param match: ACL match filter object. One of `ip_subnet` or `http_filter` & `http_filter_value` are required.
        :param index: Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
        :param description: ACL description.
        :return: :class:`Acl <Acl>`

        Usage:
        ::

            result = await api.update_acl(
                acl_id="example",
                name="example",
                action=AclAction(...),
                index=1,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_acl_id = validate_path_param("acl_id", acl_id)

        res = self._request(
            "PUT",
            f"/lb/v1/regions/{param_region}/acls/{param_acl_id}",
            body=marshal_UpdateAclRequest(
                UpdateAclRequest(
                    acl_id=acl_id,
                    name=name,
                    action=action,
                    index=index,
                    region=region,
                    match=match,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Acl(res.json())

    async def delete_acl(
        self,
        *,
        acl_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete an ACL.
        :param region: Region to target. If none is passed will use default region from the config.
        :param acl_id: ACL ID.

        Usage:
        ::

            result = await api.delete_acl(acl_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_acl_id = validate_path_param("acl_id", acl_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/acls/{param_acl_id}",
        )

        self._throw_on_error(res)
        return None

    async def create_certificate(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        letsencrypt: Optional[CreateCertificateRequestLetsencryptConfig] = None,
        custom_certificate: Optional[CreateCertificateRequestCustomCertificate] = None,
    ) -> Certificate:
        """
        Create a TLS certificate.
        Generate a new TLS certificate using Let's Encrypt or import your certificate.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID.
        :param name: Name for the certificate.
        :param letsencrypt: Object to define a new Let's Encrypt certificate to be generated.

        One-of ('type_'): at most one of 'letsencrypt', 'custom_certificate' could be set.
        :param custom_certificate: Object to define an existing custom certificate to be imported.

        One-of ('type_'): at most one of 'letsencrypt', 'custom_certificate' could be set.
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = await api.create_certificate(lb_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/certificates",
            body=marshal_CreateCertificateRequest(
                CreateCertificateRequest(
                    lb_id=lb_id,
                    region=region,
                    name=name or random_name(prefix="certificate"),
                    letsencrypt=letsencrypt,
                    custom_certificate=custom_certificate,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Certificate(res.json())

    async def list_certificates(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        order_by: ListCertificatesRequestOrderBy = ListCertificatesRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
    ) -> ListCertificatesResponse:
        """
        List all TLS certificates on a given load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID.
        :param order_by: Sort order of certificates in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of certificates to return.
        :param name: Certificate name to filter for, only certificates of this name will be returned.
        :return: :class:`ListCertificatesResponse <ListCertificatesResponse>`

        Usage:
        ::

            result = await api.list_certificates(lb_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/certificates",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListCertificatesResponse(res.json())

    async def list_certificates_all(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        order_by: Optional[ListCertificatesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
    ) -> List[Certificate]:
        """
        List all TLS certificates on a given load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID.
        :param order_by: Sort order of certificates in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of certificates to return.
        :param name: Certificate name to filter for, only certificates of this name will be returned.
        :return: :class:`List[ListCertificatesResponse] <List[ListCertificatesResponse]>`

        Usage:
        ::

            result = await api.list_certificates_all(lb_id="example")
        """

        return await fetch_all_pages_async(
            type=ListCertificatesResponse,
            key="certificates",
            fetcher=self.list_certificates,
            args={
                "lb_id": lb_id,
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
            },
        )

    async def get_certificate(
        self,
        *,
        certificate_id: str,
        region: Optional[Region] = None,
    ) -> Certificate:
        """
        Get a TLS certificate.
        :param region: Region to target. If none is passed will use default region from the config.
        :param certificate_id: Certificate ID.
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = await api.get_certificate(certificate_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_certificate_id = validate_path_param("certificate_id", certificate_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/certificates/{param_certificate_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Certificate(res.json())

    async def wait_for_certificate(
        self,
        *,
        certificate_id: str,
        region: Optional[Region] = None,
        options: Optional[
            WaitForOptions[Certificate, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> Certificate:
        """
        Waits for :class:`Certificate <Certificate>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config.
        :param certificate_id: Certificate ID.
        :param options: The options for the waiter
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = api.wait_for_certificate(certificate_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in CERTIFICATE_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_certificate,
            options=options,
            args={
                "certificate_id": certificate_id,
                "region": region,
            },
        )

    async def update_certificate(
        self,
        *,
        certificate_id: str,
        name: str,
        region: Optional[Region] = None,
    ) -> Certificate:
        """
        Update a TLS certificate.
        :param region: Region to target. If none is passed will use default region from the config.
        :param certificate_id: Certificate ID.
        :param name: Certificate name.
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = await api.update_certificate(
                certificate_id="example",
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_certificate_id = validate_path_param("certificate_id", certificate_id)

        res = self._request(
            "PUT",
            f"/lb/v1/regions/{param_region}/certificates/{param_certificate_id}",
            body=marshal_UpdateCertificateRequest(
                UpdateCertificateRequest(
                    certificate_id=certificate_id,
                    name=name,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Certificate(res.json())

    async def delete_certificate(
        self,
        *,
        certificate_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a TLS certificate.
        :param region: Region to target. If none is passed will use default region from the config.
        :param certificate_id: Certificate ID.

        Usage:
        ::

            result = await api.delete_certificate(certificate_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_certificate_id = validate_path_param("certificate_id", certificate_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/certificates/{param_certificate_id}",
        )

        self._throw_on_error(res)
        return None

    async def list_lb_types(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListLbTypesResponse:
        """
        List all load balancer offer type.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of items to return.
        :return: :class:`ListLbTypesResponse <ListLbTypesResponse>`

        Usage:
        ::

            result = await api.list_lb_types()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lb-types",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListLbTypesResponse(res.json())

    async def list_lb_types_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[LbType]:
        """
        List all load balancer offer type.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of items to return.
        :return: :class:`List[ListLbTypesResponse] <List[ListLbTypesResponse]>`

        Usage:
        ::

            result = await api.list_lb_types_all()
        """

        return await fetch_all_pages_async(
            type=ListLbTypesResponse,
            key="lb_types",
            fetcher=self.list_lb_types,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
            },
        )

    async def create_subscriber(
        self,
        *,
        name: str,
        region: Optional[Region] = None,
        email_config: Optional[SubscriberEmailConfig] = None,
        webhook_config: Optional[SubscriberWebhookConfig] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> Subscriber:
        """
        Create a subscriber, webhook or email.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Subscriber name.
        :param email_config: Email address configuration.

        One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
        :param webhook_config: WebHook URI configuration.

        One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
        :param organization_id: Organization ID to create the subscriber in.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Project ID to create the subscriber in.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :return: :class:`Subscriber <Subscriber>`

        Usage:
        ::

            result = await api.create_subscriber(name="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/subscribers",
            body=marshal_CreateSubscriberRequest(
                CreateSubscriberRequest(
                    name=name,
                    region=region,
                    email_config=email_config,
                    webhook_config=webhook_config,
                    organization_id=organization_id,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Subscriber(res.json())

    async def get_subscriber(
        self,
        *,
        subscriber_id: str,
        region: Optional[Region] = None,
    ) -> Subscriber:
        """
        Get a subscriber.
        :param region: Region to target. If none is passed will use default region from the config.
        :param subscriber_id: Subscriber ID.
        :return: :class:`Subscriber <Subscriber>`

        Usage:
        ::

            result = await api.get_subscriber(subscriber_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_subscriber_id = validate_path_param("subscriber_id", subscriber_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/subscribers/{param_subscriber_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Subscriber(res.json())

    async def list_subscriber(
        self,
        *,
        name: str,
        region: Optional[Region] = None,
        order_by: ListSubscriberRequestOrderBy = ListSubscriberRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListSubscriberResponse:
        """
        List all subscriber.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of subscribers in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of items to return.
        :param name: Subscriber name to search for.
        :param organization_id: Filter subscribers by Organization ID.
        :param project_id: Filter subscribers by Project ID.
        :return: :class:`ListSubscriberResponse <ListSubscriberResponse>`

        Usage:
        ::

            result = await api.list_subscriber(name="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/subscribers",
            params={
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
        return unmarshal_ListSubscriberResponse(res.json())

    async def list_subscriber_all(
        self,
        *,
        name: str,
        region: Optional[Region] = None,
        order_by: Optional[ListSubscriberRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Subscriber]:
        """
        List all subscriber.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Sort order of subscribers in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of items to return.
        :param name: Subscriber name to search for.
        :param organization_id: Filter subscribers by Organization ID.
        :param project_id: Filter subscribers by Project ID.
        :return: :class:`List[ListSubscriberResponse] <List[ListSubscriberResponse]>`

        Usage:
        ::

            result = await api.list_subscriber_all(name="example")
        """

        return await fetch_all_pages_async(
            type=ListSubscriberResponse,
            key="subscribers",
            fetcher=self.list_subscriber,
            args={
                "name": name,
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    async def update_subscriber(
        self,
        *,
        subscriber_id: str,
        name: str,
        region: Optional[Region] = None,
        email_config: Optional[SubscriberEmailConfig] = None,
        webhook_config: Optional[SubscriberWebhookConfig] = None,
    ) -> Subscriber:
        """
        Update a subscriber.
        :param region: Region to target. If none is passed will use default region from the config.
        :param subscriber_id: Subscriber ID.
        :param name: Subscriber name.
        :param email_config: Email address configuration.

        One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
        :param webhook_config: Webhook URI configuration.

        One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
        :return: :class:`Subscriber <Subscriber>`

        Usage:
        ::

            result = await api.update_subscriber(
                subscriber_id="example",
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_subscriber_id = validate_path_param("subscriber_id", subscriber_id)

        res = self._request(
            "PUT",
            f"/lb/v1/regions/{param_region}/subscribers/{param_subscriber_id}",
            body=marshal_UpdateSubscriberRequest(
                UpdateSubscriberRequest(
                    subscriber_id=subscriber_id,
                    name=name,
                    region=region,
                    email_config=email_config,
                    webhook_config=webhook_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Subscriber(res.json())

    async def delete_subscriber(
        self,
        *,
        subscriber_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a subscriber.
        :param region: Region to target. If none is passed will use default region from the config.
        :param subscriber_id: Subscriber ID.

        Usage:
        ::

            result = await api.delete_subscriber(subscriber_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_subscriber_id = validate_path_param("subscriber_id", subscriber_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/lb/subscriber/{param_subscriber_id}",
        )

        self._throw_on_error(res)
        return None

    async def subscribe_to_lb(
        self,
        *,
        lb_id: str,
        subscriber_id: str,
        region: Optional[Region] = None,
    ) -> Lb:
        """
        Subscribe a subscriber to a given load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID.
        :param subscriber_id: Subscriber ID.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = await api.subscribe_to_lb(
                lb_id="example",
                subscriber_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/lb/{param_lb_id}/subscribe",
            body=marshal_SubscribeToLbRequest(
                SubscribeToLbRequest(
                    lb_id=lb_id,
                    subscriber_id=subscriber_id,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    async def unsubscribe_from_lb(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
    ) -> Lb:
        """
        Unsubscribe a subscriber from a given load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = await api.unsubscribe_from_lb(lb_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/regions/{param_region}/lb/{param_lb_id}/unsubscribe",
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    async def list_lb_private_networks(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        order_by: ListPrivateNetworksRequestOrderBy = ListPrivateNetworksRequestOrderBy.CREATED_AT_ASC,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListLbPrivateNetworksResponse:
        """
        List attached private network of load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID.
        :param order_by: Sort order of Private Network objects in the response.
        :param page_size: Number of objects to return.
        :param page: The page number to return, from the paginated results.
        :return: :class:`ListLbPrivateNetworksResponse <ListLbPrivateNetworksResponse>`

        Usage:
        ::

            result = await api.list_lb_private_networks(lb_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/private-networks",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListLbPrivateNetworksResponse(res.json())

    async def list_lb_private_networks_all(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        order_by: Optional[ListPrivateNetworksRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[PrivateNetwork]:
        """
        List attached private network of load balancer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID.
        :param order_by: Sort order of Private Network objects in the response.
        :param page_size: Number of objects to return.
        :param page: The page number to return, from the paginated results.
        :return: :class:`List[ListLbPrivateNetworksResponse] <List[ListLbPrivateNetworksResponse]>`

        Usage:
        ::

            result = await api.list_lb_private_networks_all(lb_id="example")
        """

        return await fetch_all_pages_async(
            type=ListLbPrivateNetworksResponse,
            key="private_network",
            fetcher=self.list_lb_private_networks,
            args={
                "lb_id": lb_id,
                "region": region,
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
            },
        )

    async def attach_private_network(
        self,
        *,
        lb_id: str,
        private_network_id: str,
        region: Optional[Region] = None,
        static_config: Optional[PrivateNetworkStaticConfig] = None,
        dhcp_config: Optional[PrivateNetworkDHCPConfig] = None,
        ipam_config: Optional[PrivateNetworkIpamConfig] = None,
    ) -> PrivateNetwork:
        """
        Add load balancer on instance private network.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load Balancer ID.
        :param private_network_id: Private Network ID.
        :param static_config: Object containing an array of a local IP address for the Load Balancer on this Private Network.

        One-of ('config'): at most one of 'static_config', 'dhcp_config', 'ipam_config' could be set.
        :param dhcp_config: Defines whether to let DHCP assign IP addresses.

        One-of ('config'): at most one of 'static_config', 'dhcp_config', 'ipam_config' could be set.
        :param ipam_config: For internal use only.

        One-of ('config'): at most one of 'static_config', 'dhcp_config', 'ipam_config' could be set.
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = await api.attach_private_network(
                lb_id="example",
                private_network_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/private-networks/{param_private_network_id}/attach",
            body=marshal_AttachPrivateNetworkRequest(
                AttachPrivateNetworkRequest(
                    lb_id=lb_id,
                    private_network_id=private_network_id,
                    region=region,
                    static_config=static_config,
                    dhcp_config=dhcp_config,
                    ipam_config=ipam_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PrivateNetwork(res.json())

    async def detach_private_network(
        self,
        *,
        lb_id: str,
        private_network_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Remove load balancer of private network.
        :param region: Region to target. If none is passed will use default region from the config.
        :param lb_id: Load balancer ID.
        :param private_network_id: Set your instance private network id.

        Usage:
        ::

            result = await api.detach_private_network(
                lb_id="example",
                private_network_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "POST",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/private-networks/{param_private_network_id}/detach",
        )

        self._throw_on_error(res)
        return None


class LbZonedV1API(API):
    """
    Load Balancer API.

    This API allows you to manage your Scaleway Load Balancer services.
    Load Balancer API.
    """

    async def list_lbs(
        self,
        *,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        order_by: ListLbsRequestOrderBy = ListLbsRequestOrderBy.CREATED_AT_ASC,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListLbsResponse:
        """
        List Load Balancers.
        List all Load Balancers in the specified zone, for a Scaleway Organization or Scaleway Project. By default, the Load Balancers returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Load Balancer name to filter for.
        :param order_by: Sort order of Load Balancers in the response.
        :param page_size: Number of Load Balancers to return.
        :param page: Page number to return, from the paginated results.
        :param organization_id: Organization ID to filter for, only Load Balancers from this Organization will be returned.
        :param project_id: Project ID to filter for, only Load Balancers from this Project will be returned.
        :return: :class:`ListLbsResponse <ListLbsResponse>`

        Usage:
        ::

            result = await api.list_lbs()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs",
            params={
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
        return unmarshal_ListLbsResponse(res.json())

    async def list_lbs_all(
        self,
        *,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        order_by: Optional[ListLbsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Lb]:
        """
        List Load Balancers.
        List all Load Balancers in the specified zone, for a Scaleway Organization or Scaleway Project. By default, the Load Balancers returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Load Balancer name to filter for.
        :param order_by: Sort order of Load Balancers in the response.
        :param page_size: Number of Load Balancers to return.
        :param page: Page number to return, from the paginated results.
        :param organization_id: Organization ID to filter for, only Load Balancers from this Organization will be returned.
        :param project_id: Project ID to filter for, only Load Balancers from this Project will be returned.
        :return: :class:`List[ListLbsResponse] <List[ListLbsResponse]>`

        Usage:
        ::

            result = await api.list_lbs_all()
        """

        return await fetch_all_pages_async(
            type=ListLbsResponse,
            key="lbs",
            fetcher=self.list_lbs,
            args={
                "zone": zone,
                "name": name,
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    async def create_lb(
        self,
        *,
        description: str,
        type_: str,
        ssl_compatibility_level: SSLCompatibilityLevel,
        zone: Optional[Zone] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        ip_id: Optional[str] = None,
        assign_flexible_ip: Optional[bool] = None,
        tags: Optional[List[str]] = None,
    ) -> Lb:
        """
        Create a Load Balancer.
        Create a new Load Balancer. Note that the Load Balancer will be created without frontends or backends; these must be created separately via the dedicated endpoints.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param organization_id: Scaleway Organization to create the Load Balancer in.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Scaleway Project to create the Load Balancer in.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param name: Name for the Load Balancer.
        :param description: Description for the Load Balancer.
        :param ip_id: ID of an existing flexible IP address to attach to the Load Balancer.
        :param assign_flexible_ip: Defines whether to automatically assign a flexible public IP to lb. Default value is `false` (do not assign).
        :param tags: List of tags for the Load Balancer.
        :param type_: Load Balancer commercial offer type. Use the Load Balancer types endpoint to retrieve a list of available offer types.
        :param ssl_compatibility_level: Determines the minimal SSL version which needs to be supported on the client side, in an SSL/TLS offloading context. Intermediate is suitable for general-purpose servers with a variety of clients, recommended for almost all systems. Modern is suitable for services with clients that support TLS 1.3 and do not need backward compatibility. Old is compatible with a small number of very old clients and should be used only as a last resort.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = await api.create_lb(
                description="example",
                type_="example",
                ssl_compatibility_level=ssl_compatibility_level_unknown,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/lbs",
            body=marshal_ZonedApiCreateLbRequest(
                ZonedApiCreateLbRequest(
                    description=description,
                    type_=type_,
                    ssl_compatibility_level=ssl_compatibility_level,
                    zone=zone,
                    organization_id=organization_id,
                    project_id=project_id,
                    name=name or random_name(prefix="lb"),
                    ip_id=ip_id,
                    assign_flexible_ip=assign_flexible_ip,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    async def get_lb(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
    ) -> Lb:
        """
        Get a Load Balancer.
        Retrieve information about an existing Load Balancer, specified by its Load Balancer ID. Its full details, including name, status and IP address, are returned in the response object.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = await api.get_lb(lb_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    async def wait_for_lb(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        options: Optional[WaitForOptions[Lb, Union[bool, Awaitable[bool]]]] = None,
    ) -> Lb:
        """
        Waits for :class:`Lb <Lb>` to be in a final state.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :param options: The options for the waiter
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.wait_for_lb(lb_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in LB_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_lb,
            options=options,
            args={
                "lb_id": lb_id,
                "zone": zone,
            },
        )

    async def update_lb(
        self,
        *,
        lb_id: str,
        name: str,
        description: str,
        ssl_compatibility_level: SSLCompatibilityLevel,
        zone: Optional[Zone] = None,
        tags: Optional[List[str]] = None,
    ) -> Lb:
        """
        Update a Load Balancer.
        Update the parameters of an existing Load Balancer, specified by its Load Balancer ID. Note that the request type is PUT and not PATCH. You must set all parameters.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :param name: Load Balancer name.
        :param description: Load Balancer description.
        :param tags: List of tags for the Load Balancer.
        :param ssl_compatibility_level: Determines the minimal SSL version which needs to be supported on the client side, in an SSL/TLS offloading context. Intermediate is suitable for general-purpose servers with a variety of clients, recommended for almost all systems. Modern is suitable for services with clients that support TLS 1.3 and don't need backward compatibility. Old is compatible with a small number of very old clients and should be used only as a last resort.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = await api.update_lb(
                lb_id="example",
                name="example",
                description="example",
                ssl_compatibility_level=ssl_compatibility_level_unknown,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}",
            body=marshal_ZonedApiUpdateLbRequest(
                ZonedApiUpdateLbRequest(
                    lb_id=lb_id,
                    name=name,
                    description=description,
                    ssl_compatibility_level=ssl_compatibility_level,
                    zone=zone,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    async def delete_lb(
        self,
        *,
        lb_id: str,
        release_ip: bool,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a Load Balancer.
        Delete an existing Load Balancer, specified by its Load Balancer ID. Deleting a Load Balancer is permanent, and cannot be undone. The Load Balancer's flexible IP address can either be deleted with the Load Balancer, or kept in your account for future use.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: ID of the Load Balancer to delete.
        :param release_ip: Defines whether the Load Balancer's flexible IP should be deleted. Set to true to release the flexible IP, or false to keep it available in your account for future Load Balancers.

        Usage:
        ::

            result = await api.delete_lb(
                lb_id="example",
                release_ip=True,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}",
            params={
                "release_ip": release_ip,
            },
        )

        self._throw_on_error(res)
        return None

    async def migrate_lb(
        self,
        *,
        lb_id: str,
        type_: str,
        zone: Optional[Zone] = None,
    ) -> Lb:
        """
        Migrate a Load Balancer.
        Migrate an existing Load Balancer from one commercial type to another. Allows you to scale your Load Balancer up or down in terms of bandwidth or multi-cloud provision.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :param type_: Load Balancer type to migrate to (use the List all Load Balancer offer types endpoint to get a list of available offer types).
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = await api.migrate_lb(
                lb_id="example",
                type_="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/migrate",
            body=marshal_ZonedApiMigrateLbRequest(
                ZonedApiMigrateLbRequest(
                    lb_id=lb_id,
                    type_=type_,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    async def list_i_ps(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        ip_address: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListIpsResponse:
        """
        List IP addresses.
        List the Load Balancer flexible IP addresses held in the account (filtered by Organization ID or Project ID). It is also possible to search for a specific IP address.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of IP addresses to return.
        :param ip_address: IP address to filter for.
        :param organization_id: Organization ID to filter for, only Load Balancer IP addresses from this Organization will be returned.
        :param project_id: Project ID to filter for, only Load Balancer IP addresses from this Project will be returned.
        :return: :class:`ListIpsResponse <ListIpsResponse>`

        Usage:
        ::

            result = await api.list_i_ps()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/ips",
            params={
                "ip_address": ip_address,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListIpsResponse(res.json())

    async def list_i_ps_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        ip_address: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Ip]:
        """
        List IP addresses.
        List the Load Balancer flexible IP addresses held in the account (filtered by Organization ID or Project ID). It is also possible to search for a specific IP address.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of IP addresses to return.
        :param ip_address: IP address to filter for.
        :param organization_id: Organization ID to filter for, only Load Balancer IP addresses from this Organization will be returned.
        :param project_id: Project ID to filter for, only Load Balancer IP addresses from this Project will be returned.
        :return: :class:`List[ListIpsResponse] <List[ListIpsResponse]>`

        Usage:
        ::

            result = await api.list_i_ps_all()
        """

        return await fetch_all_pages_async(
            type=ListIpsResponse,
            key="ips",
            fetcher=self.list_i_ps,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "ip_address": ip_address,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    async def create_ip(
        self,
        *,
        zone: Optional[Zone] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        reverse: Optional[str] = None,
    ) -> Ip:
        """
        Create an IP address.
        Create a new Load Balancer flexible IP address, in the specified Scaleway Project. This can be attached to new Load Balancers created in the future.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param organization_id: Organization ID of the Organization where the IP address should be created.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Project ID of the Project where the IP address should be created.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param reverse: Reverse DNS (domain name) for the IP address.
        :return: :class:`Ip <Ip>`

        Usage:
        ::

            result = await api.create_ip()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/ips",
            body=marshal_ZonedApiCreateIpRequest(
                ZonedApiCreateIpRequest(
                    zone=zone,
                    organization_id=organization_id,
                    project_id=project_id,
                    reverse=reverse,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Ip(res.json())

    async def get_ip(
        self,
        *,
        ip_id: str,
        zone: Optional[Zone] = None,
    ) -> Ip:
        """
        Get an IP address.
        Retrieve the full details of a Load Balancer flexible IP address.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param ip_id: IP address ID.
        :return: :class:`Ip <Ip>`

        Usage:
        ::

            result = await api.get_ip(ip_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/ips/{param_ip_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Ip(res.json())

    async def release_ip(
        self,
        *,
        ip_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete an IP address.
        Delete a Load Balancer flexible IP address. This action is irreversible, and cannot be undone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param ip_id: IP address ID.

        Usage:
        ::

            result = await api.release_ip(ip_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/ips/{param_ip_id}",
        )

        self._throw_on_error(res)
        return None

    async def update_ip(
        self,
        *,
        ip_id: str,
        zone: Optional[Zone] = None,
        reverse: Optional[str] = None,
    ) -> Ip:
        """
        Update an IP address.
        Update the reverse DNS of a Load Balancer flexible IP address.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param ip_id: IP address ID.
        :param reverse: Reverse DNS (domain name) for the IP address.
        :return: :class:`Ip <Ip>`

        Usage:
        ::

            result = await api.update_ip(ip_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "PATCH",
            f"/lb/v1/zones/{param_zone}/ips/{param_ip_id}",
            body=marshal_ZonedApiUpdateIpRequest(
                ZonedApiUpdateIpRequest(
                    ip_id=ip_id,
                    zone=zone,
                    reverse=reverse,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Ip(res.json())

    async def list_backends(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        order_by: ListBackendsRequestOrderBy = ListBackendsRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListBackendsResponse:
        """
        List the backends of a given Load Balancer.
        List all the backends of a Load Balancer, specified by its Load Balancer ID. By default, results are returned in ascending order by the creation date of each backend. The response is an array of backend objects, containing full details of each one including their configuration parameters such as protocol, port and forwarding algorithm.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :param name: Name of the backend to filter for.
        :param order_by: Sort order of backends in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of backends to return.
        :return: :class:`ListBackendsResponse <ListBackendsResponse>`

        Usage:
        ::

            result = await api.list_backends(lb_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/backends",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListBackendsResponse(res.json())

    async def list_backends_all(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        order_by: Optional[ListBackendsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[Backend]:
        """
        List the backends of a given Load Balancer.
        List all the backends of a Load Balancer, specified by its Load Balancer ID. By default, results are returned in ascending order by the creation date of each backend. The response is an array of backend objects, containing full details of each one including their configuration parameters such as protocol, port and forwarding algorithm.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :param name: Name of the backend to filter for.
        :param order_by: Sort order of backends in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of backends to return.
        :return: :class:`List[ListBackendsResponse] <List[ListBackendsResponse]>`

        Usage:
        ::

            result = await api.list_backends_all(lb_id="example")
        """

        return await fetch_all_pages_async(
            type=ListBackendsResponse,
            key="backends",
            fetcher=self.list_backends,
            args={
                "lb_id": lb_id,
                "zone": zone,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    async def create_backend(
        self,
        *,
        lb_id: str,
        forward_port: int,
        sticky_sessions_cookie_name: str,
        health_check: HealthCheck,
        server_ip: List[str],
        on_marked_down_action: OnMarkedDownAction,
        proxy_protocol: ProxyProtocol,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        forward_protocol: Protocol = Protocol.TCP,
        forward_port_algorithm: ForwardPortAlgorithm = ForwardPortAlgorithm.ROUNDROBIN,
        sticky_sessions: StickySessionsType = StickySessionsType.NONE,
        send_proxy_v2: Optional[bool] = None,
        timeout_server: Optional[str] = None,
        timeout_connect: Optional[str] = None,
        timeout_tunnel: Optional[str] = None,
        failover_host: Optional[str] = None,
        ssl_bridging: Optional[bool] = None,
        ignore_ssl_server_verify: Optional[bool] = None,
        redispatch_attempt_count: Optional[int] = None,
        max_retries: Optional[int] = None,
        max_connections: Optional[int] = None,
        timeout_queue: Optional[str] = None,
    ) -> Backend:
        """
        Create a backend for a given Load Balancer.
        Create a new backend for a given Load Balancer, specifying its full configuration including protocol, port and forwarding algorithm.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :param name: Name for the backend.
        :param forward_protocol: Protocol to be used by the backend when forwarding traffic to backend servers.
        :param forward_port: Port to be used by the backend when forwarding traffic to backend servers.
        :param forward_port_algorithm: Load balancing algorithm to be used when determining which backend server to forward new traffic to.
        :param sticky_sessions: Defines whether to activate sticky sessions (binding a particular session to a particular backend server) and the method to use if so. None disables sticky sessions. Cookie-based uses an HTTP cookie TO stick a session to a backend server. Table-based uses the source (client) IP address to stick a session to a backend server.
        :param sticky_sessions_cookie_name: Cookie name for cookie-based sticky sessions.
        :param health_check: Object defining the health check to be carried out by the backend when checking the status and health of backend servers.
        :param server_ip: List of backend server IP addresses (IPv4 or IPv6) the backend should forward traffic to.
        :param send_proxy_v2: Deprecated in favor of proxy_protocol field.
        :param timeout_server: Maximum allowed time for a backend server to process a request.
        :param timeout_connect: Maximum allowed time for establishing a connection to a backend server.
        :param timeout_tunnel: Maximum allowed tunnel inactivity time after Websocket is established (takes precedence over client and server timeout).
        :param on_marked_down_action: Action to take when a backend server is marked as down.
        :param proxy_protocol: Protocol to use between the Load Balancer and backend servers. Allows the backend servers to be informed of the client's real IP address. The PROXY protocol must be supported by the backend servers' software.
        :param failover_host: Scaleway S3 bucket website to be served as failover if all backend servers are down, e.g. failover-website.s3-website.fr-par.scw.cloud.
        :param ssl_bridging: Defines whether to enable SSL bridging between the Load Balancer and backend servers.
        :param ignore_ssl_server_verify: Defines whether the server certificate verification should be ignored.
        :param redispatch_attempt_count: Whether to use another backend server on each attempt.
        :param max_retries: Number of retries when a backend server connection failed.
        :param max_connections: Maximum number of connections allowed per backend server.
        :param timeout_queue: Maximum time for a request to be left pending in queue when `max_connections` is reached.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = await api.create_backend(
                lb_id="example",
                forward_port=1,
                sticky_sessions_cookie_name="example",
                health_check=HealthCheck(...),
                server_ip=["example"],
                on_marked_down_action=on_marked_down_action_none,
                proxy_protocol=proxy_protocol_unknown,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/backends",
            body=marshal_ZonedApiCreateBackendRequest(
                ZonedApiCreateBackendRequest(
                    lb_id=lb_id,
                    forward_port=forward_port,
                    sticky_sessions_cookie_name=sticky_sessions_cookie_name,
                    health_check=health_check,
                    server_ip=server_ip,
                    on_marked_down_action=on_marked_down_action,
                    proxy_protocol=proxy_protocol,
                    zone=zone,
                    name=name or random_name(prefix="lbb"),
                    forward_protocol=forward_protocol,
                    forward_port_algorithm=forward_port_algorithm,
                    sticky_sessions=sticky_sessions,
                    send_proxy_v2=send_proxy_v2,
                    timeout_server=timeout_server,
                    timeout_connect=timeout_connect,
                    timeout_tunnel=timeout_tunnel,
                    failover_host=failover_host,
                    ssl_bridging=ssl_bridging,
                    ignore_ssl_server_verify=ignore_ssl_server_verify,
                    redispatch_attempt_count=redispatch_attempt_count,
                    max_retries=max_retries,
                    max_connections=max_connections,
                    timeout_queue=timeout_queue,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    async def get_backend(
        self,
        *,
        backend_id: str,
        zone: Optional[Zone] = None,
    ) -> Backend:
        """
        Get a backend of a given Load Balancer.
        Get the full details of a given backend, specified by its backend ID. The response contains the backend's full configuration parameters including protocol, port and forwarding algorithm.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param backend_id: Backend ID.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = await api.get_backend(backend_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/backends/{param_backend_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    async def update_backend(
        self,
        *,
        backend_id: str,
        name: str,
        forward_port: int,
        sticky_sessions_cookie_name: str,
        on_marked_down_action: OnMarkedDownAction,
        proxy_protocol: ProxyProtocol,
        zone: Optional[Zone] = None,
        forward_protocol: Protocol = Protocol.TCP,
        forward_port_algorithm: ForwardPortAlgorithm = ForwardPortAlgorithm.ROUNDROBIN,
        sticky_sessions: StickySessionsType = StickySessionsType.NONE,
        send_proxy_v2: Optional[bool] = None,
        timeout_server: Optional[str] = None,
        timeout_connect: Optional[str] = None,
        timeout_tunnel: Optional[str] = None,
        failover_host: Optional[str] = None,
        ssl_bridging: Optional[bool] = None,
        ignore_ssl_server_verify: Optional[bool] = None,
        redispatch_attempt_count: Optional[int] = None,
        max_retries: Optional[int] = None,
        max_connections: Optional[int] = None,
        timeout_queue: Optional[str] = None,
    ) -> Backend:
        """
        Update a backend of a given Load Balancer.
        Update a backend of a given Load Balancer, specified by its backend ID. Note that the request type is PUT and not PATCH. You must set all parameters.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param backend_id: Backend ID.
        :param name: Backend name.
        :param forward_protocol: Protocol to be used by the backend when forwarding traffic to backend servers.
        :param forward_port: Port to be used by the backend when forwarding traffic to backend servers.
        :param forward_port_algorithm: Load balancing algorithm to be used when determining which backend server to forward new traffic to.
        :param sticky_sessions: Defines whether to activate sticky sessions (binding a particular session to a particular backend server) and the method to use if so. None disables sticky sessions. Cookie-based uses an HTTP cookie to stick a session to a backend server. Table-based uses the source (client) IP address to stick a session to a backend server.
        :param sticky_sessions_cookie_name: Cookie name for cookie-based sticky sessions.
        :param send_proxy_v2: Deprecated in favor of proxy_protocol field.
        :param timeout_server: Maximum allowed time for a backend server to process a request.
        :param timeout_connect: Maximum allowed time for establishing a connection to a backend server.
        :param timeout_tunnel: Maximum allowed tunnel inactivity time after Websocket is established (takes precedence over client and server timeout).
        :param on_marked_down_action: Action to take when a backend server is marked as down.
        :param proxy_protocol: Protocol to use between the Load Balancer and backend servers. Allows the backend servers to be informed of the client's real IP address. The PROXY protocol must be supported by the backend servers' software.
        :param failover_host: Scaleway S3 bucket website to be served as failover if all backend servers are down, e.g. failover-website.s3-website.fr-par.scw.cloud.
        :param ssl_bridging: Defines whether to enable SSL bridging between the Load Balancer and backend servers.
        :param ignore_ssl_server_verify: Defines whether the server certificate verification should be ignored.
        :param redispatch_attempt_count: Whether to use another backend server on each attempt.
        :param max_retries: Number of retries when a backend server connection failed.
        :param max_connections: Maximum number of connections allowed per backend server.
        :param timeout_queue: Maximum time for a request to be left pending in queue when `max_connections` is reached.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = await api.update_backend(
                backend_id="example",
                name="example",
                forward_port=1,
                sticky_sessions_cookie_name="example",
                on_marked_down_action=on_marked_down_action_none,
                proxy_protocol=proxy_protocol_unknown,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/backends/{param_backend_id}",
            body=marshal_ZonedApiUpdateBackendRequest(
                ZonedApiUpdateBackendRequest(
                    backend_id=backend_id,
                    name=name,
                    forward_port=forward_port,
                    sticky_sessions_cookie_name=sticky_sessions_cookie_name,
                    on_marked_down_action=on_marked_down_action,
                    proxy_protocol=proxy_protocol,
                    zone=zone,
                    forward_protocol=forward_protocol,
                    forward_port_algorithm=forward_port_algorithm,
                    sticky_sessions=sticky_sessions,
                    send_proxy_v2=send_proxy_v2,
                    timeout_server=timeout_server,
                    timeout_connect=timeout_connect,
                    timeout_tunnel=timeout_tunnel,
                    failover_host=failover_host,
                    ssl_bridging=ssl_bridging,
                    ignore_ssl_server_verify=ignore_ssl_server_verify,
                    redispatch_attempt_count=redispatch_attempt_count,
                    max_retries=max_retries,
                    max_connections=max_connections,
                    timeout_queue=timeout_queue,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    async def delete_backend(
        self,
        *,
        backend_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a backend of a given Load Balancer.
        Delete a backend of a given Load Balancer, specified by its backend ID. This action is irreversible and cannot be undone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param backend_id: ID of the backend to delete.

        Usage:
        ::

            result = await api.delete_backend(backend_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/backends/{param_backend_id}",
        )

        self._throw_on_error(res)
        return None

    async def add_backend_servers(
        self,
        *,
        backend_id: str,
        server_ip: List[str],
        zone: Optional[Zone] = None,
    ) -> Backend:
        """
        Add a set of backend servers to a given backend.
        For a given backend specified by its backend ID, add a set of backend servers (identified by their IP addresses) it should forward traffic to. These will be appended to any existing set of backend servers for this backend.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param backend_id: Backend ID.
        :param server_ip: List of IP addresses to add to backend servers.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = await api.add_backend_servers(
                backend_id="example",
                server_ip=["example"],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/backends/{param_backend_id}/servers",
            body=marshal_ZonedApiAddBackendServersRequest(
                ZonedApiAddBackendServersRequest(
                    backend_id=backend_id,
                    server_ip=server_ip,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    async def remove_backend_servers(
        self,
        *,
        backend_id: str,
        server_ip: List[str],
        zone: Optional[Zone] = None,
    ) -> Backend:
        """
        Remove a set of servers for a given backend.
        For a given backend specified by its backend ID, remove the specified backend servers (identified by their IP addresses) so that it no longer forwards traffic to them.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param backend_id: Backend ID.
        :param server_ip: List of IP addresses to remove from backend servers.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = await api.remove_backend_servers(
                backend_id="example",
                server_ip=["example"],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/backends/{param_backend_id}/servers",
            body=marshal_ZonedApiRemoveBackendServersRequest(
                ZonedApiRemoveBackendServersRequest(
                    backend_id=backend_id,
                    server_ip=server_ip,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    async def set_backend_servers(
        self,
        *,
        backend_id: str,
        server_ip: List[str],
        zone: Optional[Zone] = None,
    ) -> Backend:
        """
        Define all backend servers for a given backend.
        For a given backend specified by its backend ID, define the set of backend servers (identified by their IP addresses) that it should forward traffic to. Any existing backend servers configured for this backend will be removed.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param backend_id: Backend ID.
        :param server_ip: List of IP addresses for backend servers. Any other existing backend servers will be removed.
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = await api.set_backend_servers(
                backend_id="example",
                server_ip=["example"],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/backends/{param_backend_id}/servers",
            body=marshal_ZonedApiSetBackendServersRequest(
                ZonedApiSetBackendServersRequest(
                    backend_id=backend_id,
                    server_ip=server_ip,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    async def update_health_check(
        self,
        *,
        backend_id: str,
        port: int,
        check_delay: str,
        check_timeout: str,
        check_max_retries: int,
        check_send_proxy: bool,
        zone: Optional[Zone] = None,
        tcp_config: Optional[HealthCheckTcpConfig] = None,
        mysql_config: Optional[HealthCheckMysqlConfig] = None,
        pgsql_config: Optional[HealthCheckPgsqlConfig] = None,
        ldap_config: Optional[HealthCheckLdapConfig] = None,
        redis_config: Optional[HealthCheckRedisConfig] = None,
        http_config: Optional[HealthCheckHttpConfig] = None,
        https_config: Optional[HealthCheckHttpsConfig] = None,
        transient_check_delay: Optional[str] = None,
    ) -> HealthCheck:
        """
        Update a health check for a given backend.
        Update the configuration of the health check performed by a given backend to verify the health of its backend servers, identified by its backend ID. Note that the request type is PUT and not PATCH. You must set all parameters.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param backend_id: Backend ID.
        :param port: Port to use for the backend server health check.
        :param check_delay: Time to wait between two consecutive health checks.
        :param check_timeout: Maximum time a backend server has to reply to the health check.
        :param check_max_retries: Number of consecutive unsuccessful health checks after which the server will be considered dead.
        :param check_send_proxy: Defines whether proxy protocol should be activated for the health check.
        :param tcp_config: Object to configure a basic TCP health check.

        One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
        :param mysql_config: Object to configure a MySQL health check. The check requires MySQL >=3.22, for older versions, use a TCP health check.

        One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
        :param pgsql_config: Object to configure a PostgreSQL health check.

        One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
        :param ldap_config: Object to configure an LDAP health check. The response is analyzed to find the LDAPv3 response message.

        One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
        :param redis_config: Object to configure a Redis health check. The response is analyzed to find the +PONG response message.

        One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
        :param http_config: Object to configure an HTTP health check.

        One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
        :param https_config: Object to configure an HTTPS health check.

        One-of ('config'): at most one of 'tcp_config', 'mysql_config', 'pgsql_config', 'ldap_config', 'redis_config', 'http_config', 'https_config' could be set.
        :param transient_check_delay: Time to wait between two consecutive health checks when a backend server is in a transient state (going UP or DOWN).
        :return: :class:`HealthCheck <HealthCheck>`

        Usage:
        ::

            result = await api.update_health_check(
                backend_id="example",
                port=1,
                check_delay="example",
                check_timeout="example",
                check_max_retries=1,
                check_send_proxy=True,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/backends/{param_backend_id}/healthcheck",
            body=marshal_ZonedApiUpdateHealthCheckRequest(
                ZonedApiUpdateHealthCheckRequest(
                    backend_id=backend_id,
                    port=port,
                    check_delay=check_delay,
                    check_timeout=check_timeout,
                    check_max_retries=check_max_retries,
                    check_send_proxy=check_send_proxy,
                    zone=zone,
                    tcp_config=tcp_config,
                    mysql_config=mysql_config,
                    pgsql_config=pgsql_config,
                    ldap_config=ldap_config,
                    redis_config=redis_config,
                    http_config=http_config,
                    https_config=https_config,
                    transient_check_delay=transient_check_delay,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_HealthCheck(res.json())

    async def list_frontends(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        order_by: ListFrontendsRequestOrderBy = ListFrontendsRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListFrontendsResponse:
        """
        List frontends of a given Load Balancer.
        List all the frontends of a Load Balancer, specified by its Load Balancer ID. By default, results are returned in ascending order by the creation date of each frontend. The response is an array of frontend objects, containing full details of each one including the port they listen on and the backend they are attached to.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :param name: Name of the frontend to filter for.
        :param order_by: Sort order of frontends in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of frontends to return.
        :return: :class:`ListFrontendsResponse <ListFrontendsResponse>`

        Usage:
        ::

            result = await api.list_frontends(lb_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/frontends",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListFrontendsResponse(res.json())

    async def list_frontends_all(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        order_by: Optional[ListFrontendsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[Frontend]:
        """
        List frontends of a given Load Balancer.
        List all the frontends of a Load Balancer, specified by its Load Balancer ID. By default, results are returned in ascending order by the creation date of each frontend. The response is an array of frontend objects, containing full details of each one including the port they listen on and the backend they are attached to.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :param name: Name of the frontend to filter for.
        :param order_by: Sort order of frontends in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of frontends to return.
        :return: :class:`List[ListFrontendsResponse] <List[ListFrontendsResponse]>`

        Usage:
        ::

            result = await api.list_frontends_all(lb_id="example")
        """

        return await fetch_all_pages_async(
            type=ListFrontendsResponse,
            key="frontends",
            fetcher=self.list_frontends,
            args={
                "lb_id": lb_id,
                "zone": zone,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
            },
        )

    async def create_frontend(
        self,
        *,
        lb_id: str,
        inbound_port: int,
        backend_id: str,
        enable_http3: bool,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        timeout_client: Optional[str] = None,
        certificate_id: Optional[str] = None,
        certificate_ids: Optional[List[str]] = None,
    ) -> Frontend:
        """
        Create a frontend in a given Load Balancer.
        Create a new frontend for a given Load Balancer, specifying its configuration including the port it should listen on and the backend to attach it to.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID (ID of the Load Balancer to attach the frontend to).
        :param name: Name for the frontend.
        :param inbound_port: Port the frontend should listen on.
        :param backend_id: Backend ID (ID of the backend the frontend should pass traffic to).
        :param timeout_client: Maximum allowed inactivity time on the client side.
        :param certificate_id: Certificate ID, deprecated in favor of certificate_ids array.
        :param certificate_ids: List of SSL/TLS certificate IDs to bind to the frontend.
        :param enable_http3: Defines whether to enable HTTP/3 protocol on the frontend.
        :return: :class:`Frontend <Frontend>`

        Usage:
        ::

            result = await api.create_frontend(
                lb_id="example",
                inbound_port=1,
                backend_id="example",
                enable_http3=True,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/frontends",
            body=marshal_ZonedApiCreateFrontendRequest(
                ZonedApiCreateFrontendRequest(
                    lb_id=lb_id,
                    inbound_port=inbound_port,
                    backend_id=backend_id,
                    enable_http3=enable_http3,
                    zone=zone,
                    name=name or random_name(prefix="lbf"),
                    timeout_client=timeout_client,
                    certificate_id=certificate_id,
                    certificate_ids=certificate_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Frontend(res.json())

    async def get_frontend(
        self,
        *,
        frontend_id: str,
        zone: Optional[Zone] = None,
    ) -> Frontend:
        """
        Get a frontend.
        Get the full details of a given frontend, specified by its frontend ID. The response contains the frontend's full configuration parameters including the backend it is attached to, the port it listens on, and any certificates it has.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param frontend_id: Frontend ID.
        :return: :class:`Frontend <Frontend>`

        Usage:
        ::

            result = await api.get_frontend(frontend_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/frontends/{param_frontend_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Frontend(res.json())

    async def update_frontend(
        self,
        *,
        frontend_id: str,
        name: str,
        inbound_port: int,
        backend_id: str,
        enable_http3: bool,
        zone: Optional[Zone] = None,
        timeout_client: Optional[str] = None,
        certificate_id: Optional[str] = None,
        certificate_ids: Optional[List[str]] = None,
    ) -> Frontend:
        """
        Update a frontend.
        Update a given frontend, specified by its frontend ID. You can update configuration parameters including its name and the port it listens on. Note that the request type is PUT and not PATCH. You must set all parameters.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param frontend_id: Frontend ID.
        :param name: Frontend name.
        :param inbound_port: Port the frontend should listen on.
        :param backend_id: Backend ID (ID of the backend the frontend should pass traffic to).
        :param timeout_client: Maximum allowed inactivity time on the client side.
        :param certificate_id: Certificate ID, deprecated in favor of certificate_ids array.
        :param certificate_ids: List of SSL/TLS certificate IDs to bind to the frontend.
        :param enable_http3: Defines whether to enable HTTP/3 protocol on the frontend.
        :return: :class:`Frontend <Frontend>`

        Usage:
        ::

            result = await api.update_frontend(
                frontend_id="example",
                name="example",
                inbound_port=1,
                backend_id="example",
                enable_http3=True,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/frontends/{param_frontend_id}",
            body=marshal_ZonedApiUpdateFrontendRequest(
                ZonedApiUpdateFrontendRequest(
                    frontend_id=frontend_id,
                    name=name,
                    inbound_port=inbound_port,
                    backend_id=backend_id,
                    enable_http3=enable_http3,
                    zone=zone,
                    timeout_client=timeout_client,
                    certificate_id=certificate_id,
                    certificate_ids=certificate_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Frontend(res.json())

    async def delete_frontend(
        self,
        *,
        frontend_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a frontend.
        Delete a given frontend, specified by its frontend ID. This action is irreversible and cannot be undone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param frontend_id: ID of the frontend to delete.

        Usage:
        ::

            result = await api.delete_frontend(frontend_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/frontends/{param_frontend_id}",
        )

        self._throw_on_error(res)
        return None

    async def list_routes(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: ListRoutesRequestOrderBy = ListRoutesRequestOrderBy.CREATED_AT_ASC,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        frontend_id: Optional[str] = None,
    ) -> ListRoutesResponse:
        """
        List all routes.
        List all routes for a given frontend. The response is an array of routes, each one  with a specified backend to direct to if a certain condition is matched (based on the value of the SNI field or HTTP Host header).
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of routes in the response.
        :param page_size: The number of route objects to return.
        :param page: The page number to return, from the paginated results.
        :param frontend_id: Frontend ID to filter for, only Routes from this Frontend will be returned.
        :return: :class:`ListRoutesResponse <ListRoutesResponse>`

        Usage:
        ::

            result = await api.list_routes()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/routes",
            params={
                "frontend_id": frontend_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRoutesResponse(res.json())

    async def list_routes_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListRoutesRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        frontend_id: Optional[str] = None,
    ) -> List[Route]:
        """
        List all routes.
        List all routes for a given frontend. The response is an array of routes, each one  with a specified backend to direct to if a certain condition is matched (based on the value of the SNI field or HTTP Host header).
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of routes in the response.
        :param page_size: The number of route objects to return.
        :param page: The page number to return, from the paginated results.
        :param frontend_id: Frontend ID to filter for, only Routes from this Frontend will be returned.
        :return: :class:`List[ListRoutesResponse] <List[ListRoutesResponse]>`

        Usage:
        ::

            result = await api.list_routes_all()
        """

        return await fetch_all_pages_async(
            type=ListRoutesResponse,
            key="routes",
            fetcher=self.list_routes,
            args={
                "zone": zone,
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
                "frontend_id": frontend_id,
            },
        )

    async def create_route(
        self,
        *,
        frontend_id: str,
        backend_id: str,
        zone: Optional[Zone] = None,
        match: Optional[RouteMatch] = None,
    ) -> Route:
        """
        Create a route.
        Create a new route on a given frontend. To configure a route, specify the backend to direct to if a certain condition is matched (based on the value of the SNI field or HTTP Host header).
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param frontend_id: ID of the source frontend to create the route on.
        :param backend_id: ID of the target backend for the route.
        :param match: Object defining the match condition for a route to be applied. If an incoming client session matches the specified condition (i.e. it has a matching SNI value or HTTP Host header value), it will be passed to the target backend.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = await api.create_route(
                frontend_id="example",
                backend_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/routes",
            body=marshal_ZonedApiCreateRouteRequest(
                ZonedApiCreateRouteRequest(
                    frontend_id=frontend_id,
                    backend_id=backend_id,
                    zone=zone,
                    match=match,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    async def get_route(
        self,
        *,
        route_id: str,
        zone: Optional[Zone] = None,
    ) -> Route:
        """
        Get a route.
        Retrieve information about an existing route, specified by its route ID. Its full details, origin frontend, target backend and match condition, are returned in the response object.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param route_id: Route ID.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = await api.get_route(route_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/routes/{param_route_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    async def update_route(
        self,
        *,
        route_id: str,
        backend_id: str,
        zone: Optional[Zone] = None,
        match: Optional[RouteMatch] = None,
    ) -> Route:
        """
        Update a route.
        Update the configuration of an existing route, specified by its route ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param route_id: Route ID.
        :param backend_id: ID of the target backend for the route.
        :param match: Object defining the match condition for a route to be applied. If an incoming client session matches the specified condition (i.e. it has a matching SNI value or HTTP Host header value), it will be passed to the target backend.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = await api.update_route(
                route_id="example",
                backend_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/routes/{param_route_id}",
            body=marshal_ZonedApiUpdateRouteRequest(
                ZonedApiUpdateRouteRequest(
                    route_id=route_id,
                    backend_id=backend_id,
                    zone=zone,
                    match=match,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    async def delete_route(
        self,
        *,
        route_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a route.
        Delete an existing route, specified by its route ID. Deleting a route is permanent, and cannot be undone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param route_id: Route ID.

        Usage:
        ::

            result = await api.delete_route(route_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/routes/{param_route_id}",
        )

        self._throw_on_error(res)
        return None

    async def get_lb_stats(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        backend_id: Optional[str] = None,
    ) -> LbStats:
        """
        Get usage statistics of a given Load Balancer.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :param backend_id: ID of the backend.
        :return: :class:`LbStats <LbStats>`
        :deprecated

        Usage:
        ::

            result = await api.get_lb_stats(lb_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/stats",
            params={
                "backend_id": backend_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_LbStats(res.json())

    async def list_backend_stats(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        backend_id: Optional[str] = None,
    ) -> ListBackendStatsResponse:
        """
        List backend server statistics.
        List information about your backend servers, including their state and the result of their last health check.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of items to return.
        :param backend_id: ID of the backend.
        :return: :class:`ListBackendStatsResponse <ListBackendStatsResponse>`

        Usage:
        ::

            result = await api.list_backend_stats(lb_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/backend-stats",
            params={
                "backend_id": backend_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListBackendStatsResponse(res.json())

    async def list_backend_stats_all(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        backend_id: Optional[str] = None,
    ) -> List[BackendServerStats]:
        """
        List backend server statistics.
        List information about your backend servers, including their state and the result of their last health check.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of items to return.
        :param backend_id: ID of the backend.
        :return: :class:`List[ListBackendStatsResponse] <List[ListBackendStatsResponse]>`

        Usage:
        ::

            result = await api.list_backend_stats_all(lb_id="example")
        """

        return await fetch_all_pages_async(
            type=ListBackendStatsResponse,
            key="backend_servers_stats",
            fetcher=self.list_backend_stats,
            args={
                "lb_id": lb_id,
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "backend_id": backend_id,
            },
        )

    async def list_acls(
        self,
        *,
        frontend_id: str,
        zone: Optional[Zone] = None,
        order_by: ListAclRequestOrderBy = ListAclRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
    ) -> ListAclResponse:
        """
        List ACLs for a given frontend.
        List the ACLs for a given frontend, specified by its frontend ID. The response is an array of ACL objects, each one representing an ACL that denies or allows traffic based on certain conditions.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param frontend_id: Frontend ID (ACLs attached to this frontend will be returned in the response).
        :param order_by: Sort order of ACLs in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of ACLs to return.
        :param name: ACL name to filter for.
        :return: :class:`ListAclResponse <ListAclResponse>`

        Usage:
        ::

            result = await api.list_acls(frontend_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/frontends/{param_frontend_id}/acls",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListAclResponse(res.json())

    async def list_acls_all(
        self,
        *,
        frontend_id: str,
        zone: Optional[Zone] = None,
        order_by: Optional[ListAclRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
    ) -> List[Acl]:
        """
        List ACLs for a given frontend.
        List the ACLs for a given frontend, specified by its frontend ID. The response is an array of ACL objects, each one representing an ACL that denies or allows traffic based on certain conditions.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param frontend_id: Frontend ID (ACLs attached to this frontend will be returned in the response).
        :param order_by: Sort order of ACLs in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of ACLs to return.
        :param name: ACL name to filter for.
        :return: :class:`List[ListAclResponse] <List[ListAclResponse]>`

        Usage:
        ::

            result = await api.list_acls_all(frontend_id="example")
        """

        return await fetch_all_pages_async(
            type=ListAclResponse,
            key="acls",
            fetcher=self.list_acls,
            args={
                "frontend_id": frontend_id,
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
            },
        )

    async def create_acl(
        self,
        *,
        frontend_id: str,
        action: AclAction,
        index: int,
        description: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        match: Optional[AclMatch] = None,
    ) -> Acl:
        """
        Create an ACL for a given frontend.
        Create a new ACL for a given frontend. Each ACL must have a name, an action to perform (allow or deny), and a match rule (the action is carried out when the incoming traffic matches the rule).
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param frontend_id: Frontend ID to attach the ACL to.
        :param name: ACL name.
        :param action: Action to take when incoming traffic matches an ACL filter.
        :param match: ACL match filter object. One of `ip_subnet` or `http_filter` & `http_filter_value` are required.
        :param index: Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
        :param description: ACL description.
        :return: :class:`Acl <Acl>`

        Usage:
        ::

            result = await api.create_acl(
                frontend_id="example",
                action=AclAction(...),
                index=1,
                description="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/frontends/{param_frontend_id}/acls",
            body=marshal_ZonedApiCreateAclRequest(
                ZonedApiCreateAclRequest(
                    frontend_id=frontend_id,
                    action=action,
                    index=index,
                    description=description,
                    zone=zone,
                    name=name or random_name(prefix="acl"),
                    match=match,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Acl(res.json())

    async def get_acl(
        self,
        *,
        acl_id: str,
        zone: Optional[Zone] = None,
    ) -> Acl:
        """
        Get an ACL.
        Get information for a particular ACL, specified by its ACL ID. The response returns full details of the ACL, including its name, action, match rule and frontend.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param acl_id: ACL ID.
        :return: :class:`Acl <Acl>`

        Usage:
        ::

            result = await api.get_acl(acl_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_acl_id = validate_path_param("acl_id", acl_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/acls/{param_acl_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Acl(res.json())

    async def update_acl(
        self,
        *,
        acl_id: str,
        name: str,
        action: AclAction,
        index: int,
        zone: Optional[Zone] = None,
        match: Optional[AclMatch] = None,
        description: Optional[str] = None,
    ) -> Acl:
        """
        Update an ACL.
        Update a particular ACL, specified by its ACL ID. You can update details including its name, action and match rule.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param acl_id: ACL ID.
        :param name: ACL name.
        :param action: Action to take when incoming traffic matches an ACL filter.
        :param match: ACL match filter object. One of `ip_subnet` or `http_filter` & `http_filter_value` are required.
        :param index: Priority of this ACL (ACLs are applied in ascending order, 0 is the first ACL executed).
        :param description: ACL description.
        :return: :class:`Acl <Acl>`

        Usage:
        ::

            result = await api.update_acl(
                acl_id="example",
                name="example",
                action=AclAction(...),
                index=1,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_acl_id = validate_path_param("acl_id", acl_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/acls/{param_acl_id}",
            body=marshal_ZonedApiUpdateAclRequest(
                ZonedApiUpdateAclRequest(
                    acl_id=acl_id,
                    name=name,
                    action=action,
                    index=index,
                    zone=zone,
                    match=match,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Acl(res.json())

    async def delete_acl(
        self,
        *,
        acl_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete an ACL.
        Delete an ACL, specified by its ACL ID. Deleting an ACL is irreversible and cannot be undone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param acl_id: ACL ID.

        Usage:
        ::

            result = await api.delete_acl(acl_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_acl_id = validate_path_param("acl_id", acl_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/acls/{param_acl_id}",
        )

        self._throw_on_error(res)
        return None

    async def set_acls(
        self,
        *,
        frontend_id: str,
        acls: List[AclSpec],
        zone: Optional[Zone] = None,
    ) -> SetAclsResponse:
        """
        Define all ACLs for a given frontend.
        For a given frontend specified by its frontend ID, define and add the complete set of ACLS for that frontend. Any existing ACLs on this frontend will be removed.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param frontend_id: Frontend ID.
        :param acls: List of ACLs for this frontend. Any other existing ACLs on this frontend will be removed.
        :return: :class:`SetAclsResponse <SetAclsResponse>`

        Usage:
        ::

            result = await api.set_acls(
                frontend_id="example",
                acls=[AclSpec(...)],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/frontends/{param_frontend_id}/acls",
            body=marshal_ZonedApiSetAclsRequest(
                ZonedApiSetAclsRequest(
                    frontend_id=frontend_id,
                    acls=acls,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetAclsResponse(res.json())

    async def create_certificate(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        letsencrypt: Optional[CreateCertificateRequestLetsencryptConfig] = None,
        custom_certificate: Optional[CreateCertificateRequestCustomCertificate] = None,
    ) -> Certificate:
        """
        Create an SSL/TLS certificate.
        Generate a new SSL/TLS certificate for a given Load Balancer. You can choose to create a Let's Encrypt certificate, or import a custom certificate.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :param name: Name for the certificate.
        :param letsencrypt: Object to define a new Let's Encrypt certificate to be generated.

        One-of ('type_'): at most one of 'letsencrypt', 'custom_certificate' could be set.
        :param custom_certificate: Object to define an existing custom certificate to be imported.

        One-of ('type_'): at most one of 'letsencrypt', 'custom_certificate' could be set.
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = await api.create_certificate(lb_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/certificates",
            body=marshal_ZonedApiCreateCertificateRequest(
                ZonedApiCreateCertificateRequest(
                    lb_id=lb_id,
                    zone=zone,
                    name=name or random_name(prefix="certificate"),
                    letsencrypt=letsencrypt,
                    custom_certificate=custom_certificate,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Certificate(res.json())

    async def list_certificates(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        order_by: ListCertificatesRequestOrderBy = ListCertificatesRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
    ) -> ListCertificatesResponse:
        """
        List all SSL/TLS certificates on a given Load Balancer.
        List all the SSL/TLS certificates on a given Load Balancer. The response is an array of certificate objects, which are by default listed in ascending order of creation date.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :param order_by: Sort order of certificates in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of certificates to return.
        :param name: Certificate name to filter for, only certificates of this name will be returned.
        :return: :class:`ListCertificatesResponse <ListCertificatesResponse>`

        Usage:
        ::

            result = await api.list_certificates(lb_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/certificates",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListCertificatesResponse(res.json())

    async def list_certificates_all(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        order_by: Optional[ListCertificatesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
    ) -> List[Certificate]:
        """
        List all SSL/TLS certificates on a given Load Balancer.
        List all the SSL/TLS certificates on a given Load Balancer. The response is an array of certificate objects, which are by default listed in ascending order of creation date.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :param order_by: Sort order of certificates in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: Number of certificates to return.
        :param name: Certificate name to filter for, only certificates of this name will be returned.
        :return: :class:`List[ListCertificatesResponse] <List[ListCertificatesResponse]>`

        Usage:
        ::

            result = await api.list_certificates_all(lb_id="example")
        """

        return await fetch_all_pages_async(
            type=ListCertificatesResponse,
            key="certificates",
            fetcher=self.list_certificates,
            args={
                "lb_id": lb_id,
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
            },
        )

    async def get_certificate(
        self,
        *,
        certificate_id: str,
        zone: Optional[Zone] = None,
    ) -> Certificate:
        """
        Get an SSL/TLS certificate.
        Get information for a particular SSL/TLS certificate, specified by its certificate ID. The response returns full details of the certificate, including its type, main domain name, and alternative domain names.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param certificate_id: Certificate ID.
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = await api.get_certificate(certificate_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_certificate_id = validate_path_param("certificate_id", certificate_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/certificates/{param_certificate_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Certificate(res.json())

    async def wait_for_certificate(
        self,
        *,
        certificate_id: str,
        zone: Optional[Zone] = None,
        options: Optional[
            WaitForOptions[Certificate, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> Certificate:
        """
        Waits for :class:`Certificate <Certificate>` to be in a final state.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param certificate_id: Certificate ID.
        :param options: The options for the waiter
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = api.wait_for_certificate(certificate_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in CERTIFICATE_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_certificate,
            options=options,
            args={
                "certificate_id": certificate_id,
                "zone": zone,
            },
        )

    async def update_certificate(
        self,
        *,
        certificate_id: str,
        name: str,
        zone: Optional[Zone] = None,
    ) -> Certificate:
        """
        Update an SSL/TLS certificate.
        Update the name of a particular SSL/TLS certificate, specified by its certificate ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param certificate_id: Certificate ID.
        :param name: Certificate name.
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = await api.update_certificate(
                certificate_id="example",
                name="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_certificate_id = validate_path_param("certificate_id", certificate_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/certificates/{param_certificate_id}",
            body=marshal_ZonedApiUpdateCertificateRequest(
                ZonedApiUpdateCertificateRequest(
                    certificate_id=certificate_id,
                    name=name,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Certificate(res.json())

    async def delete_certificate(
        self,
        *,
        certificate_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete an SSL/TLS certificate.
        Delete an SSL/TLS certificate, specified by its certificate ID. Deleting a certificate is irreversible and cannot be undone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param certificate_id: Certificate ID.

        Usage:
        ::

            result = await api.delete_certificate(certificate_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_certificate_id = validate_path_param("certificate_id", certificate_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/certificates/{param_certificate_id}",
        )

        self._throw_on_error(res)
        return None

    async def list_lb_types(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListLbTypesResponse:
        """
        List all Load Balancer offer types.
        List all the different commercial Load Balancer types. The response includes an array of offer types, each with a name, description, and information about its stock availability.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of items to return.
        :return: :class:`ListLbTypesResponse <ListLbTypesResponse>`

        Usage:
        ::

            result = await api.list_lb_types()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lb-types",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListLbTypesResponse(res.json())

    async def list_lb_types_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[LbType]:
        """
        List all Load Balancer offer types.
        List all the different commercial Load Balancer types. The response includes an array of offer types, each with a name, description, and information about its stock availability.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of items to return.
        :return: :class:`List[ListLbTypesResponse] <List[ListLbTypesResponse]>`

        Usage:
        ::

            result = await api.list_lb_types_all()
        """

        return await fetch_all_pages_async(
            type=ListLbTypesResponse,
            key="lb_types",
            fetcher=self.list_lb_types,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
            },
        )

    async def create_subscriber(
        self,
        *,
        name: str,
        zone: Optional[Zone] = None,
        email_config: Optional[SubscriberEmailConfig] = None,
        webhook_config: Optional[SubscriberWebhookConfig] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> Subscriber:
        """
        Create a subscriber.
        Create a new subscriber, either with an email configuration or a webhook configuration, for a specified Scaleway Project.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Subscriber name.
        :param email_config: Email address configuration.

        One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
        :param webhook_config: WebHook URI configuration.

        One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
        :param organization_id: Organization ID to create the subscriber in.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Project ID to create the subscriber in.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :return: :class:`Subscriber <Subscriber>`

        Usage:
        ::

            result = await api.create_subscriber(name="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/subscribers",
            body=marshal_ZonedApiCreateSubscriberRequest(
                ZonedApiCreateSubscriberRequest(
                    name=name,
                    zone=zone,
                    email_config=email_config,
                    webhook_config=webhook_config,
                    organization_id=organization_id,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Subscriber(res.json())

    async def get_subscriber(
        self,
        *,
        subscriber_id: str,
        zone: Optional[Zone] = None,
    ) -> Subscriber:
        """
        Get a subscriber.
        Retrieve information about an existing subscriber, specified by its subscriber ID. Its full details, including name and email/webhook configuration, are returned in the response object.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param subscriber_id: Subscriber ID.
        :return: :class:`Subscriber <Subscriber>`

        Usage:
        ::

            result = await api.get_subscriber(subscriber_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_subscriber_id = validate_path_param("subscriber_id", subscriber_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/subscribers/{param_subscriber_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Subscriber(res.json())

    async def list_subscriber(
        self,
        *,
        name: str,
        zone: Optional[Zone] = None,
        order_by: ListSubscriberRequestOrderBy = ListSubscriberRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListSubscriberResponse:
        """
        List all subscribers.
        List all subscribers to Load Balancer alerts. By default, returns all subscribers to Load Balancer alerts for the Organization associated with the authentication token used for the request.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of subscribers in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of items to return.
        :param name: Subscriber name to search for.
        :param organization_id: Filter subscribers by Organization ID.
        :param project_id: Filter subscribers by Project ID.
        :return: :class:`ListSubscriberResponse <ListSubscriberResponse>`

        Usage:
        ::

            result = await api.list_subscriber(name="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/subscribers",
            params={
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
        return unmarshal_ListSubscriberResponse(res.json())

    async def list_subscriber_all(
        self,
        *,
        name: str,
        zone: Optional[Zone] = None,
        order_by: Optional[ListSubscriberRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Subscriber]:
        """
        List all subscribers.
        List all subscribers to Load Balancer alerts. By default, returns all subscribers to Load Balancer alerts for the Organization associated with the authentication token used for the request.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of subscribers in the response.
        :param page: The page number to return, from the paginated results.
        :param page_size: The number of items to return.
        :param name: Subscriber name to search for.
        :param organization_id: Filter subscribers by Organization ID.
        :param project_id: Filter subscribers by Project ID.
        :return: :class:`List[ListSubscriberResponse] <List[ListSubscriberResponse]>`

        Usage:
        ::

            result = await api.list_subscriber_all(name="example")
        """

        return await fetch_all_pages_async(
            type=ListSubscriberResponse,
            key="subscribers",
            fetcher=self.list_subscriber,
            args={
                "name": name,
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    async def update_subscriber(
        self,
        *,
        subscriber_id: str,
        name: str,
        zone: Optional[Zone] = None,
        email_config: Optional[SubscriberEmailConfig] = None,
        webhook_config: Optional[SubscriberWebhookConfig] = None,
    ) -> Subscriber:
        """
        Update a subscriber.
        Update the parameters of a given subscriber (e.g. name, webhook configuration, email configuration), specified by its subscriber ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param subscriber_id: Subscriber ID.
        :param name: Subscriber name.
        :param email_config: Email address configuration.

        One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
        :param webhook_config: Webhook URI configuration.

        One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
        :return: :class:`Subscriber <Subscriber>`

        Usage:
        ::

            result = await api.update_subscriber(
                subscriber_id="example",
                name="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_subscriber_id = validate_path_param("subscriber_id", subscriber_id)

        res = self._request(
            "PUT",
            f"/lb/v1/zones/{param_zone}/subscribers/{param_subscriber_id}",
            body=marshal_ZonedApiUpdateSubscriberRequest(
                ZonedApiUpdateSubscriberRequest(
                    subscriber_id=subscriber_id,
                    name=name,
                    zone=zone,
                    email_config=email_config,
                    webhook_config=webhook_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Subscriber(res.json())

    async def delete_subscriber(
        self,
        *,
        subscriber_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a subscriber.
        Delete an existing subscriber, specified by its subscriber ID. Deleting a subscriber is permanent, and cannot be undone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param subscriber_id: Subscriber ID.

        Usage:
        ::

            result = await api.delete_subscriber(subscriber_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_subscriber_id = validate_path_param("subscriber_id", subscriber_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/lb/subscription/{param_subscriber_id}",
        )

        self._throw_on_error(res)
        return None

    async def subscribe_to_lb(
        self,
        *,
        lb_id: str,
        subscriber_id: str,
        zone: Optional[Zone] = None,
    ) -> Lb:
        """
        Subscribe a subscriber to alerts for a given Load Balancer.
        Subscribe an existing subscriber to alerts for a given Load Balancer.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :param subscriber_id: Subscriber ID.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = await api.subscribe_to_lb(
                lb_id="example",
                subscriber_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/lb/{param_lb_id}/subscribe",
            body=marshal_ZonedApiSubscribeToLbRequest(
                ZonedApiSubscribeToLbRequest(
                    lb_id=lb_id,
                    subscriber_id=subscriber_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    async def unsubscribe_from_lb(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
    ) -> Lb:
        """
        Unsubscribe a subscriber from alerts for a given Load Balancer.
        Unsubscribe a subscriber from alerts for a given Load Balancer. The subscriber is not deleted, and can be resubscribed in the future if necessary.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = await api.unsubscribe_from_lb(lb_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/lb/{param_lb_id}/unsubscribe",
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    async def list_lb_private_networks(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        order_by: ListPrivateNetworksRequestOrderBy = ListPrivateNetworksRequestOrderBy.CREATED_AT_ASC,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListLbPrivateNetworksResponse:
        """
        List Private Networks attached to a Load Balancer.
        List the Private Networks attached to a given Load Balancer, specified by its Load Balancer ID. The response is an array of Private Network objects, giving information including the status, configuration, name and creation date of each Private Network.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :param order_by: Sort order of Private Network objects in the response.
        :param page_size: Number of objects to return.
        :param page: The page number to return, from the paginated results.
        :return: :class:`ListLbPrivateNetworksResponse <ListLbPrivateNetworksResponse>`

        Usage:
        ::

            result = await api.list_lb_private_networks(lb_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/private-networks",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListLbPrivateNetworksResponse(res.json())

    async def list_lb_private_networks_all(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        order_by: Optional[ListPrivateNetworksRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[PrivateNetwork]:
        """
        List Private Networks attached to a Load Balancer.
        List the Private Networks attached to a given Load Balancer, specified by its Load Balancer ID. The response is an array of Private Network objects, giving information including the status, configuration, name and creation date of each Private Network.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :param order_by: Sort order of Private Network objects in the response.
        :param page_size: Number of objects to return.
        :param page: The page number to return, from the paginated results.
        :return: :class:`List[ListLbPrivateNetworksResponse] <List[ListLbPrivateNetworksResponse]>`

        Usage:
        ::

            result = await api.list_lb_private_networks_all(lb_id="example")
        """

        return await fetch_all_pages_async(
            type=ListLbPrivateNetworksResponse,
            key="private_network",
            fetcher=self.list_lb_private_networks,
            args={
                "lb_id": lb_id,
                "zone": zone,
                "order_by": order_by,
                "page_size": page_size,
                "page": page,
            },
        )

    async def attach_private_network(
        self,
        *,
        lb_id: str,
        private_network_id: str,
        zone: Optional[Zone] = None,
        static_config: Optional[PrivateNetworkStaticConfig] = None,
        dhcp_config: Optional[PrivateNetworkDHCPConfig] = None,
        ipam_config: Optional[PrivateNetworkIpamConfig] = None,
    ) -> PrivateNetwork:
        """
        Attach a Load Balancer to a Private Network.
        Attach a specified Load Balancer to a specified Private Network, defining a static or DHCP configuration for the Load Balancer on the network.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load Balancer ID.
        :param private_network_id: Private Network ID.
        :param static_config: Object containing an array of a local IP address for the Load Balancer on this Private Network.

        One-of ('config'): at most one of 'static_config', 'dhcp_config', 'ipam_config' could be set.
        :param dhcp_config: Defines whether to let DHCP assign IP addresses.

        One-of ('config'): at most one of 'static_config', 'dhcp_config', 'ipam_config' could be set.
        :param ipam_config: For internal use only.

        One-of ('config'): at most one of 'static_config', 'dhcp_config', 'ipam_config' could be set.
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = await api.attach_private_network(
                lb_id="example",
                private_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/private-networks/{param_private_network_id}/attach",
            body=marshal_ZonedApiAttachPrivateNetworkRequest(
                ZonedApiAttachPrivateNetworkRequest(
                    lb_id=lb_id,
                    private_network_id=private_network_id,
                    zone=zone,
                    static_config=static_config,
                    dhcp_config=dhcp_config,
                    ipam_config=ipam_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PrivateNetwork(res.json())

    async def detach_private_network(
        self,
        *,
        lb_id: str,
        private_network_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Detach Load Balancer from Private Network.
        Detach a specified Load Balancer from a specified Private Network.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param lb_id: Load balancer ID.
        :param private_network_id: Set your instance private network id.

        Usage:
        ::

            result = await api.detach_private_network(
                lb_id="example",
                private_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "POST",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/private-networks/{param_private_network_id}/detach",
        )

        self._throw_on_error(res)
        return None
