"""
436. Find Right Interval
https://leetcode.com/problems/find-right-interval/

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:

You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
 

Example 1:

Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.

"""


class Solution:
    def findRightInterval(self, intervals):
        ints = sorted([[j,k,i] for i,[j,k] in enumerate(intervals)])
        begs = [i for i,_,_ in ints]
        out = [-1]*len(begs)
        for i,j,k in ints:
            t = bisect.bisect_left(begs, j)
            if t < len(begs):
                out[k] = ints[t][2]
        
        return out