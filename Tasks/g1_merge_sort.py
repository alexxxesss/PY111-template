from random import randint
from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    if len(container) > 1:
        middle = len(container) // 2
        left = container[:middle]
        right = container[middle:]
        sort(left)
        sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                container[k] = left[i]
                i += 1
            else:
                container[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            container[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            container[k] = right[j]
            j += 1
            k += 1

    return container


arr = [randint(-100, 100) for _ in range(100)]
sort(arr)
