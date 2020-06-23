"""
137. Single Number II
https://leetcode.com/problems/single-number-ii/

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

"""


class Solution:
    def singleNumber(self, nums):
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            rem = count % 3
            if i == 31 and rem:
                res -= 1 << 31
            else:
                res |= rem * (1 << i)
        return res