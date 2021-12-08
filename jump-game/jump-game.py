class Solution:
    def canJump(self, A: List[int]) -> bool:
        n = len(A)
        if n==1:
            return True
        dp = [0]*n
        # 从第i个点出发，最大能到多远
        dp[0] = A[0]
        for i in range(1,n):
            if i-1 >=dp[i-1]:
                return False
            dp[i] = max(dp[i-1], i+A[i])
            if dp[i]>=n-1:
                return True
        return False
