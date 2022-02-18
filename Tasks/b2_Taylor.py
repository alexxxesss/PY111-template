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
    print(x)
    return 0
