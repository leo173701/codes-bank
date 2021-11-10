\1514. Path with Maximum Probability

11/9/2021

**Dijkstra:**
好处，通过每次pop出来的已经是最优值，如果到达终点就可以直接收工，不用再算下去了。所以省时间。

1. Initialize all vertices probabilities as `0`, except `start`, which is `1`;

2. Put all currently reachable vertices into a Priority Queue/heap, **priority ordered by the corresponding current probability, REVERSELY;**

3. **Whenever popped out a vertex with currently highest probability,** 

   check if it is the `end` vertex; 

   If yes, we have already found the solution; 

   otherwise, traverse all its neighbors to update neighbors' probabilities if necessary; 

   *Note: when forwarding one step, multiply the corresponding `succProb` value with the probaboility of current vertex.*

4. Repeat 2 & 3 to find the max probability for `end`; 

   If can NOT, return `0.0d`.

```python
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        p, g = [0.0] * n, defaultdict(list)
        for index, (a, b) in enumerate(edges):
            g[a].append((b, index))
            g[b].append((a, index))   #构建图 g
        p[start] = 1.0
        heap = [(-p[start], start)]    
        while heap:
            prob, cur = heapq.heappop(heap)
            if cur == end:
                return -prob
            for neighbor, index in g.get(cur, []):  #利用index 最快程度找到对应的概率值。
                if -prob * succProb[index] > p[neighbor]: #有更大概率，才把它加入queue当中
                    p[neighbor] = -prob * succProb[index]
                    heapq.heappush(heap, (-p[neighbor], neighbor))
        return 0.0
```







我自己写的BFS 算法

```python
# from collections import defaultdict
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        p = [0]*n
        p[start]=1
        probability = {}
        for i in range(len(edges)):
            probability[(edges[i][0],edges[i][1])]=succProb[i]
            probability[(edges[i][1],edges[i][0])]=succProb[i]
        pq = deque([start])
        
        # heapq.heappush(pq, start)
        graph =collections.defaultdict(list)    #构建图
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])

        while pq:
            cur = pq.popleft()
            # cur = heapq.heappop(pq)
            for nextnode in graph[cur]:
                temp = p[cur]*probability[(cur,nextnode)]
                if p[nextnode]<temp:
                    p[nextnode]=temp
                    pq.append(nextnode)
                    # heapq.heappush(pq,nextnode)
        return float(p[end])
```

