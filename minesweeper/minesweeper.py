class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]]=="M":
            board[click[0]][click[1]]="X"
            return board
        m = len(board)
        n = len(board[0])
        queue = collections.deque([click])
        directions = [(-1,0),(1,0),(0,1),(0,-1),(-1,1),(1,1),(-1,-1),(1,-1)]  
        # digits = {"B","1","2","3","4","5","6","7","8"}
        def count(curx,cury):
            count_mine = 0
            for dx, dy in directions:
                newx, newy = curx +dx,cury+dy
                if 0<=newx<m and 0<=newy<n:   #判断基本的还在边界范围内
                    if board[newx][newy]=="M":
                        count_mine+=1         # 在四周有多少个mine
            return count_mine
        
        count_mine = count(click[0], click[1])
        if count_mine>0:
            board[click[0]][click[1]]=str(count_mine)
            return board
        else:
            board[click[0]][click[1]]="B"
        while queue:
            curx,cury = queue.popleft()
            for dx, dy in directions:
                newx, newy = curx +dx,cury+dy
                if 0<=newx<m and 0<=newy<n and board[newx][newy]=="E":   #判断基本的还在边界范围内
                    # if board[newx][newy] in digits:
                    #     continue              # 去除重复
                    count_mine = count(newx, newy)
                    if count_mine>0:
                        board[newx][newy]=str(count_mine)
                    else:
                        board[newx][newy]="B"
                        queue.append((newx,newy))
        return board