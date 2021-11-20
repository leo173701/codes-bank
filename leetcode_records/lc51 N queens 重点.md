51. N-Queens

![image-20211120100714015](C:/Users/leo17/AppData/Roaming/Typora/typora-user-images/image-20211120100714015.png)

### 算法思路

- 因为每个皇后都必须分别占据一行，我们需要做的不过是棋盘上的每个皇后分配一列。

- 下面我们用4皇后的求解过程来讲解算法思路：

    > 从空棋盘开始，然后把皇后1 放到它所在行的第-一个可能位置上，也就是第一-行第一列。对于皇后2，在经过第-列和第二列的失败尝试之后，我们把它放在第一个可能的位置，就是格子(2, 3)，位于第二行第三列的格子。这被证明是一个死胡同，因为皇后3将没有位置可放。所以，该算法进行回溯，把皇后2放在下一个可能位置(2,4)上。这样皇后3就可以放在(3, 2),这被证明是另一个死胡同。该算法然后就回溯到底，把皇后1移到(1,2)。 接着皇后2到(2,4)， 皇后3到(3,1)， 而皇后4到(4, 3)， 这就是该问题的一个解。

![图片](https://media-test.jiuzhang.com/media/markdown/images/6/3/fd4564e8-a551-11ea-864b-0242c0a8b005.jpg)

### 代码思路

- 按行摆放，在确定一个皇后应该摆的列时，需要检查当前列是否合法，如果合法，则将皇后放置在当前位置，并进行递归，回溯。每行都摆满皇后时，则产生了一种解法，将所有解法收集并返回。
- 合法性判断方法：当前将要摆放皇后的位置和其他已摆放皇后的位置不能在同一列，且不能在同一条斜线上。这里判断是否在同一条斜线上可以通过两个皇后的位置横坐标之差和纵坐标之差的绝对值是否相等来判断。

```python
 This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding
class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        #result用于存储答案
        results = []
        self.search(n, [], results)
        return results
    
    #search函数为搜索函数，n表示已经放置了n个皇后，col表示每个皇后所在的列
    def search(self, n, col, results):
        row = len(col)
        #若已经放置了n个皇后表示出现了一种解法，绘制后加入答案result
        if row == n:
            results.append(self.Draw(col))#col 表示单独这一列
            return
        #枚举当前皇后放置的列，若不合法则跳过
        for now_col in range(n):
            if not self.isValid(col, row, now_col):
                continue
            #若合法则递归枚举下一行的皇后
            col.append(now_col)
            self.search(n, col, results)
            col.pop()
    #isValid函数为合法性判断函数
    def isValid(self, cols, row, now_col):
        for r, c in enumerate(cols):
            #若有其他皇后在同一列或同一斜线上则不合法
            if c == now_col:
                return False
            if abs( r - row ) == abs( c - now_col ):
                return False
        return True
    #Draw函数为将col数组转换为答案的绘制函数
    def Draw(self, cols):
        n = len(cols)
        board = []
        for i in range(n):
            row = ['Q' if j == cols[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board
```







实际上是一个全排列问题，比如给定 n = 4 实际上需要返回 [0,1,2,3](https://www.jiuzhang.com/problem/n-queens/) 的所有排列组合， 然后边生成边检查是否和之前已经有过的皇后位置冲突（剪枝），而不是生成所有结果之后再一起查 检查的方法就是看新数字的行列和已有的数字的行列的绝对值是否相等，如果是则冲突，返回False

得到所有结果后用写一个函数把数字字符串转化成图



```python
class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        li = [str(i) for i in range(n)]
        result = []
        self.dfs(result, "", li)   # path 是字符串
        print(result)
        return self.constructGraph(result)
        
    def dfs(self, result, path, nums):
        if not nums:
            result.append(path)
            return
        for i in range(len(nums)):
            if not self.checkValid(path, nums[i]): 
                continue
            self.dfs(result, path+nums[i], nums[:i]+nums[i+1:])
    
    def checkValid(self, path, num):
        if num in path: 
            return False
        for i in range(len(path)):
            if abs(int(num) - int(path[i])) == abs(len(path)-i):
                return False
        return True
    
    def constructGraph(self, result):
        matrix = []
        for path in result:
            row = []
            for c in path:
                queenStr = ['.' for i in range(len(path))]
                queenStr[int(c)] = 'Q'
                row.append(''.join(queenStr))
            matrix.append(row[:])
        return matrix
```

