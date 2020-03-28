/*

226. Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class InvertTree {
    public TreeNode invertTree(TreeNode root) {
        // Recursive or DFS
        if (root == null) return null;

        TreeNode leftNode = invertTree(root.left);
        TreeNode rightNode = invertTree(root.right);
        root.left = rightNode;
        root.right = leftNode;
        return root;
        
       
    }

    public TreeNode invertTree2(TreeNode root) {
        // BFS
        if (root == null) {
            return null;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while(!queue.isEmpty()) {
            TreeNode node = queue.poll();
            TreeNode left = node.left;
            node.left = node.right;
            node.right = left;

            if(node.left != null) {
                queue.offer(node.left);
            }
            if(node.right != null) {
                queue.offer(node.right);
            }
        }
        return root;
    }
}