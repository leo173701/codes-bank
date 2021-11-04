\417. Pacific Atlantic Water Flow

![img](https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg)

我的思路：

1. 从边缘往中间走，记录下可以到达的点，写入res1, res2
2. 求res1, res2的交集。

```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        qPacific = deque([])
        qAtlantic = deque([])
        for i in range(n):
            qAtlantic.append((m-1,i))
            qPacific.append((0,i))
        for i in range(m):
            qAtlantic.append((i,n-1))
            qPacific.append((i,0))
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        res1 = set()
        res2 = set()
        while qPacific:
            curx, cury = qPacific.popleft()
            res1.add((curx,cury))
            for dx,dy in directions:
                newx, newy = curx +dx, cury +dy
                if (newx,newy) in res1:
                    continue
                if 0<=newx<m and 0<=newy<n :
                    # print((newx,newy))
                    if heights[newx][newy] >=heights[curx][cury]:
                        qPacific.append((newx,newy))
        # print(res1) 
        res = set()
        while qAtlantic:
            curx, cury = qAtlantic.popleft()
            if (curx,cury) in res1:
                res.add((curx,cury))
            res2.add((curx,cury))
            for dx,dy in directions:
                newx, newy = curx +dx, cury +dy
                if (newx,newy) in res2:
                    continue
                if 0<=newx<m and 0<=newy<n :
                    # print((newx,newy))
                    if heights[newx][newy] >=heights[curx][cury]:
                        qAtlantic.append((newx,newy))
        # print(res)
        return list(res)
```



别人的思路：

从四周往内部dfs，最后判断哪些点两个大洋都可达。

```python
class Solution:
    """
    @param matrix: the given matrix
    @return: The list of grid coordinates
    """
    def pacificAtlantic(self, matrix):
        if not matrix: return []
        pacific,atlantic = set(),set()
        m,n = len(matrix),len(matrix[0])
        for i in xrange(n):
            self.dfs(0, i, matrix, pacific, 0)
            self.dfs(m - 1, i, matrix, atlantic, 0)
        for i in xrange(m):
            self.dfs(i, 0, matrix, pacific, -1)
            self.dfs(i, n - 1, matrix, atlantic, 0)
        return list(pacific&atlantic)
        
    def dfs(self, x, y, matrix, visit, height):
        m,n = len(matrix),len(matrix[0])
        if x < 0 or x >= m or y < 0 or y >= n or (x,y) in visit:
            return
        if matrix[x][y] < height:
            return
        visit.add((x,y))
        self.dfs(x - 1, y, matrix, visit, matrix[x][y]) 
        self.dfs(x + 1, y, matrix, visit, matrix[x][y]) 
        self.dfs(x, y - 1, matrix, visit, matrix[x][y]) 
        self.dfs(x, y + 1, matrix, visit, matrix[x][y])
```

