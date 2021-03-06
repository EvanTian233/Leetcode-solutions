"""
221. Maximal Square
https://leetcode.com/problems/maximal-square/

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        r, c = len(matrix), len(matrix[0])
        dp = [[int(matrix[i][j]) for j in range(c)] for i in range(r)]
        res = max(max(dp))
        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = (min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1)*int(matrix[i][j])
                res = max(res, dp[i][j]**2)
        return res