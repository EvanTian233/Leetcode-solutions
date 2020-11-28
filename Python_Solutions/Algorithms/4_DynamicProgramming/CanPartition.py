"""
416. Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        snu = sum(nums)
        if snu & 1: return False
        
        target = snu // 2
        dp = [False for i in range(target + 1)]
        dp[0] = True
        
        for num in nums:
            for j in range(target, -1, -1):
                if j >= num:
                    dp[j] = dp[j] or dp[j - num]
                else: break
        return dp[target]

