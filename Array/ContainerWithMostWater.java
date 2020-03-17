/*

11. Container With Most Water

https://leetcode.com/problems/container-with-most-water/

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

*/



class MaxArea {
    public int maxArea(int[] height) {
        
        int left = 0, right = height.length-1;
        int maxarea = 0;
        
        while(left<right){
            maxarea = Math.max(maxarea, (right - left)*Math.min(height[left], height[right]));
            if (height[left] < height[right]) left++;
            else right--;
            
        }
        return maxarea;
    }
}

