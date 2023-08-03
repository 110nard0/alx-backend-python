#!/usr/bin/env python3
"""Module 7-to_kv contains a function that takes
a string and an integer or float and returns a tuple
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Accepts a string and int/float as parameters
    and returns a tuple consisting of both members

    Args:
        k (str): string positional argument
        v (int | float): integer or float positional argument

    Returns:
        (tuple): contains string k and square of v
    """
    return (k, v ** 2)
