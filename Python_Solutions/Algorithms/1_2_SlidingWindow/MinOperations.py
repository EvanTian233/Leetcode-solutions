"""
1658. Minimum Operations to Reduce X to Zero
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

"""


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
    
        # Sliding Window : find the longest window that val = sum(nums)-target, 
		# once it is longest, then `n-windowSize` element will be the minimum number
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        
        
        currSum =  left = right = maxWindowSize = 0
        
        while right < len(nums):
            currSum += nums[right]
            while left < right and currSum > target:
                currSum -= nums[left]
                left += 1
            if currSum == target:
                maxWindowSize = max(maxWindowSize, right-left+1)
            right += 1
        
        
        return -1 if maxWindowSize == 0 else len(nums)-maxWindowSize



    """
    # DP solution
    def minOperationsHelper(self, nums, x, left, right, count, memo):
        key = str(left) + '-' + str(right) + '-' + str(x)
        if key in memo:
            return memo[key]
        if x == 0:
            return count
        if x < 0 or left > right:
            return 1e6

        l = self.minOperationsHelper(nums, x - nums[left], left+1, right, count+1, memo)
        r = self.minOperationsHelper(nums, x - nums[right], left, right-1, count+1, memo)
        memo[key] = min(l, r)
        return memo[key]
    
    def minOperations(self, nums: List[int], x: int) -> int:
        
        memo = {}
        res = self.minOperationsHelper(nums, x, 0, len(nums)-1, 0, memo)
        
        return -1 if res >= 1e6 else res
    """