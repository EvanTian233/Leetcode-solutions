"""
1291. Sequential Digits
https://leetcode.com/problems/sequential-digits/

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.


Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
"""

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = []
        for x in range(1, 9):
            while x <= high:
                r = x%10
                
                if r == 0:
                    break
                
                if x >= low:
                    nums.append(x)
                    
                x = (x*10) + r + 1
                
        return sorted(nums)

