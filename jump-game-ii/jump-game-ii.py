class Solution:
    def jump(self, A: List[int]) -> int:
        
        n = len(A)
        if n==1:
            return 0       # corner case: A=[0], 起点即终点
        if A[0]>=n:
            return 1
        dp = [0]*n
        count = [float('inf')]*n
                               # dp[i]表示从第i个点出发，最大能到达第几个点
        dp[0] = A[0] 
        
        for j in range(min(A[0]+1, n)):
            count[j] = 1
        for i in range(1,n):
            if dp[i-1]< i+A[i]:
                dp[i] = i+A[i]
                if dp[i]>=n-1:
                    return min(count[i]+1,count[n-1])  #已经到达终点，可以直接清算
                for j in range(i+1,i+A[i]+1):
                    count[j] = min(count[i]+1,count[j])  #从i开始跳
            else:
                dp[i]=dp[i-1]