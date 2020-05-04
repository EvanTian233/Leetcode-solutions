"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        curAns, maxAns = 1, 1
        nums = list(set(nums))
        nums.sort()
        length = len(nums)
        for i in range(length-1):

            if nums[i+1]-nums[i] == 1:
                curAns += 1
            else:
                curAns = 1
                
            maxAns = max(curAns, maxAns)

        return maxAns