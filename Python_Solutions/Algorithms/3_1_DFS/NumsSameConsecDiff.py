"""
967. Numbers With Same Consecutive Differences
https://leetcode.com/problems/numbers-with-same-consecutive-differences/

Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

 

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 
"""

class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return list(range(10))
            
        if K == 0:
            return [ int(''.join(str(_)*N)) for _ in range(1,10)]
        
        res = []
        
        def search(path):
            if len(path) == N:
                res.append( int(''.join(map(str, path))) )
                return
            
            next_num = path[-1] + K
            if next_num < 10:
                search(path+[next_num])
                
            next_num = path[-1] - K
            if next_num >= 0:
                search(path+[next_num])
                
        for i in range(1, 10):
            search([i])
            
        return res

