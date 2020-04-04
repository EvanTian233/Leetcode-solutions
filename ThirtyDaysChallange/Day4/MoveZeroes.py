"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""

class MoveZeroes:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        z_pointer = n_pointer = 0
        length = len(nums)
        while n_pointer < length:
            while(z_pointer < length and nums[z_pointer] != 0):
                z_pointer+=1
            while(n_pointer < length and (nums[n_pointer] == 0 or n_pointer<z_pointer)): 
                n_pointer+=1
            if n_pointer == length: return

            nums[z_pointer], nums[n_pointer] = nums[n_pointer], nums[z_pointer]
        return