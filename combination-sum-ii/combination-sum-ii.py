class Solution:
    def combinationSum2(self, num: List[int], target: int) -> List[List[int]]:
        # write your code here
        nums = sorted(num)
        subset,result = [],[]
        start_index = 0
        self.dfs(nums, target, start_index,subset,result)
        return result
        
    def dfs(self, nums, target, start_index,subset,result):
        # combination sum 例题的出口
        if target ==0:
            result.append(subset[:])
            return 
        
        for i in range(start_index, len(nums)):
            if nums[i]>target:
                return 
            # subset with duplicate 的判定
            if nums[i] == nums[i-1] and i > start_index:
                continue 
            subset.append(nums[i])
            self.dfs(nums, target-nums[i], i+1,subset,result)
            subset.pop()