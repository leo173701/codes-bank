class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j):
            # if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j]=-1
            res = 4+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
            if i > 0 and grid[i - 1][j] != 0:
                res -=2
            if j >0 and grid[i][j-1]!=0:
                res -=2
            return res
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return dfs(i,j)
            