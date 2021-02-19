"""
784. Letter Case Permutation
https://leetcode.com/problems/letter-case-permutation/

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

 

Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: S = "12345"
Output: ["12345"]
Example 4:

Input: S = "0"
Output: ["0"]

"""

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        li = []

        def make_list():
            for char in S:
                li.append(char)

        def backtrack(i):
            if i == len(li):
                res.append("".join(li))
                return
            if '0' <= li[i] <= '9':
                backtrack(i + 1)
            else:
                li[i] = li[i].lower()
                backtrack(i + 1)
                li[i] = li[i].upper()
                backtrack(i + 1)

        make_list()
        backtrack(0)
        return res