\787. Cheapest Flights Within K Stops



A good case to practice Dijkstra.



To implement Dijkstra, we need a priority queue to pop out the lowest weight node for next search. In this case, the weight would be the accumulated flight cost. So my node takes a form of `(cost, src, k)`. `cost` is the accumulated cost, `src` is the current node's location, `k` is stop times we left as we only have at most K stops. I also convert `edges` to an adjacent list based graph `g`.



Use a `vis` array to maintain visited nodes to avoid loop. `vis[x]` record the remaining steps to reach x with the lowest cost. If `vis[x] >= k`, then no need to visit that case `(start from x with k steps left)` as a better solution has been visited before (more remaining step and lower cost as heappopped beforehand). And we should initialize `vis[x]` to `0` to ensure visit always stop at a negative `k`.



Once `k` is used up (`k == 0`) or `vis[x] >= k`, we no longer push that node `x` to our queue. Once a popped cost is our destination, we get our lowest valid cost.



For Dijkstra, there is not need to maintain a `best cost` for each node since it's kind of greedy search. It always chooses the lowest cost node for next search. So the previous searched node always has a lower cost and has no chance to be updated. The first time we pop our destination from our queue, we have found the lowest cost to our destination.

Dijkstra：  /PriorityQueue 做法

```python
def findCheapestPrice(n, flights, src, dst, K):
	graph = collections.defaultdict(dict)
	for s, d, w in flights:       #建立图
		graph[s][d] = w
	pq = [(0, src, K+1)]
	vis = [0] * n
	while pq:
		w, x, k = heapq.heappop(pq)
		if x == dst:              # 到达终点了
			return w
		if vis[x] >= k:           # 
			continue
		vis[x] = k                # 
		for y, dw in graph[x].items():          # 从x出发可以到达的所有点， 都加入到heap当中
			heapq.heappush(pq, (w+dw, y, k-1))  # 输入
	return -1
```

```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        visited = {}
        graph = collections.defaultdict(list)
        for s, d, p in flights:
            graph[s].append((d, p))
        heap = [(0, 0, src)]
        while heap:
            dist, moves, node = heapq.heappop(heap)
            if node == dst and k >= moves - 1:
                return dist
            if node not in visited or visited[node] > moves:
                visited[node] = moves        # 表示到达 这个node的时候，走了几步
                for nei, weight in graph[node]:
                    heapq.heappush(heap, (dist + weight, moves + 1, nei))
        return -1
```







[重点参考一个leetcode 解法这里](https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/317262/2-Clean-Python-Solution-(BFS-Dijkstra-Explained))

普通BFS 做法：This is mostly straight forward BFS.
When we are out of stops, or price is greater than min_price, we stop adding cities to the queue.
Every time we encounter `dst`we compare the price and set it to the min.

Making the graph takes O(E)
BFS every node in adjacent list takes O(V+E)
V is the number of cities within range K stops.

```python
class Solution1(object):
	def findCheapestPrice(self, n, flights, src, dst, K):
		graph = collections.defaultdict(list)
		q = collections.deque()
        q.append((src, 0, 0))
		min_price = float('inf')  # 初始化，把目标值无限大          

		for u, v, w in flights: 
            graph[u].append((w, v))
		while q:
			city, stops, price = q.popleft()
			if city==dst:
				min_price = min(min_price, price)
				continue

			if stops<=K and price<=min_price:
				for price_to_nei, nei in graph[city]:
					q.append((nei, stops+1, price+price_to_nei))

		return min_price if min_price!=float('inf') else -1
```





```java
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        Map<Integer, Map<Integer, Integer>> prices = new HashMap<>();
        for (int[] f : flights) {
            if (!prices.containsKey(f[0])) prices.put(f[0], new HashMap<>());
            prices.get(f[0]).put(f[1], f[2]);
        }
        Queue<int[]> pq = new PriorityQueue<>((a, b) -> (Integer.compare(a[0], b[0])));
        pq.add(new int[] {0, src, k + 1});
        while (!pq.isEmpty()) {
            int[] top = pq.remove();
            int price = top[0];
            int city = top[1];
            int stops = top[2];
            if (city == dst) return price;
            if (stops > 0) {
                Map<Integer, Integer> adj = prices.getOrDefault(city, new HashMap<>());
                for (int a : adj.keySet()) {
                    pq.add(new int[] {price + adj.get(a), a, stops - 1});
                }
            }
        }
        return -1;
    }
```



```python
    def findCheapestPrice(self, n, flights, src, dst, k):
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1
```

加入visited{} 来进行减枝   加速

```PYTHON
def findCheapestPrice(self, n, flights, src, dst, K):
        visited = {}
        graph = collections.defaultdict(list)
        for s, d, p in flights:
            graph[s].append((d, p))
        heap = [(0, 0, src)]
        while heap:
            dist, moves, node = heapq.heappop(heap)
            if node == dst and K >= moves - 1:
                return dist
            if node not in visited or visited[node] > moves:
                visited[node] = moves
                for nei, weight in graph[node]:
                    heapq.heappush(heap, (dist + weight, moves + 1, nei))
        return -1
```

