class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s)==0:
            return 0
        g.sort()
        s.sort()
        left = 0
        right = 0
        res = 0
        while left<len(g) and right < len(s):
            if g[left]<=s[right]:
                left+=1
                right+=1
                res +=1
            else:
                right+=1
        return res