"""Module 5-sum_list contains a function that takes
a list of floats as argument and returns their sum
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Accepts a list of floats as a single parameter and
    returns the sum of its elements

    Args:
        input_list(list): List of floats

    Returns:
        (float): sum of members of floats
    """
    return sum(input_list)
