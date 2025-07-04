# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Any, Awaitable, Dict, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
    marshal_Money,
    unmarshal_Money,
    marshal_ScwFile,
    unmarshal_ScwFile,
    unmarshal_ServiceInfo,
    marshal_TimeSeries,
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    WaitForOptions,
    project_or_organization_id,
    random_name,
    resolve_one_of,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
)
from .types import (
    ListEventsRequestOrderBy,
    ResourceType,
    AccountOrganizationInfo,
    AccountUserInfo,
    Event,
    EventPrincipal,
    InstanceServerInfo,
    KeyManagerKeyInfo,
    KubernetesACLInfo,
    KubernetesClusterInfo,
    KubernetesNodeInfo,
    KubernetesPoolInfo,
    ListEventsRequest,
    ListEventsResponse,
    ListProductsRequest,
    ListProductsResponse,
    Product,
    ProductService,
    Resource,
    SecretManagerSecretInfo,
    SecretManagerSecretVersionInfo,
)
from .marshalling import (
    unmarshal_ListEventsResponse,
    unmarshal_ListProductsResponse,
)

class AuditTrailV1Alpha1API(API):
    """
    This API allows you to ensure accountability and security by recording events and changes performed within your Scaleway Organization.
    """
    def list_events(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        resource_type: Optional[ResourceType] = None,
        method_name: Optional[str] = None,
        status: Optional[int] = None,
        recorded_after: Optional[datetime] = None,
        recorded_before: Optional[datetime] = None,
        order_by: Optional[ListEventsRequestOrderBy] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        product_name: Optional[str] = None,
        service_name: Optional[str] = None,
    ) -> ListEventsResponse:
        """
        List events.
        Retrieve the list of Audit Trail events for a Scaleway Organization and/or Project. You must specify the `organization_id` and optionally, the `project_id`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: (Optional) ID of the Project containing the Audit Trail events.
        :param organization_id: ID of the Organization containing the Audit Trail events.
        :param resource_type: (Optional) Returns a paginated list of Scaleway resources' features.
        :param method_name: (Optional) Name of the method of the API call performed.
        :param status: (Optional) HTTP status code of the request. Returns either `200` if the request was successful or `403` if the permission was denied.
        :param recorded_after: (Optional) The `recorded_after` parameter defines the earliest timestamp from which Audit Trail events are retrieved. Returns `one hour ago` by default.
        :param recorded_before: (Optional) The `recorded_before` parameter defines the latest timestamp up to which Audit Trail events are retrieved. Returns `now` by default.
        :param order_by: 
        :param page_size: 
        :param page_token: 
        :param product_name: (Optional) Name of the Scaleway resource in a hyphenated format.
        :param service_name: (Optional) Name of the service of the API call performed.
        :return: :class:`ListEventsResponse <ListEventsResponse>`
        
        Usage:
        ::
        
            result = api.list_events()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "GET",
            f"/audit-trail/v1alpha1/regions/{param_region}/events",
            params={
                "method_name": method_name,
                "order_by": order_by,
                "organization_id": organization_id or self.client.default_organization_id,
                "page_size": page_size or self.client.default_page_size,
                "page_token": page_token,
                "product_name": product_name,
                "project_id": project_id or self.client.default_project_id,
                "recorded_after": recorded_after,
                "recorded_before": recorded_before,
                "resource_type": resource_type,
                "service_name": service_name,
                "status": status,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListEventsResponse(res.json())
        
    def list_products(
        self,
        *,
        region: Optional[ScwRegion] = None,
        organization_id: Optional[str] = None,
    ) -> ListProductsResponse:
        """
        Retrieve the list of Scaleway resources for which you have Audit Trail events.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: ID of the Organization containing the Audit Trail events.
        :return: :class:`ListProductsResponse <ListProductsResponse>`
        
        Usage:
        ::
        
            result = api.list_products()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "GET",
            f"/audit-trail/v1alpha1/regions/{param_region}/products",
            params={
                "organization_id": organization_id or self.client.default_organization_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListProductsResponse(res.json())
        
