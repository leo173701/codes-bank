class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        ans = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[j][i] = dp[j-1][i-1]+1
                    ans = max(ans, dp[j][i])
        return ans
        