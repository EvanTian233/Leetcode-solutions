/*

90. Subsets II

https://leetcode.com/problems/subsets-ii/

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

*/

class SubsetsWithDup {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(ans, new ArrayList<>(), nums, 0);
        return ans;
    }
    
    private void backtrack(List<List<Integer>> ans, List<Integer> tempList, int[] nums, int start){
        ans.add(new ArrayList<>(tempList));
        for (int i = start; i< nums.length; i++){
            if (i > start && nums[i] == nums[i-1]) continue;
            tempList.add(nums[i]);
            backtrack(ans, tempList, nums, i+1);
            tempList.remove(tempList.size()-1);
        }
    }
}