"""
1306. Jump Game III
https://leetcode.com/problems/jump-game-iii/

Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.


Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 

"""


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q, seen = collections.deque([start]), {start}
        while q:
            cur = q.popleft()
            if arr[cur] == 0:
                return True
            
            for child in cur - arr[cur], cur + arr[cur]:
                if 0 <= child < len(arr) and child not in seen:
                    seen.add(child)
                    q.append(child)
        return False

