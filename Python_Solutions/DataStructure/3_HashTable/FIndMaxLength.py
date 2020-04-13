"""
525. Contiguous Array
https://leetcode.com/problems/contiguous-array/

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

"""

class FindMaxLength:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        max_length = 0
        cur_sum = 0
        dic = {0:0}
        
        for i, elem in enumerate(nums,1):
            if elem == 0:
                cur_sum += 1
            else:
                cur_sum -= 1
                
            if cur_sum in dic:
                max_length = max(max_length, i - dic[cur_sum])
            else:
                dic[cur_sum] = i
                
        return max_length