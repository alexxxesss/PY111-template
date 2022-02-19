"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """

    min_value = arr[0]
    for value in arr:
        if value < min_value:
            min_value = value

    return arr.index(min_value)
