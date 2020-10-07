"""
1288. Remove Covered Intervals
https://leetcode.com/problems/remove-covered-intervals/

Given a list of intervals, remove all intervals that are covered by another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

"""

class Solution:
    def removeCoveredIntervals(self, A):
        res = right = 0
        A.sort(key=lambda a: (a[0], -a[1]))
        for i, j in A:
            res += j > right
            right = max(right, j)
        return res