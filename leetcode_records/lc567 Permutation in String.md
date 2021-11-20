\567. Permutation in String

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        if len(s2)<m:
            return False
        dic1 = {}
        dic2 = {}
        for i in range(m):
            dic2[s2[i]] = dic2.get(s2[i],0)+1 
            dic1[s1[i]] = dic1.get(s1[i],0)+1 
        if dic1 == dic2:
            return True
        for i in range(m,len(s2)):
            
            dic2[s2[i]] = dic2.get(s2[i],0)+1  
            dic2[s2[i-m]] -=1
            
            if dic2[s2[i-m]]==0:
                del dic2[s2[i-m]]
            if dic1==dic2:
                return True
        return False
```

