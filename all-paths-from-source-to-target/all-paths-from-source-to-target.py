class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        # visited = {}
        res = []
        queue = deque([(0,[0])])
        while queue:
            cur, path = queue.popleft()
            if cur == n-1:
                res.append(path)
                continue
            if graph[cur]:
                # print(graph[cur])
                for i in graph[cur]:
                    queue.append((i, path + [i]))
        return res