from enum import EnumMeta
from typing import Any, Optional


class StrEnumMeta(EnumMeta):
    def __call__(
        cls,
        value: str,
        names: Optional[Any] = None,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        if names is not None:
            return super().__call__(value, names, *args, **kwargs)

        try:
            # attempt to get an enum member
            return super().__call__(value, names, *args, **kwargs)
        except ValueError:
            # no such member exists, but we don't care if the value is a string
            if not isinstance(value, str):
                raise ValueError(f"{value} is not a valid {cls.__name__} or string")

        return value
