# \529. Minesweeper

## BFS 模板题





![img](https://assets.leetcode.com/uploads/2018/10/12/minesweeper_example_1.png)

### 题目总结：

1. 给一个初始位置 click， 返回最终的状态board
2. 如果某一个点周围的地雷数量>0，那就更新这个点的值为地雷的数量； 同时 不再从这个点往周围扩散
3. 如果某一个点周围的地雷数量=0，那这个点就更新为“B”， 同时继续从这个点往周围扩散

### 思路要点：

1. BFS

2. 需要做两件事情：

   1. 统计当前这个点周围地雷的数量，
   2. 如果周围地雷的数量为0，那就继续BFS 做法： 把这个点周围的点（在边界范围内的，not visited yet）, 加入到queue当中

3. 使用visited =set()进行去重，加速算法

```python
#BFS 写法1
# 统计当前坐标周围有多少地雷
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]]=="M":
            board[click[0]][click[1]]="X"
            return board
        m = len(board)
        n = len(board[0])
        queue = collections.deque([click])
        directions = [(-1,0),(1,0),(0,1),(0,-1),(-1,1),(1,1),(-1,-1),(1,-1)]  
        
        def count(curx,cury):
            count_mine = 0
            for dx, dy in directions:
                newx, newy = curx +dx,cury+dy
                if 0<=newx<m and 0<=newy<n:   #判断基本的还在边界范围内
                    if board[newx][newy]=="M":
                        count_mine+=1         # 在四周有多少个mine
            return count_mine
        
        visited = set(click)                  # 用于判重， set() 只能搭配tuple (x,y)
        while queue:
            curx,cury = queue.popleft()
            count_mine = count(curx,cury )    # 计算当前坐标周围有多少个地雷
            if count_mine>0:
                board[curx][cury]=str(count_mine) #更新当前位置的数值
            else:
                board[curx][cury]="B" # 在当前坐标附近地雷总量为0的时候，才会把周围的点加入queue
         #开始BFS做法了：
                for dx, dy in directions:
                    newx, newy = curx+dx,cury+dy 
                    if 0<=newx<m and 0<=newy<n and (newx,newy) not in visited:#判断基本的还在边界范围内
                        queue.append((newx,newy))    #单纯地做一下遍历即可
                        visited.add((newx,newy))     #加入到visited 当中
        return board
```





```python
#BFS 写法2：
      # 计算下一步坐标周围有多少个地雷，
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
            # 不研究当前点的情况，直接进入BFS，开始研究下一个结点的情况
            for dx, dy in directions:
                newx, newy = curx +dx,cury+dy
                if 0<=newx<m and 0<=newy<n and board[newx][newy]=="E":#判断基本的还在边界范围内
                    # if board[newx][newy] in digits:
                    #     continue                       # 去除重复
                    count_mine = count(newx, newy)# 计算下一步坐标周围有多少个地雷
                    if count_mine>0:
                        board[newx][newy]=str(count_mine)#更新下一个坐标的坐标值
                    else:          #周围没有地雷，才会把下一个点加入到queue当中
                        board[newx][newy]="B"
                        queue.append((newx,newy))
        return board
```

