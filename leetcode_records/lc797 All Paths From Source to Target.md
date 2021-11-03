



\797. All Paths From Source to Target

求从起起点到终点的所有路径

![img](https://assets.leetcode.com/uploads/2020/09/28/all_2.jpg)

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: `graph[i]` is a list of all nodes you can visit from node ` i` (i.e., there is a directed edge from node i to node `graph [i][j]` ).
```python
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
```



```python
# BFS写法
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:        
        n = len(graph)
        res = []
        queue = deque([(0,[0])])
        while queue:
            cur, path = queue.popleft()
            if cur == n-1:
                res.append(path)
                continue
            if graph[cur]:
                for i in graph[cur]:
                    queue.append((i, path + [i]))
        return res
```



```python
#DFS 写法
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        stack = [(0,[0])]
        while stack:
            cur, path = stack.pop()
            if cur==len(graph)-1:
                res.append(path)
            else:
                for i in graph[cur]:
                    stack.append((i, path+[i]))
        return res
```

