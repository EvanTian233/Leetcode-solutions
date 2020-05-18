"""
567. Permutation in String
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].


"""

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window + Dict
        ctr1 = defaultdict(int)
        ctr2 = defaultdict(int)
        
        for x in s1: ctr1[x] += 1
        for x in s2[:len(s1)]: ctr2[x] += 1
        
        i = 0; j = len(s1)

        while j < len(s2):
            if ctr2 == ctr1: return True
            cur = s2[i]
            ctr2[cur] -= 1
            if ctr2[cur] < 1: 
                ctr2.pop(cur)
            ctr2[s2[j]] = ctr2.get(s2[j], 0) + 1
            i += 1; j += 1
            
        return ctr2 == ctr1
        