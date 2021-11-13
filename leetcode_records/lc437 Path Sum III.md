\437. Path Sum III

参考 246 · 二叉树的路径和 II：    二叉树的路径问题

参考\560. Subarray Sum Equals K：  对前缀和进行频数 哈希表记录

![img](https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg)

![image](https://assets.leetcode.com/users/images/119b5a72-5244-4cd7-bb6e-60784d94c2a0_1596872120.09719.png)

1. 完全可以按照 前缀和的方式进行啊

2. 想到 twosum的做法，用哈希表 记录下 distance1[5] = 15, distance1[3] = 18, distance1[10] = 10 
   表示某一个结点 到出发点的距离，
   做DFS 中左右 遍历：

   用distance来统计频率    distance[15]=1： 从根节点出发，路程为15的点有1次

```python
Time O(n)  space O(n)
第一种复杂度高的原因是每个节点都要判断是否可以作为头节点，这样每个节点相当于都要再跑n次。
但是其实没有必要每次都查，这道题可以想像成two sum。
我们每次存当前到root的sum，这样每次到某个节点我们就只要看超过target的部分是不是已经在之前
存在过了（因为是root到当前节点的sum，所以必定是连续的）。
这个map我用m来表示，key是sum的值，value是个数，因为可能存在多个（假如有负数存在）。
two sum那道题其实也是类似的思想，只不过是有两个，所以不用map来存个数，直接用set来看存不存在
就可以了。

时间复杂度分析：每个节点只要走一次，但是要牺牲space来存之前的sum，所以space是n，time是n。
class Solution:
    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    def pathSum(self, root, target):                          
        self.result = 0                           # define global result and path
        distance = {0:1}                 # 用字典描述前缀和
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
```







1. 主函数采用Divide and Conquer, 即所有的解的集合是从左子树节点出发返回的解的集合 + 从右子树节点返回的解的集合 + 从根节点本身出发的集合。
2. 左右子树很简单，递归调用自个就行了
3. 从根节点出发的解的集合其实就是 lintcode376. Binary Tree Path Sum 这道题的解，稍作修改，把叶子节点的条件改成任意节点就行了



```python
# 思路清晰， 可以返回所有的路径
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        if not root:
            return 0
        left = self.pathSum(root.left, target)  
        right = self.pathSum(root.right, target)
        middle = self.fromRootToAny(root, target)  # 从根结点root 
        return left + right + middle
        
    def fromRootToAny(self, root, target):          #现在有返回值
        results = []
        path = []
        self.dfsHelper(root, target, results, path)
        #return len(results)   #返回path 的个数
    	return results        #返回所有的path
    def dfsHelper(self, root, target, results, path): #没有返回值的
        if root is None:      # 找到从 root 出发所有的 path
            return 
        path.append(root.val)
        if root.val == target:
            results.append(path[:])
        self.dfsHelper(root.left, target - root.val, results, path)
        self.dfsHelper(root.right, target - root.val, results, path)
        path.pop()
```







``` python
#思路2：  来自九章算法 令狐冲 思路可以，但是超时了。
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum2(self, root, target):
        # Write your code here
        result = []
        path = []
        if root is None:
            return result
        self.dfs(root, path, result, 0,  target)
        return result

    def dfs(self, root, path, result, level, target):
        if root is None:
            return
        path.append(root.val)
        tmp = target
        for i in range(level , -1, -1):
            tmp -= path[i]
            if tmp == 0:
                result.append(path[i:])        #挺野蛮的做法，
        self.dfs(root.left, path, result, level + 1, target)
        self.dfs(root.right, path, result, level + 1, target)

        path.pop()
```

