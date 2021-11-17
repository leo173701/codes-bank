class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, nums, path):
            res.append(path[:])
            
            for i in range(start,len(nums)):
                path.append(nums[i])
                dfs(i+1,nums,path)
                path.pop()
        res = []
        dfs(0,nums,[])
        return res