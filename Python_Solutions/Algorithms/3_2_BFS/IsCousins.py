# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None:
            return None
        # create a queue to hold (node, parent, depth)
        q = collections.deque()
        q.append((root,0,0)) # root has no parent and depth 0
        # dictionary to hold (parent, depth) for each node
        # key->val
        # key:node.val, value:(parent, depth)
        p = {} 
        while q:
            if x in p and y in p:
                break
            node,parent,depth = q.popleft()
            if node.val == x or node.val ==y:
                p[node.val] = (parent, depth) # I only insert information about x and y
            if node.left:
                q.append((node.left, node, depth+1))
            if node.right:
                q.append((node.right, node, depth+1))
        #now x and y are in the dictionary p
        xp,xd = p[x]
        yp,yd = p[y]
        if xp != yp and xd == yd:
            return True
        else:
            return False
                         
        