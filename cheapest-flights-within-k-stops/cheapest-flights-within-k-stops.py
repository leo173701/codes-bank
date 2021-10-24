class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for a, b, c in flights:
            graph[a].append((b, c))

        queue = deque([(src, 0, 0)])
        res = [float('inf')] * n
        res[src] = 0
        while queue:
            curr, cost, cnt = queue.popleft()
            if cnt>=k+1:
                break
            for temp, c in graph[curr]:
                if res[temp]>cost+c:
                    res[temp] = cost+c 
                    queue.append((temp, cost+c, cnt+1)) 
        return res[dst] if res[dst]!=float('inf') else -1