"""
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder_Traversal_Helper(root, res)
        return res
    
    def inorder_Traversal_Helper(self, root: TreeNode, res: List[int]):
        if root:
            self.inorder_Traversal_Helper(root.left, res)
            res.append(root.val)
            self.inorder_Traversal_Helper(root.right, res)

