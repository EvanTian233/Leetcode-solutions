"""
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
  
        if len(inorder) == 0:
            return None

        if len(inorder) == 1:
            return TreeNode(preorder[0])
        
        rval = preorder[0]
        root = TreeNode(rval)
        
        inorder_rval_index = inorder.index(rval)
        left_inorder = inorder[:inorder_rval_index]
        right_inorder = inorder[inorder_rval_index+1:]
        left_preorder = preorder[1: len(left_inorder) + 1]
        right_preorder = preorder[1 + len(left_preorder):]
        
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root