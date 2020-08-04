"""
342. Power of Four
https://leetcode.com/problems/power-of-four/

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false

"""

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num != 0 and num &(num-1) == 0 and num & 1431655765== num

