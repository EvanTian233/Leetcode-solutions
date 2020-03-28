/*
1. Two Sum

https://leetcode.com/problems/two-sum/

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

*/

import java.util.*;

class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        // Hash table
        int[] ans = new int[2];
        
        HashMap<Integer,Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++){
            map.put(target - nums[i],i);
            if (map.containsKey(nums[i+1]) && i+1 < nums.length){
                ans[0] = map.get(nums[i+1]);
                ans[1] = i+1;
                return ans;
            }
            
        }
        return ans;
        
        
    }

    public int[] twoSumV2(int[] nums, int target) {
        // More elegent version
        HashMap<Integer,Integer> mp = new HashMap<>();
        
        for (int i = 0; i<nums.length; i++){
            int complement = target-nums[i];

            if(mp.containsKey(complement)){
                return new int[] {mp.get(complement), i};
            }
            mp.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");        
        
    }
}
