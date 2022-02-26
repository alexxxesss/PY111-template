from typing import Iterator

def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """

    a = 0
    b = 1

    if n < 0:
        raise ValueError
    if n == a:
        return n
    if n == b:
        return n
    else:
        return fib_recursive(n-2) + fib_recursive(n-1)




def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError

    a, b = 0, 1

    for _ in range(0, n):
        a, b = b, a + b

    return a


def fib_generator(n: int) -> Iterator:

    if n < 0:
        raise ValueError

    a, b = 0, 1
    yield a
    yield b

    for _ in range(0, n):
        a, b = b, a + b
        yield a

