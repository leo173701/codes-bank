class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        
        # dp[i] 以dp[i]为最大值的子集的个数，此为核心数组，不会保存具体方案
        dp = [1] * len(nums)
        # prev[i] 代表dp[i]的最优值从哪个j算过来的
        prev = [-1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        
        # 具体方案
        path = []
        longest, last = max(dp), dp.index(max(dp))
        while last != -1:
            path.append(nums[last])
            last = prev[last]
        
        return path[::-1]