"""
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder3(self, root: TreeNode) -> List[List[int]]:
        # DFS
        res = []
        self.dfs(root, 0, res)
        return res
    
    def dfs(self, root, level, res):
        if not root:
            return
        if len(res) < level+1:
            res.append([])
        res[level].append(root.val)
        self.dfs(root.left, level+1, res)
        self.dfs(root.right, level+1, res)
        
    def levelOrder(self, root):
        # DFS + Stack
        if not root:
            return []
        res, stack = [], [(root, 0)]
        while stack:
            curr, level = stack.pop()
            if len(res) < level +1:
                res.append([])
            res[level].append(root.val)
            self.dfs(root.left, level+1, res)
            self.dfs(root.right, level+1, res)
        return res

    def levelOrder2(self, root):
        from collections import deque
        res, queue = [],deque([(root, 0)])
        while queue:
            curr, level = queue.popleft()
            if curr:
                if len(res) < level+1:
                    res.append([])
                res[level].append(curr.val)
                queue.append((curr.left, level+1))
                queue.append((curr.right, level+1))
        return res

