import time
from typing import Optional, Dict, cast

from requests import Response

from scaleway.instance.v1 import GetServerResponse
from scaleway_core.bridge import Zone as ScwZone
from scaleway_core.utils import validate_path_param
from .api import InstanceV1API
from .custom_marshalling import marshal_GetServerUserDataRequest
from .custom_types import GetServerUserDataRequest, GetAllServerUserDataResponse
from .types import (
    VolumeServerTemplate,
    BootType,
    CreateServerResponse,
)

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
    ) -> None:
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

        return

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

    def create_server(
        self,
        *,
        zone: Optional[ScwZone] = None,
        commercial_type: str,
        name: Optional[str] = None,
        dynamic_ip_required: Optional[bool] = None,
        routed_ip_enabled: Optional[bool] = None,
        image: Optional[str] = None,
        volumes: Optional[dict[str, VolumeServerTemplate]] = None,
        enable_ipv6: Optional[bool] = None,
        protected: bool = False,
        public_ip: Optional[str] = None,
        public_ips: Optional[list[str]] = None,
        boot_type: Optional[BootType] = None,
        organization: Optional[str] = None,
        project: Optional[str] = None,
        tags: Optional[list[str]] = None,
        security_group: Optional[str] = None,
        placement_group: Optional[str] = None,
        admin_password_encryption_ssh_key_id: Optional[str] = None,
    ) -> CreateServerResponse:
        """
        Create an Instance.
        Create a new Instance of the specified commercial type in the specified zone. Pay attention to the volumes parameter, which takes an object which can be used in different ways to achieve different behaviors.
        Get more information in the [Technical Information](#technical-information) section of the introduction.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param commercial_type: Define the Instance commercial type (i.e. GP1-S).
        :param name: Instance name.
        :param dynamic_ip_required: By default, `dynamic_ip_required` is true, a dynamic ip is attached to the instance (if no flexible ip is already attached).
        :param routed_ip_enabled: If true, configure the Instance so it uses the new routed IP mode.
        :param image: Instance image ID or label.
        :param volumes: Volumes attached to the server.
        :param enable_ipv6: True if IPv6 is enabled on the server (deprecated and always `False` when `routed_ip_enabled` is `True`).
        :param protected: True to activate server protection option.
        :param public_ip: ID of the reserved IP to attach to the Instance.
        :param public_ips: A list of reserved IP IDs to attach to the Instance.
        :param boot_type: Boot type to use.
        :param organization: Instance Organization ID.
        One-Of ('project_identifier'): at most one of 'project', 'organization' could be set.
        :param project: Instance Project ID.
        One-Of ('project_identifier'): at most one of 'project', 'organization' could be set.
        :param tags: Instance tags.
        :param security_group: Security group ID.
        :param placement_group: Placement group ID if Instance must be part of a placement group.
        :param admin_password_encryption_ssh_key_id: The public_key value of this key is used to encrypt the admin password.
        :return: :class:`CreateServerResponse <CreateServerResponse>`

        Usage:
        ::

            result = api.create_instance_server(
                commercial_type="example",
                protected=False,
            )
        """

        payload = {
            "zone": zone,
            "commercial_type": commercial_type,
            "name": name,
            "dynamic_ip_required": dynamic_ip_required,
            "routed_ip_enabled": routed_ip_enabled,
            "image": image,
            "volumes": volumes,
            "enable_ipv6": enable_ipv6,
            "protected": protected,
            "public_ip": public_ip,
            "public_ips": public_ips,
            "boot_type": boot_type,
            "organization": organization,
            "project": project,
            "tags": tags,
            "security_group": security_group,
            "placement_group": placement_group,
            "admin_password_encryption_ssh_key_id": admin_password_encryption_ssh_key_id,
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        return self._create_server(**clean_payload)  # type: ignore[arg-type]
