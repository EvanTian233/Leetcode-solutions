"""
99. Recover Binary Search Tree
https://leetcode.com/problems/recover-binary-search-tree/

You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?


Example 1:

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        swap = [None, None]
        self.prev = TreeNode(float('-inf'))
        def dfs(node):
            if node:
                dfs(node.left)
                if node.val < self.prev.val:
                    if not swap[0]: swap[0] = self.prev
                    swap[1] = node
                self.prev = node
                dfs(node.right)
        dfs(root)
        swap[0].val, swap[1].val = swap[1].val, swap[0].val