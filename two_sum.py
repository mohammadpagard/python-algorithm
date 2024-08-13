def two_sum_sorted(array: list[int], target: int) -> str:
    """This algorithm give an integer array, and an integer target.
    So, return your target by additional of two indext of the array.

    :param array: give a sorted integer array
    """

    left = 0
    right = len(array) - 1

    while left < right:
        current = array[left] + array[right]
        if current == target:
            return "{} + {} = {}".format(array[left], array[right], target)
        elif current > target:
            right -= 1
        elif current < target:
            left += 1
    return "So, you couldn't fund your target in this list..."
