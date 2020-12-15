
"""
131. Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]

"""

class Solution:
    
    def dfs(self, s, path, res):
        if not s:
            res.append(path[:])
            return
        
        for i in range(1, len(s)+1):
            if s[:i] == s[i-1::-1]:
                path.append(s[:i])
                self.dfs(s[i:], path, res)
                path.pop()
          
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        self.dfs(s, [], res)
        return res

        

