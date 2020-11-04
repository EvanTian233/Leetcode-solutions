"""
1446. Consecutive Characters
https://leetcode.com/problems/consecutive-characters/

Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

"""


class Solution:
    def maxPower(self, s: str) -> int:
        r = 0
        i = 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            if j - i > r:
                r = j - i
            i = j
        return r