def binary_search(array: list[int], target: int) -> str:
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (high + low) // 2

        if array[mid] == target:
            return "The {} is in the {} index of the array.".format(target, mid)
        elif target < array[mid]:
            high = mid - 1
        elif target > array[mid]:
            low = mid + 1

    return "Your target isn't in the array."

