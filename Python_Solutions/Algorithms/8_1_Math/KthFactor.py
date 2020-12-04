"""
1492. The kth Factor of n
https://leetcode.com/problems/the-kth-factor-of-n/

Given two positive integers n and k.

A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

 

Example 1:

Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
Example 2:

Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.
Example 3:

Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
Example 4:

Input: n = 1, k = 1
Output: 1
Explanation: Factors list is [1], the 1st factor is 1.

"""

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        f1, f2 = [], []
        for s in range(1, int(sqrt(n)) + 1 ):
            if n % s == 0:
                f1 += [s]
                f2 += [n//s]
                
        if f1[-1] == f2[-1]: f2.pop()
            
        factors = f1 + f2[::-1]
        
        return -1 if len(factors) < k else factors[k-1]

