"""
this file i`m learning about binary search
"""

from typing import Optional


def binary_search(_list: list, item: int) -> Optional[int]:
    """
        Perform a binary search on a sorted list to find the index of the given item.

        Args:
            _list (list): The sorted list to search.
            item (int): The item to search for.

        Returns:
            Optional[int]: The index of the item if found, or None if the item is not found.

        Examples:
           >>> binary_search([_ for _ in range(1, 10)], 8)
           7
           >>> binary_search([_ for _ in range(1, 10)], 10)

        this function is binary search
    """

    low = 0
    high = len(_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = _list[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
            continue

        else:
            low = mid + 1
            continue

    return None
