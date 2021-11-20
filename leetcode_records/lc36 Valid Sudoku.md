\36. Valid Sudoku

判断数独是否合法，return True /False

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

```python
class Solution:
    """
    @param board: the board
    @return: whether the Sudoku is valid
    """
    def isValidSudoku(self, board):        
        # 先枚举行，检查每行是否合法
        for row in range(9):
            used = set()
            for col in range(9):
                if not self.check_valid(board[row][col], used):
                    return False
        
        # 先枚举列，检查每列是否合法
        for col in range(9):
            used = set()
            for row in range(9):
                if not self.check_valid(board[row][col], used):
                    return False
        
        # 每个分块的左上角的坐标为(i * 3, j * 3)
        for i in range(3):
            for j in range(3):
                used = set()
                for row in range(i * 3, i * 3 + 3):
                    for col in range(j * 3, j * 3 + 3):
                        if not self.check_valid(board[row][col], used):
                            return False     
        return True
    
    # 检查字符是否有冲突
    def check_valid(self, c, used):
        if c == '.':
            return True
        if c in used:
            return False
        used.add(c)
        return True
```

