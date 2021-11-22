class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def helper(nums,startIndex):
            repeat = []
            if len(path)>=2:
                res.append(path[:])
            for i in range(startIndex, len(nums)):
                if nums[i] in repeat:
                    continue
                if len(path)>=1:
                    if nums[i]<path[-1]:
                        continue
                repeat.append(nums[i])
                path.append(nums[i])
                helper(nums,i+1)
                path.pop()
        helper(nums,0)
        return res