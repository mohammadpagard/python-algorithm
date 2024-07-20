"""
    You can find the best profit in the list.
    This algorithm is easy, but pay attention to the formula.
"""


def max_profit(array: list[int]):
    """
    	curr_max: get the current maximum between `array indexes` and `0` and `curr_max`.
    	max_so_far: save the best one by getting the maximum of `max_so_far` and `curr_max`.
    """
    curr_max, max_so_far = 0, 0
    for i in range(1, len(array)):
        curr_max = max(0, curr_max + array[i] - array[i-1])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far

# example
print(max_profit([7, 1, 5, 3, 6, 4]))   # 5
print(max_profit([9, 7, 6, 4, 3, 1]))   # 0
