#!/usr/bin/env python3
"""Module 9-element conains a function
that duck types an iterable object
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Finds the length of each member of an iterable object
    and returns a tuple of the sequence and its length

    Argument:
        lst (iterable): An iterable object

    Returns:
        (list(tuple)): list of tuples containing a sequence and its length
    """
    return [(i, len(i)) for i in lst]
