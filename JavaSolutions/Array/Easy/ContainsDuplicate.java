/*

217. Contains Duplicate

https://leetcode.com/problems/contains-duplicate/

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

*/


import java.util.*;
class ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i =1; i< nums.length; i++){
            if (nums[i] == nums[i-1]){
                return true;
            }
        }
    return false;
    }

    public boolean containsDuplicate2(int[] nums) {
        Set<Integer> set = new HashSet<>(nums.length);
        for (int x: nums) {
            if (set.contains(x)) return true;
            set.add(x);
        }
        return false;
    }
}