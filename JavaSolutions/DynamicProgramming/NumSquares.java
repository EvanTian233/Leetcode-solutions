/*
279. Perfect Squares
https://leetcode.com/problems/perfect-squares/

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


*/


class MumSquares {
    public int numSquares(int n) {
        int[] dp = new int[n+1];
        Arrays.fill(dp,Integer.MAX_VALUE);
        dp[0] = 0;
        for(int i=0; i<=n; i++){
            for(int j=1; i+j*j <= n; j++){
                dp[i+j*j] = Math.min(dp[i+j*j], dp[i]+1);
            }
        }
        return dp[n];
    }
}





