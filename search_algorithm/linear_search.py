def linear_search(array: list[int], target: int) -> str:
    for i in range(len(array)):
        if array[i] == target:
            return "The {} is in the {} index of the array.".format(target, i)

    return "Your target isn't in the array."
