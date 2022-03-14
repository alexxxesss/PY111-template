from typing import List
from random import randint

from Tasks.utils import benchmark


@benchmark(10)
def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    n = len(container)

    for i in range(n-1):
        for j in range(0, n - i - 1):
            if container[j] > container[j + 1]:
                container[j], container[j + 1] = container[j + 1], container[j]
    return container


arr = [randint(-10000, 10000) for _ in range(10000)]
sort(arr)
