class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[['.' for i in range(n)] for i in range(n)]
        col=[True]*n
        diag1=[True]*(2*n-1)    #左下到右上的许多对角线，从左上到右下从0开始编号
        diag2=[True]*(2*n-1)    #左上到右下的许多对角线，从左下到右上从0开始编号


        def updateBoard(x,y,n,flag):
            col[x]=flag
            diag1[x+y]=flag
            diag2[x-y+n-1]=flag
            board[y][x]='Q' if not flag else '.'
        def available(x,y):
            return col[x] and diag1[x+y] and diag2[x-y+n-1]
        def nqueens(y,n):
            if y>=n:
                temp=[]
                for i in range(n):
                    temp.append(''.join(board[i]))
                res.append(temp)
                return
            for x in range(n):  #同一排挨个试
                if not available(x,y):
                    continue
                updateBoard(x,y,n,False)    #直到出现一个可以填Q的
                nqueens(y+1,n)              #进行下一行的选取
                updateBoard(x,y,n,True)     #再调整回来
        nqueens(0,n)
        return res