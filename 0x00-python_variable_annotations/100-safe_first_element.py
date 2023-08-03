#!/usr/bin/env python3
"""Module 100-safe_first_element contains an type-annotated function
that takes a list of unknown member types
"""

from typing import Any, Optional, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Accepts a list of members of vaariable types

    Argument:
        lst (list): list of elements

    Returns:
        (any): first element of list or None
    """
    if lst:
        return lst[0]
    else:
        return None
