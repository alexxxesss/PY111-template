"""
Taylor series
"""
import math
import itertools
from typing import Union


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    exp = 1
    delta = 0.0001
    for n in itertools.count(1, 1):
        exp_n = (x ** n)/math.factorial(n)
        exp += exp_n
        if delta > exp_n:
            break
    return exp


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """

    sin_x = 0
    delta = 0.0001
    for n in itertools.count(0, 1):
        sin_x_n = (((-1) ** n) / math.factorial((2 * n) + 1)) * (x ** ((2 * n) + 1))
        sin_x += sin_x_n
        if abs(sin_x_n) < delta:
            break
    return sin_x
