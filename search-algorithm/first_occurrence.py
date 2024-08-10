def first_occurrence(array: list[int], target: int) -> int:
    pointer = 0

    while pointer < len(array):
        if array[pointer] == target:
           return pointer
        pointer += 1

    return -1

def first_occurrence_logn(array: list[int], target: int) -> int:
    """Implement with better time complexity, O(log n)
    """
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (high + low) // 2

        if low == high:
            break
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid

    if array[low] == target:
        return low
    return -1

