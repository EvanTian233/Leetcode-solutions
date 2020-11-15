"""
938. Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/

Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

 
Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root : return 0
        
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)