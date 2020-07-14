"""
1344. Angle Between Hands of a Clock
https://leetcode.com/problems/angle-between-hands-of-a-clock/

Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_min =  (minutes / 60) * 360
        hour = (hour + (minutes / 60)) % 12
        angle_hour = hour / 12 * 360
        
        angle_diff = abs(angle_hour - angle_min)
        return angle_diff if angle_diff < 180 else 360 - angle_diff 