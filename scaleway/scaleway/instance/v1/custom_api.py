import time
from typing import Optional, Dict, cast

from requests import Response

from scaleway.instance.v1 import GetServerResponse
from scaleway_core.bridge import Zone as ScwZone
from scaleway_core.utils import validate_path_param
from .api import InstanceV1API
from .custom_marshalling import marshal_GetServerUserDataRequest
from .custom_types import GetServerUserDataRequest, GetAllServerUserDataResponse

max_retry = 10
interval = 0.01


class InstanceUtilsV1API(InstanceV1API):
    """
    This API extends InstanceV1API by adding utility methods for managing Instance resources,
    such as getting and setting server user data, while inheriting all methods of InstanceV1API.
    """

    def get_server_user_data(
        self, server_id: str, key: str, zone: Optional[ScwZone] = None
    ) -> Response:
        """
        GetServerUserData gets the content of a user data on a server for the given key.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id:
        :param key:
        :return: A plain text response with data user information

        Usage:
        ::

            result = api.get_server_user_data(
                server_id="example",
                key="example",
            )
        """
        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/user_data/{key}",
            body=marshal_GetServerUserDataRequest(
                GetServerUserDataRequest(
                    zone=zone,
                    server_id=server_id,
                    key=key,
                ),
                self.client,
            ),
        )
        self._throw_on_error(res)
        return res

    def set_server_user_data(
        self, server_id: str, key: str, content: bytes, zone: Optional[ScwZone] = None
    ) -> Response:
        """
        Sets the content of a user data on a server for the given key.
        :param zone: Zone to target. If none is passed, it will use the default zone from the config.
        :param server_id: The ID of the server.
        :param key: The user data key.
        :param content: The content to set as user data in bytes.
        :return: A plain text response confirming the operation.
        """
        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        headers = {
            "Content-Type": "text/plain",
        }
        res = self._request(
            "PATCH",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/user_data/{key}",
            body=content,
            headers=headers,
        )

        self._throw_on_error(res)
        return res

    def get_all_server_user_data(
        self, server_id: str, zone: Optional[ScwZone] = None
    ) -> GetAllServerUserDataResponse:
        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        all_user_data_res = InstanceUtilsV1API.list_server_user_data(
            self, server_id=param_server_id, zone=param_zone
        )

        user_data: Dict[str, bytes] = {}
        for key in all_user_data_res.user_data:
            value = InstanceUtilsV1API.get_server_user_data(
                self, server_id=param_server_id, key=key
            )
            user_data[key] = cast(bytes, value.content)

        return GetAllServerUserDataResponse(user_data=user_data)

    def set_all_server_user_data(
        self,
        server_id: str,
        user_data: Dict[str, bytes],
        zone: Optional[ScwZone] = None,
    ) -> Optional[None]:
        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        all_user_data_res = InstanceUtilsV1API.list_server_user_data(
            self, server_id=param_server_id, zone=param_zone
        )
        for key in all_user_data_res.user_data:
            if user_data.get(key) is not None:
                continue
            InstanceUtilsV1API.delete_server_user_data(
                self, server_id=param_server_id, key=key
            )

        for key in user_data:
            InstanceUtilsV1API.set_server_user_data(
                self,
                server_id=param_server_id,
                zone=param_zone,
                key=key,
                content=user_data[key],
            )

        return None

    def wait_instance_server(self, server_id: str, zone: ScwZone) -> GetServerResponse:
        wait_interval = interval
        for i in range(1, max_retry):
            wait_interval *= i
            s = self.get_server(zone=zone, server_id=server_id)

            if s.server is not None and s.server.state in {"running", "stopped"}:
                return s

            time.sleep(wait_interval)

        raise TimeoutError(
            f"Server {server_id} in zone {zone} did not reach a stable state "
            f"after {max_retry} retries."
        )
