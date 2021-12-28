class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n=len(arr)
        if n==1:
            return 1
        dp={}
        res = 0
        for x in arr:
            dp[x] = dp.get(x-difference,0)+1
            res=max(res,dp[x])
        return res 