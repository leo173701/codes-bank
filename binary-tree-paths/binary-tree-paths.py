# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        def dfs(root, path,res):
            if not root:
                return
            if not root.left and not root.right:
                res.append(path)
            if root.left:
                dfs(root.left,  path+"->"+str(root.left.val), res)
            if root.right:
                dfs(root.right, path+"->"+str(root.right.val), res)
        
        dfs(root, str(root.val), res)
        return res