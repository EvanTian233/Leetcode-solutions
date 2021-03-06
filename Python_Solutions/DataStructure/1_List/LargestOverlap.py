"""
835. Image Overlap
https://leetcode.com/problems/image-overlap/

Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
"""


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        d = collections.defaultdict(int)
        a = []
        b = []
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if (A[i][j] == 1):
                    a.append((i, j))
                if (B[i][j] == 1):
                    b.append((i, j))
                        
        ans = 0
        for t1 in a:
            for t2 in b:
                t3 = (t2[0]-t1[0], t2[1]-t1[1])
                d[t3] += 1
                ans = max(ans, d[t3])
                
        return ans
                    