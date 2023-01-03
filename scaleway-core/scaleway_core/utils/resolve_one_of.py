from dataclasses import dataclass
from typing import Any, Dict, Generic, List, Optional, TypeVar

T = TypeVar("T")


@dataclass
class OneOfPossibility(Generic[T]):
    param: str

    value: Optional[T]

    default: Optional[T] = None


def resolve_one_of(
    possibilities: List[OneOfPossibility[Any]], is_required: bool = False
) -> Dict[str, Any]:
    """
    Resolves the ideal parameter and value amongst an optional list.
    """

    # Get the first non-empty parameter
    for possibility in possibilities:
        if possibility.value is not None:
            return {possibility.param: possibility.value}

    # Get the first non-empty default
    for possibility in possibilities:
        if possibility.default is not None:
            return {possibility.param: possibility.default}

    # If required, raise an error
    if is_required:
        possibilities_keys = " or ".join(
            [possibility.param for possibility in possibilities]
        )
        raise ValueError(f"one of ${possibilities_keys} must be present")

    # Else, return an empty dict
    return {}
