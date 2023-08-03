#!/usr/bin/env python3
"""Module 102-type_checking contains a type-annotated function
that takes a tuple as argument and returns a modified list
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Accepts a tuple parameter and an integer and returns
    each member of the tuple x number of times

    Args:
        lst (tuple): tuple of elements of any type
        factor (int): number of times tuple members are repeated

    Returns:
        zoomed_in (list): list of tuple elements in range of factor
    """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)
zoom_2x = zoom_array(array, 2)
zoom_3x = zoom_array(array, 3)

print(zoom_2x)
print(zoom_3x)
