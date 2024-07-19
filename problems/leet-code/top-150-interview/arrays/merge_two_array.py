class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Through on arrays from the last item.

            Runtime: 34ms   |   Beats 88.54%
        """
        i = m - 1
        j = n - 1
        wp = m + n - 1  # write pointer, has length of two arrays length

        while wp >= 0:
            if j < 0 or (i >= 0 and nums1[i] > nums2[j]):
                # replace `nums[wp]` to `nums1[i]` and decreasing `i`
                nums1[wp] = nums1[i]
                i -= 1
            else:
                # replace `nums2[wp]` to `nums1[j]` and decreasing `j`
                nums1[wp] = nums2[j]
                j -= 1
            wp -= 1

problem_link = "https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150"
