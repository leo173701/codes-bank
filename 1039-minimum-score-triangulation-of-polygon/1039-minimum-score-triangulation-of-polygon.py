class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n=len(values)
        dp = [[0 ]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+2,n):
                dp[i][j]=float('inf')
                temp = values[i]*values[j]
                for k in range(i+1,j):
                    dp[i][j]=min(dp[i][j], dp[i][k]+dp[k][j]+values[k]*temp)
        return dp[0][n-1]