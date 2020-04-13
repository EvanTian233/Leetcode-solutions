"""
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Recursion
        if root is None:
            return 0
        return 1 + self.max_depth_helper(root.left, root.right)
    
    def max_depth_helper(self, left_node: TreeNode, right_node: TreeNode) -> int:
        if left_node is None and right_node is None: return 0
        l = r = 0
        
        if left_node:
            l = self.max_depth_helper(left_node.left, left_node.right)
        if right_node:
            r = self.max_depth_helper(right_node.left, right_node.right)
            
        return 1 + max(l,r)
        
            
    def maxDepth(self, root: TreeNode) -> int:
        # use BFS with iterative 
        # BFS + deque
        if root is None:
            return 0
        queue = collections.deque([(root,1)])
        while queue:
            curr_node, val = queue.popleft()
            if curr_node.left:
                queue.append((curr_node.left, val+1))
            if curr_node.right:
                queue.append((curr_node.right, val+1))
        return val
            
        
        
        

