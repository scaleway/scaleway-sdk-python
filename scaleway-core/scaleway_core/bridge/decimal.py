from decimal import Decimal
from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults


def unmarshal_Decimal(data: Any) -> Decimal:
    """
    Unmarshal an instance of Decimal from the given data.
    """
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Decimal' failed as data isn't a dictionary."
        )

    if "value" not in data:
        raise TypeError(
            "Unmarshalling the type 'Decimal' failed as data does not contain a 'value' key."
        )

    return Decimal(data["value"])


def marshal_Decimal(data: Decimal, _defaults: ProfileDefaults | None) -> Dict[str, Any]:
    """
    Marshal an instance of Decimal into google.protobuf.Decimal JSON representation.
    """
    return {
        "value": str(data),
    }
