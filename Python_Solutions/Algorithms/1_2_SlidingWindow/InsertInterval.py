"""
57. Insert Interval
https://leetcode.com/problems/insert-interval/

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res, n = [], newInterval     
        for index, i in enumerate(intervals):
            if i[1] < n[0]:
                res.append(i)            
            elif n[1] < i[0]:
                res.append(n)
                return res+intervals[index:]
            else:
                n[0] = min(n[0], i[0])
                n[1] = max(n[1], i[1])     
        res.append(n)
        return res
            
            

