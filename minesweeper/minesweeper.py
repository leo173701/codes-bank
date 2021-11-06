DIR = ((-1,-1), (-1, 0),(-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # DIR = ((-1,-1), (-1, 0),(-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        x0, y0 = click[0], click[1]
        board = board.copy()
        
        if board[x0][y0] == 'M':
            board[x0][y0] = 'X'
            return board
        
        cnt = self.cnt(board, x0, y0)
        if cnt != 0:
            board[x0][y0] = str(cnt)
            return board
        
        board[x0][y0] = 'B'
        m, n = len(board), len(board[0])
        q = deque([(click[0], click[1])])
        while q:
            x, y = q.popleft()
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx <= m - 1 and 0 <= ny <= n - 1 and board[nx][ny] == 'E':
                    cnt = self.cnt(board, nx, ny)
                    if cnt != 0:
                        board[nx][ny] = str(cnt)
                    else:
                        board[nx][ny] = 'B'
                        q.append((nx, ny))
        return board
                        
    def cnt(self, board, x, y):
        m, n = len(board), len(board[0])
        res = 0
        for dx, dy in DIR:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= m - 1 and 0 <= ny <= n - 1 and board[nx][ny] == 'M':
                res += 1
        return res