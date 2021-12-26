class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        counts = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        counts[i] = counts[j]
                    elif dp[j] + 1 == dp[i]:
                        counts[i] += counts[j] #出现重复的情况
        print(dp)
        print(counts)
        max_length = 1
        max_count = 0
        for i, n in enumerate(dp):
            if n > max_length:
                max_length = n
                max_count = counts[i]
            elif n == max_length:
                max_count += counts[i]
        return max_count
                        