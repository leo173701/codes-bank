

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

另外一种做法： 再来一个哈希表 来存储结果

```python
# BFS 做法
from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        q=collections.deque()
        time =0
        m = len(rooms)
        n = len(rooms[0])
        count=0
        timetable = {}
    # 对q初始化， 统计最开始的时候有多少
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    q.append((i,j))
                elif rooms[i][j]==2147483647:
                    count+=1
                    timetable[(i,j)]=m*n
        # print(timetable.keys())
        while count>0 and len(q)>0:
            length = len(q)
            # print(q)
            # print("第",time+1,"轮扩散")
            for _ in range(length):
                i,j = q.popleft()
                # print("  从",i,j,"位置扩散，")
                for (x,y) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    
                    if x>=m or x<0 or y>=n or y<0 or rooms[x][y]==-1:#越界或者遇到墙
                        continue
                    if rooms[x][y]==0:  #在之前的过程当中，这个位置已经访问过了，它不会被扩散
                        continue
                    # print("         现在扩散到这里：", x,y)
                    rooms[x][j]=0
                    # count-=1  #同时，新鲜的数量-1
                    q.append((x,y))
                    timetable[(x,y)]=min(timetable[(x,y)], time) #记录下扩散到当前位置需要多长的时间-1
            time +=1
        for x,y in timetable.keys():
            if timetable[(x,y)]==m*n:
                rooms[x][y] = 2147483647
            else:
                rooms[x][y]=timetable[(x,y)]+1
```

