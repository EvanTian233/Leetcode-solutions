"""
1287. Element Appearing More Than 25% In Sorted Array
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
 

Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5

"""



class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        def bs(lst, tar, left):
            l, r = 0, len(lst)
            while l < r:
                m = l + (r-l) // 2
                if lst[m] < tar: l = m + 1
                elif not left and lst[m] == tar: l = m + 1 
                else: r = m
            return l if left else r
        
        st = len(arr) // 4
        if st == 0: return arr[0]
        for i in range(st, len(arr), st):
            if bs(arr, arr[i], False) - bs(arr, arr[i], True) > st: return arr[i]
        return arr[-1]


    def findSpecialInteger1(self, arr: List[int]) -> int:
        return collections.Counter(arr).most_common(1)[0][0]      