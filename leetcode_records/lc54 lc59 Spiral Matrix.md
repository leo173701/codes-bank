\54. Spiral Matrix

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])        
        left = 0
        up = 0
        right = n-1
        down =  m-1
        count = 1
        res = []
        direction = 0
        while True:
            if direction ==0:
                for i in range(left, right+1):
                    res.append(matrix[up][i])
                up+=1
            if direction ==1:
                for i in range(up, down+1):
                    res.append(matrix[i][right])                   
                right-=1
            if direction ==2:
                for i in range(right,left-1,-1):
                    res.append(matrix[down][i])
                down -=1
            if direction ==3:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left+=1
            if up > down or left > right: 
                return res
            direction = (direction+1)%4            
        return res
```









\59. Spiral Matrix II

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        if n==2:
            return [[1,2],[4,3]]
        if n==3:
            return [[1,2,3],[8,9,4],[7,6,5]]
        res = [[0]*n for _ in range(n)]
        cur = 1
        left, right, up, down = 0,n-1,0,n-1
        while cur <=n*n:
            for i in range(left,right+1):
                res[up][i]=cur
                cur+=1
            up+=1           
            for i in range(up,down+1):
                res[i][right]=cur
                cur+=1
            right-=1    
            for i in range(right, left-1, -1):
                res[down][i]=cur
                cur+=1
            down -=1            
            for i in range(down, up-1,-1):
                res[i][left]=cur
                cur+=1
            left+=1     
        return res
```

