/*

70. Climbing Stairs

https://leetcode.com/problems/climbing-stairs/

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

*/

class Solution {
    public int climbStairs(int i, int n, int[] memo){
        if(i > n){
            return 0;
        }
        if(i == n){
            return 1;
        }
        if (memo[i] > 0){
            return memo[i];
        }
        memo[i] = climbStairs(i + 1, n, memo) + climbStairs(i + 2, n, memo);
        return memo[i];
    }
    
    public int climbStairs(int n){
        int[] memo = new int[n+1];
        return climbStairs(0, n, memo);
    }

    public int climbStairs2(int n) {
        if (n == 0 || n == 1) return 1;
        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i<=n;i++){
            dp[i] = dp[i-1]+dp[i-2];
        }
        return dp[n];
    }
}

