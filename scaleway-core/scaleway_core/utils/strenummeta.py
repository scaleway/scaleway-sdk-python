from enum import EnumMeta
from typing import Any


class StrEnumMeta(EnumMeta):
    def __call__(cls, value: Any, *values: Any, **kwargs: Any) -> Any:
        names = kwargs.pop("names", None)

        if names is not None:
            return super().__call__(value, names, *values, **kwargs)

        try:
            return super().__call__(value, *values, **kwargs)
        except ValueError:
            if isinstance(value, str):
                return value
            raise
