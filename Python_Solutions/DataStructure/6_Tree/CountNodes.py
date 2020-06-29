"""
222. Count Complete Tree Nodes
https://leetcode.com/problems/count-complete-tree-nodes/

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        lh = 0
        node = root
        while(node != None):
            lh += 1
            node = node.left
        rh = 0
        node = root
        while(node != None):
            rh += 1
            node = node.right
        if lh == rh:
            return pow(2, lh) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)