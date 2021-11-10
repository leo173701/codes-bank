

\407. Trapping Rain Water II

给一个二维矩阵，问能装多少水。

思路要点：

1. BFS 遍历问题（没有起点和终点）， 那所有点都需要加入到queue 当中。（不找最值）
2. 没有明显的起点和终点时， 就从边界开始 加入到queue 当中
3. 木桶理论，以四周最短的那条边 来计算储水量。 自然想到 priorityqueue 每次pop出高度最小的点。
4. 用 `h = max(curheight, heightMap[newx][newy]) #取更大值作为新点边界，记作 h
       res +=max(0, h-heightMap[newx][newy])   #和边界的差值，就是这个新点(newx,newy)的储水量
       heapq.heappush(pq,(h, newx,newy))    #把新点以新边界 h 加入到pq当中`

![img](https://assets.leetcode.com/uploads/2021/04/08/trap1-3d.jpg)

![img](https://assets.leetcode.com/uploads/2021/04/08/trap2-3d.jpg)



九章强化班上，侯卫东老师的版本: 

首先从边界开始，边界的吃水线是其本身的高度； 利用heap来维护最小的吃水线及其位置，每次从从吃水线最低的那个点开始向四周辐射，来维护这个heap。

由于在维护heap当中，每个元素存储的是(val, x, y),其中x,y是唯一的，直接按这个顺序push和pop就没问题了

```python
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        m,n = len(heightMap), len(heightMap[0])
        pq = []
        visited = {}
        res = 0
        for i in range(m):
            for j in range(n):
                if i==0 or i==m-1 or j==0 or j==n-1:
                    visited[(i,j)]=1
                    heapq.heappush(pq,(heightMap[i][j], i,j))
                else:
                    visited[(i,j)]=0
        while pq:
            curheight, curx, cury = heapq.heappop(pq)
            for newx, newy in [(curx-1, cury),(curx+1, cury),(curx, cury-1),(curx, cury+1)]:
                if newx>=m or newx<0 or newy>=n or newy<0 or visited[(newx,newy)]==1:
                    continue
                h = max(curheight, heightMap[newx][newy]) #找到一个更大的边界，记作 h
                res +=max(0, h-heightMap[newx][newy])   #和边界的差值，就是这个新点(newx,newy)的储水量
                visited[(newx,newy)]=1         # 记录下已经visited       
                heapq.heappush(pq,(h, newx,newy))    #所有附近的点都加入到pq当中了
        return res
```

