from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class ScwFile:
    """
    Represents a Scaleway file.
    """

    name: str
    """
    Name of the file.
    """

    content_type: str
    """
    Content-type of the file.
    """

    content: str
    """
    Content of the file in base64.
    """


def unmarshal_ScwFile(data: Any) -> ScwFile:
    """
    Unmarshals a ScwFile object from a dict.
    """
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ScwFile' failed as data isn't a dictionary."
        )

    return ScwFile(
        name=data["name"],
        content_type=data["content_type"],
        content=data["content"],
    )


def marshal_ScwFile(obj: ScwFile) -> Dict[str, Any]:
    """
    Marshals a ScwFile object into a dict.
    """
    return {
        "name": obj.name,
        "content_type": obj.content_type,
        "content": obj.content,
    }
