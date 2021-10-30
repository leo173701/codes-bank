

\1091. Shortest Path in Binary Matrix

![img](https://assets.leetcode.com/uploads/2021/02/18/example2_1.png)

单起点，  单终点的最短步数问题

1.  二维BFS
2.  8个维度都能走direction = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
3.  可以使用 visited， 但直接在grid 上面修改值 就可以降低空间复杂度
4.  当curx == goalx;  cury ==goaly的时候，就是到达终点。



方法一：

```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        n = len(grid[0])
        direction = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        step = 1
        queue = deque([(0,0)])
        grid[0][0]=1                       #改变grid的值，这样避免使用visited 降低空间复杂度
        while queue:
            for _ in range(len(queue)):
                curx, cury = queue.popleft()
                if curx==n-1 and cury==n-1:    #判断是否到达终点
                    return step
                for dx,dy in direction:
                    newx, newy = dx+curx, dy+cury
                    if 0<=newx<n and 0<=newy<n and grid[newx][newy]==0:
                        queue.append((newx,newy)) 
                        grid[newx][newy]=1
            step +=1
        return -1
```



方法二

```python
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        q = [(0, 0, 1)]
        grid[0][0] = 1
        for i, j, d in q:
            if i == n-1 and j == n-1: return d
            for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    grid[x][y] = 1
                    q.append((x, y, d+1))
        return -1
```

