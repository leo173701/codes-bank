# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    def pathSum(self, root, target):
                          # define global result and path
        self.result = 0
        distance = {0:1}          
        self.dfs(root, target, 0, distance)       # recursive to get result                      
        return self.result   # return result
    
    def dfs(self, root, target, currPathSum, distance): # 中 左 右 顺序进行遍历
                           
        if root is None:   # exit condition
            return  
                     # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
                     # update result and distance
        self.result += distance.get(oldPathSum, 0)
        distance[currPathSum] = distance.get(currPathSum, 0) + 1     #更新频率
        
                    # dfs breakdown
        self.dfs(root.left, target, currPathSum, distance)
        self.dfs(root.right, target, currPathSum, distance)
                     # when move to a different branch, 
                     #the currPathSum is no longer available, hence remove one. 
        distance[currPathSum] -= 1     