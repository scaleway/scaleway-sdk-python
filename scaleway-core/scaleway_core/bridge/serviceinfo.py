from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class ServiceInfo:
    """
    Represents API metadata.

    These metadata are only here for debugging. Do not rely on these values.
    """

    name: str
    """
    Name of the API
    """

    description: str
    """
    Human readable description for the API.
    """

    version: str
    """
    Version of the API.
    """

    documentation_url: Optional[str] = None
    """
    Web url where the documentation of the API can be found.
    """


def unmarshal_ServiceInfo(data: Any) -> ServiceInfo:
    """
    Unmarshals a ServiceInfo object from a dict.
    """
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServiceInfo' failed as data isn't a dictionary."
        )

    return ServiceInfo(
        name=data["name"],
        description=data["description"],
        version=data["version"],
        documentation_url=data.get("documentation_url", None),
    )


def marshal_ServiceInfo(obj: ServiceInfo) -> Dict[str, Any]:
    """
    Marshals a ServiceInfo object into a dict.
    """
    return {
        "name": obj.name,
        "description": obj.description,
        "version": obj.version,
        "documentation_url": obj.documentation_url,
    }
