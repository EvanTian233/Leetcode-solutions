"""
849. Maximize Distance to Closest Person
https://leetcode.com/problems/maximize-distance-to-closest-person/

You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.

Example 1:

Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

"""


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i, j, zeros, res, n = 0, len(seats)-1, 0, 0, len(seats)
        while seats[j] == 0:
            zeros += 1
            res = max(res, zeros)
            j -= 1
        zeros = 0
        
        while seats[i] == 0:
            zeros += 1
            res = max(res, zeros)
            i += 1
        while i < j:
            if seats[i] == 1:
                zeros = 0
            else:
                zeros += 1
                res = max(res, (zeros + 1) // 2)
            i += 1
        return res
        

