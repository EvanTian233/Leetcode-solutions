/*

53. Maximum Subarray

https://leetcode.com/problems/maximum-subarray/

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

*/


class MaxSubArray {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0], curSum = 0;
        int maxNum = nums[0];
        
        for (int i = 0; i < nums.length; i++){
            if(nums[i]>maxNum){
                maxNum = nums[i];
            }
            
            curSum = nums[i] + curSum;
            if (curSum > 0){
                if (curSum > maxSum) maxSum = curSum;
            }
            else curSum = 0;
        }
        
        if (maxSum <= 0){
            return maxNum;
        }else{
            return maxSum;
        }
        
    }
}