from typing import Dict, Optional

from scaleway_core.bridge import Zone
from scaleway_core.utils import validate_path_param

from .api import InstanceV1API
from .marshalling import unmarshal_ServerActionResponse
from .marshalling_utils import custom_marshal_ServerActionRequest
from .types import (
    ServerAction,
    ServerActionRequest,
    ServerActionRequestVolumeBackupTemplate,
    ServerActionResponse,
)


class InstanceV1APIUtils(InstanceV1API):
    def server_action(
        self,
        *,
        server_id: str,
        action: ServerAction,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        volumes: Optional[Dict[str, ServerActionRequestVolumeBackupTemplate]] = None,
    ) -> ServerActionResponse:
        """
        Perform power related actions on a server. Be wary that when terminating a server, all the attached volumes (local *and* block storage) are deleted. So, if you want to keep your local volumes, you must use the `archive` action instead of `terminate`. And if you want to keep block-storage volumes, **you must** detach it beforehand you issue the `terminate` call.  For more information, read the [Volumes](#volumes-7e8a39) documentation.
        :param zone: Zone to target. If none is passed will use default zone from the config
        :param server_id: UUID of the server
        :param action: The action to perform on the server
        :param name: The name of the backup you want to create.
        This field should only be specified when performing a backup action.

        :param volumes: For each volume UUID, the snapshot parameters of the volume.
        This field should only be specified when performing a backup action.

        :return: :class:`ServerActionResponse <ServerActionResponse>`

        Usage:
        ::

            result = api.server_action(
                server_id="example",
                action=poweron,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/action",
            body=custom_marshal_ServerActionRequest(
                ServerActionRequest(
                    server_id=server_id,
                    action=action,
                    zone=zone,
                    name=name,
                    volumes=volumes,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ServerActionResponse(res.json())
