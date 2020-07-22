

"""
103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        switch = True
        ans = []
        if root:
            while queue:
                level = []
                for i in range(len(queue)):
                    node = queue.popleft()
                    level.append(node.val)
                    self.appendNode(queue, node.left)
                    self.appendNode(queue, node.right)
                    
                if not switch:
                    level.reverse()
                    
                ans.append(level)
                switch = not switch
                
        return ans
        
        
    def appendNode(self, queue, node):
        if node:
            queue.append(node)
        


