class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
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
            step += 1
            queue_size = len(q)
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