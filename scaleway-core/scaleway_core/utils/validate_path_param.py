from datetime import datetime
from typing import Optional, Union


def validate_path_param(name: str, value: Optional[Union[str, int, datetime]]) -> str:
    """
    Returns the parameter if it's valid as path parameter
    (string and not empty, or number), else throws an exception.
    """
    if type(value) is datetime:
        value = value.isoformat()

    if (value is None) or (isinstance(value, str) and not value):
        raise ValueError(f"Path parameter {name} is required")

    return str(value)
