class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        n = len(grid[0])
        direction = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        step = 1
        queue = deque([(0,0)])
        grid[0][0]=1
        while queue:
            
            for _ in range(len(queue)):
                curx, cury = queue.popleft()
                if curx==n-1 and cury==n-1:
                    return step
                for dx,dy in direction:
                    newx, newy = dx+curx, dy+cury
                    if 0<=newx<n and 0<=newy<n and grid[newx][newy]==0:
                        # if newx==n-1 and newy ==n-1:
                        #     return step+1
                        queue.append((newx,newy)) 
                        grid[newx][newy]=1
            step +=1
        return -1
        
        # n = len(grid)
        # if grid[0][0] or grid[n-1][n-1]:
        #     return -1
        # q = [(0, 0, 1)]
        # grid[0][0] = 1
        # for i, j, d in q:
        #     if i == n-1 and j == n-1: return d
        #     for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
        #         if 0 <= x < n and 0 <= y < n and not grid[x][y]:
        #             grid[x][y] = 1
        #             q.append((x, y, d+1))
        # return -1