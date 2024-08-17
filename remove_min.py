"""
    Remove min
    [4, 5, 2, 8, -2, 5, 1, 9] => -2

    Through the array and find a minimum index in the array
"""

def remove_min(array: list[int]) -> int:
    if len(array) == 0:
        return 0

    min_value = array[0]
    for value in array:
        if min_value > value:
            min_value = value

    return min_value
