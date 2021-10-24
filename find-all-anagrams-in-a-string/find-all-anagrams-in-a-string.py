class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
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
        