"""
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/submissions/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"


"""

class LongestPalindrome:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # Odd case
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            
            # Even case
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
    
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer        
    def helper(self, s: str, l: int, r: int):
        while(l>=0 and r< len(s) and s[l]==s[r]):
            l-=1; r+=1
        return s[l+1:r]
        
        
        
        
        