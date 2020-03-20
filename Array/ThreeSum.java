/*

15. 3Sum

https://leetcode.com/problems/3sum/

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

*/

 
class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();
        // Two loops
        for (int i=0; i<nums.length-2; i++)
        {
            if (nums[i] > 0) break;
        	if(i == 0 || (i>0 && nums[i]!= nums[i-1])) // Skip same result
        	{
                HashSet<Integer> firstLoop = new HashSet<Integer>(); 
                int lo = i+1, hi = nums.length-1, sum = 0-nums[i];
                while (lo<hi)
                {
                    firstLoop.add(sum);
                    if (firstLoop.contains(nums[lo]+nums[hi])) 
                    {
                    	ans.add(Arrays.asList(nums[i], nums[lo], nums[hi]));
                        while (lo < hi && nums[lo] == nums[lo+1]) lo++;   // skip same result
                        while (lo < hi && nums[hi] == nums[hi-1]) hi--;
                        lo++; hi--;
                    }else if (nums[lo] + nums[hi] < sum) lo++;
                    else hi--;

                }

        	}

        }
        return ans;
    }
}