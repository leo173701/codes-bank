class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0
        
        height = [[float('inf') for _ in range(n)] for k in range(n)]
        height[0][0]=grid[0][0]
        pq = [(grid[0][0],0,0)]
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        while pq:

            cur, curx, cury = heapq.heappop(pq)
            if curx==n-1 and cury==n-1:
                return cur
            for dx,dy in directions:
                newx,newy = dx+curx, dy+cury
                if newx<0 or newx>=n or newy<0 or newy>=n:
                    continue                        
                new_height = max(grid[newx][newy], cur)
                if height[newx][newy]>new_height:
                    height[newx][newy]=new_height
                    heapq.heappush(pq,(height[newx][newy], newx, newy)) 
            # print("  pq=",pq)
            # print("     height=")
            # for i in height:
            #     print("        ",i)
        return -1
                