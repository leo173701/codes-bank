class Solution:
    def totalNQueens(self, n: int) -> int:
        if n==1:
            return 1
        if n==2 or n==3:
            return 0
        if n==4:
            return 2
        board = [["." for i in range(n) ] for j in range(n)]
        col = [True]*n
        dia1 = [True]*(2*n-1)
        dia2 = [True]*(2*n-1)
        
        def update(x,y,flag):
            col[x]=flag
            dia1[x+y]=flag
            dia2[x-y+n-1]=flag
            if not flag:
                board[x][y]='Q'
            else:
                board[x][y]='.'
        def available(x,y):
            return col[x] and dia1[x+y] and dia2[x-y+n-1]
        def dfs(y):
            if y>=n:
                temp = []
                for i in range(n):
                    temp.append("".join(board[i]))
                res.append(res)
                return
            for x in range(n):
                if not available(x,y):
                    continue
                update(x,y,False)
                dfs(y+1)
                update(x,y,True)
        res = []
        dfs(0)
        return len(res)