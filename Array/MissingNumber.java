/*

268. Missing Number

https://leetcode.com/problems/missing-number/

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

*/

class MissingNumber {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int sum = (0+n)*(n+1)/2;
        int arSum = 0;
        for(int i=0; i<n;i++){
            arSum += nums[i];
        }
        return sum-arSum;
    }
}