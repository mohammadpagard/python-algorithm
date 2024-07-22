class Solution:
    """
        Runtime: 29ms   |   Beats 91.80%
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while j < len(t):
            # checking to match characters and move `i`
            if i < len(s) and s[i] == t[j]:
                i += 1
            j += 1  # move `j` otherwise

        return i == len(s)

problem_link = 'https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150'

