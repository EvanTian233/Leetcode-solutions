"""
1649. Create Sorted Array through Instructions
https://leetcode.com/problems/create-sorted-array-through-instructions/

Given an integer array instructions, you are asked to create a sorted array from the elements in instructions. You start with an empty container nums. For each element from left to right in instructions, insert it into nums. The cost of each insertion is the minimum of the following:

The number of elements currently in nums that are strictly less than instructions[i].
The number of elements currently in nums that are strictly greater than instructions[i].
For example, if inserting element 3 into nums = [1,2,3,5], the cost of insertion is min(2, 1) (elements 1 and 2 are less than 3, element 5 is greater than 3) and nums will become [1,2,3,3,5].

Return the total cost to insert all elements from instructions into nums. Since the answer may be large, return it modulo 109 + 7

 

Example 1:

Input: instructions = [1,5,6,2]
Output: 1
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 5 with cost min(1, 0) = 0, now nums = [1,5].
Insert 6 with cost min(2, 0) = 0, now nums = [1,5,6].
Insert 2 with cost min(1, 2) = 1, now nums = [1,2,5,6].
The total cost is 0 + 0 + 0 + 1 = 1.

"""


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        m = max(instructions)
        c = [0] * (m + 1)

        def update(x):
            while (x <= m):
                c[x] += 1
                x += x & -x

        def get(x):
            res = 0
            while (x > 0):
                res += c[x]
                x -= x & -x
            return res

        res = 0
        for i, a in enumerate(instructions):
            res += min(get(a - 1), i - get(a))
            update(a)
        return res % (10**9 + 7)