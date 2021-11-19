class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        
        for i in range(3):
            for j in range(3):
                used = set()
                for x in range(3*i,3*i+3):
                    for y in range(3*j,3*j+3):
                        if not self.isValidPoint(board, used, board[x][y]):
                            return False
        # 先枚举行，检查每行是否合法
        for x in range(9):
            used = set()
            for y in range(9):
                if not self.isValidPoint(board, used, board[x][y]):
                    return False
        for y in range(9):
            used = set()
            for x in range(9):
                if not self.isValidPoint(board, used, board[x][y]):
                    return False
        return True
            
    def isValidPoint(self,board, used,c):
        if c==".":
            return True
        elif c  in used:
            return False
        used.add(c)
        return True