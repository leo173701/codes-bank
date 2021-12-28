class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n==1:
            return 1
        dp = [1]*n  #表示以i 结尾的最长有多长
        res = 1
        if arr[1]!=arr[0]:
            dp[1]=2
        res=max(res,dp[1])
        for i in range(2,n):
            if arr[i]==arr[i-1]:
                dp[i]=1
                continue
            else:
                if arr[i]>arr[i-1]>arr[i-2] or arr[i]<arr[i-1]<arr[i-2]:
                    dp[i]=2
                else:
                    dp[i]=dp[i-1]+1
            res = max(res,dp[i])
        return res