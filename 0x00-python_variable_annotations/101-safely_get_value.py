#!/usr/bin/env python3

""" unctions for safely interacting with dictionaries.  """
from typing import Mapping, Any, Union, TypeVar

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """Safely retrieves a value from a dictionary by key, returning a default value if the key does not exist."""
    if key in dct:
        return dct[key]
    else:
        return default
