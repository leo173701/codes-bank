class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        visited = {}
        # dic = {}
        graph = collections.defaultdict(list)
        for s, d, p in flights:
            graph[s].append((d, p))
        # for start, end, price in flights:
        #     if start not in dic:
        #         dic[start] = [(end,price)]
        #     else:
        #         dic[start].append((end,price))
        heap = [(0,0,src)]
        while heap:
            # n = len(heap)
            totalprice, moves, node = heapq.heappop(heap)
            if node ==dst and k>=moves-1:
                return totalprice
            if node not in visited or visited[node]>moves:
                visited[node]=moves
                for nextnode, price in graph[node]:
                    heapq.heappush(heap,(totalprice + price, moves+1, nextnode))
        return -1