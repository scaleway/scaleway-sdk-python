# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
    Zone,
)
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages,
    random_name,
    validate_path_param,
    wait_for_resource,
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
    """

    def list_lbs(
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
        List load balancers
        :param region: Region to target. If none is passed will use default region from the config
        :param name: Use this to search by name
        :param order_by: Response order
        :param page_size: The number of items to return
        :param page: Page number
        :param organization_id: Filter LBs by organization ID
        :param project_id: Filter LBs by project ID
        :return: :class:`ListLbsResponse <ListLbsResponse>`

        Usage:
        ::

            result = api.list_lbs()
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

    def list_lbs_all(
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
        List load balancers
        :param region: Region to target. If none is passed will use default region from the config
        :param name: Use this to search by name
        :param order_by: Response order
        :param page_size: The number of items to return
        :param page: Page number
        :param organization_id: Filter LBs by organization ID
        :param project_id: Filter LBs by project ID
        :return: :class:`List[ListLbsResponse] <List[ListLbsResponse]>`

        Usage:
        ::

            result = api.list_lbs_all()
        """

        return fetch_all_pages(
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

    def create_lb(
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
        tags: Optional[List[str]] = None,
    ) -> Lb:
        """
        Create a load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param organization_id: Owner of resources.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Assign the resource to a project ID.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param name: Resource names
        :param description: Resource description
        :param ip_id: Just like for compute instances, when you destroy a load balancer, you can keep its highly available IP address and reuse it for another load balancer later
        :param tags: List of keyword
        :param type_: Load balancer offer type
        :param ssl_compatibility_level: Enforces minimal SSL version (in SSL/TLS offloading context).
        - `intermediate` General-purpose servers with a variety of clients, recommended for almost all systems (Supports Firefox 27, Android 4.4.2, Chrome 31, Edge, IE 11 on Windows 7, Java 8u31, OpenSSL 1.0.1, Opera 20, and Safari 9).
        - `modern` Services with clients that support TLS 1.3 and don't need backward compatibility (Firefox 63, Android 10.0, Chrome 70, Edge 75, Java 11, OpenSSL 1.1.1, Opera 57, and Safari 12.1).
        - `old` Compatible with a number of very old clients, and should be used only as a last resort (Firefox 1, Android 2.3, Chrome 1, Edge 12, IE8 on Windows XP, Java 6, OpenSSL 0.9.8, Opera 5, and Safari 1).

        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.create_lb(
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
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    def get_lb(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
    ) -> Lb:
        """
        Get a load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.get_lb(lb_id="example")
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

    def wait_for_lb(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Lb, bool]] = None,
    ) -> Lb:
        """
        Waits for :class:`Lb <Lb>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
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

        return wait_for_resource(
            fetcher=self.get_lb,
            options=options,
            args={
                "lb_id": lb_id,
                "region": region,
            },
        )

    def update_lb(
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
        Update a load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :param name: Resource name
        :param description: Resource description
        :param tags: List of keywords
        :param ssl_compatibility_level: Enforces minimal SSL version (in SSL/TLS offloading context).
        - `intermediate` General-purpose servers with a variety of clients, recommended for almost all systems (Supports Firefox 27, Android 4.4.2, Chrome 31, Edge, IE 11 on Windows 7, Java 8u31, OpenSSL 1.0.1, Opera 20, and Safari 9).
        - `modern` Services with clients that support TLS 1.3 and don't need backward compatibility (Firefox 63, Android 10.0, Chrome 70, Edge 75, Java 11, OpenSSL 1.1.1, Opera 57, and Safari 12.1).
        - `old` Compatible with a number of very old clients, and should be used only as a last resort (Firefox 1, Android 2.3, Chrome 1, Edge 12, IE8 on Windows XP, Java 6, OpenSSL 0.9.8, Opera 5, and Safari 1).

        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.update_lb(
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

    def delete_lb(
        self,
        *,
        lb_id: str,
        release_ip: bool,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :param release_ip: Set true if you don't want to keep this IP address

        Usage:
        ::

            result = api.delete_lb(
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

    def migrate_lb(
        self,
        *,
        lb_id: str,
        type_: str,
        region: Optional[Region] = None,
    ) -> Lb:
        """
        Migrate a load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :param type_: Load balancer type (check /lb-types to list all type)
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.migrate_lb(
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

    def list_i_ps(
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
        List IPs
        :param region: Region to target. If none is passed will use default region from the config
        :param page: Page number
        :param page_size: The number of items to return
        :param ip_address: Use this to search by IP address
        :param organization_id: Filter IPs by organization id
        :param project_id: Filter IPs by project ID
        :return: :class:`ListIpsResponse <ListIpsResponse>`

        Usage:
        ::

            result = api.list_i_ps()
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

    def list_i_ps_all(
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
        List IPs
        :param region: Region to target. If none is passed will use default region from the config
        :param page: Page number
        :param page_size: The number of items to return
        :param ip_address: Use this to search by IP address
        :param organization_id: Filter IPs by organization id
        :param project_id: Filter IPs by project ID
        :return: :class:`List[ListIpsResponse] <List[ListIpsResponse]>`

        Usage:
        ::

            result = api.list_i_ps_all()
        """

        return fetch_all_pages(
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

    def create_ip(
        self,
        *,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        reverse: Optional[str] = None,
    ) -> Ip:
        """
        Create an IP
        :param region: Region to target. If none is passed will use default region from the config
        :param organization_id: Owner of resources.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Assign the resource to a project ID.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param reverse: Reverse domain name
        :return: :class:`Ip <Ip>`

        Usage:
        ::

            result = api.create_ip()
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

    def get_ip(
        self,
        *,
        ip_id: str,
        region: Optional[Region] = None,
    ) -> Ip:
        """
        Get an IP
        :param region: Region to target. If none is passed will use default region from the config
        :param ip_id: IP address ID
        :return: :class:`Ip <Ip>`

        Usage:
        ::

            result = api.get_ip(ip_id="example")
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

    def release_ip(
        self,
        *,
        ip_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete an IP
        :param region: Region to target. If none is passed will use default region from the config
        :param ip_id: IP address ID

        Usage:
        ::

            result = api.release_ip(ip_id="example")
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

    def update_ip(
        self,
        *,
        ip_id: str,
        region: Optional[Region] = None,
        reverse: Optional[str] = None,
    ) -> Ip:
        """
        Update an IP
        :param region: Region to target. If none is passed will use default region from the config
        :param ip_id: IP address ID
        :param reverse: Reverse DNS
        :return: :class:`Ip <Ip>`

        Usage:
        ::

            result = api.update_ip(ip_id="example")
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

    def list_backends(
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
        List backends in a given load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :param name: Use this to search by name
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :return: :class:`ListBackendsResponse <ListBackendsResponse>`

        Usage:
        ::

            result = api.list_backends(lb_id="example")
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

    def list_backends_all(
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
        List backends in a given load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :param name: Use this to search by name
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :return: :class:`List[ListBackendsResponse] <List[ListBackendsResponse]>`

        Usage:
        ::

            result = api.list_backends_all(lb_id="example")
        """

        return fetch_all_pages(
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

    def create_backend(
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
    ) -> Backend:
        """
        Create a backend in a given load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :param name: Resource name
        :param forward_protocol: Backend protocol. TCP or HTTP
        :param forward_port: User sessions will be forwarded to this port of backend servers
        :param forward_port_algorithm: Load balancing algorithm
        :param sticky_sessions: Enables cookie-based session persistence
        :param sticky_sessions_cookie_name: Cookie name for sticky sessions
        :param health_check: See the Healthcheck object description
        :param server_ip: Backend server IP addresses list (IPv4 or IPv6)
        :param send_proxy_v2: Deprecated in favor of proxy_protocol field !
        :param timeout_server: Maximum server connection inactivity time (allowed time the server has to process the request)
        :param timeout_connect: Maximum initial server connection establishment time
        :param timeout_tunnel: Maximum tunnel inactivity time after Websocket is established (take precedence over client and server timeout)
        :param on_marked_down_action: Modify what occurs when a backend server is marked down
        :param proxy_protocol: The PROXY protocol informs the other end about the incoming connection, so that it can know the client's address or the public address it accessed to, whatever the upper layer protocol.

        * `proxy_protocol_none` Disable proxy protocol.
        * `proxy_protocol_v1` Version one (text format).
        * `proxy_protocol_v2` Version two (binary format).
        * `proxy_protocol_v2_ssl` Version two with SSL connection.
        * `proxy_protocol_v2_ssl_cn` Version two with SSL connection and common name information.

        :param failover_host: Only the host part of the Scaleway S3 bucket website is expected.
        E.g. `failover-website.s3-website.fr-par.scw.cloud` if your bucket website URL is `https://failover-website.s3-website.fr-par.scw.cloud/`.

        :param ssl_bridging: Enable SSL between load balancer and backend servers
        :param ignore_ssl_server_verify: Set to true to ignore server certificate verification
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.create_backend(
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
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    def get_backend(
        self,
        *,
        backend_id: str,
        region: Optional[Region] = None,
    ) -> Backend:
        """
        Get a backend in a given load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param backend_id: Backend ID
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.get_backend(backend_id="example")
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

    def update_backend(
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
    ) -> Backend:
        """
        Update a backend in a given load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param backend_id: Backend ID to update
        :param name: Resource name
        :param forward_protocol: Backend protocol. TCP or HTTP
        :param forward_port: User sessions will be forwarded to this port of backend servers
        :param forward_port_algorithm: Load balancing algorithm
        :param sticky_sessions: Enable cookie-based session persistence
        :param sticky_sessions_cookie_name: Cookie name for sticky sessions
        :param send_proxy_v2: Deprecated in favor of proxy_protocol field!
        :param timeout_server: Maximum server connection inactivity time (allowed time the server has to process the request)
        :param timeout_connect: Maximum initial server connection establishment time
        :param timeout_tunnel: Maximum tunnel inactivity time after Websocket is established (take precedence over client and server timeout)
        :param on_marked_down_action: Modify what occurs when a backend server is marked down
        :param proxy_protocol: The PROXY protocol informs the other end about the incoming connection, so that it can know the client's address or the public address it accessed to, whatever the upper layer protocol is.

        * `proxy_protocol_none` Disable proxy protocol.
        * `proxy_protocol_v1` Version one (text format).
        * `proxy_protocol_v2` Version two (binary format).
        * `proxy_protocol_v2_ssl` Version two with SSL connection.
        * `proxy_protocol_v2_ssl_cn` Version two with SSL connection and common name information.

        :param failover_host: Only the host part of the Scaleway S3 bucket website is expected.
        Example: `failover-website.s3-website.fr-par.scw.cloud` if your bucket website URL is `https://failover-website.s3-website.fr-par.scw.cloud/`.

        :param ssl_bridging: Enable SSL between load balancer and backend servers
        :param ignore_ssl_server_verify: Set to true to ignore server certificate verification
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.update_backend(
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
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    def delete_backend(
        self,
        *,
        backend_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a backend in a given load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param backend_id: ID of the backend to delete

        Usage:
        ::

            result = api.delete_backend(backend_id="example")
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

    def add_backend_servers(
        self,
        *,
        backend_id: str,
        server_ip: List[str],
        region: Optional[Region] = None,
    ) -> Backend:
        """
        Add a set of servers in a given backend
        :param region: Region to target. If none is passed will use default region from the config
        :param backend_id: Backend ID
        :param server_ip: Set all IPs to add on your backend
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.add_backend_servers(
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

    def remove_backend_servers(
        self,
        *,
        backend_id: str,
        server_ip: List[str],
        region: Optional[Region] = None,
    ) -> Backend:
        """
        Remove a set of servers for a given backend
        :param region: Region to target. If none is passed will use default region from the config
        :param backend_id: Backend ID
        :param server_ip: Set all IPs to remove of your backend
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.remove_backend_servers(
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

    def set_backend_servers(
        self,
        *,
        backend_id: str,
        server_ip: List[str],
        region: Optional[Region] = None,
    ) -> Backend:
        """
        Define all servers in a given backend
        :param region: Region to target. If none is passed will use default region from the config
        :param backend_id: Backend ID
        :param server_ip: Set all IPs to add on your backend and remove all other
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.set_backend_servers(
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

    def update_health_check(
        self,
        *,
        backend_id: str,
        port: int,
        check_delay: str,
        check_timeout: str,
        check_max_retries: int,
        check_send_proxy: bool,
        region: Optional[Region] = None,
        mysql_config: Optional[HealthCheckMysqlConfig] = None,
        ldap_config: Optional[HealthCheckLdapConfig] = None,
        redis_config: Optional[HealthCheckRedisConfig] = None,
        pgsql_config: Optional[HealthCheckPgsqlConfig] = None,
        tcp_config: Optional[HealthCheckTcpConfig] = None,
        http_config: Optional[HealthCheckHttpConfig] = None,
        https_config: Optional[HealthCheckHttpsConfig] = None,
    ) -> HealthCheck:
        """
        Update an health check for a given backend
        :param region: Region to target. If none is passed will use default region from the config
        :param backend_id: Backend ID
        :param port: Specify the port used to health check
        :param check_delay: Time between two consecutive health checks
        :param check_timeout: Maximum time a backend server has to reply to the health check
        :param check_max_retries: Number of consecutive unsuccessful health checks, after which the server will be considered dead
        :param mysql_config: The check requires MySQL >=3.22, for older version, please use TCP check.

        One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
        :param ldap_config: The response is analyzed to find an LDAPv3 response message.

        One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
        :param redis_config: The response is analyzed to find the +PONG response message.

        One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
        :param pgsql_config: PostgreSQL health check.

        One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
        :param tcp_config: Basic TCP health check.

        One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
        :param http_config: HTTP health check.

        One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
        :param https_config: HTTPS health check.

        One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
        :param check_send_proxy: It defines whether the health check should be done considering the proxy protocol
        :return: :class:`HealthCheck <HealthCheck>`

        Usage:
        ::

            result = api.update_health_check(
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
                    mysql_config=mysql_config,
                    ldap_config=ldap_config,
                    redis_config=redis_config,
                    pgsql_config=pgsql_config,
                    tcp_config=tcp_config,
                    http_config=http_config,
                    https_config=https_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_HealthCheck(res.json())

    def list_frontends(
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
        List frontends in a given load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :param name: Use this to search by name
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :return: :class:`ListFrontendsResponse <ListFrontendsResponse>`

        Usage:
        ::

            result = api.list_frontends(lb_id="example")
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

    def list_frontends_all(
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
        List frontends in a given load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :param name: Use this to search by name
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :return: :class:`List[ListFrontendsResponse] <List[ListFrontendsResponse]>`

        Usage:
        ::

            result = api.list_frontends_all(lb_id="example")
        """

        return fetch_all_pages(
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

    def create_frontend(
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
        Create a frontend in a given load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :param name: Resource name
        :param inbound_port: TCP port to listen on the front side
        :param backend_id: Backend ID
        :param timeout_client: Set the maximum inactivity time on the client side
        :param certificate_id: Certificate ID, deprecated in favor of certificate_ids array !
        :param certificate_ids: List of certificate IDs to bind on the frontend
        :param enable_http3: Activate HTTP 3 protocol (beta)
        :return: :class:`Frontend <Frontend>`

        Usage:
        ::

            result = api.create_frontend(
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

    def get_frontend(
        self,
        *,
        frontend_id: str,
        region: Optional[Region] = None,
    ) -> Frontend:
        """
        Get a frontend
        :param region: Region to target. If none is passed will use default region from the config
        :param frontend_id: Frontend ID
        :return: :class:`Frontend <Frontend>`

        Usage:
        ::

            result = api.get_frontend(frontend_id="example")
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

    def update_frontend(
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
        Update a frontend
        :param region: Region to target. If none is passed will use default region from the config
        :param frontend_id: Frontend ID
        :param name: Resource name
        :param inbound_port: TCP port to listen on the front side
        :param backend_id: Backend ID
        :param timeout_client: Client session maximum inactivity time
        :param certificate_id: Certificate ID, deprecated in favor of `certificate_ids` array!
        :param certificate_ids: List of certificate IDs to bind on the frontend
        :param enable_http3: Activate HTTP 3 protocol (beta)
        :return: :class:`Frontend <Frontend>`

        Usage:
        ::

            result = api.update_frontend(
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

    def delete_frontend(
        self,
        *,
        frontend_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a frontend
        :param region: Region to target. If none is passed will use default region from the config
        :param frontend_id: Frontend ID to delete

        Usage:
        ::

            result = api.delete_frontend(frontend_id="example")
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

    def list_routes(
        self,
        *,
        region: Optional[Region] = None,
        order_by: ListRoutesRequestOrderBy = ListRoutesRequestOrderBy.CREATED_AT_ASC,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        frontend_id: Optional[str] = None,
    ) -> ListRoutesResponse:
        """
        List all backend redirections
        :param region: Region to target. If none is passed will use default region from the config
        :param order_by: Response order
        :param page_size: The number of items to return
        :param page: Page number
        :param frontend_id:
        :return: :class:`ListRoutesResponse <ListRoutesResponse>`

        Usage:
        ::

            result = api.list_routes()
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

    def list_routes_all(
        self,
        *,
        region: Optional[Region] = None,
        order_by: Optional[ListRoutesRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        frontend_id: Optional[str] = None,
    ) -> List[Route]:
        """
        List all backend redirections
        :param region: Region to target. If none is passed will use default region from the config
        :param order_by: Response order
        :param page_size: The number of items to return
        :param page: Page number
        :param frontend_id:
        :return: :class:`List[ListRoutesResponse] <List[ListRoutesResponse]>`

        Usage:
        ::

            result = api.list_routes_all()
        """

        return fetch_all_pages(
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

    def create_route(
        self,
        *,
        frontend_id: str,
        backend_id: str,
        region: Optional[Region] = None,
        match: Optional[RouteMatch] = None,
    ) -> Route:
        """
        Create a backend redirection
        :param region: Region to target. If none is passed will use default region from the config
        :param frontend_id: Origin of redirection
        :param backend_id: Destination of destination
        :param match: Value to match a redirection
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = api.create_route(
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

    def get_route(
        self,
        *,
        route_id: str,
        region: Optional[Region] = None,
    ) -> Route:
        """
        Get single backend redirection
        :param region: Region to target. If none is passed will use default region from the config
        :param route_id: Id of route to get
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = api.get_route(route_id="example")
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

    def update_route(
        self,
        *,
        route_id: str,
        backend_id: str,
        region: Optional[Region] = None,
        match: Optional[RouteMatch] = None,
    ) -> Route:
        """
        Edit a backend redirection
        :param region: Region to target. If none is passed will use default region from the config
        :param route_id: Route id to update
        :param backend_id: Backend id of redirection
        :param match: Value to match a redirection
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = api.update_route(
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

    def delete_route(
        self,
        *,
        route_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a backend redirection
        :param region: Region to target. If none is passed will use default region from the config
        :param route_id: Route id to delete

        Usage:
        ::

            result = api.delete_route(route_id="example")
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

    def get_lb_stats(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
    ) -> LbStats:
        """
        Get usage statistics of a given load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :return: :class:`LbStats <LbStats>`
        :deprecated

        Usage:
        ::

            result = api.get_lb_stats(lb_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/stats",
        )

        self._throw_on_error(res)
        return unmarshal_LbStats(res.json())

    def list_backend_stats(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListBackendStatsResponse:
        """

        Usage:
        ::

            result = api.list_backend_stats(lb_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/regions/{param_region}/lbs/{param_lb_id}/backend-stats",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListBackendStatsResponse(res.json())

    def list_backend_stats_all(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[BackendServerStats]:
        """
        :return: :class:`List[ListBackendStatsResponse] <List[ListBackendStatsResponse]>`

        Usage:
        ::

            result = api.list_backend_stats_all(lb_id="example")
        """

        return fetch_all_pages(
            type=ListBackendStatsResponse,
            key="backend_servers_stats",
            fetcher=self.list_backend_stats,
            args={
                "lb_id": lb_id,
                "region": region,
                "page": page,
                "page_size": page_size,
            },
        )

    def list_acls(
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
        List ACL for a given frontend
        :param region: Region to target. If none is passed will use default region from the config
        :param frontend_id: ID of your frontend
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :param name: Filter acl per name
        :return: :class:`ListAclResponse <ListAclResponse>`

        Usage:
        ::

            result = api.list_acls(frontend_id="example")
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

    def list_acls_all(
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
        List ACL for a given frontend
        :param region: Region to target. If none is passed will use default region from the config
        :param frontend_id: ID of your frontend
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :param name: Filter acl per name
        :return: :class:`List[ListAclResponse] <List[ListAclResponse]>`

        Usage:
        ::

            result = api.list_acls_all(frontend_id="example")
        """

        return fetch_all_pages(
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

    def create_acl(
        self,
        *,
        frontend_id: str,
        action: AclAction,
        match: AclMatch,
        index: int,
        description: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
    ) -> Acl:
        """
        Create an ACL for a given frontend
        :param region: Region to target. If none is passed will use default region from the config
        :param frontend_id: ID of your frontend
        :param name: Name of your ACL ressource
        :param action: Action to undertake when an ACL filter matches
        :param match: The ACL match rule. You can have one of those three cases:

          - `ip_subnet` is defined
          - `http_filter` and `http_filter_value` are defined
          - `ip_subnet`, `http_filter` and `http_filter_value` are defined

        :param index: Order between your Acls (ascending order, 0 is first acl executed)
        :param description: Description of your ACL ressource
        :return: :class:`Acl <Acl>`

        Usage:
        ::

            result = api.create_acl(
                frontend_id="example",
                action=AclAction(...),
                match=AclMatch(...),
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
                    match=match,
                    index=index,
                    description=description,
                    region=region,
                    name=name or random_name(prefix="acl"),
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Acl(res.json())

    def get_acl(
        self,
        *,
        acl_id: str,
        region: Optional[Region] = None,
    ) -> Acl:
        """
        Get an ACL
        :param region: Region to target. If none is passed will use default region from the config
        :param acl_id: ID of your ACL ressource
        :return: :class:`Acl <Acl>`

        Usage:
        ::

            result = api.get_acl(acl_id="example")
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

    def update_acl(
        self,
        *,
        acl_id: str,
        name: str,
        action: AclAction,
        match: AclMatch,
        index: int,
        region: Optional[Region] = None,
        description: Optional[str] = None,
    ) -> Acl:
        """
        Update an ACL
        :param region: Region to target. If none is passed will use default region from the config
        :param acl_id: ID of your ACL ressource
        :param name: Name of your ACL ressource
        :param action: Action to undertake when an ACL filter matches
        :param match: The ACL match rule. At least `ip_subnet` or `http_filter` and `http_filter_value` are required
        :param index: Order between your Acls (ascending order, 0 is first acl executed)
        :param description: Description of your ACL ressource
        :return: :class:`Acl <Acl>`

        Usage:
        ::

            result = api.update_acl(
                acl_id="example",
                name="example",
                action=AclAction(...),
                match=AclMatch(...),
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
                    match=match,
                    index=index,
                    region=region,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Acl(res.json())

    def delete_acl(
        self,
        *,
        acl_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete an ACL
        :param region: Region to target. If none is passed will use default region from the config
        :param acl_id: ID of your ACL ressource

        Usage:
        ::

            result = api.delete_acl(acl_id="example")
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

    def create_certificate(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        letsencrypt: Optional[CreateCertificateRequestLetsencryptConfig] = None,
        custom_certificate: Optional[CreateCertificateRequestCustomCertificate] = None,
    ) -> Certificate:
        """
        Generate a new TLS certificate using Let's Encrypt or import your certificate.
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :param name: Certificate name
        :param letsencrypt: Let's Encrypt type.

        One-of ('type_'): at most one of 'letsencrypt', 'custom_certificate' could be set.
        :param custom_certificate: Custom import certificate.

        One-of ('type_'): at most one of 'letsencrypt', 'custom_certificate' could be set.
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = api.create_certificate(lb_id="example")
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
                    name=name or random_name(prefix="certiticate"),
                    letsencrypt=letsencrypt,
                    custom_certificate=custom_certificate,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Certificate(res.json())

    def list_certificates(
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
        List all TLS certificates on a given load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :param name: Use this to search by name
        :return: :class:`ListCertificatesResponse <ListCertificatesResponse>`

        Usage:
        ::

            result = api.list_certificates(lb_id="example")
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

    def list_certificates_all(
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
        List all TLS certificates on a given load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :param name: Use this to search by name
        :return: :class:`List[ListCertificatesResponse] <List[ListCertificatesResponse]>`

        Usage:
        ::

            result = api.list_certificates_all(lb_id="example")
        """

        return fetch_all_pages(
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

    def get_certificate(
        self,
        *,
        certificate_id: str,
        region: Optional[Region] = None,
    ) -> Certificate:
        """
        Get a TLS certificate
        :param region: Region to target. If none is passed will use default region from the config
        :param certificate_id: Certificate ID
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = api.get_certificate(certificate_id="example")
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

    def wait_for_certificate(
        self,
        *,
        certificate_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Certificate, bool]] = None,
    ) -> Certificate:
        """
        Waits for :class:`Certificate <Certificate>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config
        :param certificate_id: Certificate ID
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

        return wait_for_resource(
            fetcher=self.get_certificate,
            options=options,
            args={
                "certificate_id": certificate_id,
                "region": region,
            },
        )

    def update_certificate(
        self,
        *,
        certificate_id: str,
        name: str,
        region: Optional[Region] = None,
    ) -> Certificate:
        """
        Update a TLS certificate
        :param region: Region to target. If none is passed will use default region from the config
        :param certificate_id: Certificate ID
        :param name: Certificate name
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = api.update_certificate(
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

    def delete_certificate(
        self,
        *,
        certificate_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a TLS certificate
        :param region: Region to target. If none is passed will use default region from the config
        :param certificate_id: Certificate ID

        Usage:
        ::

            result = api.delete_certificate(certificate_id="example")
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

    def list_lb_types(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListLbTypesResponse:
        """
        List all load balancer offer type
        :param region: Region to target. If none is passed will use default region from the config
        :param page: Page number
        :param page_size: The number of items to return
        :return: :class:`ListLbTypesResponse <ListLbTypesResponse>`

        Usage:
        ::

            result = api.list_lb_types()
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

    def list_lb_types_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[LbType]:
        """
        List all load balancer offer type
        :param region: Region to target. If none is passed will use default region from the config
        :param page: Page number
        :param page_size: The number of items to return
        :return: :class:`List[ListLbTypesResponse] <List[ListLbTypesResponse]>`

        Usage:
        ::

            result = api.list_lb_types_all()
        """

        return fetch_all_pages(
            type=ListLbTypesResponse,
            key="lb_types",
            fetcher=self.list_lb_types,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
            },
        )

    def create_subscriber(
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
        Create a subscriber, webhook or email
        :param region: Region to target. If none is passed will use default region from the config
        :param name: Subscriber name
        :param email_config: Email address configuration.

        One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
        :param webhook_config: WebHook URI configuration.

        One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
        :param organization_id: Owner of resources.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Assign the resource to a project ID.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :return: :class:`Subscriber <Subscriber>`

        Usage:
        ::

            result = api.create_subscriber(name="example")
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

    def get_subscriber(
        self,
        *,
        subscriber_id: str,
        region: Optional[Region] = None,
    ) -> Subscriber:
        """
        Get a subscriber
        :param region: Region to target. If none is passed will use default region from the config
        :param subscriber_id: Subscriber ID
        :return: :class:`Subscriber <Subscriber>`

        Usage:
        ::

            result = api.get_subscriber(subscriber_id="example")
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

    def list_subscriber(
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
        List all subscriber
        :param region: Region to target. If none is passed will use default region from the config
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :param name: Use this to search by name
        :param organization_id: Filter Subscribers by organization ID
        :param project_id: Filter Subscribers by project ID
        :return: :class:`ListSubscriberResponse <ListSubscriberResponse>`

        Usage:
        ::

            result = api.list_subscriber(name="example")
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

    def list_subscriber_all(
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
        List all subscriber
        :param region: Region to target. If none is passed will use default region from the config
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :param name: Use this to search by name
        :param organization_id: Filter Subscribers by organization ID
        :param project_id: Filter Subscribers by project ID
        :return: :class:`List[ListSubscriberResponse] <List[ListSubscriberResponse]>`

        Usage:
        ::

            result = api.list_subscriber_all(name="example")
        """

        return fetch_all_pages(
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

    def update_subscriber(
        self,
        *,
        subscriber_id: str,
        name: str,
        region: Optional[Region] = None,
        email_config: Optional[SubscriberEmailConfig] = None,
        webhook_config: Optional[SubscriberWebhookConfig] = None,
    ) -> Subscriber:
        """
        Update a subscriber
        :param region: Region to target. If none is passed will use default region from the config
        :param subscriber_id: Assign the resource to a project IDs
        :param name: Subscriber name
        :param email_config: Email address configuration.

        One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
        :param webhook_config: WebHook URI configuration.

        One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
        :return: :class:`Subscriber <Subscriber>`

        Usage:
        ::

            result = api.update_subscriber(
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

    def delete_subscriber(
        self,
        *,
        subscriber_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a subscriber
        :param region: Region to target. If none is passed will use default region from the config
        :param subscriber_id: Subscriber ID

        Usage:
        ::

            result = api.delete_subscriber(subscriber_id="example")
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

    def subscribe_to_lb(
        self,
        *,
        lb_id: str,
        subscriber_id: str,
        region: Optional[Region] = None,
    ) -> Lb:
        """
        Subscribe a subscriber to a given load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :param subscriber_id: Subscriber ID
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.subscribe_to_lb(
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

    def unsubscribe_from_lb(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
    ) -> Lb:
        """
        Unsubscribe a subscriber from a given load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.unsubscribe_from_lb(lb_id="example")
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

    def list_lb_private_networks(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        order_by: ListPrivateNetworksRequestOrderBy = ListPrivateNetworksRequestOrderBy.CREATED_AT_ASC,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListLbPrivateNetworksResponse:
        """
        List attached private network of load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :param order_by: Response order
        :param page_size: The number of items to return
        :param page: Page number
        :return: :class:`ListLbPrivateNetworksResponse <ListLbPrivateNetworksResponse>`

        Usage:
        ::

            result = api.list_lb_private_networks(lb_id="example")
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

    def list_lb_private_networks_all(
        self,
        *,
        lb_id: str,
        region: Optional[Region] = None,
        order_by: Optional[ListPrivateNetworksRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[PrivateNetwork]:
        """
        List attached private network of load balancer
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :param order_by: Response order
        :param page_size: The number of items to return
        :param page: Page number
        :return: :class:`List[ListLbPrivateNetworksResponse] <List[ListLbPrivateNetworksResponse]>`

        Usage:
        ::

            result = api.list_lb_private_networks_all(lb_id="example")
        """

        return fetch_all_pages(
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

    def attach_private_network(
        self,
        *,
        lb_id: str,
        private_network_id: str,
        region: Optional[Region] = None,
        static_config: Optional[PrivateNetworkStaticConfig] = None,
        dhcp_config: Optional[PrivateNetworkDHCPConfig] = None,
    ) -> PrivateNetwork:
        """
        Add load balancer on instance private network
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :param private_network_id: Set your instance private network id
        :param static_config: Define two local ip address of your choice for each load balancer instance.

        One-of ('config'): at most one of 'static_config', 'dhcp_config' could be set.
        :param dhcp_config: Set to true if you want to let DHCP assign IP addresses.

        One-of ('config'): at most one of 'static_config', 'dhcp_config' could be set.
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = api.attach_private_network(
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
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PrivateNetwork(res.json())

    def detach_private_network(
        self,
        *,
        lb_id: str,
        private_network_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Remove load balancer of private network
        :param region: Region to target. If none is passed will use default region from the config
        :param lb_id: Load balancer ID
        :param private_network_id: Set your instance private network id

        Usage:
        ::

            result = api.detach_private_network(
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
    Load balancer API.

    This API allows you to manage your load balancer service.
    """

    def list_lbs(
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
        List load balancers
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param name: Use this to search by name
        :param order_by: Response order
        :param page_size: The number of items to return
        :param page: Page number
        :param organization_id: Filter LBs by organization ID
        :param project_id: Filter LBs by project ID
        :return: :class:`ListLbsResponse <ListLbsResponse>`

        Usage:
        ::

            result = api.list_lbs()
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

    def list_lbs_all(
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
        List load balancers
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param name: Use this to search by name
        :param order_by: Response order
        :param page_size: The number of items to return
        :param page: Page number
        :param organization_id: Filter LBs by organization ID
        :param project_id: Filter LBs by project ID
        :return: :class:`List[ListLbsResponse] <List[ListLbsResponse]>`

        Usage:
        ::

            result = api.list_lbs_all()
        """

        return fetch_all_pages(
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

    def create_lb(
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
        tags: Optional[List[str]] = None,
    ) -> Lb:
        """
        Create a load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param organization_id: Owner of resources.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Assign the resource to a project ID.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param name: Resource names
        :param description: Resource description
        :param ip_id: Just like for compute instances, when you destroy a load balancer, you can keep its highly available IP address and reuse it for another load balancer later
        :param tags: List of keyword
        :param type_: Load balancer offer type
        :param ssl_compatibility_level: Enforces minimal SSL version (in SSL/TLS offloading context).
        - `intermediate` General-purpose servers with a variety of clients, recommended for almost all systems (Supports Firefox 27, Android 4.4.2, Chrome 31, Edge, IE 11 on Windows 7, Java 8u31, OpenSSL 1.0.1, Opera 20, and Safari 9).
        - `modern` Services with clients that support TLS 1.3 and don't need backward compatibility (Firefox 63, Android 10.0, Chrome 70, Edge 75, Java 11, OpenSSL 1.1.1, Opera 57, and Safari 12.1).
        - `old` Compatible with a number of very old clients, and should be used only as a last resort (Firefox 1, Android 2.3, Chrome 1, Edge 12, IE8 on Windows XP, Java 6, OpenSSL 0.9.8, Opera 5, and Safari 1).

        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.create_lb(
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
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    def get_lb(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
    ) -> Lb:
        """
        Get a load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.get_lb(lb_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    def wait_for_lb(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        options: Optional[WaitForOptions[Lb, bool]] = None,
    ) -> Lb:
        """
        Waits for :class:`Lb <Lb>` to be in a final state.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
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

        return wait_for_resource(
            fetcher=self.get_lb,
            options=options,
            args={
                "lb_id": lb_id,
                "zone": zone,
            },
        )

    def update_lb(
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
        Update a load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :param name: Resource name
        :param description: Resource description
        :param tags: List of keywords
        :param ssl_compatibility_level: Enforces minimal SSL version (in SSL/TLS offloading context).
        - `intermediate` General-purpose servers with a variety of clients, recommended for almost all systems (Supports Firefox 27, Android 4.4.2, Chrome 31, Edge, IE 11 on Windows 7, Java 8u31, OpenSSL 1.0.1, Opera 20, and Safari 9).
        - `modern` Services with clients that support TLS 1.3 and don't need backward compatibility (Firefox 63, Android 10.0, Chrome 70, Edge 75, Java 11, OpenSSL 1.1.1, Opera 57, and Safari 12.1).
        - `old` Compatible with a number of very old clients, and should be used only as a last resort (Firefox 1, Android 2.3, Chrome 1, Edge 12, IE8 on Windows XP, Java 6, OpenSSL 0.9.8, Opera 5, and Safari 1).

        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.update_lb(
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

    def delete_lb(
        self,
        *,
        lb_id: str,
        release_ip: bool,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :param release_ip: Set true if you don't want to keep this IP address

        Usage:
        ::

            result = api.delete_lb(
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

    def migrate_lb(
        self,
        *,
        lb_id: str,
        type_: str,
        zone: Optional[Zone] = None,
    ) -> Lb:
        """
        Migrate a load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :param type_: Load balancer type (check /lb-types to list all type)
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.migrate_lb(
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

    def list_i_ps(
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
        List IPs
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param page: Page number
        :param page_size: The number of items to return
        :param ip_address: Use this to search by IP address
        :param organization_id: Filter IPs by organization id
        :param project_id: Filter IPs by project ID
        :return: :class:`ListIpsResponse <ListIpsResponse>`

        Usage:
        ::

            result = api.list_i_ps()
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

    def list_i_ps_all(
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
        List IPs
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param page: Page number
        :param page_size: The number of items to return
        :param ip_address: Use this to search by IP address
        :param organization_id: Filter IPs by organization id
        :param project_id: Filter IPs by project ID
        :return: :class:`List[ListIpsResponse] <List[ListIpsResponse]>`

        Usage:
        ::

            result = api.list_i_ps_all()
        """

        return fetch_all_pages(
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

    def create_ip(
        self,
        *,
        zone: Optional[Zone] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        reverse: Optional[str] = None,
    ) -> Ip:
        """
        Create an IP
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param organization_id: Owner of resources.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Assign the resource to a project ID.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param reverse: Reverse domain name
        :return: :class:`Ip <Ip>`

        Usage:
        ::

            result = api.create_ip()
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

    def get_ip(
        self,
        *,
        ip_id: str,
        zone: Optional[Zone] = None,
    ) -> Ip:
        """
        Get an IP
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param ip_id: IP address ID
        :return: :class:`Ip <Ip>`

        Usage:
        ::

            result = api.get_ip(ip_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/ips/{param_ip_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Ip(res.json())

    def release_ip(
        self,
        *,
        ip_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete an IP
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param ip_id: IP address ID

        Usage:
        ::

            result = api.release_ip(ip_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/ips/{param_ip_id}",
        )

        self._throw_on_error(res)
        return None

    def update_ip(
        self,
        *,
        ip_id: str,
        zone: Optional[Zone] = None,
        reverse: Optional[str] = None,
    ) -> Ip:
        """
        Update an IP
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param ip_id: IP address ID
        :param reverse: Reverse DNS
        :return: :class:`Ip <Ip>`

        Usage:
        ::

            result = api.update_ip(ip_id="example")
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

    def list_backends(
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
        List backends in a given load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :param name: Use this to search by name
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :return: :class:`ListBackendsResponse <ListBackendsResponse>`

        Usage:
        ::

            result = api.list_backends(lb_id="example")
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

    def list_backends_all(
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
        List backends in a given load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :param name: Use this to search by name
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :return: :class:`List[ListBackendsResponse] <List[ListBackendsResponse]>`

        Usage:
        ::

            result = api.list_backends_all(lb_id="example")
        """

        return fetch_all_pages(
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

    def create_backend(
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
    ) -> Backend:
        """
        Create a backend in a given load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :param name: Resource name
        :param forward_protocol: Backend protocol. TCP or HTTP
        :param forward_port: User sessions will be forwarded to this port of backend servers
        :param forward_port_algorithm: Load balancing algorithm
        :param sticky_sessions: Enables cookie-based session persistence
        :param sticky_sessions_cookie_name: Cookie name for sticky sessions
        :param health_check: See the Healthcheck object description
        :param server_ip: Backend server IP addresses list (IPv4 or IPv6)
        :param send_proxy_v2: Deprecated in favor of proxy_protocol field !
        :param timeout_server: Maximum server connection inactivity time (allowed time the server has to process the request)
        :param timeout_connect: Maximum initial server connection establishment time
        :param timeout_tunnel: Maximum tunnel inactivity time after Websocket is established (take precedence over client and server timeout)
        :param on_marked_down_action: Modify what occurs when a backend server is marked down
        :param proxy_protocol: The PROXY protocol informs the other end about the incoming connection, so that it can know the client's address or the public address it accessed to, whatever the upper layer protocol.

        * `proxy_protocol_none` Disable proxy protocol.
        * `proxy_protocol_v1` Version one (text format).
        * `proxy_protocol_v2` Version two (binary format).
        * `proxy_protocol_v2_ssl` Version two with SSL connection.
        * `proxy_protocol_v2_ssl_cn` Version two with SSL connection and common name information.

        :param failover_host: Only the host part of the Scaleway S3 bucket website is expected.
        E.g. `failover-website.s3-website.fr-par.scw.cloud` if your bucket website URL is `https://failover-website.s3-website.fr-par.scw.cloud/`.

        :param ssl_bridging: Enable SSL between load balancer and backend servers
        :param ignore_ssl_server_verify: Set to true to ignore server certificate verification
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.create_backend(
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
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    def get_backend(
        self,
        *,
        backend_id: str,
        zone: Optional[Zone] = None,
    ) -> Backend:
        """
        Get a backend in a given load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param backend_id: Backend ID
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.get_backend(backend_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/backends/{param_backend_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    def update_backend(
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
    ) -> Backend:
        """
        Update a backend in a given load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param backend_id: Backend ID to update
        :param name: Resource name
        :param forward_protocol: Backend protocol. TCP or HTTP
        :param forward_port: User sessions will be forwarded to this port of backend servers
        :param forward_port_algorithm: Load balancing algorithm
        :param sticky_sessions: Enable cookie-based session persistence
        :param sticky_sessions_cookie_name: Cookie name for sticky sessions
        :param send_proxy_v2: Deprecated in favor of proxy_protocol field!
        :param timeout_server: Maximum server connection inactivity time (allowed time the server has to process the request)
        :param timeout_connect: Maximum initial server connection establishment time
        :param timeout_tunnel: Maximum tunnel inactivity time after Websocket is established (take precedence over client and server timeout)
        :param on_marked_down_action: Modify what occurs when a backend server is marked down
        :param proxy_protocol: The PROXY protocol informs the other end about the incoming connection, so that it can know the client's address or the public address it accessed to, whatever the upper layer protocol is.

        * `proxy_protocol_none` Disable proxy protocol.
        * `proxy_protocol_v1` Version one (text format).
        * `proxy_protocol_v2` Version two (binary format).
        * `proxy_protocol_v2_ssl` Version two with SSL connection.
        * `proxy_protocol_v2_ssl_cn` Version two with SSL connection and common name information.

        :param failover_host: Only the host part of the Scaleway S3 bucket website is expected.
        Example: `failover-website.s3-website.fr-par.scw.cloud` if your bucket website URL is `https://failover-website.s3-website.fr-par.scw.cloud/`.

        :param ssl_bridging: Enable SSL between load balancer and backend servers
        :param ignore_ssl_server_verify: Set to true to ignore server certificate verification
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.update_backend(
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
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Backend(res.json())

    def delete_backend(
        self,
        *,
        backend_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a backend in a given load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param backend_id: ID of the backend to delete

        Usage:
        ::

            result = api.delete_backend(backend_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_backend_id = validate_path_param("backend_id", backend_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/backends/{param_backend_id}",
        )

        self._throw_on_error(res)
        return None

    def add_backend_servers(
        self,
        *,
        backend_id: str,
        server_ip: List[str],
        zone: Optional[Zone] = None,
    ) -> Backend:
        """
        Add a set of servers in a given backend
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param backend_id: Backend ID
        :param server_ip: Set all IPs to add on your backend
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.add_backend_servers(
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

    def remove_backend_servers(
        self,
        *,
        backend_id: str,
        server_ip: List[str],
        zone: Optional[Zone] = None,
    ) -> Backend:
        """
        Remove a set of servers for a given backend
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param backend_id: Backend ID
        :param server_ip: Set all IPs to remove of your backend
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.remove_backend_servers(
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

    def set_backend_servers(
        self,
        *,
        backend_id: str,
        server_ip: List[str],
        zone: Optional[Zone] = None,
    ) -> Backend:
        """
        Define all servers in a given backend
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param backend_id: Backend ID
        :param server_ip: Set all IPs to add on your backend and remove all other
        :return: :class:`Backend <Backend>`

        Usage:
        ::

            result = api.set_backend_servers(
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

    def update_health_check(
        self,
        *,
        backend_id: str,
        port: int,
        check_delay: str,
        check_timeout: str,
        check_max_retries: int,
        check_send_proxy: bool,
        zone: Optional[Zone] = None,
        mysql_config: Optional[HealthCheckMysqlConfig] = None,
        ldap_config: Optional[HealthCheckLdapConfig] = None,
        redis_config: Optional[HealthCheckRedisConfig] = None,
        pgsql_config: Optional[HealthCheckPgsqlConfig] = None,
        tcp_config: Optional[HealthCheckTcpConfig] = None,
        http_config: Optional[HealthCheckHttpConfig] = None,
        https_config: Optional[HealthCheckHttpsConfig] = None,
    ) -> HealthCheck:
        """
        Update an healthcheck for a given backend
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param backend_id: Backend ID
        :param port: Specify the port used to health check
        :param check_delay: Time between two consecutive health checks
        :param check_timeout: Maximum time a backend server has to reply to the health check
        :param check_max_retries: Number of consecutive unsuccessful health checks, after which the server will be considered dead
        :param mysql_config: The check requires MySQL >=3.22, for older version, please use TCP check.

        One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
        :param ldap_config: The response is analyzed to find an LDAPv3 response message.

        One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
        :param redis_config: The response is analyzed to find the +PONG response message.

        One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
        :param pgsql_config: PostgreSQL health check.

        One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
        :param tcp_config: Basic TCP health check.

        One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
        :param http_config: HTTP health check.

        One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
        :param https_config: HTTPS health check.

        One-of ('config'): at most one of 'mysql_config', 'ldap_config', 'redis_config', 'pgsql_config', 'tcp_config', 'http_config', 'https_config' could be set.
        :param check_send_proxy: It defines whether the health check should be done considering the proxy protocol
        :return: :class:`HealthCheck <HealthCheck>`

        Usage:
        ::

            result = api.update_health_check(
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
                    mysql_config=mysql_config,
                    ldap_config=ldap_config,
                    redis_config=redis_config,
                    pgsql_config=pgsql_config,
                    tcp_config=tcp_config,
                    http_config=http_config,
                    https_config=https_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_HealthCheck(res.json())

    def list_frontends(
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
        List frontends in a given load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :param name: Use this to search by name
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :return: :class:`ListFrontendsResponse <ListFrontendsResponse>`

        Usage:
        ::

            result = api.list_frontends(lb_id="example")
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

    def list_frontends_all(
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
        List frontends in a given load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :param name: Use this to search by name
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :return: :class:`List[ListFrontendsResponse] <List[ListFrontendsResponse]>`

        Usage:
        ::

            result = api.list_frontends_all(lb_id="example")
        """

        return fetch_all_pages(
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

    def create_frontend(
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
        Create a frontend in a given load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :param name: Resource name
        :param inbound_port: TCP port to listen on the front side
        :param backend_id: Backend ID
        :param timeout_client: Set the maximum inactivity time on the client side
        :param certificate_id: Certificate ID, deprecated in favor of certificate_ids array !
        :param certificate_ids: List of certificate IDs to bind on the frontend
        :param enable_http3: Activate HTTP 3 protocol (beta)
        :return: :class:`Frontend <Frontend>`

        Usage:
        ::

            result = api.create_frontend(
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

    def get_frontend(
        self,
        *,
        frontend_id: str,
        zone: Optional[Zone] = None,
    ) -> Frontend:
        """
        Get a frontend
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param frontend_id: Frontend ID
        :return: :class:`Frontend <Frontend>`

        Usage:
        ::

            result = api.get_frontend(frontend_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/frontends/{param_frontend_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Frontend(res.json())

    def update_frontend(
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
        Update a frontend
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param frontend_id: Frontend ID
        :param name: Resource name
        :param inbound_port: TCP port to listen on the front side
        :param backend_id: Backend ID
        :param timeout_client: Client session maximum inactivity time
        :param certificate_id: Certificate ID, deprecated in favor of `certificate_ids` array!
        :param certificate_ids: List of certificate IDs to bind on the frontend
        :param enable_http3: Activate HTTP 3 protocol (beta)
        :return: :class:`Frontend <Frontend>`

        Usage:
        ::

            result = api.update_frontend(
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

    def delete_frontend(
        self,
        *,
        frontend_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a frontend
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param frontend_id: Frontend ID to delete

        Usage:
        ::

            result = api.delete_frontend(frontend_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_frontend_id = validate_path_param("frontend_id", frontend_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/frontends/{param_frontend_id}",
        )

        self._throw_on_error(res)
        return None

    def list_routes(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: ListRoutesRequestOrderBy = ListRoutesRequestOrderBy.CREATED_AT_ASC,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        frontend_id: Optional[str] = None,
    ) -> ListRoutesResponse:
        """
        List all backend redirections
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: Response order
        :param page_size: The number of items to return
        :param page: Page number
        :param frontend_id:
        :return: :class:`ListRoutesResponse <ListRoutesResponse>`

        Usage:
        ::

            result = api.list_routes()
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

    def list_routes_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListRoutesRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        frontend_id: Optional[str] = None,
    ) -> List[Route]:
        """
        List all backend redirections
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: Response order
        :param page_size: The number of items to return
        :param page: Page number
        :param frontend_id:
        :return: :class:`List[ListRoutesResponse] <List[ListRoutesResponse]>`

        Usage:
        ::

            result = api.list_routes_all()
        """

        return fetch_all_pages(
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

    def create_route(
        self,
        *,
        frontend_id: str,
        backend_id: str,
        zone: Optional[Zone] = None,
        match: Optional[RouteMatch] = None,
    ) -> Route:
        """
        Create a backend redirection
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param frontend_id: Origin of redirection
        :param backend_id: Destination of destination
        :param match: Value to match a redirection
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = api.create_route(
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

    def get_route(
        self,
        *,
        route_id: str,
        zone: Optional[Zone] = None,
    ) -> Route:
        """
        Get single backend redirection
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param route_id: Id of route to get
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = api.get_route(route_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/routes/{param_route_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    def update_route(
        self,
        *,
        route_id: str,
        backend_id: str,
        zone: Optional[Zone] = None,
        match: Optional[RouteMatch] = None,
    ) -> Route:
        """
        Edit a backend redirection
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param route_id: Route id to update
        :param backend_id: Backend id of redirection
        :param match: Value to match a redirection
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = api.update_route(
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

    def delete_route(
        self,
        *,
        route_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a backend redirection
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param route_id: Route id to delete

        Usage:
        ::

            result = api.delete_route(route_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/routes/{param_route_id}",
        )

        self._throw_on_error(res)
        return None

    def get_lb_stats(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
    ) -> LbStats:
        """
        Get usage statistics of a given load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :return: :class:`LbStats <LbStats>`
        :deprecated

        Usage:
        ::

            result = api.get_lb_stats(lb_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/stats",
        )

        self._throw_on_error(res)
        return unmarshal_LbStats(res.json())

    def list_backend_stats(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListBackendStatsResponse:
        """

        Usage:
        ::

            result = api.list_backend_stats(lb_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/lbs/{param_lb_id}/backend-stats",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListBackendStatsResponse(res.json())

    def list_backend_stats_all(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[BackendServerStats]:
        """
        :return: :class:`List[ListBackendStatsResponse] <List[ListBackendStatsResponse]>`

        Usage:
        ::

            result = api.list_backend_stats_all(lb_id="example")
        """

        return fetch_all_pages(
            type=ListBackendStatsResponse,
            key="backend_servers_stats",
            fetcher=self.list_backend_stats,
            args={
                "lb_id": lb_id,
                "zone": zone,
                "page": page,
                "page_size": page_size,
            },
        )

    def list_acls(
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
        List ACL for a given frontend
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param frontend_id: ID of your frontend
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :param name: Filter acl per name
        :return: :class:`ListAclResponse <ListAclResponse>`

        Usage:
        ::

            result = api.list_acls(frontend_id="example")
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

    def list_acls_all(
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
        List ACL for a given frontend
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param frontend_id: ID of your frontend
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :param name: Filter acl per name
        :return: :class:`List[ListAclResponse] <List[ListAclResponse]>`

        Usage:
        ::

            result = api.list_acls_all(frontend_id="example")
        """

        return fetch_all_pages(
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

    def create_acl(
        self,
        *,
        frontend_id: str,
        action: AclAction,
        match: AclMatch,
        index: int,
        description: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
    ) -> Acl:
        """
        Create an ACL for a given frontend
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param frontend_id: ID of your frontend
        :param name: Name of your ACL ressource
        :param action: Action to undertake when an ACL filter matches
        :param match: The ACL match rule. You can have one of those three cases:

          - `ip_subnet` is defined
          - `http_filter` and `http_filter_value` are defined
          - `ip_subnet`, `http_filter` and `http_filter_value` are defined

        :param index: Order between your Acls (ascending order, 0 is first acl executed)
        :param description: Description of your ACL ressource
        :return: :class:`Acl <Acl>`

        Usage:
        ::

            result = api.create_acl(
                frontend_id="example",
                action=AclAction(...),
                match=AclMatch(...),
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
                    match=match,
                    index=index,
                    description=description,
                    zone=zone,
                    name=name or random_name(prefix="acl"),
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Acl(res.json())

    def get_acl(
        self,
        *,
        acl_id: str,
        zone: Optional[Zone] = None,
    ) -> Acl:
        """
        Get an ACL
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param acl_id: ID of your ACL ressource
        :return: :class:`Acl <Acl>`

        Usage:
        ::

            result = api.get_acl(acl_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_acl_id = validate_path_param("acl_id", acl_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/acls/{param_acl_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Acl(res.json())

    def update_acl(
        self,
        *,
        acl_id: str,
        name: str,
        action: AclAction,
        match: AclMatch,
        index: int,
        zone: Optional[Zone] = None,
        description: Optional[str] = None,
    ) -> Acl:
        """
        Update an ACL
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param acl_id: ID of your ACL ressource
        :param name: Name of your ACL ressource
        :param action: Action to undertake when an ACL filter matches
        :param match: The ACL match rule. At least `ip_subnet` or `http_filter` and `http_filter_value` are required
        :param index: Order between your Acls (ascending order, 0 is first acl executed)
        :param description: Description of your ACL ressource
        :return: :class:`Acl <Acl>`

        Usage:
        ::

            result = api.update_acl(
                acl_id="example",
                name="example",
                action=AclAction(...),
                match=AclMatch(...),
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
                    match=match,
                    index=index,
                    zone=zone,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Acl(res.json())

    def delete_acl(
        self,
        *,
        acl_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete an ACL
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param acl_id: ID of your ACL ressource

        Usage:
        ::

            result = api.delete_acl(acl_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_acl_id = validate_path_param("acl_id", acl_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/acls/{param_acl_id}",
        )

        self._throw_on_error(res)
        return None

    def set_acls(
        self,
        *,
        frontend_id: str,
        acls: List[AclSpec],
        zone: Optional[Zone] = None,
    ) -> SetAclsResponse:
        """
        Set all ACLs for a given frontend
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param frontend_id: The Frontend to change ACL to
        :param acls: Array of ACLs to erease the existing ACLs
        :return: :class:`SetAclsResponse <SetAclsResponse>`

        Usage:
        ::

            result = api.set_acls(
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

    def create_certificate(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        letsencrypt: Optional[CreateCertificateRequestLetsencryptConfig] = None,
        custom_certificate: Optional[CreateCertificateRequestCustomCertificate] = None,
    ) -> Certificate:
        """
        Generate a new TLS certificate using Let's Encrypt or import your certificate.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :param name: Certificate name
        :param letsencrypt: Let's Encrypt type.

        One-of ('type_'): at most one of 'letsencrypt', 'custom_certificate' could be set.
        :param custom_certificate: Custom import certificate.

        One-of ('type_'): at most one of 'letsencrypt', 'custom_certificate' could be set.
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = api.create_certificate(lb_id="example")
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
                    name=name or random_name(prefix="certiticate"),
                    letsencrypt=letsencrypt,
                    custom_certificate=custom_certificate,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Certificate(res.json())

    def list_certificates(
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
        List all TLS certificates on a given load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :param name: Use this to search by name
        :return: :class:`ListCertificatesResponse <ListCertificatesResponse>`

        Usage:
        ::

            result = api.list_certificates(lb_id="example")
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

    def list_certificates_all(
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
        List all TLS certificates on a given load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :param name: Use this to search by name
        :return: :class:`List[ListCertificatesResponse] <List[ListCertificatesResponse]>`

        Usage:
        ::

            result = api.list_certificates_all(lb_id="example")
        """

        return fetch_all_pages(
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

    def get_certificate(
        self,
        *,
        certificate_id: str,
        zone: Optional[Zone] = None,
    ) -> Certificate:
        """
        Get a TLS certificate
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param certificate_id: Certificate ID
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = api.get_certificate(certificate_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_certificate_id = validate_path_param("certificate_id", certificate_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/certificates/{param_certificate_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Certificate(res.json())

    def wait_for_certificate(
        self,
        *,
        certificate_id: str,
        zone: Optional[Zone] = None,
        options: Optional[WaitForOptions[Certificate, bool]] = None,
    ) -> Certificate:
        """
        Waits for :class:`Certificate <Certificate>` to be in a final state.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param certificate_id: Certificate ID
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

        return wait_for_resource(
            fetcher=self.get_certificate,
            options=options,
            args={
                "certificate_id": certificate_id,
                "zone": zone,
            },
        )

    def update_certificate(
        self,
        *,
        certificate_id: str,
        name: str,
        zone: Optional[Zone] = None,
    ) -> Certificate:
        """
        Update a TLS certificate
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param certificate_id: Certificate ID
        :param name: Certificate name
        :return: :class:`Certificate <Certificate>`

        Usage:
        ::

            result = api.update_certificate(
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

    def delete_certificate(
        self,
        *,
        certificate_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a TLS certificate
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param certificate_id: Certificate ID

        Usage:
        ::

            result = api.delete_certificate(certificate_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_certificate_id = validate_path_param("certificate_id", certificate_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/certificates/{param_certificate_id}",
        )

        self._throw_on_error(res)
        return None

    def list_lb_types(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListLbTypesResponse:
        """
        List all load balancer offer type
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param page: Page number
        :param page_size: The number of items to return
        :return: :class:`ListLbTypesResponse <ListLbTypesResponse>`

        Usage:
        ::

            result = api.list_lb_types()
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

    def list_lb_types_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[LbType]:
        """
        List all load balancer offer type
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param page: Page number
        :param page_size: The number of items to return
        :return: :class:`List[ListLbTypesResponse] <List[ListLbTypesResponse]>`

        Usage:
        ::

            result = api.list_lb_types_all()
        """

        return fetch_all_pages(
            type=ListLbTypesResponse,
            key="lb_types",
            fetcher=self.list_lb_types,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
            },
        )

    def create_subscriber(
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
        Create a subscriber, webhook or email
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param name: Subscriber name
        :param email_config: Email address configuration.

        One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
        :param webhook_config: WebHook URI configuration.

        One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
        :param organization_id: Owner of resources.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Assign the resource to a project ID.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :return: :class:`Subscriber <Subscriber>`

        Usage:
        ::

            result = api.create_subscriber(name="example")
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

    def get_subscriber(
        self,
        *,
        subscriber_id: str,
        zone: Optional[Zone] = None,
    ) -> Subscriber:
        """
        Get a subscriber
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param subscriber_id: Subscriber ID
        :return: :class:`Subscriber <Subscriber>`

        Usage:
        ::

            result = api.get_subscriber(subscriber_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_subscriber_id = validate_path_param("subscriber_id", subscriber_id)

        res = self._request(
            "GET",
            f"/lb/v1/zones/{param_zone}/subscribers/{param_subscriber_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Subscriber(res.json())

    def list_subscriber(
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
        List all subscriber
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :param name: Use this to search by name
        :param organization_id: Filter Subscribers by organization ID
        :param project_id: Filter Subscribers by project ID
        :return: :class:`ListSubscriberResponse <ListSubscriberResponse>`

        Usage:
        ::

            result = api.list_subscriber(name="example")
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

    def list_subscriber_all(
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
        List all subscriber
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param order_by: Response order
        :param page: Page number
        :param page_size: The number of items to return
        :param name: Use this to search by name
        :param organization_id: Filter Subscribers by organization ID
        :param project_id: Filter Subscribers by project ID
        :return: :class:`List[ListSubscriberResponse] <List[ListSubscriberResponse]>`

        Usage:
        ::

            result = api.list_subscriber_all(name="example")
        """

        return fetch_all_pages(
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

    def update_subscriber(
        self,
        *,
        subscriber_id: str,
        name: str,
        zone: Optional[Zone] = None,
        email_config: Optional[SubscriberEmailConfig] = None,
        webhook_config: Optional[SubscriberWebhookConfig] = None,
    ) -> Subscriber:
        """
        Update a subscriber
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param subscriber_id: Assign the resource to a project IDs
        :param name: Subscriber name
        :param email_config: Email address configuration.

        One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
        :param webhook_config: WebHook URI configuration.

        One-of ('config'): at most one of 'email_config', 'webhook_config' could be set.
        :return: :class:`Subscriber <Subscriber>`

        Usage:
        ::

            result = api.update_subscriber(
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

    def delete_subscriber(
        self,
        *,
        subscriber_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a subscriber
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param subscriber_id: Subscriber ID

        Usage:
        ::

            result = api.delete_subscriber(subscriber_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_subscriber_id = validate_path_param("subscriber_id", subscriber_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/lb/subscription/{param_subscriber_id}",
        )

        self._throw_on_error(res)
        return None

    def subscribe_to_lb(
        self,
        *,
        lb_id: str,
        subscriber_id: str,
        zone: Optional[Zone] = None,
    ) -> Lb:
        """
        Subscribe a subscriber to a given load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :param subscriber_id: Subscriber ID
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.subscribe_to_lb(
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

    def unsubscribe_from_lb(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
    ) -> Lb:
        """
        Unsubscribe a subscriber from a given load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :return: :class:`Lb <Lb>`

        Usage:
        ::

            result = api.unsubscribe_from_lb(lb_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_lb_id = validate_path_param("lb_id", lb_id)

        res = self._request(
            "DELETE",
            f"/lb/v1/zones/{param_zone}/lb/{param_lb_id}/unsubscribe",
        )

        self._throw_on_error(res)
        return unmarshal_Lb(res.json())

    def list_lb_private_networks(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        order_by: ListPrivateNetworksRequestOrderBy = ListPrivateNetworksRequestOrderBy.CREATED_AT_ASC,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> ListLbPrivateNetworksResponse:
        """
        List attached private network of load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :param order_by: Response order
        :param page_size: The number of items to return
        :param page: Page number
        :return: :class:`ListLbPrivateNetworksResponse <ListLbPrivateNetworksResponse>`

        Usage:
        ::

            result = api.list_lb_private_networks(lb_id="example")
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

    def list_lb_private_networks_all(
        self,
        *,
        lb_id: str,
        zone: Optional[Zone] = None,
        order_by: Optional[ListPrivateNetworksRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[PrivateNetwork]:
        """
        List attached private network of load balancer
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :param order_by: Response order
        :param page_size: The number of items to return
        :param page: Page number
        :return: :class:`List[ListLbPrivateNetworksResponse] <List[ListLbPrivateNetworksResponse]>`

        Usage:
        ::

            result = api.list_lb_private_networks_all(lb_id="example")
        """

        return fetch_all_pages(
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

    def attach_private_network(
        self,
        *,
        lb_id: str,
        private_network_id: str,
        zone: Optional[Zone] = None,
        static_config: Optional[PrivateNetworkStaticConfig] = None,
        dhcp_config: Optional[PrivateNetworkDHCPConfig] = None,
    ) -> PrivateNetwork:
        """
        Add load balancer on instance private network
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :param private_network_id: Set your instance private network id
        :param static_config: Define two local ip address of your choice for each load balancer instance.

        One-of ('config'): at most one of 'static_config', 'dhcp_config' could be set.
        :param dhcp_config: Set to true if you want to let DHCP assign IP addresses.

        One-of ('config'): at most one of 'static_config', 'dhcp_config' could be set.
        :return: :class:`PrivateNetwork <PrivateNetwork>`

        Usage:
        ::

            result = api.attach_private_network(
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
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PrivateNetwork(res.json())

    def detach_private_network(
        self,
        *,
        lb_id: str,
        private_network_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Remove load balancer of private network
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param lb_id: Load balancer ID
        :param private_network_id: Set your instance private network id

        Usage:
        ::

            result = api.detach_private_network(
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
