class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
            first of all I sorted the list and then compare the first element
            with the last element together, then `answer` save the same characters.

            Runtime: 0ms | Beats: 100.00%
        """

        answer = ""
        sorted_strs = sorted(strs)  # sort the list by ascii
        first = sorted_strs[0]
        last = sorted_strs[-1]

        for char in range(0, len(first)):
            if first[char] != last[char]:
                break
            else:
                answer += first[char]
        return answer


problem_link = 'https://leetcode.com/problems/longest-common-prefix/submissions/1434530918/?envType=study-plan-v2&envId=top-interview-150'

