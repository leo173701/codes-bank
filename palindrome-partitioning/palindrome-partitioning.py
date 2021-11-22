class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        if n==1:
            return [[s]]
        def valid(temp):
            if not temp:
                return False
            left = 0
            right = len(temp)-1
            while left<=right:
                if temp[left]!=temp[right]:
                    return False
                left+=1
                right-=1
            return True
        def dfs(start,n,path):
            if start ==n:
                res.append(path[:])
                return
            for i in range(start, n):
                temp  = s[start:i+1]
                # print("temp = ",temp)
                if valid(temp):
                    # print("         ",temp," is valid")
                    dfs(i+1, n,path+[temp])
        res = []
        dfs(0,n,[])
        return res