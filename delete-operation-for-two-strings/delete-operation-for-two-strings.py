class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # length1 = len(word1)
        # length2 = len(word2)
        # res = 0
        # dp = [[0]*(length2+1)]*(length1+1)
        # for i in range(1,length1+1):
        #     for j in range(1,length2+1):
        #         dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        #         if word1[i-1]==word2[j-1]:
        #             dp[i][j]=max(dp[i][j],dp[i-1][j-1]+1)
        # print(dp)
        # return length1+length2-dp[length1][length2]*2
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (word1[i] == word2[j]))
        return m + n - 2 * dp[m][n]