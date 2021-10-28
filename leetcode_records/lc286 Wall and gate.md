

[286. Walls and Gates](https://leetcode.com/problems/walls-and-gates)

问地图中每个点 距离最近的出口0的最小距离

其中-1 代表 墙

```python
2D网络为：
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
答案为：
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
```



用bfs来解决此问题。 一开始将所有的门push到队列中，然后bfs遍历整张图即可。

```python
# BFS 做法
from collections import deque
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, A):
        if not A or not A[0]:
            return A
        q = deque([])
        DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))
        visited = set()
        m = len(A)
        n = len(A[0])
        for i in range(m):
            for j in range(n):
                if A[i][j]==0:
                    q.append([i,j])
                    visited.add((i, j))
        while q:
            curx, cury = q.popleft()
            for dx, dy in DIRECTIONS:
                newx = curx+dx
                newy = cury+dy
                if 0<=newx<m and 0<=newy<n and (newx,newy) not in visited and A[newx][newy] == 2147483647:
                    A[newx][newy] = A[curx][cury]+1
                    q.append([newx,newy])
                    visited.add((newx, newy))
```

