



\1631. Path With Minimum Effort
https://leetcode.com/problems/path-with-minimum-effort/

标准的做法

```python

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        distance = [[float('inf')] * n for _ in range(m)]  # 用数组来表示，更快        
        distance[0][0]=0
        pq = [(0,0,0)]
        while pq:
            cur_distance, x,y = heapq.heappop(pq)
            if cur_distance>distance[x][y]:
                continue
            if x==m-1 and y==n-1:
                return cur_distance
            for dx,dy in ((-1,0),(1,0),(0,1),(0,-1)):
                newx, newy = dx+x, dy+y
                if 0<=newx<m and 0<=newy<n:
                    effort = abs(heights[newx][newy] - heights[x][y])
                    new_distance = max ( cur_distance, effort)
                    if distance[newx][newy]>new_distance:
                        distance[newx][newy]=new_distance
                        heapq.heappush(pq,(new_distance, newx, newy))
        return -1
```

