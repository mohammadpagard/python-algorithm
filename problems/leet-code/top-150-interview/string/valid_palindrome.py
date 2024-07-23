class Solution:
    """
        Runtime: 39ms   |   Beasts 85.60%

        This is my note in LeetCode for this problem:
            - The time complexity of this is better than first one that I submitted,
            I solved this by using Python abilities and some cheating :) 
    """

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        phrase = ''.join(ch for ch in s if ch.isalnum())   # cleaning `s`

        # use `[::-1]` to reverse `phrase` and check first and last char
        if phrase == phrase[::-1]:
            return True
        else:
            return False


problem_link = 'https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150'
