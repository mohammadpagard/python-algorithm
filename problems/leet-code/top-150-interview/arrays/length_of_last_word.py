class Solution:
    """
        Runtime: 33ms | Beats: 70.41%
        Memory: 16.48MB |   Beats: 88.19%
    """

    def lengthOfLastWord(self, s: str) -> int:
        result = s.strip().split(' ')

        return len(result[-1])


obj = Solution()

problem_link = "https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150"
