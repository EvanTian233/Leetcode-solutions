"""
540. Single Element in a Sorted Array
https://leetcode.com/problems/single-element-in-a-sorted-array/

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10


"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
    # Linear
        i, res = 0, 0
        while i < len(nums):
            if i % 2 == 0:
                res += nums[i]
            elif i % 2 == 1:
                res -= nums[i]
            if res < 0:
                return nums[i-1]
            i += 1
        return res


    def singleNonDuplicate(self, nums: List[int]) -> int:
    # Binary search
	lo, hi = 0, len(nums) - 1
	while lo < hi:
		mid = 2 * ((lo + hi) // 4)
		if nums[mid] == nums[mid+1]:
			lo = mid+2
		else:
			hi = mid
	return nums[lo]