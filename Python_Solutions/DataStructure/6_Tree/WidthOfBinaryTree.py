"""
662. Maximum Width of Binary Tree
https://leetcode.com/problems/maximum-width-of-binary-tree/

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return []
        width, level = 0, [(root, 1)]
        
        while len(level):
            width = max(width, level[-1][-1] - level[0][1] + 1)
            next_level = []
            for item, num in level:
                if item.left:
                    next_level.append((item.left, num*2))
                if item.right:
                    next_level.append((item.right, num*2+1))
            level = next_level
        return width

