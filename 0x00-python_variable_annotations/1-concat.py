#!/usr/bin/env python3
"""Module 1-concat contains a type-annotated function that takes
two strings as arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """Accepts two string parameters and returns a string

    Args:
        str1 (str): First string argument
        str2 (str): Second string argument

    Returns:
        (str): concatenated string of str1 and str2
    """
    return "{}{}".format(str1, str2)
