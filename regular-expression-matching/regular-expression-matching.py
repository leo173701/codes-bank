class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for i in range(0,len(p) + 1)] for j in range(0, len(s) + 1)]
        dp[0][0] = True   #dp[0][0]初始化为true，由此开始转移
        for i in range(1, len(p) + 1):
            if (p[i - 1] == '*'):		
                dp[0][i] = dp[0][i - 2]  
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':     
                    dp[i][j] = dp[i][j - 2]    
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':  #'*'不去匹配
                        dp[i][j] |= dp[i-1][j]
                else:
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':  #如果两字符相同或者为.
                        dp[i][j] = dp[i - 1][j - 1]    #当前状态由前一个转移而来
    
        return dp[len(s)][len(p)]
                