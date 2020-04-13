"""
34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]


Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

"""

class SearchRange:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Binary search + linear
        ans = [-1,-1] 
        
        if not nums:
            return ans
        start, end = 0, len(nums) - 1
        
        while start <= end:
         
            mid = (start + end)//2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return self.getTargetRange(nums, mid)
        return ans
        
        
    def getTargetRange(self, nums: List[int], mid: int) -> List[int]:
        i, j = mid-1, mid+1
        while i >= 0 and nums[i] == nums[mid]:
            i -= 1
        while j < len(nums) and nums[j] == nums[mid]:
            j += 1
            
        return [i+1, j-1]

