/*

94. Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

*/



class InorderTraversal {

    public List<Integer> inorderTraversal(TreeNode root) {
        // DFS
        List<Integer> list = new ArrayList<>();
        helper(root, list);
        return list;
    }
    
    private void helper(TreeNode root, List<Integer> list){
        if (root != null){
            if (root.left != null){
                helper(root.left, list);
            }
            list.add(root.val);
            if (root.right != null){
                helper(root.right, list);
            }
        }
    }

    public List<Integer> inorderTraversal2(TreeNode root) {
        // Like a BFS
        List<Integer> list = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()){
            while (curr != null){
                stack.push(curr);
                curr = curr.left;                
            }
            curr = stack.pop();
            list.add(curr.val);
            curr = curr.right;
        }
        return list;
    }
}