

### 93.Restore IP Addresses

排列组合，做隔板，使得分隔出来的内容满足一定的条件。

```
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
```

```python
class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        result = []
        self.dfs(s, 0, 0, "", result)
        return result
    def dfs(self, s, pos, dot, t_string, result): #pos表示当前点的位置，[0,n-1]都可以取
        # 最多加三个点
        if dot > 3:  #点的数量
            return
        # 搜索到最后时
        if pos == len(s):
            if dot == 3:
                nums = t_string.split('.')
                for num in nums:
                    if len(num) > 1 and num[0] == '0':
                        return
                    if int(num) > 255:
                        return
                result.append(t_string)
                return
            return
        
        # pos后不加点的情况
        self.dfs(s, pos + 1, dot, t_string + s[pos], result)
        
        # pos后加点的情况
        if pos < len(s) - 1:
            self.dfs(s, pos + 1, dot + 1, t_string + s[pos] + '.', result)
```

