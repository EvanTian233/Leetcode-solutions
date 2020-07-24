"""
260. Single Number III
https://leetcode.com/problems/single-number-iii/

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor, a, b = 0, 0, 0
        for num in nums:
            xor ^= num
        mask = 1
        while (xor & mask == 0):
            mask = mask << 1
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        return [a, b]
        