lc887. Super Egg Drop

[1884. Egg Drop With 2 Eggs and N Floors](https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors)

## 1. 思路1

dp(K, i)  就是K个鸡蛋 总共i层楼 需要多少次

伪代码：(在第 i 楼扔了一次)

```python
for i in range(N):
    res = min(max( 
                        dp(K - 1, i - 1), # 碎
                        dp(K, N - i)      # 没碎
                     ) + 1 # 在第 i 楼扔了一次)
```



首先我们根据 `dp(K, N)` 数组的定义（有 `K` 个鸡蛋面对 `N` 层楼，最少需要扔几次），**很容易知道 `K` 固定时，这个函数随着 `N` 的增加一定是单调递增的**，无论你策略多聪明，楼层增加测试次数一定要增加。

那么注意 `dp(K - 1, i - 1)` 和 `dp(K, N - i)` 这两个函数，其中 `i` 是从 1 到 `N` 单增的，如果我们固定 `K` 和 `N`，**把这两个函数看做关于 `i` 的函数，前者随着 `i` 的增加应该也是单调递增的，而后者随着 `i` 的增加应该是单调递减的**：

![img](https://github.com/labuladong/fucking-algorithm/raw/master/pictures/%E6%89%94%E9%B8%A1%E8%9B%8B/2.jpg)

```python
def superEggDrop(self, K: int, N: int) -> int:
        
    memo = dict()
    def dp(K, N):
        if K == 1: return N
        if N == 0: return 0
        if (K, N) in memo:
            return memo[(K, N)]                          

        res = float('INF')
        # 用二分搜索代替线性搜索
        lo, hi = 1, N
        while lo <= hi:
            mid = (lo + hi) // 2
            broken = dp(K - 1, mid - 1) # 碎
            not_broken = dp(K, N - mid) # 没碎
            # res = min(max(碎，没碎) + 1)
            if broken > not_broken:
                hi = mid - 1
                res = min(res, broken + 1)
            else:
                lo = mid + 1
                res = min(res, not_broken + 1)

        memo[(K, N)] = res
        return res
    
    return dp(K, N)
```

## 2.思路2

```python
dp[k][m] = n
# 当前有 k 个鸡蛋，可以尝试扔 m 次鸡蛋
# 这个状态下，最坏情况下最多能确切测试一栋 n 层的楼

# 比如说 dp[1][7] = 7 表示：
# 现在有 1 个鸡蛋，允许你扔 7 次;
# 这个状态下最多给你 7 层楼，
# 使得你可以确定楼层 F 使得鸡蛋恰好摔不碎
# （一层一层线性探查嘛）
```

**给你 `K` 鸡蛋，`N` 层楼，让你求最坏情况下最少的测试次数 `m`** 吗？`while` 循环结束的条件是 `dp[K][m] == N`，也就是**给你 `K` 个鸡蛋，测试 `m` 次，最坏情况下最多能测试 `N` 层楼**。



这个图描述的仅仅是某一个楼层 `i`，原始解法还得线性或者二分扫描所有楼层，要求最大值、最小值。但是现在这种 `dp` 定义根本不需要这些了，基于下面两个事实：

**1、无论你在哪层楼扔鸡蛋，鸡蛋只可能摔碎或者没摔碎，碎了的话就测楼下，没碎的话就测楼上**。

**2、无论你上楼还是下楼，总的楼层数 = 楼上的楼层数 + 楼下的楼层数 + 1（当前这层楼）**。

根据这个特点，可以写出下面的状态转移方程：

```
dp[k][m] = dp[k][m - 1] + dp[k - 1][m - 1] + 1
```

**`dp[k][m - 1]` 就是楼上的楼层数**，因为鸡蛋个数 `k` 不变，也就是鸡蛋没碎，扔鸡蛋次数 `m` 减一；

**`dp[k - 1][m - 1]` 就是楼下的楼层数**，因为鸡蛋个数 `k` 减一，也就是鸡蛋碎了，同时扔鸡蛋次数 `m` 减一。

PS：这个 `m` 为什么要减一而不是加一？之前定义得很清楚，这个 `m` 是一个允许的次数上界，而不是扔了几次。

| <img src="https://github.com/labuladong/fucking-algorithm/raw/master/pictures/%E6%89%94%E9%B8%A1%E8%9B%8B/3.jpg" alt="img" style="zoom: 50%;" /> | 在 i=4 这一层扔下去 <img src="https://github.com/labuladong/fucking-algorithm/raw/master/pictures/%E6%89%94%E9%B8%A1%E8%9B%8B/1.jpg" alt="img" style="zoom: 50%;" /> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

```python
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0 for col in range(K + 1)] for row in range(N + 1)];
        count = 0;
        while dp[count][K] < N:
            count = count + 1;
            for i in range(1,K + 1):
                dp[count][i] = dp[count - 1][i - 1] + dp[count - 1][i] + 1;
        return count;
```



参考自：	https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E9%AB%98%E6%A5%BC%E6%89%94%E9%B8%A1%E8%9B%8B%E8%BF%9B%E9%98%B6.md

