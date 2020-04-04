/*
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array. 
Minimize the total number of operations.
*/

class MoveZeroes {
    public void moveZeroes(int[] nums) {
        if(nums == null || nums.length == 0) return;
        int zeroPointer = 0, numPointer = 0;
        while(numPointer < nums.length){
            while(zeroPointer<nums.length && nums[zeroPointer] != 0) zeroPointer++;
            while(numPointer<nums.length && (nums[numPointer]==0||numPointer<zeroPointer)) numPointer++;
            if (numPointer == nums.length) return;
            nums[zeroPointer] = nums[numPointer];
            nums[numPointer] = 0;            
        }
        
    }
}