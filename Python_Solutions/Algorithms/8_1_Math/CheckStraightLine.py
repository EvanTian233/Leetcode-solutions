"""
1232. Check If It Is a Straight Line
https://leetcode.com/problems/check-if-it-is-a-straight-line/


You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.




"""


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        length = len(coordinates)
        if len(coordinates) == 2: return True
        vDiff = coordinates[1][1] - coordinates[0][1]
        hDiff = coordinates[1][0] - coordinates[0][0]
        for i in range(2, length):
            if (coordinates[i][1] - coordinates[i-1][1]) * hDiff != (coordinates[i][0] - coordinates[i-1][0]) * vDiff:
                return False
            
        return True