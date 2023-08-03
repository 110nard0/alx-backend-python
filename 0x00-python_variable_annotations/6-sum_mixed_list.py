#!/usr/bin/env python3
"""Module 6-sum_mixed_list contains a function that takes
a list of integers and floats and returns their sum
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Accepts a list of integers and floats as a single parameter
    and returns the sum of its elements

    Args:
        mxd_list(list): List of integers and floats

    Returns:
        (float): sum of members of mxd_list
    """
    return sum(mxd_list)
