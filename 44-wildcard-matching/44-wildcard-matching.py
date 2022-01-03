class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if set(p)=={"*"}:
            return True
        if not s and not p:
            return True
        
        dp = [[False ]*(len(p)+1) for j in range(len(s) + 1)]
        dp[0][0] = True   #dp[0][0]初始化为true，由此开始转移
        for i in range(1, len(p) + 1):
            if (p[i - 1] == '*'):		
                dp[0][i] = dp[0][i - 1]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1]!="*":
                    if s[i-1]==p[j-1] or p[j-1]=="?":
                        dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=dp[i][j-1] or dp[i-1][j]  #"abcd"   p="ab*cd" *对应空序列，当做不存在
        return dp[-1][-1]