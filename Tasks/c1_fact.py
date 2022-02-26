import itertools
from typing import Iterator


def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError
    if n in (0, 1):
        return 1
    else:
        return n * factorial_recursive(n-1)


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError
    a = 1
    if n == a or n == 0:
        return a
    for i in range(2, n+1):
        a *= i
    return a


def factorial_generator(n: int) -> Iterator:
    if n < 0:
        raise ValueError
    fact = 1
    if n == 0:
        yield fact
    if n > 0:
        yield 1
        for i in range(1, n + 1):
            fact *= i
            yield fact


if __name__ == '__main__':
    factorial = factorial_generator(2)
    for _ in range(6):
        print(next(factorial))
