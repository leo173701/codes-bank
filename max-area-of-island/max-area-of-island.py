class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: 
            return 0
        row = len(grid)
        col = len(grid[0])  
        res = 0

        def BFS(grid, i, j, row, col):
            curCount = 1
            q = [(i,j)]
            while q:
                cur = q.pop(0)
                for (x,y) in [(cur[0]+1,cur[1]),(cur[0]-1,cur[1]),(cur[0],cur[1]+1),(cur[0],cur[1]-1)]:
                    if 0<=x<row and 0<=y<col and grid[x][y]==1:
                        q.append((x,y))
                        curCount +=1
                        grid[x][y]=0
            return curCount
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    grid[i][j]=0
                    res = max(res,BFS(grid,i,j,row,col))
        return res