nums = [1, 2, 3, 4]


def fill_prefix_sum(nums: list[int], numsSize: int) -> list[int]:
    prefix_sum = [0] * numsSize # initialize the prefix sum list with same size

    prefix_sum[0] = nums[0] # set the first element of prefix sum to the first element of nums

    for i in range(1, numsSize):    # compute the prefix sum for the rest of the elements
        prefix_sum[i] = prefix_sum[i-1] + nums[i]

    return prefix_sum


result = [i for i in fill_prefix_sum(nums, len(nums))]
print(*result)
