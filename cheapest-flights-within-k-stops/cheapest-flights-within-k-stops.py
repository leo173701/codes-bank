class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for flight in flights:
            graph[flight[0]].append(flight[1:])
        distance = [sys.maxsize] * n
        distance[src] = 0
        queue = collections.deque([(src, 0)]) # 
        while queue:
            tmp_dst = list(distance) # nextlevel
            size = len(queue)
            for _ in range(size):
                u, steps = queue.popleft()
                if steps > K:
                    continue
                for v, cost in graph[u]:
                    if cost + distance[u] < tmp_dst[v]:
                        tmp_dst[v] = distance[u] + cost
                        queue.append((v, steps + 1))
            distance = tmp_dst
        if distance[dst] != sys.maxsize:
            return distance[dst]
        else:
            return -1