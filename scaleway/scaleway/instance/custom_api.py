from dataclasses import dataclass
from typing import Dict, Any, Optional, BinaryIO

from scaleway_core.bridge import Zone
from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import validate_path_param
from v1.api import InstanceV1API

@dataclass
class GetServerUserDataRequest:
    zone: Optional[Zone]
    """
    Zone of the user data to get
    """

    server_id: str

    key: str
    """
    Key defines the user data key to get
    """


def marshal_GetServerUserDataRequest(request: GetServerUserDataRequest, defaults: ProfileDefaults) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_id is not None:
        output["server_id"] = request.server_id
    if request.key is not None:
        output["key"] = request.key
    if request.zone is not None:
        output["zone"] = request.zone

    return output


def get_server_user_data(self, server_id: str, key: str, zone: Optional[Zone] = None):
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
                zone= zone,
                server_id= server_id,
                key=key,
            ),
            self.client,
        ),
    )

    self._throw_on_error(res)
    return res.json()

@dataclass
class SetServerUserDataRequest:
    zone: Optional[Zone]
    """
    Zone of the user data to set
    """

    server_id: str

    key: str
    """
    Key defines the user data key to set
    """

    content: BinaryIO
    """
    Content defines the data to set
    """

def marshal_SetServerUserDataRequest(request: SetServerUserDataRequest, defaults: ProfileDefaults) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_id is not None:
        output["server_id"] = request.server_id
    if request.key is not None:
        output["key"] = request.key
    if request.zone is not None:
        output["zone"] = request.zone
    if request.content is not None:
        output["content"] = request.content

    return output

def set_server_user_data(self, server_id: str, key: str, content: BinaryIO, zone: Optional[Zone] = None):
    param_zone = validate_path_param("zone", zone or self.client.default_zone)
    param_server_id = validate_path_param("server_id", server_id)

    res = self._request(
        "PATCH",
        f"/instance/v1/zones/{param_zone}/servers/{param_server_id}/user_data/{key}",
        body=marshal_SetServerUserDataRequest(
            SetServerUserDataRequest(
                zone= zone,
                server_id= server_id,
                key=key,
                content=content,
            ),
            self.client,
        ),
    )

    self._throw_on_error(res)
    return res.json()



def test_method(self):
    print("hello")

InstanceV1API.test_method = test_method