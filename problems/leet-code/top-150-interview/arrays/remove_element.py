class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
            Runtime: 27ms   |   Beats 97.63%
        """

        left = len(nums) - 1

        while left >= 0:
            if nums[left] == val:
                nums.pop(left)
            left -= 1

        return len(nums)

problem_link = "https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150"
