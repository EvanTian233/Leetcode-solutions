"""
119. Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        res = [1]*(rowIndex+1)

        for i in range(2, rowIndex+1):
            for j in range(1, i):
                res[i-j] += res[i-j-1]
        
        return res
    
    