/*

136. Single Number

https://leetcode.com/problems/single-number/

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

*/



class FindSingle {
    public int singleNumber(int[] nums) {
        Set<Integer> set = new HashSet<Integer>(nums.length);
        for (int i : nums){
            if(!set.add(i)){
                set.remove(i);
            }
            
        }
	    return set.iterator().next();        
    }

    public int singleNumber2(int[] nums) {
        // Bit Manipulation
        int ans =0;
        
        int len = nums.length;
        for(int i=0;i!=len;i++)
            ans ^= nums[i];
        
        return ans;
        
    }
}


