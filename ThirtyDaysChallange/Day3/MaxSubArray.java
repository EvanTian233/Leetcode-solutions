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

    public int maxSubArray2(int[] nums) {
        // Divide and conquer
        return Subarray(nums, 0 ,nums.length -1 );
    }
    public int Subarray(int[] A,int left, int right){
        if(left == right){return A[left];}
        int mid = left + (right - left) / 2;
        int leftSum = Subarray(A,left,mid);// left part 
        int rightSum = Subarray(A,mid+1,right);//right part
        int crossSum = crossSubarray(A,left,right);// cross part
        if(leftSum >= rightSum && leftSum >= crossSum){// left part is max
            return leftSum;
        }
        if(rightSum >= leftSum && rightSum >= crossSum){// right part is max
            return rightSum;
        }
        return crossSum; // cross part is max
    }
    public int crossSubarray(int[] A,int left,int right){
        int leftSum = Integer.MIN_VALUE;
        int rightSum = Integer.MIN_VALUE;
        int sum = 0;
        int mid = left + (right - left) / 2;
        for(int i = mid; i >= left ; i--){
            sum = sum + A[i];
            if(leftSum < sum){
                leftSum = sum;
            }
        }
        sum = 0;
        for(int j = mid + 1; j <= right; j++){
            sum = sum + A[j];
            if(rightSum < sum){
                rightSum = sum;
            }
        }
        return leftSum + rightSum;
    }
}