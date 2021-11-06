



598 · 僵尸矩阵

```python
class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # write your code here
        m = len(grid)
        n = len(grid[0])
        queue = collections.deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    queue.append((i,j))
        days = -1
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        while queue:
            k = len(queue)
            days +=1
            for _ in range(k):
                curx,cury = queue.popleft()
                for dx, dy in directions:
                    newx, newy = curx +dx,cury+dy
                    if 0<=newx<m and 0<=newy<n:  
                        if grid[newx][newy]==2 or grid[newx][newy]==1:
                            continue
                        else:
                            grid[newx][newy]=1
                            queue.append((newx,newy))
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    return -1
        return days 
```

