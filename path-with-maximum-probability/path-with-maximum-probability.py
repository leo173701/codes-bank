from collections import defaultdict
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        p = [0 for _ in range(n)]
        p[start]=1
        probability = {}
        for i in range(len(edges)):
            probability[(edges[i][0],edges[i][1])]=succProb[i]
            probability[(edges[i][1],edges[i][0])]=succProb[i]
        pq = ([])
        heapq.heappush(pq, start)
        # visited ={start}
        graph =collections.defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        # print(graph)
        # print(probability)
        while pq:
            cur = heapq.heappop(pq)
            for nextnode in graph[cur]:
                temp = p[cur]*probability[(cur,nextnode)]
                if p[nextnode]<temp:
                    p[nextnode]=temp
                    heapq.heappush(pq,nextnode)
        return float(p[end])