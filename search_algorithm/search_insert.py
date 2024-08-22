"""This algorithm find the index of key in array:
    If key exists in array, then return the index of key.
    If key does not exists in array, return the index of key if key does exists.
"""


def search_insert(array: list[int], key: int):
    """
        :param array: Array you want to find key in it.
        :param key: That key you want to know the index of it in array.
    """
    
    left = 0    # result of the function
    right = len(array) - 1
    mid = right // 2

    while left <= right:
        if key > array[mid]:
            mid += 1
            left = mid
        else:
            mid -= 1
            right = mid
    return left
