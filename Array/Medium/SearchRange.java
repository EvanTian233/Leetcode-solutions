/*

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

*/

class SearchRange {
    public int[] searchRange(int[] nums, int target) {
        int lo = 0, hi = nums.length-1;
        int[] ans = {-1, -1};
        if (nums.length == 0) return ans;
        while(nums[lo] < nums[hi]) {
            int mid = (lo+hi)/2;
            if (nums[mid]<target) 
            {
            	lo = mid+1;
            }
            else if (nums[mid]>target)
            {
            	hi = mid-1;
            }
            else 
            {//find target, then need to find the start and end point
				if(nums[lo] == nums[mid]) {
					hi--;
				}
				else 
				{
					lo++;
				}
			}
        }
    	//check whether find the target number
    	if(nums[lo] == nums[hi] && nums[lo]== target) {
    		ans[0] = lo;
    		ans[1] = hi;
    	}
        return ans;
    }
}