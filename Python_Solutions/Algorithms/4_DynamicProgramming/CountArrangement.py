"""
526. Beautiful Arrangement
https://leetcode.com/problems/beautiful-arrangement/

Suppose you have n integers from 1 to n. We define a beautiful arrangement as an array that is constructed by these n numbers successfully if one of the following is true for the ith position (1 <= i <= n) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Given an integer n, return the number of the beautiful arrangements that you can construct.

 

Example 1:

Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1, 2]:
Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
The second beautiful arrangement is [2, 1]:
Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
"""

class Solution:
    def countArrangement(self, n: int) -> int:
        cache = {}
        
        def helper(X):
            if len(X) == 1:
                return 1
            
            if X in cache:
                return cache[X]
            
            total = 0
            for j in range(len(X)):
                if X[j] % len(X) == 0 or len(X) % X[j] == 0:
                    total += helper(X[:j] + X[j+1:])
            
            cache[X] = total
            return total
        
        return helper(tuple(range(1, n+1)))

        