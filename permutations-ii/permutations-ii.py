class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = [False for _ in range(n)]
        def dfs(nums, path, n ):
            if len(path)==n:
                if path not in res:
                    res.append(path[:])
            for index, value in enumerate(nums):
                if visited[index]==True:
                    continue
                visited[index]=True
                path.append(value)
                dfs(nums,path,n)
                path.pop()
                visited[index]=False
        res = []
        dfs(nums, [ ],n)
        return res