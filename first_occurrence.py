def first_occurrence(array: list[int], target: int) -> int:
    pointer = 0

    while pointer < len(array):
        if array[pointer] == target:
           return pointer
        pointer += 1

    return -1

