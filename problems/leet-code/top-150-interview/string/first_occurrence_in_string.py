class Solution:
    """
        Runtime: 0ms | Beats: 100.00%
        Memory: 16.44MB | Beats: 80.92%
    """
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len, needle_len = len(haystack), len(needle)

        for i in range(haystack_len - needle_len + 1):  # loop and traverse on each haystack characters
            """
            check the character until the last character of haystack => haystack[i : i + needle]:
            e.g:
                - input: haystack = 'sadbutsad', needle = 'sad'
                - and for example `i` = 0
                - haystack[0 : 0 + 3] == sad  =>  sad
                -> So, when the `haystack[i : i + needle_len]` equals to needle value, return `i`
            """
            if haystack[i : i + needle_len] == needle:
                return i
        return -1


problem_link = 'https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=top-interview-150'
