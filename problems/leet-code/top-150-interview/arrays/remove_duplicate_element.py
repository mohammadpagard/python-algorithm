# Remove duplicates from sorted array, easy level

class Solution:
    def removeDuplicates(self, nums: list[int]):
        """
            Runtime: 72ms   |   Beats 76.36%
            Memory: 17.80mb |   Beats 94.36%
        """
        
        i = 0

        for r in range(0, len(nums)-1):
            if nums[r] == nums[r+1]:
                continue
            else:
                i += 1
                nums[i] = nums[r + 1]

        return i + 1    

problem_link = "https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150"
