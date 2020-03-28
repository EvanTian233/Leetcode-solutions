/*

912. Sort an Array

https://leetcode.com/problems/sort-an-array/

Given an array of integers nums, sort the array in ascending order.


Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]




*/




class SortArray {
    public List<Integer> sortArray(int[] nums) {
        // Quick sort
        List<Integer> res = new ArrayList<>();
        if (nums == null || nums.length == 0) return res;
        quickSort(nums, 0, nums.length - 1);
        for (int i : nums) res.add(i);
        return res;
    }
    private void quickSort(int[] nums, int l, int r) {
        if (l >= r) return;
        int mid = partition(nums, l, r);
        quickSort(nums, l, mid);
        quickSort(nums, mid + 1, r);
    }
    private int partition(int[] nums, int l, int r) {
        int pivot = nums[l];
        while (l < r) {
            while (l < r && nums[r] >= pivot) r--;
            nums[l] = nums[r];
            while (l < r && nums[l] <= pivot) l++;
            nums[r] = nums[l];
        }
        nums[l] = pivot;
        return l;
    }
}