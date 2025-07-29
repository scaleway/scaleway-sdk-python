from __future__ import annotations
from collections.abc import Callable
from scaleway_core.profile.profile import ProfileDefaults
from dataclasses import dataclass
from typing import Any, Dict, Generic, List, Optional, TypeVar
from _typeshed import SupportsKeysAndGetItem

T = TypeVar("T")


@dataclass
class OneOfPossibility(Generic[T]):
    param: str
    value: Optional[T]
    default: Optional[T] = None
    marshal_func: Optional[Callable[[T, ProfileDefaults], Dict[str, Any]]] = None


def resolve_one_of(
        possibilities: List[OneOfPossibility[Any]], is_required: bool = False
) -> SupportsKeysAndGetItem[str, Any]:
    for possibility in possibilities:
        if possibility.value is not None:
            if possibility.marshal_func is not None:
                return {
                    possibility.param: possibility.marshal_func(
                        possibility.value, possibility.default
                    )
                }
            return {possibility.param: possibility.value}

    for possibility in possibilities:
        if possibility.default is not None:
            if possibility.marshal_func is not None:
                raise ValueError(
                    f"{possibility.param} is missing a required value for marshal_func"
                )
            return {possibility.param: possibility.default}

    if is_required:
        possibilities_keys = " or ".join(
            [possibility.param for possibility in possibilities]
        )
        raise ValueError(f"one of ${possibilities_keys} must be present")

    return {}
