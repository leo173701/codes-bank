class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        if n==2:
            return 91
        if n==1:
            return 10
        dp=[1,9]
        for i in range(2,n+1):
            temp=dp[i-1]*(11-i)
            dp.append(temp)
        return sum(dp)