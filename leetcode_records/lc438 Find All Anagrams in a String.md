\438. Find All Anagrams in a String

思路：

1. 利用哈希表统计各个字符的频数
2. 固定窗口的滑动窗口问题
3. 适当删除 哈希表当中的元素

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = collections.Counter(p)
        k = len(p)
        temp = collections.Counter(s[:k])   # 这里做一下初始化
        res = []
        if temp== target:
            res.append(0)
        for i in range(1,len(s)-k+1):  
            temp[s[i+k-1]] = temp.get(s[i+k-1],0)+1
            temp[s[i-1]] -=1
            if temp[s[i-1]]==0:
                del temp[s[i-1]]
            if temp == target:
                # print(s[i:i+k])
                # print(temp)
                res.append(i)
        return res
```

