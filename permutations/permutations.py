class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [False for _ in range(n)]
        res = []
        def dfs(nums, n, path):
            if len(path)==n:
                res.append(path[:])
            for index,value in enumerate(nums) :
                if visited[index]==True:
                    continue
                visited[index]=True
                path.append(value)
                dfs(nums,n,path)
                path.pop()
                visited[index]=False
        dfs(nums,n,[])
        return res