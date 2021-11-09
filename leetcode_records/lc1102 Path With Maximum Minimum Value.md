

**1102 Path With Maximum Minimum Value**

BFS+PriorityQueue 模板题



给定具有R行和C列的整数矩阵，请找到一条起点为`[0,0]`，终点为`[r-1,c-1]`，且路径分数最大的路径。

其中路径分数是指该路径中的经过最小值。 例如，路径`8→4→5→9`的路径分数为`4`。

你只能从当前位置向上下左右这四个方向行走，不能斜向行走，且走过的点不能重复。

![图片](https://media.jiuzhang.com/media/markdown/images/11/19/3c9095b0-0a60-11ea-8a23-0242ac110002.jpg)

```python
示例3:
输入: [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
输出: 3
```

```python
import heapq
class Solution:
    """
    @param A: a List[List[int]]
    @return: Return the maximum score of a path
    """
    def maximumMinimumPath(self, A):
        # Write your code here
        
        minNum = A[0][0]
        start = (0, 0)
        end = (len(A) - 1, len(A[0]) - 1)
        pq = []
        heapq.heappush(pq, (-A[0][0], start))
        viewed = set()
        points = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while pq:
            num, curr = heapq.heappop(pq)
            minNum = min(minNum, -num)     # 比较的一步在这里
            viewed.add(curr)               # 在这里加入到visited
            if curr == end:
                return minNum
                
            for point in points:
                dx = curr[0] + point[0]
                dy = curr[1] + point[1]
                if dx < 0 or dx >= len(A) or dy < 0 or dy >= len(A[0]) or (dx, dy) in viewed:
                    continue
                heapq.heappush(pq, (-A[dx][dy], (dx, dy)))
        
        return -1
```



```python
    def maximumMinimumPath(self, A):
        import heapq
        q = [(-A[0][0], 0, 0)]
        visited = set((0, 0))
        n, m = len(A), len(A[0])
        res = -float('inf')

        while q:
          node = heapq.heappop(q)
          val, x, y = node
          val = -val
          if x == n - 1 and y == m - 1:
            res = max(res, val)            #在最后输出的时候，做一次比较
          for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            newx, newy = x + dx, y + dy
            if not (0 <= newx < n and 0 <= newy < m):
              continue
            if (newx, newy) in visited:
              continue
            heapq.heappush(q, (-min(val, A[newx][newy]), newx, newy))
            visited.add((newx, newy))        # 比较的一步在这里
        return res
```

