from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, Generic, List, Optional, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable
    from _typeshed import SupportsKeysAndGetItem

T = TypeVar("T")


@dataclass
class OneOfPossibility(Generic[T]):
    param: str
    value: Optional[T]
    default: Optional[T] = None
    marshal_func: Optional[Callable[[T, T], Dict[str, Any]]] = None


def resolve_one_of(
    possibilities: List[OneOfPossibility[Any]], is_required: bool = False
) -> SupportsKeysAndGetItem[str, Any]:
    """
    Resolves the ideal parameter and value amongst an optional list.
    Uses marshal_func if provided.
    """

    # Try to resolve using non-None value
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
                # When no actual value, call with None as value
                return {
                    possibility.param: possibility.marshal_func(
                        None, possibility.default
                    )
                }
            return {possibility.param: possibility.default}

    # If required but unresolved, raise an error
    if is_required:
        possibilities_keys = " or ".join(
            [possibility.param for possibility in possibilities]
        )
        raise ValueError(f"one of ${possibilities_keys} must be present")

    # Else, return empty dict
    return {}
