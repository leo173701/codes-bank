\77. Combinations

```python
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

```python
class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        results = []
        self.dfs(n, k, 0, [], results)
        return results
    
    def dfs1(self, n, k, index, combination, results):
        
        if len(combination) == k:# 第一个递归出口，如果满足 k 个，将这种组合加入最终结果中
            results.append(list(combination))
            return
        if index == n+1:
            return            # 第二个递归出口，如果以访问完1 ~ n所有数字，退出当前函数
        if n - index < k - len(combination):# 可行性剪枝，如果后面的数都放入，个数不足k的话，退出
                       #可供选择的nums数 < 组成combination所需的数, 可以提前return
            return
        #解法1: Index即代表从1....n的一个数，每遍历到一个数，两种选择: 选 / 不选
        combination.append(index + 1) #如果将当前数放入组合，将pos加入combination，继续递归
        self.dfs(n, k, index + 1, combination, results) 
        combination.pop()                   # 递归结束后，弹出pos，还原状态
        
        self.dfs(n, k, index + 1, combination, results) # 不将pos加入combination的情况
    
    def dfs2(self, n, k, index, combination, results):
        if len(combination) == k:
            results.append(list(combination))
            return
        #解法2: Index记录已选的nums数，For loop代表下一步选什么
        for i in range(index+1, n + 1):
            if n - i + 1 < k - len(combination):
                return
            combination.append(i)
            self.dfs(n, k, i, combination, results)
            combination.pop()
```

