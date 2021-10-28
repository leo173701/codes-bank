

\130. Surrounded Regions



![img](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)



可以使用BFS或DFS解题.

**方法1:**

在记录每个节点是否访问过的前提下, 依次从每个 `'O'` 开始BFS/DFS, 并且只访问未访问过的 `'O'`.

如果从一个 `'O'` 可以访问到边界, 那么不做任何操作; 否则便将这个 `'O'` 可以访问到的所有的 `'O'` 替换为 `'X'`.

------

**方法2:**

从每个边界的 `'O'` 开始遍历, 只访问 `'O'`, 先都暂时设置为 `'T'` 或其他字符.

遍历结束之后, 将剩下的 `'O'` 替换为 `'X'` 然后再将 `'T'` 还原即可.

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        q = deque([])
        
        def fill(i,j):
            if 0<=i<m and 0<=j<n and board[i][j] == 'O':
                board[i][j]='T'
                q.append((i,j))
        def bfs(i,j):
            if board[i][j] == 'O':
                q.append((i,j))
                fill(i,j)
            while q:
                curx,cury = q.popleft()
                fill(curx+1,cury)
                fill(curx-1,cury)
                fill(curx,cury+1)
                fill(curx,cury-1)
            
    
        for i in range(m):
            bfs(i,0)
            bfs(i,n-1)
        
        for j in range(n):
            bfs(0,j)
            bfs(m-1,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'        
```

