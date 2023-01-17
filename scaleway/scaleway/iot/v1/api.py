# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Any, Dict, List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages,
    random_name,
    validate_path_param,
    wait_for_resource,
)
from .types import (
    DeviceStatus,
    HubProductPlan,
    ListDevicesRequestOrderBy,
    ListHubsRequestOrderBy,
    ListNetworksRequestOrderBy,
    ListRoutesRequestOrderBy,
    NetworkNetworkType,
    CreateDeviceResponse,
    CreateNetworkResponse,
    CreateRouteRequestDatabaseConfig,
    CreateRouteRequestRestConfig,
    CreateRouteRequestS3Config,
    Device,
    DeviceMessageFilters,
    GetDeviceCertificateResponse,
    GetDeviceMetricsResponse,
    GetHubCAResponse,
    GetHubMetricsResponse,
    Hub,
    HubTwinsGraphiteConfig,
    ListDevicesResponse,
    ListHubsResponse,
    ListNetworksResponse,
    ListRoutesResponse,
    ListTwinDocumentsResponse,
    Network,
    RenewDeviceCertificateResponse,
    Route,
    RouteSummary,
    SetDeviceCertificateResponse,
    TwinDocument,
    UpdateRouteRequestDatabaseConfig,
    UpdateRouteRequestRestConfig,
    UpdateRouteRequestS3Config,
    CreateHubRequest,
    UpdateHubRequest,
    SetHubCARequest,
    CreateDeviceRequest,
    UpdateDeviceRequest,
    SetDeviceCertificateRequest,
    CreateRouteRequest,
    UpdateRouteRequest,
    CreateNetworkRequest,
    PutTwinDocumentRequest,
    PatchTwinDocumentRequest,
)
from .content import (
    HUB_TRANSIENT_STATUSES,
)
from .marshalling import (
    marshal_CreateDeviceRequest,
    marshal_CreateHubRequest,
    marshal_CreateNetworkRequest,
    marshal_CreateRouteRequest,
    marshal_PatchTwinDocumentRequest,
    marshal_PutTwinDocumentRequest,
    marshal_SetDeviceCertificateRequest,
    marshal_SetHubCARequest,
    marshal_UpdateDeviceRequest,
    marshal_UpdateHubRequest,
    marshal_UpdateRouteRequest,
    unmarshal_Device,
    unmarshal_Hub,
    unmarshal_Network,
    unmarshal_CreateDeviceResponse,
    unmarshal_CreateNetworkResponse,
    unmarshal_GetDeviceCertificateResponse,
    unmarshal_GetDeviceMetricsResponse,
    unmarshal_GetHubCAResponse,
    unmarshal_GetHubMetricsResponse,
    unmarshal_ListDevicesResponse,
    unmarshal_ListHubsResponse,
    unmarshal_ListNetworksResponse,
    unmarshal_ListRoutesResponse,
    unmarshal_ListTwinDocumentsResponse,
    unmarshal_RenewDeviceCertificateResponse,
    unmarshal_Route,
    unmarshal_SetDeviceCertificateResponse,
    unmarshal_TwinDocument,
)


class IotV1API(API):
    """
    IoT API.

    This API allows you to manage IoT hubs and devices.
    """

    def list_hubs(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListHubsRequestOrderBy = ListHubsRequestOrderBy.NAME_ASC,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ListHubsResponse:
        """
        List hubs
        :param region: Region to target. If none is passed will use default region from the config
        :param page: Page number
        :param page_size: Page size. The maximum value is 100
        :param order_by: Ordering of requested hub
        :param project_id: Filter on project
        :param organization_id: Filter on the organization
        :param name: Filter on the name
        :return: :class:`ListHubsResponse <ListHubsResponse>`

        Usage:
        ::

            result = api.list_hubs()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/hubs",
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
        return unmarshal_ListHubsResponse(res.json())

    def list_hubs_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListHubsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> List[Hub]:
        """
        List hubs
        :param region: Region to target. If none is passed will use default region from the config
        :param page: Page number
        :param page_size: Page size. The maximum value is 100
        :param order_by: Ordering of requested hub
        :param project_id: Filter on project
        :param organization_id: Filter on the organization
        :param name: Filter on the name
        :return: :class:`List[ListHubsResponse] <List[ListHubsResponse]>`

        Usage:
        ::

            result = api.list_hubs_all()
        """

        return fetch_all_pages(
            type=ListHubsResponse,
            key="hubs",
            fetcher=self.list_hubs,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
                "organization_id": organization_id,
                "name": name,
            },
        )

    def create_hub(
        self,
        *,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        product_plan: HubProductPlan = HubProductPlan.PLAN_UNKNOWN,
        disable_events: Optional[bool] = None,
        events_topic_prefix: Optional[str] = None,
        twins_graphite_config: Optional[HubTwinsGraphiteConfig] = None,
    ) -> Hub:
        """
        Create a hub
        :param region: Region to target. If none is passed will use default region from the config
        :param name: Hub name (up to 255 characters)
        :param project_id: Organization/project owning the resource
        :param product_plan: Hub feature set
        :param disable_events: Disable Hub events
        :param events_topic_prefix: Hub events topic prefix (default '$SCW/events')
        :param twins_graphite_config: BETA - not implemented yet.

        One-of ('twins_db_config'): at most one of 'twins_graphite_config' could be set.
        :return: :class:`Hub <Hub>`

        Usage:
        ::

            result = api.create_hub()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/hubs",
            body=marshal_CreateHubRequest(
                CreateHubRequest(
                    region=region,
                    name=name or random_name(prefix="hub"),
                    project_id=project_id,
                    product_plan=product_plan,
                    disable_events=disable_events,
                    events_topic_prefix=events_topic_prefix,
                    twins_graphite_config=twins_graphite_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Hub(res.json())

    def get_hub(
        self,
        *,
        hub_id: str,
        region: Optional[Region] = None,
    ) -> Hub:
        """
        Get a hub
        :param region: Region to target. If none is passed will use default region from the config
        :param hub_id: Hub ID
        :return: :class:`Hub <Hub>`

        Usage:
        ::

            result = api.get_hub(hub_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hub_id = validate_path_param("hub_id", hub_id)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/hubs/{param_hub_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Hub(res.json())

    def wait_for_hub(
        self,
        *,
        hub_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Hub, bool]] = None,
    ) -> Hub:
        """
        Waits for :class:`Hub <Hub>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config
        :param hub_id: Hub ID
        :param options: The options for the waiter
        :return: :class:`Hub <Hub>`

        Usage:
        ::

            result = api.wait_for_hub(hub_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in HUB_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_hub,
            options=options,
            args={
                "hub_id": hub_id,
                "region": region,
            },
        )

    def update_hub(
        self,
        *,
        hub_id: str,
        product_plan: HubProductPlan,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        disable_events: Optional[bool] = None,
        events_topic_prefix: Optional[str] = None,
        enable_device_auto_provisioning: Optional[bool] = None,
        twins_graphite_config: Optional[HubTwinsGraphiteConfig] = None,
    ) -> Hub:
        """
        Update a hub
        :param region: Region to target. If none is passed will use default region from the config
        :param hub_id: Hub ID
        :param name: Hub name (up to 255 characters)
        :param product_plan: Hub feature set
        :param disable_events: Disable Hub events
        :param events_topic_prefix: Hub events topic prefix
        :param enable_device_auto_provisioning: Enable device auto provisioning
        :param twins_graphite_config: BETA - not implemented yet.

        One-of ('twins_db_config'): at most one of 'twins_graphite_config' could be set.
        :return: :class:`Hub <Hub>`

        Usage:
        ::

            result = api.update_hub(
                hub_id="example",
                product_plan=plan_unknown,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hub_id = validate_path_param("hub_id", hub_id)

        res = self._request(
            "PATCH",
            f"/iot/v1/regions/{param_region}/hubs/{param_hub_id}",
            body=marshal_UpdateHubRequest(
                UpdateHubRequest(
                    hub_id=hub_id,
                    product_plan=product_plan,
                    region=region,
                    name=name,
                    disable_events=disable_events,
                    events_topic_prefix=events_topic_prefix,
                    enable_device_auto_provisioning=enable_device_auto_provisioning,
                    twins_graphite_config=twins_graphite_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Hub(res.json())

    def enable_hub(
        self,
        *,
        hub_id: str,
        region: Optional[Region] = None,
    ) -> Hub:
        """
        Enable a hub
        :param region: Region to target. If none is passed will use default region from the config
        :param hub_id: Hub ID
        :return: :class:`Hub <Hub>`

        Usage:
        ::

            result = api.enable_hub(hub_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hub_id = validate_path_param("hub_id", hub_id)

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/hubs/{param_hub_id}/enable",
        )

        self._throw_on_error(res)
        return unmarshal_Hub(res.json())

    def disable_hub(
        self,
        *,
        hub_id: str,
        region: Optional[Region] = None,
    ) -> Hub:
        """
        Disable a hub
        :param region: Region to target. If none is passed will use default region from the config
        :param hub_id: Hub ID
        :return: :class:`Hub <Hub>`

        Usage:
        ::

            result = api.disable_hub(hub_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hub_id = validate_path_param("hub_id", hub_id)

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/hubs/{param_hub_id}/disable",
        )

        self._throw_on_error(res)
        return unmarshal_Hub(res.json())

    def delete_hub(
        self,
        *,
        hub_id: str,
        region: Optional[Region] = None,
        delete_devices: Optional[bool] = None,
    ) -> Optional[None]:
        """
        Delete a hub
        :param region: Region to target. If none is passed will use default region from the config
        :param hub_id: Hub ID
        :param delete_devices: Force deletion of devices added to this hub instead of rejecting operation

        Usage:
        ::

            result = api.delete_hub(hub_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hub_id = validate_path_param("hub_id", hub_id)

        res = self._request(
            "DELETE",
            f"/iot/v1/regions/{param_region}/hubs/{param_hub_id}",
            params={
                "delete_devices": delete_devices,
            },
        )

        self._throw_on_error(res)
        return None

    def get_hub_metrics(
        self,
        *,
        hub_id: str,
        start_date: datetime,
        region: Optional[Region] = None,
    ) -> GetHubMetricsResponse:
        """
        Get a hub's metrics
        :param region: Region to target. If none is passed will use default region from the config
        :param hub_id: Hub ID
        :param start_date: Start date used to compute the best scale for the returned metrics
        :return: :class:`GetHubMetricsResponse <GetHubMetricsResponse>`
        :deprecated

        Usage:
        ::

            result = api.get_hub_metrics(
                hub_id="example",
                start_date=datetime(...),
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hub_id = validate_path_param("hub_id", hub_id)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/hubs/{param_hub_id}/metrics",
            params={
                "start_date": start_date,
            },
        )

        self._throw_on_error(res)
        return unmarshal_GetHubMetricsResponse(res.json())

    def set_hub_ca(
        self,
        *,
        hub_id: str,
        ca_cert_pem: str,
        challenge_cert_pem: str,
        region: Optional[Region] = None,
    ) -> Hub:
        """
        Set the certificate authority of a hub
        :param region: Region to target. If none is passed will use default region from the config
        :param hub_id: Hub ID
        :param ca_cert_pem: The CA's PEM-encoded certificate
        :param challenge_cert_pem: The challenge is a PEM-encoded certificate to prove the possession of the CA. It must be signed by the CA, and have a Common Name equal to the Hub ID.
        :return: :class:`Hub <Hub>`

        Usage:
        ::

            result = api.set_hub_ca(
                hub_id="example",
                ca_cert_pem="example",
                challenge_cert_pem="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hub_id = validate_path_param("hub_id", hub_id)

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/hubs/{param_hub_id}/ca",
            body=marshal_SetHubCARequest(
                SetHubCARequest(
                    hub_id=hub_id,
                    ca_cert_pem=ca_cert_pem,
                    challenge_cert_pem=challenge_cert_pem,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Hub(res.json())

    def get_hub_ca(
        self,
        *,
        hub_id: str,
        region: Optional[Region] = None,
    ) -> GetHubCAResponse:
        """
        Get the certificate authority of a hub
        :param region: Region to target. If none is passed will use default region from the config
        :param hub_id:
        :return: :class:`GetHubCAResponse <GetHubCAResponse>`

        Usage:
        ::

            result = api.get_hub_ca(hub_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_hub_id = validate_path_param("hub_id", hub_id)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/hubs/{param_hub_id}/ca",
        )

        self._throw_on_error(res)
        return unmarshal_GetHubCAResponse(res.json())

    def list_devices(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListDevicesRequestOrderBy = ListDevicesRequestOrderBy.NAME_ASC,
        name: Optional[str] = None,
        hub_id: Optional[str] = None,
        allow_insecure: Optional[bool] = None,
        status: DeviceStatus = DeviceStatus.UNKNOWN,
    ) -> ListDevicesResponse:
        """
        List devices
        :param region: Region to target. If none is passed will use default region from the config
        :param page: Page number
        :param page_size: Page size. The maximum value is 100
        :param order_by: Ordering of requested devices
        :param name: Filter on the name
        :param hub_id: Filter on the hub
        :param allow_insecure: Filter on the allow_insecure flag
        :param status: Device status (enabled, disabled, etc.)
        :return: :class:`ListDevicesResponse <ListDevicesResponse>`

        Usage:
        ::

            result = api.list_devices()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/devices",
            params={
                "allow_insecure": allow_insecure,
                "hub_id": hub_id,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "status": status,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDevicesResponse(res.json())

    def list_devices_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDevicesRequestOrderBy] = None,
        name: Optional[str] = None,
        hub_id: Optional[str] = None,
        allow_insecure: Optional[bool] = None,
        status: Optional[DeviceStatus] = None,
    ) -> List[Device]:
        """
        List devices
        :param region: Region to target. If none is passed will use default region from the config
        :param page: Page number
        :param page_size: Page size. The maximum value is 100
        :param order_by: Ordering of requested devices
        :param name: Filter on the name
        :param hub_id: Filter on the hub
        :param allow_insecure: Filter on the allow_insecure flag
        :param status: Device status (enabled, disabled, etc.)
        :return: :class:`List[ListDevicesResponse] <List[ListDevicesResponse]>`

        Usage:
        ::

            result = api.list_devices_all()
        """

        return fetch_all_pages(
            type=ListDevicesResponse,
            key="devices",
            fetcher=self.list_devices,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "name": name,
                "hub_id": hub_id,
                "allow_insecure": allow_insecure,
                "status": status,
            },
        )

    def create_device(
        self,
        *,
        hub_id: str,
        allow_insecure: bool,
        allow_multiple_connections: bool,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        message_filters: Optional[DeviceMessageFilters] = None,
        description: Optional[str] = None,
    ) -> CreateDeviceResponse:
        """
        Add a device
        :param region: Region to target. If none is passed will use default region from the config
        :param name: Device name
        :param hub_id: ID of the device's hub
        :param allow_insecure: Allow plain and server-authenticated SSL connections in addition to mutually-authenticated ones
        :param allow_multiple_connections: Allow multiple physical devices to connect with this device's credentials
        :param message_filters: Filter-sets to authorize or deny the device to publish/subscribe to specific topics
        :param description: Device description
        :return: :class:`CreateDeviceResponse <CreateDeviceResponse>`

        Usage:
        ::

            result = api.create_device(
                hub_id="example",
                allow_insecure=True,
                allow_multiple_connections=True,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/devices",
            body=marshal_CreateDeviceRequest(
                CreateDeviceRequest(
                    hub_id=hub_id,
                    allow_insecure=allow_insecure,
                    allow_multiple_connections=allow_multiple_connections,
                    region=region,
                    name=name or random_name(prefix="device"),
                    message_filters=message_filters,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateDeviceResponse(res.json())

    def get_device(
        self,
        *,
        device_id: str,
        region: Optional[Region] = None,
    ) -> Device:
        """
        Get a device
        :param region: Region to target. If none is passed will use default region from the config
        :param device_id: Device ID
        :return: :class:`Device <Device>`

        Usage:
        ::

            result = api.get_device(device_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_device_id = validate_path_param("device_id", device_id)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/devices/{param_device_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Device(res.json())

    def update_device(
        self,
        *,
        device_id: str,
        region: Optional[Region] = None,
        description: Optional[str] = None,
        allow_insecure: Optional[bool] = None,
        allow_multiple_connections: Optional[bool] = None,
        message_filters: Optional[DeviceMessageFilters] = None,
        hub_id: Optional[str] = None,
    ) -> Device:
        """
        Update a device
        :param region: Region to target. If none is passed will use default region from the config
        :param device_id: Device ID
        :param description: Device description
        :param allow_insecure: Allow plain and server-authenticated SSL connections in addition to mutually-authenticated ones
        :param allow_multiple_connections: Allow multiple physical devices to connect with this device's credentials
        :param message_filters: Filter-sets to restrict the topics the device can publish/subscribe to
        :param hub_id: Change Hub for this device, additional fees may apply, see IoT Hub pricing
        :return: :class:`Device <Device>`

        Usage:
        ::

            result = api.update_device(device_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_device_id = validate_path_param("device_id", device_id)

        res = self._request(
            "PATCH",
            f"/iot/v1/regions/{param_region}/devices/{param_device_id}",
            body=marshal_UpdateDeviceRequest(
                UpdateDeviceRequest(
                    device_id=device_id,
                    region=region,
                    description=description,
                    allow_insecure=allow_insecure,
                    allow_multiple_connections=allow_multiple_connections,
                    message_filters=message_filters,
                    hub_id=hub_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Device(res.json())

    def enable_device(
        self,
        *,
        device_id: str,
        region: Optional[Region] = None,
    ) -> Device:
        """
        Enable a device
        :param region: Region to target. If none is passed will use default region from the config
        :param device_id: Device ID
        :return: :class:`Device <Device>`

        Usage:
        ::

            result = api.enable_device(device_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_device_id = validate_path_param("device_id", device_id)

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/devices/{param_device_id}/enable",
        )

        self._throw_on_error(res)
        return unmarshal_Device(res.json())

    def disable_device(
        self,
        *,
        device_id: str,
        region: Optional[Region] = None,
    ) -> Device:
        """
        Disable a device
        :param region: Region to target. If none is passed will use default region from the config
        :param device_id: Device ID
        :return: :class:`Device <Device>`

        Usage:
        ::

            result = api.disable_device(device_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_device_id = validate_path_param("device_id", device_id)

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/devices/{param_device_id}/disable",
        )

        self._throw_on_error(res)
        return unmarshal_Device(res.json())

    def renew_device_certificate(
        self,
        *,
        device_id: str,
        region: Optional[Region] = None,
    ) -> RenewDeviceCertificateResponse:
        """
        Renew a device certificate
        :param region: Region to target. If none is passed will use default region from the config
        :param device_id: Device ID
        :return: :class:`RenewDeviceCertificateResponse <RenewDeviceCertificateResponse>`

        Usage:
        ::

            result = api.renew_device_certificate(device_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_device_id = validate_path_param("device_id", device_id)

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/devices/{param_device_id}/renew-certificate",
        )

        self._throw_on_error(res)
        return unmarshal_RenewDeviceCertificateResponse(res.json())

    def set_device_certificate(
        self,
        *,
        device_id: str,
        certificate_pem: str,
        region: Optional[Region] = None,
    ) -> SetDeviceCertificateResponse:
        """
        Set a custom certificate on a device
        :param region: Region to target. If none is passed will use default region from the config
        :param device_id: Device ID
        :param certificate_pem: The PEM-encoded custom certificate
        :return: :class:`SetDeviceCertificateResponse <SetDeviceCertificateResponse>`

        Usage:
        ::

            result = api.set_device_certificate(
                device_id="example",
                certificate_pem="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_device_id = validate_path_param("device_id", device_id)

        res = self._request(
            "PUT",
            f"/iot/v1/regions/{param_region}/devices/{param_device_id}/certificate",
            body=marshal_SetDeviceCertificateRequest(
                SetDeviceCertificateRequest(
                    device_id=device_id,
                    certificate_pem=certificate_pem,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetDeviceCertificateResponse(res.json())

    def get_device_certificate(
        self,
        *,
        device_id: str,
        region: Optional[Region] = None,
    ) -> GetDeviceCertificateResponse:
        """
        Get a device's certificate
        :param region: Region to target. If none is passed will use default region from the config
        :param device_id: Device ID
        :return: :class:`GetDeviceCertificateResponse <GetDeviceCertificateResponse>`

        Usage:
        ::

            result = api.get_device_certificate(device_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_device_id = validate_path_param("device_id", device_id)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/devices/{param_device_id}/certificate",
        )

        self._throw_on_error(res)
        return unmarshal_GetDeviceCertificateResponse(res.json())

    def delete_device(
        self,
        *,
        device_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Remove a device
        :param region: Region to target. If none is passed will use default region from the config
        :param device_id: Device ID

        Usage:
        ::

            result = api.delete_device(device_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_device_id = validate_path_param("device_id", device_id)

        res = self._request(
            "DELETE",
            f"/iot/v1/regions/{param_region}/devices/{param_device_id}",
        )

        self._throw_on_error(res)
        return None

    def get_device_metrics(
        self,
        *,
        device_id: str,
        start_date: datetime,
        region: Optional[Region] = None,
    ) -> GetDeviceMetricsResponse:
        """
        Get a device's metrics
        :param region: Region to target. If none is passed will use default region from the config
        :param device_id: Device ID
        :param start_date: Start date used to compute the best scale for the returned metrics
        :return: :class:`GetDeviceMetricsResponse <GetDeviceMetricsResponse>`
        :deprecated

        Usage:
        ::

            result = api.get_device_metrics(
                device_id="example",
                start_date=datetime(...),
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_device_id = validate_path_param("device_id", device_id)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/devices/{param_device_id}/metrics",
            params={
                "start_date": start_date,
            },
        )

        self._throw_on_error(res)
        return unmarshal_GetDeviceMetricsResponse(res.json())

    def list_routes(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListRoutesRequestOrderBy = ListRoutesRequestOrderBy.NAME_ASC,
        hub_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ListRoutesResponse:
        """
        List routes
        :param region: Region to target. If none is passed will use default region from the config
        :param page: Page number
        :param page_size: Page size. The maximum value is 100
        :param order_by: Ordering of requested routes
        :param hub_id: Filter on the hub
        :param name: Filter on route's name
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
            f"/iot/v1/regions/{param_region}/routes",
            params={
                "hub_id": hub_id,
                "name": name,
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
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListRoutesRequestOrderBy] = None,
        hub_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> List[RouteSummary]:
        """
        List routes
        :param region: Region to target. If none is passed will use default region from the config
        :param page: Page number
        :param page_size: Page size. The maximum value is 100
        :param order_by: Ordering of requested routes
        :param hub_id: Filter on the hub
        :param name: Filter on route's name
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
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "hub_id": hub_id,
                "name": name,
            },
        )

    def create_route(
        self,
        *,
        hub_id: str,
        topic: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        s3_config: Optional[CreateRouteRequestS3Config] = None,
        db_config: Optional[CreateRouteRequestDatabaseConfig] = None,
        rest_config: Optional[CreateRouteRequestRestConfig] = None,
    ) -> Route:
        """
        Multiple route kinds can be created:
        - Database Route.
          Create a route that will record subscribed MQTT messages into your database.
          <b>You need to manage the database by yourself</b>.
        - REST Route.
          Create a route that will call a REST API on received subscribed MQTT messages.
        - S3 Routes.
          Create a route that will put subscribed MQTT messages into an S3 bucket.
          You need to create the bucket yourself and grant us write access.
          The grant can be done with s3cmd (`s3cmd setacl s3://<my-bucket> --acl-grant=write:555c69c3-87d0-4bf8-80f1-99a2f757d031:555c69c3-87d0-4bf8-80f1-99a2f757d031`).

        :param region: Region to target. If none is passed will use default region from the config
        :param name: Route name
        :param hub_id: ID of the route's hub
        :param topic: Topic the route subscribes to. It must be a valid MQTT topic and up to 65535 characters
        :param s3_config: If creating S3 Route, S3-specific configuration fields.

        One-of ('config'): at most one of 's3_config', 'db_config', 'rest_config' could be set.
        :param db_config: If creating Database Route, DB-specific configuration fields.

        One-of ('config'): at most one of 's3_config', 'db_config', 'rest_config' could be set.
        :param rest_config: If creating Rest Route, Rest-specific configuration fields.

        One-of ('config'): at most one of 's3_config', 'db_config', 'rest_config' could be set.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = api.create_route(
                hub_id="example",
                topic="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/routes",
            body=marshal_CreateRouteRequest(
                CreateRouteRequest(
                    hub_id=hub_id,
                    topic=topic,
                    region=region,
                    name=name or random_name(prefix="route"),
                    s3_config=s3_config,
                    db_config=db_config,
                    rest_config=rest_config,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Route(res.json())

    def update_route(
        self,
        *,
        route_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        topic: Optional[str] = None,
        s3_config: Optional[UpdateRouteRequestS3Config] = None,
        db_config: Optional[UpdateRouteRequestDatabaseConfig] = None,
        rest_config: Optional[UpdateRouteRequestRestConfig] = None,
    ) -> Route:
        """
        Update a route
        :param region: Region to target. If none is passed will use default region from the config
        :param route_id: Route id
        :param name: Route name
        :param topic: Topic the route subscribes to. It must be a valid MQTT topic and up to 65535 characters
        :param s3_config: When updating S3 Route, S3-specific configuration fields.

        One-of ('config'): at most one of 's3_config', 'db_config', 'rest_config' could be set.
        :param db_config: When updating Database Route, DB-specific configuration fields.

        One-of ('config'): at most one of 's3_config', 'db_config', 'rest_config' could be set.
        :param rest_config: When updating Rest Route, Rest-specific configuration fields.

        One-of ('config'): at most one of 's3_config', 'db_config', 'rest_config' could be set.
        :return: :class:`Route <Route>`

        Usage:
        ::

            result = api.update_route(route_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_route_id = validate_path_param("route_id", route_id)

        res = self._request(
            "PATCH",
            f"/iot/v1/regions/{param_region}/routes/{param_route_id}",
            body=marshal_UpdateRouteRequest(
                UpdateRouteRequest(
                    route_id=route_id,
                    region=region,
                    name=name,
                    topic=topic,
                    s3_config=s3_config,
                    db_config=db_config,
                    rest_config=rest_config,
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
        Get a route
        :param region: Region to target. If none is passed will use default region from the config
        :param route_id: Route ID
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
            f"/iot/v1/regions/{param_region}/routes/{param_route_id}",
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
        Delete a route
        :param region: Region to target. If none is passed will use default region from the config
        :param route_id: Route ID

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
            f"/iot/v1/regions/{param_region}/routes/{param_route_id}",
        )

        self._throw_on_error(res)
        return None

    def list_networks(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListNetworksRequestOrderBy = ListNetworksRequestOrderBy.NAME_ASC,
        name: Optional[str] = None,
        hub_id: Optional[str] = None,
        topic_prefix: Optional[str] = None,
    ) -> ListNetworksResponse:
        """
        List the Networks
        :param region: Region to target. If none is passed will use default region from the config
        :param page: Page number
        :param page_size: Page size. The maximum value is 100
        :param order_by: Ordering of requested routes
        :param name: Filter on Network name
        :param hub_id: Filter on the hub
        :param topic_prefix: Filter on the topic prefix
        :return: :class:`ListNetworksResponse <ListNetworksResponse>`

        Usage:
        ::

            result = api.list_networks()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/networks",
            params={
                "hub_id": hub_id,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "topic_prefix": topic_prefix,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListNetworksResponse(res.json())

    def list_networks_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNetworksRequestOrderBy] = None,
        name: Optional[str] = None,
        hub_id: Optional[str] = None,
        topic_prefix: Optional[str] = None,
    ) -> List[Network]:
        """
        List the Networks
        :param region: Region to target. If none is passed will use default region from the config
        :param page: Page number
        :param page_size: Page size. The maximum value is 100
        :param order_by: Ordering of requested routes
        :param name: Filter on Network name
        :param hub_id: Filter on the hub
        :param topic_prefix: Filter on the topic prefix
        :return: :class:`List[ListNetworksResponse] <List[ListNetworksResponse]>`

        Usage:
        ::

            result = api.list_networks_all()
        """

        return fetch_all_pages(
            type=ListNetworksResponse,
            key="networks",
            fetcher=self.list_networks,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "name": name,
                "hub_id": hub_id,
                "topic_prefix": topic_prefix,
            },
        )

    def create_network(
        self,
        *,
        hub_id: str,
        topic_prefix: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        type_: NetworkNetworkType = NetworkNetworkType.UNKNOWN,
    ) -> CreateNetworkResponse:
        """
        Create a new Network
        :param region: Region to target. If none is passed will use default region from the config
        :param name: Network name
        :param type_: Type of network to connect with
        :param hub_id: Hub ID to connect the Network to
        :param topic_prefix: Topic prefix for the Network
        :return: :class:`CreateNetworkResponse <CreateNetworkResponse>`

        Usage:
        ::

            result = api.create_network(
                hub_id="example",
                topic_prefix="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/iot/v1/regions/{param_region}/networks",
            body=marshal_CreateNetworkRequest(
                CreateNetworkRequest(
                    hub_id=hub_id,
                    topic_prefix=topic_prefix,
                    region=region,
                    name=name or random_name(prefix="network"),
                    type_=type_,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateNetworkResponse(res.json())

    def get_network(
        self,
        *,
        network_id: str,
        region: Optional[Region] = None,
    ) -> Network:
        """
        Retrieve a specific Network
        :param region: Region to target. If none is passed will use default region from the config
        :param network_id: Network ID
        :return: :class:`Network <Network>`

        Usage:
        ::

            result = api.get_network(network_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_network_id = validate_path_param("network_id", network_id)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/networks/{param_network_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Network(res.json())

    def delete_network(
        self,
        *,
        network_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a Network
        :param region: Region to target. If none is passed will use default region from the config
        :param network_id: Network ID

        Usage:
        ::

            result = api.delete_network(network_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_network_id = validate_path_param("network_id", network_id)

        res = self._request(
            "DELETE",
            f"/iot/v1/regions/{param_region}/networks/{param_network_id}",
        )

        self._throw_on_error(res)
        return None

    def get_twin_document(
        self,
        *,
        twin_id: str,
        document_name: str,
        region: Optional[Region] = None,
    ) -> TwinDocument:
        """
        BETA - Get a Cloud Twin Document
        :param region: Region to target. If none is passed will use default region from the config
        :param twin_id: Twin ID
        :param document_name: Document name
        :return: :class:`TwinDocument <TwinDocument>`

        Usage:
        ::

            result = api.get_twin_document(
                twin_id="example",
                document_name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_twin_id = validate_path_param("twin_id", twin_id)
        param_document_name = validate_path_param("document_name", document_name)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/twins/{param_twin_id}/documents/{param_document_name}",
        )

        self._throw_on_error(res)
        return unmarshal_TwinDocument(res.json())

    def put_twin_document(
        self,
        *,
        twin_id: str,
        document_name: str,
        region: Optional[Region] = None,
        version: Optional[int] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> TwinDocument:
        """
        BETA - Update a Cloud Twin Document
        :param region: Region to target. If none is passed will use default region from the config
        :param twin_id: Twin ID
        :param document_name: Document name
        :param version: If set, ensures that the document's current version matches before persisting the update.
        :param data: The new data that will replace the contents of the document.
        :return: :class:`TwinDocument <TwinDocument>`

        Usage:
        ::

            result = api.put_twin_document(
                twin_id="example",
                document_name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_twin_id = validate_path_param("twin_id", twin_id)
        param_document_name = validate_path_param("document_name", document_name)

        res = self._request(
            "PUT",
            f"/iot/v1/regions/{param_region}/twins/{param_twin_id}/documents/{param_document_name}",
            body=marshal_PutTwinDocumentRequest(
                PutTwinDocumentRequest(
                    twin_id=twin_id,
                    document_name=document_name,
                    region=region,
                    version=version,
                    data=data,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_TwinDocument(res.json())

    def patch_twin_document(
        self,
        *,
        twin_id: str,
        document_name: str,
        region: Optional[Region] = None,
        version: Optional[int] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> TwinDocument:
        """
        BETA - Patch a Cloud Twin Document
        :param region: Region to target. If none is passed will use default region from the config
        :param twin_id: Twin ID
        :param document_name: Document name
        :param version: If set, ensures that the document's current version matches before persisting the update.
        :param data: A json data that will be applied on the document's current data.
        Patching rules:
        * The patch goes recursively through the patch objects.
        * If the patch object property is null, then it is removed from the final object.
        * If the patch object property is a value (number, strings, bool, arrays), it is replaced.
        * If the patch object property is an object, the previous rules will be applied recursively on it.

        :return: :class:`TwinDocument <TwinDocument>`

        Usage:
        ::

            result = api.patch_twin_document(
                twin_id="example",
                document_name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_twin_id = validate_path_param("twin_id", twin_id)
        param_document_name = validate_path_param("document_name", document_name)

        res = self._request(
            "PATCH",
            f"/iot/v1/regions/{param_region}/twins/{param_twin_id}/documents/{param_document_name}",
            body=marshal_PatchTwinDocumentRequest(
                PatchTwinDocumentRequest(
                    twin_id=twin_id,
                    document_name=document_name,
                    region=region,
                    version=version,
                    data=data,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_TwinDocument(res.json())

    def delete_twin_document(
        self,
        *,
        twin_id: str,
        document_name: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        BETA - Delete a Cloud Twin Document
        :param region: Region to target. If none is passed will use default region from the config
        :param twin_id: Twin ID
        :param document_name: Document name

        Usage:
        ::

            result = api.delete_twin_document(
                twin_id="example",
                document_name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_twin_id = validate_path_param("twin_id", twin_id)
        param_document_name = validate_path_param("document_name", document_name)

        res = self._request(
            "DELETE",
            f"/iot/v1/regions/{param_region}/twins/{param_twin_id}/documents/{param_document_name}",
        )

        self._throw_on_error(res)
        return None

    def list_twin_documents(
        self,
        *,
        twin_id: str,
        region: Optional[Region] = None,
    ) -> ListTwinDocumentsResponse:
        """
        BETA - List the documents of a Cloud Twin
        :param region: Region to target. If none is passed will use default region from the config
        :param twin_id: Twin ID
        :return: :class:`ListTwinDocumentsResponse <ListTwinDocumentsResponse>`

        Usage:
        ::

            result = api.list_twin_documents(twin_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_twin_id = validate_path_param("twin_id", twin_id)

        res = self._request(
            "GET",
            f"/iot/v1/regions/{param_region}/twins/{param_twin_id}",
        )

        self._throw_on_error(res)
        return unmarshal_ListTwinDocumentsResponse(res.json())

    def delete_twin_documents(
        self,
        *,
        twin_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        BETA - Delete all the documents of a Cloud Twin
        :param region: Region to target. If none is passed will use default region from the config
        :param twin_id: Twin ID

        Usage:
        ::

            result = api.delete_twin_documents(twin_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_twin_id = validate_path_param("twin_id", twin_id)

        res = self._request(
            "DELETE",
            f"/iot/v1/regions/{param_region}/twins/{param_twin_id}",
        )

        self._throw_on_error(res)
        return None
