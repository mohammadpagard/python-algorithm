def findMaxAverage(nums: list[int], numsSize: int, k: int) -> float:
    max_sum = window_sum = 0

    window_sum += sum(nums[0:k])    # sum of the first window -the first `k` elements-
    max_sum = window_sum    # set maximum sum to the first window's sum

    for i in range(k, numsSize):
        """ update the window sum by adding the next element
            and removing the first element of the previous window !
        """
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)  # get the maximum between `maximum sum` and `window sum`

    return max_sum/4    # return the maximum average by dividing the maximum sum by `k`

