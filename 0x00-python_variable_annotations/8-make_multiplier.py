#!/usr/bin/env python3
"""Module 8-make_multiplier contains a function that takes
 a float as argument and returns a callable function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a multiplier function

    Args:
        multiplier (float): product multiplier

    Return:
        (function): function that returns the product of two floats
    """

    def multiplier_fxn(multiplicand: float) -> float:
        """Accepts a float parameter and returns
        the product of the first argument and another float

        Args:
            multiplicand (float): product multiplicand

        Return:
            (float): product of multiplier and multiplicand
        """
        return multiplier * multiplicand

    return multiplier_fxn
    # return lambda x: x * multiplier
