class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        visited = collections.Counter(nums)
        # print(visited)
        n = len(visited)
        if n==1:
            return nums[0]*visited[nums[0]]
        dp = [0]*n
        temp = list(visited.keys())
        temp.sort()
        # print(temp)
        dp[0] = temp[0]*visited[temp[0]]
        if temp[1]-temp[0]==1:
            dp[1]=max(dp[0], temp[1]*visited[temp[1]])
        else:
            dp[1]=dp[0]+temp[1]*visited[temp[1]]
        if n==2:
            return dp[1]
        for i in range(2,n):
            if temp[i]-temp[i-1]==1:
                dp[i]=max(dp[i-1], temp[i]*visited[temp[i]] + dp[i-2])
            else:
                dp[i]=dp[i-1]+temp[i]*visited[temp[i]] 
        return dp[n-1]