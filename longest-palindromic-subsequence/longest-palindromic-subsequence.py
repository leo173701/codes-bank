class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        if length <2:
            return length
        dp = [[0] * length for _ in range(length)]
        for i in range(length - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][length - 1]
        # n = len(s)
        # if n<2:
        #     return n
        # dp = [[0]*n for _ in range(n)]
        # for i in range(n - 1,-1,-1):
        #     dp[i][i]=1
        #     for j in range(i + 1,n):
        #         if s[i]==s[j]:
        #             dp[i][j]=dp[i-1][j-1]+2
        #         else:
        #             dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        # return dp[0][n-1]