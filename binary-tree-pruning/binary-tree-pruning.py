# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return 0
            return root.val + dfs(root.left)+dfs(root.right)
        
        if not root:
            return root
        self.pruneTree(root.left)
        self.pruneTree(root.right)
        
        if dfs(root.left)==0:
            root.left =None
        if dfs(root.right)==0:
            root.right = None
        if dfs(root)==0:
            root = None
        return root