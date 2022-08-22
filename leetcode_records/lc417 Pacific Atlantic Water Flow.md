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

BFS 思路：从两个终点分别处罚，分别用visited=set() 来记录能扩散到哪些点，
         最后求一下交集
```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])
        
        qA = collections.deque()
        qB = collections.deque()
        visitedA = set()
        visitedB = set()
        for i in range(m):
            qA.append((i,0))
            visitedA.add((i,0))
            qB.append((i,n-1))
            visitedB.add((i,n-1))
        for j in range(n):
            qA.append((0,j))
            qB.append((m-1,j))
            visitedA.add((0,j))
            visitedB.add((m-1,j))
        
        while qA:
            #不用考虑步数，直接一口气全部添加
            curx, cury = qA.popleft()
            for newx, newy in [(curx,cury +1),(curx,cury -1),(curx+1,cury),(curx-1,cury)]:
                if newx<0 or newx>=m or newy<0 or newy>=n:  #越界了，
                    continue
                #满足某种条件就加入进q
                if (newx,newy) in visitedA:
                    continue
                if heights[newx][newy] >= heights[curx][cury]:
                    visitedA.add((newx,newy))
                    qA.append((newx,newy))
        
        # res = []
        while qB:
            #不用考虑步数，直接一口气全部添加
            curx, cury = qB.popleft()
            for newx, newy in [(curx,cury +1),(curx,cury -1),(curx+1,cury),(curx-1,cury)]:
                if newx<0 or newx>=m or newy<0 or newy>=n:  #越界了，
                    continue
                #满足某种条件就加入进q
                if (newx,newy) in visitedB:
                    continue
                if heights[newx][newy] >= heights[curx][cury]:
                    visitedB.add((newx,newy))
                    qB.append((newx,newy))
                    
#         print(visitedA)
#         print(visitedB)
        c = visitedA.intersection(visitedB)  #求交集
        return [[x,y] for (x,y) in c]
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

