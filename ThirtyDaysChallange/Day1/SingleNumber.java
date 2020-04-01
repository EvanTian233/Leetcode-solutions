class Solution {
    public int singleNumber(int[] nums) {
        // Hashe set
        Set<Integer> seen = new HashSet<Integer>(nums.length);
        for(int i: nums){
            if(!seen.add(i)){
                seen.remove(i);           
            }           
        }
        return seen.iterator().next();
    }

    public int singleNumber2(int[] nums) {
        // Bit XOR
        int ans = 0;
        for(int i: nums){
            ans ^= i;
        }
        return ans;
    }
}

  