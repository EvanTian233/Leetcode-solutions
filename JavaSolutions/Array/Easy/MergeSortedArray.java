/* 

88. Merge Sorted Array

https://leetcode.com/problems/merge-sorted-array/

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

*/

class MeergeSortedArray {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int tail1 = m-1, tail2 = n-1, finished = m+n-1;
        while(tail1>=0 && tail2>= 0){
            nums1[finished--]=(nums1[tail1]>nums2[tail2])?
                nums1[tail1--]:nums2[tail2--];
        }
        //only need to combine with remaining nums2
        while(tail2>=0){
            nums1[finished--] = nums2[tail2--];
        }
    }
}