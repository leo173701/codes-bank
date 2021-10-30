\1162. As Far from Land as Possible

求各个0 到距离它最近的1 的距离

求上述距离当中的最小值

![img](https://assets.leetcode.com/uploads/2019/05/03/1336_ex1.JPG)

思路：

1. BFS 多起点单一中点，步数最短，不涉及到每一步走多远（Djkstra算法）

2. step 1.找到所有的目标点1, 把它们的坐标存入queue当中，并且也存入visited 当中

3. step 2. step+=1,中间插入for 循环，这样可以很好地按照step  来进行隔断，curx, cury = queue.popleft() ，

4. step 3. 遍历4个方向 [newx, newy]
                1）判断是否在grid范围以内, 而且取值为0
                2）判断是否在visited当中
                3）如果都成立，那就加入[newx, newy] 到queue和visited当中

   ​             4）如果有需要， 可以写上path[newx, newy] = step 表示到达这个点的最短的路程。
   ​                   注意这个step +=1一直存在， 这是一个单调递增的值，所以暂时不用遍历path求最大值。

5. 遍历结束，return step



```python
class Solution:
    """
    @param grid: An array.
    @return: An integer.
    """
    def maxDistance(self, grid):
        DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q = collections.deque()
        visited = set()
        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j))
                    visited.add((i, j))

        step = -1
        while q:
            step += 1    # 每出来一次，step +=1
            queue_size = len(q) #对于这个循环当中所有的，都明确是相同的步数step
            for _ in range(queue_size): 
                x, y = q.popleft()
                for direction in DIRECTIONS:
                    new_x = x + direction[0]
                    new_y = y + direction[1]
                    if not self.is_valid(new_x, new_y, grid):
                        continue
                    if (new_x, new_y) in visited:
                        continue
                    q.append((new_x, new_y))
                    visited.add((new_x, new_y))
        
        return -1 if step == 0 else step

    def is_valid(self, x, y, grid):
        if x < 0 or x >= len(grid):
            return False
        if y < 0 or y >= len(grid[0]):
            return False
        return grid[x][y] == 0
```



```python
DIR = [-1, 0, 1, 0, -1]

class Solution:
    """
    @param grid: An array.
    @return: An integer.
    """
    def maxDistance(self, grid):
        step_to_pos = [[-1] * len(grid[0]) for _ in range(len(grid))]
        queue = collections.deque()
        num_ocean = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    step_to_pos[i][j] = 0
                    queue.append((i, j))
                else:
                    num_ocean += 1
        
        while len(queue) > 0:
            curr_pos = queue.popleft()
            curr_step = step_to_pos[curr_pos[0]][curr_pos[1]]
            for i in range(len(DIR) - 1):
                new_pos = (curr_pos[0] + DIR[i], curr_pos[1] + DIR[i + 1])
                if not self.in_bound(grid, new_pos):
                    continue
                if grid[new_pos[0]][new_pos[1]] == 1:
                    continue
                if step_to_pos[new_pos[0]][new_pos[1]] != -1:
                    continue
                queue.append(new_pos)
                step_to_pos[new_pos[0]][new_pos[1]] = curr_step + 1
        
        max_step = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_step = max(max_step, step_to_pos[i][j])
            
        return max_step if max_step != 0 else -1

    def in_bound(self, grid, pos):
        return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])
```