class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k>n or n==1 or n>45:
            return []
        nums = [i for i in range(1,10)]
        res = []
        def dfs(nums, startindex, remain, path):
            if remain==0 and len(path)==k:
                res.append(path[:])
            if len(path)==k:
                return
            # if len(path)==k:
            #     if remain==0:
            #         res.append(path[:])
            #     return
            for i in range(startindex,9):                
                if remain< nums[i]:
                    return                
                path.append(nums[i])
                dfs(nums, i+1, remain-nums[i],path)
                path.pop()
        dfs(nums,0,n,[])
        return res
        