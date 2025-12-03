from enum import EnumMeta
from typing import Any


class StrEnumMeta(EnumMeta):
    def __call__(cls, value: str, *args: Any, **kwargs: Any) -> Any:
        names = kwargs.pop("names", None)

        if names is not None:
            return super().__call__(value, names, *args, **kwargs)

        try:
            return super().__call__(value, *args, **kwargs)
        except ValueError:
            if isinstance(value, str):
                return value
            raise
