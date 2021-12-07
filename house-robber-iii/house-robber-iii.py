# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0,0
            robleft, notrobleft = helper(root.left)
            robright, notrobright = helper(root.right)
            robvalue = notrobleft+ notrobright +root.val
            notrobvalue = max(robleft, notrobleft)+max(robright, notrobright)
            return robvalue, notrobvalue
        robvalue, notrobvalue = helper(root)
        return max(robvalue, notrobvalue)