# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        if not root:
            return 0
        left = self.pathSum(root.left, target)
        right = self.pathSum(root.right, target)
        middle = self.fromRootToAny(root, target)
        return left + right + middle
        
    def fromRootToAny(self, root, target):
        results = []
        path = []
        self.dfsHelper(root, target, results, path)
        return len(results)
    
    def dfsHelper(self, root, target, results, path):
        if root is None:
            return 
        path.append(root.val)
        if root.val == target:
            results.append(path[:])
        self.dfsHelper(root.left, target - root.val, results, path)
        self.dfsHelper(root.right, target - root.val, results, path)
        path.pop()