class Solution {
    public int singleNumber(int[] nums) {
        Set<Integer> seen = new HashSet<Integer>(nums.length);
        for(int i: nums){
            if(!seen.add(i)){
                seen.remove(i);           
            }           
        }
        return seen.iterator().next();
    }
}

  