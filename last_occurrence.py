def last_occurrence(array: list[int], target: int) -> int:
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (high + low) // 2

        if (array[mid] == target and mid == len(array)-1) or\
           (array[mid] == target and array[mid+1] > target):
            return mid
        elif array[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

