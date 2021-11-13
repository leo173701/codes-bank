/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int pathSum(TreeNode root, int sum) {
        if (root == null) {
            return 0;
        }

      //1.由于它可以不从根节点出发，因此我们可以这么写
        return paths(root, sum) 
                + pathSum(root.left, sum) 
                + pathSum(root.right, sum);
    }

    private int paths(TreeNode root, int sum) {

        if (root == null) {
            return 0;
        }

        int res = 0;
        if (root.val == sum) {
            res += 1;            
        }
        
      
      //2.通过这里保证连续性
        res += paths(root.left, sum - root.val);
        res += paths(root.right, sum - root.val);
        
        return res;
    }
}