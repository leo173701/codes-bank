class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = [1] + nums + [1]
        n = len(nums)
        dp=[[0]*n  for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+2,n):
                temp_ij=nums[i]*nums[j]
                for k in range(i+1,j):
                    dp[i][j]=max(dp[i][j], dp[i][k]+dp[k][j]+temp_ij*nums[k])
        return dp[0][n-1]