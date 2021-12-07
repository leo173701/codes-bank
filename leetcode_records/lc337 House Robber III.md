# 337.House Robber III

![img](https://assets.leetcode.com/uploads/2021/03/10/rob2-tree.jpg)



## 思路

和 198.house-robber 类似，这道题也是相同的思路。 只不过数据结构从数组换成了树。

我们仍然是对每一项进行决策：**如果我抢的话，所得到的最大价值是多少。如果我不抢的话，所得到的最大价值是多少。**

- 遍历二叉树，都每一个节点我们都需要判断抢还是不抢。

  - 如果抢了的话， 那么我们不能继续抢其左右子节点
  - 如果不抢的话，那么我们可以继续抢左右子节点，当然也可以不抢。抢不抢取决于哪个价值更大。

- 抢不抢取决于哪个价值更大。

这是一个明显的递归问题，我们使用递归来解决。由于没有重复子问题，因此没有必要 cache ，也没有必要动态规划。

## 关键点

- 对每一个节点都分析，是抢还是不抢

## 代码

```python
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(cur):
            if not cur:
                return 0,0
            robleft, notrobleft = helper(cur.left)   #对应cur.left结点，抢它或者不抢它的 收益值
            robright, notrobright = helper(cur.right)
            robcur = notrobleft+ notrobright +cur.val #如果抢cur结点，
            notrobcur = max(robleft, notrobleft)+max(robright, notrobright)#如果不抢cur结点
            return robcur, notrobcur  #对应cur结点，抢它或者不抢它的 收益值
        robcur, notrobcur= helper(root)
        return max(robcur, notrobcur)
```

