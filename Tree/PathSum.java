/*

437. Path Sum III

https://leetcode.com/problems/path-sum-iii/submissions/

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class PathSum {
    public int pathSum(TreeNode root, int sum) {
        // Double recursion
        
        // Edge case
        if (root == null) return 0;
        return pathSumFrom(root, sum) + pathSum(root.left, sum) + pathSum(root.right, sum);
    }
    
    private int pathSumFrom(TreeNode root, int sum) {
        int count = 0;
        if (root == null) return 0;
        if (root.val == sum) {
            count++;
        }
        count += pathSumFrom(root.left, sum-root.val);
        count += pathSumFrom(root.right, sum-root.val);
        return count;
    }
}