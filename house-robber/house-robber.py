class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        dp = [nums[0]]*n
        dp[1]= max(nums[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[n-1]