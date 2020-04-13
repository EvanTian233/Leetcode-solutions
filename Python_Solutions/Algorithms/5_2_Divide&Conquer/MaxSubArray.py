"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


***** Kadane's algorithm
https://www.youtube.com/watch?v=86CQq3pKSUw

"""

class MaxSubArray:
    def maxSubArray(self, nums: List[int]) -> int:
        # Greedy
        if not nums:return None
        if len(nums)==1: return nums[0]
        max_sum =  max_num = nums[0]
        cur_sum = 0
        
        
        for i, num in enumerate(nums):
            if num > max_num:
                max_num = num
                
            cur_sum += num
            
            if(cur_sum > 0):
                if (cur_sum > max_sum):
                    max_sum = cur_sum
            else:
                cur_sum = 0
        
        if max_sum <= 0:
            return max_num
        else:
            return max_sum

    def maxSubArray2(self, nums: List[int]) -> int:
        # Divide and Conquer
        return self.max_Sub_Array(nums, 0, len(nums)-1)
    
    def max_Sub_Array(self, nums: List[int], l: int, r: int) -> int:
        if l == r: return nums[l]
        mid = l + (r - l) // 2
        left_sum = self.max_Sub_Array(nums, l, mid)
        right_sum = self.max_Sub_Array(nums, mid+1, r)
        cross_sum = self.max_Cross_Sub_Array(nums, l, r, mid)
        print(left_sum,right_sum,cross_sum)
        return max(left_sum, right_sum, cross_sum)
    
    def max_Cross_Sub_Array(self, nums: List[int], l: int, r: int, mid: int) -> int:
        
        left_sum = nums[mid]
        right_sum = nums[mid+1]

        cross_sum = 0
        for i in range(mid, l-1, -1):
            cross_sum += nums[i]
            left_sum = max(left_sum, cross_sum)
                
                
        cross_sum = 0
        for j in range(mid+1, r+1):

            cross_sum += nums[j]
            right_sum = max(right_sum, cross_sum)   
            
        return left_sum + right_sum
    
    def maxSubArray3(self, nums: List[int]) -> int:
        # Kadane Algorithm
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
    
    def maxSubArray4(self, nums: List[int]) -> int:
        # Dynamic Programming
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)