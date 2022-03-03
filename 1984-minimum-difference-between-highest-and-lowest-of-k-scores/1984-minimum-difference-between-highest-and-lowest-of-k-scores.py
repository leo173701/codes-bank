class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        if n<1:
            return 0
        nums.sort()
        res = nums[k-1]-nums[0]
        for i in range(k, len(nums)):
            res = min(res, nums[i] - nums[i - k + 1])
        return res