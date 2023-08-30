from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Money:
    """
    Represents an amount of money with its currency type.
    """

    currency_code: str
    """
    3-letter currency code defined in ISO 4217.
    """

    units: float
    """
    Whole units of the amount.

    For example if `currency_code` is `"USD"`, then 1 unit is one US dollar.
    """

    nanos: int
    """
    Number of nano (10^-9) units of the amount.

    The value must be between -999,999,999 and +999,999,999 inclusive.
    If `units` is positive, `nanos` must be positive or zero.
    If `units` is zero, `nanos` can be positive, zero, or negative.
    If `units` is negative, `nanos` must be negative or zero.
    For example $-1.75 is represented as `units`=-1 and `nanos`=-750,000,000.
    """


def unmarshal_Money(data: Any) -> Money:
    """
    Unmarshal an instance of Money from the given data.
    """
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Money' failed as data isn't a dictionary."
        )

    return Money(
        currency_code=data["currency_code"],
        units=data["units"],
        nanos=data["nanos"],
    )


def marshal_Money(data: Money) -> Dict[str, Any]:
    """
    Marshal an instance of Money into a JSON compatible data structure.
    """
    return {
        "currency_code": data.currency_code,
        "units": data.units,
        "nanos": data.nanos,
    }
