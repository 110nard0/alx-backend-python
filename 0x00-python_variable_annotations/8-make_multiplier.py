#!/usr/bin/env python3
"""Module 8-make_multiplier contains a function that takes
 a float as argument and returns a callable function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Accepts a float parameter and returns a function
    that multiplies a float by the first argument

    Args:
        multiplier (float): product multiplier

    Return:
        (float): product of multiplier and multiplicand
    """
    return producer


def producer(multiplicand: float) -> float:
    """Accepts a float parameter and returns the product
    of the float by the first argument of parent function

    Args:
        multiplicand (float): product multiplicand

    Return:
        (float): product of multiplier and multiplicand
    """
    return multiplicand * multiplicand
