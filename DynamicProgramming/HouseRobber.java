/*

198. House Robber

https://leetcode.com/problems/house-robber/

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

*/

class Solution {
    // DP + memo
    public int rob(int[] nums) {
        int[] memo = new int[nums.length + 1];
        Arrays.fill(memo, -1);
        return rob(nums, nums.length-1, memo);
    }
    
    private int rob(int[]nums, int i, int[] memo){
        if (i < 0) return 0;
        if (memo[i] < 0){
            memo[i] = Math.max(rob(nums, i-2, memo)+nums[i], rob(nums, i-1, memo));
        }
        return memo[i];
    }
    
    
}




