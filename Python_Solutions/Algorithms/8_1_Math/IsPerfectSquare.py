"""
367. Valid Perfect Square
https://leetcode.com/problems/valid-perfect-square/

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false


"""



class Solution:
    def isPerfectSquare(self, num: int) -> bool:        
        for i in range(num):
            if i**2 == num:
                return True
            elif i**2 > num:
                return False
        return True