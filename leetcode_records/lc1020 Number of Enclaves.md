\1020. Number of Enclaves



![img](https://assets.leetcode.com/uploads/2021/02/18/enclaves1.jpg)



参考lc200. number of islands

思路：从边界入手, 再数剩余网格的数量

```python
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid or len(grid)==0:
            return 0  
        res = 0
        row = len(grid)
        col = len(grid[0])
        q = deque([])
        for i in range(row):
            if grid[i][0]==1:
                q.append((i,0))
                grid[i][0]=0
            if grid[i][col-1]==1:
                q.append((i,col-1))
                grid[i][col-1]=0
        for j in range(col):
            if grid[0][j]==1:
                q.append((0,j))
                grid[0][j]=0
            if grid[row-1][j]==1:
                q.append((row-1,j))
                grid[row-1][j]=0
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        while q:
            curx,cury =q.popleft()
            for dx, dy in directions:
                newx, newy = curx +dx,cury+dy
                if 0<=newx<row and 0<=newy<col:
                    if grid[newx][newy]==1:
                        q.append((newx,newy))
                        grid[newx][newy]=0
        # print(grid)
        for i in grid:
            res +=sum(i)
        return res
```

