## 740.Delete and Earn

### 总结： 

1. 找到dp[i],   dp[i-1], dp[i-2] 之间的关系





#### 核心思路：

Once you store the frequency of each number, you can easily see that it is like the **198.House Robber** problem:

 

##### 1.dp的定义

 `dp[i]`   代表到第 i 个位置的时候，最大值是多少：

##### 2.转移方程

2. 如果相邻，那就和**house robber** 一模一样
   `if temp[i]-temp[i-1]==1:`
                   `dp[i]=max(dp[i-1], temp[i]*frequency[temp[i]] + dp[i-2])`
   如果不相邻：那就可以直接加上去

   `else:`
                  `dp[i]=dp[i-1]+temp[i]*frequency[temp[i]]` 

##### 3.初始化

   `dp[0] = nums[0]*frequency[nums[0]]`
   `if temp[1]-temp[0]==1:
            dp[1]=max(dp[0], temp[1]*frequency[temp[1]])
        else:
            dp[1]=dp[0]+temp[1]*frequency[temp[1]]`





```python
class Solution:
    # 输入nums = [2,2,3,3,3,4]
    def deleteAndEarn(self, nums: List[int]) -> int:
        frequency = collections.Counter(nums)  
        # frequency = Counter({3: 3, 2: 2, 4: 1})
        n = len(visited)
        if n==1:
            return nums[0]*frequency[nums[0]]
        dp = [0]*n
        temp = list(frequency.keys())    # 把所有的元素单独列出来：[2, 3, 4]
        temp.sort()
        dp[0] = temp[0]*frequency[temp[0]]
        if temp[1]-temp[0]==1:
            dp[1]=max(dp[0], temp[1]*frequency[temp[1]])
        else:
            dp[1]=dp[0]+temp[1]*frequency[temp[1]]
        if n==2:
            return dp[1]
        for i in range(2,n):
            if temp[i]-temp[i-1]==1:
                dp[i]=max(dp[i-1], temp[i]*frequency[temp[i]] + dp[i-2])
            else:
                dp[i]=dp[i-1]+temp[i]*frequency[temp[i]] 
        return dp[n-1]
```

