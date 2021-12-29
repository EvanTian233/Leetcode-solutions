"""
410. Split Array Largest Sum
https://leetcode.com/problems/split-array-largest-sum/

Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

 

Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9
Example 3:

Input: nums = [1,4,4], m = 3
Output: 4

"""

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        sum_total = sum(nums)
        max_total = max(nums)
        
        return self.binary(nums, m, sum_total, max_total)
    
    def binary(self, nums, m, high, low):
        mid = 0
        
        while low <= high:
            mid = low + (high - low) // 2
            if self.valid(nums, m, mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
    
    def valid(self, nums, m, sub_array_sum):
        cur_sum = 0
        count = 1      
        for num in nums:
            cur_sum += num
            if cur_sum > sub_array_sum:
                cur_sum = num
                count += 1
            if count > m:
                return False
        return True
            