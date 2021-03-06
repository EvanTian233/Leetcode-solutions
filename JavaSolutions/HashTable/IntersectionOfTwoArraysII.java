/*

350. Intersection of Two Arrays II

https://leetcode.com/problems/intersection-of-two-arrays-ii/

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

*/


class Intersect {
    public int[] intersect(int[] nums1, int[] nums2) {
        // Initialize HashMap & Array List
        ArrayList<Integer> result = new ArrayList<Integer>();
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i< nums1.length; i++){
            if(!map.containsKey(nums1[i])){
                map.put(nums1[i], 1);
            }else{
                map.put(nums1[i], map.get(nums1[i])+1);
            }
        }
        
        for (int i = 0; i < nums2.length; i++){
            if(map.containsKey(nums2[i]) && map.get(nums2[i]) > 0){
                result.add(nums2[i]);
                map.put(nums2[i], map.get(nums2[i])-1);
            }
        }
            
        int[] r = new int[result.size()];
        for(int i = 0; i < result.size(); i++){
            r[i] = result.get(i);
        }
    
        return r;
    }
}