/*

104. Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7


*/

class MaxDepth {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        
        int depth = 0;
        Queue<TreeNode> nodes = new LinkedList<>();
        nodes.add(root);
        while(!nodes.isEmpty()){
            int size = nodes.size();
            depth++;
            while( size-- > 0){
                TreeNode node = nodes.poll();
                if (node.left != null) nodes.add(node.left);
                if (node.right != null) nodes.add(node.right);
            }
        }
        return depth;
    }

    public int maxDepth2(TreeNode root) {
        if (root == null) return 0;
        int maxL = maxDepth(root.left);
        int maxR = maxDepth(root.right);
        if ( maxL > maxR) return maxL + 1; else return maxR + 1; 
    }
}


