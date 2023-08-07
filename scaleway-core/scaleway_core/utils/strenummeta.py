from enum import EnumMeta


class StrEnumMeta(EnumMeta):
    def __call__(
        cls, value, names=None, *, module=None, qualname=None, type=None, start=1
    ):
        if names is not None:
            # the enum is being constructed via the functional syntax
            return super().__call__(
                value,
                names=names,
                module=module,
                qualname=qualname,
                type=type,
                start=start,
            )

        try:
            # attempt to get an enum member
            return super().__call__(
                value,
                names=names,
                module=module,
                qualname=qualname,
                type=type,
                start=start,
            )
        except ValueError:
            # no such member exists, but we don't care if the value is a string
            if not isinstance(value, str):
                raise ValueError(f"{value} is not a valid {cls.__name__} or string")

            return value
