#!/usr/bin/env python3
"""Module 2-floor contains a type-annotated function that
takes a float as argument and returns the floor
"""


def floor(n: float) -> int:
    """Accepts a float parameter and returns its floor value

    Args:
        n (float): Float argument

    Returns:
        (int): floor of n
    """
    return int(n // 1)
