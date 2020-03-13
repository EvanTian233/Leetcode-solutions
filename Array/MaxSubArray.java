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