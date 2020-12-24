"""
556. Next Greater Element III
https://leetcode.com/problems/next-greater-element-iii/

Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1

"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        s = list(map(int, str(n)))
        i = len(s)-1
        while i-1>=0 and s[i]<=s[i-1]:
            i -= 1
            
        if i==0:
            return -1
        
        j = i
        while j+1<len(s) and s[j+1]>s[i-1]:
            j += 1
        
        s[i-1], s[j] = s[j], s[i-1]
        s[i:] = reversed(s[i:])
        ret = int(''.join(map(str, s)))
        
        return ret if ret<=((1<<31)-1) else -1