#!/usr/bin/env python3
"""Module 101-safely_get_value contains a type-annotated function
that takes a dictionary, key index and user-defined generic type
"""

from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Accepts a dictionary and key and returns the associated value

    Arguments:
        dct (dict): user dictionary
        key (any): dictionary index with corresponding value pair
        default (T): optional generic type variable

    Returns:
        (any): value of dict[key] or default if not present
    """
    if key in dct:
        return dct[key]
    else:
        return default
