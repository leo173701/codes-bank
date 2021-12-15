class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2==1:
            return False
        half = s//2
        dp =[False]*(half+1)
        dp[0]=True
        for number in nums:
            for j in range(half, number-1,-1):
                dp[j]=dp[j] or dp[j-number]
        return dp[half]
        