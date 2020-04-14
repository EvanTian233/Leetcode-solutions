"""
Perform String Shifts

Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"


"""


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
    
        shift_pair = [0,0]
        res = ''
        for pair in shift:
            if pair[0] == 0:
                shift_pair[1] -= pair[1]
            else:
                shift_pair[1] += pair[1]
        rot = shift_pair[1]
        rot = - rot % len(s)     

        if rot == 0:
            return s
        else:
            # Right shift
            res = s[rot:]+s[:rot]
            return res
        
        
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        # Better syntax
        left = 0
        for d, a in shift:
            if d:
                left -= a
            else:
                left += a
        left %= len(s)
        return s[left:] + s[:left]