from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults

from .marshalling import marshal_ServerActionRequestVolumeBackupTemplate
from .types import ServerAction, ServerActionRequest


def custom_marshal_ServerActionRequest(
    request: ServerActionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {
        "action": ServerAction(request.action),
    }

    if request.name is not None:
        output["name"] = request.name

    if request.volumes is not None:
        output["volumes"] = {
            k: marshal_ServerActionRequestVolumeBackupTemplate(v, defaults)
            for k, v in request.volumes.items()
        }

    return output
