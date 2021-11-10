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