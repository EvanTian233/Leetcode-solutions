"""
941. Valid Mountain Array
https://leetcode.com/problems/valid-mountain-array/

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < A[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
"""

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
  
        if len(A)<3 or A[0]>=A[1]:
            return False
			
        uphill = True
        
        for i in range(1,len(A)):
            if uphill:
                if A[i-1]>=A[i]:
                    uphill = False
            if not uphill:
                if A[i-1]<=A[i]:
                    return False
        return not uphill