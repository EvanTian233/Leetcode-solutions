"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""

class UniquePaths:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = [[1 for x in range(n)] for x in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                ans[i][j] = ans[i-1][j] + ans[i][j-1]
        return ans[-1][-1]
                