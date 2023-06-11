from typing import Optional


class BinarySearch:
    """
    Binary search class for finding the index of an item in a sorted list.

    Examples:
        >>> BinarySearch([_ for _ in range(1, 10)]).binary_search(8)
        7
        >>> BinarySearch([_ for _ in range(1, 10)]).binary_search(10)
    """

    def __init__(self, _list: list):
        """
        Initialize the BinarySearch object.

        Args:
            _list (list): The sorted list to search.
        """
        self._list = _list

    def binary_search(self, item) -> Optional[int]:
        """
        Perform a binary search on the sorted list to find the index of the given item.

        Args:
            item: The item to search for.

        Returns:
            Optional[int]: The index of the item if found, or None if the item is not found.
        """
        low = 0
        high = len(self._list) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = self._list[mid]

            if guess == item:
                return mid

            if guess > item:
                high = mid - 1
            else:
                low = mid + 1

        return None
