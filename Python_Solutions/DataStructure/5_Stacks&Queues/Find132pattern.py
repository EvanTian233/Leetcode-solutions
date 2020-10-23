"""
456. 132 Pattern
https://leetcode.com/problems/132-pattern/

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        if len(set(nums)) < 3:
            return False
        stack = [[nums[0], nums[0]]]
        current_min = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr >= stack[0][1]:  # curr >= max(nums[:i])
                stack = [[current_min, curr]]
            elif curr < current_min:  # curr < min(nums[:i])
                stack.append([curr, curr])
                current_min = curr
            elif curr == current_min:
                continue
            else:
                while stack and curr > stack[-1][0]:
                    if curr < stack[-1][1]:
                        return True
                    else:
                        stack.pop()
                stack.append([current_min, curr])
        return False