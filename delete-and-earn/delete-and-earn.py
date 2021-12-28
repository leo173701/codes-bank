class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        frequency = collections.Counter(nums)
        maxvalue = max(nums)
        dp = [[0,0] for _ in range(maxvalue+1)]
        #dp[i][0] 代表「不选」数值 i；
        #dp[i][1] 代表「选择」数值 i
        for i in range(1,maxvalue+1):
            dp[i][1]= dp[i-1][0]+ i * frequency.get(i,0)
            dp[i][0]=max(dp[i-1][0],dp[i-1][1])
        print(dp)
        return max(dp[maxvalue])