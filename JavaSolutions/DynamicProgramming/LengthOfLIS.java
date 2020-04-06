/*
300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.


*/

class LengthOfLIS {
    public int lengthOfLIS(int[] nums) {
        int[][] memo = new int[nums.length+1][nums.length];
        for (int[] i: memo){
            Arrays.fill(i, -1);
        }
        return lengthOfLIS(nums, -1, 0, memo);
    }
    
    public int lengthOfLIS(int[] nums, int prev, int curpos, int[][] memo) {
        if (curpos == nums.length) {
            return 0;
        }
        if(memo[prev+1][curpos] >=0){
            return memo[prev+1][curpos];
        }
        int taken = 0;
        if (prev<0 || nums[curpos] > nums[prev]){
            taken = 1+lengthOfLIS(nums, curpos, curpos+1, memo);
        }
        
        int nottaken = lengthOfLIS(nums, prev, curpos +1, memo);
        memo[prev + 1][curpos] = Math.max(taken, nottaken);
        return Math.max(taken, nottaken);
    }
}