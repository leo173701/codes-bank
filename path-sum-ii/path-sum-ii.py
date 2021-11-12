# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        
        
        def dfs(root, res, path, targetSum):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                if root.val==targetSum:
                    res.append(path[:])
                path.pop()
                return 
            
            dfs(root.left, res, path, targetSum - root.val )
            
            dfs(root.right, res, path, targetSum-root.val)
            path.pop()
        
        
        dfs(root,res,[],targetSum)
        return res
            