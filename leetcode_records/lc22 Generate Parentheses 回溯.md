

\22. Generate Parentheses

要点： 左括号数量>=右括号数量

1. 当左括号数量> 右括号数量， 可以添加左或者右括号
2. 当左括号数量= 右括号数量， 只可以添加左括号

递归过程中解决:

- 如果当前右括号数量等于括号对数 n, 那么当前字符串即是一种组合, 放入解中.
- 如果当前左括号数量等于括号对数 n, 那么当前字符串后续填充满右括号, 即是一种组合.
- 如果当前左括号数量未超过 n:
  - 如果左括号多于右括号, 那么此时可以添加一个左括号或右括号, 递归进入下一层
  - 如果左括号不多于右括号, 那么此时只能添加一个左括号, 递归进入下一层





对于搜索的递归函数的步骤如下：

1. 判断当前括号序列是否合法，如果不合法，返回。
2. 如果括号序列满足长为2n，将当前序列加入结果的字符串序列中，返回。
3. 尝试在末尾添加左括号，记录状态并递归。
4. 尝试在末尾添加右括号，记录状态并递归。
5. 结束递归。



```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==1:
            return ["()"]
        if n==2:
            return ["()()", "(())"]
        if n==3:
            return ["((()))","(()())","(())()","()(())","()()()"]
        res = []
        path = []
        def dfs(left, right, n, path):
            
            if left>n or right>n:# 每边的括号数小于等于 n
                return
            if left==n and right==n:  # 满足条件，加入result
                res.append(path)
            if left<right:       # 左括号个数一定小于等于右括号
                return
            dfs(left+1, right, n, path+"(")   # 搜索加左括号的情况
            dfs(left, right+1, n, path+")")   # 搜索加右括号的情况
        dfs(0,0,n,"")
        return res
```

