class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        length1 = len(s1)
        length2 = len(s2)
        if len(s3)!=length1+length2:
            return False
        dp=[[False ]*(length2+1) for _ in range(length1+1)]
        dp[0][0]=True
        for i in range(1,length1+1):
            if dp[i-1][0]==True and s3[i-1]==s1[i-1]:
                dp[i][0] =True
        for j in range(1,length2+1):
            if dp[0][j-1]==True :
                if s3[j-1]==s2[j-1]:
                    dp[0][j] =True 
        for i in range(1,length1+1):
            for j in range(1,length2+1):
                if dp[i-1][j] and s3[i+j-1]==s1[i-1]:
                    dp[i][j]= True
                if dp[i][j-1] and s3[i+j-1]==s2[j-1]:
                    dp[i][j]=True
        return dp[length1][length2]