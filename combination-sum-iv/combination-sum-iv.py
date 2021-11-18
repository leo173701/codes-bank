class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for j in range(1, target + 1):
            for num in nums:
                if num > j:
                    continue
                dp[j] += dp[j - num]
        
        return dp[target]