class Solution:
    """
        Runtime: 42ms | Beats: 80.13%

        Got help from Jadi :)
    """
    
    def romanToInt(self, s: str) -> int:
        conversion = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        result = 0
        counter = 0
        while (counter < len(s)):
            if s[counter:counter+2] in conversion:
                result += conversion[s[counter:counter+2]]
                counter += 2
            else:
                result += conversion[s[counter]]
                counter += 1

        return result


problem_link = "https://leetcode.com/problems/roman-to-integer/submissions/1389192837/?envType=study-plan-v2&envId=top-interview-150"
