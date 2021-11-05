BFS 模板题： 无权图最短路径



\909. Snakes and Ladders    

https://leetcode.com/problems/snakes-and-ladders/

类似的题目还有： lc1311. Get Watched Videos by Your Friends



![img](https://assets.leetcode.com/uploads/2018/09/23/snakes.png)



从1出发，问到达n*n 一共最少需要几步？

BFS 模板题：

1. 判断边界
2. visited 来查重，对算法加速
3. 什么时候return？   到达终点了就return

dist = {1: 0}            #用哈希表来表示距离， 同时也起到了visited 的作用。

dist[(x,y)] = 0  



```python
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)

        def loation(s):              # 找到在board 对应的位置
            # Given a square num s, return board coordinates (r, c)
            quot, remaider = divmod(s-1, N)
            row = N - 1 - quot
            if row%2 != N%2:
                col = remaider 
            else:
                col = N - 1 - remaider
            return row, col      
        distance = {1: 0}            #用哈希表来表示距离， 同时也起到了visited 的作用。
        queue = collections.deque([1])
        while queue:
            cur = queue.popleft()
            if cur == N*N: 
				return distance[cur]
            for newpoint in range(cur+1, min(cur+6, N*N) + 1): # 下一步能走到哪里
                                         # 只要在这个范围内，那就不用考虑越界的事情。
                r, c = loation(newpoint)
                if board[r][c] != -1:
                    newpoint = board[r][c]   #如果遇到楼梯，那就再多走一步
                if newpoint not in distance:     # 如果没有在visited 当中，那就加入到哈希表当中
                    distance[newpoint] = distance[cur] + 1
                    queue.append(newpoint)
        return -1
```

