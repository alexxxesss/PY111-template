from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    left_limit = 0
    right_limit = len(arr) - 1

    while True:
        middle = len(arr) // 2
        if elem < arr[middle]:
            right_limit = middle
            arr = [left_limit, right_limit]
        elif elem > arr[middle]:
            left_limit = middle
            arr = [left_limit, right_limit]
        else:
            return middle

        return None
